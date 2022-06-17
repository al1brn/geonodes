#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-17
@author: Generated from generator module
Blender version: 3.2.0
"""

from geonodes.core.node import Node


# ----------------------------------------------------------------------------------------------------
# Node AlignEulerToVector for FunctionNodeAlignEulerToVector

class AlignEulerToVector(Node):

    """

    Node AlignEulerToVector
    -----------------------
        > Geometry node name: Align Euler to Vector<br>
          Blender type: Align Euler to Vector
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - rotation : Vector
                - factor : Float
                - vector : Vector
    

            Parameters
            ----------
                - axis : str (default = 'X') in ('X', 'Y', 'Z')
                - pivot_axis : str (default = 'AUTO') in ('AUTO', 'X', 'Y', 'Z')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - rotation : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.AlignToVector : Constructor
            - Vector.align_to_vector : Method
              
    """

    def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None, node_color=None):

        super().__init__('FunctionNodeAlignEulerToVector', name='Align Euler to Vector', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node BooleanMath for FunctionNodeBooleanMath

class BooleanMath(Node):

    """

    Node BooleanMath
    ----------------
        > Geometry node name: Boolean Math<br>
          Blender type: Boolean Math
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - boolean0 : Boolean
                - boolean1 : Boolean
    

            Parameters
            ----------
                - operation : str (default = 'AND') in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - boolean : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.b_and : Method
            - Boolean.b_not : Method
            - Boolean.b_or : Method
            - Boolean.imply : Method
            - Boolean.nand : Method
            - Boolean.nimply : Method
            - Boolean.nor : Method
            - Boolean.xnor : Method
            - Boolean.xor : Method
            - functions.b_and : Function
            - functions.b_not : Function
            - functions.b_or : Function
            - functions.imply : Function
            - functions.nand : Function
            - functions.nimply : Function
            - functions.nor : Function
            - functions.xnor : Function
            - functions.xor : Function
              
    """

    def __init__(self, boolean0=None, boolean1=None, operation='AND', label=None, node_color=None):

        super().__init__('FunctionNodeBooleanMath', name='Boolean Math', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Compare for FunctionNodeCompare

class Compare(Node):

    """

    Node Compare
    ------------
        > Geometry node name: Compare<br>
          Blender type: Compare
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - a : data_type dependant
                - b : data_type dependant
                - c : Float
                - angle : Float
                - epsilon : Float
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
                - mode : str (default = 'ELEMENT') in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
                - operation : str (default = 'GREATER_THAN') in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
            - Input sockets  : ['a', 'b']
            - Output sockets : []   
              
              
    

        Output sockets
        --------------
            - result : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Color.brighter : Method
            - Color.darker : Method
            - Color.equal : Method
            - Color.not_equal : Method
            - Float.equal : Method
            - Float.greater_equal : Method
            - Float.greater_than : Method
            - Float.less_equal : Method
            - Float.less_than : Method
            - Float.not_equal : Method
            - Integer.equal : Method
            - Integer.greater_equal : Method
            - Integer.greater_than : Method
            - Integer.less_equal : Method
            - Integer.less_than : Method
            - Integer.not_equal : Method
            - String.average : Method
            - String.direction : Method
            - String.dot_product : Method
            - String.element : Method
            - String.length : Method
            - Vector.equal : Method
            - Vector.greater_equal : Method
            - Vector.greater_than : Method
            - Vector.less_equal : Method
            - Vector.less_than : Method
            - Vector.not_equal : Method
            - functions.compare : Function
              
    """

    def __init__(self, a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None, node_color=None):

        super().__init__('FunctionNodeCompare', name='Compare', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node FloatToInteger for FunctionNodeFloatToInt

class FloatToInteger(Node):

    """

    Node FloatToInteger
    -------------------
        > Geometry node name: Float to Integer<br>
          Blender type: Float to Integer
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FloatToInteger(float=None, rounding_mode='ROUND', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - float : Float
    

            Parameters
            ----------
                - rounding_mode : str (default = 'ROUND') in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - integer : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.to_integer : Method
              
    """

    def __init__(self, float=None, rounding_mode='ROUND', label=None, node_color=None):

        super().__init__('FunctionNodeFloatToInt', name='Float to Integer', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Boolean for FunctionNodeInputBool

class Boolean(Node):

    """

    Node Boolean
    ------------
        > Geometry node name: Boolean<br>
          Blender type: Boolean
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Boolean(boolean=False, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Parameters
            ----------
                - boolean : bool (default = False)
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - boolean : Boolean
    """

    def __init__(self, boolean=False, label=None, node_color=None):

        super().__init__('FunctionNodeInputBool', name='Boolean', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Color for FunctionNodeInputColor

class Color(Node):

    """

    Node Color
    ----------
        > Geometry node name: Color<br>
          Blender type: Color
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Color(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('FunctionNodeInputColor', name='Color', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'color' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Integer for FunctionNodeInputInt

class Integer(Node):

    """

    Node Integer
    ------------
        > Geometry node name: Integer<br>
          Blender type: Integer
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Integer(integer=0, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Parameters
            ----------
                - integer : int (default = 0)
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - integer : Integer
    """

    def __init__(self, integer=0, label=None, node_color=None):

        super().__init__('FunctionNodeInputInt', name='Integer', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node SpecialCharacters for FunctionNodeInputSpecialCharacters

class SpecialCharacters(Node):

    """

    Node SpecialCharacters
    ----------------------
        > Geometry node name: Special Characters<br>
          Blender type: Special Characters
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SpecialCharacters(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - line_break : String
            - tab : String
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('FunctionNodeInputSpecialCharacters', name='Special Characters', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'line_break' : 0, 'tab' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node String for FunctionNodeInputString

class String(Node):

    """

    Node String
    -----------
        > Geometry node name: String<br>
          Blender type: String
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.String(string='', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Parameters
            ----------
                - string : str (default = '')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - string : String
    """

    def __init__(self, string='', label=None, node_color=None):

        super().__init__('FunctionNodeInputString', name='String', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Vector for FunctionNodeInputVector

class Vector(Node):

    """

    Node Vector
    -----------
        > Geometry node name: Vector<br>
          Blender type: Vector
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Vector(vector=[0.0, 0.0, 0.0], label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Parameters
            ----------
                - vector : Vector (default = [0.0, 0.0, 0.0])
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vector : Vector
    """

    def __init__(self, vector=[0.0, 0.0, 0.0], label=None, node_color=None):

        super().__init__('FunctionNodeInputVector', name='Vector', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node RandomValue for FunctionNodeRandomValue

class RandomValue(Node):

    """

    Node RandomValue
    ----------------
        > Geometry node name: Random Value<br>
          Blender type: Random Value
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - min : data_type dependant
                - max : data_type dependant
                - probability : Float
                - ID : Integer
                - seed : Integer
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
            - Input sockets  : ['min', 'max']
            - Output sockets : ['value']   
              
              
    

        Output sockets
        --------------
            - value : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.Random : Constructor
            - Float.Random : Constructor
            - Integer.Random : Constructor
            - Vector.Random : Constructor
              
    """

    def __init__(self, min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None, node_color=None):

        super().__init__('FunctionNodeRandomValue', name='Random Value', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type

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

# ----------------------------------------------------------------------------------------------------
# Node ReplaceString for FunctionNodeReplaceString

class ReplaceString(Node):

    """

    Node ReplaceString
    ------------------
        > Geometry node name: Replace String<br>
          Blender type: Replace String
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ReplaceString(string=None, find=None, replace=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - string : String
                - find : String
                - replace : String
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - string : String
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - String.replace : Method
              
    """

    def __init__(self, string=None, find=None, replace=None, label=None, node_color=None):

        super().__init__('FunctionNodeReplaceString', name='Replace String', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, 'find' : 1, 'replace' : 2, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if string          is not None: self.string          = string
        if find            is not None: self.find            = find
        if replace         is not None: self.replace         = replace

# ----------------------------------------------------------------------------------------------------
# Node RotateEuler for FunctionNodeRotateEuler

class RotateEuler(Node):

    """

    Node RotateEuler
    ----------------
        > Geometry node name: Rotate Euler<br>
          Blender type: Rotate Euler
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - rotation : Vector
                - rotate_by : Vector
                - axis : Vector
                - angle : Float
    

            Parameters
            ----------
                - space : str (default = 'OBJECT') in ('OBJECT', 'LOCAL')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - rotation : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.rotate_euler : Method
              
    """

    def __init__(self, rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None, node_color=None):

        super().__init__('FunctionNodeRotateEuler', name='Rotate Euler', label=label, node_color=node_color)

        # Node parameters

        self.bnode.space           = space

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

# ----------------------------------------------------------------------------------------------------
# Node SliceString for FunctionNodeSliceString

class SliceString(Node):

    """

    Node SliceString
    ----------------
        > Geometry node name: Slice String<br>
          Blender type: Slice String
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SliceString(string=None, position=None, length=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - string : String
                - position : Integer
                - length : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - string : String
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - String.slice : Method
              
    """

    def __init__(self, string=None, position=None, length=None, label=None, node_color=None):

        super().__init__('FunctionNodeSliceString', name='Slice String', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, 'position' : 1, 'length' : 2, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if string          is not None: self.string          = string
        if position        is not None: self.position        = position
        if length          is not None: self.length          = length

# ----------------------------------------------------------------------------------------------------
# Node StringLength for FunctionNodeStringLength

class StringLength(Node):

    """

    Node StringLength
    -----------------
        > Geometry node name: String Length<br>
          Blender type: String Length
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.StringLength(string=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - string : String
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - length : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - String.length : Property
              
    """

    def __init__(self, string=None, label=None, node_color=None):

        super().__init__('FunctionNodeStringLength', name='String Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'string' : 0, }
        self.outsockets = {'length' : 0, }

        # Input sockets plugging

        if string          is not None: self.string          = string

# ----------------------------------------------------------------------------------------------------
# Node ValueToString for FunctionNodeValueToString

class ValueToString(Node):

    """

    Node ValueToString
    ------------------
        > Geometry node name: Value to String<br>
          Blender type: Value to String
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ValueToString(value=None, decimals=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - value : Float
                - decimals : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - string : String
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.to_string : Method
              
    """

    def __init__(self, value=None, decimals=None, label=None, node_color=None):

        super().__init__('FunctionNodeValueToString', name='Value to String', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'value' : 0, 'decimals' : 1, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if value           is not None: self.value           = value
        if decimals        is not None: self.decimals        = decimals

# ----------------------------------------------------------------------------------------------------
# Node AccumulateField for GeometryNodeAccumulateField

class AccumulateField(Node):

    """

    Node AccumulateField
    --------------------
        > Geometry node name: Accumulate Field<br>
          Blender type: Accumulate Field
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.AccumulateField(value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - value : data_type dependant
                - group_index : Integer
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR')
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR')
            - Input sockets  : ['value']
            - Output sockets : ['leading', 'trailing', 'total']   
              
              
    

        Output sockets
        --------------
            - leading : data_type dependant
            - trailing : data_type dependant
            - total : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.accumulate_field : Method
            - Integer.accumulate_field : Method
            - Vector.accumulate_field : Method
              
    """

    def __init__(self, value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeAccumulateField', name='Accumulate Field', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node DomainSize for GeometryNodeAttributeDomainSize

class DomainSize(Node):

    """

    Node DomainSize
    ---------------
        > Geometry node name: Domain Size<br>
          Blender type: Domain Size
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.DomainSize(geometry=None, component='MESH', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
    

            Parameters
            ----------
                - component : str (default = 'MESH') in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - point_count : Integer
            - edge_count : Integer
            - face_count : Integer
            - face_corner_count : Integer
            - spline_count : Integer
            - instance_count : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.attribute_domain_size : Method
              
    """

    def __init__(self, geometry=None, component='MESH', label=None, node_color=None):

        super().__init__('GeometryNodeAttributeDomainSize', name='Domain Size', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node AttributeStatistic for GeometryNodeAttributeStatistic

class AttributeStatistic(Node):

    """

    Node AttributeStatistic
    -----------------------
        > Geometry node name: Attribute Statistic<br>
          Blender type: Attribute Statistic
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - attribute : data_type dependant
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'FLOAT_VECTOR')
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')
            - Input sockets  : ['attribute']
            - Output sockets : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']   
              
              
    

        Output sockets
        --------------
            - mean : data_type dependant
            - median : data_type dependant
            - sum : data_type dependant
            - min : data_type dependant
            - max : data_type dependant
            - range : data_type dependant
            - standard_deviation : data_type dependant
            - variance : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.attribute_statistic : Method
            - Vector.attribute_statistic : Method
              
    """

    def __init__(self, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeAttributeStatistic', name='Attribute Statistic', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node TransferAttribute for GeometryNodeAttributeTransfer

class TransferAttribute(Node):

    """

    Node TransferAttribute
    ----------------------
        > Geometry node name: Transfer Attribute<br>
          Blender type: Transfer Attribute
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.TransferAttribute(source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - source : Geometry
                - attribute : data_type dependant
                - source_position : Vector
                - index : Integer
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
                - mapping : str (default = 'NEAREST_FACE_INTERPOLATED') in ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
            - Input sockets  : ['attribute']
            - Output sockets : ['attribute']   
              
              
    

        Output sockets
        --------------
            - attribute : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.transfer_attribute : Method
            - Color.transfer_attribute : Method
            - Float.transfer_attribute : Method
            - Geometry.transfer_boolean : Method
            - Geometry.transfer_color : Method
            - Geometry.transfer_float : Method
            - Geometry.transfer_integer : Method
            - Geometry.transfer_vector : Method
            - Integer.transfer_attribute : Method
            - Vector.transfer_attribute : Method
              
    """

    def __init__(self, source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None, node_color=None):

        super().__init__('GeometryNodeAttributeTransfer', name='Transfer Attribute', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain
        self.bnode.mapping         = mapping

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'source' : 0, 'attribute' : [1, 2, 3, 4, 5], 'source_position' : 6, 'index' : 7, }
        self.outsockets = {'attribute' : [0, 1, 2, 3, 4], }

        # Input sockets plugging

        if source          is not None: self.source          = source
        if attribute       is not None: self.attribute       = attribute
        if source_position is not None: self.source_position = source_position
        if index           is not None: self.index           = index

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
    def mapping(self):
        return self.bnode.mapping

    @mapping.setter
    def mapping(self, value):
        self.bnode.mapping = value

# ----------------------------------------------------------------------------------------------------
# Node BoundingBox for GeometryNodeBoundBox

class BoundingBox(Node):

    """

    Node BoundingBox
    ----------------
        > Geometry node name: Bounding Box<br>
          Blender type: Bounding Box
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.BoundingBox(geometry=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - bounding_box : Geometry
            - min : Vector
            - max : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.bound_box : Property
            - Geometry.box : Property
            - Geometry.box_max : Property
            - Geometry.box_min : Property
              
    """

    def __init__(self, geometry=None, label=None, node_color=None):

        super().__init__('GeometryNodeBoundBox', name='Bounding Box', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'bounding_box' : 0, 'min' : 1, 'max' : 2, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

# ----------------------------------------------------------------------------------------------------
# Node CaptureAttribute for GeometryNodeCaptureAttribute

class CaptureAttribute(Node):

    """

    Node CaptureAttribute
    ---------------------
        > Geometry node name: Capture Attribute<br>
          Blender type: Capture Attribute
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - value : data_type dependant
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
            - Input sockets  : ['value']
            - Output sockets : ['attribute']   
              
              
    

        Output sockets
        --------------
            - geometry : Geometry
            - attribute : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.capture_attribute : Method
            - Color.capture_attribute : Method
            - Float.capture_attribute : Method
            - Geometry.capture_attribute : Method
            - Integer.capture_attribute : Method
            - Vector.capture_attribute : Method
              
    """

    def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeCaptureAttribute', name='Capture Attribute', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node CollectionInfo for GeometryNodeCollectionInfo

class CollectionInfo(Node):

    """

    Node CollectionInfo
    -------------------
        > Geometry node name: Collection Info<br>
          Blender type: Collection Info
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - collection : Collection
                - separate_children : Boolean
                - reset_children : Boolean
    

            Parameters
            ----------
                - transform_space : str (default = 'ORIGINAL') in ('ORIGINAL', 'RELATIVE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Collection.info : Method
              
    """

    def __init__(self, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None, node_color=None):

        super().__init__('GeometryNodeCollectionInfo', name='Collection Info', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node ConvexHull for GeometryNodeConvexHull

class ConvexHull(Node):

    """

    Node ConvexHull
    ---------------
        > Geometry node name: Convex Hull<br>
          Blender type: Convex Hull
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ConvexHull(geometry=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - convex_hull : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.convex_hull : Method
              
    """

    def __init__(self, geometry=None, label=None, node_color=None):

        super().__init__('GeometryNodeConvexHull', name='Convex Hull', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'convex_hull' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

# ----------------------------------------------------------------------------------------------------
# Node Arc for GeometryNodeCurveArc

class Arc(Node):

    """

    Node Arc
    --------
        > Geometry node name: Arc<br>
          Blender type: Arc
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Arc(resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - resolution : Integer
                - start : Vector
                - middle : Vector
                - end : Vector
                - radius : Float
                - start_angle : Float
                - sweep_angle : Float
                - offset_angle : Float
                - connect_center : Boolean
                - invert_arc : Boolean
    

            Parameters
            ----------
                - mode : str (default = 'RADIUS') in ('POINTS', 'RADIUS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
            - center : Vector
            - normal : Vector
            - radius : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.ArcFromPoints : Static method
            - Curve.ArcFromRadius : Constructor
              
    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None, node_color=None):

        super().__init__('GeometryNodeCurveArc', name='Arc', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node EndpointSelection for GeometryNodeCurveEndpointSelection

class EndpointSelection(Node):

    """

    Node EndpointSelection
    ----------------------
        > Geometry node name: Endpoint Selection<br>
          Blender type: Endpoint Selection
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.EndpointSelection(start_size=None, end_size=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - start_size : Integer
                - end_size : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - selection : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.endpoint_selection : Fields
              
    """

    def __init__(self, start_size=None, end_size=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveEndpointSelection', name='Endpoint Selection', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'start_size' : 0, 'end_size' : 1, }
        self.outsockets = {'selection' : 0, }

        # Input sockets plugging

        if start_size      is not None: self.start_size      = start_size
        if end_size        is not None: self.end_size        = end_size

# ----------------------------------------------------------------------------------------------------
# Node HandleTypeSelection for GeometryNodeCurveHandleTypeSelection

class HandleTypeSelection(Node):

    """

    Node HandleTypeSelection
    ------------------------
        > Geometry node name: Handle Type Selection<br>
          Blender type: Handle Type Selection
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Parameters
            ----------
                - handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
                - mode : set (default = {'LEFT', 'RIGHT'})
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - selection : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.handle_type_selection : Fields
            - CurveDomain.left_handle_align : Fields
            - CurveDomain.left_handle_auto : Fields
            - CurveDomain.left_handle_free : Fields
            - CurveDomain.left_handle_selection : Fields
            - CurveDomain.left_handle_vector : Fields
            - CurveDomain.right_handle_align : Fields
            - CurveDomain.right_handle_auto : Fields
            - CurveDomain.right_handle_free : Fields
            - CurveDomain.right_handle_selection : Fields
            - CurveDomain.right_handle_vector : Fields
              
    """

    def __init__(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None):

        super().__init__('GeometryNodeCurveHandleTypeSelection', name='Handle Type Selection', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node CurveLength for GeometryNodeCurveLength

class CurveLength(Node):

    """

    Node CurveLength
    ----------------
        > Geometry node name: Curve Length<br>
          Blender type: Curve Length
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveLength(curve=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - length : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.length : Method
              
    """

    def __init__(self, curve=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveLength', name='Curve Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, }
        self.outsockets = {'length' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve

# ----------------------------------------------------------------------------------------------------
# Node BezierSegment for GeometryNodeCurvePrimitiveBezierSegment

class BezierSegment(Node):

    """

    Node BezierSegment
    ------------------
        > Geometry node name: Bezier Segment<br>
          Blender type: Bezier Segment
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - resolution : Integer
                - start : Vector
                - start_handle : Vector
                - end_handle : Vector
                - end : Vector
    

            Parameters
            ----------
                - mode : str (default = 'POSITION') in ('POSITION', 'OFFSET')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.BezierSegment : Constructor
              
    """

    def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveBezierSegment', name='Bezier Segment', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node CurveCircle for GeometryNodeCurvePrimitiveCircle

class CurveCircle(Node):

    """

    Node CurveCircle
    ----------------
        > Geometry node name: Curve Circle<br>
          Blender type: Curve Circle
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveCircle(resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - resolution : Integer
                - point_1 : Vector
                - point_2 : Vector
                - point_3 : Vector
                - radius : Float
    

            Parameters
            ----------
                - mode : str (default = 'RADIUS') in ('POINTS', 'RADIUS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
            - center : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.Circle : Constructor
              
    """

    def __init__(self, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveCircle', name='Curve Circle', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node CurveLine for GeometryNodeCurvePrimitiveLine

class CurveLine(Node):

    """

    Node CurveLine
    --------------
        > Geometry node name: Curve Line<br>
          Blender type: Curve Line
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - start : Vector
                - end : Vector
                - direction : Vector
                - length : Float
    

            Parameters
            ----------
                - mode : str (default = 'POINTS') in ('POINTS', 'DIRECTION')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.Line : Constructor
              
    """

    def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveLine', name='Curve Line', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Quadrilateral for GeometryNodeCurvePrimitiveQuadrilateral

class Quadrilateral(Node):

    """

    Node Quadrilateral
    ------------------
        > Geometry node name: Quadrilateral<br>
          Blender type: Quadrilateral
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Quadrilateral(width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - width : Float
                - height : Float
                - bottom_width : Float
                - top_width : Float
                - offset : Float
                - bottom_height : Float
                - top_height : Float
                - point_1 : Vector
                - point_2 : Vector
                - point_3 : Vector
                - point_4 : Vector
    

            Parameters
            ----------
                - mode : str (default = 'RECTANGLE') in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.Quadrilateral : Constructor
              
    """

    def __init__(self, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None, node_color=None):

        super().__init__('GeometryNodeCurvePrimitiveQuadrilateral', name='Quadrilateral', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node QuadraticBezier for GeometryNodeCurveQuadraticBezier

class QuadraticBezier(Node):

    """

    Node QuadraticBezier
    --------------------
        > Geometry node name: Quadratic Bezier<br>
          Blender type: Quadratic Bezier
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.QuadraticBezier(resolution=None, start=None, middle=None, end=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - resolution : Integer
                - start : Vector
                - middle : Vector
                - end : Vector
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.QuadraticBezier : Constructor
              
    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveQuadraticBezier', name='Quadratic Bezier', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'resolution' : 0, 'start' : 1, 'middle' : 2, 'end' : 3, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if resolution      is not None: self.resolution      = resolution
        if start           is not None: self.start           = start
        if middle          is not None: self.middle          = middle
        if end             is not None: self.end             = end

# ----------------------------------------------------------------------------------------------------
# Node SetHandleType for GeometryNodeCurveSetHandles

class SetHandleType(Node):

    """

    Node SetHandleType
    ------------------
        > Geometry node name: Set Handle Type<br>
          Blender type: Set Handle Type
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
    

            Parameters
            ----------
                - handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
                - mode : set (default = {'LEFT', 'RIGHT'})
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.set_handles : Method
              
    """

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None):

        super().__init__('GeometryNodeCurveSetHandles', name='Set Handle Type', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Spiral for GeometryNodeCurveSpiral

class Spiral(Node):

    """

    Node Spiral
    -----------
        > Geometry node name: Spiral<br>
          Blender type: Spiral
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - resolution : Integer
                - rotations : Float
                - start_radius : Float
                - end_radius : Float
                - height : Float
                - reverse : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.Spiral : Constructor
              
    """

    def __init__(self, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveSpiral', name='Spiral', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node SetSplineType for GeometryNodeCurveSplineType

class SetSplineType(Node):

    """

    Node SetSplineType
    ------------------
        > Geometry node name: Set Spline Type<br>
          Blender type: Set Spline Type
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetSplineType(curve=None, selection=None, spline_type='POLY', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
    

            Parameters
            ----------
                - spline_type : str (default = 'POLY') in ('BEZIER', 'NURBS', 'POLY')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.set_spline_type : Method
              
    """

    def __init__(self, curve=None, selection=None, spline_type='POLY', label=None, node_color=None):

        super().__init__('GeometryNodeCurveSplineType', name='Set Spline Type', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Star for GeometryNodeCurveStar

class Star(Node):

    """

    Node Star
    ---------
        > Geometry node name: Star<br>
          Blender type: Star
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - points : Integer
                - inner_radius : Float
                - outer_radius : Float
                - twist : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
            - outer_points : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.Star : Constructor
              
    """

    def __init__(self, points=None, inner_radius=None, outer_radius=None, twist=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveStar', name='Star', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'inner_radius' : 1, 'outer_radius' : 2, 'twist' : 3, }
        self.outsockets = {'curve' : 0, 'outer_points' : 1, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if inner_radius    is not None: self.inner_radius    = inner_radius
        if outer_radius    is not None: self.outer_radius    = outer_radius
        if twist           is not None: self.twist           = twist

# ----------------------------------------------------------------------------------------------------
# Node CurveToMesh for GeometryNodeCurveToMesh

class CurveToMesh(Node):

    """

    Node CurveToMesh
    ----------------
        > Geometry node name: Curve to Mesh<br>
          Blender type: Curve to Mesh
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveToMesh(curve=None, profile_curve=None, fill_caps=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - profile_curve : Geometry
                - fill_caps : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.to_mesh : Method
              
    """

    def __init__(self, curve=None, profile_curve=None, fill_caps=None, label=None, node_color=None):

        super().__init__('GeometryNodeCurveToMesh', name='Curve to Mesh', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'profile_curve' : 1, 'fill_caps' : 2, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if profile_curve   is not None: self.profile_curve   = profile_curve
        if fill_caps       is not None: self.fill_caps       = fill_caps

# ----------------------------------------------------------------------------------------------------
# Node CurveToPoints for GeometryNodeCurveToPoints

class CurveToPoints(Node):

    """

    Node CurveToPoints
    ------------------
        > Geometry node name: Curve to Points<br>
          Blender type: Curve to Points
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveToPoints(curve=None, count=None, length=None, mode='COUNT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - count : Integer
                - length : Float
    

            Parameters
            ----------
                - mode : str (default = 'COUNT') in ('EVALUATED', 'COUNT', 'LENGTH')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - points : Points
            - tangent : Vector
            - normal : Vector
            - rotation : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.to_points : Method
              
    """

    def __init__(self, curve=None, count=None, length=None, mode='COUNT', label=None, node_color=None):

        super().__init__('GeometryNodeCurveToPoints', name='Curve to Points', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node DeleteGeometry for GeometryNodeDeleteGeometry

class DeleteGeometry(Node):

    """

    Node DeleteGeometry
    -------------------
        > Geometry node name: Delete Geometry<br>
          Blender type: Delete Geometry
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
    

            Parameters
            ----------
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
                - mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.delete_geometry : Method
              
    """

    def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL', label=None, node_color=None):

        super().__init__('GeometryNodeDeleteGeometry', name='Delete Geometry', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node DistributePointsOnFaces for GeometryNodeDistributePointsOnFaces

class DistributePointsOnFaces(Node):

    """

    Node DistributePointsOnFaces
    ----------------------------
        > Geometry node name: Distribute Points on Faces<br>
          Blender type: Distribute Points on Faces
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
                - distance_min : Float
                - density_max : Float
                - density : Float
                - density_factor : Float
                - seed : Integer
    

            Parameters
            ----------
                - distribute_method : str (default = 'RANDOM') in ('RANDOM', 'POISSON')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - points : Points
            - normal : Vector
            - rotation : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.distribute_points_on_faces : Method
              
    """

    def __init__(self, mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None):

        super().__init__('GeometryNodeDistributePointsOnFaces', name='Distribute Points on Faces', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node DualMesh for GeometryNodeDualMesh

class DualMesh(Node):

    """

    Node DualMesh
    -------------
        > Geometry node name: Dual Mesh<br>
          Blender type: Dual Mesh
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.DualMesh(mesh=None, keep_boundaries=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - keep_boundaries : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - dual_mesh : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.dual : Method
              
    """

    def __init__(self, mesh=None, keep_boundaries=None, label=None, node_color=None):

        super().__init__('GeometryNodeDualMesh', name='Dual Mesh', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'keep_boundaries' : 1, }
        self.outsockets = {'dual_mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if keep_boundaries is not None: self.keep_boundaries = keep_boundaries

# ----------------------------------------------------------------------------------------------------
# Node DuplicateElements for GeometryNodeDuplicateElements

class DuplicateElements(Node):

    """

    Node DuplicateElements
    ----------------------
        > Geometry node name: Duplicate Elements<br>
          Blender type: Duplicate Elements
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - amount : Integer
    

            Parameters
            ----------
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
            - duplicate_index : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.duplicate_elements : Method
            - Geometry.duplicate_points : Method
            - Instances.duplicate_instances : Method
            - Mesh.duplicate_edges : Method
            - Mesh.duplicate_faces : Method
            - Spline.duplicate_splines : Method
              
    """

    def __init__(self, geometry=None, selection=None, amount=None, domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeDuplicateElements', name='Duplicate Elements', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node ExtrudeMesh for GeometryNodeExtrudeMesh

class ExtrudeMesh(Node):

    """

    Node ExtrudeMesh
    ----------------
        > Geometry node name: Extrude Mesh<br>
          Blender type: Extrude Mesh
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
                - offset : Vector
                - offset_scale : Float
                - individual : Boolean
    

            Parameters
            ----------
                - mode : str (default = 'FACES') in ('VERTICES', 'EDGES', 'FACES')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
            - top : Boolean
            - side : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.extrude : Method
              
    """

    def __init__(self, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None, node_color=None):

        super().__init__('GeometryNodeExtrudeMesh', name='Extrude Mesh', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node FieldAtIndex for GeometryNodeFieldAtIndex

class FieldAtIndex(Node):

    """

    Node FieldAtIndex
    -----------------
        > Geometry node name: Field at Index<br>
          Blender type: Field at Index
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - index : Integer
                - value : data_type dependant
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
            - Input sockets  : ['value']
            - Output sockets : ['value']   
              
              
    

        Output sockets
        --------------
            - value : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.field_at_index : Method
            - Color.field_at_index : Method
            - Float.field_at_index : Method
            - Integer.field_at_index : Method
            - Vector.field_at_index : Method
              
    """

    def __init__(self, index=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeFieldAtIndex', name='Field at Index', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node FillCurve for GeometryNodeFillCurve

class FillCurve(Node):

    """

    Node FillCurve
    --------------
        > Geometry node name: Fill Curve<br>
          Blender type: Fill Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FillCurve(curve=None, mode='TRIANGLES', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
    

            Parameters
            ----------
                - mode : str (default = 'TRIANGLES') in ('TRIANGLES', 'NGONS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.fill : Method
              
    """

    def __init__(self, curve=None, mode='TRIANGLES', label=None, node_color=None):

        super().__init__('GeometryNodeFillCurve', name='Fill Curve', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node FilletCurve for GeometryNodeFilletCurve

class FilletCurve(Node):

    """

    Node FilletCurve
    ----------------
        > Geometry node name: Fillet Curve<br>
          Blender type: Fillet Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - count : Integer
                - radius : Float
                - limit_radius : Boolean
    

            Parameters
            ----------
                - mode : str (default = 'BEZIER') in ('BEZIER', 'POLY')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.fillet : Method
              
    """

    def __init__(self, curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None, node_color=None):

        super().__init__('GeometryNodeFilletCurve', name='Fillet Curve', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node FlipFaces for GeometryNodeFlipFaces

class FlipFaces(Node):

    """

    Node FlipFaces
    --------------
        > Geometry node name: Flip Faces<br>
          Blender type: Flip Faces
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FlipFaces(mesh=None, selection=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.flip_faces : Method
              
    """

    def __init__(self, mesh=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeFlipFaces', name='Flip Faces', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection

# ----------------------------------------------------------------------------------------------------
# Node GeometryToInstance for GeometryNodeGeometryToInstance

class GeometryToInstance(Node):

    """

    Node GeometryToInstance
    -----------------------
        > Geometry node name: Geometry to Instance<br>
          Blender type: Geometry to Instance
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.GeometryToInstance(*geometry, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : *Geometry
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - instances : Instances
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.to_instance : Method
              
    """

    def __init__(self, *geometry, label=None, node_color=None):

        super().__init__('GeometryNodeGeometryToInstance', name='Geometry to Instance', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        self.plug(0, *geometry)

# ----------------------------------------------------------------------------------------------------
# Node Group for GeometryNodeGroup

class Group(Node):

    """

    Node Group
    ----------
        > Geometry node name: Group<br>
          Blender type: Group
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Group(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeGroup', name='Group', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {}

# ----------------------------------------------------------------------------------------------------
# Node ImageTexture for GeometryNodeImageTexture

class ImageTexture(Node):

    """

    Node ImageTexture
    -----------------
        > Geometry node name: Image Texture<br>
          Blender type: Image Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - image : Image
                - vector : Vector
                - frame : Integer
    

            Parameters
            ----------
                - extension : str (default = 'REPEAT') in ('REPEAT', 'EXTEND', 'CLIP')
                - interpolation : str (default = 'Linear') in ('Linear', 'Closest', 'Cubic')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - alpha : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Image : Static method
              
    """

    def __init__(self, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None, node_color=None):

        super().__init__('GeometryNodeImageTexture', name='Image Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node CurveHandlePositions for GeometryNodeInputCurveHandlePositions

class CurveHandlePositions(Node):

    """

    Node CurveHandlePositions
    -------------------------
        > Geometry node name: Curve Handle Positions<br>
          Blender type: Curve Handle Positions
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveHandlePositions(relative=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - relative : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - left : Vector
            - right : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.handle_positions : Fields
              
    """

    def __init__(self, relative=None, label=None, node_color=None):

        super().__init__('GeometryNodeInputCurveHandlePositions', name='Curve Handle Positions', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'relative' : 0, }
        self.outsockets = {'left' : 0, 'right' : 1, }

        # Input sockets plugging

        if relative        is not None: self.relative        = relative

# ----------------------------------------------------------------------------------------------------
# Node CurveTilt for GeometryNodeInputCurveTilt

class CurveTilt(Node):

    """

    Node CurveTilt
    --------------
        > Geometry node name: Curve Tilt<br>
          Blender type: Curve Tilt
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveTilt(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - tilt : Float
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputCurveTilt', name='Curve Tilt', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'tilt' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node ID for GeometryNodeInputID

class ID(Node):

    """

    Node ID
    -------
        > Geometry node name: ID<br>
          Blender type: ID
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ID(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - ID : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputID', name='ID', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'ID' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Index for GeometryNodeInputIndex

class Index(Node):

    """

    Node Index
    ----------
        > Geometry node name: Index<br>
          Blender type: Index
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Index(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - index : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputIndex', name='Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'index' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Material for GeometryNodeInputMaterial

class Material(Node):

    """

    Node Material
    -------------
        > Geometry node name: Material<br>
          Blender type: Material
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Material(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - material : Material
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMaterial', name='Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'material' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node MaterialIndex for GeometryNodeInputMaterialIndex

class MaterialIndex(Node):

    """

    Node MaterialIndex
    ------------------
        > Geometry node name: Material Index<br>
          Blender type: Material Index
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MaterialIndex(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - material_index : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMaterialIndex', name='Material Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'material_index' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node EdgeAngle for GeometryNodeInputMeshEdgeAngle

class EdgeAngle(Node):

    """

    Node EdgeAngle
    --------------
        > Geometry node name: Edge Angle<br>
          Blender type: Edge Angle
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.EdgeAngle(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - unsigned_angle : Float
            - signed_angle : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - EdgeDomain.angle : Fields
            - EdgeDomain.unsigned_angle : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeAngle', name='Edge Angle', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'unsigned_angle' : 0, 'signed_angle' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node EdgeNeighbors for GeometryNodeInputMeshEdgeNeighbors

class EdgeNeighbors(Node):

    """

    Node EdgeNeighbors
    ------------------
        > Geometry node name: Edge Neighbors<br>
          Blender type: Edge Neighbors
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.EdgeNeighbors(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - face_count : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - EdgeDomain.neighbors_faces : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', name='Edge Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'face_count' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node EdgeVertices for GeometryNodeInputMeshEdgeVertices

class EdgeVertices(Node):

    """

    Node EdgeVertices
    -----------------
        > Geometry node name: Edge Vertices<br>
          Blender type: Edge Vertices
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.EdgeVertices(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vertex_index_1 : Integer
            - vertex_index_2 : Integer
            - position_1 : Vector
            - position_2 : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - EdgeDomain.vertices_index_1 : Fields
            - EdgeDomain.vertices_index_2 : Fields
            - EdgeDomain.vertices_position_1 : Fields
            - EdgeDomain.vertices_position_2 : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeVertices', name='Edge Vertices', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_index_1' : 0, 'vertex_index_2' : 1, 'position_1' : 2, 'position_2' : 3, }

# ----------------------------------------------------------------------------------------------------
# Node FaceArea for GeometryNodeInputMeshFaceArea

class FaceArea(Node):

    """

    Node FaceArea
    -------------
        > Geometry node name: Face Area<br>
          Blender type: Face Area
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FaceArea(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - area : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - FaceDomain.area : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceArea', name='Face Area', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'area' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node FaceIsPlanar for GeometryNodeInputMeshFaceIsPlanar

class FaceIsPlanar(Node):

    """

    Node FaceIsPlanar
    -----------------
        > Geometry node name: Face is Planar<br>
          Blender type: Face is Planar
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FaceIsPlanar(threshold=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - threshold : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - planar : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - FaceDomain.is_planar : Fields
              
    """

    def __init__(self, threshold=None, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceIsPlanar', name='Face is Planar', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'threshold' : 0, }
        self.outsockets = {'planar' : 0, }

        # Input sockets plugging

        if threshold       is not None: self.threshold       = threshold

# ----------------------------------------------------------------------------------------------------
# Node FaceNeighbors for GeometryNodeInputMeshFaceNeighbors

class FaceNeighbors(Node):

    """

    Node FaceNeighbors
    ------------------
        > Geometry node name: Face Neighbors<br>
          Blender type: Face Neighbors
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FaceNeighbors(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vertex_count : Integer
            - face_count : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceNeighbors', name='Face Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_count' : 0, 'face_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node MeshIsland for GeometryNodeInputMeshIsland

class MeshIsland(Node):

    """

    Node MeshIsland
    ---------------
        > Geometry node name: Mesh Island<br>
          Blender type: Mesh Island
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MeshIsland(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - island_index : Integer
            - island_count : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshIsland', name='Mesh Island', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'island_index' : 0, 'island_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node VertexNeighbors for GeometryNodeInputMeshVertexNeighbors

class VertexNeighbors(Node):

    """

    Node VertexNeighbors
    --------------------
        > Geometry node name: Vertex Neighbors<br>
          Blender type: Vertex Neighbors
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.VertexNeighbors(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vertex_count : Integer
            - face_count : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshVertexNeighbors', name='Vertex Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_count' : 0, 'face_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node NamedAttribute for GeometryNodeInputNamedAttribute

class NamedAttribute(Node):

    """

    Node NamedAttribute
    -------------------
        > Geometry node name: Named Attribute<br>
          Blender type: Named Attribute
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.NamedAttribute(name=None, data_type='FLOAT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - name : String
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
            - Input sockets  : []
            - Output sockets : ['attribute']   
              
              
    

        Output sockets
        --------------
            - attribute : data_type dependant
    """

    def __init__(self, name=None, data_type='FLOAT', label=None, node_color=None):

        super().__init__('GeometryNodeInputNamedAttribute', name='Named Attribute', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Normal for GeometryNodeInputNormal

class Normal(Node):

    """

    Node Normal
    -----------
        > Geometry node name: Normal<br>
          Blender type: Normal
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Normal(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - normal : Vector
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputNormal', name='Normal', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'normal' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Position for GeometryNodeInputPosition

class Position(Node):

    """

    Node Position
    -------------
        > Geometry node name: Position<br>
          Blender type: Position
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Position(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - position : Vector
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputPosition', name='Position', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'position' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Radius for GeometryNodeInputRadius

class Radius(Node):

    """

    Node Radius
    -----------
        > Geometry node name: Radius<br>
          Blender type: Radius
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Radius(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - radius : Float
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputRadius', name='Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'radius' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node SceneTime for GeometryNodeInputSceneTime

class SceneTime(Node):

    """

    Node SceneTime
    --------------
        > Geometry node name: Scene Time<br>
          Blender type: Scene Time
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SceneTime(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - seconds : Float
            - frame : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - functions.scene : Function
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'seconds' : 0, 'frame' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node IsShadeSmooth for GeometryNodeInputShadeSmooth

class IsShadeSmooth(Node):

    """

    Node IsShadeSmooth
    ------------------
        > Geometry node name: Is Shade Smooth<br>
          Blender type: Is Shade Smooth
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.IsShadeSmooth(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - smooth : Boolean
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputShadeSmooth', name='Is Shade Smooth', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'smooth' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node IsSplineCyclic for GeometryNodeInputSplineCyclic

class IsSplineCyclic(Node):

    """

    Node IsSplineCyclic
    -------------------
        > Geometry node name: Is Spline Cyclic<br>
          Blender type: Is Spline Cyclic
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.IsSplineCyclic(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - cyclic : Boolean
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSplineCyclic', name='Is Spline Cyclic', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'cyclic' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node SplineResolution for GeometryNodeInputSplineResolution

class SplineResolution(Node):

    """

    Node SplineResolution
    ---------------------
        > Geometry node name: Spline Resolution<br>
          Blender type: Spline Resolution
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SplineResolution(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - resolution : Integer
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSplineResolution', name='Spline Resolution', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'resolution' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node CurveTangent for GeometryNodeInputTangent

class CurveTangent(Node):

    """

    Node CurveTangent
    -----------------
        > Geometry node name: Curve Tangent<br>
          Blender type: Curve Tangent
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CurveTangent(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - tangent : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.tangent : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputTangent', name='Curve Tangent', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'tangent' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node InstanceOnPoints for GeometryNodeInstanceOnPoints

class InstanceOnPoints(Node):

    """

    Node InstanceOnPoints
    ---------------------
        > Geometry node name: Instance on Points<br>
          Blender type: Instance on Points
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - points : Points
                - selection : Boolean
                - instance : Geometry
                - pick_instance : Boolean
                - instance_index : Integer
                - rotation : Vector
                - scale : Vector
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - instances : Instances
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Points.instance_on_points : Method
              
    """

    def __init__(self, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None, node_color=None):

        super().__init__('GeometryNodeInstanceOnPoints', name='Instance on Points', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node InstancesToPoints for GeometryNodeInstancesToPoints

class InstancesToPoints(Node):

    """

    Node InstancesToPoints
    ----------------------
        > Geometry node name: Instances to Points<br>
          Blender type: Instances to Points
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.InstancesToPoints(instances=None, selection=None, position=None, radius=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - instances : Instances
                - selection : Boolean
                - position : Vector
                - radius : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - points : Points
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Instances.to_points : Method
              
    """

    def __init__(self, instances=None, selection=None, position=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeInstancesToPoints', name='Instances to Points', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'position' : 2, 'radius' : 3, }
        self.outsockets = {'points' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if position        is not None: self.position        = position
        if radius          is not None: self.radius          = radius

# ----------------------------------------------------------------------------------------------------
# Node IsViewport for GeometryNodeIsViewport

class IsViewport(Node):

    """

    Node IsViewport
    ---------------
        > Geometry node name: Is Viewport<br>
          Blender type: Is Viewport
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.IsViewport(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - is_viewport : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.is_viewport : Static method
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeIsViewport', name='Is Viewport', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'is_viewport' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node JoinGeometry for GeometryNodeJoinGeometry

class JoinGeometry(Node):

    """

    Node JoinGeometry
    -----------------
        > Geometry node name: Join Geometry<br>
          Blender type: Join Geometry
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.JoinGeometry(*geometry, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : *Geometry
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.join : Method
              
    """

    def __init__(self, *geometry, label=None, node_color=None):

        super().__init__('GeometryNodeJoinGeometry', name='Join Geometry', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        self.plug(0, *geometry)

# ----------------------------------------------------------------------------------------------------
# Node MaterialSelection for GeometryNodeMaterialSelection

class MaterialSelection(Node):

    """

    Node MaterialSelection
    ----------------------
        > Geometry node name: Material Selection<br>
          Blender type: Material Selection
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MaterialSelection(material=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - material : Material
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - selection : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - FaceDomain.material_selection : Fields
            - Material.selection : Method
              
    """

    def __init__(self, material=None, label=None, node_color=None):

        super().__init__('GeometryNodeMaterialSelection', name='Material Selection', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'material' : 0, }
        self.outsockets = {'selection' : 0, }

        # Input sockets plugging

        if material        is not None: self.material        = material

# ----------------------------------------------------------------------------------------------------
# Node MergeByDistance for GeometryNodeMergeByDistance

class MergeByDistance(Node):

    """

    Node MergeByDistance
    --------------------
        > Geometry node name: Merge by Distance<br>
          Blender type: Merge by Distance
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, mode='ALL', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - distance : Float
    

            Parameters
            ----------
                - mode : str (default = 'ALL') in ('ALL', 'CONNECTED')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.merge_by_distance : Method
              
    """

    def __init__(self, geometry=None, selection=None, distance=None, mode='ALL', label=None, node_color=None):

        super().__init__('GeometryNodeMergeByDistance', name='Merge by Distance', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node MeshBoolean for GeometryNodeMeshBoolean

class MeshBoolean(Node):

    """

    Node MeshBoolean
    ----------------
        > Geometry node name: Mesh Boolean<br>
          Blender type: Mesh Boolean
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh_1 : Geometry
                - mesh_2 : *Geometry
                - self_intersection : Boolean
                - hole_tolerant : Boolean
    

            Parameters
            ----------
                - operation : str (default = 'DIFFERENCE') in ('INTERSECT', 'UNION', 'DIFFERENCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.difference : Method
            - Mesh.intersect : Method
            - Mesh.union : Method
              
    """

    def __init__(self, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None, node_color=None):

        super().__init__('GeometryNodeMeshBoolean', name='Mesh Boolean', label=label, node_color=node_color)

        # Node parameters

        self.bnode.operation       = operation

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh_1' : 0, 'mesh_2' : 1, 'self_intersection' : 2, 'hole_tolerant' : 3, }
        self.outsockets = {'mesh' : 0, }

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

# ----------------------------------------------------------------------------------------------------
# Node MeshCircle for GeometryNodeMeshCircle

class MeshCircle(Node):

    """

    Node MeshCircle
    ---------------
        > Geometry node name: Mesh Circle<br>
          Blender type: Mesh Circle
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vertices : Integer
                - radius : Float
    

            Parameters
            ----------
                - fill_type : str (default = 'NONE') in ('NONE', 'NGON', 'TRIANGLE_FAN')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.Circle : Constructor
              
    """

    def __init__(self, vertices=None, radius=None, fill_type='NONE', label=None, node_color=None):

        super().__init__('GeometryNodeMeshCircle', name='Mesh Circle', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Cone for GeometryNodeMeshCone

class Cone(Node):

    """

    Node Cone
    ---------
        > Geometry node name: Cone<br>
          Blender type: Cone
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vertices : Integer
                - side_segments : Integer
                - fill_segments : Integer
                - radius_top : Float
                - radius_bottom : Float
                - depth : Float
    

            Parameters
            ----------
                - fill_type : str (default = 'NGON') in ('NONE', 'NGON', 'TRIANGLE_FAN')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
            - top : Boolean
            - bottom : Boolean
            - side : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.Cone : Constructor
              
    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None, node_color=None):

        super().__init__('GeometryNodeMeshCone', name='Cone', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Cube for GeometryNodeMeshCube

class Cube(Node):

    """

    Node Cube
    ---------
        > Geometry node name: Cube<br>
          Blender type: Cube
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - size : Vector
                - vertices_x : Integer
                - vertices_y : Integer
                - vertices_z : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.Cube : Constructor
              
    """

    def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshCube', name='Cube', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'size' : 0, 'vertices_x' : 1, 'vertices_y' : 2, 'vertices_z' : 3, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if size            is not None: self.size            = size
        if vertices_x      is not None: self.vertices_x      = vertices_x
        if vertices_y      is not None: self.vertices_y      = vertices_y
        if vertices_z      is not None: self.vertices_z      = vertices_z

# ----------------------------------------------------------------------------------------------------
# Node Cylinder for GeometryNodeMeshCylinder

class Cylinder(Node):

    """

    Node Cylinder
    -------------
        > Geometry node name: Cylinder<br>
          Blender type: Cylinder
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vertices : Integer
                - side_segments : Integer
                - fill_segments : Integer
                - radius : Float
                - depth : Float
    

            Parameters
            ----------
                - fill_type : str (default = 'NGON') in ('NONE', 'NGON', 'TRIANGLE_FAN')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
            - top : Boolean
            - side : Boolean
            - bottom : Boolean
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.Cylinder : Constructor
              
    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None, node_color=None):

        super().__init__('GeometryNodeMeshCylinder', name='Cylinder', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Grid for GeometryNodeMeshGrid

class Grid(Node):

    """

    Node Grid
    ---------
        > Geometry node name: Grid<br>
          Blender type: Grid
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - size_x : Float
                - size_y : Float
                - vertices_x : Integer
                - vertices_y : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.Grid : Constructor
              
    """

    def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshGrid', name='Grid', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'size_x' : 0, 'size_y' : 1, 'vertices_x' : 2, 'vertices_y' : 3, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if size_x          is not None: self.size_x          = size_x
        if size_y          is not None: self.size_y          = size_y
        if vertices_x      is not None: self.vertices_x      = vertices_x
        if vertices_y      is not None: self.vertices_y      = vertices_y

# ----------------------------------------------------------------------------------------------------
# Node IcoSphere for GeometryNodeMeshIcoSphere

class IcoSphere(Node):

    """

    Node IcoSphere
    --------------
        > Geometry node name: Ico Sphere<br>
          Blender type: Ico Sphere
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.IcoSphere(radius=None, subdivisions=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - radius : Float
                - subdivisions : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.IcoSphere : Constructor
              
    """

    def __init__(self, radius=None, subdivisions=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshIcoSphere', name='Ico Sphere', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'radius' : 0, 'subdivisions' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if radius          is not None: self.radius          = radius
        if subdivisions    is not None: self.subdivisions    = subdivisions

# ----------------------------------------------------------------------------------------------------
# Node MeshLine for GeometryNodeMeshLine

class MeshLine(Node):

    """

    Node MeshLine
    -------------
        > Geometry node name: Mesh Line<br>
          Blender type: Mesh Line
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - count : Integer
                - resolution : Float
                - start_location : Vector
                - offset : Vector
    

            Parameters
            ----------
                - count_mode : str (default = 'TOTAL') in ('TOTAL', 'RESOLUTION')
                - mode : str (default = 'OFFSET') in ('OFFSET', 'END_POINTS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.Line : Constructor
              
    """

    def __init__(self, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None, node_color=None):

        super().__init__('GeometryNodeMeshLine', name='Mesh Line', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node MeshToCurve for GeometryNodeMeshToCurve

class MeshToCurve(Node):

    """

    Node MeshToCurve
    ----------------
        > Geometry node name: Mesh to Curve<br>
          Blender type: Mesh to Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MeshToCurve(mesh=None, selection=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.to_curve : Method
              
    """

    def __init__(self, mesh=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshToCurve', name='Mesh to Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection

# ----------------------------------------------------------------------------------------------------
# Node MeshToPoints for GeometryNodeMeshToPoints

class MeshToPoints(Node):

    """

    Node MeshToPoints
    -----------------
        > Geometry node name: Mesh to Points<br>
          Blender type: Mesh to Points
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
                - position : Vector
                - radius : Float
    

            Parameters
            ----------
                - mode : str (default = 'VERTICES') in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - points : Points
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.to_points : Method
              
    """

    def __init__(self, mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None, node_color=None):

        super().__init__('GeometryNodeMeshToPoints', name='Mesh to Points', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node UvSphere for GeometryNodeMeshUVSphere

class UvSphere(Node):

    """

    Node UvSphere
    -------------
        > Geometry node name: UV Sphere<br>
          Blender type: UV Sphere
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.UvSphere(segments=None, rings=None, radius=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - segments : Integer
                - rings : Integer
                - radius : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.UVSphere : Constructor
              
    """

    def __init__(self, segments=None, rings=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeMeshUVSphere', name='UV Sphere', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'segments' : 0, 'rings' : 1, 'radius' : 2, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if segments        is not None: self.segments        = segments
        if rings           is not None: self.rings           = rings
        if radius          is not None: self.radius          = radius

# ----------------------------------------------------------------------------------------------------
# Node ObjectInfo for GeometryNodeObjectInfo

class ObjectInfo(Node):

    """

    Node ObjectInfo
    ---------------
        > Geometry node name: Object Info<br>
          Blender type: Object Info
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - object : Object
                - as_instance : Boolean
    

            Parameters
            ----------
                - transform_space : str (default = 'ORIGINAL') in ('ORIGINAL', 'RELATIVE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - location : Vector
            - rotation : Vector
            - scale : Vector
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Object.geometry : Property
            - Object.info : Property
            - Object.location : Property
            - Object.rotation : Property
            - Object.scale : Property
              
    """

    def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL', label=None, node_color=None):

        super().__init__('GeometryNodeObjectInfo', name='Object Info', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node PointsToVertices for GeometryNodePointsToVertices

class PointsToVertices(Node):

    """

    Node PointsToVertices
    ---------------------
        > Geometry node name: Points to Vertices<br>
          Blender type: Points to Vertices
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.PointsToVertices(points=None, selection=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - points : Points
                - selection : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Points.to_vertices : Method
              
    """

    def __init__(self, points=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodePointsToVertices', name='Points to Vertices', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'selection' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if selection       is not None: self.selection       = selection

# ----------------------------------------------------------------------------------------------------
# Node PointsToVolume for GeometryNodePointsToVolume

class PointsToVolume(Node):

    """

    Node PointsToVolume
    -------------------
        > Geometry node name: Points to Volume<br>
          Blender type: Points to Volume
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.PointsToVolume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - points : Points
                - density : Float
                - voxel_size : Float
                - voxel_amount : Float
                - radius : Float
    

            Parameters
            ----------
                - resolution_mode : str (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - volume : Volume
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Points.to_volume : Method
              
    """

    def __init__(self, points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None, node_color=None):

        super().__init__('GeometryNodePointsToVolume', name='Points to Volume', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node GeometryProximity for GeometryNodeProximity

class GeometryProximity(Node):

    """

    Node GeometryProximity
    ----------------------
        > Geometry node name: Geometry Proximity<br>
          Blender type: Geometry Proximity
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - target : Geometry
                - source_position : Vector
    

            Parameters
            ----------
                - target_element : str (default = 'FACES') in ('POINTS', 'EDGES', 'FACES')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - position : Vector
            - distance : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.proximity : Method
              
    """

    def __init__(self, target=None, source_position=None, target_element='FACES', label=None, node_color=None):

        super().__init__('GeometryNodeProximity', name='Geometry Proximity', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Raycast for GeometryNodeRaycast

class Raycast(Node):

    """

    Node Raycast
    ------------
        > Geometry node name: Raycast<br>
          Blender type: Raycast
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - target_geometry : Geometry
                - attribute : data_type dependant
                - source_position : Vector
                - ray_direction : Vector
                - ray_length : Float
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
                - mapping : str (default = 'INTERPOLATED') in ('INTERPOLATED', 'NEAREST')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
            - Input sockets  : ['attribute']
            - Output sockets : ['attribute']   
              
              
    

        Output sockets
        --------------
            - is_hit : Boolean
            - hit_position : Vector
            - hit_normal : Vector
            - hit_distance : Float
            - attribute : data_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.raycast : Method
            - Color.raycast : Method
            - Float.raycast : Method
            - Integer.raycast : Method
            - Vector.raycast : Method
              
    """

    def __init__(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None, node_color=None):

        super().__init__('GeometryNodeRaycast', name='Raycast', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node RealizeInstances for GeometryNodeRealizeInstances

class RealizeInstances(Node):

    """

    Node RealizeInstances
    ---------------------
        > Geometry node name: Realize Instances<br>
          Blender type: Realize Instances
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.RealizeInstances(geometry=None, legacy_behavior=False, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
    

            Parameters
            ----------
                - legacy_behavior : bool (default = False)
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Instances.realize : Method
              
    """

    def __init__(self, geometry=None, legacy_behavior=False, label=None, node_color=None):

        super().__init__('GeometryNodeRealizeInstances', name='Realize Instances', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node RemoveNamedAttribute for GeometryNodeRemoveAttribute

class RemoveNamedAttribute(Node):

    """

    Node RemoveNamedAttribute
    -------------------------
        > Geometry node name: Remove Named Attribute<br>
          Blender type: Remove Named Attribute
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.RemoveNamedAttribute(geometry=None, name=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - name : String
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.remove_named_attribute : Method
              
    """

    def __init__(self, geometry=None, name=None, label=None, node_color=None):

        super().__init__('GeometryNodeRemoveAttribute', name='Remove Named Attribute', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'name' : 1, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if name            is not None: self.name            = name

# ----------------------------------------------------------------------------------------------------
# Node ReplaceMaterial for GeometryNodeReplaceMaterial

class ReplaceMaterial(Node):

    """

    Node ReplaceMaterial
    --------------------
        > Geometry node name: Replace Material<br>
          Blender type: Replace Material
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ReplaceMaterial(geometry=None, old=None, new=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - old : Material
                - new : Material
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.replace_material : Method
              
    """

    def __init__(self, geometry=None, old=None, new=None, label=None, node_color=None):

        super().__init__('GeometryNodeReplaceMaterial', name='Replace Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'old' : 1, 'new' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if old             is not None: self.old             = old
        if new             is not None: self.new             = new

# ----------------------------------------------------------------------------------------------------
# Node ResampleCurve for GeometryNodeResampleCurve

class ResampleCurve(Node):

    """

    Node ResampleCurve
    ------------------
        > Geometry node name: Resample Curve<br>
          Blender type: Resample Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
                - count : Integer
                - length : Float
    

            Parameters
            ----------
                - mode : str (default = 'COUNT') in ('EVALUATED', 'COUNT', 'LENGTH')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.resample : Method
              
    """

    def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT', label=None, node_color=None):

        super().__init__('GeometryNodeResampleCurve', name='Resample Curve', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node ReverseCurve for GeometryNodeReverseCurve

class ReverseCurve(Node):

    """

    Node ReverseCurve
    -----------------
        > Geometry node name: Reverse Curve<br>
          Blender type: Reverse Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ReverseCurve(curve=None, selection=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.reverse : Method
              
    """

    def __init__(self, curve=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeReverseCurve', name='Reverse Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection

# ----------------------------------------------------------------------------------------------------
# Node RotateInstances for GeometryNodeRotateInstances

class RotateInstances(Node):

    """

    Node RotateInstances
    --------------------
        > Geometry node name: Rotate Instances<br>
          Blender type: Rotate Instances
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.RotateInstances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - instances : Instances
                - selection : Boolean
                - rotation : Vector
                - pivot_point : Vector
                - local_space : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - instances : Instances
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Instances.rotate : Method
              
    """

    def __init__(self, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, label=None, node_color=None):

        super().__init__('GeometryNodeRotateInstances', name='Rotate Instances', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'rotation' : 2, 'pivot_point' : 3, 'local_space' : 4, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if rotation        is not None: self.rotation        = rotation
        if pivot_point     is not None: self.pivot_point     = pivot_point
        if local_space     is not None: self.local_space     = local_space

# ----------------------------------------------------------------------------------------------------
# Node SampleCurve for GeometryNodeSampleCurve

class SampleCurve(Node):

    """

    Node SampleCurve
    ----------------
        > Geometry node name: Sample Curve<br>
          Blender type: Sample Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SampleCurve(curve=None, factor=None, length=None, mode='LENGTH', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - factor : Float
                - length : Float
    

            Parameters
            ----------
                - mode : str (default = 'LENGTH') in ('FACTOR', 'LENGTH')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - position : Vector
            - tangent : Vector
            - normal : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.sample : Method
              
    """

    def __init__(self, curve=None, factor=None, length=None, mode='LENGTH', label=None, node_color=None):

        super().__init__('GeometryNodeSampleCurve', name='Sample Curve', label=label, node_color=node_color)

        # Node parameters

        self.bnode.mode            = mode

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'factor' : 1, 'length' : 2, }
        self.outsockets = {'position' : 0, 'tangent' : 1, 'normal' : 2, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if factor          is not None: self.factor          = factor
        if length          is not None: self.length          = length

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node ScaleElements for GeometryNodeScaleElements

class ScaleElements(Node):

    """

    Node ScaleElements
    ------------------
        > Geometry node name: Scale Elements<br>
          Blender type: Scale Elements
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - scale : Float
                - center : Vector
                - axis : Vector
    

            Parameters
            ----------
                - domain : str (default = 'FACE') in ('FACE', 'EDGE')
                - scale_mode : str (default = 'UNIFORM') in ('UNIFORM', 'SINGLE_AXIS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.scale_elements : Method
              
    """

    def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None, node_color=None):

        super().__init__('GeometryNodeScaleElements', name='Scale Elements', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node ScaleInstances for GeometryNodeScaleInstances

class ScaleInstances(Node):

    """

    Node ScaleInstances
    -------------------
        > Geometry node name: Scale Instances<br>
          Blender type: Scale Instances
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ScaleInstances(instances=None, selection=None, scale=None, center=None, local_space=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - instances : Instances
                - selection : Boolean
                - scale : Vector
                - center : Vector
                - local_space : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - instances : Instances
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Instances.scale : Method
              
    """

    def __init__(self, instances=None, selection=None, scale=None, center=None, local_space=None, label=None, node_color=None):

        super().__init__('GeometryNodeScaleInstances', name='Scale Instances', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'scale' : 2, 'center' : 3, 'local_space' : 4, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if scale           is not None: self.scale           = scale
        if center          is not None: self.center          = center
        if local_space     is not None: self.local_space     = local_space

# ----------------------------------------------------------------------------------------------------
# Node SeparateComponents for GeometryNodeSeparateComponents

class SeparateComponents(Node):

    """

    Node SeparateComponents
    -----------------------
        > Geometry node name: Separate Components<br>
          Blender type: Separate Components
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SeparateComponents(geometry=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
            - point_cloud : Geometry
            - curve : Curve
            - volume : Volume
            - instances : Instances
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.components : Property
            - Geometry.curve_component : Property
            - Geometry.instances_component : Property
            - Geometry.mesh_component : Property
            - Geometry.points_component : Property
            - Geometry.volume_component : Property
              
    """

    def __init__(self, geometry=None, label=None, node_color=None):

        super().__init__('GeometryNodeSeparateComponents', name='Separate Components', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, }
        self.outsockets = {'mesh' : 0, 'point_cloud' : 1, 'curve' : 2, 'volume' : 3, 'instances' : 4, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry

# ----------------------------------------------------------------------------------------------------
# Node SeparateGeometry for GeometryNodeSeparateGeometry

class SeparateGeometry(Node):

    """

    Node SeparateGeometry
    ---------------------
        > Geometry node name: Separate Geometry<br>
          Blender type: Separate Geometry
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
    

            Parameters
            ----------
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - selection : Geometry
            - inverted : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.components : Method
              
    """

    def __init__(self, geometry=None, selection=None, domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeSeparateGeometry', name='Separate Geometry', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node SetHandlePositions for GeometryNodeSetCurveHandlePositions

class SetHandlePositions(Node):

    """

    Node SetHandlePositions
    -----------------------
        > Geometry node name: Set Handle Positions<br>
          Blender type: Set Handle Positions
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
                - position : Vector
                - offset : Vector
    

            Parameters
            ----------
                - mode : str (default = 'LEFT') in ('LEFT', 'RIGHT')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.set_handle_positions : Method
            - CurveDomain.set_handle_positions : Fields
            - CurveDomain.set_left_handle_positions : Fields
            - CurveDomain.set_right_handle_positions : Fields
              
    """

    def __init__(self, curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveHandlePositions', name='Set Handle Positions', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node SetCurveRadius for GeometryNodeSetCurveRadius

class SetCurveRadius(Node):

    """

    Node SetCurveRadius
    -------------------
        > Geometry node name: Set Curve Radius<br>
          Blender type: Set Curve Radius
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetCurveRadius(curve=None, selection=None, radius=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
                - radius : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.set_radius : Method
              
    """

    def __init__(self, curve=None, selection=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveRadius', name='Set Curve Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, 'radius' : 2, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection
        if radius          is not None: self.radius          = radius

# ----------------------------------------------------------------------------------------------------
# Node SetCurveTilt for GeometryNodeSetCurveTilt

class SetCurveTilt(Node):

    """

    Node SetCurveTilt
    -----------------
        > Geometry node name: Set Curve Tilt<br>
          Blender type: Set Curve Tilt
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - selection : Boolean
                - tilt : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.set_tilt : Method
            - CurveDomain.tilt : Fields
              
    """

    def __init__(self, curve=None, selection=None, tilt=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetCurveTilt', name='Set Curve Tilt', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'selection' : 1, 'tilt' : 2, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if selection       is not None: self.selection       = selection
        if tilt            is not None: self.tilt            = tilt

# ----------------------------------------------------------------------------------------------------
# Node SetID for GeometryNodeSetID

class SetID(Node):

    """

    Node SetID
    ----------
        > Geometry node name: Set ID<br>
          Blender type: Set ID
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetID(geometry=None, selection=None, ID=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - ID : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.set_ID : Method
              
    """

    def __init__(self, geometry=None, selection=None, ID=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetID', name='Set ID', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'ID' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if ID              is not None: self.ID              = ID

# ----------------------------------------------------------------------------------------------------
# Node SetMaterial for GeometryNodeSetMaterial

class SetMaterial(Node):

    """

    Node SetMaterial
    ----------------
        > Geometry node name: Set Material<br>
          Blender type: Set Material
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetMaterial(geometry=None, selection=None, material=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - material : Material
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.set_material : Method
              
    """

    def __init__(self, geometry=None, selection=None, material=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetMaterial', name='Set Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'material' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if material        is not None: self.material        = material

# ----------------------------------------------------------------------------------------------------
# Node SetMaterialIndex for GeometryNodeSetMaterialIndex

class SetMaterialIndex(Node):

    """

    Node SetMaterialIndex
    ---------------------
        > Geometry node name: Set Material Index<br>
          Blender type: Set Material Index
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetMaterialIndex(geometry=None, selection=None, material_index=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - material_index : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - FaceDomain.material_index : Fields
            - Geometry.set_material_index : Method
              
    """

    def __init__(self, geometry=None, selection=None, material_index=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetMaterialIndex', name='Set Material Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'material_index' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if material_index  is not None: self.material_index  = material_index

# ----------------------------------------------------------------------------------------------------
# Node SetPointRadius for GeometryNodeSetPointRadius

class SetPointRadius(Node):

    """

    Node SetPointRadius
    -------------------
        > Geometry node name: Set Point Radius<br>
          Blender type: Set Point Radius
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetPointRadius(points=None, selection=None, radius=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - points : Points
                - selection : Boolean
                - radius : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - points : Points
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Points.set_radius : Method
              
    """

    def __init__(self, points=None, selection=None, radius=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetPointRadius', name='Set Point Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'points' : 0, 'selection' : 1, 'radius' : 2, }
        self.outsockets = {'points' : 0, }

        # Input sockets plugging

        if points          is not None: self.points          = points
        if selection       is not None: self.selection       = selection
        if radius          is not None: self.radius          = radius

# ----------------------------------------------------------------------------------------------------
# Node SetPosition for GeometryNodeSetPosition

class SetPosition(Node):

    """

    Node SetPosition
    ----------------
        > Geometry node name: Set Position<br>
          Blender type: Set Position
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetPosition(geometry=None, selection=None, position=None, offset=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - position : Vector
                - offset : Vector
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.set_position : Method
              
    """

    def __init__(self, geometry=None, selection=None, position=None, offset=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetPosition', name='Set Position', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'position' : 2, 'offset' : 3, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if position        is not None: self.position        = position
        if offset          is not None: self.offset          = offset

# ----------------------------------------------------------------------------------------------------
# Node SetShadeSmooth for GeometryNodeSetShadeSmooth

class SetShadeSmooth(Node):

    """

    Node SetShadeSmooth
    -------------------
        > Geometry node name: Set Shade Smooth<br>
          Blender type: Set Shade Smooth
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetShadeSmooth(geometry=None, selection=None, shade_smooth=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - shade_smooth : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.set_shade_smooth : Method
              
    """

    def __init__(self, geometry=None, selection=None, shade_smooth=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetShadeSmooth', name='Set Shade Smooth', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'shade_smooth' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if shade_smooth    is not None: self.shade_smooth    = shade_smooth

# ----------------------------------------------------------------------------------------------------
# Node SetSplineCyclic for GeometryNodeSetSplineCyclic

class SetSplineCyclic(Node):

    """

    Node SetSplineCyclic
    --------------------
        > Geometry node name: Set Spline Cyclic<br>
          Blender type: Set Spline Cyclic
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - cyclic : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.cyclic : Fields
            - Spline.set_cyclic : Method
              
    """

    def __init__(self, geometry=None, selection=None, cyclic=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetSplineCyclic', name='Set Spline Cyclic', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'cyclic' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if cyclic          is not None: self.cyclic          = cyclic

# ----------------------------------------------------------------------------------------------------
# Node SetSplineResolution for GeometryNodeSetSplineResolution

class SetSplineResolution(Node):

    """

    Node SetSplineResolution
    ------------------------
        > Geometry node name: Set Spline Resolution<br>
          Blender type: Set Spline Resolution
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SetSplineResolution(geometry=None, selection=None, resolution=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - selection : Boolean
                - resolution : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.resolution : Fields
            - Spline.set_resolution : Method
              
    """

    def __init__(self, geometry=None, selection=None, resolution=None, label=None, node_color=None):

        super().__init__('GeometryNodeSetSplineResolution', name='Set Spline Resolution', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'selection' : 1, 'resolution' : 2, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if selection       is not None: self.selection       = selection
        if resolution      is not None: self.resolution      = resolution

# ----------------------------------------------------------------------------------------------------
# Node SplineLength for GeometryNodeSplineLength

class SplineLength(Node):

    """

    Node SplineLength
    -----------------
        > Geometry node name: Spline Length<br>
          Blender type: Spline Length
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SplineLength(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - length : Float
            - point_count : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.length : Fields
            - CurveDomain.point_count : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSplineLength', name='Spline Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'length' : 0, 'point_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node SplineParameter for GeometryNodeSplineParameter

class SplineParameter(Node):

    """

    Node SplineParameter
    --------------------
        > Geometry node name: Spline Parameter<br>
          Blender type: Spline Parameter
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SplineParameter(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - factor : Float
            - length : Float
            - index : Integer
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - CurveDomain.parameter_factor : Fields
            - CurveDomain.parameter_index : Fields
            - CurveDomain.parameter_length : Fields
              
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSplineParameter', name='Spline Parameter', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'factor' : 0, 'length' : 1, 'index' : 2, }

# ----------------------------------------------------------------------------------------------------
# Node SplitEdges for GeometryNodeSplitEdges

class SplitEdges(Node):

    """

    Node SplitEdges
    ---------------
        > Geometry node name: Split Edges<br>
          Blender type: Split Edges
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SplitEdges(mesh=None, selection=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.split_edges : Method
              
    """

    def __init__(self, mesh=None, selection=None, label=None, node_color=None):

        super().__init__('GeometryNodeSplitEdges', name='Split Edges', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'selection' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if selection       is not None: self.selection       = selection

# ----------------------------------------------------------------------------------------------------
# Node StoreNamedAttribute for GeometryNodeStoreNamedAttribute

class StoreNamedAttribute(Node):

    """

    Node StoreNamedAttribute
    ------------------------
        > Geometry node name: Store Named Attribute<br>
          Blender type: Store Named Attribute
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.StoreNamedAttribute(geometry=None, name=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - name : String
                - value : data_type dependant
    

            Parameters
            ----------
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
                - domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
            - Input sockets  : ['value']
            - Output sockets : []   
              
              
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.store_named_attribute : Method
            - Geometry.store_named_boolean : Method
            - Geometry.store_named_byte_color : Method
            - Geometry.store_named_color : Method
            - Geometry.store_named_float : Method
            - Geometry.store_named_integer : Method
            - Geometry.store_named_vector : Method
              
    """

    def __init__(self, geometry=None, name=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None):

        super().__init__('GeometryNodeStoreNamedAttribute', name='Store Named Attribute', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node JoinStrings for GeometryNodeStringJoin

class JoinStrings(Node):

    """

    Node JoinStrings
    ----------------
        > Geometry node name: Join Strings<br>
          Blender type: Join Strings
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.JoinStrings(*strings, delimiter=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - delimiter : String
                - strings : *String
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - string : String
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - String.join : Method
            - functions.join_strings : Function
              
    """

    def __init__(self, *strings, delimiter=None, label=None, node_color=None):

        super().__init__('GeometryNodeStringJoin', name='Join Strings', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'delimiter' : 0, 'strings' : 1, }
        self.outsockets = {'string' : 0, }

        # Input sockets plugging

        if delimiter       is not None: self.delimiter       = delimiter
        self.plug(1, *strings)

# ----------------------------------------------------------------------------------------------------
# Node StringToCurves for GeometryNodeStringToCurves

class StringToCurves(Node):

    """

    Node StringToCurves
    -------------------
        > Geometry node name: String to Curves<br>
          Blender type: String to Curves
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.StringToCurves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - string : String
                - size : Float
                - character_spacing : Float
                - word_spacing : Float
                - line_spacing : Float
                - text_box_width : Float
                - text_box_height : Float
    

            Parameters
            ----------
                - align_x : str (default = 'LEFT') in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
                - align_y : str (default = 'TOP_BASELINE') in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
                - overflow : str (default = 'OVERFLOW') in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
                - pivot_mode : str (default = 'BOTTOM_LEFT') in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve_instances : Geometry
            - remainder : String
            - line : Integer
            - pivot_point : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - String.to_curves : Method
              
    """

    def __init__(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None, node_color=None):

        super().__init__('GeometryNodeStringToCurves', name='String to Curves', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node SubdivideCurve for GeometryNodeSubdivideCurve

class SubdivideCurve(Node):

    """

    Node SubdivideCurve
    -------------------
        > Geometry node name: Subdivide Curve<br>
          Blender type: Subdivide Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SubdivideCurve(curve=None, cuts=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - cuts : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.subdivide : Method
              
    """

    def __init__(self, curve=None, cuts=None, label=None, node_color=None):

        super().__init__('GeometryNodeSubdivideCurve', name='Subdivide Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'curve' : 0, 'cuts' : 1, }
        self.outsockets = {'curve' : 0, }

        # Input sockets plugging

        if curve           is not None: self.curve           = curve
        if cuts            is not None: self.cuts            = cuts

# ----------------------------------------------------------------------------------------------------
# Node SubdivideMesh for GeometryNodeSubdivideMesh

class SubdivideMesh(Node):

    """

    Node SubdivideMesh
    ------------------
        > Geometry node name: Subdivide Mesh<br>
          Blender type: Subdivide Mesh
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SubdivideMesh(mesh=None, level=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - level : Integer
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.subdivide : Method
              
    """

    def __init__(self, mesh=None, level=None, label=None, node_color=None):

        super().__init__('GeometryNodeSubdivideMesh', name='Subdivide Mesh', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'level' : 1, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if level           is not None: self.level           = level

# ----------------------------------------------------------------------------------------------------
# Node SubdivisionSurface for GeometryNodeSubdivisionSurface

class SubdivisionSurface(Node):

    """

    Node SubdivisionSurface
    -----------------------
        > Geometry node name: Subdivision Surface<br>
          Blender type: Subdivision Surface
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SubdivisionSurface(mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - level : Integer
                - crease : Float
    

            Parameters
            ----------
                - boundary_smooth : str (default = 'ALL') in ('PRESERVE_CORNERS', 'ALL')
                - uv_smooth : str (default = 'PRESERVE_BOUNDARIES') in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.subdivision_surface : Method
              
    """

    def __init__(self, mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None, node_color=None):

        super().__init__('GeometryNodeSubdivisionSurface', name='Subdivision Surface', label=label, node_color=node_color)

        # Node parameters

        self.bnode.boundary_smooth = boundary_smooth
        self.bnode.uv_smooth       = uv_smooth

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'mesh' : 0, 'level' : 1, 'crease' : 2, }
        self.outsockets = {'mesh' : 0, }

        # Input sockets plugging

        if mesh            is not None: self.mesh            = mesh
        if level           is not None: self.level           = level
        if crease          is not None: self.crease          = crease

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

# ----------------------------------------------------------------------------------------------------
# Node Switch for GeometryNodeSwitch

class Switch(Node):

    """

    Node Switch
    -----------
        > Geometry node name: Switch<br>
          Blender type: Switch
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Switch(switch=None, false=None, true=None, input_type='GEOMETRY', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - switch : input_type dependant
                - false : input_type dependant
                - true : input_type dependant
    

            Parameters
            ----------
                - input_type : str (default = 'GEOMETRY') in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
            - Input sockets  : ['switch', 'false', 'true']
            - Output sockets : ['output']   
              
              
    

        Output sockets
        --------------
            - output : input_type dependant
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Boolean.switch : Method
            - Collection.switch : Method
            - Float.switch : Method
            - Geometry.switch : Method
            - Image.switch : Method
            - Integer.switch : Method
            - Material.switch : Method
            - Object.switch : Method
            - String.switch : Method
            - Texture.switch : Method
            - functions.switch : Function
              
    """

    def __init__(self, switch=None, false=None, true=None, input_type='GEOMETRY', label=None, node_color=None):

        super().__init__('GeometryNodeSwitch', name='Switch', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.input_type      = input_type

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

# ----------------------------------------------------------------------------------------------------
# Node Transform for GeometryNodeTransform

class Transform(Node):

    """

    Node Transform
    --------------
        > Geometry node name: Transform<br>
          Blender type: Transform
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - geometry : Geometry
                - translation : Vector
                - rotation : Vector
                - scale : Vector
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - geometry : Geometry
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Geometry.transform : Method
              
    """

    def __init__(self, geometry=None, translation=None, rotation=None, scale=None, label=None, node_color=None):

        super().__init__('GeometryNodeTransform', name='Transform', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'geometry' : 0, 'translation' : 1, 'rotation' : 2, 'scale' : 3, }
        self.outsockets = {'geometry' : 0, }

        # Input sockets plugging

        if geometry        is not None: self.geometry        = geometry
        if translation     is not None: self.translation     = translation
        if rotation        is not None: self.rotation        = rotation
        if scale           is not None: self.scale           = scale

# ----------------------------------------------------------------------------------------------------
# Node TranslateInstances for GeometryNodeTranslateInstances

class TranslateInstances(Node):

    """

    Node TranslateInstances
    -----------------------
        > Geometry node name: Translate Instances<br>
          Blender type: Translate Instances
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.TranslateInstances(instances=None, selection=None, translation=None, local_space=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - instances : Instances
                - selection : Boolean
                - translation : Vector
                - local_space : Boolean
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - instances : Instances
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Instances.translate : Method
              
    """

    def __init__(self, instances=None, selection=None, translation=None, local_space=None, label=None, node_color=None):

        super().__init__('GeometryNodeTranslateInstances', name='Translate Instances', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'instances' : 0, 'selection' : 1, 'translation' : 2, 'local_space' : 3, }
        self.outsockets = {'instances' : 0, }

        # Input sockets plugging

        if instances       is not None: self.instances       = instances
        if selection       is not None: self.selection       = selection
        if translation     is not None: self.translation     = translation
        if local_space     is not None: self.local_space     = local_space

# ----------------------------------------------------------------------------------------------------
# Node Triangulate for GeometryNodeTriangulate

class Triangulate(Node):

    """

    Node Triangulate
    ----------------
        > Geometry node name: Triangulate<br>
          Blender type: Triangulate
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - mesh : Mesh
                - selection : Boolean
                - minimum_vertices : Integer
    

            Parameters
            ----------
                - ngon_method : str (default = 'BEAUTY') in ('BEAUTY', 'CLIP')
                - quad_method : str (default = 'SHORTEST_DIAGONAL') in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Mesh.triangulate : Method
              
    """

    def __init__(self, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None, node_color=None):

        super().__init__('GeometryNodeTriangulate', name='Triangulate', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node TrimCurve for GeometryNodeTrimCurve

class TrimCurve(Node):

    """

    Node TrimCurve
    --------------
        > Geometry node name: Trim Curve<br>
          Blender type: Trim Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.TrimCurve(curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - curve : Curve
                - start0 : Float
                - start1 : Float
                - end0 : Float
                - end1 : Float
    

            Parameters
            ----------
                - mode : str (default = 'FACTOR') in ('FACTOR', 'LENGTH')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - curve : Curve
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Curve.trim : Method
              
    """

    def __init__(self, curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None, node_color=None):

        super().__init__('GeometryNodeTrimCurve', name='Trim Curve', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node VolumeToMesh for GeometryNodeVolumeToMesh

class VolumeToMesh(Node):

    """

    Node VolumeToMesh
    -----------------
        > Geometry node name: Volume to Mesh<br>
          Blender type: Volume to Mesh
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.VolumeToMesh(volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - volume : Volume
                - voxel_size : Float
                - voxel_amount : Float
                - threshold : Float
                - adaptivity : Float
    

            Parameters
            ----------
                - resolution_mode : str (default = 'GRID') in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - mesh : Mesh
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Volume.to_mesh : Method
              
    """

    def __init__(self, volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None, node_color=None):

        super().__init__('GeometryNodeVolumeToMesh', name='Volume to Mesh', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node Clamp for ShaderNodeClamp

class Clamp(Node):

    """

    Node Clamp
    ----------
        > Geometry node name: Clamp<br>
          Blender type: Clamp
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - value : Float
                - min : Float
                - max : Float
    

            Parameters
            ----------
                - clamp_type : str (default = 'MINMAX') in ('MINMAX', 'RANGE')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - result : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.clamp : Method
              
    """

    def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX', label=None, node_color=None):

        super().__init__('ShaderNodeClamp', name='Clamp', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node CombineRgb for ShaderNodeCombineRGB

class CombineRgb(Node):

    """

    Node CombineRgb
    ---------------
        > Geometry node name: Combine RGB<br>
          Blender type: Combine RGB
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CombineRgb(r=None, g=None, b=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - r : Float
                - g : Float
                - b : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - image : Color
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Color.Combine : Constructor
              
    """

    def __init__(self, r=None, g=None, b=None, label=None, node_color=None):

        super().__init__('ShaderNodeCombineRGB', name='Combine RGB', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'r' : 0, 'g' : 1, 'b' : 2, }
        self.outsockets = {'image' : 0, }

        # Input sockets plugging

        if r               is not None: self.r               = r
        if g               is not None: self.g               = g
        if b               is not None: self.b               = b

# ----------------------------------------------------------------------------------------------------
# Node CombineXyz for ShaderNodeCombineXYZ

class CombineXyz(Node):

    """

    Node CombineXyz
    ---------------
        > Geometry node name: Combine XYZ<br>
          Blender type: Combine XYZ
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CombineXyz(x=None, y=None, z=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - x : Float
                - y : Float
                - z : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vector : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.Combine : Constructor
              
    """

    def __init__(self, x=None, y=None, z=None, label=None, node_color=None):

        super().__init__('ShaderNodeCombineXYZ', name='Combine XYZ', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'x' : 0, 'y' : 1, 'z' : 2, }
        self.outsockets = {'vector' : 0, }

        # Input sockets plugging

        if x               is not None: self.x               = x
        if y               is not None: self.y               = y
        if z               is not None: self.z               = z

# ----------------------------------------------------------------------------------------------------
# Node FloatCurve for ShaderNodeFloatCurve

class FloatCurve(Node):

    """

    Node FloatCurve
    ---------------
        > Geometry node name: Float Curve<br>
          Blender type: Float Curve
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.FloatCurve(factor=None, value=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - factor : Float
                - value : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - value : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.curve : Method
              
    """

    def __init__(self, factor=None, value=None, label=None, node_color=None):

        super().__init__('ShaderNodeFloatCurve', name='Float Curve', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'factor' : 0, 'value' : 1, }
        self.outsockets = {'value' : 0, }

        # Input sockets plugging

        if factor          is not None: self.factor          = factor
        if value           is not None: self.value           = value

# ----------------------------------------------------------------------------------------------------
# Node MapRange for ShaderNodeMapRange

class MapRange(Node):

    """

    Node MapRange
    -------------
        > Geometry node name: Map Range<br>
          Blender type: Map Range
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - value : Float
                - from_min : data_type dependant
                - from_max : data_type dependant
                - to_min : data_type dependant
                - to_max : data_type dependant
                - steps : data_type dependant
                - vector : Vector
    

            Parameters
            ----------
                - clamp : bool (default = True)
                - data_type : str (default = 'FLOAT') in ('FLOAT', 'FLOAT_VECTOR')
                - interpolation_type : str (default = 'LINEAR') in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Data type dependant sockets
        ---------------------------
            - Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')
            - Input sockets  : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']
            - Output sockets : []   
              
              
    

        Output sockets
        --------------
            - result : Float
            - vector : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.map_range : Method
            - Vector.map_range : Method
              
    """

    def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None, node_color=None):

        super().__init__('ShaderNodeMapRange', name='Map Range', label=label, node_color=node_color)

        # Node parameters to configure the sockets enablement

        self.bnode.clamp           = clamp
        self.bnode.data_type       = data_type
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

# ----------------------------------------------------------------------------------------------------
# Node Math for ShaderNodeMath

class Math(Node):

    """

    Node Math
    ---------
        > Geometry node name: Math<br>
          Blender type: Math
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - value0 : Float
                - value1 : Float
                - value2 : Float
    

            Parameters
            ----------
                - operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - value : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.abs : Method
            - Float.add : Method
            - Float.arccos : Method
            - Float.arcsin : Method
            - Float.arctan : Method
            - Float.arctan2 : Method
            - Float.ceil : Method
            - Float.compare : Method
            - Float.cos : Method
            - Float.cosh : Method
            - Float.degrees : Method
            - Float.divide : Method
            - Float.exp : Method
            - Float.floor : Method
            - Float.fract : Method
            - Float.greater_than : Method
            - Float.inverse_sqrt : Method
            - Float.less_than : Method
            - Float.log : Method
            - Float.max : Method
            - Float.min : Method
            - Float.modulo : Method
            - Float.multiply : Method
            - Float.multiply_add : Method
            - Float.pingpong : Method
            - Float.pow : Method
            - Float.radians : Method
            - Float.round : Method
            - Float.sign : Method
            - Float.sin : Method
            - Float.sinh : Method
            - Float.smooth_max : Method
            - Float.smooth_min : Method
            - Float.snap : Method
            - Float.sqrt : Method
            - Float.subtract : Method
            - Float.tan : Method
            - Float.tanh : Method
            - Float.trunc : Method
            - Float.wrap : Method
            - Integer.abs : Method
            - Integer.add : Method
            - Integer.arccos : Method
            - Integer.arcsin : Method
            - Integer.arctan : Method
            - Integer.arctan2 : Method
            - Integer.ceil : Method
            - Integer.compare : Method
            - Integer.cos : Method
            - Integer.cosh : Method
            - Integer.degrees : Method
            - Integer.divide : Method
            - Integer.exp : Method
            - Integer.floor : Method
            - Integer.fract : Method
            - Integer.greater_than : Method
            - Integer.inverse_sqrt : Method
            - Integer.less_than : Method
            - Integer.log : Method
            - Integer.max : Method
            - Integer.min : Method
            - Integer.modulo : Method
            - Integer.multiply : Method
            - Integer.multiply_add : Method
            - Integer.pingpong : Method
            - Integer.pow : Method
            - Integer.radians : Method
            - Integer.round : Method
            - Integer.sign : Method
            - Integer.sin : Method
            - Integer.sinh : Method
            - Integer.smooth_max : Method
            - Integer.smooth_min : Method
            - Integer.snap : Method
            - Integer.sqrt : Method
            - Integer.subtract : Method
            - Integer.tan : Method
            - Integer.tanh : Method
            - Integer.trunc : Method
            - Integer.wrap : Method
            - functions.abs : Function
            - functions.add : Function
            - functions.arccos : Function
            - functions.arcsin : Function
            - functions.arctan : Function
            - functions.arctan2 : Function
            - functions.ceil : Function
            - functions.compare : Function
            - functions.cos : Function
            - functions.cosh : Function
            - functions.degrees : Function
            - functions.divide : Function
            - functions.exp : Function
            - functions.floor : Function
            - functions.fract : Function
            - functions.greater_than : Function
            - functions.inverse_sqrt : Function
            - functions.less_than : Function
            - functions.log : Function
            - functions.max : Function
            - functions.min : Function
            - functions.modulo : Function
            - functions.multiply : Function
            - functions.multiply_add : Function
            - functions.pingpong : Function
            - functions.pow : Function
            - functions.radians : Function
            - functions.round : Function
            - functions.sign : Function
            - functions.sin : Function
            - functions.sinh : Function
            - functions.smooth_max : Function
            - functions.smooth_min : Function
            - functions.snap : Function
            - functions.sqrt : Function
            - functions.subtract : Function
            - functions.tan : Function
            - functions.tanh : Function
            - functions.trunc : Function
            - functions.wrap : Function
              
    """

    def __init__(self, value0=None, value1=None, value2=None, operation='ADD', label=None, node_color=None):

        super().__init__('ShaderNodeMath', name='Math', label=label, node_color=node_color)

        # Node parameters

        self.bnode.operation       = operation

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

# ----------------------------------------------------------------------------------------------------
# Node Mix for ShaderNodeMixRGB

class Mix(Node):

    """

    Node Mix
    --------
        > Geometry node name: Mix<br>
          Blender type: Mix
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Mix(color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - fac : Float
                - color1 : Color
                - color2 : Color
    

            Parameters
            ----------
                - blend_type : str (default = 'MIX') in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
                - use_alpha : bool (default = False)
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Color.add : Method
            - Color.burn : Method
            - Color.darken : Method
            - Color.difference : Method
            - Color.divide : Method
            - Color.dodge : Method
            - Color.hue : Method
            - Color.lighten : Method
            - Color.linear_light : Method
            - Color.mix : Method
            - Color.mix : Method
            - Color.mix_color : Method
            - Color.multiply : Method
            - Color.overlay : Method
            - Color.saturation : Method
            - Color.screen : Method
            - Color.soft_light : Method
            - Color.subtract : Method
            - Color.value : Method
            - functions.color_add : Function
            - functions.color_burn : Function
            - functions.color_darken : Function
            - functions.color_difference : Function
            - functions.color_divide : Function
            - functions.color_dodge : Function
            - functions.color_hue : Function
            - functions.color_lighten : Function
            - functions.color_linear_light : Function
            - functions.color_mix : Function
            - functions.color_mix_color : Function
            - functions.color_multiply : Function
            - functions.color_overlay : Function
            - functions.color_saturation : Function
            - functions.color_screen : Function
            - functions.color_soft_light : Function
            - functions.color_subtract : Function
            - functions.color_value : Function
              
    """

    def __init__(self, color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None, node_color=None):

        super().__init__('ShaderNodeMixRGB', name='Mix', label=label, node_color=node_color)

        # Node parameters

        self.bnode.blend_type      = blend_type
        self.bnode.use_alpha       = use_alpha

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, 'color1' : 1, 'color2' : 2, }
        self.outsockets = {'color' : 0, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac
        if color1          is not None: self.color1          = color1
        if color2          is not None: self.color2          = color2

    @property
    def blend_type(self):
        return self.bnode.blend_type

    @blend_type.setter
    def blend_type(self, value):
        self.bnode.blend_type = value

    @property
    def use_alpha(self):
        return self.bnode.use_alpha

    @use_alpha.setter
    def use_alpha(self, value):
        self.bnode.use_alpha = value

# ----------------------------------------------------------------------------------------------------
# Node RgbCurves for ShaderNodeRGBCurve

class RgbCurves(Node):

    """

    Node RgbCurves
    --------------
        > Geometry node name: RGB Curves<br>
          Blender type: RGB Curves
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.RgbCurves(fac=None, color=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - fac : Float
                - color : Color
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Color.curves : Method
              
    """

    def __init__(self, fac=None, color=None, label=None, node_color=None):

        super().__init__('ShaderNodeRGBCurve', name='RGB Curves', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, 'color' : 1, }
        self.outsockets = {'color' : 0, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac
        if color           is not None: self.color           = color

# ----------------------------------------------------------------------------------------------------
# Node SeparateRgb for ShaderNodeSeparateRGB

class SeparateRgb(Node):

    """

    Node SeparateRgb
    ----------------
        > Geometry node name: Separate RGB<br>
          Blender type: Separate RGB
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SeparateRgb(image=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - image : Color
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - r : Float
            - g : Float
            - b : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Color.b : Property
            - Color.g : Property
            - Color.r : Property
            - Color.separate : Property
              
    """

    def __init__(self, image=None, label=None, node_color=None):

        super().__init__('ShaderNodeSeparateRGB', name='Separate RGB', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'image' : 0, }
        self.outsockets = {'r' : 0, 'g' : 1, 'b' : 2, }

        # Input sockets plugging

        if image           is not None: self.image           = image

# ----------------------------------------------------------------------------------------------------
# Node SeparateXyz for ShaderNodeSeparateXYZ

class SeparateXyz(Node):

    """

    Node SeparateXyz
    ----------------
        > Geometry node name: Separate XYZ<br>
          Blender type: Separate XYZ
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.SeparateXyz(vector=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - x : Float
            - y : Float
            - z : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.separate : Property
            - Vector.x : Property
            - Vector.y : Property
            - Vector.z : Property
              
    """

    def __init__(self, vector=None, label=None, node_color=None):

        super().__init__('ShaderNodeSeparateXYZ', name='Separate XYZ', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, }
        self.outsockets = {'x' : 0, 'y' : 1, 'z' : 2, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector

# ----------------------------------------------------------------------------------------------------
# Node BrickTexture for ShaderNodeTexBrick

class BrickTexture(Node):

    """

    Node BrickTexture
    -----------------
        > Geometry node name: Brick Texture<br>
          Blender type: Brick Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - color1 : Color
                - color2 : Color
                - mortar : Color
                - scale : Float
                - mortar_size : Float
                - mortar_smooth : Float
                - bias : Float
                - brick_width : Float
                - row_height : Float
    

            Parameters
            ----------
                - offset : float (default = 0.5)
                - offset_frequency : int (default = 2)
                - squash : float (default = 1.0)
                - squash_frequency : int (default = 2)
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - fac : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Brick : Static method
              
    """

    def __init__(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None, node_color=None):

        super().__init__('ShaderNodeTexBrick', name='Brick Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node CheckerTexture for ShaderNodeTexChecker

class CheckerTexture(Node):

    """

    Node CheckerTexture
    -------------------
        > Geometry node name: Checker Texture<br>
          Blender type: Checker Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.CheckerTexture(vector=None, color1=None, color2=None, scale=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - color1 : Color
                - color2 : Color
                - scale : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - fac : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Checker : Static method
              
    """

    def __init__(self, vector=None, color1=None, color2=None, scale=None, label=None, node_color=None):

        super().__init__('ShaderNodeTexChecker', name='Checker Texture', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'vector' : 0, 'color1' : 1, 'color2' : 2, 'scale' : 3, }
        self.outsockets = {'color' : 0, 'fac' : 1, }

        # Input sockets plugging

        if vector          is not None: self.vector          = vector
        if color1          is not None: self.color1          = color1
        if color2          is not None: self.color2          = color2
        if scale           is not None: self.scale           = scale

# ----------------------------------------------------------------------------------------------------
# Node GradientTexture for ShaderNodeTexGradient

class GradientTexture(Node):

    """

    Node GradientTexture
    --------------------
        > Geometry node name: Gradient Texture<br>
          Blender type: Gradient Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.GradientTexture(vector=None, gradient_type='LINEAR', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
    

            Parameters
            ----------
                - gradient_type : str (default = 'LINEAR') in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - fac : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Gradient : Static method
              
    """

    def __init__(self, vector=None, gradient_type='LINEAR', label=None, node_color=None):

        super().__init__('ShaderNodeTexGradient', name='Gradient Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node MagicTexture for ShaderNodeTexMagic

class MagicTexture(Node):

    """

    Node MagicTexture
    -----------------
        > Geometry node name: Magic Texture<br>
          Blender type: Magic Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - scale : Float
                - distortion : Float
    

            Parameters
            ----------
                - turbulence_depth : int (default = 2)
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - fac : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Magic : Static method
              
    """

    def __init__(self, vector=None, scale=None, distortion=None, turbulence_depth=2, label=None, node_color=None):

        super().__init__('ShaderNodeTexMagic', name='Magic Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node MusgraveTexture for ShaderNodeTexMusgrave

class MusgraveTexture(Node):

    """

    Node MusgraveTexture
    --------------------
        > Geometry node name: Musgrave Texture<br>
          Blender type: Musgrave Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - w : Float
                - scale : Float
                - detail : Float
                - dimension : Float
                - lacunarity : Float
                - offset : Float
                - gain : Float
    

            Parameters
            ----------
                - musgrave_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')
                - musgrave_type : str (default = 'FBM') in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - fac : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Musgrave : Static method
              
    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None, node_color=None):

        super().__init__('ShaderNodeTexMusgrave', name='Musgrave Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node NoiseTexture for ShaderNodeTexNoise

class NoiseTexture(Node):

    """

    Node NoiseTexture
    -----------------
        > Geometry node name: Noise Texture<br>
          Blender type: Noise Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - w : Float
                - scale : Float
                - detail : Float
                - roughness : Float
                - distortion : Float
    

            Parameters
            ----------
                - noise_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - fac : Float
            - color : Color
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Noise : Static method
              
    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None, node_color=None):

        super().__init__('ShaderNodeTexNoise', name='Noise Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node VoronoiTexture for ShaderNodeTexVoronoi

class VoronoiTexture(Node):

    """

    Node VoronoiTexture
    -------------------
        > Geometry node name: Voronoi Texture<br>
          Blender type: Voronoi Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - w : Float
                - scale : Float
                - smoothness : Float
                - exponent : Float
                - randomness : Float
    

            Parameters
            ----------
                - distance : str (default = 'EUCLIDEAN') in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
                - feature : str (default = 'F1') in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
                - voronoi_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - distance : Float
            - color : Color
            - position : Vector
            - w : Float
            - radius : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Voronoi : Static method
              
    """

    def __init__(self, vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None, node_color=None):

        super().__init__('ShaderNodeTexVoronoi', name='Voronoi Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node WaveTexture for ShaderNodeTexWave

class WaveTexture(Node):

    """

    Node WaveTexture
    ----------------
        > Geometry node name: Wave Texture<br>
          Blender type: Wave Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - scale : Float
                - distortion : Float
                - detail : Float
                - detail_scale : Float
                - detail_roughness : Float
                - phase_offset : Float
    

            Parameters
            ----------
                - bands_direction : str (default = 'X') in ('X', 'Y', 'Z', 'DIAGONAL')
                - rings_direction : str (default = 'X') in ('X', 'Y', 'Z', 'SPHERICAL')
                - wave_profile : str (default = 'SIN') in ('SIN', 'SAW', 'TRI')
                - wave_type : str (default = 'BANDS') in ('BANDS', 'RINGS')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - fac : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.Wave : Static method
              
    """

    def __init__(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None, node_color=None):

        super().__init__('ShaderNodeTexWave', name='Wave Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node WhiteNoiseTexture for ShaderNodeTexWhiteNoise

class WhiteNoiseTexture(Node):

    """

    Node WhiteNoiseTexture
    ----------------------
        > Geometry node name: White Noise Texture<br>
          Blender type: White Noise Texture
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - w : Float
    

            Parameters
            ----------
                - noise_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - value : Float
            - color : Color
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Texture.WhiteNoise : Static method
              
    """

    def __init__(self, vector=None, w=None, noise_dimensions='3D', label=None, node_color=None):

        super().__init__('ShaderNodeTexWhiteNoise', name='White Noise Texture', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node ColorRamp for ShaderNodeValToRGB

class ColorRamp(Node):

    """

    Node ColorRamp
    --------------
        > Geometry node name: ColorRamp<br>
          Blender type: ColorRamp
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.ColorRamp(fac=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - fac : Float
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - color : Color
            - alpha : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Float.color_ramp : Method
              
    """

    def __init__(self, fac=None, label=None, node_color=None):

        super().__init__('ShaderNodeValToRGB', name='ColorRamp', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, }
        self.outsockets = {'color' : 0, 'alpha' : 1, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac

# ----------------------------------------------------------------------------------------------------
# Node Value for ShaderNodeValue

class Value(Node):

    """

    Node Value
    ----------
        > Geometry node name: Value<br>
          Blender type: Value
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.Value(label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - value : Float
    """

    def __init__(self, label=None, node_color=None):

        super().__init__('ShaderNodeValue', name='Value', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'value' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node VectorCurves for ShaderNodeVectorCurve

class VectorCurves(Node):

    """

    Node VectorCurves
    -----------------
        > Geometry node name: Vector Curves<br>
          Blender type: Vector Curves
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.VectorCurves(fac=None, vector=None, label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - fac : Float
                - vector : Vector
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vector : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.curves : Method
              
    """

    def __init__(self, fac=None, vector=None, label=None, node_color=None):

        super().__init__('ShaderNodeVectorCurve', name='Vector Curves', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {'fac' : 0, 'vector' : 1, }
        self.outsockets = {'vector' : 0, }

        # Input sockets plugging

        if fac             is not None: self.fac             = fac
        if vector          is not None: self.vector          = vector

# ----------------------------------------------------------------------------------------------------
# Node VectorMath for ShaderNodeVectorMath

class VectorMath(Node):

    """

    Node VectorMath
    ---------------
        > Geometry node name: Vector Math<br>
          Blender type: Vector Math
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector0 : Vector
                - vector1 : Vector
                - vector2 : Vector
                - scale : Float
    

            Parameters
            ----------
                - operation : str (default = 'ADD') in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vector : Vector
            - value : Float
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.absolute : Method
            - Vector.add : Method
            - Vector.ceil : Method
            - Vector.cos : Method
            - Vector.cross : Method
            - Vector.distance : Method
            - Vector.divide : Method
            - Vector.dot : Method
            - Vector.faceforward : Method
            - Vector.floor : Method
            - Vector.fraction : Method
            - Vector.length : Method
            - Vector.max : Method
            - Vector.min : Method
            - Vector.modulo : Method
            - Vector.multiply : Method
            - Vector.multiply_add : Method
            - Vector.normalize : Method
            - Vector.project : Method
            - Vector.reflect : Method
            - Vector.refract : Method
            - Vector.scale : Method
            - Vector.sin : Method
            - Vector.snap : Method
            - Vector.subtract : Method
            - Vector.tan : Method
            - Vector.wrap : Method
            - functions.cross : Function
            - functions.distance : Function
            - functions.dot : Function
            - functions.faceforward : Function
            - functions.fraction : Function
            - functions.length : Function
            - functions.normalize : Function
            - functions.project : Function
            - functions.reflect : Function
            - functions.refract : Function
            - functions.scale : Function
            - functions.vector_absolute : Function
            - functions.vector_add : Function
            - functions.vector_ceil : Function
            - functions.vector_cos : Function
            - functions.vector_divide : Function
            - functions.vector_floor : Function
            - functions.vector_max : Function
            - functions.vector_min : Function
            - functions.vector_modulo : Function
            - functions.vector_multiply : Function
            - functions.vector_multiply_add : Function
            - functions.vector_sin : Function
            - functions.vector_snap : Function
            - functions.vector_subtract : Function
            - functions.vector_tan : Function
            - functions.vector_wrap : Function
              
    """

    def __init__(self, vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None, node_color=None):

        super().__init__('ShaderNodeVectorMath', name='Vector Math', label=label, node_color=node_color)

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

# ----------------------------------------------------------------------------------------------------
# Node VectorRotate for ShaderNodeVectorRotate

class VectorRotate(Node):

    """

    Node VectorRotate
    -----------------
        > Geometry node name: Vector Rotate<br>
          Blender type: Vector Rotate
          
        <sub>go to index</sub>
    

        Initialization
        --------------
            ```python
            from geonodes import nodes
            node = nodes.VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None, node_color=None)
            ```
            
            
    

        Arguments
        ---------
    

            Input sockets
            -------------
                - vector : Vector
                - center : Vector
                - axis : Vector
                - angle : Float
                - rotation : Vector
    

            Parameters
            ----------
                - invert : bool (default = False)
                - rotation_type : str (default = 'AXIS_ANGLE') in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')
    

            Node label
            ----------
                - label : Geometry node display label (default=None)
                - node_color : Geometry node color (default=None)
    

        Output sockets
        --------------
            - vector : Vector
    

        Data sockets
        ------------
            > Data socket classes implementing this node.
              
              
            - Vector.rotate : Method
              
    """

    def __init__(self, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None, node_color=None):

        super().__init__('ShaderNodeVectorRotate', name='Vector Rotate', label=label, node_color=node_color)

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
# --------------------------------------------------------------------------------
# Create node from its bl_idname

def create_node(bl_idname, *args, **kwargs):
    nodes = {'FunctionNodeAlignEulerToVector': AlignEulerToVector,
    'FunctionNodeBooleanMath': BooleanMath,
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
    'FunctionNodeSliceString': SliceString,
    'FunctionNodeStringLength': StringLength,
    'FunctionNodeValueToString': ValueToString,
    'GeometryNodeAccumulateField': AccumulateField,
    'GeometryNodeAttributeDomainSize': DomainSize,
    'GeometryNodeAttributeStatistic': AttributeStatistic,
    'GeometryNodeAttributeTransfer': TransferAttribute,
    'GeometryNodeBoundBox': BoundingBox,
    'GeometryNodeCaptureAttribute': CaptureAttribute,
    'GeometryNodeCollectionInfo': CollectionInfo,
    'GeometryNodeConvexHull': ConvexHull,
    'GeometryNodeCurveArc': Arc,
    'GeometryNodeCurveEndpointSelection': EndpointSelection,
    'GeometryNodeCurveHandleTypeSelection': HandleTypeSelection,
    'GeometryNodeCurveLength': CurveLength,
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
    'GeometryNodeDeleteGeometry': DeleteGeometry,
    'GeometryNodeDistributePointsOnFaces': DistributePointsOnFaces,
    'GeometryNodeDualMesh': DualMesh,
    'GeometryNodeDuplicateElements': DuplicateElements,
    'GeometryNodeExtrudeMesh': ExtrudeMesh,
    'GeometryNodeFieldAtIndex': FieldAtIndex,
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
    'GeometryNodeMeshGrid': Grid,
    'GeometryNodeMeshIcoSphere': IcoSphere,
    'GeometryNodeMeshLine': MeshLine,
    'GeometryNodeMeshToCurve': MeshToCurve,
    'GeometryNodeMeshToPoints': MeshToPoints,
    'GeometryNodeMeshUVSphere': UvSphere,
    'GeometryNodeObjectInfo': ObjectInfo,
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
    'GeometryNodeScaleElements': ScaleElements,
    'GeometryNodeScaleInstances': ScaleInstances,
    'GeometryNodeSeparateComponents': SeparateComponents,
    'GeometryNodeSeparateGeometry': SeparateGeometry,
    'GeometryNodeSetCurveHandlePositions': SetHandlePositions,
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
    'GeometryNodeVolumeToMesh': VolumeToMesh,
    'ShaderNodeClamp': Clamp,
    'ShaderNodeCombineRGB': CombineRgb,
    'ShaderNodeCombineXYZ': CombineXyz,
    'ShaderNodeFloatCurve': FloatCurve,
    'ShaderNodeMapRange': MapRange,
    'ShaderNodeMath': Math,
    'ShaderNodeMixRGB': Mix,
    'ShaderNodeRGBCurve': RgbCurves,
    'ShaderNodeSeparateRGB': SeparateRgb,
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

