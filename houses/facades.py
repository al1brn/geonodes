#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 07:16:49 2023

@author: alain
"""
from pathlib import Path
import numpy as np

from importlib import reload
from geopy.houses import constants
reload(constants)

from geopy.core.timer import Timer
from geopy.core.meshbuilder import MeshBuilder, Meshes
from geopy.houses.constants import *
from geopy.houses.asset import Assets
from geopy.houses.house_builder import HouseBuilder

# ====================================================================================================
# Based on a file of facades locations
# - Build simple faces as facades
# - Build detailed facades

class Facades:
    def __init__(self, folder, rama, house_assets="house_assets.npz", use_cache=True):
        
        self.folder    = Path(folder)
        self.rama      = rama
        self.prefix = "Rama " if self.rama else ""
        
        # ----- Facades actual locations
        
        arrays = np.load(self.folder / f"{self.prefix}Facades - Locations.npz")
        
        self.locs     = arrays['locs']
        self.options  = arrays['options']
        
        
        if False: # ROTATION WAS NOT BAKED
            print("FACADES HACK")
            from geopy.core.transformations import Eulers
            locs = self.locs[:, 0]
            ag = np.arctan2(locs[:, 2], locs[:, 1])
            eulers = Eulers(shape=len(locs[:, 1]))
            eulers.x = ag

            print(f"DEBUG {np.shape(locs)=}, {np.shape(locs[:, 1])=}, {np.shape(ag)=}, {eulers.shape=}")



            locs[:, 1] = eulers @ locs[:, 1]

        
        
        
        self.visibles = np.zeros(len(self), np.byte)
        
        # ----- Facades flat locations

        arrays = np.load(self.folder / f"Facades - Locations.npz")
        
        self.flat_locs = np.array(arrays['locs'])
        del arrays
        
        # ----- Assets
        
        self.assets = Assets.Load(self.folder / house_assets)
        
        # ----- cache
        
        if use_cache:
            self.cache    = Meshes()
            self.in_cache = -np.ones(len(self.locs), int)
        else:
            self.cache    = None
        
        
        
    def __str__(self):
        return f"<Facades: {len(self.locs)} locations>"

        
    def __len__(self):
        return len(self.locs)

    # ====================================================================================================
    # To rama
    
    @staticmethod
    def to_rama(verts):
        
        RAMA_X = 28672
        RAMA_Y = 49152  # Circumference
        RAMA_RADIUS = RAMA_Y / 2 / np.pi

        thetas = verts[:, 1]/RAMA_RADIUS
        r      = RAMA_RADIUS - verts[:, 2]
        
        res = np.array(verts)

        res[:, 1] =  r*np.sin(thetas)
        res[:, 2] = -r*np.cos(thetas)
        
        return res
    
    # ====================================================================================================
    # Visibility
    
    def reset_visibles(self):
        self.visibles[:] = 0
        
    def set_visibles(self, camera):

        vis, dists = camera.visible_verts(self.locs[:, 0], close_distance=200, normals=self.locs[:, 1])
        
        self.visibles[vis] |= 0x01
        self.visibles[dists < 2000] |= 0x02
        
    # ====================================================================================================
    # Facades indices of a house
    
    def facades_indices(self, house_index):
        return np.argwhere(self.options[:, 1] == house_index).flatten()
        
    # ====================================================================================================
    # Simple face
    
    def low_detail(self, index):

        loc     = self.locs[index]
        options = self.options[index]
        
        location = loc[0]
        length   = loc[2, 0]
        angle    = loc[2, 1]
        height   = loc[2, 2]
        
        mb = MeshBuilder(materials=MATERIALS)
        mb.new_face_attribute("house_seed", 'FLOAT')
        mb.new_face_attribute("face_seed",  'FLOAT')
        
        dz = -2 if options[0] & WALL_FLOOR0 else 0
        
        uvs   = np.array(( (0, dz), (length, dz), (length, height), (0, height)) )
        verts = np.array(( (0, 0, dz), (length, 0, dz), (length, 0, height), (0, 0, height)) )
        
        M = np.array(( (np.cos(angle), np.sin(angle), 0), (-np.sin(angle), np.cos(angle), 0), (0, 0, 1) ))
        mb.add_surface(
            verts      = location + np.einsum('...ij, ...i', M, verts),
            mat        = WALL,
            UVMap      = uvs,
            house_seed = loc[3, 0],
            face_seed  = loc[3, 1],
            )
        return mb
    
    # ====================================================================================================
    # Facade
    
    def facade(self, index):
        
        # ----- Cache
        
        if self.cache is not None:
            cache_index = self.in_cache[index]
            if cache_index >= 0:
                return self.cache[cache_index]

        # ----- Build
        
        loc     = self.flat_locs[index]
        options = self.options[index]
        
        location = loc[0]
        length   = loc[2, 0]
        angle    = loc[2, 1]
        height   = loc[2, 2]
        
        hs = int(loc[3, 2])
        storey_height  = (hs % 10000)/100
        storey0_height = (hs//100000)/100
        
        # DEBUG
        storey_height  = 3.
        storey0_height = 3.5
        
        # ----- Options

        floor0  = bool(options[0] & WALL_FLOOR0)
        door    = bool(options[0] & WALL_DOOR)
        terrace = bool(options[0] & WALL_TERRACE)
        shop    = bool(options[0] & WALL_SHOP)
        garage  = bool(options[0] & WALL_GARAGE)

        # ----- Randomness
        
        house_rng = np.random.default_rng(int(loc[3, 0]*(1<<63)))
        face_rng  = np.random.default_rng(int(loc[3, 1]*(1<<63)))
        # ----- house builder
        
        hbuild = HouseBuilder(self.assets, rng=house_rng)

        # ----- Storey 0
        
        pat0 = None
        if floor0:
            pat0 = hbuild.random_pattern(7, face_rng, door=door, bay=True, garage=garage, shop=shop)
        elif terrace:
            pat0 = hbuild.random_pattern(7, face_rng, door=False, bay=True)

        # ----- Levels and storey patterns
        
        storeys = []
        if pat0 is None:
            levels  = round(height/storey_height)
            if levels == 0:
                storey_height = height
                levels = 1
            else:
                storey_height = height/levels
                
        else:
            levels = 1 + round((height - storey0_height)/storey_height)
            if levels == 1:
                storey0_height = height
            else:
                storey_height = (height - storey0_height)/(levels - 1)
            storeys = [{'count': 1, 'height': storey0_height, 'pattern': pat0}]
                
        if levels > len(storeys):
            storeys.append({'count': levels - len(storeys), 'height': storey_height, 'pattern': hbuild.random_pattern(5, face_rng)})

        # ----- Build the facade
            
        facade = hbuild.facade(length, storeys, symmetry=face_rng.uniform(0, 1) > 1.8)

        # ----- Underground

        if floor0:
            facade.add_surface([(0, 0, -2), (0, length, -2), (0, length, 0), (0, 0, 0)], mat=facade.material("Underground"))

        # ----- Rotation
        
        angle = angle - np.pi/2
        M = np.array(( (np.cos(angle), np.sin(angle), 0), (-np.sin(angle), np.cos(angle), 0), (0, 0, 1) ))
        facade._verts = location + np.einsum('...ij, ...i', M, facade.verts)
        
        facade.new_face_attribute("house_seed", 'FLOAT', value=loc[3, 0])
        facade.new_face_attribute("face_seed",  'FLOAT', value=loc[3, 1])

        if self.rama:
            facade._verts = Facades.to_rama(facade._verts)

        # ----- In cache
        
        if self.cache is not None:
            self.in_cache[index] = len(self.cache)
            self.cache.append(facade)

        return facade
    
    # ====================================================================================================
    # To object
    
    def to_object(self, spec):
        
        # ----- Far facades
        
        nfaces = len(self.locs)
        
        faces = Meshes.Load(self.folder / f"{self.prefix}Facades - Low Detail.npz")
        assert(len(faces.verts) == nfaces*4)
        
        sel = self.visibles == 1
        nsel = np.sum(sel)
        
        verts = np.reshape(faces.verts, (nfaces, 4, 3))[sel]
        assert(len(verts)==nsel)
        
        mb = MeshBuilder(uvmap=False, materials=MATERIALS)
        mb._verts   = np.reshape(verts, (nsel*4, 3))
        mb._corners = np.arange(nsel*4)
        mb._faces   = np.array([[4, 0]]*nsel)
        
        faces_uvs = faces.attributes['UVMap'].a
        uvs = np.reshape(faces_uvs, (nfaces, 4, 2))[sel]
        
        mb.uvmap("UVMap", np.reshape(uvs, (nsel*4, 2)))
        
        mb.new_face_attribute("house_seed", 'FLOAT', self.locs[sel, 3, 0])
        mb.new_face_attribute("face_seed",  'FLOAT', self.locs[sel, 3, 1])
        mb.new_face_attribute("far",  'BOOLEAN', value=True)
        
        # ----- Close facades
        
        sel = self.visibles == 3
        nsel = np.sum(sel)
        
        meshes = Meshes()
        meshes.new_face_attribute("house_seed", 'FLOAT')
        meshes.new_face_attribute("face_seed",  'FLOAT')
        meshes.new_face_attribute("far",        'BOOLEAN')
        
        timer = Timer("Close facades", nsel, delta=30)
        for i, index in enumerate(np.arange(len(self.locs))[sel]):
            timer.track(i)
            meshes.append(self.facade(index))
        timer.done()
        
        meshes.append(mb)
        
        return meshes.to_object(spec)
    
# ====================================================================================================
# Based on files for roof locations and meshes

class Roofs:
    def __init__(self, folder, file_name="Roofs"):
        
        self.folder = Path(folder)
        self.file_name = file_name
        
        self.locs = np.load(self.folder / f"{self.file_name} - Locations.npy")
        self.visibles = np.zeros(len(self), bool)
        
    def __str__(self):
        return f"<Roofs: {len(self.locs)} locations>"
        
    def __len__(self):
        return len(self.locs)
    
    # ====================================================================================================
    # Visibility
    
    def reset_visibles(self):
        self.visibles[:] = 0
        
    def set_visibles(self, camera):
        
        vis, dists = camera.visible_verts(self.locs, close_distance=200)
        
        self.visibles[vis] = True
        
    # ====================================================================================================
    # To object
    
    def to_object(self, spec):
        
        # ----- Roof meshes
        
        roofs = Meshes.Load(self.folder / f"{self.file_name} - Meshes.npz")
        assert(len(roofs) == len(self))
        
        if self.visibles is None:
            meshes = roofs
        else:
            meshes = roofs[self.visibles]
            
        meshes.to_object(spec)
    
        
        

