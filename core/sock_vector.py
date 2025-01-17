"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : sock_vector
--------------------
- Vector socket

This class inherits from Socket and from generated.Vector
which is automatically generated.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


from sys import version
import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node, NodeCurves
from .socket_class import Socket
from . import generated


class Vector(generated.Vector):

    SOCKET_TYPE = 'VECTOR'

    def __init__(self, value = (0, 0, 0), name = None, tip = None, panel=None, subtype = 'NONE',
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
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
        - panel (str = None) : panel name (overrides tree pane if exists)
        - subtype (str in ('NONE', 'TRANSLATION', 'DIRECTION', 'VELOCITY',
          'ACCELERATION', 'EULER', 'XYZ') = 'NONE') : sub type for group input
        - default_attribute (str = "") : default attribute name
        - default_input (str in ('VALUE', 'NORMAL', 'POSITION') = 'VALUE') : default input
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option

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
                bsock = Tree.new_input('NodeSocketVector', name, value=value, panel=panel,
                    subtype                 = subtype,
                    default_attribute_name  = default_attribute,
                    description             = tip,
                    default_input           = default_input,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

        super().__init__(bsock)

    # ====================================================================================================
    # Default input constructors
    # ('VALUE', 'NORMAL', 'POSITION')

    @classmethod
    def Position(cls, name="Position", tip=None, panel=None, hide_in_modifier=True):
        """ > Position vector group input

        New <#Vector> input with Position as default value (default_input='POSITION')

        > [!NOTE]
        > By default, 'hide_in_modifier' is set to True

        Returns
        -------
        - Vector
        """
        return cls(value=None, name=name, tip=tip, panel=panel, default_input='POSITION', hide_in_modifier=hide_in_modifier)

    @classmethod
    def Normal(cls, name="Normal", tip=None, panel=None, hide_in_modifier=True):
        """ > Normal vector group input

        New <#Vector> input with Normal as default value (default_input='NORMAL')

        > [!NOTE]
        > By default, 'hide_in_modifier' is set to True

        Returns
        -------
        - Vector
        """
        return cls(value=None, name=name, tip=tip, panel=panel, default_input='NORMAL', hide_in_modifier=hide_in_modifier)


    # ====================================================================================================
    # Subtype constructors
    # ('NONE', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')

    @classmethod
    def Translation(cls, value=(0., 0., 0.), name='Translation', tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Translation Vector group input

        New <#Vector> input with subtype 'TRANSLATION'.

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='TRANSLATION',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)


    @classmethod
    def Direction(cls, value=(0., 0., 0.), name='Direction', tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Direction group input

        New <#Vector> input with subtype 'DIRECTION'.

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='DIRECTION',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Velocity(cls, value=(0., 0., 0.), name='Velocity', tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Velocity group input

        New <#Vector> input with subtype 'VELOCITY'.

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='VELOCITY',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Acceleration(cls, value=(0., 0., 0.), name='Acceleration', tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Acceleration group input

        New <#Vector> input with subtype 'ACCELERATION'.

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='ACCELERATION',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Euler(cls, value=(0., 0., 0.), name='Euler', tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Euler group input

        New <#Vector> input with subtype 'EULER'.

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='EULER',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def XYZ(cls, value=(0., 0., 0.), name='XYZ', tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > XYZ group input

        New <#Vector> input with subtype 'XYZ'.

        Returns
        -------
        - Vector
        """
        return cls(value=value, name=name, tip=tip, panel=panel, subtype='XYZ',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def FromRotation(cls, rotation=None):
        """ > Constructor node <&Rotation to Euler>

        Returns
        -------
        - Vector
        """
        return Rotation(rotation).to_euler()

    # ====================================================================================================
    # Mix

    def mix(self, b=None, factor=None, clamp_factor=True):
        """ > Method <&Node Mix>

        > [NOTE]
        > Call mix_uniform or mix_non_uniform depending on the factor type

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'factor_mode' : 'UNIFORM' or 'NON_UNIFORM' depending on factor argument

        Arguments
        ---------
        - b (Vector) : socket 'B' (id: B_Vector)
        - factor (Float or Vector) : socket 'Factor'
        - clamp_factor (bool): parameter 'clamp_factor'

        Returns
        -------
        - Vector
        """
        if utils.is_vector_like(factor):
            return self.mix_non_uniform(b, factor=factor, clamp_factor=clamp_factor)
        else:
            return self.mix_uniform(b, factor=factor, clamp_factor=clamp_factor)

    # ====================================================================================================
    # Curves

    def curves(self, fac=None, curves=None):
        """ > Node <&Node Vector Curves>

        A curve is defined by a list of 3-tuples (not list):
        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        > [!NOTE]
        > handle_type is optional, its default value is 'AUTO'. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Information
        -----------
        - Socket 'Vector' : self

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (id: Fac)
        - curves (list of lists of tuples (float, float, str)) : curves points

        Returns
        -------
        - Vector
        """
        node = NodeCurves('Vector Curves', sockets={'Vector': self, 'Fac': fac})
        node.set_curves(curves)
        return node._out

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

    def out(self, name=None, **props):
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
            super().out(name=name, **props)

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
