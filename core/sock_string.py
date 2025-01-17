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

module : sock_string
---------------------
- String socket

This class inherits from Socket and from generated.String
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

class String(generated.String):

    SOCKET_TYPE = 'STRING'

    def __init__(self, value="", name=None, tip=None, panel=None, subtype='NONE',
        hide_value=False, hide_in_modifier=False):
        """ Socket of type String

        Node <&Node String>

        A group input socket of type String is created if the name is not None.

        Arguments
        ---------
        - value (str or Socket) : initial value
        - name (str = None) : group input socket name if not None
        - tip (str = None) : user type for group input socket
        - panel (str = None) : panel name (overrides tree pane if exists)
        - subtype (str in ('NONE', 'FILE_PATH') = 'NONE') : sub type for group input
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('String', string=str(value))._out
            else:
                bsock = Tree.new_input('NodeSocketString', name, value=value, panel=panel,
                    subtype             = subtype,
                    description         = tip,
                    hide_value          = hide_value,
                    hide_in_modifier    = hide_in_modifier,
                )
        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def FilePath(cls, value="", name="File Path", tip=None, panel=None,
        hide_value=False, hide_in_modifier=False):
        """ File Path input String

        New <#String> input with subtype 'FILE_PATH'.

        Returns
        -------
        - String
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='FILE_PATH',
            hide_value=hide_value, hide_in_modifier=hide_in_modifier)

    # ====================================================================================================
    # Operators

    def __add__(self, other):
        if isinstance(other, tuple):
            return Node('Join Strings', {'Strings': [self] + list(other)})._out
        else:
            return Node('Join Strings', {'Strings': [self, other]})._out

    def __radd__(self, other):
        return Node('Join Strings', {'Strings': [other, self]})._out

    def __iadd__(self, other):
        return self._jump(self + other)

    def __mul__(self, other):
        if isinstance(other, tuple):
            return self.join(*other)
        else:
            return self.join(other)

    def __imul__(self, other):
        if isinstance(other, tuple):
            return self.join(*other)
        else:
            return self.join(other)
