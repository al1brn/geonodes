from geonodes.core.node import Node

# ----------------------------------------------------------------------------------------------------
# Node AlignEulerToVector for FunctionNodeAlignEulerToVector

class AlignEulerToVector(Node):

    """Node 'Align Euler to Vector' (FunctionNodeAlignEulerToVector)

    Input sockets
    -------------
        rotation        : Vector
        factor          : Float
        vector          : Vector

    Parameters
    ----------
        axis            : 'X' in [ 'X' 'Y' 'Z']
        pivot_axis      : 'AUTO' in [ 'AUTO' 'X' 'Y' 'Z']

    Output sockets
    --------------
        rotation        : Vector
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

    """Node 'Boolean Math' (FunctionNodeBooleanMath)

    Input sockets
    -------------
        boolean0        : Boolean
        boolean1        : Boolean

    Parameters
    ----------
        operation       : 'AND' in [ 'AND' 'OR' 'NOT' 'NAND' 'NOR' 'XNOR' 'XOR' 'IMPLY' 'NIMPLY']

    Output sockets
    --------------
        boolean         : Boolean
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

    """Node 'Compare' (FunctionNodeCompare)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')

        Input sockets     : ['a', 'b']

    Input sockets
    -------------
        a               : data_type dependant
        b               : data_type dependant
        c               : Float
        angle           : Float
        epsilon         : Float

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'VECTOR' 'STRING' 'RGBA']
        mode            : 'ELEMENT' in [ 'ELEMENT' 'LENGTH' 'AVERAGE' 'DOT_PRODUCT' 'DIRECTION']
        operation       : 'GREATER_THAN' in [ 'LESS_THAN' 'LESS_EQUAL' 'GREATER_THAN' 'GREATER_EQUAL' 'EQUAL' 'NOT_EQUAL']

    Output sockets
    --------------
        result          : Boolean
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

    """Node 'Float to Integer' (FunctionNodeFloatToInt)

    Input sockets
    -------------
        float           : Float

    Parameters
    ----------
        rounding_mode   : 'ROUND' in [ 'ROUND' 'FLOOR' 'CEILING' 'TRUNCATE']

    Output sockets
    --------------
        integer         : Integer
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

    """Node 'Boolean' (FunctionNodeInputBool)

    Parameters
    ----------
        boolean         : (False) bool

    Output sockets
    --------------
        boolean         : Boolean
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

    """Node 'Color' (FunctionNodeInputColor)

    Output sockets
    --------------
        color           : Color
    """

    def __init__(self, label=None):

        super().__init__('FunctionNodeInputColor', name='Color', label=label)
        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = {'color': self.color}

# ----------------------------------------------------------------------------------------------------
# Node Integer for FunctionNodeInputInt

class Integer(Node):

    """Node 'Integer' (FunctionNodeInputInt)

    Parameters
    ----------
        integer         : (0) int

    Output sockets
    --------------
        integer         : Integer
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

    """Node 'Special Characters' (FunctionNodeInputSpecialCharacters)

    Output sockets
    --------------
        line_break      : String
        tab             : String
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

    """Node 'String' (FunctionNodeInputString)

    Parameters
    ----------
        string          : '' str

    Output sockets
    --------------
        string          : String
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

    """Node 'Vector' (FunctionNodeInputVector)

    Parameters
    ----------
        vector          : ([0.0, 0.0, 0.0]) Vector

    Output sockets
    --------------
        vector          : Vector
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

    """Node 'Random Value' (FunctionNodeRandomValue)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

        Input sockets     : ['min', 'max']
        Output sockets    : ['value']

    Input sockets
    -------------
        min             : data_type dependant
        max             : data_type dependant
        probability     : Float
        ID              : Integer
        seed            : Integer

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'BOOLEAN']

    Output sockets
    --------------
        value           : data_type dependant
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

    """Node 'Replace String' (FunctionNodeReplaceString)

    Input sockets
    -------------
        string          : String
        find            : String
        replace         : String

    Output sockets
    --------------
        string          : String
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

    """Node 'Rotate Euler' (FunctionNodeRotateEuler)

    Input sockets
    -------------
        rotation        : Vector
        rotate_by       : Vector
        axis            : Vector
        angle           : Float

    Parameters
    ----------
        space           : 'OBJECT' in [ 'OBJECT' 'LOCAL']

    Output sockets
    --------------
        rotation        : Vector
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

    """Node 'Slice String' (FunctionNodeSliceString)

    Input sockets
    -------------
        string          : String
        position        : Integer
        length          : Integer

    Output sockets
    --------------
        string          : String
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

    """Node 'String Length' (FunctionNodeStringLength)

    Input sockets
    -------------
        string          : String

    Output sockets
    --------------
        length          : Integer
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

    """Node 'Value to String' (FunctionNodeValueToString)

    Input sockets
    -------------
        value           : Float
        decimals        : Integer

    Output sockets
    --------------
        string          : String
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

    """Node 'Accumulate Field' (GeometryNodeAccumulateField)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR')

        Input sockets     : ['value']
        Output sockets    : ['leading', 'trailing', 'total']

    Input sockets
    -------------
        value           : data_type dependant
        group_index     : Integer

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        leading         : data_type dependant
        trailing        : data_type dependant
        total           : data_type dependant
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

    """Node 'Domain Size' (GeometryNodeAttributeDomainSize)

    Input sockets
    -------------
        geometry        : Geometry

    Parameters
    ----------
        component       : 'MESH' in [ 'MESH' 'POINTCLOUD' 'CURVE' 'INSTANCES']

    Output sockets
    --------------
        point_count     : Integer
        edge_count      : Integer
        face_count      : Integer
        face_corner_count : Integer
        spline_count    : Integer
        instance_count  : Integer
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

    """Node 'Attribute Remove' (GeometryNodeAttributeRemove)

    Input sockets
    -------------
        geometry        : Geometry
        attribute       : *String

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Attribute Statistic' (GeometryNodeAttributeStatistic)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')

        Input sockets     : ['attribute']
        Output sockets    : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        attribute       : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'FLOAT_VECTOR']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        mean            : data_type dependant
        median          : data_type dependant
        sum             : data_type dependant
        min             : data_type dependant
        max             : data_type dependant
        range           : data_type dependant
        standard_deviation : data_type dependant
        variance        : data_type dependant
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

    """Node 'Transfer Attribute' (GeometryNodeAttributeTransfer)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['attribute']
        Output sockets    : ['attribute']

    Input sockets
    -------------
        source          : Geometry
        attribute       : data_type dependant
        source_position : Vector
        index           : Integer

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']
        mapping         : 'NEAREST_FACE_INTERPOLATED' in [ 'NEAREST_FACE_INTERPOLATED' 'NEAREST' 'INDEX']

    Output sockets
    --------------
        attribute       : data_type dependant
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

    """Node 'Bounding Box' (GeometryNodeBoundBox)

    Input sockets
    -------------
        geometry        : Geometry

    Output sockets
    --------------
        bounding_box    : Geometry
        min             : Vector
        max             : Vector
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

    """Node 'Capture Attribute' (GeometryNodeCaptureAttribute)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['value']
        Output sockets    : ['attribute']

    Input sockets
    -------------
        geometry        : Geometry
        value           : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        geometry        : Geometry
        attribute       : data_type dependant
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

    """Node 'Collection Info' (GeometryNodeCollectionInfo)

    Input sockets
    -------------
        collection      : Collection
        separate_children : Boolean
        reset_children  : Boolean

    Parameters
    ----------
        transform_space : 'ORIGINAL' in [ 'ORIGINAL' 'RELATIVE']

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Convex Hull' (GeometryNodeConvexHull)

    Input sockets
    -------------
        geometry        : Geometry

    Output sockets
    --------------
        convex_hull     : Geometry
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

    """Node 'Arc' (GeometryNodeCurveArc)

    Input sockets
    -------------
        resolution      : Integer
        start           : Vector
        middle          : Vector
        end             : Vector
        radius          : Float
        start_angle     : Float
        sweep_angle     : Float
        offset_angle    : Float
        connect_center  : Boolean
        invert_arc      : Boolean

    Parameters
    ----------
        mode            : 'RADIUS' in [ 'POINTS' 'RADIUS']

    Output sockets
    --------------
        curve           : Curve
        center          : Vector
        normal          : Vector
        radius          : Float
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

    """Node 'Endpoint Selection' (GeometryNodeCurveEndpointSelection)

    Input sockets
    -------------
        start_size      : Integer
        end_size        : Integer

    Output sockets
    --------------
        selection       : Boolean
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

    """Node 'Handle Type Selection' (GeometryNodeCurveHandleTypeSelection)

    Parameters
    ----------
        handle_type     : 'AUTO' in [ 'FREE' 'AUTO' 'VECTOR' 'ALIGN']
        mode            : ({'RIGHT', 'LEFT'}) set

    Output sockets
    --------------
        selection       : Boolean
    """

    def __init__(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, label=None):

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

    """Node 'Curve Length' (GeometryNodeCurveLength)

    Input sockets
    -------------
        curve           : Curve

    Output sockets
    --------------
        length          : Float
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

    """Node 'Bezier Segment' (GeometryNodeCurvePrimitiveBezierSegment)

    Input sockets
    -------------
        resolution      : Integer
        start           : Vector
        start_handle    : Vector
        end_handle      : Vector
        end             : Vector

    Parameters
    ----------
        mode            : 'POSITION' in [ 'POSITION' 'OFFSET']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Curve Circle' (GeometryNodeCurvePrimitiveCircle)

    Input sockets
    -------------
        resolution      : Integer
        point_1         : Vector
        point_2         : Vector
        point_3         : Vector
        radius          : Float

    Parameters
    ----------
        mode            : 'RADIUS' in [ 'POINTS' 'RADIUS']

    Output sockets
    --------------
        curve           : Curve
        center          : Vector
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

    """Node 'Curve Line' (GeometryNodeCurvePrimitiveLine)

    Input sockets
    -------------
        start           : Vector
        end             : Vector
        direction       : Vector
        length          : Float

    Parameters
    ----------
        mode            : 'POINTS' in [ 'POINTS' 'DIRECTION']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

    Input sockets
    -------------
        width           : Float
        height          : Float
        bottom_width    : Float
        top_width       : Float
        offset          : Float
        bottom_height   : Float
        top_height      : Float
        point_1         : Vector
        point_2         : Vector
        point_3         : Vector
        point_4         : Vector

    Parameters
    ----------
        mode            : 'RECTANGLE' in [ 'RECTANGLE' 'PARALLELOGRAM' 'TRAPEZOID' 'KITE' 'POINTS']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Quadratic Bezier' (GeometryNodeCurveQuadraticBezier)

    Input sockets
    -------------
        resolution      : Integer
        start           : Vector
        middle          : Vector
        end             : Vector

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Set Handle Type' (GeometryNodeCurveSetHandles)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean

    Parameters
    ----------
        handle_type     : 'AUTO' in [ 'FREE' 'AUTO' 'VECTOR' 'ALIGN']
        mode            : ({'RIGHT', 'LEFT'}) set

    Output sockets
    --------------
        curve           : Curve
    """

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, label=None):

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

    """Node 'Spiral' (GeometryNodeCurveSpiral)

    Input sockets
    -------------
        resolution      : Integer
        rotations       : Float
        start_radius    : Float
        end_radius      : Float
        height          : Float
        reverse         : Boolean

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Set Spline Type' (GeometryNodeCurveSplineType)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean

    Parameters
    ----------
        spline_type     : 'POLY' in [ 'BEZIER' 'NURBS' 'POLY']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Star' (GeometryNodeCurveStar)

    Input sockets
    -------------
        points          : Integer
        inner_radius    : Float
        outer_radius    : Float
        twist           : Float

    Output sockets
    --------------
        curve           : Curve
        outer_points    : Boolean
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

    """Node 'Curve to Mesh' (GeometryNodeCurveToMesh)

    Input sockets
    -------------
        curve           : Curve
        profile_curve   : Geometry
        fill_caps       : Boolean

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Curve to Points' (GeometryNodeCurveToPoints)

    Input sockets
    -------------
        curve           : Curve
        count           : Integer
        length          : Float

    Parameters
    ----------
        mode            : 'COUNT' in [ 'EVALUATED' 'COUNT' 'LENGTH']

    Output sockets
    --------------
        points          : Points
        tangent         : Vector
        normal          : Vector
        rotation        : Vector
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

    """Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean

    Parameters
    ----------
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CURVE' 'INSTANCE']
        mode            : 'ALL' in [ 'ALL' 'EDGE_FACE' 'ONLY_FACE']

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Distribute Points on Faces' (GeometryNodeDistributePointsOnFaces)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean
        distance_min    : Float
        density_max     : Float
        density         : Float
        density_factor  : Float
        seed            : Integer

    Parameters
    ----------
        distribute_method : 'RANDOM' in [ 'RANDOM' 'POISSON']

    Output sockets
    --------------
        points          : Points
        normal          : Vector
        rotation        : Vector
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

    """Node 'Dual Mesh' (GeometryNodeDualMesh)

    Input sockets
    -------------
        mesh            : Mesh
        keep_boundaries : Boolean

    Output sockets
    --------------
        dual_mesh       : Geometry
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

    """Node 'Extrude Mesh' (GeometryNodeExtrudeMesh)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean
        offset          : Vector
        offset_scale    : Float
        individual      : Boolean

    Parameters
    ----------
        mode            : 'FACES' in [ 'VERTICES' 'EDGES' 'FACES']

    Output sockets
    --------------
        mesh            : Mesh
        top             : Boolean
        side            : Boolean
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

    """Node 'Field at Index' (GeometryNodeFieldAtIndex)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['value']
        Output sockets    : ['value']

    Input sockets
    -------------
        index           : Integer
        value           : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        value           : data_type dependant
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

    """Node 'Fill Curve' (GeometryNodeFillCurve)

    Input sockets
    -------------
        curve           : Curve

    Parameters
    ----------
        mode            : 'TRIANGLES' in [ 'TRIANGLES' 'NGONS']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Fillet Curve' (GeometryNodeFilletCurve)

    Input sockets
    -------------
        curve           : Curve
        count           : Integer
        radius          : Float
        limit_radius    : Boolean

    Parameters
    ----------
        mode            : 'BEZIER' in [ 'BEZIER' 'POLY']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Flip Faces' (GeometryNodeFlipFaces)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Geometry to Instance' (GeometryNodeGeometryToInstance)

    Input sockets
    -------------
        geometry        : *Geometry

    Output sockets
    --------------
        instances       : Instances
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

    """Node 'Group' (GeometryNodeGroup)

    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeGroup', name='Group', label=label)
        self.output_sockets  = {}

