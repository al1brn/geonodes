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
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socketclass import Attribute

# =============================================================================================================================
# Boolean

class Boolean(Attribute):
    SOCKET_TYPE = 'BOOLEAN'

    def __init__(self, value=False, name=None, tip=None, subtype='NONE'):
        """ Socket of type BOOLEAN

        > Node <&Node Boolean>

        Arguments
        ---------
        - value (bool or Socket = False) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        - subtype (str='NONE') : socket subtype
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('Boolean', boolean=int(value))._out
            else:
                bsock = Tree.new_input('NodeSocketBool', name, value=value, description=tip)

        super().__init__(bsock)

    @property
    def math(self):
        from . import gnmath
        return gnmath

    # ====================================================================================================
    # Constructors

    @classmethod
    def Input(cls, name='Boolean', value=False, tip=None):
        tree = Tree.CURRENT
        return tree.new_input('NodeSocketBool', name=name, value=value, description=tip)

    # ----------------------------------------------------------------------------------------------------
    # Operations

    def __neg__(self):
        return self.math.bnot(self)

    def __or__(self, other):
        return self.math.bor(self, other)

    def __add__(self, other):
        return self.math.bor(self, other)

    def __sub__(self, other):
        return self.math.bsubtract(self, other)

    def __ror__(self, other):
        return self.math.bor(other, self)

    def __and__(self, other):
        return self.math.band(self, other)

    def __mul__(self, other):
        return self.math.band(self, other)

    def __rand__(self, other):
        return self.math.band(other, self)

    def __xor__(self, other):
        return self.math.xor(self, other)

    def __rxor__(self, other):
        return self.math.xor(other, self)

    # ----------------------------------------------------------------------------------------------------
    # Random

    @classmethod
    def Random(cls, probability=None, id=None, seed=None):
        """ Constructor : random Boolean.

        > Node <&Node Random Value>

        Arguments
        ---------
        - probability (Float)
        - id (Integer)
        - seed (Integer)

        Returns
        -------
        - Boolean
        """
        return Node('Random Value', {'Probability': probability, 'ID': id, 'Seed': seed}, data_type='BOOLEAN')._out
