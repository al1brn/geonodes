#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-21
@author: Generated from generator module
Blender version: 3.2.2
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

""" Function to declare in file __init__.py
from geonodes.sockets.functions import abs, add, arccos, arcsin, arctan, arctan2, b_and, b_not, b_or, ceil
from geonodes.sockets.functions import color_add, color_burn, color_darken, color_difference, color_divide
from geonodes.sockets.functions import color_dodge, color_hue, color_lighten, color_linear_light, color_mix
from geonodes.sockets.functions import color_mix_color, color_multiply, color_overlay, color_saturation
from geonodes.sockets.functions import color_screen, color_soft_light, color_subtract, color_value, compare
from geonodes.sockets.functions import compare, cos, cosh, cross, degrees, distance, divide, dot, exp
from geonodes.sockets.functions import faceforward, floor, fract, fraction, imply, inverse_sqrt, join_strings
from geonodes.sockets.functions import length, log, math_greater_than, math_less_than, max, min, modulo
from geonodes.sockets.functions import multiply, multiply_add, nand, nimply, nor, normalize, pingpong
from geonodes.sockets.functions import pow, project, radians, reflect, refract, round, scale, scene, sign
from geonodes.sockets.functions import sin, sinh, smooth_max, smooth_min, snap, sqrt, subtract, switch
from geonodes.sockets.functions import tan, tanh, trunc, vector_absolute, vector_add, vector_ceil, vector_cos
from geonodes.sockets.functions import vector_divide, vector_floor, vector_max, vector_min, vector_modulo
from geonodes.sockets.functions import vector_multiply, vector_multiply_add, vector_sin, vector_snap, vector_subtract
from geonodes.sockets.functions import vector_tan, vector_wrap, wrap, xnor, xor
"""

""" Data class functions
"""

# ----------------------------------------------------------------------------------------------------
# Functions

def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label = None, node_color = None):
    """ Geometry node [*Compare*].
    
    
        Args:
            a: Float
            b: Float
            epsilon: Float
            data_type (str): 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
            mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
            operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Compare`
        
        
        .. blid:: FunctionNodeCompare
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation, label=node_label, node_color=node_color)
            
    """

    return nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation, label=node_label, node_color=node_color).result

def join_strings(*strings, delimiter=None, node_label = None, node_color = None):
    """ Geometry node [*Join Strings*].
    
    
        Args:
            strings: <m>String
            delimiter: String
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            String
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.JoinStrings`
        
        
        .. blid:: GeometryNodeStringJoin
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.JoinStrings(*strings, delimiter=delimiter, label=node_label, node_color=node_color)
            
    """

    return nodes.JoinStrings(*strings, delimiter=delimiter, label=node_label, node_color=node_color).string

def scene(node_label = None, node_color = None):
    """ Geometry node [*Scene Time*].
    
    
        Args:
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Sockets [seconds (Float), frame (Float)]
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.SceneTime`
        
        
        .. blid:: GeometryNodeInputSceneTime
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.SceneTime(label=node_label, node_color=node_color)
            
    """

    return nodes.SceneTime(label=node_label, node_color=node_color)

def switch(switch=None, false=None, true=None, input_type='GEOMETRY', node_label = None, node_color = None):
    """ Geometry node [*Switch*].
    
    
        Args:
            switch: Boolean
            false: Geometry
            true: Geometry
            input_type (str): 'GEOMETRY' in [FLOAT, INT, BOOLEAN, VECTOR, STRING,... , COLLECTION, TEXTURE, MATERIAL]
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            input_type dependant
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Switch`
        
        
        .. blid:: GeometryNodeSwitch
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Switch(switch=switch, false=false, true=true, input_type=input_type, label=node_label, node_color=node_color)
            
    """

    return nodes.Switch(switch=switch, false=false, true=true, input_type=input_type, label=node_label, node_color=node_color).output

def b_and(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'AND'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color).boolean

def b_or(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'OR'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color).boolean

def b_not(boolean0=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'NOT'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, operation='NOT', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, operation='NOT', label=node_label, node_color=node_color).boolean

def nand(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'NAND'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color).boolean

def nor(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'NOR'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color).boolean

def xnor(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'XNOR'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color).boolean

