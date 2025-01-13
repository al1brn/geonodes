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

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : sock_shader
---------------------
- Shader socket

This class inherits from Socket and from generated.Shader
which is automatically generated.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


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
