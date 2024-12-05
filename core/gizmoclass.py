#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/11/21

@author: alain

$ DOC transparent


-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : gizmoclass
---------------------
- Gizmo utilities

classes
-------
- Gizmo

functions
---------

updates
-------
- creation : 2024/11/21
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node


class Gizmo(Node):

    @classmethod
    def dial(cls, *value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY'):
        """ > Node <&Node Dial Gizmo>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - up (Vector) : socket 'Up' (Up)
        - screen_space (Boolean) : socket 'Screen Space' (Screen Space)
        - radius (Float) : socket 'Radius' (Radius)
        - color_id (str): Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None
        return cls('Dial Gizmo', {'Value': values, 'Position': position, 'Up': up, 'Screen Space': screen_space, 'Radius': radius}, color_id=color_id)._out

    @classmethod
    def linear(cls, *value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW'):
        """ > Node <&Node Linear Gizmo>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - direction (Vector) : socket 'Direction' (Direction)
        - color_id (str): Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')
        - draw_style (str): Node.draw_style in ('ARROW', 'CROSS', 'BOX')

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None
        return cls('Linear Gizmo', {'Value': values, 'Position': position, 'Direction': direction}, color_id=color_id, draw_style=draw_style)._out

    @classmethod
    def transform(cls, *value, position=None, rotation=None, use_rotation=True, use_scale=True, use_translation=True):
        """ > Node <&Node Transform Gizmo>

        Arguments
        ---------
        - value (Matrix) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - use_rotation (bool or triplet of bools): use_rotation_x, use_rotation_y, use_rotation_z
        - use_scale (bool or triplet of bools): use_scale_x, use_scale_y, use_scale_z
        - use_translation (bool or triplet of bools): use_translation_x, translation_y, use_translation_z

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None

        rx, ry, rz = np.resize(use_rotation,    3).astype(bool)
        sx, sy, sz = np.resize(use_scale,       3).astype(bool)
        tx, ty, tz = np.resize(use_translation, 3).astype(bool)

        return cls('Transform Gizmo', {'Value': values, 'Position': position, 'Rotation': rotation},
            use_rotation_x   =rx, use_rotation_y   =ry, use_rotation_z   =rz,
            use_scale_x      =sx, use_scale_y      =sy, use_scale_z      =sz,
            use_translation_x=tx, use_translation_y=ty, use_translation_z=tz)._out