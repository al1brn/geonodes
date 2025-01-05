#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : sock_shader
-------------------
- Implement Shader data socket

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
- update : 2024/12/29
- update : 2025/01/01
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socket_class import Socket
from .  import generated

# =============================================================================================================================
# Shader Root for Shader and VolumeShader

class ShaderRoot:

    def surface_out(self, target='ALL'):
        """ Connect the shader to the Surface socket of Material Output

        Arguments
        ---------
        - target (str = 'ALL') : parameter ' target' in ('ALL', 'EEVEE', 'CYCLES')
        """
        self._tree.set_surface(self, target=target)

    def volume_out(self, target='ALL'):
        """ Connect the shader to the Volume socket of Material Output

        Arguments
        ---------
        - target (str = 'ALL') : parameter ' target' in ('ALL', 'EEVEE', 'CYCLES')
        """
        self._tree.set_volume(self, target=target)

    # =============================================================================================================================
    # Operations

    def __add__(self, other):
        return self.add(other)

    def __mul__ (self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self.mix(other[0], fac=other[1])
        else:
            return self.mix(other)

# =============================================================================================================================
# Surface Shader

class Shader(ShaderRoot, generated.Shader):

    SOCKET_TYPE = 'SHADER'

    def out(self, name=None):
        if self._tree._is_group:
            super().out(name=name)
        else:
            self._tree.surface = self

# =============================================================================================================================
# Volume Shader

class VolumeShader(ShaderRoot, generated.VolumeShader):

    def out(self, name=None):
        if self._tree._is_group:
            super().out(name=name)
        else:
            self._tree.volume = self
