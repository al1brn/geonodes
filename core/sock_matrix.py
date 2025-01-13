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

module : sock_matrix
--------------------
- Matrix socket

This class inherits from Socket and from generated.Matrix
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


from sys import version
import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socket_class import Socket
from . import generated

class Matrix(generated.Matrix):

    SOCKET_TYPE = 'MATRIX'

    def __init__(self, value=None, name=None, tip=None, panel=None,
        default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ Matrix data socket ('MATRIX')

        A Matrix socket can be initialized with an array of size 16 (the shape is ignored)
        If **value** is None, a <&Node Combine Matrix> with no input link is created.

        If **name** argument is not None, a group input is created, using value as default initialization

        ``` python
        input = Matrix(None, "My Matrix") # Group input of type 'Matrix' with name 'My Matrix' is created
        identity = Matrix() # Identity matrix
        matrix = Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]) # Node 'Combine Matrix' with an array 16 floats
        ```

        Arguments
        ---------
        - value (array of 16 Floats = None) : initialization values
        - name (str = None) : Create group input socket with this name if not None
        - tup (str = None) : Input socket user tip if an input socket is created
        - panel (str = None) : panel name (overrides tree panel if exists)
        - default_input (str in ('VALUE', 'INSTANCE_TRANSFORM') = 'VALUE') :
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option
        """
        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                if value is not None:
                    a = utils.value_to_array(value, (16,))
                    sockets = {i: a[i] for i in range(16)}
                else:
                    sockets = {}
                bsock = Node('Combine Matrix', sockets)._out
            else:
                bsock = Tree.new_input('NodeSocketMatrix', name, value=value, panel=panel,
                    description             = tip,
                    default_input           = default_input,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def FromArray(cls, array):
        """ > Constructor node <&Node Combine Matrix>

        Arguments
        ---------
        - array (array of size 16) : 16 values to use as matrix components

        Returns
        -------
        - Matrix
        """
        a = utils.value_to_array(array, (16,))
        return Node('Combine Matrix', list(a))._out

    # ====================================================================================================
    # Operations

    def __invert__(self):
        return self.invert()

    def __matmul__(self, other):
        data_type = utils.get_input_type(other, ['MATRIX', 'VECTOR'], 'VECTOR')
        if data_type == 'MATRIX':
            return self.multiply(Matrix(other))._lcop()
        else:
            return self.transform_point(other)._lcop()
