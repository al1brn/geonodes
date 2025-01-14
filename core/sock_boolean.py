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

module : sock_boolean
---------------------
- Boolean socket

This class inherits from Socket and from generated.Boolean
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
from . treeclass import Tree, Node
from . socket_class import Socket
from . import generated
from . scripterror import NodeError

# =============================================================================================================================
# Boolean

class Boolean(generated.Boolean):

    SOCKET_TYPE = 'BOOLEAN'

    def __init__(self, value=False, name =None, tip=None, panel=None,
        default_attribute="", hide_value=False, layer_selection=False, hide_in_modifier=False, single_value=False):
        """ Socket of type BOOLEAN

        layer_selection_field

        > Node <&Node Boolean>

        Arguments
        ---------
        - value (bool or Socket = False) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        - panel (str = None) : panel name (overrides tree pane if exists)
        - default_attribute (str = "") : default attribute name
        - hide_value (bool = False) : Hide Value option
        - layer_selection (bool = False) : Layer selection field
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option
        """
        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('Boolean', boolean=int(value))._out
            else:
                bsock = Tree.new_input('NodeSocketBool', name, value=value, panel=panel,
                    description             = tip,
                    default_attribute_name  = default_attribute,
                    hide_value              = hide_value,
                    layer_selection_field   = layer_selection,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Input(cls, name='Boolean', value=False, tip=None):
        tree = Tree.CURRENT
        return tree.new_input('NodeSocketBool', name=name, value=value, description=tip)

    # ----------------------------------------------------------------------------------------------------
    # Operations

    def __neg__(self):
        return self.bnot()

    def __or__(self, other):
        return self.bor(other)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.nimply(other)

    def __ror__(self, other):
        return self.bor(other)

    def __and__(self, other):
        return self.band(other)

    def __mul__(self, other):
        return self.band( other)

    def __rand__(self, other):
        return self.band(other)

    def __xor__(self, other):
        return self.xor(self)

    def __rxor__(self, other):
        return self.xor(other)

    # To avoid user errors

    def __bool__(self):
        raise NodeError(f"Boolean Socket is not a python bool. Use 'switch' method or operators & | ")
