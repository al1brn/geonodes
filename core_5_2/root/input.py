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

module : input
------------------
- Input socket

Generated environment classes inherit from this shared root: Font
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

from .tree import Tree


# ====================================================================================================
# Input socket
# ====================================================================================================

class Input(Socket):

    __slots__ = Socket.__slots__ + ('name', 'panel', 'props')

    SOCKET_TYPE = 'CUSTOM'

    def __init__(self, name: str = None, panel: str = "", **props):
        """ Input Socket wrapping an output virtual socket.

        When plugging to the input socket of a Node, a New socket is creaated.

        Parameters
        ----------
        name : str, optional
            the name to give to the output default=None.

        panel : str, optional
            the panel to create if possible default="".

        props : dict
            socket properties

        """

        innode = Tree.current_tree().get_input_node()

        bsocket = None
        for bsock in innode._bnode.outputs:
            if bsock.type == 'CUSTOM':
                bsocket = bsock
                break

        if bsocket is None:
            raise RuntimeError(f"Impossible to initialize an Input socket: no output virtual socket found in node {innode}.")
        
        super().__init__(bsocket)

        self.name  = name
        self.panel = panel
        self.props = {**props}
