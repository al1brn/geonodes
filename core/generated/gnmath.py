# Generated 2026-04-05 13:26:22

from __future__ import annotations
from .. sockettype import SocketType
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
    class GreasePencil: ...
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

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'AND'` |

    Parameters
    ----------
    a : Integer, optional
        socket 'A' (id: A)
    
    b : Integer, optional
        socket 'B' (id: B)
    

    Returns
    -------
    Integer
    """
    node = Node('Bit Math', {'A': a, 'B': b}, operation='AND')
    return node._out

def bw_or(a: Integer = None, b: Integer = None):
    """ > Node <&Node Bit Math>

    **Fixed values**

    | Kind      | Name        | Value  |
    | --------- | ----------- | ------ |
    | Parameter | `operation` | `'OR'` |

    Parameters
    ----------
    a : Integer, optional
        socket 'A' (id: A)
    
    b : Integer, optional
        socket 'B' (id: B)
    

    Returns
    -------
    Integer
    """
    node = Node('Bit Math', {'A': a, 'B': b}, operation='OR')
    return node._out

def bw_xor(a: Integer = None, b: Integer = None):
    """ > Node <&Node Bit Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'XOR'` |

    Parameters
    ----------
    a : Integer, optional
        socket 'A' (id: A)
    
    b : Integer, optional
        socket 'B' (id: B)
    

    Returns
    -------
    Integer
    """
    node = Node('Bit Math', {'A': a, 'B': b}, operation='XOR')
    return node._out

def bw_not(a: Integer = None):
    """ > Node <&Node Bit Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'NOT'` |

    Parameters
    ----------
    a : Integer, optional
        socket 'A' (id: A)
    

    Returns
    -------
    Integer
    """
    node = Node('Bit Math', {'A': a}, operation='NOT')
    return node._out

def bw_shift(a: Integer = None, shift: Integer = None):
    """ > Node <&Node Bit Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'SHIFT'` |

    Parameters
    ----------
    a : Integer, optional
        socket 'A' (id: A)
    
    shift : Integer, optional
        socket 'Shift' (id: Shift)
    

    Returns
    -------
    Integer
    """
    node = Node('Bit Math', {'A': a, 'Shift': shift}, operation='SHIFT')
    return node._out

def bw_rotate(a: Integer = None, shift: Integer = None):
    """ > Node <&Node Bit Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'ROTATE'` |

    Parameters
    ----------
    a : Integer, optional
        socket 'A' (id: A)
    
    shift : Integer, optional
        socket 'Shift' (id: Shift)
    

    Returns
    -------
    Integer
    """
    node = Node('Bit Math', {'A': a, 'Shift': shift}, operation='ROTATE')
    return node._out

def band(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'AND'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='AND')
    return node._out

def bor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value  |
    | --------- | ----------- | ------ |
    | Parameter | `operation` | `'OR'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='OR')
    return node._out

def bnot(boolean: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'NOT'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean}, operation='NOT')
    return node._out

def not_and(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'NAND'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NAND')
    return node._out

def nor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'NOR'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NOR')
    return node._out

def xnor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'XNOR'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='XNOR')
    return node._out

def xor(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'XOR'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='XOR')
    return node._out

def imply(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'IMPLY'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='IMPLY')
    return node._out

def nimply(boolean: Boolean = None, boolean_1: Boolean = None):
    """ > Node <&Node Boolean Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'NIMPLY'` |

    Parameters
    ----------
    boolean : Boolean, optional
        socket 'Boolean' (id: Boolean)
    
    boolean_1 : Boolean, optional
        socket 'Boolean' (id: Boolean_001)
    

    Returns
    -------
    Boolean
    """
    node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NIMPLY')
    return node._out

def iadd(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'ADD'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='ADD')
    return node._out

def isubtract(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'SUBTRACT'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='SUBTRACT')
    return node._out

