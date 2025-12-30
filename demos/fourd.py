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
mat_    = G("4D Matrix")
vec_    = G("4D Vector")

main_   = G("4")
geo_    = G("4D Geometry")
mesh_   = G("4D Mesh")
curve_  = G("4D Curve")
op_     = G("4D G")



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
    build_geometry_nodes()

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
    # GROUP - Reading 4D Shading Attributes
    # ----------------------------------------------------------------------------------------------------

    with ShaderNodes("4D Attributes", is_group=True):

        # ---------------------------------------------------------------------------
        # Interior
        # ---------------------------------------------------------------------------

        interior = snd.attribute("Interior").factor

        # ---------------------------------------------------------------------------
        # Color
        # ---------------------------------------------------------------------------

        fcol = snd.attribute("Color").color
        bcol = snd.attribute("Back Color").color

        col = fcol.mix(bcol, factor=interior)

        col.out("Color")
        interior.out("Interior")
        fcol.out("Front Color")
        bcol.out("Back Color")

        # ---------------------------------------------------------------------------
        # Roughness
        # ---------------------------------------------------------------------------

        snd.attribute("Roughness").factor.out("Roughness")

        # ---------------------------------------------------------------------------
        # Normal
        # ---------------------------------------------------------------------------

        fac = snd.attribute("Use Normal").factor
        attr = snd.attribute("Projected Normal").vector
        normal = snd.geometry().normal.mix(attr, factor=fac)
        normal.out("Normal")

        # ---------------------------------------------------------------------------
        # Emission
        # ---------------------------------------------------------------------------

        fac = snd.attribute("Use Emission").factor
        attr = snd.attribute("Emission").factor
        emission = Float(0).mix(other=attr, factor=fac)
        emission.out("Emission")

    # ----------------------------------------------------------------------------------------------------
    # SHADER - Default Material
    # ----------------------------------------------------------------------------------------------------

    with ShaderNodes("4D Surface"):

        node = Group("4D Attributes")

        ped = Shader.Principled(
            base_color          = node.color,
            metallic            = 0.1,
            roughness           = node.roughness, #interior.map_range(to_min=0.1, to_max=0.8),
            normal              = node.normal,
            emission_strength   = node.emission,
            emission_color      = node.color,
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
            base_color = snd.attribute(attribute_name="Color").color,
            metallic   = 0.,
            roughness  = 0.,
            emission_strength   = snd.attribute(attribute_name="Intensity").factor,
            normal     = bump,
            )

        ped.out()

# ====================================================================================================
# MACROS
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Base vertices to draw debug lines
# ----------------------------------------------------------------------------------------------------

def domain_to_vertices(domain):

    with Layout("Mesh vertices as origin"):
        pos = domain.capture_attribute(nd.position)
        pts = Cloud.Points(count=domain.count, position=domain.sample_index(nd.position, index=nd.index))
        return pts.to_vertices()

# ----------------------------------------------------------------------------------------------------
# Draw a vector
# ----------------------------------------------------------------------------------------------------

def draw_vector(domain, v, scale=1.0):

    with Layout("Draw vectors"):
        verts = domain_to_vertices(domain)
        v = domain.sample_index(v, index=nd.index)
        verts = verts.points.extrude(offset=v, offset_scale=scale)
        return verts
    
# ----------------------------------------------------------------------------------------------------
# Draw UV Normals
# ----------------------------------------------------------------------------------------------------

def draw_normals(domain, u, v, scale=1.0):

    with Layout("Draw UV Normals"):
        verts = domain_to_vertices(domain)
        verts.points.U = domain.sample_index(u, index=nd.index)
        verts.points.V = domain.sample_index(v, index=nd.index)

        verts = verts.points.extrude(offset=Vector("U"), offset_scale=scale)
        verts = verts.points[verts.top].extrude(offset=Vector("V"), offset_scale=scale)
        verts = verts.points[verts.top].extrude(offset=-Vector("U"), offset_scale=scale)
        verts = verts.points[verts.top].extrude(offset=-Vector("V"), offset_scale=scale)
        
        return verts


    
# ----------------------------------------------------------------------------------------------------
# Visualize Normals
# ----------------------------------------------------------------------------------------------------

def vis_normals(geo, scale=1.0):

    # ---------------------------------------------------------------------------
    # Extrude one arrow
    # ---------------------------------------------------------------------------

    def draw(mesh, sel, order, v):

        with Layout("Base"):
            msh = mesh.points[sel].extrude(v, offset_scale=scale)

        return msh
        
        with Layout("First"):
            if order >= 1:
                top = msh.top
                msh.points[top].extrude(-v + .3, offset_scale=.3*scale)
            
        with Layout("Second"):
            if order == 2:
                msh.points[top & msh.top.bnot()].extrude(-v - .3, offset_scale=.3*scale)

        return msh
    
    comps = geo.separate_components()
    mesh  = comps.mesh
    curve = comps.curve

    # ---------------------------------------------------------------------------
    # Faces
    # ---------------------------------------------------------------------------
    
    with Layout("Faces Normals"):

        count = mesh.faces.count

        cloud = Cloud.Points(count)
        cloud.points.position = mesh.faces.sample_index(nd.position, nd.index)
        cloud.points.UVNN = mesh.faces.sample_index(Matrix("UVNN"), nd.index)
        faces_normals = cloud.to_vertices()

        M = Matrix4("UVNN")

        # Normals
        if False:
            N1 = M.get_vector4(2)
            N2 = M.get_vector4(3)
        # U, V
        else:
            N1 = M.get_vector4(0)
            N2 = M.get_vector4(1)

        faces_normals = draw(faces_normals, True, 0, N1.v)
        faces_normals = draw(faces_normals, nd.index.less_than(count), 1, N2.v)

    # ---------------------------------------------------------------------------
    # Curves
    # ---------------------------------------------------------------------------

    with Layout("Curves Normals"):

        count = curve.points.count

        M = Matrix4("TNNN")
        N1 = M.get_vector4(1)
        N2 = M.get_vector4(2)
        N3 = M.get_vector4(3)

        sel = nd.index.less_than(count)

        curve_normals = curve.to_mesh()
        curve_normals = draw(curve_normals, sel, 0, N1.v)
        curve_normals = draw(curve_normals, sel, 1, N2.v)
        curve_normals = draw(curve_normals, sel, 2, N3.v)

    return Mesh(faces_normals + curve_normals)


# ----------------------------------------------------------------------------------------------------
# Finalize modifiers
# ----------------------------------------------------------------------------------------------------

def finalize(geo, mat_name="4 Face"):
    with Layout("Projection"):

        with Panel("Projection"):
            ok_proj = Boolean(False, "Project")

        projected = Geometry4(geo).projection().link_inputs(None, "Projection") #, exclude=["Debug"])

        return geo.switch(ok_proj, projected)


