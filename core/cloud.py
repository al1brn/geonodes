#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov 10 11:50:13 2023

@author: alain

Mesh geometry
"""

from contextlib import contextmanager

import numpy as np
import bpy
import mathutils
import bmesh

from geonodes.maths.transformations import Transformations

from geonodes.core import blender
from geonodes.core import topology
from geonodes.core.geometry import Geometry
from geonodes.core.domain import PointDomain, CornerDomain, FaceDomain


DATA_TEMP_NAME = "GEOPY_TEMP"

class Cloud(Geometry):

    def __init__(self, points=None, **attrs):
        """ Create a new cloud of points.

        Arguments
        ---------
            - points (array of vectors = None) : the points
            - **attrs (dict) : other geometry attributes
        """

        # ----- Initialize an empty geometry

        self.points  = PointDomain.New()

        # ----- Fill the geometry

        if points is not None:
            self.points.add_points(points, **attrs)

    def __str__(self):
        return f"<Points: {self.points.shape}>"

    # =============================================================================================================================
    # Clear the geometry

    def clear(self):
        self.points.attributes.clear()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Capture another Points

    def capture(self, other):
        """ Capture the data of another Points.

        Arguments
        ---------
            - other (Points) : the points to capture

        Returns
        -------
            - self
        """

        self.points  = other.points

        return self

    # =============================================================================================================================
    # =============================================================================================================================
    # Initialization methods
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from another Mesh

    @classmethod
    def FromPoints(cls, other):
        """ Create a Points from another Points.

        Arguments
        ---------
            - other (Points) : the points to copy

        Returns
        -------
            - Points
        """

        points = cls()
        points.points.attributes  = other.points.attributes.clone()

        return points

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from an object

    @classmethod
    def FromObject(cls, obj, evaluated=False):
        """ Create a Points from an existing object.

        Arguments
        ---------
            - obj (str or Blender object) : the object to initialize from
            - evaluated (bool = False) : object modified by the modifiers if True, raw vertices otherwise

        Returns
        -------
            - Points
        """

        if evaluated:
            depsgraph = bpy.context.evaluated_depsgraph_get()
            obj = blender.get_object(obj).evaluated_get(depsgraph)
        else:
            obj = blender.get_object(obj)

        if isinstance(obj.data, bpy.types.Mesh):
            mesh = Mesh.FromObject(obj)
            points = cls()
            points.add(mesh.points.position)

        elif isinstance(obj.data, bpy.types.Curve):
            curve = Curve.FromObject(obj)
            points = cls()
            points.add(curve.points.position)

        else:
            raise RuntimeError(f"Impossible to load points from object '{obj.name}' of type '{type(obj.data)}'")

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

        points = cls()

        # ----- Vertices

        n = len(bl_mesh.vertices)
        if n != 0:
            # Positions will be read as position attribute
            points.points.add(n)

        # ----- Attributes

        points.points.attributes.from_object(bl_mesh)

        return points

    # =============================================================================================================================
    # =============================================================================================================================
    # I/O wit Blender
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create / update an object

    def to_object(self, obj):
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
        # Vertices

        if len(self.points):
            bl_mesh.vertices.add(len(self.points))

        # ----------------------------------------------------------------------------------------------------
        # Attributes

        self.points.attributes.to_object(bl_mesh, update=False)

        # ----------------------------------------------------------------------------------------------------
        # Update

        bl_mesh.update()

    # =============================================================================================================================
    # bmesh edition

    @contextmanager
    def bmesh(self, readonly=False):
        """ Acces to bmesh api.

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
            self.capture(Points.FromMeshData(data))

        bm.free()

    # =============================================================================================================================
    # Acces to blender data

    @contextmanager
    def blender_data(self, readonly=False):
        """ Acces to Blender Mesh API.

        Transfer the geometry to a temporay Blender Mesh.

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
    # Combining

    def join(self, *others):
        """ Join another Points.

        Arguments
        ---------
            - other* (Points) : the Points to append
        """

        for other in others:
            self.points.attributes.join(other.points.attributes)

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
            return

        self.points.attributes.multiply(count)

        return self


    def multiply(self, count=10, **attributes):
        """ Duplicate the geometry.

        Multiplying is a way to efficiently duplicate the geometry a great number of times.
        One duplicated, the vertices can be reshapped to address each instance individually.

        Arguments
        ---------
            - count (int=10) : number of instances
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - MeshBuilder
        """

        points = Points()
        points.join(self)

        points *= count
        return points

    # =============================================================================================================================
    # =============================================================================================================================
    # Build
    # =============================================================================================================================

    # =============================================================================================================================
    # Add points

    def add_points(self, points,  **attributes):
        index = len(self.points)
        self.points.add_points(points, **attributes)
        return index, len(self.points) - index

    # =============================================================================================================================
    # Delete points

    def clear(self):
        self.points.attributes.clear()

    def delete(self, selection):
        self.points.attributes.delete(selection)
