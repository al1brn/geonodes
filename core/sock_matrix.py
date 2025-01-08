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
- update   : 2024/12/29
"""

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
