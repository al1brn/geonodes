#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 07:58:57 2023

@author: alain

Bake 1 : bake_nearest_houses (from )
----------------------------
    - nearest.npz : 30 nearest shapes of each shape
      . input file: shaped_houses.npz
    
Bake 2 : bake_blocks
--------------------
    - blocks.npz : surfaces, houses and block of houses
      read by HouseBlocks class
      . input file: shaped_houses.npz, nearest.npz
      
      
Bake 3 : bake_facades (from HouseBlocks)
----------------------------------------
    - Facades Houses.npz
    - Facades Blocks.npz
      One entry per facade:
          - location (Vector)
          - normal (Vector)
          - length, angle, normal (floats)
          - house seed (float)
          - face seed (float)
          - RFU (float)
    
Bake 4 : bake_house_roofs, bake_block_roofs (from HouseBlocks)
--------------------------------------------------------------
    - Roofs Blocks n.npz
    - Roofs Houses n.npz
      All the roofs as saved Meshes
      
Bake 5 : bake_facades_low
-------------------------
    - Facades - Locations.npz (Houses + Blocks)
    - Facades - Low Detail.npz
      The low resolution facades
      
Bake 6 : bake_all_roofs
-----------------------
    - Roofs - Locations.npy : roof locations
    - Roofs - Meshes.npz    : meshes

Bake 7 : bake_rama
------------------
    - Rama facades - Locations.npz
    - Rama facades - Low Detail.npz
    - Rama roofs - Locations.npy
    - Rama roofs - Meshes.npz
