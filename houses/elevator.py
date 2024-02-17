#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 09:25:53 2023

@author: alain
"""

import numpy as np

from geopy.core import geo2D
from geopy.core.quickappend import QuickArray
from geopy.core.meshbuilder import MeshBuilder, Meshes

from geopy.houses.constants import *
from geopy.houses.houseblocks import Surface, Surfaces
from geopy.houses.roofbuilder import Profile, Roof
from geopy.houses.house_builder import HouseBuilder

# ====================================================================================================
# A wall

class Wall:
    def __init__(self, p0, p1, cover, wall_index, other_cover=None, other_wall=None, face_seed=0.):
        
        v = p1 - p0
        self.length = geo2D.length(p0, p1)
        u = v/self.length
        
        perp = np.array((u[1], -u[0], 0))
        self.location = np.array(p0)
        self.angle    = geo2D.segment_angle(p0, p1)
        
        self.external = other_cover is None
        
        if self.external:
            self.cover0, self.wall0, self.level0, self.height0  = None, None, 0, 0.
            self.cover1, self.wall1, self.level1, self.height1  = cover, wall_index, cover.level, cover.height
            self.verts = np.array([p0, p1, p1 + (0, 0, self.height1), p0 + (0, 0, self.height1)])
            self.normal = perp
            
        else:
            assert(cover.level != other_cover.level)
            
            if cover.level > other_cover.level:
                self.cover0, self.wall0, self.level0, self.height0  = other_cover, other_wall, other_cover.level, other_cover.height
                self.cover1, self.wall1, self.level1, self.height1  = cover, wall_index, cover.level, cover.height

                self.verts = np.array([p0 + (0, 0, self.height0), p1 + (0, 0, self.height0), p1 + (0, 0, self.height1), p0 + (0, 0, self.height1)])
                self.normal = perp

            else:
                self.cover0, self.wall0, self.level0, self.height0  = cover, wall_index, cover.level, cover.height
                self.cover1, self.wall1, self.level1, self.height1  = other_cover, other_wall, other_cover.level, other_cover.height

                self.verts = np.array([p1 + (0, 0, self.height0), p0 + (0, 0, self.height0), p0 + (0, 0, self.height1), p1 + (0, 0, self.height1)])
                self.normal = -perp
                
        self.house_seed = self.cover1.house_seed
        self.face_seed  = face_seed
        
        
        self.normal = perp
                
        self.angle   = np.arctan2(v[1], v[0])
                
        self.floor0  = self.external
        self.door    = False
        self.shop    = False
        self.garage  = False
        
    # ====================================================================================================
    # On a terrace
    
    @property
    def terrace(self):
        if self.external:
            return False
        return self.cover0.cover_type == 'TERRACE'

    # ====================================================================================================
    # Build
        
    def build(self, mb):
        uvs = np.array(( (0, self.height0), (self.length, self.height0), (self.length, self.height1), (0, self.height1)) )
        mb.add_surface(self.verts, mat=WALL, UVMap=uvs)
        
    # ====================================================================================================
    # To arrays
    
    def to_arrays(self):
        
        height  = self.cover1.params['storey_height']
        height0 = self.cover1.params['storey0_height'] if self.level0 == 0 else height
        
        a = np.zeros((4, 3), float)
        
        a[0]    = self.location + (0, 0, self.height0)
        a[1]    = self.normal
        
        a[2, 0] = self.length
        a[2, 1] = self.angle
        a[2, 2] = self.height1 - self.height0
        
        a[3, 0] = self.house_seed
        a[3, 1] = self.face_seed
        a[3, 2] = height*100 + height0*10000
        
        options  = WALL_FLOOR0  if self.floor0  else 0
        options |= WALL_DOOR    if self.door    else 0
        options |= WALL_TERRACE if self.terrace else 0
        options |= WALL_SHOP    if self.shop    else 0
        options |= WALL_GARAGE  if self.garage  else 0
        
        return a, options
    
    # ====================================================================================================
    # Build
    
    # ----------------------------------------------------------------------------------------------------
    # Simple facade
    
    def simple_facade(self):
        mb = MeshBuilder()
        dz = -2 if self.external else 0
        uvs = np.array(( (0, self.height0 + dz), (self.length, self.height0 + dz), (self.length, self.height1), (0, self.height1)) )
        mb.add_surface(self.verts + [(0, 0, dz), (0, 0, dz), (0, 0, 0), (0, 0, 0)], mat=WALL, UVMap=uvs)
        return mb

    # ----------------------------------------------------------------------------------------------------
    # Detailed facade
        
    def facade(self, hbuild, elevator):
        
        height  = self.cover1.params['storey_height']
        height0 = self.cover1.params['storey0_height'] if self.level0 == 0 else height
        
        pat0 = None
        if self.floor0:
            pat0 = hbuild.random_pattern(7, elevator.rng, door=self.door, bay=True, garage=self.garage, shop=self.shop)
        elif self.terrace:
            pat0 = hbuild.random_pattern(7, elevator.rng, door=False, bay=True)
        
        storeys = []
        if pat0 is not None:
            storeys = [{'count': 1, 'height': height0, 'pattern': pat0}]
            
        levels = self.level1 - self.level0 - len(storeys)
        if levels > 1:
            storeys.append({'count': levels, 'height': height, 'pattern': hbuild.random_pattern(5, elevator.rng)})
            
        facade = hbuild.facade(self.length, storeys, symmetry=elevator.rng.uniform(0, 1) > 1.8)
        if self.floor0:
            facade.add_surface([(0, 0, -2), (0, self.length, -2), (0, self.length, 0), (0, 0, 0)], mat=facade.material("Underground"))
        
        angle = self.angle - np.pi/2
        M = np.array(( (np.cos(angle), np.sin(angle), 0), (-np.sin(angle), np.cos(angle), 0), (0, 0, 1) ))
        facade._verts = self.location + np.einsum('...ij, ...i', M, facade.verts)
        
        facade.new_face_attribute("face_seed", 'FLOAT', value=elevator.rng.uniform(0, 1))
        
        return facade
    
    
# ----------------------------------------------------------------------------------------------------
# Roof surrounded by walls and other roofs

class Cover(Surface):
    def __init__(self, elevator, surface, level, params, house_seed):
        """ A cover is a roof, or a terrace coverinf a surface.
        """
        
        super().__init__(surface.index, surface.verts, surface.shared)
        
        self.elevator = elevator
        self.house_seed = house_seed
        
        # Rectangular contour
        walls = self.get_full_walls()
        
        self.rect_verts   = walls['verts']
        self.rect_inds    = walls['indices']
        self.rect_lengths = geo2D.lengths(self.rect_verts)
        self.i_length     = np.argmax(self.rect_lengths)
        self.length       = self.rect_lengths[self.i_length]
        self.width        = self.rect_lengths[(self.i_length + 1)%len(self.rect_lengths)]
        
        # Level, height and area
        self.level   = level
        self.height  = params['storey0_height'] + (level-1)*params['storey0_height']
        self.params  = params

        # Arrange : relationship with peer covers
        self.arranged   = False
        self.extensions = []
        
        # Built or not
        self.cover_type = None
        self.built      = False
        
        
    def __str__(self):
        return f"<Roof]>"
    
    # ====================================================================================================
    # A random roof profile
    
    def gen_roof_profile(self, width, count=None):
        
        if count is None:
            count = self.elevator.rng.choice([2, 3, 4, 5], p=[.5, .3, .1, .1])
        
        constructor = Profile.Circular if self.elevator.rng.uniform(0, 1) < .8 else Profile.CircularInverse
        
        height = self.elevator.rng.uniform(.5, 2.5)
        if height/width > 1: height = width

        return constructor(
                width  = width,
                height = self.elevator.rng.uniform(.5, 2.5),
                count  = count,
                exp    = self.elevator.rng.uniform(1, 1.3),
                )
    
    # ====================================================================================================
    # Arrange the cover
    
    def arrange(self, main_cover=None):
        
        if self.arranged:
            return
        
        self.arranged = True
        
        # ====================================================================================================
        # We create the external walls
        
        for i_seg, v0 in enumerate(self.verts):
            v1 = self.verts[(i_seg + 1)%len(self.verts)]

            if self.shared[i_seg] < 0:
                self.elevator.add_wall(Wall(v0, v1, self, i_seg, face_seed=self.elevator.rng.uniform(0, 1)))
                
            else:
                other_cover = self.elevator[self.shared[i_seg]]
                if other_cover.level < self.level:
                    other_wall = self.elevator.get_shared_wall_index(self.index, i_seg)
                    self.elevator.add_wall(Wall(v0, v1, self, i_seg, other_cover, other_wall, face_seed=self.elevator.rng.uniform(0, 1)))
                

        # ====================================================================================================
        # Arrange
        
        # ----------------------------------------------------------------------------------------------------
        # L shape house (NOT IMPLEMENTED YET)
        
        if False:
            lshape = self.elevator.L_shape()
        else:
            lshape = None
            
        if lshape is not None:
            for cover in self.elevator:
                cover.arranged = True
                cover.level    = self.level
                cover.height   = self.height
                
            self.cover_type   = 'ROOF'
            
            roof = Roof()
            
            verts   = lshape['verts']
            lengths = lshape['lengths']
            if lshape['width_indices'][0] == 1:
                
                self.roof_profile = self.gen_roof_profile(lengths[5]/2, count=2)
                
                prof0 = self.roof_profile
                prof1 = prof0.change_width(lengths[2]/2)
                
                roof.add_pane( verts[0], verts[1], prof0)
                roof.add_pane( verts[1], verts[2], prof1)
                roof.add_gable(verts[2], verts[3])
                roof.add_pane( verts[3], verts[4], prof1)
                roof.add_pane( verts[4], verts[5], prof0)
                roof.add_gable(verts[5], verts[0])
                
            else:
                self.roof_profile = self.gen_roof_profile(lengths[1]/2)
                prof = self.roof_profile
                
                roof.add_pane( verts[0], verts[1], prof)
                roof.add_gable(verts[1], verts[2])
                roof.add_pane( verts[2], verts[3], prof)
                roof.add_pane( verts[3], verts[4], prof.change_width(lengths[4]/2))
                roof.add_gable(verts[4], verts[5])
                roof.add_pane( verts[5], verts[0], prof.change_width(lengths[4]/2))
                
            roof.connect_sides()
                
            self.l_roof = roof
            
            return
            
        # ----------------------------------------------------------------------------------------------------
        # Other shape
        
        if main_cover is None:
        
            # ----- Cover type
            
            if self.height > 25:
                self.cover_type = 'FLAT'
                
            elif self.area < 10:
                self.cover_type = 'TERRACE'
                
            else:
                self.cover_type = self.elevator.rng.choice(['FLAT', 'TERRACE', 'ROOF'], p=(.1, .2, .7))
                
            # BUG :-(
            if self.cover_type == 'ROOF' and len(self.verts) > 4:
                self.cover_type = 'FLAT'
                
            param_type = self.params.get('cover_type', None)
            if param_type is not None:
                self.cover_type = param_type
                

            # DEBUG            
            #self.cover_type = 'FLAT'
                
            self.hangover  = self.elevator.rng.integers(20, 45)/100
            self.thickness = self.elevator.rng.integers(15, 40)/100
    
            # Roof profile
            if self.cover_type == 'ROOF':
                self.roof_profile = self.gen_roof_profile(self.width/2)
                
            
        # ----- Neigbours covers
        for i_seg, shared in enumerate(self.shared):
            
            if shared < 0:
                continue
            
            # Same level, smaller and not already arranged            
            other = self.elevator[shared]
            if other.level != self.level or other.arranged or other.area > self.area:
                continue
            
            # Register the cover in the extensions
            if main_cover is None:
                self.extensions.append(other)
                other.arrange(main_cover=self)
                
            else:
                main_cover.extensions.append(other)
                other.arrange(main_cover=main_cover)
                
                
    # ====================================================================================================
    # Arrange the cover
            
    def build(self):
                    
        # ----- The cover

        if self.built:
            return
        
        self.built = True
        
        # ----------------------------------------------------------------------------------------------------
        # Flat or Terrace
        
        mb = MeshBuilder()
        
        if self.cover_type in ['FLAT', 'TERRACE']:
            self.flat_roof(mb, terrace=self.cover_type == 'TERRACE')
            
        elif self.cover_type == 'ROOF':
            self.roof(mb)

        mb.new_face_attribute("face_seed", 'FLOAT', self.elevator.rng.uniform(0, 1, mb.faces_count))
        
        return mb
            
        
    # =============================================================================================================================
    # Roof builders
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Flat roof
    
    def flat_roof(self, mb, terrace=True):
        
        # The contours with the extensions
        sinds = [self.index] + [cover.index for cover in self.extensions]
        contours = self.elevator.get_contours(sinds)
        
        for contour in contours:
            verts = [seg["v0"] for seg in contour]
            
            if len(verts) < 4:
                continue
            
            ext = geo2D.inset(verts, -self.hangover)
            
            i_roof = mb.add_surface(np.array(ext) + (0, 0, self.height), mat=FLAT_ROOF)
            mb.extrude(mb.get_face_ring(i_roof), height=self.thickness, top_mat=FLAT_ROOF, mat=ROOF_BORDER)
            
        # ----- The fence where necessary
        
        if terrace:
            contours = Surfaces.inset_contours(contours, .3)
            for contour in contours:
                for i_seg, seg in enumerate(contour):
                    if seg["shared"] < 0 or self.elevator[seg["shared"]].height < self.height:
                        v0 = seg["v0"] + (0, 0, self.height)
                        v1 = seg["v1"] + (0, 0, self.height)
                        mb.add_surface([v0, v1, v1 + (0, 0, 1), v0 + (0, 0, 1)])
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Roof
    
    def roof(self, mb):
        
        if hasattr(self, 'l_roof'):
            self.l_roof.to_builder(mb, height=self.height)
            return
        
        # The contours with the extensions
        sinds = [self.index] + [cover.index for cover in self.extensions]
        contours = self.elevator.get_contours(sinds)
        
        # Normally one single contour, but you never know        
        for i, contour in enumerate(contours):
            verts = [seg["v0"] for seg in contour]
            roof  = Roof.CoverContour(verts, self.roof_profile)
            roof.to_builder(mb, self.height)
            
# ====================================================================================================
# Elevator : walls and roofs

class Elevator(Surfaces):
    def __init__(self, index, is_house, rng=None):
        
        super().__init__(index, is_house=is_house)
        
        # ----- Random generator
        
        if rng is None:
            self.rng = np.random.default_rng(index)
        else:
            self.rng = rng
        
        # ----- Walls
        
        self.walls = []
        
        # ----- Mesh builder
        #self.mb    = MeshBuilder(materials=HOUSE_MATERIALS)
        
    def __str__(self):
        return f"<Elevator,  surfaces: {len(self)}, walls: {len(self.walls)}>"
    
    # ====================================================================================================
    # House params
    
    def gen_house_params(self, area):
        
        params = {
            'storey_height': self.rng.integers(280, 320)/100,
            'roof_height'  : np.round(self.rng.normal(200, 70))/100,
            'tiny'         : area < 15,
            }
        
        params['storey0_height'] = params['storey_height'] + self.rng.integers(0, 150)/100
        
        # ----- Small area
        if area < 30:
            params['levels'] = 1
        
        # ----- Standard house
        elif area < 200:
            params['levels'] = self.rng.choice([1, 2, 3], p=(.4, .5, .1))
            
        # ----- Special
        else:
            p = [10, 15, 25, 20, 15, 19, 5]
            params['levels'] = self.rng.choice([1, 2, 3, 4, 6, 7, 8], p=np.array(p, float)/np.sum(p))
            
        return params
    
    # ====================================================================================================
    # Register a new wall
    
    def add_wall(self, wall):
        self.walls.append(wall)
        
    # ====================================================================================================
    # Walls to arrays
    
    def walls_to_arrays(self, arrays=None):
        
        if arrays is None:
            arrays = {
                'locs':    QuickArray((0, 4, 3), float),
                'options': QuickArray((0, 2), int),
                }
            
        for wall in self.walls:
            a, o  = wall.to_arrays()
            arrays['locs'].append(a)
            arrays['options'].append((o, self.index))
        
        return arrays
        
# ====================================================================================================
# House elevator

class HouseElevator(Elevator):
    
    def __init__(self, house, index, rng=None):
        
        super().__init__(index, is_house=True, rng=rng)
        
        self.house_seed = self.rng.uniform(0, 1)
        
        # ----- Height of the storeys
        
        areas  = [surf.area for surf in house]
        
        
        params = self.gen_house_params(area=sum(areas))
        
        self.storey_height  = params['storey_height']
        self.storey0_height = params['storey0_height']
        
        # ----- Roof 
        
        self.roof_height = params['roof_height']
        
        # ----------------------------------------------------------------------------------------------------
        # House is not composed and is not a rectangle
        
        if len(house) == 1 and len(house[0].verts) > 4:
            
            surface = house[0]
            area = areas[0]
            
            # ----- Small area
            if area < 15:
                return
            
            # ----- Little one storey house
            elif area < 30:
                level = 1
                
            # ----- Standard house
            elif area < 200:
                level = self.rng.choice([1, 2, 3], p=(.4, .5, .1))
                
            # ----- Special
            else:
                p = [10, 15, 25, 20, 15, 19, 5]
                level = self.rng.choice([1, 2, 3, 4, 6, 7, 8], p=np.array(p, float)/np.sum(p))
                
            self.append(Cover(self, surface, level, params, house_seed=self.house_seed))
            
        # ----------------------------------------------------------------------------------------------------
        # House is composed of joining rectangles
            
        else:
            bounds = house.bounds
            i_max  = np.argmax(areas)
            
            length = np.max(bounds)
            width  = np.min(bounds)
    
            # ----- Rectangle heights
            
            if width < 6:
                level_max   = 1
                level_count = 1
            elif width < 15:
                level_max   = 2
                level_count = 1
            elif width < 25:
                level_max   = 3
                level_count = 2
            elif width < 50:
                level_max    = 4
                level_count  = 2
            else:
                level_max    = 12
                level_count  = 3
                
            if len(self) < 3:
                levels_set = [self.rng.integers(1, level_max+2)]
            else:
                # Let's set the heigths among a set of 3 possible heights
                levels_set = np.sort(np.unique(self.rng.integers(1, level_max+2, level_count)))
                
            levels     = [self.rng.choice(levels_set) for _ in range(len(house))]

            # Max surface should be max level
            if self.rng.uniform(0, 1) < .95:
                levels[i_max] = levels_set[-1]
            
            # ----------------------------------------------------------------------------------------------------
            # Create the covers
            
            for i_surface, surface in enumerate(house):
                self.append(Cover(self, surface, levels[i_surface], params, house_seed=self.house_seed))

        # ----------------------------------------------------------------------------------------------------
        # Arrange the covers
            
        i_covers = np.argsort(-np.array([cover.area for cover in self]))
        for i_cover in i_covers:
            self[i_cover].arrange()
            
        # ----------------------------------------------------------------------------------------------------
        # Walls are created, we can set some options
        
        ext_walls = [wall for wall in self.walls if wall.external and wall.length > 3]
        if len(ext_walls):
            self.rng.choice(ext_walls).door = True
            wall = self.rng.choice(ext_walls)
            if not wall.door:
                wall.garage = True

    def __str__(self):
        return f"<House Elevator,  covers: {len(self.covers)}, walls: {len(self.walls)}>"
    
    # ====================================================================================================
    # The facades
    
    def facades(self, assets):
        
        hbuild = HouseBuilder(assets, rng=np.random.default_rng(100 + self.index))
        
        facades = Meshes()
        facades.new_face_attribute("face_seed", 'FLOAT')

        for wall in self.walls:
            facades.append(wall.facade(hbuild, self))
            
        facades.new_face_attribute("house_seed", 'FLOAT', value=self.house_seed)
        
        return facades
    
    # ====================================================================================================
    # The roofs
    
    def roofs(self):
        
        roofs = None
        
        for i_cover, cover in enumerate(self):
            
            mb = cover.build()
            if mb is None:
                continue
            
            if roofs is None:
                roofs = mb
            else:
                roofs.append(mb)
        
        if roofs is not None:
            roofs.new_face_attribute("house_seed", 'FLOAT', value=self.house_seed)
        
        return roofs
    
    # ====================================================================================================
    # Full house
    
    def build(self):
        
        mb = MeshBuilder()
        for wall in self.walls:
            mb.append(wall.simple_facade())
            
        roofs = self.roofs()
        if roofs is not None:
            mb.append(roofs)
                
        return mb
       
                
# ====================================================================================================
# Block elevator

class BlockElevator(Elevator):
    
    def __init__(self, block, index, rng=None): 
        
        super().__init__(index, is_house=False, rng=rng)
        
        block.recalc_shared()
        
        seeds = self.rng.uniform(0, 1, 6)
        self.house_seeds = self.rng.choice(seeds, len(block))
        
        for i_house, house in enumerate(block):
            params = self.gen_house_params(house.area)
            params['cover_type'] = 'FLAT'
            self.append(Cover(self, house, params['levels'], params, house_seed=self.house_seeds[i_house]))

        # ----------------------------------------------------------------------------------------------------
        # Arrange the covers
            
        i_covers = np.argsort(-np.array([cover.area for cover in self]))
        for i_cover in i_covers:
            self[i_cover].arrange()
            
        # ----------------------------------------------------------------------------------------------------
        # Walls are created, we can set some options
        
        ext_walls = [wall for wall in self.walls if wall.external and wall.length > 3]
        if len(ext_walls):
            self.rng.choice(ext_walls).door = True
            wall = self.rng.choice(ext_walls)
            wall.shop = True
        
    # ====================================================================================================
    # The facades
    
    def facades(self, assets):
        
        facades = Meshes()
        meshes.new_face_attribute("house_seed", 'FLOAT')
        meshes.new_face_attribute("face_seed",  'FLOAT')
        
        hbuilds = [HouseBuilder(assets, rng=np.random.default_rng(self.index<<20 + i_house)) for i_house in range(len(self))]
        for i_wall, wall in enumerate(self.walls):
            house_index = wall.cover1.index
            hbuild = hbuilds[house_index]
            facade = wall.facade(hbuild, self)
            facade.new_face_attribute("house_seed",  'FLOAT', value=self.house_seeds[house_index])
            facades.append(facade)
            
        return facades
    
    # ====================================================================================================
    # The roofs
    
    def roofs(self):
        
        roofs = Meshes()
        
        for i_cover, cover in enumerate(self):
            
            mb = cover.build()
            if mb is None:
                continue
            
            mb.new_face_attribute("house_seed", 'FLOAT', value=self.house_seeds[i_cover])
            
            roofs.append(mb)
            
        roofs.quick_done()
        
        return roofs
    
        
        
        
        

                
        