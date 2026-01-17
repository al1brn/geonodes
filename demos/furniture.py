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

# FONT DEFAULT
FONT_SIZE = 0.1
SECTION   = 0.01


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
        
        i_axis      = Integer(0, "Axis", 0, 2)
        show        = Boolean(True, "Show")
        p0          = Vector(0, "From")
        p1          = Vector((1, 0, 0), "To")
        font_size   = Float(FONT_SIZE, "Font Size", 0.01)
        section     = Float(SECTION, "Section", 0)
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
        # Along axis
        # ---------------------------------------------------------------------------

        #axis = String.IndexSwitch("X", "Y", "Z", index=i_axis)

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
    # Duplicate a plank
    # ====================================================================================================

    with GeoNodes("Duplicate Plank"):

        mesh = Mesh()
        plank_id = Integer(0, "Plank ID", 0)
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
            plank = G().get_dimensions(mesh, True, plank_id)
            plank_dims = plank.node
            center = (plank.min_ + plank.max_)/2
            O = center + trans
            orient = plank.orientation

            x_offset.linear_gizmo(position = O, direction=(1, 0, 0), color_id='X')
            y_offset.linear_gizmo(position = O, direction=(0, 1, 0), color_id='Y')
            z_offset.linear_gizmo(position = O, direction=(0, 0, 1), color_id='Z')

        for rep_count in repeat(count, mesh=mesh, last_id=0):

            cur_trans = trans.scale(rep_count.iteration + 1)

            for rep_linked in repeat(1 + linked, mesh=rep_count.mesh, plank_id=plank_id, last_id=0):

                plank = G().get_dimensions(rep_linked.mesh, True, rep_linked.plank_id)
                orient = plank.orientation

                plank.offset = cur_trans
                rep_linked.mesh = G().add_plank(rep_linked.mesh, plank, orientation=orient)
                rep_linked.plank_id += 1
                rep_linked.last_id = rep_linked.mesh.plank_id

            rep_count.mesh = rep_linked.mesh
            rep_count.last_id = rep_linked.last_id

        # ---------------------------------------------------------------------------
        # Cotes
        # ---------------------------------------------------------------------------

        mesh = rep_count.mesh

        x0, y0, z0 = center.xyz
        negative = x_offset.less_than(0)
        x = plank_dims.front.switch(negative, plank_dims.back)
        d = (x_offset - plank_dims.size_x).switch(negative, x_offset + plank_dims.size_x)
        cote = G().cote_line(
            axis        = 0,
            show        = Boolean(False, "Cote", panel="X") & x_change,
            from_       = (x,     y0, z0),
            to          = (x + d, y0, z0),
            font_size   = FONT_SIZE,
            section     = SECTION,
            invert      = Boolean(False, "Invert", panel="X"),
            ).link_inputs(None, "X")
        mesh += cote

        negative = y_offset.less_than(0)
        y = plank_dims.right.switch(negative, plank_dims.left)
        d = (y_offset - plank_dims.size_y).switch(negative, y_offset + plank_dims.size_y)
        cote = G().cote_line(
            axis        = 1,
            show        = Boolean(False, "Cote", panel="Y") & y_change,
            from_       = (x0, y    , z0),
            to          = (x0, y + d, z0),
            font_size   = FONT_SIZE,
            section     = SECTION,
            invert      = Boolean(False, "Invert", panel="Y"),
            ).link_inputs(None, "Y")
        mesh += cote

        negative = z_offset.less_than(0)
        z = plank_dims.top.switch(negative, plank_dims.bot)
        d = (z_offset - plank_dims.size_z).switch(negative, z_offset + plank_dims.size_z)
        cote = G().cote_line(
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
        rep_count.last_id.out("Plank ID")
        (count * (linked + 1)).out("Total")

    # ====================================================================================================
    # Rotate a Plank
    # ====================================================================================================

    with GeoNodes("Rotate Plank"):

        mesh     = Mesh()
        plank_id = Integer(0, "Plank ID", 0)
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

        plank = G().get_dimensions(mesh, True, plank_id)

        with Layout("Pivot"):
            pivot = plank.min_ + plank.size * (x_factor, y_factor, z_factor)

        with Layout("Rotation"):
            rot = Rotation.IndexSwitch((clip_angle, 0, 0), (0, clip_angle, 0), (0, 0, clip_angle), index=i_axis)

        with Layout("Rotate the positions around pivot"):
            p = pivot + (rot @ (nd.position - pivot))

            mesh[nd.id.greater_equal(plank_id) & nd.id.less_equal(plank_id + linked)].position = p

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        gizmo = angle.dial_gizmo(
            position = pivot,
            up = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
        )

        mesh.out()
        plank_id.out("Plank ID")

    # ====================================================================================================
    # Translate a Plank
    # ====================================================================================================

    with GeoNodes("Translate Plank"):

        mesh     = Mesh()
        plank_id = Integer(0, "Plank ID", 0)
        linked   = Integer(0, "Linked", 0)

        i_axis = Integer(0, "Axis", 0, 2)
        with Panel("Value"):
            value    = Float.Distance( 0.0, "Value")
            val_min  = Float.Distance(-1.0, "Min")
            val_max  = Float.Distance( 1.0, "Max")

            clip_value = gnmath.min(gnmath.max(val_min, value), val_max)

        with Layout("Vector Offset"):
            trans = Vector.IndexSwitch((clip_value, 0, 0), (0, clip_value, 0), (0, 0, clip_value), index=i_axis)
            mesh[nd.id.greater_equal(plank_id) & nd.id.less_equal(plank_id + linked)].offset = trans

        # ---------------------------------------------------------------------------
        # Gizmo
        # ---------------------------------------------------------------------------

        with Layout("Gizmo"):

            plank = G().get_dimensions(mesh, True, plank_id)
            O = (plank.min_ + plank.max_)/2

            value.linear_gizmo(
                position = O,
                direction = Vector.IndexSwitch((1, 0, 0), (0, 1, 0), (0, 0, 1), index=i_axis),
            )

        mesh.out()
        plank_id.out("Plank ID")

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
        
            id0 = Integer(0, "Plank ID")
            
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
            
                id0 = Integer(0, "Plank ID")
                
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
        plank_id = Integer(0, "ID", 0)
        model_id = Integer(0, "Model ID", 0)

        plank = G().get_dimensions(mesh, True, plank_id)
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
        mesh[nd.id.equal(plank_id)].offset = (ox - old_x, oy - old_y, oz - old_z)    
        
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
        new_id = mesh.plank_id

        # ---------------------------------------------------------------------------
        # Locate
        # ---------------------------------------------------------------------------
        
        node = Group("Locate", mesh = mesh, id = mesh.plank_id, model_id=model_id).link_inputs()
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
        new_id.out("Plank ID")
        
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
            
            "X > X"         : 'X Max',
            "X > Alignment" : 'Behind',
            "X > Plank ID"  : left_id,
            "X > Offset"    : -setback1,
            
            "Y > Y"         : 'Y Max',
            "Y > Alignment" : 'Right',
            "Y Plank ID"    : left_id,
            },
            
            mesh        = mesh,
            orientation =  "Horizontal",
            
        ).link_inputs(None, include=["From Model", "Thickness", "Z"])

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

        node = Group("Plank", {
            "Width > Plank ID"  : plank_id,
            "Width > Width"     : 'Z Min',
            
            "Length > Plank ID" : plank_id,
            "Length > Length"   : 'Length',
            "Length > Offset"   : left_ofs + right_ofs,
            
            "X > Alignment"     : 'Behind',
            "X > X"             : 'X Max',
            "X > Plank ID"      : plank_id,
            "X > Offset"        : -setback,
            
            "Y > Alignment"     : 'Right',
            "Y > Y"             : 'Y Min',
            "Y Plank ID"        : plank_id,
            "Y > Offset"        : -left_ofs,
            
            "Z > Alignment"     : 'Above',
            "Z > Z"             : 'Zero',
            },
            
            mesh        = mesh,
            orientation =  "Front",
            
        ).link_inputs(None, include=["From Model", "Thickness"])

        node.out()

    # ====================================================================================================
    # Door
    # ====================================================================================================

    with GeoNodes("Door"):
        
        mesh = Mesh()

        inside = Boolean(True,  "Inside")
        double = Boolean(False, "Double")

        count  = Integer(1, "Count")
        margin = Float.Distance(0.002, "Margin")
        over   = Float.Distance(0.007, "Over")

        with Panel("Opening"):
            right_hinge = Boolean(False, "Right Hinge")
            angle = Float.Angle(0, "Angle", 0, pi)
            
        # ---------------------------------------------------------------------------
        # Dimensions
        # ---------------------------------------------------------------------------
        
        with Panel("Left", create_layout=True):
            left, _ = ask_location(mesh, "Left", i_axis=1, default_value=0.0)
            
        with Panel("Right", create_layout=True):
            right, _ = ask_location(mesh, "Right", i_axis=1, default_value=0.8)
            
        with Panel("Bottom", create_layout=True):
            bot, _ = ask_location(mesh, "Bottom", i_axis=2, default_value=0.0)

        with Panel("Top", create_layout=True):
            top, _ = ask_location(mesh, "Top", i_axis=2, default_value=1.0)

        with Panel("Front", create_layout=True):
            front, _ = ask_location(mesh, "Top", i_axis=0, default_value=1.0)

        y0 = Float.Switch(inside, left  - over, left  + margin)
        y1 = Float.Switch(inside, right + over, right - margin)
        z0 = Float.Switch(inside, bot   - over, bot   + margin)
        z1 = Float.Switch(inside, top   + over, top   - margin)

        # ---------------------------------------------------------------------------
        # Loop on the doors
        # ---------------------------------------------------------------------------

        with Layout("Build a Door"):

            width = y1 - y0
            width = width.switch(double, width/2 - margin)

            node = Group("Plank", {
                "Width > Width"     : 'Value',
                "Width > Value"     : width,
                
                "Length > Length"   : 'Value',
                "Length > Value"    : z1 - z0,
                
                "X > Alignment"     : 'In Front',
                "X > X"             : 'Value',
                "X > Value"         : front,
                
                "Y > Alignment"     : 'Right',
                "Y > Y"             : 'Value',
                "Y > Value"         : y0,
                
                "Z > Alignment"     : 'Above',
                "Z > Z"             : 'Value',
                "Z > Value"         : z0,
                },
                mesh        = mesh,
                orientation =  "Vertical",
                
            ).link_inputs(None, include=["From Model", "Thickness"])

            left_id = node.plank_id

            with Layout("Behind"):
                new_node = node.duplicate_node()
                new_node.x_alignment = 'Behind'

                mesh = node._out.switch(inside, new_node._out)

        with Layout("Second Door"):

            mesh2 = G().duplicate_plank(mesh, left_id, translate_y=True, offset_y=width + 2*margin)
            right_id = mesh2.plank_id

            mesh = mesh.switch(double, mesh2)

        mesh.out()
        left_id.out("Plank ID")
        right_id.enable_output(double).out("Right ID")

    # ====================================================================================================
    # Drawer
    # ====================================================================================================

    with GeoNodes("Drawer"):

        mesh = Mesh()

        mesh = G().door(mesh=mesh, double=False).link_inputs(None, "Drawer Front")
        front_id = mesh.plank_id

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
                left_id = mesh.plank_id

            with Layout("Duplicate for right side"):
                mesh = G().duplicate_plank(
                    mesh        = mesh,
                    plank_id    = left_id,
                    count       = 1,
                    translate_y = True,
                    offset_y    = sy - 2*sb_side - side_thick,
                )
                right_id = mesh.plank_id

            # ---------------------------------------------------------------------------
            # Back Panel
            # ---------------------------------------------------------------------------

            with Layout("Back"):

                mesh = Group("Plank", {
                    "From Model > Model"     : 'Plank ID',
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
                back_id = mesh.plank_id

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
                bot_id = mesh.plank_id

        with Panel("Opening", create_layout=True):

            mesh = G().translate_plank(
                mesh     = mesh,
                plank_id = front_id,
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
            rep.cloud.points[sel].Dimensions = plank.points.sample_index(Vector("Dimensions"), index=rep.iteration)
            rep.cloud[sel].position = plank.points.attribute_statistic(nd.position).mean
            
        cloud = rep.cloud
        cloud.set_id(nd.index)
            
        cloud.out()


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
                          
                
            
                
                
                