"""


from time import time
import numpy as np
from pathlib import Path

from geopy.core.timer import Timer

from geopy.core.quickappend import QuickArray
from geopy.core.kdtree import nearest_indices
from geopy.core import geo2D
from geopy.core.meshbuilder import Meshes

from geopy.houses import grid
from geopy.houses.constants import *
from geopy.houses.surfaces import Surface, House
from geopy.houses.elevator import HouseElevator, BlockElevator
from geopy.houses.facades import Facades


RAMA_X = 28672
RAMA_Y = 49152  # Circumference
RAMA_RADIUS = RAMA_Y / 2 / np.pi

# ====================================================================================================
# House shapes loader

def shape_loader(folder="/Users/alain/RAMA DATA/Rama/Common"):
    
    root = Path(folder)
    
    if False:
        ars  = np.load(Path(root) / "rect_houses.npz")
        info = ars['info']
        locs = ars['loc_scale'][:, 0]
    
    # ----- shaped ahouses
    
    arrays  = np.load(root / "shaped_houses.npz")
    
    info    = arrays['info']
    verts   = arrays['items']
    
    sizes   = info[:, 0]
    offsets = np.append([0], np.cumsum(sizes))

    def get_shape(index):
        return np.array(verts[offsets[index]:offsets[index+1]])        
    
    return get_shape, len(info)

# ====================================================================================================
# Bake the nearest houses

def bake_nearest_houses(folder="/Users/alain/RAMA DATA/Rama/Common", file_name="test.npy", count=30):

    get_shape, nindices = shape_loader(folder=folder)
    
    timer = Timer(f"Houses locations", nindices, delta=60)
    
    locations = np.empty((nindices, 3), float)
    for index in range(nindices):
        timer.track(index)
        
        verts = get_shape(index)
        locations[index] = np.average(verts, axis=0)
        
    timer.done()
            
    print(f"Compute {count} nearest locations...")
    
    nearest = np.array(nearest_indices(locations, count))
    
    path = Path(folder) / file_name
    
    print(f"   Saving {np.shape(nearest)} into '{path}'...")
    
    np.save(path, nearest)
    
    print("Done")
    
# =============================================================================================================================
# Bake the blocks
#
# Explore the neighbours of each house and detect shared walls between them
#
# The walls partially overlapping are split if necessary to distinguish the overlapping
# segment from the shared one.
#
# Houses sharing a wall are grouped to form blocks of houses
#
# Build the block of houses from two files:
# - house shapes
# - nearest houses
#
# The nearest houses file give the indices of the nearest houses of each house

# =============================================================================================================================
# Block indices

class Blocks:
    def __init__(self, nindices):
        """ Build the block of houses sharing a wall.
        
        A couple of houses sharing a wall is registered with the add_neighbours method.
        If none of the two houses is already registered in a block, a new block of two
        houses is created.
        If one house is already in a block, the second house is added to this block.
        If both houses are in a block, the two blocks are merged.
        
        Finally, the method get_blocks returns the block as list of house indices.
        The first "block" returned are in fact the houses not part of a block.
        
        Args:
            - nindices (int): the total number of houses
        """
    
        self.a = np.zeros(nindices, int)
        self.block_index = 1
        
    @classmethod
    def FromList(cls, nindices, blocks):
        B = cls(nindices)
        for i_block, block in enumerate(blocks):
            if i_block == 0:
                continue
            
            B.a[block] = i_block
            
        B.block_index = len(blocks)
        return B
    
    def add_neighbours(self, index0, index1):
        """ Add the indices of two houses sharinf a wall.
        
        Args:
            - index0 (int) : first index
            - index1 (int) : second index
        """
        
        block0 = self.a[index0]
        block1 = self.a[index1]
        
        if block0:
            if block1:
                if block0 != block1:
                    self.a[self.a == block1] = block0
            else:
                self.a[index1] = block0
        else:
            if block1:
                self.a[index0] = block1
            else:
                self.a[index0] = self.block_index
                self.a[index1] = self.block_index
                self.block_index += 1
                
    def add_list(self, block):
        for i in block[1:]:
            self.add_neighbours(block[0], i)
                
    def get_blocks(self):
        """ Return the houses grouped by block.
        
        Note that the first index contains the houses which are not a a block
        
        Returns:
            - list of lists : indices of each block. First block are the houses not part of a block.
        """
        
        blocks = []
        for i_block in range(self.block_index):
            houses = np.argwhere(self.a == i_block)[:, 0]
            if len(houses) > 0:
                blocks.append(list(houses))
                
        return blocks
    
    def get_indices_sizes(self):
        inds = []
        sizes = []
        for block in self.get_blocks()[1:]:
            sizes.append(len(block))
            inds.extend(block)
            
        return inds, sizes
    
    
# =============================================================================================================================
# Build the blocks

def bake_blocks(folder="/Users/alain/RAMA DATA/Rama/Common", file_name="test.npz"):
    
    get_shape, nindices = shape_loader(folder=folder)
    nearest = np.load(Path(folder) / "nearest.npy")
    
    # ----- Surfaces
    
    surf_verts  = QuickArray((0, 3), float)
    surf_shared = []
    surf_sizes  = []
    house_sizes = []
    blocks      = Blocks(nindices)
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Let's go
    
    timer = Timer(f"Build houses and blocks from {np.shape(nearest)[-1]} neighbours per house", len(nearest), delta=60)
    
    count = 0
    top = time()
    for index, indices in enumerate(nearest):
        
        timer.track(index)
        
        # ----- The primary house surface
        
        surface = Surface(index, get_shape(index))
        in_block = False
        
        # ----- Loop on the neighbours
        # The surface can be modified if neighbours share walls
        
        for i_near in indices:
            surf = Surface(i_near, get_shape(i_near))
            if surface.shared_walls_with(surf):
                in_block = True
                blocks.add_neighbours(index, i_near)
                
        # ----- The house is part of a block, we save it now
        
        if in_block:
            
            # Surface
            if True:
                surf_verts.append(surface.verts)
            else:
                surf_verts = np.append(surf_verts, surface.verts, axis=0)

            surf_shared.extend(surface.shared) 
            surf_sizes.append(len(surface))
        
            # Single surface house
            house_sizes.append(1)
            
            #print("Block index", blocks.block_index)
            
        # ----- Otherwise, the house is isolated
        # We can try to simplify it
        else:
            house = House.FromVerts(index, get_shape(index), simplify=True)
            verts, shared, sizes = house.get_verts_shared_sizes()
            
            # ----- CONTROL
            
            if len(house) > 1:
                for surf in house:
                    if not geo2D.only_square_angles(surf.verts):
                        print("NOT SQUARE @ INDEX", index)
                        #assert(False)

            # Surfaces
            if True:
                surf_verts.append(verts)
            else:
                surf_verts  = np.append(surf_verts, verts, axis=0)

            surf_shared.extend(shared) 
            surf_sizes.extend(sizes)
            
            # Multi surfaces house
            house_sizes.append(len(sizes))
            
    timer.done()
    
    # ----------------------------------------------------------------------------------------------------
    # Save the result
    
    root = Path(folder)

    block_inds, block_sizes = blocks.get_indices_sizes()

    np.savez(root / file_name,
             surf_verts  = surf_verts.a,
             surf_shared = surf_shared,
             surf_sizes  = surf_sizes,
             
             house_sizes = house_sizes,
             
             block_inds  = block_inds,
             block_sizes = block_sizes,
             )
    
    print("Baked blocks saved to", file_name)
    
# ====================================================================================================
# Bake the facades

def bake_facades(hbs, folder, ok_houses=True, ok_blocks=True):
    
    # ----- Houses
    
    if ok_houses:
        timer = Timer('Bake house facades', len(hbs.house_inds), delta=60)
        
        arrays = None
        for i, i_house in enumerate(hbs.house_inds):
            
            timer.track(i)
                
            house = HouseElevator(hbs.get_house(i_house), i_house)
            arrays = house.walls_to_arrays(arrays)
            
        timer.done()
        
        np.savez(folder / "Facades Houses.npz", locs=arrays['locs'].a, options=arrays['options'].a)
    
    # ----- Blocks
    
    if ok_blocks:
        timer = Timer('Bake block facades', hbs.blocks_count, delta=60)
        
        arrays = None
        for i_block in range(hbs.blocks_count):
            
            timer.track(i_block)
                
            block = BlockElevator(hbs.get_block(i_block), i_block)
            arrays = block.walls_to_arrays(arrays)

        timer.done()
        
        np.savez(folder / "Facades Blocks.npz", locs=arrays['locs'].a, options=arrays['options'].a)
    
# ====================================================================================================
# Bake the roofs

def bake_house_roofs(hbs, folder, batch_size=25000, batch_num=0): 
    
    meshes = Meshes(materials=HOUSE_MATERIALS)
    meshes.new_face_attribute("house_seed", 'FLOAT')
    meshes.new_face_attribute("face_seed", 'FLOAT')

    from_index = batch_size * batch_num
    to_index   = min(batch_size * (batch_num + 1), len(hbs.house_inds))
    
    timer = Timer(f"Bake single house roofs #{batch_num} {to_index}/{len(hbs.house_inds)}", to_index - from_index, delta=30)
    
    for index in range(from_index, to_index):
        
        i_house = hbs.house_inds[index]
        
        timer.track(index - from_index)
            
        house = HouseElevator(hbs.get_house(i_house), i_house)
        roofs = house.roofs()
        if roofs is None:
            continue
        
        meshes.append(roofs)

    timer.done()
        
    if len(meshes) == 0:
        return False
        
    file_name = f"Roofs Houses {batch_num}.npz"
    print(f"write file '{file_name}'")

    meshes.quick_done()
    meshes.check()
    meshes.save(Path(folder) / file_name)
    
    return True
        
        
# ====================================================================================================
# Bake the roofs

def bake_block_roofs(hbs, folder, batch_size=10000, batch_num=0):
    
    meshes = Meshes(materials=HOUSE_MATERIALS)
    meshes.new_face_attribute("house_seed", 'FLOAT')
    meshes.new_face_attribute("face_seed", 'FLOAT')
    
    from_index = batch_size*batch_num
    to_index   = min(batch_size*(batch_num + 1), hbs.blocks_count)
    
    timer = Timer(f"Bake block roofs #{batch_num} {to_index}/{hbs.blocks_count}", to_index - from_index, delta=30)
    
    for i_block in range(from_index, to_index):
        
        timer.track(i_block - from_index)
            
        block = BlockElevator(hbs.get_block(i_block), i_block)
        roofs = block.roofs()
        if roofs is None:
            continue
        
        meshes.append(roofs)

    timer.done()
    
    if len(meshes) == 0:
        return False
        
    file_name = f"Roofs Blocks {batch_num}.npz"
    print(f"write file '{file_name}'")

    meshes.quick_done()
    meshes.check()
    meshes.save(Path(folder) / file_name)
    
    return True
    
# ====================================================================================================
# Bake faces low faces

def bake_facades_low(folder):
    
    # ----------------------------------------------------------------------------------------------------
    # All the facades in the same file
    
    print("Merge houses and blocks facades")
    
    houses = np.load(Path(folder) / "Facades Houses.npz")
    blocks = np.load(Path(folder) / "Facades Blocks.npz")
    
    assert(len(houses['locs']) == len(houses['options']))
    assert(len(blocks['locs']) == len(blocks['options']))
    
    locs    = np.append(houses['locs'], blocks['locs'], axis=0)
    options = np.append(houses['options'], blocks['options'], axis=0)
    
    assert(len(locs) == len(houses['locs']) + len(blocks['locs']))
    assert(len(locs) == len(options))
    
    facades_file_name = "Facades - Locations.npz"
    
    np.savez(Path(folder) / facades_file_name, locs=locs, options=options)
    
    print(f"{len(locs)} facades written in '{facades_file_name}'")
    print()
    
    # ----------------------------------------------------------------------------------------------------
    # Bake low detail facades as quads
    
    facades = Facades(folder)
    
    meshes = Meshes(grow=1000000)
    meshes.new_face_attribute("house_seed", 'FLOAT')
    meshes.new_face_attribute("face_seed",  'FLOAT')
    #meshes.attributes.quick_init(quick_length=1000000)
    
    timer = Timer(f"Build the low detail facades as quads", len(locs), delta=30)
    
    for i in range(len(locs)):
        timer.track(i)
        meshes.append(facades.low_detail(i))
        
    timer.done()
    
    print(meshes)
    meshes.check()
    
    file_name = "Facades - Low Detail.npz"
    meshes.save(Path(folder) / file_name)
    
    print(f"Low detail faces saved in '{file_name}'")
    
# ====================================================================================================
# Bake all roofs

def bake_all_roofs(folder):
    
    roofs = Meshes()
    roofs.new_face_attribute("house_seed", 'FLOAT')
    roofs.new_face_attribute("face_seed",  'FLOAT')
    #roofs.new_face_attribute("seed", 'FLOAT')
    #roofs.new_face_attribute("face random",  'FLOAT')
    
    for i in range(9):
        hroofs = Meshes.Load(Path(folder) / f"Roofs Houses {i}.npz")
        roofs.append(hroofs)
        
    for i in range(12):
        broofs = Meshes.Load(Path(folder) / f"Roofs Blocks {i}.npz")
        roofs.append(broofs)

    roofs.quick_done()
        
    #roofs.attributes["house_seed"] = roofs.attributes["seed"]
    #del roofs.attributes["seed"]
    #roofs.attributes["face_seed"] = roofs.attributes["face random"]
    #del roofs.attributes["face random"]
    
    roofs.materials = ['Wall', 'Roof', 'Flat Roof', 'Terrace', 'BalcFence', 'Roof Border']

    print(roofs)
    
    n = len(roofs)
    locs = np.zeros((n, 3), float)
    
    timer = Timer("Roofs location", n, delta=30)
    for i in range(n):
        timer.track(i)
        locs[i] = np.average(roofs[i].verts, axis=0)
    timer.done()
    
    file_name = "Roofs - Locations.npy"
    print(f"Save locations in '{file_name}'")
    np.save(folder / file_name, locs)
    
    file_name = "Roofs - Meshes.npz"
    print(f"Save meshes in '{file_name}'")
    roofs.save(folder / file_name)
    
# ====================================================================================================
# Bake Rama

def bake_rama(folder):
    
    def to_rama_OLD(verts):
        print(f"   > transforming {np.shape(verts)}")
        rs  = RAMA_RADIUS - verts[:, 2]
        ags = (verts[:, 1] - RAMA_Y/2)/RAMA_RADIUS
        
        res = np.array(verts)
        res[:, 1] = rs*np.sin(ags)
        res[:, 2] = -rs*np.cos(ags)
        
        return res


    def to_rama(verts):
        print(f"   > transforming {np.shape(verts)}")

        thetas = verts[:, 1]/RAMA_RADIUS
        r      = RAMA_RADIUS - verts[:, 2]
        
        res = np.array(verts)

        res[:, 1] =  r*np.sin(thetas)
        res[:, 2] = -r*np.cos(thetas)
        
        #self.verticals  = -self.locs/np.expand_dims(np.linalg.norm(self.locs[:, 1:], axis=-1), axis=-1)
        #self.verticals[:, 0] = 0
        
        return res
    
    
    # ----- Facades locations
    
    print("Facades locations...")
    
    ars = np.load(Path(folder) / "Facades - Locations.npz")
    
    locs = ars['locs']
    options = ars['options']
    
    ags = (locs[:, 0, 1] - RAMA_Y/2)/RAMA_RADIUS

    locs[:, 0] = to_rama(locs[:, 0])
    
    # ----- Normal
    # z = 0, x doesn't change

    locs[:, 1, 2] = np.sin(ags)*locs[:, 1, 1]
    locs[:, 1, 1] *= np.cos(ags)
    
    np.savez(Path(folder) / "Rama Facades - Locations.npz", locs=locs, options=options)
    
    # ----- Facades Low res

    print("Facades low res...")

    meshes = Meshes.Load(Path(folder) / "Facades - Low Detail.npz")
    meshes._verts = to_rama(meshes._verts)
    meshes.save(Path(folder) / "Rama Facades - Low Detail.npz")

    # ----- Roofs Locations

    print("Roofs locations...")
    
    a = np.load(Path(folder) / "Roofs - Locations.npy")
    np.save(Path(folder) / "Rama Roofs - Locations.npy", to_rama(a))

    # ----- Roofs Meshes

    print("Roofs meshes...")

    meshes = Meshes.Load(Path(folder) / "Roofs - Meshes.npz")
    meshes._verts = to_rama(meshes._verts)
    meshes.save(Path(folder) / "Rama Roofs - Meshes.npz")
    
    print("Rama done")
    
        