# ----------------------------------------------------------------------------------------------------
# Node ImageTexture for GeometryNodeImageTexture

class ImageTexture(Node):

    """Node 'Image Texture' (GeometryNodeImageTexture)

    Input sockets
    -------------
        image           : Image
        vector          : Vector
        frame           : Integer

    Parameters
    ----------
        extension       : 'REPEAT' in [ 'REPEAT' 'EXTEND' 'CLIP']
        interpolation   : 'Linear' in [ 'Linear' 'Closest' 'Cubic']

    Output sockets
    --------------
        color           : Color
        alpha           : Float
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

    """Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

    Input sockets
    -------------
        relative        : Boolean

    Output sockets
    --------------
        left            : Vector
        right           : Vector
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

    """Node 'Curve Tilt' (GeometryNodeInputCurveTilt)

    Output sockets
    --------------
        tilt            : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputCurveTilt', name='Curve Tilt', label=label)
        # Output sockets

        self.tilt            = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'tilt': self.tilt}

# ----------------------------------------------------------------------------------------------------
# Node ID for GeometryNodeInputID

class ID(Node):

    """Node 'ID' (GeometryNodeInputID)

    Output sockets
    --------------
        ID              : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputID', name='ID', label=label)
        # Output sockets

        self.ID              = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'ID': self.ID}

