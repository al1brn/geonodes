import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

""" Function to declare in file __init__.py
from geonodes.sockets.functions import abs, add, arccos, arcsin, arctan, arctan2, ceil, color_add, color_burn
from geonodes.sockets.functions import color_darken, color_difference, color_divide, color_dodge, color_hue
from geonodes.sockets.functions import color_lighten, color_linear_light, color_mix, color_mix_color, color_multiply
from geonodes.sockets.functions import color_overlay, color_saturation, color_screen, color_soft_light
from geonodes.sockets.functions import color_subtract, color_value, compare, compare, cos, cosh, cross
from geonodes.sockets.functions import degrees, distance, divide, dot, exp, faceforward, floor, fract
from geonodes.sockets.functions import fraction, greater_than, inverse_sqrt, join_strings, length, less_than
from geonodes.sockets.functions import log, max, min, modulo, multiply, multiply_add, normalize, pingpong
from geonodes.sockets.functions import pow, project, radians, reflect, refract, round, scale, scene, sign
from geonodes.sockets.functions import sin, sinh, smooth_max, smooth_min, snap, sqrt, subtract, tan, tanh
from geonodes.sockets.functions import trunc, vector_absolute, vector_add, vector_ceil, vector_cos, vector_divide
from geonodes.sockets.functions import vector_floor, vector_max, vector_min, vector_modulo, vector_multiply
from geonodes.sockets.functions import vector_multiply_add, vector_sin, vector_snap, vector_subtract, vector_tan
from geonodes.sockets.functions import vector_wrap, wrap
"""

""" Class functions




Functions
=========
- abs                 : value (Float) 
- add                 : value (Float) 
- arccos              : value (Float) 
- arcsin              : value (Float) 
- arctan              : value (Float) 
- arctan2             : value (Float) 
- ceil                : value (Float) 
- color_add           : color (Color) 
- color_burn          : color (Color) 
- color_darken        : color (Color) 
- color_difference    : color (Color) 
- color_divide        : color (Color) 
- color_dodge         : color (Color) 
- color_hue           : color (Color) 
- color_lighten       : color (Color) 
- color_linear_light  : color (Color) 
- color_mix           : color (Color) 
- color_mix_color     : color (Color) 
- color_multiply      : color (Color) 
- color_overlay       : color (Color) 
- color_saturation    : color (Color) 
- color_screen        : color (Color) 
- color_soft_light    : color (Color) 
- color_subtract      : color (Color) 
- color_value         : color (Color) 
- compare             : result (Boolean) 
- compare             : value (Float) 
- cos                 : value (Float) 
- cosh                : value (Float) 
- cross               : vector (Vector) 
- degrees             : value (Float) 
- distance            : value (Float) 
- divide              : value (Float) 
- dot                 : value (Float) 
- exp                 : value (Float) 
- faceforward         : vector (Vector) 
- floor               : value (Float) 
- fract               : value (Float) 
- fraction            : vector (Vector) 
- greater_than        : value (Float) 
- inverse_sqrt        : value (Float) 
- join_strings        : string (String) 
- length              : value (Float) 
- less_than           : value (Float) 
- log                 : value (Float) 
- max                 : value (Float) 
- min                 : value (Float) 
- modulo              : value (Float) 
- multiply            : value (Float) 
- multiply_add        : value (Float) 
- normalize           : vector (Vector) 
- pingpong            : value (Float) 
- pow                 : value (Float) 
- project             : vector (Vector) 
- radians             : value (Float) 
- reflect             : vector (Vector) 
- refract             : vector (Vector) 
- round               : value (Float) 
- scale               : vector (Vector) 
- scene               : Sockets      [seconds (Float), frame (Float)] 
- sign                : value (Float) 
- sin                 : value (Float) 
- sinh                : value (Float) 
- smooth_max          : value (Float) 
- smooth_min          : value (Float) 
- snap                : value (Float) 
- sqrt                : value (Float) 
- subtract            : value (Float) 
- tan                 : value (Float) 
- tanh                : value (Float) 
- trunc               : value (Float) 
- vector_absolute     : vector (Vector) 
- vector_add          : vector (Vector) 
- vector_ceil         : vector (Vector) 
- vector_cos          : vector (Vector) 
- vector_divide       : vector (Vector) 
- vector_floor        : vector (Vector) 
- vector_max          : vector (Vector) 
- vector_min          : vector (Vector) 
- vector_modulo       : vector (Vector) 
- vector_multiply     : vector (Vector) 
- vector_multiply_add : vector (Vector) 
- vector_sin          : vector (Vector) 
- vector_snap         : vector (Vector) 
- vector_subtract     : vector (Vector) 
- vector_tan          : vector (Vector) 
- vector_wrap         : vector (Vector) 
- wrap                : value (Float) 
"""


