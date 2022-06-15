#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-15
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
from geonodes.core.domains import Domain
from geonodes import Point, Edge, Face, Corner, Curve

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

def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label = None, node_color = None):
    """ > Node: Compare
      
    <sub>go to: top index
    blender ref FunctionNodeCompare
    node ref Compare </sub>
                              
    ```python
    v = functions.compare(a, b, epsilon, data_type, mode, operation, node_label = None, node_color = None)
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
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation, label=node_label, node_color=node_color).result

def join_strings(*strings, delimiter=None, node_label = None, node_color = None):
    """ > Node: JoinStrings
      
    <sub>go to: top index
    blender ref GeometryNodeStringJoin
    node ref Join Strings </sub>
                              
    ```python
    v = functions.join_strings(strings_1, strings_2, strings_3, delimiter, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - strings : *String
        - delimiter : String## Parameters
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.JoinStrings(*strings, delimiter=delimiter, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        String
        
    """

    return nodes.JoinStrings(*strings, delimiter=delimiter, label=node_label, node_color=node_color).string

def scene(node_label = None, node_color = None):
    """ > Node: SceneTime
      
    <sub>go to: top index
    blender ref GeometryNodeInputSceneTime
    node ref Scene Time </sub>
                              
    ```python
    v = functions.scene(node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Parameters
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.SceneTime(label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Sockets [seconds (Float), frame (Float)]
        
    """

    return nodes.SceneTime(label=node_label, node_color=node_color)

def b_and(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.b_and(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def b_or(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.b_or(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def b_not(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.b_not(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def nand(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.nand(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def nor(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.nor(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def xnor(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.xnor(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def xor(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.xor(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def imply(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.imply(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def nimply(boolean0=None, boolean1=None, operation='AND', node_label = None, node_color = None):
    """ > Node: BooleanMath
      
    <sub>go to: top index
    blender ref FunctionNodeBooleanMath
    node ref Boolean Math </sub>
                              
    ```python
    v = functions.nimply(boolean0, boolean1, operation, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - boolean0 : Boolean
        - boolean1 : Boolean## Parameters
        - operation : 'AND' in [AND, OR, NOT, NAND, NOR, XNOR, XOR, IMPLY, NIMPLY]
        - node_label : None
        - node_color : None


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Boolean
        
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation=operation, label=node_label, node_color=node_color).boolean

def add(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.add(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='ADD', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='ADD', label=node_label, node_color=node_color).value

def subtract(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.subtract(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SUBTRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color).value

def multiply(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.multiply(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MULTIPLY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color).value

def divide(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.divide(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'DIVIDE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color).value

def multiply_add(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.multiply_add(value0, value1, value2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MULTIPLY_ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).value

def pow(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.pow(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'POWER'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='POWER', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='POWER', label=node_label, node_color=node_color).value

def log(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.log(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'LOGARITHM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color).value

def sqrt(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sqrt(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SQRT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SQRT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SQRT', label=node_label, node_color=node_color).value

def inverse_sqrt(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.inverse_sqrt(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'INVERSE_SQRT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='INVERSE_SQRT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='INVERSE_SQRT', label=node_label, node_color=node_color).value

def abs(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.abs(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ABSOLUTE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ABSOLUTE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ABSOLUTE', label=node_label, node_color=node_color).value

def exp(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.exp(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'EXPONENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='EXPONENT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='EXPONENT', label=node_label, node_color=node_color).value

def min(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.min(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MINIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color).value

def max(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.max(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MAXIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color).value

def less_than(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.less_than(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'LESS_THAN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color).value

def greater_than(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.greater_than(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'GREATER_THAN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color).value

def sign(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sign(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SIGN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SIGN', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SIGN', label=node_label, node_color=node_color).value

def compare(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.compare(value0, value1, value2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'COMPARE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color).value

def smooth_min(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.smooth_min(value0, value1, value2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SMOOTH_MIN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color).value

def smooth_max(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.smooth_max(value0, value1, value2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SMOOTH_MAX'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color).value

def round(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.round(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ROUND'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ROUND', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ROUND', label=node_label, node_color=node_color).value

def floor(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.floor(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'FLOOR'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='FLOOR', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='FLOOR', label=node_label, node_color=node_color).value

def ceil(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.ceil(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'CEIL'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='CEIL', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='CEIL', label=node_label, node_color=node_color).value

def trunc(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.trunc(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'TRUNC'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='TRUNC', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='TRUNC', label=node_label, node_color=node_color).value

def fract(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.fract(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'FRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='FRACT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='FRACT', label=node_label, node_color=node_color).value

def modulo(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.modulo(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MODULO'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='MODULO', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='MODULO', label=node_label, node_color=node_color).value

def wrap(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.wrap(value0, value1, value2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float
        - value2 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'WRAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color).value

def snap(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.snap(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SNAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='SNAP', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='SNAP', label=node_label, node_color=node_color).value

def pingpong(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.pingpong(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'PINGPONG'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color).value

def sin(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sin(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SINE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SINE', label=node_label, node_color=node_color).value

def cos(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.cos(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'COSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='COSINE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='COSINE', label=node_label, node_color=node_color).value

def tan(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.tan(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'TANGENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='TANGENT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='TANGENT', label=node_label, node_color=node_color).value

def arcsin(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arcsin(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ARCSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ARCSINE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ARCSINE', label=node_label, node_color=node_color).value

def arccos(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arccos(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ARCCOSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ARCCOSINE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ARCCOSINE', label=node_label, node_color=node_color).value

def arctan(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arctan(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ARCTANGENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='ARCTANGENT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='ARCTANGENT', label=node_label, node_color=node_color).value

def arctan2(value0=None, value1=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.arctan2(value0, value1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float
        - value1 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ARCTAN2'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color).value

def sinh(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.sinh(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SINH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='SINH', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='SINH', label=node_label, node_color=node_color).value

def cosh(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.cosh(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'COSH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='COSH', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='COSH', label=node_label, node_color=node_color).value

def tanh(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.tanh(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'TANH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='TANH', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='TANH', label=node_label, node_color=node_color).value

def radians(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.radians(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'RADIANS'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='RADIANS', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='RADIANS', label=node_label, node_color=node_color).value

def degrees(value0=None, node_label = None, node_color = None):
    """ > Node: Math
      
    <sub>go to: top index
    blender ref ShaderNodeMath
    node ref Math </sub>
                              
    ```python
    v = functions.degrees(value0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - value0 : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'DEGREES'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Math(value0=value0, operation='DEGREES', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.Math(value0=value0, operation='DEGREES', label=node_label, node_color=node_color).value

def vector_add(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_add(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD', label=node_label, node_color=node_color).vector

def vector_subtract(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_subtract(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SUBTRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color).vector

def vector_multiply(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_multiply(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MULTIPLY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color).vector

def vector_divide(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_divide(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'DIVIDE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color).vector

def vector_multiply_add(vector0=None, vector1=None, vector2=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_multiply_add(vector0, vector1, vector2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - vector2 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MULTIPLY_ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).vector

def cross(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.cross(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'CROSS_PRODUCT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color).vector

def project(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.project(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'PROJECT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color).vector

def reflect(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.reflect(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'REFLECT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color).vector

def refract(vector0=None, vector1=None, scale=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.refract(vector0, vector1, scale, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - scale : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'REFRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color).vector

def faceforward(vector0=None, vector1=None, vector2=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.faceforward(vector0, vector1, vector2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - vector2 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'FACEFORWARD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color).vector

def dot(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.dot(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'DOT_PRODUCT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color).value

def distance(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.distance(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'DISTANCE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color).value

def length(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.length(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'LENGTH'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='LENGTH', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Float
        
    """

    return nodes.VectorMath(vector0=vector0, operation='LENGTH', label=node_label, node_color=node_color).value

def scale(vector0=None, scale=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.scale(vector0, scale, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - scale : Float## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SCALE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE', label=node_label, node_color=node_color).vector

def normalize(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.normalize(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'NORMALIZE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='NORMALIZE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='NORMALIZE', label=node_label, node_color=node_color).vector

def vector_absolute(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_absolute(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'ABSOLUTE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='ABSOLUTE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='ABSOLUTE', label=node_label, node_color=node_color).vector

def vector_min(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_min(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MINIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color).vector

def vector_max(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_max(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MAXIMUM'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color).vector

def vector_floor(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_floor(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'FLOOR'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='FLOOR', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='FLOOR', label=node_label, node_color=node_color).vector

def vector_ceil(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_ceil(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'CEIL'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='CEIL', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='CEIL', label=node_label, node_color=node_color).vector

def fraction(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.fraction(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'FRACTION'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='FRACTION', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='FRACTION', label=node_label, node_color=node_color).vector

def vector_modulo(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_modulo(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'MODULO'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color).vector

def vector_wrap(vector0=None, vector1=None, vector2=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_wrap(vector0, vector1, vector2, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector
        - vector2 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'WRAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color).vector

def vector_snap(vector0=None, vector1=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_snap(vector0, vector1, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector
        - vector1 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SNAP'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color).vector

def vector_sin(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_sin(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'SINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='SINE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='SINE', label=node_label, node_color=node_color).vector

def vector_cos(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_cos(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'COSINE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='COSINE', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='COSINE', label=node_label, node_color=node_color).vector

def vector_tan(vector0=None, node_label = None, node_color = None):
    """ > Node: VectorMath
      
    <sub>go to: top index
    blender ref ShaderNodeVectorMath
    node ref Vector Math </sub>
                              
    ```python
    v = functions.vector_tan(vector0, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - vector0 : Vector## Parameters
        - node_label : None
        - node_color : None## Fixed parameters
        - operation : 'TANGENT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.VectorMath(vector0=vector0, operation='TANGENT', label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Vector
        
    """

    return nodes.VectorMath(vector0=vector0, operation='TANGENT', label=node_label, node_color=node_color).vector

def color_mix(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_mix(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'MIX'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_darken(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_darken(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'DARKEN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_multiply(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_multiply(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'MULTIPLY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_burn(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_burn(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'BURN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_lighten(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_lighten(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'LIGHTEN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_screen(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_screen(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'SCREEN'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_dodge(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_dodge(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'DODGE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_add(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_add(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'ADD'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_overlay(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_overlay(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'OVERLAY'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_soft_light(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_soft_light(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'SOFT_LIGHT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_linear_light(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_linear_light(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'LINEAR_LIGHT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_difference(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_difference(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'DIFFERENCE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_subtract(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_subtract(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'SUBTRACT'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_divide(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_divide(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'DIVIDE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_hue(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_hue(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'HUE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_saturation(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_saturation(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'SATURATION'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_mix_color(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_mix_color(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'COLOR'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_value(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ > Node: Mix
      
    <sub>go to: top index
    blender ref ShaderNodeMixRGB
    node ref Mix </sub>
                              
    ```python
    v = functions.color_value(color1, color2, fac, use_alpha, node_label = None, node_color = None)
    ```


    Arguments
    ---------
        ## Sockets
        - color1 : Color
        - color2 : Color
        - fac : Float## Parameters
        - use_alpha : False
        - node_label : None
        - node_color : None## Fixed parameters
        - blend_type : 'VALUE'


    Node creation
    -------------
        ```python
        from geondes import nodes
        nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
        ```


    Returns
    -------
        Color
        
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color).color


