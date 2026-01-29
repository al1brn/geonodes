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

module : furniture
------------------

Designing a furniture made of planks

updates
-------
- created :   2026/01/10

$ DOC START

``` python
from geonodes.demos import furniture

furniture.demo()
```
"""

import bpy

from .. import ShaderNodes, Shader, snd
from .. import GeoNodes, G, Mesh, Curve, Cloud, Layout, Panel, gnmath, nd, pi, Break
from .. import Float, Boolean, Integer, Vector, Rotation, Object, Input, Material, Color, Group
from .. import repeat

USE_GIZMO = True


# ---------------------------------------------------------------------------
# The Mesh contains the furniture plus additional meshes such as cote lines
# The mesh type is determined by the named attribute "Content"
# ---------------------------------------------------------------------------

IS_COMPONENT = 0x80  # Flag : is a component of the piece of furniture vs a cote line

MASK_TYPE  = 0x0F  # Component type mask 

TYPE_PLANK =  0
TYPE_CLEAT =  1
TYPE_PANEL =  2
TYPE_MESH  = 15

TYPE_COTE = 0

# ---------------------------------------------------------------------------
# Min max dimensions
# ---------------------------------------------------------------------------

MIN_DIM = 0.001 # 1 mm
MAX_DIM = 5.0   # 5 meters

# ---------------------------------------------------------------------------
# UV Attributes
# ---------------------------------------------------------------------------

FACE = 0
LONG_SIDE = 1
CUT_SIDE = 2

# ---------------------------------------------------------------------------
# Constants for cote lines
# ---------------------------------------------------------------------------

FONT_SIZE = 0.1
SECTION   = 0.01

# ---------------------------------------------------------------------------
# Group Prefix
# ---------------------------------------------------------------------------

utils = G("Utils")

# ====================================================================================================
# UTILITIES
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Snap function
# ----------------------------------------------------------------------------------------------------

def snap(v, d=MIN_DIM):
    return gnmath.round(v/d)*d

# ----------------------------------------------------------------------------------------------------
# Components selector
# ----------------------------------------------------------------------------------------------------

def all_components():
    return (Integer("Content") & IS_COMPONENT).not_equal(0)

# ----------------------------------------------------------------------------------------------------
# MACRO : Dimension input
# ----------------------------------------------------------------------------------------------------

def get_dimension(mesh, name, i_axis, same_value, color=None):
    """ Dimension input

    Use a Macro rather than a Group to allow Gizmo. When dimension is required,
    we don't know yet the position.

    Arguments
    ---------
    - mesh (Mesh) : current piece of furniture
    - name (str) : "Width" or "Length"
    - i_axis (integer in (0, 1)) : axis to compute "Between" option
    - same_value (Float) : value vor option "Same"
    - color (SysColor) : the color to use for nodes

    Returns
    -------
    - dict : used to set the values and create Gizmo controls
    """

    with Layout(name):

        # ---------------------------------------------------------------------------
        # Menu as second UI item
        # ---------------------------------------------------------------------------

        sel_index = Integer.MenuSwitch({
            "Same"            : 0,
            "Value"           : 1,
            "Other Width"     : 2,
            "Other Length"    : 3,
            "Other Thickness" : 4,
            "Other Size X"    : 5,
            "Other Size Y"    : 6,
            "Other Size Z"    : 7,
            "Between"         : 8,
            },
            menu=Input(name),
        )
        between = sel_index.between
        use_value = sel_index.value
        use_offset = (use_value | between).bnot()

        # ---------------------------------------------------------------------------
        # Existing Plank
        # ---------------------------------------------------------------------------

        comp_id = Integer(0, "Other")
        comp = mesh.extract(utils.selector(comp_id))
        width, length, thickness = comp.dimensions.xyz
        size_x, size_y, size_z = comp.size.xyz

        # ---------------------------------------------------------------------------
        # Two components
        # ---------------------------------------------------------------------------

        comp_id0 = Integer(1, "From Id", 0)
        use_max0 = Boolean(True, f"From Max")
        offset0 = Float.Distance(0.0, "Offset From")
        
        comp_id1 = Integer(2, "To Id", 0)
        use_min1 = Boolean(True, f"To Min")
        offset1 = Float.Distance(0.0, "Offset To")

        comp0 = mesh.extract(utils.selector(comp_id0))
        comp1 = mesh.extract(utils.selector(comp_id1))

        vec0 = comp0.min.switch(use_max0, comp0.max)
        vec1 = comp1.max.switch(use_min1, comp1.min)

        x0, y0, z0 = vec0.xyz
        x1, y1, z1 = vec1.xyz

        bet_0 = Float.IndexSwitch(x0, y0, z0, index=i_axis)._lc("Between Pos", "Purple") + offset0
        bet_1 = Float.IndexSwitch(x1, y1, z1, index=i_axis) - offset1
        dist = (bet_1 - bet_0)._lc("Between Dim", "Purple")

        negative = dist.less_than(0)
        bet_0.switch(negative, bet_1)
        dist = dist.abs()

        # ---------------------------------------------------------------------------
        # Custom value
        # ---------------------------------------------------------------------------

        custom = Float.Distance(1.0, "Value", MIN_DIM)
        offset = Float.Distance(0.0, "Offset")

        # ---------------------------------------------------------------------------
        # Select the value
        # ---------------------------------------------------------------------------

        value = Float.IndexSwitch(
            same_value,
            custom, 
            width,
            length,
            thickness,
            size_x,
            size_y,
            size_z,
            dist,
            index=sel_index)._lc(name, color)
        
        value.switch(use_offset, (value + offset).max(MIN_DIM))

        return {
            'value'       : value, 
            'user_value'  : sel_index.value, 
            'between'     : between,
            'between_loc' : bet_0,
            'use_value'   : use_value,
            'use_offset'  : use_offset,
            'custom'      : custom,
            'offset'      : offset,
        }

# ====================================================================================================
# Demo modifiers
# ====================================================================================================

def demo():

    # ====================================================================================================
    # Shader
    # ====================================================================================================

    with ShaderNodes("Label"):
        
        ped = Shader.Principled(
            base_color = snd.attribute("Color").color,
            roughness = 0.9,    
        )
        ped.out()

    # ====================================================================================================
    # A cote between two points
    # ====================================================================================================

    with GeoNodes("Add Cote Line", is_group=True, prefix=utils):
        
        show       = Boolean(True,          "Show")
        pos        = Vector.Translation(0,  "Position")
        i_axis     = Integer(0,             "Axis", 0, 2)
        value      = Float.Distance(1.0,    "Value")

        with Panel("Aspect"):
            font_size  = Float(FONT_SIZE,  "Font Size", 0.01)
            section    = Float(SECTION,    "Section", 0)
            invert     = Boolean(False,    "Invert")
        
        offset_a = Float(0, "Cote Offset A", hide_in_modifier=True)
        offset_b = Float(0, "Cote Offset B", hide_in_modifier=True)
        
        with Layout("Positions"):
            line_dir = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis)
            pos.switch(value.less_than(0), pos + line_dir.scale(value))
            d = abs(value)
            use_ext = d.less_than(section*10)
            
        with Layout("Line"):
            h   = section*4
            h2  = section*2
            
            cone = Mesh.Cone(radius_bottom=h2, depth=h)
            
            with Mesh.Switch(use_ext) as line:
                d_int = d - h
                
                line_int = Curve.Line((0, 0, h), (0, 0, d_int))
                line_int = line_int.to_mesh(profile_curve=Curve.Circle(radius=section/2))
                
                line_int += Mesh(cone).transform(translation=(0, 0, d_int))
                line_int += Mesh(cone).transform(translation=(0, 0, h), rotation=(0, pi, 0))
                
                line_int.out("False")
                
            with line:
                line_ext = Curve.Line((0, 0, 0), (0, 0, d))
                line_ext = line_ext.to_mesh(profile_curve=Curve.Circle(radius=section/2))
                
                h_in = 0.75*h
                
                line_ext += Mesh(cone).transform(translation=(0, 0, -h_in))
                line_ext += Mesh(cone).transform(translation=(0, 0, d + h_in), rotation=(0, pi, 0))
                
                line_ext.out("True")

            #dir = Vector.IndexSwitch((d, 0, 0), (0, d, 0), (0, 0, d), index=i_axis)
            line.transform(translation=pos, rotation=Rotation().align_z_to_vector(line_dir))
            
            line = Mesh(line)
            
            line.faces.Color=Color("Black")
            line.faces.material = "Label"
            
        with Layout("Label"):
            s = (d*100).to_string(decimals=1)
            label = Curve(s.to_curves(size=font_size).realize())
            label = label.fill()
            label.transform(rotation=(pi/2, 0, 0))
            
            with Layout("Z Rotation"):
                z_rot = Float.Switch(invert, 0, pi) + Float.Switch(i_axis.equal(0), pi/2)
                label.transform(rotation=(0, 0, z_rot))
                
            vmin = label.points.attribute_statistic(nd.position).min_
            vmax = vmin.max_
            
            lx0, ly0, lz0 = vmin.xyz
            size_x, size_y, size_z = (vmax - vmin).xyz
            
            offset = Vector.IndexSwitch(
                Vector.Switch(use_ext,
                    Vector((-size_x/2 - lx0, 0, section*3)),
                    Vector((d/2 + h + font_size/3 - lx0, 0, -size_z/2))
                    ),
                Vector.Switch(use_ext,
                    Vector((0, -size_y/2 - ly0, section*3)),
                    Vector((0, d/2 + h + font_size/3 - ly0, -size_z/2))
                    ),
                Vector((0,  font_size/3 - ly0, -size_z/2)),
                index=i_axis)
                
            label.transform(translation=pos + line_dir.scale(d/2) + offset)
            
            with Layout("Finalize"):
                label.faces.Color = Color.IndexSwitch(
                    Color((0.05, 0, 0)),
                    Color((0, 0.05, 0)),
                    Color((0, 0, 0.05)),
                    index=i_axis)
                    
                label.faces.material = "Label"
                        
                line += label
                
                line = Mesh(line).faces.set_shade_smooth()
                
        with Layout("User Offset"):
            
            dir_a = Vector.IndexSwitch(
                Vector((0, 1, 0)),
                Vector((0, 0, 1)),
                Vector((1, 0, 0)),
                index = i_axis)
            
            dir_b = Vector.IndexSwitch(
                Vector((0, 0, 1)),
                Vector((1, 0, 0)),
                Vector((0, 1, 0)),
                index = i_axis)
            
            p = pos + line_dir.scale(d/2) + dir_a.scale(offset_a) + dir_b.scale(offset_b)
            gizmo_a = offset_a.linear_gizmo(position=p, direction=dir_a, color_id='PRIMARY')
            gizmo_b = offset_b.linear_gizmo(position=p, direction=dir_b, color_id='SECONDARY')
            
            line.transform(translation=dir_a.scale(offset_a) + dir_b.scale(offset_b))
            
        line = Mesh(line)
        line.points.Content = TYPE_COTE
        line.points.Axis = i_axis
        
        line.switch_false(show).out()

    # ====================================================================================================
    # Stock
    # ====================================================================================================

    with GeoNodes("Base Component"):
        """ Create base component to build the furniture.

        A base component has a material and a fix thickness.
        Width and Length can be changed or not:
        - plank & panel : both can be changed
        - cleat : only length can be changed

        Named Attributes
        ----------------
        - Max Dimensions (Vector) : Max dimensions
        - Dimensions (Vector) : init value of component dimensions, equal to Max Dimensions
        - Content (Integer) : component type and flag
        - Reference (Integer) : Unique identifier used to compute the cut sheet
        - Orientation (Integer) : 0 as default orientation
        """

        # ---------------------------------------------------------------------------
        # Selection
        # ---------------------------------------------------------------------------
        
        comp_type = Integer.MenuSwitch({
            "Plank"    : 0,
            "Cleat"    : 1,
            "Panel"    : 2,
            "Geometry" : 3,
            }, menu = Input("Type")
        )

        # Plank
        with Mesh.IndexSwitch(index=comp_type) as component:

            width  = Float.Distance(.30, "Width",     MIN_DIM)
            thick  = Float.Distance(.02, "Thickness", MIN_DIM)
            length = Float.Distance(2.0, "Max Length", MIN_DIM)

            mesh = Mesh.Cube(size=(width, length, thick))
            mesh.points.Content = IS_COMPONENT | TYPE_PLANK

            mesh.out()

        # Cleat
        with component:
            width  = Float.Distance(.05, "Width",     MIN_DIM)
            thick  = Float.Distance(.05, "Thickness", MIN_DIM)
            length = Float.Distance(2.0, "Max Length", MIN_DIM)


            mesh = Mesh.Cube(size=(width, length, thick))
            mesh.points.Content = IS_COMPONENT | TYPE_CLEAT

            mesh.out()

        # Back Panel
        with component:
            thick   = Float.Distance(.005, "Thickness", MIN_DIM)
            max_dim = Float.Distance(3.0, "Max Dimension", MIN_DIM)

            mesh = Mesh.Cube(size=(max_dim, max_dim, thick))
            mesh.points.Content = IS_COMPONENT | TYPE_PANEL

            mesh.out()

        # Input Geometry
        with component:
            mesh = Mesh()
            mesh.points.Content = IS_COMPONENT | TYPE_MESH
            mesh.out()

        # ---------------------------------------------------------------------------
        # Information
        # ---------------------------------------------------------------------------

        with Layout("Dimensions"):
            component = Mesh(component)
            dims = component.points.attribute_statistic(nd.position)
            dimensions = dims.max_ - dims.min_

            component.points.Max_Dimensions = dimensions
            component.points.Dimensions     = dimensions
            component.transform(translation=dimensions.scale(0.5))

        with Layout("Component Information"):
            component.points.Reference = dimensions.hash_value(seed=comp_type)
            component.faces.material   = Material(None, "Material")

        component.out()

    # ====================================================================================================
    # Plank Selector
    # ====================================================================================================

    with GeoNodes("Selector", is_group=True, prefix=utils):

        comp_id = Integer(0,     "Comp Id", 0)
        linked  = Boolean(False, "Linked")

        all_comps = (Integer("Content") & IS_COMPONENT).not_equal(0)

        sel = Integer("Comp Id").equal(comp_id)
        linked_sel = Integer("Owner Id").equal(comp_id)

        sel.switch(linked, sel | linked_sel)

        (sel & all_comps).out("Selection")
        (sel.bnot() & all_comps).out("Invert")
        all_comps.out("All")


    # ====================================================================================================
    # Plank location and size
    # ====================================================================================================

    with GeoNodes("Get Location and Size", is_group=True, prefix=utils):

        mesh = Mesh()
        sel  = Boolean(False, "Selection", hide_value=True)

        node = mesh.points[sel].attribute_statistic(nd.position).node

        vmin = node.min
        vmax = node.max

        center = (vmin + vmax)/2
        size = vmax - vmin

        vmin.out("Min")
        vmax.out("Max")
        center.out("Center")
        size.out("Size")

    # ====================================================================================================
    # Extract a Plank
    # ====================================================================================================

    with GeoNodes("Extract", is_group=True, prefix=utils):

        mesh = Mesh()
        sel  = Boolean(False, "Selection", hide_value=True)

        # As Mesh method
        mesh.add_method()

        comp = mesh.points[sel.bnot()].delete()

        max_dims = comp.points.sample_index(Vector("Max Dimensions"), index=0)
        dims     = comp.points.sample_index(Vector("Dimensions"), index=0)
        orient   = comp.points.sample_index(Integer("Orientation"), index=0)
        content  = comp.points.sample_index(Integer("Content"), index=0)

        loc_size = utils.get_location_and_size(comp, True).node
        
        comp.out("Mesh")

        loc_size.out()
        max_dims.out("Max Dimensions")
        dims.out("Dimensions")
        orient.out("Orientation")
        content.out("Content")

        masked = content & MASK_TYPE
        masked.equal(TYPE_PLANK).out("Plank")
        masked.equal(TYPE_CLEAT).out("Cleat")
        masked.equal(TYPE_PANEL).out("Panel")
        masked.equal(TYPE_MESH).out("Custom")


    # ====================================================================================================
    # Stock Input
    # ====================================================================================================

    with GeoNodes("Component Input", is_group=True, prefix=utils):
        """ User Input for a component

        Can be a base material from an object or and existing plank.
        """

        mesh = Mesh()

        use_obj = Boolean(False, "From Object", tip="Get the base component from an object with modifier 'Base Component'")

        with Mesh.Switch(use_obj) as stock:

            comp_id = Integer(1, "From Id", tip="Use an existing plank as model")

            plank = mesh.extract(utils.selector(comp_id))

            plank.out("False")

            """
            dimensions = plank.points.sample_index(Vector("Dimensions"), index=0)
            node = plank.points.attribute_statistic(nd.position).node
            cur_dims = node.max - node.min
            plank.transform(scale=dimensions/cur_dims)

            plank.out("False")
            """

        with stock:
            obj = Object(None, "Base Material")
            mesh = Mesh(obj.info().geometry)

            mesh.out("True")

        stock = Mesh(stock).extract(True).node
        stock.out()

    # ====================================================================================================
    # Join a Component
    # ====================================================================================================

    with GeoNodes("Join Component", is_group=True, prefix=utils):
        """ Add the component to the furniture

        Named Attributes
        ----------------
        - Comp Id (Integer) : max of the existing ids + 1
        - Content (Integer) : Ensure flag CONTENT PART is set to "Content" named attribute
        - Face Random (Float) : a random float per face
        """
        
        mesh = Mesh()
        comp = Mesh(name = "Component")

        # As Mesh method
        mesh.add_method(jump=True)

        comp_info = comp.extract(True).node
        
        max_id = mesh.points.attribute_statistic(Float(Integer("Comp Id"))).max_.to_integer()
        
        comp_id = max_id + 1

        comp.points.Content = Integer("Content") | IS_COMPONENT
        comp.points.Comp_Id = comp_id
        comp.faces.Face_Random = Float.Random(0, 1, seed=comp_id)

        new_mesh = Mesh(mesh + comp)

        new_mesh.out("Mesh")
        comp_id.out("Comp Id")

    # ====================================================================================================
    # Create a component from a model
    # ====================================================================================================

    with GeoNodes("Create From Model", is_group=True, prefix=utils):

        comp   = Mesh()
        pos    = Vector(0,  "Position")
        dims   = Vector(1,  "Dimensions")
        orient = Integer(0, "Orientation")

        # As Mesh method
        comp.add_method()

        model_info = comp.extract(True).node

        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------

        with Layout("Scale to fit required dimensions"):

            width, length, _ = dims.xyz
            max_width, max_length, thickness = model_info.max_dimensions.xyz

            width.switch(model_info.panel, max_width)
            width = gnmath.min(width, max_width)
            length = gnmath.min(length, max_length)

            dims = Vector((width, length, thickness))

            comp.transform(scale=dims/model_info.size)
            comp.points.Dimensions = dims

        # ---------------------------------------------------------------------------
        # UV
        # ---------------------------------------------------------------------------

        with Layout("Mesh UV"):
            along_x = abs(nd.normal.dot((1, 0, 0))).greater_than(0.9)
            along_y = abs(nd.normal.dot((0, 1, 0))).greater_than(0.9)
            along_z = abs(nd.normal.dot((0, 0, 1))).greater_than(0.9)

            comp.faces[along_x].Face_Type = LONG_SIDE
            comp.faces[along_y].Face_Type = CUT_SIDE
            comp.faces[along_z].Face_Type = FACE

            vmin = comp.points.attribute_statistic(nd.position).min_
            vmax = vmin.max_
            size = vmax - vmin

            dx, dy, dz = (nd.position - vmin).xyz
            sx, sy, _ = size.xyz

            longer = sx.greater_than(sy)
            w = dx.switch(longer, dy)
            l = dy.switch(longer, dx)

            comp.corners[Integer("Face Type").equal(FACE)].store_uv(     "UVMap", ( w,  l, 0))
            comp.corners[Integer("Face Type").equal(LONG_SIDE)].store_uv("UVMap", (dz,  l, 0))
            comp.corners[Integer("Face Type").equal(CUT_SIDE)].store_uv( "UVMap", (dz,  w, 0))

        # ---------------------------------------------------------------------------
        # Orientation
        # ---------------------------------------------------------------------------

        with Layout("Set Orientation"):
            comp.points.Orientation = orient

            rot = Rotation.IndexSwitch(
                (0,     0,      0),
                (pi/2,  0,      0),
                (pi/2,  0,   pi/2),
                (0,    pi/2,    0),
                (0,     0,   pi/2),
                (0,    pi/2, pi/2),
                index=orient,
            )
            comp.transform(rotation=rot)

        # ---------------------------------------------------------------------------
        # Position
        # ---------------------------------------------------------------------------

        with Layout("Set Position"):

            dims_node = comp.points.attribute_statistic(nd.position).node
            comp.transform(translation=pos - dims_node.min)

        comp.out("Mesh")

    # ====================================================================================================
    # A Position
    # ====================================================================================================

    with GeoNodes("Get Component Position", is_group=True, prefix=utils):

        mesh = Mesh()
        sel = Boolean(False, "Selection", hide_value=True)

        # As Mesh method
        mesh.add_method()

        #comp_id = Integer(0, "Comp Id")
        i_axis  = Integer(0, "Axis")
        factor  = Float.Factor(0, "Min Max", 0, 1)

        dims = mesh.points[sel].attribute_statistic(nd.position).node

        v0 = Float.IndexSwitch(*dims.min.xyz, index=i_axis)
        v1 = Float.IndexSwitch(*dims.max.xyz, index=i_axis)

        factor.map_range(to_min=v0, to_max=v1, interpolation_type='LINEAR').out()

    # ====================================================================================================
    # Cotes of a Plank
    # ====================================================================================================

    with GeoNodes("View Cotes"):

        mesh = Mesh()
        sel  = Boolean(False, "Selection", hide_value=True)

        # As mesh method
        mesh.add_method(jump=True)

        comp = mesh.extract(sel)

        with Layout("Values"):
            min_xyz  = comp.min._lc("Pos").xyz
            size_xyz = comp.size._lc("Dim").xyz
        
        with Panel("Cotes", default_closed=True):

            for i_axis in range(3):

                axis = 'XYZ'[i_axis]
                with Panel(f"Cotes {axis}", create_layout=True):
                    line = utils.add_cote_line(
                        show     = Input(f"{axis} Dimension", default=False),
                        position = comp.min,
                        axis     = i_axis, 
                        value   = size_xyz[i_axis],
                        cote_offset_a = Float(0, "Dimension Offset A", hide_in_modifier=True),
                        cote_offset_b = Float(0, "Dimension Offset B", hide_in_modifier=True),
                    )
                    node0 = line.node
                    mesh += line

                    line = utils.add_cote_line(
                        show     = Input(f"{axis} Position", default=False),
                        position = 0,
                        axis     = i_axis,
                        value    = min_xyz[i_axis],
                        cote_offset_a = Float(0, "Position Offset A", hide_in_modifier=True),
                        cote_offset_b = Float(0, "Position Offset B", hide_in_modifier=True),
                    )
                    node1 = line.node
                    mesh += line     

                    invert = Boolean(False, "Invert")
                    node0.invert = invert
                    node1.invert = invert

        mesh.out()

    # ====================================================================================================
    # Locate a component
    # ====================================================================================================

    with GeoNodes("Locate", is_group=True, prefix=utils):

        mesh = Mesh()

        # As Mesh method
        mesh.add_method(jump=True)

        with Layout("Component dimensions"):
            sel   = Boolean(False, "Selection", hide_value=True)
            model = Mesh(None, "Model")

            comp_dims = mesh.points[sel].attribute_statistic(nd.position).node

            min_xyz  = comp_dims.min.xyz
            size_xyz = (comp_dims.max - comp_dims.min).xyz

        with Layout("Default position"):
            def_dims = model.points.attribute_statistic(nd.position).node

            def_min_xyz = def_dims.min.xyz
            def_max_xyz = def_dims.max.xyz

        with Panel("Position"):

            position   = [0, 0, 0]
            cote_start = [0, 0, 0]
            cote_len   = [0, 0, 0]
            show_cotes = [False, False, False]
            inverts    = [False, False, False]

            for i_axis in range(3):

                axis = 'XYZ'[i_axis]
    
                comp_size = size_xyz[i_axis]
                comp_min  = min_xyz[i_axis]

                def_min = def_min_xyz[i_axis]
                def_max = def_max_xyz[i_axis]

                axis_col  = ((.3, 0, 0), (0, .3, 0), (0, 0, .3))[i_axis]

                with Panel(axis, create_layout=True):

                    # ---------------------------------------------------------------------------
                    # Menu as first UI item
                    # ---------------------------------------------------------------------------

                    sel_index = Integer.MenuSwitch({
                        "Same"             : 0,
                        "Shifted"          : 1,
                        f"Shifted From Id" : 2,
                        f"Between"         : 3,
                        "Value"            : 4,
                        },
                        menu=Input("Position"),
                        default_menu = "Same",
                    )
                    user_value = Float.Distance(0.0, "Value")

                    # ---------------------------------------------------------------------------
                    # Relative to model
                    # ---------------------------------------------------------------------------

                    positive_value = user_value.greater_equal(0)
                    shifted_value = Float.Switch(positive_value,
                        def_min + user_value - comp_size,
                        def_max + user_value,
                    )

                    # ---------------------------------------------------------------------------
                    # Other Component
                    # ---------------------------------------------------------------------------

                    other_id = Integer(0, "Id")
                    other = mesh.extract(utils.selector(other_id))
                    other_min = other.min.xyz[i_axis]
                    other_max = other.min.xyz[i_axis]

                    shifted_other = Float.Switch(user_value.greater_equal(0),
                        other_min + user_value - comp_size,
                        other_max + user_value,
                    )

                    # ---------------------------------------------------------------------------
                    # Between two components
                    # ---------------------------------------------------------------------------

                    comp_id0 = Integer(0, "From Id")
                    node0 = mesh.extract(utils.selector(comp_id0))
                    bet0 = node0.max.xyz[i_axis]

                    comp_id1 = Integer(0, "To Id")
                    node1 = mesh.extract(utils.selector(comp_id1))
                    bet1 = node1.min.xyz[i_axis]

                    bet_fac = Float.Factor(0.5, "Between", 0, 1)
                    ref_fac = Float.Factor(0.5, "Alignment", 0, 1)

                    ref_offset = -ref_fac.map_range(to_max=comp_size)
                    bet_value = bet_fac.map_range(to_min=bet0 - ref_offset, to_max=bet1 + comp_size + ref_offset, interpolation_type='Linear')

                    # ---------------------------------------------------------------------------
                    # Select the value
                    # ---------------------------------------------------------------------------

                    v = Float.IndexSwitch(
                        comp_min,
                        shifted_value, 
                        shifted_other, 
                        bet_value + ref_offset, 
                        user_value + ref_offset,
                        index = sel_index)
                    position[i_axis] = v
                    
                    # ---------------------------------------------------------------------------
                    # Cotes
                    # ---------------------------------------------------------------------------

                    with Layout("Cote"):
                        show_cotes[i_axis] = Boolean(False, "Cote")
                        inverts[i_axis] = Boolean(False, "Invert")

                        cote_start[i_axis] = Float.IndexSwitch(
                            0.0,
                            Float.Switch(positive_value, def_min, def_max),    
                            Float.Switch(positive_value, other_min, other_max),
                            bet0,
                            0.0,
                            index = sel_index,
                        )

                        cote_len[i_axis] = Float.IndexSwitch(
                            comp_min,
                            Float.Switch(positive_value, user_value, user_value),    
                            Float.Switch(positive_value, user_value, user_value),
                            v - bet0,
                            user_value + ref_offset,
                            index=sel_index,
                        )

        with Layout("Set the Position"):
            pos_vec = Vector(position)
            mesh.points[sel].offset = pos_vec - comp_dims.min

        with Layout("Cotes"):
            cote_pos = pos_vec + (comp_dims.max - comp_dims.min)/2
            for i in range(3):
                pos = list(cote_pos.xyz)
                pos[i] = cote_start[i]

                with Panel(f"Cotes > {'XYZ'[i]}"):
                    mesh += utils.add_cote_line(show=show_cotes[i], position=pos, axis=i, value=cote_len[i]).link_inputs(exclude=["Aspect"]) 

        mesh.out()

    
    # ====================================================================================================
    # Main modifier : add a component
    # ====================================================================================================

    with GeoNodes("Add Component"):

        mesh = Mesh()

        with Panel("Model", create_layout=True):
            
            model = utils.component_input(mesh).link_inputs(None)
            fixed_width = model.cleat

            orient = Integer.MenuSwitch({
                "Shelf"         : 0,
                "Side"          : 1,
                "Door"          : 2,
                "Drawer"        : 3,
                "Rotated Shelf" : 4,
                "Rotated Side"  : 5,
            }, menu=Input("Orientation"))

        with Panel("Dimensions"):

            info = model.extract(True)
            width, length, thickness = info.dimensions.xyz
            max_width, max_length, _ = info.max_dimensions.xyz

            # ---------------------------------------------------------------------------
            # Length
            # ---------------------------------------------------------------------------

            with Panel("Length"):
                length_axis = Integer.IndexSwitch(1, 2, 2, 1, 0, 0, index=orient)
                l_dict = get_dimension(mesh, "Length", i_axis=length_axis, same_value=length, color="darkblue")
                length = l_dict['value']
                length = gnmath.min(length, max_length)

            # ---------------------------------------------------------------------------
            # Width
            # ---------------------------------------------------------------------------

            with Panel("Width"):
                width_axis = Integer.IndexSwitch(0, 0, 1, 2, 1, 2, index=orient)
                w_dict = get_dimension(mesh, "Width", i_axis=width_axis, same_value=width, color="orangered")
                width = w_dict['value']
                width = gnmath.min(width, max_width)
                width.switch(fixed_width, max_width)

        # ---------------------------------------------------------------------------
        # Create the component at (0, 0, 0)
        # ---------------------------------------------------------------------------

        with Layout("Create the component"):
            comp = model.create_from_model(dimensions=(width, length, thickness), orientation=orient)

        # ---------------------------------------------------------------------------
        # Join the component plank
        # ---------------------------------------------------------------------------

        with Layout("Join / locate / Cotes"):

            mesh.join_component(comp)

            comp_id  = mesh.comp_id
            comp_sel = utils.selector(comp_id)

            mesh.locate(comp_sel, model).link_inputs()
            mesh.view_cotes(comp_sel).link_inputs(None, include=["Cotes"])

        # ---------------------------------------------------------------------------
        # Gizmos
        # ---------------------------------------------------------------------------

        with Layout("Length Gizmo"):

            comp_info = mesh.extract(comp_sel)

            size2 = comp_info.size/2

            giz_dir = Vector.IndexSwitch(
                (0, 1, 0),
                (0, 0, 1),
                (0, 0, 1),
                (0, 1, 0),
                (1, 0, 0),
                (1, 0, 0),
                index=orient)
            
            giz_pos = comp_info.min + size2 + size2*giz_dir

            l_dict['custom'].linear_gizmo(position=giz_pos, direction=giz_dir, color_id='PRIMARY', draw_style='CROSS')
            l_dict['offset'].linear_gizmo(position=giz_pos, direction=giz_dir, color_id='PRIMARY', draw_style='CROSS')

        with Layout("Width Gizmo"):

            giz_dir = Vector.IndexSwitch(
                (1, 0, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 2),
                (0, 1, 0),
                (0, 0, 1),
                index=orient)
            
            giz_pos = comp_info.min + size2 + size2*giz_dir

            # No Gizmo if fixed width
            giz_dir.switch(fixed_width)

            w_dict['custom'].linear_gizmo(position=giz_pos, direction=giz_dir, color_id='SECONDARY', draw_style='CROSS')
            w_dict['offset'].linear_gizmo(position=giz_pos, direction=giz_dir, color_id='SECONDARY', draw_style='CROSS')

        mesh.out()
        comp_id.out("Comp Id")

    # ====================================================================================================
    # A cote line
    # ====================================================================================================

    with GeoNodes("Cote"):

        mesh = Mesh()

        # As Mesh method
        mesh.add_method(jump=True)

        show = Boolean(True, "Show")
        i_axis = Integer.MenuSwitch({"X": 0, "Y": 1, "Z": 2}, menu=Input("Axis"))

        from_id = Integer(1, "Id", panel="From")
        to_id = Integer(1, "Id", panel="To")

        v0 = mesh.get_component_position(utils.selector(from_id), axis=i_axis).link_inputs(None, "From")
        v1 = mesh.get_component_position(utils.selector(to_id), axis=i_axis).link_inputs(None, "To")

        axis = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis)
        x, y, z = mesh.extract(from_id).center.xyz

        line = utils.add_cote_line(
            position = Vector.IndexSwitch((v0, y, z), (x, v0, z), (x, y, v0), index=i_axis),
            axis     = i_axis, 
            value    = v1 - v0,
        ).link_inputs()

        mesh += line
        mesh.out()


    return

    # ====================================================================================================
    # Duplicate a component
    # ====================================================================================================

    with GeoNodes("Duplicate Component"):

        mesh = Mesh()
        comp_id = Integer(0, "Comp Id", 0)
        with Panel("X"):
            x_change = Boolean(False, "Translate X")
            x_offset = Float.Distance(0.0, "Offset X")

        with Panel("Y"):
            y_change = Boolean(False, "Translate Y")
            y_offset = Float.Distance(0.0, "Offset Y")

        with Panel("Z"):
            z_change = Boolean(False, "Translate Z")
            z_offset = Float.Distance(0.0, "Offset Z")

        with Panel("Options"):
            count  = Integer(1, "Count", 1)
            linked = Integer(0, "Linked", 0)

        with Layout("Translation Vector"):
            trans = Vector((
                x_offset.switch_false(x_change),
                y_offset.switch_false(y_change),
                z_offset.switch_false(z_change),
            ))

        with Layout("Gizmo"):

            comp_dims = mesh.extract(utils.selector(comp_id))

            O = comp_dims.center + trans

            x_offset.linear_gizmo(position = O, direction=(1, 0, 0), color_id='X')
            y_offset.linear_gizmo(position = O, direction=(0, 1, 0), color_id='Y')
            z_offset.linear_gizmo(position = O, direction=(0, 0, 1), color_id='Z')

        for rep_count in repeat(count, mesh=mesh, last_id=0):

            cur_trans = trans.scale(rep_count.iteration + 1)

            for rep_linked in repeat(1 + linked, mesh=rep_count.mesh, comp_id=comp_id, last_id=0):

                plank = mesh.extract(utils.selector(rep_linked.comp_id))
                plank.offset = cur_trans

                rep_linked.mesh = rep_linked.mesh.join_component(plank)
                rep_linked.comp_id += 1
                rep_linked.last_id = rep_linked.mesh.comp_id

            rep_count.mesh = rep_linked.mesh
            rep_count.last_id = rep_linked.last_id

        # ---------------------------------------------------------------------------
        # Cotes
        # ---------------------------------------------------------------------------

        mesh = rep_count.mesh

        with Layout("Dimensions"):
            x0, y0, z0         = center.xyz
            back, left, bottom = comp_dims.min.xyz
            front, right, top  = comp_dims.max.xyz
            size_x, size_y, size_z  = comp_dims.size.xyz

        with Layout("Cote X"):
            negative = x_offset.less_than(0)
            x = front.switch(negative, back)
            d = (x_offset - size_x).switch(negative, x_offset + size_x)
            cote = utils.cote_line(
                axis        = 0,
                show        = Boolean(False, "Cote", panel="X") & x_change,
                from_       = (x,     y0, z0),
                to          = (x + d, y0, z0),
                font_size   = FONT_SIZE,
                section     = SECTION,
                invert      = Boolean(False, "Invert", panel="X"),
                ).link_inputs(None, "X")
            mesh += cote

        with Layout("Cote X"):
            negative = y_offset.less_than(0)
            y = right.switch(negative, left)
            d = (y_offset - size_y).switch(negative, y_offset + size_y)
            cote = utils.cote_line(
                axis        = 1,
                show        = Boolean(False, "Cote", panel="Y") & y_change,
                from_       = (x0, y    , z0),
                to          = (x0, y + d, z0),
                font_size   = FONT_SIZE,
                section     = SECTION,
                invert      = Boolean(False, "Invert", panel="Y"),
                ).link_inputs(None, "Y")
            mesh += cote

        with Layout("Cote Z"):
            negative = z_offset.less_than(0)
            z = top.switch(negative, bottom)
            d = (z_offset - size_z).switch(negative, z_offset + size_z)
            cote = utils.cote_line(
                axis        = 2,
                show        = Boolean(False, "Cote", panel="Z") & z_change,
                from_       = (x0, y0, z),
                to          = (x0, y0, z + d),
                font_size   = FONT_SIZE,
                section     = SECTION,
                invert      = Boolean(False, "Invert", panel="Z"),
                ).link_inputs(None, "Z")
            mesh += cote

        mesh.out()
        rep_count.last_id.out("Comp Id")
        (count * (linked + 1)).out("Total")

    # ====================================================================================================
    # Rotate a Component
    # ====================================================================================================

    with GeoNodes("Rotate Component"):

        mesh     = Mesh()
        comp_id = Integer(0, "Comp Id", 0)
        linked   = Integer(0, "Linked", 0)

        i_axis = Integer(0, "Axis", 0, 2)

        with Panel("Pivot", create_layout=True):

            a = []
            for i in range(3):
                with Panel("XYZ"[i]):
                    # Selector as first UI
                    i_sel = Integer.MenuSwitch({
                        "Value" : 0,
                        "Min"   : 1,
                        "Max"   : 2,
                        },
                    menu = Input("Position")
                    )

                    pid = Integer(0, "Comp Id")
                    value = Float.Distance(0.0, "Value")
                    offset = Float.Distance(0.0, "Offset")
                    dims = mesh.extract(utils.selector(pid))

                    a.append(Float.IndexSwitch(value, dims.min.xyz[i] + offset, dims.max.xyz[i] + offset, index=i_sel))

            pivot = Vector.IndexSwitch((0, a[1], a[2]), (a[0], 0, a[2]), (a[0], a[1], 0), index=i_axis)._lc("Pivot")

        with Panel("Angle"):
            angle   = Float.Angle(0, "Angle")
            ag_min  = Float.Angle(-pi/2, "Min")
            ag_max  = Float.Angle(pi/2, "Max")

            clip_angle = gnmath.min(gnmath.max(ag_min, angle), ag_max)

        with Layout("Rotation"):
            rot = Rotation.IndexSwitch((clip_angle, 0, 0), (0, clip_angle, 0), (0, 0, clip_angle), index=i_axis)

            p = pivot + (rot @ (nd.position - pivot))

            pid = Integer("Comp Id")
            mesh[pid.greater_equal(comp_id) & pid.less_equal(comp_id + linked)].position = p

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        angle.dial_gizmo(
            position = pivot,
            up = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
        )

        mesh.out()
        comp_id.out("Comp Id")   

    # ====================================================================================================
    # Translate a Plank
    # ====================================================================================================

    with GeoNodes("Translate Component"):

        mesh     = Mesh()
        comp_id = Integer(0, "Comp Id", 0)
        linked   = Integer(0, "Linked", 0)

        i_axis = Integer(0, "Axis", 0, 2)
        with Panel("Value"):
            value    = Float.Distance( 0.0, "Value")
            val_min  = Float.Distance(-1.0, "Min")
            val_max  = Float.Distance( 1.0, "Max")

            clip_value = gnmath.min(gnmath.max(val_min, value), val_max)

        with Layout("Vector Offset"):
            trans = Vector.IndexSwitch((clip_value, 0, 0), (0, clip_value, 0), (0, 0, clip_value), index=i_axis)
            pid = Integer("Comp Id")
            mesh[pid.greater_equal(comp_id) & pid.less_equal(comp_id + linked)].offset = trans

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        with Layout("Gizmo"):

            dims = mesh.extract(utils.selector(comp_id))
            O = dims.center

            value.linear_gizmo(
                position = O,
                direction = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
            )

        mesh.out()
        comp_id.out("Comp Id")

    return

    # ====================================================================================================
    # Shelf
    # ====================================================================================================

    with GeoNodes("Shelf"):
        
        mesh = Mesh()

        left_id  = Integer(0, "Left Comp Id")
        right_id = Integer(0, "Right Comp Id")
        
        setback0 = Float.Distance(0.0,  "Back Setback", 0)
        setback1 = Float.Distance(0.02, "Front Setback", 0)
        
        node = Group("Plank", {
            "Dimensions > Length > Length" : 'Between Planks',
            "Dimensions > Length > From Plank" : left_id,
            "Dimensions > Length > From Max" : True,
            "Dimensions > Length > To Plank" : right_id,
            "Dimensions > Length > To Min" : True,

            "Dimensions > Width > Offset" : -(setback0 + setback1),
            },            
            mesh        = mesh,
            orientation =  "Shelf",
            
        ).link_inputs(None, include=["Model", "Position > Z", "Cotes"])

        node.out()

    # ====================================================================================================
    # Plinths
    # ====================================================================================================

    with GeoNodes("Plinth Front"):
        
        mesh = Mesh()
        comp_id = Integer(0, "Under Comp Id")
        setback = Float.Distance(0.02, "Setback", 0)
        
        left_ofs = Float.Distance(0.0, "Left Offset")
        right_ofs = Float.Distance(0.0, "Right Offset")

        node = Group("Plank", {
            "Dimensions > Length > Length" : 'Plank Size Y',
            "Dimensions > Length > Plank" : comp_id,
            "Dimensions > Length > Offset" : -(left_ofs + right_ofs),

            "Dimensions > Width > Width" : 'Between Planks',
            "Dimensions > Width > From Plank" : 0,
            "Dimensions > Width > To Plank" : comp_id,
            "Dimensions > Width > To Min" : True,

            "Position > X > Behind" : True,
            "Position > X > Position" : 'Plank X Max',
            "Position > X > Plank" : comp_id,
            "Position > X > Offset" : -setback,

            "Position > Y > Left" : False,
            "Position > Y > Position" : 'Plank Y Min',
            "Position > Y > Plank" : comp_id,
            "Position > Y > Offset" : left_ofs,

            },            
            mesh        = mesh,
            orientation =  "Drawer",
            
        ).link_inputs(None, include=["Model", "Cotes"])

        node.out()

    with GeoNodes("Plinth Side"):
        
        mesh = Mesh()
        comp_id = Integer(0, "Under Comp Id")
        setback = Float.Distance(0.02, "Setback", 0)
        
        back_ofs = Float.Distance(0.0, "Back Offset")
        front_ofs = Float.Distance(0.0, "Front Offset")

        node = Group("Plank", {
            "Dimensions > Length > Length" : 'Plank Size X',
            "Dimensions > Length > Plank" : comp_id,
            "Dimensions > Length > Offset" : -(back_ofs + front_ofs),

            "Dimensions > Width > Width" : 'Between Planks',
            "Dimensions > Width > From Plank" : 0,
            "Dimensions > Width > To Plank" : comp_id,
            "Dimensions > Width > To Min" : True,

            "Position > X > Behind" : False,
            "Position > X > Position" : 'Value',
            "Position > X > Value" : back_ofs,

            "Position > Y > Left" : False,
            "Position > Y > Position" : 'Plank Y Min',
            "Position > Y > Plank" : comp_id,
            "Position > Y > Offset" : setback,
            },            
            mesh        = mesh,
            orientation =  "Rotated Side",
            
        ).link_inputs(None, include=["Model", "Cotes"])

        node.out()

    # ====================================================================================================
    # Ask for a box
    # ====================================================================================================

    with GeoNodes("Box Dimensions", is_group=True, prefix=utils):

        mesh = Mesh()

        with Panel("Planks"):
            left_id  = Integer(0, "Left Plank")
            right_id = Integer(0, "Right Plank")
            bot_id   = Integer(0, "Bottom Plank")
            top_id   = Integer(0, "Top Plank")

        with Layout("Left"):
            left_dims  = mesh.extract(utils.selector(left_id))

            x0, out_y0, _ = left_dims.min.xyz
            x1, in_y0, _  = left_dims.max.xyz

        with Layout("Right"):
            right_dims = mesh.extract(utils.selector(right_id))
        
            x, in_y1, _ = right_dims.min.xyz
            x0 = gnmath.min(x0, x)
            x, out_y1, _  = right_dims.max.xyz
            x1 = gnmath.max(x1, x)

        with Layout("Bottom"):
            bot_dims   = mesh.extract(utils.selector(bot_id))
        
            x, _, out_z0 = bot_dims.min.xyz
            x0 = gnmath.min(x0, x)
            x, _, in_z0  = bot_dims.max.xyz
            x1 = gnmath.max(x1, x)


        with Layout("Top"):
            top_dims   = mesh.extract(utils.selector(top_id))

            x, _, in_z1 = top_dims.min.xyz
            x0 = gnmath.min(x0, x)
            x, _, out_z1  = top_dims.max.xyz
            x1 = gnmath.max(x1, x)

        in_y0.out("In y0")
        in_y1.out("In y1")
        in_z0.out("In z0")
        in_z1.out("In z1")

        out_y0.out("Out y0")
        out_y1.out("Out y1")
        out_z0.out("Out z0")
        out_z1.out("Out z1")

        x0.out("x0")
        x1.out("x1")

    # ====================================================================================================
    # Door
    # ====================================================================================================

    with GeoNodes("Door"):
        
        mesh = Mesh()

        inside = Boolean(True,  "Inside")
        double = Boolean(False, "Double")

        gap  = Float.Distance(0.002, "Gap")
        over = Float.Distance(0.007, "Over")

        with Panel("Opening", create_layout=True):

            right_hinge = Boolean(False, "Right Hinge")

            left_angle  = Float.Angle(0, "Angle",    -pi, 0, hide_in_modifier=True)._lc("Left Angle")
            right_angle = Float.Angle(0, "Right Angle", 0, pi, hide_in_modifier=True)._lc("Right Angle")

            open_left = (double | right_hinge.bnot())._lc("Open Left")
            open_right = (double | right_hinge)._lc("Open Right")
            
        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------

        with Layout("Box values"):
            
            box = utils.box_dimensions(mesh).link_inputs()

            y0 = Float.Switch(inside, box.in_y0 - over, box.in_y0 + gap)._lc("y0")
            y1 = Float.Switch(inside, box.in_y1 + over, box.in_y1 - gap)._lc("y1")
            z0 = Float.Switch(inside, box.in_z0 - over, box.in_z0 + gap)._lc("z0")
            z1 = Float.Switch(inside, box.in_z1 + over, box.in_z1 - gap)._lc("z1")

            front = box.x1._lc("Front")

        with Layout("Dimensions"):
            width = (y1 - y0)._lc("Width")
            width.switch(double, (width - gap)/2)
            height = (z1 - z0)._lc("Height")

        # ---------------------------------------------------------------------------
        # First door
        # ---------------------------------------------------------------------------

        with Layout("First Door (left)"):

            mesh = Group("Plank", {                
                "Dimensions > Length > Length" : 'Value',
                "Dimensions > Length > Value" : height,

                "Dimensions > Width > Width" : 'Value',
                "Dimensions > Width > Value" : width,
                
                "Position > X > Behind" : inside,
                "Position > X > Position" : 'Value',
                "Position > X > Value" : front,

                "Position > Y > Position" : 'Value',
                "Position > Y > Value" : y0,

                "Position > Z > Position" : 'Value',
                "Position > Z > Value" : z0,
                },            
                mesh        = mesh,
                orientation =  "Door",
                
            ).link_inputs(None, include=["Model", "Cotes"]).mesh

            left_door_id = mesh.comp_id._lc("Left Door Id")

        # ---------------------------------------------------------------------------
        # Second door (right)
        # ---------------------------------------------------------------------------

        with Layout("Second Door"):

            mesh2 = G().duplicate_plank(mesh, left_door_id, translate_y = True, offset_y = width + gap)
            right_door_id = mesh2.comp_id._lc("Right Door Id")
            right_door_id.switch_false(double)            

            mesh = mesh.switch(double, mesh2)

        # ---------------------------------------------------------------------------
        # Open the doors
        # ---------------------------------------------------------------------------

        with Layout("Rotate doors"):

            left_mesh = G().rotate_plank(
                mesh,
                comp_id = left_door_id,
                axis = 2,
                pivot_x_position = "Value",
                pivot_x_value = front, #left_dims.max.x,
                pivot_y_position = "Value",
                pivot_y_value = y0,
                angle = left_angle,
                angle_min = -pi,
                angle_max = pi,
            )
            mesh.switch(open_left, left_mesh)

            right_mesh = G().rotate_plank(
                mesh,
                comp_id = right_door_id,
                axis = 2,
                pivot_x_position = "Value",
                pivot_x_value = front, #right_dims.max.x,
                pivot_y_position = "Value",
                pivot_y_value = y1,
                angle = right_angle,
                angle_min = -pi,
                angle_max = pi,
            )
            mesh.switch(open_right, right_mesh)
            

        mesh.out()
        left_door_id.out("Left Id")
        right_door_id.out("Right Id")


    return

    # ====================================================================================================
    # Drawer
    # ====================================================================================================

    with GeoNodes("Drawer"):

        mesh = Mesh()

        mesh = G().door(mesh=mesh, double=False).link_inputs(None, "Drawer Front")
        front_id = mesh.comp_id

        with Panel("Drawer Box", create_layout=True):

            depth = Float.Distance(0.3, "Depth", 0.05)

            with Panel("Sides"):
                sb_side    = Float.Distance(0.0,   "Side Setback",   0.0)
                sb_bot     = Float.Distance(0.0,   "Bottom Setback", 0.0)
                sb_top     = Float.Distance(0.0,   "Top Setback",    0.0)
                side_thick = Float.Distance(0.012, "Thickness",      MIN_DIM)
                back_fix   = Integer.MenuSwitch({
                    "Back Nailed on Sides": 0,
                    "Sides Nailed on Back": 1,
                    "Back and Sides @ 45°": 2,
                    },
                    menu = Input("Back Fixing")
                )
                side_mat   = Material("Plank", "Material")

            with Panel("Bottom"):
                bot_thick  = Float.Distance(0.002, "Bottom Thickness", 0.0)
                bot_nailed = Boolean(True, "Nailed Underneath")
                sb_groove  = Float.Distance(0.005, "Groove Setback", 0.0)
                groove     = Float.Distance(0.002, "Groove Depth", MIN_DIM)

                bot_mat    = Material("Plank", "Material")

            dims = G().get_dimensions(mesh, True, front_id).node
            x0, y0, z0 = dims.min.xyz
            sx, sy, sz = dims.size.xyz

            with Layout("Sides Z0"):
                side_z0 = (z0 + sb_bot)._lc("Sides Z0")
                side_z0 = side_z0.switch(bot_nailed, side_z0 + bot_thick)._lc("Sides Z0")

            with Layout("Sides Height"):
                side_height = (sz - sb_top - sb_bot)._lc("Sides Height, Bot Nailed")
                side_height = side_height.switch(bot_nailed, side_height - bot_thick)._lc("Sides Height")

            with Layout("Left Side Y0"):
                left_y0 = (y0 + sb_side)._lc("Left Side Y0")

            with Layout("Left & Right Sides Length"):
                side_length = depth.switch(back_fix.equal(0), depth - side_thick)._lc("Sides Length")

            with Layout("Back Length"):
                back_length = sy - 2*sb_side
                back_length = back_length.switch(back_fix.equal(1), back_length - 2*side_thick)._lc("Back Length")

            with Layout("Back X0"):
                back_x0 = (x0 - depth)._lc("Back X0")

            with Layout("Back Y0"):
                back_y0 = left_y0.switch(back_fix.equal(1), left_y0 + side_thick)._lc("Back Y0")

            with Layout("Bottom"):
                groove_delta = (side_thick - groove)._lc("Groove Delta")

                bot_width = (sy - 2*sb_side)._lc("Bottom Nailed Width")
                bot_width = bot_width.switch_false(bot_nailed, bot_width - 2*groove_delta)._lc("Bottom Width")

                bot_depth = depth._lc("Bottom Nailed Depth")
                bot_depth = bot_depth.switch_false(bot_nailed, bot_depth - groove_delta + groove)

                bot_x0 = (x0 - depth)._lc("Bottom Nailed X0")
                bot_x0 = bot_x0.switch_false(bot_nailed, bot_x0 + groove_delta)._lc("Bottom X0")

                bot_y0 = left_y0.switch_false(bot_nailed, left_y0 + groove_delta)._lc("Bottom Y0")

                nailed_z0 = (side_z0 - bot_thick)._lc("Bottom Nailed Z0")
                groove_z0 = (side_z0 + sb_groove)._lc("Bottom Groove Z0")
                bot_z0 = groove_z0.switch(bot_nailed, nailed_z0)._lc("Bottom Z0")

            # ---------------------------------------------------------------------------
            # Side Panels
            # ---------------------------------------------------------------------------

            with Layout("Left Side"):

                mesh = Group("Plank", {
                    "From Model > Model"     : 'Default',
                    "From Model > Material"  : side_mat,

                    "Width > Width"     : 'Value',
                    "Width > Value"     : side_length, # Orientation is 'Side'
                    
                    "Length > Length"   : 'Value',
                    "Length > Value"    : side_height,

                    "Thickness > Thickness" : 'Value',
                    "Thickness > Value"     : side_thick,
                    
                    "X > Alignment"     : 'Behind',
                    "X > X"             : 'Value',
                    "X > Value"         : x0,
                    
                    "Y > Alignment"     : 'Right',
                    "Y > Y"             : 'Value',
                    "Y > Value"         : left_y0,
                    
                    "Z > Alignment"     : 'Above',
                    "Z > Z"             : 'Value',
                    "Z > Value"         : side_z0,
                    },
                    mesh        = mesh,
                    orientation =  "Side",
                    ).mesh
                left_id = mesh.comp_id

            with Layout("Duplicate for right side"):
                mesh = G().duplicate_plank(
                    mesh        = mesh,
                    comp_id    = left_id,
                    count       = 1,
                    translate_y = True,
                    offset_y    = sy - 2*sb_side - side_thick,
                )
                right_id = mesh.comp_id

            # ---------------------------------------------------------------------------
            # Back Panel
            # ---------------------------------------------------------------------------

            with Layout("Back"):

                mesh = Group("Plank", {
                    "From Model > Model"     : 'Comp Id',
                    "From Model > Model ID"  : left_id,

                    "Width > Width"     : 'Value',
                    "Width > Value"     : back_length, # Orientation is 'Vertical'
                    
                    "Length > Length"   : 'Value',
                    "Length > Value"    : side_height,

                    "Thickness > Thickness" : 'Value',
                    "Thickness > Value"     : side_thick,
                    
                    "X > Alignment"     : 'In Front',
                    "X > X"             : 'Value',
                    "X > Value"         : back_x0,
                    
                    "Y > Alignment"     : 'Right',
                    "Y > Y"             : 'Value',
                    "Y > Value"         : back_y0,
                    
                    "Z > Alignment"     : 'Above',
                    "Z > Z"             : 'Value',
                    "Z > Value"         : side_z0,
                    },
                    mesh        = mesh,
                    orientation =  "Vertical",
                    ).mesh
                back_id = mesh.comp_id

            # ---------------------------------------------------------------------------
            # Bottom
            # ---------------------------------------------------------------------------

            with Layout("Bottom"):

                mesh = Group("Plank", {
                    "From Model > Model"     : 'Default',
                    "From Model > Material"  : bot_mat,

                    "Width > Width"     : 'Value',
                    "Width > Value"     : bot_depth, # Orientation is 'Horizontal'
                    
                    "Length > Length"   : 'Value',
                    "Length > Value"    : bot_width, # Orientation is 'Horizontal'

                    "Thickness > Thickness" : 'Value',
                    "Thickness > Value"     : bot_thick,
                    
                    "X > Alignment"     : 'In Front',
                    "X > X"             : 'Value',
                    "X > Value"         : bot_x0,
                    
                    "Y > Alignment"     : 'Right',
                    "Y > Y"             : 'Value',
                    "Y > Value"         : bot_y0,
                    
                    "Z > Alignment"     : 'Above',
                    "Z > Z"             : 'Value',
                    "Z > Value"         : bot_z0,
                    },
                    mesh        = mesh,
                    orientation =  "Horizontal",
                    ).mesh
                bot_id = mesh.comp_id

        with Panel("Opening", create_layout=True):

            mesh = G().translate_plank(
                mesh     = mesh,
                comp_id = front_id,
                linked   = 4,
                axis     = 0,
                value    = Float.Distance(0.0, "Open"),
                min      = 0.0,
                max      = 0.9*depth,
            )

        mesh.out()

        front_id.out(   "Front ID")
        left_id.out(    "Left ID")
        right_id.out(   "Right_ID")
        back_id.out(    "Back ID")
        bot_id.out(     "Bottom ID")
        
    # ====================================================================================================
    # Cut sheet
    # ====================================================================================================

    with GeoNodes("Cut Sheet"):
        
        mesh = Mesh()
        count = Group("Get Dimensions", mesh=mesh).next_id
        
        cloud = Cloud.Points(count=count)
        for rep in repeat(count, cloud=cloud):
            plank = Mesh(mesh).points[nd.id.not_equal(rep.iteration)].delete()
            
            sel = nd.index.equal(rep.iteration)
            rep.cloud.points[sel].Dimensions = plank.points.sample_index(Vector("Dimensions"), index=0)
            rep.cloud[sel].position = plank.points.attribute_statistic(nd.position).mean
            
        cloud = rep.cloud
        cloud.set_id(nd.index)
            
        cloud.out()





    return
    








    # ====================================================================================================
    # Join Part
    # ====================================================================================================

    with GeoNodes("Add Plank", is_group=True):
        
        planks, mesh = get_planks()
        plank = Mesh(name="Plank")
        orient = Integer(0, "Orientation")
        
        max_id = planks.points.attribute_statistic(Float(nd.id)).max_.to_integer()
        comp_id = max_id + 1
        #comp_id = comp_id.switch(planks.points.count.equal(0), 0)
        plank.set_id(comp_id)
        plank.faces.Face_Random = Float.Random(0, 1, seed=comp_id)

        new_mesh = Mesh(mesh + plank)
        sel = nd.id.equal(comp_id)
        new_mesh.points[sel].Orientation = orient

        new_mesh.out("Mesh")
        comp_id.out("Comp Id")



    # ====================================================================================================
    # Rotate a Plank
    # ====================================================================================================

    with GeoNodes("Rotate Plank"):

        mesh     = Mesh()
        comp_id = Integer(0, "Comp Id", 0)
        linked   = Integer(0, "Linked", 0)

        i_axis = Integer(0, "Axis", 0, 2)
        x_factor = Float.Factor(0., "Pivot X", -0.1, 1.1)
        y_factor = Float.Factor(0., "Pivot Y", -0.1, 1.1)
        z_factor = Float.Factor(0., "Pivot Z", -0.1, 1.1)
        with Panel("Angle"):
            angle   = Float.Angle(0, "Angle")
            ag_min  = Float.Angle(-pi/2, "Min")
            ag_max  = Float.Angle(pi/2, "Max")

            clip_angle = gnmath.min(gnmath.max(ag_min, angle), ag_max)

        plank = G().get_dimensions(mesh, True, comp_id)

        with Layout("Pivot"):
            pivot = plank.min_ + plank.size * (x_factor, y_factor, z_factor)

        with Layout("Rotation"):
            rot = Rotation.IndexSwitch((clip_angle, 0, 0), (0, clip_angle, 0), (0, 0, clip_angle), index=i_axis)

        with Layout("Rotate the positions around pivot"):
            p = pivot + (rot @ (nd.position - pivot))

            mesh[nd.id.greater_equal(comp_id) & nd.id.less_equal(comp_id + linked)].position = p

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        gizmo = angle.dial_gizmo(
            position = pivot,
            up = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
        )

        mesh.out()
        comp_id.out("Comp Id")


    # ====================================================================================================
    # MACRO : Ask for a Dimension
    # ====================================================================================================
        
    def ask_dimension(mesh, name, default_value=0.3, kept_value=None):
        """ Ask for a dimension

        Arguments
        ---------
        - mesh (Mesh) : the stack of planks
        - name (str) : name of the cote
        - default_value (float) : default user value
        - kept_value (Float: None) : value to keep
            
        Returns
        -------
        - value, dict: offset, no_offset, user_value, cote0
        """
        
        with Layout("Dimension"):

            # ---------------------------------------------------------------------------
            # Plank 0
            # ---------------------------------------------------------------------------
        
            id0 = Integer(0, "Comp Id")
            
            with Layout("Plank 0"):
                plank0 = G().get_dimensions(mesh, True, id0)

            # ---------------------------------------------------------------------------
            # Plank 1
            # ---------------------------------------------------------------------------

            with Layout("Plank 1"):
                id1 = Integer(1, "Other ID")
                plank1 = G().get_dimensions(mesh, True, id1)
                
                dist_x = plank1.back - plank0.front
                dist_y = plank1.left - plank0.right
                dist_z = plank1.bot  - plank0.top
                
                dist_x = dist_x.switch(dist_x.less_than(0), plank0.back - plank1.front)
                dist_y = dist_y.switch(dist_y.less_than(0), plank0.left - plank1.right)
                dist_z = dist_z.switch(dist_z.less_than(0), plank0.bot  - plank1.top)

            # ---------------------------------------------------------------------------
            # Selection
            # ---------------------------------------------------------------------------

            user_value = Float.Distance(default_value, "Value", MIN_DIM)

            with Float.MenuSwitch() as selected_value:
                if kept_value is not None:
                    kept_value.out(     "Keep")
                user_value.out(         "Value")
                plank0.width.out(       "Width")
                plank0.length.out(      "Length")
                plank0.thickness.out(   "Thickness")
                plank0.back.out(        "X Min")
                plank0.left.out(        "Y Min")
                plank0.bot.out(         "Z Min")
                plank0.front.out(       "X Max")
                plank0.right.out(       "Y Max")
                plank0.top.out(         "Z Max")
                plank0.size_x.out(      "Size X")
                plank0.size_y.out(      "Size Y")
                plank0.size_z.out(      "Size Z")
                dist_x.out(             "Distance X")
                dist_y.out(             "Distance Y")
                dist_z.out(             "Distance Z")

            selected_value.menu = Input(name, default="Keep")

            with Layout("Offset"):                                           
                
                no_offset = selected_value.value

                offset  = Float.Distance(0.0, "Offset")

                value = selected_value.switch_false(no_offset, selected_value + offset)
                value = gnmath.max(value, MIN_DIM)

        return value, {
            'no_offset'   : no_offset, 

            'user_value'  : user_value,

            'offset'      : offset, 
            #'cote0'       : selected_value.switch(no_offset),
            }
        
    # ====================================================================================================
    # MACRO : Ask for a Location
    # ====================================================================================================

    def ask_location(mesh, name, i_axis, *, default_value=0.0, model_min=None, model_max=None):
            """ Ask for a location

            Arguments
            ---------
            - mesh (Mesh) : the stack of planks
            - name (str) : name of the cote
            - i_axis (int in (0, 1, 2)) : axis index
            - default_value (float) : default user value
            - model_min (Float) : model min value
            - model_max (Float) : model max value
                
            Returns
            -------
            - value, dict: offset, no_offset, user_value, cote0
            """
            
            with Layout(f"{name} Location"):

                # ---------------------------------------------------------------------------
                # Plank 0
                # ---------------------------------------------------------------------------
            
                id0 = Integer(0, "Comp Id")
                
                with Layout("Plank 0"):
                    plank0 = G().get_dimensions(mesh, True, id0)

                axis = 'XYZ'[i_axis]

                xyz0 = plank0.min_.xyz
                xyz1 = plank0.max_.xyz

                user_value = Float.Distance(default_value, "Value")

                def_menu = None

                with Float.MenuSwitch() as selected_value:

                    if model_min is not None:
                        option_name = f"Model {axis} Min"
                        model_min.out(option_name)
                        def_menu = option_name

                    if model_max is not None:
                        option_name = f"Model {axis} Max"
                        model_max.out(option_name)
                        if def_menu is None:
                            def_menu = option_name

                    Float(0.0).out(         "Zero")
                    user_value.out(         "Value")
                    xyz0[i_axis].out(        f"{axis} Min")
                    xyz1[i_axis].out(        f"{axis} Max")

                selected_value.menu = Input(name, default="Zero" if def_menu is None else def_menu)

                no_offset = selected_value.zero | selected_value.value

                with Layout("Offset"):                                           

                    offset  = Float.Distance(0.0, "Offset")

                    value = selected_value.switch_false(no_offset, selected_value + offset)

            return value, {
                'no_offset'   : no_offset, 

                'user_value'  : user_value,

                'offset'      : offset, 
                'cote0'       : selected_value.switch(no_offset),
                }

    # ====================================================================================================
    # Locate Plank
    # ====================================================================================================

    with GeoNodes("Locate") as tree:
        
        mesh = Mesh()
        comp_id = Integer(0, "ID", 0)
        model_id = Integer(0, "Model ID", 0)

        plank = G().get_dimensions(mesh, True, comp_id)
        size_x, size_y, size_z = plank.size_x, plank.size_y, plank.size_z

        model = G().get_dimensions(mesh, True, model_id)
        
        # ---------------------------------------------------------------------------
        # Location
        # ---------------------------------------------------------------------------

        with Panel("X", create_layout=True):
            
            with Float.MenuSwitch(menu=Input("X Alignment")) as delta_x:
                Float(0.0).out(     "In Front")
                Float(size_x/2).out("Centered")
                Float(size_x).out(  "Behind")
                #(-model.back).out(  "Keep")
                
            x, x_dict = ask_location(mesh, "X", i_axis=0, model_min=model.back, model_max=model.front)

        with Panel("Y", create_layout=True):
            
            with Float.MenuSwitch(menu=Input("Y Alignment")) as delta_y:
                Float(0.0).out(     "Right")
                Float(size_y/2).out("Centered")
                Float(size_y).out(  "Left")
                #(-model.left).out(  "Keep")
                
            y, y_dict = ask_location(mesh, "Y", i_axis=1, model_min=model.left, model_max=model.right)
            
        with Panel("Z", create_layout=True):
            
            with Float.MenuSwitch(menu=Input("Z Alignment")) as delta_z:
                Float(0.0).out(     "Above")
                Float(size_z/2).out("Centered")
                Float(size_z).out(  "Below")
                #(-model.bot).out(   "Keep")

            z, z_dict = ask_location(mesh, "Z", i_axis=2, model_min=model.bot, model_max=model.top)
            
        # ---------------------------------------------------------------------------
        # Translation
        # ---------------------------------------------------------------------------
        
        # Current origin
        old_x, old_y, old_z = plank.back, plank.left, plank.bot
        
        # Target origin
        ox, oy, oz = x - delta_x, y - delta_y, z - delta_z
        
        # Translate    
        mesh[nd.id.equal(comp_id)].offset = (ox - old_x, oy - old_y, oz - old_z)    
        
        # ---------------------------------------------------------------------------
        # Labels
        # ---------------------------------------------------------------------------
        
        # Cotes params
        # User offset are hidden and connected using link_inputs 
        
        invert = False
        
        cote = G().cote_line(
            axis        = 0,
            show        = Boolean(False, "Cote", panel="X"),
            from_       = (x_dict['cote0'], 0, 0),
            to          = (x, 0, 0),
            font_size   = FONT_SIZE,
            section     = SECTION,
            invert      = Boolean(False, "Invert", panel="X"),
            ).link_inputs(None, "X")
        mesh += cote
        
        cote = G().cote_line(
            axis        = 1,
            show        = Boolean(False, "Cote", panel="Y"),
            from_       = (0, y_dict['cote0'], 0),
            to          = (0, y, 0),
            font_size   = FONT_SIZE,
            section     = SECTION,
            invert      = Boolean(False, "Invert", panel="Y"),
            ).link_inputs(None, "Y")
        mesh += cote
        
        cote = G().cote_line(
            axis        = 2,
            show        = Boolean(False, "Cote", panel="Z"),
            from_       = (0, 0, z_dict['cote0']),
            to          = (0, 0, z),
            font_size   = FONT_SIZE,
            section     = SECTION,
            invert      = Boolean(False, "Invert", panel="Z"),
            ).link_inputs(None, "Z")
        mesh += cote
                
        # ---------------------------------------------------------------------------
        # Gizmos
        # ---------------------------------------------------------------------------
                
        if USE_GIZMO:
            with Layout("Gizmo"):
                g_pos = (ox + size_x/2, oy + size_y/2, oz + size_z/2)
                g_vx = x_dict['user_value'].linear_gizmo(position=g_pos, direction=(1, 0, 0), color_id='X', draw_style='ARROW')
                g_vy = y_dict['user_value'].linear_gizmo(position=g_pos, direction=(0, 1, 0), color_id='Y', draw_style='ARROW')
                g_vz = z_dict['user_value'].linear_gizmo(position=g_pos, direction=(0, 0, 1), color_id='Z', draw_style='ARROW')
                
                g_ox = x_dict['offset'].linear_gizmo(position=g_pos, direction=(1, 0, 0), color_id='X', draw_style='BOX')
                g_oy = y_dict['offset'].linear_gizmo(position=g_pos, direction=(0, 1, 0), color_id='Y', draw_style='BOX')
                g_oz = z_dict['offset'].linear_gizmo(position=g_pos, direction=(0, 0, 1), color_id='Z', draw_style='BOX')


        mesh.out("Mesh")
        Vector((ox, oy, oz)).out("Origin")
        Vector((size_x, size_y, size_z)).out("Size")   

    # ====================================================================================================
    # A plank
    # ====================================================================================================

    with GeoNodes("Plank") as tree:
        
        # ---------------------------------------------------------------------------
        # Init
        # ---------------------------------------------------------------------------

        with Layout("Get the model"):
            
            mesh = Mesh()

            with Panel("From Model"):
            
                with Mesh.MenuSwitch(menu=Input("Model")) as model:
                    model_id = Integer(0, "Model ID", 0)
                    plank = Mesh(mesh).points[nd.id.not_equal(model_id)].delete()

                    plank_orientation = plank.points.sample_index(Integer("Orientation"), index=0)

                    # Rotate horizontal to keep UV
                    rot = Rotation.IndexSwitch(
                        0,                      # Horizontal
                        (-pi/2, 0, 0),          # Side
                        (0, -pi/2, 0),          # Front
                        (-pi/2, -pi/2, 0),      # Vertical
                        index=plank_orientation)
                    plank.transform(rotation=rot)

                    plank.out("Comp Id")

                with model:
                    def_size = (0.3, 1.0, .02)
                    plank = Mesh.Cube(size=def_size)
                    plank.points.Dimensions = def_size
                    plank.faces.material = Material("Plank", "Material")

                    plank.out("Default")
                    
                with model:
                    plank_obj = Object(None, "Model Object")
                    plank = plank_obj.info().geometry.separate_components().mesh
                    plank.points.Dimensions = G().get_dimensions(plank).size
                    plank.out("Object")
                    
                with Layout("Initialize"):            
                    plank = G().get_dimensions(model)
                    dims = plank.node
                    plank.set_id(0)
            
        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------
        
        with Panel("Width", create_layout=True):
            width, w_dict = ask_dimension(mesh, "Width", default_value=0.30, kept_value=dims.width)

            cote_width = Boolean(False, "Cote")
            invert_width = Boolean(False, "Invert")
            
        with Panel("Length", create_layout=True):
            length, l_dict = ask_dimension(mesh, "Length", default_value=1.0, kept_value=dims.length)
            cote_length = Boolean(False, "Cote")
            invert_length = Boolean(False, "Invert")
            
        with Panel("Thickness", create_layout=True):
            thickness, t_dict = ask_dimension(mesh, "Thickness", default_value=0.02, kept_value=dims.thickness)
            cote_thick = Boolean(False, "Cote")
            invert_thick = Boolean(False, "Invert")

        plank = plank.transform(scale=(
            width/dims.size_x, 
            length/dims.size_y, 
            thickness/dims.size_Z))
        
        new_dims = Vector((width, length, thickness))
        plank.points.Dimensions = new_dims
        
        plank = plank.transform(translation=new_dims.scale(0.5))

        # ---------------------------------------------------------------------------
        # UV
        # ---------------------------------------------------------------------------

        with Layout("Plank UV"):
            along_x = abs(nd.normal.dot((1, 0, 0))).greater_than(0.9)
            along_y = abs(nd.normal.dot((0, 1, 0))).greater_than(0.9)
            along_z = abs(nd.normal.dot((0, 0, 1))).greater_than(0.9)

            plank.faces[along_x].Face_Type = LONG_SIDE
            plank.faces[along_y].Face_Type = CUT_SIDE
            plank.faces[along_z].Face_Type = FACE

            vmin = plank.points.attribute_statistic(nd.position).min_
            vmax = vmin.max_
            size = vmax - vmin

            dx, dy, dz = (nd.position - vmin).xyz
            sx, sy, _ = size.xyz

            longer = sx.greater_than(sy)
            w = dx.switch(longer, dy)
            l = dy.switch(longer, dx)

            plank.corners[Integer("Face Type").equal(FACE)].store_uv(     "UVMap", ( w,  l, 0))
            plank.corners[Integer("Face Type").equal(LONG_SIDE)].store_uv("UVMap", (dz,  l, 0))
            plank.corners[Integer("Face Type").equal(CUT_SIDE)].store_uv( "UVMap", (dz,  w, 0))
        
        # ---------------------------------------------------------------------------
        # Orientation
        # ---------------------------------------------------------------------------
        
        with Integer.MenuSwitch(menu=Input("Orientation")) as orient:
            Integer(0).out("Horizontal")
            Integer(1).out("Side")
            Integer(2).out("Front")
            Integer(3).out("Vertical")
            
        with Rotation.IndexSwitch(index=orient) as rot:
            Rotation().out()
            Rotation((pi/2, 0, 0)).out()
            Rotation((0, pi/2, 0)).out()
            Rotation((pi/2, 0, pi/2)).out()
            
        plank = plank.transform(rotation=rot)
        
        # ---------------------------------------------------------------------------
        # Add the plank
        # ---------------------------------------------------------------------------
        
        mesh = G().add_plank(mesh, plank, orientation=orient)
        new_id = mesh.comp_id

        # ---------------------------------------------------------------------------
        # Locate
        # ---------------------------------------------------------------------------
        
        node = Group("Locate", mesh = mesh, id = mesh.comp_id, model_id=model_id).link_inputs()
        mesh = node.mesh
        
        # ---------------------------------------------------------------------------
        # Dimensions Cotes
        # ---------------------------------------------------------------------------
        
        with Layout("Dimensions Cotes"):
        
            O = mesh.origin
            S = mesh.size
            
            invert = False
            
            with Float.IndexSwitch(index=orient) as x_dim:
                width.out()
                width.out()
                thickness.out()
                thickness.out()
                
            with Float.IndexSwitch(index=orient) as y_dim:
                length.out()
                thickness.out()
                length.out()
                width.out()

            with Float.IndexSwitch(index=orient) as z_dim:
                thickness.out()
                length.out()
                width.out()
                length.out()
            
            cote = G().cote_line(
                axis        = 0,
                show        = Boolean.IndexSwitch(cote_width, cote_width, cote_thick, cote_thick, index=orient),
                from_       = O,
                to          = O + (x_dim, 0, 0),
                font_size   = FONT_SIZE,
                section     = SECTION,
                invert      = Boolean.IndexSwitch(invert_width, invert_width, invert_thick, invert_thick, index=orient),
                ).link_inputs(None, "Width")
            mesh += cote
            
            cote = G().cote_line(
                axis        = 1,
                show        = Boolean.IndexSwitch(cote_length, cote_thick, cote_length, cote_width, index=orient),
                from_       = O,
                to          = O + (0, y_dim, 0),
                font_size   = FONT_SIZE,
                section     = SECTION,
                invert      = Boolean.IndexSwitch(invert_length, invert_thick, invert_length, invert_width, index=orient),
                ).link_inputs(None, "Length")
            mesh += cote
            
            cote = G().cote_line(
                axis        = 2,
                show        = Boolean.IndexSwitch(cote_thick, cote_length, cote_width, cote_length, index=orient),
                from_       = O,
                to          = O + (0, 0, z_dim),
                font_size   = FONT_SIZE,
                section     = SECTION,
                invert      = Boolean.IndexSwitch(invert_thick, invert_length, invert_width, invert_length, index=orient),
                ).link_inputs(None, "Thickness")
            mesh += cote
            
        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------
        
        if USE_GIZMO:
            with Layout("Dimensions Gizmo"):
                g_pos = O + S
                
                with Vector.IndexSwitch(index=orient) as width_dir:
                    Vector((1, 0, 0)).out()
                    Vector((1, 0, 0)).out()
                    Vector((0, 0, 1)).out()
                    Vector((0, 1, 0)).out()
                    
                with Vector.IndexSwitch(index=orient) as length_dir:
                    Vector((0, 1, 0)).out()
                    Vector((0, 0, 1)).out()
                    Vector((0, 1, 0)).out()
                    Vector((0, 0, 1)).out()
                    
                with Vector.IndexSwitch(index=orient) as thick_dir:
                    Vector((0, 0, 1)).out()
                    Vector((0, 1, 0)).out()
                    Vector((1, 0, 0)).out()
                    Vector((1, 0, 0)).out()
                    
                
                g_vx = w_dict['user_value'].linear_gizmo(position=g_pos, direction=width_dir,  color_id='X', draw_style='ARROW')
                g_vy = l_dict['user_value'].linear_gizmo(position=g_pos, direction=length_dir, color_id='Y', draw_style='ARROW')
                g_vz = t_dict['user_value'].linear_gizmo(position=g_pos, direction=thick_dir,  color_id='Z', draw_style='ARROW')
                
                g_ox = w_dict['offset'].linear_gizmo(position=g_pos, direction=width_dir,  color_id='X', draw_style='BOX')
                g_oy = l_dict['offset'].linear_gizmo(position=g_pos, direction=length_dir, color_id='Y', draw_style='BOX')
                g_oz = t_dict['offset'].linear_gizmo(position=g_pos, direction=thick_dir,  color_id='Z', draw_style='BOX')
        
        mesh.out()
        new_id.out("Comp Id")
        

    # ====================================================================================================
    # Show ID
    # ====================================================================================================

    with GeoNodes("Finalize"):
        
        mesh = Mesh()
        
        with Panel("Cotes", create_layout=True):
            cotes_x = Boolean(True, "Cotes X")
            cotes_y = Boolean(True, "Cotes Y")
            cotes_z = Boolean(True, "Cotes Z")

            cotes  = mesh.points[nd.id == MAX_ID].separate().selection
            planks = cotes.inverted

            cotes = Mesh(cotes.switch_false(cotes_x, Mesh(cotes).points[Integer("Axis").equal(0)].delete()))
            cotes = Mesh(cotes.switch_false(cotes_y, Mesh(cotes).points[Integer("Axis").equal(1)].delete()))
            cotes = Mesh(cotes.switch_false(cotes_z, Mesh(cotes).points[Integer("Axis").equal(2)].delete()))

            mesh = planks + cotes

        with Panel("IDs", create_layout=True):

            show_ids = Boolean(False, "Show")
            ofs = Vector(.2, "Line")
            rot_z = Float.Factor(0., "Direction", -1, 1)*pi
        
            cloud = Group("Cut Sheet", mesh=mesh)._out
        
            for feel in cloud.points.for_each(id=nd.id, pos=nd.position):

                loc = feel.pos + ofs
                line = Curve.Line(feel.pos, loc)
                
                sid = Curve(feel.id.to_string().to_curves(size=.1, align_x='CENTER', align_y='BOTTOM').realize()).fill()
                sid = sid.transform(translation=loc, rotation=(pi/2, 0, rot_z))
                sid = Mesh(sid)
                sid.faces.material = "Label"
                
                (line + sid).out()

            ids = feel.generated.switch_false(show_ids)
            
        (mesh + ids).out()

# ====================================================================================================
# To millimeters
# ====================================================================================================

def to_mm(v):
    return round(v*1000)

# ====================================================================================================
# Cut sheet
# ====================================================================================================

def cut_sheet(name, raw: bool = False):
    
    obj = bpy.data.objects[name]
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj = obj.evaluated_get(depsgraph)
    
    mesh = obj.data
    
    planks = {}
    
    ids    = set()
    
    id_data = mesh.attributes["id"].data
    id_dims = mesh.attributes["Dimensions"].data
    
    # ---------------------------------------------------------------------------
    # Loop in verts, one per Comp Id
    # ---------------------------------------------------------------------------

    for i in range(len(id_data)):
        id = id_data[i].value
        if id in ids:
            continue
        
        ids.add(id)
        
        vec = id_dims[i].vector
        dx, dy, dz = vec
        dx, dy, dz = to_mm(dx), to_mm(dy), to_mm(dz)
        
        if dz not in planks:
            planks[dz] = {'dims': {}, 'surface': 0.0}
            
        cur = planks[dz]
        dims = (dx, dy)
        
        if dims in cur['dims']:
            cur['dims'][dims].append(id)
        else:
            cur['dims'][dims] = [id]

        cur['surface'] += dx*dy
            
    # ---------------------------------------------------------------------------
    # Print the results
    # ---------------------------------------------------------------------------

    print()
    print(f"Decoupe du meuble: {name}")
    print("="*30)
    print()
    print()

    if raw:
        print("Count;Thickness;Width;Length;Comp Ids")

    for thick, dims_surf in planks.items():

        if not raw:
            print(f"Epaisseur {thick} mm - surface : {dims_surf['surface']/1_000_000:.2f} m^2")
            print('-'*30)
            print()
        
        for dims, Comp_Ids in dims_surf['dims'].items():

            if raw:
                print(f"{len(Comp_Ids):2d};{thick};{dims[1]/10:5.1f};{dims[0]/10:5.1f};{Comp_Ids}")
            else:
                print(f"{len(Comp_Ids):2d} : {dims[1]/10:5.1f} X {dims[0]/10:5.1f} cm  | {Comp_Ids}")

        if not raw:
            print()     

       
                
