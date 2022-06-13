#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-13
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

""" Function to declare in file __init__.py
from geonodes.sockets.functions import abs, add, arccos, arcsin, arctan, arctan2, b_and, b_not, b_or, ceil
from geonodes.sockets.functions import color_add, color_burn, color_darken, color_difference, color_divide
from geonodes.sockets.functions import color_dodge, color_hue, color_lighten, color_linear_light, color_mix
from geonodes.sockets.functions import color_mix_color, color_multiply, color_overlay, color_saturation
from geonodes.sockets.functions import color_screen, color_soft_light, color_subtract, color_value, compare
from geonodes.sockets.functions import compare, cos, cosh, cross, degrees, distance, divide, dot, exp
from geonodes.sockets.functions import faceforward, floor, fract, fraction, greater_than, imply, inverse_sqrt
from geonodes.sockets.functions import join_strings, length, less_than, log, max, min, modulo, multiply
from geonodes.sockets.functions import multiply_add, nand, nimply, nor, normalize, pingpong, pow, project
from geonodes.sockets.functions import radians, reflect, refract, round, scale, scene, sign, sin, sinh
from geonodes.sockets.functions import smooth_max, smooth_min, snap, sqrt, subtract, tan, tanh, trunc
from geonodes.sockets.functions import vector_absolute, vector_add, vector_ceil, vector_cos, vector_divide
from geonodes.sockets.functions import vector_floor, vector_max, vector_min, vector_modulo, vector_multiply
from geonodes.sockets.functions import vector_multiply_add, vector_sin, vector_snap, vector_subtract, vector_tan
from geonodes.sockets.functions import vector_wrap, wrap, xnor, xor
"""

""" 

geonodes functions
------------------
    > global functions
      
    <sub>go to index</sub>
    
    Example of use:
                
    ```python
    import geonodes as gn
    value = gn.Float(14.) # A float value
    v = gn.sin(v)         # The sine of this value
    ```
    
    


    Functions
    ---------
        - abs : value (Float)
        - add : value (Float)
        - arccos : value (Float)
        - arcsin : value (Float)
        - arctan : value (Float)
        - arctan2 : value (Float)
        - b_and : boolean (Boolean)
        - b_not : boolean (Boolean)
        - b_or : boolean (Boolean)
        - ceil : value (Float)
        - color_add : color (Color)
        - color_burn : color (Color)
        - color_darken : color (Color)
        - color_difference : color (Color)
        - color_divide : color (Color)
        - color_dodge : color (Color)
        - color_hue : color (Color)
        - color_lighten : color (Color)
        - color_linear_light : color (Color)
        - color_mix : color (Color)
        - color_mix_color : color (Color)
        - color_multiply : color (Color)
        - color_overlay : color (Color)
        - color_saturation : color (Color)
        - color_screen : color (Color)
        - color_soft_light : color (Color)
        - color_subtract : color (Color)
        - color_value : color (Color)
        - compare : result (Boolean)
        - compare : value (Float)
        - cos : value (Float)
        - cosh : value (Float)
        - cross : vector (Vector)
        - degrees : value (Float)
        - distance : value (Float)
        - divide : value (Float)
        - dot : value (Float)
        - exp : value (Float)
        - faceforward : vector (Vector)
        - floor : value (Float)
        - fract : value (Float)
        - fraction : vector (Vector)
        - greater_than : value (Float)
        - imply : boolean (Boolean)
        - inverse_sqrt : value (Float)
        - join_strings : string (String)
        - length : value (Float)
        - less_than : value (Float)
        - log : value (Float)
        - max : value (Float)
        - min : value (Float)
        - modulo : value (Float)
        - multiply : value (Float)
        - multiply_add : value (Float)
        - nand : boolean (Boolean)
        - nimply : boolean (Boolean)
        - nor : boolean (Boolean)
        - normalize : vector (Vector)
        - pingpong : value (Float)
        - pow : value (Float)
        - project : vector (Vector)
        - radians : value (Float)
        - reflect : vector (Vector)
        - refract : vector (Vector)
        - round : value (Float)
        - scale : vector (Vector)
        - scene : Sockets      [seconds (Float), frame (Float)]
        - sign : value (Float)
        - sin : value (Float)
        - sinh : value (Float)
        - smooth_max : value (Float)
        - smooth_min : value (Float)
        - snap : value (Float)
        - sqrt : value (Float)
        - subtract : value (Float)
        - tan : value (Float)
        - tanh : value (Float)
        - trunc : value (Float)
        - vector_absolute : vector (Vector)
        - vector_add : vector (Vector)
        - vector_ceil : vector (Vector)
        - vector_cos : vector (Vector)
        - vector_divide : vector (Vector)
        - vector_floor : vector (Vector)
        - vector_max : vector (Vector)
        - vector_min : vector (Vector)
        - vector_modulo : vector (Vector)
        - vector_multiply : vector (Vector)
        - vector_multiply_add : vector (Vector)
        - vector_sin : vector (Vector)
        - vector_snap : vector (Vector)
        - vector_subtract : vector (Vector)
        - vector_tan : vector (Vector)
        - vector_wrap : vector (Vector)
        - wrap : value (Float)
        - xnor : boolean (Boolean)
        - xor : boolean (Boolean)
"""


