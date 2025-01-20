"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : fourd engine
---------------------

4D engine

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/fourd.py)

The 4D Engine provides modifiers to create 4D geometries, transform them and project
them into 3D space.

> [!NOTE]
> The 4D light is still work in progress

> [!IMPORTANT]
> - The engine needs an object named "4D Parameters" with the modifier "4D Parameters":
>   this is where you control the 4D paramaters.
> - The last modifier must be "4D Projection" to project the 4D geometry into a 3D space.

For instance, to visualize an Hypersphere, you have to stack two modifiers:
- 4D Hyper Sphere
- 4D Projection

### Creating 4D Geometry

You can use modifiers creating 4D geometry:
- 4D Hyper Sphere
- 4D Hyper Cube
- 4D Hyper Cone
- 4D 5 Cell Polytope
- 4D Torus
- 4-Curve Circle
- 4-Curve Line

You can also create your own geometry with modifiers and groups
- 4D Plunge into 4D
- 4-Math xxx
- 4-Vector xxx
- 4-Matrix xxx

You can then transform your geometry with:
- 4D Rotation
- 4D Translation
- 4D Scale
- 4D Roll Axes
- 4D Swap Axes



> [!NOTE]
> Modifiers:
> - 4D Parameters
> - 4D Projection
> - 4D Hyper Sphere
> - 4D Hyper Cube
> - 4D Hyper Cone
> - 4D 5 Cell Polytope
> - 4D Torus
> - 4-Curve Circle
> - 4-Curve Line
> - 4D Plunge into 4D
> - 4D Rotation
> - 4D Translation
> - 4D Scale
> - 4D Roll Axes
> - 4D Swap Axes
> - 4-Math xxx (Group)
> - 4-Vector xxx (Group)
> - 4-Matrix xxx (Group)


