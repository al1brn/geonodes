import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

""" Function to declare in file __init__.py
from geonodes.sockets.functions import abs, accumulate_field, add, arccos, arcsin, arctan, arctan2, ceil
from geonodes.sockets.functions import color_add, color_burn, color_darken, color_difference, color_divide
from geonodes.sockets.functions import color_dodge, color_hue, color_lighten, color_linear_light, color_mix
from geonodes.sockets.functions import color_mix_color, color_multiply, color_overlay, color_saturation
from geonodes.sockets.functions import color_screen, color_soft_light, color_subtract, color_value, compare
from geonodes.sockets.functions import compare, cos, cosh, cross, degrees, distance, divide, dot, exp
from geonodes.sockets.functions import faceforward, field_at_index, floor, fract, fraction, greater_than
from geonodes.sockets.functions import inverse_sqrt, join_strings, length, less_than, log, max, min, modulo
from geonodes.sockets.functions import multiply, multiply_add, normalize, pingpong, pow, project, radians
from geonodes.sockets.functions import reflect, refract, round, scale, scene, sign, sin, sinh, smooth_max
from geonodes.sockets.functions import smooth_min, snap, sqrt, subtract, tan, tanh, trunc, vector_absolute
from geonodes.sockets.functions import vector_add, vector_ceil, vector_cos, vector_divide, vector_floor
from geonodes.sockets.functions import vector_max, vector_min, vector_modulo, vector_multiply, vector_multiply_add
from geonodes.sockets.functions import vector_sin, vector_snap, vector_subtract, vector_tan, vector_wrap
from geonodes.sockets.functions import wrap
"""

""" Data socket functions

Functions
---------
    abs                       : value        (Float)
    accumulate_field          : Sockets      [leading (data_type dependant), trailing (data_type dependant), total (data_type dependant)]
    add                       : value        (Float)
    arccos                    : value        (Float)
    arcsin                    : value        (Float)
    arctan                    : value        (Float)
    arctan2                   : value        (Float)
    ceil                      : value        (Float)
    color_add                 : color        (Color)
    color_burn                : color        (Color)
    color_darken              : color        (Color)
    color_difference          : color        (Color)
    color_divide              : color        (Color)
    color_dodge               : color        (Color)
    color_hue                 : color        (Color)
    color_lighten             : color        (Color)
    color_linear_light        : color        (Color)
    color_mix                 : color        (Color)
    color_mix_color           : color        (Color)
    color_multiply            : color        (Color)
    color_overlay             : color        (Color)
    color_saturation          : color        (Color)
    color_screen              : color        (Color)
    color_soft_light          : color        (Color)
    color_subtract            : color        (Color)
    color_value               : color        (Color)
    compare                   : result       (Boolean)
    compare                   : value        (Float)
    cos                       : value        (Float)
    cosh                      : value        (Float)
    cross                     : vector       (Vector)
    degrees                   : value        (Float)
    distance                  : value        (Float)
    divide                    : value        (Float)
    dot                       : value        (Float)
    exp                       : value        (Float)
    faceforward               : vector       (Vector)
    field_at_index            : value        (data_type dependant)
    floor                     : value        (Float)
    fract                     : value        (Float)
    fraction                  : vector       (Vector)
    greater_than              : value        (Float)
    inverse_sqrt              : value        (Float)
    join_strings              : string       (String)
    length                    : value        (Float)
    less_than                 : value        (Float)
    log                       : value        (Float)
    max                       : value        (Float)
    min                       : value        (Float)
    modulo                    : value        (Float)
    multiply                  : value        (Float)
    multiply_add              : value        (Float)
    normalize                 : vector       (Vector)
    pingpong                  : value        (Float)
    pow                       : value        (Float)
    project                   : vector       (Vector)
    radians                   : value        (Float)
    reflect                   : vector       (Vector)
    refract                   : vector       (Vector)
    round                     : value        (Float)
    scale                     : vector       (Vector)
    scene                     : Sockets      [seconds (Float), frame (Float)]
    sign                      : value        (Float)
    sin                       : value        (Float)
    sinh                      : value        (Float)
    smooth_max                : value        (Float)
    smooth_min                : value        (Float)
    snap                      : value        (Float)
    sqrt                      : value        (Float)
    subtract                  : value        (Float)
    tan                       : value        (Float)
    tanh                      : value        (Float)
    trunc                     : value        (Float)
    vector_absolute           : vector       (Vector)
    vector_add                : vector       (Vector)
    vector_ceil               : vector       (Vector)
    vector_cos                : vector       (Vector)
    vector_divide             : vector       (Vector)
    vector_floor              : vector       (Vector)
    vector_max                : vector       (Vector)
    vector_min                : vector       (Vector)
    vector_modulo             : vector       (Vector)
    vector_multiply           : vector       (Vector)
    vector_multiply_add       : vector       (Vector)
    vector_sin                : vector       (Vector)
    vector_snap               : vector       (Vector)
    vector_subtract           : vector       (Vector)
    vector_tan                : vector       (Vector)
    vector_wrap               : vector       (Vector)
    wrap                      : value        (Float)
"""

