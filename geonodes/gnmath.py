"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : gnmath
---------------
- Implement geometry nodes math functions

Note that this module is name gnmath rather than math to avoid collision with math standard module

classes
-------

functions
---------
'Math', 'Vector math' and 'Boolean Math' functions
When there is a collision between Math and Vector Math, the vector math function is prefixed by character 'v':
    - sin(Float)
    - vsin(vector)

Boolean math is prefixed by character 'b' when the name collides with python operator:
    - band(bool1, bool2)
    - xor(bool1, bool2)

round, ceil, floor and trunc are implemented by 'Math' node and 'Float to Integer' node.
The second one returns an Integer rather than a Float.
The implementation from 'Math' is prefixed with 'math_':
    - math_floor() -> Float
    -floor() -> Integer

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import numpy as np

from .treeclass import Tree, Node

# =============================================================================================================================
# Boolean Math

def band(value, other):
    """ Boolean AND.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='AND')._out

def bor(value, other):
    """ Boolean OR.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='OR')._out

def bnot(value):
    """ Boolean NOT.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value}, operation='NOT')._out

def nand(value, other):
    """ Boolean NAND.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='NAND')._out

def nor(value, other):
    """ Boolean NOR.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='NOR')._out

def xnor(value, other):
    """ Boolean XNOR.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='XNOR')._out

def equal(value, other):
    """ Boolean XNOR.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return xnor(value, other)

def xor(value, other):
    """ Boolean XOR.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='XOR')._out

def not_equal(value, other):
    """ Boolean XOR.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return xor(value, other)

def imply(value, other):
    """ Boolean IMPLY.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='IMPLY')._out

def nimply(value, other):
    """ Boolean NIMPLY.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value, 1: other}, operation='NIMPLY')._out

def bsubtract(value, other):
    """ Boolean NIMPLY.

    [!Node] Boolean Math

    Arguments
    ---------
    - value (Boolean) : first value
    - other (Boolean) : second value

    Returns
    - Boolean
    """

    return nimply(value, other)


# =============================================================================================================================
# Float Math

def add(value, other, use_clamp=None):
    """ Math ADD.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='ADD')._out

def subtract(value, other, use_clamp=None):
    """ Math SUBTRACT.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='SUBTRACT')._out

def multiply(value, other, use_clamp=None):
    """ Math MULTIPLY.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MULTIPLY')._out

def divide(value, other, use_clamp=None):
    """ Math DIVIDE.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='DIVIDE')._out

def multiply_add(value, multiplier, addend, use_clamp=None):
    """ Math MULTIPLY ADD.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - multiplier (Float) : multiplier value
    - addend(Float) : add end value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: multiplier, 2: addend}, use_clamp=use_clamp, operation='MULTIPLY_ADD')._out

def power(base, exponent, use_clamp=None):
    """ Math POWER.

    [!Node] Math

    Arguments
    ---------
    - base (Float) : base value
    - exponent (Float) : exponent value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: base, 1: exponent}, use_clamp=use_clamp, operation='POWER')._out

def log(value, base=10, use_clamp=None):
    """ Math LOGARITHM.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - base (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: base}, use_clamp=use_clamp, operation='LOGARITHM')._out

def ln(value, use_clamp=None):
    """ Math neperian LOGARITHM (using base = e).

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: np.e}, use_clamp=use_clamp, operation='LOGARITHM')._out

def sqrt(value, use_clamp=None):
    """ Math SQRT.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value}, use_clamp=use_clamp, operation='SQRT')._out

def inverse_sqrt(value, use_clamp=None):
    """ Math INVERSE SQRT.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value}, use_clamp=use_clamp, operation='INVERSE_SQRT')._out

def abs(value, use_clamp=None):
    """ Math ABSOLUTE.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value}, use_clamp=use_clamp, operation='ABSOLUTE')._out

def exponent(value, use_clamp=None):
    """ Math EXPONENT.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value}, use_clamp=use_clamp, operation='EXPONENT')._out

def exp(value, use_clamp=None):
    """ Math EXPONENT.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return exponent(value, use_clamp=use_clamp)

def min(value, other, use_clamp=None):
    """ Math MINIMUM.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MINIMUM')._out

def max(value, other, use_clamp=None):
    """ Math MAXIMUM.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MAXIMUM')._out

