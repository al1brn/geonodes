#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : vectorclass
--------------------
- Implement vector like classes

classes
-------
- VectorLike    : Base class for Vector,Rotation and Color
- VectRot       : Base class for Vector and Rotation
- Vector        : Socket of type 'VECTOR'
- Rotation      : Socket of type 'ROTATION'
- Matrix        : Socket of type 'MATRIX'

functions
---------

updates
-------
- creation : 2024/07/23
- update   : 2024/09/04
"""


from sys import version
import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socket_class import Socket
from . import generated


class Rotation(generated.Rotation):

    SOCKET_TYPE = 'ROTATION'

    def __init__(self, value: tuple | Socket | str | None = (0., 0., 0.), name: str | None = None, tip: str | None = None):
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
        """
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
                bsock = Tree.new_input('NodeSocketRotation', name, value=value, description=tip)

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
        return self.invert
