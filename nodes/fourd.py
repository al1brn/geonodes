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

g_maths   = GeoNodes.prefixed("M")
g_mods    = GeoNodes.prefixed("4D")
g_curves  = GeoNodes.prefixed("C")
g_surfs   = GeoNodes.prefixed("S")

ZERO = 0.0001

# ----- Named attributes

def clear_all():
    g_maths.clear()
    g_mods.clear()
    g_curves.clear()
    g_surfs.clear()
    
def rebuild():
    
    build_shaders()
    
    build_matrices()
    build_base()
    build_vectors()
    build_transformations()
    build_lights()
    build_curves()
    

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
# A 4-vector is a couple (V: Vector, w: float)

class V4:
    def __init__(self, V, w):
        tree = GeoNodes.current_tree()
        
        if hasattr(V, 'bsocket'):
            self.V = V
        else:
            self.V = tree.Vector(V)
            
        if hasattr(w, 'bsocket'):
            self.w = w
        else:
            self.w = tree.value(w) 
        
    @property
    def x(self):
        return self.V.x
    
    @property
    def y(self):
        return self.V.y
    
    @property
    def z(self):
        return self.V.z
    
    @classmethod
    def Input(cls, tree, name=None, v=(0., 0., 0., 0.), description=""):
        name = "" if name is None else name + " "
        return cls(
            tree.vector_input(name + "V", (v[0], v[1], v[2]), description=description),
            tree.float_input( name + "w", v[3], description=description))
    
    def to_output(self, name=None):
        name = "" if name is None else name + " "
        self.V.to_output(name + "V")
        self.w.to_output(name + "w")
        
    @classmethod
    def NodeOutput(cls, node, name=None):
        name = "" if name is None else name.lower().replace(' ', '_') + "_"
        return cls(getattr(node, name + "v"), getattr(node, name + "w"))

    @property
    def args(self, name=None):
        return (self.V, self.w)
    
    def kwargs(self, name=None):
        name = "" if name is None else name.lower().replace(' ', '_') + "_"
        return {name + "v": self.V, name + "w": self.w}
    
    @classmethod
    def Xyzw(cls, x, y, z, w):
        tree = GeoNodes.current_tree()
        return cls(tree.xyz(x, y, z), w)
    
    @classmethod
    def Position(cls, geo):
        return cls(geo.position, geo.named_float("w"))
    
    def set_position(self, geo):
        geo.position = self.V
        return geo.store_named_float("w", self.w)
        
    @classmethod
    def Normal(cls, geo, suffix):
        return cls(geo.named_vector(f"N{suffix}V"), geo.FACE.named_float(f"N{suffix}w"))
    
    def set_normal(self, geo, suffix):
        geo.FACE.store_named_vector(f"N{suffix}V", self.V)
        return geo.FACE.store_named_float( f"N{suffix}w", self.w)
    
    @classmethod
    def Tangent(cls, geo):
        return cls(geo.named_vector("TV"), geo.FACE.named_float("Tw"))
    
    def set_tangent(self, geo):
        geo.POINT.store_named_vector("TV", self.V)
        return geo.POINT.store_named_float( "Tw", self.w)
        
    # ----------------------------------------------------------------------------------------------------
    # Operations
        
    def __neg__(self):
        return cls(-self.V, -self.w)
        
    def __add__(self, other):
        return V4(self.V + other.V, self.w + other.w)
    
    def __iadd__(self, other):
        self.V += other.V
        self.w += other.w
        
    def __sub__(self, other):
        return V4(self.V - other.V, self.w - other.w)
    
    def __iadd__(self, other):
        self.V -= other.V
        self.w -= other.w
        
    def __mul__(self, other):
        if isinstance(other, V4):
            return V4(self.V*other.V, self.w*other.w)
        else:
            return V4(self.V*other, self.w*other)

    def __imul__(self, other):
        if isinstance(other, V4):
            self.V *= other.V
            self.w *= other.w
        else:
            self.V *= other
            self.w *= other
            
    def __truediv__(self, other):
        if isinstance(other, V4):
            return V4(self.V/other.V, self.w/other.w)
        else:
            return V4(self.V/other, self.w/other)

    def __itruediv__(self, other):
        if isinstance(other, V4):
            self.V /= other.V
            self.w /= other.w
        else:
            self.V /= other
            self.w /= other
            
    def dot(self, other):
        return self.V.dot(other.V) + self.w*other.w
    
    @property
    def length(self):
        return self.V.tree.sqrt(self.V.dot(self.V) + self.w*self.w)
    
    def normalized(self, return_error=False):
        n = self.length
        err = n.less_than(ZERO)
        v4 = V4((self.V/n).switch(err, self.V), (self.w/n).switch(err, self.w))
        if return_error:
            return v4, err
        else:
            return v4
        
    def mat_dot(self, M):
        
        v0 = V4.NodeOutput(M, "R 0")
        v1 = V4.NodeOutput(M, "R 1")
        v2 = V4.NodeOutput(M, "R 2")
        v3 = V4.NodeOutput(M, "R 3")
        
        return V4.Xyzw(
            v0.x*self.x + v0.y*self.y + v0.z*self.z + v0.w*self.w,
            v1.x*self.x + v1.y*self.y + v1.z*self.z + v1.w*self.w,
            v2.x*self.x + v2.y*self.y + v2.z*self.z + v2.w*self.w,
            v3.x*self.x + v3.y*self.y + v3.z*self.z + v3.w*self.w)
    
    def switch(self, b, other):
        return V4(self.V.switch(b, other.V), self.w.switch(b, other.w))
    
    def angle_with(self, other):
        a = self.normalized()
        b = other.normalized()
        
        return self.V.tree.arccos(a.dot(b))

