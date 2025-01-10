#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : booleanclass
---------------------
- Implement simple Boolean class

classes
-------
- Boolean       : Socket of type 'BOOLEAN'

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
- update : 2024/12/29
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socket_class import Socket
from . import generated

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
