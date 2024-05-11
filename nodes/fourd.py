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

V4_COL = (.3, .1, .1)


# ----- Named attributes

def clear_all():
    g_maths.clear()
    g_mods.clear()
    g_curves.clear()
    g_surfs.clear()

def build4D(clear=False):

    print("-"*100)
    print("Build 4D Engine")
    print()

    if clear:
        clear_all()

    build_shaders()

    build_matrices()
    build_base()
    build_vectors()
    build_transformations()
    build_extrusions()
    build_lights()
    build_curves()
    build_surfaces()

    nodes = 0
    links = 0
    for pref in [g_maths, g_mods, g_curves, g_surfs]:

        n, l = pref._nodes_links_count
        nodes += n
        links += l

    print()
    print(f"4D Engine built : {nodes} nodes, {links} links")
    print()



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
    # Face default

    with Shader("4 Face") as tree:

        noise = tree.NoiseTexture(scale=5.)
        bump = tree.Bump(height=noise.color, strength=.1)

        ped = tree.PrincipledBSDF(
            base_color = tree.rgb(.3, .8, .7),
            metallic   = 0.,
            roughness  = 0.,
            alpha      = .1,
            normal     = bump.normal,
            )

        tree.output_surface = ped.bsdf

        tree.material.blend_method  = 'HASHED'
        tree.material.shadow_method = 'HASHED'

    # ----------------------------------------------------------------------------------------------------
    # Edge default

    with Shader("4 Edge") as tree:

        ped = tree.PrincipledBSDF(
            base_color = tree.rgb(0., .05, .9),
            roughness  = 0.,
            )

        tree.output_surface = ped.bsdf


# =============================================================================================================================
# A 4-vector is a couple (V: Vector, w: float)

