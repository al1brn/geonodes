from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

def band(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='AND')
    return node._out

def bor(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='OR')
    return node._out

def bnot(boolean=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean}, operation='NOT')
    return node._out

def not_and(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NAND')
    return node._out

def nor(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NOR')
    return node._out

def xnor(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='XNOR')
    return node._out

def xor(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='XOR')
    return node._out

def imply(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='IMPLY')
    return node._out

def nimply(boolean=None, boolean_1=None):
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
    node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation='NIMPLY')
    return node._out

def iadd(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='ADD')
    return node._out

def isubtract(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='SUBTRACT')
    return node._out

def imultiply(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='MULTIPLY')
    return node._out

def idivide(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='DIVIDE')
    return node._out

def imultiply_add(value=None, multiplier=None, addend=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD')
    return node._out

def iabs(value=None):
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
    node = Node('Integer Math', sockets={'Value': value}, operation='ABSOLUTE')
    return node._out

def negate(value=None):
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
    node = Node('Integer Math', sockets={'Value': value}, operation='NEGATE')
    return node._out

def ipower(base=None, exponent=None):
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
    node = Node('Integer Math', sockets={'Value': base, 'Value_001': exponent}, operation='POWER')
    return node._out

def imin(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='MINIMUM')
    return node._out

def imax(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='MAXIMUM')
    return node._out

def isign(value=None):
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
    node = Node('Integer Math', sockets={'Value': value}, operation='SIGN')
    return node._out

def divide_round(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='DIVIDE_ROUND')
    return node._out

def divide_floor(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='DIVIDE_FLOOR')
    return node._out

def divide_ceil(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='DIVIDE_CEIL')
    return node._out

def ifloored_modulo(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='FLOORED_MODULO')
    return node._out

def imodulo(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='MODULO')
    return node._out

def gcd(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='GCD')
    return node._out

def lcm(value=None, value_1=None):
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
    node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1}, operation='LCM')
    return node._out

def add(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='ADD', use_clamp=use_clamp)
    return node._out

def subtract(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='SUBTRACT', use_clamp=use_clamp)
    return node._out

def multiply(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='MULTIPLY', use_clamp=use_clamp)
    return node._out

def divide(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='DIVIDE', use_clamp=use_clamp)
    return node._out

