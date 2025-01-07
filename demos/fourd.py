#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/03/04

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/fourd
--------------------
Generates the fourd engine modifiers

The 4-position of a vertex is store in the first column of a Matrix (column with python index = 0, column 1 in editor).
The other columns are used to store normals:
- Surface : columns 1 and 2 store the two normals
- Curve : columns 1, 2, 3 store the three normals

updates
-------
- creation : 2024/03/04
- update   : 2024/08/07
- update   : 2024/08/03
- update   : 2024/01/03
"""


import bpy

from geonodes import *
from geonodes.core import utils

# ----- Prefixes

math_   = G.create_prefix("4-Math")
matrix_ = G.create_prefix("4-Matrix")
vector_ = G.create_prefix("4-Vector")
mod_    = G.create_prefix("4D")
curve_  = G.create_prefix("4-Curve")
surf_   = G.create_prefix("4_Surf")
debug_  = G.create_prefix("DEBUG")

ZERO = 0.0001

V4_COL = (.3, .1, .1)

PARAMETERS_OBJECT = "4D Parameters"

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

    Tree._display_counter("4D Engine built")
    #print(f"4D Engine built : {Tree._total_nodes} nodes, {Tree._total_links} links in {Tree._total_time:.1f} s")
    print()

# =============================================================================================================================
# Shaders
# =============================================================================================================================

def build_shaders():

    # ----------------------------------------------------------------------------------------------------
    # Axis Shader

    with ShaderNodes("4 Axis"):

        col = snd.attribute(attribute_name="Color").color_

        ped = Shader.Principled(base_color=col, roughness=.1, metallic=.3)

        ped.out()

    # ----------------------------------------------------------------------------------------------------
    # Face default

    with ShaderNodes("4 Face"):

        noise = Texture.Noise(scale=5.)
        bump = snd.bump(height=noise.color_, strength=.1)

        ped = Shader.Principled(
            base_color = (.3, .8, .7),
            metallic   = 0.,
            roughness  = 0.,
            alpha      = .1,
            normal     = bump,
            )

        ped.out()

    # ----------------------------------------------------------------------------------------------------
    # Edge default

    with ShaderNodes("4 Edge"):

        ped = Shader.Principled(
            base_color = (0., .05, .9),
            roughness  = 0.,
            )

        ped.out()

# =============================================================================================================================
# DEBUG

def build_debug():

    # ----------------------------------------------------------------------------------------------------
    # DEBUG - Dump the four components of a Vector

    with GeoNodes("Dump Vector", is_group=True, prefix=debug_):

        V = [0]*4
        V[0] = Float(0, "x")
        V[1] = Float(0, "y")
        V[2] = Float(0, "z")
        V[3] = Float(0, "w")

        decimals = Integer(3, "Decimals")
        size = Float(3, "Size")
        offset = Vector(0, "Offset")

        cloud = Mesh.LineEndPoints(start_location = (0, size*(-.5), 0), end_location=(0, size/2, 0), count=4).points.to_points()

        for i in range(4):
            cloud.points[i]._Value = V[3 - i]

        with cloud.points.for_each(position=nd.position, value=Float("Value")) as feel:

            label = feel.value.to_string(decimals=decimals).to_curves(size=.3, align_x='CENTER')
            label.transform(translation=feel.position)

            feel.generated.geometry = Curve(label.realize()).fill()

        geo = feel.generated.geometry
        geo.transform(translation=offset)
        geo.out()

        cloud.out(name="Cloud")

    # ----------------------------------------------------------------------------------------------------
    # DEBUG - Dump the content of a matrix

    with GeoNodes("Dump Matrix", is_group=True, prefix=debug_):

        M = Matrix(None, name="Matrix")
        decimals = Integer(3, "Decimals")
        size = Float(3, "Size")
        offset = Vector(0, "Offset")

        cloud = Mesh.Grid(size_x=size, size_y=size, vertices_x=4, vertices_y=4).points.to_points()

        a = M.separate
        for i, v in enumerate(a):
            j = (i//4)*4 + 3 - i%4
            cloud.points[j]._Value = v

        with cloud.points.for_each(position=nd.position, value=Float("Value")) as feel:

            label = feel.value.to_string(decimals=decimals).to_curves(size=.3, align_x='CENTER')
            label.transform(translation=feel.position)

            feel.generated.geometry = Curve(label.realize()).fill()

        geo = feel.generated.geometry
        geo.transform(translation=offset)
        geo.out()

        cloud.out(name="Cloud")

    # ----------------------------------------------------------------------------------------------------
    # DEBUG - Dump a matrix

    with GeoNodes("Dump Matrix at Index", prefix=debug_):
        geo = Cloud(Geometry())
        index = Integer(0, "Index")
        use_M4 = Boolean(True, "Use M4")
        M = Matrix(None, "Matrix")

        M = M.switch(use_M4, Matrix("M4"))

        M4 = geo.points.sample_index(M, index=index)
        vis_mat = debug_.dump_matrix(matrix=M4, link_from='TREE')

        sph = Mesh.UVSphere(radius=.1)
        sph.offset = geo.points.sample_index(nd.position, index=index)

        Geometry.Join(geo, sph, vis_mat).out()


    # ----------------------------------------------------------------------------------------------------
    # DEBUG - Dump operation

    with GeoNodes("Dump Matrix Operation", is_group=True, prefix=debug_):

        A = Matrix(None, name="A")
        B = Matrix(None, name="B")
        C = Matrix(None, name="C")

        vis_A = debug_.dump_matrix(A, offset = (-5, 0, 0), link_from='TREE')
        vis_B = debug_.dump_matrix(B, offset = (0, 5, 0), link_from='TREE')
        vis_C = debug_.dump_matrix(C, offset = 0, link_from='TREE')

        vis_A.transform(translation=(-5, 0, 0))
        vis_B.transform(translation=(0, 5, 0))

        Geometry.Join(vis_A, vis_B, vis_C).out()

# =============================================================================================================================
# V4 coordinates class

class V4:
    """ This class provides help to handle the four V4 components names x, y, z, w
    """
    def __init__(self, *values, panel=None):

        if len(values) == 0:
            a = [0]*4

        elif len(values) == 1:
            value = values[0]
            if isinstance(value, V4):
                a = value.a
            elif isinstance(value, (list, tuple)):
                assert(len(value) == 4)
                a = value
            else:
                a = [value, value, value, value]

        elif len(values) == 4:
            a = values

        else:
            assert(False)

        if panel is None:
            self.x, self.y, self.z, self.w = a
            for i in range(4):
                v = self[i]
                if hasattr(v, 'node') and 'x' not in [sock.name for sock in v.node._bnode.outputs]:
                    v._lc("xyzw"[i])
        else:
            with Panel(panel):
                self.x, self.y, self.z, self.w = [Float(a[i], "xyzw"[i]) for i in range(4)]

    @classmethod
    def FromNode(cls, node):
        return cls(node.x, node.y, node.z, node.w)

    def out(self):
        for v, label in zip(self, "xyzw"):
            v.out(label)

    def args(self, panel=None):
        if panel is None:
            name = ""
        else:
            name = utils.snake_case(panel) + '_'
        return {name + "xyzw"[i]: self[i] for i in range(4)}

    def __str__(self):
        return f"<V4 {[str(self[i]) for i in range(4)]}>"

    def dump(sef, offset=(0, 0, 0)):
        return debug_.dump_vector(*self, offset=offset)

    # ====================================================================================================
    # Interface

    @property
    def a(self):
        return [self.x, self.y, self.z, self.w]

    @a.setter
    def a(self, value):
        self.x, self.y, self.z, self.w = value

    def __len__(self):
        return 4

    def __getitem__(self, index):
        return self.a[index]

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        elif index == 3:
            self.w = value
        else:
            assert(False)

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index == 4:
            raise StopIteration

        else:
            v = self.a[self._iter_index]
            self._iter_index += 1
            return v

    # ====================================================================================================
    # Implement the operations node groups

    @staticmethod
    def build_operations():

        # ----------------------------------------------------------------------------------------------------
        # Swith two 4-vector

        with GeoNodes("Switch", is_group=True, prefix=vector_):
            switch = Boolean(False, "Switch")
            false  = V4(panel="False")
            true   = V4(panel="True")
            V4([false[i].switch(switch, true[i]) for i in range(4)]).out()

        # ----------------------------------------------------------------------------------------------------
        # Dot product

        with GeoNodes("Dot", is_group=True, prefix=vector_):
            v0 = V4(panel="First")
            v1 = V4(panel="Second")

            (v0.x*v1.x + v0.y*v1.y + v0.z*v1.z + v0.w*v1.w).out("Dot")

        # ----------------------------------------------------------------------------------------------------
        # Scale

        with GeoNodes("Scale", is_group=True, prefix=vector_):
            scale = Float(1, "Scale")
            v = V4(panel="Vector")

            V4([scale*v[i] for i in range(4)]).out()

        # ----------------------------------------------------------------------------------------------------
        # Math

        with GeoNodes("Math", is_group=True, prefix=vector_):
            v0 = V4(panel="First")
            v1 = V4(panel="Second")

            with Layout("Add"):
                add = V4([v0[i] + v1[i] for i in range(4)])

            with Layout("Subtract"):
                sub = V4([v0[i] - v1[i] for i in range(4)])

            with Layout("Multiply"):
                mul = V4([v0[i] * v1[i] for i in range(4)])

            with Layout("Divide"):
                dvd = V4([v0[i] / v1[i] for i in range(4)])

            index = Integer.MenuSwitch({"Add": 0, "Subtract": 1, "Multiply": 2, "Divide": 3}, menu=0, name="Operation")

            V4([Float.IndexSwitch(add[i], sub[i], mul[i], dvd[i], index=index)for i in range(4)]).out()

        # ----------------------------------------------------------------------------------------------------
        # Square Length of a 4-vector

        with GeoNodes("Square Length", is_group=True, prefix=vector_):
            v = V4(panel="Vector")
            length2 = vector_.dot(*v, *v)

            length2.out("Square Length")
            (length2 < ZERO).out("Null")

        # ----------------------------------------------------------------------------------------------------
        # Length of a 4-vector

        with GeoNodes("Length", is_group=True, prefix=vector_):
            v = V4(panel="Vector")

            length2 = vector_.square_length(*v)

            gnmath.sqrt(length2).out("Length")
            length2.null_.out("Null")

        # ----------------------------------------------------------------------------------------------------
        # Normalize of a 4-vector

        with GeoNodes("Normalize", is_group=True, prefix=vector_):

            normalize = Boolean(True, "Normalize")

            v       = V4(panel="Vector")
            default = V4(panel="Default")

            length2 = vector_.square_length(*v)
            null = length2.null_

            normalized = V4.FromNode(vector_.switch(null,
                *V4.FromNode(vector_.scale(gnmath.inverse_sqrt(length2), *v).node),
                *default).node)

            vector_.switch(normalize, *v, *normalized).node.out()
            null.out("Null")

        # ----------------------------------------------------------------------------------------------------
        # Matrix dot vector

        with GeoNodes("Dot Vector", is_group=True, prefix=matrix_):
            M = Matrix(None, "M")
            x, y, z, w = V4(panel="Vector").a

            a = M.separate
            for i in range(4):
                (a[i]*x + a[i + 4]*y + a[i + 8]*z + a[i + 12]*w).out("xyzw"[i])

        # ----------------------------------------------------------------------------------------------------
        # Component of a Vector perpendicular to an axis

        with GeoNodes("Perpendicular to Axis", is_group=True, prefix=vector_):

            v    = V4(panel="Vector")
            axis = V4(panel="Axis")

            with Panel("Options"):
                normalize_axis = Boolean(False, "Normalize Axis")
                normalize_out  = Boolean(True,  "Normalize Result")

            axis = axis.normalize(normalize_axis)

            dot = v.dot(axis)

            (v - axis.scale(dot)).normalize(normalize_out).out()

    # ====================================================================================================
    # Operations

    def switch(self, switch, true):
        return V4.FromNode(vector_.switch(switch, *self, *true).node)

    @property
    def square_length(self):
        return vector_.square_length(self)

    @property
    def length(self):
        return vector_.length(*self)

    def dot(self, other):
        return vector_.dot(*self, *other)

    def scale(self, factor):
        return V4.FromNode(vector_.scale(factor, *self).node)

    def normalize(self, normalize=True, default=(1, 0, 0, 0)):
        return V4.FromNode(vector_.normalize(normalize, *self, *default).node)

    def matmul(self, M):
        return V4.FromNode(matrix_.dot_vector(M, *self).node)

    def perpendicular_to(self, axis, normalize_axis=False, normalize_result=True):
        return V4.FromNode(vector_.perpendicular_to_axis(*self, *axis, normalize_axis=normalize_axis, normalize_result=normalize_result).node)

    def __neg__(self):
        with Layout("- 4-Vector"):
            return V4(-self.x, -self.y, -self.z, -self.w)

    def __add__(self, other):
        return V4.FromNode(vector_.math('Add', *self, *other).node)

    def __sub__(self, other):
        return V4.FromNode(vector_.math('Subtract', *self, *other).node)

    def __mult__(self, other):
        return V4.FromNode(vector_.math('Multiply', *self, *other).node)

    def __truediv__(self, other):
        return V4.FromNode(vector_.math('Divide', *self, *other).node)

# =============================================================================================================================
# Basic operations
#
# Basic operations are put in groups rather than macros to make trees more compact

def build_operations():

    # ----------------------------------------------------------------------------------------------------
    # 4-Vector Operations

    V4.build_operations()

    # ----------------------------------------------------------------------------------------------------
    # Rotate a M4 Matrix
    # Equivalent to rot @ M4

    with GeoNodes("Rotate M4", is_group=True, prefix=matrix_):

        rot = Matrix(None, "Rotation")
        M4  = Matrix(None, "M4")

        m = M4.separate
        a = []
        for i in range(4):
            U = V4(m[4*i:4*(i+1)])
            node = matrix_.dot_vector(rot, *U).node
            a.extend([node.x, node.y, node.z, node.w])

        Matrix(a).out()

    # ----------------------------------------------------------------------------------------------------
    # Roll a matrix

    with GeoNodes("Roll", is_group=True, prefix=matrix_):

        M = Matrix(None, "Matrix")
        count = Integer(0, "Count", 0, 3) % 4

        a = M.separate

        Ms = [M]
        for roll in range(1, 4):
            with Layout(f"Roll {roll} steps"):

                b = list(a)
                for i in range(4):
                    j = (i + roll)%4

                    b[4*j:4*(j+1)] = a[4*i:4*(i+1)]

                c = list(b)
                for i in range(4):
                    j = (i + roll)%4

                    c[4*i + (0 + j)%4] = b[4*i + (0 + i)%4]
                    c[4*i + (1 + j)%4] = b[4*i + (1 + i)%4]
                    c[4*i + (2 + j)%4] = b[4*i + (2 + i)%4]
                    c[4*i + (3 + j)%4] = b[4*i + (3 + i)%4]

                Ms.append(Matrix(c))

        Matrix.IndexSwitch(*Ms, index=count).out()

    # ----------------------------------------------------------------------------------------------------
    # Cross product between 3 4-Vectors

    with GeoNodes("Cross Product", is_group=True, prefix=vector_):

        # https://www.researchgate.net/publication/318543243_Vector_Cross_Product_in_4D_Euclidean_Space_A_Maple_worksheet

        ux, uy, uz, uw = V4(panel="V0")
        vx, vy, vz, vw = V4(panel="V1")
        t = V4(panel="V2")

        normalize = Boolean(False, "Normalize")

        b = [       0      ,  uw*vz - uz*vw, -uw*vy + uy*vw, -uy*vz + uz*vy,
                -uw*vz + uz*vw,         0     ,  uw*vx + ux*vw,  ux*vz - uz*vx,
                uw*vy - uy*vw, -uw*vx + ux*vw,         0     , -ux*vy + uy*vx,
                uy*vz - uz*vy, -ux*vz + uz*vx,  ux*vy - uy*vx,        0       ]
        S = Matrix(b)

        V = V4(t).matmul(S)

        V.normalize(normalize).out()

    # ----------------------------------------------------------------------------------------------------
    # Rotation 3D

    with GeoNodes("3D Rotation", is_group=True, prefix=matrix_):

        M     = Matrix(None, "Matrix")
        R     = Rotation(None, "Rotation")
        index = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2, 'W': 3}, menu='W', name="Axis")

        M_rot = Matrix.CombineTransform(rotation=R)
        M_rot = matrix_.roll(M_rot, count=(1+index)%4)
        M = M @ M_rot
        M.out()

    # ----------------------------------------------------------------------------------------------------
    # Cross product between 3 4-Vectors

    with GeoNodes("Cross Product", is_group=True, prefix=matrix_):

        # https://www.researchgate.net/publication/318543243_Vector_Cross_Product_in_4D_Euclidean_Space_A_Maple_worksheet

        M = Matrix(None, "Vectors", tip="Col 1 is unknown, cols 2 to 4 are the 3 axis")

        normalize = Boolean(True, "Normalize")

        a = list(M.separate)

        ux, uy, uz, uw = tuple(a[ 4: 8])
        vx, vy, vz, vw = tuple(a[ 8:12])
        t = tuple(a[12:16])

        b = [       0      ,  uw*vz - uz*vw, -uw*vy + uy*vw, -uy*vz + uz*vy,
                -uw*vz + uz*vw,         0     ,  uw*vx + ux*vw,  ux*vz - uz*vx,
                uw*vy - uy*vw, -uw*vx + ux*vw,         0     , -ux*vy + uy*vx,
                uy*vz - uz*vy, -ux*vz + uz*vx,  ux*vy - uy*vx,        0       ]
        S = Matrix(b)

        V = V4(t).matmul(S)

        V = V.normalize(normalize)
        V.out()

        a[:4] = V.a
        Matrix(a).out()





    # ----------------------------------------------------------------------------------------------------
    # Align a 4-rotation to a vector

    with GeoNodes("Align Axis to Vector", is_group=True, prefix=matrix_):

        #axis     = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2, 'W': 3}, menu='Z', name='Axis')
        vector   = V4(panel="Vector")

        # Initial basis is [i j k l]. We want basis [t u v w]
        # Let's name t the vector to align with and let's align x to it.
        # First step is M = [t ? ? ?]
        #
        # We decompose j along t and a vector u perpendicular to t:
        # > j = at + bu
        # If b is null, it does mean that t is aligned with j, we can end here and take M = [t k l i]
        # Otherwise we can take M = [t u ? ?]
        #
        # We decompose k along t, u and a perpendicular vector v
        # > k = ct + du + ev
        # If e is null, k is in the plane (u, t), we take l rather than k:
        # > l = ct + du + ev, e is not null for sure
        # We take v as third component: M = [t u v ?]
        #
        # The third vector is the 4-cross product or t, u, v

        T = vector.normalize()

        with Layout("Decompose J along target and U, a vector perp to target"):

            J = V4(0, 1, 0, 0)
            a = J.dot(T)
            U = J - T.scale(a)
            U = U.normalize()
            null = U.x.null_

            a = [0]*16
            a[1]  = 1
            a[4]  = 1
            a[10] = 1
            a[15] = 1
            U = U.switch(null, (0, 0, 1, 0))
            V = V4((0, 0, 0, 1))
            done = null

        Vs = []
        for i in range(2):
            with Layout(f"Decompose {'KL'[i]} along target, U and V, a perpendicular vector"):

                K = V4([(0, 0, 1, 0), (0, 0, 0, 1)][i])

                c = K.dot(T)
                V_ = (K - T.scale(c)).normalize()

                d = V_.dot(U)
                Vs.append((V_ - U.scale(d)).normalize())

        V = Vs[0].switch(Vs[0].x.null_, Vs[1]).switch(done, V)

        W = V4.FromNode(vector_.cross_product(True, *T, *U, *V).node)

        M = Matrix([*T, *U, *V, *W])

        matrix_._3d_rotation(matrix=M, link_from='TREE').out()


# =============================================================================================================================
# Matrices groups
# - Math Rotation Matrix
# - Math Arrow
# - 4D Parameters
# - Math Projection Matrix
# - Plunge into 4D
# - 4D Projection

def build_matrices():

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Rotation Matrix
    #
    # A "2-rotation" is composed of two rotations in two perpendicular planes
    # A rotation matrix is the combination of the 3 possible 2-rotations made with the axes

    with GeoNodes("Rotation Matrix", is_group=True, prefix=matrix_):

        panel_name = "Rotation 4D"

        with Panel(panel_name):
            w_euler = Vector.Euler(0, "W Euler", tip="Rotation XW, YW, ZW")
            euler   = Vector.Euler(0, "3D Euler", tip="Rotation YZ, ZX, XY")

        xw, yw, zw = w_euler.xyz
        yz, zx, xy = euler.xyz

        with Layout("Rotation XW / YZ"):
            ca, sa = gnmath.cos(xw), gnmath.sin(xw)
            c2, s2 = gnmath.cos(yz), gnmath.sin(yz)

            X = Matrix((
                ca,  0,   0, -sa,
                 0, c2,  s2,   0,
                 0,-s2,  c2,   0,
                sa,  0,   0,  ca,
            ))

        with Layout("Rotation YW / ZX"):
            ca, sa = gnmath.cos(yw), gnmath.sin(yw)
            c2, s2 = gnmath.cos(zx), gnmath.sin(zx)

            Y = Matrix((
                c2,  0,-s2,   0,
                0, ca,  0,  sa,
                s2,  0, c2,   0,
                0,-sa,  0,  ca,
            ))

        with Layout("Rotation ZW / XY"):
            ca, sa = gnmath.cos(zw), gnmath.sin(zw)
            c2, s2 = gnmath.cos(xy), gnmath.sin(xy)

            Z = Matrix((
                c2, s2,  0,   0,
               -s2, c2,  0,   0,
                0,   0, ca, -sa,
                0,   0, sa,  ca,
            ))

        with Layout("Order XYZ"):
            XYZ = X @ (Y @ Z)

        with Layout("Order XZY"):
            XZY = X @ (Z @ Y)

        with Layout("Order YXZ"):
            YXZ = Y @ (X @ Z)

        with Layout("Order YZX"):
            YZX = Y @ (Z @ X)

        with Layout("Order ZXY"):
            ZXY = Z @ (X @ Y)

        with Layout("Order ZYX"):
            ZYX = Z @ (Y @ X)

        with Panel(panel_name):
            Matrix.MenuSwitch({'XYZ': XYZ, 'XZY': XZY, 'YXZ': YXZ, 'YZX': YZX, 'ZXY': ZXY, 'ZYX': ZYX, }, menu='XYZ', name='Order').out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Arrow
    #
    # An array along a 4D vector
    # The array is defined by a matrix:
    # - row 1 : Location
    # - row 2 : Direction
    #
    # Note : this group needs to get the projection Matrix because it is used by the "4D Parameters" Groupe

    with GeoNodes("Arrow", is_group=True, prefix=math_):

        cloud = Cloud(Geometry())

        with Panel("Shape"):
            length = Float(          1, "Length", tip= "Arrow length")
            radius = Float(        .05, "Radius", 0.01)
            resol  = Integer(        8, "Resolution", 3, 32)
            mat    = Material("4 Axis", "Material")

        M_proj = Matrix(None, "Projection Matrix")

        with Layout("Project the extremities"):

            M = Matrix("M4")

            a = list(M.separate)
            a[4], a[5], a[6], a[7] = a[4]*length, a[5]*length, a[6]*length, a[7]*length
            M = Matrix(a)

            m3 = M_proj @ M
            a = m3.separate

            cloud.position = a[:3]

            arrow = Vector(a[4:7])
            ar_length = arrow.length

            rot = Rotation.AlignZToVector(arrow)

        with Layout("Arrow Shaft"):
            line = Curve.LineDirection()
            lines = cloud.instance_on(instance=line, scale=ar_length, rotation=rot)
            lines = Curve(lines.realize())

            arrows = lines.to_mesh(profile_curve=Curve.Circle(radius=radius, resolution=resol))

        with Layout("Arrow Head"):
            cone_height = 9*radius

            cone = Mesh.Cone(radius_bottom=3.5*radius, depth=9*radius, vertices=resol)
            cone.corners.store_uv = cone.uv_map_

            cones = cloud.instance_on(instance=cone)
            cones.translate(arrow)
            cones.rotate(rot)

            arrows += Mesh(cones.realize())

        arrows.material = mat
        arrows.faces.shade_smooth = True

        arrows.out()

    # ====================================================================================================
    # The 4D parameters
    # The projection matrix is defined once on the object named Projection
    # on which the modifier "4D Parameters is applied"

    # ----------------------------------------------------------------------------------------------------
    # The modifier to apply to one object named "4D Parameters"

    with GeoNodes("4D Parameters"):

        M = matrix_.rotation_matrix(link_from='TREE')

        with Panel("Show Axes"):
            show_axis = Boolean(True, "Show Axes", tip="Show the 4 axes")
            neg       = Float(-1, "Negative", max=0)
            pos       = Float(3,  "Positive", 0)

        cloud = Cloud.Points(count=4)

        for i in range(4):
            with Layout(f"Axis {i}"):
                a = [[0., 0., 0., 0.] for j in range(4)]
                a[0][i] = neg
                a[1][i] = 1

                cloud.points[i]._M4 = Matrix(a)

                col = [0, 0, 0]
                if i < 3:
                    col[i] = 1
                cloud.points[i]._Color = Color(col)

        geo = math_.arrow(cloud, projection_matrix=M, length=pos - neg, link_from='TREE')

        cloud = Cloud.Points(1)
        cloud.points._Projection = M

        cloud.switch(show_axis, cloud + geo).out()

    # ----------------------------------------------------------------------------------------------------
    # Create the object "4D Parameters"

    def set_4D_parameters():
        obj = bpy.data.objects.get(PARAMETERS_OBJECT)
        if obj is None:
            print(f"Create '{PARAMETERS_OBJECT}' object")
            mesh = bpy.data.meshes.new(PARAMETERS_OBJECT)
            obj = bpy.data.objects.new(PARAMETERS_OBJECT, mesh)
            bpy.context.scene.collection.objects.link(obj)
        else:
            print(f"Object '{obj.name}' exists")

        if not len(obj.modifiers):
            modifier = obj.modifiers.new("Geometry Nodes", type='NODES')
            modifier.node_group = bpy.data.node_groups["4D Parameters"]

    # ----------------------------------------------------------------------------------------------------
    # Create the Parameter Object

    set_4D_parameters()

    # ----------------------------------------------------------------------------------------------------
    # Projection Matrix

    with GeoNodes("Projection Matrix", is_group=True, prefix=matrix_):

        cloud = Object.info(PARAMETERS_OBJECT).geometry.point_cloud
        M_proj = cloud.points.sample_index(Matrix("Projection"), 0)
        M_proj.out()

    # ----------------------------------------------------------------------------------------------------
    # Plunge into 3D

    with GeoNodes("Plunge into 4D", prefix=mod_):

        geo       = Geometry()
        w         = Float(0, "w", tip="Fourth dimension value")
        curve_res = Integer(0, "Curve Resample", min=0, tip="Resample curve (0 or 1 for no resample)")


        mesh  = geo.mesh
        curve = geo.curve
        cloud = geo.point_cloud

        x, y, z = nd.position.xyz
        a = [0]*16
        a[0], a[1], a[2], a[3] = x, y, z, w

        with Layout("Mesh"):
            a[4:7] = nd.normal.xyz  # 4:8  = (nx, ny, nz, 0) first normal
            a[15]   = 1             # 12:16 = (0, 0, 0, 1) second normal

            mesh.points._M4 = a

        with Layout("Curve"):
            curve = curve.switch(curve_res > 1, Curve(curve).resample(curve_res))
            n1 = nd.normal
            n2 = Curve.tangent.cross(n1)
            a[ 4: 7] = n1.xyz  # 4:8   = first normal
            a[ 8:11] = n2.xyz  # 8:12  = second normal
            a[15]    = 1       # 12:16 = (0, 0, 0, 1) last normal

            curve.points._M4 = a

        with Layout("Cloud"):
            cloud.points._M4 = a

        plunged = Cloud.Join(mesh, curve, cloud)

        with Layout("Already Plunged"):
            exists = Cloud(geo).points.sample_index(Matrix("M4").exists_, 0)

            plunged.switch(exists, geo).out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Perform a projection

    with GeoNodes("Projection", prefix=mod_):

        geo = Geometry()

        with Panel("Faces"):
            del_faces   = Boolean(False,        "Delete Faces")
            face_smooth = Boolean(True,         "Face Smooth")
            face_mat    = Material("4 Face",    "Face Material")

        with Panel("Edges"):
            edge_radius = Float(0,              "Edge Radius", 0)
            edge_resol  = Integer(12,           "Edge Resolution", 3, 16)
            edge_mat    = Material("4 Edge",    "Edge Material")

        with Panel("Points"):
            point_radius = Float(0,             "Point Radius", 0)
            point_mat    = Material("4 Edge",   "Point Material")

        with Panel("Debug"):
            show_normals  = Boolean(False, "Show Normals",  tip="Show mesh normals")
            show_tangents = Boolean(False, "Show Tangents", tip="Show curve tangents")
            vect_length   = Float(1, "Vectors length", tip="Length of normals / tangents")

        with Layout("Projection into 3D Space"):

            M = Matrix("M4")
            M_proj = matrix_.projection_matrix()

            m = M_proj @ M

            a = m.separate
            geo.position = a[:3]

        mesh  = geo.mesh
        curve = geo.curve
        cloud = geo.point_cloud

        line = Curve.LineDirection(length=vect_length)

        with Layout("Mesh Normals"):
            vis  = mesh.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[4:7]))
            vis += mesh.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[8:11]))

            visualization = vis.switch(-show_normals)

        with Layout("Curve Normals & Tangents"):
            curve.points._Tangent = a[4:7]

            vis  = curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[ 4:7]))
            vis += curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[ 8:11]))
            vis += curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[12:15]))

            visualization = visualization.switch(show_normals, visualization + vis)

            tg = V4.FromNode(matrix_.cross_product(M).node)
            tg = tg.matmul(M_proj)

            vis = curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(tg[:3]))

            visualization = visualization.switch(show_tangents, visualization + vis)

        with Layout("Points"):
            spheres = Cloud(geo).points.instance_on(instance=Mesh.UVSphere(radius=point_radius))
            spheres = Mesh(spheres.realize())
            spheres.faces.smooth = True
            spheres.faces.material = point_mat

            visualization = visualization.switch(point_radius > ZERO, visualization + spheres)

        with Layout("Edges"):
            edges = mesh.to_curve().to_mesh(profile_curve=Curve.Circle(radius=edge_radius))
            edges.faces.smooth = True
            edges.faces.material = edge_mat

            visualization = visualization.switch(edge_radius > ZERO, visualization + edges)

        with Layout("No Faces"):

            no_faces = Mesh(mesh).faces.delete_only_face()

        with Layout("With Faces"):

            with_faces = Mesh(mesh)
            with_faces.faces.smooth = face_smooth
            with_faces.faces.material = face_mat

        mesh = with_faces.switch(del_faces, no_faces)

        Geometry.Join(mesh, curve, cloud, visualization).out()

    # ----------------------------------------------------------------------------------------------------
    # Resolution system de deux équations à deux inconnues
    # a0x + b0y = c0
    # a1x + b1y = c1
    #
    # D = a0b1 - a1b0
    # x = (b1c0 - b0c1)/D
    # y = (a0c1 - a1c0)/D

    with GeoNodes("Two equations solver", is_group=True, prefix=math_):

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

    with GeoNodes("Translation", fake_user=False, prefix=mod_):

        geo = Cloud(Geometry())
        trans = V4(panel="Translation")

        a = list(Matrix("M4").separate)
        for i in range(4):
            a[i] += trans[i]

        geo.points._M4 = a
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Scale

    with GeoNodes("Scale", fake_user=False, prefix=mod_):

        geo = Cloud(Geometry())

        scale = V4(1, 1, 1, 1, panel="Scale")
        pivot = V4(panel="Pivot")

        a = list(Matrix("M4").separate)
        for i in range(4):
            a[i] = pivot[i] + scale[i]*(a[i] - pivot[i])

        geo.points._M4 = a
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Rotation

    with GeoNodes("Rotation", fake_user=False, prefix=mod_):

        geo = Geometry()

        pivot = V4(panel="Pivot")

        M = matrix_.rotation_matrix(link_from='TREE')

        geo = Cloud(mod_.translation(geo, *(-pivot)))

        M4 = Matrix("M4")

        R = M @ M4

        geo.points._M4 = R

        mod_.translation(geo, *pivot).out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Swap Axes

    def swap_axes(a, ax0, ax1):
        b = list(a)
        for i in range(4):
            b[4*i + ax0] = a[4*i + ax1]
            b[4*i + ax1] = a[4*i + ax0]

        return b

    with GeoNodes("Swap Axes", prefix=mod_):

        geo = Cloud(Geometry())
        axis_0 = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2, 'W': 3}, menu='X', name='Axis 1')
        axis_1 = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2, 'W': 3}, menu='X', name='Axis 2')
        swap = Boolean(True, "Swap Axes")
        swap_other = Boolean(False, "Swap Other Axes")

        M4 = Matrix("M4")
        a = M4.separate

        for i0 in range(3):
            for i1 in range(i0 + 1, 4):
                with Layout(f"Swap axis {'XYZW'[i0]} with {'XYZW'[i1]}"):
                    ok  = axis_0.equal(i0) & axis_1.equal(i1)
                    ok |= axis_0.equal(i1) & axis_1.equal(i0)
                    ok &= swap

                    sym = swap_other
                    sym &= axis_0.not_equal(i0) & axis_1.not_equal(i0)
                    sym &= axis_0.not_equal(i1) & axis_1.not_equal(i1)

                    ok |= sym

                    M4 = M4.switch(ok, swap_axes(a, i0, i1))

        geo.points._M4 = M4

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Roll Axes

    def roll_axes(a, count):
        b = list(a)
        for i in range(4):
            b[4*i + count]           = a[4*i + 0]
            b[4*i + ((1 + count)%4)] = a[4*i + 1]
            b[4*i + ((2 + count)%4)] = a[4*i + 2]
            b[4*i + ((3 + count)%4)] = a[4*i + 3]

        return b

    with GeoNodes("Roll Axes", prefix=mod_):

        geo = Cloud(Geometry())
        count = Integer(1, "Count", 0, 3)
        roll = Boolean(True, "Roll Axes")

        M4 = Matrix("M4")
        a = M4.separate

        for i in range(1, 4):
            with Layout(f"Roll axes count = {i}"):
                ok = roll & count.equal(i)
                M4 = M4.switch(ok, roll_axes(a, i))

        geo.points._M4 = M4

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # DEBUG - Visualize a 4-D Matrix rotation

    with GeoNodes("Matrix", is_group=True, prefix=debug_):

        M = Matrix(None, "Matrix")
        pos = V4(panel="Location")
        length = Float(1, "Length")
        is_rot = Boolean(True, "Rotation / M4")

        m = M.separate
        v_pos = V4(m[:4])

        pos = v_pos.switch(is_rot, pos)
        M = M.switch(-is_rot, matrix_.cross_product(M).matrix_)

        MProj = matrix_.projection_matrix()
        node = matrix_.dot_vector(MProj, *pos).node

        O = Vector((node.x, node.y, node.z))
        vis = Mesh.UVSphere(radius=.05*length)
        vis.transform(translation=O)

        m = M.separate

        for i in range(4):
            with Layout("Rotation"):
                a = [0]*4
                a[i] = 1
                U = V4(a)
                P_rot = V4.FromNode(matrix_.dot_vector(M, *U).node)

            with Layout("Vector selection"):
                P_m4 = V4(m[4*i:4*(i+1)])
                P = V4.FromNode(vector_.switch(is_rot, *P_m4, *P_rot).node)

            with Layout("Projection"):
                node = matrix_.dot_vector(MProj, *P).node
                p = Vector((node.x, node.y, node.z)).scale(length)
                vis_lab = Curve.Line(O, O + p)

            with Layout("Label"):
                label = String("XYZW"[i]).to_curves(align_x='CENTER', size=.3*length)
                label.transform(rotation=(pi/2, 0, 0))
                label.position = O + p
                vis_lab += label

            if i== 0:
                vis += vis_lab.switch(-is_rot, None)
            else:
                vis += vis_lab


        vis.out()

    # ----------------------------------------------------------------------------------------------------
    # DEBUG - Dump a geometry

    with GeoNodes("Matrices", is_group=False, prefix=debug_):

        cloud = Cloud(Geometry)
        M = Matrix(None, "Matrix")
        use_m4 = Boolean(True, "Use M4")
        is_rot = Boolean(True, "Rotation / M4")


        M = M.switch(use_m4, Matrix("M4"))
        is_rot = is_rot.switch(use_m4, False)

        with cloud.points.for_each(m=M, m4=Matrix("M4")) as feel:

            m = feel.m4.separate
            pos = V4(m[:4])

            vis = debug_.matrix(feel.m, **pos.args(), rotation_m4=is_rot, link_from='TREE')
            feel.generated.geometry = vis

        feel.generated.geometry.out()



# =============================================================================================================================
# Primitives

def build_primitives():

    # ----------------------------------------------------------------------------------------------------
    # Mesh finalization

    with GeoNodes("Finalization", prefix=mod_):

        geo = Mesh(Geometry())
        with Panel("Finalization"):
            smooth = Boolean(True, "Smooth")
            mat    = Material("4 Face", "Material")

        geo.faces.smooth = smooth
        geo.faces.material = mat
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Line

    with GeoNodes("Line", prefix=curve_):

        start = V4(panel="Start")
        end   = V4(0, 0, 0, 1, panel="End")
        count = Integer(16, "Count", 2, 1024)

        direction = end - start
        length = direction.length

        # ----- Starts with a line along x

        line = Curve.LinePoints(end=(length, 0, 0)).resample(count)

        # ----- Normals are Y, Z, W

        a = [0]*16
        a[5], a[10], a[15]  = 1, 1, 1

        # ----- x position

        a[0] = length*Spline.parameter

        # ----- Now we orient X towards the direction

        R = matrix_.align_axis_to_vector(axis='X', **direction.args())
        M4 = R @ Matrix(a)

        # ----- Let's translate with the starting point

        a = list(M4.separate)
        for i in range(4):
            a[i] += start[i]

        # ----- We can now store the M4 matrix

        line.points._M4 = Matrix(a)
        line.position = a[:3]

        line.out()

    # ----------------------------------------------------------------------------------------------------
    # Circle

    with GeoNodes("Circle", prefix=curve_):

        with Panel("Circle"):
            radius    = Float(1, "Radius")
            segments  = Integer(32, "Segments", 3)
            angle     = Float.Factor(1, "Closed", 0, 1)*(2*pi) #Float.Angle(0, "Angle", -2*pi, 2*pi)
            offset    = Float.Factor(0, "Center Circle")

        with Layout("Dimensions"):
            closed = (angle.abs() - 2*pi).abs() < ZERO
            flat = angle.abs() < ZERO
            circ = (2*pi)*radius
            ag = -angle/2 + Spline.parameter*angle
            cag, sag = gnmath.cos(ag), gnmath.sin(ag)
            y_offset = -angle.sign()*radius*offset

        a = [0]*16
        a[ 8:12] = (0, 0, 1, 0)
        a[12:16] = (0, 0, 0, 1)

        with Layout("Circle"):
            circle = Curve.Circle(radius=radius, resolution=segments)
            circle.position = (radius*sag, y_offset + angle.sign()*radius*(1 - cag), 0)

            a[0], a[1] = nd.position.x, nd.position.y
            a[4], a[5] = sag*angle.sign(), -cag
            circle.points._M4 = a

        with Layout("Line"):
            line = Curve.LinePoints(start=(-circ/2, y_offset, 0), end=(circ/2, y_offset, 0)).resample(segments + 1)

            a[0], a[1] = nd.position.x, nd.position.y
            a[4], a[5] = 0, 1
            line.points._M4 = a

        with Layout("Curved Line"):
            curved = Curve(line)
            R = circ/angle
            ag = -angle/2 + Spline.parameter*angle
            curved.position = (R*sag, y_offset + R*(1 - cag), 0)

            a[0], a[1] = nd.position.x, nd.position.y
            a[4], a[5] = sag, -cag
            curved.points._M4 = a

        curve = curved.switch(flat, line).switch(closed, circle)

        a = Matrix("M4").separate
        curve.position = a[:3]

        curve.out()

    # ----------------------------------------------------------------------------------------------------
    # Duplicate a profile along a curve
    #
    # The extrusion can be made in two modes:
    # - Surface (curve profile) : a surface is produced between each instance
    # - Slices (mesh profile) : one separate instance at each point
    # - Edges (mesh profile) : faces are deleted and edges between each instance

    with GeoNodes("Slices", is_group=True, prefix=curve_):

        backbone = Curve(None, name="Curve")
        slice    = Mesh(None, "Slice")
        scale    = Float(1,   "Scale")
        mode     = Integer.MenuSwitch({"Slices": 0, "Surface": 1, "Edges": 2}, menu="Slices", name="Mode")

        # ----- Make sure both the geometries are in 4D

        with Layout("Plunge into 4D"):
            backbone = Curve(mod_.plunge_into_4d(backbone))
            slice    = Mesh(mod_.plunge_into_4d(slice))
            rot = matrix_.rotation_matrix(link_from='TREE')
            slice.points._M4 = rot @ Matrix("M4")

        # ----- Store Scale in the backbone and rename M4 to BB M4

        with Layout("Backbone attributes"):

            backbone.points._BB_Scale = scale

            backbone.points._BB_M4 = Matrix("M4")
            backbone.remove_names("M4")

        # ----- Slices = we instantiate the profiles a many times as required at position 0

        with Layout("Slices : instantiate and delete when scale is null"):
            insts = backbone.points.instance_on(slice)

            insts.insts[Float("BB Scale") < ZERO].delete()
            slices = Mesh(insts.realize())

        # ----- Surface: let's extrude to have the right topology

        with Layout("Surface : Extrusion"):
            grid = backbone.to_mesh(profile_curve=slice)

        # ----- Edges: we extrude points on a mesh without faces

        with Layout("Edges : vertices extrusion loop"):

            with Layout("Mesh size along x"):
                mesh_slice = slice.mesh
                max = mesh_slice.points.attribute_statistic(nd.position).max
                size = 3*(max - max.min_)
                ext_offset = Vector((size, 0, 0))

            with Layout("Create one slice per curve point"):

                count = backbone.points.count
                is_cyclic = backbone.splines.sample_index(nd.is_spline_cyclic, 0)
                iterations = (count - 1).switch(is_cyclic, count)
                backbone.position = (nd.index*size, 0, 0)
                # The first one will also be create be created in Repeat loop
                insts = backbone.points.instance_on(instance=mesh_slice)
                mesh_insts = Mesh(insts.realize())

                edges = mesh_insts

            with Layout("Extrude slice edges"):
                with Repeat(edges=mesh_slice, top=True, iterations=iterations) as rep:
                    offset = ext_offset.switch( (rep.iteration==iterations - 1) & is_cyclic, (-(count-1)*size, 0, 0))
                    edges = rep.edges[rep.top].extrude_edges(offset=offset)
                    top = edges.top_
                    rep.top = top

            with Layout("Merge extrusion with instances"):
                edges = rep.edges
                edges.points._BB_M4 = backbone.points.sample_index(Matrix("BB M4"), index=(nd.index // mesh_slice.points.count)%count)
                edges.points._BB_Scale = backbone.points.sample_index(Float("BB Scale"), index=(nd.index // mesh_slice.points.count)%count)

                edges += mesh_insts
                # MERGE DOESN'T WORK
                #edges.merge_by_distance()

        mesh = Mesh.IndexSwitch(slices, grid, edges, index=mode)

        # ----- Transform backbone M4 into rotation [tangent normal1 normal2 normal3]
        # Slices = roll into [normal1 normal2 normal3 tangent]

        with Layout("Backbone rotation"):
            B4 = Matrix("BB M4")
            rot = matrix_.cross_product(B4).matrix_
            #rot = Matrix.IndexSwitch(rot, rot, matrix_.roll(rot, 3), index=mode)

        with Layout("Slices rotation"):
            M4 = Matrix("M4")
            M4 = rot @ M4

        with Layout("4D scale and translation"):
            m = list(M4.separate)
            b = B4.separate
            scale = Float("BB Scale")

            for i in range(4):
                m[i] = m[i]*scale + b[i]

            mesh.points._M4 = Matrix(m)

        # ----- We have our result

        with Layout("3D position and remove named attrs"):
            mesh.position = m[:3]
            mesh.remove_names("BB*")

        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # Sphere slices

    with GeoNodes("Sphere Slices", is_group=True, prefix=curve_):

        backbone = Curve(None, name="Curve")
        scale    = Float(1,   "Scale")

        with Panel("Sphere"):
            use_uv_sphere = Boolean(True, "UV Sphere")
            rings    = Integer(16, "Rings", 3, 64)
            subdiv = Integer(2, "Subdivisions")

        with Layout("UV Sphere"):
            segments = rings*2
            uv_sphere  = Mesh.UVSphere(radius=radius, segments=segments, rings=rings)

        with Layout("Ico Sphere"):
            ico_sphere = Mesh.IcoSphere(radius = radius, subdivisions=subdiv)

        sphere = ico_sphere.switch(use_uv_sphere, uv_sphere)

        hyper_slices  = curve_.slices(curve=backbone, slice=sphere, scale=scale, mode='Slices', w_euler=(pi/2, 0, 0), _3d_euler=(0, 0, 0), link_from='TREE')
        hyper_edges   = curve_.slices(curve=backbone, slice=sphere, scale=scale, mode='Edges',  w_euler=(pi/2, 0, 0), _3d_euler=(0, 0, 0), link_from='TREE')

        hyper = Geometry.MenuSwitch({'Slices': hyper_slices, 'Edges': hyper_edges}, menu='Slices', name="Mode")

        hyper.out()

    # ----------------------------------------------------------------------------------------------------
    # Hyper Sphere

    with GeoNodes("Hyper Sphere", prefix=mod_):

        radius   = Float(1,   "Radius", 0.1)
        slices   = Integer(7, "Slices", 1, 17)

        slices += 2

        scale = gnmath.sqrt(1 - Spline.parameter.multiply_add(2, -1)**2)
        line   = curve_.line(slices, 0, 0, 0, -radius, 0, 0, 0, radius)

        geo = curve_.sphere_slices(curve=line, scale=scale, link_from='TREE')
        geo.out()


    # ----------------------------------------------------------------------------------------------------
    # Hyper Cone

    with GeoNodes("Hyper Cone", prefix=mod_):

        radius0   = Float(1,   "Bottom Radius", 0)
        radius1   = Float(0,   "Top Radius", 0)
        depth     = Float(2,   "Depth", 0.1)
        slices    = Integer(7, "Slices", 1, 17)

        slices   = slices.switch( (radius0 < ZERO) | (radius1 < ZERO), slices + 1)

        scale = radius0 + Spline.parameter*(radius1 - radius0)
        line   = curve_.line(slices, 0, 0, 0, 0, 0, 0, 0, depth)

        geo = curve_.sphere_slices(curve=line, scale=scale, link_from='TREE')
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Torus

    with GeoNodes("Torus", prefix=mod_):

        with Panel("First"):
            radius0   = Float(2,    "Radius", 0)
            segments0 = Integer(16, "Segments", 3, 64)
            closed0   = Float.Factor(1, "Closed", 0, 1)
        with Panel("Second"):
            radius1   = Float(2,    "Radius", 0)
            segments1 = Integer(16, "Segments", 3, 64)
            closed1   = Float.Factor(1, "Closed", 0, 1)

        circle0 = curve_.circle(radius=radius0, segments=segments0, closed=closed0)
        circle1 = Curve(curve_.circle(radius=radius1, segments=segments1, closed=closed1))
        circle1.points._M4 = matrix_.rotation_matrix(w_euler=(pi/2, 0, 0), _3d_euler=(pi/2, 0, 0)) @ Matrix("M4")

        torus = curve_.slices(curve=circle0, slice=circle1, scale=1, mode='Surface')

        torus.out()





        """

        slices   = slices.switch( (radius0 < ZERO) | (radius1 < ZERO), slices + 1)
        segments = rings*2

        scale = radius0 + Spline.parameter*(radius1 - radius0)

        sphere = Mesh.UVSphere(radius=radius, segments=segments, rings=rings)
        line   = curve_.line(slices, 0, 0, 0, 0, 0, 0, 0, depth)
        hyper  = curve_.slices(curve=line, mesh=sphere, scale=scale)

        mod_.finalization(hyper, link_from='TREE').out()
        """





















def build_extrusions():

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Compute curve tangent

    with GeoNodes("Compute Tangents", is_group=True, fake_user=False, prefix=math_):

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

    with GeoNodes("Link Slices", is_group=True, fake_user=False, prefix=math_):

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

        mesh.out("Mesh")

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Mesh along a curve

    with GeoNodes("Mesh Instances on Curve", is_group=True, fake_user=False, prefix=math_):

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

        curve = Group.Prefix(math_, "Compute Tangents", {'Curve': curve})._out

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

        #curve = math_.compute_tangents(curve).curve
        #curve = Group.Prefix(math_, "Compute Tangents", {'Curve': curve})._out

        tangents = V4.Tangent(curve, sample_index=mesh_index)

        # ---------------------------------------------------------------------------
        # Rotation to align (0, 0, 0, 1) -> Tangent and then translation

        tg = V4.Xyzw(0., 0., 1., 0.).switch(align_w, V4.Xyzw(0., 0., 0., 1.))

        #meshes = g_mods.align_vector(meshes, **tg.kwargs("From"), **tangents.kwargs("To")).geometry
        meshes = Mesh(Group.Prefix(mod_, "Align Vector", [meshes, tg.V, tg.w, tangents.V, tangents.w])._out)

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

    with GeoNodes("Point", fake_user=False, prefix=mod_):

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

        #sphere = sphere.transform(translation=math_.projection(*v.args).v)
        sphere = sphere.transform(translation=Group.Prefix(math_, "Projection", v.sockets()).v)

        # ----- To output

        point.switch(visible, point + sphere).out()

    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as light emitter

    with GeoNodes("Light Emitter", fake_user=False, prefix=mod_):

        v         = V4(0, 0, "")

        color     = Color((1, 1, 1), "Color")
        intensity = Float(1., "Intensity", 0)
        radius    = Float(.1, "Radius")
        visible   = Boolean(True, "Visible")
        mat       = Material(None, "Material")

        # ----- Is a 4 point

        #geo = g_mods.point(None, *v.args, radius=radius, visible=visible, material=mat).geometry
        geo = Group.Prefix(mod_, "Point", {'V': v.V, 'w': v.w, 'Radius': radius, 'Visible': visible, 'material': mat})._out

        mesh, cloud  = geo.mesh, geo.point_cloud

        cloud.points.store(      "Intensity", intensity)
        cloud.points.store("Color", color)

        (cloud + mesh).out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Reflect on a surface given the two normals

    with GeoNodes("Surface Reflection", is_group=True, prefix=math_):

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

        front_a.out("Front A")
        front_b.out("Front B")

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Capture light from an emitter

    with GeoNodes("Light Capture", fake_user=False, prefix=mod_):

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

        #ref_node  = math_.surface_reflection(*incident.args, *Na.args, *Nb.args)
        ref_node  = Group.Prefix(math_, "Surface Reflection", [incident.V, incident.w, Na.V, Na.w, Nb.V, Nb.w])
        reflected = V4.FromNode(ref_node)

        # ----------------------------------------------------------------------------------------------------
        # Intensity

        #proj = V4.NodeOutput(math_.projection_matrix(), "R 3")
        proj = V4.FromNode(Group.Prefix(math_, "Projection Matrix"), "R 3")

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


        mesh = Mesh(Group.Prefix(math_, "Mesh Instances on Curve",
            curve         = curve,
            mesh          = mesh,
            scale         = scale,
            use_radius    = use_radius,
            align_w       = align_w,
            resample      = resample,
            resolution    = new_resol)._out)

        # ----- Link the slices

        mesh = mesh.switch(link_slices, Group.Prefix(math_, "Link Slices",
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

        mesh = Mesh(Group.Prefix(math_, "Mesh Instances on Curve",
            curve         = curve,
            mesh          = sphere,
            scale         = size,
            use_radius    = use_radius,
            align_w       = align_w,
            resample      = resample,
            resolution    = new_resol)._out)

        # ----- Link the slices

        mesh = mesh.switch(link_slices, Group.Prefix(math_, "Link Slices",
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
        tubes_node.link_from()

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

        node.link_from(exclude=['Factor XY', 'Factor ZW', 'Twists'])

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

        node.link_from(exclude=['Factor XY', 'Factor ZW', 'Twists'])

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

        projected = Group.Prefix(mod_, "Projection", geometry=geo, shade_smooth=Boolean(False, "Shade Smooth"))._out

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