# ----------------------------------------------------------------------------------------------------
# Functions

def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):
    """Call node NodeCompare (FunctionNodeCompare)

    Sockets arguments
    -----------------
        a              : Float
        b              : Float
        epsilon        : Float

    Parameters arguments
    --------------------
        data_type      : 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
        mode           : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
        operation      : 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

    Returns
    -------
        Boolean
    """

    return nodes.NodeCompare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).result

def join_strings(*strings, delimiter=None):
    """Call node NodeJoinStrings (GeometryNodeStringJoin)

    Sockets arguments
    -----------------
        strings        : *String
        delimiter      : String

    Returns
    -------
        String
    """

    return nodes.NodeJoinStrings(*strings, delimiter=delimiter).string

def accumulate_field(value=None, group_index=None, data_type='FLOAT', domain='POINT'):
    """Call node NodeAccumulateField (GeometryNodeAccumulateField)

    Sockets arguments
    -----------------
        value          : Float
        group_index    : Integer

    Parameters arguments
    --------------------
        data_type      : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR]
        domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

    Returns
    -------
        Sockets [leading (data_type dependant), trailing (data_type dependant), total (data_type dependant)]
    """

    return nodes.NodeAccumulateField(value=value, group_index=group_index, data_type=data_type, domain=domain)

def field_at_index(index=None, value=None, data_type='FLOAT', domain='POINT'):
    """Call node NodeFieldAtIndex (GeometryNodeFieldAtIndex)

    Sockets arguments
    -----------------
        index          : Integer
        value          : Float

    Parameters arguments
    --------------------
        data_type      : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
        domain         : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

    Returns
    -------
        data_type dependant
    """

    return nodes.NodeFieldAtIndex(index=index, value=value, data_type=data_type, domain=domain).value

def scene():
    """Call node NodeSceneTime (GeometryNodeInputSceneTime)

    Returns
    -------
        Sockets [seconds (Float), frame (Float)]
    """

    return nodes.NodeSceneTime()

def add(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'ADD'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='ADD').value

