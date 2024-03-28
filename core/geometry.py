#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov 10 11:13:13 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Root class for geometries
"""

import bpy
from geonodes.core import blender

# =============================================================================================================================
# Root class for geometries

class Geometry:
    
    @staticmethod
    def LoadObject(name):
        """ Load a Blender object and returns either a Mesh or a Curve.
        
        Arguments
        ---------
            - name (str or bpy.types.Object) : the object to load
            
        Returns
        -------
            - Mesh or Curve
        """

        from geonodes.core.mesh import Mesh
        from geonodes.core.curve import Curve
        
        obj = blender_getobject(name)
        if isinstance(obj.data, bpy.types.Mesh):
            return Mesh.FromObject(oj)
        
        elif isinstance(obj.data, bpy.types.Curve):
            return Curve.FromObject(obj)
        
        else:
            raise Exception(f"Geometry.LoadObject error: impossile to load the objet '{obj.name}' of type '{type(obj.data).__name__}'")
    
    
    @staticmethod
    def LoadModel(model):
        """ Load a geometry or geometries from specification.
        
        The model can be:
            - a string : the name of a Blender object
            - a Blender object : the object to load
            - a Blender collection : the object to load
            - a list of these items : the list of objects to load
            
        Note that if model is a list or a collection, the method return Instances with models
        initialized with this list. 
        
        Arguments
        ---------
            - model (any)
            
        Returns
        -------
            - Mesh or Curve or arrays of Meshes and Curves
        """

        from geonodes.core.mesh import Mesh
        from geonodes.core.curve import Curve
        from geonodes.core.cloud import Cloud
        from geonodes.core.instances import Instances
        
        if isinstance(model, (Mesh, Curve, Cloud, Instances)):
            return model
        
        elif isinstance(model, bpy.types.Collection):
            subs = [Geometry.FromModel(obj) for obj in model.objects]
            insts = Instances(np.zeros((len(subs), 3), float), subs)
            return insts
            
        elif isinstance(model, list):
            subs = [Geometry.FromModel(obj) for obj in model]
            insts = Instances(np.zeros((len(subs), 3), float), subs)
            return insts
        
        obj = blender.get_object(model)
        if isinstance(obj.data, bpy.types.Mesh):
            return Mesh.FromObject(obj)
        
        elif isinstance(obj.data, bpy.types.Curve):
            return Curve.FromObject(obj)
        
        else:
            raise Exception(f"Geometry.FromObject error: impossile to load the objet '{obj.name}' of type '{type(obj.data).__name__}'")
    
    
    
        
        
    