# ----------------------------------------------------------------------------------------------------
# Grid Ravel indices
# ----------------------------------------------------------------------------------------------------

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

        # ---------------------------------------------------------------------------
        # Special
        # ---------------------------------------------------------------------------

        # None -> Null Vector
        if v is None:
            v = (0, 0, 0)
            if w is None:
                w = 0

        # Str -> Two named attributes
        elif isinstance(v, str):

            assert w is None, f"Shouldn't happen {v=}, {w=}"

            s = v

            v = Vector(f"{s} v")
            w = Float(f"{s} w")

        # 4-tuple -> a 4-Vectoe
        elif isinstance(v, tuple) and len(v) == 4:

            assert w is None, f"Shouldn't happen {v=}, {w=}"

            vec = v

            v = vec[:3]
            w = vec[3]

        # ---------------------------------------------------------------------------
        # Set locals
        # ---------------------------------------------------------------------------

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
    
    def _lc(self, title, color=None):
        if hasattr(self._v, 'SOCKET_TYPE'):
            self._v._lc(title + " v", color)
        if hasattr(self._w, 'SOCKET_TYPE'):
            self._w._lc(title + " w", color)
        return self
            

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
    def is_tuple(self):
        return isinstance(self._v, tuple)

    @property
    def xyz(self):
        if self.is_tuple:
            return self._v
        else:
            return self.v.xyz
        
    @property
    def xyzw(self):
        return self.xyz + (self._w,)
    
    # ====================================================================================================
    # Node in / out
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Create Group input
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Input(cls, v=(0.0, 0.0, 0.0), w=0.0, name="", **props):
        
        prefix = "" if name == "" else name + " "

        return cls(Vector(v, prefix + "xyz", **props), Float(w, prefix + "w", **props))

    # ----------------------------------------------------------------------------------------------------
    # Node output
    # ----------------------------------------------------------------------------------------------------

    def out(self, name="", rank=0, panel=""):
        prefix = "" if name == "" else name + " "
        suffix = "" if rank == 0 else f" {rank}"

        self.v.out(prefix + "xyz" + suffix, panel=panel)
        self.w.out(prefix + "w"   + suffix, panel=panel)

    # ----------------------------------------------------------------------------------------------------
    # Read from node outputs
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def FromNode(cls, node, name="", rank=0):

        if hasattr(node, 'SOCKET_TYPE'):
            node = node.node

        prefix = "" if name == "" else name + " "
        suffix = "" if rank == 0 else f" {rank}"

        sv = prefix + "xyz" + suffix
        sw = prefix + "w"   + suffix

        return cls(node[sv], node[sw])

    # ----------------------------------------------------------------------------------------------------
    # Args passed in method call
    # ----------------------------------------------------------------------------------------------------
    
    def args(self, name="", rank=0):
        """ Arguments dict

        ``` python
            mesh.method(**V4.args(name="P", rank=1))
            # Equivalent to
            mesh.method(P_xyz_1=V.v, P_w_1=w)
        ```
        """

        prefix = "" if name == "" else name + "_"
        suffix = "" if rank == 0 else f"_{rank}"

        sv = utils.snake_case(prefix + "xyz" + suffix)
        sw = utils.snake_case(prefix + "w"   + suffix)

        return {sv: self.v, sw: self.w}
    
    # ====================================================================================================
    # Conventions
    # ====================================================================================================

    @classmethod
    def Position(cls):
        return cls("P4")
    
    def store_position(self, geo):

        with Layout("Store Position"):

            # To address point domain
            cloud = Cloud(geo)

            v = cloud.points.capture_attribute(v=self.v, w=self.w)

            cloud.points.P4_v = v
            cloud.points.P4_w = v.w

            cloud.position = v

            geo._jump(cloud)

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
            Vector.Switch(condition, false.v, true.v),
            Float.Switch(condition, false.w, true.w),
        )
    
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
        
    def one_perp(self, index=0):
        """ Compute one perpendicular 4-vector

        index  returns
        -----  -------
        - 0     y -x  w -z
        - 1     z -w -x  y  
        - 2     w  z -y -x
        """
        x, y, z, w = self.xyzw
        return Vector4.IndexSwitch(
            Vector4(( y, -x,  w, -z)),
            Vector4(( z, -w, -x,  y)),
            Vector4(( w,  z, -y, -x)),
            index=index)

    # ====================================================================================================
    # Operations made with Vector4 Math Group
    # ====================================================================================================

    def neg(self):
        return Vector4.FromNode(vec_.math(**self.args(), operation="Negative")._lc("Negative"))

    def add(self, V):
        return Vector4.FromNode(vec_.math(**self.args(), **Vector4(V).args(rank=1), operation="Add")._lc("Add"))

    def sub(self, V):
        return Vector4.FromNode(vec_.math(**self.args(), **Vector4(V).args(rank=1), operation="Subtract")._lc("Subtract"))
        
    def dot(self, V):
        return vec_.math(**self.args(), **Vector4(V).args(rank=1), operation="Dot")._lc("Dot")
        
    def scale(self, scale):
        return Vector4.FromNode(vec_.scale(**self.args(), scale=scale))
        
    def length(self):
        return vec_.math(**self.args(), operation="Length")._lc("Length")
        
    def normalize(self):
        return Vector4.FromNode(vec_.math(**self.args(), operation="Normalize")._lc("Normalize"))
    
    def switch(self, condition, true=((0, 0, 0), 0)):
        return Vector4.FromNode(vec_.switch(condition, **self.args("false"), **true.args("true"))._lc("Switch"))

    def switch_false(self, condition, false=((0, 0, 0), 0)):
        return Vector4.FromNode(vec_.switch(condition, **false.args("false"), **self.args("true"))._lc("Switch"))
    
    @classmethod
    def Cross(cls, V0, V1, V2):
        return Vector4.FromNode(vec_.cross(**V0.args(), **V1.args(rank=1), **V2.args(rank=2)))
    
    @classmethod
    def IndexSwitch(cls, *vectors4, index=None):

        V4s = [Vector4(V) for V in vectors4]

        with Layout("Vector 4 index switch"):
            v = Vector.IndexSwitch(*[v.v for v in V4s], index=index)
            w = Vector.IndexSwitch(*[v.w for v in V4s], index=index)

        return Vector4(v, w)
    
    def project_on_plane(self, A=None, B=None, normalize=None):
        node = vec_.project_on_plane(**self.args(), **Vector4(A).args(name="A"), **Vector4(B).args(name="B"), normalize=normalize)
        return Vector4(node)

    # ====================================================================================================
    # Build Groups
    # ====================================================================================================

    @staticmethod
    def build_nodes():

        # ----------------------------------------------------------------------------------------------------
        # Combine / Separate
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Combine XYZW", is_group=True, prefix=vec_):
            x = Float(0, "X")
            y = Float(0, "Y")
            z = Float(0, "Z")
            w = Float(0, "W")
            Vector((x, y, z)).out("xyz")
            Float("w").out("w")

        with GeoNodes("Separate", is_group=True, prefix=vec_):
            V4 = Vector4.Input()
            x, y, z, w = V4.xyzw
            x.out("X")
            y.out("Y")
            z.out("Z")
            w.out("W")

        # ----------------------------------------------------------------------------------------------------
        # Dump a matrix
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Debug Matrix", is_group=True, prefix=mat_):
            
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
        # Get an axis vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Axis", is_group=True, prefix=vec_) as tree:
            """ Get an axis vector by its index in 0 to 3
            """
            
            axis = Integer(0, "Axis", 0, 3)
            
            Vector.IndexSwitch(
                (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0),
                index=axis,
                ).out("xyz")
                
            Float.IndexSwitch(0, 0, 0, 1, index=axis).out("w")

        tree.add_method(Vector4, ret_class=Vector4)

        # ----------------------------------------------------------------------------------------------------
        # 4-Vector math
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Math", is_group=True, prefix=vec_):
        
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
            v_perp  = V0.one_perp(index=0)

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

        with GeoNodes("Scale", is_group=True, prefix=vec_):
            V  = Vector4.Input()
            scale = Float(1., "Scale")

            V._scale(scale).out()

        # ----------------------------------------------------------------------------------------------------
        # Switch with another 4_vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Switch", is_group=True,prefix=vec_):
            condition = Boolean(False, "Condition")
            false  = Vector4.Input(name = "False")
            true   = Vector4.Input(name = "True")

            Vector4._switch(condition, false, true).out()
        
        # ----------------------------------------------------------------------------------------------------
        # Cross between 3 vectors
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Cross", is_group = True, prefix=vec_):
            """ Generalized cross product between three 4-vectors
            """
            V0 = Vector4.Input((1, 0, 0), 0, hide_value=True)
            V1 = Vector4.Input((0, 1, 0), 0, hide_value=True)
            V2 = Vector4.Input((0, 0, 1), 0, hide_value=True)

            m = [0]*16
            m[  :4]  = V0.xyzw
            m[ 4:8]  = V1.xyzw
            m[ 8:12] = V2.xyzw

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

        with GeoNodes("One Perp", is_group=True, prefix=vec_):
            index = Integer(0, "Index", 0, 2)
            V  = Vector4.Input()
            V.one_perp(index=index).out()

        # ----------------------------------------------------------------------------------------------------
        # Project on a plane
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Project on Plane", is_group=True, prefix=vec_) as tree:

            V = Vector4.Input()
            A = Vector4.Input(name = "A")
            B = Vector4.Input(name = "B")
            normalize = Boolean(False, "Normalize")

            with Layout("Normalize"):
                A = A.switch(normalize, A.normalize())
                B = B.switch(normalize, B.normalize())
                B = B.switch(normalize, B - A.scale(A.dot(B)))

            with Layout("A component"):
                a = A.scale(V.dot(A))

            with Layout("B component"):
                b = B.scale(V.dot(B))

            with Layout("Projected"):
                P = a + b
                P.v.out("xyz")
                P.w.out("w")
                P.length().out("Length")


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