class V4:
    def __init__(self, V, w):

        # Get the current tree
        tree = GeoNodes.current_tree()

        # The arguments can be either a socket or a value
        if hasattr(V, 'bsocket'):
            self.V = V
        else:
            self.V = tree.Vector(V).vector

        if hasattr(w, 'bsocket'):
            self.w = w
        else:
            self.w = tree.value(w)

    # ----------------------------------------------------------------------------------------------------
    # X, y, z, w

    @classmethod
    def Xyzw(cls, x, y, z, w):
        tree = GeoNodes.current_tree()
        return cls(tree.xyz(x, y, z), w)

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

    # ----------------------------------------------------------------------------------------------------
    # Node input / output

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

    # ----------------------------------------------------------------------------------------------------
    # From / to position

    @classmethod
    def Position(cls, geo, sample_index=None):
        with GeoNodes.current_tree().layout("Get Position V4", V4_COL):
            if sample_index is None:
                return cls(geo.position, geo.named_float("w"))
            else:
                return cls(
                    geo.POINT.sample_index_vector(geo.position,         index=sample_index),
                    geo.POINT.sample_index_float( geo.named_float("w"), index=sample_index))

    def set_position(self, geo):
        # Need to sample w before setting the position because w can be computed
        # from the position (for instance after a rotation)
        # Changing the position would change w before it is written
        with GeoNodes.current_tree().layout("Set Position V4", V4_COL):
            w = geo.POINT.sample_index_float(self.w, index=geo.index)
            geo.position = self.V
            return geo.store_named_float("w", w)

    def set_offset(self, geo):
        with GeoNodes.current_tree().layout("Set Offset V4", V4_COL):
            w = geo.POINT.sample_index_float(self.w, index=geo.index)
            geo.offset = self.V
            return geo.store_named_float("w", w + geo.named_float("w"))

    # ----------------------------------------------------------------------------------------------------
    # From / to face normal

    @classmethod
    def Normal(cls, geo, suffix, sample_index=None):
        with GeoNodes.current_tree().layout("Get Normal", V4_COL):
            if sample_index is None:
                return cls(geo.named_vector(f"N{suffix}V"), geo.named_float(f"N{suffix}w"))
            else:
                return cls(
                    geo.FACE.sample_index_vector(geo.named_vector(f"N{suffix}V"), index=sample_index),
                    geo.FACE.sample_index_float( geo.named_float( f"N{suffix}w"), index=sample_index))

    def set_normal(self, geo, suffix):
        with GeoNodes.current_tree().layout("Set Normal", V4_COL):
            w = geo.FACE.sample_index_float(self.w, index=geo.index)
            geo.FACE.store_named_vector(f"N{suffix}V", self.V)
            return geo.FACE.store_named_float( f"N{suffix}w", w)

    # ----------------------------------------------------------------------------------------------------
    # From / to curve tangent

    @classmethod
    def Tangent(cls, geo, sample_index=None):

        # ----- Does the tangent exist ?

        with GeoNodes.current_tree().layout("Get Tangent", V4_COL):
            if sample_index is None:
                return cls(geo.named_vector("TV"), geo.named_float("Tw"))
            else:
                return cls(
                    geo.POINT.sample_index_vector(geo.named_vector("TV"), index=sample_index),
                    geo.POINT.sample_index_float( geo.named_float( "Tw"), index=sample_index))

    def set_tangent(self, geo):
        with GeoNodes.current_tree().layout("Set Tangent", V4_COL):
            w = geo.POINT.sample_index_float(self.w, index=geo.index)
            geo.POINT.store_named_vector("TV", self.V)
            return geo.POINT.store_named_float( "Tw", w)

    # ----------------------------------------------------------------------------------------------------
    # Operations

    def __neg__(self):
        with GeoNodes.current_tree().layout("-V4", V4_COL):
            return cls(-self.V, -self.w)

    def __add__(self, other):
        with GeoNodes.current_tree().layout("V4 Add", V4_COL):
            return V4(self.V + other.V, self.w + other.w)

    def __iadd__(self, other):
        with GeoNodes.current_tree().layout("V4 Add", V4_COL):
            self.V += other.V
            self.w += other.w
            return self

    def __sub__(self, other):
        with GeoNodes.current_tree().layout("V4 Sub", V4_COL):
            return V4(self.V - other.V, self.w - other.w)

    def __isub__(self, other):
        with GeoNodes.current_tree().layout("V4 Sub", V4_COL):
            self.V -= other.V
            self.w -= other.w
            return self

    def __mul__(self, other):
        with GeoNodes.current_tree().layout("V4 Mul", V4_COL):
            if isinstance(other, V4):
                return V4(self.V*other.V, self.w*other.w)
            else:
                return V4(self.V*other, self.w*other)

    def __imul__(self, other):
        with GeoNodes.current_tree().layout("V4 Mul", V4_COL):
            if isinstance(other, V4):
                self.V *= other.V
                self.w *= other.w
            else:
                self.V *= other
                self.w *= other
            return self

    def __truediv__(self, other):
        with GeoNodes.current_tree().layout("V4 Div", V4_COL):
            if isinstance(other, V4):
                return V4(self.V/other.V, self.w/other.w)
            else:
                return V4(self.V/other, self.w/other)

    def __itruediv__(self, other):
        with GeoNodes.current_tree().layout("V4 Div", V4_COL):
            if isinstance(other, V4):
                self.V /= other.V
                self.w /= other.w
            else:
                self.V /= other
                self.w /= other
            return self

    def dot(self, other):
        with GeoNodes.current_tree().layout("Dot 4", V4_COL):
            return self.V.dot(other.V) + self.w*other.w

    @property
    def length(self):
        with GeoNodes.current_tree().layout("V4 Length", V4_COL):
            return self.V.tree.sqrt(self.V.dot(self.V) + self.w*self.w)

    def normalized(self, return_error=False):
        with GeoNodes.current_tree().layout("V4 Normalized", V4_COL):
            n = self.length
            #err = n.less_than(ZERO)
            err = n < ZERO
            v4 = V4((self.V/n).switch(err, self.V), (self.w/n).switch(err, self.w))
            if return_error:
                return v4, err
            else:
                return v4

    def mat_dot(self, M):
        with GeoNodes.current_tree().layout("Mat (4x4) @ V4", V4_COL):

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
        with GeoNodes.current_tree().layout("Switch V4", V4_COL):
            return V4(self.V.switch(b, other.V), self.w.switch(b, other.w))

    def angle_with(self, other):
        with GeoNodes.current_tree().layout("V4 Angle", V4_COL):
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
        mat    = tree.material_input("Material", bpy.data.materials.get("4 Axis"))

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
                #back *= dot.less_than(0)
                back &= dot < 0

            # NOTE : Storing the back flag on POINT smoothes the transition
            mesh.POINT.store_named_boolean("Back", back)

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

                #greater = n.greater_than(n3)
                greater = n > n3
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

        #tree.abs(D).less_than(0.001).to_output("Error")
        (tree.abs(D) < 0.001).to_output("Error")
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

        """
        with tree.layout("Curve"):

            t = V4.Tangent(curve)*scale
            t.normalized().set_tangent(curve)
        """

        tree.og = mesh + curve + cloud + inst

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation 4D

    with GeoNodes("Rotation 4D", is_group=True, fake_user=True, prefix=g_maths) as tree:

        v = V4.Input(tree)

        xy = tree.angle_input("XY", description="Rotation (XY,ZW) : X -> Y")
        zw = tree.angle_input("ZW", description="Rotation (XY,ZW) : Z -> W")

        yz = tree.angle_input("YZ", description="Rotation (YZ,ZW) : Y -> Z")
        xw = tree.angle_input("XW", description="Rotation (YZ,ZW) : X -> W")

        zx = tree.angle_input("ZX", description="Rotation (ZX,YW) : Z -> X")
        yw = tree.angle_input("YW", description="Rotation (ZX,YW) : Y -> W")

        # ----- Rotation xy / zw

        with tree.layout("Angles XY ZW"):
            ca, sa = tree.cos(xy), tree.sin(xy)
            cb, sb = tree.cos(zw), tree.sin(zw)
            A0 = V4.Xyzw( ca, -sa,  0.,  0.)
            A1 = V4.Xyzw( sa,  ca,  0.,  0.)
            A2 = V4.Xyzw( 0.,  0.,  cb, -sb)
            A3 = V4.Xyzw( 0.,  0.,  sb,  cb)

        # ----- Rotation xz / yw

        with tree.layout("Angles ZX YW"):
            ca, sa = tree.cos(zx), tree.sin(zx)
            cb, sb = tree.cos(yw), tree.sin(yw)
            B0 = V4.Xyzw( ca,  0.,  sa,  0.)
            B1 = V4.Xyzw( 0.,  cb,  0., -sb)
            B2 = V4.Xyzw(-sa,  0.,  ca,  0.)
            B3 = V4.Xyzw( 0.,  sb,  0.,  cb)

        # ----- Rotation xw / yz

        with tree.layout("Angles XW YZ"):
            ca, sa = tree.cos(xw), tree.sin(xw)
            cb, sb = tree.cos(yz), tree.sin(yz)
            C0 = V4.Xyzw( ca,  0.,   0., -sa)
            C1 = V4.Xyzw( 0.,  cb, -sb,  0.)
            C2 = V4.Xyzw( 0.,  sb,  cb,  0.)
            C3 = V4.Xyzw( sa,  0.,   0.,  ca)

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

        xy = tree.angle_input("XY", description="Rotation (XY,ZW) : X -> Y")
        zw = tree.angle_input("ZW", description="Rotation (XY,ZW) : Z -> W")

        yz = tree.angle_input("YZ", description="Rotation (YZ,ZW) : Y -> Z")
        xw = tree.angle_input("XW", description="Rotation (YZ,ZW) : X -> W")

        zx = tree.angle_input("ZX", description="Rotation (ZX,YW) : Z -> X")
        yw = tree.angle_input("YW", description="Rotation (ZX,YW) : Y -> W")

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

        for s in ["A","B"]:
            with tree.layout(f"Normal {s}"):
                node = g_maths.rotation_4d(**V4.Normal(mesh, s).kwargs())
                tree.input_node.plug_to(node)
                V4.NodeOutput(node).set_normal(mesh, s)

        # ----- Curve
        """

        with tree.layout("Curve"):

            node = g_maths.rotation_4d(**V4.Tangent(curve).kwargs())
            tree.input_node.plug_to(node)
            V4.NodeOutput(node).set_tangent(curve)
        """

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

        """

        with tree.layout("Curve"):
            node = g_maths.rotation_2d(*V4.Tangent(curve).args, *I.args, *J.args, angle=ag)
            V4.NodeOutput(node).set_tangent(curve)
        """

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

        """
        with tree.layout("Curve"):
            node = g_maths.align_vector(*V4.Tangent(curve).args, *va.args, *vb.args)
            V4.NodeOutput(node).set_tangent(curve)
        """

        tree.og = mesh + curve + cloud + inst

