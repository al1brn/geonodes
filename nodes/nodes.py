from geonodes.core.node import Node

# ----------------------------------------------------------------------------------------------------
# Node AlignEulerToVector for FunctionNodeAlignEulerToVector

class AlignEulerToVector(Node):

    """Class AlignEulerToVector
    

    | Geometry node name: 'Align Euler to Vector' 
    | Blender type:  FunctionNodeAlignEulerToVector 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - rotation : Vector 
            - factor   : Float 
            - vector   : Vector 
    

            Parameters
            ----------
            - axis       : 'X' in ('X', 'Y', 'Z') 
            - pivot_axis : 'AUTO' in ('AUTO', 'X', 'Y', 'Z') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - rotation : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector AlignToVector   : Constructor 
    - Vector align_to_vector : Stacked method 
    """

    def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None):

        super().__init__('FunctionNodeAlignEulerToVector', name='Align Euler to Vector', label=label)
        # Parameters

        self.bnode.axis            = axis
        self.bnode.pivot_axis      = pivot_axis

        # Input sockets

        self.plug(0, rotation)
        self.plug(1, factor)
        self.plug(2, vector)

        # Output sockets

        self.rotation        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'rotation': self.rotation}

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

    """Class BooleanMath
    

    | Geometry node name: 'Boolean Math' 
    | Blender type:  FunctionNodeBooleanMath 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - boolean0 : Boolean 
            - boolean1 : Boolean 
    

            Parameters
            ----------
            - operation : 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - boolean : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean b_and  : Method 
    - Boolean b_not  : Method 
    - Boolean b_or   : Method 
    - Boolean imply  : Method 
    - Boolean nand   : Method 
    - Boolean nimply : Method 
    - Boolean nor    : Method 
    - Boolean xnor   : Method 
    - Boolean xor    : Method 
    """

    def __init__(self, boolean0=None, boolean1=None, operation='AND', label=None):

        super().__init__('FunctionNodeBooleanMath', name='Boolean Math', label=label)
        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(0, boolean0)
        self.plug(1, boolean1)

        # Output sockets

        self.boolean         = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'boolean': self.boolean}

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

# ----------------------------------------------------------------------------------------------------
# Node Compare for FunctionNodeCompare

class Compare(Node):

    """Class Compare
    

    | Geometry node name: 'Compare' 
    | Blender type:  FunctionNodeCompare 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT',
        operation='GREATER_THAN', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - a       : data_type dependant 
            - b       : data_type dependant 
            - c       : Float 
            - angle   : Float 
            - epsilon : Float 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA') 
            - mode      : 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION') 
            - operation : 'GREATER_THAN' in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA') 
    - Input sockets     : a b 
    

    Output sockets
    ==============
    - result : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Color brighter        : Method 
    - Color darker          : Method 
    - Color equal           : Method 
    - Color not_equal       : Method 
    - Float equal           : Method 
    - Float greater_equal   : Method 
    - Float greater_than    : Method 
    - Float less_equal      : Method 
    - Float less_than       : Method 
    - Float not_equal       : Method 
    - Integer equal         : Method 
    - Integer greater_equal : Method 
    - Integer greater_than  : Method 
    - Integer less_equal    : Method 
    - Integer less_than     : Method 
    - Integer not_equal     : Method 
    - String average        : Method 
    - String direction      : Method 
    - String dot_product    : Method 
    - String element        : Method 
    - String length         : Method 
    - Vector equal          : Method 
    - Vector greater_equal  : Method 
    - Vector greater_than   : Method 
    - Vector less_equal     : Method 
    - Vector less_than      : Method 
    - Vector not_equal      : Method 
    - functions compare     : Function 
    """

    def __init__(self, a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None):

        super().__init__('FunctionNodeCompare', name='Compare', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.mode            = mode
        self.bnode.operation       = operation

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(0, a)
            self.plug(1, b)
        elif data_type == 'INT':
            self.plug(2, a)
            self.plug(3, b)
        elif data_type == 'VECTOR':
            self.plug(4, a)
            self.plug(5, b)
        elif data_type == 'STRING':
            self.plug(8, a)
            self.plug(9, b)
        elif data_type == 'RGBA':
            self.plug(6, a)
            self.plug(7, b)

        self.plug(10, c)
        self.plug(11, angle)
        self.plug(12, epsilon)


        # Output sockets

        self.result          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'result': self.result}

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

    """Class FloatToInteger
    

    | Geometry node name: 'Float to Integer' 
    | Blender type:  FunctionNodeFloatToInt 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FloatToInteger(float=None, rounding_mode='ROUND', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - float : Float 
    

            Parameters
            ----------
            - rounding_mode : 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - integer : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float to_integer : Method 
    """

    def __init__(self, float=None, rounding_mode='ROUND', label=None):

        super().__init__('FunctionNodeFloatToInt', name='Float to Integer', label=label)
        # Parameters

        self.bnode.rounding_mode   = rounding_mode

        # Input sockets

        self.plug(0, float)

        # Output sockets

        self.integer         = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'integer': self.integer}

    @property
    def rounding_mode(self):
        return self.bnode.rounding_mode

    @rounding_mode.setter
    def rounding_mode(self, value):
        self.bnode.rounding_mode = value

# ----------------------------------------------------------------------------------------------------
# Node Boolean for FunctionNodeInputBool

class Boolean(Node):

    """Class Boolean
    

    | Geometry node name: 'Boolean' 
    | Blender type:  FunctionNodeInputBool 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Boolean(boolean=False, label=None) 
    

        Arguments
        ---------
    

            Parameters
            ----------
            - boolean : False bool 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - boolean : Boolean 
    """

    def __init__(self, boolean=False, label=None):

        super().__init__('FunctionNodeInputBool', name='Boolean', label=label)
        # Parameters

        self.bnode.boolean         = boolean

        # Output sockets

        self.boolean         = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'boolean': self.boolean}

    @property
    def boolean_(self):
        return self.bnode.boolean

    @boolean_.setter
    def boolean_(self, value):
        self.bnode.boolean = value

# ----------------------------------------------------------------------------------------------------
# Node Color for FunctionNodeInputColor

class Color(Node):

    """Class Color
    

    | Geometry node name: 'Color' 
    | Blender type:  FunctionNodeInputColor 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Color(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    """

    def __init__(self, label=None):

        super().__init__('FunctionNodeInputColor', name='Color', label=label)
        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = {'color': self.color}

# ----------------------------------------------------------------------------------------------------
# Node Integer for FunctionNodeInputInt

class Integer(Node):

    """Class Integer
    

    | Geometry node name: 'Integer' 
    | Blender type:  FunctionNodeInputInt 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Integer(integer=0, label=None) 
    

        Arguments
        ---------
    

            Parameters
            ----------
            - integer : 0 int 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - integer : Integer 
    """

    def __init__(self, integer=0, label=None):

        super().__init__('FunctionNodeInputInt', name='Integer', label=label)
        # Parameters

        self.bnode.integer         = integer

        # Output sockets

        self.integer         = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'integer': self.integer}

    @property
    def integer_(self):
        return self.bnode.integer

    @integer_.setter
    def integer_(self, value):
        self.bnode.integer = value

# ----------------------------------------------------------------------------------------------------
# Node SpecialCharacters for FunctionNodeInputSpecialCharacters

class SpecialCharacters(Node):

    """Class SpecialCharacters
    

    | Geometry node name: 'Special Characters' 
    | Blender type:  FunctionNodeInputSpecialCharacters 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SpecialCharacters(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - line_break : String 
    - tab        : String 
    """

    def __init__(self, label=None):

        super().__init__('FunctionNodeInputSpecialCharacters', name='Special Characters', label=label)
        # Output sockets

        self.line_break      = self.String(self.bnode.outputs[0])
        self.tab             = self.String(self.bnode.outputs[1])
        self.output_sockets  = {'line_break': self.line_break, 'tab': self.tab}

# ----------------------------------------------------------------------------------------------------
# Node String for FunctionNodeInputString

class String(Node):

    """Class String
    

    | Geometry node name: 'String' 
    | Blender type:  FunctionNodeInputString 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.String(string='', label=None) 
    

        Arguments
        ---------
    

            Parameters
            ----------
            - string : '' str 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - string : String 
    """

    def __init__(self, string='', label=None):

        super().__init__('FunctionNodeInputString', name='String', label=label)
        # Parameters

        self.bnode.string          = string

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = {'string': self.string}

    @property
    def string_(self):
        return self.bnode.string

    @string_.setter
    def string_(self, value):
        self.bnode.string = value

# ----------------------------------------------------------------------------------------------------
# Node Vector for FunctionNodeInputVector

class Vector(Node):

    """Class Vector
    

    | Geometry node name: 'Vector' 
    | Blender type:  FunctionNodeInputVector 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Vector(vector=[0.0, 0.0, 0.0], label=None) 
    

        Arguments
        ---------
    

            Parameters
            ----------
            - vector : [0.0, 0.0, 0.0] Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vector : Vector 
    """

    def __init__(self, vector=[0.0, 0.0, 0.0], label=None):

        super().__init__('FunctionNodeInputVector', name='Vector', label=label)
        # Parameters

        self.bnode.vector          = vector

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'vector': self.vector}

    @property
    def vector_(self):
        return self.bnode.vector

    @vector_.setter
    def vector_(self, value):
        self.bnode.vector = value

# ----------------------------------------------------------------------------------------------------
# Node RandomValue for FunctionNodeRandomValue

class RandomValue(Node):

    """Class RandomValue
    

    | Geometry node name: 'Random Value' 
    | Blender type:  FunctionNodeRandomValue 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - min         : data_type dependant 
            - max         : data_type dependant 
            - probability : Float 
            - ID          : Integer 
            - seed        : Integer 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN') 
    - Input sockets     : min max 
    - Output sockets    : value 
    

    Output sockets
    ==============
    - value : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean Random : Constructor 
    - Float Random   : Constructor 
    - Integer Random : Constructor 
    - Vector Random  : Constructor 
    """

    def __init__(self, min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None):

        super().__init__('FunctionNodeRandomValue', name='Random Value', label=label)
        # Parameters

        self.bnode.data_type       = data_type

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, min)
            self.plug(3, max)
        elif data_type == 'INT':
            self.plug(4, min)
            self.plug(5, max)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(0, min)
            self.plug(1, max)

        self.plug(6, probability)
        self.plug(7, ID)
        self.plug(8, seed)

        # Output sockets

        if data_type == 'FLOAT':
            self.value           = self.Float(self.bnode.outputs[1])
        elif data_type == 'INT':
            self.value           = self.Integer(self.bnode.outputs[2])
        elif data_type == 'FLOAT_VECTOR':
            self.value           = self.Vector(self.bnode.outputs[0])
        elif data_type == 'BOOLEAN':
            self.value           = self.Boolean(self.bnode.outputs[3])

        self.output_sockets  = {'value': self.value}

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

# ----------------------------------------------------------------------------------------------------
# Node ReplaceString for FunctionNodeReplaceString

class ReplaceString(Node):

    """Class ReplaceString
    

    | Geometry node name: 'Replace String' 
    | Blender type:  FunctionNodeReplaceString 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ReplaceString(string=None, find=None, replace=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - string  : String 
            - find    : String 
            - replace : String 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - string : String 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - String replace : Stacked method 
    """

    def __init__(self, string=None, find=None, replace=None, label=None):

        super().__init__('FunctionNodeReplaceString', name='Replace String', label=label)
        # Input sockets

        self.plug(0, string)
        self.plug(1, find)
        self.plug(2, replace)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = {'string': self.string}

# ----------------------------------------------------------------------------------------------------
# Node RotateEuler for FunctionNodeRotateEuler

class RotateEuler(Node):

    """Class RotateEuler
    

    | Geometry node name: 'Rotate Euler' 
    | Blender type:  FunctionNodeRotateEuler 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - rotation  : Vector 
            - rotate_by : Vector 
            - axis      : Vector 
            - angle     : Float 
    

            Parameters
            ----------
            - space : 'OBJECT' in ('OBJECT', 'LOCAL') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - rotation : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector rotate_euler : Stacked method 
    """

    def __init__(self, rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None):

        super().__init__('FunctionNodeRotateEuler', name='Rotate Euler', label=label)
        # Parameters

        self.bnode.space           = space

        # Input sockets

        self.plug(0, rotation)
        self.plug(1, rotate_by)
        self.plug(2, axis)
        self.plug(3, angle)

        # Output sockets

        self.rotation        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'rotation': self.rotation}

    @property
    def space(self):
        return self.bnode.space

    @space.setter
    def space(self, value):
        self.bnode.space = value

# ----------------------------------------------------------------------------------------------------
# Node SliceString for FunctionNodeSliceString

class SliceString(Node):

    """Class SliceString
    

    | Geometry node name: 'Slice String' 
    | Blender type:  FunctionNodeSliceString 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SliceString(string=None, position=None, length=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - string   : String 
            - position : Integer 
            - length   : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - string : String 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - String slice : Method 
    """

    def __init__(self, string=None, position=None, length=None, label=None):

        super().__init__('FunctionNodeSliceString', name='Slice String', label=label)
        # Input sockets

        self.plug(0, string)
        self.plug(1, position)
        self.plug(2, length)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = {'string': self.string}

# ----------------------------------------------------------------------------------------------------
# Node StringLength for FunctionNodeStringLength

class StringLength(Node):

    """Class StringLength
    

    | Geometry node name: 'String Length' 
    | Blender type:  FunctionNodeStringLength 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.StringLength(string=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - string : String 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - length : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - String length : Property 
    """

    def __init__(self, string=None, label=None):

        super().__init__('FunctionNodeStringLength', name='String Length', label=label)
        # Input sockets

        self.plug(0, string)

        # Output sockets

        self.length          = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'length': self.length}

# ----------------------------------------------------------------------------------------------------
# Node ValueToString for FunctionNodeValueToString

class ValueToString(Node):

    """Class ValueToString
    

    | Geometry node name: 'Value to String' 
    | Blender type:  FunctionNodeValueToString 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ValueToString(value=None, decimals=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - value    : Float 
            - decimals : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - string : String 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float to_string : Method 
    """

    def __init__(self, value=None, decimals=None, label=None):

        super().__init__('FunctionNodeValueToString', name='Value to String', label=label)
        # Input sockets

        self.plug(0, value)
        self.plug(1, decimals)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = {'string': self.string}

# ----------------------------------------------------------------------------------------------------
# Node AccumulateField for GeometryNodeAccumulateField

