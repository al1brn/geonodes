# Generated 2025-12-08 08:30:17

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


class Vector(Socket):
    """"
    $DOC SET hidden
    """
    def less_than(self, b: Vector = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_THAN'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_VEC3)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b: Vector = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'LESS_EQUAL'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_VEC3)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b: Vector = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_THAN'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_VEC3)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b: Vector = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'GREATER_EQUAL'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_VEC3)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b: Vector = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'EQUAL'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_VEC3)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b, 'Epsilon': epsilon}, data_type='VECTOR', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b: Vector = None, epsilon: Float = None):
        """ > Node <&Node Compare>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'mode' : 'ELEMENT'
        - Parameter 'operation' : 'NOT_EQUAL'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_VEC3)
        - epsilon (Float) : socket 'Epsilon' (id: Epsilon)

        Returns
        -------
        - Boolean
        """
        node = Node('Compare', {'A_VEC3': self, 'B_VEC3': b, 'Epsilon': epsilon}, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    def to_rotation(self):
        """ > Node <&Node Euler to Rotation>

        Information
        -----------
        - Socket 'Euler' : self

        Returns
        -------
        - Rotation
        """
        node = Node('Euler to Rotation', {'Euler': self})
        return node._out

    def hash_value(self, seed: Integer = None):
        """ > Node <&Node Hash Value>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Integer
        """
        node = Node('Hash Value', {'Value': self, 'Seed': seed}, data_type='VECTOR')
        return node._out

    @classmethod
    def Random(cls,
                    min: Vector = None,
                    max: Vector = None,
                    id: Integer = None,
                    seed: Integer = None):
        """ > Node <&Node Random Value>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT_VECTOR'

        Arguments
        ---------
        - min (Vector) : socket 'Min' (id: Min)
        - max (Vector) : socket 'Max' (id: Max)
        - id (Integer) : socket 'ID' (id: ID)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Vector
        """
        node = Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    def blur(self, iterations: Integer = None, weight: Float = None):
        """ > Node <&Node Blur Attribute>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'FLOAT_VECTOR'

        Arguments
        ---------
        - iterations (Integer) : socket 'Iterations' (id: Iterations)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Vector
        """
        node = Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='FLOAT_VECTOR')
        return node._out

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT_VECTOR'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Vector
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'FLOAT_VECTOR'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Vector
        """
        node = Node('Named Attribute', {'Name': name}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    def pack_uv_islands(self,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None):
        """ > Node <&Node Pack UV Islands>

        Information
        -----------
        - Socket 'UV' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - margin (Float) : socket 'Margin' (id: Margin)
        - rotate (Boolean) : socket 'Rotate' (id: Rotate)
        - method (menu='Bounding Box') : ('Bounding Box', 'Convex Hull', 'Exact Shape')

        Returns
        -------
        - Vector
        """
        node = Node('Pack UV Islands', {'UV': self, 'Selection': self.get_selection(), 'Margin': margin, 'Rotate': rotate, 'Method': method})
        return node._out

    @classmethod
    def CombineXYZ(cls, x: Float = None, y: Float = None, z: Float = None):
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
        return cls(node._out)

    def mix_uniform(self, b: Vector = None, factor: Float = None, clamp_factor = True):
        """ > Node <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'factor_mode' : 'UNIFORM'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_Vector)
        - factor (Float) : socket 'Factor' (id: Factor_Float)
        - clamp_factor (bool): parameter 'clamp_factor'

        Returns
        -------
        - Vector
        """
        node = Node('Mix', {'A_Vector': self, 'B_Vector': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='UNIFORM')
        return node._out

    def mix_non_uniform(self, b: Vector = None, factor: Vector = None, clamp_factor = True):
        """ > Node <&Node Mix>

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'factor_mode' : 'NON_UNIFORM'

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_Vector)
        - factor (Vector) : socket 'Factor' (id: Factor_Vector)
        - clamp_factor (bool): parameter 'clamp_factor'

        Returns
        -------
        - Vector
        """
        node = Node('Mix', {'A_Vector': self, 'B_Vector': b, 'Factor_Vector': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='NON_UNIFORM')
        return node._out

    @property
    def xyz(self):
        """ > Node <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - tuple (Float, Float, Float)
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return (node.x, node.y, node.z)

    def separate_xyz(self):
        """ > Node <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - node [x (Float), y (Float), z (Float)]
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node

    @property
    def x(self):
        """ > Node <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - x
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node.x

    @property
    def y(self):
        """ > Node <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - y
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node.y

    @property
    def z(self):
        """ > Node <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - z
        """
        node = self._cache('Separate XYZ', {'Vector': self})
        return node.z

    def add(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'ADD'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='ADD')
        return node._out

    def subtract(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'SUBTRACT'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='SUBTRACT')
        return node._out

    def multiply(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'MULTIPLY'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MULTIPLY')
        return node._out

    def divide(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'DIVIDE'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='DIVIDE')
        return node._out

    def multiply_add(self, multiplier: Vector = None, addend: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'MULTIPLY_ADD'

        Arguments
        ---------
        - multiplier (Vector) : socket 'Multiplier' (id: Vector_001)
        - addend (Vector) : socket 'Addend' (id: Vector_002)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': multiplier, 'Vector_002': addend}, operation='MULTIPLY_ADD')
        return node._out

    def cross(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'CROSS_PRODUCT'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='CROSS_PRODUCT')
        return node._out

    def project(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'PROJECT'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='PROJECT')
        return node._out

    def reflect(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'REFLECT'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='REFLECT')
        return node._out

    def refract(self, vector: Vector = None, ior: Float = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'REFRACT'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)
        - ior (Float) : socket 'IOR' (id: Scale)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector, 'Scale': ior}, operation='REFRACT')
        return node._out

    def faceforward(self, incident: Vector = None, reference: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'FACEFORWARD'

        Arguments
        ---------
        - incident (Vector) : socket 'Incident' (id: Vector_001)
        - reference (Vector) : socket 'Reference' (id: Vector_002)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': incident, 'Vector_002': reference}, operation='FACEFORWARD')
        return node._out

    def dot(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'DOT_PRODUCT'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Float
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='DOT_PRODUCT')
        return node._out

    def distance(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'DISTANCE'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Float
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='DISTANCE')
        return node._out

    def length(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'LENGTH'

        Returns
        -------
        - Float
        """
        node = Node('Vector Math', {'Vector': self}, operation='LENGTH')
        return node._out

    def scale(self, scale: Float = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'SCALE'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Scale': scale}, operation='SCALE')
        return node._out

    def normalize(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'NORMALIZE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='NORMALIZE')
        return node._out

    def abs(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'ABSOLUTE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='ABSOLUTE')
        return node._out

    def power(self, exponent: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Base' : self
        - Parameter 'operation' : 'POWER'

        Arguments
        ---------
        - exponent (Vector) : socket 'Exponent' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': exponent}, operation='POWER')
        return node._out

    def sign(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'SIGN'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='SIGN')
        return node._out

    def min(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'MINIMUM'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MINIMUM')
        return node._out

    def max(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'MAXIMUM'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MAXIMUM')
        return node._out

    def floor(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'FLOOR'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='FLOOR')
        return node._out

    def ceil(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'CEIL'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='CEIL')
        return node._out

    def fraction(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'FRACTION'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='FRACTION')
        return node._out

    def modulo(self, vector: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'MODULO'

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': vector}, operation='MODULO')
        return node._out

    def wrap(self, max: Vector = None, min: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'WRAP'

        Arguments
        ---------
        - max (Vector) : socket 'Max' (id: Vector_001)
        - min (Vector) : socket 'Min' (id: Vector_002)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': max, 'Vector_002': min}, operation='WRAP')
        return node._out

    def snap(self, increment: Vector = None):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'SNAP'

        Arguments
        ---------
        - increment (Vector) : socket 'Increment' (id: Vector_001)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self, 'Vector_001': increment}, operation='SNAP')
        return node._out

    def sin(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'SINE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='SINE')
        return node._out

    def cos(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'COSINE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='COSINE')
        return node._out

    def tan(self):
        """ > Node <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'TANGENT'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', {'Vector': self}, operation='TANGENT')
        return node._out

    def rotate(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE'):
        """ > Node <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)
        - invert (bool): parameter 'invert'
        - rotation_type (str): parameter 'rotation_type' in ['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Rotate', 'rotation_type', rotation_type, 'rotate', ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'))
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type=rotation_type)
        return node._out

    def rotate_axis_angle(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False):
        """ > Node <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'rotation_type' : 'AXIS_ANGLE'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type='AXIS_ANGLE')
        return node._out

    def rotate_x_axis(self, center: Vector = None, angle: Float = None, invert = False):
        """ > Node <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'rotation_type' : 'X_AXIS'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - angle (Float) : socket 'Angle' (id: Angle)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='X_AXIS')
        return node._out

    def rotate_y_axis(self, center: Vector = None, angle: Float = None, invert = False):
        """ > Node <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'rotation_type' : 'Y_AXIS'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - angle (Float) : socket 'Angle' (id: Angle)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='Y_AXIS')
        return node._out

    def rotate_z_axis(self, center: Vector = None, angle: Float = None, invert = False):
        """ > Node <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'rotation_type' : 'Z_AXIS'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - angle (Float) : socket 'Angle' (id: Angle)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='Z_AXIS')
        return node._out

    def rotate_euler_xyz(self, center: Vector = None, rotation: Vector = None, invert = False):
        """ > Node <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'rotation_type' : 'EULER_XYZ'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - rotation (Vector) : socket 'Rotation' (id: Rotation)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Rotate', {'Vector': self, 'Center': center, 'Rotation': rotation}, invert=invert, rotation_type='EULER_XYZ')
        return node._out

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation (menu='Trilinear') : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')

        Returns
        -------
        - Vector
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='VECTOR')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - x (Integer) : socket 'X' (id: X)
        - y (Integer) : socket 'Y' (id: Y)
        - z (Integer) : socket 'Z' (id: Z)

        Returns
        -------
        - Vector
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='VECTOR')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        Information
        -----------
        - Socket 'Topology' : self
        - Parameter 'data_type' : 'VECTOR'

        Returns
        -------
        - None
        """
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='VECTOR', **sockets)
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
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - velocity (Vector) : socket 'Velocity' (id: Velocity)
        - time_step (Float) : socket 'Time Step' (id: Time Step)
        - integration_scheme (menu='Runge-Kutta 3') : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
        - limiter (menu='Clamp') : ('None', 'Clamp', 'Revert')

        Returns
        -------
        - Vector
        """
        node = Node('Advect Grid', {'Grid': self, 'Velocity': velocity, 'Time Step': time_step, 'Integration Scheme': integration_scheme, 'Limiter': limiter}, data_type='VECTOR')
        return node._out

    def grid_curl(self):
        """ > Node <&Node Grid Curl>

        Information
        -----------
        - Socket 'Grid' : self

        Returns
        -------
        - Vector
        """
        node = Node('Grid Curl', {'Grid': self})
        return node._out

    def grid_divergence(self):
        """ > Node <&Node Grid Divergence>

        Information
        -----------
        - Socket 'Grid' : self

        Returns
        -------
        - Float
        """
        node = Node('Grid Divergence', {'Grid': self})
        return node._out

    def prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Vector = None):
        """ > Node <&Node Prune Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - mode (menu='Threshold') : ('Inactive', 'Threshold', 'SDF')
        - threshold (Vector) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Vector
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode, 'Threshold': threshold}, data_type='VECTOR')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Returns
        -------
        - Vector
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='VECTOR')
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

    def set_grid_background(self, background: Vector = None):
        """ > Node <&Node Set Grid Background>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - background (Vector) : socket 'Background' (id: Background)

        Returns
        -------
        - Vector
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background}, data_type='VECTOR')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Boolean [grid_ (Vector)]
        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='VECTOR')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Returns
        -------
        - Matrix [background_value_ (Vector)]
        """
        node = Node('Grid Info', {'Grid': self}, data_type='VECTOR')
        return node._out

    def uv_tangent(self, method: Literal['Exact', 'Fast'] = None):
        """ > Node <&Node UV Tangent>

        Information
        -----------
        - Socket 'UV' : self

        Arguments
        ---------
        - method (menu='Exact') : ('Exact', 'Fast')

        Returns
        -------
        - Vector
        """
        node = Node('UV Tangent', {'Method': method, 'UV': self})
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Vector
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='VECTOR')
        return node._out

    def radial_tiling(self, sides: Float = None, roundness: Float = None, normalize = False):
        """ > Node <&Node Radial Tiling>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - sides (Float) : socket 'Sides' (id: Sides)
        - roundness (Float) : socket 'Roundness' (id: Roundness)
        - normalize (bool): parameter 'normalize'

        Returns
        -------
        - Vector [segment_id_ (Float), segment_width_ (Float), segment_rotation_ (Float)]
        """
        node = Node('Radial Tiling', {'Vector': self, 'Sides': sides, 'Roundness': roundness}, normalize=normalize)
        return node._out

    def mapping(self,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT'):
        """ > Node <&ShaderNode Mapping>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - location (Vector) : socket 'Location' (id: Location)
        - rotation (Vector) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - vector_type (str): parameter 'vector_type' in ['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Mapping', 'vector_type', vector_type, 'mapping', ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL'))
        node = Node('Mapping', {'Vector': self, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    def normal(self):
        """ > Node <&ShaderNode Normal>

        Information
        -----------
        - Socket 'Normal' : self

        Returns
        -------
        - Vector [dot_ (Float)]
        """
        node = Node('Normal', {'Normal': self})
        return node._out

    @classmethod
    def Tangent(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = ''):
        """ > Node <&ShaderNode Tangent>

        Arguments
        ---------
        - axis (str): parameter 'axis' in ['X', 'Y', 'Z']
        - direction_type (str): parameter 'direction_type' in ['RADIAL', 'UV_MAP']
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Tangent', 'axis', axis, 'Tangent', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Tangent', 'direction_type', direction_type, 'Tangent', ('RADIAL', 'UV_MAP'))
        node = Node('Tangent', axis=axis, direction_type=direction_type, uv_map=uv_map)
        return cls(node._out)

    def environment_texture(self,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR'):
        """ > Node <&ShaderNode Environment Texture>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - image (NoneType): parameter 'image'
        - interpolation (str): parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
        - projection (str): parameter 'projection' in ['EQUIRECTANGULAR', 'MIRROR_BALL']

        Returns
        -------
        - Color
        """
        utils.check_enum_arg('Environment Texture', 'interpolation', interpolation, 'environment_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Environment Texture', 'projection', projection, 'environment_texture', ('EQUIRECTANGULAR', 'MIRROR_BALL'))
        node = Node('Environment Texture', {'Vector': self}, image=image, interpolation=interpolation, projection=projection)
        return node._out

    def ies_texture_internal(self, strength: Float = None, filepath = '', ies = None):
        """ > Node <&ShaderNode IES Texture>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'mode' : 'INTERNAL'

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - filepath (str): parameter 'filepath'
        - ies (NoneType): parameter 'ies'

        Returns
        -------
        - Float
        """
        node = Node('IES Texture', {'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode='INTERNAL')
        return node._out

    def ies_texture_external(self, strength: Float = None, filepath = '', ies = None):
        """ > Node <&ShaderNode IES Texture>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'mode' : 'EXTERNAL'

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - filepath (str): parameter 'filepath'
        - ies (NoneType): parameter 'ies'

        Returns
        -------
        - Float
        """
        node = Node('IES Texture', {'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode='EXTERNAL')
        return node._out

    def ies_texture(self,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL'):
        """ > Node <&ShaderNode IES Texture>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - filepath (str): parameter 'filepath'
        - ies (NoneType): parameter 'ies'
        - mode (str): parameter 'mode' in ['INTERNAL', 'EXTERNAL']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('IES Texture', 'mode', mode, 'ies_texture', ('INTERNAL', 'EXTERNAL'))
        node = Node('IES Texture', {'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode=mode)
        return node._out

    def image_texture(self,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0):
        """ > Node <&ShaderNode Image Texture>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - extension (str): parameter 'extension' in ['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
        - image (NoneType): parameter 'image'
        - interpolation (str): parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
        - projection (str): parameter 'projection' in ['FLAT', 'BOX', 'SPHERE', 'TUBE']
        - projection_blend (float): parameter 'projection_blend'

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        utils.check_enum_arg('Image Texture', 'extension', extension, 'image_texture', ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'))
        utils.check_enum_arg('Image Texture', 'interpolation', interpolation, 'image_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Image Texture', 'projection', projection, 'image_texture', ('FLAT', 'BOX', 'SPHERE', 'TUBE'))
        node = Node('Image Texture', {'Vector': self}, extension=extension, image=image, interpolation=interpolation, projection=projection, projection_blend=projection_blend)
        return node._out

    @classmethod
    def UvMap(cls, from_instancer = False, uv_map = ''):
        """ > Node <&ShaderNode UV Map>

        Arguments
        ---------
        - from_instancer (bool): parameter 'from_instancer'
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        node = Node('UV Map', from_instancer=from_instancer, uv_map=uv_map)
        return cls(node._out)

    def vector_transform(self,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR'):
        """ > Node <&ShaderNode Vector Transform>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - convert_from (str): parameter 'convert_from' in ['WORLD', 'OBJECT', 'CAMERA']
        - convert_to (str): parameter 'convert_to' in ['WORLD', 'OBJECT', 'CAMERA']
        - vector_type (str): parameter 'vector_type' in ['POINT', 'VECTOR', 'NORMAL']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Transform', 'convert_from', convert_from, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'convert_to', convert_to, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'vector_type', vector_type, 'vector_transform', ('POINT', 'VECTOR', 'NORMAL'))
        node = Node('Vector Transform', {'Vector': self}, convert_from=convert_from, convert_to=convert_to, vector_type=vector_type)
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = (0, 0, 0),
        name: str = 'Vector',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
        subtype: str = 'NONE',
         ):
        """ > Vector Input

        New <#Vector> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Vector') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
        - subtype (str = 'NONE') : Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')

        Returns
        -------
        - Vector
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketVector', default_value = defval,
            name=name, min=min, max=max, tip=tip, panel=panel, optional_label=optional_label,
            hide_value=hide_value, hide_in_modifier=hide_in_modifier, dimensions=dimensions,
            default_attribute=default_attribute, default_input=default_input, shape=shape, subtype=subtype)

    @classmethod
    def Percentage(cls,
        value: object = (0, 0, 0),
        name: str = 'Percentage',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Percentage Input

        New <#Vector> input with subtype 'PERCENTAGE'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Percentage') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='PERCENTAGE')

    @classmethod
    def Factor(cls,
        value: object = (0, 0, 0),
        name: str = 'Factor',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Factor Input

        New <#Vector> input with subtype 'FACTOR'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Factor') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='FACTOR')

    @classmethod
    def Translation(cls,
        value: object = (0, 0, 0),
        name: str = 'Translation',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Translation Input

        New <#Vector> input with subtype 'TRANSLATION'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Translation') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='TRANSLATION')

    @classmethod
    def Direction(cls,
        value: object = (0, 0, 0),
        name: str = 'Direction',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Direction Input

        New <#Vector> input with subtype 'DIRECTION'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Direction') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='DIRECTION')

    @classmethod
    def Velocity(cls,
        value: object = (0, 0, 0),
        name: str = 'Velocity',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Velocity Input

        New <#Vector> input with subtype 'VELOCITY'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Velocity') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='VELOCITY')

    @classmethod
    def Acceleration(cls,
        value: object = (0, 0, 0),
        name: str = 'Acceleration',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Acceleration Input

        New <#Vector> input with subtype 'ACCELERATION'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Acceleration') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='ACCELERATION')

    @classmethod
    def Euler(cls,
        value: object = (0, 0, 0),
        name: str = 'Euler',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Euler Input

        New <#Vector> input with subtype 'EULER'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Euler') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='EULER')

    @classmethod
    def Xyz(cls,
        value: object = (0, 0, 0),
        name: str = 'Xyz',
        min: float = -3.40282e+38,
        max: float = 3.40282e+38,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        dimensions: int = 3,
        default_attribute: str = '',
        default_input: Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'] = 'VALUE',
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Xyz Input

        New <#Vector> input with subtype 'XYZ'.

        Aguments
        --------
        - value  (object = (0, 0, 0)) : Default value
        - name  (str = 'Xyz') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - dimensions  (int = 3) : Property dimensions
        - default_attribute  (str = '') : Property default_attribute_name
        - default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier,
            dimensions=dimensions, default_attribute=default_attribute, default_input=default_input,
            shape=shape, subtype='XYZ')