# =============================================================================================================================
# Matrices groups
# Groups:
# - Mat Mult
# - XW Rotation
# - YW Rotation
# - ZW Rotation
# - Projection Matrix
# - Projection

def build_matrices():
    
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Ensure Projection and Projection2 objects exist
    
    blender.get_empty("Projection")
    blender.get_empty("Projection2")
    
    # ----------------------------------------------------------------------------------------------------
    # Matrices multiplication
    
    with GeoNodes("Mat Mult", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        A = [V4.Input(tree, f"A {i}") for i in range(4)]
        B = [V4.Input(tree, f"B {i}") for i in range(4)]

        C = [V4.Xyzw(B[0].x, B[1].x, B[2].x, B[3].x),
             V4.Xyzw(B[0].y, B[1].y, B[2].y, B[3].y),
             V4.Xyzw(B[0].z, B[1].z, B[2].z, B[3].z),
             V4.Xyzw(B[0].w, B[1].w, B[2].w, B[3].w)]
        
        for i in range(4):
            with tree.layout(f"Line {i}"):
                V4.Xyzw(A[i].dot(C[0]), A[i].dot(C[1]), A[i].dot(C[2]), A[i].dot(C[3])).to_output(f"R {i}")
            
    # ----------------------------------------------------------------------------------------------------
    # GROUP - XW / YZ rotations
    
    with GeoNodes("XW Rotation", is_group=True, fake_user=True, prefix=g_maths) as tree:

        ag = tree.angle_input("Angle")
        ca = tree.cos(ag)
        sa = tree.sin(ag)
        
        a2 = tree.angle_input("Second")
        c2 = tree.cos(a2)
        s2 = tree.sin(a2)
        
        V4.Xyzw(ca,  0,   0, -sa).to_output("R 0")
        V4.Xyzw( 0, c2, -s2,   0).to_output("R 1")
        V4.Xyzw( 0, s2,  c2,   0).to_output("R 2")
        V4.Xyzw(sa,  0,   0,  ca).to_output("R 3")
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - YW / ZX rotations
    
    with GeoNodes("YW Rotation", is_group=True, fake_user=True, prefix=g_maths) as tree:

        ag = tree.angle_input("Angle")
        ca = tree.cos(ag)
        sa = tree.sin(ag)
        
        a2 = tree.angle_input("Second")
        c2 = tree.cos(a2)
        s2 = tree.sin(a2)
        
        V4.Xyzw(  c2,  0, s2,   0).to_output("R 0")
        V4.Xyzw(   0, ca,  0,  sa).to_output("R 1")
        V4.Xyzw( -s2,  0, c2,   0).to_output("R 2")
        V4.Xyzw(   0,-sa,  0,  ca).to_output("R 3")
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - ZW / XY rotations
    
    with GeoNodes("ZW Rotation", is_group=True, fake_user=True, prefix=g_maths) as tree:

        ag = tree.angle_input("Angle")
        ca = tree.cos(ag)
        sa = tree.sin(ag)
        
        a2 = tree.angle_input("Second")
        c2 = tree.cos(a2)
        s2 = tree.sin(a2)
        
        V4.Xyzw( c2, -s2,  0,   0).to_output("R 0")
        V4.Xyzw( s2,  c2,  0,   0).to_output("R 1")
        V4.Xyzw(  0,   0, ca, -sa).to_output("R 2")
        V4.Xyzw(  0,   0, sa,  ca).to_output("R 3")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Projection matrix

    with GeoNodes("Projection Matrix", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        abc = tree.ObjectInfo("Projection").rotation
        a = abc.x
        b = abc.y
        c = abc.z
        
        second = tree.ObjectInfo("Projection2").rotation
        a2 = second.x
        b2 = second.y
        c2 = second.z
        
        M0 = g_maths.xw_rotation(angle=a, second=a2)
        M1 = g_maths.yw_rotation(angle=b, second=b2)
        M2 = g_maths.zw_rotation(angle=c, second=c2)
        
        M_ = g_maths.mat_mult(
            M0.r_0_v, M0.r_0_w, M0.r_1_v, M0.r_1_w, M0.r_2_v, M0.r_2_w, M0.r_3_v, M0.r_3_w,
            M1.r_0_v, M1.r_0_w, M1.r_1_v, M1.r_1_w, M1.r_2_v, M1.r_2_w, M1.r_3_v, M1.r_3_w)
    
        M_ = g_maths.mat_mult(
            M_.r_0_v, M_.r_0_w, M_.r_1_v, M_.r_1_w, M_.r_2_v, M_.r_2_w, M_.r_3_v, M_.r_3_w,
            M2.r_0_v, M2.r_0_w, M2.r_1_v, M2.r_1_w, M2.r_2_v, M2.r_2_w, M2.r_3_v, M2.r_3_w)
        
        V4.NodeOutput(M_, "R 0").to_output("R 0")
        V4.NodeOutput(M_, "R 1").to_output("R 1")
        V4.NodeOutput(M_, "R 2").to_output("R 2")
        V4.NodeOutput(M_, "R 3").to_output("R 3")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Perform a projection

    with GeoNodes("Projection", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        v = V4.Input(tree)
            
        v.mat_dot(g_maths.projection_matrix()).to_output()

# ====================================================================================================
# Base modifiers
# Modifiers:
# - Plunge 3D Geometry
# - Arrow
# - Axis viewer
# - Projection

def build_base():
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Add the 4D attributes

    with GeoNodes("Plunge 3D Geometry", fake_user=True, prefix=g_mods) as tree:
        
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
        
        V4(mesh.normal,  0.).set_normal(mesh, "A")
        V4((0., 0., 0.), 1.).set_normal(mesh, "B")
        
        # ---- Curve tangents
        
        V4(curve.curve_tangent,  0.).set_tangent(curve)
            
        # ---- Result
        
        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Arrow

    with GeoNodes("Arrow", fake_user=True, prefix=g_mods) as tree:
        
        v0     = V4.Input(tree, "Start")
        v1     = V4.Input(tree, "End")
        
        radius = tree.float_input(   "Radius", 0.05)
        resol  = tree.integer_input( "Resolution", 8, min_value=3, max_value=32)
        mat    = tree.material_input("Material")
        
        with tree.layout("Arrow shaft"):
        
            # ----- Start and end point

            p0 = g_maths.projection(**v0.kwargs()).v
            p1 = g_maths.projection(**v1.kwargs()).v
            
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
            
    with GeoNodes("Axis Viewer", fake_user=True, prefix=g_mods) as tree:
        
        neg    = tree.float_input(  "Negative", -1,  max_value=0.)
        pos    = tree.float_input(  "Positive",  3,  min_value=0.)
        radius = tree.float_input(  "Radius", 0.05)
        resol  = tree.integer_input("Resolution", 8, min_value=3, max_value=32)
        
        # ----- Loop on the axis
        
        for i in range(4):
        
            node = g_mods.arrow(
                start_v = [(neg, 0, 0), (0, neg, 0), (0, 0, neg), (0, 0, 0)][i],
                start_w = [0, 0, 0, neg][i],
                end_v   = [(pos, 0, 0), (0, pos, 0), (0, 0, pos), (0, 0, 0)][i],
                end_w   = [0, 0, 0, pos][i],
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

    with GeoNodes("Projection", fake_user=True, prefix=g_mods) as tree:
        
        geo          = tree.ig
        shade_smooth = tree.bool_input("Shade smooth", True)
        
        # ===== Points projection
        
        with tree.layout("All points projection"):
            v = V4.Position(geo)
            v = g_maths.projection(*v.args).v
            geo.position = v
            
        # ===== Components
        
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Back face computation
        
        with tree.layout("Mesh projection"):
            
            m_proj = g_maths.projection_matrix()
            v_proj = V4.NodeOutput(m_proj, "R 3")
            
            back = tree.boolean(True)
            for sn in ["A", "B"]:
                n = V4.Normal(mesh, sn)
                dot = v_proj.dot(n)
                back *= dot.less_than(0)

            mesh.FACE.store_named_boolean("Back", back)
            mesh.FACE.shade_smooth = shade_smooth
            
                
        tree.og = tree.join_geometry(mesh, curve, cloud, inst)
        
        
# =============================================================================================================================
# Vectors groups
# - Normalize 2-basis
# - Normalize 3-basis
# - Cross product between 3 vectors
# - Hyperplane
# - Two equations solver 
        
def build_vectors():
    
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Normalize two vectors forming a plane

    with GeoNodes("Normalize 2-Basis", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        u0 = V4.Input(tree, "I")
        u1 = V4.Input(tree, "J")
        
        # We suppress from u1 the u0 component
        
        u1 -= u0*u1.dot(u0)
    
        # Normalized
        
        u0.normalized(False).to_output("I")
        u1.normalized(False).to_output("J")
            
            
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Normal basis
    # 3 vectors forming a normal basis to a 3D hyperplane defined by three independant vectors

    with GeoNodes("Normalize 3-Basis", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        u0 = V4.Input(tree, "I", (1., 0., 0., 0.))
        u1 = V4.Input(tree, "J", (0., 1., 0., 0.))
        u2 = V4.Input(tree, "K", (0., 0., 1., 0.))
        
        # ----- Let's normalize the first vector
        
        e0, err = u0.normalized(True)
            
        # Let's suppress this dimension in the second one
        
        with tree.layout("Make the second vector perp to the first"):
            
            # u1 minus e0 part

            d = e0.dot(u1)
            u1 -= e0*d

            # Let's normalize
            
            e1, er = u1.normalized(True)
            err += er
            
        with tree.layout("Make the third vector perp to the two other ones"):
            
            # u2 minus e0 and e1 part
            
            d = e0.dot(u2)
            u2 -= e0*d
            
            d = e1.dot(u2)
            u2 -= e1*d
            
            # Let's normalize
            
            e2, er = u2.normalized(True)
            err += er
            
        # ----- We are done :-)
        
        e0.to_output("I")
        e1.to_output("J")
        e2.to_output("K")
        
        err.to_output("Error")        

                
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Cross
    # A vector peprpendicular to three independant vectors

    with GeoNodes("Cross", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        u0 = V4.Input(tree, "I", (1., 0., 0., 0.))
        u1 = V4.Input(tree, "J", (0., 1., 0., 0.))
        u2 = V4.Input(tree, "K", (0., 0., 1., 0.))
        
        # ----- Convert the three input vectors in a normal basis
        
        node = g_maths.normalize_3_basis()
        tree.input_node.plug_to(node)
        
        u0 = V4.NodeOutput(node, "I")
        u1 = V4.NodeOutput(node, "J")
        u2 = V4.NodeOutput(node, "K")
        
        error = node.error
        
        n3 = tree.float(0)
        u3 = V4.Xyzw(0., 0., 0., 0.)
        for i in range(4):
            with tree.layout(f"Axis {i}"):
                
                v4 = [0] * 4
                v4[i] = 1
                
                u = V4.Xyzw(*v4)
                
                d0 = u0.dot(u)
                d1 = u1.dot(u)
                d2 = u2.dot(u)
                u -= u0*d0
                u -= u1*d1
                u -= u2*d2
                
                # Resulting norm
                
                n = u.length
                
                greater = n.greater_than(n3)
                u3 = u3.switch(greater, u)
                n3 = n3.switch(greater, n)
                
        # ----- Let's normalize the result
        
        u3 = u3.normalized()

        u3.to_output()
        error.to_output("Error")

            
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Compute three vectors perpendicular to a vector

    with GeoNodes("Hyperplane", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        v = V4.Input(tree)
        
        # ----- Normalize the entry
        
        v = v.normalized()
        
        # ----- Try to build a 3D-base with v and plane (k, l)
        
        node = g_maths.normalize_3_basis(*v.args, (0., 0., 1.), 0., (0., 0., 0.), 1.)
        
        u0 = V4.NodeOutput(node, "J")
        u1 = V4.NodeOutput(node, "K")
            
        error = node.error
        
        # ---------------------------------------------------------------------------
        # If error, it does mean that v is in plane (k, l), hence (i, j) is perp to v
        
        node = g_maths.cross(*v.args, (1., 0., 0.), 0., (0., 1., 0.), 0.)

        e_u2 = V4.NodeOutput(node)
        
        # ---------------------------------------------------------------------------
        # If no error, we have (u0, u1) perp to input vector
        # The third basis vector is perpendicular to these 3 vectors
        
        node = g_maths.cross(*v.args, *u0.args, *u1.args)
        u2 = V4.NodeOutput(node)

        u0 = u0.switch(error, V4.Xyzw(1., 0., 0., 0.))
        u1 = u1.switch(error, V4.Xyzw(0., 1., 0., 0.))
        u2 = u2.switch(error, e_u2)
        
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

    with GeoNodes("Two equations solver", is_group=True, prefix=g_maths) as tree:
        
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
        
def build_transformations():
    
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Translation
        
    with GeoNodes("Translation", fake_user=True, prefix=g_mods) as tree:
        
        geo = tree.ig
        
        v = V4.Input(tree)
        
        geo.transform_geometry(translation=v.V)
        geo.POINT.store_named_float("w", geo.named_float("w") + v.w)
        
        tree.og = geo
    
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Scale
        
    with GeoNodes("Scale", fake_user=True, prefix=g_mods) as tree:
        
        geo = tree.ig
        
        scale = V4.Input(tree, "Scale", (1., 1., 1., 1.))
        
        geo.transform_geometry(scale=scale.V)
        geo.POINT.store_named_float("w", geo.named_float("w")*scale.w)
        
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances

        # ----- Mesh
        
        with tree.layout("Mesh"):
            
            n = V4.Normal(mesh, "A")*scale
            n.normalized().set_normal(mesh, "A")
            
            n = V4.Normal(mesh, "B")*scale
            n.normalized().set_normal(mesh, "B")
            
        # ----- Curve
        
        with tree.layout("Curve"):

            t = V4.Tangent(curve)*scale
            t.normalized().set_tangent(curve)

        tree.og = mesh + curve + cloud + inst        
    
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation 4D
        
    with GeoNodes("Rotation 4D", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        v = V4.Input(tree)
        
        xy = tree.angle_input("XY", description="Rotation in the plane XY")
        zw = tree.angle_input("ZW", description="Rotation in the plane ZW")

        xz = tree.angle_input("XZ", description="Rotation in the plane XZ")
        yw = tree.angle_input("YW", description="Rotation in the plane YW")
        
        xw = tree.angle_input("XW", description="Rotation in the plane XW")
        yz = tree.angle_input("YZ", description="Rotation in the plane YZ")
        
        # ----- Rotation xy / zw
        
        ca, sa = tree.cos(xy), tree.sin(xy)
        cb, sb = tree.cos(zw), tree.sin(zw)
        A0 = V4.Xyzw( ca, -sa,  0.,  0.)
        A1 = V4.Xyzw( sa,  ca,  0.,  0.)
        A2 = V4.Xyzw( 0.,  0.,  cb, -sb)
        A3 = V4.Xyzw( 0.,  0.,  sb,  cb)
        
        # ----- Rotation xz / yw
        
        ca, sa = tree.cos(xz), tree.sin(xz)
        cb, sb = tree.cos(yw), tree.sin(yw)
        B0 = V4.Xyzw( ca,  0.,  sa,  0.)
        B1 = V4.Xyzw( 0.,  cb,  0.,  sb)
        B2 = V4.Xyzw(-sa,  0.,  ca,  0.)
        B3 = V4.Xyzw( 0., -sb,  0.,  cb)
        
        # ----- Rotation xw / yz
        
        ca, sa = tree.cos(xw), tree.sin(xw)
        cb, sb = tree.cos(yz), tree.sin(yz)
        C0 = V4.Xyzw( ca,  0.,  0., -sa)
        C1 = V4.Xyzw( 0.,  cb, -sb,  0.)
        C2 = V4.Xyzw( 0.,  sb, cb,  0.)
        C3 = V4.Xyzw( sa,  0.,  0.,  ca)
        
        # ----- Multiply the matrices
        
        node = g_maths.mat_mult(*A0.args, *A1.args, *A2.args, *A3.args, *B0.args, *B1.args, *B2.args, *B3.args)
        M0 = V4.NodeOutput(node, "R 0")
        M1 = V4.NodeOutput(node, "R 1")
        M2 = V4.NodeOutput(node, "R 2")
        M3 = V4.NodeOutput(node, "R 3")
        
        node = g_maths.mat_mult(*M0.args, *M1.args, *M2.args, *M3.args, *C0.args, *C1.args, *C2.args, *C3.args)

        # ----- Rotate the vector
        
        v.mat_dot(node).to_output()
        
    # ----------------------------------------------------------------------------------------------------
    # Modifier - Rotation 4D
        
    with GeoNodes("Rotation 4D", fake_user=True, prefix=g_mods) as tree:
        
        geo = tree.ig
        
        xy = tree.angle_input("XY", description="Rotation in the plane XY")
        zw = tree.angle_input("ZW", description="Rotation in the plane ZW")

        xz = tree.angle_input("XZ", description="Rotation in the plane XZ")
        yw = tree.angle_input("YW", description="Rotation in the plane YW")
        
        xw = tree.angle_input("XW", description="Rotation in the plane XW")
        yz = tree.angle_input("YZ", description="Rotation in the plane YZ")
        
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            
            node = g_maths.rotation_4d(**V4.Position(geo).kwargs())
            tree.input_node.plug_to(node)
            
            V4.NodeOutput(node).set_position(geo)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            
            for s in ["A","B"]:
                node = g_maths.rotation_4d(**V4.Normal(mesh, s).kwargs())
                tree.input_node.plug_to(node)
                V4.NodeOutput(node).set_normal(mesh, s)
            
        # ----- Curve
        
        with tree.layout("Curve"):

            node = g_maths.rotation_4d(**V4.Tangent(curve).kwargs())
            tree.input_node.plug_to(node)
            V4.NodeOutput(node).set_tangent(curve)

        tree.og = mesh + curve + cloud + inst
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation in a plane defined by two 4D vectors
        
    with GeoNodes("Rotation 2D", is_group=True, fake_user=True, prefix=g_maths) as tree:

        v  = V4.Input(tree)
        
        I  = V4.Input(tree, "I")
        J  = V4.Input(tree, "J")
        ag = tree.angle_input( "Angle", description="Rotation angle in plane (I, J)")
        
        # ---------------------------------------------------------------------------
        # Decompose the vector along I, J and remainder
        
        with tree.layout("Decompose I, J, Remainder"):
            x  = I.dot(v)
            y  = J.dot(v)
            v_ = v - I*x - J*y
        
        # ---------------------------------------------------------------------------
        # Rotate x, y
        
        with tree.layout("Rotation 2D"):
        
            ca, sa = tree.cos(ag), tree.sin(ag)
            x_ = x*ca - y*sa
            y_ = x*sa + y*ca

        # ---------------------------------------------------------------------------
        # Recompose the vector
        
        with tree.layout("Recompose"):
            
            r = v_ + I*x_ + J*y_
            
        r.to_output()
        
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Rotation in a plane defined by two 4D vectors
        
    with GeoNodes("Rotation 2D", fake_user=True, prefix=g_mods) as tree:

        geo = tree.ig
        
        v0 = V4.Input(tree, "I", (1., 0., 0., 0.))
        v1 = V4.Input(tree, "J", (0., 1., 0., 0.))
        ag = tree.angle_input("Angle", description="Rotation angle in plane (I, J)")
        
        # ===== Normal 2-Basis
        
        with tree.layout("Normal 2-Basis"):
            node = g_maths.normalize_2_basis(*I.args, *J.args)
            I = V4.NodeOutput(node, "I")
            J = V4.NodeOutput(node, "J")
            
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            node = g_maths.rotation_2d(*V4.Position(geo).args, *I.args, *J.args, angle=ag)
            V4.NodeOutput(node).set_position(geo)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            for s in ["A", "B"]:
                node = g_maths.rotation_2d(*V4.Normal(mesh, s).args, *I.args, *J.args, angle=ag)
                V4.NodeOutput(node).set_normal(mesh, s)
            
        # ----- Curve
        
        with tree.layout("Curve"):
            node = g_maths.rotation_2d(*V4.Tangent(curve).args, *I.args, *J.args, angle=ag)
            V4.NodeOutput(node).set_tangent(curve)

        tree.og = mesh + curve + cloud + inst            
        
        
    # ----------------------------------------------------------------------------------------------------
    # GROUP - Follow a vector
    #
    # Rotate a vector such as the vector A rotates to vector B

    with GeoNodes("Align Vector", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        v = V4.Input(tree)

        va = V4.Input(tree, "From")
        vb = V4.Input(tree, "To")

        # ----- Normal 2-Basis
        
        with tree.layout("Normal 2-Basis"):
            node = g_maths.normalize_2_basis(*va.args, *vb.args)
            I = V4.NodeOutput(node, "I")
            J = V4.NodeOutput(node, "J")
        
        # ----- Angle between the two vectors
        
        ag = va.angle_with(vb)
        
        # ----- Rotate in the plane I, J
        
        node = g_maths.rotation_2D(*v.args, *I.args, *J.args, angle=ag)
        V4.NodeOutput(node).to_output()

            
    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Follow a vector
    #
    # Rotate a vector such as the vector A rotates to vector B

    with GeoNodes("Align vector", fake_user=True, prefix=g_mods) as tree:

        geo = tree.ig
        
        va = V4.Input(tree, "From")
        vb = V4.Input(tree, "To")
        
        # ===== Geometry position
        
        with tree.layout("All points rotation"):
            node = g_maths.align_vector(*V4.Position(geo).args, *va.args, *vb.args)
            V4.NodeOutput(node).set_position(geo)
            
        # ===== Normals and tangents
            
        comps = geo.separate_components()
        
        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances
        
        # ----- Mesh
        
        with tree.layout("Mesh"):
            for s in ["A", "B"]:
                node = g_maths.align_vector(*V4.Normal(mesh, s).args, *va.args, *vb.args)
                V4.NodeOutput(node).set_normal(mesh, s)
            
        # ----- Curve
        
        with tree.layout("Curve"):
            node = g_maths.align_vector(*V4.Tangent(curve).args, *va.args, *vb.args)
            V4.NodeOutput(node).set_tangent(curve)

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


                
        
            
            
            
    


    
        
    
    
    

        


        

