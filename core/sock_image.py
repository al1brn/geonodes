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

module : sock_image
---------------------
- Image socket

This class inherits from Socket and from generated.Image
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


class Image(generated.Image):

    SOCKET_TYPE = 'IMAGE'

    def __init__(self, value=None, name=None, tip=None, panel=None,
        hide_value=False, hide_in_modifier=False):
        """ Class Image data socket

        Node <&Node Image>

        Arguments
        ---------
        - value (bpy.types.Image or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip (str = None) : user tip for group input socket
        - panel (str = None) : panel name (overrides tree panel if exists)
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        """
        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('IMAGE', value)
            if name is None:
                bsock = Node('Image', image=image)._out
            else:
                bsock = Tree.new_input('NodeSocketImage', name=name, value=image, panel=panel,
                    description             = tip,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                )

        super().__init__(bsock)
