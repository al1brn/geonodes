#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : vectorclass
--------------------
- Implement vector like classes

classes
-------
- VectorLike    : Base class for Vector,Rotation and Color
- VectRot       : Base class for Vector and Rotation
- Vector        : DataSocket of type 'VECTOR'
- Rotation      : DataSocket of type 'ROTATION'
- Matrix        : DataSocket of type 'MATRIX'

functions
---------

updates
-------
- creation : 2024/07/23
- update   : 2024/09/04
"""


import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socketclass import ValueSocket

# =============================================================================================================================
# =============================================================================================================================
# Base Vector, Rotation and Color
# =============================================================================================================================
# =============================================================================================================================

class VectorLike(ValueSocket):

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.math.scale(self, -1)._lcop()

    def __abs__(self):
        return self.math.vabs(self)._lcop()

    # ----- Addition

    def __add__(self, other):
        return self.math.vadd(self, other)._lcop()

    def __radd__(self, other):
        return self.math.vadd(other, self)._lcop()

    def __iadd__(self, other):
        return self._jump(self.math.vadd(self, other))

    # ----- Subtraction

    def __sub__(self, other):
        return self.math.vsubtract(self, other)._lcop()

    def __rsub__(self, other):
        return self.math.vsubtract(other, self)._lcop()

    def __isub__(self, other):
        return self._jump(self.math.vsubtract(self, other))

    # ----- Multiplication

    def __mul__(self, other):
        if utils.is_value_like(other):
            return self.math.scale(self, other)
        return self.math.vmultiply(self, other)._lcop()

    def __rmul__(self, other):
        if utils.is_value_like(other):
            return self.math.scale(self, other)
        return self.math.vmultiply(other, self)._lcop()

    def __imul__(self, other):
        return self._jump(self.math.vmultiply(self, other))

    # ----- Division

    def __truediv__(self, other):
        return self.math.vdivide(self, other)._lcop()

    def __rtruediv__(self, other):
        return self.math.vdivide(other, self)._lcop()

    def __itruediv__(self, other):
        return self._jump(self.math.vdivide(self, other))

    # ----- Modulo

    def __mod__(self, other):
        return self.math.vmodulo(self, other)._lcop()

    def __rmod__(self, other):
        return self.math.vmodulo(other, self)._lcop()

    def __imod__(self, other):
        return self._jump(self.math.vmodulo(self, other))

    # ----- Mat mul -> dot product

    def __matmul__(self, other):
        return self.math.dot_product(self, other)._lcop()

    # ----- Power -> cross product

    def __pow__(self, other):
        return self.math.cross_product(self, other)._lcop()

    def __rpow__(self, other):
        return self.math.cross_product(other, self)._lcop()

    def __ipow__(self, other):
        return self._jump(self.math.cross_product(self, other))

    # ----- Functions

    def __floor__(self):
        return self.math.vfloor(self)._lcop()

    def __ceil__(self):
        return self.math.vceil(self)._lcop()

    def __abs__(self):
        return self.math.vabs(self)._lcop()




# =============================================================================================================================
# =============================================================================================================================
# Base Vector and Rotation
# =============================================================================================================================
# =============================================================================================================================

class VectRot(VectorLike):

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
    def Combine(cls, x, y, z):
        return cls(Node('Combine XYZ', {0: x, 1: y, 2:z})._out)

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
        return self.math.cross_product(self, other)

    def cross(self, other):
        return self.math.cross_product(self, other)

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

    def dot(self, other):
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

    # ----- Clamp

    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        return Node('Clamp', {'Value': self, 'Min': min, 'Max': max}, clamp_type=clamp_type)._out

    def clamp_range(self, min=None, max=None, clamp_type='RANGE'):
        return self.clamp(min, max, clamp_type)

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type=None):
        return Node('Map Range', {'value': self, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max}, clamp=clamp, interpolation_type=interpolation_type)._out

    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='LINEAR')

    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='STEPPED')

    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHSTEP')

    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=None):
        return self.map_range(from_min, from_max, to_min, to_max, clamp=clamp, interpolation_type='SMOOTHERSTEP')

    # ----- Other

    def curves(self, fac=None, keep=None):
        return Node('Vector Curves', {'Vector': self, 'Fac': fac}, _keep=keep)._out

    # ====================================================================================================
    # Comparison

    def less_than(self, other, epsilon=None, mode='ELEMENT'):
        # mode in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='VECTOR', operation='LESS_THAN', mode=mode)._out

    def less_equal(self, other, epsilon=None, mode='ELEMENT'):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='VECTOR', operation='LESS_EQUAL', mode=mode)._out

    def greater_than(self, other, epsilon=None, mode='ELEMENT'):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='VECTOR', operation='GREATER_THAN', mode=mode)._out

    def greater_equal(self, other, epsilon=None, mode='ELEMENT'):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='VECTOR', operation='GREATER_EQUAL', mode=mode)._out

    def equal(self, other, epsilon=None, mode='ELEMENT'):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='VECTOR', operation='EQUAL', mode=mode)._out

    def not_equal(self, other, epsilon=None, mode='ELEMENT'):
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='VECTOR', operation='NOT_EQUAL', mode=mode)._out




# =============================================================================================================================
# =============================================================================================================================
# Vector
# =============================================================================================================================
# =============================================================================================================================

class Vector(VectRot):

    SOCKET_TYPE = 'VECTOR'

    def __init__(self, value=(0, 0, 0), name=None, tip=None, subtype='NONE'):
        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                a = utils.value_to_array(value, (3,))
                if utils.has_bsocket(a) or Tree.is_shader:
                    bsock = Node('Combine XYZ', {0: a[0], 1: a[1], 2:a[2]})._out
                else:
                    bsock = Node('Vector', vector=tuple(a))._out
            else:
                bsock = Tree.new_input('NodeSocketVector', name, value=value, subtype=subtype, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Translation(cls, value=(0., 0., 0.), name='Translation', tip=None):
        return cls(value=value, name=name, tip=tip, subtype='TRANSLATION')

    @classmethod
    def Direction(cls, value=(0., 0., 0.), name='Direction', tip=None):
        return cls(value=value, name=name, tip=tip, subtype='DIRECTION')

    @classmethod
    def Velocity(cls, value=(0., 0., 0.), name='Velocity', tip=None):
        return cls(value=value, name=name, tip=tip, subtype='VELOCITY')

    @classmethod
    def Acceleration(cls, value=(0., 0., 0.), name='Acceleration', tip=None):
        return cls(value=value, name=name, tip=tip, subtype='ACCELERATION')

    @classmethod
    def Euler(cls, value=(0., 0., 0.), name='Euler', tip=None):
        return cls(value=value, name=name, tip=tip, subtype='EULER')

    @classmethod
    def XYZ(cls, value=(0., 0., 0.), name='XYZ', tip=None):
        return cls(value=value, name=name, tip=tip, subtype='XYZ')

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
        return Vector(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, factor_mode=factor_mode, data_type='VECTOR')._out)

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

    # ----- Geometry

    def index_of_nearest(self, group_id=None):
        index = Node('Index of Nearest', {'Position': self, 'Group ID': group_id})._out
        index.has_neighbor_ = index.node.has_neighbor
        return index

    # ====================================================================================================
    # Shader

    def to_output(self, name=None):
        if self._tree._btree.bl_idname == 'ShaderNodeTree' and not self._tree._is_group:
            if name is None:
                self._tree.set_displacement(self)
            else:
                self._tree.aov_output(name=name, color=self)
        else:
            super().to_output(name=name)

    def displacement_out(self, target='ALL'):
        self._tree.set_displacement(self, target=target)


    @classmethod
    def Tangent(cls, axis='Z', direction_type='RADIAL', uv_map=''):
        """ Node 'Tangent' (ShaderNodeTangent)
        - axis in ('X', 'Y', 'Z')
        - direction_type in ('RADIAL', 'UV_MAP')
        """

        node = Node('Tangent', axis=axis, direction_type=direction_type, uv_map=uv_map)
        return node._out

    @classmethod
    def UVMap(cls, uv_map='', from_instancer=False):
        """ Node 'UV Map' (ShaderNodeUVMap)
        """

        node = Node('UV Map', from_instancer=from_instancer, uv_map=uv_map)
        return node._out

    # ----- Vector

    def bump(self, strength=None, distance=None, height=None, invert=False):
        node = Node('Bump', {'Strength': strength, 'Distance': distance, 'Height': height, 'Normal': self}, invert=invert)
        return node._out

    def displacement(self, height=None, midlevel=None, scale=None, space='OBJECT'):
        node = Node('Displacement', {'Height': height, 'Midlevel': midlevel, 'Scale': scale, 'Normal': self}, space=space)
        return node._out

    def mapping(self, location=None, rotation=None, scale=None, vector_type='POINT'):
        # vector_type in ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL')
        node = Node('Mapping', {'Vector': self, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    def normal(self, normal=None):
        """Node 'Normal'

        Tree: Shader

        Arguments
        ---------
        - normal (Vector) :

        Returns
        -------
        - Vector
        """
        node = Node('Normal', {'Normal': self})
        vec = node._out
        vec._bsocket.default_value = normal
        vec.dot_ = node.dot
        return vec

    @classmethod
    def NormalMap(cls, strength=None, color=None, space='TANGENT', uv_map=''):
        # space in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
        node = Node('Normal Map', {'Strength': strength, 'Color': color}, space=space, uv_map=uv_map)
        return node._out

    def vector_displacement(self, midlevel=None, scale=None, space='TANGENT'):
        # space in ('TANGENT', 'OBJECT', 'WORLD')
        node = Node('Vector Displacement', {'Vector': self, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out

    def transform(self, convert_from='WORLD', convert_to='OBJECT', vector_type='NORMAL'):
        # convert_from in ('WORLD', 'OBJECT', 'CAMERA')
        # convert_to in ('WORLD', 'OBJECT', 'CAMERA')
        # vector_type in ('POINT', 'VECTOR', 'NORMAL')
        node = Node('Vector Transform', {'Vector': self}, convert_from=convert_from, convert_to=convert_to, vector_type=vector_type)
        return node._out


# =============================================================================================================================
# =============================================================================================================================
# Rotation
# =============================================================================================================================
# =============================================================================================================================

class Rotation(VectRot):

    SOCKET_TYPE = 'ROTATION'

    def __init__(self, value=(0., 0., 0.), name=None, tip=None):
        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                a = utils.value_to_array(value, (3,))
                if utils.has_bsocket(a):
                    bsock = Node('Combine XYZ', {0: a[0], 1: a[1], 2:a[2]})._out
                else:
                    bsock = Node('Rotation', rotation_euler=value)._out
            else:
                bsock = Tree.new_input('NodeSocketRotation', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def AxesToRotation(cls, axis_1='Z', target_1=(0, 0, 1), axis_2='X', target_2=(1, 0, 0)):
        return Node('Axes to Rotation', {'Primary Axis': target_1, 'Secondary Axis': target_2}, primary_axis=axis_1, secondary_axis=axis_2)._out

    @classmethod
    def FromAxes(cls, axis_1='Z', target_1=(0, 0, 1), axis_2='X', target_2=(1, 0, 0)):
        return cls.AxesToRotation(axis_1, target_1, axis_2, target_2)

    @classmethod
    def AxisAngleToRotation(cls, axis=(0, 0, 1), angle=0):
        return Node('Axis Angle to Rotation', {'Axis': axis, 'Angle': angle})._out

    @classmethod
    def FromAxisAngle(cls, axis=(0, 0, 1), angle=0):
        return cls.AxisAngleToRotation(axis, angle)

    @classmethod
    def EulerToRotation(cls, euler=(0, 0, 0)):
        return Node('Euler to Rotation', {'Euler': euler})._out

    @classmethod
    def FromEuler(cls, euler=(0, 0, 0)):
        return cls.EulerToRotation(euler)

    @classmethod
    def QuaternionToRotation(cls, w=0, x=0, y=0, z=0):
        return Node('Quaternion to Rotation', {'W': w, 'X': x, 'Y': y, 'Z': z})._out

    @classmethod
    def FromQuaternion(cls, w=0, x=0, y=0, z=0):
        return cls.QuaternionToRotation(w, x, y, z)

    @classmethod
    def AlignToVector(cls, vector=None, factor=None, axis=None, pivot_axis=None):
        return Node('Align Rotation to Vector', {'Rotation': None, 'Factor': factor, 'Vector': vector},
            axis=axis, pivot_axis=pivot_axis)._out

    @classmethod
    def AlignXToVector(cls, vector=None, factor=None, pivot_axis=None):
        return cls.AlignToVector(vector, factor, axis='X', pivot_axis=pivot_axis)

    @classmethod
    def AlignYToVector(cls, vector=None, factor=None, pivot_axis=None):
        return cls.AlignToVector(vector, factor, axis='Y', pivot_axis=pivot_axis)

    @classmethod
    def AlignZToVector(cls, vector=None, factor=None, pivot_axis=None):
        return cls.AlignToVector(vector, factor, axis='Z', pivot_axis=pivot_axis)

    # ====================================================================================================
    # Conversion

    def to_axis_angle(self):
        return Node("Rotation to Axis Angle", {'Rotation': self})

    def to_euler(self):
        return Node("Rotation to Euler", {'Rotation': self})._out

    def to_quaternion(self):
        return Node("Rotation to Quaternion", {'Rotation': self})

    # ====================================================================================================
    # Methods

    def mix(self, factor=None, other=None, clamp_factor=None):
        return Rotation(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='ROTATION'))

    # ----- Rotate vector

    def rotate_vector(self, vector=None):
        return Vector(Node('Rotate Vector', {'Vector': vector, 'Rotation': self})._out)

    # ----- Rotation

    def rotate(self, rotate_by=None, rotation_space='GLOBAL'):
        # rotation_space in ('GLOBAL', 'LOCAL')
        return Rotation(Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space=rotation_space)._out)

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

    # ====================================================================================================
    # Operations

    def __matmul__(self, other):
        data_type = utils.get_input_type(other, ['ROTATION', 'VECTOR'], ['VECTOR'])
        if data_type == 'ROTATION':
            return self.rotate_global(other)._lcop()
        else:
            return self.rotate_vector(other)._lcop()

    def __invert__(self):
        return self.invert()._lcop('~')


# =============================================================================================================================
# =============================================================================================================================
# Matrix
# =============================================================================================================================
# =============================================================================================================================

class Matrix(ValueSocket):

    SOCKET_TYPE = 'MATRIX'

    def __init__(self, value=None, name=None, tip=None):
        """ Matrix data socket ('MATRIX')

        A Matrix socket can be initialized with an array of size 16 (the shape is ignored)
        If the value is None, a 'Combine Matrix' with no input link is created.

        If the 'name' argument is not None, a group input is created, using value as default initialization

        ``` python
        import numpy as np

        input = Matrix(None, "My Matrix") # Group input to type 'Matrix' with name 'My Matrix' is created
        identity = Matrix() # Identity matrix
        matrix = Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]) # Node 'Combine Matrix' with an array 16 floats
        ```

        Arguments
        ---------
        - value (array of 16 Floats = None) : initialization values
        - name (str = None) : Create group input socket with this name if not None
        - type (str = None) : Input socket user tip if an input socket is created
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                if value is not None:
                    a = utils.value_to_array(value, (16,))
                    sockets = {i: a[i] for i in range(16)}
                else:
                    sockets = {}
                bsock = Node('Combine Matrix', sockets)._out
            else:
                bsock = Tree.new_input('NodeSocketMatrix', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Combine(cls,
                c1r1=1, c1r2=0, c1r3=0, c1r4=0,
                c2r1=0, c2r2=1, c2r3=0, c2r4=0,
                c3r1=0, c3r2=0, c3r3=1, c3r4=0,
                c4r1=0, c4r2=0, c4r3=0, c4r4=1):

            return Node('Combine Matrix', {
                 0: c1r1,  1: c1r2,  2: c1r3,  3: c1r4,
                 4: c1r1,  5: c1r2,  6: c1r3,  7: c1r4,
                 8: c1r1,  9: c1r2, 10: c1r3, 10: c1r4,
                12: c1r1, 13: c1r2, 14: c1r3, 15: c1r4,
                })._out

    @classmethod
    def FromArray(cls, array):
        a = utils.value_to_array(array, (16,))
        return Node('Combine Matrix', list(a))._out

    @classmethod
    def Transform(cls, translation=None, rotation=None, scale=None):
        return Node('Combine Transform', {'Translation': translation, 'Rotation': rotation, 'Scale': scale})._out

    # ====================================================================================================
    # Properties

    # ----- Array items

    @property
    def separate_matrix(self):
        return self._cache('Separate Matrix', {'Matrix': self})

    @property
    def c1r1(self):
        return self.separate_matrix[0]

    @property
    def c1r2(self):
        return self.separate_matrix[1]

    @property
    def c1r3(self):
        return self.separate_matrix[2]

    @property
    def c1r4(self):
        return self.separate_matrix[3]

    @property
    def c2r1(self):
        return self.separate_matrix[4]

    @property
    def c2r2(self):
        return self.separate_matrix[5]

    @property
    def c2r3(self):
        return self.separate_matrix[6]

    @property
    def c2r4(self):
        return self.separate_matrix[7]

    @property
    def c3r1(self):
        return self.separate_matrix[8]

    @property
    def c3r2(self):
        return self.separate_matrix[9]

    @property
    def c3r3(self):
        return self.separate_matrix[10]

    @property
    def c3r4(self):
        return self.separate_matrix[11]

    @property
    def c4r1(self):
        return self.separate_matrix[12]

    @property
    def c4r2(self):
        return self.separate_matrix[13]

    @property
    def c4r3(self):
        return self.separate_matrix[14]

    @property
    def c4r4(self):
        return self.separate_matrix[15]

    @property
    def array(self):
        node = self.separate_matrix
        return np.reshape(np.array([node[i] for i in range(16)], object), (4, 4))

    # ----- Components

    @property
    def separate_transform(self):
        return self._cache('Separate Transform', {'Transform': self})

    @property
    def translation(self):
        return self.separate_transform.translation

    @property
    def rotation(self):
        return self.separate_transform.rotation

    @property
    def scale(self):
        return self.separate_transform.scale

    # ====================================================================================================
    # Methods

    def transpose(self):
        return Node('Transpose Matrix', {'Matrix': self})._out

    def invert(self):
        matrix = Node('Invert Matrix', {'Matrix': self})._out
        matrix.invertible_ = matrix.node.invertible
        return matrix

    def multiply(self, other):
        return Node('Multiply Matrices', {0: self, 1: Matrix(other)})._out

    def transform_point(self, vector):
        return Node('Transform Point', {'Transform': self, 'Vector': vector})._out

    def project_point(self, vector):
        return Node('Project Point', {'Transform': self, 'Vector': vector})._out

    def transform_direction(self, vector):
        return Node('Transform Direction', {'Transform': self, 'Direction': vector})._out

    # ====================================================================================================
    # Operations

    def __invert__(self):
        return self.invert()

    def __matmul__(self, other):
        data_type = utils.get_input_type(other, ['MATRIX', 'VECTOR'], 'VECTOR')
        if data_type == 'MATRIX':
            return self.multiply(Matrix(other))._lcop()
        else:
            return self.transform_point(other)._lcop()
