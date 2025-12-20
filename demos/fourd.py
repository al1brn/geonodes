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


ZERO = 0.0001

# Prefixes
group_  = G("4D G")         # Groups
vec4_   = G("4D Vec")       # 4-Vector math
mat4_   = G("4D Mat")       # Matrix 4
mod_    = G("4D Op")        # Modifiers
curve_  = G("4D Curve")     # Curve
mesh_   = G("4D Mesh")      # Mesh

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

    Vector4.build_nodes()
    Matrix4.build_nodes()
    Position4.build_nodes()
    Geometry4.build_nodes()
    Curve4.build_nodes()

    return

    build_engine()
    build_primitives()

    #build_operations()
    #build_matrices()
    #build_transformations(with_debug=with_debug)
    #build_primitives()

    #build_lights()

    #show_case()


    Tree._display_counter("4D Engine built")
    print(f"4D Engine built : {Tree._total_nodes} nodes, {Tree._total_links} links in {Tree._total_time:.1f} s")
    print()

# ====================================================================================================
# Shaders
# ====================================================================================================

def build_shaders():

    # ----------------------------------------------------------------------------------------------------
    # Grid shader group
    # ----------------------------------------------------------------------------------------------------

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
    # ----------------------------------------------------------------------------------------------------

    with ShaderNodes("4 Axis"):

        col = snd.attribute(attribute_name="Color").color

        ped = Shader.Principled(base_color=col, roughness=.1, metallic=.3)

        ped.out()

    # ----------------------------------------------------------------------------------------------------
    # 4D Light utility
    # Get the enlightments parameter
    # ----------------------------------------------------------------------------------------------------

    with ShaderNodes("4D Get Light", is_group=True):

        light_in  = snd.attribute(attribute_name="Inner Light").factor
        light_out = snd.attribute(attribute_name="Outer Light").factor
        int_fac   = snd.attribute(attribute_name="Interior").factor

        spot_in  = snd.attribute(attribute_name="Inner Spot").factor
        spot_out = snd.attribute(attribute_name="Outer Spot").factor

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

        #node = G()._4d_get_light().node
        node = Group("4D Get Light")
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

        transp_fac = snd.attribute(attribute_name="Transparency").factor
        transp = Shader.Transparent()
        shader = snd.mix_shader(ped, transp, factor=transp_fac)

        shader.out()

    with ShaderNodes("4 Faces Orientation"):

        interior = snd.attribute(attribute_name="Interior").factor
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

        transp_fac = snd.attribute(attribute_name="Transparency").factor

        transp = Shader.Transparent()

        shader = snd.mix_shader(ped, transp, factor=transp_fac)

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

# ====================================================================================================
# MACROS
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Transform geometry into a single cloud of points
# ----------------------------------------------------------------------------------------------------

def to_cloud(geo):
    """ Convert the full geometry to Cloud
    """
    with Layout("To Cloud", color='MACRO'):
        node = Geometry().separate_components()
        cloud = node.point_cloud
        cloud += node.mesh.to_points()
        cloud += node.curve.to_points(count=node.curve.points.count)
        return cloud

# ----------------------------------------------------------------------------------------------------
# Visualize Matrix vectors
# ----------------------------------------------------------------------------------------------------

def vis_mat4D(geo, *indices):
    
    with Layout("Visualize Matrix vectors"):
        
        #cloud = Group("4D G To Cloud", geometry=Geometry()).cloud
        cloud = to_cloud(Geometry())
        
        M = get_projection() @ Matrix("M4D")
        Vecs = [Vector4.FromMatrix(M, i) for i in (0,) + tuple(indices)]
        cloud.position = Vecs[0].v
        
        mesh = None
        for index, V in zip(indices, Vecs[1:]):
            
            msh = cloud.to_vertices()
            msh = msh.points.extrude(V.v)
            
            if index >= 2:
                top = msh.top
                msh.points[top].extrude(-V.v + .3, offset_scale=.3)
                
            if index == 3:
                msh.points[top & msh.top.bnot()].extrude(-V.v - .3, offset_scale=.3)
            
            if mesh is None:
                mesh = msh
            else:
                mesh += msh
                
    return mesh

def unravel_index(index, shape, grid=True):

    with Layout("Unravel Index", color='MACRO'):
        nx, ny = shape
        if grid:
            return index // ny, index % ny
        else:
            return index % nx, index // nx
    
def ravel_indices(i, j, shape, grid=True):

    with Layout("Ravel Indices", color='MACRO'):
        nx, ny = shape
        if grid:
            return j + i*ny
        else:
            return i + j*nx

# ====================================================================================================
# 4-Vector
# ====================================================================================================

