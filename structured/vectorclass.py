import numpy as np

import bpy
from geonodes.structured.treeclass import Tree, Node
from geonodes.structured.socketclass import DataSocket
from geonodes.structured.floatclass import Float

# =============================================================================================================================
# Boolean

class VectRot(DataSocket):

    @property
    def math(self):
        from geonodes.structured import math
        return math

    def _reset(self):
        self._separate_xyz = None

    # ====================================================================================================
    # Properties

    @property
    def separate_xyz(self):
        if self._separate_xyz is None:
            self._separate_xyz = Node("Separate XYZ", {'Vector': self})
        return self._separate_xyz

    @property
    def x(self):
        return self.separate_xyz.x

    @property
    def y(self):
        return self.separate_xyz.y

    @property
    def z(self):
        return self.separate_xyz.z

    # ====================================================================================================
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        return cls(Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT_VECTOR')._out)

    # ====================================================================================================
    # Methods

    # ----- Vector math

    def add(self, other):
        return self.math.vadd(self, other)

    def subtract(self, other):
        return self.math.vsubtract(self, other)

    def multiply(self, other):
        return self.math.vmultiply(self, other)

    def divide(self, other):
        return self.math.vdivide(self, other)

    def multiply_add(self, multiplier, addend):
        return self.math.vmultiply_add(self, multiplier, addend)

    def cross_product(self, other):
        return self.math.vmulticross_productply_add(self, multiplier, addend)

    def project(self, other):
        return self.math.project(self, other)

    def reflect(self, other):
        return self.math.reflect(self, other)

    def refract(self, other, ior=None):
        return self.math.refract(self, other, ior=ior)

    def faceforward(self, incident=None, reference=None):
        return self.math.faceforward(self, incident, reference)

    def dot_product(self, other):
        return self.math.dot_product(self, other)

    def distance(self, other):
        return self.math.distance(self, other)

    @property
    def length(self):
        return self.math.length(self)

    def scale(self, scale):
        return self.math.scale(self, scale)

    def normalize(self):
        return self.math.normalize(self)

    def abs(self):
        return self.math.vabs(self)

    def min(self, other):
        return self.math.vmin(self, other)

    def max(self, other):
        return self.math.vmax(self, other)

    def floor(self):
        return self.math.vfloor(self)

    def ceil(self):
        return self.math.vceil(self)

    def fraction(self):
        return self.math.vfraction(self)

    def modulo(self, other):
        return self.math.vmodulo(self, other)

    def wrap(self, max=None, min=None):
        return self.math.vwrap(self, max, min)

    def snap(self, increment):
        return self.math.vsnap(self, increment)

    def sin(self):
        return self.math.vsin(self)

    def cos(self):
        return self.math.vcos(self)

    def tan(self):
        return self.math.vtan(self)

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_factor=None):
        return Float(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='FLOAT')._out)

    # ----- Clamp

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        return Float(Node('Clamp', {'Value': self, 'Min': min, 'Max': max}, clamp_type=clamp_type)._out)

    def clamp_range(self, min=None, max=None, clamp_type='RANGE'):
        return self.clamp(min, max, clamp_type)

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type=None):
        return Float(Node('Map Range', {'value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, interpolation_type=interpolation_type)._out)

    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='LINEAR')

    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='STEPPED')

    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHSTEP')

    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHERSTEP')

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.math.scale(self, -1)

    # ----- Addition

    def __add__(self, other):
        return self.math.vadd(self, other)

    def __radd__(self, other):
        return self.math.vadd(other, self)

    # ----- Subtraction

    def __sub__(self, other):
        return self.math.vsubtract(self, other)

    def __rsub__(self, other):
        return self.math.vsubtract(other, self)

    # ----- Multiplication

    def __mul__(self, other):
        return self.math.vmultiply(self, other)

    def __rmul__(self, other):
        return self.math.vmultiply(other, self)

    # ----- Division

    def __truediv__(self, other):
        return self.vdivide(self, other)

    def __rtruediv__(self, other):
        return self.vdivide(other, self)

    # ----- Modulo

    def __mod__(self, other):
        return self.math.vmodulo(self, other)

    def __rmod__(self, other):
        return self.math.vmodulo(other, self)

    # ----- Mat mul -> dot product

    def __matmul__(self, other):
        return self.math.dot_product(self, other)

    def __rmatmul__(self, other):
        return self.math.dot_product(other, self)

    # ----- Power -> cross product

    def __pow__(self, other):
        return self.math.cross_product(self, other)

    def __rpow__(self, other):
        return self.math.cross_product(other, self)



class Vector(VectRot):

    SOCKET_TYPE = 'VECTOR'

    # ====================================================================================================
    # Constructor

    @classmethod
    def FromRotation(cls, rotation=None):
        return Rotation(rotation).to_euler()

    # ====================================================================================================
    # Conversion

    def to_rotation(self):
        return Rotation.FromEuler(self)

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_factor=None, factor_mode=None):
        return Vector(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, factor_mode=factor_mode, data_type='VECTOR'))

    def mix_uniform(self, factor=None, other=None, clamp_factor=None):
        return self.mix(factor, other, clamp_factor, factor_mode='UNIFORM')

    def mix_non_uniform(self, factor=None, other=None, clamp_factor=None):
        return self.mix(factor, other, clamp_factor, factor_mode='NON_UNIFORM')

    # ----- Rotation

    def vector_rotate(self, center=None, axis=None, angle=None, rotation=None, invert=None, rotation_type=None):
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle, 'Rotation': rotation},
            invert=invert, rotation_type=rotation_type)._out)

    def rotate_axis(self, center=None, axis=None, angle=None, invert=None):
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle},
            invert=invert, rotation_type='AXIS_ANGLE')._out)

    def rotate_x(self, center=None, angle=None, invert=None):
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle},
            invert=invert, rotation_type='X_AXIS')._out)

    def rotate_y(self, center=None, angle=None, invert=None):
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle},
            invert=invert, rotation_type='Y_AXIS')._out)

    def rotate_z(self, center=None, angle=None, invert=None):
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle},
            invert=invert, rotation_type='Z_AXIS')._out)

    def rotate_euler(self, center=None, rotation=None, invert=None):
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Rotation': rotation},
            invert=invert, rotation_type='EULER_XYZ')._out)

    def rotate(self, rotation=None):
        return Vector(Node('Rotate Vector', {'Vector': self, 'Rotation': rotation})._out)


