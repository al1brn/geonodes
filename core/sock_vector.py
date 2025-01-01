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
- update   : 2024/&2/29
"""

from sys import version
import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socket_class import Socket
from . import generated


class Vector(generated.Vector):

    SOCKET_TYPE = 'VECTOR'

    def __init__(self, value: tuple | Socket | str | None = (0, 0, 0), name: str | None = None, tip: str | None = None, subtype: str = 'NONE'):
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
        if isinstance(value, str):
            value = type(self).Named(value)

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
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.scale(-1)

    def __abs__(self):
        return self.abs

    # ----- Addition

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self._jump(self.add(other))

    # ----- Subtraction

    def __sub__(self, other):
        return self.subtract(other)

    def __rsub__(self, other):
        return Vector(other).subtract(self)

    def __isub__(self, other):
        return self._jump(self.subtract(other))

    # ----- Multiplication

    def __mul__(self, other):
        if utils.is_value_like(other):
            return self.scale(other)
        return self.multiply(other)

    def __rmul__(self, other):
        if utils.is_value_like(other):
            return self.scale(other)
        return self.multiply(other)

    def __imul__(self, other):
        if utils.is_value_like(other):
            return self._jump(self.scale(other))
        return self._jump(self.multiply(other))

    # ----- Division

    def __truediv__(self, other):
        return self.divide(other)

    def __rtruediv__(self, other):
        return Vector(other).divide(self)

    def __itruediv__(self, other):
        return self._jump(self.divide(other))

    # ----- Modulo

    def __mod__(self, other):
        return self.modulo(other)

    def __rmod__(self, other):
        return Vector(other).modulo(self)

    def __imod__(self, other):
        return self._jump(self.modulo(other))

    # ----- Mat mul -> dot product

    def __matmul__(self, other):
        return self.dot(other)

    # ----- Power -> cross product

    def __pow__(self, other):
        return self.cross(other)

    def __rpow__(self, other):
        return Vector(other).cross(self)

    def __ipow__(self, other):
        return self._jump(self.cross(other))

    # ----- Functions

    def __floor__(self):
        return self.floor

    def __ceil__(self):
        return self.ceil

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