def build_extrusions():

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Compute curve tangent

    with GeoNodes("Compute Tangents", is_group=True, fake_user=True, prefix=g_maths) as tree:

        curve = tree.geometry_input("Curve")

        count = curve.domain_size(component='CURVE').point_count
        count1 = count-1
        dt = .25/count1

        # ------ Tangent computation script

        def compute(fac0, fac1, title="Compute tangent: normalized(V4(t + dt) - V4(t - dt)"):
            with tree.layout(title):
                v1 = V4(curve.sample_curve(      factor=fac1, mode='FACTOR').position,
                        curve.sample_curve_float(factor=fac1, value=curve.named_float("w"), mode='FACTOR').value)

                v0 = V4(curve.sample_curve(      factor=fac0, mode='FACTOR').position,
                        curve.sample_curve_float(factor=fac0, value=curve.named_float("w"), mode='FACTOR').value)

                return (v1 - v0).normalized()

        # ------ All points

        compute((curve.index/(count1) - dt) % 1.0001, (curve.index/(count1) + dt) % 1.0001).set_tangent(curve)

        cyclic_curve = tree.GEOMETRY(curve)

        # ------ First and, last if not cyclic

        tg = compute(0, dt, "First tangent")
        with tree.layout("Set first"):
            sel = curve.index == 0
            curve[sel].POINT.store_named_vector("TV", tg.V)
            curve[sel].POINT.store_named_float("Tw",  tg.w)

        tg = compute(1-dt, 1, "Last tagent")
        with tree.layout("Set last"):
            sel = curve.index == count1
            curve[sel].POINT.store_named_vector("TV", tg.V)
            curve[sel].POINT.store_named_float("Tw", tg.w)

        # ----- Done

        cyclic = curve.sample_curve_boolean(value=curve.spline_cyclic).value

        curve.switch(cyclic, cyclic_curve).to_output("Curve")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Link slices
    #
    # Slices are isntanntied along a curve and properly rotated
    # Then faces can be created to link the instances between them
    # Count is the number of instances
    # The indices and edges are supposed to be ordered instance after instance

    with GeoNodes("Link Slices", is_group=True, fake_user=True, prefix=g_maths) as tree:

        mesh       = tree.geometry_input("Mesh")
        count      = tree.integer_input( "Count", 1, min_value=1, description="Number of items to link")
        with_faces = tree.bool_input(    "With Faces", True)
        side_mat   = tree.material_input("Sides Material", bpy.data.materials.get("4 Face"))

        # ----------------------------------------------------------------------------------------------------
        # Dimensions

        with tree.layout("Dimenions"):
            domain_size = mesh.domain_size(component='MESH')
            total_verts = domain_size.point_count
            total_edges = domain_size.edge_count
            nedges      = (total_edges / count).float_to_integer()

        # ----------------------------------------------------------------------------------------------------
        # Unique ID per vertex

        with tree.layout("Index unique id"):
            mesh.POINT.store_named_int("vid", mesh.index)

        # ----------------------------------------------------------------------------------------------------
        # Loop on the edges

        with tree.repeat(iterations=nedges, faces=None, index=0) as rep:
        #with tree.repeat(iterations=1, faces=None, index=0) as rep:

            # ----- Create a new face per interval
            # face (grid) : 2*count points
            # instance index : face/2
            # instance edge index : (instance index)*(# edges) + num

            with tree.layout("Grid with one edge per instance"):
                face = tree.grid(vertices_x=count, vertices_y=2)
                edge_index = rep.index + (face.index/2).float_to_integer(rounding_mode='FLOOR')*nedges
                edge_vertices = tree.EdgeVertices()

            # ----- The two vertex indices of edge per instance

            with tree.layout("The two vertex indices"):

                i0 = mesh.EDGE.sample_index_int(edge_vertices.vertex_index_1, index=edge_index)
                i1 = mesh.EDGE.sample_index_int(edge_vertices.vertex_index_2, index=edge_index)

            # ----- Locate each vertex

            for i, vert_index in enumerate([i0, i1]):
                with tree.layout(f"Vertex #{i}"):
                    v   = mesh.POINT.sample_index_vector(mesh.position,         index=vert_index)
                    w   = mesh.POINT.sample_index_float( mesh.named_float("w"), index=vert_index)
                    vid = mesh.POINT.sample_index_int(   mesh.named_int("vid"), index=vert_index)
                    sel = (face.index % 2) == i
                    face.POINT[sel].set_position(position=v)
                    face.POINT[sel].store_named_float("w",   w)
                    face.POINT[sel].store_named_int(  "vid", vid)

            rep.faces += face
            rep.index += 1

        # ----------------------------------------------------------------------------------------------------
        # Finalization

        faces = rep.faces
        faces.material = side_mat

        edges_only = tree.GEOMETRY(faces).FACE.delete_geometry(mode='ONLY_FACE')
        mesh += edges_only.switch(with_faces, faces)

        # ----------------------------------------------------------------------------------------------------
        # Remove duplicate indices

        with tree.repeat(iterations=total_verts, mesh=mesh, index=0) as rep:
            rep.mesh[rep.mesh.named_int("vid") == rep.index].merge_by_distance(distance=1000.)
            rep.index += 1

        mesh = rep.mesh

        mesh.to_output("Mesh")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Mesh along a curve

    with GeoNodes("Mesh instances on curve", is_group=True, fake_user=True, prefix=g_maths) as tree:

        curve       = tree.geometry_input("Curve")
        mesh        = tree.geometry_input("Mesh")
        scale       = tree.float_input(   "Scale", 1.)
        use_radius  = tree.bool_input(    "Use Radius",  False)
        align_w     = tree.bool_input(    "Align w",     True)
        resample    = tree.bool_input(    "Resample",    False)
        resol       = tree.integer_input( "Resolution",  32, min_value=2)

        # ---------------------------------------------------------------------------
        # Resample the curve

        curve = curve.switch(resample, tree.GEOMETRY(curve).resample_curve(resol))

        # ---------------------------------------------------------------------------
        # Points at origin to instantiate the meshes

        count = curve.domain_size(component='CURVE').point_count
        pts = tree.points(count)
        pts.position = 0

        # ---------------------------------------------------------------------------
        # Instantiate the surface the right number of times at location zero
        # to perform rotation

        n = mesh.domain_size(component='MESH').point_count

        insts = pts.instance_on_points(instance=mesh)

        # Scale with spline radius
        insts.scale_instances(scale=scale.switch(use_radius, curve.sample_index_float(curve.radius, insts.index)*scale))

        # Realize the instances
        meshes = insts.realize_instances()
        mesh_index = meshes.index/n

        # ---------------------------------------------------------------------------
        # Read position and tangent from the curve

        centers  = V4.Position(curve, sample_index=mesh_index)

        curve = g_maths.compute_tangents(curve).curve
        tangents = V4.Tangent(curve, sample_index=mesh_index)

        # ---------------------------------------------------------------------------
        # Rotation to align (0, 0, 0, 1) -> Tangent and then translation

        tg = V4.Xyzw(0., 0., 1., 0.).switch(align_w, V4.Xyzw(0., 0., 0., 1.))

        meshes = g_mods.align_vector(meshes, **tg.kwargs("From"), **tangents.kwargs("To")).geometry

        meshes.offset = centers.V
        meshes.POINT.store_named_float("w", meshes.named_float("w") + centers.w)

        # Done

        meshes.to_output("Mesh")