# ----------------------------------------------------------------------------------------------------
# Node Index for GeometryNodeInputIndex

class Index(Node):

    """Node 'Index' (GeometryNodeInputIndex)

    Output sockets
    --------------
        index           : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputIndex', name='Index', label=label)
        # Output sockets

        self.index           = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'index': self.index}

# ----------------------------------------------------------------------------------------------------
# Node Material for GeometryNodeInputMaterial

class Material(Node):

    """Node 'Material' (GeometryNodeInputMaterial)

    Output sockets
    --------------
        material        : Material
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMaterial', name='Material', label=label)
        # Output sockets

        self.material        = self.Material(self.bnode.outputs[0])
        self.output_sockets  = {'material': self.material}

# ----------------------------------------------------------------------------------------------------
# Node MaterialIndex for GeometryNodeInputMaterialIndex

class MaterialIndex(Node):

    """Node 'Material Index' (GeometryNodeInputMaterialIndex)

    Output sockets
    --------------
        material_index  : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMaterialIndex', name='Material Index', label=label)
        # Output sockets

        self.material_index  = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'material_index': self.material_index}

# ----------------------------------------------------------------------------------------------------
# Node EdgeAngle for GeometryNodeInputMeshEdgeAngle

class EdgeAngle(Node):

    """Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

    Output sockets
    --------------
        unsigned_angle  : Float
        signed_angle    : Float
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

    """Node 'Edge Neighbors' (GeometryNodeInputMeshEdgeNeighbors)

    Output sockets
    --------------
        face_count      : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', name='Edge Neighbors', label=label)
        # Output sockets

        self.face_count      = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'face_count': self.face_count}

# ----------------------------------------------------------------------------------------------------
# Node EdgeVertices for GeometryNodeInputMeshEdgeVertices

class EdgeVertices(Node):

    """Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

    Output sockets
    --------------
        vertex_index_1  : Integer
        vertex_index_2  : Integer
        position_1      : Vector
        position_2      : Vector
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

    """Node 'Face Area' (GeometryNodeInputMeshFaceArea)

    Output sockets
    --------------
        area            : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshFaceArea', name='Face Area', label=label)
        # Output sockets

        self.area            = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'area': self.area}

# ----------------------------------------------------------------------------------------------------
# Node FaceNeighbors for GeometryNodeInputMeshFaceNeighbors

class FaceNeighbors(Node):

    """Node 'Face Neighbors' (GeometryNodeInputMeshFaceNeighbors)

    Output sockets
    --------------
        vertex_count    : Integer
        face_count      : Integer
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

    """Node 'Mesh Island' (GeometryNodeInputMeshIsland)

    Output sockets
    --------------
        island_index    : Integer
        island_count    : Integer
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

    """Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

    Output sockets
    --------------
        vertex_count    : Integer
        face_count      : Integer
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

    """Node 'Normal' (GeometryNodeInputNormal)

    Output sockets
    --------------
        normal          : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputNormal', name='Normal', label=label)
        # Output sockets

        self.normal          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'normal': self.normal}

# ----------------------------------------------------------------------------------------------------
# Node Position for GeometryNodeInputPosition

class Position(Node):

    """Node 'Position' (GeometryNodeInputPosition)

    Output sockets
    --------------
        position        : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputPosition', name='Position', label=label)
        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'position': self.position}

