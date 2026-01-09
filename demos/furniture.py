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

from geonodes import *

from geonodes.core import constants

USE_GIZMO = True
MAX_ID = 1000000
MIN_DIM = 0.001 # 1 mm

# FACES TYPE
FACE = 0
LONG_SIDE = 1
CUT_SIDE = 2

# ====================================================================================================
# UTILITIES
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Snap function
# ----------------------------------------------------------------------------------------------------

def snap(v, d=MIN_DIM):
    return gnmath.round(v/d)*d

# ----------------------------------------------------------------------------------------------------
# Get the planks
# ----------------------------------------------------------------------------------------------------

def get_planks():
    mesh = Mesh()
    planks = Mesh(mesh).points[nd.id.greater_equal(MAX_ID)].delete()
    return planks, mesh

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

    with GeoNodes("Cote Line", is_group=True):
        
        i_axis      = Integer(0, "Axis", 0, 2) #.MenuSwitch({"X": 0, "Y": 1, "Z": 2}, menu=Input("Axis"))
        show        = Boolean(True, "Show")
        p0          = Vector(0, "From")
        p1          = Vector((1, 0, 0), "To")
        font_size   = Float(.1, "Font Size", 0.01)
        section     = Float(.01, "Section", 0)
        invert      = Boolean(False, "Invert")
        
        offset_a    = Float(0, "Cote Offset A", hide_in_modifier=True)
        offset_b    = Float(0, "Cote Offset B", hide_in_modifier=True)
        
        with Layout("The vector"):
            #v       = p1 - p0
            x0, y0, z0 = p0.xyz
            x1, y1, z1 = p1.xyz
            d = abs(Float.IndexSwitch(x1 - x0, y1 - y0, z1 - z0, index=i_axis))
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
                
            with Vector.IndexSwitch(index=i_axis) as dir:
                Vector((x1 - x0, 0, 0)).out()
                Vector((0, y1 - y0, 0)).out()
                Vector((0, 0, z1 - z0)).out()

            line.transform(translation=p0, rotation=Rotation().align_z_to_vector(dir))
            
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
                
            label.transform(translation=p0 + dir/2 + offset)
            
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
            
            p = (p0 + p1)/2 + dir_a.scale(offset_a) + dir_b.scale(offset_b)
            gizmo_a = offset_a.linear_gizmo(position=p, direction=dir_a, color_id='PRIMARY')
            gizmo_b = offset_b.linear_gizmo(position=p, direction=dir_b, color_id='SECONDARY')
            
            line.transform(translation=dir_a.scale(offset_a) + dir_b.scale(offset_b))
            
        # The cote won't be considered as a plank
        line.set_id(MAX_ID)
        line = Mesh(line)
        line.points.Axis = i_axis
        
        line.switch_false(show).out()

    # ====================================================================================================
    # Join Part
    # ====================================================================================================

    with GeoNodes("Add Plank", is_group=True):
        
        planks, mesh = get_planks()
        plank = Mesh(name="Plank")
        orient = Integer(0, "Orientation")
        
        max_id = planks.points.attribute_statistic(nd.id).max_.to_integer()
        plank_id = max_id + 1
        plank_id = plank_id.switch(planks.points.count.equal(0), 0)
        plank.set_id(plank_id)
        plank.faces.Face_Random = Float.Random(0, 1, seed=plank_id)

        new_mesh = Mesh(mesh + plank)
        new_mesh.points[nd.id.equal(plank_id)].Orientation = orient

        new_mesh.out("Mesh")
        plank_id.out("Plank ID")

    # ====================================================================================================
    # Mesh dimensions
    # ====================================================================================================

    with GeoNodes("Get Dimensions", is_group=True):
        
        with Layout("Reference Mesh"):
            mesh, _ = get_planks()
            use_id = Boolean(False, "Use ID")
            id = Integer(0, "ID")
            
            max_id = mesh.points.attribute_statistic(nd.id).max_.to_integer()
            
            mesh = Mesh(mesh.switch(use_id, Mesh(mesh).points[nd.id.not_equal(id)].delete()))
            
        with Layout("Dimensions"):
            node = mesh.points.attribute_statistic(nd.position)
            vmax = node.max_
            vmin = node.min_
            size = vmax - vmin
            
        mesh.out()

        mesh.points.sample_index(Integer("Orientation"), index=0).out("Orientation")
        
        vmin.out("Min")
        vmax.out("Max")
        size.out("Size")
        
        x, y, z = vmin.xyz    
        x.out("Back")
        y.out("Left")
        z.out("Bot")
        
        x, y, z = vmax.xyz
        x.out("Front")
        y.out("Right")
        z.out("Top")
        
        x, y, z = size.xyz
        x.out("Size X")
        y.out("Size Y")
        z.out("Size Z")
        
        dims = mesh.points.sample_index(Vector("Dimensions"), index=0)
        dims.out("Dimensions")
        
        x, y, z = dims.xyz
        x.out("Width")
        y.out("Length")
        z.out("Thickness")
        
        max_id.out("Max ID")
        (max_id + 1).out("Next ID")
        
    # ====================================================================================================
    # MACRO : Get a cote
    # ====================================================================================================
        
    def get_cote(mesh, name, is_dim, *, default_value=0.0, default_dim=None):
        """ Get a cote from other planks
        
        The cote can be a user defined value or a cote from other planks : dimension, position
        or distance between two planks.
        
        Two special choices are defined:
        - Zero (for location) : the value zero
        - Same (for dimension) : keep the model plank dimension
        
        In addition, the user can define an offset which is added to is selection.
        Note the the offset is not proposed for:
        - Zero : use Value rather than Zero + Offset
        - Value : Value + Offset has no sense
        
        Value and Offset are driven by a linear Gizmo:
        - direction : given by axis argument
        - color : given by color argument
        
        Arguments
        ---------
        - mesh (Mesh) : the stack of planks
        - name (str) : name of the cote
        - axis (int in (0, 1, 2)) : axis
        - is_dim (bool) : the cote is a dimension (not a distance)
        - default (float or FLoat) : User value default value (is_dim = False) or default dimension (is_dim = True)
            
            
        Returns
        -------
        - value, dict: 'offset': Float, 'no_offset': bool (ignore offset), 'user_value': value without offset
        """
        
        with Layout("Get Cote"):
        
            id0 = Integer(0, "Plank ID")
            
            with Layout("Plank 0"):
                plank0 = G().get_dimensions(mesh, True, id0)
                
            with Layout("Plank 1"):
                id1 = Integer(1, "Other ID")
                plank1 = G().get_dimensions(mesh, True, id1)
                
                dist_x = plank1.back - plank0.front
                dist_y = plank1.left - plank0.right
                dist_z = plank1.bot  - plank0.top
                
                dist_x = dist_x.switch(dist_x.less_than(0), plank0.back - plank1.front)
                dist_y = dist_y.switch(dist_y.less_than(0), plank0.left - plank1.right)
                dist_z = dist_z.switch(dist_z.less_than(0), plank0.bot  - plank1.top)
                
            # User defined value
            if is_dim:
                user_value = Float.Distance(default_value, "Value", MIN_DIM)
            else:
                user_value = Float.Distance(default_value, "Value")
            
            with Float.MenuSwitch(menu=Input(name)) as selected_value:
                if is_dim:                
                    default_dim.out(    "Keep")
                else:
                    Float(0.0).out(     "Zero")
                    
                user_value.out(         "Value")
                plank0.width.out(       "Width")
                plank0.length.out(      "Length")
                plank0.thickness.out(   "Thickness")
                plank0.back.out(        "Back")
                plank0.left.out(        "Left")
                plank0.bot.out(         "Bottom")
                plank0.front.out(       "Front")
                plank0.right.out(       "Right")
                plank0.top.out(         "Top")
                plank0.size_x.out(      "Size X")
                plank0.size_y.out(      "Size Y")
                plank0.size_z.out(      "Size Z")
                dist_x.out(             "Distance X")
                dist_y.out(             "Distance Y")
                dist_z.out(             "Distance Z")

            # Additional offset
            offset  = Float.Distance(0.0, "Offset")
                
            # No offset if user defined value
            no_offset = selected_value.value
            
            # When not a dim, no offset if zero (use Value instaed of Zero + Offset)
            if not is_dim:
                no_offset |= selected_value.node[1]

            value = selected_value.switch_false(no_offset, selected_value + offset)
            if is_dim:
                value = gnmath.max(value, MIN_DIM)
            
            return value, {
                'offset'      : offset, 
                'no_offset'   : no_offset, 
                'user_value'  : user_value,
                'offset'      : offset,
                }
                
    # ====================================================================================================
    # Locate Plank
    # ====================================================================================================

    with GeoNodes("Locate") as tree:
        
        mesh = Mesh()
        plank_id = Integer(0, "ID", 0)

        plank = G().get_dimensions(mesh, True, plank_id)
        size_x, size_y, size_z = plank.size_x, plank.size_y, plank.size_z
        
        #show_cotes = Boolean(False, "Show Cotes")
        
        # ---------------------------------------------------------------------------
        # Location
        # ---------------------------------------------------------------------------

        with Panel("X", create_layout=True):
            
            with Float.MenuSwitch(menu=Input("X Alignment")) as delta_x:
                Float(0.0).out(     "In Front")
                Float(size_x/2).out("Centered")
                Float(size_x).out(  "Behind")
                
            x, x_dict = get_cote(mesh, "X", False)
            
        with Panel("Y", create_layout=True):
            
            with Float.MenuSwitch(menu=Input("Y Alignment")) as delta_y:
                Float(0.0).out(     "Right")
                Float(size_y/2).out("Centered")
                Float(size_y).out(  "Left")
                
            y, y_dict = get_cote(mesh, "Y", False)
            
        with Panel("Z", create_layout=True):
            
            with Float.MenuSwitch(menu=Input("Z Alignment")) as delta_z:
                Float(0.0).out(     "Above")
                Float(size_z/2).out("Centered")
                Float(size_z).out(  "Below")

            z, z_dict = get_cote(mesh, "Z", False)
            
        # ---------------------------------------------------------------------------
        # Translation
        # ---------------------------------------------------------------------------
        
        # Current origin
        old_x, old_y, old_z = plank.back, plank.left, plank.bot
        
        # Target origin
        ox, oy, oz = x - delta_x, y - delta_y, z - delta_z
        
        # Translate    
        mesh[nd.id.equal(plank_id)].offset = (ox - old_x, oy - old_y, oz - old_z)    
        
        # ---------------------------------------------------------------------------
        # Labels
        # ---------------------------------------------------------------------------
        
        # Cotes params
        # User offset are hidden and connected using link_inputs 
        
        font_size = 0.1
        section = 0.01
        invert = False
        
        cote = G().cote_line(
            axis        = 0,
            show        = Boolean(False, "Cote", panel="X"),
            from_       = (0, 0, 0),
            to          = (x, 0, 0),
            font_size   = font_size,
            section     = section,
            invert      = Boolean(False, "Invert", panel="X"),
            ).link_inputs(None, "X")
        mesh += cote
        
        cote = G().cote_line(
            axis        = 1,
            show        = Boolean(False, "Cote", panel="Y"),
            from_       = (0, 0, 0),
            to          = (0, y, 0),
            font_size   = font_size,
            section     = section,
            invert      = Boolean(False, "Invert", panel="Y"),
            ).link_inputs(None, "Y")
        mesh += cote
        
        cote = G().cote_line(
            axis        = 2,
            show        = Boolean(False, "Cote", panel="Z"),
            from_       = (0, 0, 0),
            to          = (0, 0, z),
            font_size   = font_size,
            section     = section,
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
            
            with Mesh.MenuSwitch(menu=Input("Model")) as model:
                plank_id = Integer(0, "From ID", 0)
                plank = Mesh(mesh).points[nd.id.not_equal(plank_id)].delete()

                plank_orientation = plank.points.sample_index(Integer("Orientation"), index=0)

                # Rotate horizontal to keep UV
                rot = Rotation.IndexSwitch(0, (-pi/2, 0, 0), (0, -pi/2, 0), index=plank_orientation)
                plank.transform(rotation=rot)

                plank.out("Plank ID")
                
            with model:
                def_size = (0.3, 1.0, .02)
                plank = Mesh.Cube(size=def_size)
                plank.points.Dimensions = def_size
                plank.faces.material = Material("Plank", "Material")

                plank.out("Default")
                
            with model:
                plank_obj = Object(None, "Model")
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
        
        #with Panel("Cotes", create_layout=True):        
        #    dim_cotes = Boolean(False, "Dimensions Cotes")
        #    loc_cotes = Boolean(False, "Location Cotes")
        
        with Panel("Width", create_layout=True):
            width, w_dict = get_cote(mesh, "Width", True, default_value=0.30, default_dim=dims.width)
            cote_width = Boolean(False, "Cote")
            invert_width = Boolean(False, "Invert")
            
        with Panel("Length", create_layout=True):
            length, l_dict = get_cote(mesh, "Length", True, default_value=1.0, default_dim=dims.length)
            cote_length = Boolean(False, "Cote")
            invert_length = Boolean(False, "Invert")
            
        with Panel("Thickness", create_layout=True):
            thickness, t_dict = get_cote(mesh, "Thickness", True, default_value=0.02, default_dim=dims.thickness)
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

            x0, y0, z0 = vmin.xyz
            x, y, z = nd.position.xyz

            plank.corners[Integer("Face Type").equal(FACE)].store_uv(     "UVMap", (x - x0, y - y0, 0))
            plank.corners[Integer("Face Type").equal(LONG_SIDE)].store_uv("UVMap", (z - z0, y - y0, 0))
            plank.corners[Integer("Face Type").equal(CUT_SIDE)].store_uv( "UVMap", (z - z0, x - x0, 0))

        
        # ---------------------------------------------------------------------------
        # Orientation
        # ---------------------------------------------------------------------------
        
        with Integer.MenuSwitch(menu=Input("Orientation")) as orient:
            Integer(0).out("Horizontal")
            Integer(1).out("Side")
            Integer(2).out("Front")
            
        with Rotation.IndexSwitch(index=orient) as rot:
            Rotation().out()
            Rotation((pi/2, 0, 0)).out()
            Rotation((0, pi/2, 0)).out()
            
        plank = plank.transform(rotation=rot)
        
        # ---------------------------------------------------------------------------
        # Add the plank
        # ---------------------------------------------------------------------------
        
        mesh = G().add_plank(mesh, plank, orientation=orient)

        # ---------------------------------------------------------------------------
        # Locate
        # ---------------------------------------------------------------------------
        
        node = Group("Locate", mesh = mesh, id = mesh.plank_id).link_inputs()
        mesh = node.mesh
        
        # ---------------------------------------------------------------------------
        # Dimensions Cotes
        # ---------------------------------------------------------------------------
        
        with Layout("Dimensions Cotes"):
        
            O = mesh.origin
            S = mesh.size
            
            font_size = 0.1
            section = 0.01
            invert = False
            
            with Float.IndexSwitch(index=orient) as x_dim:
                width.out()
                width.out()
                thickness.out()
                
            with Float.IndexSwitch(index=orient) as y_dim:
                length.out()
                thickness.out()
                length.out()

            with Float.IndexSwitch(index=orient) as z_dim:
                thickness.out()
                length.out()
                width.out()
            
            cote = G().cote_line(
                axis        = 0,
                show        = Boolean.IndexSwitch(cote_width, cote_width, cote_thick, index=orient),
                from_       = O,
                to          = O + (x_dim, 0, 0),
                font_size   = font_size,
                section     = section,
                invert      = Boolean.IndexSwitch(invert_width, invert_width, invert_thick, index=orient),
                ).link_inputs(None, "Width")
            mesh += cote
            
            cote = G().cote_line(
                axis        = 1,
                show        = Boolean.IndexSwitch(cote_length, cote_thick, cote_length, index=orient),
                from_       = O,
                to          = O + (0, y_dim, 0),
                font_size   = font_size,
                section     = section,
                invert      = Boolean.IndexSwitch(invert_length, invert_thick, invert_length, index=orient),
                ).link_inputs(None, "Length")
            mesh += cote
            
            cote = G().cote_line(
                axis        = 2,
                show        = Boolean.IndexSwitch(cote_thick, cote_length, cote_width, index=orient),
                from_       = O,
                to          = O + (0, 0, z_dim),
                font_size   = font_size,
                section     = section,
                invert      = Boolean.IndexSwitch(invert_thick, invert_length, invert_width, index=orient),
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
                    
                with Vector.IndexSwitch(index=orient) as length_dir:
                    Vector((0, 1, 0)).out()
                    Vector((0, 0, 1)).out()
                    Vector((0, 1, 0)).out()
                    
                with Vector.IndexSwitch(index=orient) as thick_dir:
                    Vector((0, 0, 1)).out()
                    Vector((0, 1, 0)).out()
                    Vector((1, 0, 0)).out()
                    
                
                g_vx = w_dict['user_value'].linear_gizmo(position=g_pos, direction=width_dir,  color_id='X', draw_style='ARROW')
                g_vy = l_dict['user_value'].linear_gizmo(position=g_pos, direction=length_dir, color_id='Y', draw_style='ARROW')
                g_vz = t_dict['user_value'].linear_gizmo(position=g_pos, direction=thick_dir,  color_id='Z', draw_style='ARROW')
                
                g_ox = w_dict['offset'].linear_gizmo(position=g_pos, direction=width_dir,  color_id='X', draw_style='BOX')
                g_oy = l_dict['offset'].linear_gizmo(position=g_pos, direction=length_dir, color_id='Y', draw_style='BOX')
                g_oz = t_dict['offset'].linear_gizmo(position=g_pos, direction=thick_dir,  color_id='Z', draw_style='BOX')
        
        mesh.out()
        
    # ====================================================================================================
    # Shelf
    # ====================================================================================================

    with GeoNodes("Shelf"):
        
        mesh = Mesh()
        left_id  = Integer(0, "Left Plank ID")
        right_id = Integer(0, "Right Plank ID")
        
        setback0 = Float.Distance(0.0,  "Back Setback", 0)
        setback1 = Float.Distance(0.02, "Front Setback", 0)
        
        node = Group("Plank", {
            "Width > Offset" : -(setback0 + setback1),
            
            "Length > Length" : 'Distance Y',
            "Length > Plank ID" : left_id,
            "Length > Other ID" : right_id,
            
            "X > X"         : 'Front',
            "X > Alignment" : 'Behind',
            "X > Plank ID"  : left_id,
            "X > Offset"    : -setback1,
            
            "Y > Y"         : 'Right',
            "Y > Alignment" : 'Right',
            "Y Plank ID"    : left_id,
            },
            
            mesh        = mesh,
            from_id     = left_id,
            orientation =  "Horizontal",
            
        ).link_inputs(None, include=["Thickness", "Z", "Material", "Set Material"])
        node.out()

    # ====================================================================================================
    # Plinth
    # ====================================================================================================

    with GeoNodes("Plinth"):
        
        mesh = Mesh()
        plank_id = Integer(0, "Under Plank ID")
        setback = Float.Distance(0.02, "Setback", 0)
        
        left_ofs = Float.Distance(0.0, "Left Offset")
        right_ofs = Float.Distance(0.0, "Right Offset")

        with Panel("Model"):
            use_plank = Boolean(True, "Use Plank")
            model_id = Integer(0, "Model ID").switch(use_plank, plank_id)
        
        node = Group("Plank", {
            "Width > Plank ID"  : plank_id,
            "Width > Width"     : 'Bottom',
            
            "Length > Plank ID" : plank_id,
            "Length > Length"   : 'Length',
            "Length > Offset"   : left_ofs + right_ofs,
            
            "X > Alignment"     : 'Behind',
            "X > X"             : 'Front',
            "X > Plank ID"      : plank_id,
            "X > Offset"        : -setback,
            
            "Y > Alignment"     : 'Right',
            "Y > Y"             : 'Left',
            "Y Plank ID"        : plank_id,
            "Y > Offset"        : -left_ofs,
            
            "Z > Alignment"     : 'Above',
            "Z > Z"             : 'Zero',
            },
            
            mesh        = mesh,
            from_id     = model_id,
            orientation =  "Front",
            
        ).link_inputs(None, include=["Thickness"])
        node.out()
        
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
            rep.cloud.points[sel].Dimensions = plank.points.sample_index(Vector("Dimensions"), index=rep.iteration)
            rep.cloud[sel].position = plank.points.attribute_statistic(nd.position).mean
            
        cloud = rep.cloud
        cloud.set_id(nd.index)
            
        cloud.out()

    # ====================================================================================================
    # Dimension
    # ====================================================================================================

    with GeoNodes("Cote"):

        mesh = Mesh()

        show = Boolean(True, "Show")

        id0 = Integer(0, "Plank 0")
        id1 = Integer(0, "Plank 1")

        i_axis = Integer.MenuSwitch({"X": 0, "Y": 1, "Z": 2}, menu=Input("Axis"))
        
        plank0 = G().get_dimensions(mesh, True, id0)
        plank1 = G().get_dimensions(mesh, True, id1)
        whole  = G().get_dimensions(mesh)

        # ---------------------------------------------------------------------------
        # Start location
        # ---------------------------------------------------------------------------
        
        #pos = plank0.min + plank0.size.scale(0.5)
        #x, y, z = pos.xyz
        
        # ---------------------------------------------------------------------------
        # Along axis
        # ---------------------------------------------------------------------------

        axis = String.IndexSwitch("X", "Y", "Z", index=i_axis)

        with Layout("Select Values From -> To"):
        
            wmin = Float.IndexSwitch(*whole.min.xyz, index=i_axis)
            wmax = Float.IndexSwitch(*whole.max.xyz, index=i_axis)

            min0 = Float.IndexSwitch(*plank0.min.xyz, index=i_axis)
            max0 = Float.IndexSwitch(*plank0.max.xyz, index=i_axis)
            min1 = Float.IndexSwitch(*plank1.min.xyz, index=i_axis)
            max1 = Float.IndexSwitch(*plank1.max.xyz, index=i_axis)

            i_from = Integer.MenuSwitch({
                "Zero" :         0,
                f"Whole Min" :   1,
                f"Whole Max" :   2,
                f"Plank 0 Min" : 3,
                f"Plank 0 Max" : 4,
                f"Plank 1 Min" : 5,
                f"Plank 1 Max" : 6,
                }, menu = Input("From"))
                
            i_to = Integer.MenuSwitch({
                f"Whole Min" :   0,
                f"Whole Max" :   1,
                f"Plank 0 Min" : 2,
                f"Plank 0 Max" : 3,
                f"Plank 1 Min" : 4,
                f"Plank 1 Max" : 5,
                }, menu = Input("To"))
                    
            v0 = Float.IndexSwitch(0.0, wmin, wmax, min0, max0, min1, max1, index=i_from)
            v1 = Float.IndexSwitch(wmin, wmax, min0, max0, min1, max1, index=i_to)
            delta = v1 - v0

        with Layout("Start and End Points"):

            Ow = (whole.min + whole.max)/2
            O0 = (plank0.min + plank0.max)/2
            O1 = (plank1.min + plank1.max)/2

            p0 = Vector.IndexSwitch(Ow, Ow, Ow, O0, O0, O1, O1, index=i_from)
            p1 = p0 + Vector.IndexSwitch((delta, 0, 0), (0, delta, 0), (0, 0, delta), index=i_axis)

            cote = G().cote_line(
                axis        = i_axis,
                show        = show,
                from_       = p0,
                to          = p1,
                ).link_inputs(None, "Options")
            
            mesh += cote
            
        mesh.out()    

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
                          
                
            
                
                
                
    
    
    
    
    
    
    
    
    
    
    
        
            
       


def OLD():        
            
            
            
    # ====================================================================================================
    # Get Distance
    # ====================================================================================================

    with GeoNodes("Get Distances", is_group=True):
        
        with Panel("First"):
            part0 = Mesh()
            
        with Panel("Second"):
            part1 = Mesh()
            
        dims0 = Group("Get Dimensions", mesh=part0).link_inputs(None, "First")
        dims1 = Group("Get Dimensions", mesh=part1).link_inputs(None, "Second")
        
        dx = dims1.back - dims0.front
        dy = dims1.left - dims0.right
        dz = dims1.bot  - dims0.top

        Vector((dx, dy, dz)).out("Distances")
        dx.out("X")
        dy.out("Y")
        dz.out("Z")
        


    # ====================================================================================================
    # Alignment
    # ====================================================================================================
        
    with GeoNodes("Alignment", is_group=True):
        
        fix_0 = Float.Distance(0., "Fix 0")
        fix_1 = Float.Distance(0., "Fix 1")
            
        mob_0 = Float.Distance(0., "Mobile 0")
        mob_1 = Float.Distance(0., "Mobile 1")
        
        ofs   = Float.Distance(0, "Offset")
        
        with Integer.MenuSwitch(index=Input("Alignment")) as i_align:
            Integer(0).out("None")        
            Integer(1).out("Align Start")
            Integer(2).out("Align End")
            Integer(3).out("Before")
            Integer(4).out("After")
            Integer(5).out("Between")
        
        with Float.IndexSwitch(index=i_align) as offset:
            
            Float(0).out()        
            (fix_0 - mob_0).out()
            (fix_1 - mob_1).out()
            (fix_0 - mob_1).out()
            (fix_1 - mob_0).out()
            (fix_0 - mob_0).out()
            
        offset += ofs
        
        length = (mob_1 - mob_0).switch(i_align.equal(5), fix_1 - fix_0 - 2*ofs)
        
        offset.out("Offset")
        length.out("Length")
        
    # ====================================================================================================
    # Locate
    # ====================================================================================================

    with GeoNodes("Locate"):
        
        mesh = Mesh()
        id   = Integer(0, "ID")
        
        plank_dims = Group("Get Dimensions", mesh=mesh, use_id=True, id=id)
        
        deltas = [0]*3
        for i_axis in range(3):
            axis = 'XYZ'[i_axis]
        
            with Panel(axis, create_layout=True):
                with Integer.MenuSwitch(Menu=Input("Align")) as x_align:
                    Integer(0).out("No Change")
                    
                    if i_axis == 0:
                        Integer(1).out("In Front")
                        Integer(2).out("Behind")
                        Integer(3).out("Align Back")
                        Integer(4).out("Align Front")
                        
                    elif i_axis == 1:
                        Integer(1).out("Right To")
                        Integer(2).out("Left To")
                        Integer(3).out("Align Left")
                        Integer(4).out("Align Right")
                        
                    elif i_axis == 2:
                        Integer(1).out("Above")
                        Integer(2).out("Below")
                        Integer(3).out("Align Bottom")
                        Integer(4).out("Align Top")
                        
                use_id  = Boolean(False, "Use ID")
                x_fix   = Float(0.0, axis)
                x_id    = Integer(1, "ID Ref")
                x_ofs   = Float.Distance(0.0, "Offset")
                
                dims = Group("Get Dimensions", mesh=mesh, use_id=True, id=x_id)
                low  = dims.min.xyz[i_axis]
                high = dims.max.xyz[i_axis]
                with Float.IndexSwitch(index=x_align) as x_rel:
                    Float(0.0).out()
                    high.out()
                    low.out()
                    low.out()
                    high.out()
                    
                x_ref = x_fix.switch(use_id, x_rel) + x_ofs
                
                delta_front = x_ref - plank_dims.min.xyz[i_axis]
                delta_back  = delta_front - plank_dims.dimensions.xyz[i_axis]
                
                with Float.IndexSwitch(index=x_align) as x_delta:
                    Float(0.0).out()
                    delta_front.out()
                    delta_back.out()
                    delta_front.out()
                    delta_back.out()
                    
                deltas[i_axis] = x_delta
                
                
        mesh[nd.id.equal(id)].offset = deltas
        
        mesh.out()
        
        
    # ====================================================================================================
    # A Single Plank from Mesh
    # ====================================================================================================

    with GeoNodes("Single Plank"):
        
        mesh = Mesh()
        
        width     = Float(0.3, "Width")
        length    = Float(1.0, "Length")
        thickness = Float(0.3, "Thckness")
        
        dims = Group("Get Dimensions", mesh=mesh)
        
        mesh = mesh.transform(scale=(width/dims.width, length/dims.length, thickness/dims.height))
        mesh.set_id(0)
        dimensions = Vector((width, length, thickness))
        mesh.points.Dimensions = dimensions
        mesh = mesh.transform(translation = dimensions.scale(.5))
        
        with Rotation.MenuSwitch() as rot:
            Rotation().out("Horizontal")
            Rotation((pi/2, 0, 0)).out("Side")
            Rotation((0, pi/2, 0)).out("Front")
            
        rot.menu = Input("Orientation")
        
        mesh = mesh.transform(rotation=rot)
        
        Group("Locate", mesh=mesh).link_inputs(None).out()
        
    # ====================================================================================================
    # Duplicate
    # ====================================================================================================

    with GeoNodes("Duplicate"):
        
        mesh = Mesh()
        id = Integer(0, "ID")
        
        dims = Group("Get Dimensions", mesh=mesh, use_id=True, id=id)
        plank = dims.mesh
        
        dimensions = plank.points.sample_index(Vector("Dimensions"), index=0)
        width, length, thickness = dimensions.xyz
        
        width  += Float.Distance(0.0, "Width Offset")
        length += Float.Distance(0.0, "Length Offset")

        plank = plank.transform(scale=(width/dims.width, length/dims.length, thickness/dims.height))
        plank.points.Dimensions = (width, length, thickness)
        plank.set_id(0)
        
        mesh = Group("Join Part", mesh=mesh, part=plank)._out
        
        Group("Locate", mesh=mesh, id=mesh.id_).link_inputs(None).out()    
        
        
        
      

         
            

        
        
        
        
        
            
            
            
                
            
            
        
    
    
    
        
        
        
        


def test():
    
    with GeoNodes("TEMP"):
        
        
        
        model = Object(None, "Model")
        
        
        
        wood   = Object("Wood", "Wood")
        id     = Integer(0, "ID")
        length = Float.Distance(1.0, "Length")
        
        with Panel("Width"):
            change_width = Boolean(False, "Change Width")
            width        = Float.Distance(0.3, "Width")
            offset       = Float.Distance(0.0, "Offset", -1.0, 1.0)
            
        with Layout("Scale"):
            base = Mesh(wood.info().geometry)
            base.set_id(id)
            dims = base.points.sample_index(Vector("Dimensions"), index=0)
            l, w, thickness = dims.xyz
            
            width = w.switch(change_width, width)
            
            scale_x = length/l
            scale_y = width/w
            
            plank = base.transform(scale=(scale_x, scale_y, 1.))
            plank.points.Dimensions = (length, width, thickness)
            
        with Layout("Rotation"):
            with Rotation.MenuSwitch() as rot:
                Rotation().out("Horizontal")
                Rotation((0, -pi/2, 0)).out("Side")
                Rotation((pi/2, 0, 0)).out("Front")
                
            rot.node.menu = Input("Oritentation", default='Horizontal')
            
        with Layout("Locate in O"):
            plank = base.transform(translation=(length/2, width/2, thickness/2), rotation=rot)
            
        with Layout("User Location"):
            dims = Group("Get Dimensions", furniture=plank)
            with Panel("Location"):
                lx = Float.Distance(0, "X")
                ly = Float.Distance(0, "Y")
                lz = Float.Distance(0, "Z")
                
                dx = dims.length.switch_false(Boolean(True, "Left"), 0.0) 
                dy = dims.width.switch_false(Boolean(False, "Back"), 0.0) 
                dz = dims.height.switch_false(Boolean(False, "Bottom"), 0.0)
                
                plank = plank.transform(translation=Vector((lx, ly, lz)) - dims.min - (dx, dy, dz))
            
        
        plank.out("Plank")
        Group("Get Dimensions", furniture=plank).out()
            
        
            
            
            
    # ====================================================================================================
    # Reference Wood
    # ====================================================================================================
        
    with GeoNodes("Wood Reference"):
        
        geo = Geometry()
        material = Material("Wood", "Material")
        width = Float.Distance(0.3, "Width", 0.01, 3)
        thickness = Float.Distance(0.018, "Thickness", 0.01, 0.2)
        
        cube = Mesh.Cube(size=(1, width, thickness))
        cube.faces.material = material
        cube.points.Dimensions = (1, width, thickness)
        
        cube.out()
        

    # ====================================================================================================
    # Plank
    # ====================================================================================================

    with GeoNodes("New Plank"):
        
        wood   = Object("Wood", "Wood")
        id     = Integer(0, "ID")
        length = Float.Distance(1.0, "Length")
        
        with Panel("Width"):
            change_width = Boolean(False, "Change Width")
            width        = Float.Distance(0.3, "Width")
            offset       = Float.Distance(0.0, "Offset", -1.0, 1.0)
            
        with Layout("Scale"):
            base = Mesh(wood.info().geometry)
            base.set_id(id)
            dims = base.points.sample_index(Vector("Dimensions"), index=0)
            l, w, thickness = dims.xyz
            
            width = w.switch(change_width, width)
            
            scale_x = length/l
            scale_y = width/w
            
            plank = base.transform(scale=(scale_x, scale_y, 1.))
            plank.points.Dimensions = (length, width, thickness)
            
        with Layout("Rotation"):
            with Rotation.MenuSwitch() as rot:
                Rotation().out("Horizontal")
                Rotation((0, -pi/2, 0)).out("Side")
                Rotation((pi/2, 0, 0)).out("Front")
                
            rot.node.menu = Input("Oritentation", default='Horizontal')
            
        with Layout("Locate in O"):
            plank = base.transform(translation=(length/2, width/2, thickness/2), rotation=rot)
            
        with Layout("User Location"):
            dims = Group("Get Dimensions", furniture=plank)
            with Panel("Location"):
                lx = Float.Distance(0, "X")
                ly = Float.Distance(0, "Y")
                lz = Float.Distance(0, "Z")
                
                dx = dims.length.switch_false(Boolean(True, "Left"), 0.0) 
                dy = dims.width.switch_false(Boolean(False, "Back"), 0.0) 
                dz = dims.height.switch_false(Boolean(False, "Bottom"), 0.0)
                
                plank = plank.transform(translation=Vector((lx, ly, lz)) - dims.min - (dx, dy, dz))
            
        
        plank.out("Plank")
        Group("Get Dimensions", furniture=plank).out()
        
    # ====================================================================================================
    # Duplicate
    # ====================================================================================================

    with GeoNodes("Duplicate"):
        
        furniture = Mesh(None, "Furniture")
        id = Integer(0, "ID")
        
        abs_dx = Boolean(False, "X Absolute")
        dx = Float(0.0, "X Offset")
        
        abs_dy = Boolean(False, "Y Absolute")
        dy = Float(0.0, "Y Offset")

        abs_dz = Boolean(False, "Z Absolute")
        dz = Float(0.0, "Z Offset")
        
        part = Mesh(furniture).points[nd.id.not_equal(id)].delete()
        dims = Group("Get Dimensions", furniture=part)

        trans = Vector((
            dx.switch(abs_dx, dx - dims.left),
            dy.switch(abs_dy, dy - dims.back),
            dz.switch(abs_dz, dz - dims.bot),
        ))
        
        part = part.transform(translation=trans)
        
        Group("Join Part", furniture=furniture, part=part)._out.out("Furniture")
        
        
        
        
        

    # ====================================================================================================
    # Align a block
    # ====================================================================================================

    with GeoNodes("Locate", is_group=True):

        with Panel("Part"):
            part = Mesh(None, "Part")
            p_use_id = Boolean(False, "Use ID")
            p_id = Integer(0, "ID")
            
        p_dims = Group("Get Dimensions", furniture=part, use_id=p_use_id, id=p_id)
            
        deltas = []
        for i in range(3):
            axis = 'XYZ'[i]
            panel_name = f"{axis} Alignment"
            with Layout(panel_name):
                with Panel(panel_name):
                    
                    ref    = Float.Distance(0.0, axis, -3, 2)
                    offset = Float.Distance(0.0, "Offset", -3, 3)
                    
                    use_furniture = Boolean(False, "Use Furniture")
                    furniture = Mesh(None, "Furniture")
                    f_use_id = Boolean(False, "Use ID")
                    f_id = Integer(0, "ID")
                
                f_dims = Group("Get Dimensions", furniture=furniture, use_id=f_use_id, id=f_id)
                low  = f_dims.min.xyz[i]
                high = f_dims.max.xyz[i]
                
                delta = G().alignment(
                    base_low    = ref.switch(use_furniture, low),
                    base_high   = ref.switch(use_furniture, high),
                    mobile_low  = p_dims.min.xyz[i],
                    mobile_high = p_dims.max.xyz[i],
                    alignment   = Input(f"{axis} Alignment", panel=panel_name),
                    )
               
            deltas.append(delta + offset)
            
        sel = nd.id.equal(p_id).switch_false(p_use_id, True)
        part.points[sel].offset = deltas
        
        part.out("Part")
        Group("Get Dimensions", furniture=plank).out()
        
        
        


if False:
    
    # ====================================================================================================
    # Dimension
    # ====================================================================================================

    def get_label(val, font_size, align_x='CENTER', align_y='MIDDLE'):
        
        with Layout("Label"):
            s = (val*100).to_string(decimals=1)
            c = Curve(s.to_curves(size=font_size, align_x=align_x, align_y=align_y).realize())
            c = c.fill()
            c = c.transform(rotation=(pi/2, 0, 0))
            return c
        
    def get_line(p0, p1, section=0.01):
        with Layout("Line"):
            h = section*4
            h2 = section*2
            v = p1 - p0
            d = v.length() - h
            
            line = Curve.Line((0, 0, h), (0, 0, d))
            line = line.to_mesh(profile_curve=Curve.Circle(radius=section/2))
            
            cone = Mesh.Cone(radius_bottom=h2, depth=h)
            line += Mesh(cone).transform(translation=(0, 0, d))
            line += cone.transform(translation=(0, 0, h), rotation=(0, pi, 0))
            
            return line.transform(translation=p0, rotation=Rotation().align_z_to_vector(v))


    with GeoNodes("Cote"):
        
        obj = Object(None, "Object")
        mesh = obj.info().geometry.separate_components().mesh
        
        with Panel("Size"):
            font_size = Float(.1, "Font Size", 0.01)
            section = Float(.01, "Section", 0)
        
        id0 = Integer(0, "Plank 0")
        id1 = Integer(0, "Plank 1")
        
        plank0 = G().get_dimensions(mesh, True, id0)
        plank1 = G().get_dimensions(mesh, True, id1)
        whole = G().get_dimensions(mesh)

        # ---------------------------------------------------------------------------
        # Start location
        # ---------------------------------------------------------------------------
        
        pos = plank0.min + plank0.size.scale(0.5)
        x, y, z = pos.xyz
        
        # ---------------------------------------------------------------------------
        # Along axis
        # ---------------------------------------------------------------------------
        
        wmin = whole.min.xyz
        wmax = whole.max.xyz
        
        min0 = plank0.min.xyz
        max0 = plank0.max.xyz
        min1 = plank1.min.xyz
        max1 = plank1.max.xyz
        
        for i_axis in range(3):
            
            axis = 'XYZ'[i_axis]
        
            with Panel(f"Along {axis}", create_layout=True):
                
                ok = Boolean(False, "Show")
                
                with Float.MenuSwitch(menu=Input("From")) as v0:
                    Float(0).out(       "Zero")
                    wmin[i_axis].out(   f"Whole {axis} Min")
                    min0[i_axis].out(   f"Whole 0 {axis} Min")
                    max0[i_axis].out(   f"Plank 0 {axis} Max")
                    min1[i_axis].out(   f"Plank 1 {axis} Min")
                    min1[i_axis].out(   f"Plank 1 {axis} Max")
                    
                with Float.MenuSwitch(menu=Input("To")) as v1:
                    wmin[i_axis].out(   f"Whole {axis} Min")
                    wmax[i_axis].out(   f"Whole {axis} Max")
                    min0[i_axis].out(   f"Plank 0 {axis} Min")
                    max0[i_axis].out(   f"Plank 0 {axis} Max")
                    min1[i_axis].out(   f"Plank 1 {axis} Min")
                    min1[i_axis].out(   f"Plank 1 {axis} Max")
                    
                rotate = Boolean(False, "Rotate")
                        
                dist = v1 - v0
                
                va, vb = Float(0, "Offset A", hide_in_modifier=True), Float(0, "Offset B", hide_in_modifier=True)
                
                p0 = [x, y, z]
                p1 = [x, y, z]
                rz = Float.Switch(rotate, pi)
                
                if i_axis == 0:
                    p0 = Vector((v0, y + va, z + vb))
                    p1 = Vector((v1, y + va, z + vb))
                    dira, dirb = (0, 1, 0), (0, 0, 1)
                    align_x, align_y = 'CENTER', 'BOTTOM'
                    lab_ofs = [0, 0, section]
                    
                elif i_axis == 1:
                    p0 = Vector((x + va, v0, z + vb))
                    p1 = Vector((x + va, v1, z + vb))
                    dira, dirb = (1, 0, 0), (0, 0, 1)
                    align_x, align_y = 'CENTER', 'BOTTOM'
                    rz -= pi/2
                    lab_ofs = [0, 0, section]
                    
                elif i_axis == 2:
                    p0 = Vector((x + va, y + vb, v0))
                    p1 = Vector((x + va, y + vb, v1))
                    dira, dirb = (1, 0, 0), (0, 1, 0)
                    align_x, align_y = 'LEFT', 'MIDDLE'
                    rz += pi/2
                    lab_ofs = [0, font_size/3, 0]
                    

                label = get_label(dist, font_size, align_x=align_x, align_y=align_y)
                    
                plab = (p0 + p1)/2

                gizmo_a = va.linear_gizmo(position=plab, direction=dira, color_id='PRIMARY')
                gizmo_b = vb.linear_gizmo(position=plab, direction=dirb, color_id='SECONDARY')
            
                label = label.transform(translation=plab + lab_ofs, rotation=(0, 0, rz))
                line = get_line(p0, p1, section=section)
                
                if i_axis == 0:
                    geo = (line + label).switch_false(ok)
                else:
                    geo = geo.switch(ok, geo + (line, label))
            
            
        geo.out()


    # ====================================================================================================
    # MACRO : Get a cote
    # ====================================================================================================

    def get_cote_OLD(mesh, default_value, name, replaced, *, gizmo_dir=None, draw_style='ARROW'):
        
        id0 = Integer(0, "Plank ID")
        
        with Layout("Plank 0"):
            plank0 = G().get_dimensions(mesh, True, id0)
            
        with Layout("Plank 1"):
            id1 = Integer(1, "Other ID")
            plank1 = G().get_dimensions(mesh, True, id1)
            
            dist_x = plank1.back - plank0.front
            dist_y = plank1.left - plank0.right
            dist_z = plank1.bot  - plank0.top
            
            dist_x = dist_x.switch(dist_x.less_than(0), plank0.back - plank1.front)
            dist_y = dist_y.switch(dist_y.less_than(0), plank0.left - plank1.right)
            dist_z = dist_z.switch(dist_z.less_than(0), plank0.bot  - plank1.top)
            
        v      = Float.Distance(default_value, "Value")
        offset = Float.Distance(0.0, "Offset")
        
        with Float.MenuSwitch(menu=Input(name)) as user_value:
            
            if replaced is None:
                Float(0.0).out(     "Zero")
            else:
                replaced.out(       "No Change")
            
            v.out(                  "Value")
            plank0.width.out(       "Width")
            plank0.length.out(      "Length")
            plank0.thickness.out(   "Thickness")
            plank0.back.out(        "Back")
            plank0.left.out(        "Left")
            plank0.bot.out(         "Bottom")
            plank0.front.out(       "Front")
            plank0.right.out(       "Right")
            plank0.top.out(         "Top")
            plank0.size_x.out(      "Size X")
            plank0.size_y.out(      "Size Y")
            plank0.size_z.out(      "Size Z")
            dist_x.out(             "Distance X")
            dist_y.out(             "Distance Y")
            dist_z.out(             "Distance Z")
            
        no_offset = user_value.value | user_value.node[1]
            
        value = snap(user_value.switch_false(no_offset, user_value + offset))
        
        # ----------------------------------------------------------------------------------------------------
        # Gizmo
        # ----------------------------------------------------------------------------------------------------
        
        gizmo = {}
            
        if USE_GIZMO and gizmo_dir is not None:
            
            g_dir = [0, 0, 0]
            g_dir[gizmo_dir] = 1
            color_id = 'XYZ'[gizmo_dir]
            
            gizmo['gizmo'] = v.linear_gizmo(color_id=color_id, direction=g_dir, draw_style=draw_style)
            
            gizmo['offset'] = offset
            ds = 'ARROW' if replaced is None else 'BOX'
            gizmo['gizmo_offset'] = offset.linear_gizmo(color_id=color_id, direction=g_dir, draw_style=ds)
            
        return value, gizmo


    # ====================================================================================================
    # Locate Plank
    # ====================================================================================================

    with GeoNodes("Locate OLD") as tree:
        
        mesh = Mesh()
        plank_id = Integer(0, "ID", 0)

        plank = G().get_dimensions(mesh, True, plank_id)
        size_x, size_y, size_z = plank.size_x, plank.size_y, plank.size_z
        
        # ---------------------------------------------------------------------------
        # Location
        # ---------------------------------------------------------------------------

        with Panel("X", create_layout=True):
            
            x, gizmo_x = get_cote(mesh, 0.0, "X",  None, gizmo_dir=0, draw_style='CROSS')
            
            with Float.MenuSwitch(menu=Input("X Alignment")) as delta_x:
                Float(0.0).out("In Front")
                Float(size_x/2).out("Centered")
                Float(size_x).out("Behind")
                
        with Panel("Y", create_layout=True):
            
            y, gizmo_y = get_cote(mesh, 0.0, "Y", None, gizmo_dir=1, draw_style='CROSS')
            
            with Float.MenuSwitch(menu=Input("Y Alignment")) as delta_y:
                Float(size_y).out("Left")
                Float(size_y/2).out("Centered")
                Float(0.0).out("Right")
                 
        with Panel("Z", create_layout=True):
            
            z, gizmo_z = get_cote(mesh, 0.0, "Z", None, gizmo_dir=2, draw_style='CROSS')
            
            with Float.MenuSwitch(menu=Input("Z Alignment")) as delta_z:
                Float(size_z).out("Below")
                Float(size_z/2).out("Centered")
                Float(0.0).out("Above")

        # ---------------------------------------------------------------------------
        # Translation
        # ---------------------------------------------------------------------------
        
        # Current origin
        old_x, old_y, old_z = plank.back, plank.left, plank.bot
        
        # Target origin
        ox, oy, oz = x - delta_x, y - delta_y, z - delta_z
        
        # Translate    
        mesh[nd.id.equal(plank_id)].offset = (ox - old_x, oy - old_y, oz - old_z)    
                
        # ---------------------------------------------------------------------------
        # Gizmos
        # ---------------------------------------------------------------------------
                
        if USE_GIZMO:
                        
            with Layout("Gizmo Location"):
                g_pos = (ox + size_x/2, oy + size_y/2, oz + size_z/2)
                gizmo_x['gizmo_offset'].node.position = g_pos
                gizmo_y['gizmo_offset'].node.position = g_pos
                gizmo_z['gizmo_offset'].node.position = g_pos
                
            with Layout("Gizmo Location Offset"):
                g_pos = (ox + size_x/2, oy + size_y/2, oz + size_z/2)
                gizmo_x['gizmo'].node.position = g_pos
                gizmo_y['gizmo'].node.position = g_pos
                gizmo_z['gizmo'].node.position = g_pos

        
        mesh.out("Mesh")
        Vector((ox, oy, oz)).out("Origin")
        Vector((size_x, size_y, size_z)).out("Size")


            
            
            
            
            
        
        
    
    
    
    
    
    
    
    
    
    
 
    
    
    
    
    
    
    
        
        
    
    
    
    
    