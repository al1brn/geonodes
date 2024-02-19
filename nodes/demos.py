#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:17:44 2024

@author: alain
"""

from geonodes import GeoNodes, Shader

# ====================================================================================================
# Hello world

def hello_word():

    with GeoNodes("Hello World", clear=True) as tree:
        
        # Let's document our parameters
        count  = 100  # Grid resolution
        size   = 20   # Size
        omega  = 2.   # Period
        height = 2.   # Height of the surface
        
        
        # The base (x, y) grid
        grid = tree.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
        
        # We compute z
        with tree.layout("Computing the wave"):
            # Separate XYZ the position vector 
            s_pos = tree.position().separate_xyz()
            # Compute the distance
            distance = tree.sqrt(s_pos.x**2 + s_pos.y**2)
            # Height in z
            z = height * tree.sin(distance*omega)/distance
            
        # Let's change the z coordinate of our vertices
        grid.set_position(offset=(0, 0, z))
        
        # We are done: plugging the deformed grid as the modified geometry
        tree.output_geometry = grid.set_shade_smooth()


# ====================================================================================================
# Test tree input sockets

def test_inputs(ints=True, floats=True, vectors=True, geometry=False, other=True, constants=True, image=None, material=None):
    
    import bpy
    
    with GeoNodes("Test inputs", clear=True, names=locals()) as tree:
        
        tree.clear_io_sockets()
        tree.ig
        tree.og

        if ints:

            val = 7
            min_value = 0
            max_value = 100
            
            tree.int_input(           "Int",            value=val, min_value=min_value, max_value=max_value, description="Int")
            tree.integer_input(       "Integer",        value=val, min_value=min_value, max_value=max_value, description="Integer")
            tree.int_factor_input(    "Int Factor",     value=val, min_value=min_value, max_value=max_value, description="Int Factor")
            tree.int_percentage_input("Int Percentage", value=val, min_value=min_value, max_value=max_value, description="Int Percentage")
        
        if floats:
            
            val = 1
            min_value = 0
            max_value = 10
            
            tree.float_input(        "Float",       value=val, min_value=min_value, max_value=max_value, description="Float")
            tree.value_input(        "Value",       value=val, min_value=min_value, max_value=max_value, description="Value")
            tree.angle_input(        "Angle",       value=val, min_value=min_value, max_value=max_value, description="Angle")
            tree.distance_input(     "Distance",    value=val, min_value=min_value, max_value=max_value, description="Factor")
            tree.factor_input(       "Factor",      value=val, description="")
            tree.percentage_input(   "Percentage",  value=val, min_value=min_value, max_value=max_value, description="Percentage")
            tree.time_input(         "Time",        value=val, min_value=min_value, max_value=max_value, description="Time")
            tree.time_absolute_input("Time abs",    value=1., min_value=min_value, max_value=max_value, description="Time Absolute")
            
        if vectors:
            
            val = (1., 2., 3.)
            min_value = 0.
            max_value = 10
            
            
            tree.rotation_input("Rotation", value=None, min_value=None, max_value=None, description="")

            tree.vector_input(      "Vector",       value=val, min_value=min_value, max_value=max_value, description="Vector")
            tree.translation_input( "Translation",  value=val, min_value=min_value, max_value=max_value, description="Translation")
            tree.direction_input(   "Direction",    value=val, min_value=min_value, max_value=max_value, description="Direction")
            tree.velocity_input(    "Velocity",     value=val, min_value=min_value, max_value=max_value, description="Velocity")
            tree.acceleration_input("Acceleration", value=val, min_value=min_value, max_value=max_value, description="Acceleration")
            tree.euler_input(       "Euler",        value=val, min_value=min_value, max_value=max_value, description="Euler")
            tree.xyz_input(         "xyz",          value=val, min_value=min_value, max_value=max_value, description="xyz")
            
        if geometry:
            tree.geometry_input(    "Geometry",     value=None, description="Geometry")
            
        if other:
            
            tree.bool_input(        "Bool",         value=True,         description="Bool")
            tree.color_input(       "Color",        value=(.2, .3, 5),  description="Color")
            tree.string_input(      "String",       value="Def string", description="String")

            tree.collection_input(  "Collection",   value=None,         description="Collection")
            tree.image_input(       "Image",        value=image,        description="Image")
            tree.material_input(    "Material",     value=material,     description="Material")
            tree.object_input(      "Object",       value=None,         description="Object")
            tree.texture_input(     "Texture",      value=None,         description="Texture")
            
        if constants:
            tree.boolean(True)
            tree.color((.1, .2, .3))
            tree.image(image)
            tree.integer(123)
            tree.material(material)
            tree.string("Hello")
            tree.value(3.14)
            tree.vector((1, 2, 3))
            
            