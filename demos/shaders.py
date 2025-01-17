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
        negative  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Negative").fac
        transp    = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        neg_color = pos_color.hue_saturation_value(hue=.5, saturation=.9, value=.9)
        color = pos_color.mix(negative, neg_color)

        ped = Shader.Principled(
            base_color = color,
            roughness  = negative.map_range(to_min=.1, to_max=.9),
        )

        shader = ped.mix(transp, Shader.Transparent())

        shader.out()
