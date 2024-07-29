#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/29

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : macros
---------------
- Some macros

classes
-------

functions
---------
- Solidify

updates
-------
- creation : 2024/07/29
"""

from geonodes.script import Layout, Group, Repeat, Simulation
from geonodes.script import Geometry, Mesh, Curve, Points, Instances, Volume
from geonodes.script import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, String, nd, gnmath


def solidify(mesh, thickness=.01, individual=False, merge_distance=.001):

    with Layout("Macro - Solidify", color='MACRO'):

        mesh = Mesh(mesh)
        solidified = mesh.faces.flip() + mesh.faces.extrude(offset_scale=thickness, individual=individual)
        solidified = solidified.switch(Float(merge_distance).greater_than(0), solidified.merge_by_distance(distance=merge_distance))

        return solidified.switch(Float(thickness).less_than(0), solidified.faces.flip())
