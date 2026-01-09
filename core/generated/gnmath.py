# Generated 2026-01-09 13:18:08

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


def bw_and(a: Integer = None, b: Integer = None):
    """ > Node <&Node Bit Math>

    Information
    -----------
    - Parameter 'operation' : 'AND'

    Arguments
    ---------
    - a (Integer) : socket 'A' (id: A)
    - b (Integer) : socket 'B' (id: B)

    Returns
    -------
    - Integer
    """
    node = Node('Bit Math', {'A': a, 'B': b}, operation='AND')
    return node._out

def bw_or(a: Integer = None, b: Integer = None):
    """ > Node <&Node Bit Math>

    Information
    -----------
    - Parameter 'operation' : 'OR'

    Arguments
    ---------
    - a (Integer) : socket 'A' (id: A)
    - b (Integer) : socket 'B' (id: B)

    Returns
    -------
    - Integer
    """
    node = Node('Bit Math', {'A': a, 'B': b}, operation='OR')
    return node._out

def bw_xor(a: Integer = None, b: Integer = None):
    """ > Node <&Node Bit Math>

    Information
    -----------
    - Parameter 'operation' : 'XOR'

    Arguments
    ---------
    - a (Integer) : socket 'A' (id: A)
    - b (Integer) : socket 'B' (id: B)

    Returns
    -------
    - Integer
    """
    node = Node('Bit Math', {'A': a, 'B': b}, operation='XOR')
    return node._out

def bw_not(a: Integer = None):
    """ > Node <&Node Bit Math>

    Information
    -----------
    - Parameter 'operation' : 'NOT'

    Arguments
    ---------
    - a (Integer) : socket 'A' (id: A)

    Returns
    -------
    - Integer
    """
    node = Node('Bit Math', {'A': a}, operation='NOT')
    return node._out

def bw_shift(a: Integer = None, shift: Integer = None):
    """ > Node <&Node Bit Math>

    Information
    -----------
    - Parameter 'operation' : 'SHIFT'

    Arguments
    ---------
    - a (Integer) : socket 'A' (id: A)
    - shift (Integer) : socket 'Shift' (id: Shift)

    Returns
    -------
    - Integer
    """
    node = Node('Bit Math', {'A': a, 'Shift': shift}, operation='SHIFT')
    return node._out

def bw_rotate(a: Integer = None, shift: Integer = None):
    """ > Node <&Node Bit Math>

    Information
    -----------
    - Parameter 'operation' : 'ROTATE'

    Arguments
    ---------
    - a (Integer) : socket 'A' (id: A)
    - shift (Integer) : socket 'Shift' (id: Shift)

    Returns
    -------
    - Integer
    """
    node = Node('Bit Math', {'A': a, 'Shift': shift}, operation='ROTATE')
    return node._out

def band(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'AND'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='AND')
    return node._out

def bor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'OR'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='OR')
    return node._out

def bnot(boolean: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'NOT'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean}, operation='NOT')
    return node._out

def not_and(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'NAND'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NAND')
    return node._out

def nor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'NOR'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NOR')
    return node._out

def xnor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'XNOR'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='XNOR')
    return node._out

def xor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'XOR'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='XOR')
    return node._out

def imply(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'IMPLY'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='IMPLY')
    return node._out

def nimply(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    Information
    -----------
    - Parameter 'operation' : 'NIMPLY'

    Arguments
    ---------
    - boolean (Boolean) : socket 'Boolean' (id: Boolean)
    - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)

    Returns
    -------
    - Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NIMPLY')
    return node._out

def iadd(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'ADD'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='ADD')
    return node._out

def isubtract(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'SUBTRACT'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='SUBTRACT')
    return node._out

