#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov 10 11:50:13 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Mesh geometry.

"""

import bpy
from mathutils.bvhtree import BVHTree
from mathutils import Vector
import bmesh

from contextlib import contextmanager
import numpy as np


from geonodes.maths.transformations import Transformations, tracker

from geonodes.core import blender
from geonodes.core import topology
from geonodes.core.geometry import Geometry
from geonodes.core.domain import PointDomain, CornerDomain, FaceDomain, reduce_indices


DATA_TEMP_NAME = "GEOPY_TEMP"

# =============================================================================================================================
# Mesh Gemetry

class Mesh(Geometry):

    def __init__(self, verts=None, corners=None, sizes=None, materials=None, **attrs):
        """ Mesh Geometry.

        Arguments
        ---------
            - verts (array of vectors = None) : the vertices
            - corners (array of ints = None) : corners, i.e. indices on the array of points
            - sizes (array of ints = None) : size of the faces, the sum of this array must be equal to the length of the corners array
            - materials (str or list of strs = None) : list of materials used in the geometry
            - **attrs (dict) : other geometry attributes
        """

        # ----- Initialize an empty geometry

        self.points  = PointDomain.New()
        self.corners = CornerDomain.New(points=self.points)
        self.faces   = FaceDomain.New(corners=self.corners)
        self._edges  = None

        # ----- The materials

        if materials is None:
            self.materials = []
        elif isinstance(materials, str):
            self.materials = [materials]
        else:
            self.materials = [mat for mat in materials]

        # ----- Fill the geometry

        if verts is None:
            return

        # Vertices

        self.points.add_points(verts, **attrs)

        # Corners is provided, we need the size of the faces

        if corners is not None:

            # Sizes is not provided, the corners must be properly shaped

            if sizes is None:
                if len(np.shape(corners)) < 2:
                    raise RuntimeError(f"Mesh init error: 'sizes' is not provided, 'corners' must be shaped (n, size), not flat: {np.shape(corners)}")

                size  = np.shape(corners)[-1]
                sizes = np.ones(np.size(corners)//size)*size

            elif np.shape(sizes) == ():
                sizes = np.ones(np.size(corners)//sizes)*sizes

            corners = np.reshape(corners, np.size(corners))

            # Check consistency to avoid a crash

            if np.sum(sizes) != len(corners):
                raise RuntimeError(f"Mesh.FromComponents error: the sum of the sizes {np.sum(sizes)} is not equal to the number of corners {len(corners)}.")

            self.corners.add_corners(corners, **attrs)
            self.faces.add_faces(sizes, **attrs)

        # ---------------------------------------------------------------------------
        # Concatenated attributes  DOMAIN_TYPE_name

        for k, v in attrs.items():
            split = k.split('_')
            domain_name = split[0]

            if domain_name not in ['POINT', 'CORNER', 'FACE'] or len(split) == 1:
                continue

            concat = k[len(domain_name)+1:]

            if domain_name == 'POINT':
                self.points.attributes.from_concat(concat)
                setattr(mesh.points, v)
            elif domain_name == 'FACE':
                self.faces.attributes.from_concat(concat)
                setattr(mesh.faces, v)
            else:
                self.corners.attributes.from_concat(concat)
                setattr(mesh.corners, v)


    # -----------------------------------------------------------------------------------------------------------------------------
    # Utilities

    def check(self, halt=True):
        return self.corners.check(halt=halt) and self.faces.check(halt=halt)

    def __str__(self):
        return f"<Mesh: points {self.points.shape}, corners {self.corners.shape}, faces {self.faces.shape}>"

    def __repr__(self):
        s = "Mesh:\n   " + "\n   ".join([str(self.points), str(self.corners), str(self.faces)])
        return s

    # =============================================================================================================================
    # Clear the geometry

    def clear(self):
        """ Clear the geometry.

        Delete all the content.
        """

        self.points.attributes.clear()
        self.corners.attributes.clear()
        self.faces.attributes.clear()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Capture another Mesh

    def capture(self, other):
        """ Capture the data of another Mesh.

        Utilities used to avoid array creation. Equivalent to FromMesh.

        Arguments
        ---------
            - other (Mesh) : the mesh to capture

        Returns
        -------
            - self
        """

        self.materials = other.materials

        self.points  = other.points
        self.corners = other.corners
        self.faces   = other.faces

        return self

    # =============================================================================================================================
    # =============================================================================================================================
    # Initialization methods
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from another Mesh

    @classmethod
    def FromMesh(cls, other):
        """ Create a Mesh from another mesh.

        Arguments
        ---------
            - other (Mesh) : the mesh to copy

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=other.materials)
        mesh.points.attributes  = other.points.attributes.clone()
        mesh.corners.attributes = other.corners.attributes.clone()
        mesh.faces.attributes   = other.faces.attributes.clone()

        return mesh

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from an object

    @classmethod
    def FromObject(cls, obj, evaluated=False):
        """ Create a Mesh from an existing object.

        Arguments
        ---------
            - obj (str or Blender object) : the object to initialize from
            - evaluated (bool = False) : object modified by the modifiers if True, raw vertices otherwise

        Returns
        -------
            - Mesh
        """

        if evaluated:
            depsgraph = bpy.context.evaluated_depsgraph_get()
            object_eval = blender.get_object(obj).evaluated_get(depsgraph)
            return cls.FromMeshData(object_eval.data)

        else:
            return cls.FromMeshData(blender.get_object(obj).data)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from mesh data

    @classmethod
    def FromMeshData(cls, data):
        """ Initialize the geometry from a Blender Mesh

        Arguments
        ---------
            - mesh (Blender Mesh instance) : the mesh to load
        """

        bl_mesh = blender.get_mesh(data)

        mesh = cls()

        # ----- Vertices

        n = len(bl_mesh.vertices)
        if n != 0:
            # Positions will be read as position attribute
            mesh.points.add(n)

        # ----- Corners

        n = len(bl_mesh.polygons)
        if n != 0:
            a = np.empty(len(bl_mesh.loops), int)
            bl_mesh.loops.foreach_get("vertex_index", a)
            mesh.corners.add_corners(a)

            a = np.empty(n, int)
            bl_mesh.polygons.foreach_get("loop_total", a)
            mesh.faces.add_faces(a)

            del a

        # ----- Materials

        mesh.materials = [None if mat is None else mat.name for mat in bl_mesh.materials]

        # ----- Attributes

        mesh.points.attributes.from_object(bl_mesh)
        mesh.corners.attributes.from_object(bl_mesh)
        mesh.faces.attributes.from_object(bl_mesh)

        #print("FROM DATA", mesh.faces.attributes)
        #for battr in bl_mesh.attributes:
        #    print(battr.domain, battr.name)

        return mesh

    # ====================================================================================================
    # From something

    @classmethod
    def FromModel(cls, model, materials=None):

        if isinstance(model, (str, bpy.types.Object)):
            mesh = cls.FromObject(model, evaluated=True)

        elif isinstance(model, dict):
            mesh = cls(materials=materials, **model)

        elif isinstance(model, Mesh):
            mesh = cls.FromMesh(model)

        elif isinstance(model, bpy.types.Mesh):
            mesh = cls.FromMeshData(model)

        else:
            raise Exception(f"Mesh.FromModel: 'model' type is not valid: {type(model)}")

        return mesh

    # =============================================================================================================================
    # Serialization

    def as_dict(self):
        return {
            'points'    : self.points.attributes.as_dict(),
            'corners'   : self.corners.attributes.as_dict(),
            'faces'     : self.faces.attributes.as_dict(),
            'materials' : self.materials,
            }

    @classmethod
    def FromDict(cls, d):

        mesh = cls(materials = d['materials'])

        mesh.points  = PointDomain.FromDict(d['points'])
        mesh.corners = CornerDomain.FromDict(mesh.points, d['corners'])
        mesh.faces   = FaceDomain.FromDict(mesh.corners, d['faces'])

        return mesh


    # =============================================================================================================================
    # =============================================================================================================================
    # I/O wit Blender
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create / update an object

    def to_object(self, obj, shade_smooth=None):
        """ Create or update a blender object.

        The method 'to_object' creates the whole geometry. It creates a new object if it doesn't already exist.
        If the object exists, it must be a mesh, there is no object type conversion.

        Once the object is created, use the method 'update_object' to change the vertices.

        Arguments
        ---------
            - obj (str or Blender object) : the object the create

        Returns
        -------
            - Blender mesh object
        """

        res = blender.create_mesh_object(obj)
        self.to_mesh_data(res.data)
        if shade_smooth is not None:
            res.data.polygons.foreach_set('use_smooth', [shade_smooth]*len(res.data.polygons))
        return res

    # -----------------------------------------------------------------------------------------------------------------------------
    # To blenbder mesh data

    def to_mesh_data(self, data):
        """ Write the geometry into a Blender Mesh

        Arguments
        ---------
            - mesh (Blender Mesh instance) : the mesh to write
        """

        bl_mesh = blender.get_data(data)
        bl_mesh.clear_geometry()

        # ----------------------------------------------------------------------------------------------------
        # Materials

        bl_mesh.materials.clear()
        for mat_name in self.materials:
            bl_mesh.materials.append(bpy.data.materials.get(mat_name))

        # ----------------------------------------------------------------------------------------------------
        # Vertices

        if len(self.points):
            bl_mesh.vertices.add(len(self.points))

        # ----------------------------------------------------------------------------------------------------
        # Corners

        if len(self.corners):
            bl_mesh.loops.add(len(self.corners))
            bl_mesh.loops.foreach_set("vertex_index", np.array(self.corners.vertex_index))

        # ----------------------------------------------------------------------------------------------------
        # Faces

        if len(self.faces):
            bl_mesh.polygons.add(len(self.faces))
            bl_mesh.polygons.foreach_set("loop_start", self.faces.loop_start)
            bl_mesh.polygons.foreach_set("loop_total", np.array(self.faces.loop_total))

        # ----------------------------------------------------------------------------------------------------
        # Attributes

        self.points.attributes.to_object(bl_mesh, update=False)
        self.corners.attributes.to_object(bl_mesh, update=False)
        self.faces.attributes.to_object(bl_mesh, update=False)

        # ----------------------------------------------------------------------------------------------------
        # Update

        bl_mesh.update()

    # =============================================================================================================================
    # bmesh edition

    @contextmanager
    def bmesh(self, readonly=False):
        """ Acces to bmesh api.

        The example below use bmesh to offset the vertices of +1 in the x axis.

        ``` python
        mesh = Mesh.Cube()

        # Move the vertices with bmesh
        with mesh.bmesh() as bm:
            for v in bm.verts:
                v.co.x += 1.0

        # Move the vertices directy in numpy array
        mesh.points.position[:, 1] += 1

        # Cube moved along x and y
        mesh.to_object("Cube")
        ```

        Arguments
        ---------
            - readonly (bool=False) : avoid to read back the bmesh if not modications were done
        """

        data = bpy.data.meshes.get(DATA_TEMP_NAME)
        if data is None:
            data = bpy.data.meshes.new(DATA_TEMP_NAME)
        self.to_mesh_data(data)

        bm = bmesh.new()   # create an empty BMesh
        bm.from_mesh(data) # fill it in from a Mesh

        yield bm

        # ----- Back

        if not readonly:
            bm.to_mesh(data)
            self.capture(Mesh.FromMeshData(data))

        bm.free()

    # =============================================================================================================================
    # Acces to blender data

    @contextmanager
    def blender_data(self, readonly=False):
        """ Acces to Blender Mesh API.

        Transfer the geometry to a temporay Blender Mesh.
        The example below use a blender Mesh to get the normals.

        ``` python
        mesh = Mesh.Cube()

        with mesh.blender_data() as data:
            normals = np.array([poly.normal for poly in data.polygons])

        print(normals)

        # > [[-1. -0.  0.]
        #    [ 0.  1.  0.]
        #    [ 1. -0.  0.]
        #    [ 0. -1.  0.]
        #    [ 0.  0. -1.]
        #    [ 0. -0.  1.]]
        ```

        Arguments
        ---------
            - readonly (bool=False) : don't read back the geometry if not modified

        Returns
        -------
            - Blender Mesh
        """

        data = bpy.data.meshes.get(DATA_TEMP_NAME)
        if data is None:
            data = bpy.data.meshes.new(DATA_TEMP_NAME)

        self.to_mesh_data(data)

        yield data

        # ----- Back

        if not readonly:
            self.capture(Mesh.FromMeshData(data))

    # =============================================================================================================================
    # Edges

    def build_edges(self):
        with self.blender_data(read_only=True) as mesh:
            count = len(mesh.edges)
            a = np.zeros(count*2, int)
            mesh.edges.foreach_get('vertices', a)

        a = np.reshape(a, (count, 2))

        self._edges = EdgeDomain.New(self.points)
        self._edges.add(n, vertex0=a[:, 0], vertex1=a[:, 1])

    @property
    def edges(self):
        if self._edges is None:
            self.build_edges()

        return self._edges

    # =============================================================================================================================
    # Material

    def get_material_index(self, mat_name):
        """ Return the index of a material name.

        If the material doesn't exist, it is created

        Arguments
        ---------
            - mat_name (str) : material name

        Returns
        -------
            - int : index of the material name in the materials list
        """

        if mat_name in self.materials:
            return self.materials.index(mat_name)
        else:
            self.materials.append(mat_name)
            return len(self.materials)-1

    def change_material(self, old, new):
        """ Change the material index from one value to another.

        Arguments
        ---------
            - old (int) : material index to replace
            - new (int) : new material index
        """

        self.faces.material_index[self.faces.material_index == old] = new

    def add_materials(self, materials):
        """ Add a materials list to the existing one.

        If a material already exist, it is not added another time.

        Arguments
        ---------
            - materials (list of strs) : the list of materials to append.
        """

        if isinstance(materials, str):
            self.materials.append(materials)
        else:
            self.materials.extend(materials)


    # =============================================================================================================================
    # Combining

    def join(self, *others):
        """ Join another Mesh.

        To append the MeshBuilder:
            - The verts, faces and corners arrays array appended
            - Before being appends, the values of the corners array are shifted by the number of existing vertices
            - The materials are merged:
                - materials is added with add_materials
                - appended material indices are remapped to the new materials list

        If the appened geometry has attributes which don't exist, they are created.

        Arguments
        ---------
            - other (Mesh) : the Mesh to append
            - quick (bool=False) : don't check the attributes and the material indices
        """

        for other in others:

            # ----------------------------------------------------------------------------------------------------
            # Vertices

            v_ofs = self.points.size
            self.points.attributes.join(other.points.attributes)

            # ----------------------------------------------------------------------------------------------------
            # Corners

            c_ofs = self.corners.size
            self.corners.attributes.join(other.corners.attributes)
            self.corners.vertex_index[c_ofs:] += v_ofs

            # ----------------------------------------------------------------------------------------------------
            # Faces

            f_ofs = self.faces.size
            self.faces.attributes.join(other.faces.attributes)
            self.faces.loop_start[f_ofs:] += c_ofs

            # ----- Materials

            remap = np.array([self.get_material_index(mat_name) for mat_name in other.materials])
            if len(remap)>0:
                self.faces.material_index[f_ofs:] = remap[other.faces.material_index]

        return self


    # =============================================================================================================================
    # Multiply

    def __mul__(self, count):
        if not isinstance(count, (int, np.int32, np.int64)):
            print("count:", type(count))
            raise Exception(f"A Mesh can be multiplied only by an int, not '{count}'")

        return self.multiply(count)

    def __imul__(self, count):
        if not isinstance(count, (int, np.int32, np.int64)):
            raise Exception(f"A Mesh can be multiplied only by an int, not '{count}'")

        if count <= 1:
            return self

        # ----------------------------------------------------------------------------------------------------
        # Vertices

        v_ofs = self.points.size
        self.points.attributes.multiply(count)

        # ----------------------------------------------------------------------------------------------------
        # Corners

        c_ofs = self.corners.size
        ofs = (np.arange(count)*v_ofs)[:, None] + np.zeros((1, c_ofs), int)
        self.corners.attributes.multiply(count)
        self.corners.vertex_index += np.reshape(ofs, ofs.size)

        # ----------------------------------------------------------------------------------------------------
        # Faces

        f_ofs = self.faces.size
        ofs = (np.arange(count)*c_ofs)[:, None] + np.zeros((1, f_ofs), int)
        self.faces.attributes.multiply(count)

        self.faces.update_loop_start()

        return self


    def multiply(self, count=10, **attributes):
        """ Duplicate the geometry.

        Multiplying is a way to efficiently duplicate the geometry a great number of times.
        Once duplicated, the vertices can be reshapped to address each instance individually.

        ``` python
        count = 16

        cube = Mesh.Cube() * count

        # Shape the points as 16 blocks of 8 vertices
        points = np.reshape(cube.points.position, (16, 8, 3))

        # Place the cubes in a circle
        ags = np.linspace(0, 2*np.pi, count, endpoint=False)
        points[..., 0] += 6 * np.cos(ags)[:, None]
        points[..., 1] += 6 * np.sin(ags)[:, None]

        cube.to_object("Cubes")
        ```

        Arguments
        ---------
            - count (int=10) : number of instances
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - Mesh
        """

        mesh = Mesh()
        mesh.join(self)

        mesh *= count

        return mesh

    # =============================================================================================================================
    # =============================================================================================================================
    # Build
    # =============================================================================================================================

    # =============================================================================================================================
    # Add Vertices

    def add_verts(self, verts,  **attributes):
        """ Add vertices.

        Arguments
        ---------
            - verts (array of vectors) : the vertices to add
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - array of ints : indices of the added vertices
        """

        index = len(self.points)
        self.points.add_points(verts, **attributes)
        return np.arange(index, len(self.points))

    # =============================================================================================================================
    # Add faces

    def add_faces(self, corners, offset_index=0, **attributes):
        """ Add faces.

        Faces can be added in different formats:
            - a list or 1D-array of ints : a single face
            - a list of list of ints : a list of faces
            - a 2D-array of ints : a list of faces of the same size
            - a tuple (array of ints, array of ints) : sizes and corners

        The offset_index is the value to add to the vertex indices. It allows to add geometry faces defined from
        index 0 to a geometry with existing vertices.

        ``` python
        # ----- One face at a time

        mesh = Mesh()

        # Create 8 vertices form a cube
        mesh.add_verts(Mesh.Cube().points.position)

        # list of ints
        mesh.add_faces([0, 1, 3, 2])

        # tuple of ints
        mesh.add_faces((2, 3, 7, 6))

        # array of ints
        mesh.add_faces(np.array((6, 7, 5, 4)))

        obj = mesh.to_object("Single faces")
        obj.location.x = -3

        # ----- Several faces

        mesh = Mesh()

        # Create 8 vertices form a cube
        mesh.add_verts(Mesh.Cube().points.position)

        # list of lists
        mesh.add_faces( [[0, 1, 3, 2], [2, 3, 7, 6], [6, 7, 5, 4]])

        # Structured array
        faces = np.reshape([4, 5, 1, 0, 2, 6, 4, 0, 7, 3, 1, 5], (3, 4))
        mesh.add_faces(faces)

        mesh.to_object("List of faces")

        # ----- Corners and sizes

        mesh = Mesh()

        # Create 8 vertices form a cube
        mesh.add_verts(Mesh.Cube().points.position)

        mesh.add_faces((
            [0, 1, 3, 2, 2, 3, 7, 6, 6, 7, 5, 4, 4, 5, 1, 0, 2, 6, 4, 0, 7, 3, 1, 5],
            [4, 4, 4, 4, 4, 4],
            ))

        obj = mesh.to_object("Corners, faces")
        obj.location.x = 3
        ```

        Arguments
        ---------
            - faces (various) : the faces to add
            - mat (int or array of ints = 0) : material indices of the faces
            - offset (int) : the offset to add to the vertex indices.
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - array of ints : indices of the created faces
        """

        corner_index = len(self.corners)
        face_index   = len(self.faces)

        # ----------------------------------------------------------------------------------------------------
        # A numpy array : a set of corners with the same size

        if isinstance(corners, np.ndarray):

            # Or a single face :-)
            if corners.ndim == 1:
                self.corners.add_corners(corners, **attributes)
                self.faces.add_faces(len(corners), **attributes)

            else:
                face_len = np.shape(corners)[-1]
                nfaces = np.size(corners)//face_len

                self.corners.add_corners(corners, **attributes)
                self.faces.add_faces([face_len]*nfaces, **attributes)

        # ----------------------------------------------------------------------------------------------------
        # A tuple : a single face or (sizes, corners)

        elif isinstance(corners, tuple):
            if len(corners) > 0:

                ok = False

                # A tuple of ints
                if isinstance(corners[0], int):
                    self.corners.add_corners(corners, **attributes)
                    self.faces.add_faces(len(corners), **attributes)
                    ok = True

                # Corners, sizes
                elif len(corners) == 2:
                    cs = corners[0]
                    fs = corners[1]

                    if hasattr(cs, '__len__') and hasattr(fs, '__len__') and np.sum(fs) == len(cs):
                        self.corners.add_corners(cs, **attributes)
                        self.faces.add_faces(fs, **attributes)
                        ok = True

                if not ok:
                    raise Exception(f"Mesh.add_faces error: unknwon corners specification. The 'corners' argument is an incorrect tuple:\n", corners)

        # ----------------------------------------------------------------------------------------------------
        # A list : list of corners or a single face

        elif isinstance(corners, list):
            if len(corners) > 0:

                # A list of lists
                if isinstance(corners[0], list):
                    sizes = []
                    for cs in corners:
                        self.corners.add_corners(cs, **attributes)
                        sizes.append(len(cs))
                    self.faces.add_faces(sizes)
                else:
                    self.corners.add_corners(corners, **attributes)
                    self.faces.add_faces(len(corners), **attributes)

        else:
            raise Exception(f"Mesh error: error in 'add_faces', unknown type for corners : {type(corners)}")

        # ----------------------------------------------------------------------------------------------------
        # Finalizing

        if len(self.corners) > corner_index:
            if offset_index > 0:
                self.corners.vertex_index[corner_index:] += offset_index

        return np.arange(face_index, len(self.faces))

    # =============================================================================================================================
    # Add a surface defined by its vertices

    def add_surface(self, verts, **attributes):
        """ Add a surface from a list of vertices.

        The method 'add_face' uses existing vertices. The method 'add_surface' gives the vertices.

        If the verts array is a single list of vertices, one face is added with these vertices.
        If the verts array is a 2D list of vertices, ie a 3D array of floats, it is interpreted
        as a list of faces to insert:
            - verts shape is (4, 3) : a quad face is added
            - verts shape is (10, 4, 3) : 10 quad faces are added

        ``` python
        # ----- Build a stack of half disks

        # Base half disk
        ag = np.linspace(0, np.pi, 10)
        verts = np.c_[np.cos(ag), np.sin(ag), np.zeros_like(ag)]

        # Stack along z
        z = np.zeros((7, 3), float)
        z[:, 2] = np.linspace(0, 3, 7)
        verts = verts[None] + z[:, None, :]

        # Some rotation
        eulers = np.zeros((7, 3), float)
        eulers[:, 2] = np.linspace(0, np.pi, 7)
        verts = Transformations(rotation=eulers)[:, None] @ verts

        # Let's build the mesh
        mesh = Mesh()

        mesh.add_surface(verts)

        mesh.to_object("Half Disks")
        ```

        Arguments
        ---------
            - verts (array of vectors) : the vertices of the surface
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - array of ints : indices of created faces
        """

        assert(len(np.shape(verts)) >= 2)

        v_inds = self.add_verts(verts, **attributes)

        if len(np.shape(verts)) == 2:
            return self.add_faces(v_inds, **attributes)
        else:
            return self.add_faces(np.reshape(v_inds, np.shape(verts)[:-1]), **attributes)

    # =============================================================================================================================
    # =============================================================================================================================
    # Constructors
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Test the constructors

    @staticmethod
    def all_primitives():

        # ----- Plane geometries

        Mesh.Grid(
            transformation=Transformations(locations=( 0,  0, 0))).to_object("Grid")

        Mesh.Circle(fill_segments=0,
            transformation=Transformations(locations=( 5, 0, 0))).to_object("Circle Plain")

        Mesh.Circle(segments=6, fill_segments=1,
            transformation=Transformations(locations=(10, 0, 0))).to_object("Circle Fans 1")

        Mesh.Circle(fill_segments=3,
            transformation=Transformations(locations=(15, 0, 0))).to_object("Circle Fans 3")

        # ----- Basics

        Mesh.Cube(
            transformation=Transformations(locations=( 0,  5, 0))).to_object("Cube")

        Mesh.UVSphere(
            transformation=Transformations(locations=( 5,  5, 0))).to_object("UVSphere")

        Mesh.IcoSphere(
            transformation=Transformations(locations=(10,  5, 0))).to_object("IcoSphere")

        Mesh.Torus(
            transformation=Transformations(locations=(15,  5, 0))).to_object("Torus")

        Mesh.Monkey(
            transformation=Transformations(locations=(20,  5, 0))).to_object("Monkey")

        # ----- Cylinders

        Mesh.Cylinder(
            transformation=Transformations(locations=( 0, 10, 0))).to_object("Cylinder")

        Mesh.Cylinder(side_segments=7,
            transformation=Transformations(locations=( 5, 10, 0))).to_object("Cylinder side 7")

        Mesh.Cylinder(vertices=6, fill_segments=3, fill_type=('TRIANGLE_FAN', 'TRIANGLE_FAN'),
            transformation=Transformations(locations=(10, 10, 0))).to_object("Cylinder NGON + FANS")

        Mesh.Cone(
            transformation=Transformations(locations=(15, 10, 0))).to_object("Cone")

        Mesh.Pyramid(
            transformation=Transformations(locations=(20, 10, 0))).to_object("Pyramid")


        #Mesh.Torus(transformation      = Transformations(locations=( 0, 10, 0))).to_object("Torus")
        #Mesh.ChainLink(transformation  = Transformations(locations=( 5, 10, 0))).to_object("ChainLink")

    # =============================================================================================================================
    # Grid

    @classmethod
    def Grid(cls, size_x=1, size_y=1, vertices_x=3, vertices_y=3, materials=None, transformation=None):
        """ Create a Grid.

        Arguments
        ---------
            - size_x (float=1) : size along x
            _ size_y (float=1) : size along y
            - vertices_x (int=3) : number of vertices along x
            - vertices_y (int=3) : number of vertices along y
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials, **topology.grid(x_size=size_x, y_size=size_y, x_count=vertices_x, y_count=vertices_y))

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    @classmethod
    def BGrid(cls, x_segments=1, y_segments=1, size=2, transformation=None, materials=None):
        """ Create a Grid.

        Blender constructor for a Grid.

        Arguments
        ---------
            - x_segments (int=1) : number of segments along x axis
            - y_segments (int=1) : number of segments along y axis
            - size (float or tuple of floats = 1. : size of the grid
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials)
        with mesh.bmesh() as bm:
            bmesh.ops.create_grid(bm, x_segments=x_segments, y_segments=y_segments, size=size, calc_uvs=True)

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # =============================================================================================================================
    # Cube

    @classmethod
    def Cube(cls, size=2, materials=None, transformation=None):
        """ Create a Cube.

        Arguments
        ---------
            - size (float=1.) : size of the cube
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        verts = [[-1., -1., -1.], [-1., -1.,  1.], [-1.,  1., -1.], [-1.,  1.,  1.], [ 1., -1., -1.], [ 1., -1.,  1.], [ 1.,  1., -1.], [ 1.,  1.,  1.],]
        corners = [[0, 1, 3, 2], [2, 3, 7, 6], [6, 7, 5, 4], [4, 5, 1, 0], [2, 6, 4, 0], [7, 3, 1, 5]]
        uvs   = [[0.375, 0.000], [0.625, 0.000], [0.625, 0.250], [0.375, 0.250], [0.375, 0.250], [0.625, 0.250], [0.625, 0.500], [0.375, 0.500],
                 [0.375, 0.500], [0.625, 0.500], [0.625, 0.750], [0.375, 0.750], [0.375, 0.750], [0.625, 0.750], [0.625, 1.000], [0.375, 1.000],
                 [0.125, 0.500], [0.375, 0.500], [0.375, 0.750], [0.125, 0.750], [0.625, 0.500], [0.875, 0.500], [0.875, 0.750], [0.625, 0.750], ]


        mesh = cls(verts=verts, corners=corners, materials=materials)

        if size != 2:
            mesh.points.position *= size/2

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # =============================================================================================================================
    # Circle

    @classmethod
    def Circle(cls, radius=1, segments=16, fill_segments=0, materials=None, transformation=None):
        """ Create a Circle.

        'fill_segments' argument gives the number of internal circles to create.
        If zero, the circle if filled with a polygon.
        If positive, the circle is filled with triangle fans.

        Arguments
        ---------
            - radius (float=1.) : circle radius
            - segments (int=16) : number of segments
            - fill_segments (int = 0) : number of internal segments, polygon is None
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        if fill_segments == 0:
            y_count = 1
            fans = False
        else:
            y_count = fill_segments
            fans = True

        mesh = cls(materials=materials, **topology.disk(radius, x_count=segments, y_count=y_count, fans=fans))

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    @classmethod
    def BCircle(cls, radius=1, segments=16, fill_tris=False, materials=None, transformation=None):
        """ Create a Circle.

        Blender constructor for a Circle.

        Arguments
        ---------
            - radius (float=1.) : circle radius
            - segments (int=16) : number of segments
            - fill_tris (bool = False) : fill with triangle fans
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials)
        with mesh.bmesh() as bm:
            bmesh.ops.create_circle(bm, cap_ends=True, cap_tris=fill_tris, segments=segments, radius=radius, calc_uvs=True)

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # =============================================================================================================================
    # Cylinder

    @classmethod
    def BCylinder(cls, radius=1, depth=2, segments=32, cap_ends=True, cap_tris=False, materials=None, transformation=None):
        """ Create a Cylinder.

        Blender constructor for a Cylinder.

        Arguments
        ---------
            - radius (float=1.) : radius
            - depth (float=2.) : cylinder height
            - segments (int=16) : number of segments
            - cap_ends (bool=True) : fill cap faces
            - cap_tris (bool = False) : fill with triangle fans
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        return cls.BCone(radius1=radius, radius2=radius, depth=depth, segments=segments, cap_ends=cap_ends, cap_tris=cap_tris, transformation=transformation, materials=materials)

    @classmethod
    def Cylinder(cls, vertices=32, side_segments=1, fill_segments=1, radius=1, depth=2, fill_type='NGON', materials=None, transformation=None):
        """ Create a Cylinder.

        Arguments
        ---------
            - vertices (int=16) : number of segments
            - side_segments (int = 1) : number of vertical segments
            - fill_segments (int = 1) : number of internal circles on the caps
            - radius (float=1.) : radius
            - depth (float=2.) : cylinder height
            - fill_type (str or couple of strs ='NGON' in 'NGON', 'TRIANGLE_FAN', 'NONE') : cap filling
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials, **topology.cylinder(
            radius,
            radius1   = None,
            depth     = depth,
            x_count   = vertices,
            y_count   = fill_segments,
            z_count   = side_segments+1,
            caps      = fill_type))

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # =============================================================================================================================
    # Cone

    @classmethod
    def BCone(cls, radius1=1, radius2=0, depth=2, segments=16, cap_ends=True, cap_tris=False, materials=None, transformation=None):
        """ Create a Cone.

        Blender constructor for a Cone.

        Arguments
        ---------
            - radius1 (float=1.) : base radius
            - radius2 (float=0.) : top radius
            - depth (float=2.) : cone height
            - segments (int=16) : number of segments
            - cap_ends (bool=True) : fill cap faces
            - cap_tris (bool = False) : fill with triangle fans
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials)
        with mesh.bmesh() as bm:
            bmesh.ops.create_cone(bm, cap_ends=cap_ends, cap_tris=cap_tris, segments=segments, radius1=radius1, radius2=radius2, depth=depth, calc_uvs=True)

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh


    @classmethod
    def Cone(cls, vertices=32, side_segments=1, fill_segments=1, radius_top=0, radius_bottom=1, depth=2, fill_type='NGON', materials=None, transformation=None):
        """ Create a Cone.

        Arguments
        ---------
            - vertices (int=16) : number of segments
            - side_segments (int = 1) : number of vertical segments
            - fill_segments (int = 1) : number of internal circles on the caps
            - radius_top (float=0) : top radius
            - radius_bottom (float=1) : bottom radius
            - depth (float=2.) : cylinder height
            - fill_type (str or couple of strs ='NGON' in 'NGON', 'TRIANGLE_FAN', 'NONE') : cap filling
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials, **topology.cylinder(
            radius    = radius_bottom,
            radius1   = radius_top,
            depth     = depth,
            x_count   = vertices,
            y_count   = fill_segments,
            z_count   = side_segments+1,
            caps      = fill_type))

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh


    # =============================================================================================================================
    # Pyramid

    @classmethod
    def Pyramid(cls, size=1, materials=None, transformation=None):
        """ Create a Pyramid.

        Arguments
        ---------
            - size (float=1.) : size

        Returns
        -------
            - Mesh
        """

        return cls.Cone(vertices=3, radius_bottom=size*0.8660254037844386, depth=size, materials=materials, transformation=transformation)

    # =============================================================================================================================
    # UV Sphere

    @classmethod
    def BUVSphere(cls, radius=1, u_segments=32, v_segments=16, materials=None, transformation=None):
        """ Create a uv sphere.

        Blender constructor for a UVSphere.

        Arguments
        ---------
            - radius (float=1.) : radius
            - u_segments (int=32) : number of u segments
            - v_segments (int=16) : number of v segments
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials)
        with mesh.bmesh() as bm:
            bmesh.ops.create_uvsphere(bm, u_segments=u_segments, v_segments=v_segments, radius=radius, calc_uvs=True)

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    @classmethod
    def UVSphere(cls, segments=32, rings=16, radius=1, materials=None, transformation=None):
        """ Create a uv sphere.

        Arguments
        ---------
            - segments (int=32) : number of segments
            - rings (int=16) : number of rings
            - radius (float=1.) : radius
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials, **topology.uv_sphere(radius=radius, x_count=segments, y_count=rings+1))

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    @classmethod
    def IcoSphere(cls, radius=1, subdivisions=2, materials=None, transformation=None):
        """ Create a IcoSphere.

        Blender constructor for a IcoSphere.

        Arguments
        ---------
            - radius (float=1.) : radius
            - subdivisions (int=2) : number subdivisions
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials)
        with mesh.bmesh() as bm:
            bmesh.ops.create_icosphere(bm, subdivisions=subdivisions, radius=radius, calc_uvs=True)

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # ----------------------------------------------------------------------------------------------------
    # Torus

    @classmethod
    def Torus(cls, major_segments=48, minor_segments=12, major_radius=1., minor_radius=0.25, materials=None, transformation=None):
        """ Create a Torus.

        Arguments
        ---------
            - major_segments (int=48) : number of segments for the major radius
            - minor_segments (int=12) : number of segments for the minor radius
            - major_radius (float=1.) : major radius
            - minor_radius (float=.25) : minor radius
            - materials (list of strs = None) : materials list
            - transformation (Transformations = None) : the transformation to apply

        Returns
        -------
            - Mesh
        """

        mesh = cls(materials=materials, **topology.torus(major_radius=major_radius, minor_radius=minor_radius, x_count=minor_segments, y_count=major_segments))

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # =============================================================================================================================
    # Monkey

    @classmethod
    def Monkey(cls, materials=None, transformation=None):
        """ Create a Monkey.

        Arguments
        ---------
            - materials (list of strs = None) : materials list

        Returns
        -------
            - MeshBuilder
        """
        mesh = cls(materials=materials)
        with mesh.bmesh() as bm:
            bmesh.ops.create_monkey(bm)

        if transformation is not None:
            mesh.points.position = transformation @ mesh.points.position

        return mesh

    # =============================================================================================================================
    # Arrow

    @classmethod
    def Arrow(cls, vector=(0, 0, 1), radius=.05, angle=24., segments=8, adjust_norm=None, materials=None):

        height = np.linalg.norm(vector)
        if type(adjust_norm).__name__ == 'function':
            height = adjust_norm(height)
        elif adjust_norm is not None:
            height = min(adjust_norm, height)

        head_radius = 3*radius
        head_height = head_radius/np.tan(np.radians(angle))

        cyl_height = height - head_height*.8

        cyl  = cls.Cylinder(vertices=segments, side_segments=2, radius=radius, depth=cyl_height, transformation=Transformations(position=(0, 0, cyl_height/2)), materials=materials)
        cyl.points[[segments + i for i in range(segments)]].position -= (0, 0, cyl_height/2 - .01)

        cone = cls.Cone(vertices=segments, side_segments=2, fill_segments=1, radius_top=0, radius_bottom=head_radius, depth=head_height, fill_type='TRIANGLE_FAN', materials=materials)
        cone.points[-1].position += (0, 0, head_height/10)
        cone.points.position += (0, 0, height - head_height/2)

        arrow = cyl.join(cone)
        arrow.points.position = tracker(vector, track_axis='Z') @ arrow.points.position

        return arrow

    @classmethod
    def VectorField(cls, locations, vectors, radius=.05, scale_length=1., angle=24., segments=8, head=None, adjust_norm=None, materials=None):

        """ Create an arrow at each location corresponding to the vectors.

        The arrow length is equal to the corresponding vector lengths.
        The arrow radius is constant and equal to the value passe in argument for lengths greater that
        the argument scale_length. When the length is less than this value, the arrow is scaled down.

        Use the adjust_norm argument to transform the vector lengths to arrows lengths.

        Arguments
        ---------
            - locations (array of 3-vectors) : vectors locations
            - vectors (array of 3 vectors) : vectors to visualize
            - radius (float = .05) : arrow radius
            - angle (float = 24) : head radius in degrees
            - segments (int = 8) : number of segments for the section
            - head (mesh = None) : mesh model for the head. Create a cone if None
            - adjust_norm (max length or function = None) : max arrow length or function transforming
                the vector length into arrow length
            - scale_length (float = 1.) : arrow length below which the arrow radius is scaled

        Returns
        -------
            - Mesh Object
        """

        cyl_height  = 1.
        head_radius = 3*radius
        head_height = head_radius/np.tan(np.radians(angle))

        # ----------------------------------------------------------------------------------------------------
        # Base models

        # ----- Cylinder model

        cyl = cls.Cylinder(vertices=segments, side_segments=2, radius=radius, depth=cyl_height, transformation=Transformations(position=(0, 0, cyl_height/2)), materials=materials)
        cyl.points[[segments + i for i in range(segments)]].position -= (0, 0, cyl_height/2 - .01)

        # ----- Head model

        if head is None:
            cone = cls.Cone(vertices=segments, side_segments=2, fill_segments=1, radius_top=0, radius_bottom=head_radius, depth=head_height, fill_type='TRIANGLE_FAN', materials=materials)
            cone.points[-1].position += (0, 0, head_height/10)
        else:
            cone = head


        # ----------------------------------------------------------------------------------------------------
        # Vectors lengths

        n = len(locations)

        lengths = np.linalg.norm(vectors, axis=-1)
        if type(adjust_norm).__name__ == 'function':
            lengths = adjust_norm(lengths)
        elif adjust_norm is not None:
            lengths = np.minimum(adjust_norm, lengths)

        # ----------------------------------------------------------------------------------------------------
        # Duplicate the models

        cyls  = cyl * n
        cones = cone * n

        cyls_pos  = np.reshape(cyls.points.position, (n, len(cyl.points),   3))
        cones_pos = np.reshape(cones.points.position,(n, len(cone.points),  3))

        # ----- Scale the radius for lengths less then scale_length

        if scale_length is not None:
            scales = np.minimum(lengths/scale_length, 1.)
            cyls_pos[..., :2] *= scales[:, None, None]
            cones_pos *= scales[:, None, None]
            head_height = scales*head_height

        # ----- Locate properly the cylinders and the cones

        """"
        heights = np.linalg.norm(vectors, axis=-1)
        if type(adjust_norm).__name__ == 'function':
            heights = adjust_norm(heights)
        elif adjust_norm is not None:
            heights = np.minimum(adjust_norm, heights)
        """

        cyls_pos[:, -segments:, 2] = (lengths - head_height*.8)[:, None]
        cones_pos[..., 2] += np.maximum(0, (lengths - head_height/2))[:, None]

        # ----- Orient them toward the vectors

        trf = tracker(vectors, track_axis='Z')
        cyls.points.transform(trf)
        cones.points.transform(trf)

        # ----- And to their locations

        cyls.points.translate(locations)
        cones.points.translate(locations)

        return cyls.join(cones)


    # ----------------------------------------------------------------------------------------------------
    # Chain Link

    @classmethod
    def ChainLink(cls, major_segments=48, minor_segments=12, radius=1., section=0.5, length=4., transformation=None, materials=None):
        """ Create a chain link.

        ``` python
        # ----- Some maths

        # Chain follows a catenary curve
        def catenary(t):
            return np.stack((t, np.zeros_like(t), np.cosh(t)), axis=-1)

        # Orientation is given by the derivative
        def derivative(t):
            dt = 1/10000
            return (catenary(t + dt) - catenary(t - dt))/(2*dt)

        # Catenary length
        pts = catenary(np.linspace(-1, 1, 1000))
        cat_s = np.cumsum(np.linalg.norm(pts[1:] - pts[:-1], axis=-1))
        cat_len = cat_s[-1]

        # Catenary inverse : t from length
        def cat_inverse(l):
            return 2*np.argmin(np.abs(cat_s - l))/1000 - 1

        # ----- Let's build the geometry

        # One chain link
        section = .02
        length  = .15
        link = MeshBuilder.ChainLink(radius=.04, section=section, length=length)

        # Link length taking into account the section
        l = length - 2*section

        # Number of links
        count = round(cat_len / l)

        # The chain
        chain = link*count

        # Rotate pi/2 one on two
        eulers = Eulers(shape=count)
        eulers[[i % 2 == 1 for i in range(count)]] = (0, np.pi/2, 0)

        chain.rotate(eulers)
        chain.rotate_z(np.pi/2)

        # Location of each link
        t = np.array([cat_inverse(l*i) for i in range(count)])

        chain.toward(derivative(t), track_axis='X', up_axis='Z')
        chain.translate(catenary(t))

        # To object
        chain.to_object("Catenary")
        ```

        Arguments
        ---------
            - major_segments (int=48) : number of segments for the link
            - minor_segments (int=12) : number of segments for the section
            - radius (float=1.) : radius of the link
            - section (float=.5) : section (diameter)
            - length (float=4.) : total length of the link
            - materials (list of strs = None) : materials list

        Returns
        -------
            - MeshBuilder
        """

        # ----- Profile

        ags = np.linspace(0, 2*np.pi, minor_segments, endpoint=False)
        profile = (section/2)*np.stack((np.cos(ags), np.sin(ags), np.zeros_like(ags)), axis=-1)

        # ----- Backbone

        offset = max(0., length - 2*radius - section)

        nmaj = major_segments//2
        ags = np.linspace(0, np.pi, nmaj)
        verts = radius*np.stack((np.cos(ags), np.sin(ags), np.zeros_like(ags)), axis=-1)
        verts[:, 1] += offset/2
        verts = np.resize(verts, (2, nmaj, 3))
        verts[1] *= -1

        # ----- The link

        return cls(materials=materials).add_pipe(np.reshape(verts, (2*nmaj, 3)), profile=profile, caps=False, torus=True)


    # ====================================================================================================
    # Build a pipe around a line

    @classmethod
    def CurveToMesh(cls, points, profile=8, radius=1., torus=False, caps=True, mat=0, **attributes):
        """ Add a cylinder topology by extruding a profile along a line.

        The 'points' argument provides the line to extrude along.
        The profile argument either gives the resolution of a round profile or gives the
        vertices of a profile. The profile is given in the plane (x, y).

        ``` python
        count = 100
        z = np.linspace(0, 2, count)
        ag = np.linspace(0, 4*np.pi, count)
        verts = np.stack((np.cos(ag), np.sin(ag), z), axis=-1)

        helix = MeshBuilder().add_pipe(verts, profile=16, radius=.1, caps=True)

        helix.to_object("Helix")

        helix = MeshBuilder().add_pipe(verts, profile=16, radius=np.linspace(.1, .5, count), caps=True)

        obj = helix.to_object("Helix var raidus")
        obj.location.y = 3
        ```

        Arguments
        ---------
            - points (array[n, 3] of floats) : the line
            - profile (array[m, 3] of floats or int = 3) : the resolution of a round profile if int else the profile
            - radius (float or array of floats=1.) : the scale to apply to each instance of profile
            - torus (bool=False) : the cylinder as the topology of a torus
            - caps (bool=True) : add faces to the ends (meaningless if torus)
            - mat (int=0) : material index
            - attributes (name=value) : value for named attributes
        """

        # ----- Round profile

        if isinstance(profile, (int, np.int32, np.int64)):
            n = profile
            ags = np.linspace(0, np.pi*2, n, endpoint=False)
            profile = np.zeros((n, 3), float)
            profile[:, 0] = np.cos(ags)
            profile[:, 1] = np.sin(ags)

        # ----- Base shape : profiles multiplied by the number of vertices
        # Add_cylinder will create the faces

        cyl = MeshBuilder()
        cyl.add_cylinder(np.resize(profile, (len(verts), len(profile), 3)), torus=torus, caps=caps, mat=mat, **attributes)

        # ----- Profiles orientation

        dirs = np.empty((len(verts), 3), float)
        dirs[1:-1] = verts[2:] - verts[:-2]
        if torus:
            dirs[0]    = verts[1] - verts[-1]
            dirs[-1]   = verts[0] - verts[-2]
        else:
            dirs[0]    = verts[1] - verts[0]
            dirs[-1]   = verts[-1] - verts[-2]

        cyl.toward(dirs, track_axis='Z', up_axis='Y')

        # ----- Profiles scale and locations
        cyl.scale(np.reshape(radius, np.shape(radius) + (1,)))
        cyl.translate(verts)

        self.append(cyl)

        return self

    # =============================================================================================================================
    # Operations

    @staticmethod
    def from_geom(geom):
        inds = {'vert_inds': [], 'face_inds': [], 'edge_inds': [], 'verts': [], 'faces': [], 'edges': []}
        for item in geom['geom']:
            if isinstance(item, bmesh.types.BMVert):
                inds['vert_inds'].append(item.index)
                inds['verts'].append(item)
            elif isinstance(item, bmesh.types.BMFace):
                inds['face_inds'].append(item.index)
                inds['faces'].append(item)
            elif isinstance(item, bmesh.types.BMEdge):
                inds['edge_inds'].append(item.index)
                inds['edges'].append(item)
            else:
                print(type(item))
                assert(False)
        return inds

    # -----------------------------------------------------------------------------------------------------------------------------
    # Burdge two loops

    def bridge(self, loop0, loop1, close=False, **attributes):
        corners = topology.bridge_corners(loop0, loop1, clockwise=False, close=close)
        return self.add_faces(corners, **attributes)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Extrude a loop

    def extrude(self, loop, offset=1., direction=None, clockwise=False, **attributes):
        """ Extrude a loop of vertices.

        Arguments
        ---------
            - loop (array of ints) : vertex indices
            - offset (float = 1) : multiplicator of the direction vector
            - direction (vector = None) : extrusion direction, normal if None
            - clockwise (bool=False) : faces orientation
            - attributes : attribute for the new geometry

        Returns
        -------
            - dictionnary of the created geometry : vertex indices, face indices
        """

        if not isinstance(loop, np.ndarray):
            loop = np.array(loop)

        # ----- Extruded vertices

        verts = self.points.position[loop]

        # ----- Extrusion direction

        if direction is None:
            direction = FaceDomain.area_vect(verts, len(verts), 'NORMAL')
        elif not isinstance(direction, np.ndarray):
            direction = np.array(direction)

        direction = direction * offset

        if clockwise:
            direction *= -1

        # ------ Extrude the vertices

        new_verts = verts + direction
        new_loop = self.add_verts(new_verts)

        # ------ Bridge the two loops

        sides = self.bridge(loop, new_loop, close=True, clockwise=clockwise, **attributes)

        return {'faces': sides, 'corners': new_loop}

    # -----------------------------------------------------------------------------------------------------------------------------
    # Extrude individual faces

    def extrude_faces(self, selection, offset=1., direction=None, **attributes):
        """ Extrude individual faces.

        ``` python
        # Simply a cylinder

        mesh = Mesh()
        ag = np.linspace(0, 2*np.pi, 7)
        inds = mesh.add_surface(np.c_[np.cos(ag), np.sin(ag), np.zeros_like(ag)])

        mesh.extrude_faces(0)

        mesh.to_object("Cylinder")

        ```

        Arguments
        ---------
            - selection : indices of the faces to extrude
            - offset (float = 1.) : multiplicator of the extrusion direction
            - direction (vector = None) : extrusion direction, normal if None
            - attributes : attributes for the faces and vertices

        Returns
        -------
            - dictionnary : 'top' : extruded faces, 'side' : extruded side faces
        """

        # ----- The indices of the faces to extrude

        faces_sel = np.arange(self.faces.size)[selection]
        if np.shape(faces_sel) == ():
            faces_sel = [faces_sel]

        # ----- Extrusion directions

        if direction is None:
            direction = self.faces.normal[faces_sel]

        elif np.shape(direction) == (3,):
            direction = np.reshape(direction, (len(faces_sel), 3))

        else:
            if len(direction) != len(faces_sel):
                raise RuntimeError(f"Mesh.extrude_faces error: the number of direction {len(direction)} is different from the number of faces to extrude {len(faces_sel)}")

        if np.shape(offset) == ():
            direction = direction*offset
        else:
            direction = direction*offset[:, None]

        # ----- Let's extrude

        tops  = []
        sides = np.empty(0, int)

        #print(self.corners.dump("Before"))

        for face_index, v in zip(faces_sel, direction):

            # ----- Extrude vertices

            verts = self.faces[face_index].get_verts()
            new_verts = verts + v

            # ----- Extruded face points to the new vertices

            new_loop = self.add_verts(new_verts, **attributes)

            c0 = self.faces[face_index].loop_start
            nc = self.faces[face_index].loop_total
            old_loop = np.array(self.corners.vertex_index[c0:c0+nc])

            self.corners.vertex_index[c0:c0+nc] = new_loop

            # ----- Create side faces

            sides = np.append(sides, self.bridge(old_loop, new_loop, close=True, **attributes))

            tops.append(face_index)

        return {'top': tops, 'side': sides}

    # -----------------------------------------------------------------------------------------------------------------------------
    # Extrude region

    def extrude_region(self, selection, offset=1., direction=None, **attributes):

        with self.bmesh() as bm:

            faces_sel = np.arange(self.faces.size)[selection]
            bm.faces.ensure_lookup_table()
            if np.shape(faces_sel) == ():
                faces = [bm.faces[faces_sel]]
            else:
                faces = [bm.faces[i] for i in faces_sel]



            extruded = bmesh.ops.extrude_face_region(bm,
                        geom                     = faces,
                        #edges_exclude            = set(),
                        #use_keep_orig            = False,
                        #use_normal_flip          = False,
                        #use_normal_from_adjacent = False,
                        #use_dissolve_ortho_edges = False,
                        #use_select_history       = False,
                        )

            inds = self.from_geom(extruded)

            vecs = None
            if direction is not None:
                if np.shape(direction) == (3,):
                    vec = offset * Vector(direction)
                else:
                    vecs = direction
                    if len(vecs) != len(inds['face_inds']):
                        raise RuntimeError(f"Mesh.extrude_faces error: the number of direction {len(vecs)} is different from the number of extruded faces {len(inds['face_inds'])}")

            new_indices = inds['face_inds']

            for i_face, face in enumerate(inds['faces']):

                if direction is None:
                    vec = offset * face.normal
                elif vecs is not None:
                    vec = vecs[i_face]

                bmesh.ops.translate(bm,
                    verts = face.verts,
                    vec   = vec)

        self.faces[new_indices].set_attributes(**attributes)

        return {key: inds[key] for key in ['vert_inds', 'edge_inds', 'face_inds']}

    # =============================================================================================================================
    # Inset
    #
    # A side is defined by point A and 3 unary vectors :
    # - a : along the side
    # - b : perpendicular to a, inside the face
    # - N : normal to the face
    #
    # Previous point is (A', a', b', N)
    #
    # The inset line at distance d of a side is defined by the equation:
    # M = A + db + ka
    #
    # Hence, the point inset in A is given by the equation:
    # A + db + ka = A' + db' + k'a' = A + AA' + db' + k'a'
    # db + ka = AA' + db' + k'a'
    # ka = AA' + d(b' - b) + k'a'
    #
    # We can dot with b':
    # k = (AA' + d(b' - b)).b' / a.b'

    def inset(self, faces, delta, **attributes):
        """  Inset one or several faces.

        ```python
        # Base icosphere
        ico = Mesh.IcoSphere()

        # Select random faces
        inds = np.random.default_rng(0).choice(range(0, len(ico.faces)), 20, replace=False)

        # Inset the faces
        ext = ico.inset(inds, delta=.05)

        # Extrude them
        ext = ico.extrude_faces(inds, offset=.1)

        # Let's see the result
        ico.to_object("Icosphere", shade_smooth=False)
        ```

        Arguments
        ---------
            - faces (int or array of inds) : the faces to extrude
            - delta (float) : inset length
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - couple of arrays of ints : inset face indices, top face indices
        """


        # ----- Extrude with null offset

        extr = self.extrude_faces(faces, offset=0, **attributes)

        normals = self.faces.normal

        # ----- Loop on the top faces

        for face_index in extr['top']:

            # ----- Vertices

            verts = self.faces[face_index].get_verts()

            # ----- Compute the locations of the new top vertices

            # Points and sides = AA'
            A = verts
            sides = np.roll(A, 1, axis=0) - A

            # Unary vectors a and previous ones
            # Caution: AA' is previous side, oriented in the opposite direction of a'
            a_ = -sides / np.linalg.norm(sides, axis=-1)[:, None]
            a  = np.roll(a_, -1, axis=0)

            # Normals
            N = normals[face_index]

            # Inside vectors
            b = np.cross(N, a)
            b_ = np.roll(b, 1, axis=0)

            # Let's compute k
            # k = (AA' + d(b' - b)).b' / a.b'

            k = np.einsum('...i, ...i', sides + (b_ - b)*delta, b_) / np.einsum('...i, ...i', a, b_)

            # Which gives the new locations
            new_verts = A + delta*b + a*k[:, None]

            self.points[self.faces[face_index].get_point_indices()].position = new_verts


        return extr

    # =============================================================================================================================
    # Deletion

    # -----------------------------------------------------------------------------------------------------------------------------
    # Delete faces

    def delete_faces(self, selection):
        """ Delete only faces.
        """

        self.faces.delete(selection)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Delete vertices

    def get_point_faces(self, points):

        # Corners matching points
        corners = np.isin(self.corners.vertex_index, points)

        # Faces having one deleted corner
        return np.unique(self.faces.reversed_indices[corners])


    def delete_vertices(self, faces=None, points=None):
        """ Delete vertices.

        Arguments
        ---------
            - faces (int or array of ints) : face indices owning the vertices
            - points (int or array of ints) : point indices to delete (and the faces)
        """

        if faces is None:
            pt_inds = np.empty(0, int)
        else:
            pt_inds = self.faces[faces].get_point_indices()

        if points is not None:
            pt_inds = np.append(pt_inds, points)

        if len(pt_inds) == 0:
            return

        faces = self.get_point_faces(pt_inds)

        # ----- Delete the faces

        if len(faces) != 0:
            self.faces.delete(faces)

        # ----- Delete the vertices

        # New vertex indices

        ren = np.ones(len(self.points))
        ren[pt_inds] = 0
        ren = np.roll(np.cumsum(ren), 1)
        ren[0] = 0

        # Delete the points

        self.points.delete(pt_inds)
        self.corners.vertex_index = ren[self.corners.vertex_index]

    # =============================================================================================================================
    # Separate islands

    # ----------------------------------------------------------------------------------------------------
    # Separate faces

    def separate_faces(self, face_indices):

        # Vertex indices

        if True:
            corner_inds = []
            for ls, lt in zip(self.faces[face_indices].loop_start, self.faces[face_indices].loop_total):
                corner_inds.extend([ls + i for i in range(lt)])
            vert_inds = self.corners.vertex_index[corner_inds]
        else:
            vert_inds   = []
            for ls, lt in zip(self.faces[face_indices].loop_start, self.faces[face_indices].loop_total):
                vert_inds.extend(list(self.corners[ls:ls+lt].vertex_index))
            vert_inds = np.array(vert_inds)

        # Reduce to the used vertices

        new_vert_inds = reduce_indices(vert_inds)

        # The extracted vertices

        verts = self.points.position[sorted(list(set(vert_inds)))]

        # Extracted mesh

        sizes = self.faces.loop_total[face_indices]

        assert(np.max(new_vert_inds)==len(verts)-1)
        assert(np.sum(sizes) == len(new_vert_inds))

        mesh = Mesh(
                verts           = verts,
                corners         = new_vert_inds,
                sizes           = sizes,
                materials       = self.materials,
                #material_index  = self.faces.material_index[face_indices],
                )

        # ----- Transfer the attributes

        vert_inds = sorted(list(set(vert_inds)))
        mesh.points.attributes.copy_from(self.points.attributes,   vert_inds,    only_new=True)
        mesh.corners.attributes.copy_from(self.corners.attributes, corner_inds,  only_new=True)
        mesh.faces.attributes.copy_from(self.faces.attributes,     face_indices, only_new=True)

        return mesh

    # ----------------------------------------------------------------------------------------------------
    # Separate islands

    def separate_islands(self):

        # ----------------------------------------------------------------------------------------------------
        # Island class

        class Island:
            def __init__(self, mesh, uniqs, face_index):
                self.mesh         = mesh
                self.uniqs        = set(uniqs)
                self.face_indices = [face_index]

            def __str__(self):
                return f"faces: {self.face_indices}, uniqs: {self.uniqs}"

            def add(self, uniqs, face_index):
                self.uniqs.update(uniqs)
                self.face_indices.append(face_index)

            def merge(self, other):
                self.uniqs.update(other.uniqs)
                self.face_indices += other.face_indices

            def to_mesh(self):
                return self.mesh.separate_faces(self.face_indices)

        # ----------------------------------------------------------------------------------------------------
        # Main

        # ----- Loop on faces to merge connected faces in their island

        islands = []
        indices = np.array(self.corners.vertex_index)

        for face_index, (vert_index, face_len) in enumerate(zip(self.faces.loop_start, self.faces.loop_total)):

            vert_indices = indices[vert_index:vert_index + face_len]
            uniqs = set(vert_indices)
            to_merge = []
            for island in islands:
                if not island.uniqs.isdisjoint(uniqs):
                    to_merge.append(island)

            if len(to_merge) == 0:
                islands.append(Island(self, uniqs, face_index))

            else:
                to_merge[0].add(uniqs, face_index)

                for i in range(1, len(to_merge)):
                    island = to_merge[i]
                    islands.remove(island)
                    to_merge[0].merge(island)

        # ----- Build one mesh per island

        return [island.to_mesh() for island in islands]

    # ====================================================================================================
    # Remove doubles

    def remove_doubles(self, dist=.001):
        """ Remove doubles.

        Arguments:
            - dist (float=0.001) : maximum distance between vertices to merge.
        """

        with self.bmesh() as bm:
            bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=dist)

    # ====================================================================================================
    # Modifiers

    # ----------------------------------------------------------------------------------------------------
    # Boolean modifier

    def boolean(self, other, operation='INTERSECT', solver='EXACT'):
        """ Boolean operation with another Mesh.

        ``` python
        sphere = Mesh.UVSphere()
        cone = Mesh.Cone(transformation=Transformations(scale=(.8, .8, 2)))

        cone.points.rotate_around(axis='Y', angle=np.pi/2)

        mesh = sphere.boolean(cone, 'DIFFERENCE')

        mesh.to_object("Boolean", shade_smooth=False)
        ```

        The methods uses the Boolean Modifier

        Arguments
        ---------
            - other (Mesh) : the mesh to make the boolean operation with
            - operation (str='INTERSECT') : boolean operation code in ['INTERSECT', 'DIFFERENCE', 'UNION']
            - solver (str='EXACT') : a valid solver key

        Returns
        -------
            - Mesh : the result of the boolean operation
        """

        obj0 = self.to_object( "GEOPY Boolean 0")
        obj1 = other.to_object("GEOPY Boolean 1")

        mod = obj0.modifiers.new("Boolean", 'BOOLEAN')

        mod.object    = obj1
        mod.operation = operation
        mod.solver    = solver

        res = Mesh.FromObject(obj0, evaluated=True)

        # ----- Remove temp objects with their meshes

        mesh0 = obj0.data
        mesh1 = obj1.data

        bpy.data.objects.remove(obj0)
        bpy.data.objects.remove(obj1)

        bpy.data.meshes.remove(mesh0)
        bpy.data.meshes.remove(mesh1)

        return res

    # ----------------------------------------------------------------------------------------------------
    # Boolean difference

    def difference(self, other, solver='EXACT'):
        """ Boolean difference with another Mesh.

        The methods uses the Boolean Modifier

        Arguments
        ---------
            - other (Mesh) : the mesh to make the boolean operation with
            - solver (str='EXACT') : a valid solver key

        Returns
        -------
            - Mesh : the result of the boolean operation
        """

        return self.boolean(other, 'DIFFERENCE', solver)

    # ----------------------------------------------------------------------------------------------------
    # Boolean intersection

    def intersect(self, other, solver='EXACT'):
        """ Boolean intersection with another Mesh.

        The methods uses the Boolean Modifier

        Arguments
        ---------
            - other (Mesh) : the mesh to make the boolean operation with
            - solver (str='EXACT') : a valid solver key

        Returns
        -------
            - Mesh : the result of the boolean operation
        """

        return self.boolean(other, 'INTERSECT', solver)

    # ----------------------------------------------------------------------------------------------------
    # Boolean union

    def union(self, other, solver='EXACT'):
        """ Boolean union with another Mesh.

        The methods uses the Boolean Modifier

        Arguments
        ---------
            - other (Mesh) : the mesh to make the boolean operation with
            - solver (str='EXACT') : a valid solver key

        Returns
        -------
            - Mesh : the result of the boolean operation
        """

        return self.boolean(other, 'UNION', solver)

    # ----------------------------------------------------------------------------------------------------
    # Boolean solidify

    def solidify(self, thickness=.01, offset=-1):
        """ Boolean difference with another MeshBuilder.

        The methods uses the Solidify Modifier

        ``` python
        glass = Mesh.Circle(segments=128)
        glass.extrude_faces(0, -.01)
        glass.extrude_faces(0, -2)
        glass.extrude_faces(0, -.01)

        glass.points.translate((0, 0, 2))

        glass = glass.solidify(thickness=.1)

        glass.to_object("Solidify", shade_smooth=True)
        ```

        Arguments
        ---------
            - thickness (float=.01) : thickness
            - offset (float=-1) : offset

        Returns
        -------
            - MeshBuilder : the result of the solidify operation
        """

        obj = self.to_object("GEOPY Solidify")

        mod = obj.modifiers.new("Solidify", 'SOLIDIFY')

        mod.thickness       = thickness
        mod.use_even_offset = True
        mod.offset          = offset

        res = Mesh.FromObject(obj, evaluated=True)

        # ----- Remove temp object with its mesh

        mesh = obj.data
        bpy.data.objects.remove(obj)
        bpy.data.meshes.remove(mesh)

        return res

    # =============================================================================================================================
    # =============================================================================================================================
    # BVHTree
    # =============================================================================================================================

    def bvh_tree(self, count=None):
        if count is None:
            return BVHTree.FromPolygons(self.points.position, self.faces.sequences(), all_triangles=False, epsilon=0.0)

        else:
            pos    = self.points.position
            pos    = np.reshape(pos, (count, len(pos)//count, 3))

            nfaces = len(self.faces)//count
            inds   = list(self.corners.vertex_index)
            faces  = [inds[lstart:lstart+ltotal] for (lstart, ltotal) in zip(self.faces.loop_start[:nfaces], self.faces.loop_total[:nfaces])]

            return [BVHTree.FromPolygons(pos[i], faces, all_triangles=False, epsilon=0.0) for i in range(count)]
