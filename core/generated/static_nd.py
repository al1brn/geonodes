from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class nd:
    """" Static class

    Exposes all nodes as static methods:

    ``` python
    a = nd.math(1, 2, operation='ADD')
    ```
    """

    @classmethod
    def align_rotation_to_vector(cls, rotation=None, vector=None, factor=None, axis='Z', pivot_axis='AUTO'):
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
        node = Node('Align Rotation to Vector', sockets={'Rotation': rotation, 'Vector': vector, 'Factor': factor}, axis=axis, pivot_axis=pivot_axis)
        return node._out

    @classmethod
    def axes_to_rotation(cls, primary_axis_1=None, secondary_axis_1=None, primary_axis='Z', secondary_axis='X'):
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
        node = Node('Axes to Rotation', sockets={'Primary Axis': primary_axis_1, 'Secondary Axis': secondary_axis_1}, primary_axis=primary_axis, secondary_axis=secondary_axis)
        return node._out

    @classmethod
    def axis_angle_to_rotation(cls, axis=None, angle=None):
        """ > Node <&Node Axis Angle to Rotation>

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)

        Returns
        -------
        - Rotation
        """
        node = Node('Axis Angle to Rotation', sockets={'Axis': axis, 'Angle': angle})
        return node._out

    @classmethod
    def boolean_math(cls, boolean=None, boolean_1=None, operation='AND'):
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
        node = Node('Boolean Math', sockets={'Boolean': boolean, 'Boolean_001': boolean_1}, operation=operation)
        return node._out

    @classmethod
    def combine_color(cls, red=None, green=None, blue=None, alpha=None, mode='RGB'):
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
        node = Node('Combine Color', sockets={'Red': red, 'Green': green, 'Blue': blue, 'Alpha': alpha}, mode=mode)
        return node._out

    @classmethod
    def combine_matrix(cls, column_1_row_1=None, column_1_row_2=None, column_1_row_3=None, column_1_row_4=None, column_2_row_1=None, column_2_row_2=None, column_2_row_3=None, column_2_row_4=None, column_3_row_1=None, column_3_row_2=None, column_3_row_3=None, column_3_row_4=None, column_4_row_1=None, column_4_row_2=None, column_4_row_3=None, column_4_row_4=None):
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
        node = Node('Combine Matrix', sockets={'Column 1 Row 1': column_1_row_1, 'Column 1 Row 2': column_1_row_2, 'Column 1 Row 3': column_1_row_3, 'Column 1 Row 4': column_1_row_4, 'Column 2 Row 1': column_2_row_1, 'Column 2 Row 2': column_2_row_2, 'Column 2 Row 3': column_2_row_3, 'Column 2 Row 4': column_2_row_4, 'Column 3 Row 1': column_3_row_1, 'Column 3 Row 2': column_3_row_2, 'Column 3 Row 3': column_3_row_3, 'Column 3 Row 4': column_3_row_4, 'Column 4 Row 1': column_4_row_1, 'Column 4 Row 2': column_4_row_2, 'Column 4 Row 3': column_4_row_3, 'Column 4 Row 4': column_4_row_4})
        return node._out

    @classmethod
    def combine_transform(cls, translation=None, rotation=None, scale=None):
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
        node = Node('Combine Transform', sockets={'Translation': translation, 'Rotation': rotation, 'Scale': scale})
        return node._out

    @classmethod
    def compare(cls, a=None, b=None, a_1=None, b_1=None, a_2=None, b_2=None, a_3=None, b_3=None, a_4=None, b_4=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):
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
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA']
        - mode (str): parameter 'mode' in ['ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION']
        - operation (str): parameter 'operation' in ['LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL']

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Compare', 'data_type', data_type, 'compare', ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA'))
        utils.check_enum_arg('Compare', 'mode', mode, 'compare', ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION'))
        utils.check_enum_arg('Compare', 'operation', operation, 'compare', ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL'))
        node = Node('Compare', sockets={'A': a, 'B': b, 'A_INT': a_1, 'B_INT': b_1, 'A_VEC3': a_2, 'B_VEC3': b_2, 'A_COL': a_3, 'B_COL': b_3, 'A_STR': a_4, 'B_STR': b_4, 'C': c, 'Angle': angle, 'Epsilon': epsilon}, data_type=data_type, mode=mode, operation=operation)
        return node._out

    @classmethod
    def euler_to_rotation(cls, euler=None):
        """ > Node <&Node Euler to Rotation>

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (id: Euler)

        Returns
        -------
        - Rotation
        """
        node = Node('Euler to Rotation', sockets={'Euler': euler})
        return node._out

    @classmethod
    def float_to_integer(cls, float=None, rounding_mode='ROUND'):
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
        node = Node('Float to Integer', sockets={'Float': float}, rounding_mode=rounding_mode)
        return node._out

    @classmethod
    def hash_value(cls, value=None, seed=None, data_type='INT'):
        """ > Node <&Node Hash Value>

        Arguments
        ---------
        - value (Integer) : socket 'Value' (id: Value)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA']

        Returns
        -------
        - Integer
        """
        utils.check_enum_arg('Hash Value', 'data_type', data_type, 'hash_value', ('FLOAT', 'INT', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA'))
        node = Node('Hash Value', sockets={'Value': value, 'Seed': seed}, data_type=data_type)
        return node._out

    @classmethod
    def boolean(cls, boolean=False):
        """ > Node <&Node Boolean>

        Arguments
        ---------
        - boolean (bool): parameter 'boolean'

        Returns
        -------
        - Boolean
        """
        node = Node('Boolean', sockets={}, boolean=boolean)
        return node._out

    @classmethod
    @property
    def color(cls):
        """ > Node <&Node Color>

        Returns
        -------
        - Color
        """
        node = Node('Color', sockets={})
        return node._out

    @classmethod
    def integer(cls, integer=0):
        """ > Node <&Node Integer>

        Arguments
        ---------
        - integer (int): parameter 'integer'

        Returns
        -------
        - Integer
        """
        node = Node('Integer', sockets={}, integer=integer)
        return node._out

    @classmethod
    @property
    def rotation(cls):
        """ > Node <&Node Rotation>

        Returns
        -------
        - Rotation
        """
        node = Node('Rotation', sockets={})
        return node._out

    @classmethod
    def special_characters(cls):
        """ > Node <&Node Special Characters>

        Returns
        -------
        - String [tab_ (String)]
        """
        node = Node('Special Characters', sockets={})
        return node

    @classmethod
    def string(cls, string=''):
        """ > Node <&Node String>

        Arguments
        ---------
        - string (str): parameter 'string'

        Returns
        -------
        - String
        """
        node = Node('String', sockets={}, string=string)
        return node._out

    @classmethod
    @property
    def vector(cls):
        """ > Node <&Node Vector>

        Returns
        -------
        - Vector
        """
        node = Node('Vector', sockets={})
        return node._out

    @classmethod
    def integer_math(cls, value=None, value_1=None, value_2=None, operation='ADD'):
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
        node = Node('Integer Math', sockets={'Value': value, 'Value_001': value_1, 'Value_002': value_2}, operation=operation)
        return node._out

    @classmethod
    def invert_matrix(cls, matrix=None):
        """ > Node <&Node Invert Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Matrix [invertible_ (Boolean)]
        """
        node = Node('Invert Matrix', sockets={'Matrix': matrix})
        return node._out

    @classmethod
    def invert_rotation(cls, rotation=None):
        """ > Node <&Node Invert Rotation>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Rotation
        """
        node = Node('Invert Rotation', sockets={'Rotation': rotation})
        return node._out

    @classmethod
    def matrix_determinant(cls, matrix=None):
        """ > Node <&Node Matrix Determinant>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Float
        """
        node = Node('Matrix Determinant', sockets={'Matrix': matrix})
        return node._out

    @classmethod
    def multiply_matrices(cls, matrix=None, matrix_1=None):
        """ > Node <&Node Multiply Matrices>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)
        - matrix_1 (Matrix) : socket 'Matrix' (id: Matrix_001)

        Returns
        -------
        - Matrix
        """
        node = Node('Multiply Matrices', sockets={'Matrix': matrix, 'Matrix_001': matrix_1})
        return node._out

    @classmethod
    def project_point(cls, vector=None, transform=None):
        """ > Node <&Node Project Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector
        """
        node = Node('Project Point', sockets={'Vector': vector, 'Transform': transform})
        return node._out

    @classmethod
    def quaternion_to_rotation(cls, w=None, x=None, y=None, z=None):
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
        node = Node('Quaternion to Rotation', sockets={'W': w, 'X': x, 'Y': y, 'Z': z})
        return node._out

    @classmethod
    def random_value(cls, min=None, max=None, min_1=None, max_1=None, min_2=None, max_2=None, probability=None, id=None, seed=None, data_type='FLOAT'):
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
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Random Value', 'data_type', data_type, 'random_value', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN'))
        node = Node('Random Value', sockets={'Min': min, 'Max': max, 'Min_001': min_1, 'Max_001': max_1, 'Min_002': min_2, 'Max_002': max_2, 'Probability': probability, 'ID': id, 'Seed': seed}, data_type=data_type)
        return node._out

    @classmethod
    def replace_string(cls, string=None, find=None, replace=None):
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
        node = Node('Replace String', sockets={'String': string, 'Find': find, 'Replace': replace})
        return node._out

    @classmethod
    def rotate_rotation(cls, rotation=None, rotate_by=None, rotation_space='GLOBAL'):
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
        node = Node('Rotate Rotation', sockets={'Rotation': rotation, 'Rotate By': rotate_by}, rotation_space=rotation_space)
        return node._out

    @classmethod
    def rotate_vector(cls, vector=None, rotation=None):
        """ > Node <&Node Rotate Vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Vector
        """
        node = Node('Rotate Vector', sockets={'Vector': vector, 'Rotation': rotation})
        return node._out

    @classmethod
    def rotation_to_axis_angle(cls, rotation=None):
        """ > Node <&Node Rotation to Axis Angle>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Vector [angle_ (Float)]
        """
        node = Node('Rotation to Axis Angle', sockets={'Rotation': rotation})
        return node._out

    @classmethod
    def rotation_to_euler(cls, rotation=None):
        """ > Node <&Node Rotation to Euler>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Vector
        """
        node = Node('Rotation to Euler', sockets={'Rotation': rotation})
        return node._out

    @classmethod
    def rotation_to_quaternion(cls, rotation=None):
        """ > Node <&Node Rotation to Quaternion>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)

        Returns
        -------
        - Float [x_ (Float), y_ (Float), z_ (Float)]
        """
        node = Node('Rotation to Quaternion', sockets={'Rotation': rotation})
        return node._out

    @classmethod
    def separate_color(cls, color=None, mode='RGB'):
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
        node = Node('Separate Color', sockets={'Color': color}, mode=mode)
        return node._out

    @classmethod
    def separate_matrix(cls, matrix=None):
        """ > Node <&Node Separate Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Float [column_1_row_2_ (Float), column_1_row_3_ (Float), column_1_row_4_ (Float), column_2_row_1_ (Float), column_2_row_2_ (Float), column_2_row_3_ (Float), column_2_row_4_ (Float), column_3_row_1_ (Float), column_3_row_2_ (Float), column_3_row_3_ (Float), column_3_row_4_ (Float), column_4_row_1_ (Float), column_4_row_2_ (Float), column_4_row_3_ (Float), column_4_row_4_ (Float)]
        """
        node = Node('Separate Matrix', sockets={'Matrix': matrix})
        return node._out

    @classmethod
    def separate_transform(cls, transform=None):
        """ > Node <&Node Separate Transform>

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector [rotation_ (Rotation), scale_ (Vector)]
        """
        node = Node('Separate Transform', sockets={'Transform': transform})
        return node._out

    @classmethod
    def slice_string(cls, string=None, position=None, length=None):
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
        node = Node('Slice String', sockets={'String': string, 'Position': position, 'Length': length})
        return node._out

    @classmethod
    def string_length(cls, string=None):
        """ > Node <&Node String Length>

        Arguments
        ---------
        - string (String) : socket 'String' (id: String)

        Returns
        -------
        - Integer
        """
        node = Node('String Length', sockets={'String': string})
        return node._out

    @classmethod
    def transform_direction(cls, direction=None, transform=None):
        """ > Node <&Node Transform Direction>

        Arguments
        ---------
        - direction (Vector) : socket 'Direction' (id: Direction)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector
        """
        node = Node('Transform Direction', sockets={'Direction': direction, 'Transform': transform})
        return node._out

    @classmethod
    def transform_point(cls, vector=None, transform=None):
        """ > Node <&Node Transform Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Vector
        """
        node = Node('Transform Point', sockets={'Vector': vector, 'Transform': transform})
        return node._out

    @classmethod
    def transpose_matrix(cls, matrix=None):
        """ > Node <&Node Transpose Matrix>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (id: Matrix)

        Returns
        -------
        - Matrix
        """
        node = Node('Transpose Matrix', sockets={'Matrix': matrix})
        return node._out

    @classmethod
    def value_to_string(cls, value=None, decimals=None, data_type='FLOAT'):
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
        utils.check_enum_arg('Value to String', 'data_type', data_type, 'value_to_string', ('FLOAT', 'INT'))
        node = Node('Value to String', sockets={'Value': value, 'Decimals': decimals}, data_type=data_type)
        return node._out

    @classmethod
    def accumulate_field(cls, value=None, group_id=None, data_type='FLOAT', domain='POINT'):
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
        utils.check_enum_arg('Accumulate Field', 'data_type', data_type, 'accumulate_field', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'))
        utils.check_enum_arg('Accumulate Field', 'domain', domain, 'accumulate_field', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Accumulate Field', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def domain_size(cls, geometry=None, component='MESH'):
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
        node = Node('Domain Size', sockets={'Geometry': geometry}, component=component)
        return node._out

    @classmethod
    def attribute_statistic(cls, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT'):
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
        utils.check_enum_arg('Attribute Statistic', 'data_type', data_type, 'attribute_statistic', ('FLOAT', 'FLOAT_VECTOR'))
        utils.check_enum_arg('Attribute Statistic', 'domain', domain, 'attribute_statistic', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Attribute Statistic', sockets={'Geometry': geometry, 'Selection': selection, 'Attribute': attribute}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def bake(cls, geometry=None):
        """ > Node <&Node Bake>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Item_0)

        Returns
        -------
        - Geometry
        """
        node = Node('Bake', sockets={'Item_0': geometry})
        return node._out

    @classmethod
    def blur_attribute(cls, value=None, iterations=None, weight=None, data_type='FLOAT'):
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
        utils.check_enum_arg('Blur Attribute', 'data_type', data_type, 'blur_attribute', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR'))
        node = Node('Blur Attribute', sockets={'Value': value, 'Iterations': iterations, 'Weight': weight}, data_type=data_type)
        return node._out

    @classmethod
    def bounding_box(cls, geometry=None):
        """ > Node <&Node Bounding Box>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Mesh [min_ (Vector), max_ (Vector)]
        """
        node = Node('Bounding Box', sockets={'Geometry': geometry})
        return node._out

    @classmethod
    def capture_attribute(cls, geometry=None, domain='POINT'):
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
        node = Node('Capture Attribute', sockets={'Geometry': geometry}, domain=domain)
        return node._out

    @classmethod
    def collection_info(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
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
        node = Node('Collection Info', sockets={'Collection': collection, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out

    @classmethod
    def convex_hull(cls, geometry=None):
        """ > Node <&Node Convex Hull>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Mesh
        """
        node = Node('Convex Hull', sockets={'Geometry': geometry})
        return node._out

    @classmethod
    def corners_of_edge(cls, edge_index=None, weights=None, sort_index=None):
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
        node = Node('Corners of Edge', sockets={'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_face(cls, face_index=None, weights=None, sort_index=None):
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
        node = Node('Corners of Face', sockets={'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corners_of_vertex(cls, vertex_index=None, weights=None, sort_index=None):
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
        node = Node('Corners of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def arc(cls, resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS'):
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
        node = Node('Arc', sockets={'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Offset Angle': offset_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode=mode)
        return node._out

    @classmethod
    def endpoint_selection(cls, start_size=None, end_size=None):
        """ > Node <&Node Endpoint Selection>

        Arguments
        ---------
        - start_size (Integer) : socket 'Start Size' (id: Start Size)
        - end_size (Integer) : socket 'End Size' (id: End Size)

        Returns
        -------
        - Boolean
        """
        node = Node('Endpoint Selection', sockets={'Start Size': start_size, 'End Size': end_size})
        return node._out

    @classmethod
    def handle_type_selection(cls, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
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
        node = Node('Handle Type Selection', sockets={}, handle_type=handle_type, mode=mode)
        return node._out

    @classmethod
    def curve_length(cls, curve=None):
        """ > Node <&Node Curve Length>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)

        Returns
        -------
        - Float
        """
        node = Node('Curve Length', sockets={'Curve': curve})
        return node._out

    @classmethod
    def curve_of_point(cls, point_index=None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - Integer [index_in_curve_ (Integer)]
        """
        node = Node('Curve of Point', sockets={'Point Index': point_index})
        return node._out

    @classmethod
    def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
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
        node = Node('Bézier Segment', sockets={'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode=mode)
        return node._out

    @classmethod
    def curve_circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):
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
        node = Node('Curve Circle', sockets={'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Radius': radius}, mode=mode)
        return node._out

    @classmethod
    def curve_line(cls, start=None, end=None, direction=None, length=None, mode='POINTS'):
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
        node = Node('Curve Line', sockets={'Start': start, 'End': end, 'Direction': direction, 'Length': length}, mode=mode)
        return node._out

    @classmethod
    def quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
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
        node = Node('Quadrilateral', sockets={'Width': width, 'Height': height, 'Bottom Width': bottom_width, 'Top Width': top_width, 'Offset': offset, 'Bottom Height': bottom_height, 'Top Height': top_height, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Point 4': point_4}, mode=mode)
        return node._out

    @classmethod
    def quadratic_bezier(cls, resolution=None, start=None, middle=None, end=None):
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
        node = Node('Quadratic Bézier', sockets={'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end})
        return node._out

    @classmethod
    def set_handle_type(cls, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ > Node <&Node Set Handle Type>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
        - mode (set): parameter 'mode'

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': curve, 'Selection': selection}, handle_type=handle_type, mode=mode)
        return node._out

    @classmethod
    def spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
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
        node = Node('Spiral', sockets={'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius, 'End Radius': end_radius, 'Height': height, 'Reverse': reverse})
        return node._out

    @classmethod
    def set_spline_type(cls, curve=None, selection=None, spline_type='POLY'):
        """ > Node <&Node Set Spline Type>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - spline_type (str): parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'set_spline_type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', sockets={'Curve': curve, 'Selection': selection}, spline_type=spline_type)
        return node._out

    @classmethod
    def star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
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
        node = Node('Star', sockets={'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})
        return node._out

    @classmethod
    def curve_to_mesh(cls, curve=None, profile_curve=None, fill_caps=None):
        """ > Node <&Node Curve to Mesh>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - profile_curve (Geometry) : socket 'Profile Curve' (id: Profile Curve)
        - fill_caps (Boolean) : socket 'Fill Caps' (id: Fill Caps)

        Returns
        -------
        - Mesh
        """
        node = Node('Curve to Mesh', sockets={'Curve': curve, 'Profile Curve': profile_curve, 'Fill Caps': fill_caps})
        return node._out

    @classmethod
    def curve_to_points(cls, curve=None, count=None, length=None, mode='COUNT'):
        """ > Node <&Node Curve to Points>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - count (Integer) : socket 'Count' (id: Count)
        - length (Float) : socket 'Length' (id: Length)
        - mode (str): parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        utils.check_enum_arg('Curve to Points', 'mode', mode, 'curve_to_points', ('EVALUATED', 'COUNT', 'LENGTH'))
        node = Node('Curve to Points', sockets={'Curve': curve, 'Count': count, 'Length': length}, mode=mode)
        return node._out

    @classmethod
    def curves_to_grease_pencil(cls, curves=None, selection=None, instances_as_layers=None):
        """ > Node <&Node Curves to Grease Pencil>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (id: Curves)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - instances_as_layers (Boolean) : socket 'Instances as Layers' (id: Instances as Layers)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Curves to Grease Pencil', sockets={'Curves': curves, 'Selection': selection, 'Instances as Layers': instances_as_layers})
        return node._out

    @classmethod
    def deform_curves_on_surface(cls, curves=None):
        """ > Node <&Node Deform Curves on Surface>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (id: Curves)

        Returns
        -------
        - Curve
        """
        node = Node('Deform Curves on Surface', sockets={'Curves': curves})
        return node._out

    @classmethod
    def delete_geometry(cls, geometry=None, selection=None, domain='POINT', mode='ALL'):
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
        node = Node('Delete Geometry', sockets={'Geometry': geometry, 'Selection': selection}, domain=domain, mode=mode)
        return node._out

    @classmethod
    def distribute_points_in_grid(cls, grid=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):
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
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Density': density, 'Seed': seed, 'Spacing': spacing, 'Threshold': threshold}, mode=mode)
        return node._out

    @classmethod
    def distribute_points_in_volume(cls, volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Volume>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (id: Volume)
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - mode (str): parameter 'mode' in ['DENSITY_RANDOM', 'DENSITY_GRID']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Distribute Points in Volume', 'mode', mode, 'distribute_points_in_volume', ('DENSITY_RANDOM', 'DENSITY_GRID'))
        node = Node('Distribute Points in Volume', sockets={'Volume': volume, 'Density': density, 'Seed': seed, 'Spacing': spacing, 'Threshold': threshold}, mode=mode)
        return node._out

    @classmethod
    def distribute_points_on_faces(cls, mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', use_legacy_normal=False):
        """ > Node <&Node Distribute Points on Faces>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - distance_min (Float) : socket 'Distance Min' (id: Distance Min)
        - density_max (Float) : socket 'Density Max' (id: Density Max)
        - density (Float) : socket 'Density' (id: Density)
        - density_factor (Float) : socket 'Density Factor' (id: Density Factor)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - distribute_method (str): parameter 'distribute_method' in ['RANDOM', 'POISSON']
        - use_legacy_normal (bool): parameter 'use_legacy_normal'

        Returns
        -------
        - Cloud [normal_ (Vector), rotation_ (Rotation)]
        """
        utils.check_enum_arg('Distribute Points on Faces', 'distribute_method', distribute_method, 'distribute_points_on_faces', ('RANDOM', 'POISSON'))
        node = Node('Distribute Points on Faces', sockets={'Mesh': mesh, 'Selection': selection, 'Distance Min': distance_min, 'Density Max': density_max, 'Density': density, 'Density Factor': density_factor, 'Seed': seed}, distribute_method=distribute_method, use_legacy_normal=use_legacy_normal)
        return node._out

    @classmethod
    def dual_mesh(cls, mesh=None, keep_boundaries=None):
        """ > Node <&Node Dual Mesh>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - keep_boundaries (Boolean) : socket 'Keep Boundaries' (id: Keep Boundaries)

        Returns
        -------
        - Mesh
        """
        node = Node('Dual Mesh', sockets={'Mesh': mesh, 'Keep Boundaries': keep_boundaries})
        return node._out

    @classmethod
    def duplicate_elements(cls, geometry=None, selection=None, amount=None, domain='POINT'):
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
        node = Node('Duplicate Elements', sockets={'Geometry': geometry, 'Selection': selection, 'Amount': amount}, domain=domain)
        return node._out

    @classmethod
    def edge_paths_to_curves(cls, mesh=None, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Curves>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Curve
        """
        node = Node('Edge Paths to Curves', sockets={'Mesh': mesh, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edge_paths_to_selection(cls, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Selection>

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Boolean
        """
        node = Node('Edge Paths to Selection', sockets={'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def edges_of_corner(cls, corner_index=None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [previous_edge_index_ (Integer)]
        """
        node = Node('Edges of Corner', sockets={'Corner Index': corner_index})
        return node._out

    @classmethod
    def edges_of_vertex(cls, vertex_index=None, weights=None, sort_index=None):
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
        node = Node('Edges of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def edges_to_face_groups(cls, boundary_edges=None):
        """ > Node <&Node Edges to Face Groups>

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (id: Boundary Edges)

        Returns
        -------
        - Integer
        """
        node = Node('Edges to Face Groups', sockets={'Boundary Edges': boundary_edges})
        return node._out

    @classmethod
    def extrude_mesh(cls, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """ > Node <&Node Extrude Mesh>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
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
        node = Node('Extrude Mesh', sockets={'Mesh': mesh, 'Selection': selection, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode=mode)
        return node._out

    @classmethod
    def face_of_corner(cls, corner_index=None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [index_in_face_ (Integer)]
        """
        node = Node('Face of Corner', sockets={'Corner Index': corner_index})
        return node._out

    @classmethod
    def evaluate_at_index(cls, index=None, value=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Evaluate at Index>

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Evaluate at Index', 'data_type', data_type, 'evaluate_at_index', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Evaluate at Index', 'domain', domain, 'evaluate_at_index', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Evaluate at Index', sockets={'Index': index, 'Value': value}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def evaluate_on_domain(cls, value=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Evaluate on Domain>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Evaluate on Domain', 'data_type', data_type, 'evaluate_on_domain', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Evaluate on Domain', 'domain', domain, 'evaluate_on_domain', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Evaluate on Domain', sockets={'Value': value}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def fill_curve(cls, curve=None, group_id=None, mode='TRIANGLES'):
        """ > Node <&Node Fill Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - mode (str): parameter 'mode' in ['TRIANGLES', 'NGONS']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Fill Curve', 'mode', mode, 'fill_curve', ('TRIANGLES', 'NGONS'))
        node = Node('Fill Curve', sockets={'Curve': curve, 'Group ID': group_id}, mode=mode)
        return node._out

    @classmethod
    def fillet_curve(cls, curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """ > Node <&Node Fillet Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - count (Integer) : socket 'Count' (id: Count)
        - radius (Float) : socket 'Radius' (id: Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (id: Limit Radius)
        - mode (str): parameter 'mode' in ['BEZIER', 'POLY']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Fillet Curve', 'mode', mode, 'fillet_curve', ('BEZIER', 'POLY'))
        node = Node('Fillet Curve', sockets={'Curve': curve, 'Count': count, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)
        return node._out

    @classmethod
    def flip_faces(cls, mesh=None, selection=None):
        """ > Node <&Node Flip Faces>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Mesh
        """
        node = Node('Flip Faces', sockets={'Mesh': mesh, 'Selection': selection})
        return node._out

    @classmethod
    def for_each_geometry_element_input(cls, geometry=None, selection=None):
        """ > Node <&Node For Each Geometry Element Input>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Integer
        """
        node = Node('For Each Geometry Element Input', sockets={'Geometry': geometry, 'Selection': selection})
        return node._out

    @classmethod
    def for_each_geometry_element_output(cls, geometry=None, active_generation_index=0, active_input_index=0, active_main_index=0, domain='POINT', inspection_index=0):
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
        node = Node('For Each Geometry Element Output', sockets={'Generation_0': geometry}, active_generation_index=active_generation_index, active_input_index=active_input_index, active_main_index=active_main_index, domain=domain, inspection_index=inspection_index)
        return node._out

    @classmethod
    def geometry_to_instance(cls, *geometry):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Instances
        """
        node = Node('Geometry to Instance', sockets={'Geometry': list(geometry)})
        return node._out

    @classmethod
    def get_named_grid(cls, volume=None, name=None, remove=None, data_type='FLOAT'):
        """ > Node <&Node Get Named Grid>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (id: Volume)
        - name (String) : socket 'Name' (id: Name)
        - remove (Boolean) : socket 'Remove' (id: Remove)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'VECTOR']

        Returns
        -------
        - Volume [grid_ (Float)]
        """
        utils.check_enum_arg('Get Named Grid', 'data_type', data_type, 'get_named_grid', ('FLOAT', 'VECTOR'))
        node = Node('Get Named Grid', sockets={'Volume': volume, 'Name': name, 'Remove': remove}, data_type=data_type)
        return node._out

    @classmethod
    def dial_gizmo(cls, *value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY'):
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
        node = Node('Dial Gizmo', sockets={'Value': list(value), 'Position': position, 'Up': up, 'Screen Space': screen_space, 'Radius': radius}, color_id=color_id)
        return node._out

    @classmethod
    def linear_gizmo(cls, *value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW'):
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
        node = Node('Linear Gizmo', sockets={'Value': list(value), 'Position': position, 'Direction': direction}, color_id=color_id, draw_style=draw_style)
        return node._out

    @classmethod
    def transform_gizmo(cls, *value, position=None, rotation=None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True):
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
        node = Node('Transform Gizmo', sockets={'Value': list(value), 'Position': position, 'Rotation': rotation}, use_rotation_x=use_rotation_x, use_rotation_y=use_rotation_y, use_rotation_z=use_rotation_z, use_scale_x=use_scale_x, use_scale_y=use_scale_y, use_scale_z=use_scale_z, use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)
        return node._out

    @classmethod
    def grease_pencil_to_curves(cls, grease_pencil=None, selection=None, layers_as_instances=None):
        """ > Node <&Node Grease Pencil to Curves>

        Arguments
        ---------
        - grease_pencil (Geometry) : socket 'Grease Pencil' (id: Grease Pencil)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - layers_as_instances (Boolean) : socket 'Layers as Instances' (id: Layers as Instances)

        Returns
        -------
        - Curve
        """
        node = Node('Grease Pencil to Curves', sockets={'Grease Pencil': grease_pencil, 'Selection': selection, 'Layers as Instances': layers_as_instances})
        return node._out

    @classmethod
    def grid_to_mesh(cls, grid=None, threshold=None, adaptivity=None):
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
        node = Node('Grid to Mesh', sockets={'Grid': grid, 'Threshold': threshold, 'Adaptivity': adaptivity})
        return node._out

    @classmethod
    def group(cls, node_tree=None):
        """ > Node <&Node Group>

        Arguments
        ---------
        - node_tree (NoneType): parameter 'node_tree'

        Returns
        -------
        - None
        """
        node = Node('Group', sockets={}, node_tree=node_tree)
        return node._out

    @classmethod
    def image_info(cls, image=None, frame=None):
        """ > Node <&Node Image Info>

        Arguments
        ---------
        - image (Image) : socket 'Image' (id: Image)
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - Integer [height_ (Integer), has_alpha_ (Boolean), frame_count_ (Integer), fps_ (Float)]
        """
        node = Node('Image Info', sockets={'Image': image, 'Frame': frame})
        return node._out

    @classmethod
    def image_texture(cls, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
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
        node = Node('Image Texture', sockets={'Image': image, 'Vector': vector, 'Frame': frame}, extension=extension, interpolation=interpolation)
        return node._out

    @classmethod
    def import_obj(cls, path=None):
        """ > Node <&Node Import OBJ>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Instances
        """
        node = Node('Import OBJ', sockets={'Path': path})
        return node._out

    @classmethod
    def import_ply(cls, path=None):
        """ > Node <&Node Import PLY>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import PLY', sockets={'Path': path})
        return node._out

    @classmethod
    def import_stl(cls, path=None):
        """ > Node <&Node Import STL>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import STL', sockets={'Path': path})
        return node._out

    @classmethod
    def index_of_nearest(cls, position=None, group_id=None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Integer [has_neighbor_ (Boolean)]
        """
        node = Node('Index of Nearest', sockets={'Position': position, 'Group ID': group_id})
        return node._out

    @classmethod
    def index_switch(cls, index=None, _0=None, _1=None, data_type='GEOMETRY'):
        """ > Node <&Node Index Switch>

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - _0 (Geometry) : socket '0' (id: Item_0)
        - _1 (Geometry) : socket '1' (id: Item_1)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Index Switch', 'data_type', data_type, 'index_switch', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL'))
        node = Node('Index Switch', sockets={'Index': index, 'Item_0': _0, 'Item_1': _1}, data_type=data_type)
        return node._out

    @classmethod
    @property
    def active_camera(cls):
        """ > Node <&Node Active Camera>

        Returns
        -------
        - Object
        """
        node = Node('Active Camera', sockets={})
        return node._out

    @classmethod
    def curve_handle_positions(cls, relative=None):
        """ > Node <&Node Curve Handle Positions>

        Arguments
        ---------
        - relative (Boolean) : socket 'Relative' (id: Relative)

        Returns
        -------
        - Vector [right_ (Vector)]
        """
        node = Node('Curve Handle Positions', sockets={'Relative': relative})
        return node._out

    @classmethod
    @property
    def curve_tilt(cls):
        """ > Node <&Node Curve Tilt>

        Returns
        -------
        - Float
        """
        node = Node('Curve Tilt', sockets={})
        return node._out

    @classmethod
    @property
    def is_edge_smooth(cls):
        """ > Node <&Node Is Edge Smooth>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Edge Smooth', sockets={})
        return node._out

    @classmethod
    @property
    def id(cls):
        """ > Node <&Node ID>

        Returns
        -------
        - Integer
        """
        node = Node('ID', sockets={})
        return node._out

    @classmethod
    def image(cls, image=None):
        """ > Node <&Node Image>

        Arguments
        ---------
        - image (NoneType): parameter 'image'

        Returns
        -------
        - Image
        """
        node = Node('Image', sockets={}, image=image)
        return node._out

    @classmethod
    @property
    def index(cls):
        """ > Node <&Node Index>

        Returns
        -------
        - Integer
        """
        node = Node('Index', sockets={})
        return node._out

    @classmethod
    @property
    def instance_rotation(cls):
        """ > Node <&Node Instance Rotation>

        Returns
        -------
        - Rotation
        """
        node = Node('Instance Rotation', sockets={})
        return node._out

    @classmethod
    @property
    def instance_scale(cls):
        """ > Node <&Node Instance Scale>

        Returns
        -------
        - Vector
        """
        node = Node('Instance Scale', sockets={})
        return node._out

    @classmethod
    def material(cls, material=None):
        """ > Node <&Node Material>

        Arguments
        ---------
        - material (NoneType): parameter 'material'

        Returns
        -------
        - Material
        """
        node = Node('Material', sockets={}, material=material)
        return node._out

    @classmethod
    @property
    def material_index(cls):
        """ > Node <&Node Material Index>

        Returns
        -------
        - Integer
        """
        node = Node('Material Index', sockets={})
        return node._out

    @classmethod
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - Float [signed_angle_ (Float)]
        """
        node = Node('Edge Angle', sockets={})
        return node

    @classmethod
    @property
    def edge_neighbors(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        - Integer
        """
        node = Node('Edge Neighbors', sockets={})
        return node._out

    @classmethod
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - Integer [vertex_index_2_ (Integer), position_1_ (Vector), position_2_ (Vector)]
        """
        node = Node('Edge Vertices', sockets={})
        return node

    @classmethod
    @property
    def face_area(cls):
        """ > Node <&Node Face Area>

        Returns
        -------
        - Float
        """
        node = Node('Face Area', sockets={})
        return node._out

    @classmethod
    def is_face_planar(cls, threshold=None):
        """ > Node <&Node Is Face Planar>

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Boolean
        """
        node = Node('Is Face Planar', sockets={'Threshold': threshold})
        return node._out

    @classmethod
    def face_neighbors(cls):
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        - Integer [face_count_ (Integer)]
        """
        node = Node('Face Neighbors', sockets={})
        return node

    @classmethod
    def mesh_island(cls):
        """ > Node <&Node Mesh Island>

        Returns
        -------
        - Integer [island_count_ (Integer)]
        """
        node = Node('Mesh Island', sockets={})
        return node

    @classmethod
    def vertex_neighbors(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        - Integer [face_count_ (Integer)]
        """
        node = Node('Vertex Neighbors', sockets={})
        return node

    @classmethod
    def named_attribute(cls, name=None, data_type='FLOAT'):
        """ > Node <&Node Named Attribute>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Float [exists_ (Boolean)]
        """
        utils.check_enum_arg('Named Attribute', 'data_type', data_type, 'named_attribute', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        node = Node('Named Attribute', sockets={'Name': name}, data_type=data_type)
        return node._out

    @classmethod
    def named_layer_selection(cls, name=None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', sockets={'Name': name})
        return node._out

    @classmethod
    @property
    def normal(cls):
        """ > Node <&Node Normal>

        Returns
        -------
        - Vector
        """
        node = Node('Normal', sockets={})
        return node._out

    @classmethod
    @property
    def position(cls):
        """ > Node <&Node Position>

        Returns
        -------
        - Vector
        """
        node = Node('Position', sockets={})
        return node._out

    @classmethod
    @property
    def radius(cls):
        """ > Node <&Node Radius>

        Returns
        -------
        - Float
        """
        node = Node('Radius', sockets={})
        return node._out

    @classmethod
    def scene_time(cls):
        """ > Node <&Node Scene Time>

        Returns
        -------
        - Float [frame_ (Float)]
        """
        node = Node('Scene Time', sockets={})
        return node

    @classmethod
    @property
    def is_face_smooth(cls):
        """ > Node <&Node Is Face Smooth>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Face Smooth', sockets={})
        return node._out

    @classmethod
    def shortest_edge_paths(cls, end_vertex=None, edge_cost=None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (id: End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (id: Edge Cost)

        Returns
        -------
        - Integer [total_cost_ (Float)]
        """
        node = Node('Shortest Edge Paths', sockets={'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    @classmethod
    @property
    def is_spline_cyclic(cls):
        """ > Node <&Node Is Spline Cyclic>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Spline Cyclic', sockets={})
        return node._out

    @classmethod
    @property
    def spline_resolution(cls):
        """ > Node <&Node Spline Resolution>

        Returns
        -------
        - Integer
        """
        node = Node('Spline Resolution', sockets={})
        return node._out

    @classmethod
    @property
    def curve_tangent(cls):
        """ > Node <&Node Curve Tangent>

        Returns
        -------
        - Vector
        """
        node = Node('Curve Tangent', sockets={})
        return node._out

    @classmethod
    def instance_on_points(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Node <&Node Instance on Points>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - instance (Geometry) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', sockets={'Points': points, 'Selection': selection, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    @classmethod
    @property
    def instance_transform(cls):
        """ > Node <&Node Instance Transform>

        Returns
        -------
        - Matrix
        """
        node = Node('Instance Transform', sockets={})
        return node._out

    @classmethod
    def instances_to_points(cls, instances=None, selection=None, position=None, radius=None):
        """ > Node <&Node Instances to Points>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Instances to Points', sockets={'Instances': instances, 'Selection': selection, 'Position': position, 'Radius': radius})
        return node._out

    @classmethod
    def interpolate_curves(cls, guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Node <&Node Interpolate Curves>

        Arguments
        ---------
        - guide_curves (Geometry) : socket 'Guide Curves' (id: Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - points (Geometry) : socket 'Points' (id: Points)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve [closest_index_ (Integer), closest_weight_ (Float)]
        """
        node = Node('Interpolate Curves', sockets={'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node._out

    @classmethod
    @property
    def is_viewport(cls):
        """ > Node <&Node Is Viewport>

        Returns
        -------
        - Boolean
        """
        node = Node('Is Viewport', sockets={})
        return node._out

    @classmethod
    def join_geometry(cls, *geometry):
        """ > Node <&Node Join Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Geometry
        """
        node = Node('Join Geometry', sockets={'Geometry': list(geometry)})
        return node._out

    @classmethod
    def material_selection(cls, material=None):
        """ > Node <&Node Material Selection>

        Arguments
        ---------
        - material (Material) : socket 'Material' (id: Material)

        Returns
        -------
        - Boolean
        """
        node = Node('Material Selection', sockets={'Material': material})
        return node._out

    @classmethod
    def menu_switch(cls, menu=None, a=None, b=None, data_type='GEOMETRY'):
        """ > Node <&Node Menu Switch>

        Arguments
        ---------
        - menu (Menu) : socket 'Menu' (id: Menu)
        - a (Geometry) : socket 'A' (id: Item_0)
        - b (Geometry) : socket 'B' (id: Item_1)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Menu Switch', 'data_type', data_type, 'menu_switch', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL'))
        node = Node('Menu Switch', sockets={'Menu': menu, 'Item_0': a, 'Item_1': b}, data_type=data_type)
        return node._out

    @classmethod
    def merge_by_distance(cls, geometry=None, selection=None, distance=None, mode='ALL'):
        """ > Node <&Node Merge by Distance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - distance (Float) : socket 'Distance' (id: Distance)
        - mode (str): parameter 'mode' in ['ALL', 'CONNECTED']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Merge by Distance', 'mode', mode, 'merge_by_distance', ('ALL', 'CONNECTED'))
        node = Node('Merge by Distance', sockets={'Geometry': geometry, 'Selection': selection, 'Distance': distance}, mode=mode)
        return node._out

    @classmethod
    def merge_layers(cls, grease_pencil=None, selection=None, group_id=None, mode='MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        Arguments
        ---------
        - grease_pencil (Geometry) : socket 'Grease Pencil' (id: Grease Pencil)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - mode (str): parameter 'mode' in ['MERGE_BY_NAME', 'MERGE_BY_ID']

        Returns
        -------
        - GreasePencil
        """
        utils.check_enum_arg('Merge Layers', 'mode', mode, 'merge_layers', ('MERGE_BY_NAME', 'MERGE_BY_ID'))
        node = Node('Merge Layers', sockets={'Grease Pencil': grease_pencil, 'Selection': selection, 'Group ID': group_id}, mode=mode)
        return node._out

    @classmethod
    def mesh_boolean(cls, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>

        Arguments
        ---------
        - mesh_1 (Geometry) : socket 'Mesh 1' (id: Mesh 1)
        - mesh_2 (Geometry) : socket 'Mesh 2' (id: Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (id: Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (id: Hole Tolerant)
        - operation (str): parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']
        - solver (str): parameter 'solver' in ['EXACT', 'FLOAT']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Mesh Boolean', 'operation', operation, 'mesh_boolean', ('INTERSECT', 'UNION', 'DIFFERENCE'))
        utils.check_enum_arg('Mesh Boolean', 'solver', solver, 'mesh_boolean', ('EXACT', 'FLOAT'))
        node = Node('Mesh Boolean', sockets={'Mesh 1': mesh_1, 'Mesh 2': list(mesh_2), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, operation=operation, solver=solver)
        return node._out

    @classmethod
    def mesh_circle(cls, vertices=None, radius=None, fill_type='NONE'):
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
        node = Node('Mesh Circle', sockets={'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        return node._out

    @classmethod
    def cone(cls, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
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
        node = Node('Cone', sockets={'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        return node._out

    @classmethod
    def cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
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
        node = Node('Cube', sockets={'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        return node._out

    @classmethod
    def cylinder(cls, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
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
        node = Node('Cylinder', sockets={'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments, 'Radius': radius, 'Depth': depth}, fill_type=fill_type)
        return node._out

    @classmethod
    def face_group_boundaries(cls, face_group_id=None):
        """ > Node <&Node Face Group Boundaries>

        Arguments
        ---------
        - face_group_id (Integer) : socket 'Face Group ID' (id: Face Set)

        Returns
        -------
        - Boolean
        """
        node = Node('Face Group Boundaries', sockets={'Face Set': face_group_id})
        return node._out

    @classmethod
    def grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
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
        node = Node('Grid', sockets={'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        return node._out

    @classmethod
    def ico_sphere(cls, radius=None, subdivisions=None):
        """ > Node <&Node Ico Sphere>

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - subdivisions (Integer) : socket 'Subdivisions' (id: Subdivisions)

        Returns
        -------
        - Mesh [uv_map_ (Vector)]
        """
        node = Node('Ico Sphere', sockets={'Radius': radius, 'Subdivisions': subdivisions})
        return node._out

    @classmethod
    def mesh_line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
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
        node = Node('Mesh Line', sockets={'Count': count, 'Resolution': resolution, 'Start Location': start_location, 'Offset': offset}, count_mode=count_mode, mode=mode)
        return node._out

    @classmethod
    def mesh_to_curve(cls, mesh=None, selection=None):
        """ > Node <&Node Mesh to Curve>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Curve
        """
        node = Node('Mesh to Curve', sockets={'Mesh': mesh, 'Selection': selection})
        return node._out

    @classmethod
    def mesh_to_density_grid(cls, mesh=None, density=None, voxel_size=None, gradient_width=None):
        """ > Node <&Node Mesh to Density Grid>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - density (Float) : socket 'Density' (id: Density)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - gradient_width (Float) : socket 'Gradient Width' (id: Gradient Width)

        Returns
        -------
        - Float
        """
        node = Node('Mesh to Density Grid', sockets={'Mesh': mesh, 'Density': density, 'Voxel Size': voxel_size, 'Gradient Width': gradient_width})
        return node._out

    @classmethod
    def mesh_to_points(cls, mesh=None, selection=None, position=None, radius=None, mode='VERTICES'):
        """ > Node <&Node Mesh to Points>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)
        - mode (str): parameter 'mode' in ['VERTICES', 'EDGES', 'FACES', 'CORNERS']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Mesh to Points', 'mode', mode, 'mesh_to_points', ('VERTICES', 'EDGES', 'FACES', 'CORNERS'))
        node = Node('Mesh to Points', sockets={'Mesh': mesh, 'Selection': selection, 'Position': position, 'Radius': radius}, mode=mode)
        return node._out

    @classmethod
    def mesh_to_sdf_grid(cls, mesh=None, voxel_size=None, band_width=None):
        """ > Node <&Node Mesh to SDF Grid>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - band_width (Integer) : socket 'Band Width' (id: Band Width)

        Returns
        -------
        - Float
        """
        node = Node('Mesh to SDF Grid', sockets={'Mesh': mesh, 'Voxel Size': voxel_size, 'Band Width': band_width})
        return node._out

    @classmethod
    def mesh_to_volume(cls, mesh=None, density=None, voxel_size=None, voxel_amount=None, interior_band_width=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Mesh to Volume>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - density (Float) : socket 'Density' (id: Density)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - interior_band_width (Float) : socket 'Interior Band Width' (id: Interior Band Width)
        - resolution_mode (str): parameter 'resolution_mode' in ['VOXEL_AMOUNT', 'VOXEL_SIZE']

        Returns
        -------
        - Volume
        """
        utils.check_enum_arg('Mesh to Volume', 'resolution_mode', resolution_mode, 'mesh_to_volume', ('VOXEL_AMOUNT', 'VOXEL_SIZE'))
        node = Node('Mesh to Volume', sockets={'Mesh': mesh, 'Density': density, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width}, resolution_mode=resolution_mode)
        return node._out

    @classmethod
    def uv_sphere(cls, segments=None, rings=None, radius=None):
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
        node = Node('UV Sphere', sockets={'Segments': segments, 'Rings': rings, 'Radius': radius})
        return node._out

    @classmethod
    def object_info(cls, object=None, as_instance=None, transform_space='ORIGINAL'):
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
        node = Node('Object Info', sockets={'Object': object, 'As Instance': as_instance}, transform_space=transform_space)
        return node._out

    @classmethod
    def offset_corner_in_face(cls, corner_index=None, offset=None):
        """ > Node <&Node Offset Corner in Face>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Integer
        """
        node = Node('Offset Corner in Face', sockets={'Corner Index': corner_index, 'Offset': offset})
        return node._out

    @classmethod
    def offset_point_in_curve(cls, point_index=None, offset=None):
        """ > Node <&Node Offset Point in Curve>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Boolean [point_index_ (Integer)]
        """
        node = Node('Offset Point in Curve', sockets={'Point Index': point_index, 'Offset': offset})
        return node._out

    @classmethod
    def points(cls, count=None, position=None, radius=None):
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
        node = Node('Points', sockets={'Count': count, 'Position': position, 'Radius': radius})
        return node._out

    @classmethod
    def points_of_curve(cls, curve_index=None, weights=None, sort_index=None):
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
        node = Node('Points of Curve', sockets={'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def points_to_curves(cls, points=None, curve_group_id=None, weight=None):
        """ > Node <&Node Points to Curves>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - curve_group_id (Integer) : socket 'Curve Group ID' (id: Curve Group ID)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Curve
        """
        node = Node('Points to Curves', sockets={'Points': points, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out

    @classmethod
    def points_to_sdf_grid(cls, points=None, radius=None, voxel_size=None):
        """ > Node <&Node Points to SDF Grid>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - radius (Float) : socket 'Radius' (id: Radius)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)

        Returns
        -------
        - Float
        """
        node = Node('Points to SDF Grid', sockets={'Points': points, 'Radius': radius, 'Voxel Size': voxel_size})
        return node._out

    @classmethod
    def points_to_vertices(cls, points=None, selection=None):
        """ > Node <&Node Points to Vertices>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Mesh
        """
        node = Node('Points to Vertices', sockets={'Points': points, 'Selection': selection})
        return node._out

    @classmethod
    def points_to_volume(cls, points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Points to Volume>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - density (Float) : socket 'Density' (id: Density)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - radius (Float) : socket 'Radius' (id: Radius)
        - resolution_mode (str): parameter 'resolution_mode' in ['VOXEL_AMOUNT', 'VOXEL_SIZE']

        Returns
        -------
        - Volume
        """
        utils.check_enum_arg('Points to Volume', 'resolution_mode', resolution_mode, 'points_to_volume', ('VOXEL_AMOUNT', 'VOXEL_SIZE'))
        node = Node('Points to Volume', sockets={'Points': points, 'Density': density, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Radius': radius}, resolution_mode=resolution_mode)
        return node._out

    @classmethod
    def geometry_proximity(cls, geometry=None, group_id=None, sample_position=None, sample_group_id=None, target_element='FACES'):
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
        node = Node('Geometry Proximity', sockets={'Target': geometry, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=target_element)
        return node._out

    @classmethod
    def raycast(cls, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED'):
        """ > Node <&Node Raycast>

        Arguments
        ---------
        - target_geometry (Geometry) : socket 'Target Geometry' (id: Target Geometry)
        - attribute (Float) : socket 'Attribute' (id: Attribute)
        - source_position (Vector) : socket 'Source Position' (id: Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (id: Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (id: Ray Length)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']
        - mapping (str): parameter 'mapping' in ['INTERPOLATED', 'NEAREST']

        Returns
        -------
        - Boolean [hit_position_ (Vector), hit_normal_ (Vector), hit_distance_ (Float), attribute_ (Float)]
        """
        utils.check_enum_arg('Raycast', 'data_type', data_type, 'raycast', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Raycast', 'mapping', mapping, 'raycast', ('INTERPOLATED', 'NEAREST'))
        node = Node('Raycast', sockets={'Target Geometry': target_geometry, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type, mapping=mapping)
        return node._out

    @classmethod
    def realize_instances(cls, geometry=None, selection=None, realize_all=None, depth=None):
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
        node = Node('Realize Instances', sockets={'Geometry': geometry, 'Selection': selection, 'Realize All': realize_all, 'Depth': depth})
        return node._out

    @classmethod
    def remove_named_attribute(cls, geometry=None, name=None, pattern_mode='EXACT'):
        """ > Node <&Node Remove Named Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - name (String) : socket 'Name' (id: Name)
        - pattern_mode (str): parameter 'pattern_mode' in ['EXACT', 'WILDCARD']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Remove Named Attribute', 'pattern_mode', pattern_mode, 'remove_named_attribute', ('EXACT', 'WILDCARD'))
        node = Node('Remove Named Attribute', sockets={'Geometry': geometry, 'Name': name}, pattern_mode=pattern_mode)
        return node._out

    @classmethod
    def repeat_input(cls, iterations=None):
        """ > Node <&Node Repeat Input>

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)

        Returns
        -------
        - Integer
        """
        node = Node('Repeat Input', sockets={'Iterations': iterations})
        return node._out

    @classmethod
    def repeat_output(cls, geometry=None, inspection_index=0):
        """ > Node <&Node Repeat Output>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Item_0)
        - inspection_index (int): parameter 'inspection_index'

        Returns
        -------
        - Geometry
        """
        node = Node('Repeat Output', sockets={'Item_0': geometry}, inspection_index=inspection_index)
        return node._out

    @classmethod
    def replace_material(cls, geometry=None, old=None, new=None):
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
        node = Node('Replace Material', sockets={'Geometry': geometry, 'Old': old, 'New': new})
        return node._out

    @classmethod
    def resample_curve(cls, curve=None, selection=None, count=None, length=None, mode='COUNT'):
        """ > Node <&Node Resample Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - count (Integer) : socket 'Count' (id: Count)
        - length (Float) : socket 'Length' (id: Length)
        - mode (str): parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Resample Curve', 'mode', mode, 'resample_curve', ('EVALUATED', 'COUNT', 'LENGTH'))
        node = Node('Resample Curve', sockets={'Curve': curve, 'Selection': selection, 'Count': count, 'Length': length}, mode=mode)
        return node._out

    @classmethod
    def reverse_curve(cls, curve=None, selection=None):
        """ > Node <&Node Reverse Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Curve
        """
        node = Node('Reverse Curve', sockets={'Curve': curve, 'Selection': selection})
        return node._out

    @classmethod
    def rotate_instances(cls, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None):
        """ > Node <&Node Rotate Instances>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - pivot_point (Vector) : socket 'Pivot Point' (id: Pivot Point)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Rotate Instances', sockets={'Instances': instances, 'Selection': selection, 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})
        return node._out

    @classmethod
    def sdf_grid_boolean(cls, *grid_2, grid_1=None, operation='DIFFERENCE'):
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
        node = Node('SDF Grid Boolean', sockets={'Grid 1': grid_1, 'Grid 2': list(grid_2)}, operation=operation)
        return node._out

    @classmethod
    def sample_curve(cls, curves=None, value=None, length=None, curve_index=None, factor=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):
        """ > Node <&Node Sample Curve>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (id: Curves)
        - value (Float) : socket 'Value' (id: Value)
        - length (Float) : socket 'Length' (id: Length)
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - factor (Float) : socket 'Factor' (id: Factor)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']
        - mode (str): parameter 'mode' in ['FACTOR', 'LENGTH']
        - use_all_curves (bool): parameter 'use_all_curves'

        Returns
        -------
        - Float [position_ (Vector), tangent_ (Vector), normal_ (Vector)]
        """
        utils.check_enum_arg('Sample Curve', 'data_type', data_type, 'sample_curve', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Sample Curve', 'mode', mode, 'sample_curve', ('FACTOR', 'LENGTH'))
        node = Node('Sample Curve', sockets={'Curves': curves, 'Value': value, 'Length': length, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode=mode, use_all_curves=use_all_curves)
        return node._out

    @classmethod
    def sample_grid(cls, grid=None, position=None, data_type='FLOAT', interpolation_mode='TRILINEAR'):
        """ > Node <&Node Sample Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - position (Vector) : socket 'Position' (id: Position)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']
        - interpolation_mode (str): parameter 'interpolation_mode' in ['NEAREST', 'TRILINEAR', 'TRIQUADRATIC']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Sample Grid', 'data_type', data_type, 'sample_grid', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR'))
        utils.check_enum_arg('Sample Grid', 'interpolation_mode', interpolation_mode, 'sample_grid', ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC'))
        node = Node('Sample Grid', sockets={'Grid': grid, 'Position': position}, data_type=data_type, interpolation_mode=interpolation_mode)
        return node._out

    @classmethod
    def sample_grid_index(cls, grid=None, x=None, y=None, z=None, data_type='FLOAT'):
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
        utils.check_enum_arg('Sample Grid Index', 'data_type', data_type, 'sample_grid_index', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR'))
        node = Node('Sample Grid Index', sockets={'Grid': grid, 'X': x, 'Y': y, 'Z': z}, data_type=data_type)
        return node._out

    @classmethod
    def sample_index(cls, geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Sample Index>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Sample Index', 'data_type', data_type, 'sample_index', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Sample Index', 'domain', domain, 'sample_index', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Sample Index', sockets={'Geometry': geometry, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def sample_nearest(cls, geometry=None, sample_position=None, domain='POINT'):
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
        node = Node('Sample Nearest', sockets={'Geometry': geometry, 'Sample Position': sample_position}, domain=domain)
        return node._out

    @classmethod
    def sample_nearest_surface(cls, mesh=None, value=None, group_id=None, sample_position=None, sample_group_id=None, data_type='FLOAT'):
        """ > Node <&Node Sample Nearest Surface>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Float [is_valid_ (Boolean)]
        """
        utils.check_enum_arg('Sample Nearest Surface', 'data_type', data_type, 'sample_nearest_surface', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        node = Node('Sample Nearest Surface', sockets={'Mesh': mesh, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)
        return node._out

    @classmethod
    def sample_uv_surface(cls, mesh=None, value=None, uv_map=None, sample_uv=None, data_type='FLOAT'):
        """ > Node <&Node Sample UV Surface>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - value (Float) : socket 'Value' (id: Value)
        - uv_map (Vector) : socket 'UV Map' (id: Source UV Map)
        - sample_uv (Vector) : socket 'Sample UV' (id: Sample UV)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']

        Returns
        -------
        - Float [is_valid_ (Boolean)]
        """
        utils.check_enum_arg('Sample UV Surface', 'data_type', data_type, 'sample_uv_surface', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        node = Node('Sample UV Surface', sockets={'Mesh': mesh, 'Value': value, 'Source UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)
        return node._out

    @classmethod
    def scale_elements(cls, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """ > Node <&Node Scale Elements>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)
        - domain (str): parameter 'domain' in ['FACE', 'EDGE']
        - scale_mode (str): parameter 'scale_mode' in ['UNIFORM', 'SINGLE_AXIS']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Scale Elements', 'domain', domain, 'scale_elements', ('FACE', 'EDGE'))
        utils.check_enum_arg('Scale Elements', 'scale_mode', scale_mode, 'scale_elements', ('UNIFORM', 'SINGLE_AXIS'))
        node = Node('Scale Elements', sockets={'Geometry': geometry, 'Selection': selection, 'Scale': scale, 'Center': center, 'Axis': axis}, domain=domain, scale_mode=scale_mode)
        return node._out

    @classmethod
    def scale_instances(cls, instances=None, selection=None, scale=None, center=None, local_space=None):
        """ > Node <&Node Scale Instances>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Scale Instances', sockets={'Instances': instances, 'Selection': selection, 'Scale': scale, 'Center': center, 'Local Space': local_space})
        return node._out

    @classmethod
    @property
    def self_object(cls):
        """ > Node <&Node Self Object>

        Returns
        -------
        - Object
        """
        node = Node('Self Object', sockets={})
        return node._out

    @classmethod
    def separate_components(cls, geometry=None):
        """ > Node <&Node Separate Components>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Mesh [curve_ (Curve), grease_pencil_ (GreasePencil), point_cloud_ (Cloud), volume_ (Volume), instances_ (Instances)]
        """
        node = Node('Separate Components', sockets={'Geometry': geometry})
        return node._out

    @classmethod
    def separate_geometry(cls, geometry=None, selection=None, domain='POINT'):
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
        node = Node('Separate Geometry', sockets={'Geometry': geometry, 'Selection': selection}, domain=domain)
        return node._out

    @classmethod
    def set_handle_positions(cls, curve=None, selection=None, position=None, offset=None, mode='LEFT'):
        """ > Node <&Node Set Handle Positions>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - mode (str): parameter 'mode' in ['LEFT', 'RIGHT']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Positions', 'mode', mode, 'set_handle_positions', ('LEFT', 'RIGHT'))
        node = Node('Set Handle Positions', sockets={'Curve': curve, 'Selection': selection, 'Position': position, 'Offset': offset}, mode=mode)
        return node._out

    @classmethod
    def set_curve_normal(cls, curve=None, selection=None, normal=None, mode='MINIMUM_TWIST'):
        """ > Node <&Node Set Curve Normal>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - mode (str): parameter 'mode' in ['MINIMUM_TWIST', 'Z_UP', 'FREE']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Curve Normal', 'mode', mode, 'set_curve_normal', ('MINIMUM_TWIST', 'Z_UP', 'FREE'))
        node = Node('Set Curve Normal', sockets={'Curve': curve, 'Selection': selection, 'Normal': normal}, mode=mode)
        return node._out

    @classmethod
    def set_curve_radius(cls, curve=None, selection=None, radius=None):
        """ > Node <&Node Set Curve Radius>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Radius', sockets={'Curve': curve, 'Selection': selection, 'Radius': radius})
        return node._out

    @classmethod
    def set_curve_tilt(cls, curve=None, selection=None, tilt=None):
        """ > Node <&Node Set Curve Tilt>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - tilt (Float) : socket 'Tilt' (id: Tilt)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Tilt', sockets={'Curve': curve, 'Selection': selection, 'Tilt': tilt})
        return node._out

    @classmethod
    def set_geometry_name(cls, geometry=None, name=None):
        """ > Node <&Node Set Geometry Name>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Geometry Name', sockets={'Geometry': geometry, 'Name': name})
        return node._out

    @classmethod
    def set_id(cls, geometry=None, selection=None, id=None):
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
        node = Node('Set ID', sockets={'Geometry': geometry, 'Selection': selection, 'ID': id})
        return node._out

    @classmethod
    def set_instance_transform(cls, instances=None, selection=None, transform=None):
        """ > Node <&Node Set Instance Transform>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Instances
        """
        node = Node('Set Instance Transform', sockets={'Instances': instances, 'Selection': selection, 'Transform': transform})
        return node._out

    @classmethod
    def set_material(cls, geometry=None, selection=None, material=None):
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
        node = Node('Set Material', sockets={'Geometry': geometry, 'Selection': selection, 'Material': material})
        return node._out

    @classmethod
    def set_material_index(cls, geometry=None, selection=None, material_index=None):
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
        node = Node('Set Material Index', sockets={'Geometry': geometry, 'Selection': selection, 'Material Index': material_index})
        return node._out

    @classmethod
    def set_point_radius(cls, points=None, selection=None, radius=None):
        """ > Node <&Node Set Point Radius>

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Set Point Radius', sockets={'Points': points, 'Selection': selection, 'Radius': radius})
        return node._out

    @classmethod
    def set_position(cls, geometry=None, selection=None, position=None, offset=None):
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
        node = Node('Set Position', sockets={'Geometry': geometry, 'Selection': selection, 'Position': position, 'Offset': offset})
        return node._out

    @classmethod
    def set_shade_smooth(cls, geometry=None, selection=None, shade_smooth=None, domain='FACE'):
        """ > Node <&Node Set Shade Smooth>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)
        - domain (str): parameter 'domain' in ['EDGE', 'FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Set Shade Smooth', 'domain', domain, 'set_shade_smooth', ('EDGE', 'FACE'))
        node = Node('Set Shade Smooth', sockets={'Geometry': geometry, 'Selection': selection, 'Shade Smooth': shade_smooth}, domain=domain)
        return node._out

    @classmethod
    def set_spline_cyclic(cls, geometry=None, selection=None, cyclic=None):
        """ > Node <&Node Set Spline Cyclic>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - cyclic (Boolean) : socket 'Cyclic' (id: Cyclic)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Spline Cyclic', sockets={'Geometry': geometry, 'Selection': selection, 'Cyclic': cyclic})
        return node._out

    @classmethod
    def set_spline_resolution(cls, geometry=None, selection=None, resolution=None):
        """ > Node <&Node Set Spline Resolution>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - resolution (Integer) : socket 'Resolution' (id: Resolution)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Spline Resolution', sockets={'Geometry': geometry, 'Selection': selection, 'Resolution': resolution})
        return node._out

    @classmethod
    @property
    def simulation_input(cls):
        """ > Node <&Node Simulation Input>

        Returns
        -------
        - Float
        """
        node = Node('Simulation Input', sockets={})
        return node._out

    @classmethod
    def simulation_output(cls, skip=None, geometry=None):
        """ > Node <&Node Simulation Output>

        Arguments
        ---------
        - skip (Boolean) : socket 'Skip' (id: Skip)
        - geometry (Geometry) : socket 'Geometry' (id: Item_0)

        Returns
        -------
        - Geometry
        """
        node = Node('Simulation Output', sockets={'Skip': skip, 'Item_0': geometry})
        return node._out

    @classmethod
    def sort_elements(cls, geometry=None, selection=None, group_id=None, sort_weight=None, domain='POINT'):
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
        node = Node('Sort Elements', sockets={'Geometry': geometry, 'Selection': selection, 'Group ID': group_id, 'Sort Weight': sort_weight}, domain=domain)
        return node._out

    @classmethod
    def spline_length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - Float [point_count_ (Integer)]
        """
        node = Node('Spline Length', sockets={})
        return node

    @classmethod
    def spline_parameter(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - Float [length_ (Float), index_ (Integer)]
        """
        node = Node('Spline Parameter', sockets={})
        return node

    @classmethod
    def split_edges(cls, mesh=None, selection=None):
        """ > Node <&Node Split Edges>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)

        Returns
        -------
        - Mesh
        """
        node = Node('Split Edges', sockets={'Mesh': mesh, 'Selection': selection})
        return node._out

    @classmethod
    def split_to_instances(cls, geometry=None, selection=None, group_id=None, domain='POINT'):
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
        node = Node('Split to Instances', sockets={'Geometry': geometry, 'Selection': selection, 'Group ID': group_id}, domain=domain)
        return node._out

    @classmethod
    def store_named_attribute(cls, geometry=None, selection=None, name=None, value=None, data_type='FLOAT', domain='POINT'):
        """ > Node <&Node Store Named Attribute>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Store Named Attribute', 'data_type', data_type, 'store_named_attribute', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Store Named Attribute', 'domain', domain, 'store_named_attribute', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Store Named Attribute', sockets={'Geometry': geometry, 'Selection': selection, 'Name': name, 'Value': value}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def store_named_grid(cls, volume=None, name=None, grid=None, data_type='FLOAT'):
        """ > Node <&Node Store Named Grid>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (id: Volume)
        - name (String) : socket 'Name' (id: Name)
        - grid (Float) : socket 'Grid' (id: Grid)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'FLOAT_VECTOR', 'FLOAT2']

        Returns
        -------
        - Volume
        """
        utils.check_enum_arg('Store Named Grid', 'data_type', data_type, 'store_named_grid', ('FLOAT', 'FLOAT_VECTOR', 'FLOAT2'))
        node = Node('Store Named Grid', sockets={'Volume': volume, 'Name': name, 'Grid': grid}, data_type=data_type)
        return node._out

    @classmethod
    def join_strings(cls, *strings, delimiter=None):
        """ > Node <&Node Join Strings>

        Arguments
        ---------
        - delimiter (String) : socket 'Delimiter' (id: Delimiter)
        - strings (String) : socket 'Strings' (id: Strings)

        Returns
        -------
        - String
        """
        node = Node('Join Strings', sockets={'Delimiter': delimiter, 'Strings': list(strings)})
        return node._out

    @classmethod
    def string_to_curves(cls, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
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
        node = Node('String to Curves', sockets={'String': string, 'Size': size, 'Character Spacing': character_spacing, 'Word Spacing': word_spacing, 'Line Spacing': line_spacing, 'Text Box Width': text_box_width, 'Text Box Height': text_box_height}, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
        return node._out

    @classmethod
    def subdivide_curve(cls, curve=None, cuts=None):
        """ > Node <&Node Subdivide Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
        - cuts (Integer) : socket 'Cuts' (id: Cuts)

        Returns
        -------
        - Curve
        """
        node = Node('Subdivide Curve', sockets={'Curve': curve, 'Cuts': cuts})
        return node._out

    @classmethod
    def subdivide_mesh(cls, mesh=None, level=None):
        """ > Node <&Node Subdivide Mesh>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - level (Integer) : socket 'Level' (id: Level)

        Returns
        -------
        - Mesh
        """
        node = Node('Subdivide Mesh', sockets={'Mesh': mesh, 'Level': level})
        return node._out

    @classmethod
    def subdivision_surface(cls, mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """ > Node <&Node Subdivision Surface>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - level (Integer) : socket 'Level' (id: Level)
        - edge_crease (Float) : socket 'Edge Crease' (id: Edge Crease)
        - vertex_crease (Float) : socket 'Vertex Crease' (id: Vertex Crease)
        - boundary_smooth (str): parameter 'boundary_smooth' in ['PRESERVE_CORNERS', 'ALL']
        - uv_smooth (str): parameter 'uv_smooth' in ['NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Subdivision Surface', 'boundary_smooth', boundary_smooth, 'subdivision_surface', ('PRESERVE_CORNERS', 'ALL'))
        utils.check_enum_arg('Subdivision Surface', 'uv_smooth', uv_smooth, 'subdivision_surface', ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL'))
        node = Node('Subdivision Surface', sockets={'Mesh': mesh, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease}, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth)
        return node._out

    @classmethod
    def switch(cls, switch=None, false=None, true=None, input_type='GEOMETRY'):
        """ > Node <&Node Switch>

        Arguments
        ---------
        - switch (Boolean) : socket 'Switch' (id: Switch)
        - false (Geometry) : socket 'False' (id: False)
        - true (Geometry) : socket 'True' (id: True)
        - input_type (str): parameter 'input_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Switch', 'input_type', input_type, 'switch', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL'))
        node = Node('Switch', sockets={'Switch': switch, 'False': false, 'True': true}, input_type=input_type)
        return node._out

    @classmethod
    def _3d_cursor(cls):
        """ > Node <&Node 3D Cursor>

        Returns
        -------
        - Vector [rotation_ (Rotation)]
        """
        node = Node('3D Cursor', sockets={})
        return node

    @classmethod
    def active_element(cls, domain='POINT'):
        """ > Node <&Node Active Element>

        Arguments
        ---------
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE']

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        utils.check_enum_arg('Active Element', 'domain', domain, 'active_element', ('POINT', 'EDGE', 'FACE'))
        node = Node('Active Element', sockets={}, domain=domain)
        return node

    @classmethod
    def face_set(cls):
        """ > Node <&Node Face Set>

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Face Set', sockets={})
        return node

    @classmethod
    def mouse_position(cls):
        """ > Node <&Node Mouse Position>

        Returns
        -------
        - Integer [mouse_y_ (Integer), region_width_ (Integer), region_height_ (Integer)]
        """
        node = Node('Mouse Position', sockets={})
        return node

    @classmethod
    def selection(cls):
        """ > Node <&Node Selection>

        Returns
        -------
        - Boolean [float_ (Float)]
        """
        node = Node('Selection', sockets={})
        return node

    @classmethod
    def set_face_set(cls, mesh=None, selection=None, face_set=None):
        """ > Node <&Node Set Face Set>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - face_set (Integer) : socket 'Face Set' (id: Face Set)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Face Set', sockets={'Mesh': mesh, 'Selection': selection, 'Face Set': face_set})
        return node._out

    @classmethod
    def set_selection(cls, geometry=None, selection=None, domain='POINT', selection_type='BOOLEAN'):
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
        node = Node('Set Selection', sockets={'Geometry': geometry, 'Selection': selection}, domain=domain, selection_type=selection_type)
        return node._out

    @classmethod
    def transform_geometry(cls, geometry=None, translation=None, rotation=None, scale=None, transform=None, mode='COMPONENTS'):
        """ > Node <&Node Transform Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - transform (Matrix) : socket 'Transform' (id: Transform)
        - mode (str): parameter 'mode' in ['COMPONENTS', 'MATRIX']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Transform Geometry', 'mode', mode, 'transform_geometry', ('COMPONENTS', 'MATRIX'))
        node = Node('Transform Geometry', sockets={'Geometry': geometry, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform}, mode=mode)
        return node._out

    @classmethod
    def translate_instances(cls, instances=None, selection=None, translation=None, local_space=None):
        """ > Node <&Node Translate Instances>

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (id: Instances)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - translation (Vector) : socket 'Translation' (id: Translation)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Translate Instances', sockets={'Instances': instances, 'Selection': selection, 'Translation': translation, 'Local Space': local_space})
        return node._out

    @classmethod
    def triangulate(cls, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ > Node <&Node Triangulate>

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (id: Mesh)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - minimum_vertices (Integer) : socket 'Minimum Vertices' (id: Minimum Vertices)
        - ngon_method (str): parameter 'ngon_method' in ['BEAUTY', 'CLIP']
        - quad_method (str): parameter 'quad_method' in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Triangulate', 'ngon_method', ngon_method, 'triangulate', ('BEAUTY', 'CLIP'))
        utils.check_enum_arg('Triangulate', 'quad_method', quad_method, 'triangulate', ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL'))
        node = Node('Triangulate', sockets={'Mesh': mesh, 'Selection': selection, 'Minimum Vertices': minimum_vertices}, ngon_method=ngon_method, quad_method=quad_method)
        return node._out

    @classmethod
    def trim_curve(cls, curve=None, selection=None, start=None, end=None, start_1=None, end_1=None, mode='FACTOR'):
        """ > Node <&Node Trim Curve>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (id: Curve)
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
        node = Node('Trim Curve', sockets={'Curve': curve, 'Selection': selection, 'Start': start, 'End': end, 'Start_001': start_1, 'End_001': end_1}, mode=mode)
        return node._out

    @classmethod
    def pack_uv_islands(cls, uv=None, selection=None, margin=None, rotate=None):
        """ > Node <&Node Pack UV Islands>

        Arguments
        ---------
        - uv (Vector) : socket 'UV' (id: UV)
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - margin (Float) : socket 'Margin' (id: Margin)
        - rotate (Boolean) : socket 'Rotate' (id: Rotate)

        Returns
        -------
        - Vector
        """
        node = Node('Pack UV Islands', sockets={'UV': uv, 'Selection': selection, 'Margin': margin, 'Rotate': rotate})
        return node._out

    @classmethod
    def uv_unwrap(cls, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """ > Node <&Node UV Unwrap>

        Arguments
        ---------
        - selection (Boolean) : socket 'Selection' (id: Selection)
        - seam (Boolean) : socket 'Seam' (id: Seam)
        - margin (Float) : socket 'Margin' (id: Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (id: Fill Holes)
        - method (str): parameter 'method' in ['ANGLE_BASED', 'CONFORMAL']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('UV Unwrap', 'method', method, 'uv_unwrap', ('ANGLE_BASED', 'CONFORMAL'))
        node = Node('UV Unwrap', sockets={'Selection': selection, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)
        return node._out

    @classmethod
    def vertex_of_corner(cls, corner_index=None):
        """ > Node <&Node Vertex of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer
        """
        node = Node('Vertex of Corner', sockets={'Corner Index': corner_index})
        return node._out

    @classmethod
    def viewer(cls, geometry=None, value=None, data_type='FLOAT', domain='AUTO'):
        """ > Node <&Node Viewer>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)
        - value (Float) : socket 'Value' (id: Value)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4']
        - domain (str): parameter 'domain' in ['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Viewer', 'data_type', data_type, 'viewer', ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'))
        utils.check_enum_arg('Viewer', 'domain', domain, 'viewer', ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        node = Node('Viewer', sockets={'Geometry': geometry, 'Value': value}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def viewport_transform(cls):
        """ > Node <&Node Viewport Transform>

        Returns
        -------
        - Matrix [view_ (Matrix), is_orthographic_ (Boolean)]
        """
        node = Node('Viewport Transform', sockets={})
        return node

    @classmethod
    def volume_cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
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
        node = Node('Volume Cube', sockets={'Density': density, 'Background': background, 'Min': min, 'Max': max, 'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})
        return node._out

    @classmethod
    def volume_to_mesh(cls, volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ > Node <&Node Volume to Mesh>

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (id: Volume)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)
        - resolution_mode (str): parameter 'resolution_mode' in ['GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Volume to Mesh', 'resolution_mode', resolution_mode, 'volume_to_mesh', ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE'))
        node = Node('Volume to Mesh', sockets={'Volume': volume, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Threshold': threshold, 'Adaptivity': adaptivity}, resolution_mode=resolution_mode)
        return node._out

    @classmethod
    def warning(cls, show=None, message=None, warning_type='ERROR'):
        """ > Node <&Node Warning>

        Arguments
        ---------
        - show (Boolean) : socket 'Show' (id: Show)
        - message (String) : socket 'Message' (id: Message)
        - warning_type (str): parameter 'warning_type'

        Returns
        -------
        - Boolean
        """
        node = Node('Warning', sockets={'Show': show, 'Message': message}, warning_type=warning_type)
        return node._out

    @classmethod
    def frame(cls, label_size=20, shrink=True, text=None):
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
        node = Node('Frame', sockets={}, label_size=label_size, shrink=shrink, text=text)
        return node._out

    @classmethod
    @property
    def group_input(cls):
        """ > Node <&Node Group Input>

        Returns
        -------
        - None
        """
        node = Node('Group Input', sockets={})
        return node._out

    @classmethod
    def group_output(cls, is_active_output=True):
        """ > Node <&Node Group Output>

        Arguments
        ---------
        - is_active_output (bool): parameter 'is_active_output'

        Returns
        -------
        - None
        """
        node = Node('Group Output', sockets={}, is_active_output=is_active_output)
        return node._out

    @classmethod
    def reroute(cls, input=None, socket_idname='NodeSocketColor'):
        """ > Node <&Node Reroute>

        Arguments
        ---------
        - input (Color) : socket 'Input' (id: Input)
        - socket_idname (str): parameter 'socket_idname'

        Returns
        -------
        - Color
        """
        node = Node('Reroute', sockets={'Input': input}, socket_idname=socket_idname)
        return node._out

    @classmethod
    def blackbody(cls, temperature=None):
        """ > Node <&Node Blackbody>

        Arguments
        ---------
        - temperature (Float) : socket 'Temperature' (id: Temperature)

        Returns
        -------
        - Color
        """
        node = Node('Blackbody', sockets={'Temperature': temperature})
        return node._out

    @classmethod
    def clamp(cls, value=None, min=None, max=None, clamp_type='MINMAX'):
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
        node = Node('Clamp', sockets={'Value': value, 'Min': min, 'Max': max}, clamp_type=clamp_type)
        return node._out

    @classmethod
    def combine_xyz(cls, x=None, y=None, z=None):
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
        node = Node('Combine XYZ', sockets={'X': x, 'Y': y, 'Z': z})
        return node._out

    @classmethod
    def float_curve(cls, value=None, factor=None):
        """ > Node <&Node Float Curve>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - factor (Float) : socket 'Factor' (id: Factor)

        Returns
        -------
        - Float
        """
        node = NodeCurves('Float Curve', sockets={'Value': value, 'Factor': factor})
        return node._out

    @classmethod
    def map_range(cls, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, from_min_1=None, from_max_1=None, to_min_1=None, to_max_1=None, steps_1=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR'):
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
        utils.check_enum_arg('Map Range', 'data_type', data_type, 'map_range', ('FLOAT', 'FLOAT_VECTOR'))
        utils.check_enum_arg('Map Range', 'interpolation_type', interpolation_type, 'map_range', ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'))
        node = Node('Map Range', sockets={'Value': value, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max, 'Steps': steps, 'Vector': vector, 'From_Min_FLOAT3': from_min_1, 'From_Max_FLOAT3': from_max_1, 'To_Min_FLOAT3': to_min_1, 'To_Max_FLOAT3': to_max_1, 'Steps_FLOAT3': steps_1}, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)
        return node._out

    @classmethod
    def math(cls, value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False):
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
        node = Node('Math', sockets={'Value': value, 'Value_001': value_1, 'Value_002': value_2}, operation=operation, use_clamp=use_clamp)
        return node._out

    @classmethod
    def mix(cls, a=None, b=None, a_1=None, b_1=None, a_2=None, b_2=None, a_3=None, b_3=None, factor=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM'):
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
        utils.check_enum_arg('Mix', 'data_type', data_type, 'mix', ('FLOAT', 'VECTOR', 'RGBA', 'ROTATION'))
        utils.check_enum_arg('Mix', 'factor_mode', factor_mode, 'mix', ('UNIFORM', 'NON_UNIFORM'))
        node = Node('Mix', sockets={'A_Float': a, 'B_Float': b, 'A_Vector': a_1, 'B_Vector': b_1, 'A_Color': a_2, 'B_Color': b_2, 'A_Rotation': a_3, 'B_Rotation': b_3, 'Factor_Vector': factor}, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type=data_type, factor_mode=factor_mode)
        return node._out

    @classmethod
    def rgb_curves(cls, color=None, fac=None):
        """ > Node <&Node RGB Curves>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Color
        """
        node = NodeCurves('RGB Curves', sockets={'Color': color, 'Fac': fac})
        return node._out

    @classmethod
    def separate_xyz(cls, vector=None):
        """ > Node <&Node Separate XYZ>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)

        Returns
        -------
        - Float [y_ (Float), z_ (Float)]
        """
        node = Node('Separate XYZ', sockets={'Vector': vector})
        return node._out

    @classmethod
    def brick_texture(cls, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
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
        - Color [fac_ (Float)]
        """
        node = Node('Brick Texture', sockets={'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node._out

    @classmethod
    def checker_texture(cls, vector=None, color1=None, color2=None, scale=None):
        """ > Node <&Node Checker Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - scale (Float) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Color [fac_ (Float)]
        """
        node = Node('Checker Texture', sockets={'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return node._out

    @classmethod
    def gabor_texture(cls, vector=None, scale=None, frequency=None, anisotropy=None, orientation=None, orientation_1=None, gabor_type='2D'):
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
        node = Node('Gabor Texture', sockets={'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation 2D': orientation, 'Orientation 3D': orientation_1}, gabor_type=gabor_type)
        return node._out

    @classmethod
    def gradient_texture(cls, vector=None, gradient_type='LINEAR'):
        """ > Node <&Node Gradient Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - gradient_type (str): parameter 'gradient_type' in ['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']

        Returns
        -------
        - Color [fac_ (Float)]
        """
        utils.check_enum_arg('Gradient Texture', 'gradient_type', gradient_type, 'gradient_texture', ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'))
        node = Node('Gradient Texture', sockets={'Vector': vector}, gradient_type=gradient_type)
        return node._out

    @classmethod
    def magic_texture(cls, vector=None, scale=None, distortion=None, turbulence_depth=2):
        """ > Node <&Node Magic Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - turbulence_depth (int): parameter 'turbulence_depth'

        Returns
        -------
        - Color [fac_ (Float)]
        """
        node = Node('Magic Texture', sockets={'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return node._out

    @classmethod
    def noise_texture(cls, vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, offset=None, gain=None, distortion=None, noise_dimensions='3D', noise_type='FBM', normalize=True):
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
        node = Node('Noise Texture', sockets={'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Offset': offset, 'Gain': gain, 'Distortion': distortion}, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize)
        return node._out

    @classmethod
    def voronoi_texture(cls, vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', normalize=False, voronoi_dimensions='3D'):
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
        node = Node('Voronoi Texture', sockets={'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Smoothness': smoothness, 'Exponent': exponent, 'Randomness': randomness}, distance=distance, feature=feature, normalize=normalize, voronoi_dimensions=voronoi_dimensions)
        return node._out

    @classmethod
    def wave_texture(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
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
        - Color [fac_ (Float)]
        """
        utils.check_enum_arg('Wave Texture', 'bands_direction', bands_direction, 'wave_texture', ('X', 'Y', 'Z', 'DIAGONAL'))
        utils.check_enum_arg('Wave Texture', 'rings_direction', rings_direction, 'wave_texture', ('X', 'Y', 'Z', 'SPHERICAL'))
        utils.check_enum_arg('Wave Texture', 'wave_profile', wave_profile, 'wave_texture', ('SIN', 'SAW', 'TRI'))
        utils.check_enum_arg('Wave Texture', 'wave_type', wave_type, 'wave_texture', ('BANDS', 'RINGS'))
        node = Node('Wave Texture', sockets={'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node._out

    @classmethod
    def white_noise_texture(cls, vector=None, w=None, noise_dimensions='3D'):
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
        node = Node('White Noise Texture', sockets={'Vector': vector, 'W': w}, noise_dimensions=noise_dimensions)
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

    @classmethod
    @property
    def value(cls):
        """ > Node <&Node Value>

        Returns
        -------
        - Float
        """
        node = Node('Value', sockets={})
        return node._out

    @classmethod
    def vector_curves(cls, vector=None, fac=None):
        """ > Node <&Node Vector Curves>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Vector
        """
        node = NodeCurves('Vector Curves', sockets={'Vector': vector, 'Fac': fac})
        return node._out

    @classmethod
    def vector_math(cls, vector=None, vector_1=None, vector_2=None, scale=None, operation='ADD'):
        """ > Node <&Node Vector Math>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - vector_1 (Vector) : socket 'Vector' (id: Vector_001)
        - vector_2 (Vector) : socket 'Vector' (id: Vector_002)
        - scale (Float) : socket 'Scale' (id: Scale)
        - operation (str): parameter 'operation' in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Math', 'operation', operation, 'vector_math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'))
        node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1, 'Vector_002': vector_2, 'Scale': scale}, operation=operation)
        return node._out

    @classmethod
    def vector_rotate(cls, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
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
        node = Node('Vector Rotate', sockets={'Vector': vector, 'Center': center, 'Axis': axis, 'Angle': angle, 'Rotation': rotation}, invert=invert, rotation_type=rotation_type)
        return node._out