# ----------------------------------------------------------------------------------------------------
# Node Radius for GeometryNodeInputRadius

class Radius(Node):

    """Node 'Radius' (GeometryNodeInputRadius)

    Output sockets
    --------------
        radius          : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputRadius', name='Radius', label=label)
        # Output sockets

        self.radius          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'radius': self.radius}

# ----------------------------------------------------------------------------------------------------
# Node SceneTime for GeometryNodeInputSceneTime

class SceneTime(Node):

    """Node 'Scene Time' (GeometryNodeInputSceneTime)

    Output sockets
    --------------
        seconds         : Float
        frame           : Float
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

    """Node 'Is Shade Smooth' (GeometryNodeInputShadeSmooth)

    Output sockets
    --------------
        smooth          : Boolean
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputShadeSmooth', name='Is Shade Smooth', label=label)
        # Output sockets

        self.smooth          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'smooth': self.smooth}

# ----------------------------------------------------------------------------------------------------
# Node IsSplineCyclic for GeometryNodeInputSplineCyclic

class IsSplineCyclic(Node):

    """Node 'Is Spline Cyclic' (GeometryNodeInputSplineCyclic)

    Output sockets
    --------------
        cyclic          : Boolean
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSplineCyclic', name='Is Spline Cyclic', label=label)
        # Output sockets

        self.cyclic          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'cyclic': self.cyclic}

# ----------------------------------------------------------------------------------------------------
# Node SplineResolution for GeometryNodeInputSplineResolution

class SplineResolution(Node):

    """Node 'Spline Resolution' (GeometryNodeInputSplineResolution)

    Output sockets
    --------------
        resolution      : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSplineResolution', name='Spline Resolution', label=label)
        # Output sockets

        self.resolution      = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = {'resolution': self.resolution}

# ----------------------------------------------------------------------------------------------------
# Node CurveTangent for GeometryNodeInputTangent

class CurveTangent(Node):

    """Node 'Curve Tangent' (GeometryNodeInputTangent)

    Output sockets
    --------------
        tangent         : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputTangent', name='Curve Tangent', label=label)
        # Output sockets

        self.tangent         = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = {'tangent': self.tangent}

# ----------------------------------------------------------------------------------------------------
# Node InstanceOnPoints for GeometryNodeInstanceOnPoints