class Vector4:
    """ This class provides help to handle the four Vector4 components stored in a couple (Vector, Float)
    """

    def __init__(self, v=None, w=None):

        if v is None:
            v = (0, 0, 0)

        if isinstance(v, tuple) and len(v) == 4:
            w = v[3]
            v = v[:3]

        if isinstance(v, Vector4):
            self._v = v._v
            self._w = v._w
        elif isinstance(v, Vector):
            self._v = v
            if w is None:
                # Must exists as output socket of v.node (suppposed to be 'xyz')
                assert v._bsocket.name == 'xyz'
                self._w = v.w
            else:
                self._w = w
        else:
            self._v = v # A Vector or a tuple
            self._w = w # A Float or a float

    def __str__(self):
        return f"<Vector4 ({self._v}, {self._w}>"


    # ====================================================================================================
    # Properties
    # ====================================================================================================

    @property
    def v(self):
        return Vector(self._v)
    
    @v.setter
    def v(self, value):
        self._v = value

    @property
    def w(self):
        return Float(self._w)

    @w.setter
    def w(self, value):
        self._w = value

    @property
    def xyz(self):
        if isinstance(self._v, tuple):
            return self._v
        else:
            return self.v.xyz
        
    @property
    def as_tuple(self):
        return self.xyz + (self._w,)
    
    @property
    def is_tuple(self):
        return isinstance(self._v, tuple)
        
    # ====================================================================================================
    # In / Out
    # ====================================================================================================

    @classmethod
    def Input(cls, v=(0.0, 0.0, 0.0), w=0.0, name="", **props):
        
        prefix = "" if name == "" else name + " "

        return cls(Vector(v, prefix + "xyz", **props), Float(w, prefix + "w", **props))
    
    def out(self, name="", rank=0, panel=""):
        prefix = "" if name == "" else name + " "
        suffix = "" if rank == 0 else f" {rank}"

        self.v.out(prefix + "xyz" + suffix, panel=panel)
        self.w.out(prefix + "w"   + suffix, panel=panel)

    @classmethod
    def FromNode(cls, node, name="", rank=0):

        if hasattr(node, 'SOCKET_TYPE'):
            node = node.node

        prefix = "" if name == "" else name + " "
        suffix = "" if rank == 0 else f" {rank}"

        sv = prefix + "xyz" + suffix
        sw = prefix + "w"   + suffix

        return cls(node[sv], node[sw])
    
    def as_args(self, name="", rank=0):

        prefix = "" if name == "" else name + "_"
        suffix = "" if rank == 0 else f"_{rank}"

        sv = utils.snake_case(prefix + "xyz" + suffix)
        sw = utils.snake_case(prefix + "w"   + suffix)

        return {sv: self.v, sw: self.w}

    @classmethod
    def FromMatrix(cls, M, index=0):
        if isinstance(M, (list, tuple)):
            return cls(M[index*4:index*4 + 3], M[index*4 + 3])
        else:
            return cls.FromMatrix(M.as_tuple, index)
        
    def to_matrix(self, M, index=0):
        if isinstance(M, list):
            m = M
        elif isinstance(M, tuple):
            m = list(M)
        else:
            m = list(M.as_tuple)

        m[index*4:(index+1)*4] = self.as_tuple

        return m
    
    @classmethod
    def I(cls):
        return cls((1, 0, 0), 0)
        
    @classmethod
    def J(cls):
        return cls((0, 1, 0), 0)
        
    @classmethod
    def K(cls):
        return cls((0, 0, 1), 0)
        
    @classmethod
    def L(cls):
        return cls((0, 0, 0), 1)
        
    # ====================================================================================================
    # Native operations
    # ====================================================================================================

    def _neg(self):
        with Layout("Neg"):
            if self.is_tuple:
                return Vector4((-self._v[0], -self._v[1], -self._v[2]), -self._w)
            else:
                return Vector4(-self.v, -self._w)

    def _add(self, V):
        with Layout("Add"):
            V = Vector4(V)
            return Vector4(self.v + V.v, self._w + V._w)

    def _sub(self, V):
        with Layout("Sub"):
            V = Vector4(V)
            return Vector4(self.v - V.v, self._w - V.w)
        
    def _dot(self, V):
        with Layout("Dot"):
            V = Vector4(V)
            return self.v.dot(V.v) + self._w*V._w
        
    def _scale(self, scale):
        if self.is_tuple:
            return Vector4((self._v[0]*scale, self._v[1]*scale, self._v[2]*scale), self._w*scale)
        else:
            return Vector4(self.v.scale(scale), self._w*scale)
        
    @classmethod
    def _switch(cls, condition, false=((0, 0, 0), 0), true=((0, 0, 0), 0)):
        false = Vector4(false)
        true = Vector4(true)

        return cls(
            Vector.switch(condition, false.v, true.v),
            Float.switch(condition, false.w, true.w),
        )
    
    @classmethod
    def IndexSwitch(cls, *V, index=None):

        V4s = [Vector4(v) for v in V]

        with Layout("Vector 4 index switch"):
            v = Vector.IndexSwitch(*[v.v for v in V4s], index=index)
            w = Vector.IndexSwitch(*[v.w for v in V4s], index=index)

        return Vector4(v, w)

    
    def _squared_length(self):
        with Layout("Squared Length"):
            if self.is_tuple:
                return self._v[0]*self._v[0] + self._v[1]*self._v[1] + self._v[2]*self._v[2] + self._w*self._w
            else:
                return self.v.dot(self.v) + self._w*self._w

    def _length(self):
        with Layout("Length"):
            return gnmath.sqrt(self._squared_length())
        
    def _inverse_length(self):
        with Layout("Length"):
            return gnmath.inverse_sqrt(self._squared_length())
        
    def _normalize(self):
        with Layout("Normalize"):
            return self._scale(self._inverse_length())
        
    def _one_perp(self, index=0):
        """ Compute one perpendicular 4-vector

        x y z w
        -y x -w z

        index  returns
        -----  -------
        - 0    -y  x -w  z
        - 1     z  w -x -y  
        - 2    -w -z  y  x
        """
        x, y, z, w = self.as_tuple
        return Vector4((
            Float.IndexSwitch(-y,  z, -w, index=index),
            Float.IndexSwitch( x,  w, -z, index=index),
            Float.IndexSwitch(-w, -x,  y, index=index),
            ),
            Float.IndexSwitch( z, -y,  x, index=index)
        )
        
    def _align_axis_to(self, axis=0):
        """ Compute a matrix rotating axis index to the vector
        """
        with Layout("Align to Vector"):
            x, y, z, w = self._normalize().as_tuple
            mx, my, mz, mw = -x, -y, -z, -w
            M0 = Matrix((
                x,  y,  z,  w,
                my,  x, mw,  z,
                z,  w, mx, my,
                mw, mz,  y,  x
            ))
            M1 = Matrix((
                mw, mz,  y,  x,
                x,  y,  z,  w,
                my,  x, mw,  z,
                z,  w, mx, my,
            ))
            M2 = Matrix((
                z,  w, mx, my,
                mw, mz,  y,  x,
                x,  y,  z,  w,
                my,  x, mw,  z,
            ))
            M3 = Matrix((
                my,  x, mw,  z,
                z,  w, mx, my,
                mw, mz,  y,  x,
                x,  y,  z,  w,
            ))
            return Matrix.IndexSwitch(M0, M1, M2, M3, index=axis)
        
    def _mat_mul(self, M):
        with Layout("Multiply by matrix"):
            if isinstance(M, tuple):
                m = M
            else:
                m = M.as_tuple
            x, y, z, w = self.as_tuple

            return Vector4(
                (
                m[0]*x + m[4]*y + m[ 8]*z + m[12]*w, 
                m[1]*x + m[5]*y + m[ 9]*z + m[13]*w, 
                m[2]*x + m[6]*y + m[10]*z + m[14]*w, 
                ),
                m[3]*x + m[7]*y + m[11]*z + m[15]*w, 
            )

    # ====================================================================================================
    # Operations made with Vector4 Math Groyp
    # ====================================================================================================

    def neg(self):
        return Vector4.FromNode(vec4_.math(**self.as_args(), operation="Negative")._lc("Negative"))

    def add(self, V):
        return Vector4.FromNode(vec4_.math(**self.as_args(), **Vector4(V).as_args(rank=1), operation="Add")._lc("Add"))

    def sub(self, V):
        return Vector4.FromNode(vec4_.math(**self.as_args(), **Vector4(V).as_args(rank=1), operation="Subtract")._lc("Subtract"))
        
    def dot(self, V):
        return vec4_.math(**self.as_args(), **Vector4(V).as_args(rank=1), operation="Dot")._lc("Dot")
        
    def scale(self, scale):
        return Vector4.FromNode(vec4_.scale(**self.as_args(), scale=scale))
        
    def length(self):
        return vec4_.math(**self.as_args(), operation="Length")._lc("Length")
        
    def normalize(self):
        return Vector4.FromNode(vec4_.math(**self.as_args(), operation="Normalize")._lc("Normalize"))
    
    def one_perp(self, index=0):
        return Vector4.FromNode(vec4_.one_perp(**self.as_args(), index=index))
    
    def align_axis_to(self, axis=0):
        return vec4_.align_axis_to(**self.as_args(), axis=axis)

    def switch(self, condition, true=((0, 0, 0), 0)):
        return Vector4.FromNode(vec4_.switch(**self.as_args("false"), **true.as_args("true"))._lc("Switch"))

    def switch_false(self, condition, false=((0, 0, 0), 0)):
        return Vector4.FromNode(vec4_.switch(**false.as_args("false"), **self.as_args("true"))._lc("Switch"))
    
    def mat_mul(self, M):
        return Vector4.FromNode(vec4_.mat_mul(**self.as_args(), matrix=Matrix(M)))
    
    @classmethod
    def Cross(cls, V0, V1, V2):
        return Vector4.FromNode(vec4_.cross(**V0.as_args(), **V1.as_args(rank=1), **V2.as_args(rank=2)))

    # ====================================================================================================
    # Build Groups
    # ====================================================================================================

    @staticmethod
    def build_nodes():

        # ----------------------------------------------------------------------------------------------------
        # Dump a matrix
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Debug Matrix", is_group=True, prefix=vec4_):
            
            M = Matrix(name="Matrix")
            
            grid = Mesh.Grid(vertices_x=4, vertices_y=4, size_x=3, size_y=3).to_points()
            grid.transform(scale=(1, -1, 1))
            m = M.as_tuple
            
            for i, v in enumerate(m):
                grid.points[nd.index.equal(i)].Value = m[i]
                
            for feel in grid.points.for_each(value=Float("Value"), pos=nd.position):
                s = feel.value.to_string(decimals=3).to_curves(size=.3)
                s = Curve(s.realize()).fill()
                s.transform(translation=feel.pos)
                s.out()
                
            feel.generated.out()

        # ----------------------------------------------------------------------------------------------------
        # Get on axis vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Axis Vector", is_group=True, prefix=vec4_):
            """ Get an axis vector by its index in 0 to 3
            """
            
            axis = Integer(0, "Axis", 0, 3)
            
            Vector.IndexSwitch(
                (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0),
                index=axis,
                ).out("xyz")
                
            Float.IndexSwitch(0, 0, 0, 1, index=axis).out("w")

        # ----------------------------------------------------------------------------------------------------
        # 4-Vector math
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Math", is_group=True, prefix=vec4_):
        
            ope = Integer.MenuSwitch(
                named_sockets = {
                    "Add":          0,
                    "Subtract":     1,
                    "Negative":     2,
                    "Dot":          3,
                    "Length":       4,
                    "Normalize":    5,
                    },
                menu=Input("Operation"),
                )
        
            V0 = Vector4.Input(hide_value=True)
            V1 = Vector4.Input(hide_value=True)

            v_neg   = V0._neg()
            v_add   = V0._add(V1)
            v_sub   = V0._sub(V1)
            val_dot = V0._dot(V1)
            val_len = V0._length()
            v_norm  = V0._scale(1/V0._length())
            v_perp  = V0._one_perp(index=0)

            ok_value = Boolean.IndexSwitch(False, False, False, True, True, False, False, index=ope)
            ok_vec = ok_value.bnot()

            null_vec = Vector()
            with Vector.IndexSwitch(index=ope) as v:
                v_add.v.out()
                v_sub.v.out()
                v_neg.v.out()
                null_vec.out()
                null_vec.out()
                v_norm.v.out()
                v_perp.v.out()

            null_val = Float()
            with Float.IndexSwitch(index=ope) as w:
                v_add.w.out()
                v_sub.w.out()
                v_neg.w.out()
                null_val.out()
                null_val.out()
                v_norm.w.out()
                v_perp.w.out()

            with Float.IndexSwitch(index=ope) as val:
                null_val.out()
                null_val.out()
                null_val.out()
                val_dot.out()
                val_len.out()
                null_val.out()
                null_val.out()

            v.enable_output(ok_vec).out("xyz")
            w.enable_output(ok_vec).out("w")
            val.enable_output(ok_value).out("Value")

        # ----------------------------------------------------------------------------------------------------
        # Scale
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Scale", is_group=True, prefix=vec4_):
            V  = Vector4.Input()
            scale = Float(1., "Scale")

            V._scale(scale).out()

        # ----------------------------------------------------------------------------------------------------
        # Matrix Multiplication
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Mat Mul", is_group=True, prefix=vec4_):
            M = Matrix(None, "Matrix")
            V  = Vector4.Input()

            V._mat_mul(M).out()
        
        # ----------------------------------------------------------------------------------------------------
        # Switch with another 4_vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Switch", is_group=True,prefix=vec4_):
            condition = Boolean(False, "Condition")
            false  = Vector4.Input(name = "False")
            true   = Vector4.Input(name = "True")

            Vector4._switch(condition, false, true).out()
        
        # ----------------------------------------------------------------------------------------------------
        # Cross between 3 vectors
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Cross", is_group = True, prefix=vec4_):
            """ Generalized cross product between three 4-vectors
            """
            V0 = Vector4.Input((1, 0, 0), 0, hide_value=True)
            V1 = Vector4.Input((0, 1, 0), 0, hide_value=True)
            V2 = Vector4.Input((0, 0, 1), 0, hide_value=True)

            m = [0]*16
            m[  :4]  = V0.as_tuple
            m[ 4:8]  = V1.as_tuple
            m[ 8:12] = V2.as_tuple

            m[12:16] = (1, 0, 0, 0)
            x = Matrix(m).determinant()

            m[12:16] = (0, 1, 0, 0)
            y = Matrix(m).determinant()

            m[12:16] = (0, 0, 1, 0)
            z = Matrix(m).determinant()

            m[12:16] = (0, 0, 0, 1)
            w = Matrix(m).determinant()

            V = Vector4((x, y, z), w).normalize()

            V.out()
        
        # ----------------------------------------------------------------------------------------------------
        # One perpendicular vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("One Perp", is_group=True, prefix=vec4_):
            index = Integer(0, "Index", 0, 2)
            V  = Vector4.Input()
            V._one_perp(index=index).out()

        # ----------------------------------------------------------------------------------------------------
        # Align to Matrix
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Align Axis To", is_group=True, prefix=vec4_):
            V = Vector4.Input()
            axis = Integer(0, "Axis", 0, 3)
            V._align_axis_to(axis=axis).out("Matrix")

        # ----------------------------------------------------------------------------------------------------
        # Perpendicular Plane
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Perp Plane", is_group=True, prefix=vec4_):
            """ Compute two 4-vectors perpendicular to two 4-vectors

            This Group returns a normalized Matrix with:
            - Col 0 : normalized V0
            - Col 1 : normalized V1 plus perpendicular to V0
            - Col 2 : first perp vector
            - Col 3 : second perp vector
            """
            V0 = Vector4.Input((1, 0, 0), 0, hide_value=True)
            V1 = Vector4.Input((0, 1, 0), 0, hide_value=True)
            perp_last = Boolean(True, "Last Vectors", tip="Plane in vectors 0, 1 and Perp in vectors 2, 3.")

            with Layout("Make sure the two vectors are perpendicular and normalized"):
                V0 = V0.normalize()
                V1 = (V1 - V0.scale(V0.dot(V1))).normalize()

            with Layout("Rotation Matrix V1 -> L"):
                M = V1.align_axis_to(axis=3)

            with Layout("Inverse rotation of V0 as no w component"):
                iV0 = V0.mat_mul(M.transpose())

            with Layout("We need a 3D rotation to align this 3-vector to Z"):
                rot = Rotation().align_z_to_vector(iV0.v)
                Mrot = Matrix.CombineTransform(rotation=rot)

            with Layout("Final Matrix is the combination of the two"):
                M = (M.transpose() @ Mrot.transpose()).transpose()

            with Matrix.Switch(perp_last) as Res:
                m = M.as_tuple
                m2 = [0]*16
                m2[:8] = m[8:]
                m2[8:] = m[:8]
                Matrix(m2).out()

            with Res:
                M.out()

            Res.out()

    # ====================================================================================================
    # Dunder operations
    # ====================================================================================================

    def __neg__(self):
        return self.neg()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.scale(other)

    def __truediv__(self, other):
        return self.scale(1/other)
    
