#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

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
- Vector        : Socket of type 'VECTOR'
- Rotation      : Socket of type 'ROTATION'
- Matrix        : Socket of type 'MATRIX'

functions
---------

updates
-------
- creation : 2024/07/23
- update   : 2024/09/04
"""


from sys import version
import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socketclass import Attribute

# =============================================================================================================================
# =============================================================================================================================
# Base Vector, Rotation and Color
# =============================================================================================================================
# =============================================================================================================================

class VectorLike(Attribute):
    """
    $DOC hidden
    """

    ""

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
        # multiply add
        if isinstance(other, tuple) and len(other) == 2:
            return self._jump(self.math.multiply_add(self, other[0], other[1]))

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
    """
    $DOC hidden
    """


    def _reset(self):
        self._separate_xyz = None

    # ====================================================================================================
    # Properties

    @property
    def separate_xyz(self):
        """ > Node <&Separate XYZ"

        Returns
        -------
        - Node
        """
        if self._separate_xyz is None:
            self._separate_xyz = Node("Separate XYZ", {'Vector': self})
        return self._separate_xyz

    @property
    def x(self):
        """ Socket 'X' of node <&Separate XYZ>

        Returns
        -------
        - Float
        """
        return self.separate_xyz.x

    @property
    def y(self):
        """ Socket 'Y' of node <&Separate XYZ>

        Returns
        -------
        - Float
        """
        return self.separate_xyz.y

    @property
    def z(self):
        """ Socket 'Z' of node <&Separate XYZ>

        Returns
        -------
        - Float
        """
        return self.separate_xyz.z

    # ====================================================================================================
    # Constructors

    @classmethod
    def Combine(cls, x, y, z):
        """ Constructor node <&Combine XYZ>

        Returns
        -------
        - Vector
        """
        return cls(Node('Combine XYZ', [x, y, z])._out)

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        """ Constructor node <&Random Value>

        Returns
        -------
        - Vector
        """
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
        """ > Socket of type VECTOR

        If **value** argument is None:
        - if **name** argument is None, a node 'Vector' is added
        - otherwise a new group input is created using **tip** and **subtype**
          arguments

        If **value** argument is not None, a new **Vector** is created from the value:
        - using a <&Node Vector> node if the **value** is a float or a tuple of floats
        - using a <&Node Combine XYZ> node if the **value** is a tuple containing <!Socket"Sockets>

        ``` python
        vect = Vector()                    # 'Vector' node
        vect = Vector((1, 2, 3.14)).       # 'Vector' node
        vect = Vector((Float(1), 2, 3.14)) # 'Combine XYZ' node
        vect = Vector(name="User input").  # Create a new Vector group input
        ```

        Arguments
        ---------
        - value (tuple of floats or Sockets) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        - subtype (str = None) : sub type for group input
        """
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
        """ > Translation group input

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, subtype='TRANSLATION')

    @classmethod
    def Direction(cls, value=(0., 0., 0.), name='Direction', tip=None):
        """ > Direction group input

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, subtype='DIRECTION')

    @classmethod
    def Velocity(cls, value=(0., 0., 0.), name='Velocity', tip=None):
        """ > Velocity group input

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, subtype='VELOCITY')

    @classmethod
    def Acceleration(cls, value=(0., 0., 0.), name='Acceleration', tip=None):
        """ > Acceleration group input

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, subtype='ACCELERATION')

    @classmethod
    def Euler(cls, value=(0., 0., 0.), name='Euler', tip=None):
        """ > Euler group input

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, subtype='EULER')

    @classmethod
    def XYZ(cls, value=(0., 0., 0.), name='XYZ', tip=None):
        """ > XYZ group input

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, subtype='XYZ')

    @classmethod
    def FromRotation(cls, rotation=None):
        """ > Constructor node <&Rotation to Euler>

        Returns
        -------
        - Vector
        """
        return Rotation(rotation).to_euler()

    # ====================================================================================================
    # Conversion

    def to_rotation(self):
        """ Node <&Euler to Rotation>

        Returns
        -------
        - Rotation
        """
        return Rotation.FromEuler(self)

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_factor=None, factor_mode=None):
        """ > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float = None) : socket 'Factor'
        - other (Vector = None) : socket 'B'
        - clamp_factor (bool = None) : clamp_factor parameter
        - factor_mode (str in 'UNIFORM', 'NON_UNIFORM')

        Returns
        -------
        - Vector
        """
        return Vector(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, factor_mode=factor_mode, data_type='VECTOR')._out)

    def mix_uniform(self, factor=None, other=None, clamp_factor=None):
        """ > Node <&Node Mix>, factor_mode = 'UNIFORM'

        Arguments
        ---------
        - factor (Float = None) : socket 'Factor'
        - other (Vector = None) : socket 'B'
        - clamp_factor (bool = None) : clamp_factor parameter

        Returns
        -------
        - Vector
        """
        return self.mix(factor, other, clamp_factor, factor_mode='UNIFORM')

    def mix_non_uniform(self, factor=None, other=None, clamp_factor=None):
        """ > Node <&Node Mix>, factor_mode = 'NON_UNIFORM'

        Arguments
        ---------
        - factor (Float = None) : socket 'Factor'
        - other (Vector = None) : socket 'B'
        - clamp_factor (bool = None) : clamp_factor parameter

        Returns
        -------
        - Vector
        """
        return self.mix(factor, other, clamp_factor, factor_mode='NON_UNIFORM')

    # ----- Rotation

    def vector_rotate(self, center=None, axis=None, angle=None, rotation=None, invert=None, rotation_type=None):
        """ > Node <&Node Vector Rotate>

        Arguments
        ---------
        - center (Vector) : socket 'Center' (Center)
        - axis (Vector) : socket 'Axis' (Axis)
        - angle (Float) : socket 'Angle' (Angle)
        - rotation (Vector) : socket 'Rotation' (Rotation)
        - invert (bool): Node.invert
        - rotation_type (str): Node.rotation_type in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')

        Returns
        -------
        - Vector
        """
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle, 'Rotation': rotation},
            invert=invert, rotation_type=rotation_type)._out)

    def rotate_axis(self, center=None, axis=None, angle=None, invert=None):
        """ > Node <&Node Vector Rotate>, rotation_type = 'AXIS_ANGLE'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (Center)
        - axis (Vector) : socket 'Axis' (Axis)
        - angle (Float) : socket 'Angle' (Angle)
        - invert (bool): Node.invert

        Returns
        -------
        - Vector
        """
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Axis': axis, 'Angle': angle},
            invert=invert, rotation_type='AXIS_ANGLE')._out)

    def rotate_x(self, center=None, angle=None, invert=None):
        """ > Node <&Node Vector Rotate>, rotation_type = 'X_AXIS'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (Center)
        - angle (Float) : socket 'Angle' (Angle)
        - invert (bool): Node.invert

        Returns
        -------
        - Vector
        """
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle},
            invert=invert, rotation_type='X_AXIS')._out)

    def rotate_y(self, center=None, angle=None, invert=None):
        """ > Node <&Node Vector Rotate>, rotation_type = 'Y_AXIS'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (Center)
        - angle (Float) : socket 'Angle' (Angle)
        - invert (bool): Node.invert

        Returns
        -------
        - Vector
        """
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle},
            invert=invert, rotation_type='Y_AXIS')._out)

    def rotate_z(self, center=None, angle=None, invert=None):
        """ > Node <&Node Vector Rotate>, rotation_type = 'Z_AXIS'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (Center)
        - angle (Float) : socket 'Angle' (Angle)
        - invert (bool): Node.invert

        Returns
        -------
        - Vector
        """
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Angle': angle},
            invert=invert, rotation_type='Z_AXIS')._out)

    def rotate_euler(self, center=None, rotation=None, invert=None):
        """ > Node <&Node Vector Rotate>, rotation_type = 'EULER_XYZ'

        Arguments
        ---------
        - center (Vector) : socket 'Center' (Center)
        - rotation (Vector) : socket 'Rotation' (Rotation)
        - invert (bool): Node.invert

        Returns
        -------
        - Vector
        """
        return Vector(Node('Vector Rotate', {'Vector': self, 'Center': center, 'Rotation': rotation},
            invert=invert, rotation_type='EULER_XYZ')._out)

    def rotate(self, rotation=None):
        """ > Node <&Node Rotate Vector>

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Vector
        """
        return Vector(Node('Rotate Vector', {'Vector': self, 'Rotation': rotation})._out)

    # ----- Geometry

    def index_of_nearest(self, group_id=None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)

        Returns
        -------
        - Integer
        """
        return Node('Index of Nearest', {'Position': self, 'Group ID': group_id})._out

    # ====================================================================================================
    # Shader

    def out(self, name=None):
        """ > Plug the Vector to the group output

        [!MIX]

        > [!NOTE]
        > - <!GeoNodes> : the Vector is plug as group output
        > - <!ShaderNodes> : if **name** argument is None, the vecteur is plugged
        >.  into the `Displacement` socket of <&ShaderNode &Material Output>,
        >   otherwise it is plugged to a <&ShaderNode AOV Output> node.

        """
        if self._tree._btree.bl_idname == 'ShaderNodeTree' and not self._tree._is_group:
            if name is None:
                self._tree.set_displacement(self)
            else:
                self._tree.aov_output(name=name, color=self)
        else:
            super().out(name=name)

    def displacement_out(self, target='ALL'):
        """ > Plug the value to 'Displacement' socket of <&ShaderNode Material Output> node

        [!SHADER]
        """
        self._tree.set_displacement(self, target=target)


    @classmethod
    def Tangent(cls, axis='Z', direction_type='RADIAL', uv_map=''):
        """ > Node <&ShaderNode Tangent>

        [!SHADER]

        Arguments
        ---------
        - axis (str): Node.axis in ('X', 'Y', 'Z')
        - direction_type (str): Node.direction_type in ('RADIAL', 'UV_MAP')
        - uv_map (str): Node.uv_map

        Returns
        -------
        - Vector
        """
        node = Node('Tangent', axis=axis, direction_type=direction_type, uv_map=uv_map)
        return node._out

    @classmethod
    def UVMap(cls, uv_map='', from_instancer=False):
        """ > Node <&ShaderNode UV Map>

        [!SHADER]

        Arguments
        ---------
        - uv_map (str): Node.uv_map
        - from_instancer (bool): Node.from_instancer

        Returns
        -------
        - Vector
        """
        node = Node('UV Map', from_instancer=from_instancer, uv_map=uv_map)
        return node._out

    # ----- Vector

    def bump(self, strength=None, distance=None, height=None, invert=False):
        """ > Node <&ShaderNode Bump>

        [!SHADER]

        > [!NOTE]
        > Self Vector is plugged to 'Normal' socket

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (Strength)
        - distance (Float) : socket 'Distance' (Distance)
        - height (Float) : socket 'Height' (Height)
        - invert (bool): Node.invert

        Returns
        -------
        - Vector
        """
        node = Node('Bump', {'Strength': strength, 'Distance': distance, 'Height': height, 'Normal': self}, invert=invert)
        return node._out

    def displacement(self, height=None, midlevel=None, scale=None, space='OBJECT'):
        """ > Node <&ShaderNode Displacement>

        [!SHADER]

        > [!NOTE]
        > Self Vector is plugged to 'Normal' socket

        Arguments
        ---------
        - height (Float) : socket 'Height' (Height)
        - midlevel (Float) : socket 'Midlevel' (Midlevel)
        - scale (Float) : socket 'Scale' (Scale)
        - space (str): Node.space in ('OBJECT', 'WORLD')

        Returns
        -------
        - Vector
        """
        node = Node('Displacement', {'Height': height, 'Midlevel': midlevel, 'Scale': scale, 'Normal': self}, space=space)
        return node._out

    def mapping(self, location=None, rotation=None, scale=None, vector_type='POINT'):
        """ > Node <&ShaderNode Mapping>

        [!SHADER]

        Arguments
        ---------
        - location (Vector) : socket 'Location' (Location)
        - rotation (Vector) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)
        - vector_type (str): Node.vector_type in ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL')

        Returns
        -------
        - Vector
        """
        node = Node('Mapping', {'Vector': self, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    def normal(self):
        """ > Node <&ShaderNode Normal>

        [!SHADER]

        Returns
        -------
        - Vector
        """
        node = Node('Normal', {'Normal': self})
        vect = node._out
        vect._bsocket.default_value = normal
        return vect

    @classmethod
    def NormalMap(cls, strength=None, color=None, space='TANGENT', uv_map=''):
        """ > Constructor node <&ShaderNode Normal Map>

        [!SHADER]

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (Strength)
        - color (Color) : socket 'Color' (Color)
        - space (str): Node.space in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
        - uv_map (str): Node.uv_map

        Returns
        -------
        - Vector
        """
        node = Node('Normal Map', {'Strength': strength, 'Color': color}, space=space, uv_map=uv_map)
        return node._out

    def vector_displacement(self, midlevel=None, scale=None, space='TANGENT'):
        """ > Node <&ShaderNode Vector Displacement>

        [!SHADER]

        Arguments
        ---------
        - midlevel (Float) : socket 'Midlevel' (Midlevel)
        - scale (Float) : socket 'Scale' (Scale)
        - space (str): Node.space in ('TANGENT', 'OBJECT', 'WORLD')

        Returns
        -------
        - Vector
        """
        node = Node('Vector Displacement', {'Vector': self, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out

    def transform(self, convert_from='WORLD', convert_to='OBJECT', vector_type='NORMAL'):
        """ > Node <&ShaderNode Vector Transform>

        [!SHADER]

        Arguments
        ---------
        - convert_from (str): Node.convert_from in ('WORLD', 'OBJECT', 'CAMERA')
        - convert_to (str): Node.convert_to in ('WORLD', 'OBJECT', 'CAMERA')
        - vector_type (str): Node.vector_type in ('POINT', 'VECTOR', 'NORMAL')

        Returns
        -------
        - Vector
        """
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
        """ > Socket of type ROTATION

        If **value** argument is None:
        - if **name** argument is None, a node <&Node Rotation> is added
        - otherwise a new group input is created using **tip** argument.

        If **value** argument is not None, a new **Rotation** is created from the value:
        - using a <&Node Rotation> node if the **value** is a float or a tuple of floats
        - using <&Node Combine XYZ> and <&Node Euler to Rotation> nodes if the **value**
          is a tuple containing <!Socket"Sockets>

        ``` python
        rot = Rotation()                    # 'Rotation' node
        rot = Rotation((1, 2, 3.14)).       # 'Rotation' node
        rot = Rotation((Float(1), 2, 3.14)) # 'Combine XYZ' + 'Euler to Rotation' nodes
        rot = Rotation(name="User input").  # Create a new Rotation group input
        ```

        Arguments
        ---------
        - value (tuple of floats or Sockets) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                a = utils.value_to_array(value, (3,))
                if utils.has_bsocket(a):
                    bsock = Vector(value).to_rotation()
                    #bsock = Node('Combine XYZ', {0: a[0], 1: a[1], 2:a[2]})._out
                else:
                    bsock = Node('Rotation', rotation_euler=value)._out
            else:
                bsock = Tree.new_input('NodeSocketRotation', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def AxesToRotation(cls, primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X'):
        """ > Constructor node <&Node Axes to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#FromAxes> constructor
        > See also <#FromXYAxes>, <#FromYXAxes>, <#FromXZAxes>, <#FromZXAxes>, <#FromYZAxes>, <#FromZYAxes>,

        > [!NOTE]
        > In the node <*Node Axes to Rotation>, the parameter names is the **snake_case** version
        > of the sockets (primary_target and 'Primary Target').
        > It is why, the corresponding arguments are renamed into **primary_align** and **secondary_align**.

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (Secondary Axis)
        - primary_align (str): Node.primary_axis in ('X', 'Y', 'Z')
        - secondary_align (str): Node.secondary_axis in ('X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis=primary_align, secondary_axis=secondary_align)._out

    @classmethod
    def FromAxes(cls, primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X'):
        """ > Constructor node <&Node Axes to Rotation>

        > [!NOTE]
        > This constructor is synonym of <#AxesToRotation> constructor
        > See also <#FromXYAxes>, <#FromYXAxes>, <#FromXZAxes>, <#FromZXAxes>, <#FromYZAxes>, <#FromZYAxes>,

        > [!NOTE]
        > In the node <*Node Axes to Rotation>, the parameter names is the **snake_case** version
        > of the sockets (primary_target and 'Primary Target').
        > It is why, the corresponding arguments are renamed into **primary_align** and **secondary_align**.

        Arguments
        ---------
        - primary_axis (Vector) : socket 'Primary Axis' (Primary Axis)
        - secondary_axis (Vector) : socket 'Secondary Axis' (Secondary Axis)
        - primary_align (str): Node.primary_axis in ('X', 'Y', 'Z')
        - secondary_align (str): Node.secondary_axis in ('X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return Node('Axes to Rotation', {'Primary Axis': primary_axis, 'Secondary Axis': secondary_axis}, primary_axis=primary_align, secondary_axis=secondary_align)._out


    @classmethod
    def FromXYAxes(cls, primary_axis=None, secondary_axis=None):
        """ > Constructor node <&Node Axes to Rotation>, with XY alignment

        Arguments
        ---------
        - primary_axis (Vector) : axis aligned with X
        - secondary_axis (Vector) : axis aligned with Y

        Returns
        -------
        - Rotation
        """
        return cls.AxesToRotation(primary_axis=primary_axis, secondary_axis=secondary_axis,
            primary_align='X', secondary_align='Y')

    @classmethod
    def FromYXAxes(cls, primary_axis=None, secondary_axis=None):
        """ > Constructor node <&Node Axes to Rotation>, with YX alignment

        Arguments
        ---------
        - primary_axis (Vector) : axis aligned with Y
        - secondary_axis (Vector) : axis aligned with X

        Returns
        -------
        - Rotation
        """
        return cls.AxesToRotation(primary_axis=primary_axis, secondary_axis=secondary_axis,
            primary_align='Y', secondary_align='X')

    @classmethod
    def FromXZAxes(cls, primary_axis=None, secondary_axis=None):
        """ > Constructor node <&Node Axes to Rotation>, with XZ alignment

        Arguments
        ---------
        - primary_axis (Vector) : axis aligned with X
        - secondary_axis (Vector) : axis aligned with Z

        Returns
        -------
        - Rotation
        """
        return cls.AxesToRotation(primary_axis=primary_axis, secondary_axis=secondary_axis,
            primary_align='X', secondary_align='Z')

    @classmethod
    def FromZXAxes(cls, primary_axis=None, secondary_axis=None):
        """ > Constructor node <&Node Axes to Rotation>, with ZX alignment

        Arguments
        ---------
        - primary_axis (Vector) : axis aligned with Z
        - secondary_axis (Vector) : axis aligned with X

        Returns
        -------
        - Rotation
        """
        return cls.AxesToRotation(primary_axis=primary_axis, secondary_axis=secondary_axis,
            primary_align='Z', secondary_align='X')

    @classmethod
    def FromYZAxes(cls, primary_axis=None, secondary_axis=None):
        """ > Constructor node <&Node Axes to Rotation>, with YZ alignment

        Arguments
        ---------
        - primary_axis (Vector) : axis aligned with Y
        - secondary_axis (Vector) : axis aligned with Z

        Returns
        -------
        - Rotation
        """
        return cls.AxesToRotation(primary_axis=primary_axis, secondary_axis=secondary_axis,
            primary_align='Y', secondary_align='Z')

    @classmethod
    def FromZYAxes(cls, primary_axis=None, secondary_axis=None):
        """ > Constructor node <&Node Axes to Rotation>, with ZY alignment

        Arguments
        ---------
        - primary_axis (Vector) : axis aligned with Z
        - secondary_axis (Vector) : axis aligned with Y

        Returns
        -------
        - Rotation
        """
        return cls.AxesToRotation(primary_axis=primary_axis, secondary_axis=secondary_axis,
            primary_align='Z', secondary_align='Y')

    @classmethod
    def AxisAngleToRotation(cls, axis=(0, 0, 1), angle=0):
        """ > Node <&Node Axis Angle to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#FromAxisAngle> constructor

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (Axis)
        - angle (Float) : socket 'Angle' (Angle)

        Returns
        -------
        - Rotation
        """
        return Node('Axis Angle to Rotation', {'Axis': axis, 'Angle': angle})._out

    @classmethod
    def FromAxisAngle(cls, axis=(0, 0, 1), angle=0):
        """ > Node <&Node Axis Angle to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#AxisAngleToRotation> constructor

        Arguments
        ---------
        - axis (Vector) : socket 'Axis' (Axis)
        - angle (Float) : socket 'Angle' (Angle)

        Returns
        -------
        - Rotation
        """
        return cls.AxisAngleToRotation(axis, angle)

    @classmethod
    def EulerToRotation(cls, euler=(0, 0, 0)):
        """ > Node <&Node Euler to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#FromEuler> constructor

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (Euler)

        Returns
        -------
        - Rotation
        """
        return Node('Euler to Rotation', {'Euler': euler})._out

    @classmethod
    def FromEuler(cls, euler=(0, 0, 0)):
        """ > Node <&Node Euler to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#EulerToRotation> constructor

        Arguments
        ---------
        - euler (Vector) : socket 'Euler' (Euler)

        Returns
        -------
        - Rotation
        """
        return cls.EulerToRotation(euler)

    @classmethod
    def QuaternionToRotation(cls, w=0, x=0, y=0, z=0):
        """ > Node <&Node Quaternion to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#FromQuaternion> constructor

        Arguments
        ---------
        - w (Float) : socket 'W' (W)
        - x (Float) : socket 'X' (X)
        - y (Float) : socket 'Y' (Y)
        - z (Float) : socket 'Z' (Z)

        Returns
        -------
        - Rotation
        """
        return Node('Quaternion to Rotation', {'W': w, 'X': x, 'Y': y, 'Z': z})._out

    @classmethod
    def FromQuaternion(cls, w=0, x=0, y=0, z=0):
        """ > Node <&Node Quaternion to Rotation>

        > [!NOTE]
        > This constructor is homonym of <#QuaternionToRotation> constructor

        Arguments
        ---------
        - w (Float) : socket 'W' (W)
        - x (Float) : socket 'X' (X)
        - y (Float) : socket 'Y' (Y)
        - z (Float) : socket 'Z' (Z)

        Returns
        -------
        - Rotation
        """
        return cls.QuaternionToRotation(w, x, y, z)

    @classmethod
    def AlignToVector(cls, vector=None, factor=None, axis='Z', pivot_axis='AUTO'):
        """ > Constructor node <&Node Align Rotation to Vector>

        > [!NOTE]
        > This constructor creates a <*Node Align Rotation to Vector> node without
        > connecting the 'Rotation' input socket. To align a **Rotation** other than
        > **Identity** uses method <#align_to_vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - factor (Float) : socket 'Factor' (Factor)
        - axis (str): Node.axis in ('X', 'Y', 'Z')
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return Node('Align Rotation to Vector', {'Factor': factor, 'Vector': vector},
            axis=axis, pivot_axis=pivot_axis)._out

    @classmethod
    def AlignXToVector(cls, vector=None, factor=None, pivot_axis=None):
        """ > Constructor node <&Node Align Rotation to Vector>, axis = X

        > [!NOTE]
        > This constructor creates a <*Node Align Rotation to Vector> node without
        > connecting the 'Rotation' input socket. To align a **Rotation** other than
        > **Identity** uses method <#align_x_to_vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - factor (Float) : socket 'Factor' (Factor)
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return cls.AlignToVector(vector, factor, axis='X', pivot_axis=pivot_axis)

    @classmethod
    def AlignYToVector(cls, vector=None, factor=None, pivot_axis=None):
        """ > Constructor node <&Node Align Rotation to Vector>, axis = Y

        > [!NOTE]
        > This constructor creates a <*Node Align Rotation to Vector> node without
        > connecting the 'Rotation' input socket. To align a **Rotation** other than
        > **Identity** uses method <#align_y_to_vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - factor (Float) : socket 'Factor' (Factor)
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return cls.AlignToVector(vector, factor, axis='Y', pivot_axis=pivot_axis)

    @classmethod
    def AlignZToVector(cls, vector=None, factor=None, pivot_axis=None):
        """ > Constructor node <&Node Align Rotation to Vector>, axis = Z

        > [!NOTE]
        > This constructor creates a <*Node Align Rotation to Vector> node without
        > connecting the 'Rotation' input socket. To align a **Rotation** other than
        > **Identity** uses method <#align_z_to_vector>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - factor (Float) : socket 'Factor' (Factor)
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return cls.AlignToVector(vector, factor, axis='Z', pivot_axis=pivot_axis)

    # ====================================================================================================
    # Conversion

    def to_axis_angle(self):
        """ > Node <&Node Rotation to Axis Angle>

        > [!NOTE]
        > The method returns the <!Vector>. To get the angle, you can use
        > the **peer socket** naming :

        ``` python
        vect = rotation.to_axis_angle()
        angle = vect.angle_ # equivalent to vect.node.angle
        ```

        Returns
        -------
        - Vector
        """
        return Node("Rotation to Axis Angle", {'Rotation': self})._out

    def to_euler(self):
        """ > Node <&Node Rotation to Euler>

        Returns
        -------
        - Vector
        """
        return Node("Rotation to Euler", {'Rotation': self})._out

    def to_quaternion(self):
        """ > Node <&Node Rotation to Quaternion>

        > [!CAUTION]
        > By exception, this method returns the node, not the first output socket

        ``` python
        quat = rotation.to_quaternion()
        w = quat.w
        x = quat.x
        y = quat.y
        z = quat.z
        ```

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)

        Returns
        -------
        - Node : node with **w**, **x**, **y** and **z** properties
        """
        return Node("Rotation to Quaternion", {'Rotation': self})

    # ====================================================================================================
    # Methods

    def mix(self, factor=None, other=None, clamp_factor=None):
        """ > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor_Float)
        - other (Rotation) : socket 'B' (B_Float)
        - clamp_factor (bool): Node.clamp_factor

        Returns
        -------
        - Rotation
        """
        return Rotation(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='ROTATION')._out)

    # ----- Rotate vector

    def rotate_vector(self, vector=None):
        """ > Node <&Node Rotate Vector>

        > [!NOTE]
        > Operator **@** can be used as an alternative

        ``` python
        # Rotate vector v
        w = rotation.rotate_vector(v)

        # or
        w = rotation @ v
        ```

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)

        Returns
        -------
        - Vector
        """
        return Vector(Node('Rotate Vector', {'Vector': vector, 'Rotation': self})._out)

    # ----- Rotation

    def rotate(self, rotate_by=None, rotation_space='GLOBAL'):
        """ > Node <&Node Rotate Rotation>

        > See also <#rotate_local> and <#rotate_global>

        Arguments
        ---------
        - rotate_by (Rotation) : socket 'Rotate By' (Rotate By)
        - rotation_space (str): Node.rotation_space in ('GLOBAL', 'LOCAL')

        Returns
        -------
        - Rotation
        """
        return Rotation(Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space=rotation_space)._out)

    def rotate_local(self, rotate_by=None):
        """ > Node <&Node Rotate Rotation>, rotation_space='LOCAL'

        Arguments
        ---------
        - rotate_by (Rotation) : socket 'Rotate By' (Rotate By)

        Returns
        -------
        - Rotation
        """
        return Rotation(Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space='LOCAL')._out)

    def rotate_global(self, rotate_by=None):
        """ > Node <&Node Rotate Rotation>, rotation_space='GLOBAL'

        > [!NOTE]
        > Operator **@** can be used as an alternative

        ``` python
        # Rotate rotation r
        s = rotation.rotate_global(r)

        # or
        s = rotation @ r
        ```

        Arguments
        ---------
        - rotate_by (Rotation) : socket 'Rotate By' (Rotate By)

        Returns
        -------
        - Rotation
        """
        return Rotation(Node('Rotate Rotation', {'Rotation': self, 'Rotate By': rotate_by}, rotation_space='GLOBAL')._out)

    # ----- Align to vector

    def align_to_vector(self, vector=None, factor=None, axis='Z', pivot_axis='AUTO'):
        """ > Node <&Node Align Rotation to Vector>

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor)
        - vector (Vector) : socket 'Vector' (Vector)
        - axis (str): Node.axis in ('X', 'Y', 'Z')
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return Rotation(Node('Align Rotation to Vector', {'Rotation': self, 'Factor': factor, 'Vector': vector},
            axis=axis, pivot_axis=pivot_axis)._out)

    def align_x_to_vector(self, vector=None, factor=None, pivot_axis=None):
        """ > Node <&Node Align Rotation to Vector>, axis = 'X'

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor)
        - vector (Vector) : socket 'Vector' (Vector)
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return self.align_to_vector(vector, factor, axis='X', pivot_axis=pivot_axis)

    def align_y_to_vector(self, vector=None, factor=None, pivot_axis=None):
        """ > Node <&Node Align Rotation to Vector>, axis = 'Y'

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor)
        - vector (Vector) : socket 'Vector' (Vector)
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return self.align_to_vector(vector, factor, axis='Y', pivot_axis=pivot_axis)

    def align_z_to_vector(self, vector=None, factor=None, pivot_axis=None):
        """ > Node <&Node Align Rotation to Vector>, axis = 'Z'

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor)
        - vector (Vector) : socket 'Vector' (Vector)
        - pivot_axis (str): Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')

        Returns
        -------
        - Rotation
        """
        return self.align_to_vector(vector, factor, axis='Z', pivot_axis=pivot_axis)

    # ----- Invert

    def invert(self):
        """ > Node <&Node Invert Rotation>

        Returns
        -------
        - Rotation
        """
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

class Matrix(Attribute):

    SOCKET_TYPE = 'MATRIX'

    def __init__(self, value=None, name=None, tip=None):
        """ Matrix data socket ('MATRIX')

        A Matrix socket can be initialized with an array of size 16 (the shape is ignored)
        If **value** is None, a <&Node Combine Matrix> with no input link is created.

        If **name** argument is not None, a group input is created, using value as default initialization

        ``` python
        input = Matrix(None, "My Matrix") # Group input of type 'Matrix' with name 'My Matrix' is created
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
        """ > Constructor node <&Node Combine Matrix>

        Arguments
        ---------
        - c1r1 (Float) : socket 'Column 1 Row 1' (Column 1 Row 1)
        - c1r2 (Float) : socket 'Column 1 Row 2' (Column 1 Row 2)
        - c1r3 (Float) : socket 'Column 1 Row 3' (Column 1 Row 3)
        - c1r4 (Float) : socket 'Column 1 Row 4' (Column 1 Row 4)
        - c2r1 (Float) : socket 'Column 2 Row 1' (Column 2 Row 1)
        - c2r2 (Float) : socket 'Column 2 Row 2' (Column 2 Row 2)
        - c2r3 (Float) : socket 'Column 2 Row 3' (Column 2 Row 3)
        - c2r4 (Float) : socket 'Column 2 Row 4' (Column 2 Row 4)
        - c3r1 (Float) : socket 'Column 3 Row 1' (Column 3 Row 1)
        - c3r2 (Float) : socket 'Column 3 Row 2' (Column 3 Row 2)
        - c3r3 (Float) : socket 'Column 3 Row 3' (Column 3 Row 3)
        - c3r4 (Float) : socket 'Column 3 Row 4' (Column 3 Row 4)
        - c4r1 (Float) : socket 'Column 4 Row 1' (Column 4 Row 1)
        - c4r2 (Float) : socket 'Column 4 Row 2' (Column 4 Row 2)
        - c4r3 (Float) : socket 'Column 4 Row 3' (Column 4 Row 3)
        - c4r4 (Float) : socket 'Column 4 Row 4' (Column 4 Row 4)

        Returns
        -------
        - Matrix
        """
        return Node('Combine Matrix', {
                0: c1r1,  1: c1r2,  2: c1r3,  3: c1r4,
                4: c1r1,  5: c1r2,  6: c1r3,  7: c1r4,
                8: c1r1,  9: c1r2, 10: c1r3, 10: c1r4,
            12: c1r1, 13: c1r2, 14: c1r3, 15: c1r4,
            })._out

    @classmethod
    def FromArray(cls, array):
        """ > Constructor node <&Node Combine Matrix>

        Arguments
        ---------
        - array (array of size 16) : 16 values to use as matrix components

        Returns
        -------
        - Matrix
        """
        a = utils.value_to_array(array, (16,))
        return Node('Combine Matrix', list(a))._out

    @classmethod
    def Transform(cls, translation=None, rotation=None, scale=None):
        """ > Constructor node <&Node Combine Transform>

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)

        Returns
        -------
        - Matrix
        """
        return Node('Combine Transform', {'Translation': translation, 'Rotation': rotation, 'Scale': scale})._out

    # ====================================================================================================
    # Properties

    # ----- Array items

    @property
    def separate_matrix(self):
        """ > Node <&Node Separate Matrix>

        > [!CAUTION]
        > By exception, this method returns the node, not the first output socket

        Returns
        -------
        - Node
        """
        return self._cache('Separate Matrix', {'Matrix': self})

    @property
    def c1r1(self):
        """ > Node <&Node Separate Matrix>, column 1 row 1

        Returns
        -------
        - Float
        """
        return self.separate_matrix[0]

    @property
    def c1r2(self):
        """ > Node <&Node Separate Matrix>, column 1 row 2

        Returns
        -------
        - Float
        """
        return self.separate_matrix[1]

    @property
    def c1r3(self):
        """ > Node <&Node Separate Matrix>, column 1 row 3

        Returns
        -------
        - Float
        """
        return self.separate_matrix[2]

    @property
    def c1r4(self):
        """ > Node <&Node Separate Matrix>, column 1 row 4

        Returns
        -------
        - Float
        """
        return self.separate_matrix[3]

    @property
    def c2r1(self):
        """ > Node <&Node Separate Matrix>, column 2 row 1

        Returns
        -------
        - Float
        """
        return self.separate_matrix[4]

    @property
    def c2r2(self):
        """ > Node <&Node Separate Matrix>, column 2 row 2

        Returns
        -------
        - Float
        """
        return self.separate_matrix[5]

    @property
    def c2r3(self):
        """ > Node <&Node Separate Matrix>, column 2 row 3

        Returns
        -------
        - Float
        """
        return self.separate_matrix[6]

    @property
    def c2r4(self):
        """ > Node <&Node Separate Matrix>, column 2 row 4

        Returns
        -------
        - Float
        """
        return self.separate_matrix[7]

    @property
    def c3r1(self):
        """ > Node <&Node Separate Matrix>, column 3 row 1

        Returns
        -------
        - Float
        """
        return self.separate_matrix[8]

    @property
    def c3r2(self):
        """ > Node <&Node Separate Matrix>, column 3 row 2

        Returns
        -------
        - Float
        """
        return self.separate_matrix[9]

    @property
    def c3r3(self):
        """ > Node <&Node Separate Matrix>, column 3 row 3

        Returns
        -------
        - Float
        """
        return self.separate_matrix[10]

    @property
    def c3r4(self):
        """ > Node <&Node Separate Matrix>, column 3 row 4

        Returns
        -------
        - Float
        """
        return self.separate_matrix[11]

    @property
    def c4r1(self):
        """ > Node <&Node Separate Matrix>, column 4 row 1

        Returns
        -------
        - Float
        """
        return self.separate_matrix[12]

    @property
    def c4r2(self):
        """ > Node <&Node Separate Matrix>, column 4 row 2

        Returns
        -------
        - Float
        """
        return self.separate_matrix[13]

    @property
    def c4r3(self):
        """ > Node <&Node Separate Matrix>, column 4 row 3

        Returns
        -------
        - Float
        """
        return self.separate_matrix[14]

    @property
    def c4r4(self):
        """ > Node <&Node Separate Matrix>, column 4 row 4

        Returns
        -------
        - Float
        """
        return self.separate_matrix[15]

    @property
    def array(self):
        """ > Node <&Node Separate Matrix> as a numpy array shaped (4, 4)

        Returns
        -------
        - numpy ndarray
        """
        node = self.separate_matrix
        return np.reshape(np.array([node[i] for i in range(16)], object), (4, 4))

    # ----- Components

    @property
    def separate_transform(self):
        """ > Node <&Node Separate Transform>

        > [!CAUTION]
        > By exception, this property returns the node, not the first output socket

        Returns
        -------
        - Node
        """
        return self._cache('Separate Transform', {'Transform': self})

    @property
    def translation(self):
        """ > Socket 'Translation' of node <&Node Separate Transform>

        Returns
        -------
        - Vector
        """
        return self.separate_transform.translation

    @property
    def rotation(self):
        """ > Socket 'Rotation' of node <&Node Separate Transform>

        Returns
        -------
        - Rotation
        """
        return self.separate_transform.rotation

    @property
    def scale(self):
        """ > Socket 'Scale' of node <&Node Separate Transform>

        Returns
        -------
        - Vector
        """
        return self.separate_transform.scale

    @property
    def determinant(self):
        """ > Node <&Node Matrix Determinant>

        Arguments
        ---------
        - matrix (Matrix) : socket 'Matrix' (Matrix)

        Returns
        -------
        - Float
        """
        return Node('Matrix Determinant', {'Matrix': self})._out

    def transform_gizmo(self, position=None, rotation=None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True):
        """ > Node <&Node Transform Gizmo>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - use_rotation_x (bool): Node.use_rotation_x
        - use_rotation_y (bool): Node.use_rotation_y
        - use_rotation_z (bool): Node.use_rotation_z
        - use_scale_x (bool): Node.use_scale_x
        - use_scale_y (bool): Node.use_scale_y
        - use_scale_z (bool): Node.use_scale_z
        - use_translation_x (bool): Node.use_translation_x
        - use_translation_y (bool): Node.use_translation_y
        - use_translation_z (bool): Node.use_translation_z

        Returns
        -------
        - Gizmo Node
        """
        from geonodes import Gizmo

        return Gizmo.Transform(self, position=position, rotation=rotation,
            use_rotation_x   =use_rotation_x,    use_rotation_y   =use_rotation_y,    use_rotation_z   =use_rotation_z,
            use_scale_x      =use_scale_x,       use_scale_y      =use_scale_y,       use_scale_z      =use_scale_z,
            use_translation_x=use_translation_x, use_translation_y=use_translation_y, use_translation_z=use_translation_z)

    # ====================================================================================================
    # Methods

    def transpose(self):
        """ > Node <&Node Transpose Matrix>

        Returns
        -------
        - Matrix
        """
        return Node('Transpose Matrix', {'Matrix': self})._out

    def invert(self):
        """ > Node <&Node Invert Matrix>

        Returns
        -------
        - Matrix
        """
        matrix = Node('Invert Matrix', {'Matrix': self})._out
        matrix.invertible_ = matrix.node.invertible
        return matrix

    def multiply(self, other):
        """ > Node <&Node Multiply Matrices>

        > [!NOTE]
        > Operator **@** can be used as an alternative

        ``` python
        # Multiply to matrices
        mat3 = mat0.multiply(mat1)

        # or
        mat3 = mat0 @ mat1
        ```

        Arguments
        ---------
        - other (Matrix) : socket 'Matrix' (Matrix_001)

        Returns
        -------
        - Matrix
        """
        return Node('Multiply Matrices', {0: self, 1: Matrix(other)})._out

    def transform_point(self, vector):
        """ > Node <&Node Transform Point>

        > [!NOTE]
        > Operator **@** can be used as an alternative

        ``` python
        # Transform a point
        Q = mat.transform_point(P)

        # or
        Q = mat @ P
        ```

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)

        Returns
        -------
        - Vector
        """
        return Node('Transform Point', {'Transform': self, 'Vector': vector})._out

    def project_point(self, vector):
        """ > Node <&Node Project Point>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)

        Returns
        -------
        - Vector
        """
        return Node('Project Point', {'Transform': self, 'Vector': vector})._out

    def transform_direction(self, vector):
        """ > Node <&Node Transform Direction>

        Arguments
        ---------
        - direction (Vector) : socket 'Direction' (Direction)

        Returns
        -------
        - Vector
        """
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
