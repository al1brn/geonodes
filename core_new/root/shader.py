from .socket import Socket
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

Generated environment classes inherit from this shared root: Shader
the environment supplies the generated node methods.

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


from ..common import utils as utils
from .socket import Socket
# =============================================================================================================================
# Shader Root for Shader and VolumeShader

class ShaderRoot:

    def surface_out(self, target='ALL'):
        """ Connect the shader to the Surface socket of Material Output

        Parameters
        ----------
        target : str, optional
            parameter ' target' in ('ALL', 'EEVEE', 'CYCLES') default='ALL'.

        """
        self._tree.set_surface(self, target=target)

    def volume_out(self, target='ALL'):
        """ Connect the shader to the Volume socket of Material Output

        Parameters
        ----------
        target : str, optional
            parameter ' target' in ('ALL', 'EEVEE', 'CYCLES') default='ALL'.

        """
        self._tree.set_volume(self, target=target)

    # =============================================================================================================================
    # Operations

    def __add__(self, other):
        return self.add(other)

    def __mul__ (self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self.mix(other[0], factor=other[1])
        else:
            return self.mix(other)

# =============================================================================================================================
# Surface Shader

class Shader(ShaderRoot, Socket):

    SOCKET_TYPE = 'SHADER'

    def __init__(self, 
        value: Socket = None,
        name: str = None,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        ):
        """ Socket of type Shader

        A group input socket of type Shader.

        Parameters
        ----------
        value : Socket
            initial value

        name : str, optional
            group input socket name if not None default=None.

        tip : str, default=''
            Property description

        panel : str, optional
            Panel name default="".

        optional_label : bool, default=False
            Property optional_label

        hide_value : bool, default=False
            Property hide_value

        hide_in_modifier : bool, default=False
            Property hide_in_modifier

        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            bsock = self._create_input_socket(name=name, tip=tip,
                panel=panel, optional_label=optional_label, hide_value=hide_value,
                hide_in_modifier=hide_in_modifier)

        super().__init__(bsock)



# =============================================================================================================================
# Volume Shader

class VolumeShader(ShaderRoot, Socket):

    pass