# ====================================================================================================
# Matrix 4D
# ====================================================================================================

class Matrix4:

    def __init__(self, m):
        if m is None:
            self._m = [
                1, 0, 0, 0,  
                0, 1, 0, 0,
                0, 0, 1, 0, 
                0, 0, 0, 1]
            
        elif isinstance(m, Matrix):
            self._m = m

        elif isinstance(m, Matrix4):
            if m.is_list:
                self._m = list(m._m)
            else:
                self._m = m._m
        else:
            self._m = list(m)

    @classmethod
    def Input(cls, name="Matrix"):
        return cls(Matrix(None, name=name))
    
    #@classmethod
    #def RotationMatrix(cls):
    #    return mat4_.rotation_matrix()

    def out(self, name="Matrix"):
        self.M.out(name=name)

    @property
    def is_list(self):
        return isinstance(self._m, list)

    @property
    def M(self):
        if self.is_list:
            return Matrix(self._m)
        else:
            return self._m

    @property
    def as_tuple(self):
        if self.is_list:
            return tuple(self._m)
        else:
            return self._m.as_tuple
        
    def _get_vector(self, index):
        m = self.as_tuple
        i = index*4
        return Vector4(m[i:i+3], m[i+3])

    def _set_vector(self, index, value):
        m = list(self.as_tuple)
        i = index*4
        m[i:i+4] = Vector4(value).as_tuple
        self._m = m
        return self
        
    @classmethod
    def FromVectors(cls, V0=None, V1=None, V2=None, V3=None):
        M = cls()
        if V0 is not None:
            M._set_vector(0, V0)
        if V1 is not None:
            M._set_vector(1, V1)
        if V2 is not None:
            M._set_vector(2, V2)
        if V3 is not None:
            M._set_vector(3, V3)

        return M
    
    # ====================================================================================================
    # Build the nodes
    # ====================================================================================================

    @staticmethod
    def build_nodes():

        # ---------------------------------------------------------------------------
        # Get the projection Matrix
        # ---------------------------------------------------------------------------

        with GeoNodes("Projection Matrix", is_group=True, prefix=group_) as tree:
            """ Get the Global projection Matrix from an object named "4D Parameters"

            By using a defined object, 4D parameters can be shared between different objects.

            The object must have the modifier "4D_ Parameters"
            """
            with Layout("Projection Matrix"):
                cloud = Object("4D Parameters").info().geometry.separate_components().point_cloud
                cloud.points(0, Matrix("Projection")).out("Projection")

        # Add the static method : projection_matrix
        tree.add_method(Matrix4)

        # ---------------------------------------------------------------------------
        # Split into 4 4-vectors
        # ---------------------------------------------------------------------------
        
        with GeoNodes("Vectors", is_group=True, prefix=mat4_) as tree:
            
            M4 = Matrix4.Input()
            M4._get_vector(0).out()
            M4._get_vector(1).out(rank=1)
            M4._get_vector(2).out(rank=2)
            M4._get_vector(3).out(rank=3)

        # Add the method : vectors
        tree.add_method(Matrix4, self_attr='M')

        # ---------------------------------------------------------------------------
        # Get one of the 4-vectors
        # ---------------------------------------------------------------------------

        with GeoNodes("Get Vector", is_group=True, prefix=mat4_) as tree:
            
            M4 = Matrix4.Input()
            index = Integer(0, "Index", 0, 3)

            Vector4.IndexSwitch(
                M4._get_vector(0),
                M4._get_vector(1),
                M4._get_vector(2),
                M4._get_vector(3),
                index = index,
                ).out()
            
        # Add the method : get_vector
        tree.add_method(Matrix4, self_attr='M', ret_class = Vector4)
            
        # ---------------------------------------------------------------------------
        # Set one of the 4-vectors
        # ---------------------------------------------------------------------------
            
        with GeoNodes("Set Vector", is_group=True, prefix=mat4_) as tree:
            
            M4 = Matrix4.Input()
            index = Integer(0, "Index", 0, 3)
            V = Vector4.Input()

            Matrix.IndexSwitch(
                M4._set_vector(0, V).M,
                M4._set_vector(1, V).M,
                M4._set_vector(2, V).M,
                M4._set_vector(3, V).M,
                index = index,
                ).out()
            
        # Add the method : set_vector
        tree.add_method(Matrix4, self_attr='M', ret_class = Matrix4)
            
        # ---------------------------------------------------------------------------
        # Create a Rotation Matrix from 6 angles
        # ---------------------------------------------------------------------------
        
        with GeoNodes("Rotation Matrix", is_group=True, prefix=mat4_) as tree:
            """ Create a rotation Matrix from 6 angles.
            """
            
            w_euler = Vector.Euler(0, "W Euler",  tip="Rotation XW, YW, ZW")
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
                
            with Matrix.MenuSwitch(menu=Input("Order")) as rot_mat:
                (X @ (Y @ Z)).out("XYZ")
                (X @ (Z @ Y)).out("XZY")
                (Y @ (X @ Z)).out("YXZ")
                (Y @ (Z @ X)).out("YZX")
                (Z @ (X @ Y)).out("ZXY")
                (Z @ (Y @ X)).out("ZYX")
                
            rot_mat.out("Matrix")

        # Add the method : rotation_matrix
        tree.add_method(Matrix4, ret_class = Matrix4)
                
            