class Matrix4(Matrix):
        
    @classmethod
    def FromVectors(cls, V0=None, V1=None, V2=None, V3=None):
        m = [0]*16
        m[:4]   = Vector4(V0).xyzw
        m[4:8]  = Vector4(V1).xyzw
        m[8:12] = Vector4(V2).xyzw
        m[12:]  = Vector4(V3).xyzw

        return cls(m)

    def get_vector4(self, index):
        return Vector4(self.get_col(index))

    def set_vector4(self, index, V):
        return self.set_col(index, Vector4(V))
                               
    def get_vectors(self):
        m = self.as_tuple
        return Vector4(m[:4]), Vector4(m[4:8]), Vector4(m[8:12]), Vector4(m[12:])
    
    @classmethod
    def AlignAxisToVector(cls, axis=0, V4=(1, 0, 0, 0)):
         return cls(mat_.align_axis_to_vector(axis=axis, **Vector4(V4).args()))
    
    def rotate_vector(self, V4):
        return Vector4(mat_.rotate_vector(matrix=self, **Vector4(V4).args()))
    
    def __matmul__(self, other):
        if isinstance(other, Vector4):
            return self.rotate_vector(other)
        else:
            return super().__matmul__(other)

    
    # ====================================================================================================
    # Build the nodes
    # ====================================================================================================

    @staticmethod
    def build_nodes():

        # ---------------------------------------------------------------------------
        # Get the projection Matrix
        # ---------------------------------------------------------------------------

        with GeoNodes("Projection Matrix", is_group=True, prefix=mat_) as tree:
            """ Get the Global projection Matrix from an object named "4D Parameters"

            By using a defined object, 4D parameters can be shared between different objects.

            The object must have the modifier "4D_ Parameters"
            """
            with Layout("Projection Matrix"):
                cloud = Object("4D Parameters").info().geometry.separate_components().point_cloud
                
                Proj = cloud.points(0, Matrix("Projection"))
                Dir  = Vector4(Proj.get_row(3))
                
                Proj.out("Projection")
                Dir.out()

        # Add the static method : projection_matrix
        tree.add_method(Matrix4, ret_class=Matrix4)
            
        # ---------------------------------------------------------------------------
        # Create a Rotation Matrix from 6 angles
        # ---------------------------------------------------------------------------
        
        with GeoNodes("Rotation Matrix", is_group=True, prefix=mat_) as tree:
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

        # ----------------------------------------------------------------------------------------------------
        # Rotate a vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Rotate Vector", is_group=True, prefix=mat_):
            M = Matrix4(name="Matrix")
            V = Vector4.Input()

            m = M.as_tuple
            x, y, z, w = V.xyzw

            Vector4((
                m[0]*x + m[4]*y + m[ 8]*z + m[12]*w,
                m[1]*x + m[5]*y + m[ 9]*z + m[13]*w,
                m[2]*x + m[6]*y + m[10]*z + m[14]*w,
                m[3]*x + m[7]*y + m[11]*z + m[15]*w,

            )).out()

        # ----------------------------------------------------------------------------------------------------
        # A Matrix rotating an axis to a target vector
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Align Axis to Vector", is_group=True, prefix=mat_) as tree:

            axis = Integer(0, "Axis", 0, 3)
            V    = Vector4.Input()

            x, y, z, w = V._normalize().xyzw
            mx, my, mz, mw = -x, -y, -z, -w

            M0 = Matrix((
                x,  y,  z,  w,
                y, mx,  w, mz,
                z, mw, mx,  y,
                w,  z, my, mx,
            ))._lc("Axis 0")
            M1 = Matrix((
                w,  z, my, mx,
                x,  y,  z,  w,
                y, mx,  w, mz,
                z, mw, mx,  y,
            ))._lc("Axis 1")
            M2 = Matrix((
                z, mw, mx,  y,
                w,  z, my, mx,
                x,  y,  z,  w,
                y, mx,  w, mz,
            ))._lc("Axis 2")
            M3 = Matrix((
                y, mx,  w, mz,
                z, mw, mx,  y,
                w,  z, my, mx,
                x,  y,  z,  w,
            ))._lc("Axis 3")

            Matrix.IndexSwitch(M0, M1, M2, M3, index=axis).out("Matrix")

        # ----------------------------------------------------------------------------------------------------
        # Perpendicular Planes
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Perp Planes", is_group=True, prefix=mat_) as tree:
            """ Compute a Matrix from two vectors.

            This Group returns a normalized Matrix with:
            - Col 0 : normalized V0
            - Col 1 : normalized V1 plus perpendicular to V0
            - Col 2 : first perp vector
            - Col 3 : second perp vector
            """

            # The couple of base vectors
            V0 = Vector4.Input((1, 0, 0), 0, hide_value=True)
            V1 = Vector4.Input((0, 1, 0), 0, hide_value=True)

            # As second plane
            second = Boolean(False, "Second Plane", tip="The two vectors are placed in columns 2 & 3.")

            with Layout("Make sure the two vectors are perpendicular and normalized"):
                V0 = V0.normalize()
                V1 = (V1 - V0.scale(V0.dot(V1))).normalize()

            for i in range(4):
                with Layout(f"Project {'XYZW'[i]}"):
                    axis = [0]*4
                    axis[i] = 1
                    Axis = Vector4(tuple(axis))
                    Proj = Axis.project_on_plane(V0, V1, normalize=False)
                    P = Axis - Proj
                    lg = P.length()

                    if i == 0:
                        Perp = P
                        length = lg
                    else:
                        replace = lg.greater_than(length)
                        length = length.switch(replace, lg)
                        Perp = Perp.switch(replace, P)

            Perp = Perp.scale(1/length)

            M = Matrix4.FromVectors(V0, V1, Perp, Vector4.Cross(V0, V1, Perp))

            M.out("Matrix")

        # Add the method : perp_planes
        tree.add_method(Matrix4, ret_class = Matrix4)

        # ----------------------------------------------------------------------------------------------------
        # Roll vectors
        # ----------------------------------------------------------------------------------------------------

        with GeoNodes("Roll Columns", is_group=True, prefix=mat_) as tree:
            matrix = Matrix4(None, "Matrix")
            index  = Integer(0, "Count")

            m = matrix.as_tuple

            m0 = m
            m1 = m[4:] + m[:4]
            m2 = m[8:] + m[:8] 
            m3 = m[12:] + m[:12]

            with Matrix.IndexSwitch(index=index % 4) as M:
                Matrix(m0).out()
                Matrix(m1).out()
                Matrix(m2).out()
                Matrix(m3).out()

            M.out()

        tree.add_method(Matrix4, self_attr="self", ret_class=Matrix4)

# ====================================================================================================
# Geometry 4
# ====================================================================================================

class G4Interface:
    
    @classmethod
    def Plunge(cls, geo=None, w=0):
        if geo is None:
            return cls(Geometry()).plunge(w=w)
        else:
            return cls(geo).plunge(w=w)
    
    @classmethod
    def Plunged(cls, name="Geometry"):
        return cls.Plunge(Geometry(None, name=name))
    
class Geometry4(Geometry, G4Interface):
    pass

class Mesh4(Mesh, G4Interface):
    pass

class Curve4(Curve, G4Interface):
    pass

class Cloud4(Cloud, G4Interface):
    pass

# ====================================================================================================
# Build nodes
# ====================================================================================================

