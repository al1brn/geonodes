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

module : demo counters
----------------------

Digital and analogic counters

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/counters.py)

The elementay digit can be either digital or analogic.

A digital figure is made of 7 elementary segments with a different material
depending on its state : ON or OFF.

A digital clock is built with 4 digits.

A analog figure is built from font. The value displayed is the floor part
of the value passed to the modifier. The figure is then slightly moved
to simulatue wheel rotation.

A counter is made of a variable number of analog figure.

To be complete, a analogic clock is provided with its default shaders


> [!NOTE]
> Modifiers:
> - Digit
> - Digital Clock
> - Digital Counter
> - Figure
> - Wheels Counter
> - Clock

``` python
from geonodes.demos import counters

counters.demo()
```
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/counters
-----------------------
Generates modifiers for counters: digital counter and wheels counter

Geometry Nodes
--------------
    -

updates
-------
- creation : 2024/08/24
- update   : 2024/09/04
- update   : 2025/01/23 # Analogic Clock
"""

from geonodes import *

def demo(font=None):

    # ====================================================================================================
    # Shaders for digits

    with ShaderNodes("LCD On"):
        ped = Shader.Principled(
            base_color = snd.attribute("Color").color,
            roughness  = .3,
            metallic   = .2,
        )

        ped.out()

    with ShaderNodes("LCD Off"):
        ped = Shader.Principled(
            base_color = Color.CombineHSV(0, 0, 0.396),
            roughness  = .3,
            metallic   = .2,
        )

        ped.out()

    # ====================================================================================================
    # Shaders for figures

    with ShaderNodes("Wheel Figure"):

        wheel_index = snd.attribute("Wheel").factor
        black = Color.Combine(.05, .05, .05)
        red   = Color.Combine(.95, .05, .05)

        col = black.mix(red, factor=wheel_index.compare(0))

        ped = Shader.Principled(
            base_color = col,
            roughness  = .3,
            metallic   = .2,
        )

        ped.out()

    with ShaderNodes("Wheel Background"):

        ped = Shader.Principled(
            base_color = (.95, .95, .95),
            roughness  = .3,
            metallic   = .2,
        )

        ped.out()

    with ShaderNodes("Wheel Box"):

        ped = Shader.Principled(
            #base_color = (.95, .95, .95),
            base_color = snd.attribute("Box Color").color,
            roughness  = .1,
            metallic   = .95,
        )

        ped.out()

        # ===========================================================================
        # A rounded rect
        # ===========================================================================

        with GeoNodes("Rounded Rectangle"):

            """ A rounded rect

            Arguments
            ---------
            - width (Float) : rectangle total width
            - height (Float) : rectangle total height
            - radius (Float) : radius
            - resol (Integer) : number of points (min is 2)
            - axis (str = 'Z') : perpendicular axis
            - geometry (str in ('Mesh', 'Curve')) : the geometry to build
            - fill_type (str in ('NONE', 'NGON', 'TRIANGLE_FAN') : Mesh circle fill type

            Returns
            -------
            - Geometry as requested per geometry argument
            """

            width  = Float(1., "Width", 0)
            height = Float(1., "Height", 0)
            radius = Float(0.01, "Radius", 0)
            resol  = Integer(12, "Resolution", 2, 128)
            fill   = Boolean(False, "Fill Mesh")

            with Layout("Prepare"):

                w, h = width/2, height/2
                l = gnmath.min(w, h)
                r = gnmath.min(radius, l)
                resol = gnmath.max(resol, 2)
                total = resol*4
                
                corner = Mesh.Circle(radius=r, vertices=total-4)
                corner.points[nd.index.greater_than(resol)].delete()
                
            with Geometry.MenuSwitch(menu=Input("Geometry"), default_menu='Curve') as geo: 
                
                with Mesh.Switch(fill) as circle:         
                    Mesh.Circle(vertices=total, fill_type='NONE').out()
                    Mesh.Circle(vertices=total, fill_type='NGON').out()
                circle.out("Mesh")
                
                Curve.Circle(resolution=total).out("Curve")
                
            for i in range(4):
                
                with Layout(f"Part {i+1}/4"):
                    
                    index = nd.index - i*resol
                    if i == 0:
                        geo.position = (w - r, h - r, 0) + corner.points.sample_index(nd.position, index)
                        corner.transform(rotation=(0, 0, pi/2))
                    elif i == 1:
                        sel = nd.index.greater_equal(resol)
                        geo[sel].position = (r - w, h - r, 0) + corner.points.sample_index(nd.position, index)
                        corner.transform(rotation=(0, 0, pi/2))
                    elif i == 2:
                        sel = nd.index.greater_equal(resol*2)
                        geo[sel].position = (r - w, r - h, 0) + corner.points.sample_index(nd.position, index)
                        corner.transform(rotation=(0, 0, pi/2))
                    else:
                        sel = nd.index.greater_equal(resol*3)
                        geo[sel].position = (w - r, r - h, 0) + corner.points.sample_index(nd.position, index)
                        
                    
            geo.out()

        # ===========================================================================
        # A rounded box
        # ===========================================================================

        with GeoNodes("Rounded Box"):

            size   = Vector(1, "Size", min=0.1)
            hrad   = Vector(.1, "H Radius", min=0)
            vrad   = Vector(.1, "V Radius", min=0)
            resol  = Integer(12, "Resolution", 2, 128)

            with Layout("Prepare"):
                
                size_x, size_y, size_z = size.scale(.5).xyz
                vrad = gnmath.min(vrad, gnmath.min(size_z, gnmath.min(size_x, size_y)))
                
                resol = gnmath.max(resol, 2)
                total = resol*4
                
                with Layout("Starting Rectangle"):
                    w = 2*(size_x - vrad)
                    h = 2*(size_y - vrad)
                    base = Group("Rounded Rectangle", 
                        width       = w,
                        height      = h, 
                        radius      = hrad,
                        resolution  = resol,
                        geometry    = 'Mesh', 
                        fill_mesh   = True)._out
                        
                    base = Mesh(base)
                    base.offset = (0, 0, -size_z)
                    
                with Layout("Bottom looping"):

                    for rep in base.repeat(resol - 1, selection=True):
                        
                        ag = (rep.iteration + 1)/(resol-1)*(pi/2)
                        dh = gnmath.sin(ag)*vrad
                        dz = (1 - gnmath.cos(ag))*vrad
                        
                        base = base.edges[rep.selection].extrude((0, 0, dz))
                        top = base.top
                        
                        ring = Group("Rounded Rectangle", 
                            width       = w + dh*2,
                            height      = h + dh*2, 
                            radius      = hrad,
                            resolution  = resol,
                            geometry    = 'Mesh', 
                            fill_mesh   = False)._out
                            
                        ring = Mesh(ring)
                        ring.offset = (0, 0, -size_z + dz)
                            
                        base[top].position = ring.points.sample_index(nd.position, nd.index - total*(rep.iteration + 1))
                            
                        base.out()
                        rep.selection = top
                        
                bot_mesh = Mesh(base)
                        
                with Layout("Vertical Mirror"):
                    
                    top_mesh = Mesh(bot_mesh)
                    top_mesh.transform(rotation=(0, pi, 0))
                    
                    bot_mesh.edges[rep.selection].extrude((0, 0, 2*(size_z - vrad)))
                    
                    box = Mesh(bot_mesh + top_mesh)
                    box.merge_by_distance()
                    
                
                box.faces.shade_smooth = Boolean(True, "Smooth")
                box.faces.material = Material(name="Material")
                    
                box.out("Mesh")        


    # ====================================================================================================
    # A digital digit : each light item is a face
    # ====================================================================================================

    with GeoNodes("G Digit"):

        size  = Float(1, "Size", 0)

        with Panel("Appearance"):
            on_mat     = Material("LCD On", "On")
            off_mat    = Material("LCD Off", "Off")
            shear      = Float.Factor(.4, "Shear", 0, 1)

        with Panel("Options"):
            ok_0       = Boolean(True, "Display 0")
            minus      = Boolean(False, "Minus Sign", tip="Only minus sign")
            positive   = Boolean(False, "Positive", tip="Sign is off (True) or on (False)")

        # ----- Dimensions

        X = size
        Z = size*1.8
        z1 = Z/2
        z0 = -z1
        x1 = X/2
        x0 = -x1

        d = Z*.1
        d2 = d/2
        e = d/10
        
        with Layout("0x10 : Hrz Bottom"):
            item0 = Mesh.Circle(vertices=4, fill_type='NGON')
            item0[0].position = (x0 + e, 0, z0)
            item0[1].position = (x1 - e, 0, z0)
            item0[2].position = (x1 - d - e, 0, z0 + d)
            item0[3].position = (x0 + d + e, 0, z0 + d)

            item0.faces.Mask = int(0x10)
            digit = item0

        with Layout("0x20 : Hrz Middle"):
            item = Mesh.Circle(vertices=6, fill_type='NGON')
            item[0].position = (x0, 0, 0)
            item[1].position = (x0 + d, 0, -d2)
            item[2].position = (x1 - d, 0, -d2)
            item[3].position = (x1, 0, 0)
            item[4].position = (x1 - d, 0, d2)
            item[5].position = (x0 + d, 0, d2)

            item.faces.Mask = int(0x20)
            digit += item

            with Layout("Minus sign"):
                minus_mesh = Mesh(item)
                minus_mesh.material = on_mat.switch(positive, off_mat)

        with Layout("0x40 : Hrz Top"):
            item0.faces.Mask = int(0x40)
            digit += item0.transform(rotation=Rotation.FromEuler((0, pi, 0)))

        with Layout("0x01: Bottom Left"):
            item3 = Mesh.Circle(vertices=4, fill_type='NGON')
            item3[0].position = (x0, 0, z0 + e)
            item3[1].position = (x0 + d, 0, z0 + d + e)
            item3[2].position = (x0 + d, 0, -d2 - e)
            item3[3].position = (x0, 0, -e)
            
            item3.faces.Mask = int(0x01)

            digit += item3

        with Layout("0x02 : Top Left"):
            item4 = Mesh(item3).transform(scale=(1, 1, -1))
            item4.flip_faces()
            
            item4.faces.Mask= int(0x02)

            digit += item4

        with Layout("0x04 : Bottom Right"):
            item4.faces.Mask= int(0x04)
            digit += item4.transform(rotation=Rotation.FromEuler((0, pi, 0)))

        with Layout("0x08 : Top Right"):
            item3.faces.Mask = int(0x08)
            digit += item3.transform(rotation=Rotation.FromEuler((0, pi, 0)))

        with Layout("Shear"):
            digit.offset = (nd.position.z*.4*shear, 0, 0)
            
            
        # 0x10, 0x20, 0x40, Hrz from bot to top
        # 0x01, 0x02,       Vrt Left
        # 0x04, 0x08        Vrt Right

        with Integer.IndexSwitch(index=Input("Value")) as mask:

            Integer(0x5F).out() # 0
            Integer(0x0C).out() # 1
            Integer(0x79).out() # 2
            Integer(0x7C).out() # 3
            Integer(0x2E).out() # 4
            Integer(0x76).out() # 5
            Integer(0x77).out() # 6
            Integer(0x7F).out() # 8
            Integer(0x7E).out() # 9
            
        digit.faces.material = off_mat
        zero_off = Mesh(digit)

        digit.faces[(Integer("Mask") & mask).not_equal(0)].material =  on_mat

        # 0x5F is mask for value 0
        with Layout("Display 0"):
            digit = zero_off.switch(ok_0 | mask.not_equal(0x5F), digit)

        digit.switch(minus, minus_mesh).out("Digit")

    # ====================================================================================================
    # A digital counter
    # ====================================================================================================

    with GeoNodes("Counter Digital"):

        value    = Integer(12, "Value", tip="Value to display")
        digits   = Integer(3, "Digits", 1, 10, tip="Number of digits")
        size     = Float(1, "Size", 0)
        y_offset = Float(-.01, "Y Offset")

        with Panel("Appearance"):
            color = Color((1, 0, 0), "Color")

        with Panel("Options"):
            merge      = Boolean(False, "Merge with Input")
            leading_0  = Boolean(False, "Leading 0", tip="Display leading zero value")
            minus      = Boolean(True, "Minus Sign")

        sign = gnmath.sign(value)
        value = gnmath.abs(value)
        
        size_factor = 1.25

        # Loop on the digits
        
        for rep in Mesh.Repeat(digits, value=value):
            
            mesh = rep.mesh

            mesh.transform(translation=(size_factor*size, 0, 0))
            digit_value = rep.value % 10
            res_value = (rep.value - digit_value)/10
            rep.value = res_value

            digit_node = Group("G Digit", {
                "Value" : digit_value,
                "Size"  : size,
                "Display 0" : leading_0 | rep.iteration.equal(0) | res_value.not_equal(0),
                "Minus Sign" : False,
            })
            digit_node.link_inputs('TREE', "Appearance", panel="Appearance")

            mesh += digit_node.digit
            
            mesh.out()

        mesh = rep.mesh

        # Add the leading sign 

        with Layout("Sign"):

            signed_mesh = Mesh(mesh).transform(translation=(size_factor*size, 0, 0))

            digit = Group("G Digit", {
                "Size"       : size,
                "Minus Sign" : True,
                "Positive"   : sign > 0,
            }).digit
            digit.node.link_inputs('TREE', "Appearance", panel="Appearance")
            signed_mesh = signed_mesh + digit

        # Combine

        mesh = Mesh(mesh).switch(minus, signed_mesh)
        mesh = Mesh(mesh.transform(translation=(0, y_offset, 0)))
        mesh.faces.store("Color", color)
        mesh += Geometry().switch_false(merge)

        mesh.out()

    # ====================================================================================================
    # A digital clock
    # ====================================================================================================

    with GeoNodes("Clock Digital"):

        minutes = Integer(132, "Minutes", tip="Time in minutes")
        size    = Float(1, "Size", 0)

        with Panel("Options"):
            merge      = Boolean(False, "Merge with Input")
            dots_on    = Boolean(True, "Dots are On")

        with Layout("Minutes and hours"):
            mins  = minutes % 60
            hours = (minutes - mins)/60

        with Layout("Minutes"):
            m_mesh = Group("Counter Digital", {
                "Value"            : mins,
                "Digits"           : 2,
                "Leading 0"        : True,
                "Minus Sign"       : False,
                "Merge with Input" : False,
                "Y Offset"         : 0,
            }).geometry

            m_mesh.node.link_inputs(None, "Appearance", panel="Appearance")
            m_mesh = m_mesh.transform(translation=(.8*size, 0, 0))

        with Layout("Hours"):

            h_mesh = Group("Counter Digital", {
                "Value"            : hours,
                "Digits"           : 2,
                "Leading 0"        : False,
                "Minus Sign"       : False,
                "Merge with Input" : False,
                "Y Offset"         : 0,
            }).geometry

            h_mesh.node.link_inputs(None, "Appearance", panel="Appearance")
            h_mesh = h_mesh.transform(translation=(-2.2*size, 0, 0))

        with Layout("Dots"):

            size = Float.Input("Size")
            shear = Float.Input("Shear")

            side = size*.15
            z    = size*.25
            square = Mesh.Grid(size_x=side, size_y=side, vertices_x=2, vertices_y=2).transform(rotation=(halfpi, 0, 0))
            square0 = Mesh(square).transform(translation=(0, 0, -z))
            square1 = square.transform(translation=(0, 0, z))
            squares = square0 + square1
            squares.offset = (nd.position.z*.4*shear, 0, 0)

            squares.material = off_mat.switch(dots_on, on_mat)
            squares.faces._Color = color

        clock = h_mesh + squares + m_mesh
        clock = clock.transform(translation=(0, y_offset, 0))

        clock += Geometry().switch_false(merge)

        clock.out()

    # ====================================================================================================
    # A Figure
    # ====================================================================================================

    with GeoNodes("G Figure"):

        figure     = Float(8, "Figure", 0, tip="Figure with frac part")
        size       = Float(1, "Size", 0)
        continuous = Boolean(False, "Continuous", tip="Move continuously between the figure and the next one using fract part")
        fig_mat    = Material("Wheel Figure", "Figure material")
        back_mat   = Material("Wheel Background", "Background material")

        figure = figure % 10

        fig0 = gnmath.floor(figure)
        fig1 = (fig0 + 1).switch(fig0.equal(9), 0)
        frac = figure - fig0

        with Layout("Figure and next"):
            curve0 = fig0.to_string().to_curves(size=size, align_x='CENTER', align_y='MIDDLE', font = font)
            curve1 = fig1.to_string().to_curves(size=size, align_x='CENTER', align_y='MIDDLE', font = font).transform(translation=(0, -size, 0))

            figure = Curve((curve0 + curve1).realize()).fill()

        with Layout("Intermediary factor"):
            fac = frac.map_range_smooth_step(.5, 1, 0, 1).switch(continuous, frac)

        with Layout("Move the figures"):
            figure = figure.transform(translation=(0, size*fac, 0))

        figure.material = fig_mat

        with Layout("Cut"):
            cut = Mesh.Cube((size, size*1.3, 1))
            figure = figure.intersect(cut)

        back = Mesh.Grid(size_x=size, size_y=1.4*size, vertices_x=2, vertices_y=2)
        back.material = back_mat
        back = back.transform(translation=(0, 0, size*(-.05)))

        figure = back + figure
        figure = figure.transform(rotation=(halfpi, 0, 0))

        figure.out()

    # ====================================================================================================
    # Wheels counter

    with GeoNodes("Counter Wheels"):

        value      = Float(123, "Value", 0, tip="Counter value")
        count      = Integer(3, "Number of Wheels", 1, 10)
        size       = Float(1, "Size", 0)
        fig_mat    = Material("Wheel Figure", "Figure material")
        back_mat   = Material("Wheel Background", "Background material")
        with_box   = Boolean(True, "Create Box")
        box_mat    = Material("Wheel Box", "Box material")
        box_color  = Color((.5, .5, .5), "Box Color")
        box_margin = Float(.3, "Box Margin", .01)
        box_depth  = Float(.5, "Box Depth", .01)
        merge      = Boolean(False, "Merge with input")

        size_factor = 1.05

        for rep in Mesh.Repeat(count, value=value):

            wheels = rep.mesh
            wheels.transform(translation=(size*size_factor, 0, 0))

            fig = rep.value % 10
            new_figure = Mesh(Group("G Figure", {
                "Figure"   : fig,
                "Size"     : size,
                "Continuous" : rep.iteration.equal(0),
                "Figure material" : fig_mat,
                "Background material" : back_mat,
            }).geometry)

            new_figure.faces.Wheel = rep.iteration

            wheels += new_figure

            ifig = gnmath.floor(fig)
            ok9 = ifig.equal(9)
            frac = fig - ifig

            value = gnmath.floor(rep.value/10)
            rep.value = value + Float(0).switch(ok9, frac)
            wheels.out()

        wheels = rep.mesh

        with Layout("Box"):

            bbox = wheels.bounding_box()
            center = (bbox.min_ + bbox.max_).scale(-.5)
            wheels = wheels.transform(translation=center)

            margin = gnmath.max(0.05, box_margin)
            depth  = gnmath.max(0.1, box_depth)

            bbox = wheels.bounding_box()
            wsize = bbox.max - bbox.min
            size = wsize + (margin, depth, margin)

            ext_box = Group("Rounded Box", size=size, h_radius=.1, v_radius=.1, resolution=8, material=box_mat)._out
            ext_box.faces.Color = box_color

            int_box = Mesh.Cube(size = wsize + (-.1, depth, -.1))
            int_box = int_box.transform(translation=(0, -depth/2, 0))

            box = ext_box.difference(int_box)
            box.transform(translation=(0, depth/5, 0))
            box.material = box_mat
            box.faces.Box_Color = box_color


        wheels += box.switch_false(with_box)
        wheels += Geometry().switch_false(merge)


        wheels.out()

    # ====================================================================================================
    # Analogic clock materials
    # ====================================================================================================

    with ShaderNodes("Clock Background"):

        ped = Shader.Principled(
            base_color = (1, 1, 1),
            roughness = .3,
            metallic = 0.,
        )

        ped.out()

    with ShaderNodes("Clock Needles"):

        ped = Shader.Metallic(
            base_color = (0.1, 0.05, 0.05),
            roughness = 0.1,
        )

        ped.out()

    with ShaderNodes("Clock Seconds"):

        ped = Shader.Principled(
            base_color = (1, 0, 0),
            roughness = 0.1,
        )

        ped.out()

    with ShaderNodes("Clock Seconds"):

        ped = Shader.Principled(
            base_color = (1, 0, 0),
            roughness = 0.1,
        )

        ped.out()


    with ShaderNodes("Clock Marks"):

        ped = Shader.Metallic(
            base_color = (0.1, 0.05, 0.05),
            roughness = 0.1,
        )

        ped.out()


    with ShaderNodes("Clock Outer"):

        ped = Shader.Principled(
            base_color = snd.attribute("Color").color,
            roughness = 0.1,
        )

        ped.out()

    # ====================================================================================================
    # Analogic clock
    # ====================================================================================================

    with GeoNodes("Clock Needles"):

        t          = Float(438, "Time", tip="Time in seconds")

        show_hours = Boolean(True, "Hours")
        show_mins  = Boolean(True, "Minutes")
        show_secs  = Boolean(True, "Seconds")
        show_torus = Boolean(True, "Outer")

        radius     = Float(1, "Radius", 0)
        torus_r    = Float.Percentage(5, "Outer Radius", 1, 25)

        back_mat   = Material("Clock Background", "Background")
        marks_mat  = Material("Clock Marks", "Marks")
        needle_mat = Material("Clock Needles", "Needles")
        sec_mat    = Material("Clock Seconds", "Seconds Needle")
        torus_mat  = Material("Clock Outer", "Outer")

        color      = Color((0, 0, 1), "Color")

        with Panel("Brand"):
            brand = String("Les Idées Froides", "Brand")
            brand_mat = Material("Clock Outer", "Material")
            brand_col = Color(0, "Color")


        h_marks = .04
        h_needle = 0.01

        with Layout("Base Circle"):

            circle = Mesh.Circle(vertices=12).to_points()
            hours_circle = Cloud(circle.points[(nd.index % 3).equal(0)].separate())
            min_circle = Cloud(hours_circle.inverted_)

        with Layout("Minutes Marks"):

            l = .15
            scale = (1 - l/2)
            min_circle.transform(scale=scale)

            mark = Mesh.Cube(size=(l, .05, h_marks))
            marks = min_circle.instance_on(instance=mark, rotation=Rotation.AlignXToVector(nd.position))

        clock = marks


        with Layout("Hours Marks"):

            l = .25
            scale = (1 - l/2)
            hours_circle.transform(scale=scale)

            mark = Mesh.Cube(size=(l, .05, h_marks))

            marks = hours_circle.instance_on(instance=mark, rotation=Rotation.AlignXToVector(nd.position))

        clock += marks

        with Layout("Seconds Marks"):

            l = .1
            scale = (1 - l/2)
            sec_circle = Mesh.Circle(radius=scale, vertices=60).to_points()
            sec_circle.points[(nd.index % 5).equal(0)].delete()

            mark = Mesh.Cube(size=(l, .01, h_marks))

            marks = sec_circle.instance_on(instance=mark, rotation=Rotation.AlignXToVector(nd.position))

        clock += marks
        clock.transform(translation=(0, 0, h_marks/2))
        clock.material = marks_mat

        with Layout("Hours Needle"):

            l = .5
            r = .1

            z = Float(h_marks + .1*h_needle)

            needle = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=r, size_y=r).transform(translation=(0, 0, z), rotation=(0, 0, pi/4))
            needle.points[2].offset = (l - r/2, 0, 0)

            angle = gnmath.radians(((t/360) % 60)*(-6) + 90)
            needle.transform(rotation=(0, 0, angle))

            needle.faces.material = needle_mat

            needles = needle.switch_false(show_hours)
            z = z.switch(show_hours, z + 1.1*h_needle)

        with Layout("Minutes Needle"):

            l = .75
            r = .08

            needle = Mesh.Grid(vertices_x=2, vertices_y=2, size_x=r, size_y=r).transform(translation=(0, 0, z), rotation=(0, 0, pi/4))
            needle.points[2].offset = (l - r/2, 0, 0)

            angle = gnmath.radians(((t/60) % 60)*(-6) + 90)
            needle.transform(rotation=(0, 0, angle))

            needle.faces.material = needle_mat

            needles += needle.switch_false(show_mins)
            z = z.switch(show_mins, z + 1.1*h_needle)

        with Layout("Seconds Needle"):

            l = .9

            angle = gnmath.radians(gnmath.floor(t % 60)*(-6) + 90)
            needle = Mesh.Circle(radius=.04, fill_type='NGON').transform(translation=(0, 0, z))
            #needle.faces.smooth = True
            needle += Mesh.Grid(size_x = l, size_y=.02, vertices_x = 2, vertices_y=2).transform(translation=(l/2, 0, z)).transform(rotation=(0, 0, angle))

            needle.faces.material = sec_mat

            needles += needle.switch_false(show_secs)
            z = z.switch(show_secs, z + 1.1*h_needle)


        needles = (Mesh(needles).flip_faces() + Mesh(needles).faces.extrude(offset=(0, 0, h_needle))).merge_by_distance()
        clock += needles

        with Layout("Needle Center"):

            h = z + h_needle
            cyl = Mesh.Cylinder(radius=.01, vertices=12, fill_type='NGON', depth=h).transform(translation=(0, 0, h/2))
            cyl.faces.material = needle_mat
            cyl.faces.smooth=True

        clock += cyl

        with Layout("Background"):

            if True:
                h = torus_r/100
                back = Mesh.Cylinder(radius=1.05 + h, vertices=64, fill_type='NGON', depth=h).transform(translation=(0, 0, -h/2))
                back.faces.material = torus_mat
                back.faces[0].material = back_mat

            else:
                back = Mesh.Circle(radius=1.05, vertices=64, fill_type='NGON')
                back.faces.material = back_mat


        clock += back

        with Layout("Torus"):

            r = torus_r/100

            torus = Curve.Circle(radius=1.05 + r, resolution=64).to_mesh(profile_curve=Curve.Circle(radius=r, resolution=12))
            torus.faces.material = torus_mat
            torus.faces.smooth = True

            clock += torus.switch_false(show_torus)

        clock = Mesh(clock)
        clock.faces.Color = color

        with Layout("Brand"):
            txt = brand.to_curves(
                size = 1,
                align_x = 'CENTER',
                align_y = 'MIDDLE',
                font=font).realize()
            txt = Curve(txt).fill()

            stats = txt.points.attribute_statistic(nd.position)
            sx, sy, _ = (stats.max_ - stats.min_).xyz

            xmax, ymax = 1.25, 0.45
            scale = gnmath.min(xmax/sx, ymax/sy)
            txt.transform(translation = (0, -0.8*ymax, 0.01), scale=scale)

            txt = Mesh(txt)
            txt.faces.material = brand_mat
            txt.faces.Color = brand_col

            clock += txt

        with Layout("Finalize"):
            clock.transform(scale=radius, rotation=Rotation((pi/2, 0, 0)))

        clock.out()
