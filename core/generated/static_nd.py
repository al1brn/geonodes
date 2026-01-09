# Generated 2026-01-09 13:18:08

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
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


class ND:
    """" Static class

    Exposes all nodes as static methods:

    ``` python
    a = nd.math(1, 2, operation='ADD')
    ```
    """

    @classmethod
    def align_rotation_to_vector(cls,
                    rotation: Rotation = None,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Factor)
        - axis (str): parameter 'axis' in ['X', 'Y', 'Z']
        - pivot_axis (str): parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Align Rotation to Vector', 'axis', axis, 'align_rotation_to_vector', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Align Rotation to Vector', 'pivot_axis', pivot_axis, 'align_rotation_to_vector', ('AUTO', 'X', 'Y', 'Z'))
        node = Node('Align Rotation to Vector', {'Rotation': rotation, 'Vector': vector, 'Factor': factor}, axis=axis, pivot_axis=pivot_axis)
        return node._out

    @classmethod
    def axes_to_rotation(cls,
                    primary_axis_1: Vector = None,
                    secondary_axis_1: Vector = None,
                    primary_axis: Literal['X', 'Y', 'Z'] = 'Z',
                    secondary_axis: Literal['X', 'Y', 'Z'] = 'X'):
        """ > Node <&Node Axes to Rotation>

        Arguments
        ---------
        - primary_axis_1 (Vector) : socket 'Primary Axis' (id: Primary Axis)
        - secondary_axis_1 (Vector) : socket 'Secondary Axis' (id: Secondary Axis)
        - primary_axis (str): parameter 'primary_axis' in ['X', 'Y', 'Z']
        - secondary_axis (str): parameter 'secondary_axis' in ['X', 'Y', 'Z']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Axes to Rotation', 'primary_axis', primary_axis, 'axes_to_rotation', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Axes to Rotation', 'secondary_axis', secondary_axis, 'axes_to_rotation', ('X', 'Y', 'Z'))
        node = Node('Axes to Rotation', {'Primary Axis': primary_axis_1, 'Secondary Axis': secondary_axis_1}, primary_axis=primary_axis, secondary_axis=secondary_axis)
        return node._out

    @classmethod
    def axis_angle_to_rotation(cls, axis: Vector = None, angle: Float = None):
        """ > Node <&Node Axis Angle to Rotation>

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)

        Returns
        -------
        - Rotation
        """
        node = Node('Axis Angle to Rotation', {'Axis': axis, 'Angle': angle})
        return node._out

    @classmethod
    def bit_math(cls,
                    a: Integer = None,
                    b: Integer = None,
                    shift: Integer = None,
                    operation: Literal['AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE'] = 'AND'):
        """ > Node <&Node Bit Math>

        Arguments
        ---------
        - a (Integer) : socket 'A' (id: A)
        - b (Integer) : socket 'B' (id: B)
        - shift (Integer) : socket 'Shift' (id: Shift)
        - operation (str): parameter 'operation' in ['AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Bit Math', 'operation', operation, 'bit_math', ('AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE'))
        node = Node('Bit Math', {'A': a, 'B': b, 'Shift': shift}, operation=operation)
        return node._out

    @classmethod
    def boolean_math(cls,
                    boolean: Boolean = None,
                    boolean_1: Boolean = None,
                    operation: Literal['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY'] = 'AND'):
        """ > Node <&Node Boolean Math>

        Arguments
        ---------
        - boolean (Boolean) : socket 'Boolean' (id: Boolean)
        - boolean_1 (Boolean) : socket 'Boolean' (id: Boolean_001)
        - operation (str): parameter 'operation' in ['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY']

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Boolean Math', 'operation', operation, 'boolean_math', ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY'))
        node = Node('Boolean Math', {'Boolean': boolean, 'Boolean_001': boolean_1}, operation=operation)
        return node._out

    @classmethod
    def combine_color(cls,
                    red: Float = None,
                    green: Float = None,
                    blue: Float = None,
                    alpha: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&Node Combine Color>

        Arguments
        ---------
        - red (Float) : socket 'Red' (id: Red)
        - green (Float) : socket 'Green' (id: Green)
        - blue (Float) : socket 'Blue' (id: Blue)
        - alpha (Float) : socket 'Alpha' (id: Alpha)
        - mode (str): parameter 'mode' in ['RGB', 'HSV', 'HSL']

        Returns
        -------
        - Color
        """
        utils.check_enum_arg('Combine Color', 'mode', mode, 'combine_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Combine Color', {'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode=mode)
        return node._out

    @classmethod
    def combine_matrix(cls,
                    column_1_row_1: Float = None,
                    column_1_row_2: Float = None,
                    column_1_row_3: Float = None,
                    column_1_row_4: Float = None,
                    column_2_row_1: Float = None,
                    column_2_row_2: Float = None,
                    column_2_row_3: Float = None,
                    column_2_row_4: Float = None,
                    column_3_row_1: Float = None,
                    column_3_row_2: Float = None,
                    column_3_row_3: Float = None,
                    column_3_row_4: Float = None,
                    column_4_row_1: Float = None,
                    column_4_row_2: Float = None,
                    column_4_row_3: Float = None,
                    column_4_row_4: Float = None):
        """ > Node <&Node Combine Matrix>

        Arguments
        ---------
        - column_1_row_1 (Float) : socket 'Column 1 Row 1' (id: Column 1 Row 1)
        - column_1_row_2 (Float) : socket 'Column 1 Row 2' (id: Column 1 Row 2)
        - column_1_row_3 (Float) : socket 'Column 1 Row 3' (id: Column 1 Row 3)
        - column_1_row_4 (Float) : socket 'Column 1 Row 4' (id: Column 1 Row 4)
        - column_2_row_1 (Float) : socket 'Column 2 Row 1' (id: Column 2 Row 1)
        - column_2_row_2 (Float) : socket 'Column 2 Row 2' (id: Column 2 Row 2)
        - column_2_row_3 (Float) : socket 'Column 2 Row 3' (id: Column 2 Row 3)
        - column_2_row_4 (Float) : socket 'Column 2 Row 4' (id: Column 2 Row 4)
        - column_3_row_1 (Float) : socket 'Column 3 Row 1' (id: Column 3 Row 1)
        - column_3_row_2 (Float) : socket 'Column 3 Row 2' (id: Column 3 Row 2)
        - column_3_row_3 (Float) : socket 'Column 3 Row 3' (id: Column 3 Row 3)
        - column_3_row_4 (Float) : socket 'Column 3 Row 4' (id: Column 3 Row 4)
        - column_4_row_1 (Float) : socket 'Column 4 Row 1' (id: Column 4 Row 1)
        - column_4_row_2 (Float) : socket 'Column 4 Row 2' (id: Column 4 Row 2)
        - column_4_row_3 (Float) : socket 'Column 4 Row 3' (id: Column 4 Row 3)
        - column_4_row_4 (Float) : socket 'Column 4 Row 4' (id: Column 4 Row 4)

        Returns
        -------
        - Matrix
        """
        node = Node('Combine Matrix', {'Column 1 Row 1': column_1_row_1, 'Column 1 Row 2': column_1_row_2, 'Column 1 Row 3': column_1_row_3, 'Column 1 Row 4': column_1_row_4, 'Column 2 Row 1': column_2_row_1, 'Column 2 Row 2': column_2_row_2, 'Column 2 Row 3': column_2_row_3, 'Column 2 Row 4': column_2_row_4, 'Column 3 Row 1': column_3_row_1, 'Column 3 Row 2': column_3_row_2, 'Column 3 Row 3': column_3_row_3, 'Column 3 Row 4': column_3_row_4, 'Column 4 Row 1': column_4_row_1, 'Column 4 Row 2': column_4_row_2, 'Column 4 Row 3': column_4_row_3, 'Column 4 Row 4': column_4_row_4})
        return node._out

    @classmethod
    def combine_transform(cls,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Combine Transform>

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Matrix
        """
        node = Node('Combine Transform', {'Translation': translation, 'Rotation': rotation, 'Scale': scale})
        return node._out

    @classmethod
    def compare(cls,
                    a: Float = None,
                    b: Float = None,
                    a_1: Integer = None,
                    b_1: Integer = None,
                    a_2: Vector = None,
                    b_2: Vector = None,
                    a_3: Color = None,
                    b_3: Color = None,
                    a_4: String = None,
                    b_4: String = None,
                    c: Float = None,
                    angle: Float = None,
                    epsilon: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR', 'RGBA', 'STRING'] = 'FLOAT',
                    mode: Literal['ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION'] = 'ELEMENT',
                    operation: Literal['LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL'] = 'GREATER_THAN'):
        """ > Node <&Node Compare>

        Arguments
        ---------
        - a (Float) : socket 'A' (id: A)
        - b (Float) : socket 'B' (id: B)
        - a_1 (Integer) : socket 'A' (id: A_INT)
        - b_1 (Integer) : socket 'B' (id: B_INT)
        - a_2 (Vector) : socket 'A' (id: A_VEC3)
        - b_2 (Vector) : socket 'B' (id: B_VEC3)
        - a_3 (Color) : socket 'A' (id: A_COL)
        - b_3 (Color) : socket 'B' (id: B_COL)
        - a_4 (String) : socket 'A' (id: A_STR)
        - b_4 (String) : socket 'B' (id: B_STR)
        - c (Float) : socket 'C' (id: C)
        - angle (Float) : socket 'Angle' (id: Angle)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'VECTOR', 'RGBA', 'STRING']
        - mode (str): parameter 'mode' in ['ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION']
        - operation (str): parameter 'operation' in ['LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL']

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Compare', 'mode', mode, 'compare', ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION'))
        utils.check_enum_arg('Compare', 'operation', operation, 'compare', ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL'))
        node = Node('Compare', {'A': a, 'B': b, 'A_INT': a_1, 'B_INT': b_1, 'A_VEC3': a_2, 'B_VEC3': b_2, 'A_COL': a_3, 'B_COL': b_3, 'A_STR': a_4, 'B_STR': b_4, 'C': c, 'Angle': angle, 'Epsilon': epsilon}, data_type=data_type, mode=mode, operation=operation)
        return node._out

    @classmethod
    def euler_to_rotation(cls, euler: Vector = None):
        """ > Node <&Node Euler to Rotation>

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (id: Euler)

        Returns
        -------
        - Rotation
        """
        node = Node('Euler to Rotation', {'Euler': euler})
        return node._out

    @classmethod
    def find_in_string(cls, string: String = None, search: String = None):
        """ > Node <&Node Find in String>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)
        - search (String) : socket 'Search' (id: Search)

        Returns
        -------
        - Integer [count_ (Integer)]
        """
        node = Node('Find in String', {'String': string, 'Search': search})
        return node._out

    @classmethod
    def float_to_integer(cls,
                    float: Float = None,
                    rounding_mode: Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'] = 'ROUND'):
        """ > Node <&Node Float to Integer>

        Arguments
        ---------
        - float (Float) : socket 'Float' (id: Float)
        - rounding_mode (str): parameter 'rounding_mode' in ['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Float to Integer', 'rounding_mode', rounding_mode, 'float_to_integer', ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'))
        node = Node('Float to Integer', {'Float': float}, rounding_mode=rounding_mode)
        return node._out

    @classmethod
    def format_string(cls, named_sockets: dict = {}, format: String = None, **sockets):
        """ > Node <&Node Format String>

        Arguments
        ---------
        - format (String) : socket 'Format' (id: Format)

        Returns
        -------
        - String
        """
        node = Node('Format String', {'Format': format, **named_sockets}, **sockets)
        return node._out

    @classmethod
    def hash_value(cls,
                    value: Integer = None,
                    seed: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING'] = 'INT'):
        """ > Node <&Node Hash Value>

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING']

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': value, 'Seed': seed}, data_type=data_type)
        return node._out

    @classmethod
    def boolean(cls, boolean = False):
        """ > Node <&Node Boolean>

        Arguments
        ---------
        - boolean (bool): parameter 'boolean'

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean', boolean=boolean)
        return node._out

    @property
    def color(self):
        """ > Node <&Node Color>

        Returns
        -------
        - Color
        """
        node = Node('Color', )
        return node._out

    @classmethod
    def integer(cls, integer = 0):
        """ > Node <&Node Integer>

        Arguments
        ---------
        - integer (int): parameter 'integer'

        Returns
        -------
        - Integer
        """
        node = Node('Integer', integer=integer)
        return node._out

    @property
    def rotation(self):
        """ > Node <&Node Rotation>

        Returns
        -------
        - Rotation
        """
        node = Node('Rotation', )
        return node._out

    @classmethod
    def special_characters(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        - String [tab_ (String)]
        """
        node = Node('Special Characters', )
        return node

    @classmethod
    def string(cls, string = ''):
        """ > Node <&Node String>

        Arguments
        ---------
        - string (str): parameter 'string'

        Returns
        -------
        - String
        """
        node = Node('String', string=string)
        return node._out

    @property
    def vector(self):
        """ > Node <&Node Vector>

        Returns
        -------
        - Vector
        """
        node = Node('Vector', )
        return node._out

    @classmethod
    def integer_math(cls,
                    value: Integer = None,
                    value_1: Integer = None,
                    value_2: Integer = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM'] = 'ADD'):
        """ > Node <&Node Integer Math>

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value)
        - value_1 (Integer) : socket 'Value' (id: Value_001)
        - value_2 (Integer) : socket 'Value' (id: Value_002)
        - operation (str): parameter 'operation' in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Integer Math', 'operation', operation, 'integer_math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM'))
        node = Node('Integer Math', {'Value': value, 'Value_001': value_1, 'Value_002': value_2}, operation=operation)
        return node._out

    @classmethod
    def invert_matrix(cls, matrix: Matrix = None):
        """ > Node <&Node Invert Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Matrix [invertible_ (Boolean)]
        """
        node = Node('Invert Matrix', {'Matrix': matrix})
        return node._out

    @classmethod
    def invert_rotation(cls, rotation: Rotation = None):
        """ > Node <&Node Invert Rotation>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Rotation
        """
        node = Node('Invert Rotation', {'Rotation': rotation})
        return node._out

    @classmethod
    def match_string(cls,
                    string: String = None,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None):
        """ > Node <&Node Match String>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)
        - operation (menu='Starts With') : ('Starts With', 'Ends With', 'Contains')
        - key (String) : socket 'Key' (id: Key)

        Returns
        -------
        - Boolean
        """
        node = Node('Match String', {'String': string, 'Operation': operation, 'Key': key})
        return node._out

    @classmethod
    def matrix_determinant(cls, matrix: Matrix = None):
        """ > Node <&Node Matrix Determinant>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Float
        """
        node = Node('Matrix Determinant', {'Matrix': matrix})
        return node._out

    @classmethod
    def multiply_matrices(cls, matrix: Matrix = None, matrix_1: Matrix = None):
        """ > Node <&Node Multiply Matrices>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)
        - matrix_1 (Matrix) : socket 'Matrix' (id: Matrix_001)

        Returns
        -------
        - Matrix
        """
        node = Node('Multiply Matrices', {'Matrix': matrix, 'Matrix_001': matrix_1})
        return node._out

    @classmethod
    def project_point(cls, vector: Vector = None, transform: Matrix = None):
        """ > Node <&Node Project Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector
        """
        node = Node('Project Point', {'Vector': vector, 'Transform': transform})
        return node._out

    @classmethod
    def quaternion_to_rotation(cls, w: Float = None, x: Float = None, y: Float = None, z: Float = None):
        """ > Node <&Node Quaternion to Rotation>

        Arguments
        ---------
        - w (Float) : socket 'W' (id: W)
        - x (Float) : socket 'X' (id: X)
        - y (Float) : socket 'Y' (id: Y)
        - z (Float) : socket 'Z' (id: Z)

        Returns
        -------
        - Rotation
        """
        node = Node('Quaternion to Rotation', {'W': w, 'X': x, 'Y': y, 'Z': z})
        return node._out

    @classmethod
    def random_value(cls,
                    min: Vector = None,
                    max: Vector = None,
                    min_1: Float = None,
                    max_1: Float = None,
                    min_2: Integer = None,
                    max_2: Integer = None,
                    probability: Float = None,
                    id: Integer = None,
                    seed: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR'] = 'FLOAT'):
        """ > Node <&Node Random Value>

        Arguments
        ---------
        - min (Vector) : socket 'Min' (id: Min)
        - max (Vector) : socket 'Max' (id: Max)
        - min_1 (Float) : socket 'Min' (id: Min_001)
        - max_1 (Float) : socket 'Max' (id: Max_001)
        - min_2 (Integer) : socket 'Min' (id: Min_002)
        - max_2 (Integer) : socket 'Max' (id: Max_002)
        - probability (Float) : socket 'Probability' (id: Probability)
        - id (Integer) : socket 'ID' (id: ID)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Random Value', {'Min': min, 'Max': max, 'Min_001': min_1, 'Max_001': max_1, 'Min_002': min_2, 'Max_002': max_2, 'Probability': probability, 'ID': id, 'Seed': seed}, data_type=data_type)
        return node._out

    @classmethod
    def replace_string(cls, string: String = None, find: String = None, replace: String = None):
        """ > Node <&Node Replace String>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)
        - find (String) : socket 'Find' (id: Find)
        - replace (String) : socket 'Replace' (id: Replace)

        Returns
        -------
        - String
        """
        node = Node('Replace String', {'String': string, 'Find': find, 'Replace': replace})
        return node._out

    @classmethod
    def rotate_rotation(cls,
                    rotation: Rotation = None,
                    rotate_by: Rotation = None,
                    rotation_space: Literal['GLOBAL', 'LOCAL'] = 'GLOBAL'):
        """ > Node <&Node Rotate Rotation>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - rotate_by (Rotation) : socket 'Rotate By' (id: Rotate By)
        - rotation_space (str): parameter 'rotation_space' in ['GLOBAL', 'LOCAL']

        Returns
        -------
        - Rotation
        """
        utils.check_enum_arg('Rotate Rotation', 'rotation_space', rotation_space, 'rotate_rotation', ('GLOBAL', 'LOCAL'))
        node = Node('Rotate Rotation', {'Rotation': rotation, 'Rotate By': rotate_by}, rotation_space=rotation_space)
        return node._out

    @classmethod
    def rotate_vector(cls, vector: Vector = None, rotation: Rotation = None):
        """ > Node <&Node Rotate Vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Vector
        """
        node = Node('Rotate Vector', {'Vector': vector, 'Rotation': rotation})
        return node._out

    @classmethod
    def rotation_to_axis_angle(cls, rotation: Rotation = None):
        """ > Node <&Node Rotation to Axis Angle>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Vector [angle_ (Float)]
        """
        node = Node('Rotation to Axis Angle', {'Rotation': rotation})
        return node._out

    @classmethod
    def rotation_to_euler(cls, rotation: Rotation = None):
        """ > Node <&Node Rotation to Euler>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Vector
        """
        node = Node('Rotation to Euler', {'Rotation': rotation})
        return node._out

    @classmethod
    def rotation_to_quaternion(cls, rotation: Rotation = None):
        """ > Node <&Node Rotation to Quaternion>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Float [x_ (Float), y_ (Float), z_ (Float)]
        """
        node = Node('Rotation to Quaternion', {'Rotation': rotation})
        return node._out

    @classmethod
    def separate_color(cls, color: Color = None, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&Node Separate Color>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - mode (str): parameter 'mode' in ['RGB', 'HSV', 'HSL']

        Returns
        -------
        - Float [green_ (Float), blue_ (Float), alpha_ (Float)]
        """
        utils.check_enum_arg('Separate Color', 'mode', mode, 'separate_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Separate Color', {'Color': color}, mode=mode)
        return node

    @classmethod
    def separate_matrix(cls, matrix: Matrix = None):
        """ > Node <&Node Separate Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Float [column_1_row_2_ (Float), column_1_row_3_ (Float), column_1_row_4_ (Float), column_2_row_1_ (Float), column_2_row_2_ (Float), column_2_row_3_ (Float), column_2_row_4_ (Float), column_3_row_1_ (Float), column_3_row_2_ (Float), column_3_row_3_ (Float), column_3_row_4_ (Float), column_4_row_1_ (Float), column_4_row_2_ (Float), column_4_row_3_ (Float), column_4_row_4_ (Float)]
        """
        node = Node('Separate Matrix', {'Matrix': matrix})
        return node

    @classmethod
    def separate_transform(cls, transform: Matrix = None):
        """ > Node <&Node Separate Transform>

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector [rotation_ (Rotation), scale_ (Vector)]
        """
        node = Node('Separate Transform', {'Transform': transform})
        return node

    @classmethod
    def slice_string(cls, string: String = None, position: Integer = None, length: Integer = None):
        """ > Node <&Node Slice String>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)
        - position (Integer) : socket 'Position' (id: Position)
        - length (Integer) : socket 'Length' (id: Length)

        Returns
        -------
        - String
        """
        node = Node('Slice String', {'String': string, 'Position': position, 'Length': length})
        return node._out

    @classmethod
    def string_length(cls, string: String = None):
        """ > Node <&Node String Length>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)

        Returns
        -------
        - Integer
        """
        node = Node('String Length', {'String': string})
        return node._out

    @classmethod
    def string_to_value(cls, string: String = None, data_type: Literal['FLOAT', 'INT'] = 'FLOAT'):
        """ > Node <&Node String to Value>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT']

        Returns
        -------
        - Float [length_ (Integer)]
        """
        node = Node('String to Value', {'String': string}, data_type=data_type)
        return node._out

    @classmethod
    def transform_direction(cls, direction: Vector = None, transform: Matrix = None):
        """ > Node <&Node Transform Direction>

        Arguments
        ---------
        - direction (Vector) : socket 'Direction' (id: Direction)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector
        """
        node = Node('Transform Direction', {'Direction': direction, 'Transform': transform})
        return node._out

    @classmethod
    def transform_point(cls, vector: Vector = None, transform: Matrix = None):
        """ > Node <&Node Transform Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector
        """
        node = Node('Transform Point', {'Vector': vector, 'Transform': transform})
        return node._out

    @classmethod
    def transpose_matrix(cls, matrix: Matrix = None):
        """ > Node <&Node Transpose Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Matrix
        """
        node = Node('Transpose Matrix', {'Matrix': matrix})
        return node._out

    @classmethod
    def value_to_string(cls,
                    value: Float = None,
                    decimals: Integer = None,
                    data_type: Literal['FLOAT', 'INT'] = 'FLOAT'):
        """ > Node <&Node Value to String>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - decimals (Integer) : socket 'Decimals' (id: Decimals)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT']

        Returns
        -------
        - String
        """
        node = Node('Value to String', {'Value': value, 'Decimals': decimals}, data_type=data_type)
        return node._out

    @classmethod
    def accumulate_field(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Accumulate Field>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        utils.check_enum_arg('Accumulate Field', 'domain', domain, 'accumulate_field', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def domain_size(cls,
                    geometry: Geometry = None,
                    component: Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL'] = 'MESH'):
        """ > Node <&Node Domain Size>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - component (str): parameter 'component' in ['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL']

        Returns
        -------
        - Integer [edge_count_ (Integer), face_count_ (Integer), face_corner_count_ (Integer)]
        """
        utils.check_enum_arg('Domain Size', 'component', component, 'domain_size', ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL'))
        node = Node('Domain Size', {'Geometry': geometry}, component=component)
        return node._out

    @classmethod
    def attribute_statistic(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    attribute: Float = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Attribute Statistic>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - attribute (Float) : socket 'Attribute' (id: Attribute)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'FLOAT_VECTOR']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        utils.check_enum_arg('Attribute Statistic', 'domain', domain, 'attribute_statistic', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Attribute Statistic', {'Geometry': geometry, 'Selection': selection, 'Attribute': attribute}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def bake(cls, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Bake>

        Returns
        -------
        - None
        """
        node = Node('Bake', named_sockets, **sockets)
        return node._out

    @classmethod
    def blur_attribute(cls,
                    value: Float = None,
                    iterations: Integer = None,
                    weight: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR'] = 'FLOAT'):
        """ > Node <&Node Blur Attribute>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)
        - weight (Float) : socket 'Weight' (id: Weight)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR']

        Returns
        -------
        - Float
        """
        node = Node('Blur Attribute', {'Value': value, 'Iterations': iterations, 'Weight': weight}, data_type=data_type)
        return node._out

    @classmethod
    def bounding_box(cls, geometry: Geometry = None, use_radius: Boolean = None):
        """ > Node <&Node Bounding Box>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - use_radius (Boolean) : socket 'Use Radius' (id: Use Radius)

        Returns
        -------
        - Mesh [min_ (Vector), max_ (Vector)]
        """
        node = Node('Bounding Box', {'Geometry': geometry, 'Use Radius': use_radius})
        return node._out

    @classmethod
    def camera_info(cls, camera: Object = None):
        """ > Node <&Node Camera Info>

        Arguments
        ---------
        - camera (Object) : socket 'Camera' (id: Camera)

        Returns
        -------
        - Matrix [focal_length_ (Float), sensor_ (Vector), shift_ (Vector), clip_start_ (Float), clip_end_ (Float), focus_distance_ (Float), is_orthographic_ (Boolean), orthographic_scale_ (Float)]
        """
        node = Node('Camera Info', {'Camera': camera})
        return node._out

    @classmethod
    def capture_attribute(cls,
                    named_sockets: dict = {},
                    geometry: Geometry = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT',
                    **sockets):
        """ > Node <&Node Capture Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Capture Attribute', 'domain', domain, 'capture_attribute', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Capture Attribute', {'Geometry': geometry, **named_sockets}, domain=domain, **sockets)
        return node._out

    @classmethod
    def collection_info(cls,
                    collection: Collection = None,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Collection Info>

        Arguments
        ---------
        - collection (Collection) : socket 'Collection' (id: Collection)
        - separate_children (Boolean) : socket 'Separate Children' (id: Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (id: Reset Children)
        - transform_space (str): parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']

        Returns
        -------
        - Instances
        """
        utils.check_enum_arg('Collection Info', 'transform_space', transform_space, 'collection_info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Collection Info', {'Collection': collection, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out

    @classmethod
    def convex_hull(cls, geometry: Geometry = None):
        """ > Node <&Node Convex Hull>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Mesh
        """
        node = Node('Convex Hull', {'Geometry': geometry})
        return node._out

    @classmethod
    def corners_of_edge(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (id: Edge Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_face(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Face>

        Arguments
        ---------
        - face_index (Integer) : socket 'Face Index' (id: Face Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_vertex(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def arc(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    offset_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS'):
        """ > Node <&Node Arc>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - middle (Vector) : socket 'Middle' (id: Middle)
        - end (Vector) : socket 'End' (id: End)
        - radius (Float) : socket 'Radius' (id: Radius)
        - start_angle (Float) : socket 'Start Angle' (id: Start Angle)
        - sweep_angle (Float) : socket 'Sweep Angle' (id: Sweep Angle)
        - offset_angle (Float) : socket 'Offset Angle' (id: Offset Angle)
        - connect_center (Boolean) : socket 'Connect Center' (id: Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (id: Invert Arc)
        - mode (str): parameter 'mode' in ['POINTS', 'RADIUS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Arc', 'mode', mode, 'arc', ('POINTS', 'RADIUS'))
        node = Node('Arc', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Offset Angle': offset_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode=mode)
        return node._out

    @classmethod
    def endpoint_selection(cls, start_size: Integer = None, end_size: Integer = None):
        """ > Node <&Node Endpoint Selection>

        Arguments
        ---------
        - start_size (Integer) : socket 'Start Size' (id: Start Size)
        - end_size (Integer) : socket 'End Size' (id: End Size)

        Returns
        -------
        - Boolean
        """
        node = Node('Endpoint Selection', {'Start Size': start_size, 'End Size': end_size})
        return node._out

    @classmethod
    def handle_type_selection(cls,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'}):
        """ > Node <&Node Handle Type Selection>

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
        - mode (set): parameter 'mode'

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Handle Type Selection', 'handle_type', handle_type, 'handle_type_selection', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Handle Type Selection', handle_type=handle_type, mode=mode)
        return node._out

    @classmethod
    def curve_length(cls, curve: Curve = None):
        """ > Node <&Node Curve Length>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)

        Returns
        -------
        - Float
        """
        node = Node('Curve Length', {'Curve': curve})
        return node._out

    @classmethod
    def curve_of_point(cls, point_index: Integer = None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - Integer [index_in_curve_ (Integer)]
        """
        node = Node('Curve of Point', {'Point Index': point_index})
        return node._out

    @classmethod
    def bezier_segment(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None,
                    mode: Literal['POSITION', 'OFFSET'] = 'POSITION'):
        """ > Node <&Node Bézier Segment>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - start_handle (Vector) : socket 'Start Handle' (id: Start Handle)
        - end_handle (Vector) : socket 'End Handle' (id: End Handle)
        - end (Vector) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ['POSITION', 'OFFSET']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Bézier Segment', 'mode', mode, 'bezier_segment', ('POSITION', 'OFFSET'))
        node = Node('Bézier Segment', {'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode=mode)
        return node._out

    @classmethod
    def curve_circle(cls,
                    resolution: Integer = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    radius: Float = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS'):
        """ > Node <&Node Curve Circle>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - point_1 (Vector) : socket 'Point 1' (id: Point 1)
        - point_2 (Vector) : socket 'Point 2' (id: Point 2)
        - point_3 (Vector) : socket 'Point 3' (id: Point 3)
        - radius (Float) : socket 'Radius' (id: Radius)
        - mode (str): parameter 'mode' in ['POINTS', 'RADIUS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Curve Circle', 'mode', mode, 'curve_circle', ('POINTS', 'RADIUS'))
        node = Node('Curve Circle', {'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Radius': radius}, mode=mode)
        return node._out

    @classmethod
    def curve_line(cls,
                    start: Vector = None,
                    end: Vector = None,
                    direction: Vector = None,
                    length: Float = None,
                    mode: Literal['POINTS', 'DIRECTION'] = 'POINTS'):
        """ > Node <&Node Curve Line>

        Arguments
        ---------
        - start (Vector) : socket 'Start' (id: Start)
        - end (Vector) : socket 'End' (id: End)
        - direction (Vector) : socket 'Direction' (id: Direction)
        - length (Float) : socket 'Length' (id: Length)
        - mode (str): parameter 'mode' in ['POINTS', 'DIRECTION']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Curve Line', 'mode', mode, 'curve_line', ('POINTS', 'DIRECTION'))
        node = Node('Curve Line', {'Start': start, 'End': end, 'Direction': direction, 'Length': length}, mode=mode)
        return node._out

    @classmethod
    def quadrilateral(cls,
                    width: Float = None,
                    height: Float = None,
                    bottom_width: Float = None,
                    top_width: Float = None,
                    offset: Float = None,
                    bottom_height: Float = None,
                    top_height: Float = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    point_4: Vector = None,
                    mode: Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'] = 'RECTANGLE'):
        """ > Node <&Node Quadrilateral>

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - height (Float) : socket 'Height' (id: Height)
        - bottom_width (Float) : socket 'Bottom Width' (id: Bottom Width)
        - top_width (Float) : socket 'Top Width' (id: Top Width)
        - offset (Float) : socket 'Offset' (id: Offset)
        - bottom_height (Float) : socket 'Bottom Height' (id: Bottom Height)
        - top_height (Float) : socket 'Top Height' (id: Top Height)
        - point_1 (Vector) : socket 'Point 1' (id: Point 1)
        - point_2 (Vector) : socket 'Point 2' (id: Point 2)
        - point_3 (Vector) : socket 'Point 3' (id: Point 3)
        - point_4 (Vector) : socket 'Point 4' (id: Point 4)
        - mode (str): parameter 'mode' in ['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Quadrilateral', 'mode', mode, 'quadrilateral', ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'))
        node = Node('Quadrilateral', {'Width': width, 'Height': height, 'Bottom Width': bottom_width, 'Top Width': top_width, 'Offset': offset, 'Bottom Height': bottom_height, 'Top Height': top_height, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Point 4': point_4}, mode=mode)
        return node._out

    @classmethod
    def quadratic_bezier(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None):
        """ > Node <&Node Quadratic Bézier>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - middle (Vector) : socket 'Middle' (id: Middle)
        - end (Vector) : socket 'End' (id: End)

        Returns
        -------
        - Curve
        """
        node = Node('Quadratic Bézier', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end})
        return node._out

    @classmethod
    def set_handle_type(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'}):
        """ > Node <&Node Set Handle Type>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
        - mode (set): parameter 'mode'

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': curve, 'Selection': selection}, handle_type=handle_type, mode=mode)
        return node._out

    @classmethod
    def spiral(cls,
                    resolution: Integer = None,
                    rotations: Float = None,
                    start_radius: Float = None,
                    end_radius: Float = None,
                    height: Float = None,
                    reverse: Boolean = None):
        """ > Node <&Node Spiral>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - rotations (Float) : socket 'Rotations' (id: Rotations)
        - start_radius (Float) : socket 'Start Radius' (id: Start Radius)
        - end_radius (Float) : socket 'End Radius' (id: End Radius)
        - height (Float) : socket 'Height' (id: Height)
        - reverse (Boolean) : socket 'Reverse' (id: Reverse)

        Returns
        -------
        - Curve
        """
        node = Node('Spiral', {'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius, 'End Radius': end_radius, 'Height': height, 'Reverse': reverse})
        return node._out

    @classmethod
    def set_spline_type(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY'):
        """ > Node <&Node Set Spline Type>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - spline_type (str): parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'set_spline_type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', {'Curve': curve, 'Selection': selection}, spline_type=spline_type)
        return node._out

    @classmethod
    def star(cls,
                    points: Integer = None,
                    inner_radius: Float = None,
                    outer_radius: Float = None,
                    twist: Float = None):
        """ > Node <&Node Star>

        Arguments
        ---------
        - points (Integer) : socket 'Points' (id: Points)
        - inner_radius (Float) : socket 'Inner Radius' (id: Inner Radius)
        - outer_radius (Float) : socket 'Outer Radius' (id: Outer Radius)
        - twist (Float) : socket 'Twist' (id: Twist)

        Returns
        -------
        - Curve [outer_points_ (Boolean)]
        """
        node = Node('Star', {'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})
        return node._out

    @classmethod
    def curve_to_mesh(cls,
                    curve: Curve = None,
                    profile_curve: Curve = None,
                    scale: Float = None,
                    fill_caps: Boolean = None):
        """ > Node <&Node Curve to Mesh>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - profile_curve (Curve) : socket 'Profile Curve' (id: Profile Curve)
        - scale (Float) : socket 'Scale' (id: Scale)
        - fill_caps (Boolean) : socket 'Fill Caps' (id: Fill Caps)

        Returns
        -------
        - Mesh
        """
        node = Node('Curve to Mesh', {'Curve': curve, 'Profile Curve': profile_curve, 'Scale': scale, 'Fill Caps': fill_caps})
        return node._out

    @classmethod
    def curve_to_points(cls,
                    curve: Curve = None,
                    count: Integer = None,
                    length: Float = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT'):
        """ > Node <&Node Curve to Points>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - count (Integer) : socket 'Count' (id: Count)
        - length (Float) : socket 'Length' (id: Length)
        - mode (str): parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        utils.check_enum_arg('Curve to Points', 'mode', mode, 'curve_to_points', ('EVALUATED', 'COUNT', 'LENGTH'))
        node = Node('Curve to Points', {'Curve': curve, 'Count': count, 'Length': length}, mode=mode)
        return node._out

    @classmethod
    def curves_to_grease_pencil(cls,
                    curves: Curve = None,
                    selection: Boolean = None,
                    instances_as_layers: Boolean = None):
        """ > Node <&Node Curves to Grease Pencil>

        Arguments
        ---------
        - curves (Curve) : socket 'Curves' (id: Curves)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - instances_as_layers (Boolean) : socket 'Instances as Layers' (id: Instances as Layers)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Curves to Grease Pencil', {'Curves': curves, 'Selection': selection, 'Instances as Layers': instances_as_layers})
        return node._out

    @classmethod
    def deform_curves_on_surface(cls, curves: Curve = None):
        """ > Node <&Node Deform Curves on Surface>

        Arguments
        ---------
        - curves (Curve) : socket 'Curves' (id: Curves)

        Returns
        -------
        - Curve
        """
        node = Node('Deform Curves on Surface', {'Curves': curves})
        return node._out

    @classmethod
    def delete_geometry(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT',
                    mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER']
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'domain', domain, 'delete_geometry', ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'))
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': geometry, 'Selection': selection}, domain=domain, mode=mode)
        return node._out

    @classmethod
    def distribute_points_in_grid(cls,
                    grid: Float = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None,
                    mode: Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - mode (str): parameter 'mode' in ['DENSITY_RANDOM', 'DENSITY_GRID']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Distribute Points in Grid', 'mode', mode, 'distribute_points_in_grid', ('DENSITY_RANDOM', 'DENSITY_GRID'))
        node = Node('Distribute Points in Grid', {'Grid': grid, 'Density': density, 'Seed': seed, 'Spacing': spacing, 'Threshold': threshold}, mode=mode)
        return node._out

    @classmethod
    def distribute_points_in_volume(cls,
                    volume: Volume = None,
                    mode: Literal['Random', 'Grid'] = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None):
        """ > Node <&Node Distribute Points in Volume>

        Arguments
        ---------
        - volume (Volume) : socket 'Volume' (id: Volume)
        - mode (menu='Random') : ('Random', 'Grid')
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Volume', {'Volume': volume, 'Mode': mode, 'Density': density, 'Seed': seed, 'Spacing': spacing, 'Threshold': threshold})
        return node._out

    @classmethod
    def distribute_points_on_faces(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM'):
        """ > Node <&Node Distribute Points on Faces>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - distance_min (Float) : socket 'Distance Min' (id: Distance Min)
        - density_max (Float) : socket 'Density Max' (id: Density Max)
        - density (Float) : socket 'Density' (id: Density)
        - density_factor (Float) : socket 'Density Factor' (id: Density Factor)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - distribute_method (str): parameter 'distribute_method' in ['RANDOM', 'POISSON']

        Returns
        -------
        - Cloud [normal_ (Vector), rotation_ (Rotation)]
        """
        utils.check_enum_arg('Distribute Points on Faces', 'distribute_method', distribute_method, 'distribute_points_on_faces', ('RANDOM', 'POISSON'))
        node = Node('Distribute Points on Faces', {'Mesh': mesh, 'Selection': selection, 'Distance Min': distance_min, 'Density Max': density_max, 'Density': density, 'Density Factor': density_factor, 'Seed': seed}, distribute_method=distribute_method)
        return node._out

    @classmethod
    def dual_mesh(cls, mesh: Mesh = None, keep_boundaries: Boolean = None):
        """ > Node <&Node Dual Mesh>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - keep_boundaries (Boolean) : socket 'Keep Boundaries' (id: Keep Boundaries)

        Returns
        -------
        - Mesh
        """
        node = Node('Dual Mesh', {'Mesh': mesh, 'Keep Boundaries': keep_boundaries})
        return node._out

    @classmethod
    def duplicate_elements(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    amount: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE'] = 'POINT'):
        """ > Node <&Node Duplicate Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - amount (Integer) : socket 'Amount' (id: Amount)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE']

        Returns
        -------
        - Geometry [duplicate_index_ (Integer)]
        """
        utils.check_enum_arg('Duplicate Elements', 'domain', domain, 'duplicate_elements', ('POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE'))
        node = Node('Duplicate Elements', {'Geometry': geometry, 'Selection': selection, 'Amount': amount}, domain=domain)
        return node._out

    @classmethod
    def edge_paths_to_curves(cls,
                    mesh: Mesh = None,
                    start_vertices: Boolean = None,
                    next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Curves>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Curve
        """
        node = Node('Edge Paths to Curves', {'Mesh': mesh, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edge_paths_to_selection(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Selection>

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Boolean
        """
        node = Node('Edge Paths to Selection', {'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edges_of_corner(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [previous_edge_index_ (Integer)]
        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def edges_of_vertex(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def edges_to_face_groups(cls, boundary_edges: Boolean = None):
        """ > Node <&Node Edges to Face Groups>

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (id: Boundary Edges)

        Returns
        -------
        - Integer
        """
        node = Node('Edges to Face Groups', {'Boundary Edges': boundary_edges})
        return node._out

    @classmethod
    def extrude_mesh(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES'):
        """ > Node <&Node Extrude Mesh>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - offset_scale (Float) : socket 'Offset Scale' (id: Offset Scale)
        - individual (Boolean) : socket 'Individual' (id: Individual)
        - mode (str): parameter 'mode' in ['VERTICES', 'EDGES', 'FACES']

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean)]
        """
        utils.check_enum_arg('Extrude Mesh', 'mode', mode, 'extrude_mesh', ('VERTICES', 'EDGES', 'FACES'))
        node = Node('Extrude Mesh', {'Mesh': mesh, 'Selection': selection, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode=mode)
        return node._out

    @classmethod
    def face_of_corner(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [index_in_face_ (Integer)]
        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def evaluate_at_index(cls,
                    value: Float = None,
                    index: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Evaluate at Index>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Evaluate at Index', 'domain', domain, 'evaluate_at_index', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_average(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Average>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'FLOAT_VECTOR']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [median_ (Float)]
        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_min_max(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Min & Max>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [max_ (Float)]
        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Evaluate on Domain>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Evaluate on Domain', 'domain', domain, 'evaluate_on_domain', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_to_grid(cls,
                    named_sockets: dict = {},
                    topology: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT',
                    **sockets):
        """ > Node <&Node Field to Grid>

        Arguments
        ---------
        - topology (Float) : socket 'Topology' (id: Topology)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - None
        """
        node = Node('Field to Grid', {'Topology': topology, **named_sockets}, data_type=data_type, **sockets)
        return node._out

    @classmethod
    def field_variance(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Variance>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'FLOAT_VECTOR']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [variance_ (Float)]
        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def fill_curve(cls,
                    curve: Curve = None,
                    group_id: Integer = None,
                    mode: Literal['Triangles', 'N-gons'] = None):
        """ > Node <&Node Fill Curve>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - mode (menu='Triangles') : ('Triangles', 'N-gons')

        Returns
        -------
        - Mesh
        """
        node = Node('Fill Curve', {'Curve': curve, 'Group ID': group_id, 'Mode': mode})
        return node._out

    @classmethod
    def fillet_curve(cls,
                    curve: Curve = None,
                    radius: Float = None,
                    limit_radius: Boolean = None,
                    mode: Literal['Bézier', 'Poly'] = None,
                    count: Integer = None):
        """ > Node <&Node Fillet Curve>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - radius (Float) : socket 'Radius' (id: Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (id: Limit Radius)
        - mode (menu='Bézier') : ('Bézier', 'Poly')
        - count (Integer) : socket 'Count' (id: Count)

        Returns
        -------
        - Curve
        """
        node = Node('Fillet Curve', {'Curve': curve, 'Radius': radius, 'Limit Radius': limit_radius, 'Mode': mode, 'Count': count})
        return node._out

    @classmethod
    def flip_faces(cls, mesh: Mesh = None, selection: Boolean = None):
        """ > Node <&Node Flip Faces>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Mesh
        """
        node = Node('Flip Faces', {'Mesh': mesh, 'Selection': selection})
        return node._out

    @classmethod
    def for_each_geometry_element_input(cls, geometry: Geometry = None, selection: Boolean = None):
        """ > Node <&Node For Each Geometry Element Input>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Integer
        """
        node = Node('For Each Geometry Element Input', {'Geometry': geometry, 'Selection': selection})
        return node._out

    @classmethod
    def for_each_geometry_element_output(cls,
                    geometry: Geometry = None,
                    active_generation_index = 0,
                    active_input_index = 0,
                    active_main_index = 0,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT',
                    inspection_index = 0):
        """ > Node <&Node For Each Geometry Element Output>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Generation_0)
        - active_generation_index (int): parameter 'active_generation_index'
        - active_input_index (int): parameter 'active_input_index'
        - active_main_index (int): parameter 'active_main_index'
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']
        - inspection_index (int): parameter 'inspection_index'

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('For Each Geometry Element Output', 'domain', domain, 'for_each_geometry_element_output', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('For Each Geometry Element Output', {'Generation_0': geometry}, active_generation_index=active_generation_index, active_input_index=active_input_index, active_main_index=active_main_index, domain=domain, inspection_index=inspection_index)
        return node._out

    @classmethod
    def geometry_to_instance(cls, *geometry: Geometry):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Instances
        """
        node = Node('Geometry to Instance', {'Geometry': list(geometry)})
        return node._out

    @classmethod
    def get_named_grid(cls,
                    volume: Volume = None,
                    name: String = None,
                    remove: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Get Named Grid>

        Arguments
        ---------
        - volume (Volume) : socket 'Volume' (id: Volume)
        - name (String) : socket 'Name' (id: Name)
        - remove (Boolean) : socket 'Remove' (id: Remove)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Volume [grid_ (Float)]
        """
        node = Node('Get Named Grid', {'Volume': volume, 'Name': name, 'Remove': remove}, data_type=data_type)
        return node._out

    @classmethod
    def dial_gizmo(cls,
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
        node = Node('Dial Gizmo', {'Value': list(value), 'Position': position, 'Up': up, 'Screen Space': screen_space, 'Radius': radius}, color_id=color_id)
        return node._out

    @classmethod
    def linear_gizmo(cls,
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
        node = Node('Linear Gizmo', {'Value': list(value), 'Position': position, 'Direction': direction}, color_id=color_id, draw_style=draw_style)
        return node._out

    @classmethod
    def transform_gizmo(cls,
                    *value: Matrix,
                    position: Vector = None,
                    rotation: Rotation = None,
                    use_rotation_x = True,
                    use_rotation_y = True,
                    use_rotation_z = True,
                    use_scale_x = True,
                    use_scale_y = True,
                    use_scale_z = True,
                    use_translation_x = True,
                    use_translation_y = True,
                    use_translation_z = True):
        """ > Node <&Node Transform Gizmo>

        Arguments
        ---------
        - value (Matrix) : socket 'Value' (id: Value)
        - position (Vector) : socket 'Position' (id: Position)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - use_rotation_x (bool): parameter 'use_rotation_x'
        - use_rotation_y (bool): parameter 'use_rotation_y'
        - use_rotation_z (bool): parameter 'use_rotation_z'
        - use_scale_x (bool): parameter 'use_scale_x'
        - use_scale_y (bool): parameter 'use_scale_y'
        - use_scale_z (bool): parameter 'use_scale_z'
        - use_translation_x (bool): parameter 'use_translation_x'
        - use_translation_y (bool): parameter 'use_translation_y'
        - use_translation_z (bool): parameter 'use_translation_z'

        Returns
        -------
        - Geometry
        """
        node = Node('Transform Gizmo', {'Value': list(value), 'Position': position, 'Rotation': rotation}, use_rotation_x=use_rotation_x, use_rotation_y=use_rotation_y, use_rotation_z=use_rotation_z, use_scale_x=use_scale_x, use_scale_y=use_scale_y, use_scale_z=use_scale_z, use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)
        return node._out

    @classmethod
    def grease_pencil_to_curves(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    layers_as_instances: Boolean = None):
        """ > Node <&Node Grease Pencil to Curves>

        Arguments
        ---------
        - grease_pencil (GreasePencil) : socket 'Grease Pencil' (id: Grease Pencil)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - layers_as_instances (Boolean) : socket 'Layers as Instances' (id: Layers as Instances)

        Returns
        -------
        - Curve
        """
        node = Node('Grease Pencil to Curves', {'Grease Pencil': grease_pencil, 'Selection': selection, 'Layers as Instances': layers_as_instances})
        return node._out

    @classmethod
    def advect_grid(cls,
                    grid: Float = None,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Advect Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - velocity (Vector) : socket 'Velocity' (id: Velocity)
        - time_step (Float) : socket 'Time Step' (id: Time Step)
        - integration_scheme (menu='Runge-Kutta 3') : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
        - limiter (menu='Clamp') : ('None', 'Clamp', 'Revert')
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Advect Grid', {'Grid': grid, 'Velocity': velocity, 'Time Step': time_step, 'Integration Scheme': integration_scheme, 'Limiter': limiter}, data_type=data_type)
        return node._out

    @classmethod
    def grid_curl(cls, grid: Vector = None):
        """ > Node <&Node Grid Curl>

        Arguments
        ---------
        - grid (Vector) : socket 'Grid' (id: Grid)

        Returns
        -------
        - Vector
        """
        node = Node('Grid Curl', {'Grid': grid})
        return node._out

    @classmethod
    def grid_divergence(cls, grid: Vector = None):
        """ > Node <&Node Grid Divergence>

        Arguments
        ---------
        - grid (Vector) : socket 'Grid' (id: Grid)

        Returns
        -------
        - Float
        """
        node = Node('Grid Divergence', {'Grid': grid})
        return node._out

    @classmethod
    def grid_gradient(cls, grid: Float = None):
        """ > Node <&Node Grid Gradient>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)

        Returns
        -------
        - Vector
        """
        node = Node('Grid Gradient', {'Grid': grid})
        return node._out

    @classmethod
    def grid_info(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Grid Info>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Matrix [background_value_ (Float)]
        """
        node = Node('Grid Info', {'Grid': grid}, data_type=data_type)
        return node._out

    @classmethod
    def grid_laplacian(cls, grid: Float = None):
        """ > Node <&Node Grid Laplacian>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)

        Returns
        -------
        - Float
        """
        node = Node('Grid Laplacian', {'Grid': grid})
        return node._out

    @classmethod
    def prune_grid(cls,
                    grid: Float = None,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Prune Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - mode (menu='Threshold') : ('Inactive', 'Threshold', 'SDF')
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Prune Grid', {'Grid': grid, 'Mode': mode, 'Threshold': threshold}, data_type=data_type)
        return node._out

    @classmethod
    def grid_to_mesh(cls, grid: Float = None, threshold: Float = None, adaptivity: Float = None):
        """ > Node <&Node Grid to Mesh>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Grid to Mesh', {'Grid': grid, 'Threshold': threshold, 'Adaptivity': adaptivity})
        return node._out

    @classmethod
    def voxelize_grid(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Voxelize Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Voxelize Grid', {'Grid': grid}, data_type=data_type)
        return node._out

    @classmethod
    def group(cls, node_tree = None):
        """ > Node <&Node Group>

        Arguments
        ---------
        - node_tree (NoneType): parameter 'node_tree'

        Returns
        -------
        - None
        """
        node = Node('Group', node_tree=node_tree)
        return node._out

    @classmethod
    def image_info(cls, image: Image = None, frame: Integer = None):
        """ > Node <&Node Image Info>

        Arguments
        ---------
        - image (Image) : socket 'Image' (id: Image)
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - Integer [height_ (Integer), has_alpha_ (Boolean), frame_count_ (Integer), fps_ (Float)]
        """
        node = Node('Image Info', {'Image': image, 'Frame': frame})
        return node._out

    @classmethod
    def image_texture(cls,
                    image: Image = None,
                    vector: Vector = None,
                    frame: Integer = None,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    interpolation: Literal['Linear', 'Closest', 'Cubic'] = 'Linear'):
        """ > Node <&Node Image Texture>

        Arguments
        ---------
        - image (Image) : socket 'Image' (id: Image)
        - vector (Vector) : socket 'Vector' (id: Vector)
        - frame (Integer) : socket 'Frame' (id: Frame)
        - extension (str): parameter 'extension' in ['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
        - interpolation (str): parameter 'interpolation' in ['Linear', 'Closest', 'Cubic']

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        utils.check_enum_arg('Image Texture', 'extension', extension, 'image_texture', ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'))
        utils.check_enum_arg('Image Texture', 'interpolation', interpolation, 'image_texture', ('Linear', 'Closest', 'Cubic'))
        node = Node('Image Texture', {'Image': image, 'Vector': vector, 'Frame': frame}, extension=extension, interpolation=interpolation)
        return node._out

    @classmethod
    def import_csv(cls, path: String = None, delimiter: String = None):
        """ > Node <&Node Import CSV>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)
        - delimiter (String) : socket 'Delimiter' (id: Delimiter)

        Returns
        -------
        - Cloud
        """
        node = Node('Import CSV', {'Path': path, 'Delimiter': delimiter})
        return node._out

    @classmethod
    def import_obj(cls, path: String = None):
        """ > Node <&Node Import OBJ>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Instances
        """
        node = Node('Import OBJ', {'Path': path})
        return node._out

    @classmethod
    def import_ply(cls, path: String = None):
        """ > Node <&Node Import PLY>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import PLY', {'Path': path})
        return node._out

    @classmethod
    def import_stl(cls, path: String = None):
        """ > Node <&Node Import STL>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import STL', {'Path': path})
        return node._out

    @classmethod
    def import_text(cls, path: String = None):
        """ > Node <&Node Import Text>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - String
        """
        node = Node('Import Text', {'Path': path})
        return node._out

    @classmethod
    def import_vdb(cls, path: String = None):
        """ > Node <&Node Import VDB>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Volume
        """
        node = Node('Import VDB', {'Path': path})
        return node._out

    @classmethod
    def index_of_nearest(cls, position: Vector = None, group_id: Integer = None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Integer [has_neighbor_ (Boolean)]
        """
        node = Node('Index of Nearest', {'Position': position, 'Group ID': group_id})
        return node._out

    @classmethod
    def index_switch(cls,
                    named_sockets: dict = {},
                    index: Integer = None,
                    _0: Geometry = None,
                    _1: Geometry = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE'] = 'GEOMETRY',
                    **sockets):
        """ > Node <&Node Index Switch>

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - _0 (Geometry) : socket '0' (id: Item_0)
        - _1 (Geometry) : socket '1' (id: Item_1)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE']

        Returns
        -------
        - Geometry
        """
        node = Node('Index Switch', {'Index': index, 'Item_0': _0, 'Item_1': _1, **named_sockets}, data_type=data_type, **sockets)
        return node._out

    @property
    def active_camera(self):
        """ > Node <&Node Active Camera>

        Returns
        -------
        - Object
        """
        node = Node('Active Camera', )
        return node._out

    @classmethod
    def collection(cls, collection = None):
        """ > Node <&Node Collection>

        Arguments
        ---------
        - collection (NoneType): parameter 'collection'

        Returns
        -------
        - Collection
        """
        node = Node('Collection', collection=collection)
        return node._out

    @classmethod
    def curve_handle_positions(cls, relative: Boolean = None):
        """ > Node <&Node Curve Handle Positions>

        Arguments
        ---------
        - relative (Boolean) : socket 'Relative' (id: Relative)

        Returns
        -------
        - Vector [right_ (Vector)]
        """
        node = Node('Curve Handle Positions', {'Relative': relative})
        return node._out

    @property
    def curve_tilt(self):
        """ > Node <&Node Curve Tilt>

        Returns
        -------
        - Float
        """
        node = Node('Curve Tilt', )
        return node._out

    @property
    def is_edge_smooth(self):
        """ > Node <&Node Is Edge Smooth>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Edge Smooth', )
        return node._out

    @property
    def id(self):
        """ > Node <&Node ID>

        Returns
        -------
        - Integer
        """
        node = Node('ID', )
        return node._out

    @classmethod
    def image(cls, image = None):
        """ > Node <&Node Image>

        Arguments
        ---------
        - image (NoneType): parameter 'image'

        Returns
        -------
        - Image
        """
        node = Node('Image', image=image)
        return node._out

    @property
    def index(self):
        """ > Node <&Node Index>

        Returns
        -------
        - Integer
        """
        node = Node('Index', )
        return node._out

    @classmethod
    def instance_bounds(cls, use_radius: Boolean = None):
        """ > Node <&Node Instance Bounds>

        Arguments
        ---------
        - use_radius (Boolean) : socket 'Use Radius' (id: Use Radius)

        Returns
        -------
        - Vector [max_ (Vector)]
        """
        node = Node('Instance Bounds', {'Use Radius': use_radius})
        return node._out

    @property
    def instance_rotation(self):
        """ > Node <&Node Instance Rotation>

        Returns
        -------
        - Rotation
        """
        node = Node('Instance Rotation', )
        return node._out

    @property
    def instance_scale(self):
        """ > Node <&Node Instance Scale>

        Returns
        -------
        - Vector
        """
        node = Node('Instance Scale', )
        return node._out

    @classmethod
    def material(cls, material = None):
        """ > Node <&Node Material>

        Arguments
        ---------
        - material (NoneType): parameter 'material'

        Returns
        -------
        - Material
        """
        node = Node('Material', material=material)
        return node._out

    @property
    def material_index(self):
        """ > Node <&Node Material Index>

        Returns
        -------
        - Integer
        """
        node = Node('Material Index', )
        return node._out

    @classmethod
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - Float [signed_angle_ (Float)]
        """
        node = Node('Edge Angle', )
        return node

    @property
    def edge_neighbors(self):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        - Integer
        """
        node = Node('Edge Neighbors', )
        return node._out

    @classmethod
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - Integer [vertex_index_2_ (Integer), position_1_ (Vector), position_2_ (Vector)]
        """
        node = Node('Edge Vertices', )
        return node

    @property
    def face_area(self):
        """ > Node <&Node Face Area>

        Returns
        -------
        - Float
        """
        node = Node('Face Area', )
        return node._out

    @classmethod
    def is_face_planar(cls, threshold: Float = None):
        """ > Node <&Node Is Face Planar>

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Boolean
        """
        node = Node('Is Face Planar', {'Threshold': threshold})
        return node._out

    @classmethod
    def face_neighbors(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        - Integer [face_count_ (Integer)]
        """
        node = Node('Face Neighbors', )
        return node

    @classmethod
    def mesh_island(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        - Integer [island_count_ (Integer)]
        """
        node = Node('Mesh Island', )
        return node

    @classmethod
    def vertex_neighbors(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        - Integer [face_count_ (Integer)]
        """
        node = Node('Vertex Neighbors', )
        return node

    @classmethod
    def named_attribute(cls,
                    name: String = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT'):
        """ > Node <&Node Named Attribute>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Float [exists_ (Boolean)]
        """
        node = Node('Named Attribute', {'Name': name}, data_type=data_type)
        return node._out

    @classmethod
    def named_layer_selection(cls, name: String = None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', {'Name': name})
        return node._out

    @property
    def normal(self):
        """ > Node <&Node Normal>

        Returns
        -------
        - Vector [true_normal_ (Vector)]
        """
        node = Node('Normal', )
        return node._out

    @classmethod
    def object(cls, object = None):
        """ > Node <&Node Object>

        Arguments
        ---------
        - object (NoneType): parameter 'object'

        Returns
        -------
        - Object
        """
        node = Node('Object', object=object)
        return node._out

    @property
    def position(self):
        """ > Node <&Node Position>

        Returns
        -------
        - Vector
        """
        node = Node('Position', )
        return node._out

    @property
    def radius(self):
        """ > Node <&Node Radius>

        Returns
        -------
        - Float
        """
        node = Node('Radius', )
        return node._out

    @classmethod
    def scene_time(cls):
        """ > Node <&Node Scene Time>

        Returns
        -------
        - Float [frame_ (Float)]
        """
        node = Node('Scene Time', )
        return node

    @property
    def is_face_smooth(self):
        """ > Node <&Node Is Face Smooth>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Face Smooth', )
        return node._out

    @classmethod
    def shortest_edge_paths(cls, end_vertex: Boolean = None, edge_cost: Float = None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (id: End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (id: Edge Cost)

        Returns
        -------
        - Integer [total_cost_ (Float)]
        """
        node = Node('Shortest Edge Paths', {'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    @property
    def is_spline_cyclic(self):
        """ > Node <&Node Is Spline Cyclic>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Spline Cyclic', )
        return node._out

    @property
    def spline_resolution(self):
        """ > Node <&Node Spline Resolution>

        Returns
        -------
        - Integer
        """
        node = Node('Spline Resolution', )
        return node._out

    @property
    def curve_tangent(self):
        """ > Node <&Node Curve Tangent>

        Returns
        -------
        - Vector
        """
        node = Node('Curve Tangent', )
        return node._out

    @classmethod
    def voxel_index(cls):
        """ > Node <&Node Voxel Index>

        Returns
        -------
        - Integer [y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_x_ (Integer), extent_y_ (Integer), extent_z_ (Integer)]
        """
        node = Node('Voxel Index', )
        return node

    @classmethod
    def instance_on_points(cls,
                    points: Cloud = None,
                    selection: Boolean = None,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Instance on Points>

        Arguments
        ---------
        - points (Cloud) : socket 'Points' (id: Points)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - instance (Instances) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', {'Points': points, 'Selection': selection, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    @property
    def instance_transform(self):
        """ > Node <&Node Instance Transform>

        Returns
        -------
        - Matrix
        """
        node = Node('Instance Transform', )
        return node._out

    @classmethod
    def instances_to_points(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    radius: Float = None):
        """ > Node <&Node Instances to Points>

        Arguments
        ---------
        - instances (Instances) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Instances to Points', {'Instances': instances, 'Selection': selection, 'Position': position, 'Radius': radius})
        return node._out

    @classmethod
    def interpolate_curves(cls,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None):
        """ > Node <&Node Interpolate Curves>

        Arguments
        ---------
        - guide_curves (Curve) : socket 'Guide Curves' (id: Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - points (Cloud) : socket 'Points' (id: Points)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve [closest_index_ (Integer), closest_weight_ (Float)]
        """
        node = Node('Interpolate Curves', {'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node._out

    @property
    def is_viewport(self):
        """ > Node <&Node Is Viewport>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Viewport', )
        return node._out

    @classmethod
    def join_geometry(cls, *geometry: Geometry):
        """ > Node <&Node Join Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Geometry
        """
        node = Node('Join Geometry', {'Geometry': list(geometry)})
        return node._out

    @classmethod
    def list(cls,
                    count: Integer = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'MENU'] = 'FLOAT'):
        """ > Node <&Node List>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'MENU']

        Returns
        -------
        - Float
        """
        node = Node('List', {'Count': count, 'Value': value}, data_type=data_type)
        return node._out

    @classmethod
    def get_list_item(cls,
                    list: Float = None,
                    index: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'MENU'] = 'FLOAT'):
        """ > Node <&Node Get List Item>

        Arguments
        ---------
        - list (Float) : socket 'List' (id: List)
        - index (Integer) : socket 'Index' (id: Index)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'MENU']

        Returns
        -------
        - Float
        """
        node = Node('Get List Item', {'List': list, 'Index': index}, data_type=data_type)
        return node._out

    @classmethod
    def list_length(cls,
                    list: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'MENU'] = 'FLOAT'):
        """ > Node <&Node List Length>

        Arguments
        ---------
        - list (Float) : socket 'List' (id: List)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'MENU']

        Returns
        -------
        - Integer
        """
        node = Node('List Length', {'List': list}, data_type=data_type)
        return node._out

    @classmethod
    def material_selection(cls, material: Material = None):
        """ > Node <&Node Material Selection>

        Arguments
        ---------
        - material (Material) : socket 'Material' (id: Material)

        Returns
        -------
        - Boolean
        """
        node = Node('Material Selection', {'Material': material})
        return node._out

    @classmethod
    def menu_switch(cls,
                    named_sockets: dict = {},
                    menu = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE'] = 'GEOMETRY',
                    **sockets):
        """ > Node <&Node Menu Switch>

        Arguments
        ---------
        - Default selection
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE']

        Returns
        -------
        - Geometry [a_ (Boolean), b_ (Boolean)]
        """
        node = Node('Menu Switch', {'Menu': menu, **named_sockets}, data_type=data_type, **sockets)
        return node._out

    @classmethod
    def merge_by_distance(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    mode: Literal['All', 'Connected'] = None,
                    distance: Float = None):
        """ > Node <&Node Merge by Distance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - mode (menu='All') : ('All', 'Connected')
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Geometry
        """
        node = Node('Merge by Distance', {'Geometry': geometry, 'Selection': selection, 'Mode': mode, 'Distance': distance})
        return node._out

    @classmethod
    def merge_layers(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    mode: Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        Arguments
        ---------
        - grease_pencil (GreasePencil) : socket 'Grease Pencil' (id: Grease Pencil)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - mode (str): parameter 'mode' in ['MERGE_BY_NAME', 'MERGE_BY_ID']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Merge Layers', 'mode', mode, 'merge_layers', ('MERGE_BY_NAME', 'MERGE_BY_ID'))
        node = Node('Merge Layers', {'Grease Pencil': grease_pencil, 'Selection': selection, 'Group ID': group_id}, mode=mode)
        return node._out

    @classmethod
    def mesh_boolean(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    self_intersection: Boolean = None,
                    hole_tolerant: Boolean = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Arguments
        ---------
        - mesh_1 (Mesh) : socket 'Mesh 1' (id: Mesh 1)
        - mesh_2 (Mesh) : socket 'Mesh 2' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - operation (str): parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'operation', operation, 'mesh_boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'mesh_boolean', ('EXACT', 'FLOAT', 'MANIFOLD'))
        node = Node('Mesh Boolean', {'Mesh 1': mesh_1, 'Mesh 2': list(mesh_2), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation=operation, solver=solver)
        return node._out

    @classmethod
    def mesh_circle(cls,
                    vertices: Integer = None,
                    radius: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE'):
        """ > Node <&Node Mesh Circle>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (id: Vertices)
        - radius (Float) : socket 'Radius' (id: Radius)
        - fill_type (str): parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Circle', 'fill_type', fill_type, 'mesh_circle', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Mesh Circle', {'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        return node._out

    @classmethod
    def cone(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius_top: Float = None,
                    radius_bottom: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON'):
        """ > Node <&Node Cone>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (id: Vertices)
        - side_segments (Integer) : socket 'Side Segments' (id: Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (id: Fill Segments)
        - radius_top (Float) : socket 'Radius Top' (id: Radius Top)
        - radius_bottom (Float) : socket 'Radius Bottom' (id: Radius Bottom)
        - depth (Float) : socket 'Depth' (id: Depth)
        - fill_type (str): parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']

        Returns
        -------
        - Mesh [top_ (Boolean), bottom_ (Boolean), side_ (Boolean), uv_map_ (Vector)]
        """
        utils.check_enum_arg('Cone', 'fill_type', fill_type, 'cone', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Cone', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        return node._out

    @classmethod
    def cube(cls,
                    size: Vector = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None,
                    vertices_z: Integer = None):
        """ > Node <&Node Cube>

        Arguments
        ---------
        - size (Vector) : socket 'Size' (id: Size)
        - vertices_x (Integer) : socket 'Vertices X' (id: Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (id: Vertices Y)
        - vertices_z (Integer) : socket 'Vertices Z' (id: Vertices Z)

        Returns
        -------
        - Mesh [uv_map_ (Vector)]
        """
        node = Node('Cube', {'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        return node._out

    @classmethod
    def cylinder(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON'):
        """ > Node <&Node Cylinder>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (id: Vertices)
        - side_segments (Integer) : socket 'Side Segments' (id: Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (id: Fill Segments)
        - radius (Float) : socket 'Radius' (id: Radius)
        - depth (Float) : socket 'Depth' (id: Depth)
        - fill_type (str): parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean), bottom_ (Boolean), uv_map_ (Vector)]
        """
        utils.check_enum_arg('Cylinder', 'fill_type', fill_type, 'cylinder', ('NONE', 'NGON', 'TRIANGLE_FAN'))
        node = Node('Cylinder', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius': radius, 'Depth': depth}, fill_type=fill_type)
        return node._out

    @classmethod
    def face_group_boundaries(cls, face_group_id: Integer = None):
        """ > Node <&Node Face Group Boundaries>

        Arguments
        ---------
        - face_group_id (Integer) : socket 'Face Group ID' (id: Face Set)

        Returns
        -------
        - Boolean
        """
        node = Node('Face Group Boundaries', {'Face Set': face_group_id})
        return node._out

    @classmethod
    def grid(cls,
                    size_x: Float = None,
                    size_y: Float = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None):
        """ > Node <&Node Grid>

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (id: Size X)
        - size_y (Float) : socket 'Size Y' (id: Size Y)
        - vertices_x (Integer) : socket 'Vertices X' (id: Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (id: Vertices Y)

        Returns
        -------
        - Mesh [uv_map_ (Vector)]
        """
        node = Node('Grid', {'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        return node._out

    @classmethod
    def ico_sphere(cls, radius: Float = None, subdivisions: Integer = None):
        """ > Node <&Node Ico Sphere>

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - subdivisions (Integer) : socket 'Subdivisions' (id: Subdivisions)

        Returns
        -------
        - Mesh [uv_map_ (Vector)]
        """
        node = Node('Ico Sphere', {'Radius': radius, 'Subdivisions': subdivisions})
        return node._out

    @classmethod
    def mesh_line(cls,
                    count: Integer = None,
                    resolution: Float = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL',
                    mode: Literal['OFFSET', 'END_POINTS'] = 'OFFSET'):
        """ > Node <&Node Mesh Line>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - resolution (Float) : socket 'Resolution' (id: Resolution)
        - start_location (Vector) : socket 'Start Location' (id: Start Location)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - count_mode (str): parameter 'count_mode' in ['TOTAL', 'RESOLUTION']
        - mode (str): parameter 'mode' in ['OFFSET', 'END_POINTS']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Line', 'count_mode', count_mode, 'mesh_line', ('TOTAL', 'RESOLUTION'))
        utils.check_enum_arg('Mesh Line', 'mode', mode, 'mesh_line', ('OFFSET', 'END_POINTS'))
        node = Node('Mesh Line', {'Count': count, 'Resolution': resolution, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode=mode)
        return node._out

    @classmethod
    def mesh_to_curve(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    mode: Literal['EDGES', 'FACES'] = 'EDGES'):
        """ > Node <&Node Mesh to Curve>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - mode (str): parameter 'mode' in ['EDGES', 'FACES']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Mesh to Curve', 'mode', mode, 'mesh_to_curve', ('EDGES', 'FACES'))
        node = Node('Mesh to Curve', {'Mesh': mesh, 'Selection': selection}, mode=mode)
        return node._out

    @classmethod
    def mesh_to_density_grid(cls,
                    mesh: Mesh = None,
                    density: Float = None,
                    voxel_size: Float = None,
                    gradient_width: Float = None):
        """ > Node <&Node Mesh to Density Grid>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - density (Float) : socket 'Density' (id: Density)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - gradient_width (Float) : socket 'Gradient Width' (id: Gradient Width)

        Returns
        -------
        - Float
        """
        node = Node('Mesh to Density Grid', {'Mesh': mesh, 'Density': density, 'Voxel Size': voxel_size, 'Gradient Width': gradient_width})
        return node._out

    @classmethod
    def mesh_to_points(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    radius: Float = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES'):
        """ > Node <&Node Mesh to Points>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)
        - mode (str): parameter 'mode' in ['VERTICES', 'EDGES', 'FACES', 'CORNERS']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Mesh to Points', 'mode', mode, 'mesh_to_points', ('VERTICES', 'EDGES', 'FACES', 'CORNERS'))
        node = Node('Mesh to Points', {'Mesh': mesh, 'Selection': selection, 'Position': position, 'Radius': radius}, mode=mode)
        return node._out

    @classmethod
    def mesh_to_sdf_grid(cls, mesh: Mesh = None, voxel_size: Float = None, band_width: Integer = None):
        """ > Node <&Node Mesh to SDF Grid>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - band_width (Integer) : socket 'Band Width' (id: Band Width)

        Returns
        -------
        - Float
        """
        node = Node('Mesh to SDF Grid', {'Mesh': mesh, 'Voxel Size': voxel_size, 'Band Width': band_width})
        return node._out

    @classmethod
    def mesh_to_volume(cls,
                    mesh: Mesh = None,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    interior_band_width: Float = None):
        """ > Node <&Node Mesh to Volume>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - density (Float) : socket 'Density' (id: Density)
        - resolution_mode (menu='Amount') : ('Amount', 'Size')
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - interior_band_width (Float) : socket 'Interior Band Width' (id: Interior Band Width)

        Returns
        -------
        - Volume
        """
        node = Node('Mesh to Volume', {'Mesh': mesh, 'Density': density, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width})
        return node._out

    @classmethod
    def uv_sphere(cls, segments: Integer = None, rings: Integer = None, radius: Float = None):
        """ > Node <&Node UV Sphere>

        Arguments
        ---------
        - segments (Integer) : socket 'Segments' (id: Segments)
        - rings (Integer) : socket 'Rings' (id: Rings)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Mesh [uv_map_ (Vector)]
        """
        node = Node('UV Sphere', {'Segments': segments, 'Rings': rings, 'Radius': radius})
        return node._out

    @classmethod
    def object_info(cls,
                    object: Object = None,
                    as_instance: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Object Info>

        Arguments
        ---------
        - object (Object) : socket 'Object' (id: Object)
        - as_instance (Boolean) : socket 'As Instance' (id: As Instance)
        - transform_space (str): parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']

        Returns
        -------
        - Matrix [location_ (Vector), rotation_ (Rotation), scale_ (Vector), geometry_ (Geometry)]
        """
        utils.check_enum_arg('Object Info', 'transform_space', transform_space, 'object_info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Object Info', {'Object': object, 'As Instance': as_instance}, transform_space=transform_space)
        return node._out

    @classmethod
    def offset_corner_in_face(cls, corner_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Corner in Face>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Integer
        """
        node = Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})
        return node._out

    @classmethod
    def offset_point_in_curve(cls, point_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Point in Curve>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Boolean [point_index_ (Integer)]
        """
        node = Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset})
        return node._out

    @classmethod
    def points(cls, count: Integer = None, position: Vector = None, radius: Float = None):
        """ > Node <&Node Points>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Points', {'Count': count, 'Position': position, 'Radius': radius})
        return node._out

    @classmethod
    def points_of_curve(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def points_to_curves(cls,
                    points: Cloud = None,
                    curve_group_id: Integer = None,
                    weight: Float = None):
        """ > Node <&Node Points to Curves>

        Arguments
        ---------
        - points (Cloud) : socket 'Points' (id: Points)
        - curve_group_id (Integer) : socket 'Curve Group ID' (id: Curve Group ID)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Curve
        """
        node = Node('Points to Curves', {'Points': points, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out

    @classmethod
    def points_to_sdf_grid(cls, points: Cloud = None, radius: Float = None, voxel_size: Float = None):
        """ > Node <&Node Points to SDF Grid>

        Arguments
        ---------
        - points (Cloud) : socket 'Points' (id: Points)
        - radius (Float) : socket 'Radius' (id: Radius)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)

        Returns
        -------
        - Float
        """
        node = Node('Points to SDF Grid', {'Points': points, 'Radius': radius, 'Voxel Size': voxel_size})
        return node._out

    @classmethod
    def points_to_vertices(cls, points: Cloud = None, selection: Boolean = None):
        """ > Node <&Node Points to Vertices>

        Arguments
        ---------
        - points (Cloud) : socket 'Points' (id: Points)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Mesh
        """
        node = Node('Points to Vertices', {'Points': points, 'Selection': selection})
        return node._out

    @classmethod
    def points_to_volume(cls,
                    points: Cloud = None,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    radius: Float = None):
        """ > Node <&Node Points to Volume>

        Arguments
        ---------
        - points (Cloud) : socket 'Points' (id: Points)
        - density (Float) : socket 'Density' (id: Density)
        - resolution_mode (menu='Amount') : ('Amount', 'Size')
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Volume
        """
        node = Node('Points to Volume', {'Points': points, 'Density': density, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Radius': radius})
        return node._out

    @classmethod
    def geometry_proximity(cls,
                    geometry: Geometry = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES'):
        """ > Node <&Node Geometry Proximity>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Target)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)
        - target_element (str): parameter 'target_element' in ['POINTS', 'EDGES', 'FACES']

        Returns
        -------
        - Vector [distance_ (Float), is_valid_ (Boolean)]
        """
        utils.check_enum_arg('Geometry Proximity', 'target_element', target_element, 'geometry_proximity', ('POINTS', 'EDGES', 'FACES'))
        node = Node('Geometry Proximity', {'Target': geometry, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=target_element)
        return node._out

    @classmethod
    def raycast(cls,
                    target_geometry: Geometry = None,
                    attribute: Float = None,
                    interpolation: Literal['Interpolated', 'Nearest'] = None,
                    source_position: Vector = None,
                    ray_direction: Vector = None,
                    ray_length: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT'):
        """ > Node <&Node Raycast>

        Arguments
        ---------
        - target_geometry (Geometry) : socket 'Target Geometry' (id: Target Geometry)
        - attribute (Float) : socket 'Attribute' (id: Attribute)
        - interpolation (menu='Interpolated') : ('Interpolated', 'Nearest')
        - source_position (Vector) : socket 'Source Position' (id: Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (id: Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (id: Ray Length)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Boolean [hit_position_ (Vector), hit_normal_ (Vector), hit_distance_ (Float), attribute_ (Float)]
        """
        node = Node('Raycast', {'Target Geometry': target_geometry, 'Attribute': attribute, 'Interpolation': interpolation, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type)
        return node._out

    @classmethod
    def realize_instances(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    realize_all: Boolean = None,
                    depth: Integer = None):
        """ > Node <&Node Realize Instances>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - realize_all (Boolean) : socket 'Realize All' (id: Realize All)
        - depth (Integer) : socket 'Depth' (id: Depth)

        Returns
        -------
        - Geometry
        """
        node = Node('Realize Instances', {'Geometry': geometry, 'Selection': selection, 'Realize All': realize_all, 'Depth': depth})
        return node._out

    @classmethod
    def remove_named_attribute(cls,
                    geometry: Geometry = None,
                    pattern_mode: Literal['Exact', 'Wildcard'] = None,
                    name: String = None):
        """ > Node <&Node Remove Named Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - pattern_mode (menu='Exact') : ('Exact', 'Wildcard')
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Remove Named Attribute', {'Geometry': geometry, 'Pattern Mode': pattern_mode, 'Name': name})
        return node._out

    @classmethod
    def repeat_input(cls, iterations: Integer = None):
        """ > Node <&Node Repeat Input>

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Integer
        """
        node = Node('Repeat Input', {'Iterations': iterations})
        return node._out

    @classmethod
    def repeat_output(cls, geometry: Geometry = None, inspection_index = 0):
        """ > Node <&Node Repeat Output>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Item_0)
        - inspection_index (int): parameter 'inspection_index'

        Returns
        -------
        - Geometry
        """
        node = Node('Repeat Output', {'Item_0': geometry}, inspection_index=inspection_index)
        return node._out

    @classmethod
    def replace_material(cls, geometry: Geometry = None, old: Material = None, new: Material = None):
        """ > Node <&Node Replace Material>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - old (Material) : socket 'Old' (id: Old)
        - new (Material) : socket 'New' (id: New)

        Returns
        -------
        - Geometry
        """
        node = Node('Replace Material', {'Geometry': geometry, 'Old': old, 'New': new})
        return node._out

    @classmethod
    def resample_curve(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    mode: Literal['Evaluated', 'Count', 'Length'] = None,
                    count: Integer = None,
                    length: Float = None,
                    keep_last_segment = True):
        """ > Node <&Node Resample Curve>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - mode (menu='Count') : ('Evaluated', 'Count', 'Length')
        - count (Integer) : socket 'Count' (id: Count)
        - length (Float) : socket 'Length' (id: Length)
        - keep_last_segment (bool): parameter 'keep_last_segment'

        Returns
        -------
        - Curve
        """
        node = Node('Resample Curve', {'Curve': curve, 'Selection': selection, 'Mode': mode, 'Count': count, 'Length': length}, keep_last_segment=keep_last_segment)
        return node._out

    @classmethod
    def reverse_curve(cls, curve: Curve = None, selection: Boolean = None):
        """ > Node <&Node Reverse Curve>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Curve
        """
        node = Node('Reverse Curve', {'Curve': curve, 'Selection': selection})
        return node._out

    @classmethod
    def rotate_instances(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    rotation: Rotation = None,
                    pivot_point: Vector = None,
                    local_space: Boolean = None):
        """ > Node <&Node Rotate Instances>

        Arguments
        ---------
        - instances (Instances) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - pivot_point (Vector) : socket 'Pivot Point' (id: Pivot Point)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Rotate Instances', {'Instances': instances, 'Selection': selection, 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})
        return node._out

    @classmethod
    def sdf_grid_boolean(cls,
                    *grid_2: Float,
                    grid_1: Float = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE'):
        """ > Node <&Node SDF Grid Boolean>

        Arguments
        ---------
        - grid_1 (Float) : socket 'Grid 1' (id: Grid 1)
        - grid_2 (Float) : socket 'Grid 2' (id: Grid 2)
        - operation (str): parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('SDF Grid Boolean', 'operation', operation, 'sdf_grid_boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        node = Node('SDF Grid Boolean', {'Grid 1': grid_1, 'Grid 2': list(grid_2)}, operation=operation)
        return node._out

    @classmethod
    def sdf_grid_fillet(cls, grid: Float = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Fillet>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Fillet', {'Grid': grid, 'Iterations': iterations})
        return node._out

    @classmethod
    def sdf_grid_laplacian(cls, grid: Float = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Laplacian>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Laplacian', {'Grid': grid, 'Iterations': iterations})
        return node._out

    @classmethod
    def sdf_grid_mean(cls, grid: Float = None, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Mean>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - width (Integer) : socket 'Width' (id: Width)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Mean', {'Grid': grid, 'Width': width, 'Iterations': iterations})
        return node._out

    @classmethod
    def sdf_grid_mean_curvature(cls, grid: Float = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Mean Curvature>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Mean Curvature', {'Grid': grid, 'Iterations': iterations})
        return node._out

    @classmethod
    def sdf_grid_median(cls, grid: Float = None, width: Integer = None, iterations: Integer = None):
        """ > Node <&Node SDF Grid Median>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - width (Integer) : socket 'Width' (id: Width)
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Median', {'Grid': grid, 'Width': width, 'Iterations': iterations})
        return node._out

    @classmethod
    def sdf_grid_offset(cls, grid: Float = None, distance: Float = None):
        """ > Node <&Node SDF Grid Offset>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Float
        """
        node = Node('SDF Grid Offset', {'Grid': grid, 'Distance': distance})
        return node._out

    @classmethod
    def sample_curve(cls,
                    curves: Curve = None,
                    value: Float = None,
                    length: Float = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR',
                    use_all_curves = False):
        """ > Node <&Node Sample Curve>

        Arguments
        ---------
        - curves (Curve) : socket 'Curves' (id: Curves)
        - value (Float) : socket 'Value' (id: Value)
        - length (Float) : socket 'Length' (id: Length)
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - factor (Float) : socket 'Factor' (id: Factor)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']
        - mode (str): parameter 'mode' in ['FACTOR', 'LENGTH']
        - use_all_curves (bool): parameter 'use_all_curves'

        Returns
        -------
        - Float [position_ (Vector), tangent_ (Vector), normal_ (Vector)]
        """
        utils.check_enum_arg('Sample Curve', 'mode', mode, 'sample_curve', ('FACTOR', 'LENGTH'))
        node = Node('Sample Curve', {'Curves': curves, 'Value': value, 'Length': length, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode=mode, use_all_curves=use_all_curves)
        return node._out

    @classmethod
    def sample_grid(cls,
                    grid: Float = None,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Sample Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation (menu='Trilinear') : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Sample Grid', {'Grid': grid, 'Position': position, 'Interpolation': interpolation}, data_type=data_type)
        return node._out

    @classmethod
    def sample_grid_index(cls,
                    grid: Float = None,
                    x: Integer = None,
                    y: Integer = None,
                    z: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Sample Grid Index>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - x (Integer) : socket 'X' (id: X)
        - y (Integer) : socket 'Y' (id: Y)
        - z (Integer) : socket 'Z' (id: Z)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Sample Grid Index', {'Grid': grid, 'X': x, 'Y': y, 'Z': z}, data_type=data_type)
        return node._out

    @classmethod
    def sample_index(cls,
                    geometry: Geometry = None,
                    value: Float = None,
                    index: Integer = None,
                    clamp = False,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Sample Index>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Sample Index', 'domain', domain, 'sample_index', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Sample Index', {'Geometry': geometry, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def sample_nearest(cls,
                    geometry: Geometry = None,
                    sample_position: Vector = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER'] = 'POINT'):
        """ > Node <&Node Sample Nearest>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Sample Nearest', 'domain', domain, 'sample_nearest', ('POINT', 'EDGE', 'FACE', 'CORNER'))
        node = Node('Sample Nearest', {'Geometry': geometry, 'Sample Position': sample_position}, domain=domain)
        return node._out

    @classmethod
    def sample_nearest_surface(cls,
                    mesh: Mesh = None,
                    value: Float = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT'):
        """ > Node <&Node Sample Nearest Surface>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Float [is_valid_ (Boolean)]
        """
        node = Node('Sample Nearest Surface', {'Mesh': mesh, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)
        return node._out

    @classmethod
    def sample_uv_surface(cls,
                    mesh: Mesh = None,
                    value: Float = None,
                    uv_map: Vector = None,
                    sample_uv: Vector = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT'):
        """ > Node <&Node Sample UV Surface>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - value (Float) : socket 'Value' (id: Value)
        - uv_map (Vector) : socket 'UV Map' (id: Source UV Map)
        - sample_uv (Vector) : socket 'Sample UV' (id: Sample UV)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Float [is_valid_ (Boolean)]
        """
        node = Node('Sample UV Surface', {'Mesh': mesh, 'Value': value, 'Source UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)
        return node._out

    @classmethod
    def scale_elements(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None,
                    domain: Literal['FACE', 'EDGE'] = 'FACE'):
        """ > Node <&Node Scale Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - scale_mode (menu='Uniform') : ('Uniform', 'Single Axis')
        - axis (Vector) : socket 'Axis' (id: Axis)
        - domain (str): parameter 'domain' in ['FACE', 'EDGE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Scale Elements', 'domain', domain, 'scale_elements', ('FACE', 'EDGE'))
        node = Node('Scale Elements', {'Geometry': geometry, 'Selection': selection, 'Scale': scale, 'Center': center, 'Scale Mode': scale_mode, 'Axis': axis}, domain=domain)
        return node._out

    @classmethod
    def scale_instances(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    scale: Vector = None,
                    center: Vector = None,
                    local_space: Boolean = None):
        """ > Node <&Node Scale Instances>

        Arguments
        ---------
        - instances (Instances) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Scale Instances', {'Instances': instances, 'Selection': selection, 'Scale': scale, 'Center': center, 'Local Space': local_space})
        return node._out

    @property
    def self_object(self):
        """ > Node <&Node Self Object>

        Returns
        -------
        - Object
        """
        node = Node('Self Object', )
        return node._out

    @classmethod
    def separate_components(cls, geometry: Geometry = None):
        """ > Node <&Node Separate Components>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Mesh [curve_ (Curve), grease_pencil_ (GreasePencil), point_cloud_ (Cloud), volume_ (Volume), instances_ (Instances)]
        """
        node = Node('Separate Components', {'Geometry': geometry})
        return node

    @classmethod
    def separate_geometry(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Separate Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Geometry [inverted_ (Geometry)]
        """
        utils.check_enum_arg('Separate Geometry', 'domain', domain, 'separate_geometry', ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Separate Geometry', {'Geometry': geometry, 'Selection': selection}, domain=domain)
        return node

    @classmethod
    def set_handle_positions(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    offset: Vector = None,
                    mode: Literal['LEFT', 'RIGHT'] = 'LEFT'):
        """ > Node <&Node Set Handle Positions>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - mode (str): parameter 'mode' in ['LEFT', 'RIGHT']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Positions', 'mode', mode, 'set_handle_positions', ('LEFT', 'RIGHT'))
        node = Node('Set Handle Positions', {'Curve': curve, 'Selection': selection, 'Position': position, 'Offset': offset}, mode=mode)
        return node._out

    @classmethod
    def set_curve_normal(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None,
                    normal: Vector = None):
        """ > Node <&Node Set Curve Normal>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - mode (menu='Minimum Twist') : ('Minimum Twist', 'Z Up', 'Free')
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', {'Curve': curve, 'Selection': selection, 'Mode': mode, 'Normal': normal})
        return node._out

    @classmethod
    def set_curve_radius(cls, curve: Curve = None, selection: Boolean = None, radius: Float = None):
        """ > Node <&Node Set Curve Radius>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Radius', {'Curve': curve, 'Selection': selection, 'Radius': radius})
        return node._out

    @classmethod
    def set_curve_tilt(cls, curve: Curve = None, selection: Boolean = None, tilt: Float = None):
        """ > Node <&Node Set Curve Tilt>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - tilt (Float) : socket 'Tilt' (id: Tilt)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Tilt', {'Curve': curve, 'Selection': selection, 'Tilt': tilt})
        return node._out

    @classmethod
    def set_geometry_name(cls, geometry: Geometry = None, name: String = None):
        """ > Node <&Node Set Geometry Name>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Geometry Name', {'Geometry': geometry, 'Name': name})
        return node._out

    @classmethod
    def set_grease_pencil_color(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    color: Color = None,
                    opacity: Float = None,
                    mode: Literal['STROKE', 'FILL'] = 'STROKE'):
        """ > Node <&Node Set Grease Pencil Color>

        Arguments
        ---------
        - grease_pencil (GreasePencil) : socket 'Grease Pencil' (id: Grease Pencil)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - color (Color) : socket 'Color' (id: Color)
        - opacity (Float) : socket 'Opacity' (id: Opacity)
        - mode (str): parameter 'mode' in ['STROKE', 'FILL']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Color', 'mode', mode, 'set_grease_pencil_color', ('STROKE', 'FILL'))
        node = Node('Set Grease Pencil Color', {'Grease Pencil': grease_pencil, 'Selection': selection, 'Color': color, 'Opacity': opacity}, mode=mode)
        return node._out

    @classmethod
    def set_grease_pencil_depth(cls,
                    grease_pencil: GreasePencil = None,
                    depth_order: Literal['2D', '3D'] = '2D'):
        """ > Node <&Node Set Grease Pencil Depth>

        Arguments
        ---------
        - grease_pencil (GreasePencil) : socket 'Grease Pencil' (id: Grease Pencil)
        - depth_order (str): parameter 'depth_order' in ['2D', '3D']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Set Grease Pencil Depth', 'depth_order', depth_order, 'set_grease_pencil_depth', ('2D', '3D'))
        node = Node('Set Grease Pencil Depth', {'Grease Pencil': grease_pencil}, depth_order=depth_order)
        return node._out

    @classmethod
    def set_grease_pencil_softness(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    softness: Float = None):
        """ > Node <&Node Set Grease Pencil Softness>

        Arguments
        ---------
        - grease_pencil (GreasePencil) : socket 'Grease Pencil' (id: Grease Pencil)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - softness (Float) : socket 'Softness' (id: Softness)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Set Grease Pencil Softness', {'Grease Pencil': grease_pencil, 'Selection': selection, 'Softness': softness})
        return node._out

    @classmethod
    def set_grid_background(cls,
                    grid: Float = None,
                    background: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Set Grid Background>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - background (Float) : socket 'Background' (id: Background)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Float
        """
        node = Node('Set Grid Background', {'Grid': grid, 'Background': background}, data_type=data_type)
        return node._out

    @classmethod
    def set_grid_transform(cls,
                    grid: Float = None,
                    transform: Matrix = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Set Grid Transform>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - transform (Matrix) : socket 'Transform' (id: Transform)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - Boolean [grid_ (Float)]
        """
        node = Node('Set Grid Transform', {'Grid': grid, 'Transform': transform}, data_type=data_type)
        return node._out

    @classmethod
    def set_id(cls, geometry: Geometry = None, selection: Boolean = None, id: Integer = None):
        """ > Node <&Node Set ID>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - id (Integer) : socket 'ID' (id: ID)

        Returns
        -------
        - Geometry
        """
        node = Node('Set ID', {'Geometry': geometry, 'Selection': selection, 'ID': id})
        return node._out

    @classmethod
    def set_instance_transform(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    transform: Matrix = None):
        """ > Node <&Node Set Instance Transform>

        Arguments
        ---------
        - instances (Instances) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Instances
        """
        node = Node('Set Instance Transform', {'Instances': instances, 'Selection': selection, 'Transform': transform})
        return node._out

    @classmethod
    def set_material(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    material: Material = None):
        """ > Node <&Node Set Material>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - material (Material) : socket 'Material' (id: Material)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Material', {'Geometry': geometry, 'Selection': selection, 'Material': material})
        return node._out

    @classmethod
    def set_material_index(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    material_index: Integer = None):
        """ > Node <&Node Set Material Index>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - material_index (Integer) : socket 'Material Index' (id: Material Index)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Material Index', {'Geometry': geometry, 'Selection': selection, 'Material Index': material_index})
        return node._out

    @classmethod
    def set_mesh_normal(cls,
                    mesh: Mesh = None,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT',
                    mode: Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS'):
        """ > Node <&Node Set Mesh Normal>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - remove_custom (Boolean) : socket 'Remove Custom' (id: Remove Custom)
        - edge_sharpness (Boolean) : socket 'Edge Sharpness' (id: Edge Sharpness)
        - face_sharpness (Boolean) : socket 'Face Sharpness' (id: Face Sharpness)
        - domain (str): parameter 'domain' in ['POINT', 'FACE', 'CORNER']
        - mode (str): parameter 'mode' in ['SHARPNESS', 'FREE', 'TANGENT_SPACE']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Set Mesh Normal', 'domain', domain, 'set_mesh_normal', ('POINT', 'FACE', 'CORNER'))
        utils.check_enum_arg('Set Mesh Normal', 'mode', mode, 'set_mesh_normal', ('SHARPNESS', 'FREE', 'TANGENT_SPACE'))
        node = Node('Set Mesh Normal', {'Mesh': mesh, 'Remove Custom': remove_custom, 'Edge Sharpness': edge_sharpness, 'Face Sharpness': face_sharpness}, domain=domain, mode=mode)
        return node._out

    @classmethod
    def set_point_radius(cls, points: Cloud = None, selection: Boolean = None, radius: Float = None):
        """ > Node <&Node Set Point Radius>

        Arguments
        ---------
        - points (Cloud) : socket 'Points' (id: Points)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Set Point Radius', {'Points': points, 'Selection': selection, 'Radius': radius})
        return node._out

    @classmethod
    def set_position(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    offset: Vector = None):
        """ > Node <&Node Set Position>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Position', {'Geometry': geometry, 'Selection': selection, 'Position': position, 'Offset': offset})
        return node._out

    @classmethod
    def set_shade_smooth(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    shade_smooth: Boolean = None,
                    domain: Literal['EDGE', 'FACE'] = 'FACE'):
        """ > Node <&Node Set Shade Smooth>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)
        - domain (str): parameter 'domain' in ['EDGE', 'FACE']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Set Shade Smooth', 'domain', domain, 'set_shade_smooth', ('EDGE', 'FACE'))
        node = Node('Set Shade Smooth', {'Geometry': mesh, 'Selection': selection, 'Shade Smooth': shade_smooth}, domain=domain)
        return node._out

    @classmethod
    def set_spline_cyclic(cls, curve: Curve = None, selection: Boolean = None, cyclic: Boolean = None):
        """ > Node <&Node Set Spline Cyclic>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - cyclic (Boolean) : socket 'Cyclic' (id: Cyclic)

        Returns
        -------
        - Curve
        """
        node = Node('Set Spline Cyclic', {'Geometry': curve, 'Selection': selection, 'Cyclic': cyclic})
        return node._out

    @classmethod
    def set_spline_resolution(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    resolution: Integer = None):
        """ > Node <&Node Set Spline Resolution>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - resolution (Integer) : socket 'Resolution' (id: Resolution)

        Returns
        -------
        - Curve
        """
        node = Node('Set Spline Resolution', {'Geometry': curve, 'Selection': selection, 'Resolution': resolution})
        return node._out

    @property
    def simulation_input(self):
        """ > Node <&Node Simulation Input>

        Returns
        -------
        - Float
        """
        node = Node('Simulation Input', )
        return node._out

    @classmethod
    def simulation_output(cls, skip: Boolean = None, geometry: Geometry = None):
        """ > Node <&Node Simulation Output>

        Arguments
        ---------
        - skip (Boolean) : socket 'Skip' (id: Skip)
        - geometry (Geometry) : socket 'Geometry' (id: Item_0)

        Returns
        -------
        - Geometry
        """
        node = Node('Simulation Output', {'Skip': skip, 'Item_0': geometry})
        return node._out

    @classmethod
    def sort_elements(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    sort_weight: Float = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE'] = 'POINT'):
        """ > Node <&Node Sort Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (id: Sort Weight)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Sort Elements', 'domain', domain, 'sort_elements', ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE'))
        node = Node('Sort Elements', {'Geometry': geometry, 'Selection': selection, 'Group ID': group_id, 'Sort Weight': sort_weight}, domain=domain)
        return node._out

    @classmethod
    def spline_length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - Float [point_count_ (Integer)]
        """
        node = Node('Spline Length', )
        return node

    @classmethod
    def spline_parameter(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - Float [length_ (Float), index_ (Integer)]
        """
        node = Node('Spline Parameter', )
        return node

    @classmethod
    def split_edges(cls, mesh: Mesh = None, selection: Boolean = None):
        """ > Node <&Node Split Edges>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Mesh
        """
        node = Node('Split Edges', {'Mesh': mesh, 'Selection': selection})
        return node._out

    @classmethod
    def split_to_instances(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Split to Instances>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Instances [group_id_ (Integer)]
        """
        utils.check_enum_arg('Split to Instances', 'domain', domain, 'split_to_instances', ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Split to Instances', {'Geometry': geometry, 'Selection': selection, 'Group ID': group_id}, domain=domain)
        return node._out

    @classmethod
    def store_named_attribute(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    name: String = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'INT8', 'FLOAT2', 'BYTE_COLOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Store Named Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'INT8', 'FLOAT2', 'BYTE_COLOR']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Store Named Attribute', 'domain', domain, 'store_named_attribute', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Store Named Attribute', {'Geometry': geometry, 'Selection': selection, 'Name': name, 'Value': value}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def store_named_grid(cls,
                    volume: Volume = None,
                    name: String = None,
                    grid: Float = None,
                    data_type: Literal['BOOLEAN', 'FLOAT', 'INT', 'VECTOR_FLOAT'] = 'FLOAT'):
        """ > Node <&Node Store Named Grid>

        Arguments
        ---------
        - volume (Volume) : socket 'Volume' (id: Volume)
        - name (String) : socket 'Name' (id: Name)
        - grid (Float) : socket 'Grid' (id: Grid)
        - data_type (str): parameter 'data_type' in ['BOOLEAN', 'FLOAT', 'INT', 'VECTOR_FLOAT']

        Returns
        -------
        - Volume
        """
        node = Node('Store Named Grid', {'Volume': volume, 'Name': name, 'Grid': grid}, data_type=data_type)
        return node._out

    @classmethod
    def join_strings(cls, *strings: String, delimiter: String = None):
        """ > Node <&Node Join Strings>

        Arguments
        ---------
        - delimiter (String) : socket 'Delimiter' (id: Delimiter)
        - strings (String) : socket 'Strings' (id: Strings)

        Returns
        -------
        - String
        """
        node = Node('Join Strings', {'Delimiter': delimiter, 'Strings': list(strings)})
        return node._out

    @classmethod
    def string_to_curves(cls,
                    string: String = None,
                    size: Float = None,
                    character_spacing: Float = None,
                    word_spacing: Float = None,
                    line_spacing: Float = None,
                    text_box_width: Float = None,
                    text_box_height: Float = None,
                    align_x: Literal['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH'] = 'LEFT',
                    align_y: Literal['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM'] = 'TOP_BASELINE',
                    font = None,
                    overflow: Literal['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE'] = 'OVERFLOW',
                    pivot_mode: Literal['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT'] = 'BOTTOM_LEFT'):
        """ > Node <&Node String to Curves>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)
        - size (Float) : socket 'Size' (id: Size)
        - character_spacing (Float) : socket 'Character Spacing' (id: Character Spacing)
        - word_spacing (Float) : socket 'Word Spacing' (id: Word Spacing)
        - line_spacing (Float) : socket 'Line Spacing' (id: Line Spacing)
        - text_box_width (Float) : socket 'Text Box Width' (id: Text Box Width)
        - text_box_height (Float) : socket 'Text Box Height' (id: Text Box Height)
        - align_x (str): parameter 'align_x' in ['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH']
        - align_y (str): parameter 'align_y' in ['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM']
        - font (Blender VectorFont | str): VectorFont, or name of a valid font in bpy.types.fonts (see `utils.get_font`)
        - overflow (str): parameter 'overflow' in ['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE']
        - pivot_mode (str): parameter 'pivot_mode' in ['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT']

        Returns
        -------
        - Instances [line_ (Integer), pivot_point_ (Vector)]
        """
        utils.check_enum_arg('String to Curves', 'align_x', align_x, 'string_to_curves', ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH'))
        utils.check_enum_arg('String to Curves', 'align_y', align_y, 'string_to_curves', ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM'))
        utils.check_enum_arg('String to Curves', 'overflow', overflow, 'string_to_curves', ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE'))
        utils.check_enum_arg('String to Curves', 'pivot_mode', pivot_mode, 'string_to_curves', ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT'))
        node = Node('String to Curves', {'String': string, 'Size': size, 'Character Spacing': character_spacing, 'Word Spacing': word_spacing, 'Line Spacing': line_spacing, 'Text Box Width': text_box_width, 'Text Box Height': text_box_height}, align_x=align_x, align_y=align_y, font=utils.get_font(font), overflow=overflow, pivot_mode=pivot_mode)
        return node._out

    @classmethod
    def subdivide_curve(cls, curve: Curve = None, cuts: Integer = None):
        """ > Node <&Node Subdivide Curve>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - cuts (Integer) : socket 'Cuts' (id: Cuts)

        Returns
        -------
        - Curve
        """
        node = Node('Subdivide Curve', {'Curve': curve, 'Cuts': cuts})
        return node._out

    @classmethod
    def subdivide_mesh(cls, mesh: Mesh = None, level: Integer = None):
        """ > Node <&Node Subdivide Mesh>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - level (Integer) : socket 'Level' (id: Level)

        Returns
        -------
        - Mesh
        """
        node = Node('Subdivide Mesh', {'Mesh': mesh, 'Level': level})
        return node._out

    @classmethod
    def subdivision_surface(cls,
                    mesh: Mesh = None,
                    level: Integer = None,
                    edge_crease: Float = None,
                    vertex_crease: Float = None,
                    limit_surface: Boolean = None,
                    uv_smooth: Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All'] = None,
                    boundary_smooth: Literal['Keep Corners', 'All'] = None):
        """ > Node <&Node Subdivision Surface>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - level (Integer) : socket 'Level' (id: Level)
        - edge_crease (Float) : socket 'Edge Crease' (id: Edge Crease)
        - vertex_crease (Float) : socket 'Vertex Crease' (id: Vertex Crease)
        - limit_surface (Boolean) : socket 'Limit Surface' (id: Limit Surface)
        - uv_smooth (menu='Keep Boundaries') : ('None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All')
        - boundary_smooth (menu='All') : ('Keep Corners', 'All')

        Returns
        -------
        - Mesh
        """
        node = Node('Subdivision Surface', {'Mesh': mesh, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease, 'Limit Surface': limit_surface, 'UV Smooth': uv_smooth, 'Boundary Smooth': boundary_smooth})
        return node._out

    @classmethod
    def switch(cls,
                    switch: Boolean = None,
                    false: Geometry = None,
                    true: Geometry = None,
                    input_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE'] = 'GEOMETRY'):
        """ > Node <&Node Switch>

        Arguments
        ---------
        - switch (Boolean) : socket 'Switch' (id: Switch)
        - false (Geometry) : socket 'False' (id: False)
        - true (Geometry) : socket 'True' (id: True)
        - input_type (str): parameter 'input_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Switch', 'input_type', input_type, 'switch', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE'))
        node = Node('Switch', {'Switch': switch, 'False': false, 'True': true}, input_type=input_type)
        return node._out

    @classmethod
    def _3d_cursor(cls):
        """ > Node <&Node 3D Cursor>

        Returns
        -------
        - Vector [rotation_ (Rotation)]
        """
        node = Node('3D Cursor', )
        return node

    @classmethod
    def active_element(cls, domain: Literal['POINT', 'EDGE', 'FACE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Active Element>

        Arguments
        ---------
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'LAYER']

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        utils.check_enum_arg('Active Element', 'domain', domain, 'active_element', ('POINT', 'EDGE', 'FACE', 'LAYER'))
        node = Node('Active Element', domain=domain)
        return node

    @classmethod
    def face_set(cls):
        """ > Node <&Node Face Set>

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Face Set', )
        return node

    @classmethod
    def mouse_position(cls):
        """ > Node <&Node Mouse Position>

        Returns
        -------
        - Integer [mouse_y_ (Integer), region_width_ (Integer), region_height_ (Integer)]
        """
        node = Node('Mouse Position', )
        return node

    @classmethod
    def selection(cls):
        """ > Node <&Node Selection>

        Returns
        -------
        - Boolean [float_ (Float)]
        """
        node = Node('Selection', )
        return node

    @classmethod
    def set_face_set(cls, mesh: Mesh = None, selection: Boolean = None, face_set: Integer = None):
        """ > Node <&Node Set Face Set>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - face_set (Integer) : socket 'Face Set' (id: Face Set)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Face Set', {'Mesh': mesh, 'Selection': selection, 'Face Set': face_set})
        return node._out

    @classmethod
    def set_selection(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE'] = 'POINT',
                    selection_type: Literal['BOOLEAN', 'FLOAT'] = 'BOOLEAN'):
        """ > Node <&Node Set Selection>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CURVE']
        - selection_type (str): parameter 'selection_type' in ['BOOLEAN', 'FLOAT']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Set Selection', 'domain', domain, 'set_selection', ('POINT', 'EDGE', 'FACE', 'CURVE'))
        utils.check_enum_arg('Set Selection', 'selection_type', selection_type, 'set_selection', ('BOOLEAN', 'FLOAT'))
        node = Node('Set Selection', {'Geometry': geometry, 'Selection': selection}, domain=domain, selection_type=selection_type)
        return node._out

    @classmethod
    def transform_geometry(cls,
                    geometry: Geometry = None,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None):
        """ > Node <&Node Transform Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - mode (menu='Components') : ('Components', 'Matrix')
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Geometry
        """
        node = Node('Transform Geometry', {'Geometry': geometry, 'Mode': mode, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform})
        return node._out

    @classmethod
    def translate_instances(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    translation: Vector = None,
                    local_space: Boolean = None):
        """ > Node <&Node Translate Instances>

        Arguments
        ---------
        - instances (Instances) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - translation (Vector) : socket 'Translation' (id: Translation)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Translate Instances', {'Instances': instances, 'Selection': selection, 'Translation': translation, 'Local Space': local_space})
        return node._out

    @classmethod
    def triangulate(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    quad_method: Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal'] = None,
                    n_gon_method: Literal['Beauty', 'Clip'] = None):
        """ > Node <&Node Triangulate>

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - quad_method (menu='Shortest Diagonal') : ('Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal')
        - n_gon_method (menu='Beauty') : ('Beauty', 'Clip')

        Returns
        -------
        - Mesh
        """
        node = Node('Triangulate', {'Mesh': mesh, 'Selection': selection, 'Quad Method': quad_method, 'N-gon Method': n_gon_method})
        return node._out

    @classmethod
    def trim_curve(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    start: Float = None,
                    end: Float = None,
                    start_1: Float = None,
                    end_1: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR'):
        """ > Node <&Node Trim Curve>

        Arguments
        ---------
        - curve (Curve) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - start (Float) : socket 'Start' (id: Start)
        - end (Float) : socket 'End' (id: End)
        - start_1 (Float) : socket 'Start' (id: Start_001)
        - end_1 (Float) : socket 'End' (id: End_001)
        - mode (str): parameter 'mode' in ['FACTOR', 'LENGTH']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Trim Curve', 'mode', mode, 'trim_curve', ('FACTOR', 'LENGTH'))
        node = Node('Trim Curve', {'Curve': curve, 'Selection': selection, 'Start': start, 'End': end, 'Start_001': start_1, 'End_001': end_1}, mode=mode)
        return node._out

    @classmethod
    def pack_uv_islands(cls,
                    uv: Vector = None,
                    selection: Boolean = None,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None):
        """ > Node <&Node Pack UV Islands>

        Arguments
        ---------
        - uv (Vector) : socket 'UV' (id: UV)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - margin (Float) : socket 'Margin' (id: Margin)
        - rotate (Boolean) : socket 'Rotate' (id: Rotate)
        - method (menu='Bounding Box') : ('Bounding Box', 'Convex Hull', 'Exact Shape')

        Returns
        -------
        - Vector
        """
        node = Node('Pack UV Islands', {'UV': uv, 'Selection': selection, 'Margin': margin, 'Rotate': rotate, 'Method': method})
        return node._out

    @classmethod
    def uv_tangent(cls, method: Literal['Exact', 'Fast'] = None, uv: Vector = None):
        """ > Node <&Node UV Tangent>

        Arguments
        ---------
        - method (menu='Exact') : ('Exact', 'Fast')
        - uv (Vector) : socket 'UV' (id: UV)

        Returns
        -------
        - Vector
        """
        node = Node('UV Tangent', {'Method': method, 'UV': uv})
        return node._out

    @classmethod
    def uv_unwrap(cls,
                    selection: Boolean = None,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal'] = None):
        """ > Node <&Node UV Unwrap>

        Arguments
        ---------
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - seam (Boolean) : socket 'Seam' (id: Seam)
        - margin (Float) : socket 'Margin' (id: Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (id: Fill Holes)
        - method (menu='Angle Based') : ('Angle Based', 'Conformal')

        Returns
        -------
        - Vector
        """
        node = Node('UV Unwrap', {'Selection': selection, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes, 'Method': method})
        return node._out

    @classmethod
    def vertex_of_corner(cls, corner_index: Integer = None):
        """ > Node <&Node Vertex of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer
        """
        node = Node('Vertex of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def viewer(cls,
                    named_sockets: dict = {},
                    domain: Literal['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'AUTO',
                    ui_shortcut = 0,
                    **sockets):
        """ > Node <&Node Viewer>

        Arguments
        ---------
        - domain (str): parameter 'domain' in ['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']
        - ui_shortcut (int): parameter 'ui_shortcut'

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Viewer', 'domain', domain, 'viewer', ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Viewer', named_sockets, domain=domain, ui_shortcut=ui_shortcut, **sockets)
        return node._out

    @classmethod
    def viewport_transform(cls):
        """ > Node <&Node Viewport Transform>

        Returns
        -------
        - Matrix [view_ (Matrix), is_orthographic_ (Boolean)]
        """
        node = Node('Viewport Transform', )
        return node

    @classmethod
    def volume_cube(cls,
                    density: Float = None,
                    background: Float = None,
                    min: Vector = None,
                    max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None):
        """ > Node <&Node Volume Cube>

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - background (Float) : socket 'Background' (id: Background)
        - min (Vector) : socket 'Min' (id: Min)
        - max (Vector) : socket 'Max' (id: Max)
        - resolution_x (Integer) : socket 'Resolution X' (id: Resolution X)
        - resolution_y (Integer) : socket 'Resolution Y' (id: Resolution Y)
        - resolution_z (Integer) : socket 'Resolution Z' (id: Resolution Z)

        Returns
        -------
        - Volume
        """
        node = Node('Volume Cube', {'Density': density, 'Background': background, 'Min': min, 'Max': max, 'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})
        return node._out

    @classmethod
    def volume_to_mesh(cls,
                    volume: Volume = None,
                    resolution_mode: Literal['Grid', 'Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    threshold: Float = None,
                    adaptivity: Float = None):
        """ > Node <&Node Volume to Mesh>

        Arguments
        ---------
        - volume (Volume) : socket 'Volume' (id: Volume)
        - resolution_mode (menu='Grid') : ('Grid', 'Amount', 'Size')
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Volume to Mesh', {'Volume': volume, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Threshold': threshold, 'Adaptivity': adaptivity})
        return node._out

    @classmethod
    def warning(cls,
                    show: Boolean = None,
                    message: String = None,
                    warning_type: Literal['ERROR', 'WARNING', 'INFO'] = 'ERROR'):
        """ > Node <&Node Warning>

        Arguments
        ---------
        - show (Boolean) : socket 'Show' (id: Show)
        - message (String) : socket 'Message' (id: Message)
        - warning_type (str): parameter 'warning_type' in ['ERROR', 'WARNING', 'INFO']

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Warning', 'warning_type', warning_type, 'warning', ('ERROR', 'WARNING', 'INFO'))
        node = Node('Warning', {'Show': show, 'Message': message}, warning_type=warning_type)
        return node._out

    @property
    def closure_input(self):
        """ > Node <&Node Closure Input>

        Returns
        -------
        - None
        """
        node = Node('Closure Input', )
        return node._out

    @classmethod
    def closure_output(cls, active_input_index = 0, active_output_index = 0, define_signature = False):
        """ > Node <&Node Closure Output>

        Arguments
        ---------
        - active_input_index (int): parameter 'active_input_index'
        - active_output_index (int): parameter 'active_output_index'
        - define_signature (bool): parameter 'define_signature'

        Returns
        -------
        - Closure
        """
        node = Node('Closure Output', active_input_index=active_input_index, active_output_index=active_output_index, define_signature=define_signature)
        return node._out

    @classmethod
    def combine_bundle(cls, named_sockets: dict = {}, define_signature = False, **sockets):
        """ > Node <&Node Combine Bundle>

        Arguments
        ---------
        - define_signature (bool): parameter 'define_signature'

        Returns
        -------
        - Bundle
        """
        node = Node('Combine Bundle', named_sockets, define_signature=define_signature, **sockets)
        return node._out

    @classmethod
    def enable_output(cls,
                    enable: Boolean = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE'] = 'FLOAT'):
        """ > Node <&Node Enable Output>

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE']

        Returns
        -------
        - Float
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': value}, data_type=data_type)
        return node._out

    @classmethod
    def evaluate_closure(cls,
                    closure: Closure = None,
                    active_input_index = 0,
                    active_output_index = 0,
                    define_signature = False):
        """ > Node <&Node Evaluate Closure>

        Arguments
        ---------
        - closure (Closure) : socket 'Closure' (id: Closure)
        - active_input_index (int): parameter 'active_input_index'
        - active_output_index (int): parameter 'active_output_index'
        - define_signature (bool): parameter 'define_signature'

        Returns
        -------
        - None
        """
        node = Node('Evaluate Closure', {'Closure': closure}, active_input_index=active_input_index, active_output_index=active_output_index, define_signature=define_signature)
        return node._out

    @classmethod
    def frame(cls, label_size = 20, shrink = True, text = None):
        """ > Node <&Node Frame>

        Arguments
        ---------
        - label_size (int): parameter 'label_size'
        - shrink (bool): parameter 'shrink'
        - text (NoneType): parameter 'text'

        Returns
        -------
        - None
        """
        node = Node('Frame', label_size=label_size, shrink=shrink, text=text)
        return node._out

    @property
    def group_input(self):
        """ > Node <&Node Group Input>

        Returns
        -------
        - None
        """
        node = Node('Group Input', )
        return node._out

    @classmethod
    def group_output(cls, is_active_output = True):
        """ > Node <&Node Group Output>

        Arguments
        ---------
        - is_active_output (bool): parameter 'is_active_output'

        Returns
        -------
        - None
        """
        node = Node('Group Output', is_active_output=is_active_output)
        return node._out

    @classmethod
    def join_bundle(cls, *bundle: Bundle):
        """ > Node <&Node Join Bundle>

        Arguments
        ---------
        - bundle (Bundle) : socket 'Bundle' (id: Bundle)

        Returns
        -------
        - Bundle
        """
        node = Node('Join Bundle', {'Bundle': list(bundle)})
        return node._out

    @classmethod
    def reroute(cls, input: Color = None, socket_idname = 'NodeSocketColor'):
        """ > Node <&Node Reroute>

        Arguments
        ---------
        - input (Color) : socket 'Input' (id: Input)
        - socket_idname (str): parameter 'socket_idname'

        Returns
        -------
        - Color
        """
        node = Node('Reroute', {'Input': input}, socket_idname=socket_idname)
        return node._out

    @classmethod
    def separate_bundle(cls,
                    named_sockets: dict = {},
                    bundle: Bundle = None,
                    define_signature = False,
                    **sockets):
        """ > Node <&Node Separate Bundle>

        Arguments
        ---------
        - bundle (Bundle) : socket 'Bundle' (id: Bundle)
        - define_signature (bool): parameter 'define_signature'

        Returns
        -------
        - None
        """
        node = Node('Separate Bundle', {'Bundle': bundle, **named_sockets}, define_signature=define_signature, **sockets)
        return node

    @classmethod
    def blackbody(cls, temperature: Float = None):
        """ > Node <&Node Blackbody>

        Arguments
        ---------
        - temperature (Float) : socket 'Temperature' (id: Temperature)

        Returns
        -------
        - Color
        """
        node = Node('Blackbody', {'Temperature': temperature})
        return node._out

    @classmethod
    def clamp(cls,
                    value: Float = None,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX'):
        """ > Node <&Node Clamp>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - min (Float) : socket 'Min' (id: Min)
        - max (Float) : socket 'Max' (id: Max)
        - clamp_type (str): parameter 'clamp_type' in ['MINMAX', 'RANGE']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Clamp', 'clamp_type', clamp_type, 'clamp', ('MINMAX', 'RANGE'))
        node = Node('Clamp', {'Value': value, 'Min': min, 'Max': max}, clamp_type=clamp_type)
        return node._out

    @classmethod
    def combine_xyz(cls, x: Float = None, y: Float = None, z: Float = None):
        """ > Node <&Node Combine XYZ>

        Arguments
        ---------
        - x (Float) : socket 'X' (id: X)
        - y (Float) : socket 'Y' (id: Y)
        - z (Float) : socket 'Z' (id: Z)

        Returns
        -------
        - Vector
        """
        node = Node('Combine XYZ', {'X': x, 'Y': y, 'Z': z})
        return node._out

    @classmethod
    def float_curve(cls, value: Float = None, factor: Float = None):
        """ > Node <&Node Float Curve>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - factor (Float) : socket 'Factor' (id: Factor)

        Returns
        -------
        - Float
        """
        node = NodeCurves('Float Curve', {'Value': value, 'Factor': factor})
        return node._out

    @classmethod
    def gamma(cls, color: Color = None, gamma: Float = None):
        """ > Node <&Node Gamma>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - gamma (Float) : socket 'Gamma' (id: Gamma)

        Returns
        -------
        - Color
        """
        node = Node('Gamma', {'Color': color, 'Gamma': gamma})
        return node._out

    @classmethod
    def map_range(cls,
                    value: Float = None,
                    from_min: Float = None,
                    from_max: Float = None,
                    to_min: Float = None,
                    to_max: Float = None,
                    steps: Float = None,
                    vector: Vector = None,
                    from_min_1: Vector = None,
                    from_max_1: Vector = None,
                    to_min_1: Vector = None,
                    to_max_1: Vector = None,
                    steps_1: Vector = None,
                    clamp = True,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR'):
        """ > Node <&Node Map Range>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - from_min (Float) : socket 'From Min' (id: From Min)
        - from_max (Float) : socket 'From Max' (id: From Max)
        - to_min (Float) : socket 'To Min' (id: To Min)
        - to_max (Float) : socket 'To Max' (id: To Max)
        - steps (Float) : socket 'Steps' (id: Steps)
        - vector (Vector) : socket 'Vector' (id: Vector)
        - from_min_1 (Vector) : socket 'From Min' (id: From_Min_FLOAT3)
        - from_max_1 (Vector) : socket 'From Max' (id: From_Max_FLOAT3)
        - to_min_1 (Vector) : socket 'To Min' (id: To_Min_FLOAT3)
        - to_max_1 (Vector) : socket 'To Max' (id: To_Max_FLOAT3)
        - steps_1 (Vector) : socket 'Steps' (id: Steps_FLOAT3)
        - clamp (bool): parameter 'clamp'
        - data_type (str): parameter 'data_type' in ['FLOAT', 'FLOAT_VECTOR']
        - interpolation_type (str): parameter 'interpolation_type' in ['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Map Range', 'interpolation_type', interpolation_type, 'map_range', ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'))
        node = Node('Map Range', {'Value': value, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max, 'Steps': steps, 'Vector': vector, 'From_Min_FLOAT3': from_min_1, 'From_Max_FLOAT3': from_max_1, 'To_Min_FLOAT3': to_min_1, 'To_Max_FLOAT3': to_max_1, 'Steps_FLOAT3': steps_1}, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)
        return node._out

    @classmethod
    def math(cls,
                    value: Float = None,
                    value_1: Float = None,
                    value_2: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD',
                    use_clamp = False):
        """ > Node <&Node Math>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - value_1 (Float) : socket 'Value' (id: Value_001)
        - value_2 (Float) : socket 'Value' (id: Value_002)
        - operation (str): parameter 'operation' in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES']
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Math', 'operation', operation, 'math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'))
        node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': value_2}, operation=operation, use_clamp=use_clamp)
        return node._out

    @classmethod
    def mix(cls,
                    a: Float = None,
                    b: Float = None,
                    a_1: Vector = None,
                    b_1: Vector = None,
                    a_2: Color = None,
                    b_2: Color = None,
                    a_3: Rotation = None,
                    b_3: Rotation = None,
                    factor: Vector = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    clamp_factor = True,
                    clamp_result = False,
                    data_type: Literal['FLOAT', 'VECTOR', 'RGBA', 'ROTATION'] = 'FLOAT',
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM'):
        """ > Node <&Node Mix>

        Arguments
        ---------
        - a (Float) : socket 'A' (id: A_Float)
        - b (Float) : socket 'B' (id: B_Float)
        - a_1 (Vector) : socket 'A' (id: A_Vector)
        - b_1 (Vector) : socket 'B' (id: B_Vector)
        - a_2 (Color) : socket 'A' (id: A_Color)
        - b_2 (Color) : socket 'B' (id: B_Color)
        - a_3 (Rotation) : socket 'A' (id: A_Rotation)
        - b_3 (Rotation) : socket 'B' (id: B_Rotation)
        - factor (Vector) : socket 'Factor' (id: Factor_Vector)
        - blend_type (str): parameter 'blend_type' in ['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'
        - data_type (str): parameter 'data_type' in ['FLOAT', 'VECTOR', 'RGBA', 'ROTATION']
        - factor_mode (str): parameter 'factor_mode' in ['UNIFORM', 'NON_UNIFORM']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Mix', 'blend_type', blend_type, 'mix', ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'))
        utils.check_enum_arg('Mix', 'factor_mode', factor_mode, 'mix', ('UNIFORM', 'NON_UNIFORM'))
        node = Node('Mix', {'A_Float': a, 'B_Float': b, 'A_Vector': a_1, 'B_Vector': b_1, 'A_Color': a_2, 'B_Color': b_2, 'A_Rotation': a_3, 'B_Rotation': b_3, 'Factor_Vector': factor}, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type=data_type, factor_mode=factor_mode)
        return node._out

    @classmethod
    def rgb_curves(cls, color: Color = None, factor: Float = None):
        """ > Node <&Node RGB Curves>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - factor (Float) : socket 'Factor' (id: Fac)

        Returns
        -------
        - Color
        """
        node = NodeCurves('RGB Curves', {'Color': color, 'Fac': factor})
        return node._out

    @classmethod
    def radial_tiling(cls,
                    vector: Vector = None,
                    sides: Float = None,
                    roundness: Float = None,
                    normalize = False):
        """ > Node <&Node Radial Tiling>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - sides (Float) : socket 'Sides' (id: Sides)
        - roundness (Float) : socket 'Roundness' (id: Roundness)
        - normalize (bool): parameter 'normalize'

        Returns
        -------
        - Vector [segment_id_ (Float), segment_width_ (Float), segment_rotation_ (Float)]
        """
        node = Node('Radial Tiling', {'Vector': vector, 'Sides': sides, 'Roundness': roundness}, normalize=normalize)
        return node._out

    @classmethod
    def separate_xyz(cls, vector: Vector = None):
        """ > Node <&Node Separate XYZ>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)

        Returns
        -------
        - Float [y_ (Float), z_ (Float)]
        """
        node = Node('Separate XYZ', {'Vector': vector})
        return node

    @classmethod
    def brick_texture(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2):
        """ > Node <&Node Brick Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - mortar (Color) : socket 'Mortar' (id: Mortar)
        - scale (Float) : socket 'Scale' (id: Scale)
        - mortar_size (Float) : socket 'Mortar Size' (id: Mortar Size)
        - mortar_smooth (Float) : socket 'Mortar Smooth' (id: Mortar Smooth)
        - bias (Float) : socket 'Bias' (id: Bias)
        - brick_width (Float) : socket 'Brick Width' (id: Brick Width)
        - row_height (Float) : socket 'Row Height' (id: Row Height)
        - offset (float): parameter 'offset'
        - offset_frequency (int): parameter 'offset_frequency'
        - squash (float): parameter 'squash'
        - squash_frequency (int): parameter 'squash_frequency'

        Returns
        -------
        - Color [factor_ (Float)]
        """
        node = Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node._out

    @classmethod
    def checker_texture(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None):
        """ > Node <&Node Checker Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - scale (Float) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Color [factor_ (Float)]
        """
        node = Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return node._out

    @classmethod
    def gabor_texture(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    orientation_1: Vector = None,
                    gabor_type: Literal['2D', '3D'] = '2D'):
        """ > Node <&Node Gabor Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - frequency (Float) : socket 'Frequency' (id: Frequency)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - orientation (Float) : socket 'Orientation' (id: Orientation 2D)
        - orientation_1 (Vector) : socket 'Orientation' (id: Orientation 3D)
        - gabor_type (str): parameter 'gabor_type' in ['2D', '3D']

        Returns
        -------
        - Float [phase_ (Float), intensity_ (Float)]
        """
        utils.check_enum_arg('Gabor Texture', 'gabor_type', gabor_type, 'gabor_texture', ('2D', '3D'))
        node = Node('Gabor Texture', {'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation 2D': orientation, 'Orientation 3D': orientation_1}, gabor_type=gabor_type)
        return node._out

    @classmethod
    def gradient_texture(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR'):
        """ > Node <&Node Gradient Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - gradient_type (str): parameter 'gradient_type' in ['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']

        Returns
        -------
        - Color [factor_ (Float)]
        """
        utils.check_enum_arg('Gradient Texture', 'gradient_type', gradient_type, 'gradient_texture', ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'))
        node = Node('Gradient Texture', {'Vector': vector}, gradient_type=gradient_type)
        return node._out

    @classmethod
    def magic_texture(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2):
        """ > Node <&Node Magic Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - turbulence_depth (int): parameter 'turbulence_depth'

        Returns
        -------
        - Color [factor_ (Float)]
        """
        node = Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return node._out

    @classmethod
    def noise_texture(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    offset: Float = None,
                    gain: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True):
        """ > Node <&Node Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - w (Float) : socket 'W' (id: W)
        - scale (Float) : socket 'Scale' (id: Scale)
        - detail (Float) : socket 'Detail' (id: Detail)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (id: Lacunarity)
        - offset (Float) : socket 'Offset' (id: Offset)
        - gain (Float) : socket 'Gain' (id: Gain)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - noise_dimensions (str): parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']
        - noise_type (str): parameter 'noise_type' in ['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']
        - normalize (bool): parameter 'normalize'

        Returns
        -------
        - Float [color_ (Color)]
        """
        utils.check_enum_arg('Noise Texture', 'noise_dimensions', noise_dimensions, 'noise_texture', ('1D', '2D', '3D', '4D'))
        utils.check_enum_arg('Noise Texture', 'noise_type', noise_type, 'noise_texture', ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'))
        node = Node('Noise Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Offset': offset, 'Gain': gain, 'Distortion': distortion}, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize)
        return node._out

    @classmethod
    def voronoi_texture(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    smoothness: Float = None,
                    exponent: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&Node Voronoi Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - w (Float) : socket 'W' (id: W)
        - scale (Float) : socket 'Scale' (id: Scale)
        - detail (Float) : socket 'Detail' (id: Detail)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (id: Lacunarity)
        - smoothness (Float) : socket 'Smoothness' (id: Smoothness)
        - exponent (Float) : socket 'Exponent' (id: Exponent)
        - randomness (Float) : socket 'Randomness' (id: Randomness)
        - distance (str): parameter 'distance' in ['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']
        - feature (str): parameter 'feature' in ['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']
        - normalize (bool): parameter 'normalize'
        - voronoi_dimensions (str): parameter 'voronoi_dimensions' in ['1D', '2D', '3D', '4D']

        Returns
        -------
        - Float [color_ (Color), position_ (Vector)]
        """
        utils.check_enum_arg('Voronoi Texture', 'distance', distance, 'voronoi_texture', ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'))
        utils.check_enum_arg('Voronoi Texture', 'feature', feature, 'voronoi_texture', ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'))
        utils.check_enum_arg('Voronoi Texture', 'voronoi_dimensions', voronoi_dimensions, 'voronoi_texture', ('1D', '2D', '3D', '4D'))
        node = Node('Voronoi Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Smoothness': smoothness, 'Exponent': exponent, 'Randomness': randomness}, distance=distance, feature=feature, normalize=normalize, voronoi_dimensions=voronoi_dimensions)
        return node._out

    @classmethod
    def wave_texture(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS'):
        """ > Node <&Node Wave Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - detail (Float) : socket 'Detail' (id: Detail)
        - detail_scale (Float) : socket 'Detail Scale' (id: Detail Scale)
        - detail_roughness (Float) : socket 'Detail Roughness' (id: Detail Roughness)
        - phase_offset (Float) : socket 'Phase Offset' (id: Phase Offset)
        - bands_direction (str): parameter 'bands_direction' in ['X', 'Y', 'Z', 'DIAGONAL']
        - rings_direction (str): parameter 'rings_direction' in ['X', 'Y', 'Z', 'SPHERICAL']
        - wave_profile (str): parameter 'wave_profile' in ['SIN', 'SAW', 'TRI']
        - wave_type (str): parameter 'wave_type' in ['BANDS', 'RINGS']

        Returns
        -------
        - Color [factor_ (Float)]
        """
        utils.check_enum_arg('Wave Texture', 'bands_direction', bands_direction, 'wave_texture', ('X', 'Y', 'Z', 'DIAGONAL'))
        utils.check_enum_arg('Wave Texture', 'rings_direction', rings_direction, 'wave_texture', ('X', 'Y', 'Z', 'SPHERICAL'))
        utils.check_enum_arg('Wave Texture', 'wave_profile', wave_profile, 'wave_texture', ('SIN', 'SAW', 'TRI'))
        utils.check_enum_arg('Wave Texture', 'wave_type', wave_type, 'wave_texture', ('BANDS', 'RINGS'))
        node = Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node._out

    @classmethod
    def white_noise_texture(cls,
                    vector: Vector = None,
                    w: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&Node White Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - w (Float) : socket 'W' (id: W)
        - noise_dimensions (str): parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']

        Returns
        -------
        - Float [color_ (Color)]
        """
        utils.check_enum_arg('White Noise Texture', 'noise_dimensions', noise_dimensions, 'white_noise_texture', ('1D', '2D', '3D', '4D'))
        node = Node('White Noise Texture', {'Vector': vector, 'W': w}, noise_dimensions=noise_dimensions)
        return node._out

    @classmethod
    def color_ramp(cls, fac=None, stops=None, interpolation='LINEAR'):
        """ Node <&Node Color Ramp>

        Exposes utilities to manage the color ramp

        ``` python
        ramp1 = Float(.5).color_ramp(stops=[.1, .9])
        ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
        ```

        Arguments
        ---------
        - fac (Float = None)
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)
        - interpolation in ('EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT')
        """
        node = ColorRamp(fac=fac, stops=stops, interpolation=interpolation)
        return node._out

    @property
    def value(self):
        """ > Node <&Node Value>

        Returns
        -------
        - Float
        """
        node = Node('Value', )
        return node._out

    @classmethod
    def vector_curves(cls, vector: Vector = None, factor: Float = None):
        """ > Node <&Node Vector Curves>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - factor (Float) : socket 'Factor' (id: Fac)

        Returns
        -------
        - Vector
        """
        node = NodeCurves('Vector Curves', {'Vector': vector, 'Fac': factor})
        return node._out

    @classmethod
    def vector_math(cls,
                    vector: Vector = None,
                    vector_1: Vector = None,
                    vector_2: Vector = None,
                    scale: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD'):
        """ > Node <&Node Vector Math>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - vector_1 (Vector) : socket 'Vector' (id: Vector_001)
        - vector_2 (Vector) : socket 'Vector' (id: Vector_002)
        - scale (Float) : socket 'Scale' (id: Scale)
        - operation (str): parameter 'operation' in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Math', 'operation', operation, 'vector_math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'))
        node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1, 'Vector_002': vector_2, 'Scale': scale}, operation=operation)
        return node._out

    @classmethod
    def vector_rotate(cls,
                    vector: Vector = None,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    rotation: Vector = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE'):
        """ > Node <&Node Vector Rotate>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)
        - rotation (Vector) : socket 'Rotation' (id: Rotation)
        - invert (bool): parameter 'invert'
        - rotation_type (str): parameter 'rotation_type' in ['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Rotate', 'rotation_type', rotation_type, 'vector_rotate', ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'))
        node = Node('Vector Rotate', {'Vector': vector, 'Center': center, 'Axis': axis, 'Angle': angle, 'Rotation': rotation}, invert=invert, rotation_type=rotation_type)
        return node._out




# Create one single instance to access properties

nd = ND()

