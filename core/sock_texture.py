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

module : sock_texture
---------------------
- Texture socket

This class inherits from Socket and from generated.Texture
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


import bpy
from . import constants, utils
from .treeclass import Tree, Node
from .socket_class import Socket
from . import generated

class Texture(generated.Texture):

    SOCKET_TYPE = 'TEXTURE'

    def __init__(self, value: bpy.types.Texture | Socket | None = None, name: str | None = None, tip: str | None = None):
        """ Socket of type Texture

        Arguments
        ---------
        - value (bpy.types.Texture or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('TEXTURE', value)
            if name is None:
                name = "Texture"
            bsock = Tree.new_input('NodeSocketTexture', name=name, value=image, description=tip)

        super().__init__(bsock)
