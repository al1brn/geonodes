#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:15:55 2023

@author: alain
"""

import numpy as np

from geopy.core.meshbuilder import MeshBuilder
from geopy.houses import constants
from geopy.houses.asset import Asset, Assets

REMOVE_DOUBLES = False
  
# =============================================================================================================================
# Build a window

class HouseBuilder:
    
    def __init__(self, components, rng=None, **kwargs):
        
        # Any change in the use of rng won't impact the generation sequence
        seed = None if rng is None else rng.integers(1<<63)
        self.rng = np.random.default_rng(seed)
        
        self.components = components
        self.assets     = components.random_selection(rng=self.rng)
        self.store_type = self.rng.choice(constants.STORE_TYPES)
        self.win_top    = kwargs.get('win_top', 2.15)
        self.win_margin = kwargs.get('win_margin', .4)
        
        self.build_assets = Assets()

        for i in range(3):
            n, hs = self.win_dims
            self.build_assets.add_assets('window', self.window(hole_size=hs, panels_count=n))

        n, hs = self.bay_dims
        self.build_assets.add_assets('bay', self.bay(width=hs[0], panels_count=n))

        n, hs = self.door_dims
        self.build_assets.add_assets('door', self.door(width=hs[0], panels_count=n))

        
    @property
    def win_dims(self):
        dims = constants.WIN_DIMS
        dim  = dims[self.rng.choice(len(dims))]
        return dim[0], (dim[2], dim[1])
    
    @property
    def bay_dims(self):
        dims = constants.BAY_DIMS
        dim  = dims[self.rng.choice(len(dims))]
        return dim[0], (dim[2], dim[1])
    
    @property
    def door_dims(self):
        dims = constants.DOOR_DIMS
        dim  = dims[self.rng.choice(len(dims))]
        return dim[0], (dim[2], dim[1])
        
    # ----------------------------------------------------------------------------------------------------
    # Build window stores
        
    def stores(self, hole_size, store_type, left=True, right=False, closed=False):
        
        # ----- Internal store
        
        if store_type == constants.STORE_INTERNAL:
            
            stores = MeshBuilder(materials=["StoreInt"])

            stores.external   = False
            stores.left_size  = 0
            stores.right_size = 0
            
            x = -.05
            y  = hole_size[0]/2
            z1 = hole_size[1]/2
            z0 = -hole_size[1]/2 if closed else z1 - 0.07

            stores.add_surface(( (x, -y, z0), (x, y, z0), (x, y, z1), (x, -y, z1)), UVMap=((-y, -z1),(y, -z1),(y, z1),(-y, z1)))

            return stores

        # ----- External store
        
        else:
            
            stores = MeshBuilder(materials=["StoreExt"])

            count = 2 if left and right else 1

            stores.external = True
            height = hole_size[1] - 0.02
            
            if count == 1:
                width = hole_size[0] - 0.03

                one_store = MeshBuilder.Cube(size=1)
                one_store._verts[:, 0] *= .03
                one_store._verts[:, 1] *= width
                one_store._verts[:, 2] *= height
                
                if left:
                    stores.left_size   = hole_size[0]
                    stores.right_size  = 0
                    one_store._verts[:, 1] -= hole_size[0] + 0.07
                else:
                    stores.left_size  = 0
                    stores.right_size = hole_size[0]
                    one_store._verts[:, 1] += hole_size[0] + 0.07

                stores.append(one_store)

            else:
                width = hole_size[0]/2 - 0.01

                stores.left_size  = hole_size[0]/2
                stores.right_size = hole_size[0]/2

                one_store = MeshBuilder.Cube(size=1)
                one_store._verts[:, 0] *= .03
                one_store._verts[:, 1] *= width
                one_store._verts[:, 2] *= height
                
                if closed:
                    one_store._verts[:, 0] -= .01
                    dy = 0.25*hole_size[0]
                else:
                    one_store._verts[:, 0] += .04
                    dy = 0.75*hole_size[0] + 0.07
                    
                one_store._verts[:, 1] -= dy
                stores.append(one_store)

                one_store._verts[:, 1] += 2*dy
                stores.append(one_store)
                
            return stores

    def stores_OLD(self, hole_size, store_asset, left=True, right=False, closed=False):
        
        stores = Asset.Copy(store_asset)
        stores.left_size  = 0
        stores.right_size = 0
        stores.external   = "EXT" in stores.name.split(" ")
        
        # ---------------------------------------------------------------------------
        # External stores
        
        if stores.external:
            
            count = 2 if left and right else 1
            stores.resize_to((hole_size[0]/count - .01, hole_size[1] - .02), right=False)
            
            if count == 2:
                stores.left_size  = hole_size[0]/2
                stores.right_size = hole_size[0]/2
            elif left:
                stores.left_size  = hole_size[0]
            else:
                stores.right_size = hole_size[0]
            
            if closed:
                # Rotate 180°
                stores.verts[:, :2] *= (-1, -1)
                
                # Little right shift
                stores.verts[:, :2] += (.01, -hole_size[0]/2 + .005)
            
            else:
                # Left and front shift
                stores.verts[:, :2] += (.05, -hole_size[0]/2 - .07)
                
            if right:
                stores.hrz_symmetry(append = count==2)
                
        # ---------------------------------------------------------------------------
        # Internal stores
        
        else:
            stores.resize_to((hole_size[0], hole_size[1]))
            z = hole_size[1] if closed else .07
            stores.delta_resize((0, - hole_size[1] + z), top=False)
            
        return stores
    
    # ----------------------------------------------------------------------------------------------------
    # Build an opening
        
    def opening(self, hole_size, frame_in, panel_asset, frame_out, store_type,
                  is_door=False, panels_count=1, store_left=True, store_closed=False):
        
        # ---------------------------------------------------------------------------
        # Adjust parameter
        
        width  = hole_size[0]
        height = self.win_top if is_door else hole_size[1]
        hole_size = (width, height)
        
        # ---------------------------------------------------------------------------
        # Resize the frame in
        
        opening = Asset.Copy(frame_in)
        opening.resize_to(hole_size)
        
        # ---------------------------------------------------------------------------
        # Store

        window_is_visible = True
        if store_type is None:
            stores       = None
            store_left   = 0
            store_right  = 0
            
        else:
            stores = self.stores(hole_size, store_type,
                            left   = panels_count>=2 or store_left, 
                            right  = panels_count>=2 or (not store_left),
                            closed = store_closed)
            if is_door:
                stores.verts[:, 2] += height/2

            opening.append(stores)
            
            store_left  = stores.left_size
            store_right = stores.right_size
            
            window_is_visible = not store_closed and stores.external
            
            opening.external_stores = stores.external

        # ---------------------------------------------------------------------------
        # Build panels inside
        
        #print("window_is_visible", window_is_visible, "" if stores is None else stores.external)
        window_is_visible = True
        
        if window_is_visible:
        
            # Inner size is given by the back most vertices
            
            panels_size = opening.back_size
            panels = Asset.Copy(panel_asset)
            panels.resize_to((panels_size[0]/panels_count, panels_size[1]))
            if panels_count > 1:
                panels.array(panels_count, offset=(1, 0), margin=(.01, 0), keep_center=True)
            
            # Merge within the frame in
            
            panels.verts[:, 0] += opening.bounds[0][0]
    
            opening.append(panels)

        # ---------------------------------------------------------------------------
        # Add a frame out
        
        if frame_out is not None:
            
            frout = Asset.Copy(frame_out)
            
            # Resize such as the back size fits the size of the hole
            
            back_size = frout.back_size
            frout.delta_resize((hole_size[0] - back_size[0], hole_size[1] - back_size[1]))
            
            # Adjust the back most vertices which are set x neg for computation
            frout.verts[frout.verts[:, 0] < 0, 0] = 0
            
            # Merge
            opening.append(frout)

        # ---------------------------------------------------------------------------
        # The piece of wall around the opening
        
        if height < self.win_top:

            opening.verts[:, 2] += self.win_top - hole_size[1]/2
            
            yw, ym = hole_size[0]/2, hole_size[0]/2 + self.win_margin
            z0, z1, zw = 0, self.win_top, self.win_top - hole_size[1]
            yl, yr = -ym - store_left, ym + store_right
            
            opening.append(Asset.Wall([
                (yl, z0), (yr, z0), (yr, z1), (yw, z1), (yw, zw), (-yw, zw), (-yw, z1), (yl, z1)
                ]))
            
            # Left align
            opening.verts[:, 1] -= yl
            
        else:
            yw, ym = width/2, width/2 + self.win_margin
            z0, z1 = 0, self.win_top
            yl, yr = -ym - store_left, ym + store_right
            
            opening.append(Asset.Wall([
                (yl, z0), (-yw, z0), (-yw, z1), (yl, z1)
                ]))
            opening.append(Asset.Wall([
                (yw, z0), (yr, z0), (yr, z1), (yw, z1)
                ]))

            # Left align
            opening.verts[:, 1] -= yl
            
        if REMOVE_DOUBLES:
            opening.remove_doubles(.001)
            
        return opening        
    
    # ----------------------------------------------------------------------------------------------------
    # Build a window with stores
        
    def window(self, hole_size=(1, 1.15), panels_count=2, store_left=True):
        
        frame_in  = self.assets['frame_in']
        panel     = self.assets['panel']
        frame_out = self.assets['frame_out']
        #store     = self.assets['store']
        
        open_stores = self.opening(hole_size, frame_in, panel, frame_out, self.store_type,
                        is_door         = False, 
                        panels_count    = panels_count, 
                        store_left      = store_left, 
                        store_closed    = False,
                        )

        closed_stores = self.opening(hole_size, frame_in, panel, frame_out, self.store_type,
                        is_door         = False, 
                        panels_count    = panels_count, 
                        store_left      = store_left, 
                        store_closed    = True,
                        )
        
        return Asset.Variants(open_stores, closed_stores) if open_stores.external_stores else Asset.Deform(open_stores, closed_stores)
    
    # ----------------------------------------------------------------------------------------------------
    # Build a door
    
    def door(self, width=1.1, panels_count=1):
        
        return self.opening((width, self.win_top), self.assets['door_in'], self.assets['door'], None, None,
                        is_door         = True, 
                        panels_count    = panels_count,
                        )
        
    # ----------------------------------------------------------------------------------------------------
    # Build a bay
    
    def bay(self, width=1.8, panels_count=2, store_left=True):

        frame_in  = self.assets['door_in']
        panel     = self.assets['bay_panel']
        #store     = self.assets['store']
        
        open_stores = self.opening((width, self.win_top), frame_in, panel, None, self.store_type,
                        is_door         = True, 
                        panels_count    = panels_count,
                        store_left      = store_left, 
                        store_closed    = False,
                        )
        closed_stores = self.opening((width, self.win_top), frame_in, panel, None, self.store_type,
                        is_door         = True, 
                        panels_count    = panels_count,
                        store_left      = store_left, 
                        store_closed    = True,
                        )
        
        return Asset.Variants(open_stores, closed_stores) if open_stores.external_stores else Asset.Deform(open_stores, closed_stores)
    
    # ----------------------------------------------------------------------------------------------------
    # Balcony
    
    def balcony(self, dims):
        balc = Asset(self.assets['balcony'])
        
        width = dims[1] - dims[0]
        
        balc.resize_to((width, balc.size[1]))
        balc.verts[:, 1] += dims[0] + width/2

        return balc
    
    # ----------------------------------------------------------------------------------------------------
    # A shop
    
    def shop(self, hole_size):
        shop = self.components.random_asset('shop', self.rng).variation(self.rng)
        
        # Back size gives the margin for resize
        shop.resize_to(hole_size, center=shop.back_rect, bot=False)
        
        # Left align
        shop.verts[:, 1] += hole_size[0]/2

        return shop
    
    # ====================================================================================================
    # Random pattern
    
    @staticmethod
    def random_pattern(length, rng, door=False, bay=True, garage=False, shop=False, once=["D", "G"]):
        
        items = ["W", "W"]
        if door:
            items.append("D")
        if bay:
            items.append("B")
        if garage:
            #items.append("G")
            items.append("S")
        if shop:
            items.append("S")

        pattern = ""
        while len(pattern) < length:
            c = rng.choice(items)
            if c in once and c in pattern:
                continue
            pattern += c
            
        return pattern

    # ====================================================================================================
    # Build a storey
    
    def storey(self, width, height, level=0, pattern='WBWD', symmetry=False):
        
        if width < 1.5:
            return Asset.Wall([(0, 0), (width, 0), (width, height), (0, height)])            
        
        # ------------------------------------------------------------
        # Balcony pattern if not level 0

        balc_pattern = [False]*len(pattern)
        if level > 0:
            for i, P in enumerate(pattern):
                if P == 'B':
                    balc_pattern[i] = True

                    for j in reversed(range(i)):
                        if self.rng.uniform(0, 1) < .5:
                            break
                        balc_pattern[j] = True

                    for j in range(i+1, len(pattern)):
                        if self.rng.uniform(0, 1) < .5:
                            break
                        balc_pattern[j] = True
                        
        # ------------------------------------------------------------
        # List of openings according to the pattern
        
            
        # Let's go
        
        balconies    = []
        balc_cur     = None
        items        = []
        right_items  = []
        w            = 0
        target_width = width/2 if symmetry and width > 20 else width
        item_widths  = [] # Let's compute the widths once
        
        for wd in range(100):
            done = False
            
            for P, ok_balc in zip(pattern, balc_pattern):
                
                # A shop
                if P == 'S':
                    hole_size = min(target_width - w - 2*self.win_margin, 6), height-.2
                    shop = self.shop(hole_size)
                    items.append(shop)
                    item_widths.append(shop.size[0])
                    
                    if symmetry:
                        right_items.append(self.shop(hole_size))
                    
                # A standard opening
                else:
                    key = {'W': 'window', 'B': 'bay', 'D': 'door'}[P]
                    opening = self.build_assets.random_asset(key=key, rng=self.rng)
                    #opening = self.build_assets.random_asset(key=key, rng=self.rng).variation(rng=self.rng, f=lambda t: t**2)
                    items.append(opening.variation(rng=self.rng, f=lambda t: t**2))
                    item_widths.append(opening.size[0])
                    
                    if symmetry:
                        right_items.append(opening.variation(rng=self.rng, f=lambda t: t**2))
                
                # Balcony
                if ok_balc:
                    if balc_cur is None:
                        balc_cur = [w, None]
                elif balc_cur is not None:
                    balc_cur[1] = w
                    balconies.append(balc_cur)
                    balc_cur = None
                
                # Done or not
                w += item_widths[-1]
                if w >= target_width - 2*self.win_margin:
                    done = True
                    break
            if done:
                break
            
        # ------------------------------------------------------------
        # Stick the items along y axis

        # Small width, let's stay simple
        if len(items) == 1:
            delta = (target_width - w)/2 # For balconies
            
            if delta > 3*self.win_margin:
                storey = Asset.Wall([(0, 0), (width, 0), (width, height), (0, height)])
            else:
                storey = items[0]
                storey.adjust_width(width)
                
        # At least 2 openings
        else:
            
            # ----- Stick the items
            
            # Left items
            w = 0.
            storey = Asset()
            for item, item_width in zip(items[:-1], item_widths[:-1]):
                item.verts[:, 1] += w
                storey.append(item)
                w += item_width
                
            delta = (target_width - w)/2 # For balconies

            storey.adjust_width(target_width)
            
            # Right items (with different stores)
            if symmetry:
                right_storey = Asset()
                w = 0.
                for item, item_width in zip(reversed(right_items[:-1]), reversed(item_widths[:-1])):
                    item.verts[:, 1] -= w
                    right_storey.append(item)
                    w -= item_width
                
                right_storey.adjust_width(target_width)
                right_storey.verts[:, 1] += target_width
                storey.append(right_storey)
                    
            # ----- Balconies
            
            if balc_cur is not None and target_width > balc_cur[0] + 1.2:
                balc_cur[1] = target_width
                balconies.append(balc_cur)
                
            balc_asset = Asset()
            for dim in balconies:
                sh_dim = dim[0] + delta, min(dim[1] + delta, target_width - self.win_margin/2)
                if sh_dim[1] > sh_dim[0] + 1.2:
                    balc_asset.append(self.balcony(sh_dim))
                    
            if symmetry:
                copy = Asset(balc_asset)
                copy.hrz_symmetry(append=False)
                copy.verts[:, 1] += 2*target_width
                balc_asset.append(copy)
                
            # ----- Fence uvmap
            
            balc_asset.unwrap_vertical_faces(face_indices=balc_asset.faces_by_mat(mat=balc_asset.material("BalcFence")))
  

            storey.append(balc_asset)
                    
                    
        # ------------------------------------------------------------
        # Top piece of wall
        
        z0 = self.win_top
        z1 = height
        y0 = 0
        y1 = width
        
        storey.append(Asset.Wall([(y0, z0), (y1, z0), (y1, z1), (y0, z1)]))
        
        # ------------------------------------------------------------
        # Done
        
        if REMOVE_DOUBLES:
            opening.remove_doubles(.001)
            
        return storey
    
    # ====================================================================================================
    # Build a facade
    
    def facade(self, width, storeys, start_level=0, symmetry=False):
        
        facade = Asset()
        
        level = start_level
        z     = 0.
        for storey_spec in storeys:
            
            if isinstance(storey_spec, str):
                spec = {'pattern': storey_spec}
            else:
                spec = storey_spec
                
            height = spec.get('height', 3.8 if level == 0 else 3)
            for _ in range(spec.get('count', 1)):
                storey = self.storey(
                    width    = width,
                    height   = height,
                    level    = level,
                    pattern  = spec['pattern'],
                    symmetry = symmetry,
                    )
                storey.verts[:, 2] += z
                facade.append(storey)
                
                level += 1
                z     += height
                
        # ----- Build uv for wall faces
        
        imat = facade.material("Wall")
        facade.uvmap() # Make sure UVMap exists
        
        facade.unwrap_in_plane(facade.faces[:, 1]==imat, plane='YZ', offset=(0, 0))
        
        # Done
        
        if False and REMOVE_DOUBLES:
            facade.remove_doubles(.001)
        
        return facade
    
    
    
    
    
    
            
        
        
        
        
    
            