def build_geometry_nodes():

    # ====================================================================================================
    # MODIFIER - Plunge a Geometry into 4D
    # ====================================================================================================

    with GeoNodes("Plunge", prefix=main_) as tree:
        """ Plunge an object into 4D Space.

        Do nothing if already plunged
        """

        with Layout("By Geometry type"):
            geo = Geometry()
            w = Float(0, "w")
            comps = geo.separate_components()

        # ---------------------------------------------------------------------------
        # Cloud
        # ---------------------------------------------------------------------------
            
        with Layout("Cloud - Nothing"):
            
            cloud = comps.point_cloud

            # Exists if at least one point already plunged
            exists = cloud.points.sample_index(Float("P4 w").exists, 0)

            # Position
            cloud.points.P4_v = nd.position
            cloud.points.P4_w = w

        # ---------------------------------------------------------------------------
        # Mesh
        # Matrix (U, V, Normal 1, Normal 2) stored on faces
        # ---------------------------------------------------------------------------

        with Layout("Mesh"):   
            
            mesh = comps.mesh

            # Exists if at least one point already plunged
            exists = exists | mesh.points.sample_index(Float("P4 w").exists, 0)

            # Position
            mesh.points.P4_v = nd.position
            mesh.points.P4_w = w

            # U, V and 2 normals
            x, y, z = nd.normal.xyz

            u = Vector((y + z, -x, -x)).normalize()
            v = nd.normal.cross(u)

            U = Vector4(u, 0)
            V = Vector4(v, 0)
            N1 = Vector4(nd.normal, 0)
            N2 = Vector4.Cross(U, V, N1)

            # Local space matrix
            mesh.faces.UVNN = Matrix4.FromVectors(U, V, N1, N2)

        # ---------------------------------------------------------------------------
        # Curve
        # Matrix (Tangent, 3 normals) stored on points
        # ---------------------------------------------------------------------------
            
        with Layout("Curve"):
            
            curve = comps.curve

            # Exists if at least one point already plunged
            exists = exists | curve.points.sample_index(Float("P4 w").exists, 0)

            # Position
            curve.points.P4_v = nd.position
            curve.points.P4_w = w

            # Tangent and 3 normals
            T  = Vector4(nd.curve_tangent, 0)
            N1 = Vector4(nd.normal, 0)
            N2 = Vector4(nd.curve_tangent.cross(nd.normal), 0)
            N3 = Vector4((0, 0, 0, 1))

            curve.points.TNNN = Matrix4.FromVectors(T, N1, N2, N3)

        # ---------------------------------------------------------------------------
        # Join
        # ---------------------------------------------------------------------------

        with Layout("Join & switch"):
            new_geo = Geometry(Geometry.Join(cloud, mesh, curve))
            new_geo = new_geo.switch(exists, geo)

        new_geo.out("Geometry")

    tree.add_method(Geometry4,  self_attr="self", ret_class=Geometry4)
    tree.add_method(Mesh4,      self_attr="self", ret_class=Mesh4)
    tree.add_method(Curve4,     self_attr="self", ret_class=Curve4)
    tree.add_method(Cloud4,     self_attr="self", ret_class=Cloud4)

    # ====================================================================================================
    # MODIFIER - Show Normals
    # ====================================================================================================

    with GeoNodes("Normals", prefix=geo_) as tree:

        # Projected geometry
        geo = Geometry(tip="Projected Geometry")

        show_proj_normal = Boolean(False, "Show Projected Normal", tip="Projected Normal")
        show_uv          = Boolean(False, "Show UV", tip="Faces UV")
        show_uv_normals  = Boolean(False, "Show UV Normals", tip="Faces Normals")
        show_N1          = Boolean(False, "Show N1", tip="First Normal in Mesh UVNN or Curve TNNN")
        show_N2          = Boolean(False, "Show N2", tip="Second Normal in Mesh UVNN or Curve TNNN")
        show_N3          = Boolean(False, "Show N3", tip="Third Normal in Mesh TNNN")
        show_N4          = Boolean(False, "Show N4", tip="Normal in Mesh points")
        scale            = Float(1., "Scale")

        with Layout("Separate"):
            comps  = geo.separate_components()
            mesh   = comps.mesh
            curve  = comps.curve

        with Layout("Faces"):

            U, V, N1, N2 = Matrix4("UVNN").get_vectors()

            m_lines  = Mesh.Switch(show_proj_normal, None, draw_vector(mesh.faces, Vector("Projected Normal"), scale=scale))
            m_lines += Mesh.Switch(show_uv, None, draw_normals(mesh.faces, U.v, V.v, scale=scale))
            m_lines += Mesh.Switch(show_uv_normals, None, draw_normals(mesh.faces, N1.v, N2.v, scale=scale))
            m_lines += Mesh.Switch(show_N1, None, draw_vector(mesh.faces, N1.v,scale=scale))
            m_lines += Mesh.Switch(show_N2, None, draw_vector(mesh.faces, N2.v,scale=scale))

            m_lines += Mesh.Switch(show_N4, None, draw_vector(mesh.points, Vector("N4 v"), scale=scale))

        with Layout("Curve"):

            T, N1, N2, N3 = Matrix4("TNNN").get_vectors()

            c_lines  = Curve.Switch(show_N1, None, draw_vector(curve.points, N1.v,scale=scale))
            c_lines += Curve.Switch(show_N2, None, draw_vector(curve.points, N2.v,scale=scale))
            c_lines += Curve.Switch(show_N3, None, draw_vector(curve.points, N3.v,scale=scale))

        (m_lines + c_lines).out("Normals")
        m_lines.out("Faces")
        c_lines.out("Curves")

    tree.add_method(Geometry4, self_attr="self", ret_class=Mesh)


    # ====================================================================================================
    # GROUP - Compute faces UV Indices
    # ====================================================================================================

    with GeoNodes("Compute UV Indices", is_group=True, prefix=op_) as tree:
        
        mesh = Mesh4.Plunge()
        keep = Mesh(mesh)
        
        with Layout("4 Vertex indices for a Face Corner"):
            corner = nd.corners_of_face()
            edge0 = nd.edges_of_corner(corner)
            edge1 = edge0.previous_edge_index
            
            v1 = nd.edge_vertices().vertex_index_1
            v2 = v1.vertex_index_2
            
        with Layout("Read the 4 indices"):
            A = mesh.edges.sample_index(v1, index=edge0)._lc("A")
            B = mesh.edges.sample_index(v2, index=edge0)._lc("B")
            C = mesh.edges.sample_index(v1, index=edge1)._lc("C")
            D = mesh.edges.sample_index(v2, index=edge1)._lc("D")
            
        with Layout("Exactly two of them are identical"):
            # A = C : index 0
            AD = A.equal(D)._lc("A = D") # index = 1
            BC = B.equal(C)._lc("B = C") # index = 2
            BD = B.equal(D)._lc("B = D") # index = 3
            
        with Layout("Compute an index 0 to 3"):
            index = Integer.Switch(AD, 0, 1)
            index = index.switch(BC, 2)
            index = index.switch(BD, 3)
            
        with Layout("The 3 vertex indices in each case"):
            # ---------------------  A=C A=D B=C B=D
            Oi = Integer.IndexSwitch( A,  A,  B,  B, index=index)._lc("Origin")
            Ui = Integer.IndexSwitch( B,  B,  A,  A, index=index)._lc("U Index")
            Vi = Integer.IndexSwitch( D,  C,  D,  C, index=index)._lc("V Index")

        with Layout("Order to match the normal"):
            pO = mesh.faces.capture_attribute(mesh.points.sample_index(nd.position, index=Oi))
            pU = mesh.faces.capture_attribute(mesh.points.sample_index(nd.position, index=Ui))
            pV = mesh.faces.capture_attribute(mesh.points.sample_index(nd.position, index=Vi))

            U = pU - pO
            V = pU - pO
            N = U.cross(V)
            inv = nd.normal.true_normal.dot(N).less_than(0)

            Ui_ = Ui.switch(inv, Vi)
            Vi_ = Vi.switch(inv, Ui)

        with Layout("Store the 3 different indices"):
            mesh.faces.Oi = Oi
            mesh.faces.Ui = Ui_
            mesh.faces.Vi = Vi_

        with Layout("No change if already done"):
            exists = keep.faces.sample_index(Integer("Oi").exists, index=0)
            mesh = mesh.switch(exists, keep)
            
        mesh.out()

    tree.add_method(Mesh4, self_attr="self", ret_class=Mesh4)

    # ====================================================================================================
    # GROUP - Compute faces UV 4-Vectors
    # ====================================================================================================

    with GeoNodes("Compute UV Vectors", is_group=True, prefix=op_) as tree:
        
        mesh = Mesh4.Plunge().compute_uv_indices()

        P = Vector4.Position()

        with Layout("O Position"):
            index = Integer("Oi")
            PO = Vector4(
                mesh.points.sample_index(P.v, index=index),
                mesh.points.sample_index(P.w, index=index),
                )

        with Layout("U Position"):
            index = Integer("Ui")
            PU = Vector4(
                mesh.points.sample_index(P.v, index=index),
                mesh.points.sample_index(P.w, index=index),
                )

        with Layout("V Position"):
            index = Integer("Vi")
            PV = Vector4(
                mesh.points.sample_index(P.v, index=index),
                mesh.points.sample_index(P.w, index=index),
                )
            
        with Layout("Vectors U, V"):
            U = PU - PO
            V = PV - PO

        #with Layout("Capture values on faces"):
        #    node = mesh.faces.capture_attribute(uv=U.v, uw=U.w, vv=V.v, vw=V.w)
        #    U = Vector4(node.uv, node.uw)
        #    V = Vector4(node.vv, node.vw)

        mesh.out()
        U.out(name="U")
        V.out(name="V")


    tree.add_method(Mesh4, self_attr="self", ret_class=Mesh4)

    # ====================================================================================================
    # GROUP - To Cloud
    # ====================================================================================================

    """
    with GeoNodes("To Cloud", is_group=True, prefix=geo_) as tree:

        with Layout("By Geometry type"):
            geo = Geometry()
            w = Float(0, "w")
            comps = geo.separate_components()

        cloud = comps.point_cloud
        cloud.points.Geo4 = 0

        mesh_cloud = comps.mesh.to_points()
        mesh_cloud.points.Geo4 = 1
        
        curve_cloud = comps.curve.to_mesh().to_points()
        curve_cloud.points.Geo4 = 2

        Geometry.Join(cloud, mesh_cloud, curve_cloud).out("Cloud")

    tree.add_method(Geometry4, self_attr="self", ret_class=Cloud)
    """

    # ====================================================================================================
    # MODIFIER - Compute Visible Faces from a point (typically a source of light)
    # ====================================================================================================

    with GeoNodes("Compute Visible Faces", is_group=True, prefix=op_) as tree:
        
        mesh = Mesh4.Plunge()
        O = Vector4.Input()
        tolerance = Float(0.1, "Tolerance", 0, 0.5)

        keep = Mesh(mesh)

        with Layout("Projection 1"):
            Proj = Matrix4.projection_matrix()
            P0 = Proj @ Vector4.Position()
            O0 = Proj @ O

            mesh.position = P0.v

        with Layout("Additional rotation"):
            Rot = Matrix4.rotation_matrix(w_euler=(1, 1, 1), _3d_euler=(1, 1, 1))
            P1 = Rot @ P0
            O1 = Rot @ O0

        for rep in repeat(2, mesh=mesh, o=O0.v):

            mesh = rep.mesh
                
            with Layout("Direction and distance"):

                ray = nd.position - rep.o
                dist = ray.length()

            node = mesh.raycast(
                #attribute: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                #interpolation: Literal['Interpolated', 'Nearest'] = None,
                source_position = O.v,
                ray_direction   = ray.normalize(),
                ray_length      = 1.1*dist,
            ).node

            d = mesh.faces.capture_attribute(nd.position).distance(mesh.faces.capture_attribute(node.hit_position))
            vis = node.is_hit & d.less_than(tolerance)

            vis = Boolean.Switch(rep.iteration.equal(0), Boolean("Visible") | vis, vis)
            mesh.faces.Visible = vis

            mesh.position = P1.v

            rep.mesh = mesh
            rep.o = O1.v

        keep.faces.Visible = rep.mesh.faces.sample_index(Boolean("Visible"), index=nd.index)

        keep.out()
        #rep.mesh.out("Debug")

    tree.add_method(Mesh, self_attr="self", ret_class=Mesh)

    # ====================================================================================================
    # MODIFIER - Light
    # ====================================================================================================

    with GeoNodes("Light", prefix=main_):

        P4 = Vector4.Input()
        intensity = Float(1, "Intensity", 0)
        col = Color(1, "Color")

        sph = Mesh.UVSphere(radius=.1)
        sph.faces.P4_v = P4.v
        sph.faces.P4_w = P4.w
        sph.faces.Intensity = intensity
        sph.faces.Color = col
        sph.faces.material = "4 Light"

        # Projection Matrix
        Proj = Matrix4.projection_matrix()

        P = Matrix4(Proj) @ P4
        sph.transform(translation=P.v)

        sph.out("Mesh")

    # ====================================================================================================
    # MODIFIER - Light on surface
    # ====================================================================================================

    with GeoNodes("Normal Plane Reflection", prefix=mesh_) as tree:

        mesh = Mesh4.Plunged()
        coll = Collection("4D Lights", "Lights")
        tolerance = Float(0.1, "Tolerance", 0, 0.5)

        with Layout("Projection Matrix"):
            Proj = Matrix4.projection_matrix()

            # Observation direction
            Obs = Vector4(Proj.xyz)

        with Layout("Face Position & Perpendicular Plane"):

            UVNN = Matrix4("UVNN")
            N1 = UVNN.get_vector4(2)
            N2 = UVNN.get_vector4(3)
            P4 = Vector4.Position()

            mesh.faces.Use_Emission = True
            mesh.faces.Emission     = 0.0
            mesh.faces.Light_Color  = Vector()

        with Layout("Lights"):
            lights  = coll.info(separate_children=True).instances
            nlights = lights.insts.count

        with Layout("Loop on light sources"):

            for rep in repeat(nlights, mesh=mesh, rays=None):

                with Layout("Light info"):

                    light = Mesh(lights[nd.index.equal(rep.iteration)].realize())

                    S4_v  = light.faces.sample_index(Vector("P4 v"), index=0)
                    S4_w  = light.faces.sample_index(Float("P4 w"), index=0)
                    S_int = light.faces.sample_index(Float("Intensity"), index=0)
                    S_col = light.faces.sample_index(Color.Named("Color"), index=0)

                with Layout("Visible faces from this source"):
                    mesh = mesh.compute_visible_faces(xyz=S4_v, w=S4_w, tolerance=tolerance)

                with Layout("Incident Direction"):
                    ray = (P4 - Vector4(S4_v, S4_w))
                    Dir = ray.normalize()

                with Layout("Projection on the perpendicular plane"):
                    P1 = N1.scale(N1.dot(Dir))
                    P2 = N2.scale(N2.dot(Dir))

                    In_plane = P1 + P2
                    Out_plane = Dir - In_plane

                with Layout("Outcoming direction"):
                    Out_dir = Out_plane - In_plane
                    d = Out_dir.dot(Obs)

                with Layout("Color & intensity contribution"):

                    intensity = d.map_range(from_min=0, from_max=-1)*S_int

                    intensity = intensity.switch_false(Boolean("Visible"), 0.0)

                    mesh.faces.Emission = Float("Emission") + intensity
                    mesh.faces.Light_Color = Vector("Light_Color") + Vector(S_col).scale(intensity)

                with Layout("Ray visualization"):

                    count = mesh.faces.count
                    light_pos = (Proj @ Vector4(S4_v, S4_w)).v
                    lines = Cloud.Points(count, position=light_pos).to_vertices()

                    Face_pos = Vector4(
                        mesh.faces.sample_index(P4.v, index=nd.index), 
                        mesh.faces.sample_index(P4.w, index=nd.index))
                    face_pos = (Proj @ Face_pos).v
                    out_dir = mesh.faces.sample_index((Proj @ Out_dir).v, index=nd.index).normalize()

                    lines.points.Out_Dir = out_dir

                    lines = lines.points.extrude(offset=face_pos - light_pos)
                    lines.points[lines.top].extrude(offset=Vector("Out Dir"), offset_scale=3)

                    rep.rays = rep.rays + lines

                rep.mesh = mesh

        mesh = rep.mesh

        mesh.faces.Light_Color = Vector("Light Color") / Float("Intensity")

        mesh.out()
        rep.rays.out("Rays")

    tree.add_method(Mesh4, self_attr="self", ret_class=Mesh4)

    # ====================================================================================================
    # MODIFIER - Translation
    # ====================================================================================================

    with GeoNodes("Translation", prefix=geo_) as tree:

        geo = Geometry4.Plunged()
        T = Vector4.Input()

        P4 = Vector4.Position()
        P4 = P4 + T
        P4.store_position(geo)

        geo.out("Geometry")

    tree.add_method(Geometry4, self_attr = "self", ret_class=Geometry4)

    # ====================================================================================================
    # MODIFIER - Scale
    # ====================================================================================================

    with GeoNodes("Scale", prefix=geo_) as tree:

        geo = Geometry4.Plunged()

        scale = Float(1.0, "Scale")
        pivot = Vector4.Input(name="Pivot")

        P4 = Vector4.Position()
        P4 = P4 - pivot

        P4 = P4.scale(scale)

        P4 = P4 + pivot
        P4.store_position(geo)

        geo.out("Geometry")

    tree.add_method(Geometry4, self_attr = "self", ret_class=Geometry4)

    # ====================================================================================================
    # MODIFIER - Matrix Rotation
    # ====================================================================================================

    with GeoNodes("Matrix Rotation", is_group = True, prefix=op_) as tree:

        geo = Geometry4.Plunged()
        R = Matrix(None, "Rotation")
        pivot = Vector4.Input(name="Pivot")

        with Layout("Position"):

            P4 = Vector4.Position()
            P4 = P4 - pivot

            #P4 = P4.matmul(R)
            P4 = Matrix4(R) @ P4

            P4 = P4 + pivot
            P4.store_position(geo)

        comps = geo.separate_components()

        cloud = comps.point_cloud
        mesh = comps.mesh
        curve = comps.curve

        with Layout("Face Matrices"):
            # UV matrix
            mesh.faces.UVNN = R @ Matrix("UVNN")

            # Normal
            N4 = Vector4("N4")
            exists = N4.v.exists
            N4 = Matrix4(R) @ N4
            mesh.faces[exists].N4_v = N4.v
            mesh.faces[exists].N4_w = N4.w

        with Layout("Curve Matrices"):
            curve.points.TNNN = R @ Matrix("TNNN")

        Geometry.Join(cloud, mesh, curve).out("Geometry")

    tree.add_method(Geometry4, self_attr = "self", ret_class=Geometry4)

    # ====================================================================================================
    # MODIFIER - Rotation
    # ====================================================================================================

    with GeoNodes("Rotation", prefix=geo_) as tree:

        geo = Geometry4.Plunged()

        R = Matrix4.rotation_matrix().link_inputs()

        geo = geo.matrix_rotation(rotation=R).link_inputs()

        geo.out()


    tree.add_method(Geometry4, self_attr = "self", ret_class=Geometry4)    

    # ====================================================================================================
    # MODIFIER - 4D Parameters
    # ====================================================================================================

    with GeoNodes("Parameters", prefix=main_):
        """ Set an object as the global host for shared 4D parameters

        The modifier requires 6 angles to defined the projection Matrix.
        The projection can be cancelled with 'No Transformation' switch.

        The user can optionnally display the 4 axis.
        """
        
        nope = Boolean(False, "No Transformation")
        
        # ---------------------------------------------------------------------------
        # Projection Matrix
        # ---------------------------------------------------------------------------
        
        with Layout("Store the projection matrix in a 1-Point Cloud"):

            P = Matrix4.rotation_matrix().link_inputs(None, "Angles")
            
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

                P0 = Matrix4(M).get_vector4(0)
                P1 = Matrix4(M).get_vector4(1)
                
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

    # ====================================================================================================
    # MODIFIER - Projection
    # ====================================================================================================
        
    with GeoNodes("Projection", prefix=main_) as tree:
        """ Projection a 4D geometry into 3D
        """
        geo = Geometry4.Plunged()

        use_mat = Boolean(False, "Set Material")
        mat     = Material("4 Face", "Material")

        with Panel("Options"):
            smooth       = Boolean(True,  "Smooth")
            use_emission = Boolean(True,  "Emission")
            use_normal   = Boolean(True,  "Projected Normal")
            vol_normal   = Boolean(False, "Volume Normal")
            use_interior = Boolean(True,  "Interior")
            color        = Color((.6, .6, .8), "Color")
            back_color   = Color((.1, .1, .2), "Interior Color")
            roughness    = Float.Factor(.5, "Roughness", 0, 1)

        with Layout("Projection"):

            # Projection Matrix
            Proj = Matrix4.projection_matrix()

            # Observation direction
            Obs = Vector4(Proj.xyz)

            # Rotation
            geo = Geometry4(geo).matrix_rotation(Proj)

        with Layout("Separate"):
            comps = geo.separate_components()
            mesh  = comps.mesh
            curve = comps.curve
            cloud  = comps.point_cloud

        with Layout("Faces options"):
            mesh.faces.Use_Emission  = use_emission
            mesh.faces.Use_Normal    = use_normal
            mesh.faces.Color         = color
            mesh.faces.Back_Color    = back_color

        with Layout("Faces Normals"):

            # UVNN Normal
            N1 = Matrix4("UVNN").get_vector4(2)

            # Volume Normal
            N4 = Vector4("N4")

            Normal = N1.switch(vol_normal, N4)
            mesh.faces.Projected_Normal = Normal.v

        with Layout("Orientation"):
            interior = Obs.dot(N1).map_range(from_min=-0.05, from_max=0.05)
            mesh.faces.Roughness = interior.map_range(to_min=roughness, to_max=roughness + 0.3)
            mesh.faces.Interior = interior.switch_false(use_interior)

        with Layout("Material & Smoothness"):
            mesh = mesh.switch(use_mat, mesh.set_material(mat))
            mesh = Mesh(mesh)
            mesh.faces.smooth = smooth

        with Layout("Add Normals"):
            lines = geo.normals().link_inputs(None, "Normals").normals

        geo = Geometry.Join(cloud, curve, mesh, lines)
        geo.out("Geometry")

    tree.add_method(Geometry4, "projection", "", ret_class=Geometry)

    # ====================================================================================================
    # MODIFIER - Mesh Merge Points
    # ====================================================================================================

    with GeoNodes("Merge Points", prefix=mesh_) as tree:

        geo = Mesh4.Plunge()
        comps = geo.separate_components()
        cloud, mesh, curve = comps.point_cloud, comps.mesh, comps.curve

        with Layout("Merge Mesh points"):
            sel = Boolean(False, "Selection", hide_value=True)

            P4 = Vector4.Position()

            stats = mesh.points.attribute_statistic(P4.v)
            vmax = stats.node.max + (1, 1, 1)

            stats = mesh.points.attribute_statistic(P4.w)
            wmin = stats.node.min

            mesh.offset = vmax + P4.w - wmin

            mesh = mesh[sel].merge_by_distance()

            mesh.position = P4.v

        Geometry.Join(cloud, mesh, curve).out("Mesh")

    tree.add_method(Mesh4, self_attr = "self", ret_class=Mesh4)

    # ====================================================================================================
    # PRIMITIVE - Curve Line
    # ====================================================================================================

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

        # Since the 3D Curve could be a single point, we can't rely on P.v for the trim

        line = Curve.Line(0, (1, 1, 1))
        line.points.P4_v = nd.position.map_range(to_min=V0.v, to_max=V1.v)
        line.points.P4_w = nd.position.x.map_range(to_min=V0.w, to_max=V1.w)
        line = line.trim(trim0, trim1).resample(mode='Count', count=resol)
        line.position = Vector("P4 v")

        T = (V1 - V0).normalize()
        line.points.TNNN = Matrix4.AlignAxisToVector(axis=0, V4=T)
        
        finalize(line).out("Curve'")

    tree.add_method(Curve4, ret_class=Curve4)

    # ====================================================================================================
    # PRIMITIVE - Curve Circle
    # ====================================================================================================

    with GeoNodes("Circle", prefix=curve_) as tree:

        radius  = Float(1, "Radius", 0.)
        resol   = Integer(32, "Count", 3)

        with Panel("Trim"):
            trim0 = Float.Factor(0, "Start", 0, 1)
            trim1 = gnmath.max(trim0, Float.Factor(1, "End", 0, 1))

        factor     = Float.Factor(1, "Close", 0, 1)
        move_curve = Boolean(False, "Move Curve", tip="The curve moves to the origin when open")
        z_rot      = Float.Angle(0, "Rotation")

        close = factor.equal(1) & (trim0.equal(0) & trim1.equal(1))

        with Layout("Closed Circle"):
            circle = Curve.Circle(resolution=resol, radius=radius)
            circle.transform(rotation = Rotation((0, 0, z_rot)))
            circle = Geometry4.Plunge(circle)

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
            line.transform(rotation=Rotation((0, 0, z_rot)))

        with Layout("Plunge into 4D"):

            if True:
                line = Geometry4.Plunge(line)

            else:
                m = [0]*16
                m[:3] = nd.position.xyz
                m[4:8]  = gnmath.cos(ag + z_rot), gnmath.sin(ag + z_rot), 0, 0
                m[8:12] = 0, 0, 1, 0
                m[12:]  = 0, 0, 0, 1

                line = Curve(line)
                line.points.M4D = Matrix(m)

        with Layout("Closed"):
            line = line.switch(close & factor.equal(1), circle)

        finalize(line, False).out("Curve")

    tree.add_method(Curve4, ret_class=Curve4)

    # ====================================================================================================
    # PRIMITIVE - Mesh Plane
    # ====================================================================================================

    with GeoNodes("Plane", prefix=mesh_) as tree:
        """ Create a 4-Plane

        The plane is a XY plane or is defined by two vectors.

        In addition, the plane can be rotated.

        The user can optionnally create a plane perpendicular to the two vectors.
        """
        
        with Layout("Base Grid"):
            use_vectors = Boolean(True, "Use Vectors")
            use_perp    = Boolean(False, "Perp. Plane")

            grid = Mesh.Grid().link_inputs(None, "Grid")
            grid.corners.UV_Map = grid.uv_map
            use_tris = Boolean(False, "Triangles")

            with Layout("Face UV Indices"):
                nx = Integer.Input("Vertices X")
                ny = Integer.Input("vertices Y")

                with Layout("Rectangle Faces"):
                    # Faces along y : faces count = ny - 1
                    # y ----->
                    # point : 0 --- 1 --- 2 --- 3 --- 4  : 5 points
                    # face  :    0     1     2     3     : 4 faces = ny - 1
                    #
                    # faces_per_col = ny - 1
                    # - face_index // faces_per_col : point row index
                    # - face_index % faces_per_col  : point col index

                    rOi = ( ny*(nd.index // (ny - 1)) ) + ( nd.index%(ny - 1) )
                    rUi = rOi + ny
                    rVi = rOi + 1

                with Layout("Triangle Faces"):
                    # Faces along y : faces count = (ny - 1) * 2
                    # y ----->
                    # point : 0 --- 1 --- 2 --- 3 --- 4  : 5 points
                    # face  :   0,1   2,3   4,5   6,7    : 8 faces = 2(ny - 1)
                    #
                    # faces_per_col = 2*(ny - 1)
                    # - face_index // faces_per_col : point row index
                    # - face_index % faces_per_col  : twice point col index

                    faces_per_col = 2*(ny - 1)
                    i = nd.index // faces_per_col
                    j = (nd.index % faces_per_col) // 2

                    if True:
                        is_odd = (nd.index % 2).equal(1)

                        O0 = i*ny + j
                        O1 = i*ny + j + ny + 1

                        tOi = Integer.Switch(is_odd, O0,      O1)
                        tUi = Integer.Switch(is_odd, O0 + ny, O1 - ny)
                        tVi = Integer.Switch(is_odd, O0 +  1, O1 -  1)
                    else:
                        even_Oi = ( ny*(nd.index // faces_y) ) + ( nd.index % faces_y ) // 2
                        even_Ui = even_Oi + 1
                        even_Vi = even_Oi + ny

                        odd_Oi = ( ny*(nd.index // nfaces) ) + ( nd.index % nfaces ) // 2 + ny + 1
                        odd_Ui = odd_Oi - ny
                        odd_Vi = odd_Oi - 1

                        is_odd = (nd.index % 2).equal(1)
                        tOi = even_Oi.switch(is_odd, odd_Oi)
                        tUi = even_Ui.switch(is_odd, odd_Ui)
                        tVi = even_Vi.switch(is_odd, odd_Vi)

                grid = Mesh(grid.switch(use_tris, Mesh(grid).triangulate()))

                grid.faces.Oi = rOi.switch(use_tris, tOi)
                grid.faces.Ui = rUi.switch(use_tris, tUi)
                grid.faces.Vi = rVi.switch(use_tris, tVi)

            # Plunge
            grid4 = Geometry4.Plunge(grid)

        with Layout("Defined by Rotation"):

            with Matrix.Switch(use_vectors) as R:
                Matrix4.rotation_matrix().link_inputs(None, "Rotation").out("False")

        with R:
            with Panel("Vectors"):
                V1 = Vector4.Input((1, 0, 0), shape="Single")
                V2 = Vector4.Input((0, 1, 0), shape="Single")

            M = Matrix4.perp_planes(**V1.args(), **V2.args(rank=1))
                
            with Layout("Perpendicular Plane"):
                m = M.as_tuple
                m2 = [0]*16
                m2[:8] = m[8:]
                m2[8:] = m[:8]
                
                M = M.switch(use_perp, Matrix(m2))

            M.out("True")

        # Rotation
        grid4 = grid4.matrix_rotation(R)

        finalize(grid4, Material("4 Face", "Material")).out("Mesh")

    tree.add_method(Mesh4, ret_class=Mesh4)

    # ====================================================================================================
    # MODIFIER - Curve to Surface
    # ====================================================================================================

    with GeoNodes("To Surface", prefix=curve_) as tree:

        bbone = Curve(Geometry4.Plunge(Curve()))

        with Panel("Profile"):
            use_object  = Boolean(False, "Object")
            profile     = Curve(None, "Curve", tip="Curve in XY plane")
            obj         = Object(None, "Curve Object", tip="Curve in XY plane")

        with Layout("Profile Curve"):
            profile = Curve(Geometry4.Plunge(profile.switch(use_object, obj.info().geometry)))

        with Panel("Transformation"):
            twist_clx = Closure(None, "Twist X", tip="Factor -> Angle")
            twist_cly = Closure(None, "Twist Y", tip="Factor -> Angle")

            use_scale = Boolean(False, "Scale")
            scale_cl  = Closure(None, "Scale",    tip="Factor -> Scale")

        mat    = Material("4 Face", "Material")
        smooth = Boolean(True, "Shade Smooth")

        # ---------------------------------------------------------------------------
        # Backbone
        # ---------------------------------------------------------------------------

        with Layout("Backbone"):
            bb_closed = bbone.splines.sample_index(nd.is_spline_cyclic, index=0)
            bb_count  = bbone.points.count
            nx        = bb_count.switch(bb_closed, bb_count + 1)

        # ---------------------------------------------------------------------------
        # Profile
        # ---------------------------------------------------------------------------

        with Layout("Profile"):
            pf_closed = profile.splines.sample_index(nd.is_spline_cyclic, index=0)
            pf_count  = profile.points.count
            ny        = pf_count.switch(pf_closed, pf_count + 1)

        # ---------------------------------------------------------------------------
        # Grid
        # ---------------------------------------------------------------------------

        with Layout("Grid"):

            shape = (nx, ny)
            ix, iy = unravel_index(nd.index, shape)

            grid = Mesh4.plane(
                vertices_x = nx,
                vertices_y = ny,
                triangles = True,
            )

        with Layout("Backbone position and extrusion local matrix"):
            BB_v = bbone.points.sample_index(  Vector("P4 v"), index=ix % bb_count)
            BB_w = bbone.points.sample_index(  Float( "P4 w"), index=ix % bb_count)

        with Layout("Profile Position and Normal"):

            # Position
            P4_v = profile.points.sample_index(Vector("P4 v"), index=iy % pf_count)
            P4_w = profile.points.sample_index(Float( "P4 w"), index=iy % pf_count)
            P4 = Vector4(P4_v, P4_w)

            # Normal
            TNNN = Matrix4(profile.points.sample_index(Matrix("TNNN"), index=iy % pf_count))
            N4 = TNNN.get_vector4(1)

        """
        with Layout("Twist & scale"):

            sig = ({'Factor': 'Float'}, {'Value': 'Float'})

            fac = ix/(nx - 1)
            twist_x = twist_clx.evaluate(signature=sig, factor=fac)
            twist_y = twist_cly.evaluate(signature=sig, factor=fac)
            scale   = scale_cl.evaluate(signature=sig,  factor=fac)
            scale = scale.switch_false(use_scale, 1)

            R_twist = Rotation((twist_x, twist_y, 0))
            M_twist = Matrix4(Matrix.CombineTransform(rotation=R_twist))

            # Position
            P4 = M_twist @ Vector4(P4_v, P4_w)
            P4 = P4.scale(scale)

            # Normal
            N = M_twist @ Vector4(N_v, N_w)
        """

        with Layout("Profile points on backbone"):

            with Layout("Backbone"):
                BB_Rot = Matrix4(bbone.points.sample_index(Matrix("TNNN"), index=ix % bb_count))

                # TNNN --> NNTN
                BB_Rot = BB_Rot.roll_columns(2)

            with Layout("Rotation translation"):
                P4 = BB_Rot @ P4
                N4 = BB_Rot @ N4

                # Translate to backbone position
                P4 = P4 + Vector4(BB_v, BB_w)._lc("BB Position")

                # Store
                P4.store_position(grid)
                grid.points.N4_v = N4.v
                grid.points.N4_w = N4.w

        # ---------------------------------------------------------------------------
        # Face normals
        # ---------------------------------------------------------------------------

        with Layout("Faces Normals"):
                
            grid = Mesh4(grid).compute_uv_vectors()
            U = Vector4(grid.u_xyz, grid.u_w)
            V = Vector4(grid.v_xyz, grid.v_w)
            
            o_index = Integer("Oi")
            N = Vector4(
                grid.points.sample_index(Vector("N4 v"), index=o_index),
                grid.points.sample_index(Float("N4 w"), index=o_index),
            )
                
            N2 = Vector4.Cross(U, V, N)
            grid.faces.UVNN = Matrix4.FromVectors(U, V, N, N2)

        # ---------------------------------------------------------------------------
        # When closed, the points can be merged
        # ---------------------------------------------------------------------------

        with Layout("Merge to close"):
            sel  = Boolean.Switch(bb_closed, False, ix.equal(0) | ix.equal(nx - 1))
            sel |= Boolean.Switch(pf_closed, False, iy.equal(0) | iy.equal(ny - 1))
            grid = grid.merge_points(sel)

        finalize(grid, Material("4 Face", "Material")).out("Mesh")

    tree.add_method(Curve4, self_attr="self", ret_class=Mesh4)

    # ====================================================================================================
    # PRIMITVE - Mesh Torus
    # ====================================================================================================

    with GeoNodes("Torus", prefix=mesh_) as tree:

        curve0 = Geometry4.Plunge(curve_.circle().link_inputs(None, "Curve 0", exclude=["Projection"]))
        curve1 = Geometry4.Plunge(curve_.circle().link_inputs(None, "Curve 1", exclude=["Projection"]))

        twist_x = Float.Angle(0, "Twist X")
        twist_y = Float.Angle(0, "Twist Y")

        use_scale = Boolean(False, "Scale", hide_in_modifier=True)
        scale = Closure(None, "Scale", hide_in_modifier=True)

        trim0 = Float.Input("Curve 0 > Trim > Start")
        trim1 = Float.Input("Curve 0 > Trim > End")
        with Closure(closure=Input("Twist X")) as twist_clx:
            factor = Float(name="Factor")
            factor.map_range(to_min=trim0*twist_x, to_max=trim1*twist_x).out("Value")

        with Closure(closure=Input("Twist Y")) as twist_cly:
            factor = Float(name="Factor")
            factor.map_range(to_min=trim0*twist_y, to_max=trim1*twist_y).out("Value")

        mesh = Curve4(curve0).to_surface(
            curve_1 = curve1, 
            twist_x = twist_clx, 
            twist_y = twist_cly, 
            scale   = use_scale, 
            scale_1 = scale).link_inputs(None, exclude=["Profile", "Transformation"])

        mesh.out("Mesh")

    tree.add_method(Mesh4, ret_class=Mesh4)

    # ====================================================================================================
    # MODIFIER - Slices along a curve
    # ====================================================================================================

    with GeoNodes("Slices OLD", prefix=curve_) as tree:

        bbone = Curve4.Plunge()

        with Panel("3D Profile"):

            profile     = Mesh4.Plunged(name="Profile")
            use_object  = Boolean(False, "Object")
            obj         = Object(None, "Mesh Object")
            scale       = Float(1., "Scale")
            orient      = Integer(1, "Orientation", 0, 3)

            profile = Mesh4.Plunge(profile.switch(use_object, obj.info().geometry))

        with Layout("Instantiate the profile on the backbone"):

            vol = Mesh(bbone.points.instance_on(instance=profile).realize())

        with Layout("Indices"):

            nprof = Mesh(profile).points.count + Curve(profile).points.count + Cloud(profile).points.count
            ix = nd.index // nprof
            iy = nd.index % nprof

        with Layout("Backbone Position and Orientation"):

            BB_v = bbone.points.sample_index(Vector("P4 v"), index=ix)
            BB_w = bbone.points.sample_index(Float("P4 w"), index=ix)

            TNNN = bbone.points.sample_index(Matrix("TNNN"), index=ix)

            BB_scale = bbone.points.sample_index(bbone.points.capture_attribute(scale), index=ix)

        with Layout("Profile Position"):

            PF_v = profile.points.sample_index(Vector("P4 v"), index=iy)
            PF_w = profile.points.sample_index(Vector("P4 w"), index=iy)

        with Layout("Scale and rotate slices"):

            with Layout("Scale"):
                PF_v = PF_v.scale(BB_scale)
                PF_w = PF_w * BB_scale

            with Layout("Rotate"):
                Rot = Matrix4(TNNN).roll_columns(orient)
                P4 = Rot.rotate_vector(Vector4(PF_v, PF_w))

            with Layout("To backbone position"):
                P4 = P4 + Vector4(BB_v, BB_w)
                P4.store_position(vol)

        finalize(vol).out("Mesh")

    # ====================================================================================================
    # MODIFIER - Slices along a curve
    # ====================================================================================================

    with GeoNodes("Slices", prefix=curve_) as tree:

        bbone = Curve4.Plunge()

        with Panel("3D Profile"):

            profile     = Mesh(name="Profile")
            use_object  = Boolean(False, "Object")
            obj         = Object(None, "Mesh Object")
            use_radius  = Boolean(False, "Use Radius")
            orient      = Integer(1, "Orientation", 0, 3)

            profile = Geometry4.Plunge(profile.switch(use_object, obj.info().geometry))


        for rep in repeat(bbone.points.count, slices=None):

            with Layout("Backbone Position and Orientation"):

                bb_v = bbone.points.sample_index(Vector("P4 v"), index=rep.iteration)
                bb_w = bbone.points.sample_index(Float("P4 w"),  index=rep.iteration)

                TNNN = bbone.points.sample_index(Matrix("TNNN"), index=rep.iteration)
                Rot = Matrix4(TNNN).roll_columns(orient)

                bb_scale = bbone.points.sample_index(nd.radius, index=rep.iteration).switch_false(use_radius, 1.0)

            with Layout("Scale & Rotate"):

                sl = profile.matrix_rotation(Rot)
                sl = sl.scale(bb_scale)

            with Layout("Translate"):
                sl = sl.translation(xyz=bb_v, w=bb_w)

            rep.slices = rep.slices + sl

        slices = rep.slices

        finalize(slices).out("Mesh")        

    tree.add_method(Curve4, self_attr="self", ret_class=Mesh4)    

    # ====================================================================================================
    # PRIMITIVE - Dev
    # ====================================================================================================

    with GeoNodes("Slices Test"):

        curve = Curve4.Plunged()
        profile = Mesh(Geometry4.Plunge(Mesh(None, "Profile")))

        with Layout("Base Slices"):
            base = curve.slices(profile=profile)
            base = base.compute_uv_vectors()

        with Layout("Build a fake skin to compute the faces normals"):
            N = Matrix4("UVNN").get_vector4(2)
            P4 = Vector4("P4") + N.scale(0.1)

            count = profile.faces.count
            cloud = Cloud.Points(count, position=profile.faces.sample_index(P4.v, index=nd.index))
            cloud.points.P4_v = nd.position
            cloud.points.P4_w = profile.faces.sample_index(P4.w, index=nd.index)

            skin = curve.slices(profile=cloud)

        with Layout("Compute the direction of the skin as normal"):
            P4 = Vector4.Position()

            Oi = Integer("Oi")
            O0 = Vector4(base.points.sample_index(P4.v, Oi), base.points.sample_index(P4.w, Oi), )
            O1 = Vector4(skin.points.sample_index(P4.v, Oi), skin.points.sample_index(P4.w, Oi), )
            N = (O1 - O0).normalize()

        with Layout("Compute the local Matrix wih U, V and N"):

            U = Vector4("U")
            V = Vector4("V")

            N2 = Vector4.Cross(U, V, N)
            N1 = Vector4.Cross(U, V, N2)

            d = N1.dot(N)

            Normal = N1.switch(d.less_than(0), -N1)

            base.faces.UVNN = Matrix4.FromVectors(U, V, Normal, N2)

        base.out()
        skin.out("Skin")


    # ====================================================================================================
    # PRIMITIVE - Mesh Hyper Sphere
    # ====================================================================================================

    with GeoNodes("Hyper Sphere", prefix=mesh_) as tree:

        radius = Float(1, "Radius", 0)
        slices = Integer(7, "Slices", 1)

        with Layout("A Sphere as slice"):
            sphere = Mesh.UVSphere(radius=radius).link_inputs(None, "Sphere")
            sphere.corners.UV_Map = sphere.uv_map
            sphere.faces.material = Material("4 Face", "Material")

        with Layout("Backbone along w"):
            line = Curve4.line(xyz=0, w = -radius, xyz_1=0, w_1=radius, count=slices + 2)
            w = 2*nd.index/(slices+1) - 1
            #scale = gnmath.sqrt(gnmath.max(0, 1 - w*w))
            line.radius = gnmath.sqrt(gnmath.max(0, 1 - w*w))

        hsph = line.slices(profile=sphere, use_radius=True, orientation=1)

        # ----- Normals are easy to compute

        N4 = Vector4(Vector("P4 v"), Float("P4 w")).normalize()
        hsph.points.N4_v = N4.v
        hsph.points.N4_w = N4.w

        """
        UVNN = Matrix4("UVNN")
        U, V, _, N2 = UVNN.get_vectors()
        node = hsph.faces.capture_attribute(v = Vector("N4 v"), w=Float("N4 w"))
        N1 = Vector4(node.v, node.w).normalize()
        hsph.faces.UVNN = Matrix4.FromVectors(U, V, N1, Vector4.Cross(U, V, N1))
        """

        finalize(hsph).out("Mesh")

    tree.add_method(Mesh4, ret_class=Mesh4)

    return


# ====================================================================================================
# Class Edges 4
# ====================================================================================================

class Edges4:

    def __init__(self):
        self.verts = np.zeros((0, 4), float)
        self.edges = np.zeros((0, 2), int)

    def create():
        pass








    
    
     
            
# ====================================================================================================
# Position and Normals
# ====================================================================================================

class Position4(Matrix4):

    @property
    def location(self):
        return self.get_vector4(0)
    
    @location.setter
    def location(self, V):
        self.set_vector4(0, V)

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def _translate(self, T):
        with Layout("Position4 Translate", color='MACRO'):
            T = Vector4(T)
            self.position = self.position + T
            return self

    def _rotate(self, R, pivot=None):
        with Layout("Position4 Rotate", color='MACRO'):

            P4 = Position4(self)

            if pivot is not None:
                P = Vector4(P4)
                P4 = P4.translate(-P)

            P4 = Position4(R @ P4)

            if pivot is not None:
                P4 = P4.translate(P)

            return self._jump(P4)
    
    def _scale(self, scale, pivot=None):
        with Layout("Position4 Scale", color='MACRO'):

            pos = self.position

            if pivot is not None:
                P = Vector4(pivot)
                pos = pos - P

            pos = pos.scale(scale)

            if pivot is not None:
                pos = pos + P

            self.position = pos
            return self
    
    # ====================================================================================================
    # Build the nodes
    # ====================================================================================================

    @staticmethod
    def build_nodes():

        # ---------------------------------------------------------------------------
        # Translation Node
        # ---------------------------------------------------------------------------

        with GeoNodes("Translate", is_group=True, prefix=mat_) as tree:

            P4 = Position4.Input()
            T = Vector4.Input()

            P._translate(T).out()

        tree.add_method(Position4, self_attr='M', ret_class=Position4)

        # ---------------------------------------------------------------------------
        # Rotation Node
        # ---------------------------------------------------------------------------

        with GeoNodes("Rotate", is_group=True, prefix=mat_) as tree:

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

        with GeoNodes("Curve Local Matrix", is_group=True, prefix=mat4_) as tree:

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

        tree.add_method(Position4, self_attr='M', ret_class=Matrix)

        # ---------------------------------------------------------------------------
        # Mesh Local space
        # ---------------------------------------------------------------------------

        with GeoNodes("Mesh Local Matrix", is_group=True, prefix=mat4_) as tree:

            P = Position4.Input()
            perp_last = Boolean(True, "Normals Last", tip="Tangent plane in vectors 0, 1 and Normal plane in 2, 3.")

            with Layout("Vectors from Matrix"):
                V1 = P.get_vector(1)
                V2 = P.get_vector(2)
                M = vec_.perp_plane(**V1.args(), **V2.args(rank=1), last_vectors=perp_last)

            M.out()

        tree.add_method(Position4, self_attr='M', ret_class=Matrix)






















    

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
        geo = mod_.translation(geo, **(-P).args())
        
        # Rotation
        M = group_.rotation_matrix().link_inputs(None, "Rotation")
        
        geo = Cloud(geo)
        geo.points.M4D = M @ Matrix("M4D")
        
        # Back to initial position
        geo = mod_.translation(geo, **P.args())
        
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

    def set_4D_parameters_OLD():
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

    # ====================================================================================================
    # Line
    # ====================================================================================================

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
