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

module : sock_menu
---------------------
- Menu socket

This class inherits from Socket and from generated.Menu
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


class Menu(Socket):

    SOCKET_TYPE = 'MENU'

    def __init__(self, socket): #, name="Menu", menu=0, items={'A': None, 'B': None}, tip=None, input_type=None):
        """ > Menu socket, node <&Node Menu Switch>

        > [!IMPORTANT]
        > A Menu socket can't be instantiated directly. It must be created with
        > <!Socket#MenuSwitch> method

        Arguments
        ---------
        - socket (socket) : menu socket, can't be None
        """
        if socket is None:
            raise Exception("Menu Socket can't be instantiated directly, use 'Socket.MenuSwitch' instead")
        else:
            super().__init__(socket)
