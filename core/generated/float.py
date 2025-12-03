# Generated 2025-12-03 13:34:00

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves, MenuNode, IndexSwitchNode
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Float(Socket):
    """"
    $DOC SET hidden
    """
    def less_than(self, b: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_THAN'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A': self, 'B': b}, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_EQUAL'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A': self, 'B': b}, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_THAN'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A': self, 'B': b}, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_EQUAL'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A': self, 'B': b}, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b: Float = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'EQUAL'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A': self, 'B': b, 'Epsilon': epsilon}, data_type='FLOAT', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: Float = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'NOT_EQUAL'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A': self, 'B': b, 'Epsilon': epsilon}, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def to_integer(self,
                    rounding_mode: Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'] = 'ROUND'):
        """ > Node <&Node Float to Integer>

        Information
        -----------
        - Socket 'Float' : self

        Arguments
        ---------
        - rounding_mode (str): parameter 'rounding_mode' in ['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Float to Integer', 'rounding_mode', rounding_mode, 'to_integer', ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'))
        node = Node('Float to Integer', {'Float': self}, rounding_mode=rounding_mode)
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='FLOAT')
        return node._out

    @classmethod
    def Random(cls,
                    min: Float = None,
                    max: Float = None,
                    id: Integer = None,
                    seed: Integer = None):
        """ > Node <&Node Random Value>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - min (Float) : socket 'Min' (id: Min_001)
        - max (Float) : socket 'Max' (id: Max_001)
        - id (Integer) : socket 'ID' (id: ID)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Float
        """
        node = Node('Random Value', {'Min_001': min, 'Max_001': max, 'ID': id, 'Seed': seed}, data_type='FLOAT')
        return cls(node._out)

    def to_string(self, decimals: Integer = None):
        """ > Node <&Node Value to String>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - decimals (Integer) : socket 'Decimals' (id: Decimals)

        Returns
        -------
        - String
        """
        node = Node('Value to String', {'Value': self, 'Decimals': decimals}, data_type='FLOAT')
        return node._out

    def blur(self, iterations: Integer = None, weight: Float = None):
        """ > Node <&Node Blur Attribute>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Float
        """
        node = Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='FLOAT')
        return node._out

    def dial_gizmo(self,
                    *value: Float,
                    position: Vector = None,
                    up: Vector = None,
                    screen_space: Boolean = None,
                    radius: Float = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY'):
        """ > Node <&Node Dial Gizmo>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - position (Vector) : socket 'Position' (id: Position)
        - up (Vector) : socket 'Up' (id: Up)
        - screen_space (Boolean) : socket 'Screen Space' (id: Screen Space)
        - radius (Float) : socket 'Radius' (id: Radius)
        - color_id (str): parameter 'color_id' in ['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Dial Gizmo', 'color_id', color_id, 'dial_gizmo', ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'))
        node = Node('Dial Gizmo', {'Value': [self] + list(value), 'Position': position, 'Up': up, 'Screen Space': screen_space, 'Radius': radius}, color_id=color_id)
        return node._out

    def linear_gizmo(self,
                    *value: Float,
                    position: Vector = None,
                    direction: Vector = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY',
                    draw_style: Literal['ARROW', 'CROSS', 'BOX'] = 'ARROW'):
        """ > Node <&Node Linear Gizmo>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - position (Vector) : socket 'Position' (id: Position)
        - direction (Vector) : socket 'Direction' (id: Direction)
        - color_id (str): parameter 'color_id' in ['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']
        - draw_style (str): parameter 'draw_style' in ['ARROW', 'CROSS', 'BOX']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Linear Gizmo', 'color_id', color_id, 'linear_gizmo', ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'))
        utils.check_enum_arg('Linear Gizmo', 'draw_style', draw_style, 'linear_gizmo', ('ARROW', 'CROSS', 'BOX'))
        node = Node('Linear Gizmo', {'Value': [self] + list(value), 'Position': position, 'Direction': direction}, color_id=color_id, draw_style=draw_style)
        return node._out

    def grid_to_mesh(self, threshold: Float = None, adaptivity: Float = None):
        """ > Node <&Node Grid to Mesh>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Grid to Mesh', {'Grid': self, 'Threshold': threshold, 'Adaptivity': adaptivity})
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Float
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Float
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT')
        return cls(node._out)

    @classmethod
    def scene_time(cls):
        """ > Node <&Node Scene Time>

        Returns
        -------
        - node [seconds (Float), frame (Float)]
        """
        node = Node('Scene Time', )
        return node

    @classmethod
    @property
    def seconds(cls):
        """ > Node <&Node Scene Time>

        Returns
        -------
        - seconds
        """
        node = Node('Scene Time', )
        return node.seconds

    @classmethod
    @property
    def frame(cls):
        """ > Node <&Node Scene Time>

        Returns
        -------
        - frame
        """
        node = Node('Scene Time', )
        return node.frame

    def clamp(self,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX'):
        """ > Node <&Node Clamp>

        Information
        -----------
        - Socket 'Value' : self

        Arguments
        ---------
        - min (Float) : socket 'Min' (id: Min)
        - max (Float) : socket 'Max' (id: Max)
        - clamp_type (str): parameter 'clamp_type' in ['MINMAX', 'RANGE']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Clamp', 'clamp_type', clamp_type, 'clamp', ('MINMAX', 'RANGE'))
        node = Node('Clamp', {'Value': self, 'Min': min, 'Max': max}, clamp_type=clamp_type)
        return node._out

    def clamp_minmax(self, min: Float = None, max: Float = None):
        """ > Node <&Node Clamp>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'clamp_type' : 'MINMAX'

        Arguments
        ---------
        - min (Float) : socket 'Min' (id: Min)
        - max (Float) : socket 'Max' (id: Max)

        Returns
        -------
        - Float
        """
        node = Node('Clamp', {'Value': self, 'Min': min, 'Max': max}, clamp_type='MINMAX')
        return node._out

    def clamp_range(self, min: Float = None, max: Float = None):
        """ > Node <&Node Clamp>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'clamp_type' : 'RANGE'

        Arguments
        ---------
        - min (Float) : socket 'Min' (id: Min)
        - max (Float) : socket 'Max' (id: Max)

        Returns
        -------
        - Float
        """
        node = Node('Clamp', {'Value': self, 'Min': min, 'Max': max}, clamp_type='RANGE')
        return node._out

    def map_range(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True,
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR'):
        """ > Node <&Node Map Range>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : depending on 'from_min' type

        Arguments
        ---------
        - from_min (Float | Vector) : socket 'From Min' (id: From Min)
        - from_max (Float | Vector) : socket 'From Max' (id: From Max)
        - to_min (Float | Vector) : socket 'To Min' (id: To Min)
        - to_max (Float | Vector) : socket 'To Max' (id: To Max)
        - clamp (bool): parameter 'clamp'
        - interpolation_type (str): parameter 'interpolation_type' in ['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Map Range', 'interpolation_type', interpolation_type, 'map_range', ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'))
        data_type = utils.get_argument_data_type(from_min, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Float.map_range', 'from_min')
        node = Node('Map Range', {'Value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)
        return node._out

    def map_range_linear(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True):
        """ > Node <&Node Map Range>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : depending on 'from_min' type
        - Parameter 'interpolation_type' : 'LINEAR'

        Arguments
        ---------
        - from_min (Float | Vector) : socket 'From Min' (id: From Min)
        - from_max (Float | Vector) : socket 'From Max' (id: From Max)
        - to_min (Float | Vector) : socket 'To Min' (id: To Min)
        - to_max (Float | Vector) : socket 'To Max' (id: To Max)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(from_min, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Float.map_range_linear', 'from_min')
        node = Node('Map Range', {'Value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, data_type=data_type, interpolation_type='LINEAR')
        return node._out

    def map_range_stepped(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    steps: Float = None,
                    clamp = True):
        """ > Node <&Node Map Range>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : depending on 'from_min' type
        - Parameter 'interpolation_type' : 'STEPPED'

        Arguments
        ---------
        - from_min (Float | Vector) : socket 'From Min' (id: From Min)
        - from_max (Float | Vector) : socket 'From Max' (id: From Max)
        - to_min (Float | Vector) : socket 'To Min' (id: To Min)
        - to_max (Float | Vector) : socket 'To Max' (id: To Max)
        - steps (Float) : socket 'Steps' (id: Steps)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(from_min, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Float.map_range_stepped', 'from_min')
        node = Node('Map Range', {'Value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max, 'Steps': steps}, clamp=clamp, data_type=data_type, interpolation_type='STEPPED')
        return node._out

    def map_range_smooth_step(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True):
        """ > Node <&Node Map Range>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : depending on 'from_min' type
        - Parameter 'interpolation_type' : 'SMOOTHSTEP'

        Arguments
        ---------
        - from_min (Float | Vector) : socket 'From Min' (id: From Min)
        - from_max (Float | Vector) : socket 'From Max' (id: From Max)
        - to_min (Float | Vector) : socket 'To Min' (id: To Min)
        - to_max (Float | Vector) : socket 'To Max' (id: To Max)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(from_min, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Float.map_range_smooth_step', 'from_min')
        node = Node('Map Range', {'Value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, data_type=data_type, interpolation_type='SMOOTHSTEP')
        return node._out

    def map_range_smoother_step(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True):
        """ > Node <&Node Map Range>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : depending on 'from_min' type
        - Parameter 'interpolation_type' : 'SMOOTHERSTEP'

        Arguments
        ---------
        - from_min (Float | Vector) : socket 'From Min' (id: From Min)
        - from_max (Float | Vector) : socket 'From Max' (id: From Max)
        - to_min (Float | Vector) : socket 'To Min' (id: To Min)
        - to_max (Float | Vector) : socket 'To Max' (id: To Max)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(from_min, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Float.map_range_smoother_step', 'from_min')
        node = Node('Map Range', {'Value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, data_type=data_type, interpolation_type='SMOOTHERSTEP')
        return node._out

    def add(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ADD'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='ADD', use_clamp=use_clamp)
        return node._out

    def subtract(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SUBTRACT'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='SUBTRACT', use_clamp=use_clamp)
        return node._out

    def multiply(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MULTIPLY'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='MULTIPLY', use_clamp=use_clamp)
        return node._out

    def divide(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='DIVIDE', use_clamp=use_clamp)
        return node._out

    def multiply_add(self, multiplier: Float = None, addend: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MULTIPLY_ADD'

        Arguments
        ---------
        - multiplier (Float) : socket 'Multiplier' (id: Value_001)
        - addend (Float) : socket 'Addend' (id: Value_002)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD', use_clamp=use_clamp)
        return node._out

    def power(self, exponent: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Base' : self
        - Parameter 'operation' : 'POWER'

        Arguments
        ---------
        - exponent (Float) : socket 'Exponent' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': exponent}, operation='POWER', use_clamp=use_clamp)
        return node._out

    def log(self, base: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'LOGARITHM'

        Arguments
        ---------
        - base (Float) : socket 'Base' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': base}, operation='LOGARITHM', use_clamp=use_clamp)
        return node._out

    def sqrt(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SQRT'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='SQRT', use_clamp=use_clamp)
        return node._out

    def inverse_sqrt(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'INVERSE_SQRT'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='INVERSE_SQRT', use_clamp=use_clamp)
        return node._out

    def abs(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ABSOLUTE'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='ABSOLUTE', use_clamp=use_clamp)
        return node._out

    def exp(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'EXPONENT'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='EXPONENT', use_clamp=use_clamp)
        return node._out

    def min(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MINIMUM'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='MINIMUM', use_clamp=use_clamp)
        return node._out

    def max(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MAXIMUM'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='MAXIMUM', use_clamp=use_clamp)
        return node._out

    def mless_than(self, threshold: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'LESS_THAN'

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': threshold}, operation='LESS_THAN', use_clamp=use_clamp)
        return node._out

    def mgreater_than(self, threshold: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'GREATER_THAN'

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': threshold}, operation='GREATER_THAN', use_clamp=use_clamp)
        return node._out

    def sign(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SIGN'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='SIGN', use_clamp=use_clamp)
        return node._out

    def compare(self, value: Float = None, epsilon: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'COMPARE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - epsilon (Float) : socket 'Epsilon' (id: Value_002)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value, 'Value_002': epsilon}, operation='COMPARE', use_clamp=use_clamp)
        return node._out

    def smooth_min(self, value: Float = None, distance: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SMOOTH_MIN'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - distance (Float) : socket 'Distance' (id: Value_002)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value, 'Value_002': distance}, operation='SMOOTH_MIN', use_clamp=use_clamp)
        return node._out

    def smooth_max(self, value: Float = None, distance: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SMOOTH_MAX'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - distance (Float) : socket 'Distance' (id: Value_002)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value, 'Value_002': distance}, operation='SMOOTH_MAX', use_clamp=use_clamp)
        return node._out

    def round(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ROUND'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='ROUND', use_clamp=use_clamp)
        return node._out

    def floor(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'FLOOR'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='FLOOR', use_clamp=use_clamp)
        return node._out

    def ceil(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'CEIL'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='CEIL', use_clamp=use_clamp)
        return node._out

    def trunc(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'TRUNC'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='TRUNC', use_clamp=use_clamp)
        return node._out

    def fract(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'FRACT'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='FRACT', use_clamp=use_clamp)
        return node._out

    def modulo(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MODULO'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='MODULO', use_clamp=use_clamp)
        return node._out

    def floored_modulo(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'FLOORED_MODULO'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='FLOORED_MODULO', use_clamp=use_clamp)
        return node._out

    def wrap(self, max: Float = None, min: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'WRAP'

        Arguments
        ---------
        - max (Float) : socket 'Max' (id: Value_001)
        - min (Float) : socket 'Min' (id: Value_002)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': max, 'Value_002': min}, operation='WRAP', use_clamp=use_clamp)
        return node._out

    def snap(self, increment: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SNAP'

        Arguments
        ---------
        - increment (Float) : socket 'Increment' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': increment}, operation='SNAP', use_clamp=use_clamp)
        return node._out

    def pingpong(self, scale: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'PINGPONG'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': scale}, operation='PINGPONG', use_clamp=use_clamp)
        return node._out

    def sin(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SINE'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='SINE', use_clamp=use_clamp)
        return node._out

    def cos(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'COSINE'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='COSINE', use_clamp=use_clamp)
        return node._out

    def tan(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'TANGENT'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='TANGENT', use_clamp=use_clamp)
        return node._out

    def asin(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ARCSINE'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='ARCSINE', use_clamp=use_clamp)
        return node._out

    def acos(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ARCCOSINE'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='ARCCOSINE', use_clamp=use_clamp)
        return node._out

    def arctangent(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ARCTANGENT'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='ARCTANGENT', use_clamp=use_clamp)
        return node._out

    def atan2(self, value: Float = None, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ARCTAN2'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value_001)
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self, 'Value_001': value}, operation='ARCTAN2', use_clamp=use_clamp)
        return node._out

    def sinh(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SINH'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='SINH', use_clamp=use_clamp)
        return node._out

    def cosh(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'COSH'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='COSH', use_clamp=use_clamp)
        return node._out

    def tanh(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'TANH'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='TANH', use_clamp=use_clamp)
        return node._out

    def radians(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Degrees' : self
        - Parameter 'operation' : 'RADIANS'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='RADIANS', use_clamp=use_clamp)
        return node._out

    def degrees(self, use_clamp = False):
        """ > Node <&Node Math>

        Information
        -----------
        - Socket 'Radians' : self
        - Parameter 'operation' : 'DEGREES'

        Arguments
        ---------
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        node = Node('Math', {'Value': self}, operation='DEGREES', use_clamp=use_clamp)
        return node._out

    def mix(self, b: Float = None, factor: Float = None, clamp_factor = True):
        """ > Node <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'FLOAT'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Float) : socket 'B' (id: B_Float)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'

        Returns
        -------
        - Float
        """
        node = Node('Mix', {'A_Float': self, 'B_Float': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM')
        return node._out

    @classmethod
    def Gabor(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    gabor_type: Literal['2D', '3D'] = '2D'):
        """ > Node <&Node Gabor Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - frequency (Float) : socket 'Frequency' (id: Frequency)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - orientation (Float) : socket 'Orientation' (id: Orientation 2D)
        - gabor_type (str): parameter 'gabor_type' in ['2D', '3D']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Gabor Texture', 'gabor_type', gabor_type, 'Gabor', ('2D', '3D'))
        node = Node('Gabor Texture', {'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation 2D': orientation}, gabor_type=gabor_type)
        return cls(node._out)

    @classmethod
    def Noise(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True):
        """ > Node <&Node Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - detail (Float) : socket 'Detail' (id: Detail)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (id: Lacunarity)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - noise_dimensions (str): parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']
        - noise_type (str): parameter 'noise_type' in ['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']
        - normalize (bool): parameter 'normalize'

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Noise Texture', 'noise_dimensions', noise_dimensions, 'Noise', ('1D', '2D', '3D', '4D'))
        utils.check_enum_arg('Noise Texture', 'noise_type', noise_type, 'Noise', ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'))
        node = Node('Noise Texture', {'Vector': vector, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Distortion': distortion}, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize)
        return cls(node._out)

    @classmethod
    def Voronoi(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&Node Voronoi Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - detail (Float) : socket 'Detail' (id: Detail)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (id: Lacunarity)
        - randomness (Float) : socket 'Randomness' (id: Randomness)
        - distance (str): parameter 'distance' in ['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']
        - feature (str): parameter 'feature' in ['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']
        - normalize (bool): parameter 'normalize'
        - voronoi_dimensions (str): parameter 'voronoi_dimensions' in ['1D', '2D', '3D', '4D']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Voronoi Texture', 'distance', distance, 'Voronoi', ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'))
        utils.check_enum_arg('Voronoi Texture', 'feature', feature, 'Voronoi', ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'))
        utils.check_enum_arg('Voronoi Texture', 'voronoi_dimensions', voronoi_dimensions, 'Voronoi', ('1D', '2D', '3D', '4D'))
        node = Node('Voronoi Texture', {'Vector': vector, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Randomness': randomness}, distance=distance, feature=feature, normalize=normalize, voronoi_dimensions=voronoi_dimensions)
        return cls(node._out)

    @classmethod
    def WhiteNoise(cls,
                    vector: Vector = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&Node White Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - noise_dimensions (str): parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('White Noise Texture', 'noise_dimensions', noise_dimensions, 'WhiteNoise', ('1D', '2D', '3D', '4D'))
        node = Node('White Noise Texture', {'Vector': vector}, noise_dimensions=noise_dimensions)
        return cls(node._out)

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation (menu='Trilinear') : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')

        Returns
        -------
        - Float
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='FLOAT')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - x (Integer) : socket 'X' (id: X)
        - y (Integer) : socket 'Y' (id: Y)
        - z (Integer) : socket 'Z' (id: Z)

        Returns
        -------
        - Float
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='FLOAT')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        Information
        -----------
        - Socket 'Topology' : self
        - Parameter 'data_type' : 'FLOAT'

        Returns
        -------
        - None
        """
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='FLOAT', **sockets)
        return node._out

    def advect_grid(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None):
        """ > Node <&Node Advect Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - velocity (Vector) : socket 'Velocity' (id: Velocity)
        - time_step (Float) : socket 'Time Step' (id: Time Step)
        - integration_scheme (menu='Runge-Kutta 3') : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
        - limiter (menu='Clamp') : ('None', 'Clamp', 'Revert')

        Returns
        -------
        - Float
        """
        node = Node('Advect Grid', {'Grid': self, 'Velocity': velocity, 'Time Step': time_step, 'Integration Scheme': integration_scheme, 'Limiter': limiter}, data_type='FLOAT')
        return node._out

    def grid_gradient(self):
        """ > Node <&Node Grid Gradient>

        Information
        -----------
        - Socket 'Grid' : self

        Returns
        -------
        - Vector
        """
        node = Node('Grid Gradient', {'Grid': self})
        return node._out

    def grid_laplacian(self):
        """ > Node <&Node Grid Laplacian>

        Information
        -----------
        - Socket 'Grid' : self

        Returns
        -------
        - Float
        """
        node = Node('Grid Laplacian', {'Grid': self})
        return node._out

    def prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Float = None):
        """ > Node <&Node Prune Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - mode (menu='Threshold') : ('Inactive', 'Threshold', 'SDF')
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Float
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode, 'Threshold': threshold}, data_type='FLOAT')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Returns
        -------
        - Float
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='FLOAT')
        return node._out

    @classmethod
    def voxel_index(cls):
        """ > Node <&Node Voxel Index>

        Returns
        -------
        - Integer [y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_x_ (Integer), extent_y_ (Integer), extent_z_ (Integer)]
        """
        node = Node('Voxel Index', )
        return node._out

    def sdf_grid_fillet(self, iterations: Integer = None):
        """ > Node <&Node SDF Grid Fillet>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Fillet', {'Grid': self, 'Iterations': iterations})
        return node._out

    def sdf_grid_laplacian(self, iterations: Integer = None):
        """ > Node <&Node SDF Grid Laplacian>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Laplacian', {'Grid': self, 'Iterations': iterations})
        return node._out

    def sdf_grid_mean(self, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Mean>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - width (Integer) : socket 'Width' (id: Width)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Mean', {'Grid': self, 'Width': width, 'Iterations': iterations})
        return node._out

    def sdf_grid_mean_curvature(self, iterations: Integer = None):
        """ > Node <&Node SDF Grid Mean Curvature>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Mean Curvature', {'Grid': self, 'Iterations': iterations})
        return node._out

    def sdf_grid_median(self, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Median>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - width (Integer) : socket 'Width' (id: Width)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Median', {'Grid': self, 'Width': width, 'Iterations': iterations})
        return node._out

    def sdf_grid_offset(self, distance: Float = None):
        """ > Node <&Node SDF Grid Offset>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Offset', {'Grid': self, 'Distance': distance})
        return node._out

    def set_grid_background(self, background: Float = None):
        """ > Node <&Node Set Grid Background>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - background (Float) : socket 'Background' (id: Background)

        Returns
        -------
        - Float
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background}, data_type='FLOAT')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Boolean [grid_ (Float)]
        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='FLOAT')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'FLOAT'

        Returns
        -------
        - Matrix [background_value_ (Float)]
        """
        node = Node('Grid Info', {'Grid': self}, data_type='FLOAT')
        return node._out

    def distribute_points_in_grid_density_random(self, density: Float = None, seed: Integer = None):
        """ > Node <&Node Distribute Points in Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'mode' : 'DENSITY_RANDOM'

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', {'Grid': self, 'Density': density, 'Seed': seed}, mode='DENSITY_RANDOM')
        return node._out

    def distribute_points_in_grid_density_grid(self, spacing: Vector = None, threshold: Float = None):
        """ > Node <&Node Distribute Points in Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'mode' : 'DENSITY_GRID'

        Arguments
        ---------
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', {'Grid': self, 'Spacing': spacing, 'Threshold': threshold}, mode='DENSITY_GRID')
        return node._out

    def distribute_points_in_grid(self,
                    density: Float = None,
                    seed: Integer = None,
                    mode: Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Grid>

        Information
        -----------
        - Socket 'Grid' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - mode (str): parameter 'mode' in ['DENSITY_RANDOM', 'DENSITY_GRID']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Distribute Points in Grid', 'mode', mode, 'distribute_points_in_grid', ('DENSITY_RANDOM', 'DENSITY_GRID'))
        node = Node('Distribute Points in Grid', {'Grid': self, 'Density': density, 'Seed': seed}, mode=mode)
        return node._out

    def sdf_grid_boolean(self,
                    *grid_2: Float,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE'):
        """ > Node <&Node SDF Grid Boolean>

        Information
        -----------
        - Socket 'Grid 1' : self

        Arguments
        ---------
        - grid_2 (Float) : socket 'Grid 2' (id: Grid 2)
        - operation (str): parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('SDF Grid Boolean', 'operation', operation, 'sdf_grid_boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        node = Node('SDF Grid Boolean', {'Grid 1': self, 'Grid 2': list(grid_2)}, operation=operation)
        return node._out

    def sdf_intersect(self, *grid: Float):
        """ > Node <&Node SDF Grid Boolean>

        Information
        -----------
        - Parameter 'operation' : 'INTERSECT'

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid 2)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Boolean', {'Grid 2': [self] + list(grid)}, operation='INTERSECT')
        return node._out

    def sdf_union(self, *grid: Float):
        """ > Node <&Node SDF Grid Boolean>

        Information
        -----------
        - Parameter 'operation' : 'UNION'

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid 2)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Boolean', {'Grid 2': [self] + list(grid)}, operation='UNION')
        return node._out

    def sdf_difference(self, *grid_2: Float):
        """ > Node <&Node SDF Grid Boolean>

        Information
        -----------
        - Socket 'Grid 1' : self
        - Parameter 'operation' : 'DIFFERENCE'

        Arguments
        ---------
        - grid_2 (Float) : socket 'Grid 2' (id: Grid 2)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Boolean', {'Grid 1': self, 'Grid 2': list(grid_2)}, operation='DIFFERENCE')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Float
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='FLOAT')
        return node._out

    def bevel(self, normal: Vector = None, samples = 4):
        """ > Node <&ShaderNode Bevel>

        Information
        -----------
        - Socket 'Radius' : self

        Arguments
        ---------
        - normal (Vector) : socket 'Normal' (id: Normal)
        - samples (int): parameter 'samples'

        Returns
        -------
        - Vector
        """
        node = Node('Bevel', {'Radius': self, 'Normal': normal}, samples=samples)
        return node._out

    def bump(self,
                    distance: Float = None,
                    filter_width: Float = None,
                    height: Float = None,
                    normal: Vector = None,
                    invert = False):
        """ > Node <&ShaderNode Bump>

        Information
        -----------
        - Socket 'Strength' : self

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (id: Distance)
        - filter_width (Float) : socket 'Filter Width' (id: Filter Width)
        - height (Float) : socket 'Height' (id: Height)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Bump', {'Strength': self, 'Distance': distance, 'Filter Width': filter_width, 'Height': height, 'Normal': normal}, invert=invert)
        return node._out

    def combine_color_RGB(self, green: Float = None, blue: Float = None):
        """ > Node <&ShaderNode Combine Color>

        Information
        -----------
        - Socket 'Red' : self
        - Parameter 'mode' : 'RGB'

        Arguments
        ---------
        - green (Float) : socket 'Green' (id: Green)
        - blue (Float) : socket 'Blue' (id: Blue)

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', {'Red': self, 'Green': green, 'Blue': blue}, mode='RGB')
        return node._out

    def combine_color_HSV(self, saturation: Float = None, value: Float = None):
        """ > Node <&ShaderNode Combine Color>

        Information
        -----------
        - Socket 'Hue' : self
        - Parameter 'mode' : 'HSV'

        Arguments
        ---------
        - saturation (Float) : socket 'Saturation' (id: Green)
        - value (Float) : socket 'Value' (id: Blue)

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', {'Red': self, 'Green': saturation, 'Blue': value}, mode='HSV')
        return node._out

    def combine_color_HSL(self, saturation: Float = None, lightness: Float = None):
        """ > Node <&ShaderNode Combine Color>

        Information
        -----------
        - Socket 'Hue' : self
        - Parameter 'mode' : 'HSL'

        Arguments
        ---------
        - saturation (Float) : socket 'Saturation' (id: Green)
        - lightness (Float) : socket 'Lightness' (id: Blue)

        Returns
        -------
        - Color
        """
        node = Node('Combine Color', {'Red': self, 'Green': saturation, 'Blue': lightness}, mode='HSL')
        return node._out

    def combine_color(self,
                    green: Float = None,
                    blue: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&ShaderNode Combine Color>

        Information
        -----------
        - Socket 'Red' : self

        Arguments
        ---------
        - green (Float) : socket 'Green' (id: Green)
        - blue (Float) : socket 'Blue' (id: Blue)
        - mode (str): parameter 'mode' in ['RGB', 'HSV', 'HSL']

        Returns
        -------
        - Color
        """
        utils.check_enum_arg('Combine Color', 'mode', mode, 'combine_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Combine Color', {'Red': self, 'Green': green, 'Blue': blue}, mode=mode)
        return node._out

    def displacement(self,
                    midlevel: Float = None,
                    scale: Float = None,
                    normal: Vector = None,
                    space: Literal['OBJECT', 'WORLD'] = 'OBJECT'):
        """ > Node <&ShaderNode Displacement>

        Information
        -----------
        - Socket 'Height' : self

        Arguments
        ---------
        - midlevel (Float) : socket 'Midlevel' (id: Midlevel)
        - scale (Float) : socket 'Scale' (id: Scale)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - space (str): parameter 'space' in ['OBJECT', 'WORLD']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Displacement', 'space', space, 'displacement', ('OBJECT', 'WORLD'))
        node = Node('Displacement', {'Height': self, 'Midlevel': midlevel, 'Scale': scale, 'Normal': normal}, space=space)
        return node._out

    def fresnel(self, normal: Vector = None):
        """ > Node <&ShaderNode Fresnel>

        Information
        -----------
        - Socket 'IOR' : self

        Arguments
        ---------
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Float
        """
        node = Node('Fresnel', {'IOR': self, 'Normal': normal})
        return node._out

    def hue_saturation_value(self,
                    saturation: Float = None,
                    value: Float = None,
                    color: Color = None,
                    factor: Float = None):
        """ > Node <&ShaderNode Hue/Saturation/Value>

        Information
        -----------
        - Socket 'Hue' : self

        Arguments
        ---------
        - saturation (Float) : socket 'Saturation' (id: Saturation)
        - value (Float) : socket 'Value' (id: Value)
        - color (Color) : socket 'Color' (id: Color)
        - factor (Float) : socket 'Factor' (id: Fac)

        Returns
        -------
        - Color
        """
        node = Node('Hue/Saturation/Value', {'Hue': self, 'Saturation': saturation, 'Value': value, 'Color': color, 'Fac': factor})
        return node._out

    def layer_weight(self, normal: Vector = None):
        """ > Node <&ShaderNode Layer Weight>

        Information
        -----------
        - Socket 'Blend' : self

        Arguments
        ---------
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Float [facing_ (Float)]
        """
        node = Node('Layer Weight', {'Blend': self, 'Normal': normal})
        return node._out

    def light_falloff(self, smooth: Float = None):
        """ > Node <&ShaderNode Light Falloff>

        Information
        -----------
        - Socket 'Strength' : self

        Arguments
        ---------
        - smooth (Float) : socket 'Smooth' (id: Smooth)

        Returns
        -------
        - Float [linear_ (Float), constant_ (Float)]
        """
        node = Node('Light Falloff', {'Strength': self, 'Smooth': smooth})
        return node._out

    def normal_map(self,
                    color: Color = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT',
                    uv_map = ''):
        """ > Node <&ShaderNode Normal Map>

        Information
        -----------
        - Socket 'Strength' : self

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - space (str): parameter 'space' in ['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD']
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Normal Map', 'space', space, 'normal_map', ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'))
        node = Node('Normal Map', {'Strength': self, 'Color': color}, space=space, uv_map=uv_map)
        return node._out

    def wavelength(self):
        """ > Node <&ShaderNode Wavelength>

        Information
        -----------
        - Socket 'Wavelength' : self

        Returns
        -------
        - Color
        """
        node = Node('Wavelength', {'Wavelength': self})
        return node._out

    def wireframe(self, use_pixel_size = False):
        """ > Node <&ShaderNode Wireframe>

        Information
        -----------
        - Socket 'Size' : self

        Arguments
        ---------
        - use_pixel_size (bool): parameter 'use_pixel_size'

        Returns
        -------
        - Float
        """
        node = Node('Wireframe', {'Size': self}, use_pixel_size=use_pixel_size)
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = 0.0,
        name: str = 'Float',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
        subtype: str = 'NONE',
         ):
        """ > Float Input

        New <#Float> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Float') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
        - subtype (str = 'NONE') : Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY')

        Returns
        -------
        - Float
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketFloat', value=value, name=name, min=min,
            max=max, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default=default, default_attribute=default_attribute,
            shape=shape, subtype=subtype)

    @classmethod
    def Percentage(cls,
        value: object = 0.0,
        name: str = 'Percentage',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Percentage Input

        New <#Float> input with subtype 'PERCENTAGE'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Percentage') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls,
        value: object = 0.0,
        name: str = 'Factor',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Factor Input

        New <#Float> input with subtype 'FACTOR'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Factor') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='FACTOR')

    @classmethod
    def Angle(cls,
        value: object = 0.0,
        name: str = 'Angle',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Angle Input

        New <#Float> input with subtype 'ANGLE'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Angle') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='ANGLE')

    @classmethod
    def Time(cls,
        value: object = 0.0,
        name: str = 'Time',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Time Input

        New <#Float> input with subtype 'TIME'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Time') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='TIME')

    @classmethod
    def TimeAbsolute(cls,
        value: object = 0.0,
        name: str = 'TimeAbsolute',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > TimeAbsolute Input

        New <#Float> input with subtype 'TIME_ABSOLUTE'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'TimeAbsolute') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='TIME_ABSOLUTE')

    @classmethod
    def Distance(cls,
        value: object = 0.0,
        name: str = 'Distance',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Distance Input

        New <#Float> input with subtype 'DISTANCE'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Distance') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='DISTANCE')

    @classmethod
    def Wavelength(cls,
        value: object = 0.0,
        name: str = 'Wavelength',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Wavelength Input

        New <#Float> input with subtype 'WAVELENGTH'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Wavelength') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='WAVELENGTH')

    @classmethod
    def ColorTemperature(cls,
        value: object = 0.0,
        name: str = 'ColorTemperature',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > ColorTemperature Input

        New <#Float> input with subtype 'COLOR_TEMPERATURE'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'ColorTemperature') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='COLOR_TEMPERATURE')

    @classmethod
    def Frequency(cls,
        value: object = 0.0,
        name: str = 'Frequency',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: float = 0.0,
        default_attribute: str = '',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Frequency Input

        New <#Float> input with subtype 'FREQUENCY'.

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Frequency') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (float = 0.0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, shape=shape, subtype='FREQUENCY')