# ====================================================================================================
# Position and Normals
# ====================================================================================================

class Position4(Matrix4):

    @property
    def _position(self):
        return self._get_vector(0)
    
    @_position.setter
    def _position(self, value):
        self._set_vector(0, value)

    @classmethod
    def Input(cls, name="Position4"):
        return cls(Matrix(None, name=name))

    def out(self, name="Position4"):
        self.M.out(name=name)

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def _translate(self, T):
        T = Vector4(T)
        self._position = self._position + T
        return self

    def _rotate(self, R, pivot=None):
        pivot = Vector4(pivot)
        self._position = self._position - pivot
        self._m = R @ self.M
        self._position = pivot + self._position
        return self
    
    def _scale(self, scale, pivot=None):
        pivot = Vector4(pivot)
        pos = self._position - pivot
        pos = pos.scale(scale)
        self._position = pivot + pos
        return self
    
    # ====================================================================================================
    # Build the nodes
    # ====================================================================================================

    @staticmethod
    def build_nodes():

        # ---------------------------------------------------------------------------
        # Translation Node
        # ---------------------------------------------------------------------------

        with GeoNodes("Translate", is_group=True, prefix=mat4_) as tree:

            P = Position4.Input()
            T = Vector4.Input()

            P._translate(T).out()

        tree.add_method(Position4, self_attr='M', ret_class=Position4)

        # ---------------------------------------------------------------------------
        # Rotation Node
        # ---------------------------------------------------------------------------

        with GeoNodes("Rotate", is_group=True, prefix=mat4_) as tree:

            P = Position4.Input()
            R = Matrix(None, "Rotation")
            pivot = Vector4.Input(name="Pivot")

            P._rotate(R, pivot=pivot).out()

        tree.add_method(Position4, self_attr='M', ret_class=Position4)


        # ---------------------------------------------------------------------------
        # Scale Node
        # ---------------------------------------------------------------------------

        with GeoNodes("Scale", is_group=True, prefix=mat4_) as tree:

            P = Position4.Input()
            scale = Float(1., "Scale")
            pivot = Vector4.Input(name="Pivot")

            P._scale(R, pivot=pivot).out()

        tree.add_method(Position4, self_attr='M', ret_class=Position4)

        # ---------------------------------------------------------------------------
        # Curve Local space
        # ---------------------------------------------------------------------------

        with GeoNodes("Curve Local Space", is_group=True, prefix=mat4_) as tree:

            P = Position4.Input()
            tg_axis = Integer(0, "Tangent Axis", 0, 3)

            with Layout("Vectors from Matrix"):
                V1 = P.get_vector(1)
                V2 = P.get_vector(2)
                V3 = P.get_vector(3)
                V0 = Vector4.Cross(V1, V2, V3)

            m = [0]*16

            with Matrix.IndexSwitch(index=tg_axis) as M:
                m[:4]   = V0.as_tuple
                m[4:8]  = V1.as_tuple
                m[8:12] = V2.as_tuple
                m[12:]  = V3.as_tuple
                Matrix(m).out()

            with M:
                m[:4]   = V3.as_tuple
                m[4:8]  = V0.as_tuple
                m[8:12] = V1.as_tuple
                m[12:]  = V2.as_tuple
                Matrix(m).out()

            with M:
                m[:4]   = V2.as_tuple
                m[4:8]  = V3.as_tuple
                m[8:12] = V0.as_tuple
                m[12:]  = V1.as_tuple
                Matrix(m).out()

            with M:
                m[:4]   = V1.as_tuple
                m[4:8]  = V2.as_tuple
                m[8:12] = V3.as_tuple
                m[12:]  = V0.as_tuple
                Matrix(m).out()

            M.out("Matrix")

        tree.add_method(Position4, self_attr='M', ret_class=Matrix4)

        # ---------------------------------------------------------------------------
        # Mesh Local space
        # ---------------------------------------------------------------------------

        with GeoNodes("Mesh Local Space", is_group=True, prefix=mat4_) as tree:

            P = Position4.Input()
            perp_last = Boolean(True, "Normals Last", tip="Tangent plane in vectors 0, 1 and Normal plane in 2, 3.")

            with Layout("Vectors from Matrix"):
                V1 = P.get_vector(1)
                V2 = P.get_vector(2)
                M = vec4_.perp_plane(**V1.as_args(), **V2.as_args(rank=1), last_vectors=perp_last)

            M.out()

        tree.add_method(Position4, self_attr='M', ret_class=Matrix4)


# ====================================================================================================
# Geometry 4D Interface
# ====================================================================================================

