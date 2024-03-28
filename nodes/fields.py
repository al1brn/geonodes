#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:06:28 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

bonus : fields
--------------
"""

import bpy
from mathutils import Color

from geonodes import GeoNodes, Shader

subs = GeoNodes.prefixed("G")

# =============================================================================================================================
# Base Geometry nodes

# -----------------------------------------------------------------------------------------------------------------------------
# Vector coordinates from index
#
# coords(resolution=10) -> vector, x, y

with GeoNodes("Coords", is_group=True, prefix=subs) as tree:
    count = tree.integer_input("Resolution", 10, min_value=2, max_value=1000)
    
    idx = tree.Index().index
    count2 = count-1
    
    i = (idx/count).float_to_integer("TRUNCATE")/count2
    j = (idx % count)/count2
    
    i.float_to_integer('TRUNCATE').to_output("i")
    j.float_to_integer('TRUNCATE').to_output("j")
    
    
    #tree.xyz(x, y, 0).to_output("Vector")
    
    #x.to_output("x")
    #y.to_output("y")

# -----------------------------------------------------------------------------------------------------------------------------
# Gradient : Nabla dot Scalar Field
#
# The scalar field is passed as a group of template:
# field(vector) -> value

# gradient(vector, delta=.01) -> Vector

def gen_gradient(name, group_name, is_3d=False):
    
    with GeoNodes(name, is_group=True, prefix=subs) as tree:

        v     = tree.vector_input("Vector")
        delta = tree.float_input("Delta", 0.01, min_value=0., max_value=1)
    
        delta2 = delta/2
    
        x = (tree.group(group_name, vector= v + tree.xyz(delta2, 0, 0)).value -  tree.group(group_name, vector= v - tree.xyz(delta2, 0, 0)).value)/delta
        y = (tree.group(group_name, vector= v + tree.xyz(0, delta2, 0)).value -  tree.group(group_name, vector= v - tree.xyz(0, delta2, 0)).value)/delta
        if is_3d:
            z = (tree.group(group_name, vector= v + tree.xyz(0, 0, delta2)).value -  tree.group(group_name, vector= v - tree.xyz(0, 0, delta2)).value)/delta
        else:
            z = 0
    
        tree.xyz(x, y, z).to_output("Vector")
        
# -----------------------------------------------------------------------------------------------------------------------------
# Curl : Nabla cross Vector Field
#
# The vector field is passed as a group of template:
# field(vector) -> vector

# curl(vector, delta=.01) -> Vector

def gen_curl(name, group_name):
    
    with GeoNodes(name, is_group=True, prefix=subs) as tree:
        
        v     = tree.vector_input("Vector")
        delta = tree.float_input("Delta", 0.01, min_value=0., max_value=1)
        
        delta2 = delta/2
        
        with tree.layout("Deriving along x"):
            v1x = tree.group(group_name, vector=v + (delta2, 0, 0)).vector
            v0x = tree.group(group_name, vector=v - (delta2, 0, 0)).vector
            dx = (v1x - v0x)/delta
            
        with tree.layout("Deriving along y"):
            v1y = tree.group(group_name, vector=v + (0, delta2, 0)).vector
            v0y = tree.group(group_name, vector=v - (0, delta2, 0)).vector
            dy = (v1y - v0y)/delta
            
        with tree.layout("Deriving along z"):
            v1z = tree.group(group_name, vector=v + (0, 0, delta2)).vector
            v0z = tree.group(group_name, vector=v - (0, 0, delta2)).vector
            dz = (v1z - v0z)/delta
            
        with tree.layout("Resulting vector"):
            tree.xyz(dy.z - dz.y, dz.x - dx.z, dy.x - dx.y).to_output("Vector")
            
# -----------------------------------------------------------------------------------------------------------------------------
# Visualize a vector field
#
# show_vector_field(points, fieldn size=.1, use_cone=True)

with GeoNodes("Show Vector Field", is_group=True, prefix=subs) as tree:
    
    points   = tree.geometry_input("Points")
    field    = tree.vector_input("Field")
    size     = tree.float_input("Size", .1, min_value=0, max_value=1)
    use_cone = tree.boolean_input("Use Cones", True)
    mat      = tree.material_input("Material", True)
    
    line = tree.mesh_line(offset=(0, 0, 1)).switch(use_cone, tree.cone(radius_bottom=.1))
    
    length = tree.min(field.length(), 10)
    
    lines  = points.instance_on_points(instance=line, scale=length*size)
    
    lines.rotate_instances(rotation=tree.AlignEulerToVector(vector=field, axis='Z').rotation)
    
    lines.material = mat
    
    lines.to_output("Arrows")
    
# -----------------------------------------------------------------------------------------------------------------------------
# Charges field
#
# Scalar field based on charges defined at points in a geometry

with GeoNodes("Charged Field", is_group=True, prefix=subs) as tree:
    
    v = tree.vector_input("Vector")
    
    charges = tree.ObjectInfo("Charges").geometry
    
    n = charges.domain_size(component='MESH').point_count
    
    with tree.repeat(iterations=n, values=v.x * 0., index=0) as rep:
        
        q = charges.sample_index_float(value=charges.named_float("charge"), index=rep.index)
        p = charges.sample_index_vector(value=charges.position, index=rep.index)
        
        r = (p - v).length()
        
        rep.values += q/r**2
        
        rep.index += 1
        
    value = rep.values
    value.to_output("Value")
    
    
    
    
# =============================================================================================================================
# Demo
# Use a random scalar field generated fo

def gen_demo1():
    
    with Shader("Scalar Field") as tree:
        ped = tree.PrincipledBSDF(base_color = tree.Attribute(attribute_name="scalar").fac)
        tree.output_surface = ped.bsdf
    
    with Shader("Red Arrows") as tree:
        ped = tree.PrincipledBSDF(base_color=Color((.7, 0, 0)), roughness=.2)
        tree.output_surface = ped.bsdf
    
    with Shader("Blue Arrows") as tree:
        ped = tree.PrincipledBSDF(base_color=Color((0, 0, .7)), roughness=.2)
        tree.output_surface = ped.bsdf
    
    # ------------------------------------------------------------------------------------------------------------------------
    # Scalar field
    
    with GeoNodes("Scalar Field", is_group=True, prefix=subs) as tree:
        
        v  = tree.vector_input("Vector")
        
        v *= (1, 1, 0)
        
        noise = tree.NoiseTexture(vector=v, scale=2)
        
        noise.fac.to_output("Value")
    
    # ------------------------------------------------------------------------------------------------------------------------
    # Vector field
    
    gen_gradient("Vector Field", "G Scalar Field")
    
    gen_curl("Curl Field", "G Vector Field")
    
    # ------------------------------------------------------------------------------------------------------------------------
    # Main
    
    with GeoNodes("Field Demo") as tree:
        
        resol  = tree.integer_input("Resolution", 10, min_value=2, max_value=1000)        
        size   = tree.float_input("Size", 0.1, min_value=0., max_value=1.)
        
        grid = tree.grid(10, 10, resol, resol)
        grid.POINT.store_named_float("scalar", value=subs.scalar_field(vector=subs.coords(resolution=resol).vector).value)
        
        grid.material="Scalar Field"
        
        # ----- Show the vector field
        
        field = subs.vector_field(vector=subs.coords(resolution=resol).vector).vector
        lines = subs.show_vector_field(points=grid, field=field, size=size, material=bpy.data.materials["Red Arrows"]).arrows
        
        # ----- Show the curl vector field
        
        curl_field = subs.curl_field(vector=field, delta=0.02).vector
        curl_lines = subs.show_vector_field(points=grid, field=curl_field, size=size*10, material=bpy.data.materials["Blue Arrows"]).arrows
            
        
        tree.og = grid.join_geometry(lines, curl_lines)
        
# =============================================================================================================================
# Electric field

def gen_electric_field():

    with Shader("Scalar Field") as tree:
        ped = tree.PrincipledBSDF(base_color = tree.Attribute(attribute_name="scalar").fac)
        tree.output_surface = ped.bsdf
    
    with Shader("Red Arrows") as tree:
        ped = tree.PrincipledBSDF(base_color=Color((.7, 0, 0)), roughness=.2)
        tree.output_surface = ped.bsdf
    
    with Shader("Blue Arrows") as tree:
        ped = tree.PrincipledBSDF(base_color=Color((0, 0, .7)), roughness=.2)
        tree.output_surface = ped.bsdf

    # ------------------------------------------------------------------------------------------------------------------------
    # Vector fields
    
    gen_gradient("Vector Field", "G Charged Field")
    
    gen_curl("Curl Field", "G Vector Field")
    
    # ------------------------------------------------------------------------------------------------------------------------
    # Main
    
    with GeoNodes("Field Demo") as tree:

        resol  = tree.integer_input("Resolution", 10, min_value=2, max_value=1000)
        size   = tree.float_input("Size", 10)
        
        show_field = tree.boolean_input("Show Vector Field", True)
        show_curl  = tree.boolean_input("Show Curl Field",  True)
        
        field_size = tree.float_input("Field Size", .1)
        curl_size  = tree.float_input("Curl Size", .1)
        
        
        grid = tree.grid(size, size, resol, resol)
        grid.POINT.store_named_float("scalar", value=subs.charged_field(vector=grid.position).value)
        
        grid.material="Scalar Field"
        
        # ----- Show the vector field
        
        field = subs.vector_field(vector=grid.position).vector
        lines = subs.show_vector_field(points=grid, field=field, size=field_size, material=bpy.data.materials["Red Arrows"]).arrows
        
        grid = grid.switch(show_field, grid + lines)
        
        # ----- Show the curl vector field
        
        curl_field = subs.curl_field(vector=field, delta=0.02).vector
        curl_lines = subs.show_vector_field(points=grid, field=curl_field, size=curl_size, material=bpy.data.materials["Blue Arrows"]).arrows
            
        grid = grid.switch(show_curl, grid + curl_lines)
        
        tree.og = grid       
        
        
        
        
        
        
        
        
        

    