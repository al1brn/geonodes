#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-12-22

@author: Generated from generator module

Blender version: 3.4.0
"""

from geonodes.core.node import Node


# ----------------------------------------------------------------------------------------------------
# Node AlignEulerToVector for FunctionNodeAlignEulerToVector

class AlignEulerToVector(Node):

    """Node *Align Euler to Vector*

    .. _AlignEulerToVector:

    Node implementation:
        global functions:
            align_euler_to_vector 
        Vector:
            align_euler_to_vector 

    Args:
        rotation (DataSocket): Vector
        factor (DataSocket): Float
        vector (DataSocket): Vector
        axis (str): Node parameter, default = 'X' in ('X', 'Y', 'Z')
        pivot_axis (str): Node parameter, default = 'AUTO' in ('AUTO', 'X', 'Y', 'Z')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **rotation** : Vector

    .. blid:: FunctionNodeAlignEulerToVector

    """

    def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None, node_color=None):

        super().__init__('FunctionNodeAlignEulerToVector', node_name='Align Euler to Vector', label=label, node_color=node_color)

        # Node parameters

        self.bnode.axis            = axis
        self.bnode.pivot_axis      = pivot_axis

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'rotation' : 0, 'factor' : 1, 'vector' : 2, }
        self.outsockets = {'rotation' : 0, }

        # Input sockets plugging

        if rotation        is not None: self.rotation        = rotation
        if factor          is not None: self.factor          = factor
        if vector          is not None: self.vector          = vector

    @property
    def axis(self):
        return self.bnode.axis

    @axis.setter
    def axis(self, value):
        self.bnode.axis = value

    @property
    def pivot_axis(self):
        return self.bnode.pivot_axis

    @pivot_axis.setter
    def pivot_axis(self, value):
        self.bnode.pivot_axis = value

    @property
    def rotation(self):
        return self.get_output_socket('rotation')

    @rotation.setter
    def rotation(self, value):
        self.set_input_socket('rotation', value)

    @property
    def factor(self):
        raise AttributeError("Attribute error on node 'AlignEulerToVector': the input socket 'factor' is write only.")

    @factor.setter
    def factor(self, value):
        self.set_input_socket('factor', value)

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'AlignEulerToVector': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

# ----------------------------------------------------------------------------------------------------
# Node BooleanMath for FunctionNodeBooleanMath

class BooleanMath(Node):

    """Node *Boolean Math*

    .. _BooleanMath:

    Node implementation:
        global functions:
            b_and b_or b_not nand nor xnor xor imply nimply 
        Boolean:
            b_and b_or b_not nand nor xnor xor imply nimply 

    Args:
        boolean0 (DataSocket): Boolean
        boolean1 (DataSocket): Boolean
        operation (str): Node parameter, default = 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **boolean** : Boolean

    .. blid:: FunctionNodeBooleanMath

    """

    def __init__(self, boolean0=None, boolean1=None, operation='AND', label=None, node_color=None):

        super().__init__('FunctionNodeBooleanMath', node_name='Boolean Math', label=label, node_color=node_color)

        # Node parameters

        self.bnode.operation       = operation

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'boolean0' : 0, 'boolean1' : 1, }
        self.outsockets = {'boolean' : 0, }

        # Input sockets plugging

        if boolean0        is not None: self.boolean0        = boolean0
        if boolean1        is not None: self.boolean1        = boolean1

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

    @property
    def boolean(self):
        return self.get_output_socket('boolean')

    @property
    def boolean0(self):
        raise AttributeError("Attribute error on node 'BooleanMath': the input socket 'boolean0' is write only.")

    @boolean0.setter
    def boolean0(self, value):
        self.set_input_socket('boolean0', value)

    @property
    def boolean1(self):
        raise AttributeError("Attribute error on node 'BooleanMath': the input socket 'boolean1' is write only.")

    @boolean1.setter
    def boolean1(self, value):
        self.set_input_socket('boolean1', value)

# ----------------------------------------------------------------------------------------------------
# Node CombineColor for FunctionNodeCombineColor

class CombineColor(Node):

    """Node *Combine Color*

    .. _CombineColor:

    Node implementation:
        global functions:
            combine_rgb combine_hsv combine_hsl 
        Color:
            RGB HSV HSL 

    Args:
        red (DataSocket): Float
        green (DataSocket): Float
        blue (DataSocket): Float
        alpha (DataSocket): Float
        mode (str): Node parameter, default = 'RGB' in ('RGB', 'HSV', 'HSL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color

    .. blid:: FunctionNodeCombineColor

    """

    def __init__(self, red=None, green=None, blue=None, alpha=None, mode='RGB', label=None, node_color=None):

        super().__init__('FunctionNodeCombineColor', node_name='Combine Color', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'red' : 0, 'green' : 1, 'blue' : 2, 'alpha' : 3, }
        self.outsockets = {'color' : 0, }

        # Input sockets plugging

        if red             is not None: self.red             = red
        if green           is not None: self.green           = green
        if blue            is not None: self.blue            = blue
        if alpha           is not None: self.alpha           = alpha

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def red(self):
        raise AttributeError("Attribute error on node 'CombineColor': the input socket 'red' is write only.")

    @red.setter
    def red(self, value):
        self.set_input_socket('red', value)

    @property
    def green(self):
        raise AttributeError("Attribute error on node 'CombineColor': the input socket 'green' is write only.")

    @green.setter
    def green(self, value):
        self.set_input_socket('green', value)

    @property
    def blue(self):
        raise AttributeError("Attribute error on node 'CombineColor': the input socket 'blue' is write only.")

    @blue.setter
    def blue(self, value):
        self.set_input_socket('blue', value)

    @property
    def alpha(self):
        raise AttributeError("Attribute error on node 'CombineColor': the input socket 'alpha' is write only.")

    @alpha.setter
    def alpha(self, value):
        self.set_input_socket('alpha', value)

# ----------------------------------------------------------------------------------------------------
# Node Compare for FunctionNodeCompare

class Compare(Node):

    """Node *Compare*

    .. _Compare:

    Node implementation:
        global functions:
            compare 
        Float:
            compare less_than less_equal greater_than greater_equal equal not_equal 
        Integer:
            compare less_than less_equal greater_than greater_equal equal not_equal 
        String:
            equal not_equal 
        Vector:
            compare elements_less_than elements_less_equal elements_greater_than elements_greater_equal elements_equal elements_not_equal length_less_than length_less_equal length_greater_than 
            length_greater_equal length_equal length_not_equal average_less_than average_less_equal average_greater_than average_greater_equal average_equal average_not_equal dot_product_less_than 
            dot_product_less_equal dot_product_greater_than dot_product_greater_equal dot_product_equal dot_product_not_equal direction_less_than direction_less_equal direction_greater_than direction_greater_equal direction_equal 
            direction_not_equal 
        Color:
            darker brighter equal equal 

    Args:
        a (DataSocket): ``data_type`` dependant
        b (DataSocket): ``data_type`` dependant
        c (DataSocket): Float
        angle (DataSocket): Float
        epsilon (DataSocket): Float
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
        mode (str): Node parameter, default = 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
        operation (str): Node parameter, default = 'GREATER_THAN' in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **result** : Boolean

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
        - Input sockets  : ['a', 'b']
        - Output sockets : []

    .. blid:: FunctionNodeCompare

    """

    def __init__(self, a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None, node_color=None):

        super().__init__('FunctionNodeCompare', node_name='Compare', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(b) if data_type is None else data_type
        self.bnode.mode            = mode
        self.bnode.operation       = operation

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'a' : [0, 2, 4, 6, 8], 'b' : [1, 3, 5, 7, 9], 'c' : 10, 'angle' : 11, 'epsilon' : 12, }
        self.outsockets = {'result' : 0, }

        # Input sockets plugging

        if a               is not None: self.a               = a
        if b               is not None: self.b               = b
        if c               is not None: self.c               = c
        if angle           is not None: self.angle           = angle
        if epsilon         is not None: self.epsilon         = epsilon

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

    @property
    def result(self):
        return self.get_output_socket('result')

    @property
    def a(self):
        raise AttributeError("Attribute error on node 'Compare': the input socket 'a' is write only.")

    @a.setter
    def a(self, value):
        self.set_input_socket('a', value)

    @property
    def b(self):
        raise AttributeError("Attribute error on node 'Compare': the input socket 'b' is write only.")

    @b.setter
    def b(self, value):
        self.set_input_socket('b', value)

    @property
    def c(self):
        raise AttributeError("Attribute error on node 'Compare': the input socket 'c' is write only.")

    @c.setter
    def c(self, value):
        self.set_input_socket('c', value)

    @property
    def angle(self):
        raise AttributeError("Attribute error on node 'Compare': the input socket 'angle' is write only.")

    @angle.setter
    def angle(self, value):
        self.set_input_socket('angle', value)

    @property
    def epsilon(self):
        raise AttributeError("Attribute error on node 'Compare': the input socket 'epsilon' is write only.")

    @epsilon.setter
    def epsilon(self, value):
        self.set_input_socket('epsilon', value)

# ----------------------------------------------------------------------------------------------------
# Node FloatToInteger for FunctionNodeFloatToInt

class FloatToInteger(Node):

    """Node *Float to Integer*

    .. _FloatToInteger:

    Node implementation:
        Float:
            to_integer round floor ceiling truncate 

    Args:
        float (DataSocket): Float
        rounding_mode (str): Node parameter, default = 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **integer** : Integer

    .. blid:: FunctionNodeFloatToInt

    """

    def __init__(self, float=None, rounding_mode='ROUND', label=None, node_color=None):

        super().__init__('FunctionNodeFloatToInt', node_name='Float to Integer', label=label, node_color=node_color)

        # Node parameters

        self.bnode.rounding_mode   = rounding_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'float' : 0, }
        self.outsockets = {'integer' : 0, }

        # Input sockets plugging

        if float           is not None: self.float           = float

    @property
    def rounding_mode(self):
        return self.bnode.rounding_mode

    @rounding_mode.setter
    def rounding_mode(self, value):
        self.bnode.rounding_mode = value

    @property
    def integer(self):
        return self.get_output_socket('integer')

    @property
    def float(self):
        raise AttributeError("Attribute error on node 'FloatToInteger': the input socket 'float' is write only.")

    @float.setter
    def float(self, value):
        self.set_input_socket('float', value)

# ----------------------------------------------------------------------------------------------------
# Node Boolean for FunctionNodeInputBool

class Boolean(Node):

    """Node *Boolean*

    .. _Boolean:

    Node implementation:
        Boolean:
            Boolean 

    Args:
        boolean (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **boolean** : Boolean

    .. blid:: FunctionNodeInputBool

    """

    def __init__(self, boolean=False, label=None, node_color=None):

        super().__init__('FunctionNodeInputBool', node_name='Boolean', label=label, node_color=node_color)

        # Node parameters

        self.bnode.boolean         = boolean

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'boolean' : 0, }

    @property
    def boolean_(self):
        return self.bnode.boolean

    @boolean_.setter
    def boolean_(self, value):
        self.bnode.boolean = value

    @property
    def boolean(self):
        return self.get_output_socket('boolean')

# ----------------------------------------------------------------------------------------------------
# Node Color for FunctionNodeInputColor

class Color(Node):

    """Node *Color*

    .. _Color:

    Node implementation:
        Color:
            Color 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color

    .. blid:: FunctionNodeInputColor

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('FunctionNodeInputColor', node_name='Color', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'color' : 0, }

    @property
    def color(self):
        return self.get_output_socket('color')

# ----------------------------------------------------------------------------------------------------
# Node Integer for FunctionNodeInputInt

class Integer(Node):

    """Node *Integer*

    .. _Integer:

    Node implementation:
        Integer:
            Integer 

    Args:
        integer (int): Node parameter, default = 0
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **integer** : Integer

    .. blid:: FunctionNodeInputInt

    """

    def __init__(self, integer=0, label=None, node_color=None):

        super().__init__('FunctionNodeInputInt', node_name='Integer', label=label, node_color=node_color)

        # Node parameters

        self.bnode.integer         = integer

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'integer' : 0, }

    @property
    def integer_(self):
        return self.bnode.integer

    @integer_.setter
    def integer_(self, value):
        self.bnode.integer = value

    @property
    def integer(self):
        return self.get_output_socket('integer')

# ----------------------------------------------------------------------------------------------------
# Node SpecialCharacters for FunctionNodeInputSpecialCharacters

class SpecialCharacters(Node):

    """Node *Special Characters*

    .. _SpecialCharacters:

    Node implementation:
        String:
            LineBreak Tab 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **line_break** : String
        - **tab** : String

    .. blid:: FunctionNodeInputSpecialCharacters

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('FunctionNodeInputSpecialCharacters', node_name='Special Characters', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'line_break' : 0, 'tab' : 1, }

    @property
    def line_break(self):
        return self.get_output_socket('line_break')

    @property
    def tab(self):
        return self.get_output_socket('tab')

# ----------------------------------------------------------------------------------------------------
# Node String for FunctionNodeInputString

class String(Node):

    """Node *String*

    .. _String:

    Node implementation:
        String:
            String 

    Args:
        string (str): Node parameter, default = ''
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **string** : String

    .. blid:: FunctionNodeInputString

    """

    def __init__(self, string='', label=None, node_color=None):

        super().__init__('FunctionNodeInputString', node_name='String', label=label, node_color=node_color)

        # Node parameters

        self.bnode.string          = string

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'string' : 0, }

    @property
    def string_(self):
        return self.bnode.string

    @string_.setter
    def string_(self, value):
        self.bnode.string = value

    @property
    def string(self):
        return self.get_output_socket('string')

# ----------------------------------------------------------------------------------------------------
# Node Vector for FunctionNodeInputVector

class Vector(Node):

    """Node *Vector*

    .. _Vector:

    Node implementation:
        Vector:
            Vector 

    Args:
        vector (Vector): Node parameter, default = [0.0, 0.0, 0.0]
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vector** : Vector

    .. blid:: FunctionNodeInputVector

    """

    def __init__(self, vector=[0.0, 0.0, 0.0], label=None, node_color=None):

        super().__init__('FunctionNodeInputVector', node_name='Vector', label=label, node_color=node_color)

        # Node parameters

        self.bnode.vector          = vector

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vector' : 0, }

    @property
    def vector_(self):
        return self.bnode.vector

    @vector_.setter
    def vector_(self, value):
        self.bnode.vector = value

    @property
    def vector(self):
        return self.get_output_socket('vector')

# ----------------------------------------------------------------------------------------------------
# Node RandomValue for FunctionNodeRandomValue

class RandomValue(Node):

    """Node *Random Value*

    .. _RandomValue:

    Node implementation:
        global functions:
            random_float random_integer random_vector random_boolean 
        Geometry:
            random_float random_integer random_vector random_boolean 
        Domain:
            random_float random_integer random_vector random_boolean 

    Args:
        min (DataSocket): ``data_type`` dependant
        max (DataSocket): ``data_type`` dependant
        probability (DataSocket): Float
        ID (DataSocket): Integer
        seed (DataSocket): Integer
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
        - Input sockets  : ['min', 'max']
        - Output sockets : ['value']

    .. blid:: FunctionNodeRandomValue

    """

    def __init__(self, min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None, node_color=None):

        super().__init__('FunctionNodeRandomValue', node_name='Random Value', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(max) if data_type is None else data_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'min' : [0, 2, 4], 'max' : [1, 3, 5], 'probability' : 6, 'ID' : 7, 'seed' : 8, }
        self.outsockets = {'value' : [0, 1, 2, 3], }

        # Input sockets plugging

        if min             is not None: self.min             = min
        if max             is not None: self.max             = max
        if probability     is not None: self.probability     = probability
        if ID              is not None: self.ID              = ID
        if seed            is not None: self.seed            = seed

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def min(self):
        raise AttributeError("Attribute error on node 'RandomValue': the input socket 'min' is write only.")

    @min.setter
    def min(self, value):
        self.set_input_socket('min', value)

    @property
    def max(self):
        raise AttributeError("Attribute error on node 'RandomValue': the input socket 'max' is write only.")

    @max.setter
    def max(self, value):
        self.set_input_socket('max', value)

    @property
    def probability(self):
        raise AttributeError("Attribute error on node 'RandomValue': the input socket 'probability' is write only.")

    @probability.setter
    def probability(self, value):
        self.set_input_socket('probability', value)

    @property
    def ID(self):
        raise AttributeError("Attribute error on node 'RandomValue': the input socket 'ID' is write only.")

    @ID.setter
    def ID(self, value):
        self.set_input_socket('ID', value)

    @property
    def seed(self):
        raise AttributeError("Attribute error on node 'RandomValue': the input socket 'seed' is write only.")

    @seed.setter
    def seed(self, value):
        self.set_input_socket('seed', value)

# ----------------------------------------------------------------------------------------------------
# Node ReplaceString for FunctionNodeReplaceString

class ReplaceString(Node):

    """Node *Replace String*

    .. _ReplaceString:

    Node implementation:
        global functions:
            replace_string 
        String:
            replace 

    Args:
        string (DataSocket): String
        find (DataSocket): String
        replace (DataSocket): String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **string** : String

    .. blid:: FunctionNodeReplaceString

    """

    def __init__(self, string=None, find=None, replace=None, label=None, node_color=None):

        super().__init__('FunctionNodeReplaceString', node_name='Replace String', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, 'find' : 1, 'replace' : 2, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if string          is not None: self.string          = string
        if find            is not None: self.find            = find
        if replace         is not None: self.replace         = replace

    @property
    def string(self):
        return self.get_output_socket('string')

    @string.setter
    def string(self, value):
        self.set_input_socket('string', value)

    @property
    def find(self):
        raise AttributeError("Attribute error on node 'ReplaceString': the input socket 'find' is write only.")

    @find.setter
    def find(self, value):
        self.set_input_socket('find', value)

    @property
    def replace(self):
        raise AttributeError("Attribute error on node 'ReplaceString': the input socket 'replace' is write only.")

    @replace.setter
    def replace(self, value):
        self.set_input_socket('replace', value)

# ----------------------------------------------------------------------------------------------------
# Node RotateEuler for FunctionNodeRotateEuler

class RotateEuler(Node):

    """Node *Rotate Euler*

    .. _RotateEuler:

    Node implementation:
        global functions:
            rotate_euler rotate_axis_angle 

    Args:
        rotation (DataSocket): Vector
        rotate_by (DataSocket): Vector
        axis (DataSocket): Vector
        angle (DataSocket): Float
        space (str): Node parameter, default = 'OBJECT' in ('OBJECT', 'LOCAL')
        type (str): Node parameter, default = 'EULER' in ('AXIS_ANGLE', 'EULER')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **rotation** : Vector

    .. blid:: FunctionNodeRotateEuler

    """

    def __init__(self, rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER', label=None, node_color=None):

        super().__init__('FunctionNodeRotateEuler', node_name='Rotate Euler', label=label, node_color=node_color)

        # Node parameters

        self.bnode.space           = space
        self.bnode.type            = type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'rotation' : 0, 'rotate_by' : 1, 'axis' : 2, 'angle' : 3, }
        self.outsockets = {'rotation' : 0, }

        # Input sockets plugging

        if rotation        is not None: self.rotation        = rotation
        if rotate_by       is not None: self.rotate_by       = rotate_by
        if axis            is not None: self.axis            = axis
        if angle           is not None: self.angle           = angle

    @property
    def space(self):
        return self.bnode.space

    @space.setter
    def space(self, value):
        self.bnode.space = value

    @property
    def type(self):
        return self.bnode.type

    @type.setter
    def type(self, value):
        self.bnode.type = value

    @property
    def rotation(self):
        return self.get_output_socket('rotation')

    @rotation.setter
    def rotation(self, value):
        self.set_input_socket('rotation', value)

    @property
    def rotate_by(self):
        raise AttributeError("Attribute error on node 'RotateEuler': the input socket 'rotate_by' is write only.")

    @rotate_by.setter
    def rotate_by(self, value):
        self.set_input_socket('rotate_by', value)

    @property
    def axis(self):
        raise AttributeError("Attribute error on node 'RotateEuler': the input socket 'axis' is write only.")

    @axis.setter
    def axis(self, value):
        self.set_input_socket('axis', value)

    @property
    def angle(self):
        raise AttributeError("Attribute error on node 'RotateEuler': the input socket 'angle' is write only.")

    @angle.setter
    def angle(self, value):
        self.set_input_socket('angle', value)

# ----------------------------------------------------------------------------------------------------
# Node SeparateColor for FunctionNodeSeparateColor

class SeparateColor(Node):

    """Node *Separate Color*

    .. _SeparateColor:

    Node implementation:
        global functions:
            separate_rgb separate_hsv separate_hsl 
        Color:
            rgb hsv hsl alpha red green blue hue saturation value 
            lightness 

    Args:
        color (DataSocket): Color
        mode (str): Node parameter, default = 'RGB' in ('RGB', 'HSV', 'HSL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **red** : Float
        - **green** : Float
        - **blue** : Float
        - **alpha** : Float

    .. blid:: FunctionNodeSeparateColor

    """

    def __init__(self, color=None, mode='RGB', label=None, node_color=None):

        super().__init__('FunctionNodeSeparateColor', node_name='Separate Color', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'color' : 0, }
        self.outsockets = {'red' : 0, 'green' : 1, 'blue' : 2, 'alpha' : 3, }

        # Input sockets plugging

        if color           is not None: self.color           = color

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def red(self):
        return self.get_output_socket('red')

    @property
    def green(self):
        return self.get_output_socket('green')

    @property
    def blue(self):
        return self.get_output_socket('blue')

    @property
    def alpha(self):
        return self.get_output_socket('alpha')

    @property
    def color(self):
        raise AttributeError("Attribute error on node 'SeparateColor': the input socket 'color' is write only.")

    @color.setter
    def color(self, value):
        self.set_input_socket('color', value)

# ----------------------------------------------------------------------------------------------------
# Node SliceString for FunctionNodeSliceString

class SliceString(Node):

    """Node *Slice String*

    .. _SliceString:

    Node implementation:
        global functions:
            slice_string 
        String:
            slice 

    Args:
        string (DataSocket): String
        position (DataSocket): Integer
        length (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **string** : String

    .. blid:: FunctionNodeSliceString

    """

    def __init__(self, string=None, position=None, length=None, label=None, node_color=None):

        super().__init__('FunctionNodeSliceString', node_name='Slice String', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, 'position' : 1, 'length' : 2, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if string          is not None: self.string          = string
        if position        is not None: self.position        = position
        if length          is not None: self.length          = length

    @property
    def string(self):
        return self.get_output_socket('string')

    @string.setter
    def string(self, value):
        self.set_input_socket('string', value)

    @property
    def position(self):
        raise AttributeError("Attribute error on node 'SliceString': the input socket 'position' is write only.")

    @position.setter
    def position(self, value):
        self.set_input_socket('position', value)

    @property
    def length(self):
        raise AttributeError("Attribute error on node 'SliceString': the input socket 'length' is write only.")

    @length.setter
    def length(self, value):
        self.set_input_socket('length', value)

# ----------------------------------------------------------------------------------------------------
# Node StringLength for FunctionNodeStringLength

class StringLength(Node):

    """Node *String Length*

    .. _StringLength:

    Node implementation:
        global functions:
            string_length 
        String:
            length 

    Args:
        string (DataSocket): String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **length** : Integer

    .. blid:: FunctionNodeStringLength

    """

    def __init__(self, string=None, label=None, node_color=None):

        super().__init__('FunctionNodeStringLength', node_name='String Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, }
        self.outsockets = {'length' : 0, }

        # Input sockets plugging

        if string          is not None: self.string          = string

    @property
    def length(self):
        return self.get_output_socket('length')

    @property
    def string(self):
        raise AttributeError("Attribute error on node 'StringLength': the input socket 'string' is write only.")

    @string.setter
    def string(self, value):
        self.set_input_socket('string', value)

# ----------------------------------------------------------------------------------------------------
# Node ValueToString for FunctionNodeValueToString

class ValueToString(Node):

    """Node *Value to String*

    .. _ValueToString:

    Node implementation:
        global functions:
            value_to_string 
        Float:
            to_string 
        Integer:
            to_string 

    Args:
        value (DataSocket): Float
        decimals (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **string** : String

    .. blid:: FunctionNodeValueToString

    """

    def __init__(self, value=None, decimals=None, label=None, node_color=None):

        super().__init__('FunctionNodeValueToString', node_name='Value to String', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value' : 0, 'decimals' : 1, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if value           is not None: self.value           = value
        if decimals        is not None: self.decimals        = decimals

    @property
    def string(self):
        return self.get_output_socket('string')

    @property
    def value(self):
        raise AttributeError("Attribute error on node 'ValueToString': the input socket 'value' is write only.")

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def decimals(self):
        raise AttributeError("Attribute error on node 'ValueToString': the input socket 'decimals' is write only.")

    @decimals.setter
    def decimals(self, value):
        self.set_input_socket('decimals', value)

# ----------------------------------------------------------------------------------------------------
# Node AccumulateField for GeometryNodeAccumulateField

class AccumulateField(Node):

    """Node *Accumulate Field*

    .. _AccumulateField:

    Node implementation:
        Domain:
            accumulate_field 

    Args:
        value (DataSocket): ``data_type`` dependant
        group_index (DataSocket): Integer
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **leading** : ``data_type`` dependant
        - **trailing** : ``data_type`` dependant
        - **total** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR')
        - Input sockets  : ['value']
        - Output sockets : ['leading', 'trailing', 'total']

    .. blid:: GeometryNodeAccumulateField

    """

    def __init__(self, value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeAccumulateField', node_name='Accumulate Field', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value' : [0, 1, 2], 'group_index' : 3, }
        self.outsockets = {'leading' : [0, 1, 2], 'trailing' : [3, 4, 5], 'total' : [6, 7, 8], }

        # Input sockets plugging

        if value           is not None: self.value           = value
        if group_index     is not None: self.group_index     = group_index

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def leading(self):
        return self.get_output_socket('leading')

    @property
    def trailing(self):
        return self.get_output_socket('trailing')

    @property
    def total(self):
        return self.get_output_socket('total')

    @property
    def value(self):
        raise AttributeError("Attribute error on node 'AccumulateField': the input socket 'value' is write only.")

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def group_index(self):
        raise AttributeError("Attribute error on node 'AccumulateField': the input socket 'group_index' is write only.")

    @group_index.setter
    def group_index(self, value):
        self.set_input_socket('group_index', value)

# ----------------------------------------------------------------------------------------------------
# Node DomainSize for GeometryNodeAttributeDomainSize

class DomainSize(Node):

    """Node *Domain Size*

    .. _DomainSize:

    Node implementation:
        Geometry:
            domain_size 
        Mesh:
            domain_size point_count face_count edge_count corner_count 
        Curve:
            domain_size point_count spline_count 
        Points:
            domain_size 
        Instances:
            domain_size 
        Vertex:
            count 
        Face:
            count 
        Edge:
            count 
        Corner:
            count 
        Spline:
            count 
        ControlPoint:
            count 
        CloudPoint:
            count 
        Instance:
            count 

    Args:
        geometry (DataSocket): Geometry
        component (str): Node parameter, default = 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **point_count** : Integer
        - **edge_count** : Integer
        - **face_count** : Integer
        - **face_corner_count** : Integer
        - **spline_count** : Integer
        - **instance_count** : Integer

    .. blid:: GeometryNodeAttributeDomainSize

    """

    def __init__(self, geometry=None, component='MESH', label=None, node_color=None):

        super().__init__('GeometryNodeAttributeDomainSize', node_name='Domain Size', label=label, node_color=node_color)

        # Node parameters

        self.bnode.component       = component

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'point_count' : 0, 'edge_count' : 1, 'face_count' : 2, 'face_corner_count' : 3, 'spline_count' : 4, 'instance_count' : 5, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

    @property
    def component(self):
        return self.bnode.component

    @component.setter
    def component(self, value):
        self.bnode.component = value

    @property
    def point_count(self):
        return self.get_output_socket('point_count')

    @property
    def edge_count(self):
        return self.get_output_socket('edge_count')

    @property
    def face_count(self):
        return self.get_output_socket('face_count')

    @property
    def face_corner_count(self):
        return self.get_output_socket('face_corner_count')

    @property
    def spline_count(self):
        return self.get_output_socket('spline_count')

    @property
    def instance_count(self):
        return self.get_output_socket('instance_count')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'DomainSize': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node AttributeStatistic for GeometryNodeAttributeStatistic

class AttributeStatistic(Node):

    """Node *Attribute Statistic*

    .. _AttributeStatistic:

    Node implementation:
        Geometry:
            attribute_statistic 
        Domain:
            attribute_statistic attribute_mean attribute_median attribute_sum attribute_min attribute_max attribute_range attribute_std attribute_var 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        attribute (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mean** : ``data_type`` dependant
        - **median** : ``data_type`` dependant
        - **sum** : ``data_type`` dependant
        - **min** : ``data_type`` dependant
        - **max** : ``data_type`` dependant
        - **range** : ``data_type`` dependant
        - **standard_deviation** : ``data_type`` dependant
        - **variance** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')
        - Input sockets  : ['attribute']
        - Output sockets : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

    .. blid:: GeometryNodeAttributeStatistic

    """

    def __init__(self, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeAttributeStatistic', node_name='Attribute Statistic', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(attribute) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'attribute' : [2, 3], }
        self.outsockets = {'mean' : [0, 8], 'median' : [1, 9], 'sum' : [2, 10], 'min' : [3, 11], 'max' : [4, 12], 'range' : [5, 13], 'standard_deviation' : [6, 14], 'variance' : [7, 15], }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if attribute       is not None: self.attribute       = attribute

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def mean(self):
        return self.get_output_socket('mean')

    @property
    def median(self):
        return self.get_output_socket('median')

    @property
    def sum(self):
        return self.get_output_socket('sum')

    @property
    def min(self):
        return self.get_output_socket('min')

    @property
    def max(self):
        return self.get_output_socket('max')

    @property
    def range(self):
        return self.get_output_socket('range')

    @property
    def standard_deviation(self):
        return self.get_output_socket('standard_deviation')

    @property
    def variance(self):
        return self.get_output_socket('variance')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'AttributeStatistic': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'AttributeStatistic': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def attribute(self):
        raise AttributeError("Attribute error on node 'AttributeStatistic': the input socket 'attribute' is write only.")

    @attribute.setter
    def attribute(self, value):
        self.set_input_socket('attribute', value)

# ----------------------------------------------------------------------------------------------------
# Node BoundingBox for GeometryNodeBoundBox

class BoundingBox(Node):

    """Node *Bounding Box*

    .. _BoundingBox:

    Node implementation:
        Geometry:
            bounding_box bounding_box_min bounding_box_min 

    Args:
        geometry (DataSocket): Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **bounding_box** : Geometry
        - **min** : Vector
        - **max** : Vector

    .. blid:: GeometryNodeBoundBox

    """

    def __init__(self, geometry=None, label=None, node_color=None):

        super().__init__('GeometryNodeBoundBox', node_name='Bounding Box', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'bounding_box' : 0, 'min' : 1, 'max' : 2, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

    @property
    def bounding_box(self):
        return self.get_output_socket('bounding_box')

    @property
    def min(self):
        return self.get_output_socket('min')

    @property
    def max(self):
        return self.get_output_socket('max')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'BoundingBox': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node CaptureAttribute for GeometryNodeCaptureAttribute

class CaptureAttribute(Node):

    """Node *Capture Attribute*

    .. _CaptureAttribute:

    Node implementation:
        Geometry:
            capture_attribute capture_attribute_node 
        Domain:
            capture_attribute 

    Args:
        geometry (DataSocket): Geometry
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry
        - **attribute** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeCaptureAttribute

    """

    def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeCaptureAttribute', node_name='Capture Attribute', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'value' : [1, 2, 3, 4, 5], }
        self.outsockets = {'geometry' : 0, 'attribute' : [1, 2, 3, 4, 5], }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if value           is not None: self.value           = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @property
    def attribute(self):
        return self.get_output_socket('attribute')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def value(self):
        raise AttributeError("Attribute error on node 'CaptureAttribute': the input socket 'value' is write only.")

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

# ----------------------------------------------------------------------------------------------------
# Node CollectionInfo for GeometryNodeCollectionInfo

class CollectionInfo(Node):

    """Node *Collection Info*

    .. _CollectionInfo:

    Node implementation:
        Geometry:
            Collection 

    Args:
        collection (DataSocket): Collection
        separate_children (DataSocket): Boolean
        reset_children (DataSocket): Boolean
        transform_space (str): Node parameter, default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeCollectionInfo

    """

    def __init__(self, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None, node_color=None):

        super().__init__('GeometryNodeCollectionInfo', node_name='Collection Info', label=label, node_color=node_color)

        # Node parameters

        self.bnode.transform_space = transform_space

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'collection' : 0, 'separate_children' : 1, 'reset_children' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if collection      is not None: self.collection      = collection
        if separate_children is not None: self.separate_children = separate_children
        if reset_children  is not None: self.reset_children  = reset_children

    @property
    def transform_space(self):
        return self.bnode.transform_space

    @transform_space.setter
    def transform_space(self, value):
        self.bnode.transform_space = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @property
    def collection(self):
        raise AttributeError("Attribute error on node 'CollectionInfo': the input socket 'collection' is write only.")

    @collection.setter
    def collection(self, value):
        self.set_input_socket('collection', value)

    @property
    def separate_children(self):
        raise AttributeError("Attribute error on node 'CollectionInfo': the input socket 'separate_children' is write only.")

    @separate_children.setter
    def separate_children(self, value):
        self.set_input_socket('separate_children', value)

    @property
    def reset_children(self):
        raise AttributeError("Attribute error on node 'CollectionInfo': the input socket 'reset_children' is write only.")

    @reset_children.setter
    def reset_children(self, value):
        self.set_input_socket('reset_children', value)

# ----------------------------------------------------------------------------------------------------
# Node ConvexHull for GeometryNodeConvexHull

class ConvexHull(Node):

    """Node *Convex Hull*

    .. _ConvexHull:

    Node implementation:
        Geometry:
            convex_hull 

    Args:
        geometry (DataSocket): Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **convex_hull** : Geometry

    .. blid:: GeometryNodeConvexHull

    """

    def __init__(self, geometry=None, label=None, node_color=None):

        super().__init__('GeometryNodeConvexHull', node_name='Convex Hull', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'convex_hull' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

    @property
    def convex_hull(self):
        return self.get_output_socket('convex_hull')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'ConvexHull': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node CornersOfFace for GeometryNodeCornersOfFace

class CornersOfFace(Node):

    """Node *Corners of Face*

    .. _CornersOfFace:

    Node implementation:
        Mesh:
            corners_of_face 
        Face:
            corners corners_index corners_total 

    Args:
        face_index (DataSocket): Integer
        weights (DataSocket): Float
        sort_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **corner_index** : Integer
        - **total** : Integer

    .. blid:: GeometryNodeCornersOfFace

    """

    def __init__(self, face_index=None, weights=None, sort_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeCornersOfFace', node_name='Corners of Face', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'face_index' : 0, 'weights' : 1, 'sort_index' : 2, }
        self.outsockets = {'corner_index' : 0, 'total' : 1, }

        # Input sockets plugging

        if face_index      is not None: self.face_index      = face_index
        if weights         is not None: self.weights         = weights
        if sort_index      is not None: self.sort_index      = sort_index

    @property
    def corner_index(self):
        return self.get_output_socket('corner_index')

    @property
    def total(self):
        return self.get_output_socket('total')

    @property
    def face_index(self):
        raise AttributeError("Attribute error on node 'CornersOfFace': the input socket 'face_index' is write only.")

    @face_index.setter
    def face_index(self, value):
        self.set_input_socket('face_index', value)

    @property
    def weights(self):
        raise AttributeError("Attribute error on node 'CornersOfFace': the input socket 'weights' is write only.")

    @weights.setter
    def weights(self, value):
        self.set_input_socket('weights', value)

    @property
    def sort_index(self):
        raise AttributeError("Attribute error on node 'CornersOfFace': the input socket 'sort_index' is write only.")

    @sort_index.setter
    def sort_index(self, value):
        self.set_input_socket('sort_index', value)

# ----------------------------------------------------------------------------------------------------
# Node CornersOfVertex for GeometryNodeCornersOfVertex

class CornersOfVertex(Node):

    """Node *Corners of Vertex*

    .. _CornersOfVertex:

    Node implementation:
        Mesh:
            corners_of_vertex 
        Vertex:
            corners corners_index corners_total 

    Args:
        vertex_index (DataSocket): Integer
        weights (DataSocket): Float
        sort_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **corner_index** : Integer
        - **total** : Integer

    .. blid:: GeometryNodeCornersOfVertex

    """

    def __init__(self, vertex_index=None, weights=None, sort_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeCornersOfVertex', node_name='Corners of Vertex', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vertex_index' : 0, 'weights' : 1, 'sort_index' : 2, }
        self.outsockets = {'corner_index' : 0, 'total' : 1, }

        # Input sockets plugging

        if vertex_index    is not None: self.vertex_index    = vertex_index
        if weights         is not None: self.weights         = weights
        if sort_index      is not None: self.sort_index      = sort_index

    @property
    def corner_index(self):
        return self.get_output_socket('corner_index')

    @property
    def total(self):
        return self.get_output_socket('total')

    @property
    def vertex_index(self):
        raise AttributeError("Attribute error on node 'CornersOfVertex': the input socket 'vertex_index' is write only.")

    @vertex_index.setter
    def vertex_index(self, value):
        self.set_input_socket('vertex_index', value)

    @property
    def weights(self):
        raise AttributeError("Attribute error on node 'CornersOfVertex': the input socket 'weights' is write only.")

    @weights.setter
    def weights(self, value):
        self.set_input_socket('weights', value)

    @property
    def sort_index(self):
        raise AttributeError("Attribute error on node 'CornersOfVertex': the input socket 'sort_index' is write only.")

    @sort_index.setter
    def sort_index(self, value):
        self.set_input_socket('sort_index', value)

# ----------------------------------------------------------------------------------------------------
# Node Arc for GeometryNodeCurveArc

class Arc(Node):

    """Node *Arc*

    .. _Arc:

    Node implementation:
        Curve:
            Arc ArcFromPoints 

    Args:
        resolution (DataSocket): Integer
        start (DataSocket): Vector
        middle (DataSocket): Vector
        end (DataSocket): Vector
        radius (DataSocket): Float
        start_angle (DataSocket): Float
        sweep_angle (DataSocket): Float
        offset_angle (DataSocket): Float
        connect_center (DataSocket): Boolean
        invert_arc (DataSocket): Boolean
        mode (str): Node parameter, default = 'RADIUS' in ('POINTS', 'RADIUS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve
        - **center** : Vector
        - **normal** : Vector
        - **radius** : Float

    .. blid:: GeometryNodeCurveArc

    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None, node_color=None):

        super().__init__('GeometryNodeCurveArc', node_name='Arc', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'resolution' : 0, 'start' : 1, 'middle' : 2, 'end' : 3, 'radius' : 4, 'start_angle' : 5, 'sweep_angle' : 6, 'offset_angle' : 7, 'connect_center' : 8, 'invert_arc' : 9, }
        self.outsockets = {'curve' : 0, 'center' : 1, 'normal' : 2, 'radius' : 3, }

        # Input sockets plugging

        if resolution      is not None: self.resolution      = resolution
        if start           is not None: self.start           = start
        if middle          is not None: self.middle          = middle
        if end             is not None: self.end             = end
        if radius          is not None: self.radius          = radius
        if start_angle     is not None: self.start_angle     = start_angle
        if sweep_angle     is not None: self.sweep_angle     = sweep_angle
        if offset_angle    is not None: self.offset_angle    = offset_angle
        if connect_center  is not None: self.connect_center  = connect_center
        if invert_arc      is not None: self.invert_arc      = invert_arc

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def center(self):
        return self.get_output_socket('center')

    @property
    def normal(self):
        return self.get_output_socket('normal')

    @property
    def radius(self):
        return self.get_output_socket('radius')

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

    @property
    def start(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'start' is write only.")

    @start.setter
    def start(self, value):
        self.set_input_socket('start', value)

    @property
    def middle(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'middle' is write only.")

    @middle.setter
    def middle(self, value):
        self.set_input_socket('middle', value)

    @property
    def end(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'end' is write only.")

    @end.setter
    def end(self, value):
        self.set_input_socket('end', value)

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

    @property
    def start_angle(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'start_angle' is write only.")

    @start_angle.setter
    def start_angle(self, value):
        self.set_input_socket('start_angle', value)

    @property
    def sweep_angle(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'sweep_angle' is write only.")

    @sweep_angle.setter
    def sweep_angle(self, value):
        self.set_input_socket('sweep_angle', value)

    @property
    def offset_angle(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'offset_angle' is write only.")

    @offset_angle.setter
    def offset_angle(self, value):
        self.set_input_socket('offset_angle', value)

    @property
    def connect_center(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'connect_center' is write only.")

    @connect_center.setter
    def connect_center(self, value):
        self.set_input_socket('connect_center', value)

    @property
    def invert_arc(self):
        raise AttributeError("Attribute error on node 'Arc': the input socket 'invert_arc' is write only.")

    @invert_arc.setter
    def invert_arc(self, value):
        self.set_input_socket('invert_arc', value)

# ----------------------------------------------------------------------------------------------------
# Node EndpointSelection for GeometryNodeCurveEndpointSelection

class EndpointSelection(Node):

    """Node *Endpoint Selection*

    .. _EndpointSelection:

    Node implementation:
        ControlPoint:
            endpoint_selection 

    Args:
        start_size (DataSocket): Integer
        end_size (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **selection** : Boolean

    .. blid:: GeometryNodeCurveEndpointSelection

    """

    def __init__(self, start_size=None, end_size=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveEndpointSelection', node_name='Endpoint Selection', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'start_size' : 0, 'end_size' : 1, }
        self.outsockets = {'selection' : 0, }

        # Input sockets plugging

        if start_size      is not None: self.start_size      = start_size
        if end_size        is not None: self.end_size        = end_size

    @property
    def selection(self):
        return self.get_output_socket('selection')

    @property
    def start_size(self):
        raise AttributeError("Attribute error on node 'EndpointSelection': the input socket 'start_size' is write only.")

    @start_size.setter
    def start_size(self, value):
        self.set_input_socket('start_size', value)

    @property
    def end_size(self):
        raise AttributeError("Attribute error on node 'EndpointSelection': the input socket 'end_size' is write only.")

    @end_size.setter
    def end_size(self, value):
        self.set_input_socket('end_size', value)

# ----------------------------------------------------------------------------------------------------
# Node HandleTypeSelection for GeometryNodeCurveHandleTypeSelection

class HandleTypeSelection(Node):

    """Node *Handle Type Selection*

    .. _HandleTypeSelection:

    Node implementation:
        ControlPoint:
            handle_type_selection_node handle_type_selection handle_type_selection handle_type_selection handle_type_selection handle_type_selection 

    Args:
        handle_type (str): Node parameter, default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        mode (set): Node parameter, default = {'LEFT', 'RIGHT'}
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **selection** : Boolean

    .. blid:: GeometryNodeCurveHandleTypeSelection

    """

    def __init__(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None):

        super().__init__('GeometryNodeCurveHandleTypeSelection', node_name='Handle Type Selection', label=label, node_color=node_color)

        # Node parameters

        self.bnode.handle_type     = handle_type
        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'selection' : 0, }

    @property
    def handle_type(self):
        return self.bnode.handle_type

    @handle_type.setter
    def handle_type(self, value):
        self.bnode.handle_type = value

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def selection(self):
        return self.get_output_socket('selection')

# ----------------------------------------------------------------------------------------------------
# Node CurveLength for GeometryNodeCurveLength

class CurveLength(Node):

    """Node *Curve Length*

    .. _CurveLength:

    Node implementation:
        Curve:
            length 

    Args:
        curve (DataSocket): Curve
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **length** : Float

    .. blid:: GeometryNodeCurveLength

    """

    def __init__(self, curve=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveLength', node_name='Curve Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, }
        self.outsockets = {'length' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve

    @property
    def length(self):
        return self.get_output_socket('length')

    @property
    def curve(self):
        raise AttributeError("Attribute error on node 'CurveLength': the input socket 'curve' is write only.")

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveOfPoint for GeometryNodeCurveOfPoint

class CurveOfPoint(Node):

    """Node *Curve of Point*

    .. _CurveOfPoint:

    Node implementation:
        Curve:
            curve_of_point 
        ControlPoint:
            curve 

    Args:
        point_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve_index** : Integer
        - **index_in_curve** : Integer

    .. blid:: GeometryNodeCurveOfPoint

    """

    def __init__(self, point_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveOfPoint', node_name='Curve of Point', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'point_index' : 0, }
        self.outsockets = {'curve_index' : 0, 'index_in_curve' : 1, }

        # Input sockets plugging

        if point_index     is not None: self.point_index     = point_index

    @property
    def curve_index(self):
        return self.get_output_socket('curve_index')

    @property
    def index_in_curve(self):
        return self.get_output_socket('index_in_curve')

    @property
    def point_index(self):
        raise AttributeError("Attribute error on node 'CurveOfPoint': the input socket 'point_index' is write only.")

    @point_index.setter
    def point_index(self, value):
        self.set_input_socket('point_index', value)

# ----------------------------------------------------------------------------------------------------
# Node BezierSegment for GeometryNodeCurvePrimitiveBezierSegment

class BezierSegment(Node):

    """Node *Bezier Segment*

    .. _BezierSegment:

    Node implementation:
        Curve:
            bezier_segment 

    Args:
        resolution (DataSocket): Integer
        start (DataSocket): Vector
        start_handle (DataSocket): Vector
        end_handle (DataSocket): Vector
        end (DataSocket): Vector
        mode (str): Node parameter, default = 'POSITION' in ('POSITION', 'OFFSET')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurvePrimitiveBezierSegment

    """

    def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveBezierSegment', node_name='Bezier Segment', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'resolution' : 0, 'start' : 1, 'start_handle' : 2, 'end_handle' : 3, 'end' : 4, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if resolution      is not None: self.resolution      = resolution
        if start           is not None: self.start           = start
        if start_handle    is not None: self.start_handle    = start_handle
        if end_handle      is not None: self.end_handle      = end_handle
        if end             is not None: self.end             = end

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'BezierSegment': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

    @property
    def start(self):
        raise AttributeError("Attribute error on node 'BezierSegment': the input socket 'start' is write only.")

    @start.setter
    def start(self, value):
        self.set_input_socket('start', value)

    @property
    def start_handle(self):
        raise AttributeError("Attribute error on node 'BezierSegment': the input socket 'start_handle' is write only.")

    @start_handle.setter
    def start_handle(self, value):
        self.set_input_socket('start_handle', value)

    @property
    def end_handle(self):
        raise AttributeError("Attribute error on node 'BezierSegment': the input socket 'end_handle' is write only.")

    @end_handle.setter
    def end_handle(self, value):
        self.set_input_socket('end_handle', value)

    @property
    def end(self):
        raise AttributeError("Attribute error on node 'BezierSegment': the input socket 'end' is write only.")

    @end.setter
    def end(self, value):
        self.set_input_socket('end', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveCircle for GeometryNodeCurvePrimitiveCircle

class CurveCircle(Node):

    """Node *Curve Circle*

    .. _CurveCircle:

    Node implementation:
        Curve:
            Circle CircleFromPoints 

    Args:
        resolution (DataSocket): Integer
        point_1 (DataSocket): Vector
        point_2 (DataSocket): Vector
        point_3 (DataSocket): Vector
        radius (DataSocket): Float
        mode (str): Node parameter, default = 'RADIUS' in ('POINTS', 'RADIUS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve
        - **center** : Vector

    .. blid:: GeometryNodeCurvePrimitiveCircle

    """

    def __init__(self, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveCircle', node_name='Curve Circle', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'resolution' : 0, 'point_1' : 1, 'point_2' : 2, 'point_3' : 3, 'radius' : 4, }
        self.outsockets = {'curve' : 0, 'center' : 1, }

        # Input sockets plugging

        if resolution      is not None: self.resolution      = resolution
        if point_1         is not None: self.point_1         = point_1
        if point_2         is not None: self.point_2         = point_2
        if point_3         is not None: self.point_3         = point_3
        if radius          is not None: self.radius          = radius

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def center(self):
        return self.get_output_socket('center')

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'CurveCircle': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

    @property
    def point_1(self):
        raise AttributeError("Attribute error on node 'CurveCircle': the input socket 'point_1' is write only.")

    @point_1.setter
    def point_1(self, value):
        self.set_input_socket('point_1', value)

    @property
    def point_2(self):
        raise AttributeError("Attribute error on node 'CurveCircle': the input socket 'point_2' is write only.")

    @point_2.setter
    def point_2(self, value):
        self.set_input_socket('point_2', value)

    @property
    def point_3(self):
        raise AttributeError("Attribute error on node 'CurveCircle': the input socket 'point_3' is write only.")

    @point_3.setter
    def point_3(self, value):
        self.set_input_socket('point_3', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'CurveCircle': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveLine for GeometryNodeCurvePrimitiveLine

class CurveLine(Node):

    """Node *Curve Line*

    .. _CurveLine:

    Node implementation:
        Curve:
            Line LineDirection 

    Args:
        start (DataSocket): Vector
        end (DataSocket): Vector
        direction (DataSocket): Vector
        length (DataSocket): Float
        mode (str): Node parameter, default = 'POINTS' in ('POINTS', 'DIRECTION')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurvePrimitiveLine

    """

    def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveLine', node_name='Curve Line', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'start' : 0, 'end' : 1, 'direction' : 2, 'length' : 3, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if start           is not None: self.start           = start
        if end             is not None: self.end             = end
        if direction       is not None: self.direction       = direction
        if length          is not None: self.length          = length

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def start(self):
        raise AttributeError("Attribute error on node 'CurveLine': the input socket 'start' is write only.")

    @start.setter
    def start(self, value):
        self.set_input_socket('start', value)

    @property
    def end(self):
        raise AttributeError("Attribute error on node 'CurveLine': the input socket 'end' is write only.")

    @end.setter
    def end(self, value):
        self.set_input_socket('end', value)

    @property
    def direction(self):
        raise AttributeError("Attribute error on node 'CurveLine': the input socket 'direction' is write only.")

    @direction.setter
    def direction(self, value):
        self.set_input_socket('direction', value)

    @property
    def length(self):
        raise AttributeError("Attribute error on node 'CurveLine': the input socket 'length' is write only.")

    @length.setter
    def length(self, value):
        self.set_input_socket('length', value)

# ----------------------------------------------------------------------------------------------------
# Node Quadrilateral for GeometryNodeCurvePrimitiveQuadrilateral

class Quadrilateral(Node):

    """Node *Quadrilateral*

    .. _Quadrilateral:

    Node implementation:
        Curve:
            Quadrilateral 

    Args:
        width (DataSocket): Float
        height (DataSocket): Float
        bottom_width (DataSocket): Float
        top_width (DataSocket): Float
        offset (DataSocket): Float
        bottom_height (DataSocket): Float
        top_height (DataSocket): Float
        point_1 (DataSocket): Vector
        point_2 (DataSocket): Vector
        point_3 (DataSocket): Vector
        point_4 (DataSocket): Vector
        mode (str): Node parameter, default = 'RECTANGLE' in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurvePrimitiveQuadrilateral

    """

    def __init__(self, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveQuadrilateral', node_name='Quadrilateral', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'width' : 0, 'height' : 1, 'bottom_width' : 2, 'top_width' : 3, 'offset' : 4, 'bottom_height' : 5, 'top_height' : 6, 'point_1' : 7, 'point_2' : 8, 'point_3' : 9, 'point_4' : 10, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if width           is not None: self.width           = width
        if height          is not None: self.height          = height
        if bottom_width    is not None: self.bottom_width    = bottom_width
        if top_width       is not None: self.top_width       = top_width
        if offset          is not None: self.offset          = offset
        if bottom_height   is not None: self.bottom_height   = bottom_height
        if top_height      is not None: self.top_height      = top_height
        if point_1         is not None: self.point_1         = point_1
        if point_2         is not None: self.point_2         = point_2
        if point_3         is not None: self.point_3         = point_3
        if point_4         is not None: self.point_4         = point_4

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def width(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'width' is write only.")

    @width.setter
    def width(self, value):
        self.set_input_socket('width', value)

    @property
    def height(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'height' is write only.")

    @height.setter
    def height(self, value):
        self.set_input_socket('height', value)

    @property
    def bottom_width(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'bottom_width' is write only.")

    @bottom_width.setter
    def bottom_width(self, value):
        self.set_input_socket('bottom_width', value)

    @property
    def top_width(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'top_width' is write only.")

    @top_width.setter
    def top_width(self, value):
        self.set_input_socket('top_width', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

    @property
    def bottom_height(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'bottom_height' is write only.")

    @bottom_height.setter
    def bottom_height(self, value):
        self.set_input_socket('bottom_height', value)

    @property
    def top_height(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'top_height' is write only.")

    @top_height.setter
    def top_height(self, value):
        self.set_input_socket('top_height', value)

    @property
    def point_1(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'point_1' is write only.")

    @point_1.setter
    def point_1(self, value):
        self.set_input_socket('point_1', value)

    @property
    def point_2(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'point_2' is write only.")

    @point_2.setter
    def point_2(self, value):
        self.set_input_socket('point_2', value)

    @property
    def point_3(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'point_3' is write only.")

    @point_3.setter
    def point_3(self, value):
        self.set_input_socket('point_3', value)

    @property
    def point_4(self):
        raise AttributeError("Attribute error on node 'Quadrilateral': the input socket 'point_4' is write only.")

    @point_4.setter
    def point_4(self, value):
        self.set_input_socket('point_4', value)

# ----------------------------------------------------------------------------------------------------
# Node QuadraticBezier for GeometryNodeCurveQuadraticBezier

class QuadraticBezier(Node):

    """Node *Quadratic Bezier*

    .. _QuadraticBezier:

    Node implementation:
        Curve:
            QuadraticBezier 

    Args:
        resolution (DataSocket): Integer
        start (DataSocket): Vector
        middle (DataSocket): Vector
        end (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurveQuadraticBezier

    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveQuadraticBezier', node_name='Quadratic Bezier', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'resolution' : 0, 'start' : 1, 'middle' : 2, 'end' : 3, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if resolution      is not None: self.resolution      = resolution
        if start           is not None: self.start           = start
        if middle          is not None: self.middle          = middle
        if end             is not None: self.end             = end

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'QuadraticBezier': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

    @property
    def start(self):
        raise AttributeError("Attribute error on node 'QuadraticBezier': the input socket 'start' is write only.")

    @start.setter
    def start(self, value):
        self.set_input_socket('start', value)

    @property
    def middle(self):
        raise AttributeError("Attribute error on node 'QuadraticBezier': the input socket 'middle' is write only.")

    @middle.setter
    def middle(self, value):
        self.set_input_socket('middle', value)

    @property
    def end(self):
        raise AttributeError("Attribute error on node 'QuadraticBezier': the input socket 'end' is write only.")

    @end.setter
    def end(self, value):
        self.set_input_socket('end', value)

# ----------------------------------------------------------------------------------------------------
# Node SetHandleType for GeometryNodeCurveSetHandles

class SetHandleType(Node):

    """Node *Set Handle Type*

    .. _SetHandleType:

    Node implementation:
        ControlPoint:
            set_handle_type_node set_handle_type 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        handle_type (str): Node parameter, default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        mode (set): Node parameter, default = {'LEFT', 'RIGHT'}
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurveSetHandles

    """

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None):

        super().__init__('GeometryNodeCurveSetHandles', node_name='Set Handle Type', label=label, node_color=node_color)

        # Node parameters

        self.bnode.handle_type     = handle_type
        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection

    @property
    def handle_type(self):
        return self.bnode.handle_type

    @handle_type.setter
    def handle_type(self, value):
        self.bnode.handle_type = value

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetHandleType': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node Spiral for GeometryNodeCurveSpiral

class Spiral(Node):

    """Node *Spiral*

    .. _Spiral:

    Node implementation:
        Curve:
            Spiral 

    Args:
        resolution (DataSocket): Integer
        rotations (DataSocket): Float
        start_radius (DataSocket): Float
        end_radius (DataSocket): Float
        height (DataSocket): Float
        reverse (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurveSpiral

    """

    def __init__(self, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveSpiral', node_name='Spiral', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'resolution' : 0, 'rotations' : 1, 'start_radius' : 2, 'end_radius' : 3, 'height' : 4, 'reverse' : 5, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if resolution      is not None: self.resolution      = resolution
        if rotations       is not None: self.rotations       = rotations
        if start_radius    is not None: self.start_radius    = start_radius
        if end_radius      is not None: self.end_radius      = end_radius
        if height          is not None: self.height          = height
        if reverse         is not None: self.reverse         = reverse

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'Spiral': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

    @property
    def rotations(self):
        raise AttributeError("Attribute error on node 'Spiral': the input socket 'rotations' is write only.")

    @rotations.setter
    def rotations(self, value):
        self.set_input_socket('rotations', value)

    @property
    def start_radius(self):
        raise AttributeError("Attribute error on node 'Spiral': the input socket 'start_radius' is write only.")

    @start_radius.setter
    def start_radius(self, value):
        self.set_input_socket('start_radius', value)

    @property
    def end_radius(self):
        raise AttributeError("Attribute error on node 'Spiral': the input socket 'end_radius' is write only.")

    @end_radius.setter
    def end_radius(self, value):
        self.set_input_socket('end_radius', value)

    @property
    def height(self):
        raise AttributeError("Attribute error on node 'Spiral': the input socket 'height' is write only.")

    @height.setter
    def height(self, value):
        self.set_input_socket('height', value)

    @property
    def reverse(self):
        raise AttributeError("Attribute error on node 'Spiral': the input socket 'reverse' is write only.")

    @reverse.setter
    def reverse(self, value):
        self.set_input_socket('reverse', value)

# ----------------------------------------------------------------------------------------------------
# Node SetSplineType for GeometryNodeCurveSplineType

class SetSplineType(Node):

    """Node *Set Spline Type*

    .. _SetSplineType:

    Node implementation:
        Spline:
            set_type type type 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        spline_type (str): Node parameter, default = 'POLY' in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeCurveSplineType

    """

    def __init__(self, curve=None, selection=None, spline_type='POLY', label=None, node_color=None):

        super().__init__('GeometryNodeCurveSplineType', node_name='Set Spline Type', label=label, node_color=node_color)

        # Node parameters

        self.bnode.spline_type     = spline_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection

    @property
    def spline_type(self):
        return self.bnode.spline_type

    @spline_type.setter
    def spline_type(self, value):
        self.bnode.spline_type = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetSplineType': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node Star for GeometryNodeCurveStar

class Star(Node):

    """Node *Star*

    .. _Star:

    Node implementation:
        Curve:
            Star 

    Args:
        points (DataSocket): Integer
        inner_radius (DataSocket): Float
        outer_radius (DataSocket): Float
        twist (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve
        - **outer_points** : Boolean

    .. blid:: GeometryNodeCurveStar

    """

    def __init__(self, points=None, inner_radius=None, outer_radius=None, twist=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveStar', node_name='Star', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'inner_radius' : 1, 'outer_radius' : 2, 'twist' : 3, }
        self.outsockets = {'curve' : 0, 'outer_points' : 1, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if inner_radius    is not None: self.inner_radius    = inner_radius
        if outer_radius    is not None: self.outer_radius    = outer_radius
        if twist           is not None: self.twist           = twist

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def outer_points(self):
        return self.get_output_socket('outer_points')

    @property
    def points(self):
        raise AttributeError("Attribute error on node 'Star': the input socket 'points' is write only.")

    @points.setter
    def points(self, value):
        self.set_input_socket('points', value)

    @property
    def inner_radius(self):
        raise AttributeError("Attribute error on node 'Star': the input socket 'inner_radius' is write only.")

    @inner_radius.setter
    def inner_radius(self, value):
        self.set_input_socket('inner_radius', value)

    @property
    def outer_radius(self):
        raise AttributeError("Attribute error on node 'Star': the input socket 'outer_radius' is write only.")

    @outer_radius.setter
    def outer_radius(self, value):
        self.set_input_socket('outer_radius', value)

    @property
    def twist(self):
        raise AttributeError("Attribute error on node 'Star': the input socket 'twist' is write only.")

    @twist.setter
    def twist(self, value):
        self.set_input_socket('twist', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveToMesh for GeometryNodeCurveToMesh

class CurveToMesh(Node):

    """Node *Curve to Mesh*

    .. _CurveToMesh:

    Node implementation:
        Curve:
            to_mesh 

    Args:
        curve (DataSocket): Curve
        profile_curve (DataSocket): Geometry
        fill_caps (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeCurveToMesh

    """

    def __init__(self, curve=None, profile_curve=None, fill_caps=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveToMesh', node_name='Curve to Mesh', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'profile_curve' : 1, 'fill_caps' : 2, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if profile_curve   is not None: self.profile_curve   = profile_curve
        if fill_caps       is not None: self.fill_caps       = fill_caps

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def curve(self):
        raise AttributeError("Attribute error on node 'CurveToMesh': the input socket 'curve' is write only.")

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def profile_curve(self):
        raise AttributeError("Attribute error on node 'CurveToMesh': the input socket 'profile_curve' is write only.")

    @profile_curve.setter
    def profile_curve(self, value):
        self.set_input_socket('profile_curve', value)

    @property
    def fill_caps(self):
        raise AttributeError("Attribute error on node 'CurveToMesh': the input socket 'fill_caps' is write only.")

    @fill_caps.setter
    def fill_caps(self, value):
        self.set_input_socket('fill_caps', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveToPoints for GeometryNodeCurveToPoints

class CurveToPoints(Node):

    """Node *Curve to Points*

    .. _CurveToPoints:

    Node implementation:
        Curve:
            to_points to_points_count to_points_length to_points_evaluated 

    Args:
        curve (DataSocket): Curve
        count (DataSocket): Integer
        length (DataSocket): Float
        mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **points** : Points
        - **tangent** : Vector
        - **normal** : Vector
        - **rotation** : Vector

    .. blid:: GeometryNodeCurveToPoints

    """

    def __init__(self, curve=None, count=None, length=None, mode='COUNT', label=None, node_color=None):

        super().__init__('GeometryNodeCurveToPoints', node_name='Curve to Points', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'count' : 1, 'length' : 2, }
        self.outsockets = {'points' : 0, 'tangent' : 1, 'normal' : 2, 'rotation' : 3, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if count           is not None: self.count           = count
        if length          is not None: self.length          = length

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def points(self):
        return self.get_output_socket('points')

    @property
    def tangent(self):
        return self.get_output_socket('tangent')

    @property
    def normal(self):
        return self.get_output_socket('normal')

    @property
    def rotation(self):
        return self.get_output_socket('rotation')

    @property
    def curve(self):
        raise AttributeError("Attribute error on node 'CurveToPoints': the input socket 'curve' is write only.")

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def count(self):
        raise AttributeError("Attribute error on node 'CurveToPoints': the input socket 'count' is write only.")

    @count.setter
    def count(self, value):
        self.set_input_socket('count', value)

    @property
    def length(self):
        raise AttributeError("Attribute error on node 'CurveToPoints': the input socket 'length' is write only.")

    @length.setter
    def length(self, value):
        self.set_input_socket('length', value)

# ----------------------------------------------------------------------------------------------------
# Node DeformCurvesOnSurface for GeometryNodeDeformCurvesOnSurface

class DeformCurvesOnSurface(Node):

    """Node *Deform Curves on Surface*

    .. _DeformCurvesOnSurface:

    Node implementation:
        Curve:
            deform_on_surface 

    Args:
        curves (DataSocket): Curve
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curves** : Curve

    .. blid:: GeometryNodeDeformCurvesOnSurface

    """

    def __init__(self, curves=None, label=None, node_color=None):

        super().__init__('GeometryNodeDeformCurvesOnSurface', node_name='Deform Curves on Surface', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curves' : 0, }
        self.outsockets = {'curves' : 0, }

        # Input sockets plugging

        if curves          is not None: self.curves          = curves

    @property
    def curves(self):
        return self.get_output_socket('curves')

    @curves.setter
    def curves(self, value):
        self.set_input_socket('curves', value)

# ----------------------------------------------------------------------------------------------------
# Node DeleteGeometry for GeometryNodeDeleteGeometry

class DeleteGeometry(Node):

    """Node *Delete Geometry*

    .. _DeleteGeometry:

    Node implementation:
        Geometry:
            delete 
        Mesh:
            delete_all delete_edges delete_faces 
        ('Vertex', 'Edge', 'Face', 'Spline', 'ControlPoint', 'Instance', 'CloudPoint'):
            delete 
        Vertex:
            delete_all delete_edges delete_faces 
        Edge:
            delete_all delete_edges delete_faces 
        Face:
            delete_all delete_edges delete_faces 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
        mode (str): Node parameter, default = 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeDeleteGeometry

    """

    def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL', label=None, node_color=None):

        super().__init__('GeometryNodeDeleteGeometry', node_name='Delete Geometry', label=label, node_color=node_color)

        # Node parameters

        self.bnode.domain          = domain
        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'DeleteGeometry': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node DistributePointsInVolume for GeometryNodeDistributePointsInVolume

class DistributePointsInVolume(Node):

    """Node *Distribute Points in Volume*

    .. _DistributePointsInVolume:

    Node implementation:
        Volume:
            distribute_points distribute_points_random distribute_points_grid 

    Args:
        volume (DataSocket): Volume
        density (DataSocket): Float
        seed (DataSocket): Integer
        spacing (DataSocket): Vector
        threshold (DataSocket): Float
        mode (str): Node parameter, default = 'DENSITY_RANDOM' in ('DENSITY_RANDOM', 'DENSITY_GRID')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **points** : Points

    .. blid:: GeometryNodeDistributePointsInVolume

    """

    def __init__(self, volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', label=None, node_color=None):

        super().__init__('GeometryNodeDistributePointsInVolume', node_name='Distribute Points in Volume', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'volume' : 0, 'density' : 1, 'seed' : 2, 'spacing' : 3, 'threshold' : 4, }
        self.outsockets = {'points' : 0, }

        # Input sockets plugging

        if volume          is not None: self.volume          = volume
        if density         is not None: self.density         = density
        if seed            is not None: self.seed            = seed
        if spacing         is not None: self.spacing         = spacing
        if threshold       is not None: self.threshold       = threshold

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def points(self):
        return self.get_output_socket('points')

    @property
    def volume(self):
        raise AttributeError("Attribute error on node 'DistributePointsInVolume': the input socket 'volume' is write only.")

    @volume.setter
    def volume(self, value):
        self.set_input_socket('volume', value)

    @property
    def density(self):
        raise AttributeError("Attribute error on node 'DistributePointsInVolume': the input socket 'density' is write only.")

    @density.setter
    def density(self, value):
        self.set_input_socket('density', value)

    @property
    def seed(self):
        raise AttributeError("Attribute error on node 'DistributePointsInVolume': the input socket 'seed' is write only.")

    @seed.setter
    def seed(self, value):
        self.set_input_socket('seed', value)

    @property
    def spacing(self):
        raise AttributeError("Attribute error on node 'DistributePointsInVolume': the input socket 'spacing' is write only.")

    @spacing.setter
    def spacing(self, value):
        self.set_input_socket('spacing', value)

    @property
    def threshold(self):
        raise AttributeError("Attribute error on node 'DistributePointsInVolume': the input socket 'threshold' is write only.")

    @threshold.setter
    def threshold(self, value):
        self.set_input_socket('threshold', value)

# ----------------------------------------------------------------------------------------------------
# Node DistributePointsOnFaces for GeometryNodeDistributePointsOnFaces

class DistributePointsOnFaces(Node):

    """Node *Distribute Points on Faces*

    .. _DistributePointsOnFaces:

    Node implementation:
        Mesh:
            distribute_points_on_faces 
        Face:
            distribute_points_random distribute_points_poisson 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        distance_min (DataSocket): Float
        density_max (DataSocket): Float
        density (DataSocket): Float
        density_factor (DataSocket): Float
        seed (DataSocket): Integer
        distribute_method (str): Node parameter, default = 'RANDOM' in ('RANDOM', 'POISSON')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **points** : Points
        - **normal** : Vector
        - **rotation** : Vector

    .. blid:: GeometryNodeDistributePointsOnFaces

    """

    def __init__(self, mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None):

        super().__init__('GeometryNodeDistributePointsOnFaces', node_name='Distribute Points on Faces', label=label, node_color=node_color)

        # Node parameters

        self.bnode.distribute_method = distribute_method

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, 'distance_min' : 2, 'density_max' : 3, 'density' : 4, 'density_factor' : 5, 'seed' : 6, }
        self.outsockets = {'points' : 0, 'normal' : 1, 'rotation' : 2, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection
        if distance_min    is not None: self.distance_min    = distance_min
        if density_max     is not None: self.density_max     = density_max
        if density         is not None: self.density         = density
        if density_factor  is not None: self.density_factor  = density_factor
        if seed            is not None: self.seed            = seed

    @property
    def distribute_method(self):
        return self.bnode.distribute_method

    @distribute_method.setter
    def distribute_method(self, value):
        self.bnode.distribute_method = value

    @property
    def points(self):
        return self.get_output_socket('points')

    @property
    def normal(self):
        return self.get_output_socket('normal')

    @property
    def rotation(self):
        return self.get_output_socket('rotation')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def distance_min(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'distance_min' is write only.")

    @distance_min.setter
    def distance_min(self, value):
        self.set_input_socket('distance_min', value)

    @property
    def density_max(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'density_max' is write only.")

    @density_max.setter
    def density_max(self, value):
        self.set_input_socket('density_max', value)

    @property
    def density(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'density' is write only.")

    @density.setter
    def density(self, value):
        self.set_input_socket('density', value)

    @property
    def density_factor(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'density_factor' is write only.")

    @density_factor.setter
    def density_factor(self, value):
        self.set_input_socket('density_factor', value)

    @property
    def seed(self):
        raise AttributeError("Attribute error on node 'DistributePointsOnFaces': the input socket 'seed' is write only.")

    @seed.setter
    def seed(self, value):
        self.set_input_socket('seed', value)

# ----------------------------------------------------------------------------------------------------
# Node DualMesh for GeometryNodeDualMesh

class DualMesh(Node):

    """Node *Dual Mesh*

    .. _DualMesh:

    Node implementation:
        Mesh:
            dual_mesh 

    Args:
        mesh (DataSocket): Mesh
        keep_boundaries (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **dual_mesh** : Geometry

    .. blid:: GeometryNodeDualMesh

    """

    def __init__(self, mesh=None, keep_boundaries=None, label=None, node_color=None):

        super().__init__('GeometryNodeDualMesh', node_name='Dual Mesh', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'keep_boundaries' : 1, }
        self.outsockets = {'dual_mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if keep_boundaries is not None: self.keep_boundaries = keep_boundaries

    @property
    def dual_mesh(self):
        return self.get_output_socket('dual_mesh')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'DualMesh': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def keep_boundaries(self):
        raise AttributeError("Attribute error on node 'DualMesh': the input socket 'keep_boundaries' is write only.")

    @keep_boundaries.setter
    def keep_boundaries(self, value):
        self.set_input_socket('keep_boundaries', value)

# ----------------------------------------------------------------------------------------------------
# Node DuplicateElements for GeometryNodeDuplicateElements

class DuplicateElements(Node):

    """Node *Duplicate Elements*

    .. _DuplicateElements:

    Node implementation:
        Geometry:
            duplicate 
        ('Vertex', 'ControlPoint', 'CloudPoint', 'Edge', 'Face', 'Instance'):
            duplicate 
        Spline:
            duplicate 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        amount (DataSocket): Integer
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry
        - **duplicate_index** : Integer

    .. blid:: GeometryNodeDuplicateElements

    """

    def __init__(self, geometry=None, selection=None, amount=None, domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeDuplicateElements', node_name='Duplicate Elements', label=label, node_color=node_color)

        # Node parameters

        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'amount' : 2, }
        self.outsockets = {'geometry' : 0, 'duplicate_index' : 1, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if amount          is not None: self.amount          = amount

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @property
    def duplicate_index(self):
        return self.get_output_socket('duplicate_index')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'DuplicateElements': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def amount(self):
        raise AttributeError("Attribute error on node 'DuplicateElements': the input socket 'amount' is write only.")

    @amount.setter
    def amount(self, value):
        self.set_input_socket('amount', value)

# ----------------------------------------------------------------------------------------------------
# Node EdgePathsToCurves for GeometryNodeEdgePathsToCurves

class EdgePathsToCurves(Node):

    """Node *Edge Paths to Curves*

    .. _EdgePathsToCurves:

    Node implementation:
        Mesh:
            edge_paths_to_curves 
        Edge:
            edge_paths_to_curves 

    Args:
        mesh (DataSocket): Mesh
        start_vertices (DataSocket): Boolean
        next_vertex_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curves** : Curve

    .. blid:: GeometryNodeEdgePathsToCurves

    """

    def __init__(self, mesh=None, start_vertices=None, next_vertex_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeEdgePathsToCurves', node_name='Edge Paths to Curves', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'start_vertices' : 1, 'next_vertex_index' : 2, }
        self.outsockets = {'curves' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if start_vertices  is not None: self.start_vertices  = start_vertices
        if next_vertex_index is not None: self.next_vertex_index = next_vertex_index

    @property
    def curves(self):
        return self.get_output_socket('curves')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'EdgePathsToCurves': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def start_vertices(self):
        raise AttributeError("Attribute error on node 'EdgePathsToCurves': the input socket 'start_vertices' is write only.")

    @start_vertices.setter
    def start_vertices(self, value):
        self.set_input_socket('start_vertices', value)

    @property
    def next_vertex_index(self):
        raise AttributeError("Attribute error on node 'EdgePathsToCurves': the input socket 'next_vertex_index' is write only.")

    @next_vertex_index.setter
    def next_vertex_index(self, value):
        self.set_input_socket('next_vertex_index', value)

# ----------------------------------------------------------------------------------------------------
# Node EdgePathsToSelection for GeometryNodeEdgePathsToSelection

class EdgePathsToSelection(Node):

    """Node *Edge Paths to Selection*

    .. _EdgePathsToSelection:

    Node implementation:
        Mesh:
            edge_paths_to_selection 

    Args:
        start_vertices (DataSocket): Boolean
        next_vertex_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **selection** : Boolean

    .. blid:: GeometryNodeEdgePathsToSelection

    """

    def __init__(self, start_vertices=None, next_vertex_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeEdgePathsToSelection', node_name='Edge Paths to Selection', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'start_vertices' : 0, 'next_vertex_index' : 1, }
        self.outsockets = {'selection' : 0, }

        # Input sockets plugging

        if start_vertices  is not None: self.start_vertices  = start_vertices
        if next_vertex_index is not None: self.next_vertex_index = next_vertex_index

    @property
    def selection(self):
        return self.get_output_socket('selection')

    @property
    def start_vertices(self):
        raise AttributeError("Attribute error on node 'EdgePathsToSelection': the input socket 'start_vertices' is write only.")

    @start_vertices.setter
    def start_vertices(self, value):
        self.set_input_socket('start_vertices', value)

    @property
    def next_vertex_index(self):
        raise AttributeError("Attribute error on node 'EdgePathsToSelection': the input socket 'next_vertex_index' is write only.")

    @next_vertex_index.setter
    def next_vertex_index(self, value):
        self.set_input_socket('next_vertex_index', value)

# ----------------------------------------------------------------------------------------------------
# Node EdgesOfCorner for GeometryNodeEdgesOfCorner

class EdgesOfCorner(Node):

    """Node *Edges of Corner*

    .. _EdgesOfCorner:

    Node implementation:
        Mesh:
            edges_of_corner 
        Corner:
            edges previous_vertex next_vertex 

    Args:
        corner_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **next_edge_index** : Integer
        - **previous_edge_index** : Integer

    .. blid:: GeometryNodeEdgesOfCorner

    """

    def __init__(self, corner_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeEdgesOfCorner', node_name='Edges of Corner', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'corner_index' : 0, }
        self.outsockets = {'next_edge_index' : 0, 'previous_edge_index' : 1, }

        # Input sockets plugging

        if corner_index    is not None: self.corner_index    = corner_index

    @property
    def next_edge_index(self):
        return self.get_output_socket('next_edge_index')

    @property
    def previous_edge_index(self):
        return self.get_output_socket('previous_edge_index')

    @property
    def corner_index(self):
        raise AttributeError("Attribute error on node 'EdgesOfCorner': the input socket 'corner_index' is write only.")

    @corner_index.setter
    def corner_index(self, value):
        self.set_input_socket('corner_index', value)

# ----------------------------------------------------------------------------------------------------
# Node EdgesOfVertex for GeometryNodeEdgesOfVertex

class EdgesOfVertex(Node):

    """Node *Edges of Vertex*

    .. _EdgesOfVertex:

    Node implementation:
        Mesh:
            edges_of_vertex 
        Vertex:
            edges edges_index edges_total 

    Args:
        vertex_index (DataSocket): Integer
        weights (DataSocket): Float
        sort_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **edge_index** : Integer
        - **total** : Integer

    .. blid:: GeometryNodeEdgesOfVertex

    """

    def __init__(self, vertex_index=None, weights=None, sort_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeEdgesOfVertex', node_name='Edges of Vertex', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vertex_index' : 0, 'weights' : 1, 'sort_index' : 2, }
        self.outsockets = {'edge_index' : 0, 'total' : 1, }

        # Input sockets plugging

        if vertex_index    is not None: self.vertex_index    = vertex_index
        if weights         is not None: self.weights         = weights
        if sort_index      is not None: self.sort_index      = sort_index

    @property
    def edge_index(self):
        return self.get_output_socket('edge_index')

    @property
    def total(self):
        return self.get_output_socket('total')

    @property
    def vertex_index(self):
        raise AttributeError("Attribute error on node 'EdgesOfVertex': the input socket 'vertex_index' is write only.")

    @vertex_index.setter
    def vertex_index(self, value):
        self.set_input_socket('vertex_index', value)

    @property
    def weights(self):
        raise AttributeError("Attribute error on node 'EdgesOfVertex': the input socket 'weights' is write only.")

    @weights.setter
    def weights(self, value):
        self.set_input_socket('weights', value)

    @property
    def sort_index(self):
        raise AttributeError("Attribute error on node 'EdgesOfVertex': the input socket 'sort_index' is write only.")

    @sort_index.setter
    def sort_index(self, value):
        self.set_input_socket('sort_index', value)

# ----------------------------------------------------------------------------------------------------
# Node ExtrudeMesh for GeometryNodeExtrudeMesh

class ExtrudeMesh(Node):

    """Node *Extrude Mesh*

    .. _ExtrudeMesh:

    Node implementation:
        Mesh:
            extrude 
        Face:
            extrude 
        Edge:
            extrude 
        Vertex:
            extrude 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        offset (DataSocket): Vector
        offset_scale (DataSocket): Float
        individual (DataSocket): Boolean
        mode (str): Node parameter, default = 'FACES' in ('VERTICES', 'EDGES', 'FACES')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh
        - **top** : Boolean
        - **side** : Boolean

    .. blid:: GeometryNodeExtrudeMesh

    """

    def __init__(self, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None, node_color=None):

        super().__init__('GeometryNodeExtrudeMesh', node_name='Extrude Mesh', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, 'offset' : 2, 'offset_scale' : 3, 'individual' : 4, }
        self.outsockets = {'mesh' : 0, 'top' : 1, 'side' : 2, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection
        if offset          is not None: self.offset          = offset
        if offset_scale    is not None: self.offset_scale    = offset_scale
        if individual      is not None: self.individual      = individual

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def top(self):
        return self.get_output_socket('top')

    @property
    def side(self):
        return self.get_output_socket('side')

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'ExtrudeMesh': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'ExtrudeMesh': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

    @property
    def offset_scale(self):
        raise AttributeError("Attribute error on node 'ExtrudeMesh': the input socket 'offset_scale' is write only.")

    @offset_scale.setter
    def offset_scale(self, value):
        self.set_input_socket('offset_scale', value)

    @property
    def individual(self):
        raise AttributeError("Attribute error on node 'ExtrudeMesh': the input socket 'individual' is write only.")

    @individual.setter
    def individual(self, value):
        self.set_input_socket('individual', value)

# ----------------------------------------------------------------------------------------------------
# Node FaceOfCorner for GeometryNodeFaceOfCorner

class FaceOfCorner(Node):

    """Node *Face of Corner*

    .. _FaceOfCorner:

    Node implementation:
        Mesh:
            face_of_corner 
        Corner:
            face face_index index_in_face 

    Args:
        corner_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **face_index** : Integer
        - **index_in_face** : Integer

    .. blid:: GeometryNodeFaceOfCorner

    """

    def __init__(self, corner_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeFaceOfCorner', node_name='Face of Corner', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'corner_index' : 0, }
        self.outsockets = {'face_index' : 0, 'index_in_face' : 1, }

        # Input sockets plugging

        if corner_index    is not None: self.corner_index    = corner_index

    @property
    def face_index(self):
        return self.get_output_socket('face_index')

    @property
    def index_in_face(self):
        return self.get_output_socket('index_in_face')

    @property
    def corner_index(self):
        raise AttributeError("Attribute error on node 'FaceOfCorner': the input socket 'corner_index' is write only.")

    @corner_index.setter
    def corner_index(self, value):
        self.set_input_socket('corner_index', value)

# ----------------------------------------------------------------------------------------------------
# Node FieldAtIndex for GeometryNodeFieldAtIndex

class FieldAtIndex(Node):

    """Node *Field at Index*

    .. _FieldAtIndex:

    Node implementation:
        Geometry:
            field_at_index 
        Domain:
            field_at_index 

    Args:
        index (DataSocket): Integer
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeFieldAtIndex

    """

    def __init__(self, index=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeFieldAtIndex', node_name='Field at Index', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'index' : 0, 'value' : [1, 2, 3, 4, 5], }
        self.outsockets = {'value' : [0, 1, 2, 3, 4], }

        # Input sockets plugging

        if index           is not None: self.index           = index
        if value           is not None: self.value           = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def index(self):
        raise AttributeError("Attribute error on node 'FieldAtIndex': the input socket 'index' is write only.")

    @index.setter
    def index(self, value):
        self.set_input_socket('index', value)

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

# ----------------------------------------------------------------------------------------------------
# Node InterpolateDomain for GeometryNodeFieldOnDomain

class InterpolateDomain(Node):

    """Node *Interpolate Domain*

    .. _InterpolateDomain:

    Node implementation:
        Geometry:
            interpolate_domain 
        Domain:
            interpolate 

    Args:
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeFieldOnDomain

    """

    def __init__(self, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeFieldOnDomain', node_name='Interpolate Domain', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value' : [0, 1, 2, 3, 4], }
        self.outsockets = {'value' : [0, 1, 2, 3, 4], }

        # Input sockets plugging

        if value           is not None: self.value           = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

# ----------------------------------------------------------------------------------------------------
# Node FillCurve for GeometryNodeFillCurve

class FillCurve(Node):

    """Node *Fill Curve*

    .. _FillCurve:

    Node implementation:
        Curve:
            fill fill_triangles fill_ngons 

    Args:
        curve (DataSocket): Curve
        mode (str): Node parameter, default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeFillCurve

    """

    def __init__(self, curve=None, mode='TRIANGLES', label=None, node_color=None):

        super().__init__('GeometryNodeFillCurve', node_name='Fill Curve', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def curve(self):
        raise AttributeError("Attribute error on node 'FillCurve': the input socket 'curve' is write only.")

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

# ----------------------------------------------------------------------------------------------------
# Node FilletCurve for GeometryNodeFilletCurve

class FilletCurve(Node):

    """Node *Fillet Curve*

    .. _FilletCurve:

    Node implementation:
        Curve:
            fillet fillet_bezier fillet_poly 

    Args:
        curve (DataSocket): Curve
        count (DataSocket): Integer
        radius (DataSocket): Float
        limit_radius (DataSocket): Boolean
        mode (str): Node parameter, default = 'BEZIER' in ('BEZIER', 'POLY')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeFilletCurve

    """

    def __init__(self, curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None, node_color=None):

        super().__init__('GeometryNodeFilletCurve', node_name='Fillet Curve', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'count' : 1, 'radius' : 2, 'limit_radius' : 3, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if count           is not None: self.count           = count
        if radius          is not None: self.radius          = radius
        if limit_radius    is not None: self.limit_radius    = limit_radius

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def count(self):
        raise AttributeError("Attribute error on node 'FilletCurve': the input socket 'count' is write only.")

    @count.setter
    def count(self, value):
        self.set_input_socket('count', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'FilletCurve': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

    @property
    def limit_radius(self):
        raise AttributeError("Attribute error on node 'FilletCurve': the input socket 'limit_radius' is write only.")

    @limit_radius.setter
    def limit_radius(self, value):
        self.set_input_socket('limit_radius', value)

# ----------------------------------------------------------------------------------------------------
# Node FlipFaces for GeometryNodeFlipFaces

class FlipFaces(Node):

    """Node *Flip Faces*

    .. _FlipFaces:

    Node implementation:
        Mesh:
            flip_faces 
        Face:
            flip 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeFlipFaces

    """

    def __init__(self, mesh=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeFlipFaces', node_name='Flip Faces', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'FlipFaces': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node GeometryToInstance for GeometryNodeGeometryToInstance

class GeometryToInstance(Node):

    """Node *Geometry to Instance*

    .. _GeometryToInstance:

    Node implementation:
        global functions:
            geometry_to_instance 
        Geometry:
            to_instance 

    Args:
        geometry (DataSocket): <m> Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **instances** : Instances

    .. blid:: GeometryNodeGeometryToInstance

    """

    def __init__(self, *geometry, label=None, node_color=None):

        super().__init__('GeometryNodeGeometryToInstance', node_name='Geometry to Instance', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        self.plug(0, *geometry)

    @property
    def instances(self):
        return self.get_output_socket('instances')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'GeometryToInstance': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node Group for GeometryNodeGroup

class Group(Node):

    """Node *Group*

    .. _Group:

    Args:
        node_color (color): Node color
        node_label (str): Node label


    .. blid:: GeometryNodeGroup

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeGroup', node_name='Group', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {}

# ----------------------------------------------------------------------------------------------------
# Node ImageTexture for GeometryNodeImageTexture

class ImageTexture(Node):

    """Node *Image Texture*

    .. _ImageTexture:

    Node implementation:
        Texture:
            image 
        Image:
            texture 

    Args:
        image (DataSocket): Image
        vector (DataSocket): Vector
        frame (DataSocket): Integer
        extension (str): Node parameter, default = 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP')
        interpolation (str): Node parameter, default = 'Linear' in ('Linear', 'Closest', 'Cubic')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **alpha** : Float

    .. blid:: GeometryNodeImageTexture

    """

    def __init__(self, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None, node_color=None):

        super().__init__('GeometryNodeImageTexture', node_name='Image Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.extension       = extension
        self.bnode.interpolation   = interpolation

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'image' : 0, 'vector' : 1, 'frame' : 2, }
        self.outsockets = {'color' : 0, 'alpha' : 1, }

        # Input sockets plugging

        if image           is not None: self.image           = image
        if vector          is not None: self.vector          = vector
        if frame           is not None: self.frame           = frame

    @property
    def extension(self):
        return self.bnode.extension

    @extension.setter
    def extension(self, value):
        self.bnode.extension = value

    @property
    def interpolation(self):
        return self.bnode.interpolation

    @interpolation.setter
    def interpolation(self, value):
        self.bnode.interpolation = value

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def alpha(self):
        return self.get_output_socket('alpha')

    @property
    def image(self):
        raise AttributeError("Attribute error on node 'ImageTexture': the input socket 'image' is write only.")

    @image.setter
    def image(self, value):
        self.set_input_socket('image', value)

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'ImageTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def frame(self):
        raise AttributeError("Attribute error on node 'ImageTexture': the input socket 'frame' is write only.")

    @frame.setter
    def frame(self, value):
        self.set_input_socket('frame', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveHandlePositions for GeometryNodeInputCurveHandlePositions

class CurveHandlePositions(Node):

    """Node *Curve Handle Positions*

    .. _CurveHandlePositions:

    Node implementation:
        ControlPoint:
            handle_positions left_handle_positions right_handle_positions 

    Args:
        relative (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **left** : Vector
        - **right** : Vector

    .. blid:: GeometryNodeInputCurveHandlePositions

    """

    def __init__(self, relative=None, label=None, node_color=None):

        super().__init__('GeometryNodeInputCurveHandlePositions', node_name='Curve Handle Positions', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'relative' : 0, }
        self.outsockets = {'left' : 0, 'right' : 1, }

        # Input sockets plugging

        if relative        is not None: self.relative        = relative

    @property
    def left(self):
        return self.get_output_socket('left')

    @property
    def right(self):
        return self.get_output_socket('right')

    @property
    def relative(self):
        raise AttributeError("Attribute error on node 'CurveHandlePositions': the input socket 'relative' is write only.")

    @relative.setter
    def relative(self, value):
        self.set_input_socket('relative', value)

# ----------------------------------------------------------------------------------------------------
# Node CurveTilt for GeometryNodeInputCurveTilt

class CurveTilt(Node):

    """Node *Curve Tilt*

    .. _CurveTilt:

    Node implementation:
        ControlPoint:
            tilt 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **tilt** : Float

    .. blid:: GeometryNodeInputCurveTilt

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputCurveTilt', node_name='Curve Tilt', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'tilt' : 0, }

    @property
    def tilt(self):
        return self.get_output_socket('tilt')

# ----------------------------------------------------------------------------------------------------
# Node ID for GeometryNodeInputID

class ID(Node):

    """Node *ID*

    .. _ID:

    Node implementation:
        Geometry:
            ID 
        Domain:
            ID 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **ID** : Integer

    .. blid:: GeometryNodeInputID

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputID', node_name='ID', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'ID' : 0, }

    @property
    def ID(self):
        return self.get_output_socket('ID')

# ----------------------------------------------------------------------------------------------------
# Node Index for GeometryNodeInputIndex

class Index(Node):

    """Node *Index*

    .. _Index:

    Node implementation:
        Geometry:
            index 
        Domain:
            index domain_index 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **index** : Integer

    .. blid:: GeometryNodeInputIndex

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputIndex', node_name='Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'index' : 0, }

    @property
    def index(self):
        return self.get_output_socket('index')

# ----------------------------------------------------------------------------------------------------
# Node InstanceRotation for GeometryNodeInputInstanceRotation

class InstanceRotation(Node):

    """Node *Instance Rotation*

    .. _InstanceRotation:

    Node implementation:
        Instances:
            rotation 
        Instance:
            rotation 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **rotation** : Vector

    .. blid:: GeometryNodeInputInstanceRotation

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputInstanceRotation', node_name='Instance Rotation', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'rotation' : 0, }

    @property
    def rotation(self):
        return self.get_output_socket('rotation')

# ----------------------------------------------------------------------------------------------------
# Node InstanceScale for GeometryNodeInputInstanceScale

class InstanceScale(Node):

    """Node *Instance Scale*

    .. _InstanceScale:

    Node implementation:
        Instances:
            scale 
        Instance:
            scale 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **scale** : Vector

    .. blid:: GeometryNodeInputInstanceScale

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputInstanceScale', node_name='Instance Scale', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'scale' : 0, }

    @property
    def scale(self):
        return self.get_output_socket('scale')

# ----------------------------------------------------------------------------------------------------
# Node Material for GeometryNodeInputMaterial

class Material(Node):

    """Node *Material*

    .. _Material:

    Node implementation:
        Material:
            Material 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **material** : Material

    .. blid:: GeometryNodeInputMaterial

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMaterial', node_name='Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'material' : 0, }

    @property
    def material(self):
        return self.get_output_socket('material')

# ----------------------------------------------------------------------------------------------------
# Node MaterialIndex for GeometryNodeInputMaterialIndex

class MaterialIndex(Node):

    """Node *Material Index*

    .. _MaterialIndex:

    Node implementation:
        Geometry:
            material_index 
        Domain:
            material_index 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **material_index** : Integer

    .. blid:: GeometryNodeInputMaterialIndex

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMaterialIndex', node_name='Material Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'material_index' : 0, }

    @property
    def material_index(self):
        return self.get_output_socket('material_index')

# ----------------------------------------------------------------------------------------------------
# Node EdgeAngle for GeometryNodeInputMeshEdgeAngle

class EdgeAngle(Node):

    """Node *Edge Angle*

    .. _EdgeAngle:

    Node implementation:
        Edge:
            angle unsigned_angle signed_angle 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **unsigned_angle** : Float
        - **signed_angle** : Float

    .. blid:: GeometryNodeInputMeshEdgeAngle

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeAngle', node_name='Edge Angle', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'unsigned_angle' : 0, 'signed_angle' : 1, }

    @property
    def unsigned_angle(self):
        return self.get_output_socket('unsigned_angle')

    @property
    def signed_angle(self):
        return self.get_output_socket('signed_angle')

# ----------------------------------------------------------------------------------------------------
# Node EdgeNeighbors for GeometryNodeInputMeshEdgeNeighbors

class EdgeNeighbors(Node):

    """Node *Edge Neighbors*

    .. _EdgeNeighbors:

    Node implementation:
        Edge:
            neighbors 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **face_count** : Integer

    .. blid:: GeometryNodeInputMeshEdgeNeighbors

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', node_name='Edge Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'face_count' : 0, }

    @property
    def face_count(self):
        return self.get_output_socket('face_count')

# ----------------------------------------------------------------------------------------------------
# Node EdgeVertices for GeometryNodeInputMeshEdgeVertices

class EdgeVertices(Node):

    """Node *Edge Vertices*

    .. _EdgeVertices:

    Node implementation:
        Edge:
            vertices vertices_index vertices_position 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vertex_index_1** : Integer
        - **vertex_index_2** : Integer
        - **position_1** : Vector
        - **position_2** : Vector

    .. blid:: GeometryNodeInputMeshEdgeVertices

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeVertices', node_name='Edge Vertices', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_index_1' : 0, 'vertex_index_2' : 1, 'position_1' : 2, 'position_2' : 3, }

    @property
    def vertex_index_1(self):
        return self.get_output_socket('vertex_index_1')

    @property
    def vertex_index_2(self):
        return self.get_output_socket('vertex_index_2')

    @property
    def position_1(self):
        return self.get_output_socket('position_1')

    @property
    def position_2(self):
        return self.get_output_socket('position_2')

# ----------------------------------------------------------------------------------------------------
# Node FaceArea for GeometryNodeInputMeshFaceArea

class FaceArea(Node):

    """Node *Face Area*

    .. _FaceArea:

    Node implementation:
        Face:
            area 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **area** : Float

    .. blid:: GeometryNodeInputMeshFaceArea

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceArea', node_name='Face Area', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'area' : 0, }

    @property
    def area(self):
        return self.get_output_socket('area')

# ----------------------------------------------------------------------------------------------------
# Node FaceIsPlanar for GeometryNodeInputMeshFaceIsPlanar

class FaceIsPlanar(Node):

    """Node *Face is Planar*

    .. _FaceIsPlanar:

    Node implementation:
        Mesh:
            face_is_planar 
        Face:
            is_planar 

    Args:
        threshold (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **planar** : Boolean

    .. blid:: GeometryNodeInputMeshFaceIsPlanar

    """

    def __init__(self, threshold=None, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceIsPlanar', node_name='Face is Planar', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'threshold' : 0, }
        self.outsockets = {'planar' : 0, }

        # Input sockets plugging

        if threshold       is not None: self.threshold       = threshold

    @property
    def planar(self):
        return self.get_output_socket('planar')

    @property
    def threshold(self):
        raise AttributeError("Attribute error on node 'FaceIsPlanar': the input socket 'threshold' is write only.")

    @threshold.setter
    def threshold(self, value):
        self.set_input_socket('threshold', value)

# ----------------------------------------------------------------------------------------------------
# Node FaceNeighbors for GeometryNodeInputMeshFaceNeighbors

class FaceNeighbors(Node):

    """Node *Face Neighbors*

    .. _FaceNeighbors:

    Node implementation:
        Face:
            neighbors neighbors_vertex_count neighbors_face_count 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vertex_count** : Integer
        - **face_count** : Integer

    .. blid:: GeometryNodeInputMeshFaceNeighbors

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceNeighbors', node_name='Face Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_count' : 0, 'face_count' : 1, }

    @property
    def vertex_count(self):
        return self.get_output_socket('vertex_count')

    @property
    def face_count(self):
        return self.get_output_socket('face_count')

# ----------------------------------------------------------------------------------------------------
# Node MeshIsland for GeometryNodeInputMeshIsland

class MeshIsland(Node):

    """Node *Mesh Island*

    .. _MeshIsland:

    Node implementation:
        Mesh:
            island island_index island_count 
        Face:
            island island_index island_count 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **island_index** : Integer
        - **island_count** : Integer

    .. blid:: GeometryNodeInputMeshIsland

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshIsland', node_name='Mesh Island', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'island_index' : 0, 'island_count' : 1, }

    @property
    def island_index(self):
        return self.get_output_socket('island_index')

    @property
    def island_count(self):
        return self.get_output_socket('island_count')

# ----------------------------------------------------------------------------------------------------
# Node VertexNeighbors for GeometryNodeInputMeshVertexNeighbors

class VertexNeighbors(Node):

    """Node *Vertex Neighbors*

    .. _VertexNeighbors:

    Node implementation:
        Vertex:
            neighbors neighbors_vertex_count neighbors_face_count 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vertex_count** : Integer
        - **face_count** : Integer

    .. blid:: GeometryNodeInputMeshVertexNeighbors

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshVertexNeighbors', node_name='Vertex Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_count' : 0, 'face_count' : 1, }

    @property
    def vertex_count(self):
        return self.get_output_socket('vertex_count')

    @property
    def face_count(self):
        return self.get_output_socket('face_count')

# ----------------------------------------------------------------------------------------------------
# Node NamedAttribute for GeometryNodeInputNamedAttribute

class NamedAttribute(Node):

    """Node *Named Attribute*

    .. _NamedAttribute:

    Node implementation:
        Geometry:
            named_attribute get_named_float get_named_integer get_named_vector get_named_color get_named_boolean 
        Domain:
            named_attribute get_named_float get_named_integer get_named_vector get_named_color get_named_boolean 

    Args:
        name (DataSocket): String
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **attribute** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : []
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeInputNamedAttribute

    """

    def __init__(self, name=None, data_type='FLOAT', label=None, node_color=None):

        super().__init__('GeometryNodeInputNamedAttribute', node_name='Named Attribute', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'name' : 0, }
        self.outsockets = {'attribute' : [0, 1, 2, 3, 4], }

        # Input sockets plugging

        if name            is not None: self.name            = name

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def attribute(self):
        return self.get_output_socket('attribute')

    @property
    def name(self):
        raise AttributeError("Attribute error on node 'NamedAttribute': the input socket 'name' is write only.")

    @name.setter
    def name(self, value):
        self.set_input_socket('name', value)

# ----------------------------------------------------------------------------------------------------
# Node Normal for GeometryNodeInputNormal

class Normal(Node):

    """Node *Normal*

    .. _Normal:

    Node implementation:
        Geometry:
            normal 
        Domain:
            normal 
        Spline:
            normal 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **normal** : Vector

    .. blid:: GeometryNodeInputNormal

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputNormal', node_name='Normal', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'normal' : 0, }

    @property
    def normal(self):
        return self.get_output_socket('normal')

# ----------------------------------------------------------------------------------------------------
# Node Position for GeometryNodeInputPosition

class Position(Node):

    """Node *Position*

    .. _Position:

    Node implementation:
        Geometry:
            position 
        Domain:
            position 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **position** : Vector

    .. blid:: GeometryNodeInputPosition

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputPosition', node_name='Position', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'position' : 0, }

    @property
    def position(self):
        return self.get_output_socket('position')

# ----------------------------------------------------------------------------------------------------
# Node Radius for GeometryNodeInputRadius

class Radius(Node):

    """Node *Radius*

    .. _Radius:

    Node implementation:
        Geometry:
            radius 
        ControlPoint:
            radius 
        CloudPoint:
            radius 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **radius** : Float

    .. blid:: GeometryNodeInputRadius

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputRadius', node_name='Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'radius' : 0, }

    @property
    def radius(self):
        return self.get_output_socket('radius')

# ----------------------------------------------------------------------------------------------------
# Node SceneTime for GeometryNodeInputSceneTime

class SceneTime(Node):

    """Node *Scene Time*

    .. _SceneTime:

    Node implementation:
        Float:
            Seconds Frame 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **seconds** : Float
        - **frame** : Float

    .. blid:: GeometryNodeInputSceneTime

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSceneTime', node_name='Scene Time', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'seconds' : 0, 'frame' : 1, }

    @property
    def seconds(self):
        return self.get_output_socket('seconds')

    @property
    def frame(self):
        return self.get_output_socket('frame')

# ----------------------------------------------------------------------------------------------------
# Node IsShadeSmooth for GeometryNodeInputShadeSmooth

class IsShadeSmooth(Node):

    """Node *Is Shade Smooth*

    .. _IsShadeSmooth:

    Node implementation:
        Mesh:
            is_shade_smooth 
        Face:
            shade_smooth 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **smooth** : Boolean

    .. blid:: GeometryNodeInputShadeSmooth

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputShadeSmooth', node_name='Is Shade Smooth', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'smooth' : 0, }

    @property
    def smooth(self):
        return self.get_output_socket('smooth')

# ----------------------------------------------------------------------------------------------------
# Node ShortestEdgePaths for GeometryNodeInputShortestEdgePaths

class ShortestEdgePaths(Node):

    """Node *Shortest Edge Paths*

    .. _ShortestEdgePaths:

    Node implementation:
        Mesh:
            shortest_edge_paths 

    Args:
        end_vertex (DataSocket): Boolean
        edge_cost (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **next_vertex_index** : Integer
        - **total_cost** : Float

    .. blid:: GeometryNodeInputShortestEdgePaths

    """

    def __init__(self, end_vertex=None, edge_cost=None, label=None, node_color=None):

        super().__init__('GeometryNodeInputShortestEdgePaths', node_name='Shortest Edge Paths', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'end_vertex' : 0, 'edge_cost' : 1, }
        self.outsockets = {'next_vertex_index' : 0, 'total_cost' : 1, }

        # Input sockets plugging

        if end_vertex      is not None: self.end_vertex      = end_vertex
        if edge_cost       is not None: self.edge_cost       = edge_cost

    @property
    def next_vertex_index(self):
        return self.get_output_socket('next_vertex_index')

    @property
    def total_cost(self):
        return self.get_output_socket('total_cost')

    @property
    def end_vertex(self):
        raise AttributeError("Attribute error on node 'ShortestEdgePaths': the input socket 'end_vertex' is write only.")

    @end_vertex.setter
    def end_vertex(self, value):
        self.set_input_socket('end_vertex', value)

    @property
    def edge_cost(self):
        raise AttributeError("Attribute error on node 'ShortestEdgePaths': the input socket 'edge_cost' is write only.")

    @edge_cost.setter
    def edge_cost(self, value):
        self.set_input_socket('edge_cost', value)

# ----------------------------------------------------------------------------------------------------
# Node IsSplineCyclic for GeometryNodeInputSplineCyclic

class IsSplineCyclic(Node):

    """Node *Is Spline Cyclic*

    .. _IsSplineCyclic:

    Node implementation:
        Spline:
            cyclic 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **cyclic** : Boolean

    .. blid:: GeometryNodeInputSplineCyclic

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSplineCyclic', node_name='Is Spline Cyclic', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'cyclic' : 0, }

    @property
    def cyclic(self):
        return self.get_output_socket('cyclic')

# ----------------------------------------------------------------------------------------------------
# Node SplineResolution for GeometryNodeInputSplineResolution

class SplineResolution(Node):

    """Node *Spline Resolution*

    .. _SplineResolution:

    Node implementation:
        Spline:
            resolution 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **resolution** : Integer

    .. blid:: GeometryNodeInputSplineResolution

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSplineResolution', node_name='Spline Resolution', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'resolution' : 0, }

    @property
    def resolution(self):
        return self.get_output_socket('resolution')

# ----------------------------------------------------------------------------------------------------
# Node CurveTangent for GeometryNodeInputTangent

class CurveTangent(Node):

    """Node *Curve Tangent*

    .. _CurveTangent:

    Node implementation:
        ControlPoint:
            tangent 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **tangent** : Vector

    .. blid:: GeometryNodeInputTangent

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputTangent', node_name='Curve Tangent', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'tangent' : 0, }

    @property
    def tangent(self):
        return self.get_output_socket('tangent')

# ----------------------------------------------------------------------------------------------------
# Node InstanceOnPoints for GeometryNodeInstanceOnPoints

class InstanceOnPoints(Node):

    """Node *Instance on Points*

    .. _InstanceOnPoints:

    Node implementation:
        Instances:
            InstanceOnPoints on_points 
        ('Points', 'Mesh', 'Curve'):
            instance_on_points 
        Vertex:
            instance_on_points 
        ControlPoint:
            instance_on_points 
        CloudPoint:
            instance_on_points 

    Args:
        points (DataSocket): Points
        selection (DataSocket): Boolean
        instance (DataSocket): Geometry
        pick_instance (DataSocket): Boolean
        instance_index (DataSocket): Integer
        rotation (DataSocket): Vector
        scale (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **instances** : Instances

    .. blid:: GeometryNodeInstanceOnPoints

    """

    def __init__(self, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None, node_color=None):

        super().__init__('GeometryNodeInstanceOnPoints', node_name='Instance on Points', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'selection' : 1, 'instance' : 2, 'pick_instance' : 3, 'instance_index' : 4, 'rotation' : 5, 'scale' : 6, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if selection       is not None: self.selection       = selection
        if instance        is not None: self.instance        = instance
        if pick_instance   is not None: self.pick_instance   = pick_instance
        if instance_index  is not None: self.instance_index  = instance_index
        if rotation        is not None: self.rotation        = rotation
        if scale           is not None: self.scale           = scale

    @property
    def instances(self):
        return self.get_output_socket('instances')

    @property
    def points(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'points' is write only.")

    @points.setter
    def points(self, value):
        self.set_input_socket('points', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def instance(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'instance' is write only.")

    @instance.setter
    def instance(self, value):
        self.set_input_socket('instance', value)

    @property
    def pick_instance(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'pick_instance' is write only.")

    @pick_instance.setter
    def pick_instance(self, value):
        self.set_input_socket('pick_instance', value)

    @property
    def instance_index(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'instance_index' is write only.")

    @instance_index.setter
    def instance_index(self, value):
        self.set_input_socket('instance_index', value)

    @property
    def rotation(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'rotation' is write only.")

    @rotation.setter
    def rotation(self, value):
        self.set_input_socket('rotation', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'InstanceOnPoints': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

# ----------------------------------------------------------------------------------------------------
# Node InstancesToPoints for GeometryNodeInstancesToPoints

class InstancesToPoints(Node):

    """Node *Instances to Points*

    .. _InstancesToPoints:

    Node implementation:
        Instances:
            to_points 
        Instance:
            to_points 

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **points** : Points

    .. blid:: GeometryNodeInstancesToPoints

    """

    def __init__(self, instances=None, selection=None, position=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeInstancesToPoints', node_name='Instances to Points', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'position' : 2, 'radius' : 3, }
        self.outsockets = {'points' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if position        is not None: self.position        = position
        if radius          is not None: self.radius          = radius

    @property
    def points(self):
        return self.get_output_socket('points')

    @property
    def instances(self):
        raise AttributeError("Attribute error on node 'InstancesToPoints': the input socket 'instances' is write only.")

    @instances.setter
    def instances(self, value):
        self.set_input_socket('instances', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'InstancesToPoints': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def position(self):
        raise AttributeError("Attribute error on node 'InstancesToPoints': the input socket 'position' is write only.")

    @position.setter
    def position(self, value):
        self.set_input_socket('position', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'InstancesToPoints': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node IsViewport for GeometryNodeIsViewport

class IsViewport(Node):

    """Node *Is Viewport*

    .. _IsViewport:

    Node implementation:
        Geometry:
            is_viewport 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **is_viewport** : Boolean

    .. blid:: GeometryNodeIsViewport

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeIsViewport', node_name='Is Viewport', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'is_viewport' : 0, }

    @property
    def is_viewport(self):
        return self.get_output_socket('is_viewport')

# ----------------------------------------------------------------------------------------------------
# Node JoinGeometry for GeometryNodeJoinGeometry

class JoinGeometry(Node):

    """Node *Join Geometry*

    .. _JoinGeometry:

    Node implementation:
        global functions:
            join_geometry 
        Geometry:
            join 

    Args:
        geometry (DataSocket): <m> Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeJoinGeometry

    """

    def __init__(self, *geometry, label=None, node_color=None):

        super().__init__('GeometryNodeJoinGeometry', node_name='Join Geometry', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        self.plug(0, *geometry)

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node MaterialSelection for GeometryNodeMaterialSelection

class MaterialSelection(Node):

    """Node *Material Selection*

    .. _MaterialSelection:

    Node implementation:
        Geometry:
            material_selection 
        Domain:
            material_selection 

    Args:
        material (DataSocket): Material
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **selection** : Boolean

    .. blid:: GeometryNodeMaterialSelection

    """

    def __init__(self, material=None, label=None, node_color=None):

        super().__init__('GeometryNodeMaterialSelection', node_name='Material Selection', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'material' : 0, }
        self.outsockets = {'selection' : 0, }

        # Input sockets plugging

        if material        is not None: self.material        = material

    @property
    def selection(self):
        return self.get_output_socket('selection')

    @property
    def material(self):
        raise AttributeError("Attribute error on node 'MaterialSelection': the input socket 'material' is write only.")

    @material.setter
    def material(self, value):
        self.set_input_socket('material', value)

# ----------------------------------------------------------------------------------------------------
# Node MergeByDistance for GeometryNodeMergeByDistance

class MergeByDistance(Node):

    """Node *Merge by Distance*

    .. _MergeByDistance:

    Node implementation:
        Geometry:
            merge_by_distance 
        Vertex:
            merge_by_distance 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        distance (DataSocket): Float
        mode (str): Node parameter, default = 'ALL' in ('ALL', 'CONNECTED')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeMergeByDistance

    """

    def __init__(self, geometry=None, selection=None, distance=None, mode='ALL', label=None, node_color=None):

        super().__init__('GeometryNodeMergeByDistance', node_name='Merge by Distance', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'distance' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if distance        is not None: self.distance        = distance

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'MergeByDistance': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def distance(self):
        raise AttributeError("Attribute error on node 'MergeByDistance': the input socket 'distance' is write only.")

    @distance.setter
    def distance(self, value):
        self.set_input_socket('distance', value)

# ----------------------------------------------------------------------------------------------------
# Node MeshBoolean for GeometryNodeMeshBoolean

class MeshBoolean(Node):

    """Node *Mesh Boolean*

    .. _MeshBoolean:

    Node implementation:
        Mesh:
            boolean_intersect boolean_union boolean_difference 

    Args:
        mesh_1 (DataSocket): Geometry
        mesh_2 (DataSocket): <m> Geometry
        self_intersection (DataSocket): Boolean
        hole_tolerant (DataSocket): Boolean
        operation (str): Node parameter, default = 'DIFFERENCE' in ('INTERSECT', 'UNION', 'DIFFERENCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh
        - **intersecting_edges** : Boolean

    .. blid:: GeometryNodeMeshBoolean

    """

    def __init__(self, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None, node_color=None):

        super().__init__('GeometryNodeMeshBoolean', node_name='Mesh Boolean', label=label, node_color=node_color)

        # Node parameters

        self.bnode.operation       = operation

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh_1' : 0, 'mesh_2' : 1, 'self_intersection' : 2, 'hole_tolerant' : 3, }
        self.outsockets = {'mesh' : 0, 'intersecting_edges' : 1, }

        # Input sockets plugging

        if mesh_1          is not None: self.mesh_1          = mesh_1
        self.plug(1, *mesh_2)
        if self_intersection is not None: self.self_intersection = self_intersection
        if hole_tolerant   is not None: self.hole_tolerant   = hole_tolerant

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def intersecting_edges(self):
        return self.get_output_socket('intersecting_edges')

    @property
    def mesh_1(self):
        raise AttributeError("Attribute error on node 'MeshBoolean': the input socket 'mesh_1' is write only.")

    @mesh_1.setter
    def mesh_1(self, value):
        self.set_input_socket('mesh_1', value)

    @property
    def mesh_2(self):
        raise AttributeError("Attribute error on node 'MeshBoolean': the input socket 'mesh_2' is write only.")

    @mesh_2.setter
    def mesh_2(self, value):
        self.set_input_socket('mesh_2', value)

    @property
    def self_intersection(self):
        raise AttributeError("Attribute error on node 'MeshBoolean': the input socket 'self_intersection' is write only.")

    @self_intersection.setter
    def self_intersection(self, value):
        self.set_input_socket('self_intersection', value)

    @property
    def hole_tolerant(self):
        raise AttributeError("Attribute error on node 'MeshBoolean': the input socket 'hole_tolerant' is write only.")

    @hole_tolerant.setter
    def hole_tolerant(self, value):
        self.set_input_socket('hole_tolerant', value)

# ----------------------------------------------------------------------------------------------------
# Node MeshCircle for GeometryNodeMeshCircle

class MeshCircle(Node):

    """Node *Mesh Circle*

    .. _MeshCircle:

    Node implementation:
        Mesh:
            Circle 

    Args:
        vertices (DataSocket): Integer
        radius (DataSocket): Float
        fill_type (str): Node parameter, default = 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeMeshCircle

    """

    def __init__(self, vertices=None, radius=None, fill_type='NONE', label=None, node_color=None):

        super().__init__('GeometryNodeMeshCircle', node_name='Mesh Circle', label=label, node_color=node_color)

        # Node parameters

        self.bnode.fill_type       = fill_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vertices' : 0, 'radius' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if vertices        is not None: self.vertices        = vertices
        if radius          is not None: self.radius          = radius

    @property
    def fill_type(self):
        return self.bnode.fill_type

    @fill_type.setter
    def fill_type(self, value):
        self.bnode.fill_type = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def vertices(self):
        raise AttributeError("Attribute error on node 'MeshCircle': the input socket 'vertices' is write only.")

    @vertices.setter
    def vertices(self, value):
        self.set_input_socket('vertices', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'MeshCircle': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node Cone for GeometryNodeMeshCone

class Cone(Node):

    """Node *Cone*

    .. _Cone:

    Node implementation:
        Mesh:
            Cone 

    Args:
        vertices (DataSocket): Integer
        side_segments (DataSocket): Integer
        fill_segments (DataSocket): Integer
        radius_top (DataSocket): Float
        radius_bottom (DataSocket): Float
        depth (DataSocket): Float
        fill_type (str): Node parameter, default = 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh
        - **top** : Boolean
        - **bottom** : Boolean
        - **side** : Boolean

    .. blid:: GeometryNodeMeshCone

    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None, node_color=None):

        super().__init__('GeometryNodeMeshCone', node_name='Cone', label=label, node_color=node_color)

        # Node parameters

        self.bnode.fill_type       = fill_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vertices' : 0, 'side_segments' : 1, 'fill_segments' : 2, 'radius_top' : 3, 'radius_bottom' : 4, 'depth' : 5, }
        self.outsockets = {'mesh' : 0, 'top' : 1, 'bottom' : 2, 'side' : 3, }

        # Input sockets plugging

        if vertices        is not None: self.vertices        = vertices
        if side_segments   is not None: self.side_segments   = side_segments
        if fill_segments   is not None: self.fill_segments   = fill_segments
        if radius_top      is not None: self.radius_top      = radius_top
        if radius_bottom   is not None: self.radius_bottom   = radius_bottom
        if depth           is not None: self.depth           = depth

    @property
    def fill_type(self):
        return self.bnode.fill_type

    @fill_type.setter
    def fill_type(self, value):
        self.bnode.fill_type = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def top(self):
        return self.get_output_socket('top')

    @property
    def bottom(self):
        return self.get_output_socket('bottom')

    @property
    def side(self):
        return self.get_output_socket('side')

    @property
    def vertices(self):
        raise AttributeError("Attribute error on node 'Cone': the input socket 'vertices' is write only.")

    @vertices.setter
    def vertices(self, value):
        self.set_input_socket('vertices', value)

    @property
    def side_segments(self):
        raise AttributeError("Attribute error on node 'Cone': the input socket 'side_segments' is write only.")

    @side_segments.setter
    def side_segments(self, value):
        self.set_input_socket('side_segments', value)

    @property
    def fill_segments(self):
        raise AttributeError("Attribute error on node 'Cone': the input socket 'fill_segments' is write only.")

    @fill_segments.setter
    def fill_segments(self, value):
        self.set_input_socket('fill_segments', value)

    @property
    def radius_top(self):
        raise AttributeError("Attribute error on node 'Cone': the input socket 'radius_top' is write only.")

    @radius_top.setter
    def radius_top(self, value):
        self.set_input_socket('radius_top', value)

    @property
    def radius_bottom(self):
        raise AttributeError("Attribute error on node 'Cone': the input socket 'radius_bottom' is write only.")

    @radius_bottom.setter
    def radius_bottom(self, value):
        self.set_input_socket('radius_bottom', value)

    @property
    def depth(self):
        raise AttributeError("Attribute error on node 'Cone': the input socket 'depth' is write only.")

    @depth.setter
    def depth(self, value):
        self.set_input_socket('depth', value)

# ----------------------------------------------------------------------------------------------------
# Node Cube for GeometryNodeMeshCube

class Cube(Node):

    """Node *Cube*

    .. _Cube:

    Node implementation:
        Mesh:
            Cube 

    Args:
        size (DataSocket): Vector
        vertices_x (DataSocket): Integer
        vertices_y (DataSocket): Integer
        vertices_z (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeMeshCube

    """

    def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshCube', node_name='Cube', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'size' : 0, 'vertices_x' : 1, 'vertices_y' : 2, 'vertices_z' : 3, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if size            is not None: self.size            = size
        if vertices_x      is not None: self.vertices_x      = vertices_x
        if vertices_y      is not None: self.vertices_y      = vertices_y
        if vertices_z      is not None: self.vertices_z      = vertices_z

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def size(self):
        raise AttributeError("Attribute error on node 'Cube': the input socket 'size' is write only.")

    @size.setter
    def size(self, value):
        self.set_input_socket('size', value)

    @property
    def vertices_x(self):
        raise AttributeError("Attribute error on node 'Cube': the input socket 'vertices_x' is write only.")

    @vertices_x.setter
    def vertices_x(self, value):
        self.set_input_socket('vertices_x', value)

    @property
    def vertices_y(self):
        raise AttributeError("Attribute error on node 'Cube': the input socket 'vertices_y' is write only.")

    @vertices_y.setter
    def vertices_y(self, value):
        self.set_input_socket('vertices_y', value)

    @property
    def vertices_z(self):
        raise AttributeError("Attribute error on node 'Cube': the input socket 'vertices_z' is write only.")

    @vertices_z.setter
    def vertices_z(self, value):
        self.set_input_socket('vertices_z', value)

# ----------------------------------------------------------------------------------------------------
# Node Cylinder for GeometryNodeMeshCylinder

class Cylinder(Node):

    """Node *Cylinder*

    .. _Cylinder:

    Node implementation:
        Mesh:
            Cylinder 

    Args:
        vertices (DataSocket): Integer
        side_segments (DataSocket): Integer
        fill_segments (DataSocket): Integer
        radius (DataSocket): Float
        depth (DataSocket): Float
        fill_type (str): Node parameter, default = 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh
        - **top** : Boolean
        - **side** : Boolean
        - **bottom** : Boolean

    .. blid:: GeometryNodeMeshCylinder

    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None, node_color=None):

        super().__init__('GeometryNodeMeshCylinder', node_name='Cylinder', label=label, node_color=node_color)

        # Node parameters

        self.bnode.fill_type       = fill_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vertices' : 0, 'side_segments' : 1, 'fill_segments' : 2, 'radius' : 3, 'depth' : 4, }
        self.outsockets = {'mesh' : 0, 'top' : 1, 'side' : 2, 'bottom' : 3, }

        # Input sockets plugging

        if vertices        is not None: self.vertices        = vertices
        if side_segments   is not None: self.side_segments   = side_segments
        if fill_segments   is not None: self.fill_segments   = fill_segments
        if radius          is not None: self.radius          = radius
        if depth           is not None: self.depth           = depth

    @property
    def fill_type(self):
        return self.bnode.fill_type

    @fill_type.setter
    def fill_type(self, value):
        self.bnode.fill_type = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def top(self):
        return self.get_output_socket('top')

    @property
    def side(self):
        return self.get_output_socket('side')

    @property
    def bottom(self):
        return self.get_output_socket('bottom')

    @property
    def vertices(self):
        raise AttributeError("Attribute error on node 'Cylinder': the input socket 'vertices' is write only.")

    @vertices.setter
    def vertices(self, value):
        self.set_input_socket('vertices', value)

    @property
    def side_segments(self):
        raise AttributeError("Attribute error on node 'Cylinder': the input socket 'side_segments' is write only.")

    @side_segments.setter
    def side_segments(self, value):
        self.set_input_socket('side_segments', value)

    @property
    def fill_segments(self):
        raise AttributeError("Attribute error on node 'Cylinder': the input socket 'fill_segments' is write only.")

    @fill_segments.setter
    def fill_segments(self, value):
        self.set_input_socket('fill_segments', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'Cylinder': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

    @property
    def depth(self):
        raise AttributeError("Attribute error on node 'Cylinder': the input socket 'depth' is write only.")

    @depth.setter
    def depth(self, value):
        self.set_input_socket('depth', value)

# ----------------------------------------------------------------------------------------------------
# Node FaceSetBoundaries for GeometryNodeMeshFaceSetBoundaries

class FaceSetBoundaries(Node):

    """Node *Face Set Boundaries*

    .. _FaceSetBoundaries:

    Node implementation:
        Mesh:
            face_set_boundaries 
        Face:
            face_set_boundaries 

    Args:
        face_set (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **boundary_edges** : Boolean

    .. blid:: GeometryNodeMeshFaceSetBoundaries

    """

    def __init__(self, face_set=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshFaceSetBoundaries', node_name='Face Set Boundaries', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'face_set' : 0, }
        self.outsockets = {'boundary_edges' : 0, }

        # Input sockets plugging

        if face_set        is not None: self.face_set        = face_set

    @property
    def boundary_edges(self):
        return self.get_output_socket('boundary_edges')

    @property
    def face_set(self):
        raise AttributeError("Attribute error on node 'FaceSetBoundaries': the input socket 'face_set' is write only.")

    @face_set.setter
    def face_set(self, value):
        self.set_input_socket('face_set', value)

# ----------------------------------------------------------------------------------------------------
# Node Grid for GeometryNodeMeshGrid

class Grid(Node):

    """Node *Grid*

    .. _Grid:

    Node implementation:
        Mesh:
            Grid 

    Args:
        size_x (DataSocket): Float
        size_y (DataSocket): Float
        vertices_x (DataSocket): Integer
        vertices_y (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeMeshGrid

    """

    def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshGrid', node_name='Grid', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'size_x' : 0, 'size_y' : 1, 'vertices_x' : 2, 'vertices_y' : 3, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if size_x          is not None: self.size_x          = size_x
        if size_y          is not None: self.size_y          = size_y
        if vertices_x      is not None: self.vertices_x      = vertices_x
        if vertices_y      is not None: self.vertices_y      = vertices_y

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def size_x(self):
        raise AttributeError("Attribute error on node 'Grid': the input socket 'size_x' is write only.")

    @size_x.setter
    def size_x(self, value):
        self.set_input_socket('size_x', value)

    @property
    def size_y(self):
        raise AttributeError("Attribute error on node 'Grid': the input socket 'size_y' is write only.")

    @size_y.setter
    def size_y(self, value):
        self.set_input_socket('size_y', value)

    @property
    def vertices_x(self):
        raise AttributeError("Attribute error on node 'Grid': the input socket 'vertices_x' is write only.")

    @vertices_x.setter
    def vertices_x(self, value):
        self.set_input_socket('vertices_x', value)

    @property
    def vertices_y(self):
        raise AttributeError("Attribute error on node 'Grid': the input socket 'vertices_y' is write only.")

    @vertices_y.setter
    def vertices_y(self, value):
        self.set_input_socket('vertices_y', value)

# ----------------------------------------------------------------------------------------------------
# Node IcoSphere for GeometryNodeMeshIcoSphere

class IcoSphere(Node):

    """Node *Ico Sphere*

    .. _IcoSphere:

    Node implementation:
        Mesh:
            IcoSphere 

    Args:
        radius (DataSocket): Float
        subdivisions (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeMeshIcoSphere

    """

    def __init__(self, radius=None, subdivisions=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshIcoSphere', node_name='Ico Sphere', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'radius' : 0, 'subdivisions' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if radius          is not None: self.radius          = radius
        if subdivisions    is not None: self.subdivisions    = subdivisions

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'IcoSphere': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

    @property
    def subdivisions(self):
        raise AttributeError("Attribute error on node 'IcoSphere': the input socket 'subdivisions' is write only.")

    @subdivisions.setter
    def subdivisions(self, value):
        self.set_input_socket('subdivisions', value)

# ----------------------------------------------------------------------------------------------------
# Node MeshLine for GeometryNodeMeshLine

class MeshLine(Node):

    """Node *Mesh Line*

    .. _MeshLine:

    Node implementation:
        Mesh:
            Line LineEndPoints LineOffset LineEndPointsResolution LineOffsetResolution 

    Args:
        count (DataSocket): Integer
        resolution (DataSocket): Float
        start_location (DataSocket): Vector
        offset (DataSocket): Vector
        count_mode (str): Node parameter, default = 'TOTAL' in ('TOTAL', 'RESOLUTION')
        mode (str): Node parameter, default = 'OFFSET' in ('OFFSET', 'END_POINTS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeMeshLine

    """

    def __init__(self, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None, node_color=None):

        super().__init__('GeometryNodeMeshLine', node_name='Mesh Line', label=label, node_color=node_color)

        # Node parameters

        self.bnode.count_mode      = count_mode
        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'count' : 0, 'resolution' : 1, 'start_location' : 2, 'offset' : 3, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if count           is not None: self.count           = count
        if resolution      is not None: self.resolution      = resolution
        if start_location  is not None: self.start_location  = start_location
        if offset          is not None: self.offset          = offset

    @property
    def count_mode(self):
        return self.bnode.count_mode

    @count_mode.setter
    def count_mode(self, value):
        self.bnode.count_mode = value

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def count(self):
        raise AttributeError("Attribute error on node 'MeshLine': the input socket 'count' is write only.")

    @count.setter
    def count(self, value):
        self.set_input_socket('count', value)

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'MeshLine': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

    @property
    def start_location(self):
        raise AttributeError("Attribute error on node 'MeshLine': the input socket 'start_location' is write only.")

    @start_location.setter
    def start_location(self, value):
        self.set_input_socket('start_location', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'MeshLine': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

# ----------------------------------------------------------------------------------------------------
# Node MeshToCurve for GeometryNodeMeshToCurve

class MeshToCurve(Node):

    """Node *Mesh to Curve*

    .. _MeshToCurve:

    Node implementation:
        Mesh:
            to_curve 
        Edge:
            to_curve 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeMeshToCurve

    """

    def __init__(self, mesh=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshToCurve', node_name='Mesh to Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'MeshToCurve': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'MeshToCurve': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node MeshToPoints for GeometryNodeMeshToPoints

class MeshToPoints(Node):

    """Node *Mesh to Points*

    .. _MeshToPoints:

    Node implementation:
        Mesh:
            to_points 
        Vertex:
            to_points 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        radius (DataSocket): Float
        mode (str): Node parameter, default = 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **points** : Points

    .. blid:: GeometryNodeMeshToPoints

    """

    def __init__(self, mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None, node_color=None):

        super().__init__('GeometryNodeMeshToPoints', node_name='Mesh to Points', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, 'position' : 2, 'radius' : 3, }
        self.outsockets = {'points' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection
        if position        is not None: self.position        = position
        if radius          is not None: self.radius          = radius

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def points(self):
        return self.get_output_socket('points')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'MeshToPoints': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'MeshToPoints': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def position(self):
        raise AttributeError("Attribute error on node 'MeshToPoints': the input socket 'position' is write only.")

    @position.setter
    def position(self, value):
        self.set_input_socket('position', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'MeshToPoints': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node MeshToVolume for GeometryNodeMeshToVolume

class MeshToVolume(Node):

    """Node *Mesh to Volume*

    .. _MeshToVolume:

    Node implementation:
        Mesh:
            to_volume 
        Vertex:
            to_volume 

    Args:
        mesh (DataSocket): Mesh
        density (DataSocket): Float
        voxel_size (DataSocket): Float
        voxel_amount (DataSocket): Float
        exterior_band_width (DataSocket): Float
        interior_band_width (DataSocket): Float
        fill_volume (DataSocket): Boolean
        resolution_mode (str): Node parameter, default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **volume** : Volume

    .. blid:: GeometryNodeMeshToVolume

    """

    def __init__(self, mesh=None, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT', label=None, node_color=None):

        super().__init__('GeometryNodeMeshToVolume', node_name='Mesh to Volume', label=label, node_color=node_color)

        # Node parameters

        self.bnode.resolution_mode = resolution_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'density' : 1, 'voxel_size' : 2, 'voxel_amount' : 3, 'exterior_band_width' : 4, 'interior_band_width' : 5, 'fill_volume' : 6, }
        self.outsockets = {'volume' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if density         is not None: self.density         = density
        if voxel_size      is not None: self.voxel_size      = voxel_size
        if voxel_amount    is not None: self.voxel_amount    = voxel_amount
        if exterior_band_width is not None: self.exterior_band_width = exterior_band_width
        if interior_band_width is not None: self.interior_band_width = interior_band_width
        if fill_volume     is not None: self.fill_volume     = fill_volume

    @property
    def resolution_mode(self):
        return self.bnode.resolution_mode

    @resolution_mode.setter
    def resolution_mode(self, value):
        self.bnode.resolution_mode = value

    @property
    def volume(self):
        return self.get_output_socket('volume')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def density(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'density' is write only.")

    @density.setter
    def density(self, value):
        self.set_input_socket('density', value)

    @property
    def voxel_size(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'voxel_size' is write only.")

    @voxel_size.setter
    def voxel_size(self, value):
        self.set_input_socket('voxel_size', value)

    @property
    def voxel_amount(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'voxel_amount' is write only.")

    @voxel_amount.setter
    def voxel_amount(self, value):
        self.set_input_socket('voxel_amount', value)

    @property
    def exterior_band_width(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'exterior_band_width' is write only.")

    @exterior_band_width.setter
    def exterior_band_width(self, value):
        self.set_input_socket('exterior_band_width', value)

    @property
    def interior_band_width(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'interior_band_width' is write only.")

    @interior_band_width.setter
    def interior_band_width(self, value):
        self.set_input_socket('interior_band_width', value)

    @property
    def fill_volume(self):
        raise AttributeError("Attribute error on node 'MeshToVolume': the input socket 'fill_volume' is write only.")

    @fill_volume.setter
    def fill_volume(self, value):
        self.set_input_socket('fill_volume', value)

# ----------------------------------------------------------------------------------------------------
# Node UvSphere for GeometryNodeMeshUVSphere

class UvSphere(Node):

    """Node *UV Sphere*

    .. _UvSphere:

    Node implementation:
        Mesh:
            UVSphere 

    Args:
        segments (DataSocket): Integer
        rings (DataSocket): Integer
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeMeshUVSphere

    """

    def __init__(self, segments=None, rings=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshUVSphere', node_name='UV Sphere', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'segments' : 0, 'rings' : 1, 'radius' : 2, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if segments        is not None: self.segments        = segments
        if rings           is not None: self.rings           = rings
        if radius          is not None: self.radius          = radius

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def segments(self):
        raise AttributeError("Attribute error on node 'UvSphere': the input socket 'segments' is write only.")

    @segments.setter
    def segments(self, value):
        self.set_input_socket('segments', value)

    @property
    def rings(self):
        raise AttributeError("Attribute error on node 'UvSphere': the input socket 'rings' is write only.")

    @rings.setter
    def rings(self, value):
        self.set_input_socket('rings', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'UvSphere': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node ObjectInfo for GeometryNodeObjectInfo

class ObjectInfo(Node):

    """Node *Object Info*

    .. _ObjectInfo:

    Node implementation:
        Object:
            info location rotation scale geometry 

    Args:
        object (DataSocket): Object
        as_instance (DataSocket): Boolean
        transform_space (str): Node parameter, default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **location** : Vector
        - **rotation** : Vector
        - **scale** : Vector
        - **geometry** : Geometry

    .. blid:: GeometryNodeObjectInfo

    """

    def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL', label=None, node_color=None):

        super().__init__('GeometryNodeObjectInfo', node_name='Object Info', label=label, node_color=node_color)

        # Node parameters

        self.bnode.transform_space = transform_space

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'object' : 0, 'as_instance' : 1, }
        self.outsockets = {'location' : 0, 'rotation' : 1, 'scale' : 2, 'geometry' : 3, }

        # Input sockets plugging

        if object          is not None: self.object          = object
        if as_instance     is not None: self.as_instance     = as_instance

    @property
    def transform_space(self):
        return self.bnode.transform_space

    @transform_space.setter
    def transform_space(self, value):
        self.bnode.transform_space = value

    @property
    def location(self):
        return self.get_output_socket('location')

    @property
    def rotation(self):
        return self.get_output_socket('rotation')

    @property
    def scale(self):
        return self.get_output_socket('scale')

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @property
    def object(self):
        raise AttributeError("Attribute error on node 'ObjectInfo': the input socket 'object' is write only.")

    @object.setter
    def object(self, value):
        self.set_input_socket('object', value)

    @property
    def as_instance(self):
        raise AttributeError("Attribute error on node 'ObjectInfo': the input socket 'as_instance' is write only.")

    @as_instance.setter
    def as_instance(self, value):
        self.set_input_socket('as_instance', value)

# ----------------------------------------------------------------------------------------------------
# Node OffsetCornerInFace for GeometryNodeOffsetCornerInFace

class OffsetCornerInFace(Node):

    """Node *Offset Corner in Face*

    .. _OffsetCornerInFace:

    Node implementation:
        Mesh:
            offset_corner_in_face 
        Corner:
            offset_in_face 

    Args:
        corner_index (DataSocket): Integer
        offset (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **corner_index** : Integer

    .. blid:: GeometryNodeOffsetCornerInFace

    """

    def __init__(self, corner_index=None, offset=None, label=None, node_color=None):

        super().__init__('GeometryNodeOffsetCornerInFace', node_name='Offset Corner in Face', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'corner_index' : 0, 'offset' : 1, }
        self.outsockets = {'corner_index' : 0, }

        # Input sockets plugging

        if corner_index    is not None: self.corner_index    = corner_index
        if offset          is not None: self.offset          = offset

    @property
    def corner_index(self):
        return self.get_output_socket('corner_index')

    @corner_index.setter
    def corner_index(self, value):
        self.set_input_socket('corner_index', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'OffsetCornerInFace': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

# ----------------------------------------------------------------------------------------------------
# Node OffsetPointInCurve for GeometryNodeOffsetPointInCurve

class OffsetPointInCurve(Node):

    """Node *Offset Point in Curve*

    .. _OffsetPointInCurve:

    Node implementation:
        Curve:
            offset_point 
        ControlPoint:
            offset 

    Args:
        point_index (DataSocket): Integer
        offset (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **is_valid_offset** : Boolean
        - **point_index** : Integer

    .. blid:: GeometryNodeOffsetPointInCurve

    """

    def __init__(self, point_index=None, offset=None, label=None, node_color=None):

        super().__init__('GeometryNodeOffsetPointInCurve', node_name='Offset Point in Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'point_index' : 0, 'offset' : 1, }
        self.outsockets = {'is_valid_offset' : 0, 'point_index' : 1, }

        # Input sockets plugging

        if point_index     is not None: self.point_index     = point_index
        if offset          is not None: self.offset          = offset

    @property
    def is_valid_offset(self):
        return self.get_output_socket('is_valid_offset')

    @property
    def point_index(self):
        return self.get_output_socket('point_index')

    @point_index.setter
    def point_index(self, value):
        self.set_input_socket('point_index', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'OffsetPointInCurve': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

# ----------------------------------------------------------------------------------------------------
# Node Points for GeometryNodePoints

class Points(Node):

    """Node *Points*

    .. _Points:

    Node implementation:
        Points:
            Points 

    Args:
        count (DataSocket): Integer
        position (DataSocket): Vector
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodePoints

    """

    def __init__(self, count=None, position=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodePoints', node_name='Points', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'count' : 0, 'position' : 1, 'radius' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if count           is not None: self.count           = count
        if position        is not None: self.position        = position
        if radius          is not None: self.radius          = radius

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @property
    def count(self):
        raise AttributeError("Attribute error on node 'Points': the input socket 'count' is write only.")

    @count.setter
    def count(self, value):
        self.set_input_socket('count', value)

    @property
    def position(self):
        raise AttributeError("Attribute error on node 'Points': the input socket 'position' is write only.")

    @position.setter
    def position(self, value):
        self.set_input_socket('position', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'Points': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node PointsOfCurve for GeometryNodePointsOfCurve

class PointsOfCurve(Node):

    """Node *Points of Curve*

    .. _PointsOfCurve:

    Node implementation:
        Curve:
            points_of_curve 
        Spline:
            points 

    Args:
        curve_index (DataSocket): Integer
        weights (DataSocket): Float
        sort_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **point_index** : Integer
        - **total** : Integer

    .. blid:: GeometryNodePointsOfCurve

    """

    def __init__(self, curve_index=None, weights=None, sort_index=None, label=None, node_color=None):

        super().__init__('GeometryNodePointsOfCurve', node_name='Points of Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve_index' : 0, 'weights' : 1, 'sort_index' : 2, }
        self.outsockets = {'point_index' : 0, 'total' : 1, }

        # Input sockets plugging

        if curve_index     is not None: self.curve_index     = curve_index
        if weights         is not None: self.weights         = weights
        if sort_index      is not None: self.sort_index      = sort_index

    @property
    def point_index(self):
        return self.get_output_socket('point_index')

    @property
    def total(self):
        return self.get_output_socket('total')

    @property
    def curve_index(self):
        raise AttributeError("Attribute error on node 'PointsOfCurve': the input socket 'curve_index' is write only.")

    @curve_index.setter
    def curve_index(self, value):
        self.set_input_socket('curve_index', value)

    @property
    def weights(self):
        raise AttributeError("Attribute error on node 'PointsOfCurve': the input socket 'weights' is write only.")

    @weights.setter
    def weights(self, value):
        self.set_input_socket('weights', value)

    @property
    def sort_index(self):
        raise AttributeError("Attribute error on node 'PointsOfCurve': the input socket 'sort_index' is write only.")

    @sort_index.setter
    def sort_index(self, value):
        self.set_input_socket('sort_index', value)

# ----------------------------------------------------------------------------------------------------
# Node PointsToVertices for GeometryNodePointsToVertices

class PointsToVertices(Node):

    """Node *Points to Vertices*

    .. _PointsToVertices:

    Node implementation:
        Points:
            to_vertices 
        CloudPoint:
            to_vertices 

    Args:
        points (DataSocket): Points
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodePointsToVertices

    """

    def __init__(self, points=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodePointsToVertices', node_name='Points to Vertices', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'selection' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if selection       is not None: self.selection       = selection

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def points(self):
        raise AttributeError("Attribute error on node 'PointsToVertices': the input socket 'points' is write only.")

    @points.setter
    def points(self, value):
        self.set_input_socket('points', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'PointsToVertices': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node PointsToVolume for GeometryNodePointsToVolume

class PointsToVolume(Node):

    """Node *Points to Volume*

    .. _PointsToVolume:

    Node implementation:
        Points:
            to_volume to_volume_size to_volume_amount 

    Args:
        points (DataSocket): Points
        density (DataSocket): Float
        voxel_size (DataSocket): Float
        voxel_amount (DataSocket): Float
        radius (DataSocket): Float
        resolution_mode (str): Node parameter, default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **volume** : Volume

    .. blid:: GeometryNodePointsToVolume

    """

    def __init__(self, points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None, node_color=None):

        super().__init__('GeometryNodePointsToVolume', node_name='Points to Volume', label=label, node_color=node_color)

        # Node parameters

        self.bnode.resolution_mode = resolution_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'density' : 1, 'voxel_size' : 2, 'voxel_amount' : 3, 'radius' : 4, }
        self.outsockets = {'volume' : 0, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if density         is not None: self.density         = density
        if voxel_size      is not None: self.voxel_size      = voxel_size
        if voxel_amount    is not None: self.voxel_amount    = voxel_amount
        if radius          is not None: self.radius          = radius

    @property
    def resolution_mode(self):
        return self.bnode.resolution_mode

    @resolution_mode.setter
    def resolution_mode(self, value):
        self.bnode.resolution_mode = value

    @property
    def volume(self):
        return self.get_output_socket('volume')

    @property
    def points(self):
        raise AttributeError("Attribute error on node 'PointsToVolume': the input socket 'points' is write only.")

    @points.setter
    def points(self, value):
        self.set_input_socket('points', value)

    @property
    def density(self):
        raise AttributeError("Attribute error on node 'PointsToVolume': the input socket 'density' is write only.")

    @density.setter
    def density(self, value):
        self.set_input_socket('density', value)

    @property
    def voxel_size(self):
        raise AttributeError("Attribute error on node 'PointsToVolume': the input socket 'voxel_size' is write only.")

    @voxel_size.setter
    def voxel_size(self, value):
        self.set_input_socket('voxel_size', value)

    @property
    def voxel_amount(self):
        raise AttributeError("Attribute error on node 'PointsToVolume': the input socket 'voxel_amount' is write only.")

    @voxel_amount.setter
    def voxel_amount(self, value):
        self.set_input_socket('voxel_amount', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'PointsToVolume': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node GeometryProximity for GeometryNodeProximity

class GeometryProximity(Node):

    """Node *Geometry Proximity*

    .. _GeometryProximity:

    Node implementation:
        Geometry:
            proximity proximity_points proximity_edges proximity_faces 
        ('Vertex', 'ControlPoint', 'CloudPoint'):
            proximity 
        Edge:
            proximity 
        Face:
            proximity 

    Args:
        target (DataSocket): Geometry
        source_position (DataSocket): Vector
        target_element (str): Node parameter, default = 'FACES' in ('POINTS', 'EDGES', 'FACES')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **position** : Vector
        - **distance** : Float

    .. blid:: GeometryNodeProximity

    """

    def __init__(self, target=None, source_position=None, target_element='FACES', label=None, node_color=None):

        super().__init__('GeometryNodeProximity', node_name='Geometry Proximity', label=label, node_color=node_color)

        # Node parameters

        self.bnode.target_element  = target_element

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'target' : 0, 'source_position' : 1, }
        self.outsockets = {'position' : 0, 'distance' : 1, }

        # Input sockets plugging

        if target          is not None: self.target          = target
        if source_position is not None: self.source_position = source_position

    @property
    def target_element(self):
        return self.bnode.target_element

    @target_element.setter
    def target_element(self, value):
        self.bnode.target_element = value

    @property
    def position(self):
        return self.get_output_socket('position')

    @property
    def distance(self):
        return self.get_output_socket('distance')

    @property
    def target(self):
        raise AttributeError("Attribute error on node 'GeometryProximity': the input socket 'target' is write only.")

    @target.setter
    def target(self, value):
        self.set_input_socket('target', value)

    @property
    def source_position(self):
        raise AttributeError("Attribute error on node 'GeometryProximity': the input socket 'source_position' is write only.")

    @source_position.setter
    def source_position(self, value):
        self.set_input_socket('source_position', value)

# ----------------------------------------------------------------------------------------------------
# Node Raycast for GeometryNodeRaycast

class Raycast(Node):

    """Node *Raycast*

    .. _Raycast:

    Node implementation:
        Geometry:
            raycast raycast_interpolated raycast_nearest 

    Args:
        target_geometry (DataSocket): Geometry
        attribute (DataSocket): ``data_type`` dependant
        source_position (DataSocket): Vector
        ray_direction (DataSocket): Vector
        ray_length (DataSocket): Float
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        mapping (str): Node parameter, default = 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **is_hit** : Boolean
        - **hit_position** : Vector
        - **hit_normal** : Vector
        - **hit_distance** : Float
        - **attribute** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['attribute']
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeRaycast

    """

    def __init__(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None, node_color=None):

        super().__init__('GeometryNodeRaycast', node_name='Raycast', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(attribute) if data_type is None else data_type
        self.bnode.mapping         = mapping

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'target_geometry' : 0, 'attribute' : [1, 2, 3, 4, 5], 'source_position' : 6, 'ray_direction' : 7, 'ray_length' : 8, }
        self.outsockets = {'is_hit' : 0, 'hit_position' : 1, 'hit_normal' : 2, 'hit_distance' : 3, 'attribute' : [4, 5, 6, 7, 8], }

        # Input sockets plugging

        if target_geometry is not None: self.target_geometry = target_geometry
        if attribute       is not None: self.attribute       = attribute
        if source_position is not None: self.source_position = source_position
        if ray_direction   is not None: self.ray_direction   = ray_direction
        if ray_length      is not None: self.ray_length      = ray_length

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def mapping(self):
        return self.bnode.mapping

    @mapping.setter
    def mapping(self, value):
        self.bnode.mapping = value

    @property
    def is_hit(self):
        return self.get_output_socket('is_hit')

    @property
    def hit_position(self):
        return self.get_output_socket('hit_position')

    @property
    def hit_normal(self):
        return self.get_output_socket('hit_normal')

    @property
    def hit_distance(self):
        return self.get_output_socket('hit_distance')

    @property
    def attribute(self):
        return self.get_output_socket('attribute')

    @property
    def target_geometry(self):
        raise AttributeError("Attribute error on node 'Raycast': the input socket 'target_geometry' is write only.")

    @target_geometry.setter
    def target_geometry(self, value):
        self.set_input_socket('target_geometry', value)

    @attribute.setter
    def attribute(self, value):
        self.set_input_socket('attribute', value)

    @property
    def source_position(self):
        raise AttributeError("Attribute error on node 'Raycast': the input socket 'source_position' is write only.")

    @source_position.setter
    def source_position(self, value):
        self.set_input_socket('source_position', value)

    @property
    def ray_direction(self):
        raise AttributeError("Attribute error on node 'Raycast': the input socket 'ray_direction' is write only.")

    @ray_direction.setter
    def ray_direction(self, value):
        self.set_input_socket('ray_direction', value)

    @property
    def ray_length(self):
        raise AttributeError("Attribute error on node 'Raycast': the input socket 'ray_length' is write only.")

    @ray_length.setter
    def ray_length(self, value):
        self.set_input_socket('ray_length', value)

# ----------------------------------------------------------------------------------------------------
# Node RealizeInstances for GeometryNodeRealizeInstances

class RealizeInstances(Node):

    """Node *Realize Instances*

    .. _RealizeInstances:

    Node implementation:
        Instances:
            realize 

    Args:
        geometry (DataSocket): Geometry
        legacy_behavior (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeRealizeInstances

    """

    def __init__(self, geometry=None, legacy_behavior=False, label=None, node_color=None):

        super().__init__('GeometryNodeRealizeInstances', node_name='Realize Instances', label=label, node_color=node_color)

        # Node parameters

        self.bnode.legacy_behavior = legacy_behavior

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

    @property
    def legacy_behavior(self):
        return self.bnode.legacy_behavior

    @legacy_behavior.setter
    def legacy_behavior(self, value):
        self.bnode.legacy_behavior = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node RemoveNamedAttribute for GeometryNodeRemoveAttribute

class RemoveNamedAttribute(Node):

    """Node *Remove Named Attribute*

    .. _RemoveNamedAttribute:

    Node implementation:
        Geometry:
            remove_named_attribute 
        Domain:
            remove_named_attribute 

    Args:
        geometry (DataSocket): Geometry
        name (DataSocket): String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeRemoveAttribute

    """

    def __init__(self, geometry=None, name=None, label=None, node_color=None):

        super().__init__('GeometryNodeRemoveAttribute', node_name='Remove Named Attribute', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'name' : 1, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if name            is not None: self.name            = name

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def name(self):
        raise AttributeError("Attribute error on node 'RemoveNamedAttribute': the input socket 'name' is write only.")

    @name.setter
    def name(self, value):
        self.set_input_socket('name', value)

# ----------------------------------------------------------------------------------------------------
# Node ReplaceMaterial for GeometryNodeReplaceMaterial

class ReplaceMaterial(Node):

    """Node *Replace Material*

    .. _ReplaceMaterial:

    Node implementation:
        Geometry:
            replace_material 

    Args:
        geometry (DataSocket): Geometry
        old (DataSocket): Material
        new (DataSocket): Material
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeReplaceMaterial

    """

    def __init__(self, geometry=None, old=None, new=None, label=None, node_color=None):

        super().__init__('GeometryNodeReplaceMaterial', node_name='Replace Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'old' : 1, 'new' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if old             is not None: self.old             = old
        if new             is not None: self.new             = new

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def old(self):
        raise AttributeError("Attribute error on node 'ReplaceMaterial': the input socket 'old' is write only.")

    @old.setter
    def old(self, value):
        self.set_input_socket('old', value)

    @property
    def new(self):
        raise AttributeError("Attribute error on node 'ReplaceMaterial': the input socket 'new' is write only.")

    @new.setter
    def new(self, value):
        self.set_input_socket('new', value)

# ----------------------------------------------------------------------------------------------------
# Node ResampleCurve for GeometryNodeResampleCurve

class ResampleCurve(Node):

    """Node *Resample Curve*

    .. _ResampleCurve:

    Node implementation:
        Curve:
            resample resample_count resample_length resample_evaluated 
        Spline:
            resample resample_count resample_length resample_evaluated 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        count (DataSocket): Integer
        length (DataSocket): Float
        mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeResampleCurve

    """

    def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT', label=None, node_color=None):

        super().__init__('GeometryNodeResampleCurve', node_name='Resample Curve', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, 'count' : 2, 'length' : 3, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection
        if count           is not None: self.count           = count
        if length          is not None: self.length          = length

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'ResampleCurve': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def count(self):
        raise AttributeError("Attribute error on node 'ResampleCurve': the input socket 'count' is write only.")

    @count.setter
    def count(self, value):
        self.set_input_socket('count', value)

    @property
    def length(self):
        raise AttributeError("Attribute error on node 'ResampleCurve': the input socket 'length' is write only.")

    @length.setter
    def length(self, value):
        self.set_input_socket('length', value)

# ----------------------------------------------------------------------------------------------------
# Node ReverseCurve for GeometryNodeReverseCurve

class ReverseCurve(Node):

    """Node *Reverse Curve*

    .. _ReverseCurve:

    Node implementation:
        Curve:
            reverse 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeReverseCurve

    """

    def __init__(self, curve=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeReverseCurve', node_name='Reverse Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'ReverseCurve': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node RotateInstances for GeometryNodeRotateInstances

class RotateInstances(Node):

    """Node *Rotate Instances*

    .. _RotateInstances:

    Node implementation:
        Instances:
            rotate 
        Instance:
            rotate 

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        rotation (DataSocket): Vector
        pivot_point (DataSocket): Vector
        local_space (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **instances** : Instances

    .. blid:: GeometryNodeRotateInstances

    """

    def __init__(self, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, label=None, node_color=None):

        super().__init__('GeometryNodeRotateInstances', node_name='Rotate Instances', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'rotation' : 2, 'pivot_point' : 3, 'local_space' : 4, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if rotation        is not None: self.rotation        = rotation
        if pivot_point     is not None: self.pivot_point     = pivot_point
        if local_space     is not None: self.local_space     = local_space

    @property
    def instances(self):
        return self.get_output_socket('instances')

    @instances.setter
    def instances(self, value):
        self.set_input_socket('instances', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'RotateInstances': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def rotation(self):
        raise AttributeError("Attribute error on node 'RotateInstances': the input socket 'rotation' is write only.")

    @rotation.setter
    def rotation(self, value):
        self.set_input_socket('rotation', value)

    @property
    def pivot_point(self):
        raise AttributeError("Attribute error on node 'RotateInstances': the input socket 'pivot_point' is write only.")

    @pivot_point.setter
    def pivot_point(self, value):
        self.set_input_socket('pivot_point', value)

    @property
    def local_space(self):
        raise AttributeError("Attribute error on node 'RotateInstances': the input socket 'local_space' is write only.")

    @local_space.setter
    def local_space(self, value):
        self.set_input_socket('local_space', value)

# ----------------------------------------------------------------------------------------------------
# Node SampleCurve for GeometryNodeSampleCurve

class SampleCurve(Node):

    """Node *Sample Curve*

    .. _SampleCurve:

    Node implementation:
        Curve:
            sample 

    Args:
        curves (DataSocket): Curve
        value (DataSocket): ``data_type`` dependant
        factor (DataSocket): Float
        length (DataSocket): Float
        curve_index (DataSocket): Integer
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        mode (str): Node parameter, default = 'FACTOR' in ('FACTOR', 'LENGTH')
        use_all_curves (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant
        - **position** : Vector
        - **tangent** : Vector
        - **normal** : Vector

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeSampleCurve

    """

    def __init__(self, curves=None, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, label=None, node_color=None):

        super().__init__('GeometryNodeSampleCurve', node_name='Sample Curve', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.mode            = mode
        self.bnode.use_all_curves  = use_all_curves

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curves' : 0, 'value' : [1, 2, 3, 4, 5], 'factor' : 6, 'length' : 7, 'curve_index' : 8, }
        self.outsockets = {'value' : [0, 1, 2, 3, 4], 'position' : 5, 'tangent' : 6, 'normal' : 7, }

        # Input sockets plugging

        if curves          is not None: self.curves          = curves
        if value           is not None: self.value           = value
        if factor          is not None: self.factor          = factor
        if length          is not None: self.length          = length
        if curve_index     is not None: self.curve_index     = curve_index

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def use_all_curves(self):
        return self.bnode.use_all_curves

    @use_all_curves.setter
    def use_all_curves(self, value):
        self.bnode.use_all_curves = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def position(self):
        return self.get_output_socket('position')

    @property
    def tangent(self):
        return self.get_output_socket('tangent')

    @property
    def normal(self):
        return self.get_output_socket('normal')

    @property
    def curves(self):
        raise AttributeError("Attribute error on node 'SampleCurve': the input socket 'curves' is write only.")

    @curves.setter
    def curves(self, value):
        self.set_input_socket('curves', value)

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def factor(self):
        raise AttributeError("Attribute error on node 'SampleCurve': the input socket 'factor' is write only.")

    @factor.setter
    def factor(self, value):
        self.set_input_socket('factor', value)

    @property
    def length(self):
        raise AttributeError("Attribute error on node 'SampleCurve': the input socket 'length' is write only.")

    @length.setter
    def length(self, value):
        self.set_input_socket('length', value)

    @property
    def curve_index(self):
        raise AttributeError("Attribute error on node 'SampleCurve': the input socket 'curve_index' is write only.")

    @curve_index.setter
    def curve_index(self, value):
        self.set_input_socket('curve_index', value)

# ----------------------------------------------------------------------------------------------------
# Node SampleIndex for GeometryNodeSampleIndex

class SampleIndex(Node):

    """Node *Sample Index*

    .. _SampleIndex:

    Node implementation:
        Geometry:
            sample_index 
        Domain:
            sample_index 

    Args:
        geometry (DataSocket): Geometry
        value (DataSocket): ``data_type`` dependant
        index (DataSocket): Integer
        clamp (bool): Node parameter, default = False
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeSampleIndex

    """

    def __init__(self, geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeSampleIndex', node_name='Sample Index', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.clamp           = clamp
        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'value' : [1, 2, 3, 4, 5], 'index' : 6, }
        self.outsockets = {'value' : [0, 1, 2, 3, 4], }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if value           is not None: self.value           = value
        if index           is not None: self.index           = index

    @property
    def clamp(self):
        return self.bnode.clamp

    @clamp.setter
    def clamp(self, value):
        self.bnode.clamp = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'SampleIndex': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def index(self):
        raise AttributeError("Attribute error on node 'SampleIndex': the input socket 'index' is write only.")

    @index.setter
    def index(self, value):
        self.set_input_socket('index', value)

# ----------------------------------------------------------------------------------------------------
# Node SampleNearest for GeometryNodeSampleNearest

class SampleNearest(Node):

    """Node *Sample Nearest*

    .. _SampleNearest:

    Node implementation:
        Geometry:
            sample_nearest 
        ('Vertex', 'Edge', 'Face', 'Corner'):
            sample_nearest 

    Args:
        geometry (DataSocket): Geometry
        sample_position (DataSocket): Vector
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **index** : Integer

    .. blid:: GeometryNodeSampleNearest

    """

    def __init__(self, geometry=None, sample_position=None, domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeSampleNearest', node_name='Sample Nearest', label=label, node_color=node_color)

        # Node parameters

        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'sample_position' : 1, }
        self.outsockets = {'index' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if sample_position is not None: self.sample_position = sample_position

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def index(self):
        return self.get_output_socket('index')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'SampleNearest': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def sample_position(self):
        raise AttributeError("Attribute error on node 'SampleNearest': the input socket 'sample_position' is write only.")

    @sample_position.setter
    def sample_position(self, value):
        self.set_input_socket('sample_position', value)

# ----------------------------------------------------------------------------------------------------
# Node SampleNearestSurface for GeometryNodeSampleNearestSurface

class SampleNearestSurface(Node):

    """Node *Sample Nearest Surface*

    .. _SampleNearestSurface:

    Node implementation:
        Mesh:
            sample_nearest_surface 

    Args:
        mesh (DataSocket): Mesh
        value (DataSocket): ``data_type`` dependant
        sample_position (DataSocket): Vector
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeSampleNearestSurface

    """

    def __init__(self, mesh=None, value=None, sample_position=None, data_type='FLOAT', label=None, node_color=None):

        super().__init__('GeometryNodeSampleNearestSurface', node_name='Sample Nearest Surface', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'value' : [1, 2, 3, 4, 5], 'sample_position' : 6, }
        self.outsockets = {'value' : [0, 1, 2, 3, 4], }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if value           is not None: self.value           = value
        if sample_position is not None: self.sample_position = sample_position

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'SampleNearestSurface': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def sample_position(self):
        raise AttributeError("Attribute error on node 'SampleNearestSurface': the input socket 'sample_position' is write only.")

    @sample_position.setter
    def sample_position(self, value):
        self.set_input_socket('sample_position', value)

# ----------------------------------------------------------------------------------------------------
# Node SampleUvSurface for GeometryNodeSampleUVSurface

class SampleUvSurface(Node):

    """Node *Sample UV Surface*

    .. _SampleUvSurface:

    Node implementation:
        Mesh:
            sample_uv_surface 

    Args:
        mesh (DataSocket): Mesh
        value (DataSocket): ``data_type`` dependant
        source_uv_map (DataSocket): Vector
        sample_uv (DataSocket): Vector
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : ``data_type`` dependant
        - **is_valid** : Boolean

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeSampleUVSurface

    """

    def __init__(self, mesh=None, value=None, source_uv_map=None, sample_uv=None, data_type='FLOAT', label=None, node_color=None):

        super().__init__('GeometryNodeSampleUVSurface', node_name='Sample UV Surface', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'value' : [1, 2, 3, 4, 5], 'source_uv_map' : 6, 'sample_uv' : 7, }
        self.outsockets = {'value' : [0, 1, 2, 3, 4], 'is_valid' : 5, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if value           is not None: self.value           = value
        if source_uv_map   is not None: self.source_uv_map   = source_uv_map
        if sample_uv       is not None: self.sample_uv       = sample_uv

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def is_valid(self):
        return self.get_output_socket('is_valid')

    @property
    def mesh(self):
        raise AttributeError("Attribute error on node 'SampleUvSurface': the input socket 'mesh' is write only.")

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def source_uv_map(self):
        raise AttributeError("Attribute error on node 'SampleUvSurface': the input socket 'source_uv_map' is write only.")

    @source_uv_map.setter
    def source_uv_map(self, value):
        self.set_input_socket('source_uv_map', value)

    @property
    def sample_uv(self):
        raise AttributeError("Attribute error on node 'SampleUvSurface': the input socket 'sample_uv' is write only.")

    @sample_uv.setter
    def sample_uv(self, value):
        self.set_input_socket('sample_uv', value)

# ----------------------------------------------------------------------------------------------------
# Node ScaleElements for GeometryNodeScaleElements

class ScaleElements(Node):

    """Node *Scale Elements*

    .. _ScaleElements:

    Node implementation:
        Mesh:
            scale_elements scale_uniform scale_single_axis 
        Face:
            scale_uniform scale_single_axis 
        Edge:
            scale_uniform scale_single_axis 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        scale (DataSocket): Float
        center (DataSocket): Vector
        axis (DataSocket): Vector
        domain (str): Node parameter, default = 'FACE' in ('FACE', 'EDGE')
        scale_mode (str): Node parameter, default = 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeScaleElements

    """

    def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None, node_color=None):

        super().__init__('GeometryNodeScaleElements', node_name='Scale Elements', label=label, node_color=node_color)

        # Node parameters

        self.bnode.domain          = domain
        self.bnode.scale_mode      = scale_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'scale' : 2, 'center' : 3, 'axis' : 4, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if scale           is not None: self.scale           = scale
        if center          is not None: self.center          = center
        if axis            is not None: self.axis            = axis

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def scale_mode(self):
        return self.bnode.scale_mode

    @scale_mode.setter
    def scale_mode(self, value):
        self.bnode.scale_mode = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'ScaleElements': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'ScaleElements': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def center(self):
        raise AttributeError("Attribute error on node 'ScaleElements': the input socket 'center' is write only.")

    @center.setter
    def center(self, value):
        self.set_input_socket('center', value)

    @property
    def axis(self):
        raise AttributeError("Attribute error on node 'ScaleElements': the input socket 'axis' is write only.")

    @axis.setter
    def axis(self, value):
        self.set_input_socket('axis', value)

# ----------------------------------------------------------------------------------------------------
# Node ScaleInstances for GeometryNodeScaleInstances

class ScaleInstances(Node):

    """Node *Scale Instances*

    .. _ScaleInstances:

    Node implementation:
        Instances:
            set_scale 
        Instance:
            set_scale 

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        scale (DataSocket): Vector
        center (DataSocket): Vector
        local_space (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **instances** : Instances

    .. blid:: GeometryNodeScaleInstances

    """

    def __init__(self, instances=None, selection=None, scale=None, center=None, local_space=None, label=None, node_color=None):

        super().__init__('GeometryNodeScaleInstances', node_name='Scale Instances', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'scale' : 2, 'center' : 3, 'local_space' : 4, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if scale           is not None: self.scale           = scale
        if center          is not None: self.center          = center
        if local_space     is not None: self.local_space     = local_space

    @property
    def instances(self):
        return self.get_output_socket('instances')

    @instances.setter
    def instances(self, value):
        self.set_input_socket('instances', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'ScaleInstances': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'ScaleInstances': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def center(self):
        raise AttributeError("Attribute error on node 'ScaleInstances': the input socket 'center' is write only.")

    @center.setter
    def center(self, value):
        self.set_input_socket('center', value)

    @property
    def local_space(self):
        raise AttributeError("Attribute error on node 'ScaleInstances': the input socket 'local_space' is write only.")

    @local_space.setter
    def local_space(self, value):
        self.set_input_socket('local_space', value)

# ----------------------------------------------------------------------------------------------------
# Node SelfObject for GeometryNodeSelfObject

class SelfObject(Node):

    """Node *Self Object*

    .. _SelfObject:

    Node implementation:
        Object:
            Self 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **self_object** : Object

    .. blid:: GeometryNodeSelfObject

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSelfObject', node_name='Self Object', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'self_object' : 0, }

    @property
    def self_object(self):
        return self.get_output_socket('self_object')

# ----------------------------------------------------------------------------------------------------
# Node SeparateComponents for GeometryNodeSeparateComponents

class SeparateComponents(Node):

    """Node *Separate Components*

    .. _SeparateComponents:

    Node implementation:
        Geometry:
            separate_components mesh_component curve_component points_component volume_component instances_component 

    Args:
        geometry (DataSocket): Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh
        - **point_cloud** : Geometry
        - **curve** : Curve
        - **volume** : Volume
        - **instances** : Instances

    .. blid:: GeometryNodeSeparateComponents

    """

    def __init__(self, geometry=None, label=None, node_color=None):

        super().__init__('GeometryNodeSeparateComponents', node_name='Separate Components', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'mesh' : 0, 'point_cloud' : 1, 'curve' : 2, 'volume' : 3, 'instances' : 4, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def point_cloud(self):
        return self.get_output_socket('point_cloud')

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @property
    def volume(self):
        return self.get_output_socket('volume')

    @property
    def instances(self):
        return self.get_output_socket('instances')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'SeparateComponents': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

# ----------------------------------------------------------------------------------------------------
# Node SeparateGeometry for GeometryNodeSeparateGeometry

class SeparateGeometry(Node):

    """Node *Separate Geometry*

    .. _SeparateGeometry:

    Node implementation:
        Geometry:
            separate 
        ('Vertex', 'Edge', 'Face', 'ControlPoint', 'Spline', 'Instance'):
            separate 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **selection** : Geometry
        - **inverted** : Geometry

    .. blid:: GeometryNodeSeparateGeometry

    """

    def __init__(self, geometry=None, selection=None, domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeSeparateGeometry', node_name='Separate Geometry', label=label, node_color=node_color)

        # Node parameters

        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, }
        self.outsockets = {'selection' : 0, 'inverted' : 1, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def selection(self):
        return self.get_output_socket('selection')

    @property
    def inverted(self):
        return self.get_output_socket('inverted')

    @property
    def geometry(self):
        raise AttributeError("Attribute error on node 'SeparateGeometry': the input socket 'geometry' is write only.")

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node SetHandlePositions for GeometryNodeSetCurveHandlePositions

class SetHandlePositions(Node):

    """Node *Set Handle Positions*

    .. _SetHandlePositions:

    Node implementation:
        ControlPoint:
            set_handle_positions set_handle_positions_left set_handle_positions_right left_handle_positions right_handle_positions 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        offset (DataSocket): Vector
        mode (str): Node parameter, default = 'LEFT' in ('LEFT', 'RIGHT')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeSetCurveHandlePositions

    """

    def __init__(self, curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveHandlePositions', node_name='Set Handle Positions', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, 'position' : 2, 'offset' : 3, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection
        if position        is not None: self.position        = position
        if offset          is not None: self.offset          = offset

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetHandlePositions': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def position(self):
        raise AttributeError("Attribute error on node 'SetHandlePositions': the input socket 'position' is write only.")

    @position.setter
    def position(self, value):
        self.set_input_socket('position', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'SetHandlePositions': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

# ----------------------------------------------------------------------------------------------------
# Node SetCurveNormal for GeometryNodeSetCurveNormal

class SetCurveNormal(Node):

    """Node *Set Curve Normal*

    .. _SetCurveNormal:

    Node implementation:
        Spline:
            set_normal normal 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        mode (str): Node parameter, default = 'MINIMUM_TWIST' in ('MINIMUM_TWIST', 'Z_UP')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeSetCurveNormal

    """

    def __init__(self, curve=None, selection=None, mode='MINIMUM_TWIST', label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveNormal', node_name='Set Curve Normal', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetCurveNormal': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node SetCurveRadius for GeometryNodeSetCurveRadius

class SetCurveRadius(Node):

    """Node *Set Curve Radius*

    .. _SetCurveRadius:

    Node implementation:
        ControlPoint:
            set_radius radius 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeSetCurveRadius

    """

    def __init__(self, curve=None, selection=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveRadius', node_name='Set Curve Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, 'radius' : 2, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection
        if radius          is not None: self.radius          = radius

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetCurveRadius': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'SetCurveRadius': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node SetCurveTilt for GeometryNodeSetCurveTilt

class SetCurveTilt(Node):

    """Node *Set Curve Tilt*

    .. _SetCurveTilt:

    Node implementation:
        ControlPoint:
            set_tilt tilt 

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        tilt (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeSetCurveTilt

    """

    def __init__(self, curve=None, selection=None, tilt=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveTilt', node_name='Set Curve Tilt', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, 'tilt' : 2, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection
        if tilt            is not None: self.tilt            = tilt

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetCurveTilt': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def tilt(self):
        raise AttributeError("Attribute error on node 'SetCurveTilt': the input socket 'tilt' is write only.")

    @tilt.setter
    def tilt(self, value):
        self.set_input_socket('tilt', value)

# ----------------------------------------------------------------------------------------------------
# Node SetID for GeometryNodeSetID

class SetID(Node):

    """Node *Set ID*

    .. _SetID:

    Node implementation:
        Geometry:
            set_ID 
        Domain:
            set_ID ID 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        ID (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetID

    """

    def __init__(self, geometry=None, selection=None, ID=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetID', node_name='Set ID', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'ID' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if ID              is not None: self.ID              = ID

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetID': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def ID(self):
        raise AttributeError("Attribute error on node 'SetID': the input socket 'ID' is write only.")

    @ID.setter
    def ID(self, value):
        self.set_input_socket('ID', value)

# ----------------------------------------------------------------------------------------------------
# Node SetMaterial for GeometryNodeSetMaterial

class SetMaterial(Node):

    """Node *Set Material*

    .. _SetMaterial:

    Node implementation:
        Geometry:
            set_material 
        ('Face', 'Spline'):
            set_material material material 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        material (DataSocket): Material
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetMaterial

    """

    def __init__(self, geometry=None, selection=None, material=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetMaterial', node_name='Set Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'material' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if material        is not None: self.material        = material

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetMaterial': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def material(self):
        raise AttributeError("Attribute error on node 'SetMaterial': the input socket 'material' is write only.")

    @material.setter
    def material(self, value):
        self.set_input_socket('material', value)

# ----------------------------------------------------------------------------------------------------
# Node SetMaterialIndex for GeometryNodeSetMaterialIndex

class SetMaterialIndex(Node):

    """Node *Set Material Index*

    .. _SetMaterialIndex:

    Node implementation:
        Geometry:
            set_material_index 
        Domain:
            set_material_index 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        material_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetMaterialIndex

    """

    def __init__(self, geometry=None, selection=None, material_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetMaterialIndex', node_name='Set Material Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'material_index' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if material_index  is not None: self.material_index  = material_index

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetMaterialIndex': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def material_index(self):
        raise AttributeError("Attribute error on node 'SetMaterialIndex': the input socket 'material_index' is write only.")

    @material_index.setter
    def material_index(self, value):
        self.set_input_socket('material_index', value)

# ----------------------------------------------------------------------------------------------------
# Node SetPointRadius for GeometryNodeSetPointRadius

class SetPointRadius(Node):

    """Node *Set Point Radius*

    .. _SetPointRadius:

    Node implementation:
        Points:
            set_point_radius 
        CloudPoint:
            radius 

    Args:
        points (DataSocket): Points
        selection (DataSocket): Boolean
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **points** : Points

    .. blid:: GeometryNodeSetPointRadius

    """

    def __init__(self, points=None, selection=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetPointRadius', node_name='Set Point Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'selection' : 1, 'radius' : 2, }
        self.outsockets = {'points' : 0, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if selection       is not None: self.selection       = selection
        if radius          is not None: self.radius          = radius

    @property
    def points(self):
        return self.get_output_socket('points')

    @points.setter
    def points(self, value):
        self.set_input_socket('points', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetPointRadius': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def radius(self):
        raise AttributeError("Attribute error on node 'SetPointRadius': the input socket 'radius' is write only.")

    @radius.setter
    def radius(self, value):
        self.set_input_socket('radius', value)

# ----------------------------------------------------------------------------------------------------
# Node SetPosition for GeometryNodeSetPosition

class SetPosition(Node):

    """Node *Set Position*

    .. _SetPosition:

    Node implementation:
        Geometry:
            set_position 
        Domain:
            set_position position 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        offset (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetPosition

    """

    def __init__(self, geometry=None, selection=None, position=None, offset=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetPosition', node_name='Set Position', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'position' : 2, 'offset' : 3, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if position        is not None: self.position        = position
        if offset          is not None: self.offset          = offset

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetPosition': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def position(self):
        raise AttributeError("Attribute error on node 'SetPosition': the input socket 'position' is write only.")

    @position.setter
    def position(self, value):
        self.set_input_socket('position', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'SetPosition': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

# ----------------------------------------------------------------------------------------------------
# Node SetShadeSmooth for GeometryNodeSetShadeSmooth

class SetShadeSmooth(Node):

    """Node *Set Shade Smooth*

    .. _SetShadeSmooth:

    Node implementation:
        Mesh:
            set_shade_smooth 
        Face:
            set_shade_smooth shade_smooth 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        shade_smooth (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetShadeSmooth

    """

    def __init__(self, geometry=None, selection=None, shade_smooth=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetShadeSmooth', node_name='Set Shade Smooth', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'shade_smooth' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if shade_smooth    is not None: self.shade_smooth    = shade_smooth

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetShadeSmooth': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def shade_smooth(self):
        raise AttributeError("Attribute error on node 'SetShadeSmooth': the input socket 'shade_smooth' is write only.")

    @shade_smooth.setter
    def shade_smooth(self, value):
        self.set_input_socket('shade_smooth', value)

# ----------------------------------------------------------------------------------------------------
# Node SetSplineCyclic for GeometryNodeSetSplineCyclic

class SetSplineCyclic(Node):

    """Node *Set Spline Cyclic*

    .. _SetSplineCyclic:

    Node implementation:
        Spline:
            set_cyclic cyclic 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        cyclic (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetSplineCyclic

    """

    def __init__(self, geometry=None, selection=None, cyclic=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetSplineCyclic', node_name='Set Spline Cyclic', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'cyclic' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if cyclic          is not None: self.cyclic          = cyclic

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetSplineCyclic': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def cyclic(self):
        raise AttributeError("Attribute error on node 'SetSplineCyclic': the input socket 'cyclic' is write only.")

    @cyclic.setter
    def cyclic(self, value):
        self.set_input_socket('cyclic', value)

# ----------------------------------------------------------------------------------------------------
# Node SetSplineResolution for GeometryNodeSetSplineResolution

class SetSplineResolution(Node):

    """Node *Set Spline Resolution*

    .. _SetSplineResolution:

    Node implementation:
        Spline:
            set_resolution resolution 

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        resolution (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeSetSplineResolution

    """

    def __init__(self, geometry=None, selection=None, resolution=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetSplineResolution', node_name='Set Spline Resolution', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'resolution' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if resolution      is not None: self.resolution      = resolution

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SetSplineResolution': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def resolution(self):
        raise AttributeError("Attribute error on node 'SetSplineResolution': the input socket 'resolution' is write only.")

    @resolution.setter
    def resolution(self, value):
        self.set_input_socket('resolution', value)

# ----------------------------------------------------------------------------------------------------
# Node SplineLength for GeometryNodeSplineLength

class SplineLength(Node):

    """Node *Spline Length*

    .. _SplineLength:

    Node implementation:
        Spline:
            length 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **length** : Float
        - **point_count** : Integer

    .. blid:: GeometryNodeSplineLength

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSplineLength', node_name='Spline Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'length' : 0, 'point_count' : 1, }

    @property
    def length(self):
        return self.get_output_socket('length')

    @property
    def point_count(self):
        return self.get_output_socket('point_count')

# ----------------------------------------------------------------------------------------------------
# Node SplineParameter for GeometryNodeSplineParameter

class SplineParameter(Node):

    """Node *Spline Parameter*

    .. _SplineParameter:

    Node implementation:
        ControlPoint:
            parameter parameter_factor parameter_length parameter_index 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **factor** : Float
        - **length** : Float
        - **index** : Integer

    .. blid:: GeometryNodeSplineParameter

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSplineParameter', node_name='Spline Parameter', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'factor' : 0, 'length' : 1, 'index' : 2, }

    @property
    def factor(self):
        return self.get_output_socket('factor')

    @property
    def length(self):
        return self.get_output_socket('length')

    @property
    def index(self):
        return self.get_output_socket('index')

# ----------------------------------------------------------------------------------------------------
# Node SplitEdges for GeometryNodeSplitEdges

class SplitEdges(Node):

    """Node *Split Edges*

    .. _SplitEdges:

    Node implementation:
        Mesh:
            split_edges 
        Edge:
            split 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeSplitEdges

    """

    def __init__(self, mesh=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeSplitEdges', node_name='Split Edges', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'SplitEdges': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

# ----------------------------------------------------------------------------------------------------
# Node StoreNamedAttribute for GeometryNodeStoreNamedAttribute

class StoreNamedAttribute(Node):

    """Node *Store Named Attribute*

    .. _StoreNamedAttribute:

    Node implementation:
        Geometry:
            store_named_attribute set_named_boolean set_named_integer set_named_float set_named_vector set_named_color 
        Domain:
            store_named_attribute set_named_boolean set_named_integer set_named_float set_named_vector set_named_color 

    Args:
        geometry (DataSocket): Geometry
        name (DataSocket): String
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : []

    .. blid:: GeometryNodeStoreNamedAttribute

    """

    def __init__(self, geometry=None, name=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeStoreNamedAttribute', node_name='Store Named Attribute', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = self.value_data_type(value) if data_type is None else data_type
        self.bnode.domain          = domain

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'name' : 1, 'value' : [2, 3, 4, 5, 6], }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if name            is not None: self.name            = name
        if value           is not None: self.value           = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def name(self):
        raise AttributeError("Attribute error on node 'StoreNamedAttribute': the input socket 'name' is write only.")

    @name.setter
    def name(self, value):
        self.set_input_socket('name', value)

    @property
    def value(self):
        raise AttributeError("Attribute error on node 'StoreNamedAttribute': the input socket 'value' is write only.")

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

# ----------------------------------------------------------------------------------------------------
# Node JoinStrings for GeometryNodeStringJoin

class JoinStrings(Node):

    """Node *Join Strings*

    .. _JoinStrings:

    Node implementation:
        global functions:
            join_strings 
        String:
            join 

    Args:
        delimiter (DataSocket): String
        strings (DataSocket): <m> String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **string** : String

    .. blid:: GeometryNodeStringJoin

    """

    def __init__(self, *strings, delimiter=None, label=None, node_color=None):

        super().__init__('GeometryNodeStringJoin', node_name='Join Strings', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'delimiter' : 0, 'strings' : 1, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if delimiter       is not None: self.delimiter       = delimiter
        self.plug(1, *strings)

    @property
    def string(self):
        return self.get_output_socket('string')

    @property
    def delimiter(self):
        raise AttributeError("Attribute error on node 'JoinStrings': the input socket 'delimiter' is write only.")

    @delimiter.setter
    def delimiter(self, value):
        self.set_input_socket('delimiter', value)

    @property
    def strings(self):
        raise AttributeError("Attribute error on node 'JoinStrings': the input socket 'strings' is write only.")

    @strings.setter
    def strings(self, value):
        self.set_input_socket('strings', value)

# ----------------------------------------------------------------------------------------------------
# Node StringToCurves for GeometryNodeStringToCurves

class StringToCurves(Node):

    """Node *String to Curves*

    .. _StringToCurves:

    Node implementation:
        global functions:
            string_to_curves 
        String:
            to_curves 

    Args:
        string (DataSocket): String
        size (DataSocket): Float
        character_spacing (DataSocket): Float
        word_spacing (DataSocket): Float
        line_spacing (DataSocket): Float
        text_box_width (DataSocket): Float
        text_box_height (DataSocket): Float
        align_x (str): Node parameter, default = 'LEFT' in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
        align_y (str): Node parameter, default = 'TOP_BASELINE' in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
        overflow (str): Node parameter, default = 'OVERFLOW' in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
        pivot_mode (str): Node parameter, default = 'BOTTOM_LEFT' in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve_instances** : Geometry
        - **remainder** : String
        - **line** : Integer
        - **pivot_point** : Vector

    .. blid:: GeometryNodeStringToCurves

    """

    def __init__(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None, node_color=None):

        super().__init__('GeometryNodeStringToCurves', node_name='String to Curves', label=label, node_color=node_color)

        # Node parameters

        self.bnode.align_x         = align_x
        self.bnode.align_y         = align_y
        self.bnode.overflow        = overflow
        self.bnode.pivot_mode      = pivot_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, 'size' : 1, 'character_spacing' : 2, 'word_spacing' : 3, 'line_spacing' : 4, 'text_box_width' : 5, 'text_box_height' : 6, }
        self.outsockets = {'curve_instances' : 0, 'remainder' : 1, 'line' : 2, 'pivot_point' : 3, }

        # Input sockets plugging

        if string          is not None: self.string          = string
        if size            is not None: self.size            = size
        if character_spacing is not None: self.character_spacing = character_spacing
        if word_spacing    is not None: self.word_spacing    = word_spacing
        if line_spacing    is not None: self.line_spacing    = line_spacing
        if text_box_width  is not None: self.text_box_width  = text_box_width
        if text_box_height is not None: self.text_box_height = text_box_height

    @property
    def align_x(self):
        return self.bnode.align_x

    @align_x.setter
    def align_x(self, value):
        self.bnode.align_x = value

    @property
    def align_y(self):
        return self.bnode.align_y

    @align_y.setter
    def align_y(self, value):
        self.bnode.align_y = value

    @property
    def overflow(self):
        return self.bnode.overflow

    @overflow.setter
    def overflow(self, value):
        self.bnode.overflow = value

    @property
    def pivot_mode(self):
        return self.bnode.pivot_mode

    @pivot_mode.setter
    def pivot_mode(self, value):
        self.bnode.pivot_mode = value

    @property
    def curve_instances(self):
        return self.get_output_socket('curve_instances')

    @property
    def remainder(self):
        return self.get_output_socket('remainder')

    @property
    def line(self):
        return self.get_output_socket('line')

    @property
    def pivot_point(self):
        return self.get_output_socket('pivot_point')

    @property
    def string(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'string' is write only.")

    @string.setter
    def string(self, value):
        self.set_input_socket('string', value)

    @property
    def size(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'size' is write only.")

    @size.setter
    def size(self, value):
        self.set_input_socket('size', value)

    @property
    def character_spacing(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'character_spacing' is write only.")

    @character_spacing.setter
    def character_spacing(self, value):
        self.set_input_socket('character_spacing', value)

    @property
    def word_spacing(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'word_spacing' is write only.")

    @word_spacing.setter
    def word_spacing(self, value):
        self.set_input_socket('word_spacing', value)

    @property
    def line_spacing(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'line_spacing' is write only.")

    @line_spacing.setter
    def line_spacing(self, value):
        self.set_input_socket('line_spacing', value)

    @property
    def text_box_width(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'text_box_width' is write only.")

    @text_box_width.setter
    def text_box_width(self, value):
        self.set_input_socket('text_box_width', value)

    @property
    def text_box_height(self):
        raise AttributeError("Attribute error on node 'StringToCurves': the input socket 'text_box_height' is write only.")

    @text_box_height.setter
    def text_box_height(self, value):
        self.set_input_socket('text_box_height', value)

# ----------------------------------------------------------------------------------------------------
# Node SubdivideCurve for GeometryNodeSubdivideCurve

class SubdivideCurve(Node):

    """Node *Subdivide Curve*

    .. _SubdivideCurve:

    Node implementation:
        Curve:
            subdivide 

    Args:
        curve (DataSocket): Curve
        cuts (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeSubdivideCurve

    """

    def __init__(self, curve=None, cuts=None, label=None, node_color=None):

        super().__init__('GeometryNodeSubdivideCurve', node_name='Subdivide Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'cuts' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if cuts            is not None: self.cuts            = cuts

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def cuts(self):
        raise AttributeError("Attribute error on node 'SubdivideCurve': the input socket 'cuts' is write only.")

    @cuts.setter
    def cuts(self, value):
        self.set_input_socket('cuts', value)

# ----------------------------------------------------------------------------------------------------
# Node SubdivideMesh for GeometryNodeSubdivideMesh

class SubdivideMesh(Node):

    """Node *Subdivide Mesh*

    .. _SubdivideMesh:

    Node implementation:
        Mesh:
            subdivide 

    Args:
        mesh (DataSocket): Mesh
        level (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeSubdivideMesh

    """

    def __init__(self, mesh=None, level=None, label=None, node_color=None):

        super().__init__('GeometryNodeSubdivideMesh', node_name='Subdivide Mesh', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'level' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if level           is not None: self.level           = level

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def level(self):
        raise AttributeError("Attribute error on node 'SubdivideMesh': the input socket 'level' is write only.")

    @level.setter
    def level(self, value):
        self.set_input_socket('level', value)

# ----------------------------------------------------------------------------------------------------
# Node SubdivisionSurface for GeometryNodeSubdivisionSurface

class SubdivisionSurface(Node):

    """Node *Subdivision Surface*

    .. _SubdivisionSurface:

    Node implementation:
        Mesh:
            subdivision_surface 

    Args:
        mesh (DataSocket): Mesh
        level (DataSocket): Integer
        edge_crease (DataSocket): Float
        vertex_crease (DataSocket): Float
        boundary_smooth (str): Node parameter, default = 'ALL' in ('PRESERVE_CORNERS', 'ALL')
        uv_smooth (str): Node parameter, default = 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeSubdivisionSurface

    """

    def __init__(self, mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None, node_color=None):

        super().__init__('GeometryNodeSubdivisionSurface', node_name='Subdivision Surface', label=label, node_color=node_color)

        # Node parameters

        self.bnode.boundary_smooth = boundary_smooth
        self.bnode.uv_smooth       = uv_smooth

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'level' : 1, 'edge_crease' : 2, 'vertex_crease' : 3, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if level           is not None: self.level           = level
        if edge_crease     is not None: self.edge_crease     = edge_crease
        if vertex_crease   is not None: self.vertex_crease   = vertex_crease

    @property
    def boundary_smooth(self):
        return self.bnode.boundary_smooth

    @boundary_smooth.setter
    def boundary_smooth(self, value):
        self.bnode.boundary_smooth = value

    @property
    def uv_smooth(self):
        return self.bnode.uv_smooth

    @uv_smooth.setter
    def uv_smooth(self, value):
        self.bnode.uv_smooth = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def level(self):
        raise AttributeError("Attribute error on node 'SubdivisionSurface': the input socket 'level' is write only.")

    @level.setter
    def level(self, value):
        self.set_input_socket('level', value)

    @property
    def edge_crease(self):
        raise AttributeError("Attribute error on node 'SubdivisionSurface': the input socket 'edge_crease' is write only.")

    @edge_crease.setter
    def edge_crease(self, value):
        self.set_input_socket('edge_crease', value)

    @property
    def vertex_crease(self):
        raise AttributeError("Attribute error on node 'SubdivisionSurface': the input socket 'vertex_crease' is write only.")

    @vertex_crease.setter
    def vertex_crease(self, value):
        self.set_input_socket('vertex_crease', value)

# ----------------------------------------------------------------------------------------------------
# Node Switch for GeometryNodeSwitch

class Switch(Node):

    """Node *Switch*

    .. _Switch:

    Node implementation:
        global functions:
            switch switch_float switch_integer switch_boolean switch_vector switch_string switch_color switch_object switch_image switch_geometry 
            switch_collection switch_texture switch_material 
        Float:
            switch 
        Integer:
            switch 
        Boolean:
            switch 
        Vector:
            switch 
        String:
            switch 
        Color:
            switch 
        Object:
            switch 
        Image:
            switch 
        Geometry:
            switch 
        Collection:
            switch 
        Texture:
            switch 
        Material:
            switch 

    Args:
        switch (DataSocket): ``input_type`` dependant
        false (DataSocket): ``input_type`` dependant
        true (DataSocket): ``input_type`` dependant
        input_type (str): Node parameter, default = 'GEOMETRY' in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **output** : ``input_type`` dependant

    Shared sockets:
        - Driving parameter : ``input_type`` in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
        - Input sockets  : ['switch', 'false', 'true']
        - Output sockets : ['output']

    .. blid:: GeometryNodeSwitch

    """

    def __init__(self, switch=None, false=None, true=None, input_type='GEOMETRY', label=None, node_color=None):

        super().__init__('GeometryNodeSwitch', node_name='Switch', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.input_type      = self.value_data_type(true) if input_type is None else input_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'switch' : [0, 1], 'false' : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], 'true' : [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25], }
        self.outsockets = {'output' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], }

        # Input sockets plugging

        if switch          is not None: self.switch          = switch
        if false           is not None: self.false           = false
        if true            is not None: self.true            = true

    @property
    def input_type(self):
        return self.bnode.input_type

    @input_type.setter
    def input_type(self, value):
        self.bnode.input_type = value

    @property
    def output(self):
        return self.get_output_socket('output')

    @property
    def switch(self):
        raise AttributeError("Attribute error on node 'Switch': the input socket 'switch' is write only.")

    @switch.setter
    def switch(self, value):
        self.set_input_socket('switch', value)

    @property
    def false(self):
        raise AttributeError("Attribute error on node 'Switch': the input socket 'false' is write only.")

    @false.setter
    def false(self, value):
        self.set_input_socket('false', value)

    @property
    def true(self):
        raise AttributeError("Attribute error on node 'Switch': the input socket 'true' is write only.")

    @true.setter
    def true(self, value):
        self.set_input_socket('true', value)

# ----------------------------------------------------------------------------------------------------
# Node Transform for GeometryNodeTransform

class Transform(Node):

    """Node *Transform*

    .. _Transform:

    Node implementation:
        Geometry:
            transform 

    Args:
        geometry (DataSocket): Geometry
        translation (DataSocket): Vector
        rotation (DataSocket): Vector
        scale (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **geometry** : Geometry

    .. blid:: GeometryNodeTransform

    """

    def __init__(self, geometry=None, translation=None, rotation=None, scale=None, label=None, node_color=None):

        super().__init__('GeometryNodeTransform', node_name='Transform', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'translation' : 1, 'rotation' : 2, 'scale' : 3, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if translation     is not None: self.translation     = translation
        if rotation        is not None: self.rotation        = rotation
        if scale           is not None: self.scale           = scale

    @property
    def geometry(self):
        return self.get_output_socket('geometry')

    @geometry.setter
    def geometry(self, value):
        self.set_input_socket('geometry', value)

    @property
    def translation(self):
        raise AttributeError("Attribute error on node 'Transform': the input socket 'translation' is write only.")

    @translation.setter
    def translation(self, value):
        self.set_input_socket('translation', value)

    @property
    def rotation(self):
        raise AttributeError("Attribute error on node 'Transform': the input socket 'rotation' is write only.")

    @rotation.setter
    def rotation(self, value):
        self.set_input_socket('rotation', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'Transform': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

# ----------------------------------------------------------------------------------------------------
# Node TranslateInstances for GeometryNodeTranslateInstances

class TranslateInstances(Node):

    """Node *Translate Instances*

    .. _TranslateInstances:

    Node implementation:
        Instances:
            translate 
        Instance:
            translate 

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        translation (DataSocket): Vector
        local_space (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **instances** : Instances

    .. blid:: GeometryNodeTranslateInstances

    """

    def __init__(self, instances=None, selection=None, translation=None, local_space=None, label=None, node_color=None):

        super().__init__('GeometryNodeTranslateInstances', node_name='Translate Instances', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'translation' : 2, 'local_space' : 3, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if translation     is not None: self.translation     = translation
        if local_space     is not None: self.local_space     = local_space

    @property
    def instances(self):
        return self.get_output_socket('instances')

    @instances.setter
    def instances(self, value):
        self.set_input_socket('instances', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'TranslateInstances': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def translation(self):
        raise AttributeError("Attribute error on node 'TranslateInstances': the input socket 'translation' is write only.")

    @translation.setter
    def translation(self, value):
        self.set_input_socket('translation', value)

    @property
    def local_space(self):
        raise AttributeError("Attribute error on node 'TranslateInstances': the input socket 'local_space' is write only.")

    @local_space.setter
    def local_space(self, value):
        self.set_input_socket('local_space', value)

# ----------------------------------------------------------------------------------------------------
# Node Triangulate for GeometryNodeTriangulate

class Triangulate(Node):

    """Node *Triangulate*

    .. _Triangulate:

    Node implementation:
        Mesh:
            triangulate 
        Face:
            triangulate 

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        minimum_vertices (DataSocket): Integer
        ngon_method (str): Node parameter, default = 'BEAUTY' in ('BEAUTY', 'CLIP')
        quad_method (str): Node parameter, default = 'SHORTEST_DIAGONAL' in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeTriangulate

    """

    def __init__(self, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None, node_color=None):

        super().__init__('GeometryNodeTriangulate', node_name='Triangulate', label=label, node_color=node_color)

        # Node parameters

        self.bnode.ngon_method     = ngon_method
        self.bnode.quad_method     = quad_method

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, 'minimum_vertices' : 2, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection
        if minimum_vertices is not None: self.minimum_vertices = minimum_vertices

    @property
    def ngon_method(self):
        return self.bnode.ngon_method

    @ngon_method.setter
    def ngon_method(self, value):
        self.bnode.ngon_method = value

    @property
    def quad_method(self):
        return self.bnode.quad_method

    @quad_method.setter
    def quad_method(self, value):
        self.bnode.quad_method = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @mesh.setter
    def mesh(self, value):
        self.set_input_socket('mesh', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'Triangulate': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def minimum_vertices(self):
        raise AttributeError("Attribute error on node 'Triangulate': the input socket 'minimum_vertices' is write only.")

    @minimum_vertices.setter
    def minimum_vertices(self, value):
        self.set_input_socket('minimum_vertices', value)

# ----------------------------------------------------------------------------------------------------
# Node TrimCurve for GeometryNodeTrimCurve

class TrimCurve(Node):

    """Node *Trim Curve*

    .. _TrimCurve:

    Node implementation:
        Curve:
            trim trim_factor trim_length 

    Args:
        curve (DataSocket): Curve
        start0 (DataSocket): Float
        start1 (DataSocket): Float
        end0 (DataSocket): Float
        end1 (DataSocket): Float
        mode (str): Node parameter, default = 'FACTOR' in ('FACTOR', 'LENGTH')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **curve** : Curve

    .. blid:: GeometryNodeTrimCurve

    """

    def __init__(self, curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None, node_color=None):

        super().__init__('GeometryNodeTrimCurve', node_name='Trim Curve', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'start0' : 1, 'start1' : 3, 'end0' : 2, 'end1' : 4, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if start0          is not None: self.start0          = start0
        if start1          is not None: self.start1          = start1
        if end0            is not None: self.end0            = end0
        if end1            is not None: self.end1            = end1

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

    @property
    def curve(self):
        return self.get_output_socket('curve')

    @curve.setter
    def curve(self, value):
        self.set_input_socket('curve', value)

    @property
    def start0(self):
        raise AttributeError("Attribute error on node 'TrimCurve': the input socket 'start0' is write only.")

    @start0.setter
    def start0(self, value):
        self.set_input_socket('start0', value)

    @property
    def start1(self):
        raise AttributeError("Attribute error on node 'TrimCurve': the input socket 'start1' is write only.")

    @start1.setter
    def start1(self, value):
        self.set_input_socket('start1', value)

    @property
    def end0(self):
        raise AttributeError("Attribute error on node 'TrimCurve': the input socket 'end0' is write only.")

    @end0.setter
    def end0(self, value):
        self.set_input_socket('end0', value)

    @property
    def end1(self):
        raise AttributeError("Attribute error on node 'TrimCurve': the input socket 'end1' is write only.")

    @end1.setter
    def end1(self, value):
        self.set_input_socket('end1', value)

# ----------------------------------------------------------------------------------------------------
# Node PackUvIslands for GeometryNodeUVPackIslands

class PackUvIslands(Node):

    """Node *Pack UV Islands*

    .. _PackUvIslands:

    Node implementation:
        Mesh:
            pack_uv_islands 
        Face:
            pack_uv_islands 

    Args:
        uv (DataSocket): Vector
        selection (DataSocket): Boolean
        margin (DataSocket): Float
        rotate (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **uv** : Vector

    .. blid:: GeometryNodeUVPackIslands

    """

    def __init__(self, uv=None, selection=None, margin=None, rotate=None, label=None, node_color=None):

        super().__init__('GeometryNodeUVPackIslands', node_name='Pack UV Islands', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'uv' : 0, 'selection' : 1, 'margin' : 2, 'rotate' : 3, }
        self.outsockets = {'uv' : 0, }

        # Input sockets plugging

        if uv              is not None: self.uv              = uv
        if selection       is not None: self.selection       = selection
        if margin          is not None: self.margin          = margin
        if rotate          is not None: self.rotate          = rotate

    @property
    def uv(self):
        return self.get_output_socket('uv')

    @uv.setter
    def uv(self, value):
        self.set_input_socket('uv', value)

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'PackUvIslands': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def margin(self):
        raise AttributeError("Attribute error on node 'PackUvIslands': the input socket 'margin' is write only.")

    @margin.setter
    def margin(self, value):
        self.set_input_socket('margin', value)

    @property
    def rotate(self):
        raise AttributeError("Attribute error on node 'PackUvIslands': the input socket 'rotate' is write only.")

    @rotate.setter
    def rotate(self, value):
        self.set_input_socket('rotate', value)

# ----------------------------------------------------------------------------------------------------
# Node UvUnwrap for GeometryNodeUVUnwrap

class UvUnwrap(Node):

    """Node *UV Unwrap*

    .. _UvUnwrap:

    Node implementation:
        Mesh:
            uv_unwrap 
        Face:
            uv_unwrap 

    Args:
        selection (DataSocket): Boolean
        seam (DataSocket): Boolean
        margin (DataSocket): Float
        fill_holes (DataSocket): Boolean
        method (str): Node parameter, default = 'ANGLE_BASED' in ('ANGLE_BASED', 'CONFORMAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **uv** : Vector

    .. blid:: GeometryNodeUVUnwrap

    """

    def __init__(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED', label=None, node_color=None):

        super().__init__('GeometryNodeUVUnwrap', node_name='UV Unwrap', label=label, node_color=node_color)

        # Node parameters

        self.bnode.method          = method

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'selection' : 0, 'seam' : 1, 'margin' : 2, 'fill_holes' : 3, }
        self.outsockets = {'uv' : 0, }

        # Input sockets plugging

        if selection       is not None: self.selection       = selection
        if seam            is not None: self.seam            = seam
        if margin          is not None: self.margin          = margin
        if fill_holes      is not None: self.fill_holes      = fill_holes

    @property
    def method(self):
        return self.bnode.method

    @method.setter
    def method(self, value):
        self.bnode.method = value

    @property
    def uv(self):
        return self.get_output_socket('uv')

    @property
    def selection(self):
        raise AttributeError("Attribute error on node 'UvUnwrap': the input socket 'selection' is write only.")

    @selection.setter
    def selection(self, value):
        self.set_input_socket('selection', value)

    @property
    def seam(self):
        raise AttributeError("Attribute error on node 'UvUnwrap': the input socket 'seam' is write only.")

    @seam.setter
    def seam(self, value):
        self.set_input_socket('seam', value)

    @property
    def margin(self):
        raise AttributeError("Attribute error on node 'UvUnwrap': the input socket 'margin' is write only.")

    @margin.setter
    def margin(self, value):
        self.set_input_socket('margin', value)

    @property
    def fill_holes(self):
        raise AttributeError("Attribute error on node 'UvUnwrap': the input socket 'fill_holes' is write only.")

    @fill_holes.setter
    def fill_holes(self, value):
        self.set_input_socket('fill_holes', value)

# ----------------------------------------------------------------------------------------------------
# Node VertexOfCorner for GeometryNodeVertexOfCorner

class VertexOfCorner(Node):

    """Node *Vertex of Corner*

    .. _VertexOfCorner:

    Node implementation:
        Mesh:
            vertex_of_corner 
        Corner:
            vertex_index 

    Args:
        corner_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vertex_index** : Integer

    .. blid:: GeometryNodeVertexOfCorner

    """

    def __init__(self, corner_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeVertexOfCorner', node_name='Vertex of Corner', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'corner_index' : 0, }
        self.outsockets = {'vertex_index' : 0, }

        # Input sockets plugging

        if corner_index    is not None: self.corner_index    = corner_index

    @property
    def vertex_index(self):
        return self.get_output_socket('vertex_index')

    @property
    def corner_index(self):
        raise AttributeError("Attribute error on node 'VertexOfCorner': the input socket 'corner_index' is write only.")

    @corner_index.setter
    def corner_index(self, value):
        self.set_input_socket('corner_index', value)

# ----------------------------------------------------------------------------------------------------
# Node VolumeCube for GeometryNodeVolumeCube

class VolumeCube(Node):

    """Node *Volume Cube*

    .. _VolumeCube:

    Node implementation:
        Volume:
            Cube 

    Args:
        density (DataSocket): Float
        background (DataSocket): Float
        min (DataSocket): Vector
        max (DataSocket): Vector
        resolution_x (DataSocket): Integer
        resolution_y (DataSocket): Integer
        resolution_z (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **volume** : Volume

    .. blid:: GeometryNodeVolumeCube

    """

    def __init__(self, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None, label=None, node_color=None):

        super().__init__('GeometryNodeVolumeCube', node_name='Volume Cube', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'density' : 0, 'background' : 1, 'min' : 2, 'max' : 3, 'resolution_x' : 4, 'resolution_y' : 5, 'resolution_z' : 6, }
        self.outsockets = {'volume' : 0, }

        # Input sockets plugging

        if density         is not None: self.density         = density
        if background      is not None: self.background      = background
        if min             is not None: self.min             = min
        if max             is not None: self.max             = max
        if resolution_x    is not None: self.resolution_x    = resolution_x
        if resolution_y    is not None: self.resolution_y    = resolution_y
        if resolution_z    is not None: self.resolution_z    = resolution_z

    @property
    def volume(self):
        return self.get_output_socket('volume')

    @property
    def density(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'density' is write only.")

    @density.setter
    def density(self, value):
        self.set_input_socket('density', value)

    @property
    def background(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'background' is write only.")

    @background.setter
    def background(self, value):
        self.set_input_socket('background', value)

    @property
    def min(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'min' is write only.")

    @min.setter
    def min(self, value):
        self.set_input_socket('min', value)

    @property
    def max(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'max' is write only.")

    @max.setter
    def max(self, value):
        self.set_input_socket('max', value)

    @property
    def resolution_x(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'resolution_x' is write only.")

    @resolution_x.setter
    def resolution_x(self, value):
        self.set_input_socket('resolution_x', value)

    @property
    def resolution_y(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'resolution_y' is write only.")

    @resolution_y.setter
    def resolution_y(self, value):
        self.set_input_socket('resolution_y', value)

    @property
    def resolution_z(self):
        raise AttributeError("Attribute error on node 'VolumeCube': the input socket 'resolution_z' is write only.")

    @resolution_z.setter
    def resolution_z(self, value):
        self.set_input_socket('resolution_z', value)

# ----------------------------------------------------------------------------------------------------
# Node VolumeToMesh for GeometryNodeVolumeToMesh

class VolumeToMesh(Node):

    """Node *Volume to Mesh*

    .. _VolumeToMesh:

    Node implementation:
        Volume:
            to_mesh 

    Args:
        volume (DataSocket): Volume
        voxel_size (DataSocket): Float
        voxel_amount (DataSocket): Float
        threshold (DataSocket): Float
        adaptivity (DataSocket): Float
        resolution_mode (str): Node parameter, default = 'GRID' in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **mesh** : Mesh

    .. blid:: GeometryNodeVolumeToMesh

    """

    def __init__(self, volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None, node_color=None):

        super().__init__('GeometryNodeVolumeToMesh', node_name='Volume to Mesh', label=label, node_color=node_color)

        # Node parameters

        self.bnode.resolution_mode = resolution_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'volume' : 0, 'voxel_size' : 1, 'voxel_amount' : 2, 'threshold' : 3, 'adaptivity' : 4, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if volume          is not None: self.volume          = volume
        if voxel_size      is not None: self.voxel_size      = voxel_size
        if voxel_amount    is not None: self.voxel_amount    = voxel_amount
        if threshold       is not None: self.threshold       = threshold
        if adaptivity      is not None: self.adaptivity      = adaptivity

    @property
    def resolution_mode(self):
        return self.bnode.resolution_mode

    @resolution_mode.setter
    def resolution_mode(self, value):
        self.bnode.resolution_mode = value

    @property
    def mesh(self):
        return self.get_output_socket('mesh')

    @property
    def volume(self):
        raise AttributeError("Attribute error on node 'VolumeToMesh': the input socket 'volume' is write only.")

    @volume.setter
    def volume(self, value):
        self.set_input_socket('volume', value)

    @property
    def voxel_size(self):
        raise AttributeError("Attribute error on node 'VolumeToMesh': the input socket 'voxel_size' is write only.")

    @voxel_size.setter
    def voxel_size(self, value):
        self.set_input_socket('voxel_size', value)

    @property
    def voxel_amount(self):
        raise AttributeError("Attribute error on node 'VolumeToMesh': the input socket 'voxel_amount' is write only.")

    @voxel_amount.setter
    def voxel_amount(self, value):
        self.set_input_socket('voxel_amount', value)

    @property
    def threshold(self):
        raise AttributeError("Attribute error on node 'VolumeToMesh': the input socket 'threshold' is write only.")

    @threshold.setter
    def threshold(self, value):
        self.set_input_socket('threshold', value)

    @property
    def adaptivity(self):
        raise AttributeError("Attribute error on node 'VolumeToMesh': the input socket 'adaptivity' is write only.")

    @adaptivity.setter
    def adaptivity(self, value):
        self.set_input_socket('adaptivity', value)

# ----------------------------------------------------------------------------------------------------
# Node Clamp for ShaderNodeClamp

class Clamp(Node):

    """Node *Clamp*

    .. _Clamp:

    Node implementation:
        global functions:
            clamp clamp_min_max clamp_range 
        Float:
            clamp clamp_min_max clamp_range 

    Args:
        value (DataSocket): Float
        min (DataSocket): Float
        max (DataSocket): Float
        clamp_type (str): Node parameter, default = 'MINMAX' in ('MINMAX', 'RANGE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **result** : Float

    .. blid:: ShaderNodeClamp

    """

    def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX', label=None, node_color=None):

        super().__init__('ShaderNodeClamp', node_name='Clamp', label=label, node_color=node_color)

        # Node parameters

        self.bnode.clamp_type      = clamp_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value' : 0, 'min' : 1, 'max' : 2, }
        self.outsockets = {'result' : 0, }

        # Input sockets plugging

        if value           is not None: self.value           = value
        if min             is not None: self.min             = min
        if max             is not None: self.max             = max

    @property
    def clamp_type(self):
        return self.bnode.clamp_type

    @clamp_type.setter
    def clamp_type(self, value):
        self.bnode.clamp_type = value

    @property
    def result(self):
        return self.get_output_socket('result')

    @property
    def value(self):
        raise AttributeError("Attribute error on node 'Clamp': the input socket 'value' is write only.")

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def min(self):
        raise AttributeError("Attribute error on node 'Clamp': the input socket 'min' is write only.")

    @min.setter
    def min(self, value):
        self.set_input_socket('min', value)

    @property
    def max(self):
        raise AttributeError("Attribute error on node 'Clamp': the input socket 'max' is write only.")

    @max.setter
    def max(self, value):
        self.set_input_socket('max', value)

# ----------------------------------------------------------------------------------------------------
# Node CombineXyz for ShaderNodeCombineXYZ

class CombineXyz(Node):

    """Node *Combine XYZ*

    .. _CombineXyz:

    Node implementation:
        Vector:
            Combine 

    Args:
        x (DataSocket): Float
        y (DataSocket): Float
        z (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vector** : Vector

    .. blid:: ShaderNodeCombineXYZ

    """

    def __init__(self, x=None, y=None, z=None, label=None, node_color=None):

        super().__init__('ShaderNodeCombineXYZ', node_name='Combine XYZ', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'x' : 0, 'y' : 1, 'z' : 2, }
        self.outsockets = {'vector' : 0, }

        # Input sockets plugging

        if x               is not None: self.x               = x
        if y               is not None: self.y               = y
        if z               is not None: self.z               = z

    @property
    def vector(self):
        return self.get_output_socket('vector')

    @property
    def x(self):
        raise AttributeError("Attribute error on node 'CombineXyz': the input socket 'x' is write only.")

    @x.setter
    def x(self, value):
        self.set_input_socket('x', value)

    @property
    def y(self):
        raise AttributeError("Attribute error on node 'CombineXyz': the input socket 'y' is write only.")

    @y.setter
    def y(self, value):
        self.set_input_socket('y', value)

    @property
    def z(self):
        raise AttributeError("Attribute error on node 'CombineXyz': the input socket 'z' is write only.")

    @z.setter
    def z(self, value):
        self.set_input_socket('z', value)

# ----------------------------------------------------------------------------------------------------
# Node FloatCurve for ShaderNodeFloatCurve

class FloatCurve(Node):

    """Node *Float Curve*

    .. _FloatCurve:

    Node implementation:
        Float:
            float_curve 

    Args:
        factor (DataSocket): Float
        value (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : Float

    .. blid:: ShaderNodeFloatCurve

    """

    def __init__(self, factor=None, value=None, label=None, node_color=None):

        super().__init__('ShaderNodeFloatCurve', node_name='Float Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'factor' : 0, 'value' : 1, }
        self.outsockets = {'value' : 0, }

        # Input sockets plugging

        if factor          is not None: self.factor          = factor
        if value           is not None: self.value           = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def factor(self):
        raise AttributeError("Attribute error on node 'FloatCurve': the input socket 'factor' is write only.")

    @factor.setter
    def factor(self, value):
        self.set_input_socket('factor', value)

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

# ----------------------------------------------------------------------------------------------------
# Node MapRange for ShaderNodeMapRange

class MapRange(Node):

    """Node *Map Range*

    .. _MapRange:

    Node implementation:
        Float:
            map_range map_range_linear map_range_stepped map_range_smooth map_range_smoother 
        Vector:
            map_range map_range_linear map_range_stepped map_range_smooth map_range_smoother 

    Args:
        value (DataSocket): Float
        from_min (DataSocket): ``data_type`` dependant
        from_max (DataSocket): ``data_type`` dependant
        to_min (DataSocket): ``data_type`` dependant
        to_max (DataSocket): ``data_type`` dependant
        steps (DataSocket): ``data_type`` dependant
        vector (DataSocket): Vector
        clamp (bool): Node parameter, default = True
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
        interpolation_type (str): Node parameter, default = 'LINEAR' in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **result** : Float
        - **vector** : Vector

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')
        - Input sockets  : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']
        - Output sockets : []

    .. blid:: ShaderNodeMapRange

    """

    def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None, node_color=None):

        super().__init__('ShaderNodeMapRange', node_name='Map Range', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.clamp           = clamp
        self.bnode.data_type       = self.value_data_type(steps) if data_type is None else data_type
        self.bnode.interpolation_type = interpolation_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value' : 0, 'from_min' : [1, 7], 'from_max' : [2, 8], 'to_min' : [3, 9], 'to_max' : [4, 10], 'steps' : [5, 11], 'vector' : 6, }
        self.outsockets = {'result' : 0, 'vector' : 1, }

        # Input sockets plugging

        if value           is not None: self.value           = value
        if from_min        is not None: self.from_min        = from_min
        if from_max        is not None: self.from_max        = from_max
        if to_min          is not None: self.to_min          = to_min
        if to_max          is not None: self.to_max          = to_max
        if steps           is not None: self.steps           = steps
        if vector          is not None: self.vector          = vector

    @property
    def clamp(self):
        return self.bnode.clamp

    @clamp.setter
    def clamp(self, value):
        self.bnode.clamp = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def interpolation_type(self):
        return self.bnode.interpolation_type

    @interpolation_type.setter
    def interpolation_type(self, value):
        self.bnode.interpolation_type = value

    @property
    def result(self):
        return self.get_output_socket('result')

    @property
    def vector(self):
        return self.get_output_socket('vector')

    @property
    def value(self):
        raise AttributeError("Attribute error on node 'MapRange': the input socket 'value' is write only.")

    @value.setter
    def value(self, value):
        self.set_input_socket('value', value)

    @property
    def from_min(self):
        raise AttributeError("Attribute error on node 'MapRange': the input socket 'from_min' is write only.")

    @from_min.setter
    def from_min(self, value):
        self.set_input_socket('from_min', value)

    @property
    def from_max(self):
        raise AttributeError("Attribute error on node 'MapRange': the input socket 'from_max' is write only.")

    @from_max.setter
    def from_max(self, value):
        self.set_input_socket('from_max', value)

    @property
    def to_min(self):
        raise AttributeError("Attribute error on node 'MapRange': the input socket 'to_min' is write only.")

    @to_min.setter
    def to_min(self, value):
        self.set_input_socket('to_min', value)

    @property
    def to_max(self):
        raise AttributeError("Attribute error on node 'MapRange': the input socket 'to_max' is write only.")

    @to_max.setter
    def to_max(self, value):
        self.set_input_socket('to_max', value)

    @property
    def steps(self):
        raise AttributeError("Attribute error on node 'MapRange': the input socket 'steps' is write only.")

    @steps.setter
    def steps(self, value):
        self.set_input_socket('steps', value)

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

# ----------------------------------------------------------------------------------------------------
# Node Math for ShaderNodeMath

class Math(Node):

    """Node *Math*

    .. _Math:

    Node implementation:
        global functions:
            math multiply_add mul_add power logarithm log sqrt inverse_sqrt absolute abs 
            exponent exp minimum min maximum max math_less_than math_greater_than sign math_compare 
            smooth_minimum smooth_maximum math_round math_floor math_ceil math_truncate math_trun fraction modulo wrap 
            snap ping_pong sine sin cosine cos tangent tan arcsine arcsin 
            arccosine arccos arctangent arctan arctan2 sinh cosh tanh to_radians to_degrees 
        ('Integer', 'Float'):
            multiply_add mul_add power pow logarithm log sqrt inverse_sqrt absolute abs 
            exponent exp minimum min maximum max math_less_than math_greater_than sign math_compare 
            smooth_minimum smooth_maximum math_round math_floor math_ceil math_truncate math_trunc fraction fact modulo 
            wrap snap ping_pong sine sin cosine cos tangent tan arcsine 
            arcsin arccosine arccos arctangent arctan arctan2 sinh cosh tanh to_radians 
            to_degrees 

    Args:
        value0 (DataSocket): Float
        value1 (DataSocket): Float
        value2 (DataSocket): Float
        operation (str): Node parameter, default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
        use_clamp (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : Float

    .. blid:: ShaderNodeMath

    """

    def __init__(self, value0=None, value1=None, value2=None, operation='ADD', use_clamp=False, label=None, node_color=None):

        super().__init__('ShaderNodeMath', node_name='Math', label=label, node_color=node_color)

        # Node parameters

        self.bnode.operation       = operation
        self.bnode.use_clamp       = use_clamp

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value0' : 0, 'value1' : 1, 'value2' : 2, }
        self.outsockets = {'value' : 0, }

        # Input sockets plugging

        if value0          is not None: self.value0          = value0
        if value1          is not None: self.value1          = value1
        if value2          is not None: self.value2          = value2

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

    @property
    def use_clamp(self):
        return self.bnode.use_clamp

    @use_clamp.setter
    def use_clamp(self, value):
        self.bnode.use_clamp = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def value0(self):
        raise AttributeError("Attribute error on node 'Math': the input socket 'value0' is write only.")

    @value0.setter
    def value0(self, value):
        self.set_input_socket('value0', value)

    @property
    def value1(self):
        raise AttributeError("Attribute error on node 'Math': the input socket 'value1' is write only.")

    @value1.setter
    def value1(self, value):
        self.set_input_socket('value1', value)

    @property
    def value2(self):
        raise AttributeError("Attribute error on node 'Math': the input socket 'value2' is write only.")

    @value2.setter
    def value2(self, value):
        self.set_input_socket('value2', value)

# ----------------------------------------------------------------------------------------------------
# Node Mix for ShaderNodeMix

class Mix(Node):

    """Node *Mix*

    .. _Mix:

    Node implementation:
        global functions:
            float_mix vector_mix color_mix color_darken color_multiply color_burn color_lighten color_screen color_dodge color_add 
            color_overlay color_soft_light color_linear_light color_difference color_subtract color_divide color_hue color_saturation color_color color_value 
        Color:
            mix mix_darken mix_multiply mix_burn mix_lighten mix_screen mix_dodge mix_add mix_overlay mix_soft_light 
            mix_linear_light mix_difference mix_subtract mix_divide mix_hue mix_saturation mix_color mix_value 
        Float:
            mix 
        Vector:
            mix mix_uniform mix_non_uniform 

    Args:
        factor (DataSocket): ``data_type`` dependant
        a (DataSocket): ``data_type`` dependant
        b (DataSocket): ``data_type`` dependant
        blend_type (str): Node parameter, default = 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
        clamp_factor (bool): Node parameter, default = True
        clamp_result (bool): Node parameter, default = False
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'VECTOR', 'RGBA')
        factor_mode (str): Node parameter, default = 'UNIFORM' in ('UNIFORM', 'NON_UNIFORM')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **result** : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'VECTOR', 'RGBA')
        - Input sockets  : ['factor', 'a', 'b']
        - Output sockets : ['result']

    .. blid:: ShaderNodeMix

    """

    def __init__(self, factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', label=None, node_color=None):

        super().__init__('ShaderNodeMix', node_name='Mix', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.blend_type      = blend_type
        self.bnode.clamp_factor    = clamp_factor
        self.bnode.clamp_result    = clamp_result
        self.bnode.data_type       = self.value_data_type(b) if data_type is None else data_type
        self.bnode.factor_mode     = factor_mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'factor' : [0, 1], 'a' : [2, 4, 6], 'b' : [3, 5, 7], }
        self.outsockets = {'result' : [0, 1, 2], }

        # Input sockets plugging

        if factor          is not None: self.factor          = factor
        if a               is not None: self.a               = a
        if b               is not None: self.b               = b

    @property
    def blend_type(self):
        return self.bnode.blend_type

    @blend_type.setter
    def blend_type(self, value):
        self.bnode.blend_type = value

    @property
    def clamp_factor(self):
        return self.bnode.clamp_factor

    @clamp_factor.setter
    def clamp_factor(self, value):
        self.bnode.clamp_factor = value

    @property
    def clamp_result(self):
        return self.bnode.clamp_result

    @clamp_result.setter
    def clamp_result(self, value):
        self.bnode.clamp_result = value

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    @property
    def factor_mode(self):
        return self.bnode.factor_mode

    @factor_mode.setter
    def factor_mode(self, value):
        self.bnode.factor_mode = value

    @property
    def result(self):
        return self.get_output_socket('result')

    @property
    def factor(self):
        raise AttributeError("Attribute error on node 'Mix': the input socket 'factor' is write only.")

    @factor.setter
    def factor(self, value):
        self.set_input_socket('factor', value)

    @property
    def a(self):
        raise AttributeError("Attribute error on node 'Mix': the input socket 'a' is write only.")

    @a.setter
    def a(self, value):
        self.set_input_socket('a', value)

    @property
    def b(self):
        raise AttributeError("Attribute error on node 'Mix': the input socket 'b' is write only.")

    @b.setter
    def b(self, value):
        self.set_input_socket('b', value)

# ----------------------------------------------------------------------------------------------------
# Node RgbCurves for ShaderNodeRGBCurve

class RgbCurves(Node):

    """Node *RGB Curves*

    .. _RgbCurves:

    Node implementation:
        global functions:
            rgb_curves 
        Color:
            rgb_curves 

    Args:
        fac (DataSocket): Float
        color (DataSocket): Color
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color

    .. blid:: ShaderNodeRGBCurve

    """

    def __init__(self, fac=None, color=None, label=None, node_color=None):

        super().__init__('ShaderNodeRGBCurve', node_name='RGB Curves', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, 'color' : 1, }
        self.outsockets = {'color' : 0, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac
        if color           is not None: self.color           = color

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def fac(self):
        raise AttributeError("Attribute error on node 'RgbCurves': the input socket 'fac' is write only.")

    @fac.setter
    def fac(self, value):
        self.set_input_socket('fac', value)

    @color.setter
    def color(self, value):
        self.set_input_socket('color', value)

# ----------------------------------------------------------------------------------------------------
# Node SeparateXyz for ShaderNodeSeparateXYZ

class SeparateXyz(Node):

    """Node *Separate XYZ*

    .. _SeparateXyz:

    Node implementation:
        Vector:
            separate 

    Args:
        vector (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **x** : Float
        - **y** : Float
        - **z** : Float

    .. blid:: ShaderNodeSeparateXYZ

    """

    def __init__(self, vector=None, label=None, node_color=None):

        super().__init__('ShaderNodeSeparateXYZ', node_name='Separate XYZ', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, }
        self.outsockets = {'x' : 0, 'y' : 1, 'z' : 2, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector

    @property
    def x(self):
        return self.get_output_socket('x')

    @property
    def y(self):
        return self.get_output_socket('y')

    @property
    def z(self):
        return self.get_output_socket('z')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'SeparateXyz': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

# ----------------------------------------------------------------------------------------------------
# Node BrickTexture for ShaderNodeTexBrick

class BrickTexture(Node):

    """Node *Brick Texture*

    .. _BrickTexture:

    Node implementation:
        Texture:
            brick 

    Args:
        vector (DataSocket): Vector
        color1 (DataSocket): Color
        color2 (DataSocket): Color
        mortar (DataSocket): Color
        scale (DataSocket): Float
        mortar_size (DataSocket): Float
        mortar_smooth (DataSocket): Float
        bias (DataSocket): Float
        brick_width (DataSocket): Float
        row_height (DataSocket): Float
        offset (float): Node parameter, default = 0.5
        offset_frequency (int): Node parameter, default = 2
        squash (float): Node parameter, default = 1.0
        squash_frequency (int): Node parameter, default = 2
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **fac** : Float

    .. blid:: ShaderNodeTexBrick

    """

    def __init__(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None, node_color=None):

        super().__init__('ShaderNodeTexBrick', node_name='Brick Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.offset          = offset
        self.bnode.offset_frequency = offset_frequency
        self.bnode.squash          = squash
        self.bnode.squash_frequency = squash_frequency

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'color1' : 1, 'color2' : 2, 'mortar' : 3, 'scale' : 4, 'mortar_size' : 5, 'mortar_smooth' : 6, 'bias' : 7, 'brick_width' : 8, 'row_height' : 9, }
        self.outsockets = {'color' : 0, 'fac' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if color1          is not None: self.color1          = color1
        if color2          is not None: self.color2          = color2
        if mortar          is not None: self.mortar          = mortar
        if scale           is not None: self.scale           = scale
        if mortar_size     is not None: self.mortar_size     = mortar_size
        if mortar_smooth   is not None: self.mortar_smooth   = mortar_smooth
        if bias            is not None: self.bias            = bias
        if brick_width     is not None: self.brick_width     = brick_width
        if row_height      is not None: self.row_height      = row_height

    @property
    def offset(self):
        return self.bnode.offset

    @offset.setter
    def offset(self, value):
        self.bnode.offset = value

    @property
    def offset_frequency(self):
        return self.bnode.offset_frequency

    @offset_frequency.setter
    def offset_frequency(self, value):
        self.bnode.offset_frequency = value

    @property
    def squash(self):
        return self.bnode.squash

    @squash.setter
    def squash(self, value):
        self.bnode.squash = value

    @property
    def squash_frequency(self):
        return self.bnode.squash_frequency

    @squash_frequency.setter
    def squash_frequency(self, value):
        self.bnode.squash_frequency = value

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def color1(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'color1' is write only.")

    @color1.setter
    def color1(self, value):
        self.set_input_socket('color1', value)

    @property
    def color2(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'color2' is write only.")

    @color2.setter
    def color2(self, value):
        self.set_input_socket('color2', value)

    @property
    def mortar(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'mortar' is write only.")

    @mortar.setter
    def mortar(self, value):
        self.set_input_socket('mortar', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def mortar_size(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'mortar_size' is write only.")

    @mortar_size.setter
    def mortar_size(self, value):
        self.set_input_socket('mortar_size', value)

    @property
    def mortar_smooth(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'mortar_smooth' is write only.")

    @mortar_smooth.setter
    def mortar_smooth(self, value):
        self.set_input_socket('mortar_smooth', value)

    @property
    def bias(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'bias' is write only.")

    @bias.setter
    def bias(self, value):
        self.set_input_socket('bias', value)

    @property
    def brick_width(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'brick_width' is write only.")

    @brick_width.setter
    def brick_width(self, value):
        self.set_input_socket('brick_width', value)

    @property
    def row_height(self):
        raise AttributeError("Attribute error on node 'BrickTexture': the input socket 'row_height' is write only.")

    @row_height.setter
    def row_height(self, value):
        self.set_input_socket('row_height', value)

# ----------------------------------------------------------------------------------------------------
# Node CheckerTexture for ShaderNodeTexChecker

class CheckerTexture(Node):

    """Node *Checker Texture*

    .. _CheckerTexture:

    Node implementation:
        Texture:
            checker 

    Args:
        vector (DataSocket): Vector
        color1 (DataSocket): Color
        color2 (DataSocket): Color
        scale (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **fac** : Float

    .. blid:: ShaderNodeTexChecker

    """

    def __init__(self, vector=None, color1=None, color2=None, scale=None, label=None, node_color=None):

        super().__init__('ShaderNodeTexChecker', node_name='Checker Texture', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'color1' : 1, 'color2' : 2, 'scale' : 3, }
        self.outsockets = {'color' : 0, 'fac' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if color1          is not None: self.color1          = color1
        if color2          is not None: self.color2          = color2
        if scale           is not None: self.scale           = scale

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'CheckerTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def color1(self):
        raise AttributeError("Attribute error on node 'CheckerTexture': the input socket 'color1' is write only.")

    @color1.setter
    def color1(self, value):
        self.set_input_socket('color1', value)

    @property
    def color2(self):
        raise AttributeError("Attribute error on node 'CheckerTexture': the input socket 'color2' is write only.")

    @color2.setter
    def color2(self, value):
        self.set_input_socket('color2', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'CheckerTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

# ----------------------------------------------------------------------------------------------------
# Node GradientTexture for ShaderNodeTexGradient

class GradientTexture(Node):

    """Node *Gradient Texture*

    .. _GradientTexture:

    Node implementation:
        Texture:
            gradient gradient_linear gradient_quadratic gradient_easing gradient_diagonal gradient_spherical gradient_quadratic_sphere gradient_radial 

    Args:
        vector (DataSocket): Vector
        gradient_type (str): Node parameter, default = 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **fac** : Float

    .. blid:: ShaderNodeTexGradient

    """

    def __init__(self, vector=None, gradient_type='LINEAR', label=None, node_color=None):

        super().__init__('ShaderNodeTexGradient', node_name='Gradient Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.gradient_type   = gradient_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, }
        self.outsockets = {'color' : 0, 'fac' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector

    @property
    def gradient_type(self):
        return self.bnode.gradient_type

    @gradient_type.setter
    def gradient_type(self, value):
        self.bnode.gradient_type = value

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'GradientTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

# ----------------------------------------------------------------------------------------------------
# Node MagicTexture for ShaderNodeTexMagic

class MagicTexture(Node):

    """Node *Magic Texture*

    .. _MagicTexture:

    Node implementation:
        Texture:
            magic 

    Args:
        vector (DataSocket): Vector
        scale (DataSocket): Float
        distortion (DataSocket): Float
        turbulence_depth (int): Node parameter, default = 2
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **fac** : Float

    .. blid:: ShaderNodeTexMagic

    """

    def __init__(self, vector=None, scale=None, distortion=None, turbulence_depth=2, label=None, node_color=None):

        super().__init__('ShaderNodeTexMagic', node_name='Magic Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.turbulence_depth = turbulence_depth

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'scale' : 1, 'distortion' : 2, }
        self.outsockets = {'color' : 0, 'fac' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if scale           is not None: self.scale           = scale
        if distortion      is not None: self.distortion      = distortion

    @property
    def turbulence_depth(self):
        return self.bnode.turbulence_depth

    @turbulence_depth.setter
    def turbulence_depth(self, value):
        self.bnode.turbulence_depth = value

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'MagicTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'MagicTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def distortion(self):
        raise AttributeError("Attribute error on node 'MagicTexture': the input socket 'distortion' is write only.")

    @distortion.setter
    def distortion(self, value):
        self.set_input_socket('distortion', value)

# ----------------------------------------------------------------------------------------------------
# Node MusgraveTexture for ShaderNodeTexMusgrave

class MusgraveTexture(Node):

    """Node *Musgrave Texture*

    .. _MusgraveTexture:

    Node implementation:
        Texture:
            musgrave 

    Args:
        vector (DataSocket): Vector
        w (DataSocket): Float
        scale (DataSocket): Float
        detail (DataSocket): Float
        dimension (DataSocket): Float
        lacunarity (DataSocket): Float
        offset (DataSocket): Float
        gain (DataSocket): Float
        musgrave_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')
        musgrave_type (str): Node parameter, default = 'FBM' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **fac** : Float

    .. blid:: ShaderNodeTexMusgrave

    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None, node_color=None):

        super().__init__('ShaderNodeTexMusgrave', node_name='Musgrave Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.musgrave_dimensions = musgrave_dimensions
        self.bnode.musgrave_type   = musgrave_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'w' : 1, 'scale' : 2, 'detail' : 3, 'dimension' : 4, 'lacunarity' : 5, 'offset' : 6, 'gain' : 7, }
        self.outsockets = {'fac' : 0, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if w               is not None: self.w               = w
        if scale           is not None: self.scale           = scale
        if detail          is not None: self.detail          = detail
        if dimension       is not None: self.dimension       = dimension
        if lacunarity      is not None: self.lacunarity      = lacunarity
        if offset          is not None: self.offset          = offset
        if gain            is not None: self.gain            = gain

    @property
    def musgrave_dimensions(self):
        return self.bnode.musgrave_dimensions

    @musgrave_dimensions.setter
    def musgrave_dimensions(self, value):
        self.bnode.musgrave_dimensions = value

    @property
    def musgrave_type(self):
        return self.bnode.musgrave_type

    @musgrave_type.setter
    def musgrave_type(self, value):
        self.bnode.musgrave_type = value

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def w(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'w' is write only.")

    @w.setter
    def w(self, value):
        self.set_input_socket('w', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def detail(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'detail' is write only.")

    @detail.setter
    def detail(self, value):
        self.set_input_socket('detail', value)

    @property
    def dimension(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'dimension' is write only.")

    @dimension.setter
    def dimension(self, value):
        self.set_input_socket('dimension', value)

    @property
    def lacunarity(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'lacunarity' is write only.")

    @lacunarity.setter
    def lacunarity(self, value):
        self.set_input_socket('lacunarity', value)

    @property
    def offset(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'offset' is write only.")

    @offset.setter
    def offset(self, value):
        self.set_input_socket('offset', value)

    @property
    def gain(self):
        raise AttributeError("Attribute error on node 'MusgraveTexture': the input socket 'gain' is write only.")

    @gain.setter
    def gain(self, value):
        self.set_input_socket('gain', value)

# ----------------------------------------------------------------------------------------------------
# Node NoiseTexture for ShaderNodeTexNoise

class NoiseTexture(Node):

    """Node *Noise Texture*

    .. _NoiseTexture:

    Node implementation:
        Texture:
            noise noise_1D noise_2D noise_3D noise_4D 

    Args:
        vector (DataSocket): Vector
        w (DataSocket): Float
        scale (DataSocket): Float
        detail (DataSocket): Float
        roughness (DataSocket): Float
        distortion (DataSocket): Float
        noise_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **fac** : Float
        - **color** : Color

    .. blid:: ShaderNodeTexNoise

    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None, node_color=None):

        super().__init__('ShaderNodeTexNoise', node_name='Noise Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.noise_dimensions = noise_dimensions

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'w' : 1, 'scale' : 2, 'detail' : 3, 'roughness' : 4, 'distortion' : 5, }
        self.outsockets = {'fac' : 0, 'color' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if w               is not None: self.w               = w
        if scale           is not None: self.scale           = scale
        if detail          is not None: self.detail          = detail
        if roughness       is not None: self.roughness       = roughness
        if distortion      is not None: self.distortion      = distortion

    @property
    def noise_dimensions(self):
        return self.bnode.noise_dimensions

    @noise_dimensions.setter
    def noise_dimensions(self, value):
        self.bnode.noise_dimensions = value

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'NoiseTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def w(self):
        raise AttributeError("Attribute error on node 'NoiseTexture': the input socket 'w' is write only.")

    @w.setter
    def w(self, value):
        self.set_input_socket('w', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'NoiseTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def detail(self):
        raise AttributeError("Attribute error on node 'NoiseTexture': the input socket 'detail' is write only.")

    @detail.setter
    def detail(self, value):
        self.set_input_socket('detail', value)

    @property
    def roughness(self):
        raise AttributeError("Attribute error on node 'NoiseTexture': the input socket 'roughness' is write only.")

    @roughness.setter
    def roughness(self, value):
        self.set_input_socket('roughness', value)

    @property
    def distortion(self):
        raise AttributeError("Attribute error on node 'NoiseTexture': the input socket 'distortion' is write only.")

    @distortion.setter
    def distortion(self, value):
        self.set_input_socket('distortion', value)

# ----------------------------------------------------------------------------------------------------
# Node VoronoiTexture for ShaderNodeTexVoronoi

class VoronoiTexture(Node):

    """Node *Voronoi Texture*

    .. _VoronoiTexture:

    Node implementation:
        Texture:
            voronoi voronoi_1D voronoi_2D voronoi_3D voronoi_4D 

    Args:
        vector (DataSocket): Vector
        w (DataSocket): Float
        scale (DataSocket): Float
        smoothness (DataSocket): Float
        exponent (DataSocket): Float
        randomness (DataSocket): Float
        distance (str): Node parameter, default = 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
        feature (str): Node parameter, default = 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
        voronoi_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **distance** : Float
        - **color** : Color
        - **position** : Vector
        - **w** : Float
        - **radius** : Float

    .. blid:: ShaderNodeTexVoronoi

    """

    def __init__(self, vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None, node_color=None):

        super().__init__('ShaderNodeTexVoronoi', node_name='Voronoi Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.distance        = distance
        self.bnode.feature         = feature
        self.bnode.voronoi_dimensions = voronoi_dimensions

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'w' : 1, 'scale' : 2, 'smoothness' : 3, 'exponent' : 4, 'randomness' : 5, }
        self.outsockets = {'distance' : 0, 'color' : 1, 'position' : 2, 'w' : 3, 'radius' : 4, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if w               is not None: self.w               = w
        if scale           is not None: self.scale           = scale
        if smoothness      is not None: self.smoothness      = smoothness
        if exponent        is not None: self.exponent        = exponent
        if randomness      is not None: self.randomness      = randomness

    @property
    def distance_(self):
        return self.bnode.distance

    @distance_.setter
    def distance_(self, value):
        self.bnode.distance = value

    @property
    def feature(self):
        return self.bnode.feature

    @feature.setter
    def feature(self, value):
        self.bnode.feature = value

    @property
    def voronoi_dimensions(self):
        return self.bnode.voronoi_dimensions

    @voronoi_dimensions.setter
    def voronoi_dimensions(self, value):
        self.bnode.voronoi_dimensions = value

    @property
    def distance(self):
        return self.get_output_socket('distance')

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def position(self):
        return self.get_output_socket('position')

    @property
    def w(self):
        return self.get_output_socket('w')

    @property
    def radius(self):
        return self.get_output_socket('radius')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'VoronoiTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @w.setter
    def w(self, value):
        self.set_input_socket('w', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'VoronoiTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def smoothness(self):
        raise AttributeError("Attribute error on node 'VoronoiTexture': the input socket 'smoothness' is write only.")

    @smoothness.setter
    def smoothness(self, value):
        self.set_input_socket('smoothness', value)

    @property
    def exponent(self):
        raise AttributeError("Attribute error on node 'VoronoiTexture': the input socket 'exponent' is write only.")

    @exponent.setter
    def exponent(self, value):
        self.set_input_socket('exponent', value)

    @property
    def randomness(self):
        raise AttributeError("Attribute error on node 'VoronoiTexture': the input socket 'randomness' is write only.")

    @randomness.setter
    def randomness(self, value):
        self.set_input_socket('randomness', value)

# ----------------------------------------------------------------------------------------------------
# Node WaveTexture for ShaderNodeTexWave

class WaveTexture(Node):

    """Node *Wave Texture*

    .. _WaveTexture:

    Node implementation:
        Texture:
            wave wave_bands wave_rings wave_bands_sine wave_bands_saw wave_bands_triangle wave_rings_sine wave_rings_saw wave_rings_triangle 

    Args:
        vector (DataSocket): Vector
        scale (DataSocket): Float
        distortion (DataSocket): Float
        detail (DataSocket): Float
        detail_scale (DataSocket): Float
        detail_roughness (DataSocket): Float
        phase_offset (DataSocket): Float
        bands_direction (str): Node parameter, default = 'X' in ('X', 'Y', 'Z', 'DIAGONAL')
        rings_direction (str): Node parameter, default = 'X' in ('X', 'Y', 'Z', 'SPHERICAL')
        wave_profile (str): Node parameter, default = 'SIN' in ('SIN', 'SAW', 'TRI')
        wave_type (str): Node parameter, default = 'BANDS' in ('BANDS', 'RINGS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **fac** : Float

    .. blid:: ShaderNodeTexWave

    """

    def __init__(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None, node_color=None):

        super().__init__('ShaderNodeTexWave', node_name='Wave Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.bands_direction = bands_direction
        self.bnode.rings_direction = rings_direction
        self.bnode.wave_profile    = wave_profile
        self.bnode.wave_type       = wave_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'scale' : 1, 'distortion' : 2, 'detail' : 3, 'detail_scale' : 4, 'detail_roughness' : 5, 'phase_offset' : 6, }
        self.outsockets = {'color' : 0, 'fac' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if scale           is not None: self.scale           = scale
        if distortion      is not None: self.distortion      = distortion
        if detail          is not None: self.detail          = detail
        if detail_scale    is not None: self.detail_scale    = detail_scale
        if detail_roughness is not None: self.detail_roughness = detail_roughness
        if phase_offset    is not None: self.phase_offset    = phase_offset

    @property
    def bands_direction(self):
        return self.bnode.bands_direction

    @bands_direction.setter
    def bands_direction(self, value):
        self.bnode.bands_direction = value

    @property
    def rings_direction(self):
        return self.bnode.rings_direction

    @rings_direction.setter
    def rings_direction(self, value):
        self.bnode.rings_direction = value

    @property
    def wave_profile(self):
        return self.bnode.wave_profile

    @wave_profile.setter
    def wave_profile(self, value):
        self.bnode.wave_profile = value

    @property
    def wave_type(self):
        return self.bnode.wave_type

    @wave_type.setter
    def wave_type(self, value):
        self.bnode.wave_type = value

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def fac(self):
        return self.get_output_socket('fac')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

    @property
    def distortion(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'distortion' is write only.")

    @distortion.setter
    def distortion(self, value):
        self.set_input_socket('distortion', value)

    @property
    def detail(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'detail' is write only.")

    @detail.setter
    def detail(self, value):
        self.set_input_socket('detail', value)

    @property
    def detail_scale(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'detail_scale' is write only.")

    @detail_scale.setter
    def detail_scale(self, value):
        self.set_input_socket('detail_scale', value)

    @property
    def detail_roughness(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'detail_roughness' is write only.")

    @detail_roughness.setter
    def detail_roughness(self, value):
        self.set_input_socket('detail_roughness', value)

    @property
    def phase_offset(self):
        raise AttributeError("Attribute error on node 'WaveTexture': the input socket 'phase_offset' is write only.")

    @phase_offset.setter
    def phase_offset(self, value):
        self.set_input_socket('phase_offset', value)

# ----------------------------------------------------------------------------------------------------
# Node WhiteNoiseTexture for ShaderNodeTexWhiteNoise

class WhiteNoiseTexture(Node):

    """Node *White Noise Texture*

    .. _WhiteNoiseTexture:

    Node implementation:
        Texture:
            white_noise white_noise_1D white_noise_2D white_noise_3D white_noise_4D 

    Args:
        vector (DataSocket): Vector
        w (DataSocket): Float
        noise_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : Float
        - **color** : Color

    .. blid:: ShaderNodeTexWhiteNoise

    """

    def __init__(self, vector=None, w=None, noise_dimensions='3D', label=None, node_color=None):

        super().__init__('ShaderNodeTexWhiteNoise', node_name='White Noise Texture', label=label, node_color=node_color)

        # Node parameters

        self.bnode.noise_dimensions = noise_dimensions

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'w' : 1, }
        self.outsockets = {'value' : 0, 'color' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if w               is not None: self.w               = w

    @property
    def noise_dimensions(self):
        return self.bnode.noise_dimensions

    @noise_dimensions.setter
    def noise_dimensions(self, value):
        self.bnode.noise_dimensions = value

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def vector(self):
        raise AttributeError("Attribute error on node 'WhiteNoiseTexture': the input socket 'vector' is write only.")

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def w(self):
        raise AttributeError("Attribute error on node 'WhiteNoiseTexture': the input socket 'w' is write only.")

    @w.setter
    def w(self, value):
        self.set_input_socket('w', value)

# ----------------------------------------------------------------------------------------------------
# Node ColorRamp for ShaderNodeValToRGB

class ColorRamp(Node):

    """Node *ColorRamp*

    .. _ColorRamp:

    Node implementation:
        global functions:
            color_ramp 
        Float:
            color_ramp 

    Args:
        fac (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **color** : Color
        - **alpha** : Float

    .. blid:: ShaderNodeValToRGB

    """

    def __init__(self, fac=None, label=None, node_color=None):

        super().__init__('ShaderNodeValToRGB', node_name='ColorRamp', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, }
        self.outsockets = {'color' : 0, 'alpha' : 1, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac

    @property
    def color(self):
        return self.get_output_socket('color')

    @property
    def alpha(self):
        return self.get_output_socket('alpha')

    @property
    def fac(self):
        raise AttributeError("Attribute error on node 'ColorRamp': the input socket 'fac' is write only.")

    @fac.setter
    def fac(self, value):
        self.set_input_socket('fac', value)

# ----------------------------------------------------------------------------------------------------
# Node Value for ShaderNodeValue

class Value(Node):

    """Node *Value*

    .. _Value:

    Node implementation:
        Float:
            Value 

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **value** : Float

    .. blid:: ShaderNodeValue

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('ShaderNodeValue', node_name='Value', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'value' : 0, }

    @property
    def value(self):
        return self.get_output_socket('value')

# ----------------------------------------------------------------------------------------------------
# Node VectorCurves for ShaderNodeVectorCurve

class VectorCurves(Node):

    """Node *Vector Curves*

    .. _VectorCurves:

    Node implementation:
        Vector:
            curves 

    Args:
        fac (DataSocket): Float
        vector (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vector** : Vector

    .. blid:: ShaderNodeVectorCurve

    """

    def __init__(self, fac=None, vector=None, label=None, node_color=None):

        super().__init__('ShaderNodeVectorCurve', node_name='Vector Curves', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, 'vector' : 1, }
        self.outsockets = {'vector' : 0, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac
        if vector          is not None: self.vector          = vector

    @property
    def vector(self):
        return self.get_output_socket('vector')

    @property
    def fac(self):
        raise AttributeError("Attribute error on node 'VectorCurves': the input socket 'fac' is write only.")

    @fac.setter
    def fac(self, value):
        self.set_input_socket('fac', value)

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

# ----------------------------------------------------------------------------------------------------
# Node VectorMath for ShaderNodeVectorMath

class VectorMath(Node):

    """Node *Vector Math*

    .. _VectorMath:

    Node implementation:
        Vector:
            add subtract sub multiply mul divide div multiply_add mul_add cross_product 
            cross project reflect refract face_forward dot_product dot distance length scale 
            normalize absolute abs minimum min maximum max floor ceil fraction 
            fract modulo wrap snap sine sin cosine cos tangent tan 

    Args:
        vector0 (DataSocket): Vector
        vector1 (DataSocket): Vector
        vector2 (DataSocket): Vector
        scale (DataSocket): Float
        operation (str): Node parameter, default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vector** : Vector
        - **value** : Float

    .. blid:: ShaderNodeVectorMath

    """

    def __init__(self, vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None, node_color=None):

        super().__init__('ShaderNodeVectorMath', node_name='Vector Math', label=label, node_color=node_color)

        # Node parameters

        self.bnode.operation       = operation

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector0' : 0, 'vector1' : 1, 'vector2' : 2, 'scale' : 3, }
        self.outsockets = {'vector' : 0, 'value' : 1, }

        # Input sockets plugging

        if vector0         is not None: self.vector0         = vector0
        if vector1         is not None: self.vector1         = vector1
        if vector2         is not None: self.vector2         = vector2
        if scale           is not None: self.scale           = scale

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

    @property
    def vector(self):
        return self.get_output_socket('vector')

    @property
    def value(self):
        return self.get_output_socket('value')

    @property
    def vector0(self):
        raise AttributeError("Attribute error on node 'VectorMath': the input socket 'vector0' is write only.")

    @vector0.setter
    def vector0(self, value):
        self.set_input_socket('vector0', value)

    @property
    def vector1(self):
        raise AttributeError("Attribute error on node 'VectorMath': the input socket 'vector1' is write only.")

    @vector1.setter
    def vector1(self, value):
        self.set_input_socket('vector1', value)

    @property
    def vector2(self):
        raise AttributeError("Attribute error on node 'VectorMath': the input socket 'vector2' is write only.")

    @vector2.setter
    def vector2(self, value):
        self.set_input_socket('vector2', value)

    @property
    def scale(self):
        raise AttributeError("Attribute error on node 'VectorMath': the input socket 'scale' is write only.")

    @scale.setter
    def scale(self, value):
        self.set_input_socket('scale', value)

# ----------------------------------------------------------------------------------------------------
# Node VectorRotate for ShaderNodeVectorRotate

class VectorRotate(Node):

    """Node *Vector Rotate*

    .. _VectorRotate:

    Node implementation:
        Vector:
            rotate_euler rotate_axis_angle rotate_x rotate_y rotate_z 

    Args:
        vector (DataSocket): Vector
        center (DataSocket): Vector
        axis (DataSocket): Vector
        angle (DataSocket): Float
        rotation (DataSocket): Vector
        invert (bool): Node parameter, default = False
        rotation_type (str): Node parameter, default = 'AXIS_ANGLE' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - **vector** : Vector

    .. blid:: ShaderNodeVectorRotate

    """

    def __init__(self, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None, node_color=None):

        super().__init__('ShaderNodeVectorRotate', node_name='Vector Rotate', label=label, node_color=node_color)

        # Node parameters

        self.bnode.invert          = invert
        self.bnode.rotation_type   = rotation_type

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'center' : 1, 'axis' : 2, 'angle' : 3, 'rotation' : 4, }
        self.outsockets = {'vector' : 0, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if center          is not None: self.center          = center
        if axis            is not None: self.axis            = axis
        if angle           is not None: self.angle           = angle
        if rotation        is not None: self.rotation        = rotation

    @property
    def invert(self):
        return self.bnode.invert

    @invert.setter
    def invert(self, value):
        self.bnode.invert = value

    @property
    def rotation_type(self):
        return self.bnode.rotation_type

    @rotation_type.setter
    def rotation_type(self, value):
        self.bnode.rotation_type = value

    @property
    def vector(self):
        return self.get_output_socket('vector')

    @vector.setter
    def vector(self, value):
        self.set_input_socket('vector', value)

    @property
    def center(self):
        raise AttributeError("Attribute error on node 'VectorRotate': the input socket 'center' is write only.")

    @center.setter
    def center(self, value):
        self.set_input_socket('center', value)

    @property
    def axis(self):
        raise AttributeError("Attribute error on node 'VectorRotate': the input socket 'axis' is write only.")

    @axis.setter
    def axis(self, value):
        self.set_input_socket('axis', value)

    @property
    def angle(self):
        raise AttributeError("Attribute error on node 'VectorRotate': the input socket 'angle' is write only.")

    @angle.setter
    def angle(self, value):
        self.set_input_socket('angle', value)

    @property
    def rotation(self):
        raise AttributeError("Attribute error on node 'VectorRotate': the input socket 'rotation' is write only.")

    @rotation.setter
    def rotation(self, value):
        self.set_input_socket('rotation', value)
# --------------------------------------------------------------------------------
# Create node from its bl_idname

def create_node(bl_idname, *args, **kwargs):
    nodes = {'FunctionNodeAlignEulerToVector': AlignEulerToVector,
    'FunctionNodeBooleanMath': BooleanMath,
    'FunctionNodeCombineColor': CombineColor,
    'FunctionNodeCompare': Compare,
    'FunctionNodeFloatToInt': FloatToInteger,
    'FunctionNodeInputBool': Boolean,
    'FunctionNodeInputColor': Color,
    'FunctionNodeInputInt': Integer,
    'FunctionNodeInputSpecialCharacters': SpecialCharacters,
    'FunctionNodeInputString': String,
    'FunctionNodeInputVector': Vector,
    'FunctionNodeRandomValue': RandomValue,
    'FunctionNodeReplaceString': ReplaceString,
    'FunctionNodeRotateEuler': RotateEuler,
    'FunctionNodeSeparateColor': SeparateColor,
    'FunctionNodeSliceString': SliceString,
    'FunctionNodeStringLength': StringLength,
    'FunctionNodeValueToString': ValueToString,
    'GeometryNodeAccumulateField': AccumulateField,
    'GeometryNodeAttributeDomainSize': DomainSize,
    'GeometryNodeAttributeStatistic': AttributeStatistic,
    'GeometryNodeBoundBox': BoundingBox,
    'GeometryNodeCaptureAttribute': CaptureAttribute,
    'GeometryNodeCollectionInfo': CollectionInfo,
    'GeometryNodeConvexHull': ConvexHull,
    'GeometryNodeCornersOfFace': CornersOfFace,
    'GeometryNodeCornersOfVertex': CornersOfVertex,
    'GeometryNodeCurveArc': Arc,
    'GeometryNodeCurveEndpointSelection': EndpointSelection,
    'GeometryNodeCurveHandleTypeSelection': HandleTypeSelection,
    'GeometryNodeCurveLength': CurveLength,
    'GeometryNodeCurveOfPoint': CurveOfPoint,
    'GeometryNodeCurvePrimitiveBezierSegment': BezierSegment,
    'GeometryNodeCurvePrimitiveCircle': CurveCircle,
    'GeometryNodeCurvePrimitiveLine': CurveLine,
    'GeometryNodeCurvePrimitiveQuadrilateral': Quadrilateral,
    'GeometryNodeCurveQuadraticBezier': QuadraticBezier,
    'GeometryNodeCurveSetHandles': SetHandleType,
    'GeometryNodeCurveSpiral': Spiral,
    'GeometryNodeCurveSplineType': SetSplineType,
    'GeometryNodeCurveStar': Star,
    'GeometryNodeCurveToMesh': CurveToMesh,
    'GeometryNodeCurveToPoints': CurveToPoints,
    'GeometryNodeDeformCurvesOnSurface': DeformCurvesOnSurface,
    'GeometryNodeDeleteGeometry': DeleteGeometry,
    'GeometryNodeDistributePointsInVolume': DistributePointsInVolume,
    'GeometryNodeDistributePointsOnFaces': DistributePointsOnFaces,
    'GeometryNodeDualMesh': DualMesh,
    'GeometryNodeDuplicateElements': DuplicateElements,
    'GeometryNodeEdgePathsToCurves': EdgePathsToCurves,
    'GeometryNodeEdgePathsToSelection': EdgePathsToSelection,
    'GeometryNodeEdgesOfCorner': EdgesOfCorner,
    'GeometryNodeEdgesOfVertex': EdgesOfVertex,
    'GeometryNodeExtrudeMesh': ExtrudeMesh,
    'GeometryNodeFaceOfCorner': FaceOfCorner,
    'GeometryNodeFieldAtIndex': FieldAtIndex,
    'GeometryNodeFieldOnDomain': InterpolateDomain,
    'GeometryNodeFillCurve': FillCurve,
    'GeometryNodeFilletCurve': FilletCurve,
    'GeometryNodeFlipFaces': FlipFaces,
    'GeometryNodeGeometryToInstance': GeometryToInstance,
    'GeometryNodeGroup': Group,
    'GeometryNodeImageTexture': ImageTexture,
    'GeometryNodeInputCurveHandlePositions': CurveHandlePositions,
    'GeometryNodeInputCurveTilt': CurveTilt,
    'GeometryNodeInputID': ID,
    'GeometryNodeInputIndex': Index,
    'GeometryNodeInputInstanceRotation': InstanceRotation,
    'GeometryNodeInputInstanceScale': InstanceScale,
    'GeometryNodeInputMaterial': Material,
    'GeometryNodeInputMaterialIndex': MaterialIndex,
    'GeometryNodeInputMeshEdgeAngle': EdgeAngle,
    'GeometryNodeInputMeshEdgeNeighbors': EdgeNeighbors,
    'GeometryNodeInputMeshEdgeVertices': EdgeVertices,
    'GeometryNodeInputMeshFaceArea': FaceArea,
    'GeometryNodeInputMeshFaceIsPlanar': FaceIsPlanar,
    'GeometryNodeInputMeshFaceNeighbors': FaceNeighbors,
    'GeometryNodeInputMeshIsland': MeshIsland,
    'GeometryNodeInputMeshVertexNeighbors': VertexNeighbors,
    'GeometryNodeInputNamedAttribute': NamedAttribute,
    'GeometryNodeInputNormal': Normal,
    'GeometryNodeInputPosition': Position,
    'GeometryNodeInputRadius': Radius,
    'GeometryNodeInputSceneTime': SceneTime,
    'GeometryNodeInputShadeSmooth': IsShadeSmooth,
    'GeometryNodeInputShortestEdgePaths': ShortestEdgePaths,
    'GeometryNodeInputSplineCyclic': IsSplineCyclic,
    'GeometryNodeInputSplineResolution': SplineResolution,
    'GeometryNodeInputTangent': CurveTangent,
    'GeometryNodeInstanceOnPoints': InstanceOnPoints,
    'GeometryNodeInstancesToPoints': InstancesToPoints,
    'GeometryNodeIsViewport': IsViewport,
    'GeometryNodeJoinGeometry': JoinGeometry,
    'GeometryNodeMaterialSelection': MaterialSelection,
    'GeometryNodeMergeByDistance': MergeByDistance,
    'GeometryNodeMeshBoolean': MeshBoolean,
    'GeometryNodeMeshCircle': MeshCircle,
    'GeometryNodeMeshCone': Cone,
    'GeometryNodeMeshCube': Cube,
    'GeometryNodeMeshCylinder': Cylinder,
    'GeometryNodeMeshFaceSetBoundaries': FaceSetBoundaries,
    'GeometryNodeMeshGrid': Grid,
    'GeometryNodeMeshIcoSphere': IcoSphere,
    'GeometryNodeMeshLine': MeshLine,
    'GeometryNodeMeshToCurve': MeshToCurve,
    'GeometryNodeMeshToPoints': MeshToPoints,
    'GeometryNodeMeshToVolume': MeshToVolume,
    'GeometryNodeMeshUVSphere': UvSphere,
    'GeometryNodeObjectInfo': ObjectInfo,
    'GeometryNodeOffsetCornerInFace': OffsetCornerInFace,
    'GeometryNodeOffsetPointInCurve': OffsetPointInCurve,
    'GeometryNodePoints': Points,
    'GeometryNodePointsOfCurve': PointsOfCurve,
    'GeometryNodePointsToVertices': PointsToVertices,
    'GeometryNodePointsToVolume': PointsToVolume,
    'GeometryNodeProximity': GeometryProximity,
    'GeometryNodeRaycast': Raycast,
    'GeometryNodeRealizeInstances': RealizeInstances,
    'GeometryNodeRemoveAttribute': RemoveNamedAttribute,
    'GeometryNodeReplaceMaterial': ReplaceMaterial,
    'GeometryNodeResampleCurve': ResampleCurve,
    'GeometryNodeReverseCurve': ReverseCurve,
    'GeometryNodeRotateInstances': RotateInstances,
    'GeometryNodeSampleCurve': SampleCurve,
    'GeometryNodeSampleIndex': SampleIndex,
    'GeometryNodeSampleNearest': SampleNearest,
    'GeometryNodeSampleNearestSurface': SampleNearestSurface,
    'GeometryNodeSampleUVSurface': SampleUvSurface,
    'GeometryNodeScaleElements': ScaleElements,
    'GeometryNodeScaleInstances': ScaleInstances,
    'GeometryNodeSelfObject': SelfObject,
    'GeometryNodeSeparateComponents': SeparateComponents,
    'GeometryNodeSeparateGeometry': SeparateGeometry,
    'GeometryNodeSetCurveHandlePositions': SetHandlePositions,
    'GeometryNodeSetCurveNormal': SetCurveNormal,
    'GeometryNodeSetCurveRadius': SetCurveRadius,
    'GeometryNodeSetCurveTilt': SetCurveTilt,
    'GeometryNodeSetID': SetID,
    'GeometryNodeSetMaterial': SetMaterial,
    'GeometryNodeSetMaterialIndex': SetMaterialIndex,
    'GeometryNodeSetPointRadius': SetPointRadius,
    'GeometryNodeSetPosition': SetPosition,
    'GeometryNodeSetShadeSmooth': SetShadeSmooth,
    'GeometryNodeSetSplineCyclic': SetSplineCyclic,
    'GeometryNodeSetSplineResolution': SetSplineResolution,
    'GeometryNodeSplineLength': SplineLength,
    'GeometryNodeSplineParameter': SplineParameter,
    'GeometryNodeSplitEdges': SplitEdges,
    'GeometryNodeStoreNamedAttribute': StoreNamedAttribute,
    'GeometryNodeStringJoin': JoinStrings,
    'GeometryNodeStringToCurves': StringToCurves,
    'GeometryNodeSubdivideCurve': SubdivideCurve,
    'GeometryNodeSubdivideMesh': SubdivideMesh,
    'GeometryNodeSubdivisionSurface': SubdivisionSurface,
    'GeometryNodeSwitch': Switch,
    'GeometryNodeTransform': Transform,
    'GeometryNodeTranslateInstances': TranslateInstances,
    'GeometryNodeTriangulate': Triangulate,
    'GeometryNodeTrimCurve': TrimCurve,
    'GeometryNodeUVPackIslands': PackUvIslands,
    'GeometryNodeUVUnwrap': UvUnwrap,
    'GeometryNodeVertexOfCorner': VertexOfCorner,
    'GeometryNodeVolumeCube': VolumeCube,
    'GeometryNodeVolumeToMesh': VolumeToMesh,
    'ShaderNodeClamp': Clamp,
    'ShaderNodeCombineXYZ': CombineXyz,
    'ShaderNodeFloatCurve': FloatCurve,
    'ShaderNodeMapRange': MapRange,
    'ShaderNodeMath': Math,
    'ShaderNodeMix': Mix,
    'ShaderNodeRGBCurve': RgbCurves,
    'ShaderNodeSeparateXYZ': SeparateXyz,
    'ShaderNodeTexBrick': BrickTexture,
    'ShaderNodeTexChecker': CheckerTexture,
    'ShaderNodeTexGradient': GradientTexture,
    'ShaderNodeTexMagic': MagicTexture,
    'ShaderNodeTexMusgrave': MusgraveTexture,
    'ShaderNodeTexNoise': NoiseTexture,
    'ShaderNodeTexVoronoi': VoronoiTexture,
    'ShaderNodeTexWave': WaveTexture,
    'ShaderNodeTexWhiteNoise': WhiteNoiseTexture,
    'ShaderNodeValToRGB': ColorRamp,
    'ShaderNodeValue': Value,
    'ShaderNodeVectorCurve': VectorCurves,
    'ShaderNodeVectorMath': VectorMath,
    'ShaderNodeVectorRotate': VectorRotate}
    return nodes[bl_idname](*args, **kwargs)