class Geometry4:

    # ====================================================================================================
    # Build nodes
    # ====================================================================================================

    def build_nodes():

        # ----------------------------------------------------------------------------------------------------
        # MODIFIER - 4D Parameters
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("4D_ Parameters"):
            """ Set an object as the global host for shared 4D parameters

            The group is part of the 3 fundamental modifiers:
            - 4D_ Parameters : global parameters
            - 4D_ Plunge : plunge a 3D object into 4D space
            - 4D_ Projection : project a 4D object into 3D Space

            The modifier requires 6 angles to defined the projection Matrix.
            The projection can be cancelled with 'No Transformation' switch.

            The user can optionnally display the 4 axis.
            """
            
            nope = Boolean(False, "No Transformation")
            
            # ---------------------------------------------------------------------------
            # Projection Matrix
            # ---------------------------------------------------------------------------
            
            with Layout("Store the projection matrix in a 1-Point Cloud"):
                P = mat4_.rotation_matrix().link_inputs(None, "Angles")
                
                cloud = Cloud.Points(1)
                P = P.switch(nope)
                cloud.points.Projection = P
                
            # ---------------------------------------------------------------------------
            # Axis
            # ---------------------------------------------------------------------------
            
            with Panel("Axis"):
                show_axis = Boolean(False, "Show Axis")
                axis_len  = Float(5, "Length")
                mat       = Material("4 Axis", "Material")
                
            a, b = axis_len*(-1/3), axis_len*(2/3)
            
            for i, col in enumerate(('red', 'lime', 'blue', 'black')):
                
                with Layout(f"Axis {'XYZW'[i]}"):
                    m = [0]*16
                    m[i] = a
                    m[4 + i] = b
                    M = P @ Matrix(m)

                    P0 = Vector4.FromMatrix(M, 0)
                    P1 = Vector4.FromMatrix(M, 1)
                    
                    l = Curve.Line(P0.v, P1.v)
                    l.splines.Color = Color(col)
                    
                    h = Cloud.Points(1, position=P1.v)
                    h.points.Color = Color(col)
                    h.points.Dir = P1.v - P0.v
                    if i == 0:
                        lines = l
                        heads = h
                    else:
                        lines += l
                        heads += h
                    
            with Layout("Shafts"):
                axis = lines.to_mesh(profile_curve = Curve.Circle(radius=0.025, resolution=16), fill_caps=True)
                
            with Layout("Heads"):
                cone = Mesh.Cone(vertices=16, radius_bottom=.15, radius_top=0, depth=0.25)
                cones = heads.instance_on(instance=cone)
                cones.rotate(rotation=Rotation().align_to_vector(Vector("Dir")))
                
                axis = Mesh(axis + cones.realize())
            
            axis.faces.material = mat
            axis.faces.shade_smooth = True
            
            (cloud + axis.switch_false(show_axis)).out("Geometry")
            
        # ----------------------------------------------------------------------------------------------------
        # MODIFIER - Plunge a Mesh into 4D
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("4D_ Plunge"):
            """ Plunge an object into 4D Space

            The group is part of the 3 fundamental modifiers:
            - 4D_ Parameters : global parameters
            - 4D_ Plunge : plunge a 3D object into 4D space
            - 4D_ Projection : project a 4D object into 3D Space

            The 4-position of the object is taken from the 3-position with the additional w argument.

            The 4-position is stored as vector 0 in a Matrix named M4D

            For Meshes, two normals are set as vector 1 and 2 of the Matrix:
            - 3D normal to the surface
            - (0, 0, 0, 1) : 4th axis

            For Curves, the tangent and two normals are stored in the matrix
            - tangent as vector 1
            - normal as vector 2
            - (0, 0, 0, 1) as vector 3
            """
            
            geo = Geometry()
            w = Float(0, "w")
            comps = geo.separate_components()

            R = Matrix4.RotationMatrix().link_inputs(None, "Rotation")
            
            with Layout("Mesh - Normal and W axis"):   
                
                mesh = comps.mesh

                m = [0]*16
                Vector4(nd.position, w).to_matrix(m, 0)
                Vector4(nd.normal, 0).to_matrix(m, 1)
                Vector4.L().to_matrix(m, 2)

                mesh.points.M4D = R @ Matrix(m)
                
            with Layout("Curve - tangent, normal and W axis"):
                
                curve = comps.curve

                m = [0]*16
                Vector4(nd.position, w).to_matrix(m, 0)
                Vector4(nd.normal, 0).to_matrix(m, 1)
                Vector4(nd.normal.cross(nd.curve_tangent), 0).to_matrix(m, 2)
                Vector4.L().to_matrix(m, 3)

                curve.points.M4D = R @ R @ Matrix(m)
                
            with Layout("Cloud - Nothing"):
                
                cloud = comps.point_cloud

                m = [0]*16
                Vector4(nd.position, w).to_matrix(m, 0)

                cloud.points.M4D = R @ R @ Matrix(m)
                
            Geometry.Join(mesh, curve, cloud).out()

        # ----------------------------------------------------------------------------------------------------
        # MODIFIER - Projection
        # ----------------------------------------------------------------------------------------------------
            
        with GeoNodes("4D_ Projection") as tree:
            """ Projection a 4D geometry into 3D

            The group is part of the 3 fundamental modifiers:
            - 4D_ Parameters : global parameters
            - 4D_ Plunge : plunge a 3D object into 4D space
            - 4D_ Projection : project a 4D object into 3D Space

            The user can optionnally display the M4D vectors        
            """
            
            geo = Geometry()
            
            with Panel("Options"):
                show_normals = Boolean(False, "Show Normals")
            
            comps = geo.separate_components()
            M = get_projection() @ Matrix("M4D")
            
            Pos = Vector4.FromMatrix(M, index=0)
            
            with Layout("Mesh - Simple projection"):
                
                mesh = comps.mesh
                mesh.position = Pos.v

                mesh = mesh[Boolean("Merge")].merge_by_distance()
                mesh.remove_named_attribute(name="Merge")

                vis = vis_mat4D(mesh, 1, 2)        
                mesh += vis.switch_false(show_normals)
                
            with Layout("Curve - Projection, tangent and normal"):   
                
                curve = comps.curve
                curve.position = Pos.v

                vis = vis_mat4D(curve, 1, 2, 3)
                curve += vis.switch_false(show_normals)
            
            with Layout("Cloud - Simple Projection"):   
                
                cloud = comps.point_cloud
                cloud.position = Pos.v
                
            Geometry.Join(mesh, curve, cloud).out("Geometry")

        tree.add_method(Geometry4, "projection", "", ret_class=Geometry)

# ====================================================================================================
# Curve 4D
# ====================================================================================================

