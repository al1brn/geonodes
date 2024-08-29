#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : floatclass
-------------------
- Implement value classes

classes
-------
- IntFloat      : Base class for Integer and Float
- Integer       : DataSocket of type 'INT'
- Float         : DataSocket of type 'FLOAT'

functions
---------

updates
-------
- creation : 2024/07/23
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socketclass import ValueSocket

# magic methods
# __add__ __radd__ __iadd__ __sub__  __mul__ __matmul__ __truediv____floordiv__ __mod__ __divmod__ __pow__
# __lshift__ __rshift__ __and__ __xor__ __or__
# __neg__ __pos__ __abs__ __invert__
# __complex__ __int__	__float__ __index__
# __round__	__trunc__ __floor__	 __ceil__

# =============================================================================================================================
# Root for Integer and Float
# =============================================================================================================================

class IntFloat(ValueSocket):

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_factor=None):
        return Float(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='FLOAT')._out)

    # ----- Clamp

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        return Float(Node('Clamp', {'Value': self, 'Min': min, 'Max': max}, clamp_type=clamp_type)._out)

    def clamp_range(self, min=None, max=None, clamp_type='RANGE'):
        return self.clamp(min, max, clamp_type)

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type='LINEAR'):
        return Float(Node('Map Range', {'Value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, interpolation_type=interpolation_type)._out)

    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='LINEAR')

    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='STEPPED')

    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHSTEP')

    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHERSTEP')

    def color_ramp(self, keep=None):
        return Node('Color Ramp', {'Fac': self}, _keep=keep)._out

    def to_string(self, decimals=None):
        return Node('Value to String', {'Value': self, 'Decimals': decimals})._out

    def curve(self, factor=None, keep=None):
        return Node('Float Curve', {'Factor': factor, 'Value': self}, _keep=keep)._out

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.math.multiply(self, -1)

    # ----- Abs

    def __abs__(self):
        return self.math.abs(self)

    # ----- Addition

    def __add__(self, other):
        if utils.is_vector_like(other):
            return self.math.vadd(self, other)
        return self.math.add(self, other)

    def __radd__(self, other):
        if utils.is_vector_like(other):
            return self.math.vadd(other, self)
        return self.math.add(other, self)

    def __iadd__(self, other):
        return self._jump(self.math.add(self, other))

    # ----- Subtraction

    def __sub__(self, other):
        if utils.is_vector_like(other):
            return self.math.vsubtract(self, other)
        return self.math.subtract(self, other)

    def __rsub__(self, other):
        if utils.is_vector_like(other):
            return self.math.vsubtract(other, self)
        return self.math.subtract(other, self)

    def __isub__(self, other):
        return self._jump(self.math.subtract(self, other))

    # ----- Multiplication

    def __mul__(self, other):
        if utils.is_vector_like(other):
            return self.math.scale(other, self)
        return self.math.multiply(self, other)

    def __rmul__(self, other):
        if utils.is_vector_like(other):
            return self.math.scale(other, self)
        return self.math.multiply(other, self)

    def __imul__(self, other):
        return self._jump(self.math.multiply(self, other))

    # ----- Division

    def __truediv__(self, other):
        if utils.is_vector_like(other):
            return self.math.vdivide(self, other)
        return self.math.divide(self, other)

    def __rtruediv__(self, other):
        if utils.is_vector_like(other):
            return self.math.vdivide(other, self)
        return self.math.divide(other, self)

    def __itruediv__(self, other):
        return self._jump(self.math.divide(self, other))

    # ----- Modulo

    def __mod__(self, other):
        if utils.is_vector_like(other):
            return self.math.vmodulo(self, other)
        return self.math.modulo(self, other)

    def __rmod__(self, other):
        if utils.is_vector_like(other):
            return self.math.vmodulo(other, self)
        return self.math.modulo(other, self)

    def __imod__(self, other):
        return self._jump(self.math.modulo(self, other))

    # ----- Power

    def __pow__(self, other):
        return self.math.power(self, other)

    def __rpow__(self, other):
        return self.math.power(other, self)

    def __ipow__(self, other):
        return self._jump(self.math.power(self, other))

    # ----- Operations

    def __round__(self):
        return self.math.round(self)

    def __trunc__(self):
        return self.math.trunc(self)

    def __floor__(self):
        return self.math.floor(self)

    def __ceil__(self):
        return self.math.ceil(self)

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

# =============================================================================================================================
# Float
# =============================================================================================================================

class Float(IntFloat):

    SOCKET_TYPE = 'VALUE'

    def __init__(self, value=0., name=None, min=None, max=None, tip=None, subtype='NONE'):
        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('Value')._out
                bsock._bsocket.default_value = value
            else:
                bsock = Tree.new_input('NodeSocketFloat', name, value=value, subtype=subtype, min_value=min, max_value=max, description=tip)

        super().__init__(bsock)

     # ====================================================================================================
     # Constructors

    @classmethod
    def Percentage(cls, value=0., name='Percentage', min=None, max=None, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls, value=0., name='Factor', min=0, max=1, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='FACTOR')

    @classmethod
    def Angle(cls, value=0., name='Angle', min=None, max=None, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='ANGLE')

    @classmethod
    def Time(cls, value=0., name='Time', min=None, max=None, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='TIME')

    @classmethod
    def TimeAbsolute(cls, value=0., name='TimeAbsolute', min=None, max=None, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='TIME_ABSOLUTE')

    @classmethod
    def Distance(cls, value=0., name='Distance', min=None, max=None, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='DISTANCE')

    @classmethod
    def WaveLength(cls, value=0., name='WaveLength', min=None, max=None, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='WAVELENGTH')

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        return Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT')._out

    # ====================================================================================================
    # Methods

    # ----- To integer

    def to_integer(self, rounding_mode=None):
        return Node('Float to Integer', {0: self}, rounding_mode=rounding_mode)._out

    def round(self):
        if Tree.is_geonodes:
            return self.to_integer(rounding_mode='ROUND')
        else:
            return Node('Math', {0: self}, operation='ROUND')._out

    def floor(self):
        if Tree.is_geonodes:
            return self.to_integer(rounding_mode='FLOOR')
        else:
            return Node('Math', {0: self}, operation='FLOOR')._out

    def ceiling(self):
        if Tree.is_geonodes:
            return self.to_integer(rounding_mode='CEILING')
        else:
            return Node('Math', {0: self}, operation='CEIL')._out

    def truncate(self):
        if Tree.is_geonodes:
            return self.to_integer(rounding_mode='TRUNCATE')
        else:
            return Node('Math', {0: self}, operation='TRUNC')._out

    # ====================================================================================================
    # Comparison

    def less_than(self, other):
        if Tree.is_geonodes:
            return Node("Compare", {'A': self, 'B': other}, operation='LESS_THAN', data_type='FLOAT')._out
        else:
            return Node('Math', {0: self, 1: other}, operation='LESS_THAN')._out

    def less_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='LESS_EQUAL', data_type='FLOAT')._out

    def greater_than(self, other):
        if Tree.is_geonodes:
            return Node("Compare", {'A': self, 'B': other}, operation='GREATER_THAN', data_type='FLOAT')._out
        else:
            return Node('Math', {0: self, 1: other}, operation='GREATER_THAN')._out

    def greater_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='GREATER_EQUAL', data_type='FLOAT')._out

    def equal(self, other, epsilon=None):
        if Tree.is_geonodes:
            return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, operation='EQUAL', data_type='FLOAT')._out
        else:
            return Node('Math', {0: self, 1: other, 2: epsilon}, operation='COMPARE')._out

    def not_equal(self, other, epsilon=None):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, operation='NOT_EQUAL', data_type='FLOAT')._out

    # ====================================================================================================
    # Output

    def to_output(self, name=None):
        if self._tree._btree.bl_idname == 'ShaderNodeTree' and not self._tree._is_group:
            if name is None:
                self._tree.set_thickness(self)
            else:
                self._tree.aov_output(name=name, value=self)
        else:
            super().to_output(name=name)

    def thickness_out(self, target='ALL'):
        self._tree.set_thickness(self, target=target)

# =============================================================================================================================
# Integer
# =============================================================================================================================

class Integer(IntFloat):

    SOCKET_TYPE = 'INT'

    def __init__(self, value=0, name=None, min=None, max=None, tip=None, subtype='NONE'):
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
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls, value=0, name='Factor', min=100, max=100, tip=None):
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='FACTOR')

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        return Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='INT')._out

    @classmethod
    def FromFloat(cls, float=None, rounding_mode='ROUND'):
        return Float(float).to_integer(rounding_mode)

    # ====================================================================================================
    # Comparison

    def less_than(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='LESS_THAN', data_type='INT')._out

    def less_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='LESS_EQUAL', data_type='INT')._out

    def greater_than(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='GREATER_THAN', data_type='INT')._out

    def greater_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='GREATER_EQUAL', data_type='INT')._out

    def equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='EQUAL', data_type='INT')._out

    def not_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='NOT_EQUAL', data_type='INT')._out
