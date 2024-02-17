#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:36:47 2023

@author: alain

Data base of houses and blocks


Bake the roofs and facades files

"""

import numpy as np
from time import time
from pathlib import Path

ZERO = .001

from geopy.core import geo2D

from geopy.core.meshbuilder import Meshes
from geopy.houses.constants import *

# ====================================================================================================
# Read the houses and blocks file
#
# The base structure is a surface, i.e. a shape made of vertices
# A house is a list of surfaces sharing some walls
# A block is the same but each surface is a house
#
# The structure is the following:
# Surface:
# - verts  : vertices of the surface contour
# - sizes  : slicer of the verts
# - shared : index of the peer surface if the segment starting by this vertex is shared
#
# House:
# - sizes : number of surfaces of the house, used to slice range(houses_count)
#
# Block:
# - indices : indices of the houses in the block
# - sizes : number of houses in the block, used to slice the previous array
#
# Note: the houses of a block have only one surface. As a consequence, a block and a house
# share the same structure : a list of surfaces. In a house, the share index points to the
# index in the list when in a block, the shared index is the house index.


# ====================================================================================================
# Surface

class Surface:
    def __init__(self, index, verts, shared):
        self.index  = index
        self.verts  = verts
        self.shared = shared
        
    def __str__(self):
        return f"<Surface of {len(self.verts)} vertices>"
    
    # ====================================================================================================
    # Some properties
    
    @property
    def area(self):
        return geo2D.area(self.verts)
    
    @property
    def vectors(self):
        return np.roll(self.verts[:, :2], -1, axis=0) - self.verts[:, :2]
    
    @property
    def lengths(self):
        return geo2D.lengths(self.verts)
    
    @property
    def angles(self):
        return geo2D.angles(self.verts)
    
    @property
    def average_angle(self):
        return geo2D.average_angle(self.verts, precision=10)
    
    # ====================================================================================================
    # A rotated copy
    
    @staticmethod
    def rotation_matrix(angle):
        return geo2D.rotation_matrix(self.angle)
        
    def rotate(self, angle, pivot=None):
        return Surface(self.index, geo2D.rotate(self.verts, angle, pivot), self.shared)

    # ====================================================================================================
    # Relationship between two neighbours
    
    # ----------------------------------------------------------------------------------------------------
    # Get the full side wall owning a given segment
    
    def full_wall(self, index):
        """ Get the full side containing a shared side.
        """
        return geo2D.full_segment(self.verts, index)
    
    # ----------------------------------------------------------------------------------------------------
    # Get the indices of the shared walls between two neighbour surfaces
    
    def get_shared_walls(self, other):
        
        d2 = np.sum((self.verts[:, None, :2] - other.verts[None, :, :2])**2, axis=-1)
        inds = np.argwhere(d2 < ZERO)
        
        # ----- We need a correct input
        
        if np.shape(inds) != (2, 2):
            return None, None

        if inds[1, 0] == (inds[0, 0] + 1) % len(self.verts):
            return inds[0, 0], inds[1, 1]
        else:
            return inds[1, 0], inds[0, 1]
        
    # ----------------------------------------------------------------------------------------------------
    # Relation between a surface and a neighbour
    
    def relation_to(self, other):
        """ Relation to a 'major' surface.
        
        If the segments overlap, returns a dictionnary:
            - x0 (float) : location of the begining of the minor segment in the major segment (min1 location)
            - x1 (float) : location of the end of the minor segment in the major segment (min0 location)
            - major_length (float) : length of the major segment
            - loc0 (int) : -1, 0 or 1 if the minor starting point min0 is outside the major segment equal to maj1 or inside the major segment
            - loc1 (int) : -1, 0 or 1 if the minor ending point min1 is outside the major segment equal to maj0 or inside the major segment
            - P0 (vector) : start of the overlapping segment
            - P1 (vector) : end of the overlapping segment
            
        Since the segments are oriented and the overlap is taken into account only if the segments are in oppposite directions.
        For instance, the segments [A, B] and [A, B] don't overlap when [A, B] and [B, A] fully overlap.
        
        x0, x1 and P0, P1 are given in the order of the major segment : x0 < x1. P0 < P1 in the direction of the major segment
        loc0 and loc1 are flags for the minor segment.
        
        Examples: given 6 points A, B, C, D, E, F aligned are regularly spaced with an interval of value 1
        -  - B - - E -
        -  A - C D - F
        - major: [B E], minor: [D A] -> loc0, loc1: ( 1, -1), x0, x1: [-1.0,  2.0], P0 P1: [B, D]
        - major: [B E], minor: [D B] -> loc0, loc1: ( 1,  0), x0, x1: [ 0.0,  2.0], P0 P1: [B, D]
        - major: [B E], minor: [D C] -> loc0, loc1: ( 1,  1), x0, x1: [ 1.0,  2.0], P0 P1: [C, D]
        - major: [B E], minor: [E A] -> loc0, loc1: ( 0, -1), x0, x1: [-1.0,  3.0], P0 P1: [B, E]
        - major: [B E], minor: [E B] -> loc0, loc1: ( 0,  0), x0, x1: [ 0.0,  3.0], P0 P1: [B, E]
        - major: [B E], minor: [E C] -> loc0, loc1: ( 0,  1), x0, x1: [ 1.0,  3.0], P0 P1: [C, E]
        - major: [B E], minor: [F A] -> loc0, loc1: (-1, -1), x0, x1: [-1.0,  4.0], P0 P1: [B, E]
        - major: [B E], minor: [F B] -> loc0, loc1: (-1,  0), x0, x1: [ 0.0,  4.0], P0 P1: [B, E]
        - major: [B E], minor: [F C] -> loc0, loc1: (-1,  1), x0, x1: [ 1.0,  4.0], P0 P1: [C, E]
        
        
        Returns:
            - None if the segments are not aligned or don't overlap in opposite directions, dict otherwise.
        """
        
        return geo2D.joining(other.verts, self.verts)


    # ====================================================================================================
    # Get the walls
    
    def get_full_walls(self, precision=3):
        """ Get the walls, ie the succession of wall possibly into shared segments.
        """
        return geo2D.unsplit(self.verts, precision=precision)
    
    
    # ----------------------------------------------------------------------------------------------------
    # Get the unsplit vertices
    
    def unsplit_verts(self):
        return self.get_full_walls()['verts']
    

# ====================================================================================================
# List of surfaces
        
class Surfaces(list):
    def __init__(self, index, is_house=True):
        super().__init__()
        self.index    = index
        self.is_house = is_house
        
    # ====================================================================================================
    # Recalc the shared segments
        
    def recalc_shared(self):
        
        # Recover the rectangular shape
        new = [surf.unsplit_verts() for surf in self]
        
        # Split segment where there is a corner of another rectangle
        # each time a corner is created we, must redo the double loops again
        # Luckily, they is not that much surfaces !
        again = True
        while again:
            again = False
            for i in range(len(new)):
                for j, s_verts in enumerate(new):
                    if j == i:
                        continue
                    for k, p in enumerate(s_verts):
                        n = len(new[i])
                        new[i] = geo2D.split_contour(new[i], p)
                        if len(new[i]) > n:
                            again = True
                    
        # New Surfaces
        self.clear()
        for i_surf, surf in enumerate(new):
            self.append(Surface(i_surf, surf, [-1]*len(surf)))
            
        # Compute the shared segments
        for i, surf in enumerate(self[:-1]):
            for i_pt, (p0, p1) in enumerate(zip(surf.verts, np.roll(surf.verts, -1, axis=0))):
                for j in range(i+1, len(self)):
                    other = self[j]
                    for j_pt, (q0, q1) in enumerate(zip(other.verts, np.roll(other.verts, -1, axis=0))):
                        if geo2D.equal(p0, q1) and geo2D.equal(p1, q0):
                            surf.shared[i_pt] = j
                            other.shared[j_pt] = i
                            break
                        

    # ====================================================================================================
    # Properties
        
    @property
    def max_index(self):
        if len(self) == 1:
            return 0
        else:
            return np.argmax([surf.area for surf in self])
        
    @property
    def average_angle(self):
        return self[self.max_index].average_angle
    
    def rotate(self, angle, pivot=None):
        if pivot is None:
            pivot = np.average(self[self.max_index].verts, axis=0)
        
        surfaces = Surfaces(self.index, self.is_house)
        for surf in self:
            surfaces.append(surf.rotate(angle, pivot=pivot))
            
        return surfaces
    
    @property
    def all_verts(self):
        verts = np.zeros((0, 3), float)
        for surf in self:
            verts = np.append(verts, surf.verts, axis=0)
        return verts
    
    @property
    def bounds(self):
        verts = self.rotate(angle = -self.average_angle).all_verts
        return np.max(verts[:, :2], axis=0) - np.min(verts[:, :2], axis=0)
    
    @property
    def is_L_shape(self):
        return self.L_shape() is not None
    
    def L_shape(self):
        if len(self) != 2:
            return None
        
        lens = (len(self[0].verts), len(self[1].verts))
        if lens != (4, 5) and lens != (5, 4):
            return None
        
        contour = self.get_contours()[0]
        verts = geo2D.unsplit(np.array([seg["v0"] for seg in contour]))["verts"]
        
        lengths = geo2D.lengths(verts)
        i_max = np.argmax(lengths)
        verts = np.array(np.roll(verts, -i_max, axis=0))
        
        ls = geo2D.lengths(verts)
        i0 = 1 + np.argmax([ls[1], ls[3], ls[5]])*2
        i1 = (i0 + 2) % 6
        i2 = (i0 + 4) % 6
        
        iw2 = 5 if i0 == 1 else 1
        il2 = 2 if i0 == 1 else 4
        
        return {'verts': verts, 'lengths': lengths,
                'length_indicex': [0, 2, 4], 'width_indices': [i0, i1, i2], 'min_width_index': iw2, 'L_width_index': il2,
                'length': ls[0], 'width': ls[i0], 'L_width': ls[il2], 'max_width': ls[i0], 'min_width': ls[iw2],
                }
        
        
    
    # ====================================================================================================
    # Find a shared segment peer surface
    
    def get_shared_wall_index(self, surface_index, seg_index):
        
        surface = self[surface_index]
        shared  = surface.shared[seg_index]
        if shared < 0:
            return None
        
        for i_seg, i_surf in enumerate(self[shared].shared):
            if i_surf == surface_index:
                return i_seg
            
        return None
    
    
    # ====================================================================================================
    # Get contour
    
    def get_contours(self, selection=None):
        
        if selection is None:
            selection = [i for i in range(len(self))]
            
        segments = []
        for i_surf, surf in enumerate(self):
            if i_surf not in selection:
                continue
            
            for i_seg, (v0, v1) in enumerate(zip(surf.verts, np.roll(surf.verts, -1, axis=0))):
                if surf.shared[i_seg] in selection:
                    continue
                
                segments.append( {"v0": np.array(v0), "v1": np.array(v1), "surface": surf, "i_seg": i_seg, "shared": surf.shared[i_seg]})
                
        contours = []
        contour  = None
        
        while len(segments):
            if contour is None:
                contour = [segments[0]]
                contours.append(contour)
                del segments[0]
                
            ok = False
            for i_seg, seg in enumerate(segments):
                if geo2D.equal(contour[-1]["v1"], seg["v0"]):
                    contour.append(seg)
                    del segments[i_seg]
                    ok = True
                    
                    if geo2D.equal(contour[-1]["v1"], contour[0]["v0"]):
                        contour = None
                    break
                
            # Not normal: shouldn't occur
            if not ok:
                return contours
                
        return contours
    
    # ====================================================================================================
    # External surface
    
    def circumference(self):
        verts = np.array([seg["v0"] for seg in self.get_contours()[0]])
        surf = Surface(index=0, verts=verts, shared=[-1]*len(verts))
        surfs = Surfaces(index=self.index, is_house=self.is_house)
        surfs.append(surf)
        return surfs
        
    # ====================================================================================================
    # Contour utility
    
    @staticmethod
    def inset_contours(contours, delta=-.3):
        
        new_contours = []
        for contour in contours:
            
            new_contour = [{**seg} for seg in contour]
            new_contours.append(new_contour)
            
            # ----- Compute the relative angles between the segments
            
            verts = geo2D.inset(np.array([seg["v0"] for seg in contour]), delta=delta)
            for i, v in enumerate(verts):
                new_contour[i]["v0"] = v
                new_contour[(i-1)%len(new_contour)]["v1"] = v
                
        return new_contours

    # ====================================================================================================
    # Debug
        
    def plot(self, title="Surfaces"):
        
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        for surf in self:
            vs = np.resize(surf.verts, (len(surf.verts)+1, 3))
            ax.plot(vs[:, 0], vs[:, 1], 'x-', linewidth=1)
            
            ax.plot(vs[0, 0], vs[0, 1], 'o')
            
            for i, sh in enumerate(surf.shared):
                if True or sh >= 0:
                    continue
                
                ax.plot((vs[i, 0], vs[i+1, 0]), (vs[i, 1], vs[i+1, 1]), '-r', linewidth=2)
            
        plt.title(title)
        plt.show()
        
# ====================================================================================================
# House & blocks data

class HouseBlocks:
    def __init__(self, file_path):

        ars = np.load(file_path)
        
        self.surf_verts  = ars['surf_verts']
        self.surf_shared = ars['surf_shared']
        self.surf_sizes  = ars['surf_sizes']
        
        self.house_sizes = ars['house_sizes']
        
        self.block_inds  = ars['block_inds']
        self.block_sizes = ars['block_sizes']
        
        self.surf_offsets  = np.append([0], np.cumsum(self.surf_sizes))
        self.house_offsets = np.append([0], np.cumsum(self.house_sizes))
        self.block_offsets = np.append([0], np.cumsum(self.block_sizes))
        
        # ----- Single house indices
        
        sel = np.ones(len(self.house_sizes), bool)
        try:
            sel[self.block_inds] = False
            self.house_inds = np.array(np.arange(len(self.house_sizes))[sel])
        except:
            self.house_inds = np.arange(len(self.house_sizes))
            pass
        
        
    def __str__(self):
        s = "House and blocks:"
        s += f"\n   - Blocks     : {self.blocks_count:7d}"
        s += f"\n   - Houses     : {self.houses_count:7d}"
        s += f"\n      in blocks : {len(self.block_inds):7d} ({len(self.block_inds)/self.houses_count*100:.0f}%)"
        s += f"\n      single    : {len(self.house_inds):7d} ({len(self.house_inds)/self.houses_count*100:.0f}%)"
        s += f"\n   - Surfaces   : {self.surfaces_count:7d} / {self.house_offsets[-1]:7d}"
        s += f"\n   - vertices   : {self.verts_count:7d} / {self.surf_offsets[-1]:7d}"
        return s + "\n"
    
    @property
    def blocks_count(self):
        return len(self.block_sizes)
    
    @property
    def houses_count(self):
        return len(self.house_sizes)
    
    @property
    def surfaces_count(self):
        return len(self.surf_sizes)
    
    @property
    def verts_count(self):
        return len(self.surf_verts)
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Load
    
    def get_surface(self, index):
        slc = slice(self.surf_offsets[index], self.surf_offsets[index+1])
        return Surface(index, self.surf_verts[slc], self.surf_shared[slc])
    
    def get_house(self, index, set_surface_indices=True):
        
        surf_inds = np.arange(len(self.surf_sizes))[self.house_offsets[index]:self.house_offsets[index+1]]
        house = Surfaces(index, True)
        house.extend([self.get_surface(i) for i in surf_inds])
        
        # ----- Bug
        
        if set_surface_indices:
            if True:
                house.recalc_shared()
            else:
                for i, surf in enumerate(house):
                    surf.index = i
        
        return house
    
    def get_block(self, index):
        house_inds = self.block_inds[self.block_offsets[index]:self.block_offsets[index+1]]
        block = Surfaces(index, False)
        for i in house_inds:
            
            if i < self.houses_count:
                house = self.get_house(i)
            else:
                print("INVALID INDEX, block", index, "house index", i, "greater than", self.houses_count, "(", len(house_inds), ")")
            
            if len(house) == 0:
                continue
            
            if len(house) > 1:
                #print("HOUSE LEN, block", index, "house", i, "is len", len(house))
                house = house.circumference()
                #print("-->", len(house))
                
            assert(len(house)==1)
            block.append(house[0])
            
        return block
    
    def check(self, houses=True, blocks=True):
        if houses:
            print("Checking houses blocks...")
            for i_house in range(self.houses_count):
                if i_house % 10000 == 0:
                    print(f"   {i_house}/{self.houses_count}")
                house = self.get_house(i_house, set_surface_indices=False)
            print(self.houses_count, "loaded")
            
        if blocks:
            for i_block in range(self.blocks_count):
                if i_block % 10000 == 0:
                    print(f"   {i_block}/{self.blocks_count}")
                block = self.get_block(i_block)
            print(self.blocks_count, "loaded")
            
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # plot a house
    
    def plot_house(self, index):
        house = hbs.get_house(index)
        house.plot(f"House {index}")
        

    
    
if __name__ == "__main__":
    
    import matplotlib.pyplot as plt
    
    def plot_verts(*verts, title="Plot", fmt='x-'):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        for vs in verts:
            v = np.resize(vs, (len(vs)+1, 3))
            ax.plot(v[:, 0], v[:, 1], fmt)
            
        plt.title(title)
        plt.show()
    
    h_indices = [413056, 372227, 133680, 499116, 18186, 218805, 56570]
    h_indices = [56570]
    
    rng = np.random.default_rng()
    
    hbs = HouseBlocks("/Users/alain/RAMA DATA/Rama/Common/blocks.npz")
    print(hbs)
    
    for index in range(3000):
        
        house = hbs.get_house(index)
        if house.is_L_shape:
            hbs.plot_house(index)
            lshape = house.L_shape()
            
            ls = geo2D.lengths(lshape['verts'])
            print("\nIndex", index)
            print(f"Length: {ls[0]:4.1f} = {ls[2]:4.1f} + {ls[4]:4.1f} --> {ls[0] - ls[2] - ls[4]:4.1f}")
            i0 = lshape['width_indices'][0]
            i1 = lshape['width_indices'][1]
            i2 = lshape['width_indices'][2]
            print(f"Width : {ls[i0]:4.1f} = {ls[i1]:4.1f} + {ls[i2]:4.1f} --> {ls[i0] - ls[i1] - ls[i2]:4.1f}")
            print(f"L width: {lshape['L_width']:4.1f}, max_width: {lshape['max_width']:4.1f}, min_width: {lshape['min_width']:4.1f}")

            if abs(lshape['L_width'] - lshape['min_width']) < geo2D.ZERO:
                plot_verts(lshape['verts'], title=f"Index {index} 0 / {i0}")
            
            assert(i0 in [1, 5])

            
            
        
        
        continue
        
        contour = house.get_contours()[0]
        verts = [seg['v0'] for seg in contour]
        
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        vs = np.resize(verts, (len(verts)+1, 3))
        ax.plot(vs[:, 0], vs[:, 1], '-k', linewidth=1)
        
        verts = geo2D.inset(verts, .5)

        vs = np.resize(verts, (len(verts)+1, 3))
        ax.plot(vs[:, 0], vs[:, 1], '-r', linewidth=1)
        
        plt.title(f"House {index}")
        
        plt.show(f"Contours {index}")
        

   