class Curve4(Curve, Geometry4):

    # ====================================================================================================
    # Build nodes
    # ====================================================================================================

    def build_nodes():

        Group.add_method("4D_ Plunge", Curve, func_name='plunge', self_attr="", ret_class=Curve4)

        # ----------------------------------------------------------------------------------------------------
        # CONSTRUCTOR - Line
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Line", prefix=curve_) as tree:
            """ Create a 4D Line
            """
            resol = Integer(2, "Count", 2)

            with Panel("Start Point"):
                V0 = Vector4.Input()

            with Panel("End Point"):
                V1 = Vector4.Input((0, 0, 1))

            with Panel("Trim"):
                trim0 = Float.Factor(0, "Start", 0, 1)
                trim1 = gnmath.max(trim0, Float.Factor(1, "End", 0, 1))

            Dir = (V1 - V0).normalize()

            line = Curve.Line(V0.v, V1.v).trim(trim0, trim1).resample(mode='Count', count=resol)

            M = Dir.align_axis_to(axis=3)
            m = list(M.as_tuple)

            m[:3] = nd.position.xyz
            
            w0 = trim0.map_range(to_min=V0.w, to_max=V1.w)
            w1 = trim1.map_range(to_min=V0.w, to_max=V1.w)
            m[3] = (nd.index/(resol-1)).map_range(to_min=w0, to_max=w1)

            line.points.M4D = Matrix(m)
        
            line.out("Curve")

        tree.add_method(Curve4, ret_class=Curve4)

        # ----------------------------------------------------------------------------------------------------
        # CONSTRUCTOR - Circle
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Circle", prefix=curve_) as tree:

            radius  = Float(1, "Radius", 0.)
            resol   = Integer(32, "Count", 3)
            with Panel("Origin"):
                O  = Vector4.Input()

            with Panel("Trim"):
                trim0 = Float.Factor(0, "Start", 0, 1)
                trim1 = gnmath.max(trim0, Float.Factor(1, "End", 0, 1))

            factor     = Float.Factor(1, "Close", 0, 1)
            move_curve = Boolean(False, "Move Curve", tip="The curve moves to the origin when open")
            z_rot      = Float.Angle(0, "Rotation")

            close = factor.equal(1) & (trim0.equal(0) & trim1.equal(1))

            with Layout("Closed Circle"):
                circle = Curve.Circle(resolution=resol, radius=radius)
                circle.transform(translation = O.v, rotation = Rotation((0, 0, z_rot)))
                circle = Group("4D_ Plunge", geometry=circle, w=O.w).geometry

            with Layout("Compute the arc of the open line"):
                angle = (pi*factor)._lc("Half Arc Angle")
                r = (radius/factor)._lc("Arc Radius")
                resol = resol + 1

            with Layout("Base line for angles"):
                ag_min, ag_max = pi - angle, pi + angle
                angle0 = trim0.map_range(to_min=ag_min, to_max=ag_max)
                angle1 = trim1.map_range(to_min=ag_min, to_max=ag_max)

                line = Curve.Line((angle0, 0, 0), (angle1, 0, 0)).resample(mode='Count', count=resol)
                ag = line.points.sample_index(nd.position.x, nd.index)
                cag, sag = gnmath.cos(ag), gnmath.sin(ag)

            with Layout("Curved Line"):
                offset = Float.Switch(move_curve, -1, -factor)*radius
                line.position = Vector((offset + r*(1 + cag), r*sag, 0))

            with Layout("Straigth Line"):
                half_p = pi*radius
                straight = Curve.Line((offset, half_p, 0), (offset, -half_p, 0)).trim(trim0, trim1).resample(mode='Count', count=resol)
                line = line.switch(factor.equal(0), straight)

            with Layout("Rotation"):
                line.transform(translation = O.v, rotation=Rotation((0, 0, z_rot)))

            with Layout("Plunge into 4D"):
                m = [0]*16
                m[:3] = nd.position.xyz
                m[3] = O.w
                m[4:8]  = gnmath.cos(ag + z_rot), gnmath.sin(ag + z_rot), 0, 0
                m[8:12] = 0, 0, 1, 0
                m[12:]  = 0, 0, 0, 1

                line = Curve(line)
                line.points.M4D = Matrix(m)

            with Layout("Closed"):
                line = line.switch(close & factor.equal(1), circle)

            line.out("Curve")

        tree.add_method(Curve4, ret_class=Curve4)

    # ====================================================================================================
    # Curve to Surface
    # ====================================================================================================

    with GeoNodes("To Surface", prefix=curve_):

        curve0 = Curve()
        with Panel("Profile"):
            use_object  = Boolean(False, "Object")
            curve1      = Curve(None, "Curve")
            obj         = Object(None, "Curve Object")

        with Layout("Profile Curve"):
            curve1 = Curve(curve1.switch(use_object, obj.info().geometry))

        with Panel("Transformation"):
            twist_clx = Closure(None, "Twist X", tip="Factor -> Angle")
            twist_cly = Closure(None, "Twist Y", tip="Factor -> Angle")

            use_scale = Boolean(False, "Scale")
            scale_cl  = Closure(None, "Scale",    tip="Factor -> Scale")

        mat    = Material("4 Face", "Material")
        smooth = Boolean(True, "Shade Smooth")

        clouds  = []
        closeds = []
        ncurves = []
        nclouds = []

        for curve, name in zip([curve0, curve1], ["x", "y"]):
            with Layout(f"Transfer Curve {name} to cloud of points"):

                closed = curve.splines.sample_index(nd.is_spline_cyclic, index=0)
                ncurve = curve.points.count
                ncloud = ncurve.switch(closed, ncurve + 1)

                cloud  = Cloud.Points(count=ncloud)
                cloud.points.M4D = curve.points.sample_index(Matrix("M4D"), index=nd.index % ncurve)

                clouds.append(cloud)
                closeds.append(closed)
                ncurves.append(ncurve)
                nclouds.append(ncloud)

        shape = tuple(nclouds)
        nx, ny = nclouds
        idx = lambda i, j: ravel_indices(i, j, shape)
        ix, iy = unravel_index(nd.index, shape)

        ptx, pty = clouds

        # ---------------------------------------------------------------------------
        # At each point of the back bone, we rotate the profile such as:
        # Profile(I, J) -> Backbone(K, L)
        # ---------------------------------------------------------------------------

        with Layout("Backbone Matrix rotating I & J to Normals 2 & 3 of Curve X"):

            Mx = ptx.points.sample_index(Matrix("M4D"), ix)
            mx = Mx.as_tuple

            N2 = Vector4.FromMatrix(mx, 2)
            N3 = Vector4.FromMatrix(mx, 3)
            N1 = Vector4.FromMatrix(mx, 1)
            N0 = Vector4.Cross(N2, N3, N1)

            rm = [0]*16
            rm[:4]   = N2.as_tuple
            rm[4:8]  = N3.as_tuple
            rm[8:12] = N1.as_tuple
            rm[12:]  = N0.as_tuple

            R = Matrix(rm)

        # ---------------------------------------------------------------------------
        # A twist can be applied to the profile
        # The twist can vary along the backbone
        # ---------------------------------------------------------------------------

        with Layout("Twist & scale"):

            sig = ({'Factor': 'Float'}, {'Value': 'Float'})

            fac = ix/(nx - 1)
            twist_x = twist_clx.evaluate(signature=sig, factor=fac)
            twist_y = twist_cly.evaluate(signature=sig, factor=fac)
            scale   = scale_cl.evaluate(signature=sig,  factor=fac)
            scale = scale.switch_false(use_scale, 1)

            R_twist = Rotation((twist_x, twist_y, 0))

            M_twist = Matrix.CombineTransform(rotation=R_twist, scale=scale)         

            My = pty.points.sample_index(Matrix("M4D"), iy)
            My = M_twist @ My

        # ---------------------------------------------------------------------------
        # We can rotate each instance of profile along the backbone
        # ---------------------------------------------------------------------------

        with Layout("Rotate profile using this matrix"):

            My = R @ My

        # ---------------------------------------------------------------------------
        # Now we can build he grid
        # ---------------------------------------------------------------------------

        with Layout("Grid"):

            grid = Mesh.Grid(vertices_x = nx, vertices_y = ny)
            grid.corners.UV_Map = grid.uv_map

            # The normals are the ones of My
            grid.points.M4D = My

            with Layout("Position 4D"):

                m = list(My.as_tuple)
                for i in range(4):
                    m[i] += mx[i]

                grid.position = m[:3]

            grid.points.M4D = Matrix(m)

        # ---------------------------------------------------------------------------
        # When closed, the points can be merged
        # ---------------------------------------------------------------------------

        with Layout("Merge to close"):
            sel = Boolean.Switch(closeds[0], False, ix.equal(0) | ix.equal(nx - 1))
            sel |= Boolean.Switch(closeds[1], False, iy.equal(0) | iy.equal(ny - 1))
            grid.points.Merge = sel
            #grid = Mesh(grid)[sel].merge_by_distance()

        # ---------------------------------------------------------------------------
        # Finalized
        # ---------------------------------------------------------------------------

        with Layout("Finalize"):
            grid.faces.material = mat
            grid.faces.shade_smooth = smooth

        grid.out()


















            



    




        




    

    





    


    

# ====================================================================================================
# Create the base Engine
# ====================================================================================================