class InstanceOnPoints(Node):

    """Node 'Instance on Points' (GeometryNodeInstanceOnPoints)

    Input sockets
    -------------
        points          : Points
        selection       : Boolean
        instance        : Geometry
        pick_instance   : Boolean
        instance_index  : Integer
        rotation        : Vector
        scale           : Vector

    Output sockets
    --------------
        instances       : Instances
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

    """Node 'Instances to Points' (GeometryNodeInstancesToPoints)

    Input sockets
    -------------
        instances       : Instances
        selection       : Boolean
        position        : Vector
        radius          : Float

    Output sockets
    --------------
        points          : Points
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

    """Node 'Is Viewport' (GeometryNodeIsViewport)

    Output sockets
    --------------
        is_viewport     : Boolean
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeIsViewport', name='Is Viewport', label=label)
        # Output sockets

        self.is_viewport     = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = {'is_viewport': self.is_viewport}

# ----------------------------------------------------------------------------------------------------
# Node JoinGeometry for GeometryNodeJoinGeometry

class JoinGeometry(Node):

    """Node 'Join Geometry' (GeometryNodeJoinGeometry)

    Input sockets
    -------------
        geometry        : *Geometry

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Material Selection' (GeometryNodeMaterialSelection)

    Input sockets
    -------------
        material        : Material

    Output sockets
    --------------
        selection       : Boolean
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

    """Node 'Merge by Distance' (GeometryNodeMergeByDistance)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        distance        : Float

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Mesh Boolean' (GeometryNodeMeshBoolean)

    Input sockets
    -------------
        mesh_1          : Geometry
        mesh_2          : *Geometry
        self_intersection : Boolean
        hole_tolerant   : Boolean

    Parameters
    ----------
        operation       : 'DIFFERENCE' in [ 'INTERSECT' 'UNION' 'DIFFERENCE']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Mesh Circle' (GeometryNodeMeshCircle)

    Input sockets
    -------------
        vertices        : Integer
        radius          : Float

    Parameters
    ----------
        fill_type       : 'NONE' in [ 'NONE' 'NGON' 'TRIANGLE_FAN']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Cone' (GeometryNodeMeshCone)

    Input sockets
    -------------
        vertices        : Integer
        side_segments   : Integer
        fill_segments   : Integer
        radius_top      : Float
        radius_bottom   : Float
        depth           : Float

    Parameters
    ----------
        fill_type       : 'NGON' in [ 'NONE' 'NGON' 'TRIANGLE_FAN']

    Output sockets
    --------------
        mesh            : Mesh
        top             : Boolean
        bottom          : Boolean
        side            : Boolean
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

    """Node 'Cube' (GeometryNodeMeshCube)

    Input sockets
    -------------
        size            : Vector
        vertices_x      : Integer
        vertices_y      : Integer
        vertices_z      : Integer

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Cylinder' (GeometryNodeMeshCylinder)

    Input sockets
    -------------
        vertices        : Integer
        side_segments   : Integer
        fill_segments   : Integer
        radius          : Float
        depth           : Float

    Parameters
    ----------
        fill_type       : 'NGON' in [ 'NONE' 'NGON' 'TRIANGLE_FAN']

    Output sockets
    --------------
        mesh            : Mesh
        top             : Boolean
        side            : Boolean
        bottom          : Boolean
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

    """Node 'Grid' (GeometryNodeMeshGrid)

    Input sockets
    -------------
        size_x          : Float
        size_y          : Float
        vertices_x      : Integer
        vertices_y      : Integer

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Ico Sphere' (GeometryNodeMeshIcoSphere)

    Input sockets
    -------------
        radius          : Float
        subdivisions    : Integer

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Mesh Line' (GeometryNodeMeshLine)

    Input sockets
    -------------
        count           : Integer
        resolution      : Float
        start_location  : Vector
        offset          : Vector

    Parameters
    ----------
        count_mode      : 'TOTAL' in [ 'TOTAL' 'RESOLUTION']
        mode            : 'OFFSET' in [ 'OFFSET' 'END_POINTS']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Mesh to Curve' (GeometryNodeMeshToCurve)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Mesh to Points' (GeometryNodeMeshToPoints)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean
        position        : Vector
        radius          : Float

    Parameters
    ----------
        mode            : 'VERTICES' in [ 'VERTICES' 'EDGES' 'FACES' 'CORNERS']

    Output sockets
    --------------
        points          : Points
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

    """Node 'UV Sphere' (GeometryNodeMeshUVSphere)

    Input sockets
    -------------
        segments        : Integer
        rings           : Integer
        radius          : Float

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Object Info' (GeometryNodeObjectInfo)

    Input sockets
    -------------
        object          : Object
        as_instance     : Boolean

    Parameters
    ----------
        transform_space : 'ORIGINAL' in [ 'ORIGINAL' 'RELATIVE']

    Output sockets
    --------------
        location        : Vector
        rotation        : Vector
        scale           : Vector
        geometry        : Geometry
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

    """Node 'Points to Vertices' (GeometryNodePointsToVertices)

    Input sockets
    -------------
        points          : Points
        selection       : Boolean

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Points to Volume' (GeometryNodePointsToVolume)

    Input sockets
    -------------
        points          : Points
        density         : Float
        voxel_size      : Float
        voxel_amount    : Float
        radius          : Float

    Parameters
    ----------
        resolution_mode : 'VOXEL_AMOUNT' in [ 'VOXEL_AMOUNT' 'VOXEL_SIZE']

    Output sockets
    --------------
        volume          : Volume
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

    """Node 'Geometry Proximity' (GeometryNodeProximity)

    Input sockets
    -------------
        target          : Geometry
        source_position : Vector

    Parameters
    ----------
        target_element  : 'FACES' in [ 'POINTS' 'EDGES' 'FACES']

    Output sockets
    --------------
        position        : Vector
        distance        : Float
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

    """Node 'Raycast' (GeometryNodeRaycast)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['attribute']
        Output sockets    : ['attribute']

    Input sockets
    -------------
        target_geometry : Geometry
        attribute       : data_type dependant
        source_position : Vector
        ray_direction   : Vector
        ray_length      : Float

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        mapping         : 'INTERPOLATED' in [ 'INTERPOLATED' 'NEAREST']

    Output sockets
    --------------
        is_hit          : Boolean
        hit_position    : Vector
        hit_normal      : Vector
        hit_distance    : Float
        attribute       : data_type dependant
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

    """Node 'Realize Instances' (GeometryNodeRealizeInstances)

    Input sockets
    -------------
        geometry        : Geometry

    Parameters
    ----------
        legacy_behavior : (False) bool

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Replace Material' (GeometryNodeReplaceMaterial)

    Input sockets
    -------------
        geometry        : Geometry
        old             : Material
        new             : Material

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Resample Curve' (GeometryNodeResampleCurve)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean
        count           : Integer
        length          : Float

    Parameters
    ----------
        mode            : 'COUNT' in [ 'EVALUATED' 'COUNT' 'LENGTH']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Reverse Curve' (GeometryNodeReverseCurve)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Rotate Instances' (GeometryNodeRotateInstances)

    Input sockets
    -------------
        instances       : Instances
        selection       : Boolean
        rotation        : Vector
        pivot_point     : Vector
        local_space     : Boolean

    Output sockets
    --------------
        instances       : Instances
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

    """Node 'Sample Curve' (GeometryNodeSampleCurve)

    Input sockets
    -------------
        curve           : Curve
        factor          : Float
        length          : Float

    Parameters
    ----------
        mode            : 'LENGTH' in [ 'FACTOR' 'LENGTH']

    Output sockets
    --------------
        position        : Vector
        tangent         : Vector
        normal          : Vector
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

    """Node 'Scale Elements' (GeometryNodeScaleElements)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        scale           : Float
        center          : Vector
        axis            : Vector

    Parameters
    ----------
        domain          : 'FACE' in [ 'FACE' 'EDGE']
        scale_mode      : 'UNIFORM' in [ 'UNIFORM' 'SINGLE_AXIS']

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Scale Instances' (GeometryNodeScaleInstances)

    Input sockets
    -------------
        instances       : Instances
        selection       : Boolean
        scale           : Vector
        center          : Vector
        local_space     : Boolean

    Output sockets
    --------------
        instances       : Instances
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

    """Node 'Separate Components' (GeometryNodeSeparateComponents)

    Input sockets
    -------------
        geometry        : Geometry

    Output sockets
    --------------
        mesh            : Mesh
        point_cloud     : Geometry
        curve           : Curve
        volume          : Volume
        instances       : Instances
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

    """Node 'Separate Geometry' (GeometryNodeSeparateGeometry)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean

    Parameters
    ----------
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        selection       : Geometry
        inverted        : Geometry
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

    """Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean
        position        : Vector
        offset          : Vector

    Parameters
    ----------
        mode            : 'LEFT' in [ 'LEFT' 'RIGHT']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Set Curve Radius' (GeometryNodeSetCurveRadius)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean
        radius          : Float

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Set Curve Tilt' (GeometryNodeSetCurveTilt)

    Input sockets
    -------------
        curve           : Curve
        selection       : Boolean
        tilt            : Float

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Set ID' (GeometryNodeSetID)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        ID              : Integer

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Set Material' (GeometryNodeSetMaterial)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        material        : Material

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Set Material Index' (GeometryNodeSetMaterialIndex)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        material_index  : Integer

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Set Point Radius' (GeometryNodeSetPointRadius)

    Input sockets
    -------------
        points          : Points
        selection       : Boolean
        radius          : Float

    Output sockets
    --------------
        points          : Points
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

    """Node 'Set Position' (GeometryNodeSetPosition)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        position        : Vector
        offset          : Vector

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Set Shade Smooth' (GeometryNodeSetShadeSmooth)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        shade_smooth    : Boolean

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Set Spline Cyclic' (GeometryNodeSetSplineCyclic)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        cyclic          : Boolean

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Set Spline Resolution' (GeometryNodeSetSplineResolution)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        resolution      : Integer

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Spline Length' (GeometryNodeSplineLength)

    Output sockets
    --------------
        length          : Float
        point_count     : Integer
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

    """Node 'Spline Parameter' (GeometryNodeSplineParameter)

    Output sockets
    --------------
        factor          : Float
        length          : Float
        index           : Integer
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

    """Node 'Split Edges' (GeometryNodeSplitEdges)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Join Strings' (GeometryNodeStringJoin)

    Input sockets
    -------------
        delimiter       : String
        strings         : *String

    Output sockets
    --------------
        string          : String
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

    """Node 'String to Curves' (GeometryNodeStringToCurves)

    Input sockets
    -------------
        string          : String
        size            : Float
        character_spacing : Float
        word_spacing    : Float
        line_spacing    : Float
        text_box_width  : Float
        text_box_height : Float

    Parameters
    ----------
        align_x         : 'LEFT' in [ 'LEFT' 'CENTER' 'RIGHT' 'JUSTIFY' 'FLUSH']
        align_y         : 'TOP_BASELINE' in [ 'TOP_BASELINE' 'TOP' 'MIDDLE' 'BOTTOM_BASELINE' 'BOTTOM']
        overflow        : 'OVERFLOW' in [ 'OVERFLOW' 'SCALE_TO_FIT' 'TRUNCATE']
        pivot_mode      : 'BOTTOM_LEFT' in [ 'MIDPOINT' 'TOP_LEFT' 'TOP_CENTER' 'TOP_RIGHT' 'BOTTOM_LEFT' 'BOTTOM_CENTER' 'BOTTOM_RIGHT']

    Output sockets
    --------------
        curve_instances : Geometry
        remainder       : String
        line            : Integer
        pivot_point     : Vector
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

    """Node 'Subdivide Curve' (GeometryNodeSubdivideCurve)

    Input sockets
    -------------
        curve           : Curve
        cuts            : Integer

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Subdivide Mesh' (GeometryNodeSubdivideMesh)

    Input sockets
    -------------
        mesh            : Mesh
        level           : Integer

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Subdivision Surface' (GeometryNodeSubdivisionSurface)

    Input sockets
    -------------
        mesh            : Mesh
        level           : Integer
        crease          : Float

    Parameters
    ----------
        boundary_smooth : 'ALL' in [ 'PRESERVE_CORNERS' 'ALL']
        uv_smooth       : 'PRESERVE_BOUNDARIES' in [ 'NONE' 'PRESERVE_CORNERS' 'PRESERVE_CORNERS_AND_JUNCTIONS' 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE',
                             'PRESERVE_BOUNDARIES' 'SMOOTH_ALL']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Switch' (GeometryNodeSwitch)

    Data type dependant sockets
    ---------------------------

        Driving parameter : input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')

        Input sockets     : ['false', 'true']
        Output sockets    : ['output']

    Input sockets
    -------------
        switch0         : Boolean
        switch1         : Boolean
        false           : input_type dependant
        true            : input_type dependant

    Parameters
    ----------
        input_type      : 'GEOMETRY' in [ 'FLOAT' 'INT' 'BOOLEAN' 'VECTOR' 'STRING' 'RGBA' 'OBJECT' 'IMAGE' 'GEOMETRY' 'COLLECTION' 'TEXTURE',
                             'MATERIAL']

    Output sockets
    --------------
        output          : input_type dependant
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

    """Node 'Transform' (GeometryNodeTransform)

    Input sockets
    -------------
        geometry        : Geometry
        translation     : Vector
        rotation        : Vector
        scale           : Vector

    Output sockets
    --------------
        geometry        : Geometry
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

    """Node 'Translate Instances' (GeometryNodeTranslateInstances)

    Input sockets
    -------------
        instances       : Instances
        selection       : Boolean
        translation     : Vector
        local_space     : Boolean

    Output sockets
    --------------
        instances       : Instances
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

    """Node 'Triangulate' (GeometryNodeTriangulate)

    Input sockets
    -------------
        mesh            : Mesh
        selection       : Boolean
        minimum_vertices : Integer

    Parameters
    ----------
        ngon_method     : 'BEAUTY' in [ 'BEAUTY' 'CLIP']
        quad_method     : 'SHORTEST_DIAGONAL' in [ 'BEAUTY' 'FIXED' 'FIXED_ALTERNATE' 'SHORTEST_DIAGONAL' 'LONGEST_DIAGONAL']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Trim Curve' (GeometryNodeTrimCurve)

    Input sockets
    -------------
        curve           : Curve
        start0          : Float
        start1          : Float
        end0            : Float
        end1            : Float

    Parameters
    ----------
        mode            : 'FACTOR' in [ 'FACTOR' 'LENGTH']

    Output sockets
    --------------
        curve           : Curve
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

    """Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

    Input sockets
    -------------
        volume          : Volume
        voxel_size      : Float
        voxel_amount    : Float
        threshold       : Float
        adaptivity      : Float

    Parameters
    ----------
        resolution_mode : 'GRID' in [ 'GRID' 'VOXEL_AMOUNT' 'VOXEL_SIZE']

    Output sockets
    --------------
        mesh            : Mesh
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

    """Node 'Clamp' (ShaderNodeClamp)

    Input sockets
    -------------
        value           : Float
        min             : Float
        max             : Float

    Parameters
    ----------
        clamp_type      : 'MINMAX' in [ 'MINMAX' 'RANGE']

    Output sockets
    --------------
        result          : Float
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

    """Node 'Combine RGB' (ShaderNodeCombineRGB)

    Input sockets
    -------------
        r               : Float
        g               : Float
        b               : Float

    Output sockets
    --------------
        image           : Color
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

    """Node 'Combine XYZ' (ShaderNodeCombineXYZ)

    Input sockets
    -------------
        x               : Float
        y               : Float
        z               : Float

    Output sockets
    --------------
        vector          : Vector
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

    """Node 'Float Curve' (ShaderNodeFloatCurve)

    Input sockets
    -------------
        factor          : Float
        value           : Float

    Output sockets
    --------------
        value           : Float
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

    """Node 'Map Range' (ShaderNodeMapRange)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')

        Input sockets     : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']

    Input sockets
    -------------
        value           : Float
        from_min        : data_type dependant
        from_max        : data_type dependant
        to_min          : data_type dependant
        to_max          : data_type dependant
        steps           : data_type dependant
        vector          : Vector

    Parameters
    ----------
        clamp           : (True) bool
        data_type       : 'FLOAT' in [ 'FLOAT' 'FLOAT_VECTOR']
        interpolation_type : 'LINEAR' in [ 'LINEAR' 'STEPPED' 'SMOOTHSTEP' 'SMOOTHERSTEP']

    Output sockets
    --------------
        result          : Float
        vector          : Vector
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

    """Node 'Math' (ShaderNodeMath)

    Input sockets
    -------------
        value0          : Float
        value1          : Float
        value2          : Float

    Parameters
    ----------
        operation       : 'ADD' in [ 'ADD' 'SUBTRACT' 'MULTIPLY' 'DIVIDE' 'MULTIPLY_ADD' 'POWER' 'LOGARITHM' 'SQRT' 'INVERSE_SQRT' 'ABSOLUTE',
                             'EXPONENT' 'MINIMUM' 'MAXIMUM' 'LESS_THAN' 'GREATER_THAN' 'SIGN' 'COMPARE' 'SMOOTH_MIN' 'SMOOTH_MAX',
                             'ROUND' 'FLOOR' 'CEIL' 'TRUNC' 'FRACT' 'MODULO' 'WRAP' 'SNAP' 'PINGPONG' 'SINE' 'COSINE' 'TANGENT' 'ARCSINE',
                             'ARCCOSINE' 'ARCTANGENT' 'ARCTAN2' 'SINH' 'COSH' 'TANH' 'RADIANS' 'DEGREES']

    Output sockets
    --------------
        value           : Float
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

    """Node 'Mix' (ShaderNodeMixRGB)

    Input sockets
    -------------
        fac             : Float
        color1          : Color
        color2          : Color

    Parameters
    ----------
        blend_type      : 'MIX' in [ 'MIX' 'DARKEN' 'MULTIPLY' 'BURN' 'LIGHTEN' 'SCREEN' 'DODGE' 'ADD' 'OVERLAY' 'SOFT_LIGHT' 'LINEAR_LIGHT',
                             'DIFFERENCE' 'SUBTRACT' 'DIVIDE' 'HUE' 'SATURATION' 'COLOR' 'VALUE']
        use_alpha       : (False) bool

    Output sockets
    --------------
        color           : Color
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

    """Node 'RGB Curves' (ShaderNodeRGBCurve)

    Input sockets
    -------------
        fac             : Float
        color           : Color

    Output sockets
    --------------
        color           : Color
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

    """Node 'Separate RGB' (ShaderNodeSeparateRGB)

    Input sockets
    -------------
        image           : Color

    Output sockets
    --------------
        r               : Float
        g               : Float
        b               : Float
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

    """Node 'Separate XYZ' (ShaderNodeSeparateXYZ)

    Input sockets
    -------------
        vector          : Vector

    Output sockets
    --------------
        x               : Float
        y               : Float
        z               : Float
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

    """Node 'Brick Texture' (ShaderNodeTexBrick)

    Input sockets
    -------------
        vector          : Vector
        color1          : Color
        color2          : Color
        mortar          : Color
        scale           : Float
        mortar_size     : Float
        mortar_smooth   : Float
        bias            : Float
        brick_width     : Float
        row_height      : Float

    Parameters
    ----------
        offset          : (0.5) float
        offset_frequency : (2) int
        squash          : (1.0) float
        squash_frequency : (2) int

    Output sockets
    --------------
        color           : Color
        fac             : Float
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

    """Node 'Checker Texture' (ShaderNodeTexChecker)

    Input sockets
    -------------
        vector          : Vector
        color1          : Color
        color2          : Color
        scale           : Float

    Output sockets
    --------------
        color           : Color
        fac             : Float
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

    """Node 'Gradient Texture' (ShaderNodeTexGradient)

    Input sockets
    -------------
        vector          : Vector

    Parameters
    ----------
        gradient_type   : 'LINEAR' in [ 'LINEAR' 'QUADRATIC' 'EASING' 'DIAGONAL' 'SPHERICAL' 'QUADRATIC_SPHERE' 'RADIAL']

    Output sockets
    --------------
        color           : Color
        fac             : Float
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

    """Node 'Magic Texture' (ShaderNodeTexMagic)

    Input sockets
    -------------
        vector          : Vector
        scale           : Float
        distortion      : Float

    Parameters
    ----------
        turbulence_depth : (2) int

    Output sockets
    --------------
        color           : Color
        fac             : Float
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

    """Node 'Musgrave Texture' (ShaderNodeTexMusgrave)

    Input sockets
    -------------
        vector          : Vector
        w               : Float
        scale           : Float
        detail          : Float
        dimension       : Float
        lacunarity      : Float
        offset          : Float
        gain            : Float

    Parameters
    ----------
        musgrave_dimensions : '3D' in [ '1D' '2D' '3D' '4D']
        musgrave_type   : 'FBM' in [ 'MULTIFRACTAL' 'RIDGED_MULTIFRACTAL' 'HYBRID_MULTIFRACTAL' 'FBM' 'HETERO_TERRAIN']

    Output sockets
    --------------
        fac             : Float
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

    """Node 'Noise Texture' (ShaderNodeTexNoise)

    Input sockets
    -------------
        vector          : Vector
        w               : Float
        scale           : Float
        detail          : Float
        roughness       : Float
        distortion      : Float

    Parameters
    ----------
        noise_dimensions : '3D' in [ '1D' '2D' '3D' '4D']

    Output sockets
    --------------
        fac             : Float
        color           : Color
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

    """Node 'Voronoi Texture' (ShaderNodeTexVoronoi)

    Input sockets
    -------------
        vector          : Vector
        w               : Float
        scale           : Float
        smoothness      : Float
        exponent        : Float
        randomness      : Float

    Parameters
    ----------
        distance        : 'EUCLIDEAN' in [ 'EUCLIDEAN' 'MANHATTAN' 'CHEBYCHEV' 'MINKOWSKI']
        feature         : 'F1' in [ 'F1' 'F2' 'SMOOTH_F1' 'DISTANCE_TO_EDGE' 'N_SPHERE_RADIUS']
        voronoi_dimensions : '3D' in [ '1D' '2D' '3D' '4D']

    Output sockets
    --------------
        distance        : Float
        color           : Color
        position        : Vector
        w               : Float
        radius          : Float
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

    """Node 'Wave Texture' (ShaderNodeTexWave)

    Input sockets
    -------------
        vector          : Vector
        scale           : Float
        distortion      : Float
        detail          : Float
        detail_scale    : Float
        detail_roughness : Float
        phase_offset    : Float

    Parameters
    ----------
        bands_direction : 'X' in [ 'X' 'Y' 'Z' 'DIAGONAL']
        rings_direction : 'X' in [ 'X' 'Y' 'Z' 'SPHERICAL']
        wave_profile    : 'SIN' in [ 'SIN' 'SAW' 'TRI']
        wave_type       : 'BANDS' in [ 'BANDS' 'RINGS']

    Output sockets
    --------------
        color           : Color
        fac             : Float
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

    """Node 'White Noise Texture' (ShaderNodeTexWhiteNoise)

    Input sockets
    -------------
        vector          : Vector
        w               : Float

    Parameters
    ----------
        noise_dimensions : '3D' in [ '1D' '2D' '3D' '4D']

    Output sockets
    --------------
        value           : Float
        color           : Color
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

    """Node 'ColorRamp' (ShaderNodeValToRGB)

    Input sockets
    -------------
        fac             : Float

    Output sockets
    --------------
        color           : Color
        alpha           : Float
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

    """Node 'Value' (ShaderNodeValue)

    Output sockets
    --------------
        value           : Float
    """

    def __init__(self, label=None):

        super().__init__('ShaderNodeValue', name='Value', label=label)
        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = {'value': self.value}

