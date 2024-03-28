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

from geonodes.maths.transformations import Transformations

from geonodes.core import blender
from geonodes.core.domain import InstanceDomain
from geonodes.core.geometry import Geometry
from geonodes.core.mesh import Mesh
from geonodes.core.curve import Curve
from geonodes.core.cloud import Cloud



DATA_TEMP_NAME = "GEOPY_TEMP"

class Instances(InstanceDomain, Geometry):
    
    def __init__(self, points=None, models=None, indices=None, seed=0, **attributes):
        """ Create a new cloud of points.
        
        Arguments
        ---------
            - points (array of vectors = None) : the points
            - models (geometry or list of geometries = None) : the geomtries to instantiate
            - indices (array of ints = None) : indices in the array of models
            - seed (int=0) : random seed to create the indices if required
            - **attributes (dict) : other geometry attributes
        """
        
        if isinstance(points, np.ndarray):
            cloud = Cloud()
            cloud.add_points(points)
            points = cloud.points
        
        super().__init__(domain_name='INSTANCE', points=points, models=models, indices=indices, seed=seed)
        
        # ----- Attributes
        
        for k, v in attributes.items():
            setattr(self, k, v)
        
    
    def __str__(self):
        return f"<Instances: {len(self)}, models: {len(self.models)}>"
    
    def get_transformations(self):
        
        scale    = self.Scale    if self.attributes.exists("Scale") else None
        rotation = self.Rotation if self.attributes.exists("Rotation") else None
        
        return Transformations(position=self.position, scale=scale, rotation=rotation)
    
    # =============================================================================================================================
    # =============================================================================================================================
    # I/O wit Blender
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # To Mesh and Curve
    
    def realize(self):
        mesh  = Mesh()
        curve = Curve()
        cloud = Cloud()
        insts = Instances()
        
        for model_index, model in enumerate(self.models):
            
            if len(self.models) == 1:
                sel = slice(None)
                n = len(self)
            else:
                sel = self.model_index == model_index
                n = np.sum(sel)
            
            if not n:
                continue
            geo = model * n
            
            if True:
                geo.points.transform(self.get_transformations())
                
            else:
                if self.attributes.exists('Scale'):
                    geo.points.scale(self.Scale[sel])
                    
                if self.attributes.exists('Rotation'):
                    geo.points.rotate(self.Rotation[sel])
                    
                geo.points.translate(self.position[sel])
            
            if isinstance(geo, Mesh):
                mesh.join(geo)
                
            elif isinstance(geo, Curve):
                curve.join(geo)
                
            elif isinstance(geo, Cloud):
                cloud.join(geo)
                
            elif isinstance(geo, Instances):
                instances.join(geo)
                
            else:
                assert(False)
                
        geos = {}
        if len(mesh.points) > 0:
            geos['mesh'] = mesh
            
        if len(curve.points) > 0:
            geos['curve'] = curve

        if len(cloud.points) > 0:
            geos['cloud'] = cloud
            
        if len(insts) > 0:
            geos['instances'] = insts
            
        return geos
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Create / update an object
            
    def to_object(self, name):
        """ Create or update a blender object.
        
        The method 'to_object' creates the whole geometry. It creates a new object if it doesn't already exist.
        If the object exists, it must be a mesh, there is no object type conversion.
        
        Once the object is created, use the method 'update_object' to change the vertices.
        
        Arguments
        ---------
            - name (str) : the name of the object to create
            
        Returns
        -------
            - dict of blender mesh objects
        """
        
        geos = self.realize()
        objs = {}
        for k, geo in geos.items():
            
            if len(geos) == 1:
                suffix = ""
            else:
                letter = {'mesh': 'M', 'curve': 'C', 'cloud': 'P', 'instances': 'I'}[k]
                suffix = f" ({letter})"
            
            objs[k] = geo.to_object(f"{name}{suffix}")
            
        return objs
        
    # =============================================================================================================================
    # Combining
            
    def join(self, *others):
        """ Join another Instances.
        
        Arguments
        ---------
            - other* (Instances) : the Points to append
        """
        
        assert(False)
        
        for other in others:
            assert(isinstance(other, Instances))
            self.add_from_domain(other)
                
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
        
        self.attributes.multiply(count)
        
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
        
        insts = Instances()
        insts.join(self)
        
        insts.attributes.multiply(count)
        
        return insts
    
    # =============================================================================================================================
    # =============================================================================================================================
    # Build
    # =============================================================================================================================

    # =============================================================================================================================
    # Add points
    
    def add_instances(self, position, **attributes):
        index = len(self)
        self.add_points(len(position), position=position, **attributes)
        return index, len(self.points) - index
    
    # =============================================================================================================================
    # Delete points
    
    def clear(self):
        self.attributes.clear()
        
    def delete(self, selection):
        self.attributes.delete(selection)
        
    

        
    