def less_than(value, threshold, use_clamp=None):
    """ Math LESS_THAN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - threshold (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: threshold}, use_clamp=use_clamp, operation='LESS_THAN')._out

def greater_than(value, threshold, use_clamp=None):
    """ Math GREATER THAN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - threshold (Float) : second value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: threshold}, use_clamp=use_clamp, operation='GREATER_THAN')._out

def sign(value):
    """ Math SIGN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value

    Returns
    - Float
    """

    return Node("Math", {0: value}, operation='SIGN')._out

def compare(value, other, epsilon=None, use_clamp=None):
    """ Math COMPARE.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - epsilon (Float=None) : epsilon
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other, 2:epsilon}, use_clamp=use_clamp, operation='COMPARE')._out

def smooth_min(value, other, distance=None, use_clamp=None):
    """ Math SMOOTH_MIN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - distance (Float) : distance
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other, 2:distance}, use_clamp=use_clamp, operation='SMOOTH_MIN')._out

def smooth_max(value, other, distance=None, use_clamp=None):
    """ Math SMOOTH MAX.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : first value
    - other (Float) : second value
    - distance (Float) : distance
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value, 1: other, 2: distance}, use_clamp=use_clamp, operation='SMOOTH_MAX')._out

def math_round(value, use_clamp=None):
    """ Math ROUND.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """

    return Node("Math", {0: value}, use_clamp=use_clamp, operation='ROUND')._out

def math_floor(value, use_clamp=None):
    """ Math FLOOR.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='FLOOR')._out

def math_ceil(value, use_clamp=None):
    """ Math CEIL.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='CEIL')._out

def math_trunc(value, use_clamp=None):
    """ Math TRUNC.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='TRUNC')._out

def round(value, use_clamp=None):
    """ Round.

    [!Node] Math, Float to Integer

    Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

    rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float (ShaderNodes) or Integer (GeoNodes)
    """
    if Tree.is_geonodes:
        return Node("Float to Integer", {'Float': value}, rounding_mode='ROUND')._out
    else:
        return math_round(value, use_clamp=use_clamp)

def floor(value, use_clamp=None):
    """ Floor.

    [!Node] Math, Float to Integer

    Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

    rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float (ShaderNodes) or Integer (GeoNodes)
    """
    if Tree.is_geonodes:
        return Node("Float to Integer", {'Float': value}, rounding_mode='FLOOR')._out
    else:
        return math_floor(value, use_clamp=use_clamp)

def ceil(value, use_clamp=None):
    """ Ceiling.

    [!Node] Math, Float to Integer

    Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

    rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float (ShaderNodes) or Integer (GeoNodes)
    """
    if Tree.is_geonodes:
        return Node("Float to Integer", {'Float': value}, rounding_mode='CEILING')._out
    else:
        return math_ceil(value, use_clamp=use_clamp)

def trunc(value, use_clamp=None):
    """ Truncate.

    [!Node] Math, Float to Integer

    Implements 'Math' node in ShaderNodes and 'Float to Integer' for GeoNodes.

    rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float (ShaderNodes) or Integer (GeoNodes)
    """

    if Tree.is_geonodes:
        return Node("Float to Integer", {'Float': value}, rounding_mode='TRUNCATE')._out
    else:
        return math_trunc(value, use_clamp=use_clamp)

def fract(value, use_clamp=None):
    """ Math FRACT.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='FRACT')._out

def modulo(value, other, use_clamp=None):
    """ Math MODULO.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - other (Float) : other value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MODULO')._out

def floored_modulo(value, other, use_clamp=None):
    """ Math FLOORED MODULO.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - other (Float) : other value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='FLOORED_MODULO')._out

def wrap(value, max=None, min=None, use_clamp=None):
    """ Math WRAP.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - max (Float) : max value
    - min (Float) : min value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: max, 2: min}, use_clamp=use_clamp, operation='WRAP')._out

def snap(value, increment=None, use_clamp=None):
    """ Math SNAP.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - increment (Float) : other value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: increment}, use_clamp=use_clamp, operation='SNAP')._out

def ping_pong(value, scale=None, use_clamp=None):
    """ Math PINGPONG.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - scale (Float) : other value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: scale}, use_clamp=use_clamp, operation='PINGPONG')._out

def pingpong(value, scale=None, use_clamp=None):
    """ Math PINGPONG.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - scale (Float) : other value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: scale}, use_clamp=use_clamp, operation='PINGPONG')._out

def sin(value, use_clamp=None):
    """ Math SIN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='SINE')._out

