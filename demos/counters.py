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


> [!NOTE]
> Modifiers:
> - Digit
> - Digital Clock
> - Digital Counter
> - Figure
> - Wheels Counter

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
- update   : 20242/09/04
"""

from geonodes import *

def demo():

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

        wheel_index = snd.attribute("Wheel").fac
        black = Color.Combine(.05, .05, .05)
        red   = Color.Combine(.95, .05, .05)

        #col = black.mix(red, fac=wheel_index.equal(0))
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
            base_color = (.95, .95, .95),
            roughness  = .1,
            metallic   = .95,
        )

        ped.out()

    # ====================================================================================================
    # A digital digit : each light item is a face

    with GeoNodes("Digit"):

        value = Integer(8, "Value", 0, 9, tip="Digit value")
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

        with Layout("Item 0"):
            item0 = Mesh.Circle(vertices=4, fill_type='NGON')
            item0[0].position = (x0 + e, 0, z0)
            item0[1].position = (x1 - e, 0, z0)
            item0[2].position = (x1 - d - e, 0, z0 + d)
            item0[3].position = (x0 + d + e, 0, z0 + d)

            digit = item0

        with Layout("Item 1"):
            item = Mesh.Circle(vertices=6, fill_type='NGON')
            item[0].position = (x0, 0, 0)
            item[1].position = (x0 + d, 0, -d2)
            item[2].position = (x1 - d, 0, -d2)
            item[3].position = (x1, 0, 0)
            item[4].position = (x1 - d, 0, d2)
            item[5].position = (x0 + d, 0, d2)

            digit += item

            with Layout("Minus sign"):
                minus_mesh = Mesh(item)
                minus_mesh.material = on_mat.switch(positive, off_mat)

        with Layout("Item 2"):
            digit += item0.transform(rotation=Rotation.FromEuler((0, pi, 0)))

        with Layout("Item 3"):
            item3 = Mesh.Circle(vertices=4, fill_type='NGON')
            item3[0].position = (x0, 0, z0 + e)
            item3[1].position = (x0 + d, 0, z0 + d + e)
            item3[2].position = (x0 + d, 0, -d2 - e)
            item3[3].position = (x0, 0, -e)

            digit += item3

        with Layout("Item 4"):
            item4 = Mesh(item3).transform(scale=(1, 1, -1))
            item4.flip_faces()

            digit += item4

        with Layout("Item 5"):
            digit += item4.transform(rotation=Rotation.FromEuler((0, pi, 0)))

        with Layout("Item 6"):
            digit += item3.transform(rotation=Rotation.FromEuler((0, pi, 0)))

        with Layout("Shear"):
            digit.offset = (nd.position.z*.4*shear, 0, 0)

        with Layout("On / Off"):

            digit.material = off_mat
            zero_off = Mesh(digit)

            with Layout("Horizontal Bottom"):
                digit[0].material = on_mat.switch(value.equal(1) | value.equal(4) | value.equal(7), off_mat)

            with Layout("Horizontal Middle"):
                digit[1].material = on_mat.switch(value.equal(0) | value.equal(1) | value.equal(7), off_mat)

            with Layout("Horizontal Top"):
                digit[2].material = on_mat.switch(value.equal(1) | value.equal(4), off_mat)

            with Layout("Vertical Left Bottom"):
                digit[3].material = off_mat.switch(value.equal(0) | value.equal(2) | value.equal(6) | value.equal(8), on_mat)

            with Layout("Vertical Left Top"):
                digit[4].material = off_mat.switch(value.equal(0) | value.equal(4) | value.equal(5) | value.equal(6) | (value >= 8), on_mat)

            with Layout("Vertical Right Bottom"):
                digit[5].material = on_mat.switch(value.equal(2), off_mat)

            with Layout("Vertical Right Top"):
                digit[6].material = on_mat.switch(value.equal(5) | value.equal(6), off_mat)

        with Layout("Display 0"):
            digit = zero_off.switch(ok_0 | value.not_equal(0), digit)

        digit.switch(minus, minus_mesh).out()

    # ====================================================================================================
    # A digital counter

    with GeoNodes("Digital Counter"):

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

        size_factor = 1.25

        with Repeat(mesh=None, value=value, index = 0, iterations=digits) as rep:

            rep.mesh.transform(translation=(size_factor*size, 0, 0))
            digit_value = rep.value % 10
            res_value = (rep.value - digit_value)/10
            rep.value = res_value

            digit_node = Group("Digit", {
                "Value" : digit_value,
                "Size"  : size,
                "Display 0" : leading_0 | rep.index.equal(0) | res_value.not_equal(0),
                "Minus Sign" : False,
            }, link_from='TREE')

            rep.index += 1
            rep.mesh += digit_node.geometry

        mesh = rep.mesh

        with Layout("Sign"):
            signed_mesh = Mesh(mesh).transform(translation=(size_factor*size, 0, 0))

            signed_mesh = signed_mesh + Group("Digit", {
                "Size"       : size,
                "Minus Sign" : True,
                "Positive"   : sign > 0,
            }, link_from='TREE').geometry

        mesh = Mesh(mesh).switch(minus, signed_mesh)
        mesh.transform(translation=(0, y_offset, 0))
        mesh.faces.store("Color", color)
        mesh += Geometry.Switch(merge, None, Geometry())

        mesh.out()

    # ====================================================================================================
    # A digital clock

    with GeoNodes("Digital Clock"):

        minutes = Integer(132, "Minutes", tip="Time in minutes")
        size    = Float(1, "Size", 0)

        with Panel("Options"):
            merge      = Boolean(False, "Merge with Input")
            dots_on    = Boolean(True, "Dots are On")

        mins  = minutes % 60
        hours = (minutes - mins)/60

        m_mesh = Group("Digital Counter", {
            "Value"            : mins,
            "Digits"           : 2,
            "Leading 0"        : True,
            "Minus Sign"       : False,
            "Merge with Input" : False,
            "Y Offset"         : 0,
        }, link_from='TREE').geometry

        m_mesh = m_mesh.transform(translation=(.8*size, 0, 0))

        h_mesh = Group("Digital Counter", {
            "Value"            : hours,
            "Digits"           : 2,
            "Leading 0"        : False,
            "Minus Sign"       : False,
            "Merge with Input" : False,
            "Y Offset"         : 0,
        }, link_from='TREE').geometry

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

        #h_mesh._lc("h_mesh", (1, 0, 0))
        #squares._lc("squares", (1, 0, 0))
        #m_mesh._lc("m_mesh", (1, 0, 0))

        clock = h_mesh + squares + m_mesh
        clock = clock.transform(translation=(0, y_offset, 0))

        clock += Geometry.Switch(merge, None, Geometry())

        clock.out()

    # ====================================================================================================
    # A Figure

    with GeoNodes("Figure"):

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
            curve0 = fig0.to_string().to_curves(size=size, align_x='CENTER', align_y='MIDDLE')
            curve1 = fig1.to_string().to_curves(size=size, align_x='CENTER', align_y='MIDDLE').transform(translation=(0, -size, 0))

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

    with GeoNodes("Wheels Counter"):

        value      = Float(123, "Value", 0, tip="Counter value")
        count      = Integer(3, "Number of Wheels", 1, 10)
        size       = Float(1, "Size", 0)
        fig_mat    = Material("Wheel Figure", "Figure material")
        back_mat   = Material("Wheel Background", "Background material")
        with_box   = Boolean(True, "Create Box")
        box_mat    = Material("Wheel Box", "Box material")
        box_color  = Color((.5, .5, .5), "Box Color")
        merge      = Boolean(False, "Merge with input")

        size_factor = 1.05

        with Repeat(wheels=None, value=value, index=0, iterations=count) as rep:

            rep.wheels = rep.wheels.transform(translation=(size*size_factor, 0, 0))

            fig = rep.value % 10
            new_figure = Mesh(Group("Figure", {
                "Figure"   : fig,
                "Size"     : size,
                "Continuous" : rep.index.equal(0),
                "Figure material" : fig_mat,
                "Background material" : back_mat,
            }).geometry)

            new_figure.faces.store("Wheel", rep.index)

            rep.wheels += new_figure

            ifig = gnmath.floor(fig)
            ok9 = ifig.equal(9)
            frac = fig - ifig

            value = gnmath.floor(rep.value/10)
            rep.value = value + Float(0).switch(ok9, frac)

            rep.index += 1

        wheels = rep.wheels

        with Layout("Box"):

            bbox = wheels.bounding_box()
            center = (bbox.min_ + bbox.max_).scale(-.5)
            wheels = wheels.transform(translation=center)

            bbox = wheels.bounding_box()
            ext_box = Mesh.Cube(size=bbox.max_.scale(2) + (.1, .5, .11))
            ext_box = ext_box.transform(translation=(0, .2, 0))

            int_box = Mesh.Cube(size=bbox.max_.scale(2) + (-.1, .3, -.1))
            int_box = int_box.transform(translation=(0, -.1, 0))

            box = ext_box.difference(int_box)
            #box = ext_box + int_box
            box.material = box_mat
            box.faces.store("Box Color", box_color)

            if False:
                wheels = wheels.transform(translation=(0, size*.1, 0))

                box = Mesh.Cube(((count + .2)*size, size*2.1, size*1.2))
                cut = box.transform(scale=(.9, .65, 1), translation=(0, 0, .1))
                box = box.difference(cut)
                box = box.transform(rotation=(halfpi, 0, 0), translation=(size*(count-1)/2, size*.6, size*.1))
                box.material = box_mat

        wheels += Geometry.Switch(with_box, None, box)
        wheels += Geometry.Switch(merge, None, Geometry())


        wheels.out()