class AccumulateField(Node):

    """Class AccumulateField
    

    | Geometry node name: 'Accumulate Field' 
    | Blender type:  GeometryNodeAccumulateField 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.AccumulateField(value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - value       : data_type dependant 
            - group_index : Integer 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR') 
            - domain    : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR') 
    - Input sockets     : value 
    - Output sockets    : leading trailing total 
    

    Output sockets
    ==============
    - leading  : data_type dependant 
    - trailing : data_type dependant 
    - total    : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float accumulate_field   : Method 
    - Integer accumulate_field : Method 
    - Vector accumulate_field  : Method 
    """

    def __init__(self, value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeAccumulateField', name='Accumulate Field', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, value)
        elif data_type == 'INT':
            self.plug(2, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(0, value)

        self.plug(3, group_index)

        # Output sockets

        if data_type == 'FLOAT':
            self.leading         = self.Float(self.bnode.outputs[1])
            self.trailing        = self.Float(self.bnode.outputs[4])
            self.total           = self.Float(self.bnode.outputs[7])
        elif data_type == 'INT':
            self.leading         = self.Integer(self.bnode.outputs[2])
            self.trailing        = self.Integer(self.bnode.outputs[5])
            self.total           = self.Integer(self.bnode.outputs[8])
        elif data_type == 'FLOAT_VECTOR':
            self.leading         = self.Vector(self.bnode.outputs[0])
            self.trailing        = self.Vector(self.bnode.outputs[3])
            self.total           = self.Vector(self.bnode.outputs[6])

        self.output_sockets  = {'leading': self.leading, 'trailing': self.trailing, 'total': self.total}

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

    """Class DomainSize
    

    | Geometry node name: 'Domain Size' 
    | Blender type:  GeometryNodeAttributeDomainSize 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.DomainSize(geometry=None, component='MESH', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
    

            Parameters
            ----------
            - component : 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - point_count       : Integer 
    - edge_count        : Integer 
    - face_count        : Integer 
    - face_corner_count : Integer 
    - spline_count      : Integer 
    - instance_count    : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry attribute_domain_size : Method 
    """

    def __init__(self, geometry=None, component='MESH', label=None):

        super().__init__('GeometryNodeAttributeDomainSize', name='Domain Size', label=label)
        # Parameters

        self.bnode.component       = component

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.point_count     = self.Integer(self.bnode.outputs[0])
        self.edge_count      = self.Integer(self.bnode.outputs[1])
        self.face_count      = self.Integer(self.bnode.outputs[2])
        self.face_corner_count = self.Integer(self.bnode.outputs[3])
        self.spline_count    = self.Integer(self.bnode.outputs[4])
        self.instance_count  = self.Integer(self.bnode.outputs[5])
        self.output_sockets  = {'point_count': self.point_count, 'edge_count': self.edge_count, 'face_count': self.face_count, 'face_corner_count': self.face_corner_count, 'spline_count': self.spline_count, 'instance_count': self.instance_count}

    @property
    def component(self):
        return self.bnode.component

    @component.setter
    def component(self, value):
        self.bnode.component = value

# ----------------------------------------------------------------------------------------------------
# Node AttributeRemove for GeometryNodeAttributeRemove

class AttributeRemove(Node):

    """Class AttributeRemove
    

    | Geometry node name: 'Attribute Remove' 
    | Blender type:  GeometryNodeAttributeRemove 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.AttributeRemove(*attribute, geometry=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - attribute : * String 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry attribute_remove : Method 
    """

    def __init__(self, *attribute, geometry=None, label=None):

        super().__init__('GeometryNodeAttributeRemove', name='Attribute Remove', label=label)
        # Input sockets

        self.plug(1, *attribute)
        self.plug(0, geometry)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node AttributeStatistic for GeometryNodeAttributeStatistic

class AttributeStatistic(Node):

    """Class AttributeStatistic
    

    | Geometry node name: 'Attribute Statistic' 
    | Blender type:  GeometryNodeAttributeStatistic 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - attribute : data_type dependant 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR') 
            - domain    : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR') 
    - Input sockets     : attribute 
    - Output sockets    : mean median sum min max range standard_deviation variance 
    

    Output sockets
    ==============
    - mean               : data_type dependant 
    - median             : data_type dependant 
    - sum                : data_type dependant 
    - min                : data_type dependant 
    - max                : data_type dependant 
    - range              : data_type dependant 
    - standard_deviation : data_type dependant 
    - variance           : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float attribute_statistic  : Method 
    - Vector attribute_statistic : Method 
    """

    def __init__(self, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeAttributeStatistic', name='Attribute Statistic', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, attribute)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(3, attribute)

        self.plug(0, geometry)
        self.plug(1, selection)

        # Output sockets

        if data_type == 'FLOAT':
            self.mean            = self.Float(self.bnode.outputs[0])
            self.median          = self.Float(self.bnode.outputs[1])
            self.sum             = self.Float(self.bnode.outputs[2])
            self.min             = self.Float(self.bnode.outputs[3])
            self.max             = self.Float(self.bnode.outputs[4])
            self.range           = self.Float(self.bnode.outputs[5])
            self.standard_deviation = self.Float(self.bnode.outputs[6])
            self.variance        = self.Float(self.bnode.outputs[7])
        elif data_type == 'FLOAT_VECTOR':
            self.mean            = self.Vector(self.bnode.outputs[8])
            self.median          = self.Vector(self.bnode.outputs[9])
            self.sum             = self.Vector(self.bnode.outputs[10])
            self.min             = self.Vector(self.bnode.outputs[11])
            self.max             = self.Vector(self.bnode.outputs[12])
            self.range           = self.Vector(self.bnode.outputs[13])
            self.standard_deviation = self.Vector(self.bnode.outputs[14])
            self.variance        = self.Vector(self.bnode.outputs[15])

        self.output_sockets  = {'mean': self.mean, 'median': self.median, 'sum': self.sum, 'min': self.min, 'max': self.max, 'range': self.range, 'standard_deviation': self.standard_deviation, 'variance': self.variance}

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

    """Class TransferAttribute
    

    | Geometry node name: 'Transfer Attribute' 
    | Blender type:  GeometryNodeAttributeTransfer 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.TransferAttribute(source=None, attribute=None, source_position=None, index=None, data_type='FLOAT',
        domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - source          : Geometry 
            - attribute       : data_type dependant 
            - source_position : Vector 
            - index           : Integer 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
            - domain    : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
            - mapping   : 'NEAREST_FACE_INTERPOLATED' in ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
    - Input sockets     : attribute 
    - Output sockets    : attribute 
    

    Output sockets
    ==============
    - attribute : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean transfer_attribute : Method 
    - Color transfer_attribute   : Method 
    - Float transfer_attribute   : Method 
    - Geometry transfer_boolean  : Method 
    - Geometry transfer_color    : Method 
    - Geometry transfer_float    : Method 
    - Geometry transfer_integer  : Method 
    - Geometry transfer_vector   : Method 
    - Integer transfer_attribute : Method 
    - Vector transfer_attribute  : Method 
    """

    def __init__(self, source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None):

        super().__init__('GeometryNodeAttributeTransfer', name='Transfer Attribute', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain
        self.bnode.mapping         = mapping

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, attribute)
        elif data_type == 'INT':
            self.plug(5, attribute)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(1, attribute)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, attribute)
        elif data_type == 'BOOLEAN':
            self.plug(4, attribute)

        self.plug(0, source)
        self.plug(6, source_position)
        self.plug(7, index)

        # Output sockets

        if data_type == 'FLOAT':
            self.attribute       = self.Float(self.bnode.outputs[1])
        elif data_type == 'INT':
            self.attribute       = self.Integer(self.bnode.outputs[4])
        elif data_type == 'FLOAT_VECTOR':
            self.attribute       = self.Vector(self.bnode.outputs[0])
        elif data_type == 'FLOAT_COLOR':
            self.attribute       = self.Color(self.bnode.outputs[2])
        elif data_type == 'BOOLEAN':
            self.attribute       = self.Boolean(self.bnode.outputs[3])

        self.output_sockets  = {'attribute': self.attribute}

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

    """Class BoundingBox
    

    | Geometry node name: 'Bounding Box' 
    | Blender type:  GeometryNodeBoundBox 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.BoundingBox(geometry=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - bounding_box : Geometry 
    - min          : Vector 
    - max          : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry bound_box : Property 
    """

    def __init__(self, geometry=None, label=None):

        super().__init__('GeometryNodeBoundBox', name='Bounding Box', label=label)
        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.bounding_box    = self.Geometry(self.bnode.outputs[0])
        self.min             = self.Vector(self.bnode.outputs[1])
        self.max             = self.Vector(self.bnode.outputs[2])
        self.output_sockets  = {'bounding_box': self.bounding_box, 'min': self.min, 'max': self.max}

# ----------------------------------------------------------------------------------------------------
# Node CaptureAttribute for GeometryNodeCaptureAttribute

class CaptureAttribute(Node):

    """Class CaptureAttribute
    

    | Geometry node name: 'Capture Attribute' 
    | Blender type:  GeometryNodeCaptureAttribute 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
            - value    : data_type dependant 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
            - domain    : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
    - Input sockets     : value 
    - Output sockets    : attribute 
    

    Output sockets
    ==============
    - geometry  : Geometry 
    - attribute : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean capture_attribute : Method 
    - Color capture_attribute   : Method 
    - Float capture_attribute   : Method 
    - Integer capture_attribute : Method 
    - Vector capture_attribute  : Method 
    """

    def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeCaptureAttribute', name='Capture Attribute', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, value)
        elif data_type == 'INT':
            self.plug(5, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(1, value)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, value)
        elif data_type == 'BOOLEAN':
            self.plug(4, value)

        self.plug(0, geometry)

        # Output sockets

        if data_type == 'FLOAT':
            self.attribute       = self.Float(self.bnode.outputs[2])
        elif data_type == 'INT':
            self.attribute       = self.Integer(self.bnode.outputs[5])
        elif data_type == 'FLOAT_VECTOR':
            self.attribute       = self.Vector(self.bnode.outputs[1])
        elif data_type == 'FLOAT_COLOR':
            self.attribute       = self.Color(self.bnode.outputs[3])
        elif data_type == 'BOOLEAN':
            self.attribute       = self.Boolean(self.bnode.outputs[4])

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry, 'attribute': self.attribute}

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

    """Class CollectionInfo
    

    | Geometry node name: 'Collection Info' 
    | Blender type:  GeometryNodeCollectionInfo 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - collection        : Collection 
            - separate_children : Boolean 
            - reset_children    : Boolean 
    

            Parameters
            ----------
            - transform_space : 'ORIGINAL' in ('ORIGINAL', 'RELATIVE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Collection info : Method 
    """

    def __init__(self, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None):

        super().__init__('GeometryNodeCollectionInfo', name='Collection Info', label=label)
        # Parameters

        self.bnode.transform_space = transform_space

        # Input sockets

        self.plug(0, collection)
        self.plug(1, separate_children)
        self.plug(2, reset_children)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

    @property
    def transform_space(self):
        return self.bnode.transform_space

    @transform_space.setter
    def transform_space(self, value):
        self.bnode.transform_space = value

# ----------------------------------------------------------------------------------------------------
# Node ConvexHull for GeometryNodeConvexHull

class ConvexHull(Node):

    """Class ConvexHull
    

    | Geometry node name: 'Convex Hull' 
    | Blender type:  GeometryNodeConvexHull 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ConvexHull(geometry=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - convex_hull : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry convex_hull : Method 
    """

    def __init__(self, geometry=None, label=None):

        super().__init__('GeometryNodeConvexHull', name='Convex Hull', label=label)
        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.convex_hull     = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'convex_hull': self.convex_hull}

# ----------------------------------------------------------------------------------------------------
# Node Arc for GeometryNodeCurveArc