# ----------------------------------------------------------------------------------------------------
# Functions

def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):
    """ compare
    

    | Node: Compare 
    

        v = functions.compare(a, b, epsilon, data_type, mode, operation) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - a       : Float 
        - b       : Float 
        - epsilon : Float 
    

        Parameters arguments
        --------------------
        - data_type : 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA] 
        - mode      : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION] 
        - operation : 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL] 
    

    Node creation
    =============
    

        node = nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation) 
    

    Returns
    =======
            Boolean 
    """

    return nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).result

def join_strings(*strings, delimiter=None):
    """ join_strings
    

    | Node: JoinStrings 
    

        v = functions.join_strings(strings_1, strings_2, strings_3, delimiter) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - strings   : *String 
        - delimiter : String 
    

    Node creation
    =============
    

        node = nodes.JoinStrings(*strings, delimiter=delimiter) 
    

    Returns
    =======
            String 
    """

    return nodes.JoinStrings(*strings, delimiter=delimiter).string

def scene():
    """ scene
    

    | Node: SceneTime 
    

        v = functions.scene() 
    

    Arguments
    =========
    

    Node creation
    =============
    

        node = nodes.SceneTime() 
    

    Returns
    =======
            Sockets [seconds (Float), frame (Float)] 
    """

    return nodes.SceneTime()

def add(value0=None, value1=None):
    """ add
    

    | Node: Math 
    

        v = functions.add(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ADD' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='ADD') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='ADD').value

def subtract(value0=None, value1=None):
    """ subtract
    

    | Node: Math 
    

        v = functions.subtract(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SUBTRACT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='SUBTRACT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='SUBTRACT').value

def multiply(value0=None, value1=None):
    """ multiply
    

    | Node: Math 
    

        v = functions.multiply(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'MULTIPLY' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='MULTIPLY') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='MULTIPLY').value

def divide(value0=None, value1=None):
    """ divide
    

    | Node: Math 
    

        v = functions.divide(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'DIVIDE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='DIVIDE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='DIVIDE').value

def multiply_add(value0=None, value1=None, value2=None):
    """ multiply_add
    

    | Node: Math 
    

        v = functions.multiply_add(value0, value1, value2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
        - value2 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'MULTIPLY_ADD' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

def pow(value0=None, value1=None):
    """ pow
    

    | Node: Math 
    

        v = functions.pow(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'POWER' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='POWER') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='POWER').value

def log(value0=None, value1=None):
    """ log
    

    | Node: Math 
    

        v = functions.log(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'LOGARITHM' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='LOGARITHM') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='LOGARITHM').value

def sqrt(value0=None):
    """ sqrt
    

    | Node: Math 
    

        v = functions.sqrt(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SQRT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='SQRT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='SQRT').value

def inverse_sqrt(value0=None):
    """ inverse_sqrt
    

    | Node: Math 
    

        v = functions.inverse_sqrt(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'INVERSE_SQRT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='INVERSE_SQRT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='INVERSE_SQRT').value

def abs(value0=None):
    """ abs
    

    | Node: Math 
    

        v = functions.abs(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ABSOLUTE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='ABSOLUTE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='ABSOLUTE').value

def exp(value0=None):
    """ exp
    

    | Node: Math 
    

        v = functions.exp(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'EXPONENT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='EXPONENT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='EXPONENT').value

def min(value0=None, value1=None):
    """ min
    

    | Node: Math 
    

        v = functions.min(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'MINIMUM' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='MINIMUM') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='MINIMUM').value

def max(value0=None, value1=None):
    """ max
    

    | Node: Math 
    

        v = functions.max(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'MAXIMUM' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='MAXIMUM') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='MAXIMUM').value

def less_than(value0=None, value1=None):
    """ less_than
    

    | Node: Math 
    

        v = functions.less_than(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'LESS_THAN' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='LESS_THAN') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='LESS_THAN').value