def build_engine():



    # ====================================================================================================
    # MODIFIER - Translation
    # ====================================================================================================

    with GeoNodes("Translation", prefix=mod_):
        """ Translate a geometry
        """
        geo = Cloud(Geometry())
        T = Vector4.Input()
        
        m = list(Matrix("M4D").as_tuple)
        x, y, z, w = T.as_tuple
        m[0] += x
        m[1] += y
        m[2] += z
        m[3] += w
        
        geo.points.M4D = Matrix(m)
        
        geo.out("Geometry")
        
    # ====================================================================================================
    # MODIFIER - Rotation
    # ====================================================================================================

    with GeoNodes("Rotation", prefix=mod_):
        """ 4D Rotation
        """
        geo = Geometry()
        
        with Panel("Pivot"):
            P = Vector4.Input()
            
        # Initial translation
        geo = mod_.translation(geo, **(-P).as_args())
        
        # Rotation
        M = group_.rotation_matrix().link_inputs(None, "Rotation")
        
        geo = Cloud(geo)
        geo.points.M4D = M @ Matrix("M4D")
        
        # Back to initial position
        geo = mod_.translation(geo, **P.as_args())
        
        geo.out("Geometry")

    # ====================================================================================================
    # MODIFIER - Scale
    # ====================================================================================================

    with GeoNodes("Scale", prefix=mod_):
        """ 4D Scale
        """
        geo = Geometry()
        scale = Float(1., "Scale")

        with Panel("Pivot"):
            P = Vector4.Input()

        p = P.as_tuple
        m = list(Matrix("M4D").as_tuple)
        for i in range(4):
            m[i] = p[i] + (m[i] - p[i])*scale

        geo = Mesh(geo)
        geo.points.M4D = Matrix(m)

        geo.out()


    # ====================================================================================================
    # MODIFIER - Get the Local Matrix
    # ====================================================================================================

    with GeoNodes("Curve Local Matrix", is_group=True, prefix=group_):

        M4D = Matrix(None, "Matrix")
        tg_axis = Integer(0, "Tangent Axis", 0, 3)


        with Layout("Vectors from Matrix"):
            m = M4D.as_tuple
            V1 = Vector4.FromMatrix(m, 1)
            V2 = Vector4.FromMatrix(m, 2)
            V3 = Vector4.FromMatrix(m, 3)
            V0 = Vector4.Cross(V1, V2, V3)

        m = [0]*16

        with Matrix.IndexSwitch(index=tg_axis) as M:
            m[:4]   = V0.as_tuple
            m[4:8]  = V1.as_tuple
            m[8:12] = V2.as_tuple
            m[12:]  = V3.as_tuple
            Matrix(m).out()

        with M:
            m[:4]   = V3.as_tuple
            m[4:8]  = V0.as_tuple
            m[8:12] = V1.as_tuple
            m[12:]  = V2.as_tuple
            Matrix(m).out()

        with M:
            m[:4]   = V2.as_tuple
            m[4:8]  = V3.as_tuple
            m[8:12] = V0.as_tuple
            m[12:]  = V1.as_tuple
            Matrix(m).out()

        with M:
            m[:4]   = V1.as_tuple
            m[4:8]  = V2.as_tuple
            m[8:12] = V3.as_tuple
            m[12:]  = V0.as_tuple
            Matrix(m).out()

        M.out("Matrix")



# ====================================================================================================
# Primitives shapes
# ====================================================================================================

def build_primitives():


    # ====================================================================================================
    # Mesh Plane
    # ====================================================================================================

    with GeoNodes("Plane", prefix=mesh_):
        """ Create a 4-Plane

        The plane is a XY plane or is defined by two vectors.

        In addition, the plane can be rotated.

        The user can optionnally create a plane perpendiculare to the two vectors.
        """
        
        O = Vector4.Input(name="Origin")
        
        use_vectors = Boolean(True, "Use Vectors")
        use_perp    = Boolean(False, "Perp. Plane")

        V1 = Vector4.Input(shape="Single")
        V2 = Vector4.Input(shape="Single")
        
        grid = Mesh.Grid().link_inputs(None, "Grid")
        
        grid = Group("4D_ Plunge", geometry=grid)._out

        # Rotation
        R = group_.rotation_matrix().link_inputs(None, "Rotation")
        
        # Defined only by Rotation
        with Geometry.Switch(use_vectors) as geo:
            r_grid = Mesh(grid)
            r_grid.points.M4D = R @ Matrix("M4D")
            r_grid.out("False")
        
        # Defined by vectors    
        with geo:

            # Matrix
            # - 2 first vectors are normalized vectors of the plan
            # - 2 last vectors are perpendicular

            M = vec4_.perp_plane(**V1.as_args(), **V2.as_args(rank=1))
                
            with Layout("Perpendicular Plane"):
                m = M.as_tuple
                m2 = [0]*16
                m2[:8] = m[8:]
                m2[8:] = m[:8]
                
                M = M.switch(use_perp, Matrix(m2))
                
            v_grid = Mesh(grid)
            v_grid.points.M4D = R @ (M @ Matrix("M4D"))
            
            v_grid.out("True")

        geo = mod_.translation(geo, **O.as_args())
        
        geo.out("Mesh")


    # ====================================================================================================
    # Torus
    # ====================================================================================================

    with GeoNodes("Torus", prefix=mesh_):

        curve0 = curve_.circle().link_inputs(None, "Curve 0")
        curve1 = curve_.circle().link_inputs(None, "Curve 1")

        twist_x = Float.Angle(0, "Twist X")
        twist_y = Float.Angle(0, "Twist Y")

        use_scale = Boolean(False, "Scale", hide_in_modifier=True)
        scale = Closure(None, "Scale", hide_in_modifier=True)

        trim0 = Input("Curve 0 > Trim > Start")
        trim1 = Input("Curve 0 > Trim > End")
        with Closure(closure=Input("Twist X")) as twist_clx:
            factor = Float(name="Factor")
            factor.map_range(to_min=trim0*twist_x, to_max=trim1*twist_x).out("Value")

        with Closure(closure=Input("Twist Y")) as twist_cly:
            factor = Float(name="Factor")
            factor.map_range(to_min=trim0*twist_y, to_max=trim1*twist_y).out("Value")

        try:
            mesh = curve_.to_surface(
                curve0, 
                curve_1 = curve1,
                twist_x = twist_clx,
                twist_y = twist_cly,
                scale   = use_scale,
                scale_1 = scale).link_inputs(None, exclude=["Profile", "Transformation"])
            
        except Exception as e:
            raise curve_.error(curve_.to_surface, e)
        
        mesh.out()

    # ====================================================================================================
    # Slices
    # ====================================================================================================

    with GeoNodes("Slices", prefix=mesh_):

        mesh = plunge(Mesh(), 0.0)

        with Panel("Backbone"):
            use_object  = Boolean(False, "Object")
            curve       = Curve(None, "Curve")
            obj         = Object(None, "Curve Object")

        with Layout("Backbone"):
            curve = Curve(curve.switch(use_object, obj.info().geometry))

            # Mesh Z axis oriented along the backbone tangent
            Mloc = group_.curve_local_matrix(Matrix("M4D"), tangent_axis=2)

        scale = Float(1., "Scale")

        for feel in curve.points.for_each(M4D=Matrix("M4D"), local = Mloc, scale = scale):

            try:
                slice = Mesh(mod_.scale(mesh, scale=feel.scale))
            except Exception as e:
                raise mod_.error(mod_.scale, e)
            
            slice.points.M4D = feel.local @ Matrix("M4D")

            mbb = feel.M4D.as_tuple
            msl = list(Matrix("M4D").as_tuple)

            msl[0] += mbb[0]
            msl[1] += mbb[1]
            msl[2] += mbb[2]
            msl[3] += mbb[3]

            slice.points.M4D = Matrix(msl)
            
            slice.switch(feel.scale.equal(0)).out("Generated")

        feel.generated.out()

    # ====================================================================================================
    # Hyper Sphere
    # ====================================================================================================

    with GeoNodes("Hyper Sphere", prefix=mesh_):

        radius = Float(1, "Radius", 0)
        slices = Integer(7, "Slices", 1)
        sphere = Mesh.UVSphere(radius=radius).link_inputs(None, "Sphere")
        sphere.corners.UV_Map = sphere.uv_map

        line = curve_.line(xyz=0, w = -radius, xyz_1=0, w_1=radius, count=slices + 2)
        w = 2*nd.index/(slices+1) - 1
        scale = gnmath.sqrt(gnmath.max(0, 1 - w*w))

        hsph = mesh_.slices(sphere, curve=line, scale=scale)

        hsph.out()











        


        



        



        




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
# Basic operations
#
# Basic operations are put in groups rather than macros to make trees more compact