def multiply_add(value=None, multiplier=None, addend=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD', use_clamp=use_clamp)
    return node._out

def power(base=None, exponent=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': base, 'Value_001': exponent}, operation='POWER', use_clamp=use_clamp)
    return node._out

def log(value=None, base=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': base}, operation='LOGARITHM', use_clamp=use_clamp)
    return node._out

def sqrt(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='SQRT', use_clamp=use_clamp)
    return node._out

def inverse_sqrt(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='INVERSE_SQRT', use_clamp=use_clamp)
    return node._out

def abs(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='ABSOLUTE', use_clamp=use_clamp)
    return node._out

def exp(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='EXPONENT', use_clamp=use_clamp)
    return node._out

def min(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='MINIMUM', use_clamp=use_clamp)
    return node._out

def max(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='MAXIMUM', use_clamp=use_clamp)
    return node._out

def mless_than(value=None, threshold=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': threshold}, operation='LESS_THAN', use_clamp=use_clamp)
    return node._out

def mgreater_than(value=None, threshold=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': threshold}, operation='GREATER_THAN', use_clamp=use_clamp)
    return node._out

def sign(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='SIGN', use_clamp=use_clamp)
    return node._out

def compare(value=None, value_1=None, epsilon=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1, 'Value_002': epsilon}, operation='COMPARE', use_clamp=use_clamp)
    return node._out

def smooth_min(value=None, value_1=None, distance=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1, 'Value_002': distance}, operation='SMOOTH_MIN', use_clamp=use_clamp)
    return node._out

def smooth_max(value=None, value_1=None, distance=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1, 'Value_002': distance}, operation='SMOOTH_MAX', use_clamp=use_clamp)
    return node._out

def round(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='ROUND', use_clamp=use_clamp)
    return node._out

def floor(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='FLOOR', use_clamp=use_clamp)
    return node._out

def ceil(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='CEIL', use_clamp=use_clamp)
    return node._out

def trunc(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='TRUNC', use_clamp=use_clamp)
    return node._out

def fract(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='FRACT', use_clamp=use_clamp)
    return node._out

def modulo(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='MODULO', use_clamp=use_clamp)
    return node._out

def floored_modulo(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='FLOORED_MODULO', use_clamp=use_clamp)
    return node._out

def wrap(value=None, max=None, min=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': max, 'Value_002': min}, operation='WRAP', use_clamp=use_clamp)
    return node._out

def snap(value=None, increment=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': increment}, operation='SNAP', use_clamp=use_clamp)
    return node._out

def pingpong(value=None, scale=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': scale}, operation='PINGPONG', use_clamp=use_clamp)
    return node._out

def sin(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='SINE', use_clamp=use_clamp)
    return node._out

def cos(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='COSINE', use_clamp=use_clamp)
    return node._out

def tan(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='TANGENT', use_clamp=use_clamp)
    return node._out

def asin(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='ARCSINE', use_clamp=use_clamp)
    return node._out

def acos(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='ARCCOSINE', use_clamp=use_clamp)
    return node._out

def arctangent(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='ARCTANGENT', use_clamp=use_clamp)
    return node._out

def atan2(value=None, value_1=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value, 'Value_001': value_1}, operation='ARCTAN2', use_clamp=use_clamp)
    return node._out

def sinh(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='SINH', use_clamp=use_clamp)
    return node._out

def cosh(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='COSH', use_clamp=use_clamp)
    return node._out

def tanh(value=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': value}, operation='TANH', use_clamp=use_clamp)
    return node._out

def radians(degrees=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': degrees}, operation='RADIANS', use_clamp=use_clamp)
    return node._out

def degrees(radians=None, use_clamp=False):
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
    node = Node('Math', sockets={'Value': radians}, operation='DEGREES', use_clamp=use_clamp)
    return node._out

def vadd(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='ADD')
    return node._out

def vsubtract(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='SUBTRACT')
    return node._out

def vmultiply(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='MULTIPLY')
    return node._out

def vdivide(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='DIVIDE')
    return node._out

def vmultiply_add(vector=None, multiplier=None, addend=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': multiplier, 'Vector_002': addend}, operation='MULTIPLY_ADD')
    return node._out

def cross(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='CROSS_PRODUCT')
    return node._out

def project(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='PROJECT')
    return node._out

def reflect(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='REFLECT')
    return node._out

def refract(vector=None, vector_1=None, ior=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1, 'Scale': ior}, operation='REFRACT')
    return node._out

def faceforward(vector=None, incident=None, reference=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': incident, 'Vector_002': reference}, operation='FACEFORWARD')
    return node._out

def dot(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='DOT_PRODUCT')
    return node._out

def distance(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='DISTANCE')
    return node._out

def length(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='LENGTH')
    return node._out

def scale(vector=None, scale=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Scale': scale}, operation='SCALE')
    return node._out

def normalize(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='NORMALIZE')
    return node._out

def vabs(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='ABSOLUTE')
    return node._out

def vmin(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='MINIMUM')
    return node._out

def vmax(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='MAXIMUM')
    return node._out

def vfloor(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='FLOOR')
    return node._out

def vceil(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='CEIL')
    return node._out

def vfraction(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='FRACTION')
    return node._out

def vmodulo(vector=None, vector_1=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1}, operation='MODULO')
    return node._out

def vwrap(vector=None, max=None, min=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': max, 'Vector_002': min}, operation='WRAP')
    return node._out

def vsnap(vector=None, increment=None):
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
    node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': increment}, operation='SNAP')
    return node._out

def vsin(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='SINE')
    return node._out

def vcos(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='COSINE')
    return node._out

def vtan(vector=None):
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
    node = Node('Vector Math', sockets={'Vector': vector}, operation='TANGENT')
    return node._out

