import numpy as np

import bpy
from geonodes.structured.treeclass import Tree, Node
from geonodes.structured.socketclass import DataSocket
#from geonodes.structured import math

# =============================================================================================================================
# Boolean

class IntFloat(DataSocket):

    @property
    def math(self):
        from geonodes.structured import math
        return math

    # ====================================================================================================
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        return cls(Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT')._out)

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

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type=None):
        return Float(Node('Map Range', {'value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, interpolation_type=interpolation_type)._out)

    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='LINEAR')

    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='STEPPED')

    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHSTEP')

    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHERSTEP')

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.math.multiply(self, -1)

    # ----- Addition

    def __add__(self, other):
        return self.math.add(self, other)

    def __radd__(self, other):
        return self.math.add(other, self)

    # ----- Subtraction

    def __sub__(self, other):
        return self.math.subtract(self, other)

    def __rsub__(self, other):
        return self.math.subtract(other, self)

    # ----- Multiplication

    def __mul__(self, other):
        return self.math.multiply(self, other)

    def __rmul__(self, other):
        return self.math.multiply(other, self)

    # ----- Division

    def __truediv__(self, other):
        return self.math.divide(self, other)

    def __rtruediv__(self, other):
        return self.math.divide(other, self)

    # ----- Modulo

    def __mod__(self, other):
        return self.math.modulo(self, other)

    def __rmod__(self, other):
        return self.math.modulo(other, self)

    # ----- Power

    def __pow__(self, other):
        return self.math.power(self, other)

    def __rpow__(self, other):
        return self.math.power(other, self)


class Float(IntFloat):

    SOCKET_TYPE = 'VALUE'

    def get_data_type(self, node_name=None):
        return 'FLOAT'

    # ====================================================================================================
    # Methods

    # ----- To integer

    def float_to_integer(self, rounding_mode=None):
        return Integer(Node('Float to Integer', {0: self}, rounding_mode=rounding_mode)._out)

    def round(self):
        return self.float_to_integer(rounding_mode='ROUND')

    def floor(self):
        return self.float_to_integer(rounding_mode='FLOOR')

    def ceiling(self):
        return self.float_to_integer(rounding_mode='CEILING')

    def truncate(self):
        return self.float_to_integer(rounding_mode='TRUNCATE')

    # ====================================================================================================
    # Comparison

    def less_than(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='LESS_THAN', data_type='FLOAT')._out

    def less_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='LESS_EQUAL', data_type='FLOAT')._out

    def greater_than(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='GREATER_THAN', data_type='FLOAT')._out

    def greater_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, operation='GREATER_EQUAL', data_type='FLOAT')._out

    def equal(self, other, epsilon=None):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, operation='EQUAL', data_type='FLOAT')._out

    def not_equal(self, other, epsilon=None):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, operation='NOT_EQUAL', data_type='FLOAT')._out


class Integer(IntFloat):

    SOCKET_TYPE = 'INT'

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