class Rotation(VectRot):

    SOCKET_TYPE = 'ROTATION'

    # ====================================================================================================
    # Constructors

    @classmethod
    def AxesToRotation(cls, axis_1='Z', target_1=(0, 0, 1), axis_2='X', target_2=(1, 0, 0)):
        return Rotation(Node('Axes to Rotation', {'Primary Axis': target_1, 'Secondary Axis': target_2}, primary_axis=axis_1, secondary_axis=axis_2)._out)

    @classmethod
    def FromAxes(cls, axis_1='Z', target_1=(0, 0, 1), axis_2='X', target_2=(1, 0, 0)):
        return cls.AxesToRotation(axis_1, target_1, axis_2, target_2)

    @classmethod
    def AxisAngleToRotation(cls, axis=(0, 0, 1), angle=0):
        return Rotation(Node('Axis Angle to Rotation', {'Axis': axis, 'Angle': angle})._out)

    @classmethod
    def FromAxisAngle(cls, axis=(0, 0, 1), angle=0):
        return cls.AxisAngleToRotation(axis, angle)

    @classmethod
    def EulerToRotation(cls, euler=(0, 0, 0)):
        return Rotation(Node('Euler to Rotation', {'Euler': euler})._out)

    @classmethod
    def FromEuler(cls, euler=(0, 0, 0)):
        return cls.EulerToRotation(euler)

    @classmethod
    def QuaternionToRotation(cls, w=0, x=0, y=0, z=0):
        return Rotation(Node('Quaternion to Rotation', {'W': w, 'X': x, 'Y': y, 'Z': z})._out)

    @classmethod
    def FromQuaternion(cls, w=0, x=0, y=0, z=0):
        return cls.QuaternionToRotation(w, x, y, z)

    # ====================================================================================================
    # Conversion

    def to_axis_angle(self):
        node = Node("Rotation to Axis Angle", {'Rotation': self})
        return node
        return node['Axis'], node['Angle']

    def to_euler(self):
        return Vector(Node("Rotation to Euler", {'Rotation': self})._out)

    def to_quaternion(self):
        node = Node("Rotation to Quaternion", {'Rotation': self})
        return Float(node['W']), Float(node['X']), Float(node['Y']), Float(node['Z']),

    # ====================================================================================================
    # Methods

    def mix(self, factor=None, other=None, clamp_factor=None):
        return Rotation(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='ROTATION'))

    # ----- Rotate vector

    def rotate_vector(self, vector=None):
        return Vector(Node('Rotate Vector', {'Vector': vector, 'Rotation': self})._out)

    # ----- Rotation

    def rotate_local(self, rotate_by=None):
        return Rotation(Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space='LOCAL')._out)

    def rotate_global(self, rotate_by=None):
        return Rotation(Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space='GLOBAL')._out)

    # ----- Align to vector

    def align_to_vector(self, vector=None, factor=None, axis=None, pivot_axis=None):
        return Rotation(Node('Align Rotation to Vector', {'Rotation': self, 'Factor': factor, 'Vector': vector},
            axis=axis, pivot_axis=pivot_axis)._out)

    def align_x_to_vector(self, vector=None, factor=None, pivot_axis=None):
        return self.align_to_vector(vector, factor, axis='X', pivot_axis=pivot_axis)

    def align_y_to_vector(self, vector=None, factor=None, pivot_axis=None):
        return self.align_to_vector(vector, factor, axis='Y', pivot_axis=pivot_axis)

    def align_z_to_vector(self, vector=None, factor=None, pivot_axis=None):
        return self.align_to_vector(vector, factor, axis='Z', pivot_axis=pivot_axis)

    # ----- Invert

    def invert(self):
        return Rotation(Node('Invert Rotation', {'Rotation': self})._out)
