#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/shaders
----------------------
Explode points from the points of the initial geometry.
The particles can be either generated or taken from a collection.

updates
-------
- creation : 2024/08/02
- update   : 2024/09/04
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