# ====================================================================================================
# Lights
# - Point
# - Light emitter
# - Light capture

def build_lights():

    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as a 4-point

    with GeoNodes("Point", fake_user=True, prefix=g_mods) as tree:

        v       = V4.Input(tree)
        radius  = tree.float_input("Radius", .1)
        visible = tree.bool_input( "Visible", True)
        mat     = tree.material_input("Material", bpy.data.materials.get("4 Edge"))

        point = tree.points(count=1)
        v.set_position(point)

        # ----- Point visualization

        sphere = tree.uv_sphere(radius=radius)
        sphere.uv_map = sphere.node.uv_map
        sphere.shade_smooth = True
        sphere.material     = mat

        sphere.transform_geometry(translation=g_maths.projection(*v.args).v)

        # ----- To output

        tree.og = point.switch(visible, point + sphere)

    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as light emitter

    with GeoNodes("Light Emitter", fake_user=True, prefix=g_mods) as tree:

        v         = V4.Input(tree)

        color     = tree.color_input(   "Color", (1., 1., 1., 1.))
        intensity = tree.float_input(   "Intensity", 1., min_value = 0)
        radius    = tree.float_input(   "Radius", .1)
        visible   = tree.bool_input(    "Visible", True)
        mat       = tree.material_input("Material")

        # ----- Is a 4 point

        geo = g_mods.point(None, *v.args, radius=radius, visible=visible, material=mat).geometry

        comps = geo.separate_components()
        mesh  = comps.mesh
        cloud = comps.point_cloud

        cloud.POINT.store_named_float(      "Intensity", intensity)
        cloud.POINT.store_named_float_color("Color", color)

        tree.og = cloud + mesh

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Reflect on a surface given the two normals

    with GeoNodes("Surface reflection", is_group=True, prefix=g_maths) as tree:

        v  = V4.Input(tree)
        Na = V4.Input(tree, "Normal A")
        Nb = V4.Input(tree, "Normal B")

        # ---------------------------------------------------------------------------
        # Decompose the vector along the two normals and remainder

        with tree.layout("Decompose along the two normals and the remainder"):
            x = Na.dot(v)
            y = Nb.dot(v)

        # ---------------------------------------------------------------------------
        # Reflected vector inverted the decomposed parts

        with tree.layout("Inverting the components along the normals"):

            r = v - Na*(2*x) - Nb*(2*y)

            front_a = x.map_range(-.1, 0., 1, 0.)
            front_b = y.map_range(-.1, 0., 1, 0.)

        r.to_output()

        front_a.to_output("Front A")
        front_b.to_output("Front B")

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Capture light from an emitter

    with GeoNodes("Light Capture", fake_user=True, prefix=g_mods) as tree:

        geo   = tree.ig
        light = tree.object_input("Light")
        focus = tree.float_input( "Focus", 1.)

        # ----------------------------------------------------------------------------------------------------
        # Read light information

        with tree.layout("Read light information"):

            info      = light.object_info()
            cloud     = info.geometry.separate_components().point_cloud

            light_loc = V4.Position(cloud, sample_index=0)
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

            v  = V4.Position(mesh)
            Na = V4.Normal(mesh, "A")
            Nb = V4.Normal(mesh, "B")

            vray     = v - light_loc
            distance = vray.length
            incident = vray/distance

        # ----------------------------------------------------------------------------------------------------
        # Reflected vector

        ref_node  = g_maths.surface_reflection(*incident.args, *Na.args, *Nb.args)
        reflected = V4.NodeOutput(ref_node)

        # ----------------------------------------------------------------------------------------------------
        # Intensity

        proj = V4.NodeOutput(g_maths.projection_matrix(), "R 3")

        with tree.layout("Light intensity"):

            direct = proj.dot(reflected)
            intensity = intensity*(direct**focus)


        for s in ["A", "B"]:
            with tree.layout(f"Normal {s} color"):

                front_col = mesh.named_color(f"Front Color {s}")
                back_col  = mesh.named_color(f"Back Color {s}")
                front_col = front_col.switch(-front_col.node.exists, (0., 0., 0., 1.))
                back_col  = back_col.switch( -back_col.node.exists,  (0., 0., 0., 1.))

                f = getattr(ref_node, f"front_{s}".lower())

                front_col = front_col.mix_add(f*intensity, color)
                back_col  = back_col.mix_add((1-f)*intensity, color)

                mesh.POINT.store_named_float_color(f"Front Color {s}", front_col)
                mesh.POINT.store_named_float_color(f"Back Color {s}",  back_col)


        tree.og = mesh + curve + cloud + inst