def imultiply(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'MULTIPLY'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MULTIPLY')
    return node._out

def idivide(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'DIVIDE'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE')
    return node._out

def imultiply_add(value: Integer = None, multiplier: Integer = None, addend: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'MULTIPLY_ADD'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    multiplier : Integer, optional
        socket 'Multiplier' (id: Value_001)
    
    addend : Integer, optional
        socket 'Addend' (id: Value_002)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD')
    return node._out

def iabs(value: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'ABSOLUTE'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value}, operation='ABSOLUTE')
    return node._out

def negate(value: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'NEGATE'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value}, operation='NEGATE')
    return node._out

def ipower(base: Integer = None, exponent: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'POWER'` |

    Parameters
    ----------
    base : Integer, optional
        socket 'Base' (id: Value)
    
    exponent : Integer, optional
        socket 'Exponent' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': base, 'Value_001': exponent}, operation='POWER')
    return node._out

def imin(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'MINIMUM'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MINIMUM')
    return node._out

def imax(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'MAXIMUM'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MAXIMUM')
    return node._out

def isign(value: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SIGN'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value}, operation='SIGN')
    return node._out

def divide_round(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'DIVIDE_ROUND'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE_ROUND')
    return node._out

def divide_floor(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'DIVIDE_FLOOR'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE_FLOOR')
    return node._out

def divide_ceil(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value           |
    | --------- | ----------- | --------------- |
    | Parameter | `operation` | `'DIVIDE_CEIL'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE_CEIL')
    return node._out

def ifloored_modulo(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value              |
    | --------- | ----------- | ------------------ |
    | Parameter | `operation` | `'FLOORED_MODULO'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='FLOORED_MODULO')
    return node._out

def imodulo(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'MODULO'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='MODULO')
    return node._out

def gcd(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'GCD'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='GCD')
    return node._out

def lcm(value: Integer = None, value_1: Integer = None):
    """ > Node <&Node Integer Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'LCM'` |

    Parameters
    ----------
    value : Integer, optional
        socket 'Value' (id: Value)
    
    value_1 : Integer, optional
        socket 'Value' (id: Value_001)
    

    Returns
    -------
    Integer
    """
    node = Node('Integer Math', {'Value': value, 'Value_001': value_1}, operation='LCM')
    return node._out

def add(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'ADD'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='ADD', use_clamp=use_clamp)
    return node._out

def subtract(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'SUBTRACT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='SUBTRACT', use_clamp=use_clamp)
    return node._out

def multiply(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'MULTIPLY'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MULTIPLY', use_clamp=use_clamp)
    return node._out

def divide(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'DIVIDE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='DIVIDE', use_clamp=use_clamp)
    return node._out

def multiply_add(value: Float = None,
                    multiplier: Float = None,
                    addend: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'MULTIPLY_ADD'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    multiplier : Float, optional
        socket 'Multiplier' (id: Value_001)
    
    addend : Float, optional
        socket 'Addend' (id: Value_002)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD', use_clamp=use_clamp)
    return node._out

def power(base: Float = None, exponent: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'POWER'` |

    Parameters
    ----------
    base : Float, optional
        socket 'Base' (id: Value)
    
    exponent : Float, optional
        socket 'Exponent' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': base, 'Value_001': exponent}, operation='POWER', use_clamp=use_clamp)
    return node._out

def log(value: Float = None, base: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value         |
    | --------- | ----------- | ------------- |
    | Parameter | `operation` | `'LOGARITHM'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    base : Float, optional
        socket 'Base' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': base}, operation='LOGARITHM', use_clamp=use_clamp)
    return node._out

def sqrt(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SQRT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='SQRT', use_clamp=use_clamp)
    return node._out

def inverse_sqrt(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'INVERSE_SQRT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='INVERSE_SQRT', use_clamp=use_clamp)
    return node._out

def abs(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'ABSOLUTE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='ABSOLUTE', use_clamp=use_clamp)
    return node._out

def exp(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'EXPONENT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='EXPONENT', use_clamp=use_clamp)
    return node._out

def min(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'MINIMUM'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MINIMUM', use_clamp=use_clamp)
    return node._out

def max(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'MAXIMUM'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MAXIMUM', use_clamp=use_clamp)
    return node._out

def mless_than(value: Float = None, threshold: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value         |
    | --------- | ----------- | ------------- |
    | Parameter | `operation` | `'LESS_THAN'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    threshold : Float, optional
        socket 'Threshold' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': threshold}, operation='LESS_THAN', use_clamp=use_clamp)
    return node._out

def mgreater_than(value: Float = None, threshold: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'GREATER_THAN'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    threshold : Float, optional
        socket 'Threshold' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': threshold}, operation='GREATER_THAN', use_clamp=use_clamp)
    return node._out

def sign(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SIGN'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='SIGN', use_clamp=use_clamp)
    return node._out

def compare(value: Float = None,
                    value_1: Float = None,
                    epsilon: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'COMPARE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    epsilon : Float, optional
        socket 'Epsilon' (id: Value_002)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': epsilon}, operation='COMPARE', use_clamp=use_clamp)
    return node._out

def smooth_min(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value          |
    | --------- | ----------- | -------------- |
    | Parameter | `operation` | `'SMOOTH_MIN'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    distance : Float, optional
        socket 'Distance' (id: Value_002)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': distance}, operation='SMOOTH_MIN', use_clamp=use_clamp)
    return node._out

def smooth_max(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value          |
    | --------- | ----------- | -------------- |
    | Parameter | `operation` | `'SMOOTH_MAX'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    distance : Float, optional
        socket 'Distance' (id: Value_002)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': distance}, operation='SMOOTH_MAX', use_clamp=use_clamp)
    return node._out

def round(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'ROUND'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='ROUND', use_clamp=use_clamp)
    return node._out

def floor(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'FLOOR'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='FLOOR', use_clamp=use_clamp)
    return node._out

def ceil(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'CEIL'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='CEIL', use_clamp=use_clamp)
    return node._out

def trunc(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'TRUNC'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='TRUNC', use_clamp=use_clamp)
    return node._out

def fract(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'FRACT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='FRACT', use_clamp=use_clamp)
    return node._out

def modulo(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'MODULO'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='MODULO', use_clamp=use_clamp)
    return node._out

def floored_modulo(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value              |
    | --------- | ----------- | ------------------ |
    | Parameter | `operation` | `'FLOORED_MODULO'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='FLOORED_MODULO', use_clamp=use_clamp)
    return node._out

def wrap(value: Float = None, max: Float = None, min: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'WRAP'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    max : Float, optional
        socket 'Max' (id: Value_001)
    
    min : Float, optional
        socket 'Min' (id: Value_002)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': max, 'Value_002': min}, operation='WRAP', use_clamp=use_clamp)
    return node._out

def snap(value: Float = None, increment: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SNAP'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    increment : Float, optional
        socket 'Increment' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': increment}, operation='SNAP', use_clamp=use_clamp)
    return node._out

def pingpong(value: Float = None, scale: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'PINGPONG'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    scale : Float, optional
        socket 'Scale' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': scale}, operation='PINGPONG', use_clamp=use_clamp)
    return node._out

def sin(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SINE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='SINE', use_clamp=use_clamp)
    return node._out

def cos(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'COSINE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='COSINE', use_clamp=use_clamp)
    return node._out

def tan(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'TANGENT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='TANGENT', use_clamp=use_clamp)
    return node._out

def asin(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'ARCSINE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='ARCSINE', use_clamp=use_clamp)
    return node._out

def acos(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value         |
    | --------- | ----------- | ------------- |
    | Parameter | `operation` | `'ARCCOSINE'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='ARCCOSINE', use_clamp=use_clamp)
    return node._out

def arctangent(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value          |
    | --------- | ----------- | -------------- |
    | Parameter | `operation` | `'ARCTANGENT'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='ARCTANGENT', use_clamp=use_clamp)
    return node._out

def atan2(value: Float = None, value_1: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'ARCTAN2'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    value_1 : Float, optional
        socket 'Value' (id: Value_001)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value, 'Value_001': value_1}, operation='ARCTAN2', use_clamp=use_clamp)
    return node._out

def sinh(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SINH'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='SINH', use_clamp=use_clamp)
    return node._out

def cosh(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'COSH'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='COSH', use_clamp=use_clamp)
    return node._out

def tanh(value: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'TANH'` |

    Parameters
    ----------
    value : Float, optional
        socket 'Value' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': value}, operation='TANH', use_clamp=use_clamp)
    return node._out

def radians(degrees: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'RADIANS'` |

    Parameters
    ----------
    degrees : Float, optional
        socket 'Degrees' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': degrees}, operation='RADIANS', use_clamp=use_clamp)
    return node._out

def degrees(radians: Float = None, use_clamp = False):
    """ > Node <&Node Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'DEGREES'` |

    Parameters
    ----------
    radians : Float, optional
        socket 'Radians' (id: Value)
    
    use_clamp : bool
        parameter `use_clamp`
    

    Returns
    -------
    Float
    """
    node = Node('Math', {'Value': radians}, operation='DEGREES', use_clamp=use_clamp)
    return node._out

def vadd(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value   |
    | --------- | ----------- | ------- |
    | Parameter | `operation` | `'ADD'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='ADD')
    return node._out

def vsubtract(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'SUBTRACT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='SUBTRACT')
    return node._out

def vmultiply(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'MULTIPLY'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MULTIPLY')
    return node._out

def vdivide(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'DIVIDE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='DIVIDE')
    return node._out

def vmultiply_add(vector: Vector = None, multiplier: Vector = None, addend: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value            |
    | --------- | ----------- | ---------------- |
    | Parameter | `operation` | `'MULTIPLY_ADD'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    multiplier : Vector, optional
        socket 'Multiplier' (id: Vector_001)
    
    addend : Vector, optional
        socket 'Addend' (id: Vector_002)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': multiplier, 'Vector_002': addend}, operation='MULTIPLY_ADD')
    return node._out

def cross(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value             |
    | --------- | ----------- | ----------------- |
    | Parameter | `operation` | `'CROSS_PRODUCT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='CROSS_PRODUCT')
    return node._out

def project(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'PROJECT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='PROJECT')
    return node._out

def reflect(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'REFLECT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='REFLECT')
    return node._out

def refract(vector: Vector = None, vector_1: Vector = None, ior: Float = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'REFRACT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    
    ior : Float, optional
        socket 'IOR' (id: Scale)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1, 'Scale': ior}, operation='REFRACT')
    return node._out

def faceforward(vector: Vector = None, incident: Vector = None, reference: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value           |
    | --------- | ----------- | --------------- |
    | Parameter | `operation` | `'FACEFORWARD'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    incident : Vector, optional
        socket 'Incident' (id: Vector_001)
    
    reference : Vector, optional
        socket 'Reference' (id: Vector_002)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': incident, 'Vector_002': reference}, operation='FACEFORWARD')
    return node._out

def dot(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value           |
    | --------- | ----------- | --------------- |
    | Parameter | `operation` | `'DOT_PRODUCT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Float
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='DOT_PRODUCT')
    return node._out

def distance(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'DISTANCE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Float
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='DISTANCE')
    return node._out

def length(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'LENGTH'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Float
    """
    node = Node('Vector Math', {'Vector': vector}, operation='LENGTH')
    return node._out

def scale(vector: Vector = None, scale: Float = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'SCALE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    scale : Float, optional
        socket 'Scale' (id: Scale)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Scale': scale}, operation='SCALE')
    return node._out

def normalize(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value         |
    | --------- | ----------- | ------------- |
    | Parameter | `operation` | `'NORMALIZE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='NORMALIZE')
    return node._out

def vabs(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'ABSOLUTE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='ABSOLUTE')
    return node._out

def vpower(base: Vector = None, exponent: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'POWER'` |

    Parameters
    ----------
    base : Vector, optional
        socket 'Base' (id: Vector)
    
    exponent : Vector, optional
        socket 'Exponent' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': base, 'Vector_001': exponent}, operation='POWER')
    return node._out

def vsign(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SIGN'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='SIGN')
    return node._out

def vmin(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'MINIMUM'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MINIMUM')
    return node._out

def vmax(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'MAXIMUM'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MAXIMUM')
    return node._out

def vround(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'ROUND'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='ROUND')
    return node._out

def vfloor(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value     |
    | --------- | ----------- | --------- |
    | Parameter | `operation` | `'FLOOR'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='FLOOR')
    return node._out

def vceil(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'CEIL'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='CEIL')
    return node._out

def vfraction(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value        |
    | --------- | ----------- | ------------ |
    | Parameter | `operation` | `'FRACTION'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='FRACTION')
    return node._out

def vmodulo(vector: Vector = None, vector_1: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'MODULO'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    vector_1 : Vector, optional
        socket 'Vector' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1}, operation='MODULO')
    return node._out

def vwrap(vector: Vector = None, max: Vector = None, min: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'WRAP'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    max : Vector, optional
        socket 'Max' (id: Vector_001)
    
    min : Vector, optional
        socket 'Min' (id: Vector_002)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': max, 'Vector_002': min}, operation='WRAP')
    return node._out

def vsnap(vector: Vector = None, increment: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SNAP'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    
    increment : Vector, optional
        socket 'Increment' (id: Vector_001)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector, 'Vector_001': increment}, operation='SNAP')
    return node._out

def vsin(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value    |
    | --------- | ----------- | -------- |
    | Parameter | `operation` | `'SINE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='SINE')
    return node._out

def vcos(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value      |
    | --------- | ----------- | ---------- |
    | Parameter | `operation` | `'COSINE'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='COSINE')
    return node._out

def vtan(vector: Vector = None):
    """ > Node <&Node Vector Math>

    **Fixed values**

    | Kind      | Name        | Value       |
    | --------- | ----------- | ----------- |
    | Parameter | `operation` | `'TANGENT'` |

    Parameters
    ----------
    vector : Vector, optional
        socket 'Vector' (id: Vector)
    

    Returns
    -------
    Vector
    """
    node = Node('Vector Math', {'Vector': vector}, operation='TANGENT')
    return node._out