def imultiply(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'MULTIPLY'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MULTIPLY')
    return node._out

def idivide(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'DIVIDE'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE')
    return node._out

def imultiply_add(value: Integer = None, multiplier: Integer = None, addend: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'MULTIPLY_ADD'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - multiplier (Integer) : socket 'Multiplier' (id: Value_001)
    - addend (Integer) : socket 'Addend' (id: Value_002)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD')
    return node._out

def iabs(value: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'ABSOLUTE'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value}, operation='ABSOLUTE')
    return node._out

def negate(value: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'NEGATE'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value}, operation='NEGATE')
    return node._out

def ipower(base: Integer = None, exponent: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'POWER'

    Arguments
    ---------
    - base (Integer) : socket 'Base' (id: Value)
    - exponent (Integer) : socket 'Exponent' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': base, 'Value_001': exponent}, operation='POWER')
    return node._out

def imin(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'MINIMUM'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MINIMUM')
    return node._out

def imax(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'MAXIMUM'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MAXIMUM')
    return node._out

def isign(value: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'SIGN'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value}, operation='SIGN')
    return node._out

def divide_round(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'DIVIDE_ROUND'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE_ROUND')
    return node._out

def divide_floor(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'DIVIDE_FLOOR'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE_FLOOR')
    return node._out

def divide_ceil(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'DIVIDE_CEIL'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE_CEIL')
    return node._out

def ifloored_modulo(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'FLOORED_MODULO'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='FLOORED_MODULO')
    return node._out

def imodulo(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'MODULO'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MODULO')
    return node._out

def gcd(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'GCD'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='GCD')
    return node._out

def lcm(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    Information
    -----------
    - Parameter 'operation' : 'LCM'

    Arguments
    ---------
    - value (Integer) : socket 'Value' (id: Value)
    - value_1 (Integer) : socket 'Value' (id: Value_001)

    Returns
    -------
    - Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='LCM')
    return node._out

def add(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ADD'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='ADD', use_clamp=use_clamp)
    return node._out

def subtract(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SUBTRACT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='SUBTRACT', use_clamp=use_clamp)
    return node._out

def multiply(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'MULTIPLY'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MULTIPLY', use_clamp=use_clamp)
    return node._out

def divide(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'DIVIDE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE', use_clamp=use_clamp)
    return node._out

def multiply_add(value: Float = None,
                    multiplier: Float = None,
                    addend: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'MULTIPLY_ADD'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - multiplier (Float) : socket 'Multiplier' (id: Value_001)
    - addend (Float) : socket 'Addend' (id: Value_002)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD', use_clamp=use_clamp)
    return node._out

def power(base: Float = None, exponent: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'POWER'

    Arguments
    ---------
    - base (Float) : socket 'Base' (id: Value)
    - exponent (Float) : socket 'Exponent' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': base, 'Value_001': exponent}, operation='POWER', use_clamp=use_clamp)
    return node._out

def log(value: Float = None, base: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'LOGARITHM'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - base (Float) : socket 'Base' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': base}, operation='LOGARITHM', use_clamp=use_clamp)
    return node._out

def sqrt(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SQRT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='SQRT', use_clamp=use_clamp)
    return node._out

def inverse_sqrt(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'INVERSE_SQRT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='INVERSE_SQRT', use_clamp=use_clamp)
    return node._out

def abs(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ABSOLUTE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='ABSOLUTE', use_clamp=use_clamp)
    return node._out

def exp(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'EXPONENT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='EXPONENT', use_clamp=use_clamp)
    return node._out

def min(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'MINIMUM'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MINIMUM', use_clamp=use_clamp)
    return node._out

def max(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'MAXIMUM'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MAXIMUM', use_clamp=use_clamp)
    return node._out

def mless_than(value: Float = None, threshold: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'LESS_THAN'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - threshold (Float) : socket 'Threshold' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': threshold}, operation='LESS_THAN', use_clamp=use_clamp)
    return node._out

def mgreater_than(value: Float = None, threshold: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'GREATER_THAN'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - threshold (Float) : socket 'Threshold' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': threshold}, operation='GREATER_THAN', use_clamp=use_clamp)
    return node._out

def sign(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SIGN'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='SIGN', use_clamp=use_clamp)
    return node._out

def compare(value: Float = None,
                    value_1: Float = None,
                    epsilon: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'COMPARE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - epsilon (Float) : socket 'Epsilon' (id: Value_002)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': epsilon}, operation='COMPARE', use_clamp=use_clamp)
    return node._out

def smooth_min(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SMOOTH_MIN'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - distance (Float) : socket 'Distance' (id: Value_002)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': distance}, operation='SMOOTH_MIN', use_clamp=use_clamp)
    return node._out

def smooth_max(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SMOOTH_MAX'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - distance (Float) : socket 'Distance' (id: Value_002)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': distance}, operation='SMOOTH_MAX', use_clamp=use_clamp)
    return node._out

def round(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ROUND'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='ROUND', use_clamp=use_clamp)
    return node._out

def floor(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'FLOOR'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='FLOOR', use_clamp=use_clamp)
    return node._out

def ceil(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'CEIL'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='CEIL', use_clamp=use_clamp)
    return node._out

def trunc(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'TRUNC'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='TRUNC', use_clamp=use_clamp)
    return node._out

def fract(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'FRACT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='FRACT', use_clamp=use_clamp)
    return node._out

def modulo(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'MODULO'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MODULO', use_clamp=use_clamp)
    return node._out

def floored_modulo(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'FLOORED_MODULO'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='FLOORED_MODULO', use_clamp=use_clamp)
    return node._out

def wrap(value: Float = None, max: Float = None, min: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'WRAP'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - max (Float) : socket 'Max' (id: Value_001)
    - min (Float) : socket 'Min' (id: Value_002)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': max, 'Value_002': min}, operation='WRAP', use_clamp=use_clamp)
    return node._out

def snap(value: Float = None, increment: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SNAP'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - increment (Float) : socket 'Increment' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': increment}, operation='SNAP', use_clamp=use_clamp)
    return node._out

def pingpong(value: Float = None, scale: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'PINGPONG'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - scale (Float) : socket 'Scale' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': scale}, operation='PINGPONG', use_clamp=use_clamp)
    return node._out

def sin(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SINE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='SINE', use_clamp=use_clamp)
    return node._out

def cos(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'COSINE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='COSINE', use_clamp=use_clamp)
    return node._out

def tan(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'TANGENT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='TANGENT', use_clamp=use_clamp)
    return node._out

def asin(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ARCSINE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='ARCSINE', use_clamp=use_clamp)
    return node._out

def acos(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ARCCOSINE'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='ARCCOSINE', use_clamp=use_clamp)
    return node._out

def arctangent(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ARCTANGENT'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='ARCTANGENT', use_clamp=use_clamp)
    return node._out

def atan2(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'ARCTAN2'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - value_1 (Float) : socket 'Value' (id: Value_001)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='ARCTAN2', use_clamp=use_clamp)
    return node._out

def sinh(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'SINH'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='SINH', use_clamp=use_clamp)
    return node._out

def cosh(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'COSH'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='COSH', use_clamp=use_clamp)
    return node._out

def tanh(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'TANH'

    Arguments
    ---------
    - value (Float) : socket 'Value' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': value}, operation='TANH', use_clamp=use_clamp)
    return node._out

def radians(degrees: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'RADIANS'

    Arguments
    ---------
    - degrees (Float) : socket 'Degrees' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': degrees}, operation='RADIANS', use_clamp=use_clamp)
    return node._out

def degrees(radians: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    Information
    -----------
    - Parameter 'operation' : 'DEGREES'

    Arguments
    ---------
    - radians (Float) : socket 'Radians' (id: Value)
    - use_clamp (bool): parameter 'use_clamp'

    Returns
    -------
    - Float
    """
    node = Node('Math', {'Value': radians}, operation='DEGREES', use_clamp=use_clamp)
    return node._out

def vadd(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'ADD'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='ADD')
    return node._out

def vsubtract(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'SUBTRACT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='SUBTRACT')
    return node._out

def vmultiply(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'MULTIPLY'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MULTIPLY')
    return node._out

def vdivide(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'DIVIDE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='DIVIDE')
    return node._out

def vmultiply_add(vector: Vector = None, multiplier: Vector = None, addend: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'MULTIPLY_ADD'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - multiplier (Vector) : socket 'Multiplier' (id: Vector_001)
    - addend (Vector) : socket 'Addend' (id: Vector_002)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': multiplier, 'Vector_002': addend}, operation='MULTIPLY_ADD')
    return node._out

def cross(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'CROSS_PRODUCT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='CROSS_PRODUCT')
    return node._out

def project(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'PROJECT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='PROJECT')
    return node._out

def reflect(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'REFLECT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='REFLECT')
    return node._out

def refract(vector: Vector = None, vector_1: Vector = None, ior: Float = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'REFRACT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)
    - ior (Float) : socket 'IOR' (id: Scale)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1, 'Scale': ior}, operation='REFRACT')
    return node._out

def faceforward(vector: Vector = None, incident: Vector = None, reference: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'FACEFORWARD'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - incident (Vector) : socket 'Incident' (id: Vector_001)
    - reference (Vector) : socket 'Reference' (id: Vector_002)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': incident, 'Vector_002': reference}, operation='FACEFORWARD')
    return node._out

def dot(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'DOT_PRODUCT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Float
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='DOT_PRODUCT')
    return node._out

def distance(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'DISTANCE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Float
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='DISTANCE')
    return node._out

def length(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'LENGTH'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Float
    """
    node = Node('Vector Math', {'Vector': vector}, operation='LENGTH')
    return node._out

def scale(vector: Vector = None, scale: Float = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'SCALE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - scale (Float) : socket 'Scale' (id: Scale)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Scale': scale}, operation='SCALE')
    return node._out

def normalize(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'NORMALIZE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='NORMALIZE')
    return node._out

def vabs(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'ABSOLUTE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='ABSOLUTE')
    return node._out

def vpower(base: Vector = None, exponent: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'POWER'

    Arguments
    ---------
    - base (Vector) : socket 'Base' (id: Vector)
    - exponent (Vector) : socket 'Exponent' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': base, 'Vector_001': exponent}, operation='POWER')
    return node._out

def vsign(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'SIGN'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='SIGN')
    return node._out

def vmin(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'MINIMUM'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MINIMUM')
    return node._out

def vmax(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'MAXIMUM'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MAXIMUM')
    return node._out

def vfloor(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'FLOOR'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='FLOOR')
    return node._out

def vceil(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'CEIL'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='CEIL')
    return node._out

def vfraction(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'FRACTION'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='FRACTION')
    return node._out

def vmodulo(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'MODULO'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - vector_1 (Vector) : socket 'Vector' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MODULO')
    return node._out

def vwrap(vector: Vector = None, max: Vector = None, min: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'WRAP'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - max (Vector) : socket 'Max' (id: Vector_001)
    - min (Vector) : socket 'Min' (id: Vector_002)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': max, 'Vector_002': min}, operation='WRAP')
    return node._out

def vsnap(vector: Vector = None, increment: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'SNAP'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)
    - increment (Vector) : socket 'Increment' (id: Vector_001)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': increment}, operation='SNAP')
    return node._out

def vsin(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'SINE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='SINE')
    return node._out

def vcos(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'COSINE'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='COSINE')
    return node._out

def vtan(vector: Vector = None):
    """ > Node <&Node Vector Math>

    Information
    -----------
    - Parameter 'operation' : 'TANGENT'

    Arguments
    ---------
    - vector (Vector) : socket 'Vector' (id: Vector)

    Returns
    -------
    - Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='TANGENT')
    return node._out