# ----------------------------------------------------------------------------------------------------
# Functions

def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):
    """ > Node: Compare
      
    <sub>go to: top index
    blender ref FunctionNodeCompare
    node ref Compare </sub>
                              
    ```python
    v = functions.compare(a, b, epsilon, data_type, mode, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - a : Float
        - b : Float
        - epsilon : Float## Parameters
        - data_type : 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
        - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
        - operation : 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation).result

def join_strings(*strings, delimiter=None):
    """ > Node: JoinStrings
      
    <sub>go to: top index
    blender ref GeometryNodeStringJoin
    node ref Join Strings </sub>
                              
    ```python
    v = functions.join_strings(strings_1, strings_2, strings_3, delimiter)
    ```


    Arguments
    ---------
        ## Sockets
        - strings : *String
        - delimiter : String


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.JoinStrings(*strings, delimiter=delimiter)
        ```


    Returns
    -------
        String
        
    """

    return nodes.JoinStrings(*strings, delimiter=delimiter).string

def scene():
    """ > Node: SceneTime
      
    <sub>go to: top index
    blender ref GeometryNodeInputSceneTime
    node ref Scene Time </sub>
                              
    ```python
    v = functions.scene()
    ```


    Arguments
    ---------


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.SceneTime()
        ```


    Returns
    -------
        Sockets [seconds (Float), frame (Float)]
        
    """

    return nodes.SceneTime()

def b_and(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.b_and(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def b_or(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.b_or(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def b_not(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.b_not(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def nand(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.nand(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def nor(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.nor(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def xnor(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.xnor(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def xor(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.xor(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def imply(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.imply(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def nimply(boolean0=None, boolean1=None, operation='AND'):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.nimply(boolean0, boolean1, operation)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation).boolean

def add(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.add(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='ADD')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='ADD').value

def subtract(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.subtract(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'SUBTRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='SUBTRACT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='SUBTRACT').value

def multiply(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.multiply(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'MULTIPLY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MULTIPLY')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MULTIPLY').value

def divide(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.divide(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'DIVIDE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='DIVIDE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='DIVIDE').value

def multiply_add(value0=None, value1=None, value2=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.multiply_add(value0, value1, value2)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Fixed parameters
        - operation : 'MULTIPLY_ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD').value

def pow(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.pow(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'POWER'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='POWER')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='POWER').value

def log(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.log(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'LOGARITHM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='LOGARITHM')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='LOGARITHM').value

def sqrt(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sqrt(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'SQRT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SQRT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SQRT').value

def inverse_sqrt(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.inverse_sqrt(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'INVERSE_SQRT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='INVERSE_SQRT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='INVERSE_SQRT').value

def abs(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.abs(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'ABSOLUTE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ABSOLUTE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ABSOLUTE').value

def exp(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.exp(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'EXPONENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='EXPONENT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='EXPONENT').value

def min(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.min(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'MINIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MINIMUM')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MINIMUM').value

def max(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.max(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'MAXIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MAXIMUM')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MAXIMUM').value

def less_than(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.less_than(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'LESS_THAN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='LESS_THAN')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='LESS_THAN').value

def greater_than(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.greater_than(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'GREATER_THAN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN').value

def sign(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sign(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'SIGN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SIGN')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SIGN').value

def compare(value0=None, value1=None, value2=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.compare(value0, value1, value2)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Fixed parameters
        - operation : 'COMPARE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE').value

def smooth_min(value0=None, value1=None, value2=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.smooth_min(value0, value1, value2)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Fixed parameters
        - operation : 'SMOOTH_MIN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN').value

def smooth_max(value0=None, value1=None, value2=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.smooth_max(value0, value1, value2)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Fixed parameters
        - operation : 'SMOOTH_MAX'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX').value

def round(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.round(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'ROUND'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ROUND')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ROUND').value

def floor(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.floor(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'FLOOR'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='FLOOR')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='FLOOR').value

def ceil(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.ceil(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'CEIL'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='CEIL')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='CEIL').value

def trunc(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.trunc(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'TRUNC'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='TRUNC')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='TRUNC').value

def fract(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.fract(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'FRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='FRACT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='FRACT').value

def modulo(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.modulo(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'MODULO'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MODULO')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MODULO').value

def wrap(value0=None, value1=None, value2=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.wrap(value0, value1, value2)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Fixed parameters
        - operation : 'WRAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP').value

def snap(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.snap(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'SNAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='SNAP')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='SNAP').value

def pingpong(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.pingpong(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'PINGPONG'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='PINGPONG')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='PINGPONG').value

def sin(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sin(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'SINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SINE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SINE').value

def cos(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.cos(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'COSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='COSINE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='COSINE').value

def tan(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.tan(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'TANGENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='TANGENT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='TANGENT').value

def arcsin(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arcsin(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'ARCSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ARCSINE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ARCSINE').value

def arccos(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arccos(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'ARCCOSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ARCCOSINE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ARCCOSINE').value

def arctan(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arctan(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'ARCTANGENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ARCTANGENT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ARCTANGENT').value

def arctan2(value0=None, value1=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arctan2(value0, value1)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Fixed parameters
        - operation : 'ARCTAN2'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='ARCTAN2')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='ARCTAN2').value

def sinh(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sinh(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'SINH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SINH')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SINH').value

def cosh(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.cosh(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'COSH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='COSH')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='COSH').value

def tanh(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.tanh(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'TANH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='TANH')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='TANH').value

def radians(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.radians(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'RADIANS'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='RADIANS')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='RADIANS').value

def degrees(value0=None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.degrees(value0)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Fixed parameters
        - operation : 'DEGREES'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='DEGREES')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='DEGREES').value

def vector_add(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_add(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD').vector

def vector_subtract(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_subtract(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'SUBTRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT').vector

def vector_multiply(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_multiply(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'MULTIPLY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY').vector

def vector_divide(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_divide(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'DIVIDE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE').vector

def vector_multiply_add(vector0=None, vector1=None, vector2=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_multiply_add(vector0, vector1, vector2)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - vector2 : Vector## Fixed parameters
        - operation : 'MULTIPLY_ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD').vector

def cross(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.cross(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'CROSS_PRODUCT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT').vector

def project(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.project(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'PROJECT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT').vector

def reflect(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.reflect(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'REFLECT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT').vector

def refract(vector0=None, vector1=None, scale=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.refract(vector0, vector1, scale)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - scale : Float## Fixed parameters
        - operation : 'REFRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT').vector

def faceforward(vector0=None, vector1=None, vector2=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.faceforward(vector0, vector1, vector2)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - vector2 : Vector## Fixed parameters
        - operation : 'FACEFORWARD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD').vector

def dot(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.dot(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'DOT_PRODUCT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT').value

def distance(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.distance(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'DISTANCE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE').value

def length(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.length(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'LENGTH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='LENGTH')
        ```


    Returns
    -------
        Float
        
    """

    return nodes.VectorMath(vector0=vector0, operation='LENGTH').value

