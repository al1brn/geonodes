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
    def Dial(cls, *value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY'):
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
        return cls('Dial Gizmo', {'Value': values, 'Position': position, 'Up': up, 'Screen Space': screen_space, 'Radius': radius}, color_id=color_id)

    @classmethod
    def Linear(cls, *value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW'):
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
        return cls('Linear Gizmo', {'Value': values, 'Position': position, 'Direction': direction}, color_id=color_id, draw_style=draw_style)

    @classmethod
    def Transform(cls, *value, position=None, rotation=None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True):
        """ > Node <&Node Transform Gizmo>

        Arguments
        ---------
        - value (Matrix) : socket 'Value' (Value)
        - position (Vector) : socket 'Position' (Position)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - use_rotation_x (bool): Node.use_rotation_x
        - use_rotation_y (bool): Node.use_rotation_y
        - use_rotation_z (bool): Node.use_rotation_z
        - use_scale_x (bool): Node.use_scale_x
        - use_scale_y (bool): Node.use_scale_y
        - use_scale_z (bool): Node.use_scale_z
        - use_translation_x (bool): Node.use_translation_x
        - use_translation_y (bool): Node.use_translation_y
        - use_translation_z (bool): Node.use_translation_z

        Returns
        -------
        - Geometry
        """
        values = list(value) if len(value) else None
        return cls('Transform Gizmo', {'Value': values, 'Position': position, 'Rotation': rotation}, use_rotation_x=use_rotation_x, use_rotation_y=use_rotation_y, use_rotation_z=use_rotation_z, use_scale_x=use_scale_x, use_scale_y=use_scale_y, use_scale_z=use_scale_z, use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)


    def add_value(self, *values):
        self.value = values