def subtract(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'SUBTRACT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='SUBTRACT').value

def multiply(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'MULTIPLY'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='MULTIPLY').value

def divide(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'DIVIDE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='DIVIDE').value

def multiply_add(value0=None, value1=None, value2=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float
        value2         : Float

    Fixed parameters
    ----------------
        operation      : 'MULTIPLY_ADD'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

def pow(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'POWER'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='POWER').value

def log(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'LOGARITHM'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='LOGARITHM').value

def sqrt(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'SQRT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='SQRT').value

def inverse_sqrt(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'INVERSE_SQRT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='INVERSE_SQRT').value

def abs(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'ABSOLUTE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='ABSOLUTE').value

def exp(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'EXPONENT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='EXPONENT').value

def min(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'MINIMUM'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='MINIMUM').value

def max(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'MAXIMUM'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='MAXIMUM').value

def less_than(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'LESS_THAN'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='LESS_THAN').value

def greater_than(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'GREATER_THAN'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='GREATER_THAN').value

def sign(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'SIGN'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='SIGN').value

def compare(value0=None, value1=None, value2=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float
        value2         : Float

    Fixed parameters
    ----------------
        operation      : 'COMPARE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='COMPARE').value

def smooth_min(value0=None, value1=None, value2=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float
        value2         : Float

    Fixed parameters
    ----------------
        operation      : 'SMOOTH_MIN'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN').value

def smooth_max(value0=None, value1=None, value2=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float
        value2         : Float

    Fixed parameters
    ----------------
        operation      : 'SMOOTH_MAX'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX').value

def round(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'ROUND'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='ROUND').value

def floor(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'FLOOR'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='FLOOR').value

def ceil(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'CEIL'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='CEIL').value

def trunc(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'TRUNC'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='TRUNC').value

def fract(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'FRACT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='FRACT').value

def modulo(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'MODULO'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='MODULO').value

def wrap(value0=None, value1=None, value2=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float
        value2         : Float

    Fixed parameters
    ----------------
        operation      : 'WRAP'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, value2=value2, operation='WRAP').value

def snap(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'SNAP'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='SNAP').value

def pingpong(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'PINGPONG'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='PINGPONG').value

def sin(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'SINE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='SINE').value

def cos(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'COSINE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='COSINE').value

def tan(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'TANGENT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='TANGENT').value

def arcsin(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'ARCSINE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='ARCSINE').value

def arccos(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'ARCCOSINE'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='ARCCOSINE').value

def arctan(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'ARCTANGENT'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='ARCTANGENT').value

def arctan2(value0=None, value1=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float
        value1         : Float

    Fixed parameters
    ----------------
        operation      : 'ARCTAN2'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, value1=value1, operation='ARCTAN2').value

def sinh(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'SINH'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='SINH').value

def cosh(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'COSH'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='COSH').value

def tanh(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'TANH'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='TANH').value

def radians(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'RADIANS'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='RADIANS').value

def degrees(value0=None):
    """Call node NodeMath (ShaderNodeMath)

    Sockets arguments
    -----------------
        value0         : Float

    Fixed parameters
    ----------------
        operation      : 'DEGREES'

    Returns
    -------
        Float
    """

    return nodes.NodeMath(value0=value0, operation='DEGREES').value

def vector_add(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'ADD'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='ADD').vector

def vector_subtract(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'SUBTRACT'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT').vector

def vector_multiply(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'MULTIPLY'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY').vector

def vector_divide(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'DIVIDE'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE').vector

def vector_multiply_add(vector0=None, vector1=None, vector2=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector
        vector2        : Vector

    Fixed parameters
    ----------------
        operation      : 'MULTIPLY_ADD'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector

def cross(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'CROSS_PRODUCT'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT').vector

def project(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'PROJECT'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='PROJECT').vector

def reflect(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'REFLECT'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='REFLECT').vector

def refract(vector0=None, vector1=None, scale=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector
        scale          : Float

    Fixed parameters
    ----------------
        operation      : 'REFRACT'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT').vector

def faceforward(vector0=None, vector1=None, vector2=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector
        vector2        : Vector

    Fixed parameters
    ----------------
        operation      : 'FACEFORWARD'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector

def dot(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'DOT_PRODUCT'

    Returns
    -------
        Float
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT').value

def distance(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'DISTANCE'

    Returns
    -------
        Float
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE').value

def length(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'LENGTH'

    Returns
    -------
        Float
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='LENGTH').value

def scale(vector0=None, scale=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        scale          : Float

    Fixed parameters
    ----------------
        operation      : 'SCALE'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, scale=scale, operation='SCALE').vector

def normalize(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'NORMALIZE'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='NORMALIZE').vector

def vector_absolute(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'ABSOLUTE'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='ABSOLUTE').vector

def vector_min(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'MINIMUM'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM').vector

def vector_max(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'MAXIMUM'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM').vector

def vector_floor(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'FLOOR'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='FLOOR').vector

def vector_ceil(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'CEIL'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='CEIL').vector

def fraction(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'FRACTION'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='FRACTION').vector

def vector_modulo(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'MODULO'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='MODULO').vector

def vector_wrap(vector0=None, vector1=None, vector2=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector
        vector2        : Vector

    Fixed parameters
    ----------------
        operation      : 'WRAP'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP').vector

def vector_snap(vector0=None, vector1=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector
        vector1        : Vector

    Fixed parameters
    ----------------
        operation      : 'SNAP'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, vector1=vector1, operation='SNAP').vector

def vector_sin(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'SINE'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='SINE').vector

def vector_cos(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'COSINE'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='COSINE').vector

def vector_tan(vector0=None):
    """Call node NodeVectorMath (ShaderNodeVectorMath)

    Sockets arguments
    -----------------
        vector0        : Vector

    Fixed parameters
    ----------------
        operation      : 'TANGENT'

    Returns
    -------
        Vector
    """

    return nodes.NodeVectorMath(vector0=vector0, operation='TANGENT').vector

def color_mix(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'MIX'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

def color_darken(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'DARKEN'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

def color_multiply(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'MULTIPLY'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

def color_burn(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'BURN'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

def color_lighten(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'LIGHTEN'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

def color_screen(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'SCREEN'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

def color_dodge(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'DODGE'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

def color_add(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'ADD'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

def color_overlay(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'OVERLAY'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

def color_soft_light(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'SOFT_LIGHT'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

def color_linear_light(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'LINEAR_LIGHT'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

def color_difference(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'DIFFERENCE'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

def color_subtract(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'SUBTRACT'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

def color_divide(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'DIVIDE'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

def color_hue(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'HUE'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

def color_saturation(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'SATURATION'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

def color_mix_color(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'COLOR'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

def color_value(color1=None, color2=None, fac=None, use_alpha=False):
    """Call node NodeMix (ShaderNodeMixRGB)

    Sockets arguments
    -----------------
        color1         : Color
        color2         : Color
        fac            : Float

    Parameters arguments
    --------------------
        use_alpha      : False

    Fixed parameters
    ----------------
        blend_type     : 'VALUE'

    Returns
    -------
        Color
    """

    return nodes.NodeMix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color


