#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:28:36 2023

@author: alain
"""

import numpy as np

from geopy.core import blender
from geopy.core.arrayslicer import ArraySlicer
from geopy.core.quickappend import QuickArray
from geopy.core.meshbuilder import MeshBuilder

# =============================================================================================================================
# Transform an asset

class Asset(MeshBuilder):
    
    DISCREET   = 0
    CONTINUOUS = 1
    RELATIVE   = 2
    
    def __init__(self, spec=None, materials=None):
        
        super().__init__(materials=materials)
        
        self.shapes        = None
        self.variants      = None
        
        self.interpolation = 0
        self.weight        = 1
        self.name          = ""
        
        if spec is None:
            pass
        
        elif isinstance(spec, MeshBuilder):
            self.copy(spec)
            
        else:
            self.from_mesh_data(blender.get_object(spec).data)
            self.shapes = blender.get_shape_keys(spec)
            self.name   = blender.get_object(spec).name
            
            if "CONT" in self.name.split(" "):
                self.interpolation = Asset.CONTINUOUS
            elif "DIS" in self.name.split(" "):
                self.interpolation = Asset.DISCREET
            elif self.shapes is not None:
                self.interpolation = Asset.RELATIVE
                    
            words = self.name.split("(")
            if len(words) > 1:
                words = words[1].split(")")
                if words[0].isnumeric:
                    self.weight = float(words[0])
                    
    def __str__(self):
        s = f"<Asset '{self.name}': "
        if self.has_variations:
            if self.variants is None:
                sitp = ['DISCREET', 'CONTINUOUS', 'RELATIVE'][self.interpolation]
                s += f"interpolation '{sitp:10s}' on {np.shape(self.shapes)[:-1]} vertices"
            else:
                s += f" with {len(self.variants) + 1} variants"
        else:
            s += f"simple {self.verts_len} vertices"
        return s + ">"

    # ====================================================================================================
    # Dump to a meshbuilder
    
    def to_object(self, name):
        
        res = MeshBuilder.Copy(self)
        size = np.max(res.verts, axis=0) - np.min(res.verts, axis=0)
        
        if self.shapes is not None:
            n = len(self.shapes)
            
        elif self.variants is not None:
            n = len(self.variants)
            
        else:
            n = 0
            
        for i in range(n):
            mb = self.discreet_shape(i)
            mb._verts += (0, 0, i*size[2]*1.1)
            res.append(mb)
            
        return res.to_object(name)
    
    # ====================================================================================================
    # To and from arrays
    
    @staticmethod
    def new_arrays():
        arrays = MeshBuilder.new_arrays()
        
        arrays['assets'] = QuickArray((0, 5), int)
        
        return arrays
    
    def to_arrays(self, arrays):
        
        params = [len(arrays['sizes']), 0 if self.shapes is None else len(self.shapes), 0 if self.variants is None else len(self.variants), self.interpolation, self.weight]
        arrays['assets'].append(params)
        
        super().to_arrays(arrays)

        if self.shapes is not None:
            mb = MeshBuilder(uvmap=False)
            for i in range(len(self.shapes)):
                mb._verts = self.shapes[i]
                mb.to_arrays(arrays)
                
        if self.variants is not None:
            for variant in self.variants:
                variant.to_arrays(arrays)
                
        return arrays
    
    @classmethod
    def FromArrays(cls, arrays, index):
        
        params = arrays['assets'][index]
        asset_index = params[0]
        
        # ----- Asset
        
        asset = Asset(MeshBuilder.FromArrays(arrays, asset_index))
        
        asset.interpolation = params[3]
        asset.weight        = params[4]

        # ----- Shapes
        
        nshapes = params[1]
        if nshapes:
            asset.shapes = np.resize(asset.verts, (nshapes, len(asset.verts), 3))
            for i in range(nshapes):
                mb = MeshBuilder.FromArrays(arrays, asset_index + 1 + i)
                asset.shapes[i] = mb.verts

        # ----- Variants
                
        nvariants = params[2]
        if nvariants:
            asset.variants = []
            for i in range(nvariants):
                asset.variants.append(MeshBuilder.FromArrays(arrays, asset_index + nshapes + 1 + i))
                
        return asset
    
    # ====================================================================================================
    # Initialize from a list of variants of differet shape
                    
    @classmethod
    def Variants(cls, base, *variants):
        asset = cls(base)
        if len(variants):
            asset.variants = variants
        return asset

    # ====================================================================================================
    # Initialize from a list of variants with the same shape
    
    @classmethod
    def Deform(cls, base, *variants, discreet=False, relative=True):
        
        asset = cls(base)
        
        if len(variants):
            asset.shapes = np.resize(asset.verts, (len(variants) + 1, asset.verts_len, 3))
            for i, variant in enumerate(variants):
                asset.shapes[i+1] = variant.verts
                
            asset.relative = relative and len(asset.shapes) > 2
            asset.discreet = discreet
            if asset.discreet:
                asset.relative = False
                
        return asset
    
    # ====================================================================================================
    # Initialize as a wall

    @classmethod
    def Wall(cls, v2, x=0, mat_name="Wall"):
        ash = cls(materials=[mat_name])
        ash.add_surface([(x, v[0], v[1]) for v in v2])
        return ash

    # ====================================================================================================
    # Copy from another meshbuilder or asset
    
    def copy(self, other):
        super().copy(other)
        
        if isinstance(other, Asset):
            self.shapes        = other.shapes
            self.variants      = other.variants
            self.interpolation = other.interpolation
            self.weight        = other.weight
            self.name          = other.name
        
        return self
    
    # ====================================================================================================
    # Capture another meshbuidler or asset
    
    def capture(self, other):
        super().capture(other)
        
        if isinstance(other, Asset):
            self.shapes        = other.shapes
            self.variants      = other.variants
            self.interpolation = other.interpolation
            self.weight        = other.weight
            self.name          = other.name
        
        return self
    
    # ====================================================================================================
    # Shape
    
    def relative_shape(self, ts):
        
        assert(self.shapes is not None)
        assert(len(ts) == len(self.shapes) - 1)
        
        mb = MeshBuilder.Copy(self)
        for i, w in enumerate(ts):
            mb._verts += w*(self.shapes[i + 1] - self.verts)

        asset = Asset().capture(mb)
        asset.name = self.name
        
        return asset
                
    def discreet_shape(self, n):
        
        if self.variants is not None:
            assert(n >= 0 and n < len(self.variants))
            
            asset = Asset().capture(self.variants[n])
            asset.name = self.name
            
            return asset
        
        assert(self.shapes is not None)
        assert(n >= 0 and n < len(self.shapes))
        
        mb = MeshBuilder.Copy(self)
        mb._verts[:] = self.shapes[n]

        asset = Asset().capture(mb)
        asset.name = self.name
        
        return asset
    
    def continuous_shape(self, t):

        assert(self.shapes is not None)
        
        v = t*(len(self.shapes)-1)
        index = int(v)
        u = v - index
        
        if index == len(self.shapes)-1:
            index -= 1
            u = 1.

        mb = MeshBuilder.Copy(self)
        mb._verts[:] = self.shapes[index]*(1-u) + self.shapes[index + 1]*u
        
        asset = Asset().capture(mb)
        asset.name = self.name
        
        return asset

    # ====================================================================================================
    # Variations
    
    def variation(self, rng=None, f=None):
        
        if not self.has_variations:
            mb = MeshBuilder.Copy(self)
            
        else:
            if rng is None:
                rng = np.random.default_rng()
                
            if self.shapes is None:
                if f is None:
                    index = rng.choice(len(self.variants)+1)
                else:
                    index = round(f(rng.uniform(0, 1))*(len(self.variants)))
                    
                if index == 0:
                    mb = MeshBuilder.Copy(self)
                else:
                    mb = MeshBuilder.Copy(self.variants[index-1])
    
            else:
                mb = MeshBuilder.Copy(self)
                
                # Relative
                if self.relative:
                    t = rng.uniform(0, 1, len(self.shapes) - 1)
                    for i, w in enumerate(t):
                        mb._verts += w*(self.shapes[i + 1] - self.verts)
                        
                # Discreet
                elif self.discreet:
                    mb._verts[:] = self.shapes[rng.choice(len(self.shapes))]
                    
                # Continuous
                else:
                    index = rng.choice(len(self.shapes)-1)
                    t = rng.uniform(0, 1)
                    if f is not None:
                        t = f(t)
                    mb._verts[:] = self.shapes[index]*(1-t) + self.shapes[index + 1]*t
                
        asset = Asset().capture(mb)
        asset.name = self.name
        
        return asset

    @property
    def has_variations(self):
        return self.shapes is not None or self.variants is not None

    @property
    def discreet(self):
        return not (self.relative or self.continuous)
    
    @discreet.setter
    def discreet(self, value):
        if value or self.shapes is None:
            self.interpolation = Asset.DISCREET
        else:
            self.interpolation = Asset.RELATIVE
    
    @property
    def relative(self):
        return self.shapes is not None and self.interpolation == Asset.RELATIVE and len(self.shapes) > 2
    
    @relative.setter
    def relative(self, value):
        self.interpolation = Asset.RELATIVE if value else Asset.CONTINUOUS
    
    @property
    def continuous(self):
        return self.shapes is not None and self.interpolation == Asset.CONTINUOUS
    
    @continuous.setter
    def continuous(self, value):
        self.interpolation = Asset.CONTINUOUS if value else Asset.RELATIVE

    # ====================================================================================================
    # Size management
    
    @property
    def size(self):
        v_min = np.min(self.verts[:, 1:], axis=0)
        v_max = np.max(self.verts[:, 1:], axis=0)
        return tuple(v_max - v_min)
    
    @property
    def center(self):
        v_min = np.min(self.verts[:, 1:], axis=0)
        v_max = np.max(self.verts[:, 1:], axis=0)
        return (v_min + v_max)/2
    
    @property
    def back_rect(self):
        x_min = np.min(self.verts[:, 0])
        
        sel = self.verts[:, 0] < x_min + 0.005
        return np.min(self.verts[sel, 1:], axis=0), np.max(self.verts[sel, 1:], axis=0)
    
    @property
    def back_size(self):
        x_min = np.min(self.verts[:, 0])
        
        sel = self.verts[:, 0] < x_min + 0.005
        v_min = np.min(self.verts[sel, 1:], axis=0)
        v_max = np.max(self.verts[sel, 1:], axis=0)

        return tuple(v_max - v_min)

    @property
    def front_rect(self):
        x_max = np.max(self.verts[:, 0])
        
        sel = self.verts[:, 0] > x_max - 0.005
        return np.min(self.verts[sel, 1:], axis=0), np.max(self.verts[sel, 1:], axis=0)
    
        
    @property
    def front_size(self):
        x_max = np.max(self.verts[:, 0])
        
        sel = self.verts[:, 0] > x_max - 0.005
        v_min = np.min(self.verts[sel, 1:], axis=0)
        v_max = np.max(self.verts[sel, 1:], axis=0)

        return tuple(v_max - v_min)
    
    # ----------------------------------------------------------------------------------------------------
    # Change the size of a given delta
    
    def delta_resize(self, delta, center=None, bot=True, right=True, top=True, left=True):
        
        if left:
            if right:
                dleft  = delta[0]/2
                dright = delta[0]/2
            else:
                dleft  = delta[0]
                dright = 0
        else:
            dleft  = 0
            dright = delta[0]

        if bot:
            if top:
                dbot = delta[1]/2
                dtop = delta[1]/2
            else:
                dbot = delta[1]
                dtop = 0
        else:
            dbot = 0
            dtop = delta[1]
            
        if center is None:
            center = self.center
            
        C = np.array(center)
        if np.shape(C) == (2,):
            cy0, cy1, cz0, cz1 = C[0], C[0], C[1], C[1]
        else:
            cy0, cy1, cz0, cz1 = C[0, 0], C[1, 0], C[0, 1], C[1, 1]
            
        if dleft != 0:
            self.verts[self.verts[:, 1] < cy0, 1] -= dleft
        if dright != 0:
            self.verts[self.verts[:, 1] > cy1, 1] += dright
            
        if dbot != 0:
            self.verts[self.verts[:, 2] < cz0, 2] -= dbot
        if dtop != 0:
            self.verts[self.verts[:, 2] > cz1, 2] += dtop
            
    # ----------------------------------------------------------------------------------------------------
    # Change the size of a given delta
    
    def resize_to(self, size, center=None, bot=True, right=True, top=True, left=True):
        cur_size = self.size
        self.delta_resize((size[0] - cur_size[0], size[1] - cur_size[1]), center=center,
                          bot=bot, right=right, top=top, left=left)
        
    # ----------------------------------------------------------------------------------------------------
    # Adjust size for a shape left aligned
    
    def adjust_width(self, width):
        
        delta = self.size[0] - width
         
        bounds = self.bounds
        self.verts[self.verts[:, 1] < bounds[0][1] + .01, 1] += delta/2
        self.verts[self.verts[:, 1] > bounds[1][1] - .01, 1] -= delta/2
        self.verts[:, 1] -= delta/2
        
        
    # ====================================================================================================
    # Operations
    
    # ----------------------------------------------------------------------------------------------------
    # Array
    
    def array(self, count, offset=(1, 0), margin=(0, 0), keep_center=False):
        
        size = self.size
        if margin != (0, 0):
            self.delta_resize((-margin[0]/2, -margin[1]/2))
            
        mb = self.multiply(count, offset=(0, offset[0]*size[0], offset[1]*size[1]))
        self.capture(mb)
        
        if keep_center:
            new_size = self.size
            mb.verts[:, 1] -= (new_size[0] - size[0])/2
            mb.verts[:, 2] -= (new_size[1] - size[1])/2
            
    # ----------------------------------------------------------------------------------------------------
    # Symmetry
    
    def hrz_symmetry(self, center=0, append=False):
        if append:
            mb = Asset.Copy(self)
            mb.hrz_symmetry(center=center, append=False)
            self.append(mb)
            
        else:
            self.verts[:, 1] *= -1
            offsets = ArraySlicer(self.szmas).offsets
            for start, end in zip(offsets[:-1], offsets[1:]):
                self.faces[start:end] = np.flip(self.faces[start:end])
                
# =============================================================================================================================
# Assets

class Assets(dict):
    """ A dictionnary of lists of assets:
        
        key --> list of assets
    """
    
    # ========================================================================================================================
    # Save to file
    
    def save(self, file_path):
        
        arrays = Asset.new_arrays()
            
        names = []
        sizes = []
        for name, assets in self.items():
            names.append(name)
            sizes.append(len(assets))

            for asset in assets:
                asset.to_arrays(arrays)
        
        arrays['asset_names'] = QuickArray.FromArray(np.array(names))
        arrays['asset_sizes'] = QuickArray.FromArray(np.array(sizes))
        
        np.savez(file_path, **{name: qa.a for name, qa, in arrays.items()})

    # ========================================================================================================================
    # Load from file
        
    @classmethod
    def Load(cls, file_path):
        
        assets = cls()
        npz = np.load(file_path)
        
        arrays = {name: a for name, a in npz.items()}
        
        names = arrays['asset_names']
        sizes = arrays['asset_sizes']
        
        offset = 0
        for name, size in zip(names, sizes):
            assets[name] = [Asset.FromArrays(arrays, offset + i) for i in range(size)]
            offset += size

        return assets
    
    # ========================================================================================================================
    # Demo
    
    @classmethod
    def Demo(cls):
        assets = cls()
        
        assets["Cube"]   = [Asset.Cube(size=1), Asset.Cube(size=2), Asset.Cube(size=3)]
        for i, asset in enumerate(assets["Cube"]):
            asset.materials=[f"Cube {i}"]
        
        sph0 = MeshBuilder.UVSphere(1)
        sph1 = MeshBuilder.Copy(sph0)
        sph1._verts *= (.1, 1, 1)
        sph2 = MeshBuilder.Copy(sph0)
        sph2._verts *= (1, .1, 1)
        sph3 = MeshBuilder.Copy(sph0)
        sph3._verts *= (1, 1, .1)
        
        assets["Sphere"] = [
            Asset.Variants(*[
                MeshBuilder.IcoSphere(1, 1), 
                MeshBuilder.IcoSphere(1, 2), 
                MeshBuilder.IcoSphere(1, 3), 
                MeshBuilder.IcoSphere(1, 4),
                ]),
            Asset.Deform(sph0, sph1, sph2, sph3),
            ]
        assets["Things"] = [Asset.Monkey(), Asset.Cone(), Asset.Cylinder()]
        
        return assets
    

    # ========================================================================================================================
    # Methods
        
    def __str__(self):
        s = f"<Assets, key:; {len(self.keys())}, total assets: {self.total_assets}):"
        for k, v in self.items():
            items = [f"{str(asset)}" for asset in v]
            s += f"\n {k}:\n   " + "\n   ".join(items)
        return s + "\n>"
    
    @property
    def total_assets(self):
        count = 0
        for v in self.values():
            count += len(v)
        return count
        
    def add_assets(self, key, *assets):
        cur = self.get(key, [])
        cur.extend(assets)
        self[key] = cur
        return self
        
    def add_collection(self, key, collection):
        self.add_assets(key, *[Asset(obj) for obj in blender.get_collection(collection).objects])
        return self
    
    def key_weights(self, key):
        weights = [asset.weight for asset in self[key]]
        total = sum(weights)
        return np.array(weights)/total
        
    def random_asset(self, key, rng=None):
        
        if rng is None:
            rng = np.random.default_rng()
            
        assets = self.get(key, [])
        if len(assets):
            return assets[rng.choice(len(assets), p=self.key_weights(key))]
        else:
            return None
        
    def random_selection(self, keys=None, rng=None):
        
        if rng is None:
            rng = np.random.default_rng()
            
        if keys is None:
            keys = list(self.keys())
            
        single = isinstance(keys, str)
        if single:
            keys = [keys]
            
        builders = {}
        for key in keys:
            asset = self.random_asset(key, rng)
            builders[key] = asset.variation(rng)
                
        if single:
            return builders[keys[0]]
        else:
            return builders
        
    # ========================================================================================================================
    # To Objects
    
    def to_objects(self, name="Dump", delta=5):
        print(f"Dumping Assets {name}:")
        print(self)
        print()
        
        x = 0
        for key, assets in self.items():
            y = 0
            for i, asset in enumerate(assets):
                o_name = f"{name} {key} {i}"
                obj = asset.to_object(o_name)
                obj.location = (x, y, 0)
                y += delta
                
            x += delta
                

                
                
                
                
                