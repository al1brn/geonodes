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

utils     = GeoNodes.prefixed("U")
maths     = GeoNodes.prefixed("M")
modifiers = GeoNodes.prefixed("4D")
curves    = GeoNodes.prefixed("C")
surfaces  = GeoNodes.prefixed("S")

ZERO = 0.0001
N4A  = "N4a"
N4B  = "N4B"
T4   = "T4"


def clear_all():
    utils.clear()
    maths.clear()
    modifiers.clear()
    curves.clear()
    surfaces.clear()
    
def rebuild():
    
    build_shaders()
    
    utilities()
    g_matrices()
    m_base()
    g_vectors()
    transformations()
    lights()
    m_curves()
    

# ====================================================================================================
# Shaders

def build_shaders():

    # ----------------------------------------------------------------------------------------------------
    # Axis Shader
    
    with Shader("4 Axis") as tree:
        
        col = tree.Attribute(attribute_name="Axis Color").color
        
        ped = tree.PrincipledBSDF(base_color = col, roughness=.1, metallic=.3)
        
        tree.output_surface = ped.bsdf
        
    # ----------------------------------------------------------------------------------------------------
    # Surface Group
    # Reading 4D attributes
    
    with Shader("4D Surface", is_group=True) as tree:
        
        front = tree.color_input("Base Color")
        base  = tree.color_input("Base Color")
        
        intensity = tree.Attribute("L4 Intensity").fac
        color     = tree.Attribute("L4 Color").vector
        if True:
            #da = tree.Attribute("dot_a").fac
            #db = tree.Attribute("dot_b").fac
            #back = da.less_than(0) + db.less_than(0)
            #color = color.mix(back, (0., 1., 0.))
            back  = tree.Attribute("Back").fac
            
        else:
            back      = tree.Attribute("L4 Back").fac
        
        col = base.mix(intensity, color)
        
        col.to_output("Color")
        back.to_output("Back")
    


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
# Utility nodes to make trees clearer

