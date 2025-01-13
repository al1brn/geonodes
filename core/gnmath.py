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

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : gnmath
-----------------
- Math library

Implements the operations fro 'Math', 'Integer Math', 'Vector Math' and 'Boolean Math'.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START
> math library

**gnmath** libray contains the math functions for data <!Boolean"Booleans>, <!Float"Floats> and
<!Vector"Vectors> using the following nodes:
- **'Boolean Math'**
- **'Math'**
- **'Vector Math'**
- **'Integer Math'**

The name of the functions is the name of the 'operation' parameter of the node,
with some changes according the following rules:
- use python math library when it exists: <#sin> and <#cos> rather than 'sine' and 'cosine' for instance
- prefix with char ***'v'*** for <!Vector> functions when it collides with a <!Float> function : <#vsin> and <#vcos> for instance
- prefix with char ***'i'*** for <!Integer> functions when it collides with a <!Float> function : <#iadd> and <#imodulo> for instance
- prefix with char ***'b'*** boolean reserved keywords : <#band>, <#bor> and <#bnot>
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

import numpy as np

from .treeclass import Tree, Node

# =============================================================================================================================
# Boolean Math

def band(value, other):
    """ Boolean AND.

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

    Arguments
    ---------
    - value (Boolean) : value

    Returns
    - Boolean
    """

    return Node("Boolean Math", {0: value}, operation='NOT')._out

def nand(value, other):
    """ Boolean NAND.

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Boolean Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

    Arguments
    ---------
    - value (Float) : value

    Returns
    - Float
    """

    return Node("Math", {0: value}, operation='SIGN')._out

def compare(value, other, epsilon=None, use_clamp=None):
    """ Math COMPARE.

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math, Float to Integer>

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

    > Node <&Node Math, Float to Integer>

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

    > Node <&Node Math, Float to Integer>

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

    > Node <&Node Math, Float to Integer>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

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

    > Node <&Node Math>

    Arguments
    ---------
    - value (Float) : value
    - use_clamp (bool) : use_clamp flag

    Returns
    - Float
    """
    return Node("Math", {0: value}, use_clamp=use_clamp, operation='DEGREES')._out

# =============================================================================================================================
# Integer Math
# 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD',
# 'ABSOLUTE', 'NEGATE', 'POWER',
# 'MINIMUM', 'MAXIMUM', 'SIGN',
# 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL',
# 'FLOORED_MODULO', 'MODULO',
# 'GCD', 'LCM'

def iadd(value, other):
    """ Integer ADD.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='ADD')._out

def isubtract(value, other):
    """ Integer SUBTRACT.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='SUBTRACT')._out

def imultiply(value, other):
    """ Integer Math MULTIPLY.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='MULTIPLY')._out

def idivide(value, other):
    """ Integer Math DIVIDE.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='DIVIDE')._out

def imultiply_add(value, multiplier, addend):
    """ Integer Math MULTIPLY ADD.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : value
    - multiplier (Integer) : multiplier value
    - addend(Integer) : add end value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, multiplier, addend], operation='MULTIPLY_ADD')._out

def iabs(value):
    """ Integer Math ABSOLUTE.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : value

    Returns
    - Integer
    """
    return Node("Integer Math", [value], operation='ABSOLUTE')._out

def inegate(value):
    """ Integer Math NEGATE.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : value

    Returns
    - Integer
    """
    return Node("Integer Math", [value], operation='NEGATE')._out

def ipower(base, exponent):
    """ Integer Math POWER.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - base (Integer) : value
    - exponent (Integer) : value

    Returns
    - Integer
    """
    return Node("Integer Math", [base, exponent], operation='POWER')._out

def imin(value, other):
    """ Integer Math MINIMUM.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='MINIMUM')._out

def imax(value, other):
    """ Integer Math MAXIMUM.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='MAXIMUM')._out

def isign(value):
    """ Integer Math SIGN.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : value

    Returns
    - Integer
    """
    return Node("Integer Math", [value], operation='SIGN')._out

def idivide_round(value, other):
    """ Integer Math DIVIDE_ROUND.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='DIVIDE_ROUND')._out

def idivide_floor(value, other):
    """ Integer Math DIVIDE_FLOOR.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='DIVIDE_FLOOR')._out

def idivide_ceiling(value, other):
    """ Integer Math DIVIDE_CEIL.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='DIVIDE_CEIL')._out

def ifloored_modulo(value, other):
    """ Integer Math FLOORED_MODULO.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='FLOORED_MODULO')._out


def imodulo(value, other):
    """ Integer Math MODULO.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='MODULO')._out

def GCD(value, other):
    """ Integer Math GCD.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='GCD')._out

def LCM(value, other):
    """ Integer Math LCM.

    > Node <&Node Integer Math>

    Arguments
    ---------
    - value (Integer) : first value
    - other (Integer) : second value

    Returns
    - Integer
    """
    return Node("Integer Math", [value, other], operation='LCM')._out

# =============================================================================================================================
# Vector Math

def vadd(value, other):
    """ Vector Math ADD.

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Float
    """
    return Node("Vector Math", {0: value}, operation='LENGTH')._out

def scale(value, scale):
    """ Vector Math SCALE.

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='NORMALIZE')._out

def vabs(value):
    """ Vector Math ABS.

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='ABSOLUTE')._out

def vmin(value, other):
    """ Vector Math MINIMUM.

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='FLOOR')._out

def vceil(value):
    """ Vector Math CEIL.

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='CEIL')._out

def vfract(value):
    """ Vector Math FRACT.

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='FRACTION')._out

def vmodulo(value, other):
    """ Vector Math MODULO.

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value, 1: other}, operation='MODULO')._out

def vwrap(value, max=None, min=None):
    """ Vector Math WRAP.

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

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

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='SINE')._out

def vcos(value):
    """ Vector Math COS.

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='COSINE')._out

def vtan(value):
    """ Vector Math TAN.

    > Node <&Node Vector Math>

    Arguments
    ---------
    - value (Vector) : vector

    Returns
    - Vector
    """
    return Node("Vector Math", {0: value}, operation='TANGENT')._out