# ----------------------------------------------------------------------------------------------------
# Node VectorCurves for ShaderNodeVectorCurve

class VectorCurves(Node):

    """Node 'Vector Curves' (ShaderNodeVectorCurve)

    Input sockets
    -------------
        fac             : Float
        vector          : Vector

    Output sockets
    --------------
        vector          : Vector
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

    """Node 'Vector Math' (ShaderNodeVectorMath)

    Input sockets
    -------------
        vector0         : Vector
        vector1         : Vector
        vector2         : Vector
        scale           : Float

    Parameters
    ----------
        operation       : 'ADD' in [ 'ADD' 'SUBTRACT' 'MULTIPLY' 'DIVIDE' 'MULTIPLY_ADD' 'CROSS_PRODUCT' 'PROJECT' 'REFLECT' 'REFRACT' 'FACEFORWARD',
                             'DOT_PRODUCT' 'DISTANCE' 'LENGTH' 'SCALE' 'NORMALIZE' 'ABSOLUTE' 'MINIMUM' 'MAXIMUM' 'FLOOR' 'CEIL',
                             'FRACTION' 'MODULO' 'WRAP' 'SNAP' 'SINE' 'COSINE' 'TANGENT']

    Output sockets
    --------------
        vector          : Vector
        value           : Float
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

    """Node 'Vector Rotate' (ShaderNodeVectorRotate)

    Input sockets
    -------------
        vector          : Vector
        center          : Vector
        axis            : Vector
        angle           : Float
        rotation        : Vector

    Parameters
    ----------
        invert          : (False) bool
        rotation_type   : 'AXIS_ANGLE' in [ 'AXIS_ANGLE' 'X_AXIS' 'Y_AXIS' 'Z_AXIS' 'EULER_XYZ']

    Output sockets
    --------------
        vector          : Vector
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
