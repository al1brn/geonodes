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
from .. import Float, Boolean, Integer, Vector, Rotation, Object, Input, Material, Color, Group, String
from .. import repeat

USE_GIZMO = True


# ---------------------------------------------------------------------------
# The Mesh contains the furniture plus additional meshes such as cote lines
# The mesh type is determined by the named attribute "Content"
# ---------------------------------------------------------------------------

IS_COMPONENT = 0x10  # Flag : is a component of the piece of furniture
IS_ACCESSORY = 0x20  # Flag : is an accessory
IS_COTE      = 0x80  # Flag : is a cote line

MASK_TYPE  = 0x0F  # Component type mask 

TYPE_PLANK =  0
TYPE_CLEAT =  1
TYPE_PANEL =  2
TYPE_MESH  = 15

# ---------------------------------------------------------------------------
# Min max dimensions
# ---------------------------------------------------------------------------

MIN_DIM = 0.001 # 1 mm
MAX_DIM = 5.0   # 5 meters
TR_MAX  = 5.0
TR_MIN  = -TR_MAX

TH_MAX = 0.1 # Thickness max 


FREE_WIDTH   = 0x01
FREE_LENGTH  = 0x02
TILABLE      = 0X04

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
# Orientations
# ---------------------------------------------------------------------------

SHELF         = 0
SIDE          = 1
DOOR          = 2
DRAWER        = 3
ROTATED_SHELF = 4
ROTATED_SIDE  = 5

ORIENTATIONS = {
    "Shelf"         : SHELF,
    "Side"          : SIDE,
    "Door"          : DOOR,
    "Drawer"        : DRAWER,
    "Rotated Shelf" : ROTATED_SHELF,
    "Rotated Side"  : ROTATED_SIDE,
}

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
# Rotation from shelf to target orientation
# ----------------------------------------------------------------------------------------------------

