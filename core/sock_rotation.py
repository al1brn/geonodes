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

module : sock_rotation
----------------------
- Rotation socket

This class inherits from Socket and from generated.Rotation
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


class Rotation(generated.Rotation):

    SOCKET_TYPE = 'ROTATION'

    def __init__(self, value=(0., 0., 0.), name=None, tip=None, panel=None,
        hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Socket of type ROTATION

        If **value** argument is None:
        - if **name** argument is None, a node <&Node Rotation> is added
        - otherwise a new group input is created using **tip** argument.

        If **value** argument is not None, a new **Rotation** is created from the value:
        - using a <&Node Rotation> node if the **value** is a float or a tuple of floats
        - using <&Node Combine XYZ> and <&Node Euler to Rotation> nodes if the **value**
          is a tuple containing <!Socket"Sockets>

        ``` python
        rot = Rotation()                    # 'Rotation' node
        rot = Rotation((1, 2, 3.14)).       # 'Rotation' node
        rot = Rotation((Float(1), 2, 3.14)) # 'Combine XYZ' + 'Euler to Rotation' nodes
        rot = Rotation(name="User input").  # Create a new Rotation group input
        ```

        Arguments
        ---------
        - value (tuple of floats or Sockets) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        - panel (str = None) : panel name (overrides tree panel if exists)
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option
        """
        from geonodes import Vector

        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                a = utils.value_to_array(value, (3,))
                if utils.has_bsocket(a):
                    bsock = Vector(value).to_rotation()
                    #bsock = Node('Combine XYZ', {0: a[0], 1: a[1], 2:a[2]})._out
                else:
                    bsock = Node('Rotation', rotation_euler=value)._out
            else:
                bsock = Tree.new_input('NodeSocketRotation', name, value=value, panel=panel,
                    description             = tip,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

        super().__init__(bsock)

    # ====================================================================================================
    # Operations

    def __matmul__(self, other):
        data_type = utils.get_input_type(other, ['ROTATION', 'VECTOR'], ['VECTOR'])
        if data_type == 'ROTATION':
            return self.rotate_global(other)
        else:
            return self.rotate_vector(other)

    def __invert__(self):
        return self.invert()
