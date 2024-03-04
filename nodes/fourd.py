#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:38:22 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : fourd
------------------
- 4D module

"""

import bpy
from geonodes import GeoNodes, Shader
from geonodes import blender

maths     = GeoNodes.prefixed("M")
modifiers = GeoNodes.prefixed("4D")
curves    = GeoNodes.prefixed("C")
surfaces  = GeoNodes.prefixed("S")

ZERO = 0.0001

def clear_all():
    maths.clear()
    modifiers.clear()
    curves.clear()
    surfaces.clear()
    
def rebuild():
    g_matrices()
    m_base()
    g_vectors()
    
    
    

# ====================================================================================================
# Shaders

# ----------------------------------------------------------------------------------------------------
# Axis Shader

with Shader("4 Axis") as tree:
    
    col = tree.Attribute(attribute_name="Axis Color").color
    
    ped = tree.PrincipledBSDF(base_color = col, roughness=.1, metallic=.3)
    
    tree.output_surface = ped.bsdf


# =============================================================================================================================
# Utils

# -----------------------------------------------------------------------------------------------------------------------------
# Generate matrices multiplication nodes
    
def mat_dot(m, v):
    tree = m.tree
    with tree.layout("Matrix @ 4-Vector"):
        return tree.rgb(
            m.m_0.red*v.red + m.m_0.green*v.green + m.m_0.blue*v.blue + m.m_0.alpha*v.alpha,
            m.m_1.red*v.red + m.m_1.green*v.green + m.m_1.blue*v.blue + m.m_1.alpha*v.alpha,
            m.m_2.red*v.red + m.m_2.green*v.green + m.m_2.blue*v.blue + m.m_2.alpha*v.alpha,
            m.m_3.red*v.red + m.m_3.green*v.green + m.m_3.blue*v.blue + m.m_3.alpha*v.alpha)
    
def position4(geo):
    return geo.node.tree.rgb_a(geo.position, geo.named_float("w"))

def set_position4(geo, v4):
    tree = geo.tree
    with tree.layout("Set 4-Position"):
        geo.position = v4
        geo.POINT.store_named.float(v4.w)
        
def get_normal4(geo):
    return V4(geo.named_float_color("N4"))

def set_normal4(geo, v4):
    return geo.FACE.store_named_float_color("N4", v4)

def get_tangent4(geo):
    return V4(geo.named_float_color("T4"))

def set_tangent4(geo, v4):
    return geo.CURVE.store_named_float_color("T4", v4)

# =============================================================================================================================
# Matrices groups
# Groups:
# - Mat Mult
# - XW Rotation
# - YW Rotation
# - ZW Rotation
# - Projection Matrix
# - Projection

def g_matrices():
    
    # ----------------------------------------------------------------------------------------------------
    # Ensure Projection and Projection2 objects exist
    
    blender.get_empty("Projection")
    blender.get_empty("Projection2")
    
    # ----------------------------------------------------------------------------------------------------
    # Matrices multiplication
    
    with GeoNodes("Mat Mult", is_group=True, fake_user=True, prefix=maths) as tree:
        
        a0 = tree.color_input("A 0")
        a1 = tree.color_input("A 1")
        a2 = tree.color_input("A 2")
        a3 = tree.color_input("A 3")
        
        b0 = tree.color_input("B 0")
        b1 = tree.color_input("B 1")
        b2 = tree.color_input("B 2")
        b3 = tree.color_input("B 3")
        
        c0 = tree.rgb(b0.x, b1.x, b2.x, b3.x)
        c1 = tree.rgb(b0.y, b1.y, b2.y, b3.y)
        c2 = tree.rgb(b0.z, b1.z, b2.z, b3.z)
        c3 = tree.rgb(b0.w, b1.w, b2.w, b3.w)
        
        tree.rgb(a0.dot(c0), a0.dot(c1), a0.dot(c2), a0.dot(c3)).to_output("M 0")
        tree.rgb(a1.dot(c0), a1.dot(c1), a1.dot(c2), a1.dot(c3)).to_output("M 1")
        tree.rgb(a2.dot(c0), a2.dot(c1), a2.dot(c2), a2.dot(c3)).to_output("M 2")
        tree.rgb(a3.dot(c0), a3.dot(c1), a3.dot(c2), a3.dot(c3)).to_output("M 3")
            
    # ----------------------------------------------------------------------------------------------------
    # XW / YZ rotations
    
    with GeoNodes("XW Rotation", is_group=True, fake_user=True, prefix=maths) as tree:

        ag = tree.angle_input("Angle")
        ca = tree.cos(ag)
        sa = tree.sin(ag)
        
        a2 = tree.angle_input("Second")
        c2 = tree.cos(a2)
        s2 = tree.sin(a2)
        
        tree.rgb(ca,  0,   0, -sa).to_output("M 0")
        tree.rgb( 0, c2, -s2,   0).to_output("M 1")
        tree.rgb( 0, s2,  c2,   0).to_output("M 2")
        tree.rgb(sa,  0,   0,  ca).to_output("M 3")
        
    # ----------------------------------------------------------------------------------------------------
    # YW / ZX rotations
    
    with GeoNodes("YW Rotation", is_group=True, fake_user=True, prefix=maths) as tree:

        ag = tree.angle_input("Angle")
        ca = tree.cos(ag)
        sa = tree.sin(ag)
        
        a2 = tree.angle_input("Second")
        c2 = tree.cos(a2)
        s2 = tree.sin(a2)
        
        tree.rgb(  c2,  0, s2,   0).to_output("M 0")
        tree.rgb(   0, ca,  0,  sa).to_output("M 1")
        tree.rgb( -s2,  0, c2,   0).to_output("M 2")
        tree.rgb(   0,-sa,  0,  ca).to_output("M 3")
        
    # ----------------------------------------------------------------------------------------------------
    # ZW / XY rotations
    
    with GeoNodes("ZW Rotation", is_group=True, fake_user=True, prefix=maths) as tree:

        ag = tree.angle_input("Angle")
        ca = tree.cos(ag)
        sa = tree.sin(ag)
        
        a2 = tree.angle_input("Second")
        c2 = tree.cos(a2)
        s2 = tree.sin(a2)
        
        tree.rgb( c2, -s2,  0,   0).to_output("M 0")
        tree.rgb( s2,  c2,  0,   0).to_output("M 1")
        tree.rgb(  0,   0, ca, -sa).to_output("M 2")
        tree.rgb(  0,   0, sa,  ca).to_output("M 3")

    # ----------------------------------------------------------------------------------------------------
    # Projection matrix

    with GeoNodes("Projection Matrix", is_group=True, fake_user=True, prefix=maths) as tree:
        
        abc = tree.ObjectInfo("Projection").rotation
        a = abc.x
        b = abc.y
        c = abc.z
        
        second = tree.ObjectInfo("Projection2").rotation
        a2 = second.x
        b2 = second.y
        c2 = second.z
        
        m0 = maths.xw_rotation(angle=a, second=a2)
        m1 = maths.yw_rotation(angle=b, second=b2)
        m2 = maths.zw_rotation(angle=c, second=c2)
        
        m = maths.mat_mult(
            a_0 = m0.m_0, a_1 = m0.m_1, a_2 = m0.m_2, a_3 = m0.m_3,
            b_0 = m1.m_0, b_1 = m1.m_1, b_2 = m1.m_2, b_3 = m1.m_3)
            
        m = maths.mat_mult(
            a_0 = m.m_0,  a_1 = m.m_1,  a_2 = m.m_2,  a_3 = m.m_3,
            b_0 = m2.m_0, b_1 = m2.m_1, b_2 = m2.m_2, b_3 = m2.m_3)
            
        # ----- 4-vectors
            
        m.m_0.to_output("M 0")
        m.m_1.to_output("M 1")
        m.m_2.to_output("M 2")
        m.m_3.to_output("M 3")

    # ----------------------------------------------------------------------------------------------------
    # Perform a projection

    with GeoNodes("Projection", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.color_input("V4")
        m = maths.projection_matrix()
        
        r = mat_dot(m, v)
        xyz, w = r.xyz_w
        
        xyz.to_output("Vector")
        w.to_output("w")
        

# ====================================================================================================
# Base modifiers
# Modifiers:
# - To 4D
# - Arrow
# - Axis
# - Dot normal
# - Projection

def m_base():
        
    # ----------------------------------------------------------------------------------------------------
    # Add the 4D attributes

    with GeoNodes("To 4D", fake_user=True, prefix=modifiers) as tree:
        
        geo = tree.ig
        w   = tree.float_input("w")
        
        # ----- The fourth dimention
        
        geo.POINT.store_named_float("w", w)
        
        # ----- Normals and tangent
        
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ---- Mesh normals
        
        mesh.POINT.store_named_float_color("N4", tree.rgb_a(mesh.normal, 0.))
        
        # ---- Curve tangents
        
        curve.POINT.store_named_float_color("T4", tree.rgb_a(curve.curve_tangent, 0.))
            
        # ---- Result
        
        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # Arrow

    with GeoNodes("Arrow", fake_user=True, prefix=modifiers) as tree:
        
        v0     = tree.vector_input("Start xyz", (0, 0, 0))
        w0     = tree.float_input( "Start w", 0)
        v1     = tree.vector_input("End xyz", (0, 0, 1))
        w1     = tree.float_input( "End w", 0)
        
        radius = tree.float_input(   "Radius", 0.05)
        resol  = tree.integer_input( "Resolution", 8, min_value=3, max_value=32)
        mat    = tree.material_input("Material")
        
        with tree.layout("Arrow shaft"):
        
            # ----- Arrow direction
            
            u0 = tree.rgb_a(v0, w0)
            u1 = tree.rgb_a(v1, w1)
            
            # ----- Start and end point

            p0 = maths.projection(v4=u0).vector
            p1 = maths.projection(v4=u1).vector
            
            # ----- Arrow shaft
            
            line = tree.CurveLine(start=p0, end=p1).curve
            
            mesh = line.curve_to_mesh(profile_curve=tree.CurveCircle(radius=radius, resolution=resol).curve, fill_caps=True)
            
        with tree.layout("Arrow head"):
            
            cone = tree.Cone(vertices=resol, depth=9*radius, radius_bottom=3.5*radius).mesh
            
            rot = tree.vector(0).align_euler_to_vector(vector=p1 - p0, axis='Z')
            cone.transform_geometry(translation=p1, rotation=rot)
            
            mesh += cone
            
        mesh.material = mat
        mesh.FACE.shade_smooth = True
        
        tree.og = mesh
        
    # ----------------------------------------------------------------------------------------------------
    # The four Axis            
            
    with GeoNodes("Axis", fake_user=True, prefix=modifiers) as tree:
        
        neg    = tree.float_input(  "Negative", -1, max_value=0.)
        pos    = tree.float_input(  "Positive",  3,  min_value=0.)
        radius = tree.float_input(  "Radius", 0.05)
        resol  = tree.integer_input("Resolution", 8, min_value=3, max_value=32)
        
        # ----- Loop on the axis
        
        for i in range(4):
        
            node = modifiers.arrow(
                start_xyz = [(neg, 0, 0), (0, neg, 0), (0, 0, neg), (0, 0, 0)][i],
                start_w   = [0, 0, 0, neg][i],
                end_xyz   = [(pos, 0, 0), (0, pos, 0), (0, 0, pos), (0, 0, 0)][i],
                end_w     = [0, 0, 0, pos][i],
            )
            tree.input_node.plug_to(node)
            arrow = node.geometry
            
            arrow.FACE.store_named_vector("Axis Color", [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)][i])
            
            if i == 0:
                axis = arrow
            else:
                axis += arrow
                
        axis.FACE.material = "4 Axis"
                    
        tree.og = axis
        
    # ----------------------------------------------------------------------------------------------------
    # Perform a projection

    with GeoNodes("Projection", fake_user=True, prefix=modifiers) as tree:
        
        geo          = tree.ig
        shade_smooth = tree.bool_input("Shade smooth", True)
        
        # ----- All
        
        with tree.layout("All points projection"):
            
            v4 = tree.rgb_a(geo.position, geo.named_float("w"))
            geo.POINT.position = maths.projection(v4=v4).vector
            
        # ----- Components
        
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        with tree.layout("Mesh projection"):
            
            with tree.layout("Normals projection"):
                
                n4 = mesh.named_color("N4")
                n  = maths.projection(v4=n4).vector
                
                mesh.POINT.store_named_vector("N", n)
                
            with tree.layout("Back face"):
                
                proj_dir = maths.projection_matrix().m_3
                mesh.POINT.store_named_float("orientation", proj_dir.dot(n4))
                
            mesh.FACE.shade_smooth = shade_smooth
            
        with tree.layout("Curve projection"):
            
            with tree.layout("Tangents projection"):
                
                t  = maths.projection(v4=mesh.named_color("T4")).vector
                
                curve.POINT.store_named_vector("T", t)
                
        tree.og = tree.join_geometry(mesh, curve, cloud, inst)
        
        
# =============================================================================================================================
# Vectors groups
# Groups
# - Normal basis
        
def g_vectors():
            
    # ----------------------------------------------------------------------------------------------------
    # Normal basis
    #
    # 3 vectors forming a normal basis to a 2D hyperplane defined by three independant vectors

    with GeoNodes("Normal basis", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.color_input("V4 0", (1., 0., 0., 0.))
        u1 = tree.color_input("V4 1", (0., 1., 0., 0.))
        u2 = tree.color_input("V4 2", (0., 0., 1., 0.))
        
        # ----- Let's normalize the first input
        
        e0, err = u0.normalized(ZERO)
            
        # Let's suppress this dimension in the second one
        
        with tree.layout("Make the second vector perp to the first"):
            
            d = e0.dot(u1)
            u1 = u1 - d*e0
            
            # ----- Let's normalize
            
            e1, err1 = u1.normalized(ZERO)
            err += err1
            
        with tree.layout("Make the third vector perp to the two other ones"):
        
            # ----- (u0, u1) are two basis vectors
            # Let's suppress these dimensions in the third one

            d   = e0.dot(u2)
            u2  = u2 - d*e0
            
            d = e1.dot(u2)
            u2 = u2 - d*e1
            
            # ----- Let's normalize
            
            e2, err2 = u2.normalized(ZERO)
            err += err2
            
        # ----- We are done :-)
        
        e0.to_output("V4 0")
        e1.to_output("V4 1")
        e2.to_output("V4 2")
        
        err.to_output("Error")
                
    # ----------------------------------------------------------------------------------------------------
    # Cross
    #
    # A vector peprpendicular to three independant vectors

    with GeoNodes("Cross", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.color_input("V4 0") #, (1., 0., 0., 0.))
        u1 = tree.color_input("V4 1") #, (0., 1., 0., 0.))
        u2 = tree.color_input("V4 2") #, (0., 0., 1., 0.))
        
        # ----- Convert the three input vectors in a normal basis
        
        node = maths.normal_basis()
        tree.input_node.plug_to(node)
        
        u0 = node.v4_0
        u1 = node.v4_1
        u2 = node.v4_2
        
        error = node.error
        
        # ----- Test the 4 basis vectors
        
        if True:
            
            pts = tree.points(4)
            pts.POINT[0].store_named_float_color("u", (1., 0., 0., 0.))
            pts.POINT[1].store_named_float_color("u", (0., 1., 0., 0.))
            pts.POINT[2].store_named_float_color("u", (0., 0., 1., 0.))
            pts.POINT[3].store_named_float_color("u", (0., 0., 0., 1.))
            
            with tree.repeat(u3=tree.rgb(0., 0., 0., 0.), n3=tree.float(0), index=0, iterations=4) as rep:

                u = pts.sample_index_color(pts.named_color("u"), index=rep.index)
                rep.index += 1
                
                d0 = u0.dot(u)
                d1 = u1.dot(u)
                d2 = u2.dot(u)
                u -= d0*u0
                u -= d1*u1
                u -= d2*u2
                
                # Resulting norm
                
                n = u.length
                
                greater = n.greater_than(rep.n3)
                rep.u3 = rep.u3.switch(greater, u)
                rep.n3 = rep.n3.switch(greater, n)
                
            u3 = rep.u3
            
        
        else:
            n3 = tree.float(0)
            u3 = tree.rgb(0., 0., 0., 0.)
            for i in range(4):
                
                with tree.layout(f"Axis {i}"):
                    
                    v4 = [0] * 4
                    v4[i] = 1
                    
                    u = tree.rgb(*v4)
                    
                    d0 = u0.dot(u)
                    d1 = u1.dot(u)
                    d2 = u2.dot(u)
                    u -= d0*u0
                    u -= d1*u1
                    u -= d2*u2
                    
                    # Resulting norm
                    
                    n = u.length
                    
                    greater = n.greater_than(n3)
                    u3 = u3.switch(greater, u)
                    n3 = n3.switch(greater, n)
            
        # ----- Let's normalize the result
        
        u3 = u3.normalized()

        u3.to_output("V4")
        error.to_output("Error")

            
    # ----------------------------------------------------------------------------------------------------
    # Get two vectors forming a basis for a plane
    #
    # BUGGED

    def plane_basis():
        
        with GeoNodes("Plane basis", is_group=True, fake_user=True, prefix=maths) as tree:
            
            u0 = tree.vector_input("xyz 0", (1, 0, 0))
            w0 = tree.float_input( "w 0")
            u1 = tree.vector_input("xyz 1", (0, 1, 0))
            w1 = tree.float_input( "w 1")
            
            # ----- Let's try (0, 0, 1, 0) as third vector to form an hyperplane

            basis0 = maths.normal_basis(
                xyz_0 = u0,
                w_0   = w0,
                xyz_1 = u1,
                w_1   = w1,
                xyz_2 = (0, 0, 1),
                w_2   = 0)
            
            # ----- Let's try (0, 0, 0, 1) as third vector to form an hyperplane

            basis1 = maths.normal_basis(
                xyz_0 = u0,
                w_0   = w0,
                xyz_1 = u1,
                w_1   = w1,
                xyz_2 = (0, 0, 0),
                w_2   = 1)
                
            # ----- Return basis0 or basis1 depending upon the error
            
            basis0.xyz_0.switch(basis0.error, basis1.xyz_0).to_output("xyz 0")
            basis0.w_0.switch(  basis0.error, basis1.w_0  ).to_output("w 0")
            basis0.xyz_1.switch(basis0.error, basis1.xyz_1).to_output("xyz 1")
            basis0.w_1.switch(  basis0.error, basis1.w_1  ).to_output("w 1")
            
    # ----------------------------------------------------------------------------------------------------
    # Get three vectors perpendicular to a vector

    def hyperplane():
        
        with GeoNodes("Hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
            
            v = tree.vector_input("xyz")
            w = tree.float_input("w", 1.)
            
            # ----- Normalize the entry
            
            node = maths.normalize(xyz=v, w=w)
            v    = node.xyz
            w    = node.w
            
            # ----- Try to build a 3D-base with v and plane (k, l)
            
            node = maths.normal_basis(
                xyz_0 = v,
                w_0   = w,
                xyz_1 = (0, 0, 1),
                w_1   = 0,
                xyz_2 = (0, 0, 0),
                w_2   = 1)
                
            u0 = node.xyz_1
            w0 = node.w_1
            u1 = node.xyz_2
            w1 = node.w_2
            
            error = node.error
            
            # ---------------------------------------------------------------------------
            # If error, it does mean that v is in plane (k, l), hence (i, j) is perp to v
            
            node = maths.cross(
                xyz_0 = v,
                w_0   = w,
                xyz_1 = (1, 0, 0),
                w_1   = 0,
                xyz_2 = (0, 1, 0),
                w_2   = 0,
                )
                
            e_u2 = node.xyz
            e_w2 = node.w
            
            # ---------------------------------------------------------------------------
            # If no error, we have (u0, u1) perp to input vector
            # The third basis vector is perpendicular to these 3 vectors
            
            node = maths.cross(
                xyz_0 = v,
                w_0   = w,
                xyz_1 = u0,
                w_1   = w0,
                xyz_2 = u1,
                w_2   = w1,
                )

            u0 = u0.switch(error, (1, 0, 0))
            w0 = w0.switch(error, 0)
            u1 = u1.switch(error, (0, 1, 0))
            w1 = w1.switch(error, 0)
            u2 = node.xyz.switch(error, e_u2)
            w2 = node.w.switch(error, e_w2)
            
            # ----- Done
            
            u0.to_output("xyz 0")
            w0.to_output("w 0")

            u1.to_output("xyz 1")
            w1.to_output("w 1")
                
            u2.to_output("xyz 2")
            w2.to_output("w 2")
            
            v.to_output("xyz 3")
            w.to_output("w 3")
            
            
    # ----------------------------------------------------------------------------------------------------
    # Resolution system de deux équations à deux inconnues
    # a0x + b0y = c0
    # a1x + b1y = c1
    #
    # D = a0b1 - a1b0
    # x = (b1c0 - b0c1)/D
    # y = (a0c1 - a1c0)/D

    def two_equations_solver():
        with GeoNodes("Two equations solver", is_group=True, prefix=maths) as tree:
            
            a0 = tree.float_input("a0")
            b0 = tree.float_input("b0")
            c0 = tree.float_input("c0")

            a1 = tree.float_input("a1")
            b1 = tree.float_input("b1")
            c1 = tree.float_input("c1")
            
            with tree.layout("Discriminant"):
             D = a0*b1 - a1*b0
             
            with tree.layout("x"):
                x = (b1*c0 - b0*c1)/D 
                x.to_output("x")
                
            with tree.layout("y"):
                y = (a0*c1 - b1*c0)/D 
                y.to_output("y")
            
            tree.abs(D).less_than(0.001).to_output("Error")
            tree.vector((x, y, 0)).length().to_output("Length")
        
# ----------------------------------------------------------------------------------------------------
# Rotate to an hyperplane 

def rotate_to_hyperplane():
    
    with GeoNodes("Rotate to hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:

        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        hv = tree.vector_input("Hyper xyz")
        hw = tree.float_input("Hyper w", 1)
        
        node = maths.hyperplane(xyz=hv, w=hw)
        
        x = node.xyz_0.dot(v) + node.w_0*w
        y = node.xyz_1.dot(v) + node.w_1*w
        z = node.xyz_2.dot(v) + node.w_2*w
        w = node.xyz_3.dot(v) + node.w_3*w
        
        tree.vector((x, y, z)).to_output("xyz")
        w.to_output("w")
        
# ----------------------------------------------------------------------------------------------------
# Rotate from an hyperplane 

def rotate_from_hyperplane():
    
    with GeoNodes("Rotate from hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        hv = tree.vector_input("Hyper xyz")
        hw = tree.float_input("Hyper w", 1)
        
        node = maths.hyperplane(xyz=hv, w=hw)
        
        rv = node.xyz_0*v.x + node.xyz_1*v.y + node.xyz_2*v.z + node.xyz_3*w
        rw = node.w_0*v.x   + node.w_1*v.y   + node.w_2*v.z   + node.w_3*w

        rv.to_output("xyz")
        rw.to_output("w")
        
        
# ----------------------------------------------------------------------------------------------------
# Rotation 3D in an hyperplane

def rotate_in_hyperplane():
    
    with GeoNodes("Rotate in hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        hv = tree.vector_input("Hyper xyz")
        hw = tree.float_input("Hyper w", 1)

        #euler = gn.Vector.Rotation((0, 0, 0), "Euler")
        euler = tree.rotation_input("Euler")
        axis  = tree.vector_input(  "Axis", (0, 0, 1))
        angle = tree.angle_input(   "Angle")
        
        to_hp = maths.rotate_to_hyperplane(
            xyz       = v,
            w         = w,
            hyper_xyz = hv,
            hyper_w   = hw,
        )
        
        v = to_hp.xyz
        w = to_hp.w
        
        v = v.vector_rotate(rotation=euler, rotation_type='EULER_XYZ')
        v = v.vector_rotate(axis=axis, angle=angle, rotation_type='AXIS_ANGLE')
        
        from_hp = maths.rotate_from_hyperplane(
            xyz       = v,
            w         = w,
            hyper_xyz = hv,
            hyper_w   = hw,
        )
        
        from_hp.xyz.to_output("xyz")
        from_hp.w.to_output("w")
        
        
# ----------------------------------------------------------------------------------------------------
# Follow a vector
#
# Rotate a vector such as the vector a rotates to vector b

def follow_vector():
    
    with GeoNodes("Follow vector", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")

        va = tree.vector_input("A xyz")
        wa = tree.float_input( "A w", 1)
        vb = tree.vector_input("B xyz")
        wb = tree.float_input( "B w", 1)
        
        # ----- Create a normalized basis in the plane (a, b)
        
        with tree.layout("e0 = Basis first vector aligned on A"):
            
            node = maths.length(xyz=va, w=wa)

            xa   = node.length
            null = node.null

            e0 = va / xa
            t0 = wa / xa
            
        with tree.layout("e1 = Basis second vector: B - (B.e0).e0"):
            
            xb = e0.dot(vb) + t0*wb
            e1 = vb - e0*xb
            t1 = wb - t0*xb
            
            node = maths.length(xyz=e1, w=t1)
            yb   = node.length

            null = null + node.null
            e1 /= yb
            t1 /= yb
            
            # If vector are colinear, they can be opposite
            
            opposite = xb.less_than(0) 
            
        # ----- Compute the angle, cosine and sine
        
        with tree.layout("Compute the rotation cosine and sine"):
        
            ag = tree.arctan2(yb, xb)
            ag.node.node_label = "Rotation angle"
            ca = tree.cos(ag)
            sa = tree.sin(ag)
            
        # ----- Component of v on (e0, e1)
        
        with tree.layout("Components (xv, yv) on (e0, e1)"):
        
            xv = e0.dot(v) + t0*w
            yv = e1.dot(v) + t1*w
            
            xv.node.node_label = "xv"
            yv.node.node_label = "yv"
            
        # ----- Part out of the rotation plane
        
        with tree.layout("Part out of the rotation plane"):
            
            v3 = v - xv*e0 - yv*e1
            w3 = w - xv*t0 - yv*t1
            
        # ----- Rotate in the plane

        with tree.layout("Rotated coordinates"):
            
            fac0 = xv*ca - yv*sa
            fac1 = xv*sa + yv*ca
            
        # ----- Build the rotated vector

        with tree.layout("Build the resulting vector"):
            
            rv = v3 + fac0*e0 + fac1*e1
            rw = w3 + fac0*t0 + fac1*t1
            
        with tree.layout("No rotation if null"):
            
            #print(" V", v)
            #print("-V", -v)
            
            #print("SWITCH", v.switch(opposite, -v))
            #print("BEF", v)
            #v = v.switch(opposite, -v)
            #print("AFT", v)
            
            print("BEF", rv)
            rv = rv.switch(null, v.switch(opposite, -v))
            rw = rw.switch(null, w.switch(opposite, -w))
            print("AFT", rv)
            
        rv.to_output("xyz")
        rw.to_output("w")
        

# ----------------------------------------------------------------------------------------------------
# Rotation in a plane (x|y|z, w)
        
def w_plane_rotation():
    
    with GeoNodes("W plane rotation", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.vector_input("xyz")
        w = tree.float_input("w")
        
        axis  = tree.integer_input("Axis", 0, min_value=0, max_value=2)
        angle = tree.angle_input(  "Angle")
        
        # w is mapped on x
        # select y based on axis value
        
        with tree.layout("Axis on y component"):
            
            y = v.y.switch(axis.equal(0), v.x).switch(axis.equal(2), v.z)
            
        with tree.layout("Rotation around z"): 
        
            # rotation around z axis
            
            #r = gn.Vector((w, y, 0)).rotate_axis_angle(axis=(0, 0, 1), angle=angle)
            r = tree.vector((w, y, 0)).vector_rotate(axis=(0, 0, 1), angle=angle, rotation_type='AXIS_ANGLE')
            
        with tree.layout("y result on axis, x result on w"):
            
            # Returns the result
            
            tree.vector((v.x.switch(axis.equal(0), r.y),
                         v.y.switch(axis.equal(1), r.y),
                         v.z.switch(axis.equal(2), r.y)) ).to_output("xyz")
                       
            r.x.to_output("w")
            
# ----------------------------------------------------------------------------------------------------
# Utility Rotation in a plane defined by two 4D vectors
        
def rotation_2D():
    
    with GeoNodes("Rotation 2D", is_group=True, fake_user=True, prefix=maths) as tree:

        v  = tree.vector_input("xyz")
        w  = tree.float_input( "w")
        
        v0 = tree.vector_input("xyz 0")
        w0 = tree.float_input( "w 0", 1)
        v1 = tree.vector_input("xyz 1", (1, 0, 0))
        w1 = tree.float_input( "w 1")
        a  = tree.angle_input( "Angle", description="Rotation angle in plane (V0, V1)")
        
        with tree.layout("Normalize vector 0"):

            n = tree.sqrt(v0.x*v0.x + v0.y*v0.y + v0.z*v0.z + w0*w0)
            v0 = v0/n
            w0 = w0/n
            
        with tree.layout("Build second vector orthogonally"):
            
            d = v0.dot(v1) + w0*w1
            
            v1 = v1 - v0*d
            w1 = w1 - w0*d
            
        with tree.layout("Normalize second vector"):
            
            n = tree.sqrt(v1.x*v1.x + v1.y*v1.y + v1.z*v1.z + w1*w1)
            v1 = v1/n
            w1 = w1/n
            
        with tree.layout("Rotation V0 towards V1"):
            
            # ----- Components in plane (V0, V1)
            
            x = v0.dot(v) + w0*w
            y = v1.dot(v) + w1*w
            
            # ----- Rotation

            c = tree.cos(a) - 1
            s = tree.sin(a)

            # ----- Rotated components
            
            xp =  c*x - s*y
            yp =  s*x + c*y
            
            # ----- Resulting vector
            # V = V - P01 components + P01 rotated components
            
            rv = v + xp*v0 + yp*v1
            rw = w + xp*w0 + yp*w1
            
        rv.to_output("xyz")
        rw.to_output("w")
        
# ----------------------------------------------------------------------------------------------------
# Mesh along a curve
        
def build_along_curve():
    
    with GeoNodes("Build along curve", is_group=True, fake_user=True, prefix=maths) as tree:
        
        geo        = tree.geometry_input("Geometry 4D")
        curve      = tree.geometry_input("Curve 4D")
        align_v    = tree.vector_input(  "Align xyz", (0, 0, 1))
        align_w    = tree.float_input(   "Align w")
        use_radius = tree.bool_input(    "Use Radius", False)
        
        # Instantiate along the curve
        
        instances = curve.instance_on_points(instance=geo)
        
        # Instances 4D coordinates
        
        with tree.layout("Instances curve w coordinate"):
            
            w  = curve.POINT.sample_index_float(value=tree.named_float("w"))
            instances.INSTANCE.store_named_float("curve w", w)
            
            # ----- Scale with radius
            
            scale = tree.float(1).switch(use_radius, curve.POINT.sample_index_float(curve.radius))
            instances.scale_instances(scale=scale)
            
        with tree.layout("Store curve tangent and point location for further rotation"):
            
            instances.INSTANCE.store_named_vector("pivot xyz", instances.position)
            instances.INSTANCE.store_named_float( "pivot w", w)
            
            Txyz = curve.POINT.sample_index_vector(value=tree.named_vector("Txyz"))
            Tw   = curve.POINT.sample_index_float(value=tree.named_float("Tw"))

            instances.INSTANCE.store_named_vector("curve Txyz", Txyz)
            instances.INSTANCE.store_named_float( "curve Tw", Tw)
            
        # ----- Realize instances
            
        geo = instances.realize_instances()
        
        with tree.layout("Set the vertices in 4D space"):
            
            # ----- w coordinate
        
            geo.POINT.store_named_float("w", tree.named_float("w") + tree.named_float("curve w"))
            geo.remove_named_attribute("curve w")
            
            # ----- Rotation
            
            v = geo.position
            w = tree.named_float("w")
            
            pv = tree.named_vector("pivot xyz")
            pw = tree.named_float("pivot w")
            
            rv = tree.named_vector("curve Txyz")
            rw = tree.named_float("curve Tw")
            
            # ----- Points location
            
            with tree.layout("Points location"):
            
                node = maths.follow_vector(
                    xyz   = v - pv,
                    w     = w - pw,
                    a_xyz = align_v,
                    a_w   = align_w,
                    b_xyz = rv,
                    b_w   = rw,
                    )
                    
                geo.POINT.position = pv + node.xyz
                geo.POINT.store_named_float("w", pw + node.w)
                
            comps = geo.separate_components()
                
            mesh  = comps.mesh
            curve = comps.curve
            cloud = comps.point_cloud
            inst  = comps.instances
            
            # ----- Normals
            
            with tree.layout("Normals"):
            
                node = maths.follow_vector(
                    xyz   = tree.named_vector("Nxyz"),
                    w     = tree.named_float("Nw"),
                    a_xyz = align_v,
                    a_w   = align_w,
                    b_xyz = rv,
                    b_w   = rw,
                    )
                    
                mesh.POINT.store_named_vector("Nxyz", node.xyz)
                mesh.POINT.store_named_float( "Nw",   node.w)
                
            # ----- Curves tangents
            
            with tree.layout("Curves tangents"):
            
                node = maths.follow_vector(
                    xyz   = tree.named_vector("Txyz"),
                    w     = tree.named_float("Tw"),
                    a_xyz = align_v,
                    a_w   = align_w,
                    b_xyz = rv,
                    b_w   = rw,
                    )
                    
                curve.POINT.store_named_vector("Txyz", node.xyz)
                curve.POINT.store_named_float( "Tw",   node.w)
                
            # ----- Remove the named attributes
            
            geo.remove_named_attribute("pivot xyz")
            geo.remove_named_attribute("pivot w")
            geo.remove_named_attribute("curve Txyz")
            geo.remove_named_attribute("curve Tw")
        
        (mesh + curve + cloud + inst).to_output("Geometry")
       

# ====================================================================================================
# Main

def debug():        
    def vis_proj_mat():
        
        with GeoNodes("Debug PROJ") as tree:
            m = maths.projection_matrix()
            
            #m = maths.yw_rotation(angle=0, second=1)
            
            vals = [
                [m.row_0.red, m.row_0.green, m.row_0.blue, m.row_0.alpha],
                [m.row_1.red, m.row_1.green, m.row_1.blue, m.row_1.alpha],
                [m.row_2.red, m.row_2.green, m.row_2.blue, m.row_2.alpha],
                [m.row_3.red, m.row_3.green, m.row_3.blue, m.row_3.alpha],
                ]
                
            geo = None
                
            for i in range(4):
                for j in range(4):
                    x = (i+1)*3
                    y = (4-j)*3
                    s = vals[i][j].value_to_string(decimals=3).string_to_curves().curve_instances
                    s.transform_geometry(translation=(x, y, 0))
                    geo = s + geo
                    
            tree.og = geo
    

if CLEAR:
    maths.clear()        
  
if REBUILD:
    
    tree_matrices()
    
    axis_rotations()        
    
    projection_matrix()
    projection()
    length()
    normalize()
    normal_basis()
    cross()
    hyperplane()
    
    two_equations_solver()
    plane_basis()    

    rotate_to_hyperplane()
    rotate_from_hyperplane()
    rotate_in_hyperplane()
    follow_vector()
    
    w_plane_rotation()
    rotation_2D()
    
    build_along_curve()
    
        
    
    
    

        


        

