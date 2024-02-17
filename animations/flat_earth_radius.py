#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:39:07 2023

@author: alain

VIDEO : The Flat Earth Radius
"""

import numpy as np
import geopy as gp
import bpy

PI = np.pi
TAU = 2*PI

# -----------------------------------------------------------------------------------------------------------------------------
# GLOBAL

SIZE = 1.
W = 2*SIZE
H = SIZE

# -----------------------------------------------------------------------------------------------------------------------------
# Planisphere

def planisphere(earth, segms, rings):
    
    x, y = np.meshgrid(np.linspace(-W/2, W/2, segms), np.linspace(-H/2, H/2, rings))
    
    earth.points.x = np.reshape(x, segms*rings)
    earth.points.y = np.reshape(y, segms*rings)
    earth.points.z = 0

# -----------------------------------------------------------------------------------------------------------------------------
# Planisphere to disk

def plane_to_disk(earth, factor, segms, rings):
    
    planisphere(earth, segms, rings)
    
    factor = np.clip(factor, 0, 1)
    if factor < 0.001:
        return
    
    # ----- Curvature angle and rotation center
    
    angle = TAU*factor
    cy    = W/angle - W/TAU + H/2

    # ----- Polar coordinates
    
    ag = earth.points.x/W*angle
    r  = earth.points.y - cy

    # ----- Transformation
    
    x = -r*np.sin(ag)
    y = r*np.cos(ag) + cy - H/2*factor
    
    earth.points.x = x
    earth.points.y = y
    

# -----------------------------------------------------------------------------------------------------------------------------
# Planisphere to sphere

def plane_to_sphere(earth, factor, segms, rings):
    
    planisphere(earth, segms, rings)
    
    fac0 = np.clip(factor*2, 0, 1)
    fac1 = np.clip(factor*2, 1, 2) - 1
    #fac2 = np.clip(factor*3, 2, 3) - 2

    #if fac0 > 0.001:
    #    earth.points.rotate_x(PI/2*fac2)

    if fac0 > .001:
        earth.points.bend(angle=-PI*fac0, axis='X', direction='Y')
        earth.points.z += H/PI*fac0
        
    if fac1 > .001:
        earth.points.bend(angle=TAU*fac1, axis='Y', direction='X', pivot=(0, 0, H/PI))
        
# -----------------------------------------------------------------------------------------------------------------------------
# Graduated Circle

def graduated_circle(obj_name, radius=1., thickness=.01, full=True):
    
    if full:
        curve = gp.Curve.Circle(resolution=360, radius=radius)
    else:
        curve = gp.Curve.Arc(cls, resolution=180, radius=radius, start_angle=0., sweep_angle=np.pi, connect_center=False, invert_arc=False)
        
    curve.points.radius = thickness
    curve.points.new_float_attribute('angle', 0)
    curve.points.angle = np.linspace(0, 359 if full else 180, len(curve.points))
    
    meshed = curve.to_mesh(profile=12)
    meshed.materials = ["Graduations"]
    
    return meshed.to_object(obj_name)

# ====================================================================================================
# A variable arrow along an arc of circle

def arc_arrow(obj, material=None):
    
    # Arrow group of parameters, make sure it is defined
    
    group = gp.param_group("Arrow")
    #group.to_object(obj)
    
    # Read the parameters
    
    radius      = group.get_value(obj, "Radius")
    section     = group.get_value(obj, "Section")
    start_angle = group.get_value(obj, "Start Angle")
    angle       = group.get_value(obj, "Angle")
    plane       = group.get_value(obj, "Plane")
    
    # Sweep angle must be decreased to take into account the length of the head
    
    head_length = section
    delta = head_length/radius
    
    no_curve = delta > abs(angle)
    if angle < 0:
        delta *= -1
        
    # Build the arrow
    
    curve = gp.Curve.Arc(radius=radius, start_angle=start_angle, sweep_angle=angle - delta)
    curve.points.radius = section
    if no_curve:
        mesh = gp.Mesh()
    else:
        mesh  = curve.to_mesh(12)
    
    # Add the head
    
    cone = gp.Mesh.Cone()
    cone.points.translate((0, 0, 1))
    cone.points.scale((section/3, section/3, section/2))
    
    tracker = gp.tracker(curve.splines.tangent(0. if no_curve else 1.)*(-1 if no_curve else 1), 'Z', None)
    cone.points.transform(tracker[0])
    cone.points.translate(curve.points[0 if no_curve else -1].position)
    
    mesh.join(cone)
    if material is not None:
        mesh.materials = [material]
    
    # Label
    
    if False:
        txt_rot     = group.get_value(obj, "Text Rotation")
        txt_loc     = group.get_value(obj, "Text Translation")
        
        txt = gp.Text(label, align_x='CENTER', size=section*1)
        txt.solidify(extrude=section*.05, bevel_depth=section*.02)
        m_text = txt.to_mesh()
        
        m_text.points.rotate(txt_rot)
        m_text.points.translate(curve.points[-1].position + txt_loc)
        
        if text_material is not None:
            m_text.materials = [text_material]
        
        mesh.join(m_text)
    
    # Rotation
    
    if plane == 'X':
        mesh.points.rotate_y(np.pi/2)
    elif plane == 'Y':
        mesh.points.rotate_x(np.pi/2)
    
    mesh.to_object(obj.name)
    
# ====================================================================================================
# Create the group of parameters

def create_arc_arrow_group():
    group = gp.new_param_group("Arrow")
    group.new("Radius", 1., min=.01, max=10)
    group.new("Section", .1, min=.0001, max=10)
    group.new("Start Angle", 0., subtype='ANGLE')
    group.new("Angle", np.pi/4, subtype='ANGLE')
    group.new("Plane", 'Z')
    #group.new("Text Rotation",  (0., 0., 0.), subtype='ANGLE')
    #group.new("Text Translation", (0., 0., 0.))
    
def create_earth_group():
    group = gp.new_param_group("Earth")
    group.new("Factor", 0., min=-1, max=1, description="Disk to sphere transformation factor")
    
        
# -----------------------------------------------------------------------------------------------------------------------------
# Part 1

def part1():
    
    fglobe = gp.functions.Function.FromFCurve(gp.blender.get_fcurve("Globe Ctl (E)", "location.z"))
    fdisk = gp.functions.Function.FromFCurve(gp.blender.get_fcurve("Disk Ctl (E)", "location.z"))

    def update(eng):
        
        if eng.rendering:
            segms = 320
            rings = 160
        else:
            segms = 32
            rings = 16
        
        for obj_name in ['Globe', 'Disk']:
            
            obj = gp.blender.get_object(obj_name)
            if obj.hide_viewport:
                continue
            
            earth = gp.Mesh.Grid(20, 10, segms, rings, materials="Earth")

            #factor = gp.blender.get_object(f"{obj_name} Ctl (E)").location.z
            if obj_name == 'Globe':
                factor = fglobe(eng.frame)
            else:
                factor = fdisk(eng.frame)
        
            if factor < 0:
                factor = np.clip(-factor, 0, 1)
                plane_to_disk(earth, factor, segms, rings)
            else:
                factor = np.clip(factor, 0, 1)
                plane_to_sphere(earth, factor, segms, rings)
                
            earth.remove_doubles()    
            earth.to_object(obj)
        
    gp.engine.go(update)
    
# -----------------------------------------------------------------------------------------------------------------------------
# Part 2

def part2(arrows=[]):
    
    create_arc_arrow_group()
    create_earth_group()
    
    disk_name = 'Disk'
    disk_obj = gp.blender.get_object(disk_name)
    earth_group = gp.param_group("Earth")
    earth_group.to_object(disk_obj)
    
    for obj_name in arrows:
        arr_obj = gp.blender.get_object(obj_name)
        arrow_group = gp.param_group("Arrow")
        arrow_group.to_object(arr_obj)

    def update(eng):
        
        # ----- Earth
        
        if eng.rendering:
            segms = 320
            rings = 160
        else:
            segms = 32
            rings = 16
            
        earth = gp.Mesh.Grid(20, 10, segms, rings, materials="Earth")
        
        factor = earth_group.get_value(eng.get_evaluated(disk_obj), "Factor")
    
        if factor < 0:
            factor = np.clip(-factor, 0, 1)
            plane_to_disk(earth, factor, segms, rings)
        else:
            factor = np.clip(factor, 0, 1)
            plane_to_sphere(earth, factor, segms, rings)
            
        earth.remove_doubles()    
        earth.to_object(disk_obj)
        
        # ----- Arrows
        
        for obj_name in arrows:
            
            obj = eng.get_evaluated(obj_name)
            #if obj.hide_render:
            #    continue
        
            angle = arrow_group.get_value(obj, "Angle")
            
            delta = 0 if eng.frame < 882 else 10
            #label = f"{abs(np.degrees(angle) - delta):.0f}° W" if angle < 0 else f"{np.degrees(angle) + delta:.0f}° E"
            
            arc_arrow(obj, "Monocolor") 
        
    gp.engine.go(update)    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Full Resol

def full_resol():
    
    segms = 320
    rings = 160
            
    
    # ----- Disk

    earth = gp.Mesh.Grid(20, 10, segms, rings, materials="Earth")
    plane_to_disk(earth, 1, segms, rings)
    earth.remove_doubles()    
    earth.to_object("Disk")
    
    # ----- Sphere
    
    earth = gp.Mesh.Grid(20, 10, segms, rings, materials="Earth")
    plane_to_sphere(earth, 1, segms, rings)
    earth.remove_doubles()    
    earth.to_object("Sphere")

    



    