# ====================================================================================================
# Curves
# - Line
# - Circle
# - Spiral

def build_curves():

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - w from Curve

    with GeoNodes("W from Curve", fake_user=True, prefix=g_curves) as tree:

        curve    = tree.ig
        w_object = tree.object_input("W Curve", description="Z component is used to set curve W component")

        w_curve = w_object.object_info().geometry

        n = curve.domain_size(component='CURVE').point_count
        fac = curve.index/(n-1)

        curve.store_named_float("w", w_curve.sample_curve(factor=fac, mode='FACTOR').position.z)

        tree.og = curve



    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - A line

    with GeoNodes("Line", fake_user=True, prefix=g_curves) as tree:

        v0 = V4.Input(tree, "Start")
        v1 = V4.Input(tree, "End", (0., 0., 1., 0.))

        count = tree.integer_input("Resolution", 2, min_value=2)

        line = tree.curve_line(v0.V, v1.V).resample_curve(count)
        line.POINT.store_named_float("w", line.index.map_range(0, count-1, v0.w, v1.w))

        # Tangent is constant

        """
        (v1 - v0).normalized().set_tangent(line)
        """

        # Done

        tree.og = line

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Parametric Curve

    with GeoNodes("Parametric Curve", fake_user=True, prefix=g_curves) as tree:

        speed  = V4.Input(tree, "Speed", (0., 0., 0., 1.))

        r_xy   =  tree.float_input("Radius XY",           1., description="Radius in plane XY")
        om_xy  =  tree.angle_input("Omega XY",   tree.pi*1.5, description="Rotation speed in plane XY")
        r_zw   =  tree.float_input("Radius ZW",           0., description="Radius in plane ZW")
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

            x = speed.x*t + ca*r_xy
            y = speed.y*t + sa*r_xy
            z = speed.z*t + cb*r_zw
            w = speed.w*t + sb*r_zw

            curve.position = tree.xyz(x, y, z)
            curve.POINT.store_named_float("w", w)

        """
        # ===== Tangent
        # dx/dt = s - o.r.sin(o.t)

        with tree.layout("Tangent"):

            ro_xy = om_xy*r_xy
            ro_zw = om_zw*r_zw

            tx = speed.x - ro_xy*sa
            ty = speed.y + ro_xy*ca
            tz = speed.z - ro_zw*sb
            tw = speed.w + ro_zw*cb

            V4.Xyzw(tx, ty, tz, tw).normalized().set_tangent(curve)
        """

        tree.og = curve

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh along a curve

    with GeoNodes("Curve to Mesh", fake_user=True, prefix=g_curves) as tree:

        curve       = tree.ig

        resample    = tree.bool_input(     "Resample",    False)
        new_resol   = tree.integer_input(  "Resolution",  32, min_value=2)

        prof_object = tree.object_input(   "Mesh Profile", description="3D Mesh to instantiate along the curve")
        mat         = tree.material_input( "Material", bpy.data.materials.get("4 Face"))
        scale       = tree.float_input(    "Scale", 1.)
        use_radius  = tree.bool_input(     "Use Radius",  False, description="Use curve radius attribute")
        align_w     = tree.bool_input(     "Align w",     True,  description="Use mesh w axis along the curve tangent (z otherwise)")
        link_slices = tree.bool_input(     "Link slices", False, description="Link the instances between them")
        with_faces  = tree.bool_input(     "With Faces",  False, description="If the slices are linked, create surfaces between the instances.")
        sides_mat   = tree.material_input( "Sides Material", bpy.data.materials.get("4 Face"))

        # ----------------------------------------------------------------------------------------------------
        # The mesh to instantiate

        mesh = prof_object.object_info().geometry
        mesh.material = mat

        # ----- Instantiate

        mesh = g_maths.mesh_instances_on_curve(
            curve         = curve,
            mesh          = mesh,
            scale         = scale,
            use_radius    = use_radius,
            align_w       = align_w,
            resample      = resample,
            resolution    = new_resol).mesh

        # ----- Link the slices

        mesh = mesh.switch(link_slices, g_maths.link_slices(
            mesh           = mesh,
            count          = curve.domain_size(component='CURVE').point_count,
            with_faces     = with_faces,
            sides_material = sides_mat,
            ).mesh)

        # Done

        tree.og = mesh

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh along a curve

    with GeoNodes("Curve to Mesh with Spheres", fake_user=True, prefix=g_curves) as tree:

        curve       = tree.ig

        resample    = tree.bool_input(     "Resample",    False)
        new_resol   = tree.integer_input(  "Resolution",  32, min_value=2)

        resol       = tree.integer_input( "Sphere Resolution", 16, min_value=3)
        size        = tree.float_input(   "Size", 1.)
        use_radius  = tree.bool_input(    "Use Radius", False)
        align_w     = tree.bool_input(    "Align w",    True, description="Use mesh w axis along the curve tangent (z otherwise)")
        mat         = tree.material_input("Material", bpy.data.materials.get("4 Face"))
        link_slices = tree.bool_input(     "Link slices", False, description="Link the instances between them")
        with_faces  = tree.bool_input(     "With Faces",  False, description="If the slices are linked, create surfaces between the instances.")
        sides_mat   = tree.material_input( "Sides Material", bpy.data.materials.get("4 Face"))

        # ----------------------------------------------------------------------------------------------------
        # The mesh to instantiate

        sphere = tree.uv_sphere(rings=resol, segments=2*resol, radius=size)
        sphere.uv_map = sphere.node.uv_map
        sphere.material=mat

        # ----- Instantiate

        mesh = g_maths.mesh_instances_on_curve(
            curve         = curve,
            mesh          = sphere,
            scale         = size,
            use_radius    = use_radius,
            align_w       = align_w,
            resample      = resample,
            resolution    = new_resol).mesh

        # ----- Link the slices

        mesh = mesh.switch(link_slices, g_maths.link_slices(
            mesh           = mesh,
            count          = curve.domain_size(component='CURVE').point_count,
            with_faces     = with_faces,
            sides_material = sides_mat,
            ).mesh)

        # Done

        tree.og = mesh

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Tube on curves

    with GeoNodes("Curves profile", fake_user=True, prefix=g_curves) as tree:

        geo = tree.ig
        radius     = tree.float_input(   "Radius", .1)
        resol      = tree.integer_input( "Resolution", 8)
        mat        = tree.material_input("Material", bpy.data.materials.get("4 Edge"))
        ok_points  = tree.bool_input(    "With Points", False)
        pt_radius  = tree.float_input(   "Points Radius", .2)
        smooth     = tree.bool_input(    "Shade Smooth", True)

        comps = geo.separate_components()

        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances

        # ----- Profile

        meshed = curve.curve_to_mesh(profile_curve=tree.curve_circle(radius=radius, resolution=resol))

        # ----- Points

        sph = tree.uv_sphere(radius=pt_radius, rings=resol, segments=2*resol)
        sph.uv_map = sph.node.uv_map
        spheres = curve.instance_on_points(instance=sph)
        meshed  = meshed.switch(ok_points, meshed + spheres)

        # ----- Finalization

        meshed.material = mat
        meshed.shade_smooth = smooth

        # ----- Done

        tree.og = mesh + meshed + cloud + inst

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Mesh to curve (to see the edges)

    with GeoNodes("Mesh to Curve", fake_user=True, prefix=g_curves) as tree:

        geo         = tree.ig
        keep_faces  = tree.bool_input(    "Keep faces", False)

        use_profile = tree.bool_input(    "With Profile", True)
        radius      = tree.float_input(   "Radius", .01)
        resol       = tree.integer_input( "Resolution", 8)
        mat         = tree.material_input("Material", bpy.data.materials.get("4 Edge"))
        ok_points   = tree.bool_input(    "With Points", False)
        pt_radius   = tree.float_input(   "Points Radius", .02)
        smooth      = tree.bool_input(    "Shade Smooth", True)

        comps = geo.separate_components()

        mesh  = comps.mesh
        curve = comps.curve
        cloud = comps.point_cloud
        inst  = comps.instances

        # ----- To curve

        curved = mesh.mesh_to_curve() + curve

        # ----- Profile on the curve

        tubes_node = g_curves.curves_profile()
        tree.input_node.plug_to(tubes_node)
        # Replace geometry by curve only
        tubes_node.geometry = curved

        curved = curved.switch(use_profile, tubes_node.geometry)

        # ----- Done

        geo = curved + cloud + inst
        geo = geo.switch(keep_faces, tree.GEOMETRY(geo).join_geometry(mesh))

        tree.og = geo

