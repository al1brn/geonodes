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

module : demo shaders
---------------------

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/02/01 # Wood and planks

$ DOC START

[Source Code](../demos/shaders.py)

WORK IN PROGRESS

"""

from geonodes import *

def demo():

    # ====================================================================================================
    # Default Shader for Arrow

    with ShaderNodes("Arrow"):

        pos_color = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        negative  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Negative").factor
        transp    = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        neg_color = pos_color.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        color = pos_color.mix(negative, neg_color)

        ped = Shader.Principled(
            base_color = color,
            roughness  = negative.map_range(to_min=.1, to_max=.9),
        )

        shader = ped.mix(transp, Shader.Transparent())

        shader.out()

    # ====================================================================================================
    # Planks

    with ShaderNodes("Planks Splitter", is_group=True):

        vector = Vector(None, "Vector")

        with Panel("Planks"):
            scale      = Float(.6, "Scale")
            length     = Float(1, "Length")
            width      = Float(.2, "Width")
            gap        = Float(.002, "Gap")
            gap_smooth = Float.Factor(.73, "Gap Smooth", 0, 1)

        bricks = Texture.Brick(vector=vector, color1=.05, color2=1, mortar=0, bias=0,
                scale=scale, mortar_size=gap, mortar_smooth=gap_smooth, brick_width=length, row_height=width)

        bricks_offset = Texture.Brick(vector=vector, color1=.05, color2=1, mortar=0, bias=0,
                scale=scale, mortar_size=0, mortar_smooth=0, brick_width=length, row_height=width)

        is_mortar = bricks.value.mless_than(.01)
        offset = Vector(bricks_offset).scale(10)

        is_mortar.out("Mortar")
        (vector + offset).out("Vector")
        bricks.out("Color")
        offset.out("Offset")


    # ====================================================================================================
    # Wood base

    with ShaderNodes("Wood Group", is_group=True):

        vector = Vector(None, "Vector")

        with Panel("Colors"):
            col1 = Color("#181007FF", "Color 1")
            col2 = Color("#BD8B35FF", "Color 2")
            col1_fac = Float.Factor(.32, "Factor 1", 0, .5)
            col2_fac = Float.Factor(.45, "Factor 2", 0, .5)
            detail   = Float(5, "Detail", 0)

        with Panel("Coordinates"):
            scale      = Float(1.5, "Scale")
            stretch    = Float.Factor(.25, "Stretch", 0, 10)
            dist       = Float(2, "Distorsion")
            rot        = Float.Angle(0, "Rotation")

        with Panel("Appearance"):
            rough1 = Float.Factor(.23, "Roughness Min", 0, 1)
            rough2 = Float.Factor(.72, "Roughness Max", 0, 1)
            bump_fac = Float.Factor(.17, "Bump", 0, 1)
            bump_inv = Boolean(True, "Invert Bump")

        with Layout("Base"):
            sx = stretch
            sy = 1/stretch

            coord = snd.mapping(vector=vector, rotation=(0, 0, rot), scale=(sx, sy, sy))

            noise1 = Texture.Noise(vector=coord, scale=scale, detail=detail, distortion=dist)
            noise2 = Texture.Noise(vector=noise1, scale=3, detail=11, roughness=.7, lacunarity=2, distortion=0)

        with Layout("Color"):
            fac = noise2.map_range_linear(col1_fac, 1 - col2_fac)
            col = col1.mix(col2, factor=fac)

        with Layout("Roughness"):
            roughness = noise2.map_range_linear(to_min=rough1, to_max=rough2)

        with Layout("Bump"):
            bump = snd.bump(strength=bump_fac, height=noise2)
            bumpi = snd.bump(strength=bump_fac, height=noise2, invert=True)

            bump = bump.mix(bumpi, factor=bump_inv)

        ped = Shader.Principled(
            base_color = col,
            roughness  = roughness,
            normal     = bump,
            )

        ped.out()

    # ====================================================================================================
    # Planks

    with ShaderNodes("Wood Planks Group", is_group=True):

        splitter = G().planks_splitter().link_inputs()

        wood = G().wood_group(vector=splitter.vector_).link_inputs()

        m_color = Color("#2E150AFF", "Gap Color", panel="Colors")

        mortar = Shader.Principled(
            base_color = m_color,
            normal = snd.bump(strength=1, height=is_mortar, invert=True),
            )

        shader = wood.mix(mortar, factor=splitter)

        shader.out()

    # ====================================================================================================
    # Wood

    with ShaderNodes("Wood"):

        coord = snd.texture_coordinate().object

        G().wood_group(vector=coord).out()

    with ShaderNodes("Wood Planks"):

        coord = snd.texture_coordinate().object

        G().wood_planks_group(vector=coord).out()
