from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Vector(Socket):

    def less_than(self, b=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN')
        return node._out

    def less_equal(self, b=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL')
        return node._out

    def greater_than(self, b=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN')
        return node._out

    def greater_equal(self, b=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_VEC3': self, 'B_VEC3': b}, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL')
        return node._out

    def equal(self, b=None, epsilon=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_VEC3': self, 'B_VEC3': b, 'Epsilon': epsilon}, data_type='VECTOR', mode='ELEMENT', operation='EQUAL')
        return node._out

    def not_equal(self, b=None, epsilon=None):
        """ > Method <&Node Compare>

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
        node = Node('Compare', sockets={'A_VEC3': self, 'B_VEC3': b, 'Epsilon': epsilon}, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL')
        return node._out

    @property
    def to_rotation(self):
        """ > Property Get <&Node Euler to Rotation>

        Information
        -----------
        - Socket 'Euler' : self

        Returns
        -------
        - Rotation
        """
        node = Node('Euler to Rotation', sockets={'Euler': self})
        return node._out

    def hash_value(self, seed=None):
        """ > Method <&Node Hash Value>

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
        node = Node('Hash Value', sockets={'Value': self, 'Seed': seed}, data_type='VECTOR')
        return node._out

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        """ > Constructor <&Node Random Value>

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
        node = Node('Random Value', sockets={'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    def blur(self, iterations=None, weight=None):
        """ > Method <&Node Blur Attribute>

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
        node = Node('Blur Attribute', sockets={'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type='FLOAT_VECTOR')
        return node._out

    @classmethod
    def Named(cls, name=None):
        """ > Constructor <&Node Named Attribute>

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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name=None):
        """ > Constructor <&Node Named Attribute>

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
        node = Node('Named Attribute', sockets={'Name': name}, data_type='FLOAT_VECTOR')
        return cls(node._out)

    def sample_grid(self, position=None, interpolation_mode='TRILINEAR'):
        """ > Method <&Node Sample Grid>

        Information
        -----------
        - Socket 'Grid' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - interpolation_mode (str): parameter 'interpolation_mode' in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')

        Returns
        -------
        - Vector
        """
        node = Node('Sample Grid', sockets={'Grid': self, 'Position': position}, data_type='VECTOR', interpolation_mode=interpolation_mode)
        return node._out

    def sample_grid_index(self, x=None, y=None, z=None):
        """ > Method <&Node Sample Grid Index>

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
        node = Node('Sample Grid Index', sockets={'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='VECTOR')
        return node._out

    def pack_uv_islands(self, margin=None, rotate=None):
        """ > Method <&Node Pack UV Islands>

        Information
        -----------
        - Socket 'UV' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - margin (Float) : socket 'Margin' (id: Margin)
        - rotate (Boolean) : socket 'Rotate' (id: Rotate)

        Returns
        -------
        - Vector
        """
        node = Node('Pack UV Islands', sockets={'UV': self, 'Selection': self._sel, 'Margin': margin, 'Rotate': rotate})
        return node._out

    @classmethod
    def CombineXYZ(cls, x=None, y=None, z=None):
        """ > Constructor <&Node Combine XYZ>

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
        return cls(node._out)

    def mix_uniform(self, b=None, factor=None, clamp_factor=True):
        """ > Method <&Node Mix>

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
        node = Node('Mix', sockets={'A_Vector': self, 'B_Vector': b, 'Factor_Float': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='UNIFORM')
        return node._out

    def mix_non_uniform(self, b=None, factor=None, clamp_factor=True):
        """ > Method <&Node Mix>

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
        node = Node('Mix', sockets={'A_Vector': self, 'B_Vector': b, 'Factor_Vector': factor}, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='NON_UNIFORM')
        return node._out

    @property
    def xyz(self):
        """ > Property Get <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - tuple (Float, Float, Float)
        """
        node = self._cache('Separate XYZ', sockets={'Vector': self})
        return (node.x, node.y, node.z)

    @property
    def separate_xyz(self):
        """ > Property Get <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - node [x (Float), y (Float), z (Float)]
        """
        node = self._cache('Separate XYZ', sockets={'Vector': self})
        return node

    @property
    def x(self):
        """ > Property Get <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - x
        """
        node = self._cache('Separate XYZ', sockets={'Vector': self})
        return node.x

    @property
    def y(self):
        """ > Property Get <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - y
        """
        node = self._cache('Separate XYZ', sockets={'Vector': self})
        return node.y

    @property
    def z(self):
        """ > Property Get <&Node Separate XYZ>

        Information
        -----------
        - Socket 'Vector' : self

        Returns
        -------
        - z
        """
        node = self._cache('Separate XYZ', sockets={'Vector': self})
        return node.z

    def vector_curves(self, fac=None):
        """ > Method <&Node Vector Curves>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Vector
        """
        node = Node('Vector Curves', sockets={'Vector': self, 'Fac': fac})
        return node._out

    def add(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='ADD')
        return node._out

    def subtract(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='SUBTRACT')
        return node._out

    def multiply(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='MULTIPLY')
        return node._out

    def divide(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='DIVIDE')
        return node._out

    def multiply_add(self, multiplier=None, addend=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': multiplier, 'Vector_002': addend}, operation='MULTIPLY_ADD')
        return node._out

    def cross(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='CROSS_PRODUCT')
        return node._out

    def project(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='PROJECT')
        return node._out

    def reflect(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='REFLECT')
        return node._out

    def refract(self, vector=None, ior=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector, 'Scale': ior}, operation='REFRACT')
        return node._out

    def faceforward(self, incident=None, reference=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': incident, 'Vector_002': reference}, operation='FACEFORWARD')
        return node._out

    def dot(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='DOT_PRODUCT')
        return node._out

    def distance(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='DISTANCE')
        return node._out

    @property
    def length(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'LENGTH'

        Returns
        -------
        - Float
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='LENGTH')
        return node._out

    def scale(self, scale=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Scale': scale}, operation='SCALE')
        return node._out

    @property
    def normalize(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'NORMALIZE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='NORMALIZE')
        return node._out

    @property
    def abs(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'ABSOLUTE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='ABSOLUTE')
        return node._out

    def min(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='MINIMUM')
        return node._out

    def max(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='MAXIMUM')
        return node._out

    @property
    def floor(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'FLOOR'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='FLOOR')
        return node._out

    @property
    def ceil(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'CEIL'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='CEIL')
        return node._out

    @property
    def fraction(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'FRACTION'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='FRACTION')
        return node._out

    def modulo(self, vector=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': vector}, operation='MODULO')
        return node._out

    def wrap(self, max=None, min=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': max, 'Vector_002': min}, operation='WRAP')
        return node._out

    def snap(self, increment=None):
        """ > Method <&Node Vector Math>

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
        node = Node('Vector Math', sockets={'Vector': self, 'Vector_001': increment}, operation='SNAP')
        return node._out

    @property
    def sin(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'SINE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='SINE')
        return node._out

    @property
    def cos(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'COSINE'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='COSINE')
        return node._out

    @property
    def tan(self):
        """ > Property Get <&Node Vector Math>

        Information
        -----------
        - Socket 'Vector' : self
        - Parameter 'operation' : 'TANGENT'

        Returns
        -------
        - Vector
        """
        node = Node('Vector Math', sockets={'Vector': self}, operation='TANGENT')
        return node._out

    def rotate(self, center=None, axis=None, angle=None, invert=False, rotation_type='AXIS_ANGLE'):
        """ > Method <&Node Vector Rotate>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)
        - invert (bool): parameter 'invert'
        - rotation_type (str): parameter 'rotation_type' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')

        Returns
        -------
        - Vector
        """
        node = Node('Vector Rotate', sockets={'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type=rotation_type)
        return node._out

    def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):
        """ > Method <&Node Vector Rotate>

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
        node = Node('Vector Rotate', sockets={'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle}, invert=invert, rotation_type='AXIS_ANGLE')
        return node._out

    def rotate_x_axis(self, center=None, angle=None, invert=False):
        """ > Method <&Node Vector Rotate>

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
        node = Node('Vector Rotate', sockets={'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='X_AXIS')
        return node._out

    def rotate_y_axis(self, center=None, angle=None, invert=False):
        """ > Method <&Node Vector Rotate>

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
        node = Node('Vector Rotate', sockets={'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='Y_AXIS')
        return node._out

    def rotate_z_axis(self, center=None, angle=None, invert=False):
        """ > Method <&Node Vector Rotate>

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
        node = Node('Vector Rotate', sockets={'Vector': self, 'Center': center, 'Angle': angle}, invert=invert, rotation_type='Z_AXIS')
        return node._out

    def rotate_euler_xyz(self, center=None, rotation=None, invert=False):
        """ > Method <&Node Vector Rotate>

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
        node = Node('Vector Rotate', sockets={'Vector': self, 'Center': center, 'Rotation': rotation}, invert=invert, rotation_type='EULER_XYZ')
        return node._out

    def mapping(self, location=None, rotation=None, scale=None, vector_type='POINT'):
        """ > Method <&ShaderNode Mapping>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - location (Vector) : socket 'Location' (id: Location)
        - rotation (Vector) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - vector_type (str): parameter 'vector_type' in ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL')

        Returns
        -------
        - Vector
        """
        node = Node('Mapping', sockets={'Vector': self, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    def normal(self):
        """ > Method <&ShaderNode Normal>

        Information
        -----------
        - Socket 'Normal' : self

        Returns
        -------
        - Vector [dot_ (Float)]
        """
        node = Node('Normal', sockets={'Normal': self})
        return node._out

    @classmethod
    def Tangent(cls, axis='Z', direction_type='RADIAL', uv_map=''):
        """ > Constructor <&ShaderNode Tangent>

        Arguments
        ---------
        - axis (str): parameter 'axis' in ('X', 'Y', 'Z')
        - direction_type (str): parameter 'direction_type' in ('RADIAL', 'UV_MAP')
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        node = Node('Tangent', sockets={}, axis=axis, direction_type=direction_type, uv_map=uv_map)
        return cls(node._out)

    def environment_texture(self, image=None, interpolation='Linear', projection='EQUIRECTANGULAR'):
        """ > Method <&ShaderNode Environment Texture>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - image (NoneType): parameter 'image'
        - interpolation (str): parameter 'interpolation' in ('Linear', 'Closest', 'Cubic', 'Smart')
        - projection (str): parameter 'projection' in ('EQUIRECTANGULAR', 'MIRROR_BALL')

        Returns
        -------
        - Color
        """
        node = Node('Environment Texture', sockets={'Vector': self}, image=image, interpolation=interpolation, projection=projection)
        return node._out

    def ies_texture_internal(self, strength=None, filepath='', ies=None):
        """ > Method <&ShaderNode IES Texture>

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
        node = Node('IES Texture', sockets={'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode='INTERNAL')
        return node._out

    def ies_texture_external(self, strength=None, filepath='', ies=None):
        """ > Method <&ShaderNode IES Texture>

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
        node = Node('IES Texture', sockets={'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode='EXTERNAL')
        return node._out

    def ies_texture(self, strength=None, filepath='', ies=None, mode='INTERNAL'):
        """ > Method <&ShaderNode IES Texture>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - filepath (str): parameter 'filepath'
        - ies (NoneType): parameter 'ies'
        - mode (str): parameter 'mode' in ('INTERNAL', 'EXTERNAL')

        Returns
        -------
        - Float
        """
        node = Node('IES Texture', sockets={'Vector': self, 'Strength': strength}, filepath=filepath, ies=ies, mode=mode)
        return node._out

    def image_texture(self, extension='REPEAT', image=None, interpolation='Linear', projection='FLAT', projection_blend=0.0):
        """ > Method <&ShaderNode Image Texture>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - extension (str): parameter 'extension' in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
        - image (NoneType): parameter 'image'
        - interpolation (str): parameter 'interpolation' in ('Linear', 'Closest', 'Cubic', 'Smart')
        - projection (str): parameter 'projection' in ('FLAT', 'BOX', 'SPHERE', 'TUBE')
        - projection_blend (float): parameter 'projection_blend'

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        node = Node('Image Texture', sockets={'Vector': self}, extension=extension, image=image, interpolation=interpolation, projection=projection, projection_blend=projection_blend)
        return node._out

    def point_density(self, interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM', radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR'):
        """ > Method <&ShaderNode Point Density>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - interpolation (str): parameter 'interpolation' in ('Closest', 'Linear', 'Cubic')
        - object (NoneType): parameter 'object'
        - particle_color_source (str): parameter 'particle_color_source' in ('PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY')
        - particle_system (NoneType): parameter 'particle_system'
        - point_source (str): parameter 'point_source' in ('PARTICLE_SYSTEM', 'OBJECT')
        - radius (float): parameter 'radius'
        - resolution (int): parameter 'resolution'
        - space (str): parameter 'space' in ('OBJECT', 'WORLD')
        - vertex_attribute_name (str): parameter 'vertex_attribute_name'
        - vertex_color_source (str): parameter 'vertex_color_source' in ('VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL')

        Returns
        -------
        - Color [density_ (Float)]
        """
        node = Node('Point Density', sockets={'Vector': self}, interpolation=interpolation, object=object, particle_color_source=particle_color_source, particle_system=particle_system, point_source=point_source, radius=radius, resolution=resolution, space=space, vertex_attribute_name=vertex_attribute_name, vertex_color_source=vertex_color_source)
        return node._out

    @classmethod
    def UvMap(cls, from_instancer=False, uv_map=''):
        """ > Constructor <&ShaderNode UV Map>

        Arguments
        ---------
        - from_instancer (bool): parameter 'from_instancer'
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        node = Node('UV Map', sockets={}, from_instancer=from_instancer, uv_map=uv_map)
        return cls(node._out)

    def vector_transform(self, convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR'):
        """ > Method <&ShaderNode Vector Transform>

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - convert_from (str): parameter 'convert_from' in ('WORLD', 'OBJECT', 'CAMERA')
        - convert_to (str): parameter 'convert_to' in ('WORLD', 'OBJECT', 'CAMERA')
        - vector_type (str): parameter 'vector_type' in ('POINT', 'VECTOR', 'NORMAL')

        Returns
        -------
        - Vector
        """
        node = Node('Vector Transform', sockets={'Vector': self}, convert_from=convert_from, convert_to=convert_to, vector_type=vector_type)
        return node._out