def xor(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'XOR'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color).boolean

def imply(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'IMPLY'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color).boolean

def nimply(boolean0=None, boolean1=None, node_label = None, node_color = None):
    """ Geometry node [*Boolean Math*].
    
    
        Args:
            boolean0: Boolean
            boolean1: Boolean
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Boolean
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.BooleanMath`
        
            - operation = 'NIMPLY'
              
        .. blid:: FunctionNodeBooleanMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color)
            
    """

    return nodes.BooleanMath(boolean0=boolean0, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color).boolean

def add(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ADD'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='ADD', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='ADD', label=node_label, node_color=node_color).value

def subtract(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SUBTRACT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color).value

def multiply(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'MULTIPLY'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color).value

def divide(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'DIVIDE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color).value

def multiply_add(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            value2: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'MULTIPLY_ADD'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).value

def pow(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'POWER'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='POWER', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='POWER', label=node_label, node_color=node_color).value

def log(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'LOGARITHM'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color).value

def sqrt(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SQRT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='SQRT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='SQRT', label=node_label, node_color=node_color).value

def inverse_sqrt(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'INVERSE_SQRT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='INVERSE_SQRT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='INVERSE_SQRT', label=node_label, node_color=node_color).value

def abs(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ABSOLUTE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='ABSOLUTE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='ABSOLUTE', label=node_label, node_color=node_color).value

def exp(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'EXPONENT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='EXPONENT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='EXPONENT', label=node_label, node_color=node_color).value

def min(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'MINIMUM'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color).value

def max(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'MAXIMUM'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color).value

def math_less_than(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'LESS_THAN'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color).value

def math_greater_than(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'GREATER_THAN'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color).value

def sign(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SIGN'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='SIGN', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='SIGN', label=node_label, node_color=node_color).value

def compare(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            value2: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'COMPARE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color).value

def smooth_min(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            value2: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SMOOTH_MIN'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color).value

def smooth_max(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            value2: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SMOOTH_MAX'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color).value

def round(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ROUND'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='ROUND', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='ROUND', label=node_label, node_color=node_color).value

def floor(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'FLOOR'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='FLOOR', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='FLOOR', label=node_label, node_color=node_color).value

def ceil(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'CEIL'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='CEIL', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='CEIL', label=node_label, node_color=node_color).value

def trunc(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'TRUNC'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='TRUNC', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='TRUNC', label=node_label, node_color=node_color).value

def fract(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'FRACT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='FRACT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='FRACT', label=node_label, node_color=node_color).value

def modulo(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'MODULO'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='MODULO', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='MODULO', label=node_label, node_color=node_color).value

def wrap(value0=None, value1=None, value2=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            value2: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'WRAP'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color).value

def snap(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SNAP'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='SNAP', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='SNAP', label=node_label, node_color=node_color).value

def pingpong(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'PINGPONG'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color).value

def sin(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SINE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='SINE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='SINE', label=node_label, node_color=node_color).value

def cos(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'COSINE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='COSINE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='COSINE', label=node_label, node_color=node_color).value

def tan(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'TANGENT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='TANGENT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='TANGENT', label=node_label, node_color=node_color).value

def arcsin(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ARCSINE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='ARCSINE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='ARCSINE', label=node_label, node_color=node_color).value

def arccos(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ARCCOSINE'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='ARCCOSINE', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='ARCCOSINE', label=node_label, node_color=node_color).value

def arctan(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ARCTANGENT'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='ARCTANGENT', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='ARCTANGENT', label=node_label, node_color=node_color).value

def arctan2(value0=None, value1=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            value1: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'ARCTAN2'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color).value

def sinh(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'SINH'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='SINH', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='SINH', label=node_label, node_color=node_color).value

def cosh(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'COSH'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='COSH', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='COSH', label=node_label, node_color=node_color).value

def tanh(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'TANH'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='TANH', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='TANH', label=node_label, node_color=node_color).value

def radians(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'RADIANS'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='RADIANS', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='RADIANS', label=node_label, node_color=node_color).value

def degrees(value0=None, node_label = None, node_color = None):
    """ Geometry node [*Math*].
    
    
        Args:
            value0: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Math`
        
            - operation = 'DEGREES'
              
        .. blid:: ShaderNodeMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Math(value0=value0, operation='DEGREES', label=node_label, node_color=node_color)
            
    """

    return nodes.Math(value0=value0, operation='DEGREES', label=node_label, node_color=node_color).value

def vector_add(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'ADD'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD', label=node_label, node_color=node_color).vector

def vector_subtract(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'SUBTRACT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color).vector

def vector_multiply(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'MULTIPLY'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color).vector

def vector_divide(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'DIVIDE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color).vector

def vector_multiply_add(vector0=None, vector1=None, vector2=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            vector2: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'MULTIPLY_ADD'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).vector

def cross(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'CROSS_PRODUCT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color).vector

def project(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'PROJECT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color).vector

def reflect(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'REFLECT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color).vector

def refract(vector0=None, vector1=None, scale=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            scale: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'REFRACT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color).vector

def faceforward(vector0=None, vector1=None, vector2=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            vector2: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'FACEFORWARD'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color).vector

def dot(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'DOT_PRODUCT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color).value

def distance(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'DISTANCE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color).value

def length(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Float
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'LENGTH'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='LENGTH', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='LENGTH', label=node_label, node_color=node_color).value

def scale(vector0=None, scale=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            scale: Float
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'SCALE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE', label=node_label, node_color=node_color).vector

def normalize(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'NORMALIZE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='NORMALIZE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='NORMALIZE', label=node_label, node_color=node_color).vector

def vector_absolute(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'ABSOLUTE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='ABSOLUTE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='ABSOLUTE', label=node_label, node_color=node_color).vector

def vector_min(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'MINIMUM'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color).vector

def vector_max(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'MAXIMUM'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color).vector

def vector_floor(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'FLOOR'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='FLOOR', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='FLOOR', label=node_label, node_color=node_color).vector

def vector_ceil(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'CEIL'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='CEIL', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='CEIL', label=node_label, node_color=node_color).vector

def fraction(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'FRACTION'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='FRACTION', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='FRACTION', label=node_label, node_color=node_color).vector

def vector_modulo(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'MODULO'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color).vector

def vector_wrap(vector0=None, vector1=None, vector2=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            vector2: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'WRAP'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color).vector

def vector_snap(vector0=None, vector1=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            vector1: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'SNAP'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color).vector

def vector_sin(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'SINE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='SINE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='SINE', label=node_label, node_color=node_color).vector

def vector_cos(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'COSINE'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='COSINE', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='COSINE', label=node_label, node_color=node_color).vector

def vector_tan(vector0=None, node_label = None, node_color = None):
    """ Geometry node [*Vector Math*].
    
    
        Args:
            vector0: Vector
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Vector
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.VectorMath`
        
            - operation = 'TANGENT'
              
        .. blid:: ShaderNodeVectorMath
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.VectorMath(vector0=vector0, operation='TANGENT', label=node_label, node_color=node_color)
            
    """

    return nodes.VectorMath(vector0=vector0, operation='TANGENT', label=node_label, node_color=node_color).vector

def color_mix(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'MIX'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_darken(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'DARKEN'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_multiply(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'MULTIPLY'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_burn(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'BURN'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_lighten(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'LIGHTEN'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_screen(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'SCREEN'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_dodge(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'DODGE'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_add(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'ADD'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_overlay(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'OVERLAY'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_soft_light(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'SOFT_LIGHT'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_linear_light(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'LINEAR_LIGHT'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_difference(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'DIFFERENCE'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_subtract(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'SUBTRACT'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_divide(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'DIVIDE'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_hue(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'HUE'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_saturation(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'SATURATION'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_mix_color(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'COLOR'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color).color

def color_value(color1=None, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
    """ Geometry node [*Mix*].
    
    
        Args:
            color1: Color
            color2: Color
            fac: Float
            use_alpha (bool): False
            node_label (str): Node label
            node_color (color): Node background color
            
        Returns:
            Color
            
        **Node creation**
        
        Node :class:`~geonodes.nodes.nodes.Mix`
        
            - blend_type = 'VALUE'
              
        .. blid:: ShaderNodeMixRGB
        
        .. code-block:: python
        
            from geonodes import nodes
            nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
            
    """

    return nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color).color


