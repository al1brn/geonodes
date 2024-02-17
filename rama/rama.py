#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:01:54 2022

@author: alain
"""

import bpy

import numpy as np
from pathlib import Path

from importlib import reload

from geopy.core import bingrid
from geopy.core.camera import Camera
from geopy.core.varrays import VArrays
from geopy.core.transformations import Quaternions
from geopy.core.crowd import Crowd

reload(bingrid)

from geopy.core import blender
from geopy.core.bingrid import BinGrid
from geopy.core.meshbuilder import MeshBuilder
from geopy.gis.tiles import Tiles
from geopy.houses import facades
from geopy.rama.maptiler import MapTiler, Terrain

# ====================================================================================================
# Rama dimensions

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
# Free fall law
# omega such as r.w^2 = 10 m/s^2 ==> w = sqrt(10/r)

OMEGA = np.sqrt(10/RAMA_RADIUS)

def free_fall(locations, speeds, t=None, count=1000, duration=None):
    
    # ----- Radius
    
    rs  = np.linalg.norm(locations[..., 1:], axis=-1)
    
    # ----- Normal tangential vector
    
    tg = np.array(locations)
    tg[..., 0] = 0
    tg[..., 1] = -locations[..., 2]
    tg[..., 2] =  locations[..., 1]
    tg[..., 1:] /= np.linalg.norm(tg[..., None, 1:], axis=-1)
    
    # ----- Initial speeds
    
    speeds = speeds + (rs[..., None]*tg)*OMEGA

    # ----- Need the whole curve
    
    if t is None:
    
        # Tangential speeds plus distance to circumference give the fall duration
        
        if duration is None:
            ds = np.sqrt(RAMA_RADIUS**2 - np.minimum(RAMA_RADIUS, rs)**2)
            duration = np.max(ds/np.linalg.norm(speeds[..., 1:], axis=-1))
        
        # Inertial frame : the trajectory is a line at constant speed
        
        ts = np.linspace(0, duration, count)  
        
    # ----- Need at time t
    
    else:
        count = 1
        ts = np.resize(max(t, 0.), (1,)).astype(float)
        
    curves = locations[..., None, :] + speeds[..., None, :]*ts[:, None]
    
    # ----- let's convert into the rotating referenial
    
    cag = np.cos(OMEGA*ts)
    sag = np.sin(OMEGA*ts)
    
    M = np.empty((count, 2, 2), float)
    M[:, 0, 0] = cag
    M[:, 1, 1] = cag
    M[:, 0, 1] = -sag
    M[:, 1, 0] = sag
    del cag, sag, ts
    
    curves[..., 1:] = np.einsum('...ij, ...i', M, curves[..., 1:])
    
    if t is None:
        return curves
    else:
        return curves[:, 0]

# ====================================================================================================
# Slowed fall

def slowed_fall(locations, speeds, max_speed, duration=20, max_speed_at=0, count=1000):
    
    # ----- Resulting array initialization
    curves = np.empty(np.shape(locations)[:-1] + (count, 3))
    curves[..., 0, :] = locations

    # ----- Simulation delta time    
    dt = duration/(count-1)
    
    # ----- Let's loop    
    a   = np.zeros_like(locations)
    v   = np.zeros_like(locations)
    v[:] = speeds
    cor = np.zeros_like(v[..., 1:])
    t = 0
    
    for i in range(1, count):
        
        # ----- Radial acceleration
        a[..., 1:] = curves[..., i-1, 1:]*(OMEGA**2)

        # ----- Coriolis acceleration
        cor[..., 0] = -v[..., 2]
        cor[..., 1] = v[..., 1]
        
        a[..., 1:] += -2*OMEGA*cor

        # New speed
        new_v = v + a*dt
        
        # Maximize the speed
        if t >= max_speed_at:
            nv = np.linalg.norm(new_v, axis=-1)
            new_v *= np.minimum(max_speed, nv)/nv

        # New position
        curves[..., i, :] = curves[..., i-1, :] + (v + new_v)*(dt/2)
        
        # Update variables
        v = new_v
        t += dt
        
    
    return curves




def free_fall_test():
    
    from geopy.core.curvebuilder import CurveBuilder
    
    count = 1000
    shape = (20,)

    cb = CurveBuilder()
    
    verts = free_fall( np.array((0, 0, -.1*RAMA_RADIUS)), np.array((0, 0, 0)), count=count)
    
    verts /= 1000
    
    cb.add_polys(verts)
    
    locs = np.zeros(shape + (3,), float)
    locs[..., 0] = np.random.uniform(-RAMA_X, RAMA_X, shape)
    locs[..., 1] = np.random.uniform(-.7, .7, shape)*RAMA_RADIUS
    locs[..., 2] = np.random.uniform(-.7, .7, shape)*RAMA_RADIUS
    
    speeds = np.zeros(shape + (3,), float)
    speeds[..., 0] = np.random.uniform(-300, 300, shape)
    speeds[..., 1] = np.random.uniform(-100, 100, shape)
    speeds[..., 2] = np.random.uniform(-100, 100, shape)
    
    
    verts = free_fall( locs, speeds, count=count) / 1000
    verts = np.reshape(verts, (np.prod(shape, dtype=int), count, 3))
    
    cb.add_polys(verts)
    
    cb.to_object("Test")

    
    
    
    
    
    
    
    
    
    
    
    
    
    






# ====================================================================================================
# Common to Land and Sea

class RamaSegment:
    
    # ----------------------------------------------------------------------------------------------------
    # To object
        
    def to_object(self, object_name, uv_scale=1, mat=None):
        
        uv_scale = 1
        
        obj = blender.create_mesh_object(object_name)
        self.bgrid.to_object(obj, uv_scale=uv_scale, verbose=object_name) #, mat=mat)
        
        obj.data.polygons.foreach_set('use_smooth',  [1] * len(obj.data.polygons))
        
        return obj
        
        # ----- Altitude layer
        
        if self.cylindric:
            alt = cyl_radius - np.linalg.norm(self.mgrid.vertices.verts[:, 1:], axis=-1)
        else:
            alt = np.array(self.mgrid.vertices.verts[:, 2])

        v_layer = obj.data.vertex_layers_float.new(name="altitude")
        v_layer.data.foreach_set('value', alt)
        
        del alt

        # ----- Vertices layers
        
        for name, layer in self.mgrid.vertices.layers.items():
            
            if layer.dtype == float:
                v_layer = obj.data.vertex_layers_float.new(name=name)
                v_layer.data.foreach_set('value', layer)
                
            elif layer.dtpe in (int, bool):
                v_layer = obj.data.vertex_layers_int.new(name=name)
                v_layer.data.foreach_set('value', layer)    
    


# ====================================================================================================
# Rama Land

class Land(Terrain):
    def __init__(self, folder, subdivision=8, cylindric=False, x_location=0, default_mat="Material"):
        
        self.x_location = x_location
        self.cylindric  = cylindric
        
        # ----------------------------------------------------------------------------------------------------
        # Get vertices
        
        def plane_func(ijs):
            verts = np.zeros(np.shape(ijs)[:-1] + (3,), float)
            verts[..., :2] = ijs
            verts[..., 2] = self.tiles.values_at_coords(ijs) 
            
            verts[..., 0] += self.x_location

            return verts
            
        def cyl_func(ijs):
            # +1 for sea @ 0
            rs  = RAMA_RADIUS + 1 - self.tiles.values_at_coords(ijs)
            ags = (ijs[..., 1] - RAMA_Y/2)/RAMA_RADIUS
            
            verts = np.empty(ijs.shape[:-1] + (3,))
            verts[..., 0] = ijs[..., 0] + self.x_location
            verts[..., 1] = rs*np.sin(ags)
            verts[..., 2] = -rs*np.cos(ags)
            
            return verts
        
        get_verts = cyl_func if cylindric else plane_func
        
        # ----------------------------------------------------------------------------------------------------
        # Initialization
        
        super().__init__(folder, dims=(RAMA_X, RAMA_Y), max_subdiv=subdivision, get_verts=get_verts, default_mat=default_mat)
        
    # ----------------------------------------------------------------------------------------------------
    # Altitude at x and rotation
    
    def altitude_at(self, x, y_rot):
        i = round(x - self.x_location)
        j = round(RAMA_Y*np.radians(y_rot))
        return self.tiles.values_at_coords(np.array([[i, j]]))[0]
        


class Land_OLD(RamaSegment):
    def __init__(self, folder, subdivision=8, cylindric=False, x_location=0):
        
        self.tiles      = Tiles(folder, shape=(RAMA_X, RAMA_Y))
        self.x_location = x_location
        self.size_x     = RAMA_X*1.
        self.size_y     = RAMA_Y*1.
        self.cylindric  = cylindric
        
        nx = self.tiles.shape[0] // 100
        ny = self.tiles.shape[1] // 100
        
        def plane_func(ijs):
            verts = np.empty(ijs.shape[:-1] + (3,))
            verts[..., :2] = ijs + (self.x_location, -self.size_y/2)
            verts[..., 2]  = self.tiles.values_at_coords(ijs)
                
            return verts
            
        def cyl_func(ijs):
            rs  = RAMA_RADIUS - self.tiles.values_at_coords(ijs)
            ags = (ijs[..., 1] - RAMA_Y/2)/RAMA_RADIUS
            
            verts = np.empty(ijs.shape[:-1] + (3,))
            verts[..., 0] = ijs[..., 0] + self.x_location
            verts[..., 1] = rs*np.sin(ags)
            verts[..., 2] = -rs*np.cos(ags)
            
            return verts
        
        if cylindric:
            self.bgrid = BinGrid((RAMA_X, RAMA_Y), func=cyl_func, subdivision=subdivision)

        else:
            self.bgrid = BinGrid((RAMA_X, RAMA_Y), func=plane_func, subdivision=subdivision)
            
        # ----- Don't split flat faces at altitude 0
        
        v_ij = np.zeros(self.bgrid.verts_shape + (2,), int)
        i, j = np.meshgrid(np.arange(self.bgrid.verts_shape[0]), np.arange(self.bgrid.verts_shape[1]), indexing='ij', sparse=True)
        
        v_ij[..., 0] = i*self.bgrid.face_side
        v_ij[..., 1] = j*self.bgrid.face_side
        
        alts = self.tiles.values_at_coords(v_ij)
        self.bgrid.no_face[:] = True
        self.bgrid.no_face[alts[:-1, :-1]>0] = False
        self.bgrid.no_face[alts[:-1,  1:]>0] = False
        self.bgrid.no_face[alts[1:,   1:]>0] = False
        self.bgrid.no_face[alts[1:,  :-1]>0] = False
               
                
# ====================================================================================================
# South Land

class SouthLand(Land):
    def __init__(self, folder, subdivision=8, cylindric=True, tiles_folder=None ):
        super().__init__(Path(folder) / "Rama/South/altitudes", subdivision=subdivision, cylindric=cylindric, x_location=SOUTH_X_LOC, default_mat="South 14")
        
        self.init_satellite(
            mat_template    = "Rama Land",
            cache_folder    = Path(folder) / "cache",
            tiles_folder    = Path(folder) / "Sat_images" if tiles_folder is None else tiles_folder,
            origin          = SOUTH_CENTER, 
            angle           = SOUTH_ANGLE, 
            prefix          = "South", 
            mat_size        = 4,
            matrices        = {5:15, 6:16, 7:17, 8:18},
            )

# ====================================================================================================
# North Land

class NorthLand(Land):
    def __init__(self, folder, subdivision=8, cylindric=True, tiles_folder=None ):
        super().__init__(Path(folder) / "Rama/North/altitudes", subdivision=subdivision, cylindric=cylindric, x_location=NORTH_X_LOC, default_mat="North 14")

        self.init_satellite(
            mat_template    = "Rama Land",
            cache_folder    = Path(folder) / "cache",
            tiles_folder    = Path(folder) / "Sat_images" if tiles_folder is None else tiles_folder, 
            origin          = NORTH_CENTER, 
            angle           = NORTH_ANGLE, 
            prefix          = "North", 
            mat_size        = 4,
            matrices        = {5:15, 6:16, 7:17, 8:18},
            )
                

# ====================================================================================================
# Sea

class Sea(MapTiler):
    def __init__(self, altitude=0, subdivision=8, cylindric=True):
        
        SEA_X0 = -11500
        SEA_X1 =  12000
        
        SEA_X  = 4096*5
        
        def plane_func(ijs):
            verts = np.empty(ijs.shape[:-1] + (3,))
            verts[..., 0] = SEA_X0 + ijs[..., 0]*( (SEA_X1 - SEA_X0)/SEA_X)
            verts[..., 1] = ijs[..., 1] - RAMA_Y/2
            verts[..., 2] = altitude
                
            return verts
            
        def cyl_func(ijs):
            
            verts = np.empty(np.shape(ijs)[:-1] + (3,), float)

            ags = (ijs[..., 1] - RAMA_Y/2)/RAMA_RADIUS
            
            radius = RAMA_RADIUS + altitude
            
            verts[..., 0] = SEA_X0 + ijs[..., 0]*( (SEA_X1 - SEA_X0)/SEA_X)
            verts[..., 1] = radius*np.cos(ags)
            verts[..., 2] = radius*np.sin(ags)
            
            return verts    

        get_verts = cyl_func if cylindric else plane_func

        nx = 190 
        ny = 500
        
        nx = (SEA_X1 - SEA_X0)//256
        ny = RAMA_Y//256
        
        super().__init__(shape=(nx, ny), max_subdiv=subdivision, uv_scale=1, get_verts=get_verts, default_mat="Sea")
        
    # ----------------------------------------------------------------------------------------------------
    # To object
        
    def to_object_OLD(self, object_name, mat=None):
        
        uv_scale = 1/1000
        
        obj = blender.create_mesh_object(object_name)
        self.mgrid.to_object(obj, uv_scale=uv_scale, mat=mat)
        
        # ----- Vertices layers
        
        for name, layer in self.mgrid.vertices.layers.items():
            
            if layer.dtype == float:
                v_layer = obj.data.vertex_layers_float.new(name=name)
                v_layer.data.foreach_set('value', layer)
                
            elif layer.dtpe in (int, bool):
                v_layer = obj.data.vertex_layers_int.new(name=name)
                v_layer.data.foreach_set('value', layer)
                
                
class Sea_OLD(RamaSegment):
    def __init__(self, altitude=0, subdivision=8, cylindric=False):
        
        SEA_X0 = -11500
        SEA_X1 =  12000
        
        SEA_X  = 4096*5
        
        def plane_func(ijs):
            verts = np.empty(ijs.shape[:-1] + (3,))
            verts[..., 0] = SEA_X0 + ijs[..., 0]*( (SEA_X1 - SEA_X0)/SEA_X)
            verts[..., 1] = ijs[..., 1] - RAMA_Y/2
            verts[..., 2] = altitude
                
            return verts
            
        def cyl_func(ijs):
            
            verts = np.empty(np.shape(ijs)[:-1] + (3,), float)

            ags = (ijs[..., 1] - RAMA_Y/2)/RAMA_RADIUS
            
            radius = RAMA_RADIUS + altitude
            
            verts[..., 0] = SEA_X0 + ijs[..., 0]*( (SEA_X1 - SEA_X0)/SEA_X)
            verts[..., 1] = radius*np.cos(ags)
            verts[..., 2] = radius*np.sin(ags)
            
            return verts    
        
        nx = 190 
        ny = 500
        
        if cylindric:
            self.bgrid = BinGrid((SEA_X, RAMA_Y), func=cyl_func, subdivision=subdivision)
        else:
            self.bgrid = BinGrid((SEA_X, RAMA_Y), func=plane_func, subdivision=subdivision)
        
    # ----------------------------------------------------------------------------------------------------
    # To object
        
    def to_object_OLD(self, object_name, mat=None):
        
        uv_scale = 1/1000
        
        obj = blender.create_mesh_object(object_name)
        self.mgrid.to_object(obj, uv_scale=uv_scale, mat=mat)
        
        # ----- Vertices layers
        
        for name, layer in self.mgrid.vertices.layers.items():
            
            if layer.dtype == float:
                v_layer = obj.data.vertex_layers_float.new(name=name)
                v_layer.data.foreach_set('value', layer)
                
            elif layer.dtpe in (int, bool):
                v_layer = obj.data.vertex_layers_int.new(name=name)
                v_layer.data.foreach_set('value', layer)                
                
# ====================================================================================================
# Forests            
                
class Trees(Crowd):
    
    def __init__(self, root, trees_collection, cam_culling=False, percentage=0.01, cylindric=True, seed=0):
        
        # ----- Load the trees and select the requested percentage
        
        rng = np.random.default_rng(seed)
    
        all_trees = np.load(Path(root) / "Common/forest.npy")
        
        # ---- Takes only a percentage of all the possible trees
        locs = np.array(all_trees[rng.uniform(0, 1, len(all_trees)) < percentage])
        
        # ----- Cylindric location
        
        self.cylindric = cylindric
        if self.cylindric:
            self.thetas   = locs[:, 1]/RAMA_RADIUS
            r             = RAMA_RADIUS - locs[:, 2]
            locs[:, 1]    =  r*np.sin(self.thetas)
            locs[:, 2]    = -r*np.cos(self.thetas)
            self.vertical = -locs/np.expand_dims(np.linalg.norm(locs[:, 1:], axis=-1), axis=-1)
            self.vertical[:, 0] = 0
            
        # ----- Tree models

        if isinstance(trees_collection, str):
            trees_collection = bpy.data.collections[trees_collection]
            
        # ----- Big Crowd initialization
        
        super().__init__("Trees",
            models      = trees_collection.objects,
            shape       = len(locs),
            indices     = rng.integers(0, len(trees_collection.objects), len(locs)),
            cam_culling = cam_culling,
            mats        = None,
            )
        
        self.locations = locs
        self.scale(rng.normal(1, .2, len(self))[:, np.newaxis])
        self.eulers_order = 'ZYX'
        if self.cylindric:
            self.rx = self.thetas
        

        #super().__init__(locations=locs, models=trees_collection.objects, indices=rng.choice(len(trees_collection.objects), len(locs)))
        
        # ----- Start with no visible tree
        
        #self.reset_visibles()
        
    # ----------------------------------------------------------------------------------------------------
    # Orient the trees towards the camera
            
    def orient_to_camera(self):
        
        camera = Camera()
        
        rel_locs = list(camera.world_location) - self.locations
        
        if self.cylindric:
            self.track_to(np.array(camera.world_location), vertical=self.vertical)
            
            
            """ OLD
            if True:
                self.matrices = np.identity(3)
                self.rx = self.thetas
                
                rel_locs = np.cross(self.vertical, rel_locs)
                cam_ag = np.arcsin(np.clip(np.einsum('...i, ...i', (1, 0, 0), rel_locs), -1, 1)) + np.pi/2
                #cam_ag = np.arcsin(np.clip(np.einsum('...i, ...i', (1, 0, 0), rel_locs), -1, 1))
                if camera.world_location.x < 0:
                    cam_ag *= -1
                    
                #cam_ag = np.radians(0)
                self.rotate(Quaternions.AxisAngles(np.resize((0., 0., 1.), (len(self), 3)), cam_ag))
                
            else:
                rel_locs = np.cross(rel_locs, self.vertical)
                ags      = np.arctan2(rel_locs[:, 1], rel_locs[:, 0])
                self.rz  = ags - np.pi/2
            """

        else:
            ags     = np.arctan2(rel_locs[:, 1], rel_locs[:, 0])
            self.rz = ags + np.pi/2
            
# ====================================================================================================
# Houses
        
class RamaRoofs:
    
    def __init__(self, folder):
        self.folder  = Path(folder)
        self.roofs   = facades.Roofs(self.folder, "Rama roofs")
        self.roofs.reset_visibles()
        
    def visibility(self, frames=None):
        
        self.roofs.reset_visibles()
        
        def cvis():
            self.roofs.set_visibles(Camera())
        
        if frames is None:
            cvis()
        else:
            Camera.frame_range(frames, func=cvis, message="Facades and roofs visibility")
            
    def to_object(self, name="Roofs"):
        self.roofs.to_object(name)
        

class RamaFacades:
    
    def __init__(self, folder):
        self.folder  = Path(folder)
        self.facades = facades.Facades(self.folder, rama=True)
        self.facades.reset_visibles()
        
    def visibility(self, frames=None):
        
        self.facades.reset_visibles()
        
        def cvis():
            self.facades.set_visibles(Camera())
        
        if frames is None:
            cvis()
        else:
            Camera.frame_range(frames, func=cvis, message="Facades and roofs visibility")
            
    def to_object(self, name="Facades"):
        self.facades.to_object(name)


class Houses_OLD:
    
    def __init__(self, folder):
        self.folder  = Path(folder)
        self.facades = facades.Facades(self.folder, rama=True)
        self.roofs   = facades.Roofs(self.folder, "Rama roofs")
        
        self.facades.reset_visibles()
        self.roofs.reset_visibles()
        
    def visibility(self, camera, frames=None):
        
        self.facades.reset_visibles()
        self.roofs.reset_visibles()
        
        def cvis():
            self.facades.set_visibles(camera)
            self.roofs.set_visibles(camera)
        
        if frames is None:
            cvis()
        else:
            camera.frame_range(frames, func=cvis, message="Facades and roofs visibility")
            
    def to_object(self):
        self.facades.to_object("Facades")
        self.roofs.to_object("Roofs")
        
# ====================================================================================================
# Houses
        
class Cities_OLD:
    def __init__(self, folder, cylindric=False):
        
        root = Path(folder)
        
        ars = np.load(Path(root) / "Common/rect_houses.npz")
        self.info   = ars['info']
        self.locs   = ars['loc_scale'][:, 0]
        self.shapes = VArrays.load(root / "Common/shaped_houses.npz")
        
        # ----- Cylindric
        
        self.cylindric = cylindric
        if self.cylindric:
            
            thetas = self.locs[:, 1]/RAMA_RADIUS
            r      = RAMA_RADIUS - self.locs[:, 2]
                
            self.locs[:, 1] =  r*np.sin(thetas)
            self.locs[:, 2] = -r*np.cos(thetas)
            
            self.verticals  = -self.locs/np.expand_dims(np.linalg.norm(self.locs[:, 1:], axis=-1), axis=-1)
            self.verticals[:, 0] = 0
            
        else:
            self.verticals = np.zeros((len(self), 3), float)
            self.verticals[:, 2] = 1

        # ----- Visiblity
        
        self.visibles  = np.zeros(len(self), bool)
        self.distances = np.ones(len(self), int)*100000
        self.blocks    = []
        
    def __len__(self):
        return len(self.locs)
        
    def __str__(self):
        
        s = "<Cities"
        s += "\n - Rectangular houses:"
        s += f"\n   . info      : {np.shape(self.info)}"
        s += f"\n   . locs      : {np.shape(self.locs)}"
        s += "\n"
        s += "\n - Shapes:"
        s += f"\n   . count    : {len(self.shapes)}"
        s += f"\n   . vertices : {np.shape(self.shapes.items)}"
        
        return s + "\n>"
    
    # ====================================================================================================
    # For debug
        
    def to_object(self, name, visibles=None, flat=True, wall_mats=1, roof_mats=1, seed=None):
        
        shapes    = self.shapes if visibles is None else self.shapes[visibles]
        verticals = self.verticals if visibles is None else self.verticals[visibles]
        
        print(f"Cities to object: {len(shapes.items)} vertices")

        if len(shapes) == 0:
            mesh = bpy.data.objects[name].data
            mesh.clear_geometry()
            mesh.update()
            print("No visible shapes...")
            return
        
        if self.cylindric:
            
            shapes = VArrays.FromVArrays(shapes)
            verts  = shapes.items
            thetas = verts[:, 1]/RAMA_RADIUS
            r      = RAMA_RADIUS - verts[:, 2]
            verts[:, 1] =  r*np.sin(thetas)
            verts[:, 2] = -r*np.cos(thetas)
            shapes.items = verts
        
        
        if flat:
            faces = []
            n = 0
            for l in shapes._info[:, 0]:
                faces.append([n + i for i in range(l)])
                n += l
            
            mesh = bpy.data.objects["Test"].data
            mesh.clear_geometry()
            mesh.from_pydata(shapes.items, (), faces)
            mesh.update()
            
        else:
            rng = np.random.default_rng(seed)
            
            nverts = len(shapes.items)
            faces = []
            mats  = []
            n = 0
            
            central   = 9
            min_value = 3
            heights   = rng.rayleigh(1, len(shapes))*((central - min_value)/1.254) + min_value
            # Roof materials are the first ones in the liste
            wall_mats = rng.integers(roof_mats, roof_mats + wall_mats, len(shapes))
            roof_mats = rng.integers(0, roof_mats, len(shapes))
            
            verts = np.array(shapes.items)
            for i_house, (l, h, wall_mat, roof_mat, vertical) in enumerate(zip(shapes._info[:, 0], heights, wall_mats, roof_mats, verticals)):
                faces.append([nverts + n + i for i in range(l)])
                for i in range(l):
                    faces.append([n + i, n + (i+1)%l, nverts + n + (i+1)%l, nverts + n + i])
                verts[n:n+l] += h*vertical
                mats.extend([roof_mat] + [wall_mat]*l)
                n += l
                
            mesh = bpy.data.objects[name].data
            mesh.clear_geometry()
            mesh.from_pydata(np.append(shapes.items, verts, axis=0), (), faces)
            mesh.polygons.foreach_set('material_index', mats)
            mesh.update()
            
    # ====================================================================================================
    # Visibility
    
    def reset_culling(self):
        self.visibles[:]  = False
        self.distances[:] = 100000
        
    def camera_culling(self, camera, close_distance=300, frames=None):
        
        if frames is None:
            vis, dists = camera.visible_verts(self.locs, close_distance=300)
            self.visibles[vis] = True
            self.distances[vis] = np.minimum(self.distances[vis], dists[vis])
            return
        
        print( "------------------------------------------")
        print(f"Cities.camera_culling in {frames}")
        print(f"   locs shape: {np.shape(self.locs)}")
        
        print(end="")
        
        for frame in frames:
            print(f"frame {frame}")
            bpy.context.scene.frame_set(frame)
            self.camera_culling(camera, close_distance=close_distance)
        
        print("\nCamera culling done")
        print()

    # ====================================================================================================
    # Make houses visible in a region
    
    def set_region_visible(self, center, distance, detailed=False):
        
        x, y = center
        
        ag = y*(np.pi*2/RAMA_Y)
        r  = RAMA_RADIUS
    
        loc = np.array((x, r*np.sin(ag), -r*np.cos(ag)))
        
        vis = np.linalg.norm(self.locs - loc, axis=-1) <= distance
        self.visibles[vis] = True
        if detailed:
            self.distances[vis] = 1
    
        
    # ====================================================================================================
    # Build the houses
    
    def build_houses(self, collection, close_distance=1000):
        
        print("Building cities...")
        
        if isinstance(collection, str):
            collection = bpy.data.collections[collection]
        
        # ----- Clear the collection

        for obj in collection.objects:
            if False: # Seems to crash in frame update
                bpy.data.objects.remove(obj, do_unlink=True)
                #collection.objects
            else:
                obj.data.clear_geometry()
        
        # ----------------------------------------------------------------------------------------------------
        # Far houses
        
        # ----- Create the object with the proper materials
        
        mat_db = houses.MaterialDB('FAR_HOUSES')
        obj = blender.create_mesh_object("Far houses", collection=collection)
        for mat_name in mat_db.materials:
            obj.data.materials.append(bpy.data.materials.get(mat_name))
        
        # ----- Build the far houses
        
        closes   = np.logical_and(self.visibles, self.distances < close_distance)
        visibles = np.logical_and(self.visibles, self.distances >= close_distance)
        
        print(f"   Far houses: {np.sum(visibles)}...")
        self.to_object(obj.name, visibles=visibles, flat=False, wall_mats=len(mat_db['far_wall']), roof_mats=len(mat_db['far_roof']))
        del visibles
        
        # ----------------------------------------------------------------------------------------------------
        # Close houses
        
        mat_db  = houses.MaterialDB('HOUSES')
        roof_db = houses.RoofDB(bpy.data.collections['Roofs'])
        
        shapes  = self.shapes[closes]
        nshapes = len(shapes)
        
        builder = Builder(materials=mat_db.materials)
        
        print(f"   Close houses: {np.sum(closes)}...")
        for count_house, (ofs, size) in enumerate(zip(shapes.offsets, shapes.sizes)):
            
            if (count_house % 100 == 0 or count_house == nshapes-1) and count_house != 0:
                
                print(f"      {count_house}")
                
                obj = blender.create_mesh_object(f"Houses {count_house//100:03d}", collection)
                builder.to_object(obj.name)
                builder = Builder(materials=mat_db.materials)

        
            verts = shapes.items[ofs:ofs+size]
            #form  = Form(verts)
            
            """
            if form.is_rectangle:
                h_locs = a_locs[i_house]
                h_locs[0, :2] -= loc0
                #tmat = TMatrices(locations=h_locs[0], scales=h_locs[1])
                #verts = np.array(((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)), float)
                #verts = tmat.transform(verts).a[0]
         
                form = Form.FromLocScale(h_locs)
            """
            
            blind_sides = [False] * len(verts)
            house = houses.Building(verts, blind_sides, roof_db, mat_db, seed=np.random.randint(1<<31))

            if self.cylindric:
                house_builder = Builder(materials=mat_db.materials)
                house.build(house_builder, details=2)

                theta  = house_builder.verts[:, 1]/RAMA_RADIUS
                r      = RAMA_RADIUS - house_builder.verts[:, 2]
                house_builder.verts[:, 1] =  r*np.sin(theta)
                house_builder.verts[:, 2] = -r*np.cos(theta)
                
                
                house_builder.append_to(builder)
            else:
                house.build(builder, details=2)   
            
        print("Done")
        
# ====================================================================================================
# Convert rama x, y to RgeAlti native tiles coordinates
#
# x -> land center, angle and x, y

def rama_to_rge(x, y):
    
    """
    x_loc  = NORTH_LOC if north else SOUTH_LOC
    x_loc += RAMA_X/2
    x_loc += RAMA_X/2
    
    if north:
        dx = -1041
        dy = 350
    else:
        dx = -752
        dy =  650
    """
    
    # ----- North
    
    if x < 0:
        return True, NORTH_CENTER, NORTH_ANGLE, x - NORTH_X_LOC - RAMA_X/2 + 1041, y - 350

    # ----- South
    
    else:
        return False, SOUTH_CENTER, SOUTH_ANGLE, x - SOUTH_X_LOC - RAMA_X/2 + 760, y - 645 # x: 752 trop à droite, 650 trop haut
        
        
        
# ====================================================================================================
# Camera location

def ground_location(folder, x, y, z=2):
    
    north = x <= 0
    land_folder = Path(folder) / ("North/Altitudes" if north else "South/Altitudes")
    tiles = Tiles(land_folder, shape=(RAMA_X, RAMA_Y))
    dx = NORTH_X_LOC if north else SOUTH_X_LOC
    
    alt = tiles.values(np.reshape((x - dx, y + RAMA_Y/2), (1, 2)))[0]
    
    ag = y*(np.pi*2/RAMA_Y)
    r  = RAMA_RADIUS - alt - z
    
    loc = np.array((x, r*np.sin(ag), -r*np.cos(ag)))
    
    return loc, ag
        
        
# ====================================================================================================
# A detailed region
#
# - rge_folder : RGE source folder for altitudes
# - sat_folder : satellite images cache folder
# - center     : Rama coordinates of the center of region
# - size       : Size of the Zone in km

def build_detailed_region(rge_folder, sat_folder, center, size, matrix=17, obj_name="Zoom", mat_name=None):
    
    from geopy.gis.rgealti import RgePack
    from geopy.gis.sat_tiles import SatTiles
    
    north, origin, angle, rx, ry = rama_to_rge(center[0], center[1])
    
    rgepack = RgePack(rge_folder, origin=origin)
    tiles   = SatTiles(matrix=matrix, origin=origin, cache_folder=sat_folder)
    tiles.set_rotation(angle)
    
    corner = rx - size[0]/2, ry - size[1]/2
    
    # ----- Mesh
    
    grid = rgepack.extract(corner, size, resolution=1, angle=angle, return_grid=True)
    verts = grid.verts
    
    # Locate properly
    
    verts[:, :2] += (center[0], center[1])
    
    # Cylinder shape
    
    ag = verts[:, 1]*(np.pi*2/RAMA_Y)
    r  = RAMA_RADIUS - verts[:, 2]

    verts[:, 1] = r*np.sin(ag)
    verts[:, 2] = -r*np.cos(ag)
    
    # Build the object
    
    obj  = blender.create_mesh_object(obj_name)
    grid.to_object(obj, mat=mat_name)
    
    # ----- Satellite image for the material
    
    if mat_name is not None:
        img = tiles.texture(corner, size, return_image=False)
        blender.get_image_node(mat_name).image = blender.pil_array_to_image(img, mat_name)
    
    # ----- Done
    
    return obj
        
    
    
    
    
    
    
        
        



            
            
           

                
        
        
