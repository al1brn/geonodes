#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:12:49 2022

@author: alain
"""

import math
import numpy as np
from pathlib import Path
from time import time

from geopy.gis import lamb93

class Timer:
    def __init__(self, shape, message="Timer"):
        self.shape   = shape
        self.total   = np.prod(shape, dtype=int)
        self.top     = time()
        self.last    = self.top
        
        print(f"{message}, total: {self.total}")
        
    @staticmethod
    def stime(t):
        s = round(t) % 60
        m = round(t) // 60
        return f"{m}:{s:02d}"
        
    def track(self, *indices):
        t = time()
        if t - self.last < 30:
            return
        
        n = np.ravel_multi_index(indices, self.shape)
        p = n/self.total
        speed = n/(t - self.top)
        
        print(f"{p*100:.1f}%, {self.stime(t - self.top)} -> {self.stime((self.total - n)/speed)}")
        
        self.last = t
        
    def done(self):
        print(f"Done in {self.stime(time() - self.top)}")


# ====================================================================================================
# A RGE Pack
#
# - folder:      folder location
# - resolution : 1 or 5 m
# - mode:        'NATIVE' or 'NPY'
#
# KEYS are 1000 * lambert 93 coordinates of the dalle
# 
# Example:
# key 1056_6303 --> lambert 93 coordinates = (1 056 000, 6 303 000)
# This is the coordinates of the BOTTOM left corner of the Dalle

class RgePack:
    
    def __init__(self, folder, resolution=1, origin=(0, 0), mode='NPY'):
        
        self.folder      = Path(folder)
        self.resolution  = resolution
        self.dalle_size  = 1000*self.resolution
        self.native_mode = mode == 'NATIVE'
        
        # ----- Origin
        
        self.origin = origin

        # ----- Content read
        
        self.ok_content = False
        self.read_folder()
        
        
        
        """
        self.keys = {}
        i0 = None
        
        ext = "*.asc" if self.native_mode else '*.npy'
        
        for fpath in self.folder.glob(ext):
            if self.native_mode:
                key = fpath.name[12:21]
            else:
                key = fpath.stem
                
            ij  = self.key_to_ij(key)
            self.keys[key] = {'ij': ij, 'file_name': fpath.name}
            
            if i0 is None:
                i0 = ij[0]
                j0 = ij[1]
                i1 = i0
                j1 = j0
            else:
                i0 = min(ij[0], i0)
                j0 = min(ij[1], j0)
                i1 = max(ij[0], i1)
                j1 = max(ij[1], j1)
                
        if i0 is None:
            raise Exception(f"No data '{ext}' in folder '{self.folder}'")
            
        # ----- Dalles
        
        self.dalles_shape  = (i1 - i0 + 1, j1 - j0 + 1)
        self.dalles_corner = (i0, j0)
        
        # ----- lamb93 dimensions
        # CAUTION: keys are BOTTOM left corner
        
        self.l93_corner = (self.dalles_corner[0]*self.dalle_size,   (self.dalles_corner[1] - 1)*self.dalle_size)
        self.l93_size   = (self.dalles_shape[0]*self.dalle_size,    self.dalles_shape[1]*self.dalle_size)
        self.l93_center = (self.l93_corner[0] + self.l93_size[0]/2, self.l93_corner[1] + self.l93_size[1]/2)
        
        # ----- Longitude and latitude map
        
        self.gps_corner = lamb93.to_lonlat(*self.l93_corner)
        self.gps_center = lamb93.to_lonlat(*self.l93_center)

        # ----- Mercator center

        self.mer_center = lamb93.mer_to_xy(*self.gps_center)
                
        print('-'*60)
        print(repr(self))
        print()
        """
        
    # ====================================================================================================
    # Read the folder
    
    def read_folder(self):
        
        exist = []
        
        i0 = None
        for f in Path(self.folder).iterdir():
            if not f.is_file():
                continue
            
            i = int(f.stem[:4])
            j = int(f.stem[5:])
            
            if i0 is None:
                i0, i1, j0, j1 = i, i, j, j
            else:
                i0, i1, j0, j1 = min(i0, i), max(i1, i), min(j0, j), max(j1, j)
                
            exist.append((i, j))
                
        self.ij0, self.ij1 = (i0, j0), (i1, j1)
        
        self.rge_map = np.zeros((i1 - i0 + 1, j1 - j0 + 1), bool)
        for i, j in exist:
            self.rge_map[i - i0, j - j0] = True
        

    # ====================================================================================================
    # Representation
        
    def __repr__(self):
                
        # ----- str

        (x0, y0), (x1, y1) = self.cr_to_xy(*self.ij0), self.cr_to_xy(*self.ij1)
        s = f"RGE folder loaded:  {self.folder}, {x0:.1f}, {y0:.1f}, {x1:.1f}, {y1:.1f}"
        
        return s
        
    # ====================================================================================================
    # Conversions
    
    # ----------------------------------------------------------------------------------------------------
    # Dalles key conversion
    
    @staticmethod
    def key_to_ij(key):
        return int(key[:4]), int(key[5:])
    
    @staticmethod
    def ij_to_key(i, j):
        return f"{i:04d}_{j:04d}"
    
    # ----------------------------------------------------------------------------------------------------
    # Lambert 93 to array index
    
    def xy_to_cr(self, x, y):    
        return math.floor( (self.origin[0] + x)/self.dalle_size) , math.floor((self.orgin[1] + y)/self.dalle_size)
    
    def cr_to_xy(self, col, row):
        return col*self.dalle_size - self.origin[0], row*self.dalle_size - self.origin[1]

    def owning_key(self, coords):
        i, j = self.xy_to_cr(*coords)
        return self.ij_to_key(i, i)
    
    def dalle_location(self, key):
        i, j = self.key_to_ij(key)
        return self.cr_to_xy(i, j)
    
    # ====================================================================================================
    # Load a dalle
            
    def load(self, key):
        
        #if key not in self.keys:
        #    return None
        
        fname = self.folder / f"{key}.npy"
        if fname.exists():
            return np.load(fname)
        
        return None
        
        # TO UPDATE ! TO UPDATE ! TO UPDATE ! TO UPDATE ! TO UPDATE ! TO UPDATE ! TO UPDATE ! TO UPDATE ! 
        
        # ----------------------------------------------------------------------------------------------------
        # Native Mode
        
        if self.native_mode:
        
            with open(self.folder / self.keys[key]['file_name'], 'r') as f:
                lines = f.readlines()
                
            # ---------------------------------------------------------------------------
            # Load
                
            a = np.empty((1000, 1000), float)
            i_start = None
                
            for i_line, line in enumerate(lines):
                if len(line) < 50:
                    continue
                
                if i_start is None:
                    i_start = i_line
                    
                i = i_line - i_start
                    
                a[:, 999 - i] = [float(v) for v in line.split(" ") if v != ""]
                
            # ---------------------------------------------------------------------------
            # Unknown values
            
            a[abs(a) > 20000] = 0
            
            # ---------------------------------------------------------------------------
            # Done
            
            return a
        
        # ----------------------------------------------------------------------------------------------------
        # Numpy array mode
        
        return np.load(self.folder / self.keys[key]['file_name'])
    
    
    def __getitem__(self, index):
        return self.load(self.ij_to_key(*index))
    
    # ====================================================================================================
    # Save as npy file
    
    def to_arrays(self, target):
        
        if not self.native_mode:
            raise Exception(f"Use to_arrays method for native RGE packs only")
        
        counter = 0
        for key in self.keys:
            counter += 1
            print(f"{counter:4d}/{len(self.keys):4d}: saving {key}")
            
            a = self.load(key)
            if a is None:
                raise Exception(f"Impossible to load file keyed {key}")
                
            np.save(Path(target) / key, a)
            
        print("Saving done")
    
    # ====================================================================================================
    # Merge several dalles
    
    def merge(self, key0, key1, scale=100):
        
        x0, y0 = self.key_to_ij(key0)
        x1, y1 = self.key_to_ij(key1)
        
        count_x = (x1 - x0)//self.resolution
        count_y = (y1 - y0)//self.resolution
        
        nx = count_x*1000//scale
        ny = count_y*1000//scale
        
        d_size = 1000//scale
        sample = tuple(np.meshgrid(np.arange(0, 1000, scale), np.arange(0, 1000, scale), sparse=True, indexing='ij'))
        
        b = np.zeros((nx, ny), float)
        
        for ix in range(count_x):
            for iy in range(count_y):
                key_x = x0 + ix*self.resolution
                key_y = y0 + iy*self.resolution
                
                print(f"Loading key {ix, iy} -> {key_x}, {key_y} ({self.ij_to_key(key_x, key_y)}) ", end = "")
                
                a = self.load(self.ij_to_key(key_x, key_y))
                if a is None:
                    print("not found")
                    continue
                print("loaded")

                i = ix*d_size
                j = iy*d_size
                
                b[i:i+d_size, j:j+d_size] = a[sample]
                
        return b
    
    # ====================================================================================================
    # Dalle to object
    
    # ----------------------------------------------------------------------------------------------------
    # A list of dalles to individual objects
    
    def dalles_to_object(self, keys, scale=10, mercator=False):
        
        from geopy.core import blender
        from geopy.core.mesh import Mesh
        
        if isinstance(keys, str):
            keys = [keys]
            
        for key in keys:
            a = self.load(key)
            if a is None:
                grid = Mesh.HeightGrid(np.array([(0, 0), (0, 0)]), scale=1, unit_size=1000*self.resolution)
                
            else:
                grid = Mesh.HeightGrid(a, scale=scale, unit_size=1)
                
            obj = blender.create_mesh_object(key)

            if mercator:
                x, y = self.lamb93_to_mer(grid._verts[..., 0], grid._verts[..., 1])
                grid._verts[..., 0] = x
                grid._verts[..., 1] = y
                del x, y

            grid.to_object(obj)
            obj.location.x, obj.location.y = self.dalle_location(key)
         
    # ----------------------------------------------------------------------------------------------------
    # A rectangular zone between corners to a single object
            
    def zone_to_object(self, key0=None, key1=None, scale=100, mercator=False):
        
        from geopy.core import blender
        from geopy.core.mesh import Mesh
    
        if key0 is None:
            x0 = self.dalles_corner[0]
            y0 = self.dalles_corner[1]
            key0 = self.ij_to_key(x0, y0)
        else:
            x0, y0 = self.key_to_ij(key0)
    
        if key1 is None:
            x1 = self.dalles_corner[0] + self.dalles_shape[0]
            y1 = self.dalles_corner[1] + self.dalles_shape[1]
            key1 = self.ij_to_key(x1, y1)
        else:
            x1, y1 = self.key_to_ij(key1)
            x1 += 1
            y1 += 1
            
        a = self.merge(key0, key1, scale=scale)
    
        unit_size = ((x1-x0)*1000/(np.shape(a)[0]-1), (y1-y0)*1000/(np.shape(a)[1]-1))
        grid = Mesh.HeightGrid(a, scale=1, unit_size=unit_size)
        
        if mercator:
            x, y = self.lamb93_to_mer(grid._verts[..., 0], grid._verts[..., 1])
            grid._verts[..., 0] = x
            grid._verts[..., 1] = y
            del x, y
        
        obj = blender.create_mesh_object(f"{key0} - {key1}")
        return grid.to_object(obj)
    
    # ====================================================================================================
    # Compute the values at arbitrary coordinates
    
    def altitudes(self, coords):
        
        # ----------------------------------------------------------------------------------------------------
        # Load a 1001 x 1001 extended dalle
        
        def ext_dalle(i_dalle, j_dalle):
            
            xdalle = np.zeros((1001, 1001), float)
            
            # ----- Main dalle
            
            dalle = self[i_dalle, j_dalle]
            if dalle is not None:
                xdalle[:1000, :1000] = dalle
                
            # ----- Default supplementary values
                
            xdalle[1000]    = xdalle[999]
            xdalle[:, 1000] = xdalle[:, 999]
            
            # ----- Supplementary values
            
            dalle = self[i_dalle + 1, j_dalle]
            corner = True
            if dalle is not None:
                xdalle[1000, :1000] = dalle[0]
                xdalle[1000, 1000]  = dalle[0, 999]
                corner = False
                
            dalle = self[i_dalle, j_dalle + 1]
            if dalle is not None:
                xdalle[:1000, 1000] = dalle[:, 0]
                if corner:
                    xdalle[1000, 1000] = dalle[999, 0]
                    
            dalle = self[i_dalle + 1, j_dalle + 1]
            if dalle is not None:
                xdalle[1000, 1000] = dalle[0, 0]
                
            del dalle
            return xdalle
        
        # ----------------------------------------------------------------------------------------------------

        alts = np.zeros(np.shape(coords)[:-1], float)
        
        dalles, offsets = np.divmod(coords + self.origin, self.dalle_size)
        dalles = dalles.astype(int)
        
        if np.size(dalles) == 0:
            return alts
        
        i_dalle0 = np.min(dalles[..., 0])
        i_dalle1 = np.max(dalles[..., 0])
        j_dalle0 = np.min(dalles[..., 1])
        j_dalle1 = np.max(dalles[..., 1])
        
        nx = i_dalle1 - i_dalle0 + 1
        ny = j_dalle1 - j_dalle0 + 1
        
        # print(f"Extraction: {nx} x {ny} dalles from {i_dalle0}, {j_dalle0}")
        
        ni = i_dalle1 - i_dalle0 + 1
        nj = j_dalle1 - j_dalle0 + 1
        n_tot = ni*nj
        
        if n_tot > 10000:
            timer = Timer((i_dalle1 - i_dalle0 + 1, j_dalle1 - j_dalle0 + 1), message="RgePack.altitudes")
        else:
            timer = None
        
        for i_dalle in range(i_dalle0, i_dalle1 + 1):
            for j_dalle in range(j_dalle0, j_dalle1 + 1):
                
                try:
                    if not self.rge_map[i_dalle - self.ij0[0], j_dalle - self.ij0[1]]:
                        continue
                except IndexError as e:
                    continue
                
                if timer is not None:
                    timer.track(i_dalle - i_dalle0, j_dalle - j_dalle0)
                
                sel = np.logical_and(dalles[..., 0] == i_dalle, dalles[..., 1] == j_dalle)
                if np.sum(sel) == 0:
                    continue
                
                xdalle = ext_dalle(i_dalle, j_dalle)
                
                #print(f"Altitudes tile ({i_dalle}, {j_dalle}) ({i_dalle - i_dalle0 + 1}/{nx} {j_dalle - j_dalle0 + 1}/{ny}), max alt: {np.max(xdalle)}")
                
                i, wx = np.divmod(offsets[..., 0][sel], 1)
                j, wy = np.divmod(offsets[..., 1][sel], 1)
                
                i = i.astype(int)
                j = j.astype(int)
                
                alts[sel] = (
                    (xdalle[i, j]*(1 - wx) + xdalle[i+1, j]*wx)*(1 - wy)
                    +
                    (xdalle[i, j+1]*(1 - wx) + xdalle[i+1, j+1]*wx)*wy
                    )
                
        if timer is not None:
            timer.done()
                
        return alts
    
    # ====================================================================================================
    # Extract a band
    #
    # corner : bottom left corner
    # size   : size
    # origin : center
    # angle  : rotation angle
    # ret    : 'ALTITUDES' (default) or 'ARRAY'
    
    def extract(self, corner, size=(1000, 1000), resolution=1, return_grid=False):
        
        # ----- Coordinates
        
        shape = (int(round(size[0]/resolution)), int(round(size[1]/resolution)))
        
        ni, nj = shape
        
        x, y = np.meshgrid(
            np.linspace(0, size[0], ni), 
            np.linspace(0, size[1], nj), 
            indexing='ij', sparse = True)
        
        coords = np.zeros(shape + (2,), float)
        coords[..., 0] = corner[0] + x
        coords[..., 1] = corner[1] + y
        
        count = np.size(coords) // 2
                
        # ----- Altitudes
        
        zs = self.altitudes(coords)
        
        if return_grid:
            from geopy.core.meshbuilder import MeshBuilder

            grid = MeshBuilder.Rectangle(ni-1, nj-1, indexing='ij')
            grid._verts[:] = np.insert(np.reshape(coords, (count, 2)), 2, np.reshape(zs, count), axis=-1)
            return grid
        
        else:
            return zs
        
    # ====================================================================================================
    # Overview
    
    def overview(self, name="Overview"):
        
        from geopy.core.meshbuilder import MeshBuilder
        
        ni, nj = self.ij1[0] - self.ij0[0] + 1, self.ij1[1] - self.ij0[1] + 1
        
        verts = np.empty((ni, nj, 3), float)
        verts[..., 0] = (self.ij0[0] + np.arange(ni))[:, None] * self.dalle_size
        verts[..., 1] = (self.ij0[1] + np.arange(nj)) * self.dalle_size
        verts[..., :2] -= self.origin
        
        verts[..., 2]  = self.altitudes(verts[..., :2])
        
        grid = MeshBuilder.Rectangle(ni-1, nj-1, indexing='ij')
        grid._verts[:] = np.reshape(verts, (np.size(verts)//3, 3))
        
        grid.to_object(name)

        
        
        
        
        
        
        
        
    
    
        

    
    
        
        
        
        
        
        
    
        
                
                    
                
            


                
            
            
    
    
    
    
    