# ====================================================================================================
# Surfaces

def build_surfaces():

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Extrude a mesh of a given offset

    with GeoNodes("Extrude", fake_user=True, prefix=g_surfs) as tree:

        mesh0      = tree.ig
        offset     = V4.Input(tree, "Offset", (0., 0., 1., 1.))
        with_faces = tree.bool_input(   "With Faces")
        mat        = tree.material_input("Sides Material", bpy.data.materials.get("4 Face"))
        keep0      = tree.bool_input("Keep first", True)
        keep1      = tree.bool_input("Keep last",  True)

        # ----------------------------------------------------------------------------------------------------
        # Dimensions

        dom_size = mesh0.domain_size(component='MESH')
        nverts = dom_size.point_count
        nedges = dom_size.edge_count

        # ----------------------------------------------------------------------------------------------------
        # Duplicate

        mesh1 = tree.GEOMETRY(mesh0)
        offset.set_offset(mesh1)

        # ----------------------------------------------------------------------------------------------------
        # Unique ID per vertex

        mesh0.POINT.store_named_int("vid", mesh0.index)
        mesh1.POINT.store_named_int("vid", mesh0.index + nverts)

        # ----------------------------------------------------------------------------------------------------
        # Loop on the edges

        with tree.repeat(iterations=nedges, faces=None, index=0) as rep:

            # ----- Create a new face

            with tree.layout("Face base"):
                face = tree.grid(vertices_x=2, vertices_y=2)
                edge_vertices = tree.EdgeVertices()

            with tree.layout("The four vertex indices"):
                indices = [
                    (mesh0, mesh0.EDGE.sample_index_int(edge_vertices.vertex_index_1, index=rep.index)),
                    (mesh0, mesh0.EDGE.sample_index_int(edge_vertices.vertex_index_2, index=rep.index)),
                    (mesh1, mesh1.EDGE.sample_index_int(edge_vertices.vertex_index_1, index=rep.index)),
                    (mesh1, mesh1.EDGE.sample_index_int(edge_vertices.vertex_index_2, index=rep.index)),
                    ]

            for i, (msh, vert_index) in enumerate(indices):
                with tree.layout(f"Vertex #{i}"):
                    v   = msh.POINT.sample_index_vector(msh.position,      index=vert_index)
                    w   = msh.POINT.sample_index_float(msh.named_int("w"), index=vert_index)
                    vid = msh.POINT.sample_index_int(msh.named_int("vid"), index=vert_index)
                    sel = face.index == i
                    face.POINT[sel].set_position(position=v)
                    face.POINT[sel].store_named_float("w", w)
                    face.POINT[sel].store_named_int("vid", vid)

            rep.faces += face
            rep.index += 1

        # ----------------------------------------------------------------------------------------------------
        # Finalization

        faces = rep.faces
        faces.material = mat

        edges_only = tree.GEOMETRY(faces).FACE.delete_geometry(mode='ONLY_FACE')
        mesh = edges_only.switch(with_faces, faces)

        mesh = mesh.switch(keep0, mesh0 + mesh)
        mesh = mesh.switch(keep1, mesh + mesh1)

        # ----------------------------------------------------------------------------------------------------
        # Remove duplicate indices

        with tree.repeat(iterations=nverts*2, mesh=mesh, index=0) as rep:
            rep.mesh[rep.mesh.named_int("vid") == rep.index].merge_by_distance(distance=1000.)
            rep.index += 1

        mesh = rep.mesh
        mesh.remove_named_attribute("vid")

        tree.og = mesh

    # ----------------------------------------------------------------------------------------------------
    # Hypercube

    with GeoNodes("Hypercube", fake_user=True, prefix=g_surfs) as tree:

        size   = tree.float_input(   "Size",       1., min_value=.01)
        slices = tree.integer_input( "Slices",     7,  min_value=1)
        mat    = tree.material_input("Material",   bpy.data.materials.get("4 Face"))

        cube = tree.cube()
        cube.material=mat
        V4.Xyzw(0., 0., 0., -size/2).set_offset(cube)

        tree.og = g_surfs.extrude(
            geometry       = cube,
            **V4.Xyzw(0., 0., 0., size).kwargs("Offset"),
            with_faces     = True,
            sides_material = mat,
            keep_first     = True,
            keep_last      = True,
            ).geometry


    # ----------------------------------------------------------------------------------------------------
    # Hypersphere

    with GeoNodes("Hypersphere", fake_user=True, prefix=g_surfs) as tree:

        radius = tree.float_input(   "Radius",       1., min_value=.01)
        resol  = tree.integer_input( "Resolution", 16, min_value=3)
        slices = tree.integer_input( "Slices",     7,  min_value=1)
        mat    = tree.material_input("Material",   bpy.data.materials.get("4 Face"))

        line = g_curves.line(start_v=0., start_w=-radius, end_v=0., end_w=radius, resolution=slices+2).geometry

        line.radius = tree.sqrt(tree.abs(radius**2 - line.named_float("w")**2))

        line[slices+1].POINT.delete_geometry()
        line[0].POINT.delete_geometry()

        hs = g_curves.curve_to_mesh_with_spheres(
            geometry   = line,
            sphere_resolution = resol,
            use_radius = True,
            align_w    = True,
            material   = mat,
            ).geometry

        hs.shade_smooth = True

        tree.og = hs


    # ----------------------------------------------------------------------------------------------------
    # Extrude along w

    with GeoNodes("Extrude w", fake_user=True, prefix=g_surfs) as tree:

        mesh     = tree.ig
        size_w   = tree.float_input("Offset w", 1.)
        as_curve = tree.bool_input("As curve", True)

        # ----- Start a minus size

        size_w /= 2
        mesh.POINT.store_named_float("w", -size_w)

        # ----- Extrude to plus size

        mesh.EDGE.extrude_mesh(offset_scale=0.)
        mesh.POINT[mesh.node.top].store_named_float("w", size_w)

        # ----- Return the result

        tree.og = mesh.switch(as_curve, mesh.mesh_to_curve())



    # ----------------------------------------------------------------------------------------------------
    # Torus

    with GeoNodes("Torus", fake_user=True, prefix=g_surfs) as tree:

        radius0 = tree.float_input(  "Radius XY",  1.)
        radius1 = tree.float_input(  "Radius ZW",  1.)
        resol   = tree.integer_input("Resolution", 32, min_value=3)
        factor0 = tree.factor_input( "Factor XY", 1., min_value=0, max_value=1.)
        factor1 = tree.factor_input( "Factor ZW", 1., min_value=0, max_value=1.)
        twists  = tree.float_input(  "Twists", 0, min_value=-10, max_value=10)
        mat     = tree.material_input("Material", bpy.data.materials.get("4 Face"))
        smooth  = tree.bool_input(    "Shade smooth", True)

        # ----------------------------------------------------------------------------------------------------
        # Starting from a grid

        grid = tree.grid(vertices_x=resol, vertices_y=resol)
        grid.uv_map = grid.node.uv_map
        a = (grid.index/resol)/(resol-1)
        b = (grid.index%resol)/(resol-1)

        #grid.position = (0.,0., 0.)
        #grid.POINT.store_named_float("w", 0.)

        # ----------------------------------------------------------------------------------------------------
        # Curve in the plane xy

        # ----- Line

        with tree.layout("XY Factor=0: straight line"):
            l_xy = (tree.pi*2)*radius0
            lx = 0.
            ly = a*l_xy - l_xy/2

            line0 = tree.GEOMETRY(grid)
            line0.position = (lx, ly, 0)

        # ----- Circle in plane XY

        with tree.layout("XY Curve lined up to Circle"):
            ag0 = (tree.pi*2)*factor0
            r0 = l_xy/ag0
            c0 = tree.xyz(0, -r0, 0)

            ag0_ = a*ag0 - ag0/2
            cx = r0*tree.cos(ag0_)
            cy = r0*tree.sin(ag0_)

            circle0 = tree.GEOMETRY(grid)
            circle0.position = (cx - r0 + factor0*radius0, cy, 0)

        #circle0 = circle0.switch(factor0.less_than(0.001), line0)
        circle0 = circle0.switch(factor0 < 0.001, line0)

        # ----------------------------------------------------------------------------------------------------
        # Curve in the plane zw

        # ----- Line

        with tree.layout("ZW Factor=0: straight line"):
            l_zw = (tree.pi*2)*radius1
            lz = 0.
            lw = b*l_zw - l_zw/2

            line1 = tree.GEOMETRY(circle0)
            line1.offset = (0., 0., lz)
            line1.POINT.store_named_float("w", lw)

        # ----- Circle in plane ZW

        with tree.layout("ZW Curve lined up to Circle"):
            ag1 = (tree.pi*2)*factor1
            r1 = l_zw/ag1
            c1 = tree.xyz(0, 0, 0)

            ag1_ = b*ag1 - ag1/2

            cz = r1*tree.cos(ag1_)
            cw = r1*tree.sin(ag1_)

            circle1 = tree.GEOMETRY(circle0)
            circle1.offset = (0., 0., cz - r1 + factor1*radius1)
            circle1.POINT.store_named_float("w", cw)

        circle1 = circle1.switch(factor1.less_than(0.001), line1)

        # ----- Twists

        with tree.layout("ZW Twist the profile"):

            y0 = circle0.sample_index_vector(circle0.position, circle1.index).y

            ag_twist = a*(tree.pi*twists)
            cost = tree.cos(a*ag_twist)
            sint = tree.sin(a*ag_twist)

            loc = circle1.position

            y = loc.y - y0

            y_ =   y*cost + loc.z*sint
            z_ =  -y*sint + loc.z*cost

            circle1.position = (loc.x, y0 + y_, z_)


        # ----- Finalize

        #circle1.merge_by_distance()
        circle1.material = mat
        circle1.shade_smooth = smooth

        tree.og = circle1

    # ----------------------------------------------------------------------------------------------------
    # Clifford Torus

    with GeoNodes("Clifford Torus", fake_user=True, prefix=g_surfs) as tree:

        tree.og = g_surfs.torus(
            radius_xy    = tree.float_input(  "Radius XY",  1.),
            radius_zw    = tree.float_input(  "Radius ZW",  1.),
            resolution   = tree.integer_input("Resolution", 32, min_value=3),
            factor_xy    = 1.,
            factor_zw    = 1.,
            twists       = 0.,
            material     = tree.material_input("Material", bpy.data.materials.get("4 Face")),
            shade_smooth = tree.bool_input(    "Shade smooth", True),
            ).geometry


    # ----------------------------------------------------------------------------------------------------
    # Klein Torus

    with GeoNodes("Klein Torus", fake_user=True, prefix=g_surfs) as tree:

        tree.og = g_surfs.torus(
            radius_xy    = tree.float_input(  "Radius XY",  1.),
            radius_zw    = tree.float_input(  "Radius ZW",  1.),
            resolution   = tree.integer_input("Resolution", 32, min_value=3),
            factor_xy    = 1.,
            factor_zw    = 1.,
            twists       = 1.,
            material     = tree.material_input("Material", bpy.data.materials.get("4 Face")),
            shade_smooth = tree.bool_input(    "Shade smooth", True),
            ).geometry

    # ----------------------------------------------------------------------------------------------------
    # 5 Cell

    with GeoNodes("5 Cell Polytope", fake_user=True, prefix=g_surfs) as tree:

        size = tree.float_input(   "Size", 1.)
        mat  = tree.material_input("Material", bpy.data.materials.get("4 Face"))

        from math import sqrt

        v0 = V4.Xyzw(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12),  1/2)
        v1 = V4.Xyzw(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12), -1/2)
        v2 = V4.Xyzw(1/2/sqrt(10),  1/2/sqrt(6), -2/sqrt(12),    0)
        v3 = V4.Xyzw(1/2/sqrt(10), -3/2/sqrt(6),           0,    0)
        v4 = V4.Xyzw( -2/sqrt(10),            0,           0,    0)

        S = tree.cone(vertices=3)

        S[0].position = v0.V*size
        S[0].store_named_float("w", v0.w)*size
        S[1].position = v1.V*size
        S[1].store_named_float("w", v1.w)*size
        S[2].position = v2.V*size
        S[2].store_named_float("w", v2.w)*size
        S[3].position = v3.V*size
        S[3].store_named_float("w", v3.w)*size

        S = S.extrude_mesh(mode='EDGES')
        top = S.node.top

        S[top].position=v4.V
        S[top].store_named_float("w", v4.w)

        S[top].merge_by_distance(distance=1)

        S.material = mat

        tree.og = S

    # ----------------------------------------------------------------------------------------------------
    # 16 Cell

    with GeoNodes("16 Cell Polytope", fake_user=True, prefix=g_surfs) as tree:

        size = tree.float_input(   "Size", 1.)
        mat  = tree.material_input("Material", bpy.data.materials.get("4 Face"))

        vs = [V4.Xyzw( 1.,  0.,  0.,  0.), V4.Xyzw( 0.,  1.,  0.,  0.), V4.Xyzw( 0.,  0.,  1.,  0.), V4.Xyzw( 0.,  0.,  0.,  1.),
              V4.Xyzw(-1.,  0.,  0.,  0.), V4.Xyzw( 0., -1.,  0.,  0.), V4.Xyzw( 0.,  0., -1.,  0.), V4.Xyzw( 0.,  0.,  0., -1.)]

        with tree.layout("Points coordinates (w on radius)"):
            points = tree.points(8)
            for i in range(8):
                sel = points.index == i
                points[sel].position     = vs[i].V*size
                points[sel].point_radius = vs[i].w*size


        # ----------------------------------------------------------------------------------------------------
        # Loops on triplets of points

        # ----- Loop on 6 vertices
        # The last 2 ones will have been taken into account in other triangles
        # index0 : from 0 to 5

        with tree.repeat(iterations=6, mesh=None, index=0) as rep0:

            # ----- Loop on up to 7 vertices greater than index 0
            # index1 : from 1 to 6

            opp0 = (rep0.index + 4).float_to_integer()

            with tree.repeat(iterations=7 - rep0.index, mesh=rep0.mesh, index=rep0.index + 1) as rep1:

                # ----- Loop on up to 6 vertices greater than index 1
                # index2 : from 2 to 7

                opp1 = (rep1.index + 4).float_to_integer()

                with tree.repeat(iterations=7 - rep1.index, mesh=rep1.mesh, index=rep1.index + 1) as rep2:

                    trg = tree.mesh_circle(vertices=3, fill_type='NGON')

                    for i, rep in enumerate([rep0, rep1, rep2]):

                        with tree.layout(f"Set triangle vertex #{i}"):
                            sel = trg.index == i
                            trg[sel].position = points.sample_index_vector(points.position, index=rep.index)
                            trg[sel].store_named_float("w", points.sample_index_vector(points.radius, index=rep.index))
                            trg[sel].store_named_int(  "vid", rep.index)

                    with tree.layout("Opposite edges don't exist"):
                        nope = (opp0 == rep1.index) | (opp0 == rep2.index) | (opp1 == rep2.index)
                        trg.store_named_boolean("_delete", nope)

                    rep2.mesh += trg
                    rep2.index += 1

                rep1.mesh  = rep2.mesh
                rep1.index += 1

            rep0.mesh   = rep1.mesh
            rep0.index += 1


        with tree.layout("Delete non existing edges"):
            mesh = rep0.mesh.POINT[mesh.named_boolean("_delete")].delete_geometry()
            mesh.remove_named_attribute("_delete")

        with tree.layout("Delete duplicates"):
            with tree.repeat(iterations=8, mesh = mesh, index=0) as rep:
                rep.mesh[rep.mesh.named_int("vid") == rep.index].merge_by_distance(distance=1)
                rep.index += 1

        mesh = rep.mesh

        mesh.material = mat


        mesh.to_output("Geometry")























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