def cos(value, use_clamp=None):
    """ Math COS.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='COSINE')._out

def tan(value, use_clamp=None):
    """ Math TAN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='TANGENT')._out

def asin(value, use_clamp=None):
    """ Math ASIN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='ARCSINE')._out

def acos(value, use_clamp=None):
    """ Math ACOS.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='ARCCOSINE')._out

def atan(value, use_clamp=None):
    """ Math ATAN.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='ARCTANGENT')._out

def atan2(value, other, use_clamp=None):
    """ Math ATAN2.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - other (Float) : other value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='ARCTAN2')._out

def sinh(value, use_clamp=None):
    """ Math SINH.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='SINH')._out

def cosh(value, use_clamp=None):
    """ Math COSH.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='COSH')._out

def tanh(value, use_clamp=None):
    """ Math TANH.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='TANH')._out

def radians(value, use_clamp=None):
    """ Math RADIANS.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='RADIANS')._out

def degrees(value, use_clamp=None):
    """ Math DEGREES.

    [!Node] Math

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='DEGREES')._out

# =============================================================================================================================
# Vector Math

def vadd(value, other):
    """ Vector Math ADD.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """

    return Node("Vector Math", {0: value, 1: other}, operation='ADD')._out

def vsubtract(value, other):
    """ Vector Math SUBTRACT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='SUBTRACT')._out

def vmultiply(value, other):
    """ Vector Math MULTIPLY.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='MULTIPLY')._out

def vdivide(value, other):
    """ Vector Math DIVIDE.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='DIVIDE')._out

def vmultiply_add(value, multiplier, addend):
    """ Vector Math MULTIPLY ADD.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - multiplier (Vector) : other vector
    - addend (Vector) : add end vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: multiplier, 2: addend}, operation='MULTIPLY_ADD')._out

def cross_product(value, other):
    """ Vector Math CROSS PRODUCT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='CROSS_PRODUCT')._out

def project(value, other):
    """ Vector Math PROJECT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='PROJECT')._out

def reflect(value, other):
    """ Vector Math REFLECT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='REFLECT')._out

def refract(value, other, ior=None):
    """ Vector Math REFRACT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector
    - ior (Float) : IOR

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other, 'Scale': ior}, operation='REFRACT')._out

def faceforward(value, incident=None, reference=None):
    """ Vector Math FACE FORWARD.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - incident (Vector) : incident vector
    - reference (Vector) : reference vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: incident, 2: reference}, operation='FACEFORWARD')._out

def dot_product(value, other):
    """ Vector Math DOT PRODUCT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Float
    """
    return Node("Vector Math", {0: value, 1: other}, operation='DOT_PRODUCT')._out

def distance(value, other):
    """ Vector Math DISTANCE.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Float
    """
    return Node("Vector Math", {0: value, 1: other}, operation='DISTANCE')._out

def length(value):
    """ Vector Math LENGTH.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Float
    """
    return Node("Vector Math", {0: value}, operation='LENGTH')._out

def scale(value, scale):
    """ Vector Math SCALE.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - scale (Float) : scale factor

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 'Scale': scale}, operation='SCALE')._out

def normalize(value):
    """ Vector Math NORMALIZE.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='NORMALIZE')._out

def vabs(value):
    """ Vector Math ABS.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='ABSOLUTE')._out

def vmin(value, other):
    """ Vector Math MINIMUM.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='MINIMUM')._out

def vmax(value, other):
    """ Vector Math MAXIMUM.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - other (Vector) : other vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='MAXIMUM')._out

def vfloor(value):
    """ Vector Math FLOOR.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='FLOOR')._out

def vceil(value):
    """ Vector Math CEIL.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='CEIL')._out

def vfract(value):
    """ Vector Math FRACT.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='FRACTION')._out

def vmodulo(value, other):
    """ Vector Math MODULO.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='MODULO')._out

def vwrap(value, max=None, min=None):
    """ Vector Math WRAP.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - max (Vector) : max vector
    - min (Vector) : min vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: max, 2: min}, operation='WRAP')._out

def vsnap(value, increment):
    """ Vector Math SNAP.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector
    - increment (Vector) : increment vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: increment}, operation='SNAP')._out

def vsin(value):
    """ Vector Math SIN.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='SINE')._out

def vcos(value):
    """ Vector Math COS.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='COSINE')._out

def vtan(value):
    """ Vector Math TAN.

    [!Node] Vector Math

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='TANGENT')._out