def greater_than(value0=None, value1=None):
    """ greater_than
    

    | Node: Math 
    

        v = functions.greater_than(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'GREATER_THAN' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN').value

def sign(value0=None):
    """ sign
    

    | Node: Math 
    

        v = functions.sign(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SIGN' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='SIGN') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='SIGN').value

def compare(value0=None, value1=None, value2=None):
    """ compare
    

    | Node: Math 
    

        v = functions.compare(value0, value1, value2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
        - value2 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'COMPARE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE').value

def smooth_min(value0=None, value1=None, value2=None):
    """ smooth_min
    

    | Node: Math 
    

        v = functions.smooth_min(value0, value1, value2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
        - value2 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SMOOTH_MIN' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN').value

def smooth_max(value0=None, value1=None, value2=None):
    """ smooth_max
    

    | Node: Math 
    

        v = functions.smooth_max(value0, value1, value2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
        - value2 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SMOOTH_MAX' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX').value

def round(value0=None):
    """ round
    

    | Node: Math 
    

        v = functions.round(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ROUND' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='ROUND') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='ROUND').value

def floor(value0=None):
    """ floor
    

    | Node: Math 
    

        v = functions.floor(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'FLOOR' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='FLOOR') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='FLOOR').value

def ceil(value0=None):
    """ ceil
    

    | Node: Math 
    

        v = functions.ceil(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'CEIL' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='CEIL') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='CEIL').value

def trunc(value0=None):
    """ trunc
    

    | Node: Math 
    

        v = functions.trunc(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'TRUNC' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='TRUNC') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='TRUNC').value

def fract(value0=None):
    """ fract
    

    | Node: Math 
    

        v = functions.fract(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'FRACT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='FRACT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='FRACT').value

def modulo(value0=None, value1=None):
    """ modulo
    

    | Node: Math 
    

        v = functions.modulo(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'MODULO' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='MODULO') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='MODULO').value

def wrap(value0=None, value1=None, value2=None):
    """ wrap
    

    | Node: Math 
    

        v = functions.wrap(value0, value1, value2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
        - value2 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'WRAP' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP').value

def snap(value0=None, value1=None):
    """ snap
    

    | Node: Math 
    

        v = functions.snap(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SNAP' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='SNAP') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='SNAP').value

def pingpong(value0=None, value1=None):
    """ pingpong
    

    | Node: Math 
    

        v = functions.pingpong(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'PINGPONG' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='PINGPONG') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='PINGPONG').value

def sin(value0=None):
    """ sin
    

    | Node: Math 
    

        v = functions.sin(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SINE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='SINE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='SINE').value

def cos(value0=None):
    """ cos
    

    | Node: Math 
    

        v = functions.cos(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'COSINE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='COSINE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='COSINE').value

def tan(value0=None):
    """ tan
    

    | Node: Math 
    

        v = functions.tan(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'TANGENT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='TANGENT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='TANGENT').value

def arcsin(value0=None):
    """ arcsin
    

    | Node: Math 
    

        v = functions.arcsin(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ARCSINE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='ARCSINE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='ARCSINE').value

def arccos(value0=None):
    """ arccos
    

    | Node: Math 
    

        v = functions.arccos(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ARCCOSINE' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='ARCCOSINE') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='ARCCOSINE').value

def arctan(value0=None):
    """ arctan
    

    | Node: Math 
    

        v = functions.arctan(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ARCTANGENT' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='ARCTANGENT') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='ARCTANGENT').value

def arctan2(value0=None, value1=None):
    """ arctan2
    

    | Node: Math 
    

        v = functions.arctan2(value0, value1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
        - value1 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'ARCTAN2' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, value1=value1, operation='ARCTAN2') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, value1=value1, operation='ARCTAN2').value

def sinh(value0=None):
    """ sinh
    

    | Node: Math 
    

        v = functions.sinh(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SINH' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='SINH') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='SINH').value

def cosh(value0=None):
    """ cosh
    

    | Node: Math 
    

        v = functions.cosh(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'COSH' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='COSH') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='COSH').value

def tanh(value0=None):
    """ tanh
    

    | Node: Math 
    

        v = functions.tanh(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'TANH' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='TANH') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='TANH').value

def radians(value0=None):
    """ radians
    

    | Node: Math 
    

        v = functions.radians(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'RADIANS' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='RADIANS') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='RADIANS').value

def degrees(value0=None):
    """ degrees
    

    | Node: Math 
    

        v = functions.degrees(value0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - value0 : Float 
    

        Fixed parameters
        ----------------
        - operation : 'DEGREES' 
    

    Node creation
    =============
    

        node = nodes.Math(value0=value0, operation='DEGREES') 
    

    Returns
    =======
            Float 
    """

    return nodes.Math(value0=value0, operation='DEGREES').value

def vector_add(vector0=None, vector1=None):
    """ vector_add
    

    | Node: VectorMath 
    

        v = functions.vector_add(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'ADD' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD').vector

def vector_subtract(vector0=None, vector1=None):
    """ vector_subtract
    

    | Node: VectorMath 
    

        v = functions.vector_subtract(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'SUBTRACT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT').vector

def vector_multiply(vector0=None, vector1=None):
    """ vector_multiply
    

    | Node: VectorMath 
    

        v = functions.vector_multiply(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'MULTIPLY' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY').vector

def vector_divide(vector0=None, vector1=None):
    """ vector_divide
    

    | Node: VectorMath 
    

        v = functions.vector_divide(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'DIVIDE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE').vector

def vector_multiply_add(vector0=None, vector1=None, vector2=None):
    """ vector_multiply_add
    

    | Node: VectorMath 
    

        v = functions.vector_multiply_add(vector0, vector1, vector2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
        - vector2 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'MULTIPLY_ADD' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector

def cross(vector0=None, vector1=None):
    """ cross
    

    | Node: VectorMath 
    

        v = functions.cross(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'CROSS_PRODUCT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT').vector

def project(vector0=None, vector1=None):
    """ project
    

    | Node: VectorMath 
    

        v = functions.project(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'PROJECT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT').vector

def reflect(vector0=None, vector1=None):
    """ reflect
    

    | Node: VectorMath 
    

        v = functions.reflect(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'REFLECT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT').vector

def refract(vector0=None, vector1=None, scale=None):
    """ refract
    

    | Node: VectorMath 
    

        v = functions.refract(vector0, vector1, scale) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
        - scale   : Float 
    

        Fixed parameters
        ----------------
        - operation : 'REFRACT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT').vector

def faceforward(vector0=None, vector1=None, vector2=None):
    """ faceforward
    

    | Node: VectorMath 
    

        v = functions.faceforward(vector0, vector1, vector2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
        - vector2 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'FACEFORWARD' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector

def dot(vector0=None, vector1=None):
    """ dot
    

    | Node: VectorMath 
    

        v = functions.dot(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'DOT_PRODUCT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT') 
    

    Returns
    =======
            Float 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT').value

def distance(vector0=None, vector1=None):
    """ distance
    

    | Node: VectorMath 
    

        v = functions.distance(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'DISTANCE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE') 
    

    Returns
    =======
            Float 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE').value

def length(vector0=None):
    """ length
    

    | Node: VectorMath 
    

        v = functions.length(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'LENGTH' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='LENGTH') 
    

    Returns
    =======
            Float 
    """

    return nodes.VectorMath(vector0=vector0, operation='LENGTH').value

def scale(vector0=None, scale=None):
    """ scale
    

    | Node: VectorMath 
    

        v = functions.scale(vector0, scale) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - scale   : Float 
    

        Fixed parameters
        ----------------
        - operation : 'SCALE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE').vector

def normalize(vector0=None):
    """ normalize
    

    | Node: VectorMath 
    

        v = functions.normalize(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'NORMALIZE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='NORMALIZE') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='NORMALIZE').vector

def vector_absolute(vector0=None):
    """ vector_absolute
    

    | Node: VectorMath 
    

        v = functions.vector_absolute(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'ABSOLUTE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='ABSOLUTE') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='ABSOLUTE').vector

def vector_min(vector0=None, vector1=None):
    """ vector_min
    

    | Node: VectorMath 
    

        v = functions.vector_min(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'MINIMUM' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM').vector

def vector_max(vector0=None, vector1=None):
    """ vector_max
    

    | Node: VectorMath 
    

        v = functions.vector_max(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'MAXIMUM' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM').vector

def vector_floor(vector0=None):
    """ vector_floor
    

    | Node: VectorMath 
    

        v = functions.vector_floor(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'FLOOR' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='FLOOR') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='FLOOR').vector

def vector_ceil(vector0=None):
    """ vector_ceil
    

    | Node: VectorMath 
    

        v = functions.vector_ceil(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'CEIL' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='CEIL') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='CEIL').vector

def fraction(vector0=None):
    """ fraction
    

    | Node: VectorMath 
    

        v = functions.fraction(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'FRACTION' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='FRACTION') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='FRACTION').vector

def vector_modulo(vector0=None, vector1=None):
    """ vector_modulo
    

    | Node: VectorMath 
    

        v = functions.vector_modulo(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'MODULO' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO').vector

def vector_wrap(vector0=None, vector1=None, vector2=None):
    """ vector_wrap
    

    | Node: VectorMath 
    

        v = functions.vector_wrap(vector0, vector1, vector2) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
        - vector2 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'WRAP' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP').vector

def vector_snap(vector0=None, vector1=None):
    """ vector_snap
    

    | Node: VectorMath 
    

        v = functions.vector_snap(vector0, vector1) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
        - vector1 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'SNAP' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP').vector

def vector_sin(vector0=None):
    """ vector_sin
    

    | Node: VectorMath 
    

        v = functions.vector_sin(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'SINE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='SINE') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='SINE').vector

def vector_cos(vector0=None):
    """ vector_cos
    

    | Node: VectorMath 
    

        v = functions.vector_cos(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'COSINE' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='COSINE') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='COSINE').vector

def vector_tan(vector0=None):
    """ vector_tan
    

    | Node: VectorMath 
    

        v = functions.vector_tan(vector0) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - vector0 : Vector 
    

        Fixed parameters
        ----------------
        - operation : 'TANGENT' 
    

    Node creation
    =============
    

        node = nodes.VectorMath(vector0=vector0, operation='TANGENT') 
    

    Returns
    =======
            Vector 
    """

    return nodes.VectorMath(vector0=vector0, operation='TANGENT').vector

def color_mix(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_mix
    

    | Node: Mix 
    

        v = functions.color_mix(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'MIX' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

def color_darken(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_darken
    

    | Node: Mix 
    

        v = functions.color_darken(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'DARKEN' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

def color_multiply(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_multiply
    

    | Node: Mix 
    

        v = functions.color_multiply(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'MULTIPLY' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

def color_burn(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_burn
    

    | Node: Mix 
    

        v = functions.color_burn(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'BURN' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

def color_lighten(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_lighten
    

    | Node: Mix 
    

        v = functions.color_lighten(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'LIGHTEN' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

def color_screen(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_screen
    

    | Node: Mix 
    

        v = functions.color_screen(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'SCREEN' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

def color_dodge(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_dodge
    

    | Node: Mix 
    

        v = functions.color_dodge(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'DODGE' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

def color_add(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_add
    

    | Node: Mix 
    

        v = functions.color_add(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'ADD' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

def color_overlay(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_overlay
    

    | Node: Mix 
    

        v = functions.color_overlay(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'OVERLAY' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

def color_soft_light(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_soft_light
    

    | Node: Mix 
    

        v = functions.color_soft_light(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'SOFT_LIGHT' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha)
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

def color_linear_light(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_linear_light
    

    | Node: Mix 
    

        v = functions.color_linear_light(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'LINEAR_LIGHT' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

def color_difference(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_difference
    

    | Node: Mix 
    

        v = functions.color_difference(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'DIFFERENCE' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha)
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

def color_subtract(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_subtract
    

    | Node: Mix 
    

        v = functions.color_subtract(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'SUBTRACT' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

def color_divide(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_divide
    

    | Node: Mix 
    

        v = functions.color_divide(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'DIVIDE' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

def color_hue(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_hue
    

    | Node: Mix 
    

        v = functions.color_hue(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'HUE' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

def color_saturation(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_saturation
    

    | Node: Mix 
    

        v = functions.color_saturation(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'SATURATION' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha)
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

def color_mix_color(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_mix_color
    

    | Node: Mix 
    

        v = functions.color_mix_color(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'COLOR' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

def color_value(color1=None, color2=None, fac=None, use_alpha=False):
    """ color_value
    

    | Node: Mix 
    

        v = functions.color_value(color1, color2, fac, use_alpha) 
    

    Arguments
    =========
    

        Sockets arguments
        -----------------
        - color1 : Color 
        - color2 : Color 
        - fac    : Float 
    

        Fixed parameters
        ----------------
        - blend_type : 'VALUE' 
    

        Parameters arguments
        --------------------
        - use_alpha : False 
    

    Node creation
    =============
    

        node = nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha) 
    

    Returns
    =======
            Color 
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color


