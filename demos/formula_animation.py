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

module : demo formula animation
-------------------------------

This modules provide mesh animation based on the Integer attribute 'char_index'.

The formula is built with npblender Formula class

updates
-------
- creation :   2026/07/10

"""

from geonodes import *

# ====================================================================================================
# Formula utilities
# ====================================================================================================

def demo():

    # ----------------------------------------------------------------------------------------------------
    # Constant
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Frm Char Space", is_group=True, color_tag="Input"):
        Float(0.02).out("Char Space")

    def get_char_space():
        return G()._frm_char_space()

    # ----------------------------------------------------------------------------------------------------
    # Char selection
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Selection", is_group=True):
        
        merge = Boolean(False, "Merge", hide=True)
        index = Integer(0, "Char Index")
        count = Integer(1, "Count", 0)
        
        idx = Integer("char_index")
        sel = (idx >= index) & (idx < index + count)
        
        (merge | sel).out("Selection")

    def selection_input(name="Selection"):
        with Layout("Selection Input"):
            use_index = Boolean(False, "Use Index")
            sel = Boolean(True, name=name, hide=True)
            index = Integer(0, "Char Index")
            count = Integer(1, "Count", 0)

            return Boolean.Switch(use_index,
                        sel,
                        G().frm_selection(char_index=index, count=count),
                        )
        
    # ----------------------------------------------------------------------------------------------------
    # Show indices
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Frm Show Indices"):
        mesh = Mesh()
        show = Boolean(True, "Show")
        size = Float(0.1, "Size")
        mat = Material("Arrow", "Material")
        color = Color("White", "Color")

        count = mesh.faces.attribute_statistic(Integer("char_index")).max_.to_integer()+1
        for rep in repeat(count, labels=None):
            node = mesh.points[Integer("char_index") == rep.iteration].attribute_statistic(nd.position).node
            center = (node.min + node.max).scale(0.5)
            label = Curve(rep.iteration.to_string().to_curves(
                size=size,
                align_x = 'Center',
                align_y = 'Middle',
                ).realize()).fill()
            label.offset = center + (0.0, 0.0, 0.1)
 
            rep.labels += label

        labels = Mesh(rep.labels)
        labels.faces.material = mat
        labels.faces.Color = color

        mesh += labels.switch_false(show)
        mesh.out()

    # ----------------------------------------------------------------------------------------------------
    # Group
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Group Indices"):

        mesh = Mesh()
        index = Integer(0, "Char Index")
        count = Integer(1, "Count", 0)

        idx = Integer("char_index")
        sel = (idx >= index) & (idx < index + count)
        mesh.faces[sel].store_named_attribute("char_index", index)

        mesh.out()


    # ----------------------------------------------------------------------------------------------------
    # Dimensions of a selection
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Frm Dims", is_group=True):
        
        mesh = Mesh()
        sel = Boolean(True, "Selection",hide=True)
        
        node = mesh.points[sel].attribute_statistic(nd.position).node
        
        vmin = node.min
        vmax = node.max + (get_char_space(), 0, 0)
        
        center = (vmin + vmax).scale(0.5)
        size = vmax - vmin
        
        vmin.out("Min")
        vmax.out("Max")
        center.out("Center")
        size.out("Size")
        
        vmin.x.out("X Min")
        vmax.x.out("X Max")
        center.x.out("X Center")
        size.x.out("X Size")
        
    # ----------------------------------------------------------------------------------------------------
    # Select chars after a given position
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Frm Shift After", is_group=True):
        
        mesh = Mesh()
        merge = Boolean(False, "Merge", hide=True)
        exclude = Boolean(False, "Exclude", hide=True)
        x_from = Float(0.0, "After X")
        x_to = Float(0.0, "Shift To X")
        fac = Float.Factor(1.0, "Factor", 0, 1)
        
        count = mesh.points.attribute_statistic(Integer("char_index")).max_.to_integer() + 1
        
        for rep in repeat(count, mesh=mesh, merge=merge, not_excluded=exclude.bnot()):
            
            sel = Integer("char_index") == rep.iteration
            xmin = rep.mesh.points[sel].attribute_statistic(nd.position.x).mean_
            rep.mesh.points[sel].SEL = (rep.merge | (xmin >= x_from)) & rep.not_excluded
            
        mesh = rep.mesh
            
        selection = Boolean("SEL")
        
        mesh[selection].offset = ((x_to - x_from)*fac, 0.0, 0.0)
        
        sel = mesh.points.capture_attribute(selection)
        mesh.remove_named_attribute("Exact", "SEL")
        
        mesh.out()
        sel.out("After")
        
    # ----------------------------------------------------------------------------------------------------
    # Transform a selection
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Transform"):
        
        mesh = Mesh()
        sel = selection_input("Selection")
        
        x_scale = Float(1.0, "X Scale", 0.0)
        z_rot = Float.Angle(0.0, "Z Rotation")
        x_shift = Float(0.0, "X Shift")
        
        translation = Vector(name="Translation")
        rotation = Rotation(name="Rotation")
        scale = Vector(1.0, "Scale")
        pivot = Vector(name="Pivot")
        
        shift_before = Float.Factor(1.0, "Shift Before", 0, 1)
        shift_after = Float.Factor(1.0, "Shift After", 0, 1)
        
        
        with Layout("Separate"):
            
            sel_mesh = Mesh(mesh.points[sel].separate().selection)
            rem_mesh = Mesh(sel_mesh.inverted)
            
            dims = G().frm_dims(sel_mesh)
            rem_mesh = G().frm_shift_after(rem_mesh,
                after_x=dims.x_max, 
                shift_to_x=dims.x_min, 
                factor=shift_before)
                
        with Layout("X Scale and Z Rotation"):
            
            sel_mesh.offset = -dims.center
            
            x, y, z = nd.position.xyz
            x *= x_scale
            
            cag, sag = z_rot.cos(), z_rot.sin()
            x_ = cag*x - sag*y
            y_ = sag*x + cag*y
            
            x_ -= (dims.x_size/2)*(1.0 - x_scale)
            
            sel_mesh.position = (x_ + x_shift, y_, z)
            
            sel_mesh.offset = dims.center
            
        with Layout("General Transformation"):
            
            dims = G().frm_dims(sel_mesh)
            pivot += dims.center
            
            sel_mesh.offset = -pivot
            sel_mesh.transform(translation=translation, rotation=rotation, scale=scale)
            sel_mesh.offset = pivot
            
            
        with Layout("Merge the chars"):
            
            dims = G().frm_dims(sel_mesh)
            rem_mesh = G().frm_shift_after(rem_mesh, 
                after_x=dims.x_min, 
                shift_to_x=dims.x_max,
                factor=shift_after)
                
            mesh = Mesh(rem_mesh + sel_mesh)
            
        mesh.out()
        
        
    # ----------------------------------------------------------------------------------------------------
    # Replace
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Replace", is_group=True):
        
        mesh = Mesh()
        with Panel("Selection"):
            sel0 = selection_input()

        with Panel("Replace By"):
            sel1 = selection_input()

        fac  = Float.Factor(0.5, "Factor", 0.0, 1.0)
        x_scale = Float.Factor(1.0, "X Scale", 0.0, 1.0)
        
        dims0 = G().frm_dims(mesh, sel0)
        dims1 = G().frm_dims(mesh, sel1)
        
        mesh = G().frm_transform(mesh, selection=sel1, x_shift=dims0.x_max - dims1.x_min)
        
        mesh = G().frm_transform(mesh, selection=sel0, x_scale=(1.0 - fac))
        mesh = G().frm_transform(mesh, selection=sel1, x_scale=fac)

        mesh = G().frm_transform(mesh, selection=sel0 | sel1, x_scale=x_scale)
        
        mesh.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Displace
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Displace", is_group=True):
        
        mesh = Mesh()
        with Panel("Selection"):
            sel0 = selection_input()
        with Panel("Displace To"):
            sel1 = selection_input()
        use_after = Boolean(True, "After")
        y_max = Float(1.0, "Y max")
        fac  = Float.Factor(0.5, "Factor", 0.0, 1.0)

        with Layout("Start / end positions"):
            
            dims0 = G().frm_dims(mesh, sel0)

            target = G().frm_transform(mesh, selection=sel0, x_scale=0.0)
            dims1 = G().frm_dims(target, sel1)
            #dims1 = G().frm_dims(mesh, sel1)
        
            with Float.Switch(use_after) as x_shift:
                (dims1.x_max - dims0.x_min).out("True") 
                
            with x_shift:
                (dims1.x_min - dims0.x_min).out("False")

        with Layout("Current x and y"):
            easing = fac*fac*(3 - 2*fac)
            delta_x = x_shift*easing
            delta_y = y_max*(gnmath.sin(pi*fac)**0.5)

        with Layout("Gaps"):
            gap = 0.4
            shift_before = fac.map_range(0, gap, 0.0, 1.0, interpolation_type="Smooth Step")
            shift_after = fac.map_range(1.0 - gap, 1.0, 0.0, 1.0, interpolation_type="Smooth Step")
        
        mesh = G().frm_transform(mesh, selection=sel0, 
            translation=(delta_x, delta_y, 0), 
            shift_before=shift_before, 
            shift_after=shift_after)
        
        mesh.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Move
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Move", is_group=True):
        
        mesh = Mesh()
        sel  = selection_input()
        
        translation = Vector(name="Translation")
        rotation = Rotation(name="Rotation")
        scale = Vector(1, name="Scale")
        pivot = Vector(name="Pivot")
        
        close_fac = Float.Factor(0.4, "Close At", 0, 1)
        fac  = Float.Factor(0.5, "Factor", 0.0, 1.0)
        x_scale = Float.Factor(1.0, "X Scale", 0.0, 1.0)
        
        vec_fac = Vector(fac)
        
        mesh = G().frm_transform(mesh, selection=sel,
            x_scale=x_scale,
            translation=translation.scale(fac),
            rotation=vec_fac.map_range(to_min=0.0, to_max=rotation),
            scale=vec_fac.map_range(to_min=1.0, to_max=scale),
            pivot=pivot,
            shift_before=1.0, #fac.map_range(0, close_fac, 1, 0),
            shift_after =fac.map_range(0, close_fac, 1, 0),
            )
        
        mesh.out()
        
    # ----------------------------------------------------------------------------------------------------
    # Write animation
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Frm Write"):

        mesh = Mesh()
        show = Boolean(True, "Show")
        use_index = Boolean(False, "Use Char Index")

        to_x = Float(100.0, "Up to X")
        to_index = Integer(100, "Up to Index")

        with Mesh.Switch(use_index) as start_mesh:

            mesh_after = G().frm_shift_after(mesh, after_x=to_x, shift_to_x=to_x)
            mesh_after.points[mesh_after.after].separate().inverted.out("False")

        with start_mesh:
            Mesh(mesh).faces[Integer("char_index") > to_index].delete().out("True")

        Mesh(start_mesh.switch_false(show)).out()


