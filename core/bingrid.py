#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Tue Nov 22 18:27:23 2022

@author: alain.bernard
@email: alain@ligloo.net

-----
A binary grid is a grid with a variable resolution, adapted to the camera.

A BinGrid uses a grid shape of int coordinates and a function return a vertex per couple of coordinates.
Depending on the needs, each elementary square can be subdivided up to a maximum number of subdivisions.

"""


import numpy as np

import bpy

from geonodes.core import blender
from geonodes.core.cached_array import CachedArray
from geonodes.core.camera import Camera
from geonodes.core import attributes
from geonodes.core import engine

QUICK = True
 
# =============================================================================================================================
# Binary grid  
#

class BinGrid:
    """ Binary Grid
    
    A binary grid is a multi resolution grid allowing to add geometry locally.
    
    It is initialized as a grid of square faces the side of which being a power of 2.
    The faces can be subidvided up to the exponent of two.
    
    Arguments
    ---------
        - shape (int, int): the total shape of the grid
        - func (func(coords) -> vertices): the function returning the vertices from an array of int coordinates
        - subdivisions (int): the initial subdivision    
    """
    
    def __init__(self, shape, func, subdivision=3):
        
        self.shape = shape
        self.func  = func
        
        self.subdivision = subdivision
        self.face_side   = 1 << subdivision
        self.faces_shape = shape[0] >> subdivision, shape[1] >> subdivision
        self.verts_shape = self.faces_shape[0] + 1, self.faces_shape[1] + 1

        # ---------------------------------------------------------------------------
        # Compute the vertices of the base grid
        
        vi, vj = np.meshgrid(
            np.arange(0, self.shape[0] + 1, self.face_side),
            np.arange(0, self.shape[1] + 1, self.face_side),
            indexing = 'ij',
            sparse = True,
            )
        coords = np.empty(self.verts_shape + (2,), int)
        coords[..., 0] = vi
        coords[..., 1] = vj
        
        self.base_verts = self.func(coords)
        del vi, vj, coords
        
        # ---------------------------------------------------------------------------
        # Divisions to store the target subdivisions of faces
        
        self.divs    = np.zeros(self.faces_shape, int)
        self.no_face = np.zeros(self.faces_shape, bool)
        
        # ---------------------------------------------------------------------------
        # A subdivided grid makes use of templates
        # Only from 2 since below, there are no internal faces
        #
        # 2: internal grid of 2x2 faces of side = face_side // 2
        # n: internal grid of 2**n-2 x 2**n-2 faces of side = face_side // 2**(n-1)
        
        self.templates = []
        for dv in range(2, self.subdivision + 1):
            
            f_shape = (1<<dv) -  2
            v_shape = f_shape + 1
            side    = self.face_side >> dv
            
            #print("dv", dv, "v", v_shape, "f", f_shape,"side", side)
            
            # ----- Vertices
            
            vi, vj = np.meshgrid(
                np.arange(1, v_shape+1)*side,
                np.arange(1, v_shape+1)*side,
                indexing = 'ij',
                sparse = True,
                )
            
            coords = np.empty((v_shape, v_shape, 2), int)
            coords[..., 0] = vi
            coords[..., 1] = vj
            
            # ----- Sides
            
            sides    = np.zeros((4, f_shape+1), int)
            
            sides[0] = np.arange(0, f_shape+1)*(f_shape+1) 
            sides[1] = np.arange(0, f_shape+1) + (f_shape+1)*f_shape
            sides[2] = np.arange(0, f_shape+1)*(f_shape+1) + f_shape
            sides[3] = np.arange(0, f_shape+1)
            
            # ----- corners
            
            corners = np.array([0, f_shape*(f_shape+1), (f_shape+1)*(f_shape+1)-1, f_shape])
            
            # Note that corners = side[0][0], side[0][-1], side[2][-1], side[2][0]
            
            # ----- Internal faces
            
            faces = np.zeros((f_shape, f_shape, 4), int)
            for i in range(f_shape):
                for j in range(f_shape):
                    if False:
                        faces[i, j, 0] = i   + j*v_shape
                        faces[i, j, 1] = i+1 + j*v_shape
                        faces[i, j, 2] = i+1 + (j+1)*v_shape
                        faces[i, j, 3] = i   + (j+1)*v_shape
                    else:
                        faces[i, j, 0] = i*v_shape     + j
                        faces[i, j, 1] = (i+1)*v_shape + j
                        faces[i, j, 2] = (i+1)*v_shape + j+1
                        faces[i, j, 3] = i*v_shape     + j+1
                        
            # ----- Store the template
                    
            self.templates.append({
                'coords'  : np.reshape(coords, (v_shape*v_shape, 2)),
                'faces'   : np.reshape(faces, (f_shape*f_shape, 4)),
                'f_shape' : f_shape,
                'sides'   : sides,
                'corners' : corners,
                })
            
    # ----------------------------------------------------------------------------------------------------
    # Representation
    
    def __str__(self): 
        return f"<BinGrid of shape {self.shape}, faces: {self.faces_shape}, vertices: {self.verts_shape}>"
    
    # ====================================================================================================
    # Reset the divisions
    
    def reset(self):
        """ Reset the subdivisions to zero.
        """
        
        self.divs[:]    = 0
        self.no_face[:] = 0
        
    # ====================================================================================================
    # From an "altitude" function
    
    @classmethod
    def Altitude(cls, shape, alt_func, unit_size=1., center=(0, 0), subdivision=3):
        """ BinGrid constructor with an altitude function.
        
        The standard constructor expect a function return a vertex for each couple of coordinates.
        The altitude function return a single float, the altitude, for each couple of coordinates.
        
        Arguments
        ---------
            - shape (int, int): the total shape of the grid
            - func (func(coords) -> float): the function returning the altitudes from an array of int coordinates
            - subdivisions (int): the initial subdivision
            
        Returns
        -------
            - BinGrid
        """
        
        def func(coords):
            target_shape = np.shape(coords)[:-1]
            cf = np.reshape(coords, (np.size(coords)//2, 2))
            
            x = (center[0] - shape[0]*unit_size/2) + cf[:, 0]*unit_size
            y = (center[1] - shape[1]*unit_size/2) + cf[:, 1]*unit_size
            return np.reshape(np.c_[x, y, alt_func(cf)], target_shape + (3,))
        
        return cls(shape, func, subdivision=3)
        

    # ====================================================================================================
    # Adapt the resolution to the camera

    def camera_adapt(self, camera, side_in_pixels=10, margin=1.05, close_distance=None, frame_range=None):
        """ Adapt the subdivisions to the camera.
        
        Step 1:
            Get the visibility and the distances of the base vertices
            Select the faces with at least one visible corner
            
        Step 2:
            Get the meter size in pixels at the face distances
            Note: the distance is the one of one face vertex, not the minimum of the four corners
            The face size is 2**n times this size:
                face_size = meter_size * 2**n
            The maximum face size is given in argument. We must divide the face by a factor div:
                div = max/face_size
                div = max/meter_size * 2**(-n)
            This gives:
                ln2(div) = ln2(max/meter_size) - n
                
            The subdivision dv is equal to:
                dv = n - ln2(max/meter_size)
                
        Arguments
        ---------
            - camera (Camera) : Camera
            - side_in_pixels (float = 10) : target pixels size for the square sides
            - margin (float = 1.05) : camera margin
            - close_distance (float = None) : maximum resolution for close squares
            - frame_range(enumerator) : loop on the frames
        """
        
        render = camera.resolution
        
        # ===========================================================================
        # A range of frames
        
        if frame_range is not None:
            
            print( "------------------------------------------")
            print(f"BinGrid camera adapt in {frame_range}")
            print()
            
            for frame in frame_range:
                bpy.context.scene.frame_set(frame)
                self.camera_adapt(camera, side_in_pixels=side_in_pixels, margin=margin, close_distance=close_distance)
                print(f"--- {frame:3d}...")
            
            print("Camera adapt done")
            print()
            
            return
        
        # ===========================================================================
        # A single frame
        
        vis, dist = camera.visible_verts(self.base_verts, margin = margin, close_distance=close_distance)
        
        f_vis  = np.array(vis[:-1, :-1])
        f_vis += vis[:-1, 1:] 
        f_vis += vis[1:, 1:] 
        f_vis += vis[1:, :-1]
        
        f_dist = dist[:-1, :-1][f_vis]
        
        # DEBUG
        if False:
            rng = np.random.default_rng(0)
            inds = rng.integers(0, len(f_dist), 10)
            sample = f_dist[inds]
            #sample = np.array((10, 100, 1000, 5000, 10000, 20000, 50000))
            print("Camerra adapte SAMPLE, max_face_size", max_face_size, ", face_side:", self.face_side)
            print("Distances:")
            print(sample)
            print("meter_in_pixels")
            print(camera.meter_in_pixels(sample))
            print("Divisions")
            print(np.round(np.log(side_in_pixels/camera.meter_in_pixels(sample))/np.log(2)).astype(int))
        
            #return
        
        self.divs[f_vis] = np.maximum(self.divs[f_vis], np.clip(
            self.subdivision - np.round(np.log(side_in_pixels/camera.meter_in_pixels(f_dist))/np.log(2)).astype(int),
            0, self.subdivision))
    
    # ====================================================================================================
    # Build the Blender object
    
    def to_object(self, obj, uv_scale=1):
        """ Create a Blender Mesh object with grid.
        
        Arguments
        ---------
            - obj (str or Object) : the target
            - uv_scale (float = 1.) : scale to apply to the UVMap
            
        Returns
        -------
            - Object
        """
        
        verbose = None
        
        if verbose is not None:
            print(f"BinGrid '{verbose}' building mesh...")
        
        fside = self.face_side # Shortcut
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # First: create at once the vertices of the base grid
        
        vi, vj = np.meshgrid(
            np.arange(0, self.shape[0] + 1, fside),
            np.arange(0, self.shape[1] + 1, fside),
            indexing = 'ij',
            sparse = True,
            )
        a = np.empty(self.verts_shape + (2,), int)
        a[..., 0] = vi
        a[..., 1] = vj
        del vi, vj

        vcoord_dim = np.shape(a)[1] # used in base_vert function
        
        a = np.reshape(a, (np.size(a)//2, 2))

        if QUICK:
            self.vert_coords = CachedArray.FromArray(a)
        else:
            self.vert_coords = a
        
        # ----------------------------------------------------------------------------------------------------
        # Let's provide a two-dimensional access to these initial vertices indices
        
        def base_vert(i, j):
            return i*vcoord_dim + j
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # The following function builds a column vertical egdes at once
        
        def build_vrt_edges(i_edge):
            
            coords  = []               # Vertices to create
            v_edges = []               # List of edges
            coord_i = i_edge*fside     # For all the created vertices
            
            n = len(self.vert_coords)  # Vertices counter
            coord_j = 0                # To avoid multiplication, not sure it is worth
            
            for j_face in range(np.shape(self.divs)[1]):
                
                # ----- Which level of division ?
                
                # First edge column = division of first column of faces
                
                if i_edge == 0:
                    dv = self.divs[0, j_face]
                    
                # Last edge column = division of last column of faces
                
                elif i_edge == np.shape(self.divs)[0]:
                    dv = self.divs[-1, j_face]
                    
                # General case : the max division between the faces cols sharing the edge column
                    
                else:
                    dv = max(self.divs[i_edge-1, j_face], self.divs[i_edge, j_face])
                    
                # ----- Create the vertices and edges as list of vertex indices
                
                # First and last vertices
                
                n0 = base_vert(i_edge, j_face)
                n1 = base_vert(i_edge, j_face + 1)
                    
                # No division: we simply add an edge with existing vertices
                    
                if dv == 0:
                    v_edges.append([n0, n1])
                    
                # Single division: one vertex at the center
                    
                elif dv == 1:
                    side = fside >> 1
                    v_edges.append([n0, n, n1])
                    
                    coords.extend([(coord_i, coord_j + side)])
                    n += 1
                    
                # Double divisions: 3 intermediary vertices
                    
                elif dv == 2:
                    side = fside >> 2
                    v_edges.append([n0, n, n+1, n+2, n1])
                    
                    coords.extend([
                        (coord_i, coord_j + side), 
                        (coord_i, coord_j + 2*side), 
                        (coord_i, coord_j + 3*side), 
                        ])
                    n += 3
                    
                # More divisions
                    
                else:
                    side = fside >> dv
                    nv = 1 << dv
                    edge = [n+i for i in range(-1, nv)]
                    edge[0]  = n0
                    edge[-1] = n1
                    v_edges.append(edge)
                    
                    coords.extend([(coord_i, coord_j + i*side) for i in range(1, nv)])
                    n += nv - 1
                    
                # ----- For next loop
                    
                coord_j += fside
                
            # ---------------------------------------------------------------------------
            # We take into account the vertices to create
            
            if len(coords) > 0:
                if QUICK:
                    self.vert_coords.append(coords)
                else:
                    self.vert_coords = np.append(self.vert_coords, coords, axis=0)
            
            # ----- We return the edges
                
            return v_edges     
        
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # The following function builds a single horizontal edge
        
        def build_hrz_edge(i_face, j_edge):
            
            # ----- Which level of division ?
            
            if j_edge == 0:
                dv = self.divs[i_face, j_edge]
                
            # Last edge column = division of last column of faces
            
            elif j_edge == np.shape(self.divs)[1]:
                dv = self.divs[i_face, -1]
                
            # General case : the max division between the faces cols sharing the edge column
                
            else:
                dv = max(self.divs[i_face, j_edge-1], self.divs[i_face, j_edge])
                
            # ----- Create the vertices and edges as list of vertex indices
            
            n0 = base_vert(i_face,     j_edge)
            n1 = base_vert(i_face + 1, j_edge)

            n  = len(self.vert_coords)

            coord_i = i_face*fside
            coord_j = j_edge*fside
                
            # No division: we simply reuse existing vertices from surrounding edges
            
            if dv == 0:
                return [n0, n1]
                
            # Single division: one vertex at the center
                
            elif dv == 1:
                side = fside >> 1
                if QUICK:
                    self.vert_coords.append([coord_i + side, coord_j])
                else:
                    self.vert_coords = np.append(self.vert_coords, [[coord_i + side, coord_j]], axis=0)
                return [n0, n, n1]
                
            # Double divisions: 3 more vertices
                
            elif dv == 2:
                side = fside >> 2
                if QUICK:
                    self.vert_coords.append([
                        (coord_i + side,   coord_j), 
                        (coord_i + 2*side, coord_j), 
                        (coord_i + 3*side, coord_j), 
                        ])
                else:
                    self.vert_coords = np.append(self.vert_coords, [
                        (coord_i + side,   coord_j), 
                        (coord_i + 2*side, coord_j), 
                        (coord_i + 3*side, coord_j), 
                        ], axis=0)
                return [n0, n, n+1, n+2, n1]
                
            # More divisions
                
            else:
                side = fside >> dv
                nv = 1 << dv
                if QUICK:
                    self.vert_coords.append([(coord_i + i*side, coord_j) for i in range(1, nv)])
                else:
                    self.vert_coords = np.append(self.vert_coords,
                        [(coord_i + i*side, coord_j) for i in range(1, nv)],
                        axis=0)
                edge = [n + i for i in range(-1, nv)]
                edge[0]  = n0
                edge[-1] = n1
                return edge
            
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # The following function returns a sub edge from a full edge
        
        def sub_edge(edge, div, index, inverse=False):
            
            part_length = (len(edge)-1) >> div
            
            se = edge[index*part_length:index*part_length + part_length + 1]
            
            if inverse:
                se.reverse()
                
            return se
            
        # ----------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------
        # Main
        
        f_sizes   = []
        f_corners = []
        
        def add_face(face):
            f_sizes.append(len(face))
            f_corners.extend(face)
                
        def extend_faces(new_faces):
            f_sizes.extend([np.shape(new_faces)[-1]]*len(new_faces))
            f_corners.extend(list(new_faces.flatten()))
        
        # ---------------------------------------------------------------------------
        # Horizontal loop
        
        # ----- Initialize the left most edges
        
        right_edges = build_vrt_edges(0)
        
        for i_face in range(np.shape(self.divs)[0]):
            
            # For the vertical loop, we'll reuse the right edges of the previous loop
            
            left_edges = right_edges
            
            # Let's build the right edges
            
            right_edges = build_vrt_edges(i_face+1)
            
            # ---------------------------------------------------------------------------
            # Vertical loop
            
            # ----- Initialize the bottom edge
            
            top_edge = build_hrz_edge(i_face, 0)
            
            for j_face in range(np.shape(self.divs)[1]):
                
                
                left_edge  = left_edges[j_face]
                right_edge = right_edges[j_face]
                
                bot_edge = top_edge
                top_edge = build_hrz_edge(i_face, j_face + 1)
                
                # ---------------------------------------------------------------------------
                # ----- We have the four edges, we can build the faces
                # if the face has to be built
                
                if self.no_face[i_face, j_face]:
                    continue
                
                dv = self.divs[i_face, j_face]
                
                coord_i = i_face*fside
                coord_j = j_face*fside
                
                # ---------------------------------------------------------------------------
                # No subdivision: create a single face with the four edges
                
                if dv == 0:
                    face = bot_edge[:-1]
                    face.extend(right_edge[:-1])
                    face.extend([i for i in reversed(top_edge[1:])])
                    face.extend([i for i in reversed(left_edge[1:])])
                    
                    add_face(face)
                    
                # ---------------------------------------------------------------------------
                # A single subdivision: create a central point and four faces
                    
                elif dv == 1:
                    
                    # ---- Add a central point
                    n = len(self.vert_coords)
                    if QUICK:
                        self.vert_coords.append([[coord_i + (fside>>1), coord_j + (fside>>1)]])
                    else:
                        self.vert_coords = np.append(self.vert_coords, 
                            [[coord_i + (fside>>1), coord_j + (fside>>1)]],
                            axis=0)
                    
                    # ----- The four faces
                    
                    # Bottom left
                    
                    face = sub_edge(bot_edge, 1, 0)
                    face.append(n)
                    face.extend(sub_edge(left_edge, 1, 0, True)[:-1])
                    add_face(face)
                    
                    # Bottom right
                
                    face = sub_edge(bot_edge, 1, 1)
                    face.extend(sub_edge(right_edge, 1, 0)[1:])
                    face.append(n)
                    add_face(face)
                    
                    # Top right
                
                    face = sub_edge(right_edge, 1, 1)
                    face.extend(sub_edge(top_edge, 1, 1, True)[1:])
                    face.append(n)
                    add_face(face)
                    
                    # Top left
                    
                    face = sub_edge(top_edge, 1, 0, True)
                    face.extend(sub_edge(left_edge, 1, 1, True)[1:])
                    face.append(n)
                    add_face(face)
                    
                # ---------------------------------------------------------------------------
                # More subidivions: let's use a template
                    
                else:
                    template = self.templates[dv-2]
                    
                    # ----- Add the central grid
                    
                    n = len(self.vert_coords)
                    if QUICK:
                        self.vert_coords.append(template['coords'] + (i_face*fside, j_face*fside))
                    else:
                        self.vert_coords = np.append(self.vert_coords, template['coords'] + (i_face*fside, j_face*fside), axis=0)

                    extend_faces(template['faces'] + n)
                        
                    # ----- The corner faces
                    
                    ilast = (1<<dv) - 1
                    
                    # Bottom left
                    
                    face = sub_edge(bot_edge, dv, 0)
                    face.append(template['corners'][0] + n)
                    face.extend(sub_edge(left_edge, dv, 0, True)[:-1])
                    add_face(face)
                    
                    # Bottom right
                    
                    face = sub_edge(bot_edge, dv, ilast)
                    face.extend(sub_edge(right_edge, dv, 0)[1:])
                    face.append(template['corners'][1] + n)
                    add_face(face)
                    
                    # Top left
                
                    face = sub_edge(right_edge, dv, ilast)
                    face.extend(sub_edge(top_edge, dv, ilast, True)[1:])
                    face.append(template['corners'][2] + n)
                    add_face(face)
                    
                    # Top right
                    
                    face = sub_edge(top_edge, dv, 0, True)
                    face.extend(sub_edge(left_edge, dv, ilast, True)[1:])
                    face.append(template['corners'][3] + n)
                    add_face(face)
                    
                    # ----- The side faces
                    
                    f_shape = template['f_shape']
                    sides   = template['sides'] + n
                    
                    for i in range(f_shape):
                        
                        # Bottom
                        
                        face = sub_edge(bot_edge, dv, i+1)
                        face.extend([sides[0][i+1], sides[0][i]])
                        add_face(face)
                        
                        # Right
                        
                        face = sub_edge(right_edge, dv, i+1)
                        face.extend([sides[1][i+1], sides[1][i]])
                        add_face(face)
                        
                        # Top
                        
                        face = sub_edge(top_edge, dv, i+1, True)
                        face.extend([sides[2][i], sides[2][i+1]])
                        add_face(face)
                        
                        # Left
                        
                        face = sub_edge(left_edge, dv, i+1, True)
                        face.extend([sides[3][i], sides[3][i+1]])
                        add_face(face)
                
        # ----------------------------------------------------------------------------------------------------
        # We can now build the object
        
        # ----- Compute the vertices
        
        if QUICK:
            verts = self.func(self.vert_coords.a)
        else:
            verts = self.func(self.vert_coords)

        if verbose is not None:
            print(f"BinGrid '{verbose}' to object: {len(verts)} vertices...")
        
        # ----- Build the object
        
        obj = blender.create_mesh_object(obj)
        
        mesh = obj.data
        mesh.clear_geometry()
            
        # Vertices
        mesh.vertices.add(len(verts))
        mesh.vertices.foreach_set('co', verts.flatten())
        
        # Corners
        mesh.loops.add(len(f_corners))
        mesh.loops.foreach_set("vertex_index", f_corners)
        
        # Faces
        ofs = np.roll(np.cumsum(f_sizes), 1)
        ofs[0] = 0
        mesh.polygons.add(len(f_sizes))
        mesh.polygons.foreach_set("loop_start", ofs)
        mesh.polygons.foreach_set("loop_total", f_sizes)
        
        # UV Map
        attributes.create_vector2_attribute(mesh, 'UVMap', domain='CORNER', value=self.vert_coords[f_corners]*uv_scale)
        
        # We are good ;-)
        
        mesh.update()
        
        return obj
    
       
    
    # ====================================================================================================
    # A demo based on a cylinder
    
    @classmethod
    def Cylinder(cls, subdivision=3, radius=8, length=25, resolution=(7, 12)):
        
        i_dim  = resolution[0]*(1<<subdivision)
        j_dim  = resolution[1]*(1<<subdivision)
        
        #circ   = 50
        #radius = circ/2/np.pi
        #length = 10
        
        def cylinder(coords):
            
            v = np.empty(np.shape(coords)[:-1] + (3,), float)

            ag = coords[..., 1]/j_dim*2*np.pi - np.pi
            
            v[..., 0] = coords[..., 0]/i_dim*length - length/2
            v[..., 1] = radius*np.cos(ag)
            v[..., 2] = radius*np.sin(ag)
            
            return v
        
        return cls((i_dim, j_dim), func=cylinder, subdivision=subdivision)
    
    # ====================================================================================================
    # A screen to debug
    
    @classmethod
    def Screen(cls, subdivision=3):
        
        i_dim  = 1<<subdivision
        j_dim  = 1<<subdivision
        
        def screen(coords):

            v = np.empty(np.shape(coords)[:-1] + (3,), float)
            
            v[..., 0] = coords[..., 0] - i_dim//2
            v[..., 1] = 0
            v[..., 2] = coords[..., 1] - j_dim//2
            
            return v
        
        return cls((i_dim, j_dim), func=screen, subdivision=subdivision)
    
    # ====================================================================================================
    # A flat plane
    
    @classmethod
    def Plane(cls, subdivision=3):
        
        i_dim  = 100 * (1<<subdivision)
        j_dim  = 100 * (1<<subdivision)
        
        def plane(coords):

            v = np.empty(np.shape(coords)[:-1] + (3,), float)
            
            v[..., 0] = coords[..., 0] - i_dim//2
            v[..., 1] = coords[..., 1] - j_dim//2
            v[..., 2] = 0
            
            return v
        
        return cls((i_dim, j_dim), func=plane, subdivision=subdivision)
    
    @staticmethod
    def demo(subdivision=3):
        
        rng = np.random.default_rng(0)
        C = rng.uniform(-2000, 2000, (10, 2))
        W = rng.normal(50, 10, 10,)
        A = rng.normal(10, 3, 10,)
        
        def altitude(coords):
            h = np.zeros(np.shape(coords)[:-1])
            for c, w, a in zip(C, W, A):
                d = np.linalg.norm(coords - c, axis=-1)
                h += a*np.sin(d/w)
            return h
        
        
        i_dim  = 100 * (1<<subdivision)
        j_dim  = 100 * (1<<subdivision)
        
        bg = BinGrid.Altitude((i_dim, j_dim), altitude, subdivision=subdivision)
        
        def update(eng):
            bg.reset()
            bg.camera_adapt(Camera())
            bg.to_object("BinGrid Demo")
            
        engine.go(update)
            
    @staticmethod
    def demo_plane(subdivision=3):
        
        plane = BinGrid.Plane(subdivision=subdivision)
        
        def update(eng):
            plane.reset()
            plane.camera_adapt(Camera())
            plane.to_object("BinGrid Demo")
            
        engine.go(update)
            
            
            
    
    
    

    
    