def utilities():
    
    with GeoNodes("Dot", is_group=True, prefix=utils) as tree:
        u = tree.color_input("A")
        v = tree.color_input("B")
        u.dot(v).to_output("Value")

    with GeoNodes("Add", is_group=True, prefix=utils) as tree:
        u = tree.color_input("A")
        v = tree.color_input("B")
        (u + v).to_output("V")
        
    with GeoNodes("Sub", is_group=True, prefix=utils) as tree:
        u = tree.color_input("A")
        v = tree.color_input("B")
        (u - v).to_output("V")
        
    with GeoNodes("Scale", is_group=True, prefix=utils) as tree:
        s = tree.float_input("Scale")
        v = tree.color_input("V")
        (s*v).to_output("V")
        
    with GeoNodes("To XYZ W", is_group=True, prefix=utils) as tree:
        v = tree.color_input("V")
        xyz, w = v.xyz_w
        xyz.to_output("xyz")
        w.to_output("w")
        
    with GeoNodes("From XYZ W", is_group=True, prefix=utils) as tree:
        xyz = tree.vector_input("xyz")
        w   = tree.float_input("w")
        tree.rgb_a(xyz, w).to_output("V")
        
    with GeoNodes("Length", is_group=True, prefix=utils) as tree:
        v = tree.color_input("V")
        n = v.length
        n.to_output("Length")
        n.less_than(ZERO).to_output("Null")

    with GeoNodes("Normalize", is_group=True, prefix=utils) as tree:
        v = tree.color_input("V")
        u, e = v.normalized(ZERO)
        u.to_output("V")
        e.to_output("Error")
        
    with GeoNodes("Ortho Vector", is_group=True, prefix=utils) as tree:
        
        V = tree.color_input("V")
        U = tree.color_input("Direction")

        # Along U
        along = V.dot(U)*U
        
        # Perpendicular to U
        perp  = V - along
        
        # To output
        along.to_output("Along")
        perp.to_output("Perp")
        
        u, z = perp.normalized(ZERO)
        u.to_output("Unit")
        z.to_output("Null")
        
    with GeoNodes("Angle", is_group=True, prefix=utils) as tree:
        
        u = tree.color_input("U")
        v = tree.color_input("V")
        
        u = u.normalized()
        v = v.normalized()
        
        # Cosine
        ca = u.dot(v)
        
        # Sine
        sa = (v - ca*u).length
        
        # Angle
        angle = tree.arctan2(sa, ca)
        
        # To output
        angle.to_output("Angle")
        u.to_output("U")
        v.to_output("V")


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
    # GROUP - Ensure Projection and Projection2 objects exist
    
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
    # GROUP - XW / YZ rotations
    
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
    # GROUP - YW / ZX rotations
    
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
    # GROUP - ZW / XY rotations
    
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
    # GROUP - Projection matrix

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
    # GROUP - Perform a projection

    with GeoNodes("Projection", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.color_input("V")
        m = maths.projection_matrix()
        
        r = mat_dot(m, v)
        xyz, w = r.xyz_w
        
        xyz.to_output("Vector")
        w.to_output("w")
        

# ====================================================================================================
# Base modifiers
# Modifiers:
# - Plunge 3D Geometry
# - Arrow
# - Axis
# - Dot normal
# - Projection

def m_base():
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Add the 4D attributes

    with GeoNodes("Plunge 3D Geometry", fake_user=True, prefix=modifiers) as tree:
        
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
        
        mesh.FACE.store_named_float_color(N4A, tree.rgb_a(mesh.normal, 0.))
        mesh.FACE.store_named_float_color(N4B, tree.rgb(0., 0., 0., 1.))
        
        # ---- Curve tangents
        
        curve.POINT.store_named_float_color(T4, tree.rgb_a(curve.curve_tangent, 0.))
            
        # ---- Result
        
        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Arrow

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

            p0 = maths.projection(v=u0).vector
            p1 = maths.projection(v=u1).vector
            
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
    # MODIFIER - The four Axis            
            
    with GeoNodes("Axis Viewer", fake_user=True, prefix=modifiers) as tree:
        
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
    # MODIFIER - Perform a projection

    with GeoNodes("Projection", fake_user=True, prefix=modifiers) as tree:
        
        geo          = tree.ig
        shade_smooth = tree.bool_input("Shade smooth", True)
        
        # ===== Points projection
        
        with tree.layout("All points projection"):
            
            v = tree.rgb_a(geo.position, geo.named_float("w"))
            geo.POINT.position = maths.projection(v=v).vector
            
        # ===== Components
        
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh projection"):

            proj_dir = maths.projection_matrix().m_3
            
            back = tree.boolean(True)
            
            with tree.layout("Normals"):
                for N, N_, d in zip([N4A, N4B], ["Na", "Nb"], ["dot_a", "dot_b"]):
                    n4 = mesh.named_color(N4A)
                    n   = maths.projection(v=n4).vector
                    mesh.FACE.store_named_vector(N_, n)
                    dot = proj_dir.dot(n4)
                    mesh.FACE.store_named_float(d, dot)
                    
                    back *= dot.less_than(0)
                    
                mesh.FACE.store_named_float("Back", back)
                
            mesh.FACE.shade_smooth = shade_smooth
            
        # ----- Curve
            
        with tree.layout("Curve projection"):
            
            with tree.layout("Tangents projection"):
                
                t  = maths.projection(v=mesh.named_color("T4")).vector
                
                curve.POINT.store_named_vector("T", t)
                
        tree.og = tree.join_geometry(mesh, curve, cloud, inst)
        
        
# =============================================================================================================================
# Vectors groups
# - Normalize basis
# - Cross product between 3 vectors
# - Plane basis
# - Hyperplane
# - Two equations solver 
        
def g_vectors():
    
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Normalize two vectors forming a plane

    with GeoNodes("Normalize 2-Basis", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.color_input("I")
        u1 = tree.color_input("J")
        
        # ----- We suppress from u1 the u0 component
        
        if True:
            u0 = utils.normalize(u0).v
            u0.to_output("I")
            utils.ortho_vector(v=u1, direction=u0).unit.to_output("J")
            
        else:
            u1 -= (u1.dot(u0))*u0
        
            # Normalized
            
            utils.normalize(u0).v.to_output("I")
            utils.normalize(u1).v.to_output("J")
            
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Normal basis
    # 3 vectors forming a normal basis to a 3D hyperplane defined by three independant vectors

    with GeoNodes("Normalize 3-Basis", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.color_input("I", (1., 0., 0., 0.))
        u1 = tree.color_input("J", (0., 1., 0., 0.))
        u2 = tree.color_input("K", (0., 0., 1., 0.))
        
        
        if True:

            # ----- I = normalized first vector
            
            node = utils.normalize(u0)
            I, err = node.v, node.error
            
            # ----- J = perpendicular component of second vector relatively to I
            
            node = utils.ortho_vector(v=u1, direction=I)
            J = node.unit
            err += node.null
            
            # ----- K = perpendicular to I and J
            
            node = utils.ortho_vector(utils.ortho_vector(u2, I).perp, J)
            K = node.unit
            err += node.null
            
            # ----- We are done :-)
            
            I.to_output("I")
            J.to_output("J")
            K.to_output("K")
            
            err.to_output("Error")
            
        
        else:
        
            # ----- Let's normalize the first input
            
            node = utils.normalize(u0)
            e0, err = node.v, node.error
                
            # Let's suppress this dimension in the second one
            
            with tree.layout("Make the second vector perp to the first"):
    
                # d = e0.u1            
                d = utils.dot(e0, u1).value
                # u1 = u1 - d*e0
                u1 = utils.sub(u1, utils.scale(d, e0).v).v       
                
                # ----- Let's normalize
                
                node = utils.normalize(u1)
                e1 = node.v
                err += node.error
                
            with tree.layout("Make the third vector perp to the two other ones"):
            
                # ----- (u0, u1) are two basis vectors
                # Let's suppress these dimensions in the third one
    
                #d = e0.u2
                d = utils.dot(e0, u2)
                #u2 = u2 - d*e0
                u2 = utils.sub(u2, utils.scale(d, e0))
                
                #d = e1.u2
                d = utils.dot(e1, u2)
                #u2 = u2 - d*e1
                u2 = utils.sub(u2, utils.scale(d, e1))
                
                # ----- Let's normalize
                
                node = utils.normalize(u2)
                e2 = node.v
                err += node.error
                
            # ----- We are done :-)
            
            e0.to_output("I")
            e1.to_output("J")
            e2.to_output("K")
            
            err.to_output("Error")
                
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Cross
    # A vector peprpendicular to three independant vectors

    with GeoNodes("Cross", is_group=True, fake_user=True, prefix=maths) as tree:
        
        u0 = tree.color_input("I") #, (1., 0., 0., 0.))
        u1 = tree.color_input("J") #, (0., 1., 0., 0.))
        u2 = tree.color_input("K") #, (0., 0., 1., 0.))
        
        # ----- Convert the three input vectors in a normal basis
        
        node = maths.normalize_3_basis()
        tree.input_node.plug_to(node)
        
        u0 = node.i
        u1 = node.j
        u2 = node.k
        
        error = node.error
        
        # ----- Test the 4 basis vectors
        
        if True:
            
            pts = tree.points(4)
            pts.POINT[0].store_named_float_color("u", (1., 0., 0., 0.))
            pts.POINT[1].store_named_float_color("u", (0., 1., 0., 0.))
            pts.POINT[2].store_named_float_color("u", (0., 0., 1., 0.))
            pts.POINT[3].store_named_float_color("u", (0., 0., 0., 1.))
            
            with tree.repeat(u3=tree.rgb(0., 0., 0., 0.), n3=tree.float(0), index=0, iterations=4) as rep:
                
                # ----- Pick in I, J, K, L

                u = pts.sample_index_color(pts.named_color("u"), index=rep.index)
                rep.index += 1
                
                if True:
                    u = utils.ortho_vector(utils.ortho_vector(utils.ortho_vector(u, u0).perp, u1).perp, u0).perp
                
                else:
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

        u3.to_output("V")
        error.to_output("Error")
            
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Compute three vectors perpendicular to a vector

    with GeoNodes("Hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.color_input("V")
        
        # ----- Normalize the entry
        
        v = v.normalized()
        
        # ----- Try to build a 3D-base with v and plane (k, l)
        
        node = maths.normalize_3_basis(i=v, j=(0., 0., 1., 0.), k=(0., 0., 0., 1.))
            
        u0 = node.j
        u1 = node.k
        
        error = node.error
        
        # ---------------------------------------------------------------------------
        # If error, it does mean that v is in plane (k, l), hence (i, j) is perp to v
        
        node = maths.cross(i=v, j=(1., 0., 0., 0.), k=(0., 1., 0., 0.))
            
        e_u2 = node.v
        
        # ---------------------------------------------------------------------------
        # If no error, we have (u0, u1) perp to input vector
        # The third basis vector is perpendicular to these 3 vectors
        
        node = maths.cross(i=v, j= u0, k=u1)

        u0 = u0.switch(error, (1., 0., 0., 0.))
        u1 = u1.switch(error, (0., 1., 0., 0.))
        u2 = node.v.switch(error, e_u2)
        
        # ----- Done
        
        u0.to_output("I")
        u1.to_output("J")
        u2.to_output("K")
        v.to_output("L")
            
            
    # ----------------------------------------------------------------------------------------------------
    # Resolution system de deux équations à deux inconnues
    # a0x + b0y = c0
    # a1x + b1y = c1
    #
    # D = a0b1 - a1b0
    # x = (b1c0 - b0c1)/D
    # y = (a0c1 - a1c0)/D

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
        
# =============================================================================================================================
# Transformations
# - Translation
# - Scale
# - Rotation 4D
# - Rotation 2D
# - Align Vector
        
def transformations():
    
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Translation
        
    with GeoNodes("Translation", fake_user=True, prefix=modifiers) as tree:
        
        geo = tree.ig
        
        xyz = tree.vector_input("xyz")
        w   = tree.float_input("w")
        
        geo.transform_geometry(translation=xyz)
        geo.POINT.store_named_float("w", geo.named_float("w") + w)
        
        tree.og = geo
    
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Scale
        
    with GeoNodes("Scale", fake_user=True, prefix=modifiers) as tree:
        
        geo = tree.ig
        
        xyz = tree.vector_input("xyz", (1., 1., 1.))
        w   = tree.float_input("w", 1.)
        
        geo.transform_geometry(scale=xyz)
        geo.POINT.store_named_float("w", geo.named_float("w") * w)
        
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances

        scale = tree.rgb_a(xyz, w)
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            for N in [N4A, N4B]:
                mesh.FACE.store_named_float_color(N, utils.normalize(
                    scale * mesh.named_color(N)).v)
            
        # ----- Curve
        
        with tree.layout("Curve"):

            curve.POINT.store_named_float_color(T4, utils.normalize(
                scale * mesh.named_color(T4)).v)

        tree.og = mesh + curve + cloud + inst        
    
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation 4D
        
    with GeoNodes("Rotation 4D", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.color_input("V")
        
        xy = tree.angle_input("XY", description="Rotation in the plane XY")
        zw = tree.angle_input("ZW", description="Rotation in the plane ZW")

        xz = tree.angle_input("XZ", description="Rotation in the plane XZ")
        yw = tree.angle_input("YW", description="Rotation in the plane YW")
        
        xw = tree.angle_input("XW", description="Rotation in the plane XW")
        yz = tree.angle_input("YZ", description="Rotation in the plane YZ")
        
        # ----- Rotation xy / zw
        
        ca, sa = tree.cos(xy), tree.sin(xy)
        cb, sb = tree.cos(zw), tree.sin(zw)
        A0 = tree.rgb( ca, -sa,  0.,  0.)
        A1 = tree.rgb( sa,  ca,  0.,  0.)
        A2 = tree.rgb( 0.,  0.,  cb, -sb)
        A3 = tree.rgb( 0.,  0.,  sb,  cb)
        
        # ----- Rotation xz / yw
        
        ca, sa = tree.cos(xz), tree.sin(xz)
        cb, sb = tree.cos(yw), tree.sin(yw)
        B0 = tree.rgb( ca,  0.,  sa,  0.)
        B1 = tree.rgb( 0.,  cb,  0.,  sb)
        B2 = tree.rgb(-sa,  0.,  ca,  0.)
        B3 = tree.rgb( 0., -sb,  0.,  cb)
        
        # ----- Rotation xw / yz
        
        ca, sa = tree.cos(xw), tree.sin(xw)
        cb, sb = tree.cos(yz), tree.sin(yz)
        C0 = tree.rgb( ca,  0.,  0., -sa)
        C1 = tree.rgb( 0.,  cb, -sb,  0.)
        C2 = tree.rgb( 0.,  sb, cb,  0.)
        C3 = tree.rgb( sa,  0.,  0.,  ca)
        
        # ----- Multiply the matrices
        
        node = maths.mat_mult(A0, A1, A2, A3, B0, B1, B2, B3)
        M0, M1, M2, M3 = node.m_0, node.m_1, node.m_2, node.m_3
        
        M = maths.mat_mult(M0, M1, M2, M3, C0, C1, C2, C3)

        # ----- Rotate the vector
        
        mat_dot(M, v).to_output("V")
        
    # ----------------------------------------------------------------------------------------------------
    # Modifier - Rotation 4D
        
    with GeoNodes("Rotation 4D", fake_user=True, prefix=modifiers) as tree:
        
        geo = tree.ig
        
        xy = tree.angle_input("XY", description="Rotation in the plane XY")
        zw = tree.angle_input("ZW", description="Rotation in the plane ZW")

        xz = tree.angle_input("XZ", description="Rotation in the plane XZ")
        yw = tree.angle_input("YW", description="Rotation in the plane YW")
        
        xw = tree.angle_input("XW", description="Rotation in the plane XW")
        yz = tree.angle_input("YZ", description="Rotation in the plane YZ")
        
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            
            node = maths.rotation_4d(tree.rgb_a(geo.position, geo.named_float("w")))
            tree.input_node.plug_to(node)

            geo.position = node.v
            geo.POINT.store_named_float("w", node.v.w)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            for N in [N4A, N4B]:
                node = maths.rotation_4d(mesh.named_color(N))
                tree.input_node.plug_to(node)
                mesh.FACE.store_named_float_color(N, node.v)
            
        # ----- Curve
        
        with tree.layout("Curve"):

            node = maths.rotation_4d(curve.named_color(T4))
            tree.input_node.plug_to(node)
            
            curve.POINT.store_named_float_color(T4, node.v)

        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation in a plane defined by two 4D vectors
        
    with GeoNodes("Rotation 2D", is_group=True, fake_user=True, prefix=maths) as tree:

        v  = tree.color_input("V")
        
        I  = tree.color_input("I", description = "First vector of the plane basis")
        J  = tree.color_input("J", description = "Second vector of the plane basis")
        ag = tree.angle_input( "Angle", description="Rotation angle in plane (I, J)")
        
        # ---------------------------------------------------------------------------
        # Decompose the vector along I, J and remainder
        
        with tree.layout("Decompose I, J, Remainder"):
            x = utils.dot(I, v).value
            y = utils.dot(J, v).value
            v_ = utils.sub(v, utils.add(utils.scale(x, I).v, utils.scale(y, J).v).v).v
        
        # ---------------------------------------------------------------------------
        # Rotate x, y
        
        with tree.layout("Rotation 2D"):
        
            ca, sa = tree.cos(ag), tree.sin(ag)
            x_ = x*ca - y*sa
            y_ = x*sa + y*ca

        # ---------------------------------------------------------------------------
        # Recompose the vector
        
        with tree.layout("Recompose"):
            
            r = utils.add(utils.add(utils.scale(x_, I), utils.scale(y_, J)).v, v_).v
            
        r.to_output("V")
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Rotation in a plane defined by two 4D vectors
        
    with GeoNodes("Rotation 2D", fake_user=True, prefix=modifiers) as tree:

        geo = tree.ig
        
        xyz0 = tree.vector_input("xyz 0", (1., 0., 0.), description = "Vector 0")
        w0   = tree.float_input("w 0", 0., description = "w component 0")
        xyz1 = tree.vector_input("xyz 1", (0., 1., 0.), description = "Vector 1")
        w1   = tree.float_input("w 1", 0., description = "w component 1")
        ag   = tree.angle_input( "Angle", description="Rotation angle in plane (I, J)")
        
        # ===== Normal 2-Basis
        
        with tree.layout("Normal 2-Basis"):
        
            I = tree.rgb_a(xyz0, w0)
            J = tree.rgb_a(xyz1, w1)
            
            node = maths.normalize_2_basis(I, J)
            I, J = node.i, node.j
            
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            node = maths.rotation_2d(tree.rgb_a(geo.position, geo.named_float("w")),
                                     i=I, j=J, angle=ag)

            geo.position = node.v
            geo.POINT.store_named_float("w", node.v.w)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            for N in [N4A, N4B]:
                node = maths.rotation_2d(mesh.named_color(N),
                                         i=I, j=J, angle=ag)
                mesh.FACE.store_named_float_color(N, node.v)
            
        # ----- Curve
        
        with tree.layout("Curve"):
            
            node = maths.rotation_2d(curve.named_color(T4),
                                     i=I, j=J, angle=ag)
            curve.POINT.store_named_float_color(T4, node.v)

        tree.og = mesh + curve + cloud + inst            
        
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Follow a vector
    #
    # Rotate a vector such as the vector A rotates to vector B

    with GeoNodes("Align Vector", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v = tree.color_input("V")

        va = tree.color_input("From Vector")
        vb = tree.color_input("To Vector")
        
        # ----- Angle between the two vectors
        
        ag = utils.angle(va, vb).angle
        
        # ----- Normalized basis
        
        node = maths.normalize_2_basis(va, vb)
        I, J = node.i, node.j
        
        # ----- Rotate in the plane I, J
        
        v = maths.rotation_2D(v, i=I, j=J, angle=ag).v
        v.to_output("V")
        
        
        

        if False:
            
            # ----- Create a normalized basis in the plane (a, b)
            
            with tree.layout("e0 = Basis first vector aligned on A"):
                
                #node = maths.length(xyz=va, w=wa)
    
                xa   = va.length
                null = xa.less_than(ZERO)
    
                e0 = va / xa
                
            with tree.layout("e1 = Basis second vector: B - (B.e0).e0"):
                
                
                xb = e0.dot(vb)
                e1 = vb - xb*e0
                
                yb = e1.length
                null = null + yb.less_than(ZERO)
                
                e1 /= yb
                
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
            
                xv = e0.dot(v)
                yv = e1.dot(v)
                
                xv.node.node_label = "xv"
                yv.node.node_label = "yv"
                
            # ----- Part out of the rotation plane
            
            with tree.layout("Part out of the rotation plane"):
                
                v3 = v - xv*e0 - yv*e1
                
            # ----- Rotate in the plane
    
            with tree.layout("Rotated coordinates"):
                
                fac0 = xv*ca - yv*sa
                fac1 = xv*sa + yv*ca
                
            # ----- Build the rotated vector
    
            with tree.layout("Build the resulting vector"):
                
                rv = v3 + fac0*e0 + fac1*e1
                
            with tree.layout("No rotation if null"):
                
                rv = rv.switch(null, v.switch(opposite, -v))
                
            rv.to_output("V")
            
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Follow a vector
    #
    # Rotate a vector such as the vector A rotates to vector B

    with GeoNodes("Align vector", fake_user=True, prefix=modifiers) as tree:

        geo = tree.ig

        xyz0 = tree.vector_input("From xyz")
        w0   = tree.float_input("From w")
        xyz1 = tree.vector_input("To xyz")
        w1   = tree.float_input("To w")
        
        From = tree.rgb_a(xyz0, w0)
        To   = tree.rgb_a(xyz1, w1)
        
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            
            node = maths.align_vector(tree.rgb_a(geo.position, geo.named_float("w")),
                                     from_vector=From, to_vector=To)

            geo.position = node.v
            geo.POINT.store_named_float("w", node.v.w)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            for N in [N4A, N4B]:
                node = maths.align_vector(mesh.named_color(N),
                                         from_vector=From, to_vector=To)
                mesh.FACE.store_named_float_color(N, node.v)
            
        # ----- Curve
        
        with tree.layout("Curve"):
            
            node = maths.align_vector(curve.named_color(T4),
                                     from_vector=From, to_vector=To)
            curve.POINT.store_named_float_color(T4, node.v)

        tree.og = mesh + curve + cloud + inst
        
        
# ====================================================================================================
# Lights
# - Point
# - Light emitter
# - Light capture

def lights():
    
    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as a 4-point
    
    with GeoNodes("Point", fake_user=True, prefix=modifiers) as tree:
        
        xyz     = tree.vector_input("xyz", 0., description="xyz component")
        w       = tree.float_input("w",   0., description="w component")
        radius  = tree.float_input("Radius", .1)
        visible = tree.bool_input( "Visible", True)
        mat     = tree.material_input("Material")
        
        point = tree.points(count=1)
        point_loc = tree.rgb_a(xyz, w)
        point.POINT.store_named_float_color("P4", point_loc)
        
        # ----- Point visualization
        
        sphere = tree.uv_sphere(radius=radius)
        sphere.shade_smooth = True
        sphere.material     = mat
        
        sphere.transform_geometry(translation=maths.projection(point_loc).vector)
        
        # ----- To output
        
        tree.og = point.switch(visible, point + sphere)
        
    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as light emitter

    with GeoNodes("Light Emitter", fake_user=True, prefix=modifiers) as tree:
        
        xyz       = tree.vector_input("xyz", 0., description="xyz component")
        w         = tree.float_input("w", 0., description="w component")
        color     = tree.color_input( "Color", (1., 1., 1., 1.))
        intensity = tree.float_input( "Intensity", 1., min_value = 0)
        radius    = tree.float_input("Radius", .1)
        visible   = tree.bool_input( "Visible", True)
        mat       = tree.material_input("Material")
        
        # ----- Is a 4 point
        
        geo = modifiers.point(xyz=xyz, w=w, radius=radius, visible=visible, material=mat).geometry
        
        comps = geo.separate_components()
        mesh  = comps.mesh
        cloud = comps.point_cloud
        
        cloud.POINT.store_named_float("Intensity", intensity)
        cloud.POINT.store_named_float_color("Color", color)
        
        tree.og = cloud + mesh
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Reflect on a surface given the two normals
    
    with GeoNodes("Surface reflection", is_group=True, prefix=maths) as tree:
        
        v  = tree.color_input("V")
        Na = tree.color_input(N4A)
        Nb = tree.color_input(N4B)
        
        # ---------------------------------------------------------------------------
        # Decompose the vector along the two normals and remainder
        
        with tree.layout("Decompose along the two normals and the remainder"):
            x = utils.dot(Na, v).value
            y = utils.dot(Nb, v).value
            v_ = utils.sub(v, utils.add(utils.scale(x, Na).v, utils.scale(y, Nb).v).v).v
            x_back = x.less_than(0)
            y_back = y.less_than(0)
        
        # ---------------------------------------------------------------------------
        # Recompose inverting the components along the normals
        
        with tree.layout("Recompose, inverting the components along the normals"):
            
            r = utils.add(utils.add(utils.scale(-x, Na), utils.scale(-y, Nb)).v, v_).v
            
        r.to_output("V")
        x_back.to_output("Back A")
        y_back.to_output("Back B")
        #(x_back * y_back).to_output("Back")
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Capture light from an emitter
    
    with GeoNodes("Light Capture", fake_user=True, prefix=modifiers) as tree:
        
        geo   = tree.ig
        light = tree.object_input("Light")
        focus = tree.float_input( "Focus", 1.)
        
        # ----------------------------------------------------------------------------------------------------
        # Read light information
        
        with tree.layout("Read light information"):
        
            info = light.object_info()
            
            #loc   = info.location
            cloud = info.geometry.separate_components().point_cloud
            
            #w         = cloud.POINT.sample_index_float(cloud.named_float("w"),         0)
            #light_loc = tree.rgb_a(loc, w)
            light_loc = cloud.POINT.sample_index_color(cloud.named_color("P4"),        0)
            color     = cloud.POINT.sample_index_color(cloud.named_color("Color"),     0)
            intensity = cloud.POINT.sample_index_float(cloud.named_color("Intensity"), 0)
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----------------------------------------------------------------------------------------------------
        # Incident vector
        
        with tree.layout("Incident vector"):
        
            v = tree.rgb_a(mesh.position, mesh.named_float("w"))        
            Na = mesh.named_color(N4A)
            Nb = mesh.named_color(N4B)
            
            incident = utils.normalize(utils.sub(v, light_loc).v).v
            
        # ----------------------------------------------------------------------------------------------------
        # Reflected vector
        
        with tree.layout("Reflected vector"):
            
            ref_node = maths.surface_reflection(v=incident, n4a=Na, n4b=Nb)
            reflected = ref_node.v
            
        # ----------------------------------------------------------------------------------------------------
        # Intensity
        
        with tree.layout("Intensity with projection direction"):
            proj = maths.projection_matrix().m_3
            
            direct = utils.dot(proj, reflected).value
            direct = direct.switch(direct.less_than(0), 0.)
            
            intensity = intensity*(direct**focus)
            
            color = tree.hsl(color.hue, color.saturation, color.lightness*intensity)
            color = color.switch(ref_node.back, color.mix_difference(1., (.3, .3, .3)))

            mesh.POINT.store_named_float(  "L4 Intensity", intensity)
            mesh.POINT.store_named_vector( "L4 Color",     color)
        
        
        tree.og = mesh + curve + cloud + inst
        
# ====================================================================================================
# Curves
# - Line
# - Circle
# - Spiral

def m_curves():
    
    # ---------------------------------------------------------------------------------------------------- 
    # MODIFIER - A line

    with GeoNodes("Line", prefix=curves) as tree:
        
        v0 = tree.vector_input("Start xyz")
        w0 = tree.float_input( "Start w")
        
        v1 = tree.vector_input("End xyz", (0., 0., 1.))
        w1 = tree.float_input( "End w")
        
        count = tree.integer_input("Resolution", 2, min_value=2)
        
        line = tree.curve_line(v0, v1)
        line.POINT.store_named_float("w", w0)
        line.POINT[1].store_named_float("w", w1)
        
        line.resample_curve(count)
        
        # Tangent is constant
        
        p0 = tree.rgb_a(v0, w0)
        p1 = tree.rgb_a(v1, w1)
        
        line.POINT.store_named_float_color("T4", utils.normalize(utils.sub(p1, p0).v).v)
        
        # Done
        
        tree.og = line
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Parametric Curve
    
    with GeoNodes("Parametric Curve", fake_user=True, prefix=curves) as tree:
        
        s_xyz  = tree.vector_input("Speed xyz", (0., 0., 0.), description="x = speed * t")
        s_w    = tree.float_input( "Speed w",             0., description="w = speed * t")
        
        r_xy   =  tree.float_input("Radius XY",           1., description="Radius in plane XY")
        om_xy  =  tree.angle_input("Omega XY",            0., description="Rotation speed in plane XY")
        r_zw   =  tree.float_input("Radius ZW",           1., description="Radius in plane ZW")
        om_zw  =  tree.angle_input("Omega ZW",            0., description="Rotation speed in plane ZW")
        
        resol  = tree.integer_input("Resolution",         32, description="Curve resolution")
        closed = tree.bool_input(   "Closed",          False, description="Curve is closed")
        
        # ----- Line or circle
        
        curve = tree.curve_line().resample_curve(resol).switch(closed, tree.curve_circle(resolution=resol))
        
        # ----- Parameter
        
        t = (curve.index/(resol-1)).switch(closed, (curve.index/(resol-2)))
        
        ca, sa = tree.cos(om_xy*t), tree.sin(om_xy*t)
        cb, sb = tree.cos(om_zw*t), tree.sin(om_zw*t)
        
        # ===== Position
        
        with tree.layout("Point position"):
            
            x = s_xyz.x*t + ca*r_xy
            y = s_xyz.y*t + sa*r_xy
            z = s_xyz.z*t + cb*r_zw
            w = s_w*t     + sb*r_zw

            curve.position = tree.xyz(x, y, z)
            curve.POINT.store_named_float("w", w)
        
        # ===== Tangent
        # dx/dt = s - o.r.sin(o.t)
        
        with tree.layout("Tangent"):
            
            ro_xy = om_xy*r_xy
            ro_zw = om_zw*r_zw
            
            tx = s_xyz.x - ro_xy*sa
            ty = s_xyz.y + ro_xy*ca
            tz = s_xyz.z - ro_zw*sb
            tw = s_w     + ro_zw*cb
            
            curve.POINT.store_named_float_color(T4, utils.normalize(tree.rgb(tx, ty, tz, tw)).v)
        
        tree.og = curve
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Mesh along a curve
    
    with GeoNodes("Curve to Mesh", is_group=True, fake_user=True, prefix=maths) as tree:
        
        curve      = tree.geometry_input("Curve")
        mesh       = tree.geometry_input("Mesh")
        scale      = tree.float_input(   "Scale", 1.)
        use_radius = tree.bool_input(    "Use Radius", False)
        
        # ---------------------------------------------------------------------------
        # Points at origin to instantiate the meshes
        
        count = curve.CURVE.domain_size().point_count
        pts = tree.Points(count).geometry
        pts.position = 0
        
        # ---------------------------------------------------------------------------
        # Instantiate the surface the right number of times at location zero
        # to perform rotation
        
        n = mesh.domain_size().point_count
        
        insts = pts.instance_on_points(instance=mesh)
        
        # Scale with spline radius
        insts.scale_instances(scale=scale.switch(use_radius, curve.sample_index_float(curve.radius, insts.index)))
        
        # Realize the instances
        meshes = insts.realize_instances()
        mesh_index = meshes.index/n

        # ---------------------------------------------------------------------------
        # Read the information from the curve
        
        # Points location
        Cxyz = curve.sample_index_vector(curve.position, index=mesh_index)
        Cw   = curve.sample_index_float(curve.named_float("w"), index=mesh_index)
        
        # Tangent
        T    = curve.sample_index_color(curve.named_color(T4), index=mesh_index)
        node = utils.to_xyz_w(T)
        Txyz, Tw = node.xyz, node.w
        

        # ---------------------------------------------------------------------------
        # Rotation to align (0, 0, 0, 1) -> Tangent and then translation
        
        meshes = modifiers.align_vector(meshes, from_xyz=(0., 0., 0.), from_w=1., to_xyz=Txyz, to_w=Tw).geometry
        
        meshes.offset = Cxyz
        meshes.POINT.store_named_float("w", Cw + meshes.named_float("w"))
        
        # Done
        
        meshes.to_output("Mesh")
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh along a curve
    
    with GeoNodes("Curve to Mesh", fake_user=True, prefix=curves) as tree:
        
        curve      = tree.ig
        surface    = tree.object_input("Mesh Object", description="3D Mesh to instantiate along the curve")
        scale      = tree.float_input( "Scale", 1.)
        use_radius = tree.bool_input(  "Use Radius", False)

        mesh = surface.object_info().geometry
        
        mesh = maths.curve_to_mesh(
            curve      = curve,
            mesh       = mesh,
            scale      = scale,
            use_radius = use_radius).mesh
        
        tree.og = mesh
        
        if False:
            
            # ---------------------------------------------------------------------------
            # Points at origin to instantiate the meshes
            
            count = curve.CURVE.domain_size().point_count
            pts = tree.Points(count).geometry
            pts.position = 0
            
            # ---------------------------------------------------------------------------
            # Instantiate the surface the right number of times at location zero
            # to perform rotation
            
            mesh = surface.object_info().geometry
            n = mesh.domain_size().point_count
            
            insts = pts.instance_on_points(instance=mesh)
            
            # Scale with spline radius
            #insts.scale_instances(scale=scale.switch(use_radius, curve.sample_index_float(curve.radius, insts.index)))
            
            # Realize the instances
            meshes = insts.realize_instances()
            mesh_index = meshes.index/n
    
            # ---------------------------------------------------------------------------
            # Read the information from the curve
            
            # Points location
            Cxyz = curve.sample_index_vector(curve.position, index=mesh_index)
            Cw   = curve.sample_index_float(curve.named_float("w"), index=mesh_index)
            
            # Tangent
            T    = curve.sample_index_color(curve.named_color(T4), index=mesh_index)
            node = utils.to_xyz_w(T)
            Txyz, Tw = node.xyz, node.w
            
    
            # ---------------------------------------------------------------------------
            # Rotation to align (0, 0, 0, 1) -> Tangent and then translation
            
            meshes = modifiers.align_vector(meshes, from_xyz=(0., 0., 0.), from_w=1., to_xyz=Txyz, to_w=Tw).geometry
            
            meshes.offset = Cxyz
            meshes.store_named_float("w", Cw)
            
            # Done
            
            tree.og = meshes
            
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh along a curve
    
    with GeoNodes("Curve to Mesh with Spheres", fake_user=True, prefix=curves) as tree:
        
        curve      = tree.ig
        resol      = tree.integer_input("Sphere Resolution", 16, min_value=3)
        size       = tree.float_input(  "Size", 1.)
        use_radius = tree.bool_input(   "Use Radius", False)
        mat        = tree.material_input("Material")
        
        sphere = tree.uv_sphere(rings=resol, segments=2*resol, radius=size)
        sphere.material=mat
        
        mesh = maths.curve_to_mesh(
                curve       = curve,
                mesh        = sphere,
                scale       = 1.,
                use_radius  = use_radius).mesh
        
        mesh.shade_smooth = True
        
        tree.og = mesh
        
# ====================================================================================================
# Surfaces

def m_surfaces():
    
    with GeoNodes("HyperSphere", fake_user=True, prefix=surfaces) as tree:
        
        radius = tree.float_input("Radius",       1., min_value=.01)
        resol  = tree.integer_input("Resolution", 16, min_value=3)
        slices = tree.integer_input("Slices",     7,  min_value=1)
        mat    = tree.material_input("Material")
        
        line = curves.line(start_xyz=(0, 0, -radius), end_xyz=(0, 0, radius), resolution=slices+2).geometry
        z = (2*line.index/(slices+1) - 1)*(tree.pi/2)
        line.radius = radius*tree.cos(z)
        
        line[slices+1].POINT.delete_geometry()
        line[0].POINT.delete_geometry()
        
        hs = curves.curve_to_mesh_with_spheres(
            geometry   = line,
            sphere_resolution = resol,
            use_radius = True,
            material   = mat,
            )
        
        hs.shade_smooth = True
        
        tree.og = hs
        
        
        
        



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
            
            
# ====================================================================================================
# Legacy

def legacy():

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotate to an hyperplane 

    with GeoNodes("Rotate to hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:

        v = tree.color_input("V")
        
        hv = tree.color_input("Hyperplane")
        
        node = maths.hyperplane(v=hv)
        
        x = node.i.dot(v)
        y = node.j.dot(v)
        z = node.k.dot(v)
        w = node.l.dot(v)
        
        tree.rgb(x, y, z, w).to_output("V")
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotate from an hyperplane 

    with GeoNodes("Rotate from hyperplane", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v  = tree.color_input("V")
        hv = tree.color_input("Hyperplane")
        
        node = maths.hyperplane(v=hv)
        
        r = node.i*v.x + node.j*v.y + node.k*v.z + node.l*v.w
        
        r.to_output("V")
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation 3D in an hyperplane
    # Perform a 3D rotation with an hyperplane

    with GeoNodes("Rotation 3D", is_group=True, fake_user=True, prefix=maths) as tree:
        
        v  = tree.color_input("V")
        hv = tree.color_input("Hyperplane")

        euler = tree.rotation_input("Euler")
        axis  = tree.vector_input(  "Axis", (0., 0., 1.))
        angle = tree.angle_input(   "Angle")
        
        to_hp = maths.rotate_to_hyperplane(v=v, hyperplane=hv)
        
        v3 = tree.VECTOR(to_hp.v)
        
        v3 = v3.vector_rotate(rotation=euler.rotation_to_euler(), rotation_type='EULER_XYZ')
        v3 = v3.vector_rotate(axis=axis, angle=angle, rotation_type='AXIS_ANGLE')
        
        from_hp = maths.rotate_from_hyperplane(v=tree.rgb_a(v3, to_hp.v.w), hyperplane=hv)
        
        from_hp.v.to_output("V")
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - 3D Rotation

    with GeoNodes("Rotation 3D", fake_user=True, prefix=modifiers) as tree:
    
        geo   = tree.ig
        
        hv    = tree.vector_input(  "Hyper xyz")
        hw    = tree.float_input(   "Hyper w", 1.)
        euler = tree.rotation_input("Euler", description="Euler rotation within the hyperplane")
        axis  = tree.vector_input(  "Axis", (0., 0., 1.), description="Axis inside the hyperplane")
        angle = tree.angle_input(   "Angle", description="Angle to rotate around the axis within the hyperplane")
        
        hp = tree.rgb_a(hv, hw)
        
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            
            node = maths.rotation_3d(
                v = tree.rgb_a(geo.position, geo.named_float("w")),
                hyperplane = hp, euler=euler, axis=axis, angle=angle)

            geo.position = node.v
            geo.POINT.store_named_float("w", node.v.w)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            
            node = maths.rotation_3d(
                v = mesh.named_color("N4a"),
                hyperplane = hp, euler=euler, axis=axis, angle=angle)
            
            mesh.FACE.store_named_float_color("N4a", node.v)
            
            node = maths.rotation_3d(
                v = mesh.named_color("N4b"),
                hyperplane = hp, euler=euler, axis=axis, angle=angle)
            
            mesh.FACE.store_named_float_color("N4b", node.v)
            
        # ----- Curve
        
        with tree.layout("Curve"):
            
            node = maths.rotation_3d(
                v = curve.named_color("T4"),
                hyperplane = hp, euler=euler, axis=axis, angle=angle)
            
            curve.POINT.store_named_float_color("T4", node.v)

        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # Rotation in a plane (x|y|z, w)
    # Rotate a 4D object: coordinates and normals
            
    with GeoNodes("W Plane Rotation", fake_user=True, prefix=modifiers) as tree:
        
        geo   = tree.ig
        axis  = tree.integer_input("Axis", 0, min_value=0, max_value=2) 
        angle = tree.angle_input(  "Angle", 0.)
        
        # ----- All
        
        with tree.layout("All points rotation"):
            
            node = maths.w_plane_rotation(
                    v = tree.rgb_a(geo.position, geo.named_float("w")),
                    axis = axis, angle=angle)
            
            geo.POINT.position = node.v
            geo.POINT.store_named_float("w", node.v.w)
            
            
        # --- Components
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # Mesh
        
        with tree.layout("Mesh"):

            node = maths.w_plane_rotation(
                        v = mesh.named_color("N4"),
                        axis = axis, angle=angle)
            
            mesh.FACE.store_named_float_color("N4", node.v)
            
        # Curve
        
        with tree.layout("Curve"):

            node = maths.w_plane_rotation(
                        v = curve.named_color("T4"),
                        axis = axis, angle=angle)
            
            curve.POINT.store_named_float_color("T4", node.v)

        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # Rotation in a plane defined by two vectors V0 and V1
            
    with GeoNodes("Rotation 2D", fake_user=True, prefix=modifiers) as tree:
        
        geo   = tree.ig

        v0    = tree.vector_input("xyz 0")
        w0    = tree.float_input( "w 0")
        v1    = tree.vector_input("xyz 1")
        w1    = tree.float_input( "w 1")
        angle = tree.angle_input( "Angle", 0. , description="Rotation angle in plane (V0, V1)")
        
        I = tree.rgb_a(v0, w0)
        J = tree.rgb_a(v1, w1)
        
        # ----- All
        
        with tree.layout("All points rotation"):
            
            node = maths.rotation_2d(
                v = tree.rgb_a(geo.position, geo.named_float("w")),
                i=I, j=J, angle=angle)

            geo.position = node.v
            geo.POINT.store_named_float("w", node.v.w)
            
        # --- Components
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # Mesh
        
        with tree.layout("Mesh"):
            
            node = maths.rotation_2d(
                v = mesh.named_color("N4"),
                i=I, j=J, angle=angle)

            mesh.FACE.store_named_float_color("N4", node.v)
            
        # Curve
        
        with tree.layout("Curve"):
            
            node = maths.rotation_2d(
                v = curve.named_color("T4"),
                i=I, j=J, angle=angle)
            
            curve.POINT.store_named_float_color("T4", node.v)
            

        tree.og = mesh + curve + cloud + inst


                
        
            
            
            
    


    
        
    
    
    

        


        