``` python
from geonodes.demos import fourd

fourd.demo()
```
"""


import bpy

from geonodes import *
from geonodes.core import utils

# ----- Prefixes

math_   = G("4-Math")
matrix_ = G("4-Matrix")
vector_ = G("4-Vector")
curve_  = G("4-Curve")
surf_   = G("4_Surf")
debug_  = G("DEBUG")

mod_    = G("4D")
light_  = G("4D Light")

ZERO = 0.0001

V4_COL = (.3, .1, .1)

PARAMETERS_OBJECT = "4D Parameters"

# =============================================================================================================================
# Build the 4D engine

def demo(clear=False, with_debug=False):

    print("-"*100)
    print("Build 4D Engine")
    print()

    Tree._reset_counters()
    build_shaders()
    print(f"4D shaders built : {Tree._total_nodes} nodes, {Tree._total_links} links")
    print()

    Tree._reset_counters()

    if with_debug:
        build_debug()

    build_operations()
    build_matrices()
    build_transformations(with_debug=with_debug)
    build_primitives()

    build_lights()

    show_case()


    Tree._display_counter("4D Engine built")
    print(f"4D Engine built : {Tree._total_nodes} nodes, {Tree._total_links} links in {Tree._total_time:.1f} s")
    print()

# =============================================================================================================================
# Shaders
# =============================================================================================================================

def build_shaders():

    # ----------------------------------------------------------------------------------------------------
    # Grid shader group

    with ShaderNodes("Grid", is_group=True):

        uv = snd.texture_coordinate(from_instancer=False, object=None).uv

        x, y, _ = uv.xyz

        thick = .002
        count = 6

        on_x = gnmath.mless_than((x + (thick/2)) % (1/(2*count)), thick)
        on_y = gnmath.mless_than((y + (thick)) % (1/count), thick*2)

        grid = gnmath.add(on_x, on_y, True)

        color = Color() # Black

        thick *= 2
        x_green = gnmath.mless_than((x + (thick/2)) % .5, thick)
        x_red   = gnmath.mless_than((x + .25 + (thick/2)) % .5, thick)
        y_blue  = gnmath.mless_than((y + .5 + (thick)) % .5, thick*2)

        grid = gnmath.add(grid, x_green, True)
        grid = gnmath.add(grid, x_red, True)
        grid = gnmath.add(grid, y_blue, True)

        color = color.mix(Color((1, 0, 0)), x_red)
        color = color.mix(Color((0, 1, 0)), x_green)
        color = color.mix(Color((0, 0, 1)), y_blue)

        # No grid
        if True:
            grid = Float(0)

        grid.out("Grid")
        color.out("Color")


    # ----------------------------------------------------------------------------------------------------
    # Axis Shader

    with ShaderNodes("4 Axis"):

        col = snd.attribute(attribute_name="Color").color_

        ped = Shader.Principled(base_color=col, roughness=.1, metallic=.3)

        ped.out()

    # ----------------------------------------------------------------------------------------------------
    # 4D Light utility
    # Get the enlightments parameter

    with ShaderNodes("4D Get Light", is_group=True):

        light_in  = snd.attribute(attribute_name="Inner Light").fac
        light_out = snd.attribute(attribute_name="Outer Light").fac
        int_fac   = snd.attribute(attribute_name="Interior").fac

        spot_in  = snd.attribute(attribute_name="Inner Spot").fac
        spot_out = snd.attribute(attribute_name="Outer Spot").fac

        color_in  = Color((1, 1, 0)).hue_saturation_value(value=2*light_in,  fac=1)
        color_out = Color((1, 1, 1)).hue_saturation_value(value=2*light_out, fac=1)

        color = color_out.mix(color_in, int_fac)
        spot = spot_out.mix(spot_in, int_fac)

        color.out("Color")
        spot.out("Spot")
        light_in.out("Inner")
        light_out.out("Outer")
        int_fac.out("Interior")


    with ShaderNodes("4 Enlighted"):

        node = G()._4d_get_light().node
        color = node.color
        spot  = node.spot

        grid_node = G().grid().node
        color = color.mix(grid_node.color, grid_node.grid)

        ped = Shader.Principled(
            base_color = color,
            roughness  = node.interior,
            emission_strength = .1 + spot,
            emission_color = color,
            )

        transp_fac = snd.attribute(attribute_name="Transparency").fac
        transp = Shader.Transparent()
        shader = snd.mix_shader(ped, transp, fac=transp_fac)

        shader.out()

    with ShaderNodes("4 Faces Orientation"):

        interior = snd.attribute(attribute_name="Interior").fac
        color = Color((0, 1, 0)).mix((1, 0, 0), interior)

        grid_fac = G().grid()

        ped = Shader.Principled(
            base_color = color.mix(Color((0, 0, 1)), grid_fac),
            metallic   = 0.,
            roughness  = interior,
            )

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
            #alpha      = .1,
            normal     = bump,
            )

        transp_fac = snd.attribute(attribute_name="Transparency").fac

        transp = Shader.Transparent()

        shader = snd.mix_shader(ped, transp, fac=transp_fac)

        shader.out()

    # ----------------------------------------------------------------------------------------------------
    # Edge default

    with ShaderNodes("4 Edge"):

        ped = Shader.Principled(
            base_color = (0., .05, .9),
            roughness  = 0.,
            )

        ped.out()

    # ----------------------------------------------------------------------------------------------------
    # Light default

    with ShaderNodes("4 Light"):

        ped = Shader.Principled(
            base_color = (1, 1, 1), #snd.attribute(attribute_name="Color").color,
            metallic   = 0.,
            roughness  = 0.,
            emission_strength   = 1.,
            normal     = bump,
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
    def __init__(self, *values, panel=None, single_value=False):

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
                self.x, self.y, self.z, self.w = [Float(a[i], "xyzw"[i], single_value=single_value) for i in range(4)]

    @classmethod
    def FromNode(cls, node):
        return cls(node.x, node.y, node.z, node.w)

    @classmethod
    def FromM4(cls, M4, index=0):
        a = M4.separate
        return cls(a[index*4:(index+1)*4])

    def out(self, **props):
        for v, label in zip(self, "xyzw"):
            v.out(label, **props)

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
        count = Integer(0, "Count", 0, 3, single_value=True) % 4

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
        index = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2, 'W': 3}, menu='W', name="Axis", single_value=True)

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

    with GeoNodes("Align X Axis to Vector", is_group=True, prefix=matrix_):

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
    # GROUP - A Single Rotation Matrix

    with GeoNodes("Single Rotation Matrix", is_group=True, prefix=matrix_):

        panel_name = "Rotation 4D"

        with Panel(panel_name):
            w_euler = Vector.Euler(0, "W Euler", tip="Rotation XW, YW, ZW", single_value=True)
            euler   = Vector.Euler(0, "3D Euler", tip="Rotation YZ, ZX, XY", single_value=True)

        matrix_.rotation_matrix(link_from='TREE').out()


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
            resol  = Integer(        8, "Resolution", 3, 32, single_value=True)
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
            ar_length = arrow.length()

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

        M = matrix_.single_rotation_matrix(link_from='TREE')
        opposite = Boolean(False, "Opposite Direction", tip="For Mesh faces orientation")

        with Panel("Show Axes"):
            show_axis = Boolean(True, "Show Axes", tip="Show the 4 axes", single_value=True)
            neg       = Float(-1, "Negative", max=0, single_value=True)
            pos       = Float(3,  "Positive", 0, single_value=True)

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
        cloud.points._Opposite = opposite

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

        opp = cloud.points.sample_index(Boolean("Opposite"), 0)
        opp.out("Opposite")

    # ----------------------------------------------------------------------------------------------------
    # Plunge into 3D

    with GeoNodes("Plunge into 4D", prefix=mod_):

        geo       = Geometry()
        w         = Float(0, "w", tip="Fourth dimension value")
        curve_res = Integer(0, "Curve Resample", min=0, tip="Resample curve (0 or 1 for no resample)", single_value=True)
        min_light = Float(0, "Light Intensity", 0, 1)

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

            geo = Cloud(plunged.switch(exists, geo))

        with Layout("Enlightment"):
            geo.points[-Float("Inner Light").exists_]._Inner_Light = min_light
            geo.points[-Float("Outer Light").exists_]._Outer_Light = min_light

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Perform a projection

    with GeoNodes("Projection", prefix=mod_):

        geo = Geometry()

        with Panel("Faces"):
            del_faces   = Boolean(False,        "Delete Faces", single_value=True)
            transp      = Float.Factor(0,       "Transparency", 0, 1, single_value=True)
            face_smooth = Boolean(True,         "Face Smooth", single_value=True)
            set_mat     = Boolean(True,         "Set Material", single_value=True)
            face_mat    = Material("4 Face",    "Face Material")

        with Panel("Edges"):
            edge_radius = Float(0,              "Edge Radius", 0, single_value=True)
            edge_resol  = Integer(12,           "Edge Resolution", 3, 16, single_value=True)
            edge_mat    = Material("4 Edge",    "Edge Material")

        with Panel("Points"):
            merge        = Boolean(False,       "Merge", single_value=True)
            point_radius = Float(0,             "Point Radius", 0, single_value=True)
            point_mat    = Material("4 Edge",   "Point Material")

        with Panel("Debug"):
            show_nrm_A    = Boolean(False, "Show Normals A",  tip="Show first mesh/curve normals", single_value=True)
            show_nrm_B    = Boolean(False, "Show Normals B",  tip="Show second mesh/curve normals", single_value=True)
            show_nrm_C    = Boolean(False, "Show Normals C",  tip="Show third curve normals", single_value=True)
            show_tangents = Boolean(False, "Show Tangents", tip="Show curve tangents", single_value=True)
            vect_length   = Float(1, "Vectors length", tip="Length of normals / tangents", single_value=True)

        with Layout("Projection into 3D Space"):

            M = Matrix("M4")
            M_proj = matrix_.projection_matrix()
            opp = M_proj.opposite_

            # Projection direction
            look = V4(M_proj.separate[12:])

            m = M_proj @ M

            a = m.separate
            geo.position = a[:3]

        with Layout("Merge by distance if requested"):
            mesh = Mesh(geo)
            mesh.merge_by_distance()
            geo = geo.switch(merge, mesh)

        mesh  = geo.mesh
        curve = geo.curve
        cloud = geo.point_cloud

        with Layout("Face interior given by Normal A"):
            normal_A = V4(a[4:8])
            dot_look = look.dot(normal_A)
            dot_look = dot_look.switch(opp, -dot_look)

            interior = dot_look < 0
            mesh.points._Interior = interior

        line = Curve.LineDirection(length=vect_length)

        with Layout("Mesh Normals"):
            visA = mesh.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[4:7]))
            visB = mesh.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[8:11]))

        with Layout("Curve Normals & Tangents"):
            curve.points._Tangent = a[4:7]

            visA += curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[ 4:7]))
            visB += curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[ 8:11]))
            visC  = curve.points.instance_on(instance=line, rotation=Rotation.AlignZToVector(a[12:15]))

            visualization = visA.switch_false(show_nrm_A) + visB.switch_false(show_nrm_B) + visC.switch_false(show_nrm_C)

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
            with_faces.faces._Transparency = transp

            # ----- Smooth or unchanged
            smoothed = Mesh(with_faces)
            smoothed.faces.smooth = True
            with_faces = with_faces.switch(face_smooth, smoothed)

            # ----- Change material if requested
            with_mat = Mesh(with_faces)
            with_mat.faces.material = face_mat
            with_faces = with_faces.switch(set_mat, with_mat)

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
        Vector((x, y, 0)).length().out("Length")

# =============================================================================================================================
# Transformations
# - Translation
# - Scale
# - Rotation 4D
# - Rotation 2D
# - Align Vector

def build_transformations(with_debug=False):

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
        count = Integer(1, "Count", 0, 3, single_value=True)
        roll = Boolean(True, "Roll Axes", single_value=True)

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

    if not with_debug:
        return

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
    # Line

    with GeoNodes("Line", prefix=curve_):

        start = V4(panel="Start")
        end   = V4(0, 0, 0, 1, panel="End")
        count = Integer(16, "Count", 2, 1024, single_value=True)

        direction = end - start
        length = direction.length

        # ----- Starts with a line along x

        line = Curve.LinePoints(end=(length, 0, 0)).resample(count)

        # ----- Normals are Y, Z, W

        a = [0]*16
        a[5], a[10], a[15]  = 1, 1, 1

        # ----- x position

        a[0] = length*Spline.parameter_factor

        # ----- Now we orient X towards the direction

        R = matrix_.align_x_axis_to_vector(**direction.args())
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
            radius    = Float(1,            "Radius", single_value=True)
            segments  = Integer(32,         "Segments", 3, single_value=True)
            offset    = Float.Factor(0,     "Center", single_value=True)
            close_fac = Float.Factor(1,     "Closed", 0, 1, single_value=True)
            cyclic    = Boolean(True,       "Cyclic", tip="Create a cyclic curve when closed", single_value=True)

        rot = matrix_.single_rotation_matrix(link_from='TREE')

        with Layout("Dimensions"):
            angle    = close_fac*(2*pi)
            closed   = (1 - close_fac).abs() < ZERO
            flat     = close_fac < ZERO
            circ     = (2*pi)*radius
            ag       = -angle/2 + Spline.parameter_factor*angle
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
            ag = -angle/2 + Spline.parameter_factor*angle
            curved.position = (R*sag, y_offset + R*(1 - cag), 0)

            a[0], a[1] = nd.position.x, nd.position.y
            a[4], a[5] = sag, -cag
            curved.points._M4 = a

        curve = curved.switch(flat, line).switch(closed & cyclic, circle)

        curve.points._M4 = rot @ Matrix("M4")

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
    #
    # In surface mode, a curve is extrude along the backbone
    # The extrusion is made along Normal B. Normals A and C become the two normals of the resulting surface
    # IN PROGRESS

    with GeoNodes("Slices", is_group=True, prefix=curve_):

        backbone = Curve(None,      "Curve", tip="Backbone curve")
        slice    = Mesh(None,       "Slice", tip="The geometry to iterate along the backbone")
        scale    = Float(1,         "Scale", tip="Scale to apply to each slice")
        rotation = Matrix(None,     "Rotation", tip="Rotation to apply to each slice")
        mode     = Integer.MenuSwitch({"Slices": 0, "Surface": 1, "Edges": 2}, menu="Slices", name="Mode")

        # ----- Make sure both the geometries are in 4D

        with Layout("Plunge into 4D"):
            backbone = Curve(mod_.plunge_into_4d(backbone))
            slice    = Mesh(mod_.plunge_into_4d(slice))

        # ----- Store Scale in the backbone and rename M4 to BB M4

        with Layout("Backbone attributes"):

            backbone.points._BB_Scale = scale

            backbone.points._BB_M4 = Matrix("M4") @ rotation
            backbone.remove_names("M4")

        # ----------------------------------------------------------------------------------------------------
        # Index Switch
        #
        # ----- Slices = we instantiate the profiles a many times as required at position 0

        with If(Mesh, mode, tip="Slice instance at each backbone point") as mesh:

            # Instantiate the slice on each backbone point
            insts = backbone.points.instance_on(slice)

            # Delete where scale is null
            insts.insts[Float("BB Scale") < ZERO].delete()

            mesh.option = insts.realize()

        # ----- Surface : the slice is a curve extruded along the backbone

        with Elif(mesh, tip="Slice is extruded along backbone"):

            # We extrude in 3D to have to right topology
            mesh.option = backbone.to_mesh(profile_curve=slice)

        # ----- Edges : vertices extrusion

        with Elif(mesh, tip="Vertices extrusion"):

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

                mesh.option = edges

        # ----------------------------------------------------------------------------------------------------
        # -----Transform backbone M4 into rotation [tangent normal1 normal2 normal3]
        # Slices = roll into [normal1 normal2 normal3 tangent]

        with Layout("Backbone rotation"):
            B4 = Matrix("BB M4")
            rot = matrix_.cross_product(B4).matrix_
            #rot = Matrix.IndexSwitch(rot, rot, matrix_.roll(rot, 3), index=mode)

        with Layout("Slices rotation"):

            # ----- Rotation with backbone Matrix
            rot_M4 = rot @ Matrix("M4")

            with If(Matrix, mode.equal(1), tip='Keep Slice normals A & C') as M4:
                a = list(rot_M4.separate)
                a[8:12] = a[12:16]
                M4.option = Matrix(a)

            with Else(M4):
                M4.option = rot_M4

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
        sphere = Mesh(mod_.plunge_into_4d(sphere))
        rot = matrix_.rotation_matrix(w_euler=(pi/2, 0, 0))
        sphere.points._M4 = rot @ Matrix("M4")

        hyper_slices  = curve_.slices(curve=backbone, slice=sphere, scale=scale, mode='Slices', link_from='TREE')
        hyper_edges   = curve_.slices(curve=backbone, slice=sphere, scale=scale, mode='Edges',  link_from='TREE')

        hyper = Geometry.MenuSwitch({'Slices': hyper_slices, 'Edges': hyper_edges}, menu='Slices', name="Mode")

        hyper.out()

    # ----------------------------------------------------------------------------------------------------
    # Hyper Sphere

    with GeoNodes("Hyper Sphere", prefix=mod_):

        radius   = Float(1,   "Radius", 0.1, single_value=True)
        slices   = Integer(7, "Slices", 1, 17, single_value=True)

        slices += 2

        scale = gnmath.sqrt(1 - Spline.parameter_factor.multiply_add(2, -1)**2)
        line   = curve_.line(slices, 0, 0, 0, -radius, 0, 0, 0, radius)

        geo = curve_.sphere_slices(curve=line, scale=scale, link_from='TREE')
        geo.out()


    # ----------------------------------------------------------------------------------------------------
    # Hyper Cone

    with GeoNodes("Hyper Cone", prefix=mod_):

        radius0   = Float(1,   "Bottom Radius", 0, single_value=True)
        radius1   = Float(0,   "Top Radius", 0, single_value=True)
        depth     = Float(2,   "Depth", 0.1, single_value=True)
        slices    = Integer(7, "Slices", 1, 17, single_value=True)

        slices   = slices.switch( (radius0 < ZERO) | (radius1 < ZERO), slices + 1)

        scale = radius0 + Spline.parameter_factor*(radius1 - radius0)
        line   = curve_.line(slices, 0, 0, 0, 0, 0, 0, 0, depth)

        geo = curve_.sphere_slices(curve=line, scale=scale, link_from='TREE')
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Torus

    with GeoNodes("Torus", prefix=mod_):

        with Panel("First"):
            radius0    = Float(2,    "Radius", 0, single_value=True)
            segments0  = Integer(16, "Segments", 3, 64, single_value=True)
            closed0    = Float.Factor(1, "Closed", 0, 1, single_value=True)

        with Panel("Second"):
            radius1    = Float(2,    "Radius", 0, single_value=True)
            segments1  = Integer(16, "Segments", 3, 64, single_value=True)
            closed1    = Float.Factor(1, "Closed", 0, 1, single_value=True)
            twist      = Float.Angle(0, "Twist", single_value=True)

        cyclic0 = twist.abs() < ZERO
        circle0 = curve_.circle(radius=radius0, segments=segments0, center=1, closed=closed0, cyclic=cyclic0)
        circle0 = Curve(circle0)

        circle1 = curve_.circle(radius=radius1, segments=segments1, center=1, closed=closed1, cyclic=True, w_euler=(pi/2, 0, 0), _3d_euler=(pi/2, 0, 0))
        circle1 = Curve(circle1)

        #twist = half_turns*pi
        M = matrix_.rotation_matrix(w_euler=(0, Spline.parameter_factor*twist, 0))
        M = circle0.points.capture_attribute(M)

        torus = curve_.slices(curve=circle0, slice=circle1, scale=1, rotation=M, mode='Surface')

        torus.out()

    # ----------------------------------------------------------------------------------------------------
    # Hyper Cube

    with GeoNodes("Hyper Cube", prefix=mod_):

        size   = V4((1, 1, 1, 1), panel="Size", single_value=True)
        slices = Integer(2, "Slices", 2, single_value=True)

        line   = curve_.line(slices, 0, 0, 0, -size.w/2, 0, 0, 0, size.w/2)
        cube   = Mesh.Cube(size=size[:3])

        cube = Mesh(mod_.plunge_into_4d(cube))
        cube.points._M4 = matrix_.rotation_matrix(w_euler=(pi/2, 0, 0)) @ Matrix("M4")

        geo = curve_.slices(curve=line, slice=cube, scale=1, mode='Edges', link_from='TREE')

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # 5 Cell

    with GeoNodes("5 Cell Polytope", fake_user=False, prefix=mod_):

        size = Float(1, "Size", single_value=True)

        from math import sqrt

        P4 = [
            V4(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12),  1/2),
            V4(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12), -1/2),
            V4(1/2/sqrt(10),  1/2/sqrt(6), -2/sqrt(12),    0),
            V4(1/2/sqrt(10), -3/2/sqrt(6),           0,    0),
            V4( -2/sqrt(10),            0,           0,    0),
        ]

        S = Mesh.Cone(vertices=3)
        for i in range(4):
            a = [0]*16
            a[:4] = P4[i].scale(size)
            S.points[i]._M4 = Matrix(a)

        S = S.extrude_edges()
        top = S.top_
        a = [0]*16
        a[:4] = P4[4].scale(size)
        S.points[top]._M4 = Matrix(a)

        S[top].position = (3*size, 0, 0)
        S.merge_by_distance()

        a = Matrix("M4").separate
        S.position = a[:3]

        S.out()


# ====================================================================================================
# Lights
# - Point
# - Light emitter
# - Light capture

def build_lights():

    # ---------------------------------------------------------------------------------------------------
    # MODIFIER - Set an object as a 4-point

    with GeoNodes("Emitter", prefix=light_):

        with Panel("Light"):
            dist = Float(3, "Distance")
            power = Float(10, "Power", 0)
            #color = Color((1, 1, 1), "Color")

        with Panel("Show"):
            show = Boolean(True, "Show")
            radius= Float(.1, "Radius", 0)
            mat = Material("4 Light", "Material")

        cloud = Cloud.Points(1, position=(0, 0, dist))
        cloud = mod_.plunge_into_4d(cloud, w = 0)
        cloud = Cloud(mod_.rotation(cloud).link_from(exclude='Pivot'))

        M4 = cloud.points.sample_index(Matrix("M4"), 0)
        v4 = M4.separate[:4]
        cloud = Cloud(Group("4D Projection", geometry=cloud).geometry)

        with If(Geometry, show) as geo:

            sphere = Mesh.UVSphere(radius=radius)
            sphere.faces.smooth = True
            sphere.faces.material = mat
            sphere_loc = Cloud(Group("4D Projection", geometry=cloud, transparency=0).geometry)
            sphere.transform(translation=cloud.points.sample_index(nd.position, 0))

            geo.option = sphere

        with Else(geo):

            geo.option = cloud

        geo = Cloud(geo)

        geo.points._Power = power
        for axis, v in zip('xyzw', v4):
            geo.points.store(axis, v)

        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # GROUP - Reflect on a surface given the two normals

    with GeoNodes("Receiver", prefix=light_):

        geo = Cloud(Geometry())
        emitter_obj = Object(None, "Emitter", tip="Emitter object with 'Light Emitter' modifier")
        light_min = Float(.1, "Ambient intensity", 0, 1)

        with Panel("Debug"):
            show_incident  = Boolean(False, 'Show Incident')
            show_reflected = Boolean(False, 'Show Reflected')
            rays_length    = Float(1, "Rays Length")

        with Layout("Light intensity min"):
            current = Float("Light Intensity")
            geo.points[-current.exists_]._Inner_Light = light_min
            geo.points[-current.exists_]._Outer_Light = light_min

            geo.points[-current.exists_]._Inner_Spot = 0.
            geo.points[-current.exists_]._Outer_Spot = 0.

        emitter = Cloud(emitter_obj.info().geometry)

        with Layout("Light locations and parameters"):
            light_loc   = V4([emitter.points.sample_index(Float(c), index=0) for c in 'xyzw'])
            light_power = emitter.points.sample_index(Float("Power"), index=0)

        with Layout("Reflection"):

            a = Matrix("M4").separate

            pos4     = V4(a[:4])
            normal_A = V4(a[4:8])
            normal_B = V4(a[8:12])

            in_vector = pos4 - light_loc
            ray = in_vector.normalize()

            with Layout("Show Incident Ray"):
                with geo.points.for_each(m4 = Matrix("M4")) as feel:
                    pos = V4(feel.m4.separate[:4])
                    line = curve_.line(**light_loc.args("Start"), **pos.args("End"), count=2)
                    feel.generated.geometry = line

                incident_rays = feel.generated.geometry

            dot_A = normal_A.dot(ray)
            dot_B = normal_B.dot(ray)

            comp_A = normal_A.scale(dot_A)
            comp_B = normal_B.scale(dot_B)

            bounce = ray - (comp_A + comp_B).scale(2)

            with Layout("Reflected rays"):
                with geo.points.for_each(m4=Matrix("M4"), x=bounce.x, y=bounce.y, z=bounce.z, w=bounce.w) as feel:
                    pos = V4(feel.m4.separate[:4])
                    line = curve_.line(**pos.args("Start"), **(pos + V4((feel.x, feel.y, feel.z, feel.w)).scale(rays_length)).args("End"), count=2)
                    feel.generated.geometry = line

                reflected_rays = feel.generated.geometry

        with Layout("4D Camera direction"):

            M_proj = matrix_.projection_matrix()
            opp = M_proj.opposite_

            look = V4(M_proj.separate[12:])

            with Layout("Intensity"):
                dot_look = look.dot(bounce)

                # CAUTION: should be 'switch' and not 'switch_false',
                # but the result is more consistent
                # don't know why :-(
                #dot_look = dot_look.switch_false(opp, -dot_look)
                dot_look = dot_look.switch(opp, -dot_look)

                # Negative : the ray comes back toward the looking direction
                intensity  = dot_look.map_range_linear(-1, 0, 1, 0)
                emission   = dot_look.map_range_smoother_step(-1, -.9, 10, 0)
                #intensity += emission

            with Layout("Inner / outer Faces"):
                dot_look = (look.dot(normal_A))
                dot_look = dot_look.switch(opp, -dot_look)
                interior = dot_look < 0

                geo.points._Inner_Light += intensity.switch_false(interior)
                geo.points._Outer_Light += intensity.switch(interior)

                geo.points._Inner_Spot  += emission.switch_false(interior)
                geo.points._Outer_Spot  += emission.switch(interior)

        geo += incident_rays.switch_false(show_incident)
        geo += reflected_rays.switch_false(show_reflected)

        geo.out()



    return



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
# Global demo

def show_case():

    with GeoNodes("4D Show Case"):

        with If(Geometry, "Hyper Cube", name="4D Geometry") as geometry:
            geo = Group("4D Hyper Cube").geometry
            geo = Group("4D Rotation", geometry=geo).link_from(exclude='Pivot').geometry
            geometry.option = Group("4D Projection", geometry=geo,  delete_faces=True, edge_radius=.02, point_radius=.05).geometry

        with Elif(geometry, "Hyper Sphere"):
            geo = Group("4D Hyper Sphere", rings=32).geometry
            geo = Group("4D Rotation", geometry=geo).link_from(exclude='Pivot').geometry
            geometry.option = Group("4D Projection", geometry=geo, transparency=0).geometry

        with Elif(geometry, "Clifford Torus"):
            geo = Group("4D Torus", first_radius=2, first_segments=64, second_radius=1, second_segments=64).geometry
            geo = Group("4D Rotation", geometry=geo).link_from(exclude='Pivot').geometry
            geometry.option = Group("4D Projection", geometry=geo, transparency=0).geometry

        with Elif(geometry, "Klein Torus"):
            geo = Group("4D Torus", first_radius=2, first_segments=64, second_radius=1, second_segments=64, twist=pi).geometry
            geo = Group("4D Rotation", geometry=geo).link_from(exclude='Pivot').geometry
            geometry.option = Group("4D Projection", geometry=geo, transparency=0).geometry

        with Elif(geometry, "5 Cell Polytope"):
            geo = Group("4D 5 Cell Polytope").geometry
            geo = Group("4D Rotation", geometry=geo).link_from(exclude='Pivot').geometry
            geometry.option = Group("4D Projection", geometry=geo,  delete_faces=True, edge_radius=.02, point_radius=.05).geometry

        geometry.out()