def scale(vector0=None, scale=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.scale(vector0, scale)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - scale : Float## Fixed parameters
        - operation : 'SCALE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE').vector

def normalize(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.normalize(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'NORMALIZE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='NORMALIZE')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='NORMALIZE').vector

def vector_absolute(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_absolute(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'ABSOLUTE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='ABSOLUTE')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='ABSOLUTE').vector

def vector_min(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_min(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'MINIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM').vector

def vector_max(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_max(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'MAXIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM').vector

def vector_floor(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_floor(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'FLOOR'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='FLOOR')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='FLOOR').vector

def vector_ceil(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_ceil(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'CEIL'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='CEIL')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='CEIL').vector

def fraction(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.fraction(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'FRACTION'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='FRACTION')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='FRACTION').vector

def vector_modulo(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_modulo(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'MODULO'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO').vector

def vector_wrap(vector0=None, vector1=None, vector2=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_wrap(vector0, vector1, vector2)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - vector2 : Vector## Fixed parameters
        - operation : 'WRAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP').vector

def vector_snap(vector0=None, vector1=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_snap(vector0, vector1)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Fixed parameters
        - operation : 'SNAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP').vector

def vector_sin(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_sin(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'SINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='SINE')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='SINE').vector

def vector_cos(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_cos(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'COSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='COSINE')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='COSINE').vector

def vector_tan(vector0=None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_tan(vector0)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Fixed parameters
        - operation : 'TANGENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='TANGENT')
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='TANGENT').vector

def color_mix(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_mix(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'MIX'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha).color

def color_darken(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_darken(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'DARKEN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha).color

def color_multiply(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_multiply(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'MULTIPLY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha).color

def color_burn(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_burn(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'BURN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha).color

def color_lighten(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_lighten(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'LIGHTEN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha).color

def color_screen(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_screen(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'SCREEN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha).color

def color_dodge(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_dodge(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'DODGE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha).color

def color_add(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_add(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha).color

def color_overlay(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_overlay(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'OVERLAY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha).color

def color_soft_light(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_soft_light(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'SOFT_LIGHT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha).color

def color_linear_light(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_linear_light(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'LINEAR_LIGHT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha).color

def color_difference(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_difference(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'DIFFERENCE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha).color

def color_subtract(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_subtract(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'SUBTRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha).color

def color_divide(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_divide(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'DIVIDE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha).color

def color_hue(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_hue(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'HUE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha).color

def color_saturation(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_saturation(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'SATURATION'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha).color

def color_mix_color(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_mix_color(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'COLOR'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha).color

def color_value(color1=None, color2=None, fac=None, use_alpha=False):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_value(color1, color2, fac, use_alpha)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False## Fixed parameters
        - blend_type : 'VALUE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha).color


