#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module


@author: alain.bernard
@email: alain@ligloo.net

-----

Text.

"""

import bpy
import mathutils

from geonodes.core import blender
from geonodes.core.curve import Curve
from geonodes.core.mesh import Mesh

PROPERTIES = ['align_x', 'align_y', 'family', 'font', 'font_bold', 'font_bold_italic', 'font_italic',
              'shear', 'size', 'small_caps_scale', 'space_character', 'space_line', 'space_word',
              'underline_height', 'underline_position',
              'offset', 'extrude', 'bevel_mode', 'bevel_depth', 'bevel_resolution', 'bevel_object',
              ]

class Text:
    def __init__(self, text="Text", model=None, **kwargs):
        self.text   = text
        self.model  = None if model is None else blender.get_object(model)
        
        for k, v in kwargs.items():
            if k in PROPERTIES:
                setattr(self, k, v)
            else:
                raise Exception(f"Text.init: unknown Text properties: '{k}'")
        
    def __str__(self):
        smodel = "None" if self.model is None else f"{self.model.name}"
        return f"<Text '{self.text}', model: {smodel} >"
        
    def to_object(self, spec, **kwargs):
        
        obj = blender.create_text_object(spec, text=self.text)
        
        for attr_name in PROPERTIES:
            value = None
            
            if attr_name in kwargs.keys():
                value = kwargs[attr_name]
            elif attr_name in dir(self):
                value = getattr(self, attr_name)
            elif self.model is not None:
                value = getattr(self.model, attr_name)
                
            if value is not None:
                setattr(obj.data, attr_name, value)
            
        return obj
    
    def to_mesh_object(self, spec, **kwargs):
        
        mesh_object = blender.create_mesh_object(spec)
        old_data = mesh_object.data
        
        obj = self.to_object("GEOPY Temp Text")

        mesh = bpy.data.meshes.new_from_object(obj)
        
        mesh_object.data = mesh

        bpy.data.meshes.remove(old_data)
        
        bpy.data.objects.remove(obj)
        
        return mesh_object
    
    def to_mesh(self, **kwargs):
        
        obj = self.to_mesh_object("GEOPY Temp Mesh")
        mesh = Mesh.FromObject(obj)
        
        bpy.data.objects.remove(obj)
        
        return mesh
    
    
    def solidify(self, extrude=.05, bevel_depth=.02, bevel_resolution=3):
        self.extrude          = extrude
        self.bevel_depth      = bevel_depth
        self.bevel_resolution = bevel_resolution
        
        
        
        
        
        

