#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:31:57 2023

@author: alain
"""

from pathlib import Path

import numpy as np

import bpy
from geopy.core import blender
from geopy.core.camera import Camera
from geopy.core.meshbuilder import MeshBuilder, Meshes
from geopy.gis.tiles import Tiles
from geopy.gis.sat_tiles import SatTiles


RAMA_X = 28672
RAMA_Y = 49152  # Circumference
RAMA_RADIUS = RAMA_Y / 2 / np.pi

NORTH_CENTER = (528683.0, 6961315.0)
NORTH_ANGLE  = -248.8

SOUTH_CENTER = (1028389.0, 6293931)
SOUTH_ANGLE  = 130.6

NORTH_X_LOC = -35000
SOUTH_X_LOC = 2500


# ====================================================================================================
# Manages tiles of different resolutions on a map

class MapTiler:
    def __init__(self, shape=(10, 10), tile_size=256., max_subdiv=8, uv_scale=1., get_verts=None, default_mat="Material", mat_size=1, detail_mats=None):
        """ Cut a big surface in tiles.
        
        - uv_scale: 1. --> one uv unit square per tile. To get the uv unit square as a 1 meter square
          use uv_scale = 1 << max_subdiv (256 by default)
        """
        
        self.tile_size   = tile_size
        self.ij_tile_size = 1 << max_subdiv
        i, j = np.meshgrid(
            np.arange(0, (shape[0]+1)*self.ij_tile_size, self.ij_tile_size),
            np.arange(0, (shape[1]+1)*self.ij_tile_size, self.ij_tile_size),
            indexing='ij')

        self._get_verts  = get_verts
        self.corners     = self.get_verts(np.stack((i, j), axis=-1))

        self.shape       = shape
        self.max_subdiv  = max_subdiv
        self.subdivs     = np.zeros(shape, int)
        self.uv_scale    = uv_scale
        self.default_mat = default_mat
        
        # ----- Materials
        
        self.build_materials(mat_size, detail_mats)         
        
    # ====================================================================================================
    # Str
    
    def __str__(self):
        subdivs = np.bincount(self.subdivs.flatten())
        nverts = 0
        nfaces = 0
        stiles = ""
        for i in range(0, self.max_subdiv+1):
            n = np.sum(self.subdivs == i)
            nvs = n*(((1 << i) + 1)**2)
            nfs = n*((1 << i)**2)
            nverts += nvs
            nfaces += nfs
            stiles += f"\n  {i:2d} ({1 << i:4d}): {n:5d} --> {nvs:7d} vertices, {nfs:7d} faces"
            
        return f"<MapTiler: shape: {np.shape(self.subdivs)}, tile size: {self.tile_size*1.:.0f} m, max: {self.max_subdiv}, vertices: {nverts}, faces: {nfaces}" + stiles + "\n>"
    

    # ====================================================================================================
    # Values from indices
    
    def get_verts(self, ijs):
        if self._get_verts is None:
            verts = np.zeros(np.shape(ijs)[:-1] + (3,), float)
            verts[..., :2] = ijs * (self.tile_size / self.ij_tile_size)
            return verts
        
        else:
            return self._get_verts(ijs)
        
    # ====================================================================================================
    # Resolution
    
    def reset_resolution(self):
        self.subdivs[:] = 0
        
    def camera_adapt(self, max_length=12, close_distance=None, frames=None):
        """ Set subdivision based on distances.
        
        At dist d, one meter is seen as p pixels, a tile of 256 meters is seen as 256p pixels.
        We want a tile segment to be at most s pixels. We need to divide with a factor of
        256p/s.
        
        The subdivision value is log2(256p/s) = 8 - log2(s) + log2(p)
        """
        
        if close_distance is None:
            close_distance = 2*self.tile_size
        
        def setr():
            
            camera = Camera()
            
            # ----- The four corners
            
            for i, sli, slj in zip(
                    range(4), 
                    [slice(-1), slice(-1), slice(1, None), slice(1, None)], 
                    [slice(-1), slice(1, None), slice(1, None), slice(-1)]):
                
                v, d = camera.visible_verts(self.corners[sli, slj], close_distance=close_distance)
                if i == 0:
                    vis, dist = v, d
                else:
                    vis |= v
                    dist = np.minimum(dist, d)

            # ----- Resolution
            # TBD TBD TBD TBD TBD TBD TBD TBD TBD TBD 
            # 8 to adapt to tile_size
            
            sbase = round(np.log(self.tile_size)/np.log(2))
            
            self.subdivs[vis] = np.maximum(self.subdivs[vis], np.clip(np.round(
                sbase - np.log(max_length)/np.log(2) + np.log(camera.meter_in_pixels(dist))/np.log(2)).astype(int)[vis],
                1, self.max_subdiv))

        Camera.frame_range(frames, setr, message="MapTiler resolution")
        
    # ====================================================================================================
    # Materials
    
    # ----------------------------------------------------------------------------------------------------
    # Geometry tiles are grouped in material tiles of size (self.mat_size, self.mat_size)
    # Each material tile has a material index and an uv offset
    #
    # Base material uv offsets is the offset of the tile within the whole geometry
    # Detailed material uv offset is the offset of the geometry tile with is material tile
    
    def build_materials(self, mat_size=None, detail_mats=None):
        
        # ----- Initialization if not already done
        # build_materials with proper values must be called at ainitialization
        
        if mat_size is not None:
            self.mat_size = mat_size # Geometry tile per material tile
            if self.shape[0] % self.mat_size != 0 or self.shape[1] % self.mat_size != 0:
                raise Exception(f"The number of geometry tiles per material tile {self.mat_size} must divide the shape {self.shape}")
            
            if detail_mats is None:
                self.subdiv_detail = None
                
            else:
                # ----- The detail mats contains the subdivisions requiring a more detailed material
                #                0  1  2  3  4  5  6  7  8
                # [3, 5, 7] --> [0, 0, 0, 1, 1, 2, 2, 3, 3]
        
                self.subdiv_detail = [0]
                for i in range(1, self.max_subdiv + 1):
                    if i in detail_mats:
                        self.subdiv_detail.append(self.subdiv_detail[-1] + 1)
                    else:
                        self.subdiv_detail.append(self.subdiv_detail[-1])
        
        # ----- Max subdivision for each material tile
        
        ms = self.mat_size
        a = np.reshape(self.subdivs, (self.shape[0]//ms, ms, self.shape[1]//ms, ms))
        mat_tile_subs = np.max(np.max(a, axis=3), axis=1)
        del a
        
        self.mat_indices = np.zeros_like(self.subdivs)
        
        # ----- uv offsets for each material tile
        # A geometry tile is mapped on a unit uv square
        # By default, offset is mapped relatively to the global map bottom left corner
        
        self.uv_ofs = np.zeros(self.shape + (2,), float)
        self.uv_ofs[..., 0] = np.arange(0, self.shape[0])[:, None]
        self.uv_ofs[..., 1] = np.arange(0, self.shape[1])
        
        # ----- Material tiles are mapped such as to fit the unit square
        
        self.uv_tile_scale = np.ones(self.shape, float)
        
        # ----- No detailed material
        
        self.detailed_materials = [None]
        if self.subdiv_detail is None:
            return
        
        # ----- For each material tile different from 0
        # --> Create a new material
        # --> Change the uv offset relatively to the material tile offset
        
        base_uv_ofs = np.array(self.uv_ofs)
                    
        mat_tile_inds = np.zeros_like(mat_tile_subs)
        
        for i in range(np.shape(mat_tile_subs)[0]):
            for j in range(np.shape(mat_tile_subs)[1]):
                
                sd = mat_tile_subs[i, j]
                if self.subdiv_detail[sd] == 0:
                    continue
                
                # ----- New material
                
                mat_ind = len(self.detailed_materials)
                self.detailed_materials.append((i, j, self.subdiv_detail[sd]))
                
                # ----- Set the material to the geometry tiles
                # and update the uv offsets
                
                it, jt = i*self.mat_size, j*self.mat_size
                uv_ofs = base_uv_ofs[it, jt]
                
                for ii in range(it, it + self.mat_size):
                    for jj in range(jt, jt + self.mat_size):
                        self.mat_indices[ii, jj] = mat_ind
                        self.uv_ofs[ii, jj] -= uv_ofs
                        self.uv_tile_scale[ii, jj] = 1/self.mat_size
                        
    # ----------------------------------------------------------------------------------------------------
    # Create the materials
    
    def get_material(self, index):
        if index == 0:
            name = self.default_mat
            
        else:
            i, j, r = self.detailed_materials[index]
            name = f"Mat [{i:3d}, {j:3d}] {r}"
            
        if bpy.data.materials.get(name) is None:
            bpy.data.materials.new(name)
            
        return name
        
    @property
    def materials(self):
        return [self.get_material(i) for i in range(len(self.detailed_materials))]
   
    # ====================================================================================================
    # To object
    
    # ----- Mesh builder
    
    def to_builder(self, scale=None, material=None):
        
        self.build_materials()
        
        materials = self.materials
        if material is not None:
            materials[0] = material
            
        ij_ofs = np.stack(np.meshgrid(np.arange(self.shape[0]), np.arange(self.shape[1]), indexing='ij'), axis=-1)*self.ij_tile_size
        
        meshes = Meshes(materials=materials, uvmap=True)
        for subdiv in range(0, self.max_subdiv+1):
            
            inds = self.subdivs == subdiv
            count = np.sum(inds)
            if count == 0:
                continue
            
            # ----- Tile grid multiplied count times

            sd = 1 << subdiv
            mb = MeshBuilder.Rectangle(seg_x=sd, seg_y=sd, uv_scale=1, indexing='ij').multiply(count=count)
            
            # ----- Compute the vertices
            
            rg = np.arange(0, self.ij_tile_size + 1, 1 << (self.max_subdiv - subdiv))
            ijs = np.resize(np.stack(np.meshgrid(rg, rg, indexing='ij'), axis=-1), (count, (sd+1)*(sd+1), 2))
            del rg
            
            ijs += ij_ofs[inds][:, None]
            mb._verts[:] = self.get_verts(np.reshape(ijs, (count*(sd+1)*(sd+1), 2)))
            
            # ----- materials
            
            a = np.reshape(mb.faces, (count, 1 << (2*subdiv), 2))
            a[..., 1] = self.mat_indices[inds, None]

            # ----- Offset the uv maps
            
            a = np.reshape(mb.attributes["UVMap"].a, (count, 1 << (2*subdiv + 2), 2))
            a += self.uv_ofs[inds, None]
            a *= self.uv_tile_scale[inds, None, None]
            
            # ----- Append

            meshes.append(mb)
            
        # ----- UV scale
        
        meshes.attributes["UVMap"].a *= self.uv_scale
        
        if scale is not None:
            meshes._verts *= scale
        
        return meshes    
    
    # ----- Object
    
    def to_object(self, obj, threshold=.1, scale=None, material=None):
        
        o = self.to_builder(scale=scale, material=material).to_object(obj)
        
        if threshold is None:
            return o
        else:
            return blender.remove_doubles(o, threshold=threshold)
        
    # ====================================================================================================
    # Demo
    
    @staticmethod
    def Demo(max_subdiv=8):

        from geopy.core.noise import BNoise, SNoise, Noise
        
        node_type = 'SNOISE'
        
        if node_type == 'SNOISE':
            noise = SNoise(scale=.0008, detail=10., dimension=3, size=1000, seed=0)
            fac = 200
        elif node_type == 'BNOISE':
            noise = BNoise(scale=.01, detail=1., dimension=3, seed=0)
            fac = 30
        else:
            noise = Noise(scale=.005, dimension=3, octaves=3, seed=0)
            fac = 50
        
        tile_size = 256
        
        def get_verts(ijs):
            verts = np.zeros(np.shape(ijs)[:-1] + (3,), float)
            verts[..., :2] = ijs*(tile_size / (1 << max_subdiv))
            n = np.size(verts)//3
            #np.reshape(verts[..., 2], n)[:] = noise0(np.reshape(verts, (n, 3)))*100
            
            d = np.linalg.norm(verts, axis=-1)
            
            if True:
                verts[..., 2] = np.sin(d/50)*30
                
            if True:
                np.reshape(verts[..., 2], n)[:] += (noise(np.reshape(verts, (n, 3))) - .5)*fac
            
            return verts
        
        mp = MapTiler(shape=(10, 10), max_subdiv=max_subdiv, get_verts=get_verts)
        
        mp.camera_adapt(max_length=12, close_distance=512, frames=range(1, 250))
        
        mp.to_object("MapTiler Demo", threshold=.1)
        
        print("MapTiler Demo:")
        print(mp)
        print()
        
        return mp
    
# ====================================================================================================
# Altitude map

class Altitudes(MapTiler):
    
    def __init__(self, corner, size, tile_size=256, max_subdiv=8, default_mat="Material"):
        
        ni, nj = int(size[0]/tile_size), int(size[1]/tile_size)
        if ni*tile_size < size[0]:
            ni += 1
        if nj*tile_size < size[1]:
            nj += 1
            
        self.corner = corner
        self.size   = (ni*tile_size, nj*tile_size)
        self.sats   = None
            
        super().__init__(shape=(ni, nj), tile_size=tile_size, max_subdiv=max_subdiv, default_mat=default_mat)
        
    def get_verts(self, ijs):
        verts = np.zeros(np.shape(ijs)[:-1] + (3,), float)
        verts[..., :2] = ijs * (self.tile_size / self.ij_tile_size)
        verts[..., 2] = self.z(ijs)
        
        return verts
        
    def z(self, ijs):
        return 0
    
    @property
    def size_x(self):
        return self.size[0]
    
    @property
    def size_y(self):
        return self.size[1]
    
    # ----------------------------------------------------------------------------------------------------
    # Coordinates of a tile
    
    def tile_location(self, i, j):
        return self.corner[0] + i*self.tile_size, self.corner[1] + j*self.tile_size

    # ----------------------------------------------------------------------------------------------------
    # Satellite images
    
    def init_satellite(self, mat_template, cache_folder, tiles_folder, origin, angle=0, prefix="Terrain", mat_size=4, matrices={4:14, 5:15, 6:16, 7:17, 8:18}):
        
        self.cache_folder = Path(cache_folder)
        self.tiles_folder = Path(tiles_folder)
        self.prefix       = prefix
        self.mat_template = mat_template

        self.build_materials(mat_size, detail_mats=list(matrices.keys()))
        
        self.sat_origin = origin
        self.sat_cache  = cache_folder
        
        self.sats = [None]
        for matrix in matrices.values():
            sat = SatTiles(matrix=matrix, origin=origin, cache_folder=cache_folder)
            sat.set_rotation(angle)
            #tiles.set_seam(seam_y=Seam(-RAMA_Y/2, RAMA_Y, 4096))
            self.sats.append(sat)
            
    # ----------------------------------------------------------------------------------------------------
    # Create the default material
    
    def create_whole_image(self, matrix=10):
        
        # ----- No satellite image
        
        if self.sats is None:
            raise Exception("Satellite images is not initialized!")
            
        # ----- Create the image
        
        image_name = f"{self.prefix}_{matrix}_{int(self.size[0])}_{int(self.size[1])}.jpg"
        
        fname = self.tiles_folder / image_name
        if True or not fname.exists():
            sat = SatTiles(matrix=matrix, origin=self.sat_origin, cache_folder=self.sat_cache)
            img = sat.image(self.corner, self.size, return_image=True)
            img.save(fname)
        
        return image_name
            
    # ----------------------------------------------------------------------------------------------------
    # Create the materials
    
    def get_material(self, index):
        
        # ----- No satellite image
        
        if self.sats is None:
            return super().get_material(index)

        # ----- Base image
        
        if index == 0:
            return self.default_mat

        # ----- Tile material name
        
        i, j, r = self.detailed_materials[index]
        name = f"{self.prefix} [{i:3d}, {j:3d}] {r}"
            
        # ----- Create the image
        
        fname = self.tiles_folder / f"{self.prefix}_m{self.sats[r].matrix}_O{self.corner[0]*1.:0f}_{self.corner[1]*1.:.0f}_i{i}_j{j}.jpg"
        if not fname.exists():
            x, y = self.tile_location(i*self.mat_size, j*self.mat_size)
            img = self.sats[r].image((x, y), (self.mat_size*256, self.mat_size*256), return_image=True)
            img.save(fname)
            
        # ----- Create the material
            
        image = bpy.data.images.load(str(fname), check_existing=True)
        
        debug = True
        if debug:
            mat = bpy.data.materials.get(name)
            if mat is not None:
                bpy.data.materials.remove(mat)
        
        mat = blender.change_material_image(self.mat_template, name, image)
        
        # ----- Done
        
        return name
    
# ====================================================================================================
# Altitude map

class France(Altitudes):
    
    def __init__(self, folder, corner, size, tile_size=256, max_subdiv=8, default_mat="Material"):
        
        from geopy.gis.rgealti import RgePack

        self.rge = RgePack(folder, resolution=1, origin=corner, mode='NPY')
        
        super().__init__(corner=corner, size=size, tile_size=tile_size, max_subdiv=max_subdiv, default_mat=default_mat)
        
        
    def z(self, ijs):
        return self.rge.altitudes(ijs)
    
        
# ====================================================================================================
# Terrain

class Terrain(MapTiler):
    
    def __init__(self, folder, dims, center=(0, 0, 0), max_subdiv=8, get_verts=None, default_mat="Material"):
        
        self.tiles = Tiles(folder, shape=dims)
        self.center = np.array(center)
        
        def default_get_verts(ijs):
            verts = np.zeros(np.shape(ijs)[:-1] + (3,), float)
            verts[..., :2] = ijs
            verts[..., 2] = self.tiles.values_at_coords(ijs) 
            
            verts += self.center

            return verts
        
        size = 1 << max_subdiv
        
        if get_verts is None:
            get_verts = default_get_verts
        
        super().__init__(shape=(dims[0]//size, dims[1]//size), max_subdiv=max_subdiv, get_verts=get_verts, default_mat=default_mat)
        self.sats = None
        
        
    @property
    def size_x(self):
        return self.shape[0]*256
    
    @property
    def size_y(self):
        return self.shape[1]*256
    
    # ----------------------------------------------------------------------------------------------------
    # Coordinates of a tile
    
    def tile_location(self, i, j):
        return -self.size_x/2 + i*256, -self.size_y/2 + j*256

    # ----------------------------------------------------------------------------------------------------
    # Satellite images
    
    def init_satellite(self, mat_template, cache_folder, tiles_folder, origin, angle=0, prefix="Terrain", mat_size=4, matrices={4:14, 5:15, 6:16, 7:17, 8:18}):
        
        self.cache_folder = Path(cache_folder)
        self.tiles_folder = Path(tiles_folder)
        self.prefix       = prefix
        self.mat_template = mat_template

        self.build_materials(mat_size, detail_mats=list(matrices.keys()))
        
        self.sats = [None]
        for matrix in matrices.values():
            sat = SatTiles(matrix=matrix, origin=origin, cache_folder=cache_folder)
            sat.set_rotation(angle)
            #tiles.set_seam(seam_y=Seam(-RAMA_Y/2, RAMA_Y, 4096))
            self.sats.append(sat)
            
    # ----------------------------------------------------------------------------------------------------
    # Create the materials
    
    def get_material(self, index):
        
        # ----- No satellite image
        
        if self.sats is None:
            return super().get_material(index)

        # ----- Base image
        
        if index == 0:
            return self.default_mat

        # ----- Tile material name
        
        i, j, r = self.detailed_materials[index]
        name = f"{self.prefix} [{i:3d}, {j:3d}] {r}"
            
        # ----- Create the image
        
        fname = self.tiles_folder / f"{self.prefix}_{i}_{j}_{r}.jpg"
        if not fname.exists():
            print(f"Creating file {fname.stem}")
            x, y = self.tile_location(i*self.mat_size, j*self.mat_size)
            img = self.sats[r].image((x, y), (self.mat_size*256, self.mat_size*256), return_image=True)
            img.save(fname)
            
        # ----- Create the material
            
        image = bpy.data.images.load(str(fname), check_existing=True)
        
        
        debug = False
        if debug:
            mat = bpy.data.materials.get(name)
            if mat is not None:
                bpy.data.materials.remove(mat)
        
        mat = blender.change_material_image(self.mat_template, name, image)
        
        # ----- Done
        
        return name
      
    
        
        
        