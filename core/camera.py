#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 07:38:55 2022

@author: alain
"""

import numpy as np

import bpy
from mathutils import Vector

from geonodes.core import engine

# =============================================================================================================================
# Camera

class Camera:
    
    def __init__(self, camera=None):
        
        if camera is None:
            self._bcamera = None
            
        elif isinstance(camera, str):
            self._bcamera = bpy.data.objects[camera]
            
        else:
            assert(isinstance(camera.data, bpy.types.Camera))
            self._bcamera = camera
            
            
    def __str__(self):
        return f"<Camera '{self.bcamera.name}': focal: {np.degrees(self.focal_angle):.1f}°, resolution: ({self.resolution_x}, {self.resolution_y})>"
            
    # ----------------------------------------------------------------------------------------------------
    # The Blender camera
    
    @property
    def bcamera(self):
        if self._bcamera is None:
            return bpy.context.scene.camera
        else:
            return self._bcamera
        
    # ----------------------------------------------------------------------------------------------------
    # Camera world location
    
    @property
    def location(self):
        return self.bcamera.matrix_world.translation        
    
    # ----------------------------------------------------------------------------------------------------
    # Focal angle of the camera
        
    @property
    def focal_angle(self):
        return self.bcamera.data.angle
    
    # ----------------------------------------------------------------------------------------------------
    # Normalized vector representing the direction of the camera
        
    @property
    def direction(self):
        return (self.bcamera.matrix_world @ Vector((0, 0, -1, 0))).resized(3).normalized()
    
    # ----------------------------------------------------------------------------------------------------
    # Scene resolution
        
    @property
    def resolution_x(self):
        return bpy.context.scene.render.resolution_x
    
    @property
    def resolution_y(self):
        return bpy.context.scene.render.resolution_y
    
    @property
    def resolution(self):
        return self.resolution_x
    
    # ----------------------------------------------------------------------------------------------------
    # The size, in pixels, of 1 meter at a distance
    
    def meter_in_pixels(self, distances):
        """ Return the size in pixels of a meter at the given distances.

        A point (x, y, z) in the camera referentiel at distance d is projected to cam_z*(x, y)/d
        A meter gives a length of cam_z/d. This length is a fraction of the projection plane.
        We use this fraction to multiply with the render resolution.
        
        Note that cam_z is negative. We must take its absolute value.
        """
        
        render = self.resolution
        
        # ----------------------------------------------------------------------------------------------------
        # The projection rectangle

        c0, c1, c2, c3 = self.bcamera.data.view_frame(scene=bpy.context.scene)
        
        
        # Width (render resolution is horizontal)
        
        cam_x0 = min(c0.x, c1.x, c2.x, c3.x)
        cam_x1 = max(c0.x, c1.x, c2.x, c3.x)

        cam_z = abs(c0.z)

        #print(f"camera.meter_in_pixels", c0, c1, c2, c3, "cam x0, x1", cam_x0, cam_x1, "cam_z", cam_z)
        
        return (render*cam_z/(cam_x1 - cam_x0)) / distances
    
    
    # ----------------------------------------------------------------------------------------------------
    # Distance of a location to the camera
    
    def distance(self, location):   
        
        if isinstance(location, Vector) or np.shape(location) == (3,):
            return (self.location - Vector(location)).length
        
        else:
            return np.linalg.norm(location - self.location, axis=-1)
        
    # =============================================================================================================================
    # Compute the visibility of vertices
    
    def visible_verts(self, verts, radius=None, close_distance=None, max_distance=None, margin=1., normals=None):
        """ Compute the visibility of vertices.
        
        Arguments
        ---------
            - verts (array of vectors) : vertex locations
            - radius (float or array of floats = None) : size at the locations 
            - close_distance (float = None) : vertices closer than this distance are visible
            - max_distance (float = None) : vertices father that this distance are not visibles
            - margin (float, default=1.) : margin factor around the camera
            - normals (array of vectors = None) : normal pointing outwards are not visible
        
        Returns
        -------
            - visibles (array of bools)   : visible vertices
            - distances (array of floats) : The distance to the camera
        """
        
        camera = self.bcamera

        # ----------------------------------------------------------------------------------------------------
        # The projection rectangle
        # The plane is horizontal. All z<0 are identical

        c0, c1, c2, c3 = camera.data.view_frame(scene=bpy.context.scene)

        cam_x0 = min(c0.x, c1.x, c2.x, c3.x)*margin
        cam_x1 = max(c0.x, c1.x, c2.x, c3.x)*margin
        cam_y0 = min(c0.y, c1.y, c2.y, c3.y)*margin
        cam_y1 = max(c0.y, c1.y, c2.y, c3.y)*margin

        cam_z = c0.z
        
        if False:
            print("-"*80)
            print(f"CAMERA SHAPE: plane z = {cam_z:.1f}")
            print(f"   x: {cam_x0:5.1f} {cam_x1:5.1f}")
            print(f"   y: {cam_y0:5.1f} {cam_y1:5.1f}")
            print()
            
        # ----------------------------------------------------------------------------------------------------
        # Rotate the points in the camera frame
        
        M = np.array(camera.matrix_world.inverted())
        pts = np.array(np.einsum('...jk, ...k', M, np.insert(verts, 3, 1, axis=-1))[..., :3])
        
        # ----------------------------------------------------------------------------------------------------
        # Compute the distances
        
        distances = np.linalg.norm(pts, axis=-1)
        
        # ----------------------------------------------------------------------------------------------------
        # Projected radius
        
        if radius is None:
            r = 0
        else:
            r = (radius*cam_z)/distances

        # ----------------------------------------------------------------------------------------------------
        # Points must be in front of the camera
        
        visibles = pts[..., 2] <= cam_z

        # ---------------------------------------------------------------------------
        # Project the points on the plane z = cam_z

        pts = cam_z*(pts/np.expand_dims(pts[..., 2], axis=-1))[..., :2]
        
        # ---------------------------------------------------------------------------
        # Must be projected into the rectangle
        
        visibles &= (
            (pts[..., 0] - r >= cam_x0)  & 
            (pts[..., 0] + r <= cam_x1)  &
            (pts[..., 1] - r >= cam_y0)  &
            (pts[..., 1] + r <= cam_y1)
            )
            
        # ---------------------------------------------------------------------------
        # Not too far
        
        if max_distance is not None:
            visibles &= distances < max_distance
        
        # ---------------------------------------------------------------------------
        # Visible when close to the camera
        
        if close_distance is not None:
            visibles |= distances <= close_distance
            
        # ----------------------------------------------------------------------------------------------------
        # And when properly oriented
        
        if normals is not None:
            vs = verts - self.location
            visibles &= np.einsum('...i, ...i', vs, normals) < 0

        # ----------------------------------------------------------------------------------------------------
        # Return visibility and distances
        
        return visibles, distances
    
    # =============================================================================================================================
    # Demonstration
    
    @staticmethod
    def demo(count=100000, size=1000, seed=0):
        
        from geonodes.core.instances import Instances
        from geonodes.core.mesh import Mesh
        
        rng = np.random.default_rng(seed)
        
        verts = rng.uniform(-size, size, (count, 3))
        verts[..., 2] = 0
        
        radius = rng.uniform(.1, 3, count)
        
        def update(eng):
            visibles, _ = Camera().visible_verts(verts, radius, close_distance=None, max_distance=500)
            scale = np.empty_like(verts[visibles])
            scale[:] = radius[visibles, None]
            insts = Instances(verts[visibles], models=Mesh.IcoSphere(), Scale=scale)
            insts.to_object("Camera Culling")
            
        engine.go(update)
        

# =============================================================================================================================      
# Old stuff
        
        
class OLD:        
    
    # ----------------------------------------------------------------------------------------------------
    # Angle of a meter at a given location 
    # arctan2(1, distance)
    
    def meter_angle(self, location):

        if isinstance(location, Vector) or np.shape(location) == (3,):
            return np.arctan2(1, (self.location - Vector(location)).length)
        
        else:
            return np.arctan2(1, np.linalg.norm(location - self.location, axis=-1))
    
    # ----------------------------------------------------------------------------------------------------
    # Size of a meter in pixels
    
    def meter_size(self, location):
        return self.meter_angle(location)/(self.focal_angle/self.resolution)
    

    # ----------------------------------------------------------------------------------------------------
    # Resolution from meter_size
    
    def get_resolution(self, locations):
        
        if self.force_resolution is None:
            
            # Size of a meter in rendered pixels
            
            ms = np.clip(self.meter_size(locations), 1, 1000)
            
            return np.power(10, -np.round(np.log10(ms)))
            
            #return 10**np.round(-np.min(3, np.log10(np.max(1, ms)))), 

        else:
            return self.force_resolution
    
        

            

    # ----------------------------------------------------------------------------------------------------
    # Normalized vector representing the direction of an observed object
    # Direction at the center of the camera is (0, 0, -1)
    
    def obs_direction(self, location):
        return (self.camera.matrix_world.inverted() @ (Vector(location) - self.world_location).resized(4)).resized(3).normalized()

    # ----------------------------------------------------------------------------------------------------
    # Relative location of points in the camera observation referential frame
    
    def obs_locations(self, locations):
        if isinstance(locations, (Vector, tuple)):
            locs = np.ones((1, 4), float)
            locs[0, :3] = locations
        else:
            locs = np.ones((len(locations), 4), float)
            locs[:, :3] = locations
            
        m = np.array(self.camera.matrix_world.inverted())
        
        return np.array(np.einsum('...jk, ...k', m, locs)[:, :3])

    # ----------------------------------------------------------------------------------------------------
    # Angle of an observed location with the direction (0, 0, -1) of the camera

    def obs_angle(self, location):
        return Vector((0, 0, -1)).angle(self.obs_direction(location))
    
    # ----------------------------------------------------------------------------------------------------
    # Distance of a location to the camera
    
    def distance(self, location):   
        
        if isinstance(location, Vector) or np.shape(location) == (3,):
            return (self.world_location - Vector(location)).length
        
        else:
            return np.linalg.norm(location - self.world_location, axis=-1)
    
    # ====================================================================================================
    # Number of pixel for length at distance
    
    # ----------------------------------------------------------------------------------------------------
    # Screen size
    
    @property
    def screen_size(self):
        return 1920/2/np.tan(self.focal_angle/2)
    
    # ----------------------------------------------------------------------------------------------------
    # Size in pixels
    
    def pix_size(self, location):
        return self.screen_size/self.distance(location)
    

        

    # ----------------------------------------------------------------------------------------------------
    # Quads are visible
    # Quads are given by their four corners
    # - corners:  (n, 4, 3)
    # - normals: (n, 3)
    # Return indices of the visible quads

    def visible_quads(self, corners, normals=None, return_projs=False):

        # ----------------------------------------------------------------------------------------------------
        # The projection rectangle
        # The plane is horizontal. All z<0 are identical

        c0, c1, c2, c3 = self.camera.data.view_frame(scene=bpy.context.scene)

        margin = 1.2
        cam_x0 = min(c0.x, c1.x, c2.x, c3.x)*margin
        cam_x1 = max(c0.x, c1.x, c2.x, c3.x)*margin
        cam_y0 = min(c0.y, c1.y, c2.y, c3.y)*margin
        cam_y1 = max(c0.y, c1.y, c2.y, c3.y)*margin

        cam_z = c0.z

        if False:
            print("-"*80)
            print(f"CAMERA SHAPE: plane z = {cam_z:.1f}")
            print(f"   x: {cam_x0:5.1f} {cam_x1:5.1f}")
            print(f"   y: {cam_y0:5.1f} {cam_y1:5.1f}")
            print()

        # ----------------------------------------------------------------------------------------------------
        # Rotate the points in the camera frame
        
        M = np.array(self.camera.matrix_world.inverted())
        pts = np.array(np.einsum('...jk, ...k', M, np.insert(corners, 3, 1, axis=-1))[..., :3])

        # ---------------------------------------------------------------------------
        # Exclude volumes where all 4 points are >= cam_z

        i_vis = np.where(np.bincount(np.where(pts[..., 2] <= cam_z)[0]) != 0)[0]
        if len(i_vis) == 0:
            return np.zeros(0, int), np.zeros((0, 2), float)
        pts = pts[i_vis]

        # ---------------------------------------------------------------------------
        # Project the points on the plane z = cam_z

        pts = cam_z*(pts/np.expand_dims(pts[..., 2], axis=-1))[..., :2]

        # ---------------------------------------------------------------------------
        # Ok when one point is in the projection frame

        oks = np.zeros(len(pts), bool)

        in_frame = np.unique(np.where(np.logical_and(
                np.logical_and(
                    pts[..., 0] >= cam_x0,
                    pts[..., 0] <= cam_x1),
                np.logical_and(
                    pts[..., 1] >= cam_y0,
                    pts[..., 1] <= cam_y1),
                ))[0])
        
        oks[in_frame] = True

        # ---------------------------------------------------------------------------
        # If no point is visible, the camera can be close to the quad surface

        centers = np.average(pts, axis=1)
        radius  = np.max(np.linalg.norm(pts - np.reshape(centers, (len(pts), 1, 2)), axis=-1), axis=-1)

        in_circles = np.where(np.logical_or(
            np.logical_or(
                np.linalg.norm(centers - (cam_x0, cam_y0), axis=-1) < radius,
                np.linalg.norm(centers - (cam_x1, cam_y0), axis=-1) < radius),
            np.logical_or(
                np.linalg.norm(centers - (cam_x1, cam_y1), axis=-1) < radius,
                np.linalg.norm(centers - (cam_x0, cam_y1), axis=-1) < radius)
            ))[0]
        
        oks[in_circles] = True

        # ---------------------------------------------------------------------------
        # Final indices of quads in the filed of view

        i_vis = i_vis[oks]
        if return_projs:
            pts = pts[oks]
            
        if len(i_vis) > 0:

            # ----- We need centers below
    
            centers = centers[oks]
            
            # ---------------------------------------------------------------------------
            # Faces orientation
            #
            # NOT YET WORKING ?
            
            if normal is not None:
                centers = np.average(corners[i_vis], axis=1)
                oks = self.back_face(centers, normals[i_vis])
                i_vis = i_vis[oks]
                if return_projs:
                    pts = pts[oks]
                
                
        if return_projs:
            return i_vis, np.array(pts)
        else:
            return i_vis    
    
    
    # ----------------------------------------------------------------------------------------------------
    # Bounds are visible
    # Bounds is an np array shaped (n, 2, 3) or (n, 8, 3) where n is the number of bounds to check 
    
    def bounds_visible(self, bounds):
        
        single = len(np.shape(bounds)) == 2
        if single:
            bounds = np.reshape(bounds, (1,) + np.shape(bounds))
        
        visibles = np.zeros(len(bounds), bool)
        
        if self.force_visible:
            visibles[:] = True
            if single:
                return visibles[0]
            else:
                return visibles

        # ---------------------------------------------------------------------------
        # The projection rectangle
        # The plane is horizontal. All z<0 are identical
        
        c0, c1, c2, c3 = self.camera.data.view_frame(scene=bpy.context.scene)
        
        margin = 1.2
        cam_x0 = min(c0.x, c1.x, c2.x, c3.x)*margin
        cam_x1 = max(c0.x, c1.x, c2.x, c3.x)*margin
        cam_y0 = min(c0.y, c1.y, c2.y, c3.y)*margin
        cam_y1 = max(c0.y, c1.y, c2.y, c3.y)*margin
        
        cam_z = c0.z
        
        if False:
            print("-"*80)
            print(f"CAMERA SHAPE: plane z = {cam_z:.1f}")
            print(f"   x: {cam_x0:5.1f} {cam_x1:5.1f}")
            print(f"   y: {cam_y0:5.1f} {cam_y1:5.1f}")
            print()
        
        # ---------------------------------------------------------------------------
        # Rotate the points in the camera frame
        
        M = np.array(self.camera.matrix_world.inverted())
        rots = np.array(np.einsum('...jk, ...k', M, np.insert(bounds, 3, 1, axis=-1))[..., :3])
        
        # ---------------------------------------------------------------------------
        # Build the 8 points per volume
        
        if rots.shape[1] == 8:
            pts = rots
            
        else:
            pts = np.empty((len(rots), 8, 3), float)
            
            for i in range(8):
                pts[:, i, 0] = rots[:, (i//2)    %2, 0]
                pts[:, i, 1] = rots[:, ((i+1)//2)%2, 1] 
                pts[:, i, 2] = rots[:, i//4        , 2]

            del rots
            
        if False:
            for ip in range(len(pts)):
                print("Point", ip)
                for i in range(8):
                    print(f"   {i}: {pts[ip, i, 0]:5.1f} {pts[ip, i, 1]:5.1f} {pts[ip, i, 2]:5.1f}")
                
        # ---------------------------------------------------------------------------
        # Exclude volumes where all 8 points are >= cam_z
        
        i_vis = np.where(np.bincount(np.where(pts[..., 2] <= cam_z)[0]) != 0)[0]

        if len(i_vis) == 0:
            return visibles
        
        # ---------------------------------------------------------------------------
        # Project the points on the plane z = cam_z
        
        projs = cam_z*(pts[i_vis]/np.expand_dims(pts[i_vis, :, 2], axis=-1))
        
        # ---------------------------------------------------------------------------
        # Ok when one point is in the projection frame
        
        i_ok0 = np.unique(np.where(np.logical_and(
                np.logical_and(
                    projs[..., 0] >= cam_x0,
                    projs[..., 0] <= cam_x1),
                np.logical_and(
                    projs[..., 1] >= cam_y0,
                    projs[..., 1] <= cam_y1),
                ))[0])
                
        if len(i_ok0) > 0:
            visibles[i_vis[i_ok0]] = True
        
        # ---------------------------------------------------------------------------
        # If no point is visible, the camera can be close to the volume
        # Let's build the circle including the projected points and let's see if the
        # camera is inside it
        
        rem = np.ones(len(projs), bool)
        rem[i_ok0] = False
        i_rem = np.array(np.arange(len(projs))[rem])
        del rem
        
        if len(i_rem) == 0:
            return visibles
        
        # ----- Let's pass in 2D
        
        projs = np.array(projs[i_rem][..., :2])

        centers = np.average(projs, axis=1)
        radius  = np.max(np.linalg.norm(projs - np.reshape(centers, (len(projs), 1, 2)), axis=-1), axis=-1)
        
        
        i_ok1 = np.where(np.logical_or(
            np.logical_or(
                np.linalg.norm(centers - (cam_x0, cam_y0), axis=-1) < radius,
                np.linalg.norm(centers - (cam_x1, cam_y0), axis=-1) < radius),
            np.logical_or(
                np.linalg.norm(centers - (cam_x1, cam_y1), axis=-1) < radius,
                np.linalg.norm(centers - (cam_x0, cam_y1), axis=-1) < radius)
            ))[0]
            
        if len(i_ok1) > 0:
            visibles[i_vis[i_ok1]] = True
            
        if single:
            return visibles[0]
        else:
            return visibles
    
    # ----------------------------------------------------------------------------------------------------
    # An object is visible
    
    def object_is_visible(self, obj):
        
        bounds = np.array(obj.bound_box)
        bounds += obj.matrix_world.translation
        
        return self.bounds_visible(bounds)[0]
    
    # ----------------------------------------------------------------------------------------------------
    # Face is seen from the back
    
    def back_face(self, center, normal):
        
        if np.shape(center) == (3,):
            return (Vector(center) - self.world_location).dot(Vector(normal)) >= -0.01
        
        else:
            #return np.einsum('...i, ...i', center - self.world_location, normal) >= -0.01
            return np.einsum('...i, ...i', center - self.world_location, normal) <= 0.01
        
    # ----------------------------------------------------------------------------------------------------
    # Set two attributes to mesh vertices:
    # - visible (bool)   : vertex is visible
    # - distance (float) : distance to the camera
    
    def set_mesh_attributes(self, obj, prefix='cam '):
        
        mesh = obj.data
        verts = np.empty(len(mesh.vertices)*3)
        mesh.vertices.foreach_get('co', verts)
        verts = np.reshape(verts, (len(mesh.vertices), 3))
        
        # ----- Resulting arrays
        
        v_vis = np.ones(len(verts), bool)
        
        # ----------------------------------------------------------------------------------------------------
        # The projection rectangle
        # The plane is horizontal. All z<0 are identical

        c0, c1, c2, c3 = self.camera.data.view_frame(scene=bpy.context.scene)

        margin = 1.2
        cam_x0 = min(c0.x, c1.x, c2.x, c3.x)*margin
        cam_x1 = max(c0.x, c1.x, c2.x, c3.x)*margin
        cam_y0 = min(c0.y, c1.y, c2.y, c3.y)*margin
        cam_y1 = max(c0.y, c1.y, c2.y, c3.y)*margin

        cam_z = c0.z

        if False:
            print("-"*80)
            print(f"CAMERA SHAPE: plane z = {cam_z:.1f}")
            print(f"   x: {cam_x0:5.1f} {cam_x1:5.1f}")
            print(f"   y: {cam_y0:5.1f} {cam_y1:5.1f}")
            print()

        # ----------------------------------------------------------------------------------------------------
        # Rotate the points in the camera frame
        
        M = np.array(self.camera.matrix_world.inverted())
        verts = (np.matmul(M, np.insert(verts, 3, 1, axis=-1).T).T)[..., :3]
        
        v_dst = np.linalg.norm(verts, axis=-1)
        

        # ---------------------------------------------------------------------------
        # Only points vers z >= cam_z
        
        v_vis[verts[:, 2] > 0] = False
        
        # ---------------------------------------------------------------------------
        # Project the points on the plane z = cam_z

        verts = cam_z*(verts/np.expand_dims(verts[:, 2], axis=-1))
        
        # ----- In the screen
        
        v_vis[verts[:, 0] < cam_x0] = False
        v_vis[verts[:, 0] > cam_x1] = False
        v_vis[verts[:, 1] < cam_y0] = False
        v_vis[verts[:, 1] > cam_y1] = False
        
        v_layer = mesh.vertex_layers_int.new(name=f"{prefix}visible")
        v_layer.data.foreach_set('value', v_vis)
        
        del v_vis, verts

        v_layer = mesh.vertex_layers_float.new(name=f"{prefix}distance")
        v_layer.data.foreach_set('value', v_dst)
        
        del v_dst
        
        mesh.update()
        
    # ====================================================================================================
    # Frame range
    
    @classmethod
    def frame_range(cls, frames, func, message=None):
        
        if frames is None:
            func()
            return
        
        if message is not None:
            timer = Timer(message, len(frames), delta=30)
        
        cur_frame = bpy.context.scene.frame_current
        
        i = 0
        for frame in frames:
            if message is not None:
                timer.track(i)
            i += 1
            
            bpy.context.scene.frame_set(frame)
            func()
            
        if message is not None:
            timer.done()
            
        bpy.context.scene.frame_set(cur_frame)
        
    
    # ====================================================================================================
    # Test

    def TEST_VISIBILITY(self, objects, materials=("Blue", "Red", "Black")):
        
        # ---------------------------------------------------------------------------
        # Utility that change the object depending on its visibility
        # - Visible / not visible change the whole color
        # - For visible objects:
        #   - Faces color are changed when back_face
        #   - If a subdivision modifier exists, change its level based on the distance to the camera
        
        def change_obj(obj, visible):
            obj.data.materials.clear()
            for mat in materials:
                obj.data.materials.append(bpy.data.materials[mat])
            
            for poly in obj.data.polygons:
                if visible:
                    if self.back_face(obj.matrix_world.translation + poly.center, poly.normal):
                        poly.material_index = 2
                    else:
                        poly.material_index = 0
                else:
                    poly.material_index = 1
                    
            # Adjust the subdivision level based on the meter size in pixel
                    
            mod = obj.modifiers.get("Subdivision")
            if mod is not None:
                if visible:                
                    ms = self.meter_size(obj.matrix_world.translation)
                    a = 1.5
                    if ms >= 50*a**5:
                        mod.levels = 6
                    elif ms >= 50*a**4:
                        mod.levels = 5
                    elif ms >= 50*a**3:
                        mod.levels = 4
                    elif ms >= 50*a**2:
                        mod.levels = 3
                    elif ms >= 50*a:
                        mod.levels = 2
                    elif ms >= 50:
                        mod.levels = 1
                    else:
                        mod.levels = 0
                else:
                    mod.levels = 0
                    
        # ---------------------------------------------------------------------------
        # The update function
        
        def update(scene=None):
            count = len(objects)
            
            bounds = np.zeros((count, 8, 3))
            for i, obj in enumerate(objects):
                bounds[i] = np.array(obj.bound_box)
                bounds[i] += obj.matrix_world.translation
                
            visibles = self.bounds_visible(bounds)

            for obj, vis in zip(objects, visibles):
                change_obj(obj, vis)
                
        for obj in objects:
            print(obj.name, self.object_is_visible(obj))

        # ---------------------------------------------------------------------------
        # Let's test
                
        update()
        engine.go(update)
        

        
    
        
        