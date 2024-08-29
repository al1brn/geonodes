#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/03/04

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : demos/fourd
--------------------
Generates the fourd engine modifiers

Geometry Nodes
--------------
    -

updates
-------
- creation : 2024/03/04
- update   : 2024/08/07
"""


import bpy

from ..geonodes import *
from .. import shadernodes as sh

from .. import utils

# ----- Prefixes

maths_  = "M"
mods_   = "4D"
curves_ = "C"
surfs_  = "S"

gmaths = GroupF(maths_)
gmods  = GroupF(mods_)

ZERO = 0.0001

V4_COL = (.3, .1, .1)

# =============================================================================================================================
# Build the 4D engine

def demo(clear=False):

    print("-"*100)
    print("Build 4D Engine")
    print()

    Tree._reset_counters()
    build_shaders()
    print(f"4D shaders built : {Tree._total_nodes} nodes, {Tree._total_links} links")
    print()

    Tree._reset_counters()

    build_matrices()
    build_base()
    build_vectors()
    build_transformations()
    build_extrusions()
    build_lights()
    build_curves()
    build_surfaces()
    show_case()

    print(f"4D Engine built : {Tree._total_nodes} nodes, {Tree._total_links} links")
    print()

# =============================================================================================================================
# Shaders
# =============================================================================================================================

def build_shaders():

    # ----------------------------------------------------------------------------------------------------
    # Axis Shader

    with sh.ShaderNodes("4 Axis"):

        col = sh.nd.attribute(attribute_name="Axis Color").color

        ped = sh.Shader.Principled(base_color=col, roughness=.1, metallic=.3)

        ped.out()

    # ----------------------------------------------------------------------------------------------------
    # Face default

    with sh.ShaderNodes("4 Face"):

        noise = Texture.Noise(scale=5.)
        bump = sh.nd.bump(height=noise.color, strength=.1)

        ped = sh.Shader.Principled(
            base_color = (.3, .8, .7),
            metallic   = 0.,
            roughness  = 0.,
            alpha      = .1,
            normal     = bump,
            )

        ped.out()


    # ----------------------------------------------------------------------------------------------------
    # Edge default

    with sh.ShaderNodes("4 Edge"):

        ped = sh.Shader.Principled(
            base_color = (0., .05, .9),
            roughness  = 0.,
            )

        ped.out()

# =============================================================================================================================
# A 4-vector is a couple (V: Vector, w: float)
# =============================================================================================================================

class V4:
    def __init__(self, V=None, w=None, name=None, tip=None):
        if V is None and w is None or name is not None:
            if name is None or name == '':
                self.V = Vector(V, "V", tip=tip)
                self.w = Float(w, "w", tip=tip)
            else:
                self.V = Vector(V, f"{name} V", tip=tip)
                self.w = Float(w, f"{name} w", tip=tip)
        else:
            self.V = Vector(V)
            self.w = Float(w)

    # ----------------------------------------------------------------------------------------------------
    # X, y, z, w

    @classmethod
    def Xyzw(cls, x, y, z, w):
        return cls(Vector((x, y, z)), w)

    @property
    def x(self):
        return self.V.x

    @property
    def y(self):
        return self.V.y

    @property
    def z(self):
        return self.V.z

    # ----------------------------------------------------------------------------------------------------
    # Tree input / output

    def out(self, name=None):
        name = "" if name is None or name == "" else name + " "
        self.V.out(name + "V")
        self.w.out(name + "w")

    # ----------------------------------------------------------------------------------------------------
    # Node input / output

    @classmethod
    def FromNode(cls, node, name=None):
        name = "" if name is None or name == "" else utils.socket_name(name) + "_"
        return cls(getattr(node, name + "v"), getattr(node, name + "w"))

    def sockets(self, name=None):
        name = "" if name is None or name == "" else name + " "
        return {name + "V": self.V, name + "w": self.w}

    @property
    def args(self):
        return (self.V, self.w)

    def kwargs(self, name=None):
        name = "" if name is None or name == "" else utils.socket_name(name) + "_"
        return {name + "v": self.V, name + "w": self.w}

    # ----------------------------------------------------------------------------------------------------
    # From / to position

    @classmethod
    def Position(cls, geo, sample_index=None):
        with Layout("Get Position V4", V4_COL):
            if sample_index is None:
                return cls(nd.position, Float.Named("w"))
            else:
                return cls(
                    geo.points.sample_index(nd.position,      index=sample_index),
                    geo.points.sample_index( Float.Named("w"), index=sample_index))

    def set_position(self, geo):
        # Need to sample w before setting the position because w can be computed
        # from the position (for instance after a rotation)
        # Changing the position would change w before it is written

        geo = Mesh(geo)

        with Layout("Set Position V4", V4_COL):
            w = geo.points.sample_index(self.w, index=nd.index)
            geo.points.position = self.V
            return geo.points.store("w", w)

    def set_offset(self, geo):
        with Layout("Set Offset V4", V4_COL):
            w = geo.points.sample_index(self.w, index=nd.index)
            geo = geo.set_position(offset=self.V)
            return Mesh(geo).points.store("w", w + Float.Named("w"))

    # ----------------------------------------------------------------------------------------------------
    # From / to face normal

    @classmethod
    def Normal(cls, geo, suffix, sample_index=None):
        with Layout("Get Normal", V4_COL):
            if sample_index is None:
                return cls(Vector.Named(f"N{suffix}V"), Float.Named(f"N{suffix}w"))
            else:
                return cls(
                    geo.faces.sample_index(Vector.Named(f"N{suffix}V"), index=sample_index),
                    geo.faces.sample_index(Float.Named( f"N{suffix}w"), index=sample_index))

    def set_normal(self, geo, suffix):
        with Layout("Set Normal", V4_COL):
            w = geo.faces.sample_index(self.w, index=nd.index)
            geo.faces.store(f"N{suffix}V", self.V)
            return geo.faces.store(f"N{suffix}w", w)

    # ----------------------------------------------------------------------------------------------------
    # From / to curve tangent

    @classmethod
    def Tangent(cls, geo, sample_index=None):

        # ----- Does the tangent exist ?

        with Layout("Get Tangent", V4_COL):
            if sample_index is None:
                return cls(Vector.Named("TV"), Float.Named("Tw"))
            else:
                return cls(
                    geo.points.sample_index(Vector.Named("TV"), index=sample_index),
                    geo.points.sample_index(Float.Named( "Tw"), index=sample_index))

    def set_tangent(self, geo):
        with Layout("Set Tangent", V4_COL):
            w = geo.points.sample_index(self.w, index=nd.index)
            geo.points.store("TV", self.V)
            return geo.points.store( "Tw", w)

    # ----------------------------------------------------------------------------------------------------
    # Operations

    def __neg__(self):
        with Layout("-V4", V4_COL):
            return cls(-self.V, -self.w)

    def __add__(self, other):
        with Layout("V4 Add", V4_COL):
            return V4(self.V + other.V, self.w + other.w)

    def __iadd__(self, other):
        with Layout("V4 Add", V4_COL):
            self.V += other.V
            self.w += other.w
            return self

    def __sub__(self, other):
        with Layout("V4 Sub", V4_COL):
            return V4(self.V - other.V, self.w - other.w)

    def __isub__(self, other):
        with Layout("V4 Sub", V4_COL):
            self.V -= other.V
            self.w -= other.w
            return self

    def __mul__(self, other):
        with Layout("V4 Mul", V4_COL):
            if isinstance(other, V4):
                return V4(self.V*other.V, self.w*other.w)
            else:
                return V4(self.V*other, self.w*other)

    def __imul__(self, other):
        with Layout("V4 Mul", V4_COL):
            if isinstance(other, V4):
                self.V *= other.V
                self.w *= other.w
            else:
                self.V *= other
                self.w *= other
            return self

    def __truediv__(self, other):
        with Layout("V4 Div", V4_COL):
            if isinstance(other, V4):
                return V4(self.V/other.V, self.w/other.w)
            else:
                return V4(self.V/other, self.w/other)

    def __itruediv__(self, other):
        with Layout("V4 Div", V4_COL):
            if isinstance(other, V4):
                self.V /= other.V
                self.w /= other.w
            else:
                self.V /= other
                self.w /= other
            return self

    def dot(self, other):
        with Layout("Dot 4", V4_COL):
            return self.V.dot(other.V) + self.w*other.w

    @property
    def length(self):
        with Layout("V4 Length", V4_COL):
            return gnmath.sqrt(self.V.dot(self.V) + self.w*self.w)

    def normalized(self, return_error=False):
        with Layout("V4 Normalized", V4_COL):
            n = self.length
            err = n.less_than(ZERO)
            v4 = V4((self.V/n).switch(err, self.V), (self.w/n).switch(err, self.w))
            if return_error:
                return v4, err
            else:
                return v4

    def mat_dot(self, M):
        with Layout("Mat (4x4) @ V4", V4_COL):

            v0 = V4.FromNode(M, "R 0")
            v1 = V4.FromNode(M, "R 1")
            v2 = V4.FromNode(M, "R 2")
            v3 = V4.FromNode(M, "R 3")

            return V4.Xyzw(
                v0.x*self.x + v0.y*self.y + v0.z*self.z + v0.w*self.w,
                v1.x*self.x + v1.y*self.y + v1.z*self.z + v1.w*self.w,
                v2.x*self.x + v2.y*self.y + v2.z*self.z + v2.w*self.w,
                v3.x*self.x + v3.y*self.y + v3.z*self.z + v3.w*self.w)

    def switch(self, b, other):
        with Layout("Switch V4", V4_COL):
            return V4(self.V.switch(b, other.V), self.w.switch(b, other.w))

    def angle_with(self, other):
        with Layout("V4 Angle", V4_COL):
            a = self.normalized()
            b = other.normalized()

            return gnmath.acos(a.dot(b))

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

    def get_empty(name):
        obj = bpy.data.objects.get(name)
        if obj is not None:
            return obj

        empty = bpy.data.objects.new(name=name, object_data=None)
        bpy.context.collection.objects.link(empty)

        return empty

    get_empty("Projection")
    get_empty("Projection2")

    # ----------------------------------------------------------------------------------------------------
    # Matrices multiplication

    with GeoNodes("Mat Mult", is_group=True, fake_user=False, prefix=maths_):

        A = [V4(None, None, f"A {i}") for i in range(4)]
        B = [V4(None, None, f"B {i}") for i in range(4)]

        C = [V4.Xyzw(B[0].x, B[1].x, B[2].x, B[3].x),
             V4.Xyzw(B[0].y, B[1].y, B[2].y, B[3].y),
             V4.Xyzw(B[0].z, B[1].z, B[2].z, B[3].z),
             V4.Xyzw(B[0].w, B[1].w, B[2].w, B[3].w)]

        for i in range(4):
            with Layout(f"Line {i}"):
                V4.Xyzw(A[i].dot(C[0]), A[i].dot(C[1]), A[i].dot(C[2]), A[i].dot(C[3])).out(f"R {i}")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - XW / YZ rotations

    with GeoNodes("XW Rotation", is_group=True, fake_user=False, prefix=maths_):

        ag = Float.Angle(0, "Angle")
        ca = gnmath.cos(ag)
        sa = gnmath.sin(ag)

        a2 = Float(0, "Second")
        c2 = gnmath.cos(a2)
        s2 = gnmath.sin(a2)

        V4.Xyzw(ca,  0,   0, -sa).out("R 0")
        V4.Xyzw( 0, c2, -s2,   0).out("R 1")
        V4.Xyzw( 0, s2,  c2,   0).out("R 2")
        V4.Xyzw(sa,  0,   0,  ca).out("R 3")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - YW / ZX rotations

    with GeoNodes("YW Rotation", is_group=True, fake_user=False, prefix=maths_):

        ag = Float.Angle(0, "Angle")
        ca = gnmath.cos(ag)
        sa = gnmath.sin(ag)

        a2 = Float.Angle(0, "Second")
        c2 = gnmath.cos(a2)
        s2 = gnmath.sin(a2)

        V4.Xyzw(  c2,  0, s2,   0).out("R 0")
        V4.Xyzw(   0, ca,  0,  sa).out("R 1")
        V4.Xyzw( -s2,  0, c2,   0).out("R 2")
        V4.Xyzw(   0,-sa,  0,  ca).out("R 3")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - ZW / XY rotations

    with GeoNodes("ZW Rotation", is_group=True, fake_user=False, prefix=maths_):

        ag = Float.Angle(0, "Angle")
        ca = gnmath.cos(ag)
        sa = gnmath.sin(ag)

        a2 = Float.Angle(0, "Second")
        c2 = gnmath.cos(a2)
        s2 = gnmath.sin(a2)

        V4.Xyzw( c2, -s2,  0,   0).out("R 0")
        V4.Xyzw( s2,  c2,  0,   0).out("R 1")
        V4.Xyzw(  0,   0, ca, -sa).out("R 2")
        V4.Xyzw(  0,   0, sa,  ca).out("R 3")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Projection matrix

    with GeoNodes("Projection Matrix", is_group=True, fake_user=False, prefix=maths_):

        abc = Object.Info("Projection").rotation
        a = abc.x
        b = abc.y
        c = abc.z

        second = Object.Info("Projection2").rotation
        a2 = second.x
        b2 = second.y
        c2 = second.z

        if True:
            M0 = gmaths.xw_rotation(angle=a, second=a2)
            M1 = gmaths.yw_rotation(angle=b, second=b2)
            M2 = gmaths.zw_rotation(angle=c, second=c2)
        else:
            M0 = Group.Prefix(maths_, "XW Rotation", {'Angle': a, 'Second': a2})
            M1 = Group.Prefix(maths_, "YW Rotation", {'Angle': b, 'Second': b2})
            M2 = Group.Prefix(maths_, "ZW Rotation", {'Angle': c, 'Second': c2})


        if True:
            M_ = gmaths.mat_mult([
                M0.r_0_v, M0.r_0_w, M0.r_1_v, M0.r_1_w, M0.r_2_v, M0.r_2_w, M0.r_3_v, M0.r_3_w,
                M1.r_0_v, M1.r_0_w, M1.r_1_v, M1.r_1_w, M1.r_2_v, M1.r_2_w, M1.r_3_v, M1.r_3_w,
                ])

            M_ = gmaths.mat_mult([
                M_.r_0_v, M_.r_0_w, M_.r_1_v, M_.r_1_w, M_.r_2_v, M_.r_2_w, M_.r_3_v, M_.r_3_w,
                M2.r_0_v, M2.r_0_w, M2.r_1_v, M2.r_1_w, M2.r_2_v, M2.r_2_w, M2.r_3_v, M2.r_3_w,
                ])

        else:
            M_ = Group.Prefix(maths_, "Mat Mult", [
                M0.r_0_v, M0.r_0_w, M0.r_1_v, M0.r_1_w, M0.r_2_v, M0.r_2_w, M0.r_3_v, M0.r_3_w,
                M1.r_0_v, M1.r_0_w, M1.r_1_v, M1.r_1_w, M1.r_2_v, M1.r_2_w, M1.r_3_v, M1.r_3_w,
                ])

            M_ = Group.Prefix(maths_, "Mat Mult", [
                M_.r_0_v, M_.r_0_w, M_.r_1_v, M_.r_1_w, M_.r_2_v, M_.r_2_w, M_.r_3_v, M_.r_3_w,
                M2.r_0_v, M2.r_0_w, M2.r_1_v, M2.r_1_w, M2.r_2_v, M2.r_2_w, M2.r_3_v, M2.r_3_w,
                ])

        V4.FromNode(M_, "R 0").out("R 0")
        V4.FromNode(M_, "R 1").out("R 1")
        V4.FromNode(M_, "R 2").out("R 2")
        V4.FromNode(M_, "R 3").out("R 3")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Perform a projection

    with GeoNodes("Projection", is_group=True, fake_user=False, prefix=maths_):

        v = V4()

        if True:
            v.mat_dot(gmaths.projection_matrix()).out()
        else:
            v.mat_dot(Group.Prefix(maths_, "Projection Matrix")).out()

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

    with GeoNodes("Plunge 3D Geometry", fake_user=False, prefix=mods_):

        geo = Geometry()
        w   = Float(0, "w")

        # ----- The fourth dimention

        geo = Mesh(geo).points.store("w", w)

        # ----- Normals and tangent

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ---- Mesh normals

        V4(nd.normal,  0.).set_normal(mesh, "A")
        V4(0, 1.).set_normal(mesh, "B")

        # ---- Curve tangents

        curve = V4(curve.tangent,  0.).set_tangent(curve)

        # ---- Result

        mesh.join(curve, cloud, inst).out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Arrow

    with GeoNodes("Arrow", fake_user=False, prefix=mods_):

        v0     = V4(0, 0, "Start")
        v1     = V4(0, 0, "End")

        radius = Float(   .05, "Radius", 0.01)
        resol  = Integer( 8, "Resolution", 3, 32)
        mat    = Material("4 Axis", "Material")

        with Layout("Dimensions"):
            vec4 = (v1 - v0)
            length = gnmath.sqrt(vec4.dot(vec4))
            cone_height = 9*radius

            scale = length/(length + cone_height)

            length *= scale
            cone_height *= scale

            v1 = V4(v0.V + vec4.V.scale(scale), v0.w + vec4.w*scale)

        with Layout("Arrow shaft"):

            # ----- Start and end point

            if True:
                p0 = gmaths.projection(v0.sockets())._out
                p1 = gmaths.projection(v1.sockets())._out
            else:
                p0 = Group.Prefix(maths_, "Projection", v0.sockets())._out
                p1 = Group.Prefix(maths_, "Projection", v1.sockets())._out

            # ----- Arrow shaft

            line = Curve.Line(start=p0, end=p1)

            mesh = line.to_mesh(profile_curve=Curve.Circle(radius=radius, resolution=resol), fill_caps=True)

        with Layout("Arrow head"):

            cone = Mesh.Cone(vertices=resol, depth=cone_height, radius_bottom=3.5*radius)

            rot = Rotation.AlignZToVector(p1 - p0)
            cone = cone.transform(translation=p1, rotation=rot)

            mesh += cone

        mesh.faces.material = mat
        mesh.faces.smooth = True

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - The four Axis

    with GeoNodes("Axis Viewer", fake_user=False, prefix=mods_):

        neg    = Float(-1, "Negative", max=0)
        pos    = Float(3,  "Positive", 0)
        radius = Float(0.05, "Radius")
        resol  = Integer(12, "Resolution", 3, 32)

        # ----- Loop on the axis

        for i in range(4):

            if True:
                node = gmods.arrow({
                    'Start V' : [(neg, 0, 0), (0, neg, 0), (0, 0, neg), (0, 0, 0)][i],
                    'Start w' : [0, 0, 0, neg][i],
                    'End V'   : [(pos, 0, 0), (0, pos, 0), (0, 0, pos), (0, 0, 0)][i],
                    'End w'   : [0, 0, 0, pos][i],
                })
            else:
                node = Group.Prefix(mods_, "Arrow", {
                    'Start V' : [(neg, 0, 0), (0, neg, 0), (0, 0, neg), (0, 0, 0)][i],
                    'Start w' : [0, 0, 0, neg][i],
                    'End V'   : [(pos, 0, 0), (0, pos, 0), (0, 0, pos), (0, 0, 0)][i],
                    'End w'   : [0, 0, 0, pos][i],
                })

            node.plug_node_into()
            arrow = Mesh(node._out)

            arrow.faces.store("Axis Color", [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)][i])

            if i == 0:
                axis = arrow
            else:
                axis += arrow

        axis.faces.material = "4 Axis"

        axis.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Perform a projection

    with GeoNodes("Projection", fake_user=False, prefix=mods_):

        geo          = Geometry()
        shade_smooth = Boolean(True, "Shade smooth")

        # ===== Points projection

        with Layout("All points projection"):
            v = V4.Position(geo)
            #v = maths_.projection(*v.args).v
            if True:
                v = gmaths.projection(v.sockets())._out
            else:
                v = Group.Prefix(maths_, "Projection", v.sockets())._out
            geo.position = v

        # ===== Components

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- Back face computation

        with Layout("Mesh projection"):

            if True:
                m_proj = gmaths.projection_matrix()
            else:
                m_proj = Group.Prefix(maths_, "Projection Matrix")
            v_proj = V4.FromNode(m_proj, "R 3")

            back = Boolean(True)
            for sn in ["A", "B"]:
                n = V4.Normal(mesh, sn)
                dot = v_proj.dot(n)
                #back *= dot.less_than(0)
                back &= dot.less_than(0)

            # NOTE : Storing the back flag on POINT smoothes the transition
            mesh.points.store("Back", back)

            mesh.faces.smooth = shade_smooth

        mesh.join(curve, cloud, inst).out()


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

    with GeoNodes("Normalize 2-Basis", is_group=True, fake_user=False, prefix=maths_):

        u0 = V4(0, 0, "I")
        u1 = V4(0, 0, "J")

        # We suppress from u1 the u0 component

        u1 -= u0*u1.dot(u0)

        # Normalized

        u0.normalized(False).out("I")
        u1.normalized(False).out("J")


    # ----------------------------------------------------------------------------------------------------
    # GROUP - Normal basis
    # 3 vectors forming a normal basis to a 3D hyperplane defined by three independant vectors

    with GeoNodes("Normalize 3-Basis", is_group=True, fake_user=False, prefix=maths_):

        u0 = V4((1, 0, 0), 0, "I")
        u1 = V4((0, 1, 0), 0, "J")
        u2 = V4((0, 0, 1), 0, "K")

        # ----- Let's normalize the first vector

        e0, err = u0.normalized(True)

        # Let's suppress this dimension in the second one

        with Layout("Make the second vector perp to the first"):

            # u1 minus e0 part

            d = e0.dot(u1)
            u1 -= e0*d

            # Let's normalize

            e1, er = u1.normalized(True)
            err |= er

        with Layout("Make the third vector perp to the two other ones"):

            # u2 minus e0 and e1 part

            d = e0.dot(u2)
            u2 -= e0*d

            d = e1.dot(u2)
            u2 -= e1*d

            # Let's normalize

            e2, er = u2.normalized(True)
            err |= er

        # ----- We are done :-)

        e0.out("I")
        e1.out("J")
        e2.out("K")

        err.out("Error")


    # ----------------------------------------------------------------------------------------------------
    # GROUP - Cross
    # A vector peprpendicular to three independant vectors

    with GeoNodes("Cross", is_group=True, fake_user=False, prefix=maths_):

        u0 = V4((1, 0, 0), 0, "I")
        u1 = V4((0, 1, 0), 0, "J")
        u2 = V4((0, 0, 1), 0, "K")

        # ----- Convert the three input vectors in a normal basis

        #node = maths_.normalize_3_basis()
        #tree.input_node.plug_to(node)
        node = Group.Prefix(maths_, "Normalize 3-Basis")
        node.plug_node_into()

        u0 = V4.FromNode(node, "I")
        u1 = V4.FromNode(node, "J")
        u2 = V4.FromNode(node, "K")

        error = node.error

        n3 = Float()
        u3 = V4(0, 0)
        for i in range(4):
            with Layout(f"Axis {i}"):

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

                #greater = n.greater_than(n3)
                greater = n > n3
                u3 = u3.switch(greater, u)
                n3 = n3.switch(greater, n)

        # ----- Let's normalize the result

        u3 = u3.normalized()

        u3.out()
        error.out("Error")


    # ----------------------------------------------------------------------------------------------------
    # GROUP - Compute three vectors perpendicular to a vector

    with GeoNodes("Hyperplane", is_group=True, fake_user=False, prefix=maths_):

        v = V4(0, 0, "")

        # ----- Normalize the entry

        v = v.normalized()

        # ----- Try to build a 3D-base with v and plane (k, l)

        #node = maths_.normalize_3_basis(*v.args, (0., 0., 1.), 0., (0., 0., 0.), 1.)
        node = Group.Prefix(maths_, "Normalize 3-Basis", [v.V, v.w, (0., 0., 1.), 0., (0., 0., 0.), 1.])

        u0 = V4.FromNode(node, "J")
        u1 = V4.FromNode(node, "K")

        error = node.error

        # ---------------------------------------------------------------------------
        # If error, it does mean that v is in plane (k, l), hence (i, j) is perp to v

        #node = maths_.cross(*v.args, (1., 0., 0.), 0., (0., 1., 0.), 0.)
        node = Group.Prefix(maths_, "Cross", [v.V, v.w, (1., 0., 0.), 0., (0., 1., 0.), 0.])

        e_u2 = V4.FromNode(node)

        # ---------------------------------------------------------------------------
        # If no error, we have (u0, u1) perp to input vector
        # The third basis vector is perpendicular to these 3 vectors

        #node = maths_.cross(*v.args, *u0.args, *u1.args)
        node = Group.Prefix(maths_, "Cross", [v.V, v.w, u0.V, u0.w, u1.V, u1.w])
        u2 = V4.FromNode(node)

        u0 = u0.switch(error, V4((1., 0., 0.), 0.))
        u1 = u1.switch(error, V4((0., 1., 0.), 0.))
        u2 = u2.switch(error, e_u2)

        # ----- Done

        u0.out("I")
        u1.out("J")
        u2.out("K")
        v.out("L")

    # ----------------------------------------------------------------------------------------------------
    # Resolution system de deux équations à deux inconnues
    # a0x + b0y = c0
    # a1x + b1y = c1
    #
    # D = a0b1 - a1b0
    # x = (b1c0 - b0c1)/D
    # y = (a0c1 - a1c0)/D

    with GeoNodes("Two equations solver", is_group=True, prefix=maths_):

        a0 = Float(0, "a0")
        b0 = Float(0, "b0")
        c0 = Float(0, "c0")

        a1 = Float(0, "a1")
        b1 = Float(0, "b1")
        c1 = Float(0, "c1")

        with Layout("Discriminant"):
         D = a0*b1 - a1*b0

        with Layout("x"):
            x = (b1*c0 - b0*c1)/D
            x.out("x")

        with Layout("y"):
            y = (a0*c1 - b1*c0)/D
            y.out("y")

        #tree.abs(D).less_than(0.001).to_output("Error")
        (abs(D) < 0.001).out("Error")
        Vector((x, y, 0)).length.out("Length")

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

    with GeoNodes("Translation", fake_user=False, prefix=mods_):

        geo = Geometry()

        v = V4(0, 0, "")

        geo = Mesh(geo.transform(translation=v.V))
        geo.points.store("w", Float.Named("w") + v.w)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Scale

    with GeoNodes("Scale", fake_user=False, prefix=mods_):

        geo = Geometry()

        scale = V4((1., 1., 1.), 1., "Scale")

        geo = Mesh(geo.transform(scale=scale.V))
        geo.points.store("w", Float.Named("w")*scale.w)

        # ===== Normals and tangents

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- Mesh

        with Layout("Mesh"):

            n = V4.Normal(mesh, "A")*scale
            n.normalized().set_normal(mesh, "A")

            n = V4.Normal(mesh, "B")*scale
            n.normalized().set_normal(mesh, "B")

        # ----- Curve

        """
        with Layout("Curve"):

            t = V4.Tangent(curve)*scale
            t.normalized().set_tangent(curve)
        """

        mesh.join(curve, cloud, inst).out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation 4D

    with GeoNodes("Rotation 4D", is_group=True, fake_user=False, prefix=maths_):

        v = V4(0, 0, "")

        xy = Float.Angle(0, "XY", tip="Rotation (XY,ZW) : X -> Y")
        zw = Float.Angle(0, "ZW", tip="Rotation (XY,ZW) : Z -> W")

        yz = Float.Angle(0, "YZ", tip="Rotation (YZ,ZW) : Y -> Z")
        xw = Float.Angle(0, "XW", tip="Rotation (YZ,ZW) : X -> W")

        zx = Float.Angle(0, "ZX", tip="Rotation (ZX,YW) : Z -> X")
        yw = Float.Angle(0, "YW", tip="Rotation (ZX,YW) : Y -> W")

        # ----- Rotation xy / zw

        with Layout("Angles XY ZW"):
            ca, sa = gnmath.cos(xy), gnmath.sin(xy)
            cb, sb = gnmath.cos(zw), gnmath.sin(zw)
            A0 = V4.Xyzw( ca, -sa,  0.,  0.)
            A1 = V4.Xyzw( sa,  ca,  0.,  0.)
            A2 = V4.Xyzw( 0.,  0.,  cb, -sb)
            A3 = V4.Xyzw( 0.,  0.,  sb,  cb)

        # ----- Rotation xz / yw

        with Layout("Angles ZX YW"):
            ca, sa = gnmath.cos(zx), gnmath.sin(zx)
            cb, sb = gnmath.cos(yw), gnmath.sin(yw)
            B0 = V4.Xyzw( ca,  0.,  sa,  0.)
            B1 = V4.Xyzw( 0.,  cb,  0., -sb)
            B2 = V4.Xyzw(-sa,  0.,  ca,  0.)
            B3 = V4.Xyzw( 0.,  sb,  0.,  cb)

        # ----- Rotation xw / yz

        with Layout("Angles XW YZ"):
            ca, sa = gnmath.cos(xw), gnmath.sin(xw)
            cb, sb = gnmath.cos(yz), gnmath.sin(yz)
            C0 = V4.Xyzw( ca,  0.,   0., -sa)
            C1 = V4.Xyzw( 0.,  cb, -sb,  0.)
            C2 = V4.Xyzw( 0.,  sb,  cb,  0.)
            C3 = V4.Xyzw( sa,  0.,   0.,  ca)

        # ----- Multiply the matrices

        #node = maths_.mat_mult(*A0.args, *A1.args, *A2.args, *A3.args, *B0.args, *B1.args, *B2.args, *B3.args)
        node = Group.Prefix(maths_, "Mat Mult", [
            A0.V, A0.w, A1.V, A1.w, A2.V, A2.w, A3.V, A3.w,
            B0.V, B0.w, B1.V, B1.w, B2.V, B2.w, B3.V, B3.w,
        ])

        M0 = V4.FromNode(node, "R 0")
        M1 = V4.FromNode(node, "R 1")
        M2 = V4.FromNode(node, "R 2")
        M3 = V4.FromNode(node, "R 3")

        #node = maths_.mat_mult(*M0.args, *M1.args, *M2.args, *M3.args, *C0.args, *C1.args, *C2.args, *C3.args)
        node = Group.Prefix(maths_, "Mat Mult", [
            M0.V, M0.w, M1.V, M1.w, M2.V, M2.w, M3.V, M3.w,
            C0.V, C0.w, C1.V, C1.w, C2.V, C2.w, C3.V, C3.w,
        ])

        # ----- Rotate the vector

        v.mat_dot(node).out()

    # ----------------------------------------------------------------------------------------------------
    # Modifier - Rotation 4D

    with GeoNodes("Rotation 4D", fake_user=False, prefix=mods_):

        geo = Geometry()

        xy = Float.Angle(0, "XY", tip="Rotation (XY,ZW) : X -> Y")
        zw = Float.Angle(0, "ZW", tip="Rotation (XY,ZW) : Z -> W")

        yz = Float.Angle(0, "YZ", tip="Rotation (YZ,ZW) : Y -> Z")
        xw = Float.Angle(0, "XW", tip="Rotation (YZ,ZW) : X -> W")

        zx = Float.Angle(0, "ZX", tip="Rotation (ZX,YW) : Z -> X")
        yw = Float.Angle(0, "YW", tip="Rotation (ZX,YW) : Y -> W")

        # ===== Geometry position

        with Layout("All points rotation"):

            #node = maths_.rotation_4d(**V4.Position(geo).kwargs())
            #tree.input_node.plug_to(node)
            node = Group.Prefix(maths_, "Rotation 4D", V4.Position(geo).sockets())
            node.plug_node_into()

            geo = V4.FromNode(node).set_position(geo)

        # ===== Normals and tangents

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- Mesh

        for s in ["A","B"]:
            with Layout(f"Normal {s}"):
                #node = maths_.rotation_4d(**V4.Normal(mesh, s).kwargs())
                #tree.input_node.plug_to(node)
                #V4.NodeOutput(node).set_normal(mesh, s)

                node = Group.Prefix(maths_, "Rotation 4D", V4.Normal(mesh, s).sockets())
                node.plug_node_into()
                V4.FromNode(node).set_normal(mesh, s)

        # ----- Curve
        """

        with Layout("Curve"):

            node = maths_.rotation_4d(**V4.Tangent(curve).kwargs())
            tree.input_node.plug_to(node)
            V4.NodeOutput(node).set_tangent(curve)
        """

        mesh.join(curve, cloud, inst).out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation in a plane defined by two 4D vectors

    with GeoNodes("Rotation 2D", is_group=True, fake_user=False, prefix=maths_):

        v  = V4(0, 0, "")

        I  = V4((1, 0, 0), 0, "I")
        J  = V4((0, 1, 0), 0, "J")
        ag = Float.Angle(0, "Angle", tip="Rotation angle in plane (I, J)")

        # ---------------------------------------------------------------------------
        # Decompose the vector along I, J and remainder

        with Layout("Decompose I, J, Remainder"):
            x  = I.dot(v)
            y  = J.dot(v)
            v_ = v - I*x - J*y

        # ---------------------------------------------------------------------------
        # Rotate x, y

        with Layout("Rotation 2D"):

            ca, sa = gnmath.cos(ag), gnmath.sin(ag)
            x_ = x*ca - y*sa
            y_ = x*sa + y*ca

        # ---------------------------------------------------------------------------
        # Recompose the vector

        with Layout("Recompose"):

            r = v_ + I*x_ + J*y_

        r.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Rotation in a plane defined by two 4D vectors

    with GeoNodes("Rotation 2D", fake_user=False, prefix=mods_):

        geo = Geometry

        v0  = V4((1, 0, 0), 0, "I")
        v1  = V4((0, 1, 0), 0, "J")
        ag = Float.Angle(0, "Angle", tip="Rotation angle in plane (I, J)")

        # ===== Normal 2-Basis

        with Layout("Normal 2-Basis"):
            #node = maths_.normalize_2_basis(*I.args, *J.args)
            node = Group.Prefix(maths_, "Normalize 2-Basis",[I.V, I.w, J.V, J.w])
            I = V4.FromNode(node, "I")
            J = V4.FromNode(node, "J")

        # ===== Geometry position

        with Layout("All points rotation"):
            #node = maths_.rotation_2d(*V4.Position(geo).args, *I.args, *J.args, angle=ag)
            pos = V4.Position(geo)
            node = Group.Prefix(maths_, "Rotation 2D",[pos.V, pos.w, I.V, I.w, J.V, J.w, ag])
            geo = V4.FromNode(node).set_position(geo)

        # ===== Normals and tangents

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- Mesh

        with Layout("Mesh"):
            for s in ["A", "B"]:
                #node = maths_.rotation_2d(*V4.Normal(mesh, s).args, *I.args, *J.args, angle=ag)
                nrm = V4.Normal(mesh, s)
                node = Group.Prefix(maths_, "Rotation 2D", [nrm.V, nrm.w, I.V, I.w, J.V, J.w, ag])

                V4.FromNode(node).set_normal(mesh, s)

        # ----- Curve

        """

        with Layout("Curve"):
            node = maths_.rotation_2d(*V4.Tangent(curve).args, *I.args, *J.args, angle=ag)
            V4.NodeOutput(node).set_tangent(curve)
        """

        mesh.join(curve, cloud, inst).out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Follow a vector
    #
    # Rotate a vector such as the vector A rotates to vector B

    with GeoNodes("Align Vector", is_group=True, fake_user=False, prefix=maths_):

        v = V4(0, 0, "")

        va = V4(0, 0, "From")
        vb = V4(0, 0, "To")

        # ----- Normal 2-Basis

        with Layout("Normal 2-Basis"):
            #node = maths_.normalize_2_basis(*va.args, *vb.args)
            node = Group.Prefix(maths_, "Normalize 2-Basis", [va.V, va.w, vb.V, vb.w])
            I = V4.FromNode(node, "I")
            J = V4.FromNode(node, "J")

        # ----- Angle between the two vectors

        ag = va.angle_with(vb)

        # ----- Rotate in the plane I, J

        #node = maths_.rotation_2D(*v.args, *I.args, *J.args, angle=ag)
        node = Group.Prefix(maths_, "Rotation 2D", [v.V, v.w, I.V, I.w, J.V, J.w, ag])

        V4.FromNode(node).out()


    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Follow a vector
    #
    # Rotate a vector such as the vector A rotates to vector B

    with GeoNodes("Align Vector", fake_user=False, prefix=mods_):

        geo = Geometry

        va = V4(0, 0, "From")
        vb = V4(0, 0, "To")

        # ===== Geometry position

        with Layout("All points rotation"):
            #node = maths_.align_vector(*V4.Position(geo).args, *va.args, *vb.args)
            pos = V4.Position(geo)
            node = Group.Prefix(maths_, "Align Vector", [pos.V, pos.w, va.V, va.w, vb.V, vb.w])
            geo = V4.FromNode(node).set_position(geo)

        # ===== Normals and tangents

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- Mesh

        with Layout("Mesh"):
            for s in ["A", "B"]:
                #node = maths_.align_vector(*V4.Normal(mesh, s).args, *va.args, *vb.args)
                nrm = V4.Normal(mesh, s)
                node = Group.Prefix(maths_, "Align Vector", [nrm.V, nrm.w, va.V, va.w, vb.V, vb.w])
                V4.FromNode(node).set_normal(mesh, s)

        # ----- Curve

        """
        with Layout("Curve"):
            node = maths_.align_vector(*V4.Tangent(curve).args, *va.args, *vb.args)
            V4.NodeOutput(node).set_tangent(curve)
        """

        mesh.join(curve, cloud, inst).out()

def build_extrusions():

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Compute curve tangent

    with GeoNodes("Compute Tangents", is_group=True, fake_user=False, prefix=maths_):

        curve = Curve()

        count = curve.points.count
        count1 = count-1
        dt = .25/count1

        # ------ Tangent computation script

        def compute(fac0, fac1, title="Compute tangent: normalized(V4(t + dt) - V4(t - dt)"):
            with Layout(title):
                val0 = curve.sample(Float.Named("w"), factor=fac0)
                val1 = curve.sample(Float.Named("w"), factor=fac1)
                return (V4(val1.position_, val1) - V4(val0.position_, val0)).normalized()

        # ------ All points

        curve = compute((nd.index/(count1) - dt) % 1.0001, (nd.index/(count1) + dt) % 1.0001).set_tangent(curve)

        cyclic_curve = Curve(curve)

        # ------ First and, last if not cyclic

        tg = compute(0, dt, "First tangent")
        with Layout("Set first"):
            sel = nd.index == 0
            curve.points[sel].store("TV", tg.V)
            curve.points[sel].store("Tw",  tg.w)

        tg = compute(1-dt, 1, "Last tagent")
        with Layout("Set last"):
            sel = nd.index == count1
            curve.points[sel].store("TV", tg.V)
            curve.points[sel].store("Tw", tg.w)

        # ----- Done

        curve.switch(curve.splines.is_cyclic, cyclic_curve).out("Curve")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Link slices
    #
    # Slices are isntanntied along a curve and properly rotated
    # Then faces can be created to link the instances between them
    # Count is the number of instances
    # The indices and edges are supposed to be ordered instance after instance

    with GeoNodes("Link Slices", is_group=True, fake_user=False, prefix=maths_):

        mesh       = Mesh()
        count      = Integer( 1,        "Count", 1, tip="Number of items to link")
        with_faces = Boolean( True,     "With Faces")
        side_mat   = Material("4 Face", "Sides Material")

        # ----------------------------------------------------------------------------------------------------
        # Dimensions

        with Layout("Dimensions"):
            total_verts = mesh.points.count
            total_edges = mesh.edges.count
            nedges      = (total_edges / count).to_integer()

        # ----------------------------------------------------------------------------------------------------
        # Unique ID per vertex

        with Layout("Index unique id"):
            mesh.points.store("vid", nd.index)

        # ----------------------------------------------------------------------------------------------------
        # Loop on the edges

        with Repeat(iterations=nedges, faces=None, index=0) as rep:

            with Layout("Grid with one edge per instance"):
                face = Mesh.Grid(vertices_x=count, vertices_y=2)
                #edge_index = rep.index + (face.index/2).float_to_integer(rounding_mode='FLOOR')*nedges
                edge_index = rep.index + (nd.index/2).to_integer('FLOOR')*nedges
                edge_vertices = nd.edge_vertices

            # ----- The two vertex indices of edge per instance

            with Layout("The two vertex indices"):

                i0 = mesh.edges.sample_index(edge_vertices.vertex_index_1, index=edge_index)
                i1 = mesh.edges.sample_index(edge_vertices.vertex_index_2, index=edge_index)

            # ----- Locate each vertex

            for i, vert_index in enumerate([i0, i1]):
                with Layout(f"Vertex #{i}"):
                    v   = mesh.points.sample_index(nd.position,          index=vert_index)
                    w   = mesh.points.sample_index( Float.Named("w"),    index=vert_index)
                    vid = mesh.points.sample_index(Integer.Named("vid"), index=vert_index)
                    sel = (nd.index % 2) == i
                    face.points[sel].position = v
                    face.points[sel].store("w",   w)
                    face.points[sel].store("vid", vid)

            rep.faces += face
            rep.index += 1

        # ----------------------------------------------------------------------------------------------------
        # Finalization

        faces = Mesh(rep.faces)
        faces.faces.material = side_mat

        edges_only = Mesh(faces).faces.delete_faces()
        mesh += edges_only.switch(with_faces, faces)

        # ----------------------------------------------------------------------------------------------------
        # Remove duplicate indices

        with Repeat(iterations=total_verts, mesh=mesh, index=0) as rep:
            rep.mesh = rep.mesh[Integer.Named("vid") == rep.index].merge_by_distance(distance=1000.)
            rep.index += 1

        mesh = rep.mesh

        mesh.to_output("Mesh")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Mesh along a curve

    with GeoNodes("Mesh Instances on Curve", is_group=True, fake_user=False, prefix=maths_):

        curve       = Curve(name = "Curve")
        mesh        = Mesh( name = "Mesh")
        scale       = Float(1,          "Scale", 0)
        use_radius  = Boolean(False,    "Use Radius")
        align_w     = Boolean(True,     "Align W")
        resample    = Boolean(False,    "Resample")
        resol       = Integer(32,       "Resolution",  2)

        # ---------------------------------------------------------------------------
        # Resample the curve

        curve = curve.switch(resample, curve.resample(resol))

        # ---------------------------------------------------------------------------
        # Compute the tangents

        curve = Group.Prefix(maths_, "Compute Tangents", {'Curve': curve})._out

        # ---------------------------------------------------------------------------
        # Instantiate the mesh on the curve

        insts = curve.points.instance_on(
            instance = mesh,
            scale = scale.switch(use_radius, nd.radius),
        )

        # ---------------------------------------------------------------------------
        # Store the position and position to zero before rotation

        insts.insts.store("_position", nd.position)
        insts.insts.store("_w", Float.Named("w"))
        insts.insts.position = 0.
        insts.insts.store("w", 0.)

        # ---------------------------------------------------------------------------
        # The instances alignment is done on mesh

        n = insts.insts.count
        meshes = Mesh(insts.realize())
        mesh_index = round(nd.index/n)

        # ---------------------------------------------------------------------------
        # Read position and tangent from the curve

        #centers  = V4.Position(curve, sample_index=mesh_index)

        #curve = maths_.compute_tangents(curve).curve
        #curve = Group.Prefix(maths_, "Compute Tangents", {'Curve': curve})._out

        tangents = V4.Tangent(curve, sample_index=mesh_index)

        # ---------------------------------------------------------------------------
        # Rotation to align (0, 0, 0, 1) -> Tangent and then translation

        tg = V4.Xyzw(0., 0., 1., 0.).switch(align_w, V4.Xyzw(0., 0., 0., 1.))

        #meshes = g_mods.align_vector(meshes, **tg.kwargs("From"), **tangents.kwargs("To")).geometry
        meshes = Mesh(Group.Prefix(mods_, "Align Vector", [meshes, tg.V, tg.w, tangents.V, tangents.w])._out)

        #meshes.points.offset = centers.V
        #meshes.points.store("w", Float.Named("w") + centers.w)
        meshes.points.offset = Vector.Named("_position")
        meshes.points.store("w", Float.Named("w") + Float.Named("_w"))

        meshes.remove_named_attribute("_*", exact=False)

        # Done

        meshes.out()

# ====================================================================================================
# Lights
# - Point
# - Light emitter
# - Light capture

def build_lights():

    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as a 4-point

    with GeoNodes("Point", fake_user=False, prefix=mods_):

        v       = V4(0, 0, "")
        radius  = Float(.1, "Radius", 0)
        visible = Boolean(True, "Visible")
        mat     = Material("4 Edge", "Material")

        point = v.set_position(Cloud.Points(count=1))

        # ----- Point visualization

        sphere = Mesh.UVSphere(radius=radius)
        sphere.corners.store("UVMap", sphere.uv_map_)
        sphere.faces.smooth   = True
        sphere.faces.material = mat

        #sphere = sphere.transform(translation=maths_.projection(*v.args).v)
        sphere = sphere.transform(translation=Group.Prefix(maths_, "Projection", v.sockets()).v)

        # ----- To output

        point.switch(visible, point + sphere).out()

    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as light emitter

    with GeoNodes("Light Emitter", fake_user=False, prefix=mods_):

        v         = V4(0, 0, "")

        color     = Color((1, 1, 1), "Color")
        intensity = Float(1., "Intensity", 0)
        radius    = Float(.1, "Radius")
        visible   = Boolean(True, "Visible")
        mat       = Material(None, "Material")

        # ----- Is a 4 point

        #geo = g_mods.point(None, *v.args, radius=radius, visible=visible, material=mat).geometry
        geo = Group.Prefix(mods_, "Point", {'V': v.V, 'w': v.w, 'Radius': radius, 'Visible': visible, 'material': mat})._out

        mesh, cloud  = geo.mesh, geo.point_cloud

        cloud.points.store(      "Intensity", intensity)
        cloud.points.store("Color", color)

        (cloud + mesh).out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Reflect on a surface given the two normals

    with GeoNodes("Surface Reflection", is_group=True, prefix=maths_):

        v  = V4(0, 0, "")
        Na = V4(0, 0, "Normal A")
        Nb = V4(0, 0, "Normal B")

        # ---------------------------------------------------------------------------
        # Decompose the vector along the two normals and remainder

        with Layout("Decompose along the two normals and the remainder"):
            x = Na.dot(v)
            y = Nb.dot(v)

        # ---------------------------------------------------------------------------
        # Reflected vector inverted the decomposed parts

        with Layout("Inverting the components along the normals"):

            r = v - Na*(2*x) - Nb*(2*y)

            front_a = x.map_range(-.1, 0., 1, 0.)
            front_b = y.map_range(-.1, 0., 1, 0.)

        r.out()

        front_a.to_output("Front A")
        front_b.to_output("Front B")

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Capture light from an emitter

    with GeoNodes("Light Capture", fake_user=False, prefix=mods_):

        geo   = Geometry()
        light = Object(None, "Light")
        focus = Float(1,  "Focus")

        # ----------------------------------------------------------------------------------------------------
        # Read light information

        with Layout("Read light information"):

            info      = light.info()
            cloud     = info.geometry.point_cloud

            light_loc = V4.Position(cloud, sample_index=0)
            color     = cloud.points.sample_index(Color.Named("Color"),     0)
            intensity = cloud.points.sample_index(Float.Named("Intensity"), 0)

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----------------------------------------------------------------------------------------------------
        # Incident vector

        with Layout("Incident vector"):

            v  = V4.Position(mesh)
            Na = V4.Normal(mesh, "A")
            Nb = V4.Normal(mesh, "B")

            vray     = v - light_loc
            distance = vray.length
            incident = vray/distance

        # ----------------------------------------------------------------------------------------------------
        # Reflected vector

        #ref_node  = maths_.surface_reflection(*incident.args, *Na.args, *Nb.args)
        ref_node  = Group.Prefix(maths_, "Surface Reflection", [incident.V, incident.w, Na.V, Na.w, Nb.V, Nb.w])
        reflected = V4.FromNode(ref_node)

        # ----------------------------------------------------------------------------------------------------
        # Intensity

        #proj = V4.NodeOutput(maths_.projection_matrix(), "R 3")
        proj = V4.FromNode(Group.Prefix(maths_, "Projection Matrix"), "R 3")

        with Layout("Light intensity"):

            direct = proj.dot(reflected)
            intensity = intensity*(direct**focus)


        for s in ["A", "B"]:
            with Layout(f"Normal {s} color"):

                front_col = Color.Named(f"Front Color {s}")
                back_col  = Color.Named(f"Back Color {s}")
                front_col = front_col.switch(-front_col.exists_, (0., 0., 0., 1.))
                back_col  = back_col.switch( -back_col.exists_,  (0., 0., 0., 1.))

                #f = getattr(ref_node, f"front_{s}".lower())
                f = ref_node[f"Front {s}"]

                front_col = front_col.add(f*intensity, color)
                back_col  = back_col.add((1-f)*intensity, color)

                mesh.points.store(f"Front Color {s}", front_col)
                mesh.points.store(f"Back Color {s}",  back_col)

        mesh.join(curve, cloud, inst).out()

# ====================================================================================================
# Curves
# - Line
# - Circle
# - Spiral

def build_curves():

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - w from Curve

    with GeoNodes("W from Curve", fake_user=False, prefix=curves_):

        curve    = Curve()
        w_object = Object(None, "W Curve", tip="Z component is used to set curve W component")

        w_curve = Curve(w_object.info().geometry)

        n = curve.points.count
        fac = nd.index/(n-1)

        curve.points.store("w", w_curve.sample(factor=fac).position_.z)

        curve.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - A line

    with GeoNodes("Line", fake_user=False, prefix=curves_):

        v0 = V4(0, 0, "Start")
        v1 = V4((0, 0, 1), 0, "End")

        count = Integer(2, "Resolution", 22)

        line = Curve.Line(v0.V, v1.V).resample(count)
        line.points.store("w", nd.index.map_range(0, count-1, v0.w, v1.w))

        # Tangent is constant

        """
        (v1 - v0).normalized().set_tangent(line)
        """

        # Done

        line.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Parametric Curve

    with GeoNodes("Parametric Curve", fake_user=False, prefix=curves_):

        speed  = V4(0, 1, "Speed")

        r_xy   =  Float(1,            "Radius XY",    tip="Radius in plane XY")
        om_xy  =  Float.Angle(pi*1.5, "Omega XY",     tip="Rotation speed in plane XY")
        r_zw   =  Float(0,            "Radius ZW", 0, tip="Radius in plane ZW")
        om_zw  =  Float.Angle(0,      "Omega ZW",     tip="Rotation speed in plane ZW")

        resol  = Integer(32,    "Resolution",  3, tip="Curve resolution")
        closed = Boolean(False, "Closed",         tip="Curve is closed")

        # ----- Line or circle

        curve = Curve.Line().resample(resol).switch(closed, Curve.Circle(resolution=resol))

        # ----- Parameter

        t = (nd.index/(resol-1)).switch(closed, (nd.index/(resol-2)))

        ca, sa = gnmath.cos(om_xy*t), gnmath.sin(om_xy*t)
        cb, sb = gnmath.cos(om_zw*t), gnmath.sin(om_zw*t)

        # ===== Position

        with Layout("Point position"):

            x = speed.x*t + ca*r_xy
            y = speed.y*t + sa*r_xy
            z = speed.z*t + cb*r_zw
            w = speed.w*t + sb*r_zw

            curve.points.position = (x, y, z)
            curve.points.store("w", w)

        """
        # ===== Tangent
        # dx/dt = s - o.r.sin(o.t)

        with Layout("Tangent"):

            ro_xy = om_xy*r_xy
            ro_zw = om_zw*r_zw

            tx = speed.x - ro_xy*sa
            ty = speed.y + ro_xy*ca
            tz = speed.z - ro_zw*sb
            tw = speed.w + ro_zw*cb

            V4.Xyzw(tx, ty, tz, tw).normalized().set_tangent(curve)
        """

        curve.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh along a curve

    with GeoNodes("Curve to Mesh", fake_user=False, prefix=curves_):

        curve       = Curve()

        resample    = Boolean(False, "Resample")
        new_resol   = Integer(32, "Resolution",  2)

        prof_object = Object(   None, "Mesh Profile", tip="3D Mesh to instantiate along the curve")
        mat         = Material( "4 Face", "Material")
        scale       = Float(    1, "Scale", 1.)
        use_radius  = Boolean(  False, "Use Radius",  tip="Use curve radius attribute")
        align_w     = Boolean(  True, "Align W",     tip="Use mesh w axis along the curve tangent (z otherwise)")
        link_slices = Boolean(  False, "Link slices", tip="Link the instances between them")
        with_faces  = Boolean(  False, "With Faces",  tip="If the slices are linked, create surfaces between the instances.")
        sides_mat   = Material( "4 Face", "Sides Material")

        # ----------------------------------------------------------------------------------------------------
        # The mesh to instantiate

        mesh = Mesh(prof_object.info().geometry)
        mesh.faces.material = mat

        # ----- Instantiate


        mesh = Mesh(Group.Prefix(maths_, "Mesh Instances on Curve",
            curve         = curve,
            mesh          = mesh,
            scale         = scale,
            use_radius    = use_radius,
            align_w       = align_w,
            resample      = resample,
            resolution    = new_resol)._out)

        # ----- Link the slices

        mesh = mesh.switch(link_slices, Group.Prefix(maths_, "Link Slices",
            mesh           = mesh,
            count          = curve.points.count,
            with_faces     = with_faces,
            sides_material = sides_mat,
            )._out)

        # Done

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh along a curve

    with GeoNodes("Curve to Mesh with Spheres", fake_user=False, prefix=curves_):

        curve       = Curve()

        resample    = Boolean(False,  "Resample")
        new_resol   = Integer(32,  "Resolution",  32, 2)

        resol       = Integer(16, "Sphere Resolution", 3)
        size        = Float(1,   "Size", 0)
        use_radius  = Boolean(False,   "Use Radius")
        align_w     = Boolean(True, "Align W",    tip="Use mesh w axis along the curve tangent (z otherwise)")
        mat         = Material("4 Face", "Material")
        link_slices = Boolean(False, "Link slices", tip="Link the instances between them")
        with_faces  = Boolean(False, "With Faces",  tip="If the slices are linked, create surfaces between the instances.")
        sides_mat   = Material("4 Face", "Sides Material")

        # ----------------------------------------------------------------------------------------------------
        # The mesh to instantiate

        sphere = Mesh.UVSphere(rings=resol, segments=2*resol, radius=size)
        sphere.corners.store("UVMap", sphere.uv_map_)
        sphere.faces.material=mat

        # ----- Instantiate

        mesh = Mesh(Group.Prefix(maths_, "Mesh Instances on Curve",
            curve         = curve,
            mesh          = sphere,
            scale         = size,
            use_radius    = use_radius,
            align_w       = align_w,
            resample      = resample,
            resolution    = new_resol)._out)

        # ----- Link the slices

        mesh = mesh.switch(link_slices, Group.Prefix(maths_, "Link Slices",
            mesh           = mesh,
            count          = curve.points.count,
            with_faces     = with_faces,
            sides_material = sides_mat,
            )._out)

        # Done

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Tube on curves

    with GeoNodes("Curves Profile", fake_user=False, prefix=curves_):

        geo        = Geometry()
        radius     = Float(1, "Radius", 0)
        resol      = Integer(8, "Resolution", 2)
        mat        = Material("4 Face", "Material")
        ok_points  = Boolean(False, "With Points")
        pt_radius  = Float(.2, "Points Radius", 0)
        smooth     = Boolean(True, "Shade Smooth")

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- Profile

        meshed = curve.to_mesh(profile_curve=Curve.Circle(radius=radius, resolution=resol))

        # ----- Points

        sph = Mesh.UVSphere(radius=pt_radius, rings=resol, segments=2*resol)
        sph.corners.store("UVMap", sph.uv_map_)
        spheres = curve.points.instance_on(instance=sph)
        meshed  = Mesh(meshed.switch(ok_points, meshed + spheres))

        # ----- Finalization

        meshed.faces.material = mat
        meshed.faces.smooth = smooth

        # ----- Done

        mesh.join(meshed, cloud, inst).out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh to curve (to see the edges)

    with GeoNodes("Mesh to Curve", fake_user=False, prefix=curves_):

        geo         = Geometry()
        keep_faces  = Boolean(False, "Keep faces")

        use_profile = Boolean(True,  "With Profile")
        radius      = Float(.01, "Radius")
        resol       = Integer(8, "Resolution", 2)
        mat         = Material("4 Edge", "Material")
        ok_points   = Boolean(False, "With Points")
        pt_radius   = Float(.02, "Points Radius", 0)
        smooth      = Boolean(True, "Shade Smooth")

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----- To curve

        curved = mesh.to_curve() + curve

        # ----- Profile on the curve

        tubes_node = Group.Prefix(curves_, "Curves Profile", {'Geometry': curved})
        tubes_node.plug_node_into()

        curved = curved.switch(use_profile, tubes_node._out)

        # ----- Done

        geo = curved + cloud + inst
        geo = geo.switch(keep_faces, geo.join(mesh))

        geo.out()

# ====================================================================================================
# Surfaces

def build_surfaces():

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Extrude a mesh of a given offset

    with GeoNodes("Extrude", fake_user=False, prefix=surfs_):

        mesh0      = Mesh()
        offset     = V4((0, 0, 1), 1, "Offset")
        with_faces = Boolean(True, "With Faces")
        mat        = Material("4 Face", "Sides Material")
        keep0      = Boolean(True, "Keep first")
        keep1      = Boolean(True, "Keep last")

        # ----------------------------------------------------------------------------------------------------
        # Dimensions

        nverts = mesh0.points.count
        nedges = mesh0.edges.count

        # ----------------------------------------------------------------------------------------------------
        # Duplicate

        mesh1 = Mesh(mesh0)
        mesh1 = offset.set_offset(mesh1)

        # ----------------------------------------------------------------------------------------------------
        # Unique ID per vertex

        mesh0.points.store("vid", nd.index)
        mesh1.points.store("vid", nd.index + nverts)

        # ----------------------------------------------------------------------------------------------------
        # Loop on the edges

        with Repeat(iterations=nedges, faces=None, index=0) as rep:

            # ----- Create a new face

            with Layout("Face base"):
                face = Mesh.Grid(vertices_x=2, vertices_y=2)
                edge_vertices = nd.edge_vertices

            with Layout("The four vertex indices"):
                indices = [
                    (mesh0, mesh0.edges.sample_index(edge_vertices.vertex_index_1, index=rep.index)),
                    (mesh0, mesh0.edges.sample_index(edge_vertices.vertex_index_2, index=rep.index)),
                    (mesh1, mesh1.edges.sample_index(edge_vertices.vertex_index_1, index=rep.index)),
                    (mesh1, mesh1.edges.sample_index(edge_vertices.vertex_index_2, index=rep.index)),
                    ]

            for i, (msh, vert_index) in enumerate(indices):
                with Layout(f"Vertex #{i}"):
                    v   = msh.points.sample_index(msh.position,      index=vert_index)
                    w   = msh.points.sample_index(Integer.Named("w"), index=vert_index)
                    vid = msh.points.sample_index(Integer.Named("vid"), index=vert_index)
                    sel = nd.index == i
                    face.points[sel].position = v
                    face.points[sel].store("w", w)
                    face.points[sel].store("vid", vid)

            rep.faces += face
            rep.index += 1

        # ----------------------------------------------------------------------------------------------------
        # Finalization

        faces = Mesh(rep.faces)
        faces.faces.material = mat

        edges_only = Mesh(faces).faces.delete_faces()
        mesh = edges_only.switch(with_faces, faces)

        mesh = mesh.switch(keep0, mesh0 + mesh)
        mesh = mesh.switch(keep1, mesh + mesh1)

        # ----------------------------------------------------------------------------------------------------
        # Remove duplicate indices

        with Repeat(iterations=nverts*2, mesh=mesh, index=0) as rep:
            rep.mesh[Integer.Named("vid") == rep.index].merge_by_distance(distance=1000.)
            rep.index += 1

        mesh = rep.mesh
        mesh.remove_named_attribute("vid")

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # Hypercube

    with GeoNodes("Hypercube", fake_user=False, prefix=surfs_):

        size   = Float(  1, "Size", .01)
        #slices = Integer(7, "Slices", 1)
        mat    = Material("4 Face", "Material")

        cube = Mesh.Cube()
        cube.faces.material = mat
        cube = V4.Xyzw(0., 0., 0., -size/2).set_offset(cube)

        geo = Group.Prefix(surfs_, "Extrude", sockets=V4.Xyzw(0., 0., 0., size).sockets("Offset"),
            mesh           = cube,
            with_faces     = True,
            sides_material = mat,
            keep_first     = True,
            keep_last      = True,
            )._out

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Hypersphere

    with GeoNodes("Hypersphere", fake_user=False, prefix=surfs_):

        radius = Float(  1, "Radius",       .01)
        resol  = Integer( 16, "Resolution", 3)
        slices = Integer(7, "Slices",     1)
        mat    = Material("4 Face", "Material")

        line = Curve(Group.Prefix(curves_, "Line", start_v=0., start_w=-radius, end_v=0., end_w=radius, resolution=slices+2)._out)

        line.points.radius = gnmath.sqrt(abs(radius**2 - Float.Named("w")**2))

        line = line.points[slices+1].delete()
        line = line.points[0].delete()

        hs = Mesh(Group.Prefix(curves_, "Curve to Mesh with Spheres",
            curve      = line,
            sphere_resolution = resol,
            use_radius = True,
            align_w    = True,
            material   = mat,
            )._out)

        hs.faces.smooth = True

        hs.out()

    # ----------------------------------------------------------------------------------------------------
    # Extrude along w

    with GeoNodes("Extrude W", fake_user=False, prefix=surfs_):

        mesh     = Mesh()
        size_w   = Float(1, "Offset w", )
        as_curve = Boolean(True, "As curve")

        # ----- Start a minus size

        size_w /= 2
        mesh.points.store("w", -size_w)

        # ----- Extrude to plus size

        mesh = mesh.edges.extrude(offset_scale=0.)
        mesh.points[mesh.top_].store("w", size_w)

        # ----- Return the result

        mesh = mesh.switch(as_curve, mesh.to_curve())

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # Torus

    with GeoNodes("Torus", fake_user=False, prefix=surfs_):

        radius0 = Float(1,   "Radius XY",  .01)
        radius1 = Float(1,    "Radius ZW",  .01)
        resol   = Integer(32, "Resolution", 32, 3)
        factor0 = Float.Factor(1, "Factor XY", 0, 1)
        factor1 = Float.Factor(1, "Factor ZW", 0, 1)
        twists  = Float(0, "Twists", -10, 10)
        mat     = Material("4 Face", "Material")
        smooth  = Boolean(True, "Shade smooth")

        # ----------------------------------------------------------------------------------------------------
        # Starting from a grid

        grid = Mesh.Grid(vertices_x=resol, vertices_y=resol)
        grid.corners.store("UVMap", grid.uv_map_)
        a = (nd.index/resol)/(resol-1)
        b = (nd.index%resol)/(resol-1)

        # ----------------------------------------------------------------------------------------------------
        # Curve in the plane xy

        # ----- Line

        with Layout("XY Factor=0: straight line"):
            l_xy = tau*radius0
            lx = 0.
            ly = a*l_xy - l_xy/2

            line0 = Mesh(grid)
            line0.points.position = (lx, ly, 0)

        # ----- Circle in plane XY

        with Layout("XY Curve lined up to Circle"):
            ag0 = tau*factor0
            r0 = l_xy/ag0
            c0 = Vector((0, -r0, 0))

            ag0_ = a*ag0 - ag0/2
            cx = r0*gnmath.cos(ag0_)
            cy = r0*gnmath.sin(ag0_)

            circle0 = Mesh(grid)
            circle0.points.position = (cx - r0 + factor0*radius0, cy, 0)

        circle0 = circle0.switch(factor0 < 0.001, line0)

        # ----------------------------------------------------------------------------------------------------
        # Curve in the plane zw

        # ----- Line

        with Layout("ZW Factor=0: straight line"):
            l_zw = tau*radius1
            lz = 0.
            lw = b*l_zw - l_zw/2

            line1 = Mesh(circle0)
            line1.points.offset = (0., 0., lz)
            line1.points.store("w", lw)

        # ----- Circle in plane ZW

        with Layout("ZW Curve lined up to Circle"):
            ag1 = tau*factor1
            r1 = l_zw/ag1
            c1 = Vector()

            ag1_ = b*ag1 - ag1/2

            cz = r1*gnmath.cos(ag1_)
            cw = r1*gnmath.sin(ag1_)

            circle1 = Mesh(circle0)
            circle1.points.offset = (0., 0., cz - r1 + factor1*radius1)
            circle1.points.store("w", cw)

        circle1 = circle1.switch(factor1 < 0.001, line1)

        # ----- Twists

        with Layout("ZW Twist the profile"):

            y0 = circle0.points.sample_index(nd.position.y, nd.index)

            ag_twist = a*(pi*twists)
            cost = gnmath.cos(a*ag_twist)
            sint = gnmath.sin(a*ag_twist)

            loc = nd.position

            y = loc.y - y0

            y_ =   y*cost + loc.z*sint
            z_ =  -y*sint + loc.z*cost

            circle1.points.position = (loc.x, y0 + y_, z_)


        # ----- Finalize

        circle1.faces.material = mat
        circle1.faces.smooth = smooth

        circle1.out()

    # ----------------------------------------------------------------------------------------------------
    # Clifford Torus

    with GeoNodes("Clifford Torus", fake_user=False, prefix=surfs_):

        node = Group.Prefix(surfs_, "Torus",
            #radius_xy    = Float(  "Radius XY",  1.),
            #radius_zw    = Float(  "Radius ZW",  1.),
            #resolution   = Integer("Resolution", 32, min_value=3),
            factor_xy    = 1.,
            factor_zw    = 1.,
            twists       = 0.,
            #material     = Material("Material", bpy.data.materials.get("4 Face")),
            #shade_smooth = Boolean(    "Shade smooth", True),
            )

        node.plug_node_into(exclude=['Factor XY', 'Factor ZW', 'Twists'])

        node._out.out()


    # ----------------------------------------------------------------------------------------------------
    # Klein Torus

    with GeoNodes("Klein Torus", fake_user=False, prefix=surfs_):

        node = Group.Prefix(surfs_, "Torus",
            #radius_xy    = Float(  "Radius XY",  1.),
            #radius_zw    = Float(  "Radius ZW",  1.),
            #resolution   = Integer("Resolution", 32, min_value=3),
            factor_xy    = 1.,
            factor_zw    = 1.,
            twists       = 1.,
            #material     = Material("Material", bpy.data.materials.get("4 Face")),
            #shade_smooth = Boolean(    "Shade smooth", True),
            )

        node.plug_node_into(exclude=['Factor XY', 'Factor ZW', 'Twists'])

        node._out.out()

    # ----------------------------------------------------------------------------------------------------
    # 5 Cell

    with GeoNodes("5 Cell Polytope", fake_user=False, prefix=surfs_):

        size = Float(1,   "Size")
        mat  = Material("4 Face", "Material")

        from math import sqrt

        v0 = V4.Xyzw(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12),  1/2)
        v1 = V4.Xyzw(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12), -1/2)
        v2 = V4.Xyzw(1/2/sqrt(10),  1/2/sqrt(6), -2/sqrt(12),    0)
        v3 = V4.Xyzw(1/2/sqrt(10), -3/2/sqrt(6),           0,    0)
        v4 = V4.Xyzw( -2/sqrt(10),            0,           0,    0)

        S = Mesh.Cone(vertices=3)

        S.points[0].position = v0.V*size
        S.points[0].store("w", v0.w*size)
        S.points[1].position = v1.V*size
        S.points[1].store("w", v1.w*size)
        S.points[2].position = v2.V*size
        S.points[2].store("w", v2.w*size)
        S.points[3].position = v3.V*size
        S.points[3].store("w", v3.w*size)

        S = S.edges.extrude()
        top = S.top_

        S.points[top].position=v4.V
        S.points[top].store("w", v4.w)

        S = S[top].merge_by_distance(distance=1)

        S.faces.material = mat

        S.out()

    # ----------------------------------------------------------------------------------------------------
    # 16 Cell

    with GeoNodes("16 Cell Polytope", fake_user=False, prefix=surfs_):

        size = Float(1,   "Size", 0)
        mat  = Material("4 Face", "Material")

        vs = [V4.Xyzw( 1.,  0.,  0.,  0.), V4.Xyzw( 0.,  1.,  0.,  0.), V4.Xyzw( 0.,  0.,  1.,  0.), V4.Xyzw( 0.,  0.,  0.,  1.),
              V4.Xyzw(-1.,  0.,  0.,  0.), V4.Xyzw( 0., -1.,  0.,  0.), V4.Xyzw( 0.,  0., -1.,  0.), V4.Xyzw( 0.,  0.,  0., -1.)]

        with Layout("Points coordinates (w on radius)"):
            points = Cloud.Points(8)
            for i in range(8):
                sel = nd.index == i
                points.points[sel].position = vs[i].V*size
                points.points[sel].radius   = vs[i].w*size

        # ----------------------------------------------------------------------------------------------------
        # Loops on triplets of points

        # ----- Loop on 6 vertices
        # The last 2 ones will have been taken into account in other triangles
        # index0 : from 0 to 5

        with Repeat(iterations=6, mesh=None, index=0) as rep0:

            # ----- Loop on up to 7 vertices greater than index 0
            # index1 : from 1 to 6

            opp0 = rep0.index + 4

            with Repeat(iterations=7 - rep0.index, mesh=rep0.mesh, index=rep0.index + 1) as rep1:

                # ----- Loop on up to 6 vertices greater than index 1
                # index2 : from 2 to 7

                opp1 = rep1.index + 4

                with Repeat(iterations=7 - rep1.index, mesh=rep1.mesh, index=rep1.index + 1) as rep2:

                    trg = Mesh.Circle(vertices=3, fill_type='NGON')

                    for i, rep in enumerate([rep0, rep1, rep2]):

                        with Layout(f"Set triangle vertex #{i}"):
                            sel = nd.index == i
                            trg.points[sel].position = points.points.sample_index(nd.position, index=rep.index)
                            trg.points[sel].store("w", points.points.sample_index(nd.radius, index=rep.index))
                            trg.points[sel].store( "vid", rep.index)

                    with Layout("Opposite edges don't exist"):
                        nope = (opp0 == rep1.index) | (opp0 == rep2.index) | (opp1 == rep2.index)
                        trg.points.store("_delete", nope)

                    rep2.mesh += trg
                    rep2.index += 1

                rep1.mesh  = rep2.mesh
                rep1.index += 1

            rep0.mesh  = rep1.mesh
            rep0.index += 1


        with Layout("Delete non existing edges"):
            mesh = Mesh(rep0.mesh)
            mesh = mesh.points[Boolean.Named("_delete")].delete()
            mesh.remove_named_attribute("_delete")

        with Layout("Delete duplicates"):
            with Repeat(mesh=mesh, index=0, iterations=8) as rep:
                rep.mesh = rep.mesh[Integer.Named("vid") == rep.index].merge_by_distance(distance=1)
                rep.index += 1

        mesh = rep.mesh

        mesh.faces.material = mat


        mesh.out("Geometry")

# ====================================================================================================
# Global demo

def show_case():

    with GeoNodes("Show Case 4D"):

        items = {name: Group.Prefix(surfs_, name)._out for name in [
            "Hypercube", "Hypersphere", "Clifford Torus", "Klein Torus", "5 Cell Polytope", "16 Cell Polytope",
        ]}

        geo = Geometry.MenuSwitch(items=items, menu=0, name='4D Shape')

        projected = Group.Prefix(mods_, "Projection", geometry=geo, shade_smooth=Boolean(False, "Shade Smooth"))._out

        geo = geo.switch(Boolean(True, "Projection"), projected)

        geo = geo.switch(Boolean(False, "As Curve"), Group.Prefix(curves_, "Mesh to Curve", geometry=geo)._out)

        geo.out()

























# ====================================================================================================
# Main

def debug():
    def vis_proj_mat():

        with GeoNodes("Debug PROJ"):
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