def build_operations():

    # ----------------------------------------------------------------------------------------------------
    # 4-Vector Operations

    Vector4.build_operations()

    # ----------------------------------------------------------------------------------------------------
    # Rotate a M4 Matrix
    # Equivalent to rot @ M4

    with GeoNodes("Rotate M4", is_group=True, prefix=matrix_):

        rot = Matrix(None, "Rotation")
        M4  = Matrix(None, "M4")

        m = M4.separate
        a = []
        for i in range(4):
            U = Vector4(m[4*i:4*(i+1)])
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

        ux, uy, uz, uw = Vector4(panel="V0")
        vx, vy, vz, vw = Vector4(panel="V1")
        t = Vector4(panel="V2")

        normalize = Boolean(False, "Normalize")

        b = [       0      ,  uw*vz - uz*vw, -uw*vy + uy*vw, -uy*vz + uz*vy,
                -uw*vz + uz*vw,         0     ,  uw*vx + ux*vw,  ux*vz - uz*vx,
                uw*vy - uy*vw, -uw*vx + ux*vw,         0     , -ux*vy + uy*vx,
                uy*vz - uz*vy, -ux*vz + uz*vx,  ux*vy - uy*vx,        0       ]
        S = Matrix(b)

        V = Vector4(t).matmul(S)

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

        V = Vector4(t).matmul(S)

        V = V.normalize(normalize)
        V.out()

        a[:4] = V.a
        Matrix(a).out()

    # ----------------------------------------------------------------------------------------------------
    # Align a 4-rotation to a vector

    with GeoNodes("Align X Axis to Vector", is_group=True, prefix=matrix_):

        vector   = Vector4(panel="Vector")

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

            J = Vector4(0, 1, 0, 0)
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
            V = Vector4((0, 0, 0, 1))
            done = null

        Vs = []
        for i in range(2):
            with Layout(f"Decompose {'KL'[i]} along target, U and V, a perpendicular vector"):

                K = Vector4([(0, 0, 1, 0), (0, 0, 0, 1)][i])

                c = K.dot(T)
                V_ = (K - T.scale(c)).normalize()

                d = V_.dot(U)
                Vs.append((V_ - U.scale(d)).normalize())

        V = Vs[0].switch(Vs[0].x.null_, Vs[1]).switch(done, V)

        W = Vector4.FromNode(vector_.cross_product(True, *T, *U, *V).node)

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
            a[15]   = 1               # 12:16 = (0, 0, 0, 1) second normal

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
            look = Vector4(M_proj.separate[12:])

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
            normal_A = Vector4(a[4:8])
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

            tg = Vector4.FromNode(matrix_.cross_product(M).node)
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
        trans = Vector4(panel="Translation")

        a = list(Matrix("M4").separate)
        for i in range(4):
            a[i] += trans[i]

        geo.points._M4 = a
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Scale

    with GeoNodes("Scale", fake_user=False, prefix=mod_):

        geo = Cloud(Geometry())

        scale = Vector4(1, 1, 1, 1, panel="Scale")
        pivot = Vector4(panel="Pivot")

        a = list(Matrix("M4").separate)
        for i in range(4):
            a[i] = pivot[i] + scale[i]*(a[i] - pivot[i])

        geo.points._M4 = a
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # MODIFIER - Rotation

    with GeoNodes("Rotation", fake_user=False, prefix=mod_):

        geo = Geometry()

        pivot = Vector4(panel="Pivot")

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
        pos = Vector4(panel="Location")
        length = Float(1, "Length")
        is_rot = Boolean(True, "Rotation / M4")

        m = M.separate
        v_pos = Vector4(m[:4])

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
                U = Vector4(a)
                P_rot = Vector4.FromNode(matrix_.dot_vector(M, *U).node)

            with Layout("Vector selection"):
                P_m4 = Vector4(m[4*i:4*(i+1)])
                P = Vector4.FromNode(vector_.switch(is_rot, *P_m4, *P_rot).node)

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
            pos = Vector4(m[:4])

            vis = debug_.matrix(feel.m, **pos.args(), rotation_m4=is_rot, link_from='TREE')
            feel.generated.geometry = vis

        feel.generated.geometry.out()

# =============================================================================================================================
# Primitives

def build_primitives_OLD():

    # ----------------------------------------------------------------------------------------------------
    # Line

    with GeoNodes("Line", prefix=curve_):

        start = Vector4(panel="Start")
        end   = Vector4(0, 0, 0, 1, panel="End")
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
            backbone.remove_named_attribute(name="M4")

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
            mesh.remove_named_attribute(name="BB*")

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

        size   = Vector4((1, 1, 1, 1), panel="Size", single_value=True)
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
            Vector4(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12),  1/2),
            Vector4(1/2/sqrt(10),  1/2/sqrt(6),  1/sqrt(12), -1/2),
            Vector4(1/2/sqrt(10),  1/2/sqrt(6), -2/sqrt(12),    0),
            Vector4(1/2/sqrt(10), -3/2/sqrt(6),           0,    0),
            Vector4( -2/sqrt(10),            0,           0,    0),
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
            light_loc   = Vector4([emitter.points.sample_index(Float(c), index=0) for c in 'xyzw'])
            light_power = emitter.points.sample_index(Float("Power"), index=0)

        with Layout("Reflection"):

            a = Matrix("M4").separate

            pos4     = Vector4(a[:4])
            normal_A = Vector4(a[4:8])
            normal_B = Vector4(a[8:12])

            in_vector = pos4 - light_loc
            ray = in_vector.normalize()

            with Layout("Show Incident Ray"):
                with geo.points.for_each(m4 = Matrix("M4")) as feel:
                    pos = Vector4(feel.m4.separate[:4])
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
                    pos = Vector4(feel.m4.separate[:4])
                    line = curve_.line(**pos.args("Start"), **(pos + Vector4((feel.x, feel.y, feel.z, feel.w)).scale(rays_length)).args("End"), count=2)
                    feel.generated.geometry = line

                reflected_rays = feel.generated.geometry

        with Layout("4D Camera direction"):

            M_proj = matrix_.projection_matrix()
            opp = M_proj.opposite_

            look = Vector4(M_proj.separate[12:])

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

        v  = Vector4(0, 0, "")
        Na = Vector4(0, 0, "Normal A")
        Nb = Vector4(0, 0, "Normal B")

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

            light_loc = Vector4.Position(cloud, sample_index=0)
            color     = cloud.points.sample_index(Color.Named("Color"),     0)
            intensity = cloud.points.sample_index(Float.Named("Intensity"), 0)

        mesh, curve, cloud, inst = geo.mesh, geo.curve, geo.point_cloud, geo.instances

        # ----------------------------------------------------------------------------------------------------
        # Incident vector

        with Layout("Incident vector"):

            v  = Vector4.Position(mesh)
            Na = Vector4.Normal(mesh, "A")
            Nb = Vector4.Normal(mesh, "B")

            vray     = v - light_loc
            distance = vray.length
            incident = vray/distance

        # ----------------------------------------------------------------------------------------------------
        # Reflected vector

        #ref_node  = math_.surface_reflection(*incident.args, *Na.args, *Nb.args)
        ref_node  = Group.Prefix(math_, "Surface Reflection", [incident.V, incident.w, Na.V, Na.w, Nb.V, Nb.w])
        reflected = Vector4.FromNode(ref_node)

        # ----------------------------------------------------------------------------------------------------
        # Intensity

        #proj = Vector4.NodeOutput(math_.projection_matrix(), "R 3")
        proj = Vector4.FromNode(Group.Prefix(math_, "Projection Matrix"), "R 3")

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
