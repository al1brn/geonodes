#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain


$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : floatclass
-------------------
- Implement value classes

classes
-------
- IntFloat      : Base class for Integer and Float
- Integer       : Socket of type 'INT'
- Float         : Socket of type 'FLOAT'

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
from .treeclass import Tree, Node, ColorRamp
from .socket_class import Socket
from . import generated

class Integer(generated.Integer):

    SOCKET_TYPE = 'INT'

    def __init__(self, value: int | Socket | str | None = 0, name: str | None = None, min: int | None =None, max: int | None = None, tip: str | None = None, subtype: str ='NONE'):
        """ > Socket of type INTEGER

        > Node <&Node Value>

        If **value** argument is None:
        - if **name** argument is None, a node 'Integer' is added
        - otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
          arguments

        If **value** argument is not None, a new **Integer** is created from the value, either
        by transtyping or creating a 'Value' node.

        ``` python
        i = Integer()      # 'Integer' node with default initial vlaue
        i = Integer(123). # 'Integer' node with 123 initial value
        i = Integer(123, name="User input", subtype='PERCENTAGE') # Create a new integer group input
        ```

        Arguments
        ---------
        - value (integer or Socket = 0) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - min (float = None) : minimum value
        - max (float = None) : maximum value
        - tip (str = None) : User tip (for Group Input sockets)
        - subtype (str = None) : sub type for group input
        """

        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('Integer', integer=int(value))._out
            else:
                bsock = Tree.new_input('NodeSocketInt', name, value=value, subtype=subtype, min_value=min, max_value=max, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Percentage(cls, value=0, name='Percentage', min=0, max=100, tip=None):
        """ > Integer percentage group input
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls, value=0, name='Factor', min=100, max=100, tip=None):
        """ > Integer factor group input
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='FACTOR')

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        return Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='INT')._out

    @classmethod
    def FromFloat(cls, float=None, rounding_mode='ROUND'):
        return Float(float).to_integer(rounding_mode)

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_factor=None):
        """ > Mix

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor_Float)
        - other (Socket) : socket 'B' (B_Float)
        - clamp_factor (bool): Node.clamp_factor

        Returns
        -------
        - Socket
        """
        return Float(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='FLOAT')._out)

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.negate

    # ----- Abs

    def __abs__(self):
        return self.abs

    # ----- Addition

    def __add__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vadd(self, other)
        elif utils.is_int_like(other):
            return self.add( other)
        else:
            return gnmath.add(self, other)

    def __radd__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vadd(other, self)
        elif utils.is_int_like(other):
            return self.add(other)
        else:
            return gnmath.add(other, self)

    def __iadd__(self, other):
        return self._jump(self.add(other))

    # ----- Subtraction

    def __sub__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vsubtract(self, other)
        elif utils.is_int_like(other):
            return self.subtract(other)
        else:
            return gnmath.subtract(self, other)

    def __rsub__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vsubtract(other, self)
        elif utils.is_int_like(other):
            return gnmath.isubtract(other, self)
        else:
            return gnmath.subtract(other, self)

    def __isub__(self, other):
        return self._jump(self.subtract(other))

    # ----- Multiplication

    def __mul__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.scale(other, self)
        elif utils.is_int_like(other):
            return self.multiply(other)
        else:
            return gnmath.multiply(self, other)

    def __rmul__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.scale(other, self)
        elif utils.is_int_like(other):
            return gnmath.imultiply(other, self)
        else:
            return gnmath.multiply(other, self)

    def __imul__(self, other):
        return self._jump(self.multiply(other))

    # ----- Division

    def __floordiv__(self, other):
        return self.divide_floor(other)

    def __rfloordiv__(self, other):
        return Integer(other).divide_floor(self)

    def __ifloordiv__(self, other):
        return self._jump(self.divide_floor(other))

    # ----- Modulo

    def __mod__(self, other):
        return self.modulo(self, other)

    def __rmod__(self, other):
        return Integer(other).modulo(self)

    def __imod__(self, other):
        return self._jump(self.modulo(other))

    # ----- Power

    def __pow__(self, other):
        from geonodes import gnmath
        if utils.is_int_like(other):
            return self.power(other)
        else:
            return gnmath.power(self, other)

    def __rpow__(self, other):
        from geonodes import gnmath
        if utils.is_int_like(other):
            return Integer(other).power(self)
        else:
            return gnmath.power(other, self)

    def __ipow__(self, other):
        return self._jump(self.power(self, other))

    # ----- Division

    def __truediv__(self, other):
        from geonodes import Float
        return Float(self)/other

    def __rtruediv__(self, other):
        from geonodes import Float
        return other/Float(self)

    def __itruediv__(self, other):
        from geonodes import Float
        return Integer(Float(self)/other)

    # =============================================================================================================================
    # Comparison
    # __eq__ __ne__ __lt__ __gt__ __le__ __ge__

    def __ge__(self, other):
        return self.greater_equal(other)

    def __gt__(self, other):
        return self.greater_than(other)

    def __le__(self, other):
        return self.less_equal(other)

    def __lt__(self, other):
        return self.less_than(other)

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return self.not_equal(other)
