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

module : sock_float
---------------------
- Float socket

This class inherits from Socket and from generated.Float
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


import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node, ColorRamp, NodeCurves
from .socket_class import Socket
from . import generated

# magic methods
# __add__ __radd__ __iadd__ __sub__  __mul__ __matmul__ __truediv____floordiv__ __mod__ __divmod__ __pow__
# __lshift__ __rshift__ __and__ __xor__ __or__
# __neg__ __pos__ __abs__ __invert__
# __complex__ __int__	__float__ __index__
# __round__	__trunc__ __floor__	 __ceil__

# =============================================================================================================================
# Root for Integer and Float
# =============================================================================================================================

class Float(generated.Float):

    SOCKET_TYPE = 'VALUE'

    def __init__(self, value=0., name=None, min=None, max=None, tip=None, panel=None, subtype='NONE',
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Socket of type VALUE

        > Node <&Node Value>

        If **value** argument is None:
        - if **name** argument is None, a node 'Value' is added
        - otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
          arguments

        If **value** argument is not None, a new **Float** is created from the value, either
        by transtyping or creating a 'Value' node.

        ``` python
        float = Float()      # 'Value' node with default initial vlaue
        float = Float(3.14). # 'Value' node with 3.14 initial value
        float = Float(3.14, name="User input", subtype='ANGLE') # Create a new Float group input
        ```

        Arguments
        ---------
        - value (float | str | Socket = 0.) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - min (float = None) : minimum value
        - max (float = None) : maximum value
        - tip (str = None) : User tip (for Group Input sockets)
        - panel (str = None) : panel name (overrides tree pane if exists)
        - subtype (str in ('NONE', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE',
          'DISTANCE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY') = 'NONE') : sub type for group input
        - default_attribute (str = "") : default attribute name
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option
        """

        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('Value')._out
                bsock._bsocket.default_value = value
            else:
                bsock = Tree.new_input('NodeSocketFloat', name, value=value, panel=panel,
                    subtype                 = subtype,
                    min_value               = min,
                    max_value               = max,
                    description             = tip,
                    default_attribute_name  = default_attribute,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

        super().__init__(bsock)

     # ====================================================================================================
     # Constructors
     # ('NONE', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY')

    @classmethod
    def Percentage(cls, value=0., name='Percentage', min=0, max=100, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Percentage group input

        New <#Float> input with subtype 'PERCENTAGE'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='PERCENTAGE', panel=panel,
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Factor(cls, value=0., name='Factor', min=0, max=1, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Factor group input

        New <#Float> input with subtype 'FACTOR'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='FACTOR',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Angle(cls, value=0., name='Angle', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Angle group input

        New <#Float> input with subtype 'ANGLE'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='ANGLE',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Time(cls, value=0., name='Time', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Time group input

        New <#Float> input with subtype 'TIME'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='TIME',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def TimeAbsolute(cls, value=0., name='Time Absolute', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Time Absolute group input

        New <#Float> input with subtype 'TIME_ABSOLUTE'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='TIME_ABSOLUTE',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Distance(cls, value=0., name='Distance', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Distance group input

        New <#Float> input with subtype 'DISTANCE'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='DISTANCE',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def WaveLength(cls, value=0., name='Wave Length', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Wave Length group input

        New <#Float> input with subtype 'WAVELENGTH'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='WAVELENGTH',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def ColorTemperature(cls, value=0., name='Color Temperature', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Color Temperature group input

        New <#Float> input with subtype 'COLOR_TEMPERATURE'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='COLOR_TEMPERATURE',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Frequency(cls, value=0., name='Frequency', min=None, max=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Frequency group input

        New <#Float> input with subtype 'FREQUENCY'.

        Returns
        -------
        - Float
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, panel=panel, subtype='FREQUENCY',
            default_attribute=default_attribute, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value)

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        """ > Random float

        > Node <&Node Random Value>
        """
        return Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='FLOAT')._out

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_factor=None):
        """ > Mix

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (Factor_Float)
        - other (Socket) : socket 'B' (B_Float)
        - clamp_factor (bool): Node.clamp_factor

        Returns
        -------
        - Socket
        """
        return Float(Node('Mix', {'Factor': factor, 'A': self, 'B': other}, clamp_factor=clamp_factor, data_type='FLOAT')._out)

    def color_ramp(self, stops=None, interpolation='LINEAR'):
        """ > Color Ramp

        > Node <&Node Color Ramp>

        Arguments
        ---------
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)
        - interpolation in ('EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT')

        Returns
        -------
        - Color
        """
        return ColorRamp(fac=self, stops=stops, interpolation=interpolation)._out

    # ====================================================================================================
    # Float curve

    def curve(self, factor=None, curve=None):
        """ > Node <&Node Float Curve>

        A curve is defined by a list of 3-tuples (not list):
        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        > [!NOTE]
        > handle_type is optional, its default value is 'AUTO'. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Information
        -----------
        - Socket 'Value' : self

        Arguments
        ---------
        - factor (Float) : socket 'Factor' (id: Factor)
        - curve (list of tuples (float, float, str)) : curve points

        Returns
        -------
        - Float
        """
        node = NodeCurves('Float Curve', sockets={'Value': self, 'Factor': factor})
        node.set_curves(curve)
        return node._out

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.multiply(-1)

    # ----- Abs

    def __abs__(self):
        return self.abs()

    # ----- Addition

    def __add__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(self).add(other)
        return self.add(other)

    def __radd__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(other).add(self)
        return self.add(other)

    def __iadd__(self, other):
        return self._jump(self.add(other))

    # ----- Subtraction

    def __sub__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(self).subtract(other)
        return self.subtract(other)

    def __rsub__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(other).subtract(self)
        return Float(other).subtract(self)

    def __isub__(self, other):
        return self._jump(self.subtract(other))

    # ----- Multiplication

    def __mul__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(other).scale(self)
        return self.multiply(other)

    def __rmul__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(other).scale(self)
        return self.multiply(other)

    def __imul__(self, other):
        return self._jump(self.multiply(other))

    # ----- Division

    def __truediv__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(other).divide(self)
        return self.divide(other)

    def __rtruediv__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(self).divide(other)
        return Float(other).divide(self)

    def __itruediv__(self, other):
        return self._jump(self.divide(other))

    # ----- Modulo

    def __mod__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(self).modulo(other)
        return self.modulo(other)

    def __rmod__(self, other):
        from geonodes import Vector
        if utils.is_vector_like(other):
            return Vector(other).modulo(self)
        return Float(other).modulo(self)

    def __imod__(self, other):
        return self._jump(self.modulo( other))

    # ----- Power

    def __pow__(self, other):
        return self.power(other)

    def __rpow__(self, other):
        return Float(other).power(self)

    def __ipow__(self, other):
        return self._jump(self.power(other))

    # ----- Operations

    def __round__(self):
        return self.round()

    def __trunc__(self):
        return self.trunc()

    def __floor__(self):
        return self.floor()

    def __ceil__(self):
        return self.ceil()

    # =============================================================================================================================
    # Comparison
    # __eq__ __ne__ __lt__ __gt__ __le__ __ge__

    def __ge__(self, other):
        return self.greater_equal(other)

    def __gt__(self, other):
        return self.greater_than(other)

    def __le__(self, other):
        return self.less_equal(other)

    def __lt__(self, other):
        return self.less_than(other)

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return self.not_equal(other)

    # ====================================================================================================
    # Output

    def out(self, name=None, **props):
        """ > Connect to output

        [&SHADER]

        > [!IMPORTANT]
        > - Geometry Nodes : create a group output socket with the provided name
        > - Shader : create a node <&ShaderNode AOV Output>
        """
        if self._tree._btree.bl_idname == 'ShaderNodeTree' and not self._tree._is_group:
            if name is None:
                self._tree.set_thickness(self)
            else:
                self._tree.aov_output(name=name, value=self)
        else:
            super().out(name=name, **props)

    def thickness_out(self, target='ALL'):
        self._tree.set_thickness(self, target=target)
