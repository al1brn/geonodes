#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-26
@author: Generated from generator module
Blender version: 3.2.0
"""

from geonodes.core.node import Node


# ----------------------------------------------------------------------------------------------------
# Node AlignEulerToVector for FunctionNodeAlignEulerToVector

class AlignEulerToVector(Node):

    """Node *Align Euler to Vector*

    Args:
        rotation (DataSocket): Vector
        factor (DataSocket): Float
        vector (DataSocket): Vector
        axis (str): Node parameter, default = 'X' in ('X', 'Y', 'Z')
        pivot_axis (str): Node parameter, default = 'AUTO' in ('AUTO', 'X', 'Y', 'Z')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - rotation : Vector

    .. blid:: FunctionNodeAlignEulerToVector

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

    """Node *Boolean Math*

    Args:
        boolean0 (DataSocket): Boolean
        boolean1 (DataSocket): Boolean
        operation (str): Node parameter, default = 'AND' in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - boolean : Boolean

    .. blid:: FunctionNodeBooleanMath

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

    """Node *Compare*

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
        - result : Boolean

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
        - Input sockets  : ['a', 'b']
        - Output sockets : []

    .. blid:: FunctionNodeCompare

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

    """Node *Float to Integer*

    Args:
        float (DataSocket): Float
        rounding_mode (str): Node parameter, default = 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - integer : Integer

    .. blid:: FunctionNodeFloatToInt

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

    """Node *Boolean*

    Args:
        boolean (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - boolean : Boolean

    .. blid:: FunctionNodeInputBool

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

    """Node *Color*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color

    .. blid:: FunctionNodeInputColor

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('FunctionNodeInputColor', name='Color', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'color' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Integer for FunctionNodeInputInt

class Integer(Node):

    """Node *Integer*

    Args:
        integer (int): Node parameter, default = 0
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - integer : Integer

    .. blid:: FunctionNodeInputInt

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

    """Node *Special Characters*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - line_break : String
        - tab : String

    .. blid:: FunctionNodeInputSpecialCharacters

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('FunctionNodeInputSpecialCharacters', name='Special Characters', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'line_break' : 0, 'tab' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node String for FunctionNodeInputString

class String(Node):

    """Node *String*

    Args:
        string (str): Node parameter, default = ''
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - string : String

    .. blid:: FunctionNodeInputString

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

    """Node *Vector*

    Args:
        vector (Vector): Node parameter, default = [0.0, 0.0, 0.0]
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vector : Vector

    .. blid:: FunctionNodeInputVector

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

    """Node *Random Value*

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
        - value : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
        - Input sockets  : ['min', 'max']
        - Output sockets : ['value']

    .. blid:: FunctionNodeRandomValue

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

    """Node *Replace String*

    Args:
        string (DataSocket): String
        find (DataSocket): String
        replace (DataSocket): String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - string : String

    .. blid:: FunctionNodeReplaceString

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

    """Node *Rotate Euler*

    Args:
        rotation (DataSocket): Vector
        rotate_by (DataSocket): Vector
        axis (DataSocket): Vector
        angle (DataSocket): Float
        space (str): Node parameter, default = 'OBJECT' in ('OBJECT', 'LOCAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - rotation : Vector

    .. blid:: FunctionNodeRotateEuler

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

    """Node *Slice String*

    Args:
        string (DataSocket): String
        position (DataSocket): Integer
        length (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - string : String

    .. blid:: FunctionNodeSliceString

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

    """Node *String Length*

    Args:
        string (DataSocket): String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - length : Integer

    .. blid:: FunctionNodeStringLength

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

    """Node *Value to String*

    Args:
        value (DataSocket): Float
        decimals (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - string : String

    .. blid:: FunctionNodeValueToString

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

    """Node *Accumulate Field*

    Args:
        value (DataSocket): ``data_type`` dependant
        group_index (DataSocket): Integer
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - leading : ``data_type`` dependant
        - trailing : ``data_type`` dependant
        - total : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR')
        - Input sockets  : ['value']
        - Output sockets : ['leading', 'trailing', 'total']

    .. blid:: GeometryNodeAccumulateField

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

    """Node *Domain Size*

    Args:
        geometry (DataSocket): Geometry
        component (str): Node parameter, default = 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - point_count : Integer
        - edge_count : Integer
        - face_count : Integer
        - face_corner_count : Integer
        - spline_count : Integer
        - instance_count : Integer

    .. blid:: GeometryNodeAttributeDomainSize

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

    """Node *Attribute Statistic*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        attribute (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mean : ``data_type`` dependant
        - median : ``data_type`` dependant
        - sum : ``data_type`` dependant
        - min : ``data_type`` dependant
        - max : ``data_type`` dependant
        - range : ``data_type`` dependant
        - standard_deviation : ``data_type`` dependant
        - variance : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')
        - Input sockets  : ['attribute']
        - Output sockets : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

    .. blid:: GeometryNodeAttributeStatistic

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

    """Node *Transfer Attribute*

    Args:
        source (DataSocket): Geometry
        attribute (DataSocket): ``data_type`` dependant
        source_position (DataSocket): Vector
        index (DataSocket): Integer
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        mapping (str): Node parameter, default = 'NEAREST_FACE_INTERPOLATED' in ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - attribute : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['attribute']
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeAttributeTransfer

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

    """Node *Bounding Box*

    Args:
        geometry (DataSocket): Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - bounding_box : Geometry
        - min : Vector
        - max : Vector

    .. blid:: GeometryNodeBoundBox

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

    """Node *Capture Attribute*

    Args:
        geometry (DataSocket): Geometry
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry
        - attribute : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeCaptureAttribute

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

    """Node *Collection Info*

    Args:
        collection (DataSocket): Collection
        separate_children (DataSocket): Boolean
        reset_children (DataSocket): Boolean
        transform_space (str): Node parameter, default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeCollectionInfo

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

    """Node *Convex Hull*

    Args:
        geometry (DataSocket): Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - convex_hull : Geometry

    .. blid:: GeometryNodeConvexHull

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

    """Node *Arc*

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
        - curve : Curve
        - center : Vector
        - normal : Vector
        - radius : Float

    .. blid:: GeometryNodeCurveArc

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

    """Node *Endpoint Selection*

    Args:
        start_size (DataSocket): Integer
        end_size (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - selection : Boolean

    .. blid:: GeometryNodeCurveEndpointSelection

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

    """Node *Handle Type Selection*

    Args:
        handle_type (str): Node parameter, default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        mode (set): Node parameter, default = {'RIGHT', 'LEFT'}
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - selection : Boolean

    .. blid:: GeometryNodeCurveHandleTypeSelection

    """

    def __init__(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, label=None, node_color=None):

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

    """Node *Curve Length*

    Args:
        curve (DataSocket): Curve
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - length : Float

    .. blid:: GeometryNodeCurveLength

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

    """Node *Bezier Segment*

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
        - curve : Curve

    .. blid:: GeometryNodeCurvePrimitiveBezierSegment

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

    """Node *Curve Circle*

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
        - curve : Curve
        - center : Vector

    .. blid:: GeometryNodeCurvePrimitiveCircle

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

    """Node *Curve Line*

    Args:
        start (DataSocket): Vector
        end (DataSocket): Vector
        direction (DataSocket): Vector
        length (DataSocket): Float
        mode (str): Node parameter, default = 'POINTS' in ('POINTS', 'DIRECTION')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeCurvePrimitiveLine

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

    """Node *Quadrilateral*

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
        - curve : Curve

    .. blid:: GeometryNodeCurvePrimitiveQuadrilateral

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

    """Node *Quadratic Bezier*

    Args:
        resolution (DataSocket): Integer
        start (DataSocket): Vector
        middle (DataSocket): Vector
        end (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeCurveQuadraticBezier

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

    """Node *Set Handle Type*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        handle_type (str): Node parameter, default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        mode (set): Node parameter, default = {'RIGHT', 'LEFT'}
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeCurveSetHandles

    """

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, label=None, node_color=None):

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

    """Node *Spiral*

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
        - curve : Curve

    .. blid:: GeometryNodeCurveSpiral

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

    """Node *Set Spline Type*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        spline_type (str): Node parameter, default = 'POLY' in ('BEZIER', 'NURBS', 'POLY')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeCurveSplineType

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

    """Node *Star*

    Args:
        points (DataSocket): Integer
        inner_radius (DataSocket): Float
        outer_radius (DataSocket): Float
        twist (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve
        - outer_points : Boolean

    .. blid:: GeometryNodeCurveStar

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

    """Node *Curve to Mesh*

    Args:
        curve (DataSocket): Curve
        profile_curve (DataSocket): Geometry
        fill_caps (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeCurveToMesh

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

    """Node *Curve to Points*

    Args:
        curve (DataSocket): Curve
        count (DataSocket): Integer
        length (DataSocket): Float
        mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - points : Points
        - tangent : Vector
        - normal : Vector
        - rotation : Vector

    .. blid:: GeometryNodeCurveToPoints

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

    """Node *Delete Geometry*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
        mode (str): Node parameter, default = 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeDeleteGeometry

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

    """Node *Distribute Points on Faces*

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
        - points : Points
        - normal : Vector
        - rotation : Vector

    .. blid:: GeometryNodeDistributePointsOnFaces

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

    """Node *Dual Mesh*

    Args:
        mesh (DataSocket): Mesh
        keep_boundaries (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - dual_mesh : Geometry

    .. blid:: GeometryNodeDualMesh

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

    """Node *Duplicate Elements*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        amount (DataSocket): Integer
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry
        - duplicate_index : Integer

    .. blid:: GeometryNodeDuplicateElements

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

    """Node *Extrude Mesh*

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
        - mesh : Mesh
        - top : Boolean
        - side : Boolean

    .. blid:: GeometryNodeExtrudeMesh

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

    """Node *Field at Index*

    Args:
        index (DataSocket): Integer
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - value : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : ['value']

    .. blid:: GeometryNodeFieldAtIndex

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

    """Node *Fill Curve*

    Args:
        curve (DataSocket): Curve
        mode (str): Node parameter, default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeFillCurve

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

    """Node *Fillet Curve*

    Args:
        curve (DataSocket): Curve
        count (DataSocket): Integer
        radius (DataSocket): Float
        limit_radius (DataSocket): Boolean
        mode (str): Node parameter, default = 'BEZIER' in ('BEZIER', 'POLY')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeFilletCurve

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

    """Node *Flip Faces*

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeFlipFaces

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

    """Node *Geometry to Instance*

    Args:
        geometry (DataSocket): *Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - instances : Instances

    .. blid:: GeometryNodeGeometryToInstance

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

    """Node *Group*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    .. blid:: GeometryNodeGroup

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeGroup', name='Group', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {}

# ----------------------------------------------------------------------------------------------------
# Node ImageTexture for GeometryNodeImageTexture

class ImageTexture(Node):

    """Node *Image Texture*

    Args:
        image (DataSocket): Image
        vector (DataSocket): Vector
        frame (DataSocket): Integer
        extension (str): Node parameter, default = 'REPEAT' in ('REPEAT', 'EXTEND', 'CLIP')
        interpolation (str): Node parameter, default = 'Linear' in ('Linear', 'Closest', 'Cubic')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color
        - alpha : Float

    .. blid:: GeometryNodeImageTexture

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

    """Node *Curve Handle Positions*

    Args:
        relative (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - left : Vector
        - right : Vector

    .. blid:: GeometryNodeInputCurveHandlePositions

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

    """Node *Curve Tilt*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - tilt : Float

    .. blid:: GeometryNodeInputCurveTilt

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputCurveTilt', name='Curve Tilt', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'tilt' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node ID for GeometryNodeInputID

class ID(Node):

    """Node *ID*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - ID : Integer

    .. blid:: GeometryNodeInputID

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputID', name='ID', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'ID' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Index for GeometryNodeInputIndex

class Index(Node):

    """Node *Index*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - index : Integer

    .. blid:: GeometryNodeInputIndex

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputIndex', name='Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'index' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Material for GeometryNodeInputMaterial

class Material(Node):

    """Node *Material*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - material : Material

    .. blid:: GeometryNodeInputMaterial

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMaterial', name='Material', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'material' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node MaterialIndex for GeometryNodeInputMaterialIndex

class MaterialIndex(Node):

    """Node *Material Index*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - material_index : Integer

    .. blid:: GeometryNodeInputMaterialIndex

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMaterialIndex', name='Material Index', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'material_index' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node EdgeAngle for GeometryNodeInputMeshEdgeAngle

class EdgeAngle(Node):

    """Node *Edge Angle*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - unsigned_angle : Float
        - signed_angle : Float

    .. blid:: GeometryNodeInputMeshEdgeAngle

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeAngle', name='Edge Angle', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'unsigned_angle' : 0, 'signed_angle' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node EdgeNeighbors for GeometryNodeInputMeshEdgeNeighbors

class EdgeNeighbors(Node):

    """Node *Edge Neighbors*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - face_count : Integer

    .. blid:: GeometryNodeInputMeshEdgeNeighbors

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', name='Edge Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'face_count' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node EdgeVertices for GeometryNodeInputMeshEdgeVertices

class EdgeVertices(Node):

    """Node *Edge Vertices*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vertex_index_1 : Integer
        - vertex_index_2 : Integer
        - position_1 : Vector
        - position_2 : Vector

    .. blid:: GeometryNodeInputMeshEdgeVertices

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshEdgeVertices', name='Edge Vertices', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_index_1' : 0, 'vertex_index_2' : 1, 'position_1' : 2, 'position_2' : 3, }

# ----------------------------------------------------------------------------------------------------
# Node FaceArea for GeometryNodeInputMeshFaceArea

class FaceArea(Node):

    """Node *Face Area*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - area : Float

    .. blid:: GeometryNodeInputMeshFaceArea

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceArea', name='Face Area', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'area' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node FaceIsPlanar for GeometryNodeInputMeshFaceIsPlanar

class FaceIsPlanar(Node):

    """Node *Face is Planar*

    Args:
        threshold (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - planar : Boolean

    .. blid:: GeometryNodeInputMeshFaceIsPlanar

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

    """Node *Face Neighbors*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vertex_count : Integer
        - face_count : Integer

    .. blid:: GeometryNodeInputMeshFaceNeighbors

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshFaceNeighbors', name='Face Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_count' : 0, 'face_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node MeshIsland for GeometryNodeInputMeshIsland

class MeshIsland(Node):

    """Node *Mesh Island*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - island_index : Integer
        - island_count : Integer

    .. blid:: GeometryNodeInputMeshIsland

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshIsland', name='Mesh Island', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'island_index' : 0, 'island_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node VertexNeighbors for GeometryNodeInputMeshVertexNeighbors

class VertexNeighbors(Node):

    """Node *Vertex Neighbors*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vertex_count : Integer
        - face_count : Integer

    .. blid:: GeometryNodeInputMeshVertexNeighbors

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputMeshVertexNeighbors', name='Vertex Neighbors', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'vertex_count' : 0, 'face_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node NamedAttribute for GeometryNodeInputNamedAttribute

class NamedAttribute(Node):

    """Node *Named Attribute*

    Args:
        name (DataSocket): String
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - attribute : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : []
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeInputNamedAttribute

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

    """Node *Normal*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - normal : Vector

    .. blid:: GeometryNodeInputNormal

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputNormal', name='Normal', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'normal' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Position for GeometryNodeInputPosition

class Position(Node):

    """Node *Position*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - position : Vector

    .. blid:: GeometryNodeInputPosition

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputPosition', name='Position', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'position' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node Radius for GeometryNodeInputRadius

class Radius(Node):

    """Node *Radius*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - radius : Float

    .. blid:: GeometryNodeInputRadius

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputRadius', name='Radius', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'radius' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node SceneTime for GeometryNodeInputSceneTime

class SceneTime(Node):

    """Node *Scene Time*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - seconds : Float
        - frame : Float

    .. blid:: GeometryNodeInputSceneTime

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'seconds' : 0, 'frame' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node IsShadeSmooth for GeometryNodeInputShadeSmooth

class IsShadeSmooth(Node):

    """Node *Is Shade Smooth*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - smooth : Boolean

    .. blid:: GeometryNodeInputShadeSmooth

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputShadeSmooth', name='Is Shade Smooth', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'smooth' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node IsSplineCyclic for GeometryNodeInputSplineCyclic

class IsSplineCyclic(Node):

    """Node *Is Spline Cyclic*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - cyclic : Boolean

    .. blid:: GeometryNodeInputSplineCyclic

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSplineCyclic', name='Is Spline Cyclic', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'cyclic' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node SplineResolution for GeometryNodeInputSplineResolution

class SplineResolution(Node):

    """Node *Spline Resolution*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - resolution : Integer

    .. blid:: GeometryNodeInputSplineResolution

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputSplineResolution', name='Spline Resolution', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'resolution' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node CurveTangent for GeometryNodeInputTangent

class CurveTangent(Node):

    """Node *Curve Tangent*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - tangent : Vector

    .. blid:: GeometryNodeInputTangent

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeInputTangent', name='Curve Tangent', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'tangent' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node InstanceOnPoints for GeometryNodeInstanceOnPoints

class InstanceOnPoints(Node):

    """Node *Instance on Points*

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
        - instances : Instances

    .. blid:: GeometryNodeInstanceOnPoints

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

    """Node *Instances to Points*

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - points : Points

    .. blid:: GeometryNodeInstancesToPoints

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

    """Node *Is Viewport*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - is_viewport : Boolean

    .. blid:: GeometryNodeIsViewport

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeIsViewport', name='Is Viewport', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'is_viewport' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node JoinGeometry for GeometryNodeJoinGeometry

class JoinGeometry(Node):

    """Node *Join Geometry*

    Args:
        geometry (DataSocket): *Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeJoinGeometry

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

    """Node *Material Selection*

    Args:
        material (DataSocket): Material
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - selection : Boolean

    .. blid:: GeometryNodeMaterialSelection

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

    """Node *Merge by Distance*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        distance (DataSocket): Float
        mode (str): Node parameter, default = 'ALL' in ('ALL', 'CONNECTED')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeMergeByDistance

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

    """Node *Mesh Boolean*

    Args:
        mesh_1 (DataSocket): Geometry
        mesh_2 (DataSocket): *Geometry
        self_intersection (DataSocket): Boolean
        hole_tolerant (DataSocket): Boolean
        operation (str): Node parameter, default = 'DIFFERENCE' in ('INTERSECT', 'UNION', 'DIFFERENCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeMeshBoolean

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

    """Node *Mesh Circle*

    Args:
        vertices (DataSocket): Integer
        radius (DataSocket): Float
        fill_type (str): Node parameter, default = 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeMeshCircle

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

    """Node *Cone*

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
        - mesh : Mesh
        - top : Boolean
        - bottom : Boolean
        - side : Boolean

    .. blid:: GeometryNodeMeshCone

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

    """Node *Cube*

    Args:
        size (DataSocket): Vector
        vertices_x (DataSocket): Integer
        vertices_y (DataSocket): Integer
        vertices_z (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeMeshCube

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

    """Node *Cylinder*

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
        - mesh : Mesh
        - top : Boolean
        - side : Boolean
        - bottom : Boolean

    .. blid:: GeometryNodeMeshCylinder

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

    """Node *Grid*

    Args:
        size_x (DataSocket): Float
        size_y (DataSocket): Float
        vertices_x (DataSocket): Integer
        vertices_y (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeMeshGrid

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

    """Node *Ico Sphere*

    Args:
        radius (DataSocket): Float
        subdivisions (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeMeshIcoSphere

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

    """Node *Mesh Line*

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
        - mesh : Mesh

    .. blid:: GeometryNodeMeshLine

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

    """Node *Mesh to Curve*

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeMeshToCurve

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

    """Node *Mesh to Points*

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        radius (DataSocket): Float
        mode (str): Node parameter, default = 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - points : Points

    .. blid:: GeometryNodeMeshToPoints

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

    """Node *UV Sphere*

    Args:
        segments (DataSocket): Integer
        rings (DataSocket): Integer
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeMeshUVSphere

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

    """Node *Object Info*

    Args:
        object (DataSocket): Object
        as_instance (DataSocket): Boolean
        transform_space (str): Node parameter, default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - location : Vector
        - rotation : Vector
        - scale : Vector
        - geometry : Geometry

    .. blid:: GeometryNodeObjectInfo

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

    """Node *Points to Vertices*

    Args:
        points (DataSocket): Points
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodePointsToVertices

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

    """Node *Points to Volume*

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
        - volume : Volume

    .. blid:: GeometryNodePointsToVolume

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

    """Node *Geometry Proximity*

    Args:
        target (DataSocket): Geometry
        source_position (DataSocket): Vector
        target_element (str): Node parameter, default = 'FACES' in ('POINTS', 'EDGES', 'FACES')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - position : Vector
        - distance : Float

    .. blid:: GeometryNodeProximity

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

    """Node *Raycast*

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
        - is_hit : Boolean
        - hit_position : Vector
        - hit_normal : Vector
        - hit_distance : Float
        - attribute : ``data_type`` dependant

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        - Input sockets  : ['attribute']
        - Output sockets : ['attribute']

    .. blid:: GeometryNodeRaycast

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

    """Node *Realize Instances*

    Args:
        geometry (DataSocket): Geometry
        legacy_behavior (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeRealizeInstances

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

    """Node *Remove Named Attribute*

    Args:
        geometry (DataSocket): Geometry
        name (DataSocket): String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeRemoveAttribute

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

    """Node *Replace Material*

    Args:
        geometry (DataSocket): Geometry
        old (DataSocket): Material
        new (DataSocket): Material
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeReplaceMaterial

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

    """Node *Resample Curve*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        count (DataSocket): Integer
        length (DataSocket): Float
        mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeResampleCurve

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

    """Node *Reverse Curve*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeReverseCurve

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

    """Node *Rotate Instances*

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        rotation (DataSocket): Vector
        pivot_point (DataSocket): Vector
        local_space (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - instances : Instances

    .. blid:: GeometryNodeRotateInstances

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

    """Node *Sample Curve*

    Args:
        curve (DataSocket): Curve
        factor (DataSocket): Float
        length (DataSocket): Float
        mode (str): Node parameter, default = 'LENGTH' in ('FACTOR', 'LENGTH')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - position : Vector
        - tangent : Vector
        - normal : Vector

    .. blid:: GeometryNodeSampleCurve

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

    """Node *Scale Elements*

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
        - geometry : Geometry

    .. blid:: GeometryNodeScaleElements

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

    """Node *Scale Instances*

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        scale (DataSocket): Vector
        center (DataSocket): Vector
        local_space (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - instances : Instances

    .. blid:: GeometryNodeScaleInstances

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

    """Node *Separate Components*

    Args:
        geometry (DataSocket): Geometry
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh
        - point_cloud : Geometry
        - curve : Curve
        - volume : Volume
        - instances : Instances

    .. blid:: GeometryNodeSeparateComponents

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

    """Node *Separate Geometry*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - selection : Geometry
        - inverted : Geometry

    .. blid:: GeometryNodeSeparateGeometry

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

    """Node *Set Handle Positions*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        offset (DataSocket): Vector
        mode (str): Node parameter, default = 'LEFT' in ('LEFT', 'RIGHT')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeSetCurveHandlePositions

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

    """Node *Set Curve Radius*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeSetCurveRadius

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

    """Node *Set Curve Tilt*

    Args:
        curve (DataSocket): Curve
        selection (DataSocket): Boolean
        tilt (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeSetCurveTilt

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

    """Node *Set ID*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        ID (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetID

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

    """Node *Set Material*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        material (DataSocket): Material
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetMaterial

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

    """Node *Set Material Index*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        material_index (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetMaterialIndex

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

    """Node *Set Point Radius*

    Args:
        points (DataSocket): Points
        selection (DataSocket): Boolean
        radius (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - points : Points

    .. blid:: GeometryNodeSetPointRadius

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

    """Node *Set Position*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        position (DataSocket): Vector
        offset (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetPosition

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

    """Node *Set Shade Smooth*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        shade_smooth (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetShadeSmooth

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

    """Node *Set Spline Cyclic*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        cyclic (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetSplineCyclic

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

    """Node *Set Spline Resolution*

    Args:
        geometry (DataSocket): Geometry
        selection (DataSocket): Boolean
        resolution (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeSetSplineResolution

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

    """Node *Spline Length*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - length : Float
        - point_count : Integer

    .. blid:: GeometryNodeSplineLength

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSplineLength', name='Spline Length', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'length' : 0, 'point_count' : 1, }

# ----------------------------------------------------------------------------------------------------
# Node SplineParameter for GeometryNodeSplineParameter

class SplineParameter(Node):

    """Node *Spline Parameter*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - factor : Float
        - length : Float
        - index : Integer

    .. blid:: GeometryNodeSplineParameter

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('GeometryNodeSplineParameter', name='Spline Parameter', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'factor' : 0, 'length' : 1, 'index' : 2, }

# ----------------------------------------------------------------------------------------------------
# Node SplitEdges for GeometryNodeSplitEdges

class SplitEdges(Node):

    """Node *Split Edges*

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeSplitEdges

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

    """Node *Store Named Attribute*

    Args:
        geometry (DataSocket): Geometry
        name (DataSocket): String
        value (DataSocket): ``data_type`` dependant
        data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
        domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN')
        - Input sockets  : ['value']
        - Output sockets : []

    .. blid:: GeometryNodeStoreNamedAttribute

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

    """Node *Join Strings*

    Args:
        delimiter (DataSocket): String
        strings (DataSocket): *String
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - string : String

    .. blid:: GeometryNodeStringJoin

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

    """Node *String to Curves*

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
        - curve_instances : Geometry
        - remainder : String
        - line : Integer
        - pivot_point : Vector

    .. blid:: GeometryNodeStringToCurves

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

    """Node *Subdivide Curve*

    Args:
        curve (DataSocket): Curve
        cuts (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - curve : Curve

    .. blid:: GeometryNodeSubdivideCurve

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

    """Node *Subdivide Mesh*

    Args:
        mesh (DataSocket): Mesh
        level (DataSocket): Integer
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeSubdivideMesh

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

    """Node *Subdivision Surface*

    Args:
        mesh (DataSocket): Mesh
        level (DataSocket): Integer
        crease (DataSocket): Float
        boundary_smooth (str): Node parameter, default = 'ALL' in ('PRESERVE_CORNERS', 'ALL')
        uv_smooth (str): Node parameter, default = 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeSubdivisionSurface

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

    """Node *Switch*

    Args:
        switch (DataSocket): ``input_type`` dependant
        false (DataSocket): ``input_type`` dependant
        true (DataSocket): ``input_type`` dependant
        input_type (str): Node parameter, default = 'GEOMETRY' in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - output : ``input_type`` dependant

    Shared sockets:
        - Driving parameter : ``input_type`` in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
        - Input sockets  : ['switch', 'false', 'true']
        - Output sockets : ['output']

    .. blid:: GeometryNodeSwitch

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

    """Node *Transform*

    Args:
        geometry (DataSocket): Geometry
        translation (DataSocket): Vector
        rotation (DataSocket): Vector
        scale (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - geometry : Geometry

    .. blid:: GeometryNodeTransform

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

    """Node *Translate Instances*

    Args:
        instances (DataSocket): Instances
        selection (DataSocket): Boolean
        translation (DataSocket): Vector
        local_space (DataSocket): Boolean
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - instances : Instances

    .. blid:: GeometryNodeTranslateInstances

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

    """Node *Triangulate*

    Args:
        mesh (DataSocket): Mesh
        selection (DataSocket): Boolean
        minimum_vertices (DataSocket): Integer
        ngon_method (str): Node parameter, default = 'BEAUTY' in ('BEAUTY', 'CLIP')
        quad_method (str): Node parameter, default = 'SHORTEST_DIAGONAL' in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - mesh : Mesh

    .. blid:: GeometryNodeTriangulate

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

    """Node *Trim Curve*

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
        - curve : Curve

    .. blid:: GeometryNodeTrimCurve

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

    """Node *Volume to Mesh*

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
        - mesh : Mesh

    .. blid:: GeometryNodeVolumeToMesh

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

    """Node *Clamp*

    Args:
        value (DataSocket): Float
        min (DataSocket): Float
        max (DataSocket): Float
        clamp_type (str): Node parameter, default = 'MINMAX' in ('MINMAX', 'RANGE')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - result : Float

    .. blid:: ShaderNodeClamp

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

    """Node *Combine RGB*

    Args:
        r (DataSocket): Float
        g (DataSocket): Float
        b (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - image : Color

    .. blid:: ShaderNodeCombineRGB

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

    """Node *Combine XYZ*

    Args:
        x (DataSocket): Float
        y (DataSocket): Float
        z (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vector : Vector

    .. blid:: ShaderNodeCombineXYZ

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

    """Node *Float Curve*

    Args:
        factor (DataSocket): Float
        value (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - value : Float

    .. blid:: ShaderNodeFloatCurve

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

    """Node *Map Range*

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
        - result : Float
        - vector : Vector

    Shared sockets:
        - Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')
        - Input sockets  : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']
        - Output sockets : []

    .. blid:: ShaderNodeMapRange

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

    """Node *Math*

    Args:
        value0 (DataSocket): Float
        value1 (DataSocket): Float
        value2 (DataSocket): Float
        operation (str): Node parameter, default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - value : Float

    .. blid:: ShaderNodeMath

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

    """Node *Mix*

    Args:
        fac (DataSocket): Float
        color1 (DataSocket): Color
        color2 (DataSocket): Color
        blend_type (str): Node parameter, default = 'MIX' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
        use_alpha (bool): Node parameter, default = False
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color

    .. blid:: ShaderNodeMixRGB

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

    """Node *RGB Curves*

    Args:
        fac (DataSocket): Float
        color (DataSocket): Color
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color

    .. blid:: ShaderNodeRGBCurve

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

    """Node *Separate RGB*

    Args:
        image (DataSocket): Color
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - r : Float
        - g : Float
        - b : Float

    .. blid:: ShaderNodeSeparateRGB

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

    """Node *Separate XYZ*

    Args:
        vector (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - x : Float
        - y : Float
        - z : Float

    .. blid:: ShaderNodeSeparateXYZ

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

    """Node *Brick Texture*

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
        - color : Color
        - fac : Float

    .. blid:: ShaderNodeTexBrick

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

    """Node *Checker Texture*

    Args:
        vector (DataSocket): Vector
        color1 (DataSocket): Color
        color2 (DataSocket): Color
        scale (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color
        - fac : Float

    .. blid:: ShaderNodeTexChecker

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

    """Node *Gradient Texture*

    Args:
        vector (DataSocket): Vector
        gradient_type (str): Node parameter, default = 'LINEAR' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color
        - fac : Float

    .. blid:: ShaderNodeTexGradient

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

    """Node *Magic Texture*

    Args:
        vector (DataSocket): Vector
        scale (DataSocket): Float
        distortion (DataSocket): Float
        turbulence_depth (int): Node parameter, default = 2
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color
        - fac : Float

    .. blid:: ShaderNodeTexMagic

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

    """Node *Musgrave Texture*

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
        - fac : Float

    .. blid:: ShaderNodeTexMusgrave

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

    """Node *Noise Texture*

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
        - fac : Float
        - color : Color

    .. blid:: ShaderNodeTexNoise

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

    """Node *Voronoi Texture*

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
        - distance : Float
        - color : Color
        - position : Vector
        - w : Float
        - radius : Float

    .. blid:: ShaderNodeTexVoronoi

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

    """Node *Wave Texture*

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
        - color : Color
        - fac : Float

    .. blid:: ShaderNodeTexWave

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

    """Node *White Noise Texture*

    Args:
        vector (DataSocket): Vector
        w (DataSocket): Float
        noise_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - value : Float
        - color : Color

    .. blid:: ShaderNodeTexWhiteNoise

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

    """Node *ColorRamp*

    Args:
        fac (DataSocket): Float
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - color : Color
        - alpha : Float

    .. blid:: ShaderNodeValToRGB

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

    """Node *Value*

    Args:
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - value : Float

    .. blid:: ShaderNodeValue

    """

    def __init__(self, label=None, node_color=None):

        super().__init__('ShaderNodeValue', name='Value', label=label, node_color=node_color)

        # Input and output sockets names (for use in __getattr__ and __setattr__)

        self.insockets = {}
        self.outsockets = {'value' : 0, }

# ----------------------------------------------------------------------------------------------------
# Node VectorCurves for ShaderNodeVectorCurve

class VectorCurves(Node):

    """Node *Vector Curves*

    Args:
        fac (DataSocket): Float
        vector (DataSocket): Vector
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vector : Vector

    .. blid:: ShaderNodeVectorCurve

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

    """Node *Vector Math*

    Args:
        vector0 (DataSocket): Vector
        vector1 (DataSocket): Vector
        vector2 (DataSocket): Vector
        scale (DataSocket): Float
        operation (str): Node parameter, default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')
        node_color (color): Node color
        node_label (str): Node label


    Output sockets:
        - vector : Vector
        - value : Float

    .. blid:: ShaderNodeVectorMath

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

    """Node *Vector Rotate*

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
        - vector : Vector

    .. blid:: ShaderNodeVectorRotate

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