class Arc(Node):

    """Class Arc
    

    | Geometry node name: 'Arc' 
    | Blender type:  GeometryNodeCurveArc 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Arc(resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None,
        offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - resolution     : Integer 
            - start          : Vector 
            - middle         : Vector 
            - end            : Vector 
            - radius         : Float 
            - start_angle    : Float 
            - sweep_angle    : Float 
            - offset_angle   : Float 
            - connect_center : Boolean 
            - invert_arc     : Boolean 
    

            Parameters
            ----------
            - mode : 'RADIUS' in ('POINTS', 'RADIUS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve  : Curve 
    - center : Vector 
    - normal : Vector 
    - radius : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve ArcFromPoints : Static method 
    - Curve ArcFromRadius : Constructor 
    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None):

        super().__init__('GeometryNodeCurveArc', name='Arc', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, start)
        self.plug(2, middle)
        self.plug(3, end)
        self.plug(4, radius)
        self.plug(5, start_angle)
        self.plug(6, sweep_angle)
        self.plug(7, offset_angle)
        self.plug(8, connect_center)
        self.plug(9, invert_arc)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.center          = self.Vector(self.bnode.outputs[1])
        self.normal          = self.Vector(self.bnode.outputs[2])
        self.radius          = self.Float(self.bnode.outputs[3])
        self.output_sockets  = {'curve': self.curve, 'center': self.center, 'normal': self.normal, 'radius': self.radius}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node EndpointSelection for GeometryNodeCurveEndpointSelection

class EndpointSelection(Node):

    """Class EndpointSelection
    

    | Geometry node name: 'Endpoint Selection' 
    | Blender type:  GeometryNodeCurveEndpointSelection 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.EndpointSelection(start_size=None, end_size=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - start_size : Integer 
            - end_size   : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - selection : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_endpoint_selection : Capture attribute 
    - Spline endpoint_selection         : Attribute 
    """

    def __init__(self, start_size=None, end_size=None, label=None):

        super().__init__('GeometryNodeCurveEndpointSelection', name='Endpoint Selection', label=label)
        # Input sockets

        self.plug(0, start_size)
        self.plug(1, end_size)

        # Output sockets

        self.selection       = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'selection': self.selection}

# ----------------------------------------------------------------------------------------------------
# Node HandleTypeSelection for GeometryNodeCurveHandleTypeSelection

class HandleTypeSelection(Node):

    """Class HandleTypeSelection
    

    | Geometry node name: 'Handle Type Selection' 
    | Blender type:  GeometryNodeCurveHandleTypeSelection 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None) 
    

        Arguments
        ---------
    

            Parameters
            ----------
            - handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN') 
            - mode        : {'LEFT', 'RIGHT'} set 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - selection : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_handle_type_selection : Capture attribute 
    - Spline handle_type_selection         : Attribute 
    """

    def __init__(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None):

        super().__init__('GeometryNodeCurveHandleTypeSelection', name='Handle Type Selection', label=label)
        # Parameters

        self.bnode.handle_type     = handle_type
        self.bnode.mode            = mode

        # Output sockets

        self.selection       = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'selection': self.selection}

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

    """Class CurveLength
    

    | Geometry node name: 'Curve Length' 
    | Blender type:  GeometryNodeCurveLength 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveLength(curve=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve : Curve 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - length : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve length : Method 
    """

    def __init__(self, curve=None, label=None):

        super().__init__('GeometryNodeCurveLength', name='Curve Length', label=label)
        # Input sockets

        self.plug(0, curve)

        # Output sockets

        self.length          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'length': self.length}

# ----------------------------------------------------------------------------------------------------
# Node BezierSegment for GeometryNodeCurvePrimitiveBezierSegment

class BezierSegment(Node):

    """Class BezierSegment
    

    | Geometry node name: 'Bezier Segment' 
    | Blender type:  GeometryNodeCurvePrimitiveBezierSegment 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None,
        mode='POSITION', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - resolution   : Integer 
            - start        : Vector 
            - start_handle : Vector 
            - end_handle   : Vector 
            - end          : Vector 
    

            Parameters
            ----------
            - mode : 'POSITION' in ('POSITION', 'OFFSET') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve BezierSegment : Constructor 
    """

    def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None):

        super().__init__('GeometryNodeCurvePrimitiveBezierSegment', name='Bezier Segment', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, start)
        self.plug(2, start_handle)
        self.plug(3, end_handle)
        self.plug(4, end)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node CurveCircle for GeometryNodeCurvePrimitiveCircle

class CurveCircle(Node):

    """Class CurveCircle
    

    | Geometry node name: 'Curve Circle' 
    | Blender type:  GeometryNodeCurvePrimitiveCircle 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveCircle(resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - resolution : Integer 
            - point_1    : Vector 
            - point_2    : Vector 
            - point_3    : Vector 
            - radius     : Float 
    

            Parameters
            ----------
            - mode : 'RADIUS' in ('POINTS', 'RADIUS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve  : Curve 
    - center : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve Circle : Constructor 
    """

    def __init__(self, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None):

        super().__init__('GeometryNodeCurvePrimitiveCircle', name='Curve Circle', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, point_1)
        self.plug(2, point_2)
        self.plug(3, point_3)
        self.plug(4, radius)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.center          = self.Vector(self.bnode.outputs[1])
        self.output_sockets  = {'curve': self.curve, 'center': self.center}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node CurveLine for GeometryNodeCurvePrimitiveLine

class CurveLine(Node):

    """Class CurveLine
    

    | Geometry node name: 'Curve Line' 
    | Blender type:  GeometryNodeCurvePrimitiveLine 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - start     : Vector 
            - end       : Vector 
            - direction : Vector 
            - length    : Float 
    

            Parameters
            ----------
            - mode : 'POINTS' in ('POINTS', 'DIRECTION') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve Line : Constructor 
    """

    def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS', label=None):

        super().__init__('GeometryNodeCurvePrimitiveLine', name='Curve Line', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, start)
        self.plug(1, end)
        self.plug(2, direction)
        self.plug(3, length)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node Quadrilateral for GeometryNodeCurvePrimitiveQuadrilateral

class Quadrilateral(Node):

    """Class Quadrilateral
    

    | Geometry node name: 'Quadrilateral' 
    | Blender type:  GeometryNodeCurvePrimitiveQuadrilateral 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Quadrilateral(width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None,
        top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - width         : Float 
            - height        : Float 
            - bottom_width  : Float 
            - top_width     : Float 
            - offset        : Float 
            - bottom_height : Float 
            - top_height    : Float 
            - point_1       : Vector 
            - point_2       : Vector 
            - point_3       : Vector 
            - point_4       : Vector 
    

            Parameters
            ----------
            - mode : 'RECTANGLE' in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve Quadrilateral : Constructor 
    """

    def __init__(self, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None):

        super().__init__('GeometryNodeCurvePrimitiveQuadrilateral', name='Quadrilateral', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, width)
        self.plug(1, height)
        self.plug(2, bottom_width)
        self.plug(3, top_width)
        self.plug(4, offset)
        self.plug(5, bottom_height)
        self.plug(6, top_height)
        self.plug(7, point_1)
        self.plug(8, point_2)
        self.plug(9, point_3)
        self.plug(10, point_4)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node QuadraticBezier for GeometryNodeCurveQuadraticBezier

class QuadraticBezier(Node):

    """Class QuadraticBezier
    

    | Geometry node name: 'Quadratic Bezier' 
    | Blender type:  GeometryNodeCurveQuadraticBezier 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.QuadraticBezier(resolution=None, start=None, middle=None, end=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - resolution : Integer 
            - start      : Vector 
            - middle     : Vector 
            - end        : Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve QuadraticBezier : Constructor 
    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, label=None):

        super().__init__('GeometryNodeCurveQuadraticBezier', name='Quadratic Bezier', label=label)
        # Input sockets

        self.plug(0, resolution)
        self.plug(1, start)
        self.plug(2, middle)
        self.plug(3, end)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node SetHandleType for GeometryNodeCurveSetHandles

class SetHandleType(Node):

    """Class SetHandleType
    

    | Geometry node name: 'Set Handle Type' 
    | Blender type:  GeometryNodeCurveSetHandles 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
    

            Parameters
            ----------
            - handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN') 
            - mode        : {'LEFT', 'RIGHT'} set 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve set_handles : Stacked method 
    """

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None):

        super().__init__('GeometryNodeCurveSetHandles', name='Set Handle Type', label=label)
        # Parameters

        self.bnode.handle_type     = handle_type
        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

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

    """Class Spiral
    

    | Geometry node name: 'Spiral' 
    | Blender type:  GeometryNodeCurveSpiral 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None,
        reverse=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - resolution   : Integer 
            - rotations    : Float 
            - start_radius : Float 
            - end_radius   : Float 
            - height       : Float 
            - reverse      : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve Spiral : Constructor 
    """

    def __init__(self, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None):

        super().__init__('GeometryNodeCurveSpiral', name='Spiral', label=label)
        # Input sockets

        self.plug(0, resolution)
        self.plug(1, rotations)
        self.plug(2, start_radius)
        self.plug(3, end_radius)
        self.plug(4, height)
        self.plug(5, reverse)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node SetSplineType for GeometryNodeCurveSplineType

class SetSplineType(Node):

    """Class SetSplineType
    

    | Geometry node name: 'Set Spline Type' 
    | Blender type:  GeometryNodeCurveSplineType 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetSplineType(curve=None, selection=None, spline_type='POLY', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
    

            Parameters
            ----------
            - spline_type : 'POLY' in ('BEZIER', 'NURBS', 'POLY') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve set_spline_type : Stacked method 
    """

    def __init__(self, curve=None, selection=None, spline_type='POLY', label=None):

        super().__init__('GeometryNodeCurveSplineType', name='Set Spline Type', label=label)
        # Parameters

        self.bnode.spline_type     = spline_type

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def spline_type(self):
        return self.bnode.spline_type

    @spline_type.setter
    def spline_type(self, value):
        self.bnode.spline_type = value

# ----------------------------------------------------------------------------------------------------
# Node Star for GeometryNodeCurveStar

class Star(Node):

    """Class Star
    

    | Geometry node name: 'Star' 
    | Blender type:  GeometryNodeCurveStar 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - points       : Integer 
            - inner_radius : Float 
            - outer_radius : Float 
            - twist        : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve        : Curve 
    - outer_points : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve Star : Constructor 
    """

    def __init__(self, points=None, inner_radius=None, outer_radius=None, twist=None, label=None):

        super().__init__('GeometryNodeCurveStar', name='Star', label=label)
        # Input sockets

        self.plug(0, points)
        self.plug(1, inner_radius)
        self.plug(2, outer_radius)
        self.plug(3, twist)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.outer_points    = self.Boolean(self.bnode.outputs[1])
        self.output_sockets  = {'curve': self.curve, 'outer_points': self.outer_points}

# ----------------------------------------------------------------------------------------------------
# Node CurveToMesh for GeometryNodeCurveToMesh

class CurveToMesh(Node):

    """Class CurveToMesh
    

    | Geometry node name: 'Curve to Mesh' 
    | Blender type:  GeometryNodeCurveToMesh 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveToMesh(curve=None, profile_curve=None, fill_caps=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve         : Curve 
            - profile_curve : Geometry 
            - fill_caps     : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve to_mesh : Method 
    """

    def __init__(self, curve=None, profile_curve=None, fill_caps=None, label=None):

        super().__init__('GeometryNodeCurveToMesh', name='Curve to Mesh', label=label)
        # Input sockets

        self.plug(0, curve)
        self.plug(1, profile_curve)
        self.plug(2, fill_caps)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node CurveToPoints for GeometryNodeCurveToPoints

class CurveToPoints(Node):

    """Class CurveToPoints
    

    | Geometry node name: 'Curve to Points' 
    | Blender type:  GeometryNodeCurveToPoints 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveToPoints(curve=None, count=None, length=None, mode='COUNT', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve  : Curve 
            - count  : Integer 
            - length : Float 
    

            Parameters
            ----------
            - mode : 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - points   : Points 
    - tangent  : Vector 
    - normal   : Vector 
    - rotation : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve to_points : Method 
    """

    def __init__(self, curve=None, count=None, length=None, mode='COUNT', label=None):

        super().__init__('GeometryNodeCurveToPoints', name='Curve to Points', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, count)
        self.plug(2, length)

        # Output sockets

        self.points          = self.Points(self.bnode.outputs[0])
        self.tangent         = self.Vector(self.bnode.outputs[1])
        self.normal          = self.Vector(self.bnode.outputs[2])
        self.rotation        = self.Vector(self.bnode.outputs[3])
        self.output_sockets  = {'points': self.points, 'tangent': self.tangent, 'normal': self.normal, 'rotation': self.rotation}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node DeleteGeometry for GeometryNodeDeleteGeometry

class DeleteGeometry(Node):

    """Class DeleteGeometry
    

    | Geometry node name: 'Delete Geometry' 
    | Blender type:  GeometryNodeDeleteGeometry 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
    

            Parameters
            ----------
            - domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE') 
            - mode   : 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry delete_geometry : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL', label=None):

        super().__init__('GeometryNodeDeleteGeometry', name='Delete Geometry', label=label)
        # Parameters

        self.bnode.domain          = domain
        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

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

    """Class DistributePointsOnFaces
    

    | Geometry node name: 'Distribute Points on Faces' 
    | Blender type:  GeometryNodeDistributePointsOnFaces 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None,
        density_factor=None, seed=None, distribute_method='RANDOM', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh           : Mesh 
            - selection      : Boolean 
            - distance_min   : Float 
            - density_max    : Float 
            - density        : Float 
            - density_factor : Float 
            - seed           : Integer 
    

            Parameters
            ----------
            - distribute_method : 'RANDOM' in ('RANDOM', 'POISSON') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - points   : Points 
    - normal   : Vector 
    - rotation : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh distribute_points_on_faces : Method 
    """

    def __init__(self, mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None):

        super().__init__('GeometryNodeDistributePointsOnFaces', name='Distribute Points on Faces', label=label)
        # Parameters

        self.bnode.distribute_method = distribute_method

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, distance_min)
        self.plug(3, density_max)
        self.plug(4, density)
        self.plug(5, density_factor)
        self.plug(6, seed)

        # Output sockets

        self.points          = self.Points(self.bnode.outputs[0])
        self.normal          = self.Vector(self.bnode.outputs[1])
        self.rotation        = self.Vector(self.bnode.outputs[2])
        self.output_sockets  = {'points': self.points, 'normal': self.normal, 'rotation': self.rotation}

    @property
    def distribute_method(self):
        return self.bnode.distribute_method

    @distribute_method.setter
    def distribute_method(self, value):
        self.bnode.distribute_method = value

# ----------------------------------------------------------------------------------------------------
# Node DualMesh for GeometryNodeDualMesh

class DualMesh(Node):

    """Class DualMesh
    

    | Geometry node name: 'Dual Mesh' 
    | Blender type:  GeometryNodeDualMesh 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.DualMesh(mesh=None, keep_boundaries=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh            : Mesh 
            - keep_boundaries : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - dual_mesh : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh dual : Stacked method 
    """

    def __init__(self, mesh=None, keep_boundaries=None, label=None):

        super().__init__('GeometryNodeDualMesh', name='Dual Mesh', label=label)
        # Input sockets

        self.plug(0, mesh)
        self.plug(1, keep_boundaries)

        # Output sockets

        self.dual_mesh       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'dual_mesh': self.dual_mesh}

# ----------------------------------------------------------------------------------------------------
# Node ExtrudeMesh for GeometryNodeExtrudeMesh

class ExtrudeMesh(Node):

    """Class ExtrudeMesh
    

    | Geometry node name: 'Extrude Mesh' 
    | Blender type:  GeometryNodeExtrudeMesh 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh         : Mesh 
            - selection    : Boolean 
            - offset       : Vector 
            - offset_scale : Float 
            - individual   : Boolean 
    

            Parameters
            ----------
            - mode : 'FACES' in ('VERTICES', 'EDGES', 'FACES') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    - top  : Boolean 
    - side : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh extrude : Method 
    """

    def __init__(self, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None):

        super().__init__('GeometryNodeExtrudeMesh', name='Extrude Mesh', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, offset)
        self.plug(3, offset_scale)
        self.plug(4, individual)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.top             = self.Boolean(self.bnode.outputs[1])
        self.side            = self.Boolean(self.bnode.outputs[2])
        self.output_sockets  = {'mesh': self.mesh, 'top': self.top, 'side': self.side}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node FieldAtIndex for GeometryNodeFieldAtIndex

class FieldAtIndex(Node):

    """Class FieldAtIndex
    

    | Geometry node name: 'Field at Index' 
    | Blender type:  GeometryNodeFieldAtIndex 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - index : Integer 
            - value : data_type dependant 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
            - domain    : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
    - Input sockets     : value 
    - Output sockets    : value 
    

    Output sockets
    ==============
    - value : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean field_at_index : Method 
    - Color field_at_index   : Method 
    - Float field_at_index   : Method 
    - Integer field_at_index : Method 
    - Vector field_at_index  : Method 
    """

    def __init__(self, index=None, value=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeFieldAtIndex', name='Field at Index', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, value)
        elif data_type == 'INT':
            self.plug(2, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(3, value)
        elif data_type == 'FLOAT_COLOR':
            self.plug(4, value)
        elif data_type == 'BOOLEAN':
            self.plug(5, value)

        self.plug(0, index)

        # Output sockets

        if data_type == 'FLOAT':
            self.value           = self.Float(self.bnode.outputs[0])
        elif data_type == 'INT':
            self.value           = self.Integer(self.bnode.outputs[1])
        elif data_type == 'FLOAT_VECTOR':
            self.value           = self.Vector(self.bnode.outputs[2])
        elif data_type == 'FLOAT_COLOR':
            self.value           = self.Color(self.bnode.outputs[3])
        elif data_type == 'BOOLEAN':
            self.value           = self.Boolean(self.bnode.outputs[4])

        self.output_sockets  = {'value': self.value}

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

    """Class FillCurve
    

    | Geometry node name: 'Fill Curve' 
    | Blender type:  GeometryNodeFillCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FillCurve(curve=None, mode='TRIANGLES', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve : Curve 
    

            Parameters
            ----------
            - mode : 'TRIANGLES' in ('TRIANGLES', 'NGONS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve fill : Stacked method 
    """

    def __init__(self, curve=None, mode='TRIANGLES', label=None):

        super().__init__('GeometryNodeFillCurve', name='Fill Curve', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node FilletCurve for GeometryNodeFilletCurve

class FilletCurve(Node):

    """Class FilletCurve
    

    | Geometry node name: 'Fillet Curve' 
    | Blender type:  GeometryNodeFilletCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve        : Curve 
            - count        : Integer 
            - radius       : Float 
            - limit_radius : Boolean 
    

            Parameters
            ----------
            - mode : 'BEZIER' in ('BEZIER', 'POLY') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve fillet : Stacked method 
    """

    def __init__(self, curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None):

        super().__init__('GeometryNodeFilletCurve', name='Fillet Curve', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, count)
        self.plug(2, radius)
        self.plug(3, limit_radius)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node FlipFaces for GeometryNodeFlipFaces

class FlipFaces(Node):

    """Class FlipFaces
    

    | Geometry node name: 'Flip Faces' 
    | Blender type:  GeometryNodeFlipFaces 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FlipFaces(mesh=None, selection=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh      : Mesh 
            - selection : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh flip_faces : Stacked method 
    """

    def __init__(self, mesh=None, selection=None, label=None):

        super().__init__('GeometryNodeFlipFaces', name='Flip Faces', label=label)
        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node GeometryToInstance for GeometryNodeGeometryToInstance

class GeometryToInstance(Node):

    """Class GeometryToInstance
    

    | Geometry node name: 'Geometry to Instance' 
    | Blender type:  GeometryNodeGeometryToInstance 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.GeometryToInstance(*geometry, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : * Geometry 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - instances : Instances 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry to_instance : Method 
    """

    def __init__(self, *geometry, label=None):

        super().__init__('GeometryNodeGeometryToInstance', name='Geometry to Instance', label=label)
        # Input sockets

        self.plug(0, *geometry)

        # Output sockets

        self.instances       = self.Instances(self.bnode.outputs[0])
        self.output_sockets  = {'instances': self.instances}

# ----------------------------------------------------------------------------------------------------
# Node Group for GeometryNodeGroup

class Group(Node):

    """Class Group
    

    | Geometry node name: 'Group' 
    | Blender type:  GeometryNodeGroup 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Group(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeGroup', name='Group', label=label)
        self.output_sockets  = {}

# ----------------------------------------------------------------------------------------------------
# Node ImageTexture for GeometryNodeImageTexture

class ImageTexture(Node):

    """Class ImageTexture
    

    | Geometry node name: 'Image Texture' 
    | Blender type:  GeometryNodeImageTexture 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - image  : Image 
            - vector : Vector 
            - frame  : Integer 
    

            Parameters
            ----------
            - extension     : 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP') 
            - interpolation : 'Linear' in ('Linear', 'Closest', 'Cubic') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - alpha : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Image : Static method 
    """

    def __init__(self, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None):

        super().__init__('GeometryNodeImageTexture', name='Image Texture', label=label)
        # Parameters

        self.bnode.extension       = extension
        self.bnode.interpolation   = interpolation

        # Input sockets

        self.plug(0, image)
        self.plug(1, vector)
        self.plug(2, frame)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.alpha           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'alpha': self.alpha}

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

    """Class CurveHandlePositions
    

    | Geometry node name: 'Curve Handle Positions' 
    | Blender type:  GeometryNodeInputCurveHandlePositions 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveHandlePositions(relative=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - relative : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - left  : Vector 
    - right : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_handle_positions : Capture attribute 
    - Spline left_handle_position     : Attribute 
    - Spline right_handle_position    : Attribute 
    """

    def __init__(self, relative=None, label=None):

        super().__init__('GeometryNodeInputCurveHandlePositions', name='Curve Handle Positions', label=label)
        # Input sockets

        self.plug(0, relative)

        # Output sockets

        self.left            = self.Vector(self.bnode.outputs[0])
        self.right           = self.Vector(self.bnode.outputs[1])
        self.output_sockets  = {'left': self.left, 'right': self.right}

# ----------------------------------------------------------------------------------------------------
# Node CurveTilt for GeometryNodeInputCurveTilt

class CurveTilt(Node):

    """Class CurveTilt
    

    | Geometry node name: 'Curve Tilt' 
    | Blender type:  GeometryNodeInputCurveTilt 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveTilt(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - tilt : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_tilt : Capture attribute 
    - Spline tilt         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputCurveTilt', name='Curve Tilt', label=label)
        # Output sockets

        self.tilt            = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'tilt': self.tilt}

# ----------------------------------------------------------------------------------------------------
# Node ID for GeometryNodeInputID

class ID(Node):

    """Class ID
    

    | Geometry node name: 'ID' 
    | Blender type:  GeometryNodeInputID 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ID(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - ID : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry ID         : Attribute 
    - Geometry capture_ID : Capture attribute 
    - Spline spline_ID    : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputID', name='ID', label=label)
        # Output sockets

        self.ID              = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'ID': self.ID}

# ----------------------------------------------------------------------------------------------------
# Node Index for GeometryNodeInputIndex

class Index(Node):

    """Class Index
    

    | Geometry node name: 'Index' 
    | Blender type:  GeometryNodeInputIndex 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Index(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - index : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry capture_index   : Capture attribute 
    - Geometry index           : Attribute 
    - Instances instance_index : Attribute 
    - Spline spline_index      : Attribute 
    - Spline spline_position   : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputIndex', name='Index', label=label)
        # Output sockets

        self.index           = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'index': self.index}

# ----------------------------------------------------------------------------------------------------
# Node Material for GeometryNodeInputMaterial

class Material(Node):

    """Class Material
    

    | Geometry node name: 'Material' 
    | Blender type:  GeometryNodeInputMaterial 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Material(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - material : Material 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMaterial', name='Material', label=label)
        # Output sockets

        self.material        = self.Material(self.bnode.outputs[0])
        self.output_sockets  = {'material': self.material}

# ----------------------------------------------------------------------------------------------------
# Node MaterialIndex for GeometryNodeInputMaterialIndex

class MaterialIndex(Node):

    """Class MaterialIndex
    

    | Geometry node name: 'Material Index' 
    | Blender type:  GeometryNodeInputMaterialIndex 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MaterialIndex(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - material_index : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_material_index : Capture attribute 
    - Mesh material_index         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMaterialIndex', name='Material Index', label=label)
        # Output sockets

        self.material_index  = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'material_index': self.material_index}

# ----------------------------------------------------------------------------------------------------
# Node EdgeAngle for GeometryNodeInputMeshEdgeAngle

class EdgeAngle(Node):

    """Class EdgeAngle
    

    | Geometry node name: 'Edge Angle' 
    | Blender type:  GeometryNodeInputMeshEdgeAngle 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.EdgeAngle(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - unsigned_angle : Float 
    - signed_angle   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_edge_angle  : Capture attribute 
    - Mesh corner_ID           : Attribute 
    - Mesh corner_index        : Attribute 
    - Mesh corner_porision     : Attribute 
    - Mesh edge_angle          : Attribute 
    - Mesh edge_unsigned_angle : Attribute 
    - Mesh egde_ID             : Attribute 
    - Mesh egde_index          : Attribute 
    - Mesh egde_position       : Attribute 
    - Mesh face_ID             : Attribute 
    - Mesh face_index          : Attribute 
    - Mesh face_position       : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeAngle', name='Edge Angle', label=label)
        # Output sockets

        self.unsigned_angle  = self.Float(self.bnode.outputs[0])
        self.signed_angle    = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'unsigned_angle': self.unsigned_angle, 'signed_angle': self.signed_angle}

# ----------------------------------------------------------------------------------------------------
# Node EdgeNeighbors for GeometryNodeInputMeshEdgeNeighbors

class EdgeNeighbors(Node):

    """Class EdgeNeighbors
    

    | Geometry node name: 'Edge Neighbors' 
    | Blender type:  GeometryNodeInputMeshEdgeNeighbors 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.EdgeNeighbors(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - face_count : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_edge_neighbors : Capture attribute 
    - Mesh edge_neighbors         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', name='Edge Neighbors', label=label)
        # Output sockets

        self.face_count      = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'face_count': self.face_count}

# ----------------------------------------------------------------------------------------------------
# Node EdgeVertices for GeometryNodeInputMeshEdgeVertices

class EdgeVertices(Node):

    """Class EdgeVertices
    

    | Geometry node name: 'Edge Vertices' 
    | Blender type:  GeometryNodeInputMeshEdgeVertices 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.EdgeVertices(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vertex_index_1 : Integer 
    - vertex_index_2 : Integer 
    - position_1     : Vector 
    - position_2     : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_edge_vertices   : Capture attribute 
    - Mesh edge_vertices_index1    : Attribute 
    - Mesh edge_vertices_index2    : Attribute 
    - Mesh edge_vertices_position1 : Attribute 
    - Mesh edge_vertices_position2 : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeVertices', name='Edge Vertices', label=label)
        # Output sockets

        self.vertex_index_1  = self.Integer(self.bnode.outputs[0])
        self.vertex_index_2  = self.Integer(self.bnode.outputs[1])
        self.position_1      = self.Vector(self.bnode.outputs[2])
        self.position_2      = self.Vector(self.bnode.outputs[3])
        self.output_sockets  = {'vertex_index_1': self.vertex_index_1, 'vertex_index_2': self.vertex_index_2, 'position_1': self.position_1, 'position_2': self.position_2}

# ----------------------------------------------------------------------------------------------------
# Node FaceArea for GeometryNodeInputMeshFaceArea

class FaceArea(Node):

    """Class FaceArea
    

    | Geometry node name: 'Face Area' 
    | Blender type:  GeometryNodeInputMeshFaceArea 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FaceArea(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - area : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_face_area : Capture attribute 
    - Mesh face_area         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshFaceArea', name='Face Area', label=label)
        # Output sockets

        self.area            = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'area': self.area}

# ----------------------------------------------------------------------------------------------------
# Node FaceNeighbors for GeometryNodeInputMeshFaceNeighbors

class FaceNeighbors(Node):

    """Class FaceNeighbors
    

    | Geometry node name: 'Face Neighbors' 
    | Blender type:  GeometryNodeInputMeshFaceNeighbors 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FaceNeighbors(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vertex_count : Integer 
    - face_count   : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_face_neighbors      : Capture attribute 
    - Mesh face_neighbors_face_count   : Attribute 
    - Mesh face_neighbors_vertex_count : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshFaceNeighbors', name='Face Neighbors', label=label)
        # Output sockets

        self.vertex_count    = self.Integer(self.bnode.outputs[0])
        self.face_count      = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = {'vertex_count': self.vertex_count, 'face_count': self.face_count}

# ----------------------------------------------------------------------------------------------------
# Node MeshIsland for GeometryNodeInputMeshIsland

class MeshIsland(Node):

    """Class MeshIsland
    

    | Geometry node name: 'Mesh Island' 
    | Blender type:  GeometryNodeInputMeshIsland 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MeshIsland(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - island_index : Integer 
    - island_count : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_island : Capture attribute 
    - Mesh island         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshIsland', name='Mesh Island', label=label)
        # Output sockets

        self.island_index    = self.Integer(self.bnode.outputs[0])
        self.island_count    = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = {'island_index': self.island_index, 'island_count': self.island_count}

# ----------------------------------------------------------------------------------------------------
# Node VertexNeighbors for GeometryNodeInputMeshVertexNeighbors

class VertexNeighbors(Node):

    """Class VertexNeighbors
    

    | Geometry node name: 'Vertex Neighbors' 
    | Blender type:  GeometryNodeInputMeshVertexNeighbors 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.VertexNeighbors(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vertex_count : Integer 
    - face_count   : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_vertex_neighbors      : Capture attribute 
    - Mesh vertex_neighbors_face_count   : Attribute 
    - Mesh vertex_neighbors_vertex_count : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshVertexNeighbors', name='Vertex Neighbors', label=label)
        # Output sockets

        self.vertex_count    = self.Integer(self.bnode.outputs[0])
        self.face_count      = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = {'vertex_count': self.vertex_count, 'face_count': self.face_count}

# ----------------------------------------------------------------------------------------------------
# Node Normal for GeometryNodeInputNormal

class Normal(Node):

    """Class Normal
    

    | Geometry node name: 'Normal' 
    | Blender type:  GeometryNodeInputNormal 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Normal(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - normal : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry capture_normal : Capture attribute 
    - Geometry normal         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputNormal', name='Normal', label=label)
        # Output sockets

        self.normal          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'normal': self.normal}

# ----------------------------------------------------------------------------------------------------
# Node Position for GeometryNodeInputPosition

class Position(Node):

    """Class Position
    

    | Geometry node name: 'Position' 
    | Blender type:  GeometryNodeInputPosition 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Position(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - position : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry capture_position : Capture attribute 
    - Geometry position         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputPosition', name='Position', label=label)
        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'position': self.position}

# ----------------------------------------------------------------------------------------------------
# Node Radius for GeometryNodeInputRadius

class Radius(Node):

    """Class Radius
    

    | Geometry node name: 'Radius' 
    | Blender type:  GeometryNodeInputRadius 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Radius(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - radius : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry capture_radius : Capture attribute 
    - Geometry radius         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputRadius', name='Radius', label=label)
        # Output sockets

        self.radius          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'radius': self.radius}

# ----------------------------------------------------------------------------------------------------
# Node SceneTime for GeometryNodeInputSceneTime

class SceneTime(Node):

    """Class SceneTime
    

    | Geometry node name: 'Scene Time' 
    | Blender type:  GeometryNodeInputSceneTime 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SceneTime(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - seconds : Float 
    - frame   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - functions scene : Function 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time', label=label)
        # Output sockets

        self.seconds         = self.Float(self.bnode.outputs[0])
        self.frame           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'seconds': self.seconds, 'frame': self.frame}

# ----------------------------------------------------------------------------------------------------
# Node IsShadeSmooth for GeometryNodeInputShadeSmooth

class IsShadeSmooth(Node):

    """Class IsShadeSmooth
    

    | Geometry node name: 'Is Shade Smooth' 
    | Blender type:  GeometryNodeInputShadeSmooth 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.IsShadeSmooth(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - smooth : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh capture_shade_smooth : Capture attribute 
    - Mesh shade_smooth         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputShadeSmooth', name='Is Shade Smooth', label=label)
        # Output sockets

        self.smooth          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'smooth': self.smooth}

# ----------------------------------------------------------------------------------------------------
# Node IsSplineCyclic for GeometryNodeInputSplineCyclic

class IsSplineCyclic(Node):

    """Class IsSplineCyclic
    

    | Geometry node name: 'Is Spline Cyclic' 
    | Blender type:  GeometryNodeInputSplineCyclic 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.IsSplineCyclic(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - cyclic : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_cyclic : Capture attribute 
    - Spline cyclic         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSplineCyclic', name='Is Spline Cyclic', label=label)
        # Output sockets

        self.cyclic          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'cyclic': self.cyclic}

# ----------------------------------------------------------------------------------------------------
# Node SplineResolution for GeometryNodeInputSplineResolution

class SplineResolution(Node):

    """Class SplineResolution
    

    | Geometry node name: 'Spline Resolution' 
    | Blender type:  GeometryNodeInputSplineResolution 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SplineResolution(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - resolution : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_resolution : Capture attribute 
    - Spline resolution         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSplineResolution', name='Spline Resolution', label=label)
        # Output sockets

        self.resolution      = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'resolution': self.resolution}

# ----------------------------------------------------------------------------------------------------
# Node CurveTangent for GeometryNodeInputTangent

class CurveTangent(Node):

    """Class CurveTangent
    

    | Geometry node name: 'Curve Tangent' 
    | Blender type:  GeometryNodeInputTangent 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CurveTangent(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - tangent : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_tangent : Capture attribute 
    - Spline tangent         : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputTangent', name='Curve Tangent', label=label)
        # Output sockets

        self.tangent         = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'tangent': self.tangent}

# ----------------------------------------------------------------------------------------------------
# Node InstanceOnPoints for GeometryNodeInstanceOnPoints

class InstanceOnPoints(Node):

    """Class InstanceOnPoints
    

    | Geometry node name: 'Instance on Points' 
    | Blender type:  GeometryNodeInstanceOnPoints 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None,
        rotation=None, scale=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - points         : Points 
            - selection      : Boolean 
            - instance       : Geometry 
            - pick_instance  : Boolean 
            - instance_index : Integer 
            - rotation       : Vector 
            - scale          : Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - instances : Instances 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Points instance_on_points : Method 
    """

    def __init__(self, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None):

        super().__init__('GeometryNodeInstanceOnPoints', name='Instance on Points', label=label)
        # Input sockets

        self.plug(0, points)
        self.plug(1, selection)
        self.plug(2, instance)
        self.plug(3, pick_instance)
        self.plug(4, instance_index)
        self.plug(5, rotation)
        self.plug(6, scale)

        # Output sockets

        self.instances       = self.Instances(self.bnode.outputs[0])
        self.output_sockets  = {'instances': self.instances}

# ----------------------------------------------------------------------------------------------------
# Node InstancesToPoints for GeometryNodeInstancesToPoints

class InstancesToPoints(Node):

    """Class InstancesToPoints
    

    | Geometry node name: 'Instances to Points' 
    | Blender type:  GeometryNodeInstancesToPoints 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.InstancesToPoints(instances=None, selection=None, position=None, radius=None, label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - instances : Instances 
            - selection : Boolean 
            - position  : Vector 
            - radius    : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - points : Points 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Instances to_points : Method 
    """

    def __init__(self, instances=None, selection=None, position=None, radius=None, label=None):

        super().__init__('GeometryNodeInstancesToPoints', name='Instances to Points', label=label)
        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, radius)

        # Output sockets

        self.points          = self.Points(self.bnode.outputs[0])
        self.output_sockets  = {'points': self.points}

# ----------------------------------------------------------------------------------------------------
# Node IsViewport for GeometryNodeIsViewport

class IsViewport(Node):

    """Class IsViewport
    

    | Geometry node name: 'Is Viewport' 
    | Blender type:  GeometryNodeIsViewport 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.IsViewport(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - is_viewport : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry is_viewport : Static method 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeIsViewport', name='Is Viewport', label=label)
        # Output sockets

        self.is_viewport     = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'is_viewport': self.is_viewport}

# ----------------------------------------------------------------------------------------------------
# Node JoinGeometry for GeometryNodeJoinGeometry

class JoinGeometry(Node):

    """Class JoinGeometry
    

    | Geometry node name: 'Join Geometry' 
    | Blender type:  GeometryNodeJoinGeometry 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.JoinGeometry(*geometry, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : * Geometry 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry join : Method 
    """

    def __init__(self, *geometry, label=None):

        super().__init__('GeometryNodeJoinGeometry', name='Join Geometry', label=label)
        # Input sockets

        self.plug(0, *geometry)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node MaterialSelection for GeometryNodeMaterialSelection

class MaterialSelection(Node):

    """Class MaterialSelection
    

    | Geometry node name: 'Material Selection' 
    | Blender type:  GeometryNodeMaterialSelection 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MaterialSelection(material=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - material : Material 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - selection : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Material selection              : Method 
    - Mesh capture_material_selection : Capture attribute 
    - Mesh material_selection         : Attribute 
    """

    def __init__(self, material=None, label=None):

        super().__init__('GeometryNodeMaterialSelection', name='Material Selection', label=label)
        # Input sockets

        self.plug(0, material)

        # Output sockets

        self.selection       = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'selection': self.selection}

# ----------------------------------------------------------------------------------------------------
# Node MergeByDistance for GeometryNodeMergeByDistance

class MergeByDistance(Node):

    """Class MergeByDistance
    

    | Geometry node name: 'Merge by Distance' 
    | Blender type:  GeometryNodeMergeByDistance 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - distance  : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry merge_by_distance : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, distance=None, label=None):

        super().__init__('GeometryNodeMergeByDistance', name='Merge by Distance', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, distance)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node MeshBoolean for GeometryNodeMeshBoolean

class MeshBoolean(Node):

    """Class MeshBoolean
    

    | Geometry node name: 'Mesh Boolean' 
    | Blender type:  GeometryNodeMeshBoolean 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh_1            : Geometry 
            - mesh_2            : * Geometry 
            - self_intersection : Boolean 
            - hole_tolerant     : Boolean 
    

            Parameters
            ----------
            - operation : 'DIFFERENCE' in ('INTERSECT', 'UNION', 'DIFFERENCE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh difference : Method 
    - Mesh intersect  : Method 
    - Mesh union      : Method 
    """

    def __init__(self, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None):

        super().__init__('GeometryNodeMeshBoolean', name='Mesh Boolean', label=label)
        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(1, *mesh_2)
        self.plug(0, mesh_1)
        self.plug(2, self_intersection)
        self.plug(3, hole_tolerant)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

# ----------------------------------------------------------------------------------------------------
# Node MeshCircle for GeometryNodeMeshCircle

class MeshCircle(Node):

    """Class MeshCircle
    

    | Geometry node name: 'Mesh Circle' 
    | Blender type:  GeometryNodeMeshCircle 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vertices : Integer 
            - radius   : Float 
    

            Parameters
            ----------
            - fill_type : 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh Circle : Constructor 
    """

    def __init__(self, vertices=None, radius=None, fill_type='NONE', label=None):

        super().__init__('GeometryNodeMeshCircle', name='Mesh Circle', label=label)
        # Parameters

        self.bnode.fill_type       = fill_type

        # Input sockets

        self.plug(0, vertices)
        self.plug(1, radius)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

    @property
    def fill_type(self):
        return self.bnode.fill_type

    @fill_type.setter
    def fill_type(self, value):
        self.bnode.fill_type = value

# ----------------------------------------------------------------------------------------------------
# Node Cone for GeometryNodeMeshCone

class Cone(Node):

    """Class Cone
    

    | Geometry node name: 'Cone' 
    | Blender type:  GeometryNodeMeshCone 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None,
        depth=None, fill_type='NGON', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vertices      : Integer 
            - side_segments : Integer 
            - fill_segments : Integer 
            - radius_top    : Float 
            - radius_bottom : Float 
            - depth         : Float 
    

            Parameters
            ----------
            - fill_type : 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh   : Mesh 
    - top    : Boolean 
    - bottom : Boolean 
    - side   : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh Cone : Constructor 
    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None):

        super().__init__('GeometryNodeMeshCone', name='Cone', label=label)
        # Parameters

        self.bnode.fill_type       = fill_type

        # Input sockets

        self.plug(0, vertices)
        self.plug(1, side_segments)
        self.plug(2, fill_segments)
        self.plug(3, radius_top)
        self.plug(4, radius_bottom)
        self.plug(5, depth)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.top             = self.Boolean(self.bnode.outputs[1])
        self.bottom          = self.Boolean(self.bnode.outputs[2])
        self.side            = self.Boolean(self.bnode.outputs[3])
        self.output_sockets  = {'mesh': self.mesh, 'top': self.top, 'bottom': self.bottom, 'side': self.side}

    @property
    def fill_type(self):
        return self.bnode.fill_type

    @fill_type.setter
    def fill_type(self, value):
        self.bnode.fill_type = value

# ----------------------------------------------------------------------------------------------------
# Node Cube for GeometryNodeMeshCube

class Cube(Node):

    """Class Cube
    

    | Geometry node name: 'Cube' 
    | Blender type:  GeometryNodeMeshCube 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - size       : Vector 
            - vertices_x : Integer 
            - vertices_y : Integer 
            - vertices_z : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh Cube : Constructor 
    """

    def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None):

        super().__init__('GeometryNodeMeshCube', name='Cube', label=label)
        # Input sockets

        self.plug(0, size)
        self.plug(1, vertices_x)
        self.plug(2, vertices_y)
        self.plug(3, vertices_z)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node Cylinder for GeometryNodeMeshCylinder

class Cylinder(Node):

    """Class Cylinder
    

    | Geometry node name: 'Cylinder' 
    | Blender type:  GeometryNodeMeshCylinder 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None,
        fill_type='NGON', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vertices      : Integer 
            - side_segments : Integer 
            - fill_segments : Integer 
            - radius        : Float 
            - depth         : Float 
    

            Parameters
            ----------
            - fill_type : 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh   : Mesh 
    - top    : Boolean 
    - side   : Boolean 
    - bottom : Boolean 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh Cylinder : Constructor 
    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None):

        super().__init__('GeometryNodeMeshCylinder', name='Cylinder', label=label)
        # Parameters

        self.bnode.fill_type       = fill_type

        # Input sockets

        self.plug(0, vertices)
        self.plug(1, side_segments)
        self.plug(2, fill_segments)
        self.plug(3, radius)
        self.plug(4, depth)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.top             = self.Boolean(self.bnode.outputs[1])
        self.side            = self.Boolean(self.bnode.outputs[2])
        self.bottom          = self.Boolean(self.bnode.outputs[3])
        self.output_sockets  = {'mesh': self.mesh, 'top': self.top, 'side': self.side, 'bottom': self.bottom}

    @property
    def fill_type(self):
        return self.bnode.fill_type

    @fill_type.setter
    def fill_type(self, value):
        self.bnode.fill_type = value

# ----------------------------------------------------------------------------------------------------
# Node Grid for GeometryNodeMeshGrid

class Grid(Node):

    """Class Grid
    

    | Geometry node name: 'Grid' 
    | Blender type:  GeometryNodeMeshGrid 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - size_x     : Float 
            - size_y     : Float 
            - vertices_x : Integer 
            - vertices_y : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh Grid : Constructor 
    """

    def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None):

        super().__init__('GeometryNodeMeshGrid', name='Grid', label=label)
        # Input sockets

        self.plug(0, size_x)
        self.plug(1, size_y)
        self.plug(2, vertices_x)
        self.plug(3, vertices_y)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node IcoSphere for GeometryNodeMeshIcoSphere

class IcoSphere(Node):

    """Class IcoSphere
    

    | Geometry node name: 'Ico Sphere' 
    | Blender type:  GeometryNodeMeshIcoSphere 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.IcoSphere(radius=None, subdivisions=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - radius       : Float 
            - subdivisions : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh IcoSphere : Constructor 
    """

    def __init__(self, radius=None, subdivisions=None, label=None):

        super().__init__('GeometryNodeMeshIcoSphere', name='Ico Sphere', label=label)
        # Input sockets

        self.plug(0, radius)
        self.plug(1, subdivisions)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node MeshLine for GeometryNodeMeshLine

class MeshLine(Node):

    """Class MeshLine
    

    | Geometry node name: 'Mesh Line' 
    | Blender type:  GeometryNodeMeshLine 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL',
        mode='OFFSET', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - count          : Integer 
            - resolution     : Float 
            - start_location : Vector 
            - offset         : Vector 
    

            Parameters
            ----------
            - count_mode : 'TOTAL' in ('TOTAL', 'RESOLUTION') 
            - mode       : 'OFFSET' in ('OFFSET', 'END_POINTS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh Line : Constructor 
    """

    def __init__(self, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None):

        super().__init__('GeometryNodeMeshLine', name='Mesh Line', label=label)
        # Parameters

        self.bnode.count_mode      = count_mode
        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, count)
        self.plug(1, resolution)
        self.plug(2, start_location)
        self.plug(3, offset)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

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

    """Class MeshToCurve
    

    | Geometry node name: 'Mesh to Curve' 
    | Blender type:  GeometryNodeMeshToCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MeshToCurve(mesh=None, selection=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh      : Mesh 
            - selection : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh to_curve : Method 
    """

    def __init__(self, mesh=None, selection=None, label=None):

        super().__init__('GeometryNodeMeshToCurve', name='Mesh to Curve', label=label)
        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node MeshToPoints for GeometryNodeMeshToPoints

class MeshToPoints(Node):

    """Class MeshToPoints
    

    | Geometry node name: 'Mesh to Points' 
    | Blender type:  GeometryNodeMeshToPoints 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh      : Mesh 
            - selection : Boolean 
            - position  : Vector 
            - radius    : Float 
    

            Parameters
            ----------
            - mode : 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - points : Points 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh to_points : Method 
    """

    def __init__(self, mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None):

        super().__init__('GeometryNodeMeshToPoints', name='Mesh to Points', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, radius)

        # Output sockets

        self.points          = self.Points(self.bnode.outputs[0])
        self.output_sockets  = {'points': self.points}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node UvSphere for GeometryNodeMeshUVSphere

class UvSphere(Node):

    """Class UvSphere
    

    | Geometry node name: 'UV Sphere' 
    | Blender type:  GeometryNodeMeshUVSphere 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.UvSphere(segments=None, rings=None, radius=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - segments : Integer 
            - rings    : Integer 
            - radius   : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh UVSphere : Constructor 
    """

    def __init__(self, segments=None, rings=None, radius=None, label=None):

        super().__init__('GeometryNodeMeshUVSphere', name='UV Sphere', label=label)
        # Input sockets

        self.plug(0, segments)
        self.plug(1, rings)
        self.plug(2, radius)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node ObjectInfo for GeometryNodeObjectInfo

class ObjectInfo(Node):

    """Class ObjectInfo
    

    | Geometry node name: 'Object Info' 
    | Blender type:  GeometryNodeObjectInfo 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - object      : Object 
            - as_instance : Boolean 
    

            Parameters
            ----------
            - transform_space : 'ORIGINAL' in ('ORIGINAL', 'RELATIVE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - location : Vector 
    - rotation : Vector 
    - scale    : Vector 
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Object info : Property 
    """

    def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL', label=None):

        super().__init__('GeometryNodeObjectInfo', name='Object Info', label=label)
        # Parameters

        self.bnode.transform_space = transform_space

        # Input sockets

        self.plug(0, object)
        self.plug(1, as_instance)

        # Output sockets

        self.location        = self.Vector(self.bnode.outputs[0])
        self.rotation        = self.Vector(self.bnode.outputs[1])
        self.scale           = self.Vector(self.bnode.outputs[2])
        self.geometry        = self.Geometry(self.bnode.outputs[3])
        self.output_sockets  = {'location': self.location, 'rotation': self.rotation, 'scale': self.scale, 'geometry': self.geometry}

    @property
    def transform_space(self):
        return self.bnode.transform_space

    @transform_space.setter
    def transform_space(self, value):
        self.bnode.transform_space = value

# ----------------------------------------------------------------------------------------------------
# Node PointsToVertices for GeometryNodePointsToVertices

class PointsToVertices(Node):

    """Class PointsToVertices
    

    | Geometry node name: 'Points to Vertices' 
    | Blender type:  GeometryNodePointsToVertices 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.PointsToVertices(points=None, selection=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - points    : Points 
            - selection : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Points to_vertices : Method 
    """

    def __init__(self, points=None, selection=None, label=None):

        super().__init__('GeometryNodePointsToVertices', name='Points to Vertices', label=label)
        # Input sockets

        self.plug(0, points)
        self.plug(1, selection)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node PointsToVolume for GeometryNodePointsToVolume

class PointsToVolume(Node):

    """Class PointsToVolume
    

    | Geometry node name: 'Points to Volume' 
    | Blender type:  GeometryNodePointsToVolume 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.PointsToVolume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None,
        resolution_mode='VOXEL_AMOUNT', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - points       : Points 
            - density      : Float 
            - voxel_size   : Float 
            - voxel_amount : Float 
            - radius       : Float 
    

            Parameters
            ----------
            - resolution_mode : 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - volume : Volume 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Points to_volume : Method 
    """

    def __init__(self, points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None):

        super().__init__('GeometryNodePointsToVolume', name='Points to Volume', label=label)
        # Parameters

        self.bnode.resolution_mode = resolution_mode

        # Input sockets

        self.plug(0, points)
        self.plug(1, density)
        self.plug(2, voxel_size)
        self.plug(3, voxel_amount)
        self.plug(4, radius)

        # Output sockets

        self.volume          = self.Volume(self.bnode.outputs[0])
        self.output_sockets  = {'volume': self.volume}

    @property
    def resolution_mode(self):
        return self.bnode.resolution_mode

    @resolution_mode.setter
    def resolution_mode(self, value):
        self.bnode.resolution_mode = value

# ----------------------------------------------------------------------------------------------------
# Node GeometryProximity for GeometryNodeProximity

class GeometryProximity(Node):

    """Class GeometryProximity
    

    | Geometry node name: 'Geometry Proximity' 
    | Blender type:  GeometryNodeProximity 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - target          : Geometry 
            - source_position : Vector 
    

            Parameters
            ----------
            - target_element : 'FACES' in ('POINTS', 'EDGES', 'FACES') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - position : Vector 
    - distance : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry proximity : Method 
    """

    def __init__(self, target=None, source_position=None, target_element='FACES', label=None):

        super().__init__('GeometryNodeProximity', name='Geometry Proximity', label=label)
        # Parameters

        self.bnode.target_element  = target_element

        # Input sockets

        self.plug(0, target)
        self.plug(1, source_position)

        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.distance        = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'position': self.position, 'distance': self.distance}

    @property
    def target_element(self):
        return self.bnode.target_element

    @target_element.setter
    def target_element(self, value):
        self.bnode.target_element = value

# ----------------------------------------------------------------------------------------------------
# Node Raycast for GeometryNodeRaycast

class Raycast(Node):

    """Class Raycast
    

    | Geometry node name: 'Raycast' 
    | Blender type:  GeometryNodeRaycast 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None,
        data_type='FLOAT', mapping='INTERPOLATED', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - target_geometry : Geometry 
            - attribute       : data_type dependant 
            - source_position : Vector 
            - ray_direction   : Vector 
            - ray_length      : Float 
    

            Parameters
            ----------
            - data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
            - mapping   : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN') 
    - Input sockets     : attribute 
    - Output sockets    : attribute 
    

    Output sockets
    ==============
    - is_hit       : Boolean 
    - hit_position : Vector 
    - hit_normal   : Vector 
    - hit_distance : Float 
    - attribute    : data_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean raycast : Method 
    - Color raycast   : Method 
    - Float raycast   : Method 
    - Integer raycast : Method 
    - Vector raycast  : Method 
    """

    def __init__(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None):

        super().__init__('GeometryNodeRaycast', name='Raycast', label=label)
        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.mapping         = mapping

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, attribute)
        elif data_type == 'INT':
            self.plug(5, attribute)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(1, attribute)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, attribute)
        elif data_type == 'BOOLEAN':
            self.plug(4, attribute)

        self.plug(0, target_geometry)
        self.plug(6, source_position)
        self.plug(7, ray_direction)
        self.plug(8, ray_length)

        # Output sockets

        if data_type == 'FLOAT':
            self.attribute       = self.Float(self.bnode.outputs[5])
        elif data_type == 'INT':
            self.attribute       = self.Integer(self.bnode.outputs[8])
        elif data_type == 'FLOAT_VECTOR':
            self.attribute       = self.Vector(self.bnode.outputs[4])
        elif data_type == 'FLOAT_COLOR':
            self.attribute       = self.Color(self.bnode.outputs[6])
        elif data_type == 'BOOLEAN':
            self.attribute       = self.Boolean(self.bnode.outputs[7])

        self.is_hit          = self.Boolean(self.bnode.outputs[0])
        self.hit_position    = self.Vector(self.bnode.outputs[1])
        self.hit_normal      = self.Vector(self.bnode.outputs[2])
        self.hit_distance    = self.Float(self.bnode.outputs[3])
        self.output_sockets  = {'is_hit': self.is_hit, 'hit_position': self.hit_position, 'hit_normal': self.hit_normal, 'hit_distance': self.hit_distance, 'attribute': self.attribute}

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

    """Class RealizeInstances
    

    | Geometry node name: 'Realize Instances' 
    | Blender type:  GeometryNodeRealizeInstances 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.RealizeInstances(geometry=None, legacy_behavior=False, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
    

            Parameters
            ----------
            - legacy_behavior : False bool 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry realize_instances : Stacked method 
    """

    def __init__(self, geometry=None, legacy_behavior=False, label=None):

        super().__init__('GeometryNodeRealizeInstances', name='Realize Instances', label=label)
        # Parameters

        self.bnode.legacy_behavior = legacy_behavior

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

    @property
    def legacy_behavior(self):
        return self.bnode.legacy_behavior

    @legacy_behavior.setter
    def legacy_behavior(self, value):
        self.bnode.legacy_behavior = value

# ----------------------------------------------------------------------------------------------------
# Node ReplaceMaterial for GeometryNodeReplaceMaterial

class ReplaceMaterial(Node):

    """Class ReplaceMaterial
    

    | Geometry node name: 'Replace Material' 
    | Blender type:  GeometryNodeReplaceMaterial 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ReplaceMaterial(geometry=None, old=None, new=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
            - old      : Material 
            - new      : Material 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry replace_material : Stacked method 
    """

    def __init__(self, geometry=None, old=None, new=None, label=None):

        super().__init__('GeometryNodeReplaceMaterial', name='Replace Material', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, old)
        self.plug(2, new)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node ResampleCurve for GeometryNodeResampleCurve

class ResampleCurve(Node):

    """Class ResampleCurve
    

    | Geometry node name: 'Resample Curve' 
    | Blender type:  GeometryNodeResampleCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
            - count     : Integer 
            - length    : Float 
    

            Parameters
            ----------
            - mode : 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve resample : Stacked method 
    """

    def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT', label=None):

        super().__init__('GeometryNodeResampleCurve', name='Resample Curve', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, count)
        self.plug(3, length)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node ReverseCurve for GeometryNodeReverseCurve

class ReverseCurve(Node):

    """Class ReverseCurve
    

    | Geometry node name: 'Reverse Curve' 
    | Blender type:  GeometryNodeReverseCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ReverseCurve(curve=None, selection=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve reverse : Stacked method 
    """

    def __init__(self, curve=None, selection=None, label=None):

        super().__init__('GeometryNodeReverseCurve', name='Reverse Curve', label=label)
        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node RotateInstances for GeometryNodeRotateInstances

class RotateInstances(Node):

    """Class RotateInstances
    

    | Geometry node name: 'Rotate Instances' 
    | Blender type:  GeometryNodeRotateInstances 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.RotateInstances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None,
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - instances   : Instances 
            - selection   : Boolean 
            - rotation    : Vector 
            - pivot_point : Vector 
            - local_space : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - instances : Instances 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Instances rotate : Stacked method 
    """

    def __init__(self, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, label=None):

        super().__init__('GeometryNodeRotateInstances', name='Rotate Instances', label=label)
        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, rotation)
        self.plug(3, pivot_point)
        self.plug(4, local_space)

        # Output sockets

        self.instances       = self.Instances(self.bnode.outputs[0])
        self.output_sockets  = {'instances': self.instances}

# ----------------------------------------------------------------------------------------------------
# Node SampleCurve for GeometryNodeSampleCurve

class SampleCurve(Node):

    """Class SampleCurve
    

    | Geometry node name: 'Sample Curve' 
    | Blender type:  GeometryNodeSampleCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SampleCurve(curve=None, factor=None, length=None, mode='LENGTH', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve  : Curve 
            - factor : Float 
            - length : Float 
    

            Parameters
            ----------
            - mode : 'LENGTH' in ('FACTOR', 'LENGTH') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - position : Vector 
    - tangent  : Vector 
    - normal   : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve sample : Method 
    """

    def __init__(self, curve=None, factor=None, length=None, mode='LENGTH', label=None):

        super().__init__('GeometryNodeSampleCurve', name='Sample Curve', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, factor)
        self.plug(2, length)

        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.tangent         = self.Vector(self.bnode.outputs[1])
        self.normal          = self.Vector(self.bnode.outputs[2])
        self.output_sockets  = {'position': self.position, 'tangent': self.tangent, 'normal': self.normal}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node ScaleElements for GeometryNodeScaleElements

class ScaleElements(Node):

    """Class ScaleElements
    

    | Geometry node name: 'Scale Elements' 
    | Blender type:  GeometryNodeScaleElements 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE',
        scale_mode='UNIFORM', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - scale     : Float 
            - center    : Vector 
            - axis      : Vector 
    

            Parameters
            ----------
            - domain     : 'FACE' in ('FACE', 'EDGE') 
            - scale_mode : 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry scale_elements : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None):

        super().__init__('GeometryNodeScaleElements', name='Scale Elements', label=label)
        # Parameters

        self.bnode.domain          = domain
        self.bnode.scale_mode      = scale_mode

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, scale)
        self.plug(3, center)
        self.plug(4, axis)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

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

    """Class ScaleInstances
    

    | Geometry node name: 'Scale Instances' 
    | Blender type:  GeometryNodeScaleInstances 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.ScaleInstances(instances=None, selection=None, scale=None, center=None, local_space=None,
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - instances   : Instances 
            - selection   : Boolean 
            - scale       : Vector 
            - center      : Vector 
            - local_space : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - instances : Instances 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Instances scale : Stacked method 
    """

    def __init__(self, instances=None, selection=None, scale=None, center=None, local_space=None, label=None):

        super().__init__('GeometryNodeScaleInstances', name='Scale Instances', label=label)
        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, scale)
        self.plug(3, center)
        self.plug(4, local_space)

        # Output sockets

        self.instances       = self.Instances(self.bnode.outputs[0])
        self.output_sockets  = {'instances': self.instances}

# ----------------------------------------------------------------------------------------------------
# Node SeparateComponents for GeometryNodeSeparateComponents

class SeparateComponents(Node):

    """Class SeparateComponents
    

    | Geometry node name: 'Separate Components' 
    | Blender type:  GeometryNodeSeparateComponents 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SeparateComponents(geometry=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry : Geometry 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh        : Mesh 
    - point_cloud : Geometry 
    - curve       : Curve 
    - volume      : Volume 
    - instances   : Instances 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry components : Property 
    """

    def __init__(self, geometry=None, label=None):

        super().__init__('GeometryNodeSeparateComponents', name='Separate Components', label=label)
        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.point_cloud     = self.Geometry(self.bnode.outputs[1])
        self.curve           = self.Curve(self.bnode.outputs[2])
        self.volume          = self.Volume(self.bnode.outputs[3])
        self.instances       = self.Instances(self.bnode.outputs[4])
        self.output_sockets  = {'mesh': self.mesh, 'point_cloud': self.point_cloud, 'curve': self.curve, 'volume': self.volume, 'instances': self.instances}

# ----------------------------------------------------------------------------------------------------
# Node SeparateGeometry for GeometryNodeSeparateGeometry

class SeparateGeometry(Node):

    """Class SeparateGeometry
    

    | Geometry node name: 'Separate Geometry' 
    | Blender type:  GeometryNodeSeparateGeometry 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
    

            Parameters
            ----------
            - domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - selection : Geometry 
    - inverted  : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry components : Method 
    """

    def __init__(self, geometry=None, selection=None, domain='POINT', label=None):

        super().__init__('GeometryNodeSeparateGeometry', name='Separate Geometry', label=label)
        # Parameters

        self.bnode.domain          = domain

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)

        # Output sockets

        self.selection       = self.Geometry(self.bnode.outputs[0])
        self.inverted        = self.Geometry(self.bnode.outputs[1])
        self.output_sockets  = {'selection': self.selection, 'inverted': self.inverted}

    @property
    def domain(self):
        return self.bnode.domain

    @domain.setter
    def domain(self, value):
        self.bnode.domain = value

# ----------------------------------------------------------------------------------------------------
# Node SetHandlePositions for GeometryNodeSetCurveHandlePositions

class SetHandlePositions(Node):

    """Class SetHandlePositions
    

    | Geometry node name: 'Set Handle Positions' 
    | Blender type:  GeometryNodeSetCurveHandlePositions 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
            - position  : Vector 
            - offset    : Vector 
    

            Parameters
            ----------
            - mode : 'LEFT' in ('LEFT', 'RIGHT') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve set_handle_positions : Stacked method 
    """

    def __init__(self, curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None):

        super().__init__('GeometryNodeSetCurveHandlePositions', name='Set Handle Positions', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, offset)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node SetCurveRadius for GeometryNodeSetCurveRadius

class SetCurveRadius(Node):

    """Class SetCurveRadius
    

    | Geometry node name: 'Set Curve Radius' 
    | Blender type:  GeometryNodeSetCurveRadius 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetCurveRadius(curve=None, selection=None, radius=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
            - radius    : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve set_radius : Stacked method 
    """

    def __init__(self, curve=None, selection=None, radius=None, label=None):

        super().__init__('GeometryNodeSetCurveRadius', name='Set Curve Radius', label=label)
        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, radius)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node SetCurveTilt for GeometryNodeSetCurveTilt

class SetCurveTilt(Node):

    """Class SetCurveTilt
    

    | Geometry node name: 'Set Curve Tilt' 
    | Blender type:  GeometryNodeSetCurveTilt 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve     : Curve 
            - selection : Boolean 
            - tilt      : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve set_tilt : Stacked method 
    """

    def __init__(self, curve=None, selection=None, tilt=None, label=None):

        super().__init__('GeometryNodeSetCurveTilt', name='Set Curve Tilt', label=label)
        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, tilt)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node SetID for GeometryNodeSetID

class SetID(Node):

    """Class SetID
    

    | Geometry node name: 'Set ID' 
    | Blender type:  GeometryNodeSetID 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetID(geometry=None, selection=None, ID=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - ID        : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry set_ID : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, ID=None, label=None):

        super().__init__('GeometryNodeSetID', name='Set ID', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, ID)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SetMaterial for GeometryNodeSetMaterial

class SetMaterial(Node):

    """Class SetMaterial
    

    | Geometry node name: 'Set Material' 
    | Blender type:  GeometryNodeSetMaterial 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetMaterial(geometry=None, selection=None, material=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - material  : Material 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry set_material : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, material=None, label=None):

        super().__init__('GeometryNodeSetMaterial', name='Set Material', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, material)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SetMaterialIndex for GeometryNodeSetMaterialIndex

class SetMaterialIndex(Node):

    """Class SetMaterialIndex
    

    | Geometry node name: 'Set Material Index' 
    | Blender type:  GeometryNodeSetMaterialIndex 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetMaterialIndex(geometry=None, selection=None, material_index=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry       : Geometry 
            - selection      : Boolean 
            - material_index : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry set_material_index : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, material_index=None, label=None):

        super().__init__('GeometryNodeSetMaterialIndex', name='Set Material Index', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, material_index)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SetPointRadius for GeometryNodeSetPointRadius

class SetPointRadius(Node):

    """Class SetPointRadius
    

    | Geometry node name: 'Set Point Radius' 
    | Blender type:  GeometryNodeSetPointRadius 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetPointRadius(points=None, selection=None, radius=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - points    : Points 
            - selection : Boolean 
            - radius    : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - points : Points 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Points set_radius : Stacked method 
    """

    def __init__(self, points=None, selection=None, radius=None, label=None):

        super().__init__('GeometryNodeSetPointRadius', name='Set Point Radius', label=label)
        # Input sockets

        self.plug(0, points)
        self.plug(1, selection)
        self.plug(2, radius)

        # Output sockets

        self.points          = self.Points(self.bnode.outputs[0])
        self.output_sockets  = {'points': self.points}

# ----------------------------------------------------------------------------------------------------
# Node SetPosition for GeometryNodeSetPosition

class SetPosition(Node):

    """Class SetPosition
    

    | Geometry node name: 'Set Position' 
    | Blender type:  GeometryNodeSetPosition 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetPosition(geometry=None, selection=None, position=None, offset=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - position  : Vector 
            - offset    : Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry set_position : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, position=None, offset=None, label=None):

        super().__init__('GeometryNodeSetPosition', name='Set Position', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, offset)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SetShadeSmooth for GeometryNodeSetShadeSmooth

class SetShadeSmooth(Node):

    """Class SetShadeSmooth
    

    | Geometry node name: 'Set Shade Smooth' 
    | Blender type:  GeometryNodeSetShadeSmooth 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetShadeSmooth(geometry=None, selection=None, shade_smooth=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry     : Geometry 
            - selection    : Boolean 
            - shade_smooth : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry set_shade_smooth : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, shade_smooth=None, label=None):

        super().__init__('GeometryNodeSetShadeSmooth', name='Set Shade Smooth', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, shade_smooth)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SetSplineCyclic for GeometryNodeSetSplineCyclic

class SetSplineCyclic(Node):

    """Class SetSplineCyclic
    

    | Geometry node name: 'Set Spline Cyclic' 
    | Blender type:  GeometryNodeSetSplineCyclic 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry  : Geometry 
            - selection : Boolean 
            - cyclic    : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline set_cyclic : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, cyclic=None, label=None):

        super().__init__('GeometryNodeSetSplineCyclic', name='Set Spline Cyclic', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, cyclic)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SetSplineResolution for GeometryNodeSetSplineResolution

class SetSplineResolution(Node):

    """Class SetSplineResolution
    

    | Geometry node name: 'Set Spline Resolution' 
    | Blender type:  GeometryNodeSetSplineResolution 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SetSplineResolution(geometry=None, selection=None, resolution=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry   : Geometry 
            - selection  : Boolean 
            - resolution : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline set_resolution : Stacked method 
    """

    def __init__(self, geometry=None, selection=None, resolution=None, label=None):

        super().__init__('GeometryNodeSetSplineResolution', name='Set Spline Resolution', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, resolution)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node SplineLength for GeometryNodeSplineLength

class SplineLength(Node):

    """Class SplineLength
    

    | Geometry node name: 'Spline Length' 
    | Blender type:  GeometryNodeSplineLength 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SplineLength(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - length      : Float 
    - point_count : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_length : Capture attribute 
    - Spline length         : Attribute 
    - Spline point_count    : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeSplineLength', name='Spline Length', label=label)
        # Output sockets

        self.length          = self.Float(self.bnode.outputs[0])
        self.point_count     = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = {'length': self.length, 'point_count': self.point_count}

# ----------------------------------------------------------------------------------------------------
# Node SplineParameter for GeometryNodeSplineParameter

class SplineParameter(Node):

    """Class SplineParameter
    

    | Geometry node name: 'Spline Parameter' 
    | Blender type:  GeometryNodeSplineParameter 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SplineParameter(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - factor : Float 
    - length : Float 
    - index  : Integer 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Spline capture_parameter : Capture attribute 
    - Spline factor            : Attribute 
    - Spline parameter_index   : Attribute 
    - Spline parameter_length  : Attribute 
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeSplineParameter', name='Spline Parameter', label=label)
        # Output sockets

        self.factor          = self.Float(self.bnode.outputs[0])
        self.length          = self.Float(self.bnode.outputs[1])
        self.index           = self.Integer(self.bnode.outputs[2])
        self.output_sockets  = {'factor': self.factor, 'length': self.length, 'index': self.index}

# ----------------------------------------------------------------------------------------------------
# Node SplitEdges for GeometryNodeSplitEdges

class SplitEdges(Node):

    """Class SplitEdges
    

    | Geometry node name: 'Split Edges' 
    | Blender type:  GeometryNodeSplitEdges 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SplitEdges(mesh=None, selection=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh      : Mesh 
            - selection : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh split_edges : Stacked method 
    """

    def __init__(self, mesh=None, selection=None, label=None):

        super().__init__('GeometryNodeSplitEdges', name='Split Edges', label=label)
        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node JoinStrings for GeometryNodeStringJoin

class JoinStrings(Node):

    """Class JoinStrings
    

    | Geometry node name: 'Join Strings' 
    | Blender type:  GeometryNodeStringJoin 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.JoinStrings(*strings, delimiter=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - delimiter : String 
            - strings   : * String 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - string : String 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - String join            : Method 
    - functions join_strings : Function 
    """

    def __init__(self, *strings, delimiter=None, label=None):

        super().__init__('GeometryNodeStringJoin', name='Join Strings', label=label)
        # Input sockets

        self.plug(1, *strings)
        self.plug(0, delimiter)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = {'string': self.string}

# ----------------------------------------------------------------------------------------------------
# Node StringToCurves for GeometryNodeStringToCurves

class StringToCurves(Node):

    """Class StringToCurves
    

    | Geometry node name: 'String to Curves' 
    | Blender type:  GeometryNodeStringToCurves 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.StringToCurves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None,
        text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW',
        pivot_mode='BOTTOM_LEFT', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - string            : String 
            - size              : Float 
            - character_spacing : Float 
            - word_spacing      : Float 
            - line_spacing      : Float 
            - text_box_width    : Float 
            - text_box_height   : Float 
    

            Parameters
            ----------
            - align_x    : 'LEFT' in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH') 
            - align_y    : 'TOP_BASELINE' in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM') 
            - overflow   : 'OVERFLOW' in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE') 
            - pivot_mode : 'BOTTOM_LEFT' in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER',
              'BOTTOM_RIGHT') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve_instances : Geometry 
    - remainder       : String 
    - line            : Integer 
    - pivot_point     : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - String to_curves : Method 
    """

    def __init__(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None):

        super().__init__('GeometryNodeStringToCurves', name='String to Curves', label=label)
        # Parameters

        self.bnode.align_x         = align_x
        self.bnode.align_y         = align_y
        self.bnode.overflow        = overflow
        self.bnode.pivot_mode      = pivot_mode

        # Input sockets

        self.plug(0, string)
        self.plug(1, size)
        self.plug(2, character_spacing)
        self.plug(3, word_spacing)
        self.plug(4, line_spacing)
        self.plug(5, text_box_width)
        self.plug(6, text_box_height)

        # Output sockets

        self.curve_instances = self.Geometry(self.bnode.outputs[0])
        self.remainder       = self.String(self.bnode.outputs[1])
        self.line            = self.Integer(self.bnode.outputs[2])
        self.pivot_point     = self.Vector(self.bnode.outputs[3])
        self.output_sockets  = {'curve_instances': self.curve_instances, 'remainder': self.remainder, 'line': self.line, 'pivot_point': self.pivot_point}

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

    """Class SubdivideCurve
    

    | Geometry node name: 'Subdivide Curve' 
    | Blender type:  GeometryNodeSubdivideCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SubdivideCurve(curve=None, cuts=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve : Curve 
            - cuts  : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve subdivide : Stacked method 
    """

    def __init__(self, curve=None, cuts=None, label=None):

        super().__init__('GeometryNodeSubdivideCurve', name='Subdivide Curve', label=label)
        # Input sockets

        self.plug(0, curve)
        self.plug(1, cuts)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

# ----------------------------------------------------------------------------------------------------
# Node SubdivideMesh for GeometryNodeSubdivideMesh

class SubdivideMesh(Node):

    """Class SubdivideMesh
    

    | Geometry node name: 'Subdivide Mesh' 
    | Blender type:  GeometryNodeSubdivideMesh 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SubdivideMesh(mesh=None, level=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh  : Mesh 
            - level : Integer 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh subdivide : Stacked method 
    """

    def __init__(self, mesh=None, level=None, label=None):

        super().__init__('GeometryNodeSubdivideMesh', name='Subdivide Mesh', label=label)
        # Input sockets

        self.plug(0, mesh)
        self.plug(1, level)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

# ----------------------------------------------------------------------------------------------------
# Node SubdivisionSurface for GeometryNodeSubdivisionSurface

class SubdivisionSurface(Node):

    """Class SubdivisionSurface
    

    | Geometry node name: 'Subdivision Surface' 
    | Blender type:  GeometryNodeSubdivisionSurface 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SubdivisionSurface(mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh   : Mesh 
            - level  : Integer 
            - crease : Float 
    

            Parameters
            ----------
            - boundary_smooth : 'ALL' in ('PRESERVE_CORNERS', 'ALL') 
            - uv_smooth       : 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE',
              'PRESERVE_BOUNDARIES', 'SMOOTH_ALL') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh subdivision_surface : Stacked method 
    """

    def __init__(self, mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None):

        super().__init__('GeometryNodeSubdivisionSurface', name='Subdivision Surface', label=label)
        # Parameters

        self.bnode.boundary_smooth = boundary_smooth
        self.bnode.uv_smooth       = uv_smooth

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, level)
        self.plug(2, crease)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

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

    """Class Switch
    

    | Geometry node name: 'Switch' 
    | Blender type:  GeometryNodeSwitch 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Switch(switch0=None, switch1=None, false=None, true=None, input_type='GEOMETRY', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - switch0 : Boolean 
            - switch1 : Boolean 
            - false   : input_type dependant 
            - true    : input_type dependant 
    

            Parameters
            ----------
            - input_type : 'GEOMETRY' in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE',
              'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE',
      'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL') 
    - Input sockets     : false true 
    - Output sockets    : output 
    

    Output sockets
    ==============
    - output : input_type dependant 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Boolean switch    : Method 
    - Collection switch : Method 
    - Float switch      : Method 
    - Geometry switch   : Method 
    - Image switch      : Method 
    - Integer switch    : Method 
    - Material switch   : Method 
    - Object switch     : Method 
    - String switch     : Method 
    - Texture switch    : Method 
    """

    def __init__(self, switch0=None, switch1=None, false=None, true=None, input_type='GEOMETRY', label=None):

        super().__init__('GeometryNodeSwitch', name='Switch', label=label)
        # Parameters

        self.bnode.input_type      = input_type

        # Input sockets

        if input_type == 'FLOAT':
            self.plug(2, false)
            self.plug(3, true)
        elif input_type == 'INT':
            self.plug(4, false)
            self.plug(5, true)
        elif input_type == 'BOOLEAN':
            self.plug(6, false)
            self.plug(7, true)
        elif input_type == 'VECTOR':
            self.plug(8, false)
            self.plug(9, true)
        elif input_type == 'STRING':
            self.plug(12, false)
            self.plug(13, true)
        elif input_type == 'RGBA':
            self.plug(10, false)
            self.plug(11, true)
        elif input_type == 'OBJECT':
            self.plug(16, false)
            self.plug(17, true)
        elif input_type == 'IMAGE':
            self.plug(24, false)
            self.plug(25, true)
        elif input_type == 'GEOMETRY':
            self.plug(14, false)
            self.plug(15, true)
        elif input_type == 'COLLECTION':
            self.plug(18, false)
            self.plug(19, true)
        elif input_type == 'TEXTURE':
            self.plug(20, false)
            self.plug(21, true)
        elif input_type == 'MATERIAL':
            self.plug(22, false)
            self.plug(23, true)

        self.plug(0, switch0)
        self.plug(1, switch1)

        # Output sockets

        if input_type == 'FLOAT':
            self.output          = self.Float(self.bnode.outputs[0])
        elif input_type == 'INT':
            self.output          = self.Integer(self.bnode.outputs[1])
        elif input_type == 'BOOLEAN':
            self.output          = self.Boolean(self.bnode.outputs[2])
        elif input_type == 'VECTOR':
            self.output          = self.Vector(self.bnode.outputs[3])
        elif input_type == 'STRING':
            self.output          = self.String(self.bnode.outputs[5])
        elif input_type == 'RGBA':
            self.output          = self.Color(self.bnode.outputs[4])
        elif input_type == 'OBJECT':
            self.output          = self.Object(self.bnode.outputs[7])
        elif input_type == 'IMAGE':
            self.output          = self.Image(self.bnode.outputs[11])
        elif input_type == 'GEOMETRY':
            self.output          = self.Geometry(self.bnode.outputs[6])
        elif input_type == 'COLLECTION':
            self.output          = self.Collection(self.bnode.outputs[8])
        elif input_type == 'TEXTURE':
            self.output          = self.Texture(self.bnode.outputs[9])
        elif input_type == 'MATERIAL':
            self.output          = self.Material(self.bnode.outputs[10])

        self.output_sockets  = {'output': self.output}

    @property
    def input_type(self):
        return self.bnode.input_type

    @input_type.setter
    def input_type(self, value):
        self.bnode.input_type = value

# ----------------------------------------------------------------------------------------------------
# Node Transform for GeometryNodeTransform

class Transform(Node):

    """Class Transform
    

    | Geometry node name: 'Transform' 
    | Blender type:  GeometryNodeTransform 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - geometry    : Geometry 
            - translation : Vector 
            - rotation    : Vector 
            - scale       : Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - geometry : Geometry 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Geometry transform : Stacked method 
    """

    def __init__(self, geometry=None, translation=None, rotation=None, scale=None, label=None):

        super().__init__('GeometryNodeTransform', name='Transform', label=label)
        # Input sockets

        self.plug(0, geometry)
        self.plug(1, translation)
        self.plug(2, rotation)
        self.plug(3, scale)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = {'geometry': self.geometry}

# ----------------------------------------------------------------------------------------------------
# Node TranslateInstances for GeometryNodeTranslateInstances

class TranslateInstances(Node):

    """Class TranslateInstances
    

    | Geometry node name: 'Translate Instances' 
    | Blender type:  GeometryNodeTranslateInstances 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.TranslateInstances(instances=None, selection=None, translation=None, local_space=None, label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - instances   : Instances 
            - selection   : Boolean 
            - translation : Vector 
            - local_space : Boolean 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - instances : Instances 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Instances translate : Stacked method 
    """

    def __init__(self, instances=None, selection=None, translation=None, local_space=None, label=None):

        super().__init__('GeometryNodeTranslateInstances', name='Translate Instances', label=label)
        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, translation)
        self.plug(3, local_space)

        # Output sockets

        self.instances       = self.Instances(self.bnode.outputs[0])
        self.output_sockets  = {'instances': self.instances}

# ----------------------------------------------------------------------------------------------------
# Node Triangulate for GeometryNodeTriangulate

class Triangulate(Node):

    """Class Triangulate
    

    | Geometry node name: 'Triangulate' 
    | Blender type:  GeometryNodeTriangulate 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL',
        label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - mesh             : Mesh 
            - selection        : Boolean 
            - minimum_vertices : Integer 
    

            Parameters
            ----------
            - ngon_method : 'BEAUTY' in ('BEAUTY', 'CLIP') 
            - quad_method : 'SHORTEST_DIAGONAL' in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Mesh triangulate : Stacked method 
    """

    def __init__(self, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None):

        super().__init__('GeometryNodeTriangulate', name='Triangulate', label=label)
        # Parameters

        self.bnode.ngon_method     = ngon_method
        self.bnode.quad_method     = quad_method

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, minimum_vertices)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

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

    """Class TrimCurve
    

    | Geometry node name: 'Trim Curve' 
    | Blender type:  GeometryNodeTrimCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.TrimCurve(curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - curve  : Curve 
            - start0 : Float 
            - start1 : Float 
            - end0   : Float 
            - end1   : Float 
    

            Parameters
            ----------
            - mode : 'FACTOR' in ('FACTOR', 'LENGTH') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - curve : Curve 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Curve trim : Stacked method 
    """

    def __init__(self, curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None):

        super().__init__('GeometryNodeTrimCurve', name='Trim Curve', label=label)
        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, start0)
        self.plug(3, start1)
        self.plug(2, end0)
        self.plug(4, end1)

        # Output sockets

        self.curve           = self.Curve(self.bnode.outputs[0])
        self.output_sockets  = {'curve': self.curve}

    @property
    def mode(self):
        return self.bnode.mode

    @mode.setter
    def mode(self, value):
        self.bnode.mode = value

# ----------------------------------------------------------------------------------------------------
# Node VolumeToMesh for GeometryNodeVolumeToMesh

class VolumeToMesh(Node):

    """Class VolumeToMesh
    

    | Geometry node name: 'Volume to Mesh' 
    | Blender type:  GeometryNodeVolumeToMesh 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.VolumeToMesh(volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None,
        resolution_mode='GRID', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - volume       : Volume 
            - voxel_size   : Float 
            - voxel_amount : Float 
            - threshold    : Float 
            - adaptivity   : Float 
    

            Parameters
            ----------
            - resolution_mode : 'GRID' in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - mesh : Mesh 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Volume to_mesh : Method 
    """

    def __init__(self, volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None):

        super().__init__('GeometryNodeVolumeToMesh', name='Volume to Mesh', label=label)
        # Parameters

        self.bnode.resolution_mode = resolution_mode

        # Input sockets

        self.plug(0, volume)
        self.plug(1, voxel_size)
        self.plug(2, voxel_amount)
        self.plug(3, threshold)
        self.plug(4, adaptivity)

        # Output sockets

        self.mesh            = self.Mesh(self.bnode.outputs[0])
        self.output_sockets  = {'mesh': self.mesh}

    @property
    def resolution_mode(self):
        return self.bnode.resolution_mode

    @resolution_mode.setter
    def resolution_mode(self, value):
        self.bnode.resolution_mode = value

# ----------------------------------------------------------------------------------------------------
# Node Clamp for ShaderNodeClamp

class Clamp(Node):

    """Class Clamp
    

    | Geometry node name: 'Clamp' 
    | Blender type:  ShaderNodeClamp 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - value : Float 
            - min   : Float 
            - max   : Float 
    

            Parameters
            ----------
            - clamp_type : 'MINMAX' in ('MINMAX', 'RANGE') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - result : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float clamp : Stacked method 
    """

    def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX', label=None):

        super().__init__('ShaderNodeClamp', name='Clamp', label=label)
        # Parameters

        self.bnode.clamp_type      = clamp_type

        # Input sockets

        self.plug(0, value)
        self.plug(1, min)
        self.plug(2, max)

        # Output sockets

        self.result          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'result': self.result}

    @property
    def clamp_type(self):
        return self.bnode.clamp_type

    @clamp_type.setter
    def clamp_type(self, value):
        self.bnode.clamp_type = value

# ----------------------------------------------------------------------------------------------------
# Node CombineRgb for ShaderNodeCombineRGB

class CombineRgb(Node):

    """Class CombineRgb
    

    | Geometry node name: 'Combine RGB' 
    | Blender type:  ShaderNodeCombineRGB 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CombineRgb(r=None, g=None, b=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - r : Float 
            - g : Float 
            - b : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - image : Color 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Color Combine : Constructor 
    """

    def __init__(self, r=None, g=None, b=None, label=None):

        super().__init__('ShaderNodeCombineRGB', name='Combine RGB', label=label)
        # Input sockets

        self.plug(0, r)
        self.plug(1, g)
        self.plug(2, b)

        # Output sockets

        self.image           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = {'image': self.image}

# ----------------------------------------------------------------------------------------------------
# Node CombineXyz for ShaderNodeCombineXYZ

class CombineXyz(Node):

    """Class CombineXyz
    

    | Geometry node name: 'Combine XYZ' 
    | Blender type:  ShaderNodeCombineXYZ 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CombineXyz(x=None, y=None, z=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - x : Float 
            - y : Float 
            - z : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vector : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector Combine : Constructor 
    """

    def __init__(self, x=None, y=None, z=None, label=None):

        super().__init__('ShaderNodeCombineXYZ', name='Combine XYZ', label=label)
        # Input sockets

        self.plug(0, x)
        self.plug(1, y)
        self.plug(2, z)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'vector': self.vector}

# ----------------------------------------------------------------------------------------------------
# Node FloatCurve for ShaderNodeFloatCurve

class FloatCurve(Node):

    """Class FloatCurve
    

    | Geometry node name: 'Float Curve' 
    | Blender type:  ShaderNodeFloatCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.FloatCurve(factor=None, value=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - factor : Float 
            - value  : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - value : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float curve : Stacked method 
    """

    def __init__(self, factor=None, value=None, label=None):

        super().__init__('ShaderNodeFloatCurve', name='Float Curve', label=label)
        # Input sockets

        self.plug(0, factor)
        self.plug(1, value)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'value': self.value}

# ----------------------------------------------------------------------------------------------------
# Node MapRange for ShaderNodeMapRange

class MapRange(Node):

    """Class MapRange
    

    | Geometry node name: 'Map Range' 
    | Blender type:  ShaderNodeMapRange 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None,
        vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - value    : Float 
            - from_min : data_type dependant 
            - from_max : data_type dependant 
            - to_min   : data_type dependant 
            - to_max   : data_type dependant 
            - steps    : data_type dependant 
            - vector   : Vector 
    

            Parameters
            ----------
            - clamp              : True bool 
            - data_type          : 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR') 
            - interpolation_type : 'LINEAR' in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Data type dependant sockets
    ===========================
    - Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR') 
    - Input sockets     : from_min from_max to_min to_max steps 
    

    Output sockets
    ==============
    - result : Float 
    - vector : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float map_range  : Method 
    - Vector map_range : Method 
    """

    def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None):

        super().__init__('ShaderNodeMapRange', name='Map Range', label=label)
        # Parameters

        self.bnode.clamp           = clamp
        self.bnode.data_type       = data_type
        self.bnode.interpolation_type = interpolation_type

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, from_min)
            self.plug(2, from_max)
            self.plug(3, to_min)
            self.plug(4, to_max)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(7, from_min)
            self.plug(8, from_max)
            self.plug(9, to_min)
            self.plug(10, to_max)

        self.plug(0, value)
        self.plug(6, vector)


        # Output sockets

        self.result          = self.Float(self.bnode.outputs[0])
        self.vector          = self.Vector(self.bnode.outputs[1])
        self.output_sockets  = {'result': self.result, 'vector': self.vector}

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

    """Class Math
    

    | Geometry node name: 'Math' 
    | Blender type:  ShaderNodeMath 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - value0 : Float 
            - value1 : Float 
            - value2 : Float 
    

            Parameters
            ----------
            - operation : 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT',
              'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE',
              'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG',
              'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH',
              'RADIANS', 'DEGREES') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - value : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float abs              : Method 
    - Float add              : Method 
    - Float arccos           : Method 
    - Float arcsin           : Method 
    - Float arctan           : Method 
    - Float arctan2          : Method 
    - Float ceil             : Method 
    - Float compare          : Method 
    - Float cos              : Method 
    - Float cosh             : Method 
    - Float degrees          : Method 
    - Float divide           : Method 
    - Float exp              : Method 
    - Float floor            : Method 
    - Float fract            : Method 
    - Float greater_than     : Method 
    - Float inverse_sqrt     : Method 
    - Float less_than        : Method 
    - Float log              : Method 
    - Float max              : Method 
    - Float min              : Method 
    - Float modulo           : Method 
    - Float multiply         : Method 
    - Float multiply_add     : Method 
    - Float pingpong         : Method 
    - Float pow              : Method 
    - Float radians          : Method 
    - Float round            : Method 
    - Float sign             : Method 
    - Float sin              : Method 
    - Float sinh             : Method 
    - Float smooth_max       : Method 
    - Float smooth_min       : Method 
    - Float snap             : Method 
    - Float sqrt             : Method 
    - Float subtract         : Method 
    - Float tan              : Method 
    - Float tanh             : Method 
    - Float trunc            : Method 
    - Float wrap             : Method 
    - Integer abs            : Method 
    - Integer add            : Method 
    - Integer arccos         : Method 
    - Integer arcsin         : Method 
    - Integer arctan         : Method 
    - Integer arctan2        : Method 
    - Integer ceil           : Method 
    - Integer compare        : Method 
    - Integer cos            : Method 
    - Integer cosh           : Method 
    - Integer degrees        : Method 
    - Integer divide         : Method 
    - Integer exp            : Method 
    - Integer floor          : Method 
    - Integer fract          : Method 
    - Integer greater_than   : Method 
    - Integer inverse_sqrt   : Method 
    - Integer less_than      : Method 
    - Integer log            : Method 
    - Integer max            : Method 
    - Integer min            : Method 
    - Integer modulo         : Method 
    - Integer multiply       : Method 
    - Integer multiply_add   : Method 
    - Integer pingpong       : Method 
    - Integer pow            : Method 
    - Integer radians        : Method 
    - Integer round          : Method 
    - Integer sign           : Method 
    - Integer sin            : Method 
    - Integer sinh           : Method 
    - Integer smooth_max     : Method 
    - Integer smooth_min     : Method 
    - Integer snap           : Method 
    - Integer sqrt           : Method 
    - Integer subtract       : Method 
    - Integer tan            : Method 
    - Integer tanh           : Method 
    - Integer trunc          : Method 
    - Integer wrap           : Method 
    - functions abs          : Function 
    - functions add          : Function 
    - functions arccos       : Function 
    - functions arcsin       : Function 
    - functions arctan       : Function 
    - functions arctan2      : Function 
    - functions ceil         : Function 
    - functions compare      : Function 
    - functions cos          : Function 
    - functions cosh         : Function 
    - functions degrees      : Function 
    - functions divide       : Function 
    - functions exp          : Function 
    - functions floor        : Function 
    - functions fract        : Function 
    - functions greater_than : Function 
    - functions inverse_sqrt : Function 
    - functions less_than    : Function 
    - functions log          : Function 
    - functions max          : Function 
    - functions min          : Function 
    - functions modulo       : Function 
    - functions multiply     : Function 
    - functions multiply_add : Function 
    - functions pingpong     : Function 
    - functions pow          : Function 
    - functions radians      : Function 
    - functions round        : Function 
    - functions sign         : Function 
    - functions sin          : Function 
    - functions sinh         : Function 
    - functions smooth_max   : Function 
    - functions smooth_min   : Function 
    - functions snap         : Function 
    - functions sqrt         : Function 
    - functions subtract     : Function 
    - functions tan          : Function 
    - functions tanh         : Function 
    - functions trunc        : Function 
    - functions wrap         : Function 
    """

    def __init__(self, value0=None, value1=None, value2=None, operation='ADD', label=None):

        super().__init__('ShaderNodeMath', name='Math', label=label)
        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(0, value0)
        self.plug(1, value1)
        self.plug(2, value2)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'value': self.value}

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

# ----------------------------------------------------------------------------------------------------
# Node Mix for ShaderNodeMixRGB

class Mix(Node):

    """Class Mix
    

    | Geometry node name: 'Mix' 
    | Blender type:  ShaderNodeMixRGB 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Mix(color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - fac    : Float 
            - color1 : Color 
            - color2 : Color 
    

            Parameters
            ----------
            - blend_type : 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY',
              'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
            - use_alpha  : False bool 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Color add                    : Method 
    - Color burn                   : Method 
    - Color darken                 : Method 
    - Color difference             : Method 
    - Color divide                 : Method 
    - Color dodge                  : Method 
    - Color hue                    : Method 
    - Color lighten                : Method 
    - Color linear_light           : Method 
    - Color mix                    : Method 
    - Color mix                    : Method 
    - Color mix_color              : Method 
    - Color multiply               : Method 
    - Color overlay                : Method 
    - Color saturation             : Method 
    - Color screen                 : Method 
    - Color soft_light             : Method 
    - Color subtract               : Method 
    - Color value                  : Method 
    - functions color_add          : Function 
    - functions color_burn         : Function 
    - functions color_darken       : Function 
    - functions color_difference   : Function 
    - functions color_divide       : Function 
    - functions color_dodge        : Function 
    - functions color_hue          : Function 
    - functions color_lighten      : Function 
    - functions color_linear_light : Function 
    - functions color_mix          : Function 
    - functions color_mix_color    : Function 
    - functions color_multiply     : Function 
    - functions color_overlay      : Function 
    - functions color_saturation   : Function 
    - functions color_screen       : Function 
    - functions color_soft_light   : Function 
    - functions color_subtract     : Function 
    - functions color_value        : Function 
    """

    def __init__(self, color1=None, color2=None, fac=None, blend_type='MIX', use_alpha=False, label=None):

        super().__init__('ShaderNodeMixRGB', name='Mix', label=label)
        # Parameters

        self.bnode.blend_type      = blend_type
        self.bnode.use_alpha       = use_alpha

        # Input sockets

        self.plug(1, color1)
        self.plug(2, color2)
        self.plug(0, fac)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = {'color': self.color}

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

    """Class RgbCurves
    

    | Geometry node name: 'RGB Curves' 
    | Blender type:  ShaderNodeRGBCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.RgbCurves(fac=None, color=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - fac   : Float 
            - color : Color 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Color curves : Stacked method 
    """

    def __init__(self, fac=None, color=None, label=None):

        super().__init__('ShaderNodeRGBCurve', name='RGB Curves', label=label)
        # Input sockets

        self.plug(0, fac)
        self.plug(1, color)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = {'color': self.color}

# ----------------------------------------------------------------------------------------------------
# Node SeparateRgb for ShaderNodeSeparateRGB

class SeparateRgb(Node):

    """Class SeparateRgb
    

    | Geometry node name: 'Separate RGB' 
    | Blender type:  ShaderNodeSeparateRGB 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SeparateRgb(image=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - image : Color 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - r : Float 
    - g : Float 
    - b : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Color separate : Property 
    """

    def __init__(self, image=None, label=None):

        super().__init__('ShaderNodeSeparateRGB', name='Separate RGB', label=label)
        # Input sockets

        self.plug(0, image)

        # Output sockets

        self.r               = self.Float(self.bnode.outputs[0])
        self.g               = self.Float(self.bnode.outputs[1])
        self.b               = self.Float(self.bnode.outputs[2])
        self.output_sockets  = {'r': self.r, 'g': self.g, 'b': self.b}

# ----------------------------------------------------------------------------------------------------
# Node SeparateXyz for ShaderNodeSeparateXYZ

class SeparateXyz(Node):

    """Class SeparateXyz
    

    | Geometry node name: 'Separate XYZ' 
    | Blender type:  ShaderNodeSeparateXYZ 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.SeparateXyz(vector=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector : Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - x : Float 
    - y : Float 
    - z : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector separate : Property 
    """

    def __init__(self, vector=None, label=None):

        super().__init__('ShaderNodeSeparateXYZ', name='Separate XYZ', label=label)
        # Input sockets

        self.plug(0, vector)

        # Output sockets

        self.x               = self.Float(self.bnode.outputs[0])
        self.y               = self.Float(self.bnode.outputs[1])
        self.z               = self.Float(self.bnode.outputs[2])
        self.output_sockets  = {'x': self.x, 'y': self.y, 'z': self.z}

# ----------------------------------------------------------------------------------------------------
# Node BrickTexture for ShaderNodeTexBrick

class BrickTexture(Node):

    """Class BrickTexture
    

    | Geometry node name: 'Brick Texture' 
    | Blender type:  ShaderNodeTexBrick 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None,
        mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0,
        squash_frequency=2, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector        : Vector 
            - color1        : Color 
            - color2        : Color 
            - mortar        : Color 
            - scale         : Float 
            - mortar_size   : Float 
            - mortar_smooth : Float 
            - bias          : Float 
            - brick_width   : Float 
            - row_height    : Float 
    

            Parameters
            ----------
            - offset           : 0.5 float 
            - offset_frequency : 2 int 
            - squash           : 1.0 float 
            - squash_frequency : 2 int 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - fac   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Brick : Static method 
    """

    def __init__(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None):

        super().__init__('ShaderNodeTexBrick', name='Brick Texture', label=label)
        # Parameters

        self.bnode.offset          = offset
        self.bnode.offset_frequency = offset_frequency
        self.bnode.squash          = squash
        self.bnode.squash_frequency = squash_frequency

        # Input sockets

        self.plug(0, vector)
        self.plug(1, color1)
        self.plug(2, color2)
        self.plug(3, mortar)
        self.plug(4, scale)
        self.plug(5, mortar_size)
        self.plug(6, mortar_smooth)
        self.plug(7, bias)
        self.plug(8, brick_width)
        self.plug(9, row_height)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'fac': self.fac}

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

    """Class CheckerTexture
    

    | Geometry node name: 'Checker Texture' 
    | Blender type:  ShaderNodeTexChecker 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.CheckerTexture(vector=None, color1=None, color2=None, scale=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector : Vector 
            - color1 : Color 
            - color2 : Color 
            - scale  : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - fac   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Checker : Static method 
    """

    def __init__(self, vector=None, color1=None, color2=None, scale=None, label=None):

        super().__init__('ShaderNodeTexChecker', name='Checker Texture', label=label)
        # Input sockets

        self.plug(0, vector)
        self.plug(1, color1)
        self.plug(2, color2)
        self.plug(3, scale)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'fac': self.fac}

# ----------------------------------------------------------------------------------------------------
# Node GradientTexture for ShaderNodeTexGradient

class GradientTexture(Node):

    """Class GradientTexture
    

    | Geometry node name: 'Gradient Texture' 
    | Blender type:  ShaderNodeTexGradient 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.GradientTexture(vector=None, gradient_type='LINEAR', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector : Vector 
    

            Parameters
            ----------
            - gradient_type : 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE',
              'RADIAL') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - fac   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Gradient : Static method 
    """

    def __init__(self, vector=None, gradient_type='LINEAR', label=None):

        super().__init__('ShaderNodeTexGradient', name='Gradient Texture', label=label)
        # Parameters

        self.bnode.gradient_type   = gradient_type

        # Input sockets

        self.plug(0, vector)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'fac': self.fac}

    @property
    def gradient_type(self):
        return self.bnode.gradient_type

    @gradient_type.setter
    def gradient_type(self, value):
        self.bnode.gradient_type = value

# ----------------------------------------------------------------------------------------------------
# Node MagicTexture for ShaderNodeTexMagic

class MagicTexture(Node):

    """Class MagicTexture
    

    | Geometry node name: 'Magic Texture' 
    | Blender type:  ShaderNodeTexMagic 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector     : Vector 
            - scale      : Float 
            - distortion : Float 
    

            Parameters
            ----------
            - turbulence_depth : 2 int 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - fac   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Magic : Static method 
    """

    def __init__(self, vector=None, scale=None, distortion=None, turbulence_depth=2, label=None):

        super().__init__('ShaderNodeTexMagic', name='Magic Texture', label=label)
        # Parameters

        self.bnode.turbulence_depth = turbulence_depth

        # Input sockets

        self.plug(0, vector)
        self.plug(1, scale)
        self.plug(2, distortion)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'fac': self.fac}

    @property
    def turbulence_depth(self):
        return self.bnode.turbulence_depth

    @turbulence_depth.setter
    def turbulence_depth(self, value):
        self.bnode.turbulence_depth = value

# ----------------------------------------------------------------------------------------------------
# Node MusgraveTexture for ShaderNodeTexMusgrave

class MusgraveTexture(Node):

    """Class MusgraveTexture
    

    | Geometry node name: 'Musgrave Texture' 
    | Blender type:  ShaderNodeTexMusgrave 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None,
        offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector     : Vector 
            - w          : Float 
            - scale      : Float 
            - detail     : Float 
            - dimension  : Float 
            - lacunarity : Float 
            - offset     : Float 
            - gain       : Float 
    

            Parameters
            ----------
            - musgrave_dimensions : '3D' in ('1D', '2D', '3D', '4D') 
            - musgrave_type       : 'FBM' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - fac : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Musgrave : Static method 
    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None):

        super().__init__('ShaderNodeTexMusgrave', name='Musgrave Texture', label=label)
        # Parameters

        self.bnode.musgrave_dimensions = musgrave_dimensions
        self.bnode.musgrave_type   = musgrave_type

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)
        self.plug(2, scale)
        self.plug(3, detail)
        self.plug(4, dimension)
        self.plug(5, lacunarity)
        self.plug(6, offset)
        self.plug(7, gain)

        # Output sockets

        self.fac             = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'fac': self.fac}

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

    """Class NoiseTexture
    

    | Geometry node name: 'Noise Texture' 
    | Blender type:  ShaderNodeTexNoise 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None,
        noise_dimensions='3D', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector     : Vector 
            - w          : Float 
            - scale      : Float 
            - detail     : Float 
            - roughness  : Float 
            - distortion : Float 
    

            Parameters
            ----------
            - noise_dimensions : '3D' in ('1D', '2D', '3D', '4D') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - fac   : Float 
    - color : Color 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Noise : Static method 
    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None):

        super().__init__('ShaderNodeTexNoise', name='Noise Texture', label=label)
        # Parameters

        self.bnode.noise_dimensions = noise_dimensions

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)
        self.plug(2, scale)
        self.plug(3, detail)
        self.plug(4, roughness)
        self.plug(5, distortion)

        # Output sockets

        self.fac             = self.Float(self.bnode.outputs[0])
        self.color           = self.Color(self.bnode.outputs[1])
        self.output_sockets  = {'fac': self.fac, 'color': self.color}

    @property
    def noise_dimensions(self):
        return self.bnode.noise_dimensions

    @noise_dimensions.setter
    def noise_dimensions(self, value):
        self.bnode.noise_dimensions = value

# ----------------------------------------------------------------------------------------------------
# Node VoronoiTexture for ShaderNodeTexVoronoi

class VoronoiTexture(Node):

    """Class VoronoiTexture
    

    | Geometry node name: 'Voronoi Texture' 
    | Blender type:  ShaderNodeTexVoronoi 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None,
        distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector     : Vector 
            - w          : Float 
            - scale      : Float 
            - smoothness : Float 
            - exponent   : Float 
            - randomness : Float 
    

            Parameters
            ----------
            - distance           : 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI') 
            - feature            : 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS') 
            - voronoi_dimensions : '3D' in ('1D', '2D', '3D', '4D') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - distance : Float 
    - color    : Color 
    - position : Vector 
    - w        : Float 
    - radius   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Voronoi : Static method 
    """

    def __init__(self, vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None):

        super().__init__('ShaderNodeTexVoronoi', name='Voronoi Texture', label=label)
        # Parameters

        self.bnode.distance        = distance
        self.bnode.feature         = feature
        self.bnode.voronoi_dimensions = voronoi_dimensions

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)
        self.plug(2, scale)
        self.plug(3, smoothness)
        self.plug(4, exponent)
        self.plug(5, randomness)

        # Output sockets

        self.distance        = self.Float(self.bnode.outputs[0])
        self.color           = self.Color(self.bnode.outputs[1])
        self.position        = self.Vector(self.bnode.outputs[2])
        self.w               = self.Float(self.bnode.outputs[3])
        self.radius          = self.Float(self.bnode.outputs[4])
        self.output_sockets  = {'distance': self.distance, 'color': self.color, 'position': self.position, 'w': self.w, 'radius': self.radius}

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

    """Class WaveTexture
    

    | Geometry node name: 'Wave Texture' 
    | Blender type:  ShaderNodeTexWave 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None,
        phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector           : Vector 
            - scale            : Float 
            - distortion       : Float 
            - detail           : Float 
            - detail_scale     : Float 
            - detail_roughness : Float 
            - phase_offset     : Float 
    

            Parameters
            ----------
            - bands_direction : 'X' in ('X', 'Y', 'Z', 'DIAGONAL') 
            - rings_direction : 'X' in ('X', 'Y', 'Z', 'SPHERICAL') 
            - wave_profile    : 'SIN' in ('SIN', 'SAW', 'TRI') 
            - wave_type       : 'BANDS' in ('BANDS', 'RINGS') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - fac   : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture Wave : Static method 
    """

    def __init__(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None):

        super().__init__('ShaderNodeTexWave', name='Wave Texture', label=label)
        # Parameters

        self.bnode.bands_direction = bands_direction
        self.bnode.rings_direction = rings_direction
        self.bnode.wave_profile    = wave_profile
        self.bnode.wave_type       = wave_type

        # Input sockets

        self.plug(0, vector)
        self.plug(1, scale)
        self.plug(2, distortion)
        self.plug(3, detail)
        self.plug(4, detail_scale)
        self.plug(5, detail_roughness)
        self.plug(6, phase_offset)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'fac': self.fac}

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

    """Class WhiteNoiseTexture
    

    | Geometry node name: 'White Noise Texture' 
    | Blender type:  ShaderNodeTexWhiteNoise 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector : Vector 
            - w      : Float 
    

            Parameters
            ----------
            - noise_dimensions : '3D' in ('1D', '2D', '3D', '4D') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - value : Float 
    - color : Color 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Texture WhiteNoise : Static method 
    """

    def __init__(self, vector=None, w=None, noise_dimensions='3D', label=None):

        super().__init__('ShaderNodeTexWhiteNoise', name='White Noise Texture', label=label)
        # Parameters

        self.bnode.noise_dimensions = noise_dimensions

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.color           = self.Color(self.bnode.outputs[1])
        self.output_sockets  = {'value': self.value, 'color': self.color}

    @property
    def noise_dimensions(self):
        return self.bnode.noise_dimensions

    @noise_dimensions.setter
    def noise_dimensions(self, value):
        self.bnode.noise_dimensions = value

# ----------------------------------------------------------------------------------------------------
# Node Colorramp for ShaderNodeValToRGB

class Colorramp(Node):

    """Class Colorramp
    

    | Geometry node name: 'ColorRamp' 
    | Blender type:  ShaderNodeValToRGB 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Colorramp(fac=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - fac : Float 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - color : Color 
    - alpha : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Float color_ramp : Method 
    """

    def __init__(self, fac=None, label=None):

        super().__init__('ShaderNodeValToRGB', name='ColorRamp', label=label)
        # Input sockets

        self.plug(0, fac)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.alpha           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'color': self.color, 'alpha': self.alpha}

# ----------------------------------------------------------------------------------------------------
# Node Value for ShaderNodeValue

class Value(Node):

    """Class Value
    

    | Geometry node name: 'Value' 
    | Blender type:  ShaderNodeValue 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.Value(label=None) 
    

        Arguments
        ---------
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - value : Float 
    """

    def __init__(self, label=None):

        super().__init__('ShaderNodeValue', name='Value', label=label)
        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'value': self.value}

# ----------------------------------------------------------------------------------------------------
# Node VectorCurves for ShaderNodeVectorCurve

class VectorCurves(Node):

    """Class VectorCurves
    

    | Geometry node name: 'Vector Curves' 
    | Blender type:  ShaderNodeVectorCurve 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.VectorCurves(fac=None, vector=None, label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - fac    : Float 
            - vector : Vector 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vector : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector curves : Stacked method 
    """

    def __init__(self, fac=None, vector=None, label=None):

        super().__init__('ShaderNodeVectorCurve', name='Vector Curves', label=label)
        # Input sockets

        self.plug(0, fac)
        self.plug(1, vector)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'vector': self.vector}

# ----------------------------------------------------------------------------------------------------
# Node VectorMath for ShaderNodeVectorMath

class VectorMath(Node):

    """Class VectorMath
    

    | Geometry node name: 'Vector Math' 
    | Blender type:  ShaderNodeVectorMath 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.VectorMath(vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None)
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector0 : Vector 
            - vector1 : Vector 
            - vector2 : Vector 
            - scale   : Float 
    

            Parameters
            ----------
            - operation : 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT',
              'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE',
              'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vector : Vector 
    - value  : Float 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector absolute               : Method 
    - Vector add                    : Method 
    - Vector ceil                   : Method 
    - Vector cos                    : Method 
    - Vector cross                  : Method 
    - Vector distance               : Method 
    - Vector divide                 : Method 
    - Vector dot                    : Method 
    - Vector faceforward            : Method 
    - Vector floor                  : Method 
    - Vector fraction               : Method 
    - Vector length                 : Method 
    - Vector max                    : Method 
    - Vector min                    : Method 
    - Vector modulo                 : Method 
    - Vector multiply               : Method 
    - Vector multiply_add           : Method 
    - Vector normalize              : Method 
    - Vector project                : Method 
    - Vector reflect                : Method 
    - Vector refract                : Method 
    - Vector scale                  : Method 
    - Vector sin                    : Method 
    - Vector snap                   : Method 
    - Vector subtract               : Method 
    - Vector tan                    : Method 
    - Vector wrap                   : Method 
    - functions cross               : Function 
    - functions distance            : Function 
    - functions dot                 : Function 
    - functions faceforward         : Function 
    - functions fraction            : Function 
    - functions length              : Function 
    - functions normalize           : Function 
    - functions project             : Function 
    - functions reflect             : Function 
    - functions refract             : Function 
    - functions scale               : Function 
    - functions vector_absolute     : Function 
    - functions vector_add          : Function 
    - functions vector_ceil         : Function 
    - functions vector_cos          : Function 
    - functions vector_divide       : Function 
    - functions vector_floor        : Function 
    - functions vector_max          : Function 
    - functions vector_min          : Function 
    - functions vector_modulo       : Function 
    - functions vector_multiply     : Function 
    - functions vector_multiply_add : Function 
    - functions vector_sin          : Function 
    - functions vector_snap         : Function 
    - functions vector_subtract     : Function 
    - functions vector_tan          : Function 
    - functions vector_wrap         : Function 
    """

    def __init__(self, vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None):

        super().__init__('ShaderNodeVectorMath', name='Vector Math', label=label)
        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(0, vector0)
        self.plug(1, vector1)
        self.plug(2, vector2)
        self.plug(3, scale)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.value           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = {'vector': self.vector, 'value': self.value}

    @property
    def operation(self):
        return self.bnode.operation

    @operation.setter
    def operation(self, value):
        self.bnode.operation = value

# ----------------------------------------------------------------------------------------------------
# Node VectorRotate for ShaderNodeVectorRotate

class VectorRotate(Node):

    """Class VectorRotate
    

    | Geometry node name: 'Vector Rotate' 
    | Blender type:  ShaderNodeVectorRotate 
    

    Initialization
    ==============
    

        from geonodes import nodes 
        node = nodes.VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False,
        rotation_type='AXIS_ANGLE', label=None) 
    

        Arguments
        ---------
    

            Input sockets
            -------------
            - vector   : Vector 
            - center   : Vector 
            - axis     : Vector 
            - angle    : Float 
            - rotation : Vector 
    

            Parameters
            ----------
            - invert        : False bool 
            - rotation_type : 'AXIS_ANGLE' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ') 
    

            Node label
            ----------
            - label : Geometry node label 
    

    Output sockets
    ==============
    - vector : Vector 
    

    Data sockets
    ============
    | Data socket classes implementing this node 
    - Vector rotate : Method 
    """

    def __init__(self, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None):

        super().__init__('ShaderNodeVectorRotate', name='Vector Rotate', label=label)
        # Parameters

        self.bnode.invert          = invert
        self.bnode.rotation_type   = rotation_type

        # Input sockets

        self.plug(0, vector)
        self.plug(1, center)
        self.plug(2, axis)
        self.plug(3, angle)
        self.plug(4, rotation)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'vector': self.vector}

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