def orient_rotation(orient, invert=False):

    rot = Rotation.IndexSwitch(
        (0,     0,      0),
        (pi/2,  0,      0),
        (pi/2,  0,   pi/2),
        (0,    pi/2,    0),
        (0,     0,   pi/2),
        (0,    pi/2, pi/2),
        index=orient,
    )
    if invert:
        return rot.invert()
    else:
        return rot

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
        offset0 = Float.Distance(0.0, "Offset From", TR_MIN, TR_MAX)
        
        comp_id1 = Integer(2, "To Id", 0)
        use_min1 = Boolean(True, f"To Min")
        offset1 = Float.Distance(0.0, "Offset To", TR_MIN, TR_MAX)

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

        custom = Float.Distance(1.0, "Value", MIN_DIM, MAX_DIM)
        offset = Float.Distance(0.0, "Offset", TR_MIN, TR_MAX)

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

        mesh = Mesh()

        # Full (with Aspect)
        mesh.add_method(jump=True)
        # Short (without Aspect)
        mesh.add_method("cote_line", jump=True, font_size=FONT_SIZE, section=SECTION)
        
        show   = Boolean(True,          "Show")
        pos    = Vector.Translation(0,  "Position")
        i_axis = Integer(0,             "Axis", 0, 2)
        value  = Float.Distance(1.0,    "Value", TR_MIN, TR_MAX)
        invert = Boolean(False,         "Invert")

        with Panel("Aspect"):
            font_size  = Float(FONT_SIZE,  "Font Size", 0.01)
            section    = Float(SECTION,    "Section", 0)
        
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
        line.points.Content = IS_COTE
        line.points.Axis = i_axis
        
        line.switch_false(show)

        mesh += line

        mesh.out()

    # ====================================================================================================
    # Base Component
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
        - Free Dims (Integer) : Free dimensions
        """

        input_mesh = Mesh()

        # ---------------------------------------------------------------------------
        # Input
        # ---------------------------------------------------------------------------
        
        comp_type = Integer.MenuSwitch({
            "Plank"    : 0,
            "Cleat"    : 1,
            "Panel"    : 2,
            "Geometry" : 3,
            }, menu = Input("Type")
        )
        with Panel("Tiles"):
            tilable = Boolean(False, "Tilable")
            width_gap  = Float.Distance(0, "Width Gap", -TH_MAX, TH_MAX)
            length_gap = Float.Distance(0, "Length Gap", -TH_MAX, TH_MAX)

        mat = Material(None, "Material")
        #is_custom = comp_type.geometry

        # ---------------------------------------------------------------------------
        # Plank
        # ---------------------------------------------------------------------------

        with Mesh.IndexSwitch(index=comp_type) as component:

            width  = Float.Distance(0.30, "Width",     MIN_DIM, MAX_DIM)
            length = Float.Distance(2.00, "Max Length", MIN_DIM, MAX_DIM)
            thick  = Float.Distance(0.02, "Thickness", MIN_DIM, MAX_DIM)

            dims = Vector((width, length, thick))

            mesh = Mesh.Cube(size=dims)

            mesh.points.Content         = IS_COMPONENT | TYPE_PLANK
            mesh.points.Free_Dims       = FREE_LENGTH | FREE_WIDTH
            mesh.points.Max_Dimensions  = dims
            mesh.points.Dimensions      = dims
            mesh.points.Orientation     = SHELF

            mesh.faces.material         = mat

            mesh.out()

        # ---------------------------------------------------------------------------
        # Cleat
        # ---------------------------------------------------------------------------

        with component:
            width  = Float.Distance(0.05, "Width",     MIN_DIM, MAX_DIM)
            length = Float.Distance(2.00, "Max Length", MIN_DIM, MAX_DIM)
            thick  = Float.Distance(0.05, "Thickness", MIN_DIM, MAX_DIM)

            dims = Vector((width, length, thick))

            mesh = Mesh.Cube(size=dims)

            mesh.points.Content         = IS_COMPONENT | TYPE_CLEAT
            mesh.points.Free_Dims       = FREE_LENGTH
            mesh.points.Max_Dimensions  = dims
            mesh.points.Dimensions      = dims
            mesh.points.Orientation     = SHELF

            mesh.faces.material         = mat

            mesh.out()

        # ---------------------------------------------------------------------------
        # Panel
        # ---------------------------------------------------------------------------

        with component:
            thick   = Float.Distance(0.005, "Thickness", MIN_DIM, MAX_DIM)
            max_dim = Float.Distance(3.0,   "Max Dimension", MIN_DIM, MAX_DIM)

            max_dims = Vector((max_dim, max_dim, thick))
            dims = Vector((1.0, 1.0, thick))

            mesh = Mesh.Cube(size=dims)

            mesh.points.Content         = IS_COMPONENT | TYPE_PANEL
            mesh.points.Free_Dims       = FREE_LENGTH | FREE_WIDTH
            mesh.points.Max_Dimensions  = max_dims
            mesh.points.Dimensions      = dims
            mesh.points.Orientation     = SHELF

            mesh.faces.material         = mat

            mesh.out()

        # ---------------------------------------------------------------------------
        # Input Geometry
        # ---------------------------------------------------------------------------

        with component:

            with Panel("Options"):
                orient = Integer.MenuSwitch(ORIENTATIONS, menu=Input("Orientation"))
                free_width  = Boolean(False, "Free Width")
                free_length = Boolean(False, "Free Length")

            mesh = input_mesh

            node = mesh.points.attribute_statistic(nd.position).node
            sx, sy, sz = (node.max - node.min).xyz

            dims = Vector.IndexSwitch(
                (sx, sy, sz), # Shelf
                (sx, sz, sy), # Side
                (sy, sz, sx), # Door
                (sz, sy, sx), # Drawer
                (sy, sx, sz), # Rotated Shelf
                (sz, sx, sy), # Rotated Side
                index = orient)
            
            free_dims = Integer.Switch(free_width, 0, FREE_WIDTH)
            free_dims.switch(free_length, free_dims | FREE_LENGTH)
            
            mesh.points.Content         = IS_COMPONENT | TYPE_MESH
            mesh.points.Free_Dims       = free_dims
            mesh.points.Max_Dimensions  = dims
            mesh.points.Dimensions      = dims
            mesh.points.Orientation     = orient

            mesh.out()

        # ---------------------------------------------------------------------------
        # Information
        # ---------------------------------------------------------------------------

        with Layout("Dimensions"):
            component = Mesh(component)
            min_pos = component.points.attribute_statistic(nd.position).min_
            component.transform(translation=-min_pos)

        with Layout("Component Information"):
            component.points.Free_Dims = Integer("Free Dims") | tilable
            component.points.Tile_Gap = width_gap + 100*gnmath.round(length_gap*10)
            component.points.Reference = component.points.sample_index(Vector("Dimensions"), index=0).hash_value(seed=comp_type)

        component.out()

    # ====================================================================================================
    # Cut a component
    # ====================================================================================================

    with GeoNodes("Cut"):

        mesh = Mesh()
        mesh.add_method()

        width  = Float.Distance(0.3, "Width",  MIN_DIM, MAX_DIM)
        length = Float.Distance(1.0, "Length", MIN_DIM, MAX_DIM)

        node = mesh.points.attribute_statistic(nd.position).node
        size = node.max - node.min
        sz = size.z

        dims = Vector((width + 0.1, length + 0.1, 3*sz))
        cube = Mesh.Cube(size=dims).transform(translation = node.min + dims.scale(.5) - (0.1, 0.1, sz) )

        mesh.intersect(cube)
        mesh.out()

    # ====================================================================================================
    # Tile a component
    # ====================================================================================================

    with GeoNodes("Create Tiles", is_group=True, prefix=True):

        mesh = Mesh()

        mesh.add_method()

        # ---------------------------------------------------------------------------
        # Input
        # ---------------------------------------------------------------------------

        width_input  = Float.Distance(1.0, "Width",  MIN_DIM, MAX_DIM)
        length_input = Float.Distance(1.0, "Length", MIN_DIM, MAX_DIM)

        orient = Integer(0, "Orientation", 0, 5)

        rot = Rotation.MenuSwitch({
            "Same"                : (0, 0, 0),
            "Upside down"         : (0, 0, pi),
            "Perp. Clockwise"     : (0, 0, pi/2),
            "Perp. Counter Clock" : (0, 0, -pi/2),
        }, menu = Input("Direction"))

        w_gap = Float.Distance(0.0, "Width Gap", -TH_MAX, TH_MAX)
        l_gap = Float.Distance(0.0, "Length Gap", -TH_MAX, TH_MAX)

        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------

        with Layout("Switch target Width / Length"):

            keep_wl = rot.same | rot.upside_down

            width  = Float.Switch(keep_wl, length_input, width_input)
            length = Float.Switch(keep_wl, width_input, length_input)

        with Layout("Plank tile dimensions"):

            node = mesh.points.attribute_statistic(nd.position).node
            mesh.transform(translation=-node.min)
            w, l, _ = (node.max - node.min).xyz

            tile_w = (w + w_gap)._lc("Width Tile")
            tile_l = (l + l_gap)._lc("Length Tile")

        with Layout("Number of tiles"):

            w_count  = gnmath.trunc(width/tile_w)._lc("Count along width")
            l_count  = gnmath.trunc(length/tile_l)._lc("Count along length")

            total = ((w_count + 3)*(l_count + 3))._lc("Max Number of planks")

        # ---------------------------------------------------------------------------
        # Tiling loop
        # ---------------------------------------------------------------------------

        l_min = (0.1*tile_l)._lc("Length Min")
        for rep in repeat(total, tiles=None, x=0.0, y=0.0, remain=tile_l, count=0):

            with Layout("Length Cut"):
                l_cut = gnmath.min(tile_l, gnmath.min(rep.remain, length - rep.y))

            with Layout("Width Cut"):
                x_cut = gnmath.min(tile_w, width - rep.x)

            #cut = mesh.cut(width=x_cut, length=l_cut)
            cut = Mesh(mesh)
            cut.transform(translation=(rep.x, rep.y, 0))

            rep.tiles += cut

            new_y = (rep.y + l_cut)._lc("New Y")
            new_row = new_y.greater_equal(0.999*length)

            rep.y = Float.Switch(new_row, new_y, 0)
            rep.x.switch(new_row, rep.x + tile_w)

            remain = rep.remain - l_cut
            rep.remain = Float.Switch(remain.less_equal(l_min), remain, tile_l)

        tiles = Mesh(rep.tiles)
        tiles = tiles.cut(width, length)

        # ---------------------------------------------------------------------------
        # Rotate to match the required direction
        # ---------------------------------------------------------------------------

        tiles.transform(rotation=rot)

        node = tiles.points.attribute_statistic(nd.position).node
        tiles.transform(translation=-node.min)
        tiles.transform(rotation = orient_rotation(orient))

        tiles.out()

    # ====================================================================================================
    # Component Selector
    # ====================================================================================================

    with GeoNodes("Selector", is_group=True, prefix=utils):

        comp_id  = Integer(0,     "Comp Id", 0)
        linked   = Boolean(False, "Linked")
        with_acc = Boolean(False, "Accessories")

        is_comp = (Integer("Content") & IS_COMPONENT).not_equal(0)
        is_acc  = (Integer("Content") & IS_ACCESSORY).not_equal(0) & with_acc

        comp_sel   = Integer("Comp Id").equal(comp_id)
        linked_sel = Integer("Owner Id").equal(comp_id)

        sel = comp_sel | (linked_sel & linked)
        acc_sel = linked_sel & is_acc

        ((sel & is_comp) | acc_sel).out("Selection")
        (sel.bnot() & is_comp).out("Invert")
        is_comp.out("All")

    # ====================================================================================================
    # Plank location and size
    # ====================================================================================================

    with GeoNodes("Get Location and Size", is_group=True, prefix=utils):

        mesh = Mesh()
        sel  = Boolean(False, "Selection", hide_value=True)

        sel &= (Integer("Content") & IS_COMPONENT).not_equal(0)

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

        # Remove what is not a component
        comp_only = Mesh(comp).points[(Integer("Content") & IS_COMPONENT).equal(0)].delete()

        max_dims  = comp_only.points.sample_index(Vector("Max Dimensions"), index=0)
        dims      = comp_only.points.sample_index(Vector("Dimensions"), index=0)
        free_dims = comp_only.points.sample_index(Integer("Free Dims"), index=0)
        orient    = comp_only.points.sample_index(Integer("Orientation"), index=0)
        content   = comp_only.points.sample_index(Integer("Content"), index=0)
        tile_gap  = comp_only.points.sample_index(Float("Tile Gap"), index=0)

        loc_size = utils.get_location_and_size(comp_only, True).node

        comp.out("Mesh")

        loc_size.out()
        max_dims.out("Max Dimensions")
        dims.out("Dimensions")
        orient.out("Orientation")
        content.out("Content")

        (free_dims & FREE_WIDTH).not_equal(0).out("Free Width")
        (free_dims & FREE_LENGTH).not_equal(0).out("Free Length")
        (free_dims & TILABLE).not_equal(0).out("Tilable")
        (tile_gap % 100).out("Width Gap")
        (gnmath.round(tile_gap / 100)/10).out("Length Gap")

        masked = content & MASK_TYPE
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


        with stock:
            obj = Object(None, "Base Material")
            mesh = Mesh(obj.info().geometry)

            mesh.out("True")

        stock = Mesh(stock).extract(True).node
        stock.out()

    # ====================================================================================================
    # Count the number of components
    # ====================================================================================================

    with GeoNodes("Components Count", is_group = True, prefix=utils):

        mesh = Mesh()

        # As Mesh method
        mesh.add_method()

        max_id = mesh.points.attribute_statistic(Float(Integer("Comp Id"))).max_.to_integer()
        count = mesh.points.attribute_statistic(Float(Integer("Single"))).sum.to_integer()

        count.out("Count")
        max_id.out("Max Id")


    # ====================================================================================================
    # Identifiers
    # ====================================================================================================

    with GeoNodes("Identifiers"):
        """ Return a cloud of points, one per component
        """

        mesh = Mesh()

        # As Mesh method
        mesh.add_method()

        # Max Id
        max_id = mesh.components_count().max_id

        cloud = mesh.points[Integer("Single").equal(0)].delete().to_points()

        count = cloud.points.count

        cloud.out("Cloud")
        count.out("Count")
        max_id.out("Max Id")


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
        - Single (Integer) : First vertex flag (1 for the first vertex, 0 for the other ones)
        """
        
        mesh = Mesh()
        comp = Mesh(name = "Component")
        join = Boolean(True, "Join")

        # As Mesh method
        mesh.add_method(jump=True)

        max_id = mesh.points.attribute_statistic(Float(Integer("Comp Id"))).max_.to_integer()
        
        comp_id = max_id + 1

        comp.points.Content = Integer("Content") | IS_COMPONENT
        comp.points.Comp_Id = comp_id
        comp.faces.Face_Random = Float.Random(0, 1, seed=comp_id)

        # Use to keep one point per component
        comp.points.Single = Integer.Switch(nd.index.equal(0), 0, 1)

        mesh.switch(join, mesh + comp)

        mesh.out("Mesh")
        comp_id.switch_false(join).out("Comp Id")

        show_id = Boolean(True, "Display Id", hide_in_modifier=True)
        Boolean(show_id & join).info("Id " + comp_id.to_string())

    # ====================================================================================================
    # Join a Block
    # ====================================================================================================

    with GeoNodes("Join Block", is_group=True, prefix=utils):
        """ Add a block of components to the furniture

        Shift the "Comp Id" and "Owner Id" attributes to avoid duplicates in the resulting furniture.

        Named Attributes
        ----------------
        - Comp Id (Integer) : max of the existing ids + 1
        - Owner Id (Integer) : Ensure flag CONTENT PART is set to "Content" named attribute
        """
        
        mesh  = Mesh()
        block = Mesh(name = "Block")

        # As Mesh method
        mesh.add_method(jump=True)

        max_id = mesh.components_count().max_id

        with Layout("Block new ids"):

            idents = block.identifiers()
            count = idents.count

            for rep in repeat(count, cloud=idents, block=block, cur_id=max_id):

                cid = Integer("Comp Id")
                comp_id = rep.cloud.points.sample_index(cid, index=rep.iteration)

                sel = cid.equal(comp_id)
                new_id = rep.cur_id + 1

                rep.cloud.points[sel].New_Id = new_id

                block = Mesh(rep.block)
                block.points[sel].Comp_Id = new_id

                rep.block = block
                rep.cur_id = new_id

            idents = rep.cloud
            block = Mesh(rep.block)
            max_id = rep.cur_id


        with Layout("Update Owner Id"):
            for rep in repeat(count, block=block):

                oid = Integer("Owner Id")
                owner_id = idents.points.sample_index(oid, index=rep.iteration)
                new_owner = idents.points[Integer("Comp Id").equal(owner_id)].attribute_statistic(Float(Integer("New Id"))).sum.to_integer()

                sel = oid.not_equal(0) & oid.equal(owner_id)

                block = Mesh(rep.block)
                block.points[sel].Owner_Id = new_owner

                rep.block = block

            block = rep.block

        mesh += block
        mesh.out()
        max_id.out("Max Id")

    # ====================================================================================================
    # Join an accessory
    # ====================================================================================================

    with GeoNodes("Join Accessory"):

        mesh    = Mesh()
        comp_id = Integer(0, "Comp Id")
        acc_obj = Object(None, "Accessory")
        rel_pos = Vector.Factor((.5, .5, .5), "Position", 0, 1)
        ofs     = Vector(0, "Offset")

        mesh.add_method(jump=True)

        comp = mesh.extract(utils.selector(comp_id))
        pos = comp.min + comp.size*rel_pos + ofs

        acc = Mesh(acc_obj.info().geometry)
        acc.points.Owner_Id = comp_id
        acc.points.Content = IS_ACCESSORY
        acc.points.offset = pos

        mesh += acc

        mesh.out()


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

        with Layout("Model Info"):
            model_info = comp.extract(True).node
            width, length, _ = dims.xyz
            width._ul("Model Width")
            length._ul("Model Length")

        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------

        with Layout("Scale to the required dimensions"):

            max_width, max_length, thickness = model_info.max_dimensions.xyz

            width.switch_false(model_info.free_width, max_width)
            width = gnmath.min(width, max_width)

            length.switch_false(model_info.free_length, max_length)
            length = gnmath.min(length, max_length)

            dims = Vector((width, length, thickness))

            rot = orient_rotation(model_info.orientation, invert=True)
            comp.transform(rotation=rot)

            comp.transform(scale=dims/model_info.dimensions)
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

            comp.corners[Integer("Face Type").equal(FACE)].store_uv(     "Dims", ( w,  l, 0))
            comp.corners[Integer("Face Type").equal(LONG_SIDE)].store_uv("Dims", (dz,  l, 0))
            comp.corners[Integer("Face Type").equal(CUT_SIDE)].store_uv( "Dims", (dz,  w, 0))

        # ---------------------------------------------------------------------------
        # Orientation
        # ---------------------------------------------------------------------------

        with Layout("Set Orientation"):
            comp.points.Orientation = orient

            rot = orient_rotation(orient)
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
                    mesh.cote_line(
                        show     = Input(f"{axis} Dimension", default=False),
                        position = comp.min,
                        axis     = i_axis, 
                        value   = size_xyz[i_axis],
                        cote_offset_a = Float(0, "Dimension Offset A", hide_in_modifier=True),
                        cote_offset_b = Float(0, "Dimension Offset B", hide_in_modifier=True),
                    )
                    node0 = mesh.node

                    mesh.cote_line(
                        show     = Input(f"{axis} Position", default=False),
                        position = 0,
                        axis     = i_axis,
                        value    = min_xyz[i_axis],
                        cote_offset_a = Float(0, "Position Offset A", hide_in_modifier=True),
                        cote_offset_b = Float(0, "Position Offset B", hide_in_modifier=True),
                    )
                    node1 = mesh.node

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
                    user_value = Float.Distance(0.0, "Value", TR_MIN, TR_MAX)

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
                    mesh.cote_line(show=show_cotes[i], position=pos, axis=i, value=cote_len[i], invert=inverts[i]).link_inputs() 

        mesh.out()

    
    # ====================================================================================================
    # Main modifier : add a component
    # ====================================================================================================

    with GeoNodes("Add Component"):

        mesh = Mesh()

        with Panel("Model", create_layout=True):
            
            model = utils.component_input(mesh).link_inputs(None)
            fixed_width  = model.free_width.bnot()
            fixed_length = model.free_length.bnot()

            orient = Integer.MenuSwitch(ORIENTATIONS, menu=Input("Orientation"))

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
                tiled_length = length

                length = gnmath.min(length, max_length)
                length.switch(fixed_length, max_length)

            # ---------------------------------------------------------------------------
            # Width
            # ---------------------------------------------------------------------------

            with Panel("Width"):
                width_axis = Integer.IndexSwitch(0, 0, 1, 2, 1, 2, index=orient)
                w_dict = get_dimension(mesh, "Width", i_axis=width_axis, same_value=width, color="orangered")
                width = w_dict['value']
                tiled_width = width

                width = gnmath.min(width, max_width)
                width.switch(fixed_width, max_width)

            # ---------------------------------------------------------------------------
            # Tiles
            # ---------------------------------------------------------------------------

            with Panel("Tiles"):
                use_tiles = Boolean(False, "Tiles")
                tiles = model.create_tiles(
                    width       = tiled_width,
                    length      = tiled_length, 
                    orientation = orient,
                    width_gap   = info.width_gap,
                    length_gap  = info.length_gap,
                    ).link_inputs()

        # ---------------------------------------------------------------------------
        # Create the component at (0, 0, 0)
        # ---------------------------------------------------------------------------

        with Layout("Create the component"):
            comp = model.create_from_model(dimensions=(width, length, thickness), orientation=orient)
            comp.switch(use_tiles, tiles)

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

        show = Boolean(True, "Show")
        i_axis = Integer.MenuSwitch({"X": 0, "Y": 1, "Z": 2}, menu=Input("Axis"))

        from_id = Integer(1, "Id", panel="From")
        to_id = Integer(1, "Id", panel="To")

        v0 = mesh.get_component_position(utils.selector(from_id), axis=i_axis).link_inputs(None, "From")
        v1 = mesh.get_component_position(utils.selector(to_id), axis=i_axis).link_inputs(None, "To")

        x, y, z = mesh.extract(from_id).center.xyz

        mesh.add_cote_line(
            position = Vector.IndexSwitch((v0, y, z), (x, v0, z), (x, y, v0), index=i_axis),
            axis     = i_axis, 
            value    = v1 - v0,
        ).link_inputs()

        mesh.out()

    # ====================================================================================================
    # Duplicate a component
    # ====================================================================================================

    with GeoNodes("Duplicate Component"):

        mesh     = Mesh()
        comp_sel = utils.selector().link_inputs()
        count    = Integer(1, "Count", 0, 10)

        mesh.add_method(jump=True)

        transl      = [0]*3
        #change      = [False]*3
        show_cote   = [False]*3
        dist_cote   = [False]*3
        invert_cote = [False]*3 

        for i_axis in range(3):
            axis = 'XYZ'[i_axis]
            
            with Panel(axis):
                #change[i_axis] = Boolean(False, f"Translate {axis}")
                transl[i_axis] = Float.Distance(0.0, f"Offset {axis}", TR_MIN, TR_MAX)
                show_cote[i_axis] = Boolean(False, "Cote")
                dist_cote[i_axis] = Boolean(True, "Distance")
                invert_cote[i_axis] = Boolean(False, "Invert")

            # 0 if no change
            #transl[i_axis].switch_false(change[i_axis])

        with Layout("Gizmo"):

            components = mesh.extract(comp_sel)

            O = components.center + transl

            transl[0].linear_gizmo(position = O, direction=(1, 0, 0), color_id='X')
            transl[1].linear_gizmo(position = O, direction=(0, 1, 0), color_id='Y')
            transl[2].linear_gizmo(position = O, direction=(0, 0, 1), color_id='Z')

        # ----------------------------------------------------------------------------------------------------
        # Duplicate count times
        # ----------------------------------------------------------------------------------------------------

        with Layout("Join count times"):

            for rep in repeat(count, mesh=mesh, comp=components, max_id=0):

                comp = rep.comp
                comp.transform(translation=transl)
                rep.comp = comp

                rep.mesh.join_block(comp)
                rep.max_id = rep.mesh.max_id

            mesh = rep.mesh
            max_id = rep.max_id

        # ---------------------------------------------------------------------------
        # Cotes
        # ---------------------------------------------------------------------------

        with Layout("Dimensions"):
            center_xyz = components.center.xyz
            min_xyz    = components.min.xyz
            max_xyz    = components.max.xyz
            size_xyz   = components.size.xyz

        for i_axis in range(3):

            axis = "XYZ"[i_axis]
            dist = transl[i_axis]

            negative = dist.less_than(0)

            pos = list(center_xyz)
            pos[i_axis] = Float.Switch(negative, max_xyz[i_axis], min_xyz[i_axis])
            dist.switch(dist_cote[i_axis], Float.Switch(negative, dist - size_xyz[i_axis], dist + size_xyz[i_axis]))

            mesh.add_cote_line(
                position = pos,
                axis     = i_axis, 
                value    = dist,
                show        = show_cote[i_axis],
                invert      = invert_cote[i_axis],
                ).link_inputs(None, axis, exclude=["Aspect"])

        mesh.out()
        comp_sel.out("Selection")
        max_id.out("Max Id")

    # ====================================================================================================
    # Rotate a Component
    # ====================================================================================================

    with GeoNodes("Rotate Component"):

        mesh     = Mesh()
        comp_sel = utils.selector().link_inputs()
        i_axis   = Integer(0, "Axis", 0, 2)

        with Panel("Pivot", create_layout=True):

            comp_dims = mesh.extract(comp_sel)

            a = []
            for i in range(3):
                with Panel("XYZ"[i]):

                    # Selector as first UI
                    i_sel = Integer.MenuSwitch({
                        "Value"     : 0,
                        "Component" : 1,
                        "Other"     : 2,
                        },
                    menu = Input("Position")
                    )
                    pid      = Integer(0, "Other Id")
                    value    = Float.Distance(0.0, "Value", TR_MIN, TR_MAX)
                    fraction = Float.Factor(0.5, "Fraction", 0, 1)

                    # Fraction of component
                    v0 = comp_dims.min.xyz[i]
                    v1 = comp_dims.max.xyz[i]

                    comp_ref = fraction.map_range(to_min=v0, to_max=v1, interpolation_type="Linear")

                    # Fraction of other component
                    other_dims = mesh.extract(utils.selector(pid))
                    v0 = other_dims.min.xyz[i]
                    v1 = other_dims.max.xyz[i]

                    other_ref = fraction.map_range(to_min=v0, to_max=v1, interpolation_type="Linear")

                    # Final
                    a.append(Float.IndexSwitch(0.0, comp_ref, other_ref, index=i_sel) + value)

            O = comp_dims.center.xyz
            pivot = Vector.IndexSwitch((O[0], a[1], a[2]), (a[0], O[1], a[2]), (a[0], a[1], O[2]), index=i_axis)._lc("Pivot")

        with Panel("Angle"):
            angle   = Float.Angle(0, "Angle")
            ag_min  = Float.Angle(-pi/2, "Min")
            ag_max  = Float.Angle(pi/2, "Max")

            clip_angle = gnmath.min(gnmath.max(ag_min, angle), ag_max)

        with Layout("Rotation"):
            rot = Rotation.IndexSwitch((clip_angle, 0, 0), (0, clip_angle, 0), (0, 0, clip_angle), index=i_axis)

            p = pivot + (rot @ (nd.position - pivot))

            pid = Integer("Comp Id")
            mesh[comp_sel].position = p

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        angle.dial_gizmo(
            position = pivot,
            up = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
        )

        mesh.out()
        comp_sel.out("Selection")

    # ====================================================================================================
    # Translate a Plank
    # ====================================================================================================

    with GeoNodes("Translate Component"):

        mesh     = Mesh()
        comp_sel = utils.selector().link_inputs()
        i_axis   = Integer(0, "Axis", 0, 2)

        with Panel("Value"):
            value    = Float.Distance( 0.0, "Value", TR_MIN, TR_MAX)
            val_min  = Float.Distance(-1.0, "Min", TR_MIN, TR_MAX)
            val_max  = Float.Distance( 1.0, "Max", TR_MIN, TR_MAX)

            clip_value = gnmath.min(gnmath.max(val_min, value), val_max)

        with Layout("Vector Offset"):
            trans = Vector.IndexSwitch((clip_value, 0, 0), (0, clip_value, 0), (0, 0, clip_value), index=i_axis)
            mesh[comp_sel].offset = trans

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        with Layout("Gizmo"):

            dims = mesh.extract(comp_sel)

            value.linear_gizmo(
                position = dims.center,
                direction = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
            )

        mesh.out()
        comp_sel.out("Selection")

    # ====================================================================================================
    # Select a box
    # ====================================================================================================

    with GeoNodes("Box Input", is_group=True, prefix=utils):

        mesh = Mesh()
        mesh.add_method()

        comp_ids = [0]*4
        comps    = [None]*4
        has_ids  = [False]*4

        names = ("Left", "Right", "Bottom", "Top")

        with Panel("Bounding Box"):
            x0 = 1000
            x1 = 0
            for i, name in enumerate(names):
                comp_ids[i] = Integer(0, name)
                comps[i]    = mesh.extract(utils.selector(comp_ids[i]))
                has_ids[i]  = comp_ids[i].not_equal(0)

                x0 = Float.Switch(has_ids[i], x0, gnmath.min(x0, comps[i].min.x))
                x1 = Float.Switch(has_ids[i], x1, gnmath.max(x1, comps[i].max.x))

        comps[0].max.y.out("Left")
        comps[1].min.y.out("Right")
        comps[2].max.z.out("Bottom")
        comps[3].min.z.out("Top")
        x0.out("x0")
        x1.out("x1")

        for has_id, name in zip(has_ids, names):
            has_id.out(f"Has {name}")

        for comp_id, name in zip(comp_ids, names):
            comp_id.out(f"{name} Id")

    # ====================================================================================================
    # Shelf
    # ====================================================================================================

    with GeoNodes("Shelf"):
        
        mesh = Mesh()

        model = utils.component_input(mesh).link_inputs()
        count = Integer(1, "Count", 1)

        box = mesh.box_input().link_inputs()

        z = Float.Distance(.1, "Height", MIN_DIM, MAX_DIM)
        setback0 = Float.Distance(0.0,  "Back Setback", 0, TH_MAX)
        setback1 = Float.Distance(0.02, "Front Setback", 0, TH_MAX)

        pos  = Vector((box.x0 + setback0, box.left, box.bottom + z))
        dims = Vector((box.x1 - box.x0 - setback0 - setback1, box.right - box.left, model.dimensions.z))

        # Gizmo
        z.linear_gizmo(position = pos + dims/2, direction=(0, 0, 1), color_id='Z', draw_style='ARROW')

        new_comp = model.create_from_model(
            position    = pos,
            dimensions  = dims,
            orientation = SHELF,
        )

        mesh.join_component(new_comp)
        comp_id = mesh.comp_id

        # Cote
        mesh.cote_line(
            show     = Boolean(False, "Cote"),
            position = pos + (dims.x/2, dims.y/2, -z),
            axis     = 2,
            value    = z,
            invert   = Boolean(False, "Invert"),
            ).link_inputs()

        # ---------------------------------------------------------------------------
        # Other shelves
        # ---------------------------------------------------------------------------

        shelf = mesh.extract(utils.selector(comp_id))
        for rep in repeat(count-1, mesh=mesh):

            shelf.transform(translation=(0, 0, (rep.iteration+1)*z))
            shelf.points.Owner_Id = comp_id

            rep.mesh.join_component(shelf)

        mesh = rep.mesh

        mesh.out()
        comp_id.out("Comp Id")

    # ====================================================================================================
    # Plinth
    # ====================================================================================================

    with GeoNodes("Plinth"):
        
        mesh = Mesh()

        model = utils.component_input(mesh).link_inputs()
        thick = model.dimensions.z

        comp_id = Integer(0, "Under Id")
        comp = mesh.extract(utils.selector(comp_id))

        sel_index = Integer.MenuSwitch({"Front": 0, "Left": 1, "Right": 2}, menu=Input("Location"))

        setback = Float.Distance(0.02, "Setback", 0, TH_MAX)        
        ofs0    = Float.Distance(0.0, "Offset Start", -TH_MAX, TH_MAX)
        ofs1    = Float.Distance(0.0, "Offset End", -TH_MAX, TH_MAX)

        # ---------------------------------------------------------------------------
        # Position
        # ---------------------------------------------------------------------------

        with Vector.IndexSwitch(index=sel_index) as pos:
            Vector((comp.max.x - setback - thick, comp.min.y + ofs0, 0)).out()

        with pos:
            Vector((comp.min.x + ofs0, comp.min.y + setback, 0)).out()

        with pos:
            Vector((comp.min.x + ofs0, comp.max.y - setback - thick, 0)).out()

        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------

        with Vector.Switch(sel_index.front) as dims:
            Vector((comp.min.z, comp.size.y - ofs0 - ofs1, thick)).out("True")

        with dims:
            Vector((comp.min.z, comp.size.x - ofs0 - ofs1, thick)).out("False")

        # ---------------------------------------------------------------------------
        # Plinth
        # ---------------------------------------------------------------------------

        plinth = model.create_from_model(
            position    = pos,
            dimensions  = dims,
            orientation = Integer.Switch(sel_index.front, ROTATED_SIDE, DRAWER),
        )
        mesh.join_component(plinth)

        # Cote
        dx, dy, dz = dims.xyz
        mesh.cote_line(
            show     = Boolean(False, "Cote"),
            position = pos + Vector.Switch(sel_index.front, (dx/2, 0, 0), (dx, dy/2, 0)),
            axis     = 2,
            value    = dx,
            invert   = Boolean(False, "Invert"),
            ).link_inputs()

        mesh.out()

    # ====================================================================================================
    # Hinge
    # ====================================================================================================

    with GeoNodes("Hinge"):

        mesh = Mesh()

        mesh.add_method()

        comp_id = Integer(0, "Comp Id")
        i_axis  = Integer.MenuSwitch({"X": 0, "Y": 1, "Z": 2}, menu=Input("Axis"), default_menu="Z")

        comp_sel = utils.selector(comp_id, linked=True, accessories=True)
        comp = mesh.extract(comp_sel)
        min_xyz = comp.min.xyz
        max_xyz = comp.max.xyz
        O_xyz = comp.center.xyz


        facs = [0]*3
        pos = [0]*3

        for i in range(3):
            axis = 'XYZ'[i]
            facs[i] = Float.Factor(0, f"{axis} Position", 0, 1)
            pos[i] = facs[i].map_range(to_min=min_xyz[i], to_max=max_xyz[i], interpolation_type='Linear')

        angle = Float.Angle(0.0, "Angle", -pi, pi)
        angle0 = Float.Angle(-pi, "Angle Min", -2*pi, 2*pi)
        angle1 = Float.Angle( pi, "Angle Max", -2*pi, 2*pi)

        pivot = Vector.IndexSwitch(
            (O_xyz[0], pos[1], pos[2]),
            (pos[0], O_xyz[1], pos[2]),
            (pos[0], pos[1], O_xyz[2]),
            index=i_axis,
        )

        # Gizmo
        angle.dial_gizmo(
            position = pivot,
            up = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
        )

        # Clamp
        angle = angle.clamp_minmax(angle0, angle1)

        rot = Rotation.IndexSwitch((angle, 0, 0), (0, angle, 0), (0, 0, angle), index=i_axis)
        
        mesh.points[comp_sel].position = pivot + rot @ (nd.position - pivot)


        mesh.out()

    # ====================================================================================================
    # Door
    # ====================================================================================================

    with GeoNodes("Door"):
        
        mesh = Mesh()

        # Box
        box = mesh.box_input().link_inputs()

        # Component model
        with Panel("Model"):
            model =  utils.component_input(mesh).link_inputs()
            thick = model.dimensions.z

        # Options
        with Panel("Door"):

            hinge_loc = Integer.MenuSwitch({
                "Single Left"  : 0,
                "Single Right" : 1,
                "Double"       : 2,
                "Bottom"       : 3,
                "Top"          : 4,
                }, menu=Input("Hinge"))

            inside = Boolean(True,  "Inside")

            gap  = Float.Distance(0.002, "Gap", 0, TH_MAX)
            over = Float.Distance(0.007, "Over", 0, TH_MAX)

            left_open  = Float.Angle(0, "Left Open")
            right_open = Float.Angle(0, "Right Open")
            bot_open   = Float.Angle(0, "Bottom Open")
            top_open   = Float.Angle(0, "Top Open")

        with Layout("Dimensions"):
            height = box.top - box.bottom
            height = Float.Switch(inside, height + 2*over, height - 2*gap)
            
            width = box.right - box.left
            width = Float.Switch(inside, width + 2*over, width - 2*gap)

            left_width = Float.Switch(hinge_loc.double, width, (width - gap)/2)
        
        # ---------------------------------------------------------------------------
        # Left Door
        # ---------------------------------------------------------------------------

        with Layout("Left Door"):
        
            left_pos = Vector.Switch(inside,
                    (box.x1, box.left - over, box.bottom - over),
                    (box.x1 - thick, box.left + gap, box.bottom + gap),
                    )
            
            dims = (left_width, height, thick)

            left_door = model.create_from_model(
                position    = left_pos,
                dimensions  = dims,
                orientation = DOOR,
            )
            mesh.join_component(left_door)
            left_id = mesh.comp_id

        # ---------------------------------------------------------------------------
        # Right Door
        # ---------------------------------------------------------------------------

        with Layout("Right Door"):

            right_pos = left_pos + (0, left_width + gap, 0)
            right_door = model.create_from_model(
                position    = right_pos,
                dimensions  = dims,
                orientation = DOOR,
            )
            mesh.join_component(right_door, join=hinge_loc.double)
            right_id = mesh.comp_id

        # ---------------------------------------------------------------------------
        # Hinges
        # ---------------------------------------------------------------------------

        with Layout("Hinges"):

            mesh1 = mesh.hinge(
                comp_id = left_id, 
                axis='Z',
                x_position = Integer.Switch(inside, 0, 1),
                y_position = 0,
                angle = -left_open,
                angle_min = -pi,
                angle_max = 0,
            )
            mesh.switch(hinge_loc.single_left | hinge_loc.double, mesh1)

            mesh1 = mesh.hinge(
                comp_id = Integer.Switch(hinge_loc.double, left_id, right_id),
                axis='Z',
                x_position = Integer.Switch(inside, 0, 1),
                y_position = 1,
                angle = right_open,
                angle_min = 0,
                angle_max = pi,
            )
            mesh.switch(hinge_loc.single_right | hinge_loc.double, mesh1)

            mesh1 = mesh.hinge(
                comp_id = left_id, 
                axis='Y',
                x_position = Integer.Switch(inside, 0, 1),
                z_position = 0,
                angle = bot_open,
                angle_min = 0,
                angle_max = pi,
            )
            mesh.switch(hinge_loc.bottom, mesh1)

            mesh1 = mesh.hinge(
                comp_id = left_id, 
                axis='Y',
                x_position = Integer.Switch(inside, 0, 1),
                z_position = 1,
                angle = -top_open,
                angle_min = -pi,
                angle_max = 0,
            )
            mesh.switch(hinge_loc.top, mesh1)

        mesh.out()
        left_id.out("Comp Id")
        hinge_loc.double.out("Double")
        right_id.out("Right Id")

    # ====================================================================================================
    # Drawer
    # ====================================================================================================

    with GeoNodes("Drawer"):

        mesh = Mesh()

        # ----------------------------------------------------------------------------------------------------
        # Inputs
        # ----------------------------------------------------------------------------------------------------

        with Panel("Count"):
            dupl_count = Integer(1, "Count", 1, 10)
            dupl_vert  = Boolean(True, "Vertical")
            dupl_tr    = Float.Distance(0, "Gap", TR_MIN, TR_MAX)

        # Box
        box = mesh.box_input().link_inputs()

        # Component models
        with Panel("Front", create_layout=True):
            front_model =  utils.component_input(mesh).link_inputs()
            front_thick = front_model.dimensions.z._lc("Front Thickness")

            inside = Boolean(True,  "Inside")

            gap  = Float.Distance(0.002, "Gap", 0, TH_MAX)
            over = Float.Distance(0.007, "Over", 0, TH_MAX)

            open = Float.Distance(0.0, "Open", 0, TR_MAX)

            with Panel("Handle"):
                handle_obj = Object(None, "Handle")
                handle_pos = Float.Factor(.5, "Height", 0, 1)

        with Panel("Box Sides", create_layout=True):
            side_model =  utils.component_input(mesh).link_inputs()
            side_thick = side_model.dimensions.z._lc("Side Thickness")

            use_box_front = Boolean(True, "Front Panel")
            side_fix_index = Integer.MenuSwitch({
                "Side Nails"  : 0,
                "45° Shear"   : 1,
                "Front Nails" : 2,
            }, menu=Input("Fixation"))

            side_nails  = side_fix_index.side_nails
            front_nails = side_fix_index.front_nails

            rear_setback = Float.Distance(0.01, "Rear SetBack", 0, TH_MAX)
            side_setback = Float.Distance(0.13, "Side SetBack", 0, TH_MAX)
            bot_setback  = Float.Distance(0.05, "Bottom Setback", 0, TH_MAX)
            top_setback  = Float.Distance(0.02, "Top Setback", 0, TH_MAX)

        with Panel("Bottom Panel Options", create_layout=True):
            bot_model =  utils.component_input(mesh).link_inputs()
            bot_thick = bot_model.dimensions.z._lc("Bottom Thickness")

            bot_fix_index = Integer.MenuSwitch({
                "Groove"       : 0,
                "Rabbet"       : 1,
                "Nailed Underneath" : 2,
            }, menu=Input("Fixation"))
            underneath = bot_fix_index.nailed_underneath

            groove = Float.Distance(0.005, "Grove/Rabbet", MIN_DIM, TH_MAX)
            groove_setback = Float.Distance(0.005, "Groove Setback", MIN_DIM, TH_MAX)
            # 0 if nailed underneath
            groove_setback.switch_false(bot_fix_index.groove)

        # ----------------------------------------------------------------------------------------------------
        # Create the front panel
        # ----------------------------------------------------------------------------------------------------

        with Layout("Front Dimensions"):
            front_height = box.top - box.bottom
            front_height = Float.Switch(inside, front_height + 2*over, front_height - 2*gap)._ul("Front Height")
            
            front_width = box.right - box.left
            front_width = Float.Switch(inside, front_width + 2*over, front_width - 2*gap)._ul("Front Width")
        
        with Layout("Front"):
        
            front_pos = Vector.Switch(inside,
                    (box.x1, box.left - over, box.bottom - over),
                    (box.x1 - front_thick, box.left + gap, box.bottom + gap),
                    )
            
            # Drawer orientation
            front_dims = (front_height, front_width, front_thick)

            front = front_model.create_from_model(
                position    = front_pos,
                dimensions  = front_dims,
                orientation = DRAWER,
            )
            mesh.join_component(front)
            front_id = mesh.comp_id

            open.linear_gizmo(position=front_pos + (front_thick + open, front_width/2, front_height/2), direction=(1, 0, 0), color_id='PRIMARY', draw_style='ARROW')

        # ----------------------------------------------------------------------------------------------------
        # Create the box
        # ----------------------------------------------------------------------------------------------------

        with Layout("Box dimensions and positions"):

            with Layout("Box min max"):
                box_min = [box.x0 + rear_setback, box.left + side_setback, box.bottom + bot_setback]
                box_max = [front_pos.x, box.right - side_setback, box.top - top_setback]
                for i in range(3):
                    box_min[i]._lc(f"Box Min {'XYZ'[i]}")
                    box_max[i]._lc(f"Box Max {'XYZ'[i]}")

                box_depth  = (box_max[0] - box_min[0])._ul("Box Depth")
                box_width  = (box_max[1] - box_min[1])._ul("Box Width")
                #box_height = (box_max[2] - box_min[2])._ul("Box Height")

            with Layout("Side z min"):
                side_z = Float.Switch(underneath, box_min[2], box_min[2] + bot_thick)._lc("Side Z0")
                side_height = (box_max[2] - side_z)._ul("Side Height")

            with Layout("Left Side Dims and Pos"):
                lr_length = Float.Switch(front_nails, box_depth, box_depth - side_thick)._ul("Left/Right Length")
                lr_length.switch(front_nails & use_box_front, lr_length - side_thick)

                left_pos = Vector((
                    Float.Switch(front_nails, box_min[0], box_min[0] + side_thick),
                    box_min[1],
                    side_z,
                ))._lc("Left Side Pos")

            with Layout("Rear Side Dims and Pos"):
                rf_length = Float.Switch(side_nails, box_width, box_width - 2*side_thick)._ul("Rear/Front Length")

                rear_pos = Vector((
                    box_min[0],
                    Float.Switch(side_nails, box_min[1], box_min[1] + side_thick),
                    side_z
                ))._lc("Rear Side Pos")

        with Layout("Left Side"):

            left_side = side_model.create_from_model(
                position    = left_pos,
                dimensions  = (side_height, lr_length, side_thick),
                orientation = ROTATED_SIDE,
            )
            left_side.points.Owner_Id = front_id
            mesh.join_component(left_side)
            left_id = mesh.comp_id

        with Layout("Right Side"):

            right_side = side_model.create_from_model(
                position    = left_pos + (0, box_width - side_thick, 0),
                dimensions  = (side_height, lr_length, side_thick),
                orientation = ROTATED_SIDE,
            )
            right_side.points.Owner_Id = front_id
            mesh.join_component(right_side)
            right_id = mesh.comp_id

        with Layout("Rear Side"):

            rear_side = side_model.create_from_model(
                position    = rear_pos,
                dimensions  = (side_height, rf_length, side_thick),
                orientation = DRAWER,
            )
            rear_side.points.Owner_Id = front_id
            mesh.join_component(rear_side)
            rear_id = mesh.comp_id

        with Layout("Optional Front Side"):

            frt_side = side_model.create_from_model(
                position    = rear_pos + (box_depth - side_thick, 0, 0),
                dimensions  = (side_height, rf_length, side_thick),
                orientation = DRAWER,
            )
            frt_side.points.Owner_Id = front_id
            mesh.join_component(frt_side, join=use_box_front)
            frt_id = mesh.comp_id

        # ----------------------------------------------------------------------------------------------------
        # Bottom panel
        # ----------------------------------------------------------------------------------------------------

        with Layout("Bottom Panel Dimensions"):

            hrz_ofs   = Float.Switch(underneath, side_thick - groove, 0.0)._ul("Groove Hrz Offset")
            bot_width = Float.Switch(underneath, box_width - 2*hrz_ofs, box_width)._ul("Bottom Width")

            bot_length = Float.Switch(underneath, box_depth - hrz_ofs + groove, box_depth)._lc("Bottom Length")
            bot_length.switch(underneath.bnot() & use_box_front, bot_length - side_thick)

            bot_pos = Vector((box_min[0] + hrz_ofs, box_min[1] + hrz_ofs, box_min[2] + groove_setback))._lc("Bottom Pos")

        with Layout("Create Bottom Panel"):

            bot_panel = bot_model.create_from_model(
                position    = bot_pos,
                dimensions  = (bot_width, bot_length, bot_thick),
                orientation = ROTATED_SHELF,
            )
            bot_panel.points.Owner_Id = front_id
            mesh.join_component(bot_panel)
            bot_id = mesh.comp_id

        # ----------------------------------------------------------------------------------------------------
        # Add the handle
        # ----------------------------------------------------------------------------------------------------

        with Layout("Handle"):
            mesh.join_accessory(comp_id=front_id, accessory=handle_obj, position=(1, 0.5, handle_pos))

        # ----------------------------------------------------------------------------------------------------
        # Duplicate
        # ----------------------------------------------------------------------------------------------------

        with Layout("Duplicate"):
            ty = Float.Switch(dupl_vert, Float.Switch(dupl_tr.less_than(0), dupl_tr + front_width, dupl_tr -front_width), 0.0)
            tz = Float.Switch(dupl_vert, 0.0, Float.Switch(dupl_tr.less_than(0), dupl_tr + front_height, dupl_tr - front_height))
            mesh.duplicate_component(
                comp_id     = front_id,
                linked      = True, 
                accessories = True,
                count       = dupl_count - 1,
                offset_y    = ty,
                offset_z    = tz,
                )

        # ----------------------------------------------------------------------------------------------------
        # Open the drawer
        # ----------------------------------------------------------------------------------------------------

        with Layout("Open the Drawer"):
            mesh.points[utils.selector(comp_id=front_id, linked=True, accessories=True)].offset = (open, 0, 0)

        mesh.out()
        front_id.out("Front Id")
        left_id.out("Left Id")
        right_id.out("Right Id")
        frt_id.out("Inner Front Id")
        rear_id.out("Rear Id")
        bot_id.out("Bottom Id")

        return


        
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

       
                
