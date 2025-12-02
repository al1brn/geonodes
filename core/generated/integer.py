# Generated 2025-12-01 20:32:44

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


class Integer(Socket):
    """"
    $DOC SET hidden
    """
    def bw_and(self, b: Integer = None):
        """ > Node <&Node Bit Math>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'operation' : 'AND'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B)

        Returns
        -------
        - Integer
        """
        node = Node('Bit Math', {'A': self, 'B': b}, operation='AND')
        return node._out

    def bw_or(self, b: Integer = None):
        """ > Node <&Node Bit Math>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'operation' : 'OR'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B)

        Returns
        -------
        - Integer
        """
        node = Node('Bit Math', {'A': self, 'B': b}, operation='OR')
        return node._out

    def bw_xor(self, b: Integer = None):
        """ > Node <&Node Bit Math>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'operation' : 'XOR'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B)

        Returns
        -------
        - Integer
        """
        node = Node('Bit Math', {'A': self, 'B': b}, operation='XOR')
        return node._out

    def bw_not(self):
        """ > Node <&Node Bit Math>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'operation' : 'NOT'

        Returns
        -------
        - Integer
        """
        node = Node('Bit Math', {'A': self}, operation='NOT')
        return node._out

    def bw_shift(self, shift: Integer = None):
        """ > Node <&Node Bit Math>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'operation' : 'SHIFT'

        Arguments
        ---------
        - shift (Integer) : socket 'Shift' (id: Shift)

        Returns
        -------
        - Integer
        """
        node = Node('Bit Math', {'A': self, 'Shift': shift}, operation='SHIFT')
        return node._out

    def bw_rotate(self, shift: Integer = None):
        """ > Node <&Node Bit Math>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'operation' : 'ROTATE'

        Arguments
        ---------
        - shift (Integer) : socket 'Shift' (id: Shift)

        Returns
        -------
        - Integer
        """
        node = Node('Bit Math', {'A': self, 'Shift': shift}, operation='ROTATE')
        return node._out

    def less_than(self, b: Integer = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_THAN'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b: Integer = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_THAN'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: Integer = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'INT'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'NOT_EQUAL'

        Arguments
        ---------
        - b (Integer) : socket 'B' (id: B_INT)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_INT': self, 'B_INT': b}, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='INT')
        return node._out

    def add(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ADD'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='ADD')
        return node._out

    def subtract(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SUBTRACT'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='SUBTRACT')
        return node._out

    def multiply(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MULTIPLY'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MULTIPLY')
        return node._out

    def divide(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE')
        return node._out

    def multiply_add(self, multiplier: Integer = None, addend: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MULTIPLY_ADD'

        Arguments
        ---------
        - multiplier (Integer) : socket 'Multiplier' (id: Value_001)
        - addend (Integer) : socket 'Addend' (id: Value_002)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': multiplier, 'Value_002': addend}, operation='MULTIPLY_ADD')
        return node._out

    def abs(self):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'ABSOLUTE'

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self}, operation='ABSOLUTE')
        return node._out

    def negate(self):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'NEGATE'

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self}, operation='NEGATE')
        return node._out

    def power(self, exponent: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Base' : self
        - Parameter 'operation' : 'POWER'

        Arguments
        ---------
        - exponent (Integer) : socket 'Exponent' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': exponent}, operation='POWER')
        return node._out

    def min(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MINIMUM'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MINIMUM')
        return node._out

    def max(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MAXIMUM'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MAXIMUM')
        return node._out

    def sign(self):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'SIGN'

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self}, operation='SIGN')
        return node._out

    def divide_round(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE_ROUND'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE_ROUND')
        return node._out

    def divide_floor(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE_FLOOR'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE_FLOOR')
        return node._out

    def divide_ceil(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'DIVIDE_CEIL'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='DIVIDE_CEIL')
        return node._out

    def floored_modulo(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'FLOORED_MODULO'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='FLOORED_MODULO')
        return node._out

    def modulo(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'MODULO'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='MODULO')
        return node._out

    def gcd(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'GCD'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='GCD')
        return node._out

    def lcm(self, value: Integer = None):
        """ > Node <&Node Integer Math>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'operation' : 'LCM'

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value_001)

        Returns
        -------
        - Integer
        """
        node = Node('Integer Math', {'Value': self, 'Value_001': value}, operation='LCM')
        return node._out

    @classmethod
    def Random(cls,
                    min: Integer = None,
                    max: Integer = None,
                    id: Integer = None,
                    seed: Integer = None):
        """ > Node <&Node Random Value>

        Information
        -----------
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - min (Integer) : socket 'Min' (id: Min_002)
        - max (Integer) : socket 'Max' (id: Max_002)
        - id (Integer) : socket 'ID' (id: ID)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Random Value', {'Min_002': min, 'Max_002': max, 'ID': id, 'Seed': seed}, data_type='INT')
        return cls(node._out)

    def to_string(self):
        """ > Node <&Node Value to String>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Returns
        -------
        - String
        """
        node = Node('Value to String', {'Value': self}, data_type='INT')
        return node._out

    def blur(self, iterations: Integer = None, weight: Float = None):
        """ > Node <&Node Blur Attribute>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Integer
        """
        node = Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='INT')
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Integer
        """
        node = Node('Named Attribute', {'Name': name}, data_type='INT')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Integer
        """
        node = Node('Named Attribute', {'Name': name}, data_type='INT')
        return cls(node._out)

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation (menu='Trilinear') : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')

        Returns
        -------
        - Integer
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='INT')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - x (Integer) : socket 'X' (id: X)
        - y (Integer) : socket 'Y' (id: Y)
        - z (Integer) : socket 'Z' (id: Z)

        Returns
        -------
        - Integer
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='INT')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        Information
        -----------
        - Socket 'Topology' : self
        - Parameter 'data_type' : 'INT'

        Returns
        -------
        - None
        """
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='INT', **sockets)
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
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - velocity (Vector) : socket 'Velocity' (id: Velocity)
        - time_step (Float) : socket 'Time Step' (id: Time Step)
        - integration_scheme (menu='Runge-Kutta 3') : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
        - limiter (menu='Clamp') : ('None', 'Clamp', 'Revert')

        Returns
        -------
        - Integer
        """
        node = Node('Advect Grid', {'Grid': self, 'Velocity': velocity, 'Time Step': time_step, 'Integration Scheme': integration_scheme, 'Limiter': limiter}, data_type='INT')
        return node._out

    def prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Integer = None):
        """ > Node <&Node Prune Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - mode (menu='Threshold') : ('Inactive', 'Threshold', 'SDF')
        - threshold (Integer) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Integer
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode, 'Threshold': threshold}, data_type='INT')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Returns
        -------
        - Integer
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='INT')
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

    def set_grid_background(self, background: Integer = None):
        """ > Node <&Node Set Grid Background>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - background (Integer) : socket 'Background' (id: Background)

        Returns
        -------
        - Integer
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background}, data_type='INT')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Boolean [grid_ (Integer)]
        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='INT')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'INT'

        Returns
        -------
        - Matrix [background_value_ (Integer)]
        """
        node = Node('Grid Info', {'Grid': self}, data_type='INT')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'INT'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Integer
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='INT')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = 0,
        name: str = 'Integer',
        min: int = -2147483648,
        max: int = 2147483647,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: int = 0,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INDEX', 'ID_OR_INDEX'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
        subtype: str = 'NONE',
         ):
        """ > Integer Input

        New <#Integer> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = 0) : Default value
        - name  (str = 'Integer') : Input socket name
        - min  (int = -2147483648) : Property min_value
        - max  (int = 2147483647) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (int = 0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
        - subtype (str = 'NONE') : Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR')

        Returns
        -------
        - Integer
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketInt', value=value, name=name, min=min,
            max=max, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default=default, default_attribute=default_attribute,
            default_input=default_input, shape=shape, subtype=subtype)

    @classmethod
    def Percentage(cls,
        value: object = 0,
        name: str = 'Percentage',
        min: int = -2147483648,
        max: int = 2147483647,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: int = 0,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INDEX', 'ID_OR_INDEX'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Percentage Input

        New <#Integer> input with subtype 'PERCENTAGE'.

        Aguments
        --------
        - value  (object = 0) : Default value
        - name  (str = 'Percentage') : Input socket name
        - min  (int = -2147483648) : Property min_value
        - max  (int = 2147483647) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (int = 0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Integer
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, default_input=default_input, shape=shape,
            subtype='PERCENTAGE')

    @classmethod
    def Factor(cls,
        value: object = 0,
        name: str = 'Factor',
        min: int = -2147483648,
        max: int = 2147483647,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: int = 0,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'INDEX', 'ID_OR_INDEX'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Factor Input

        New <#Integer> input with subtype 'FACTOR'.

        Aguments
        --------
        - value  (object = 0) : Default value
        - name  (str = 'Factor') : Input socket name
        - min  (int = -2147483648) : Property min_value
        - max  (int = 2147483647) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (int = 0) : Property default_value
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Integer
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            default=default, default_attribute=default_attribute, default_input=default_input, shape=shape,
            subtype='FACTOR')

