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

module : sock_integer
---------------------
- Integer socket

This class inherits from Socket and from generated.Integer
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
from .treeclass import Tree, Node, ColorRamp
from .socket_class import Socket
from . import generated

class Integer(generated.Integer):

    SOCKET_TYPE = 'INT'

    def __init__(self, value=0, name=None, min=None, max=None, tip=None, panel=None, subtype='NONE',
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):

        """ > Socket of type INTEGER

        > Node <&Node Value>

        If **value** argument is None:
        - if **name** argument is None, a node 'Integer' is added
        - otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
          arguments

        If **value** argument is not None, a new **Integer** is created from the value, either
        by transtyping or creating a 'Value' node.

        ``` python
        i = Integer()      # 'Integer' node with default initial vlaue
        i = Integer(123). # 'Integer' node with 123 initial value
        i = Integer(123, name="User input", subtype='PERCENTAGE') # Create a new integer group input
        ```

        Arguments
        ---------
        - value (integer or Socket = 0) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - min (float = None) : minimum value
        - max (float = None) : maximum value
        - tip (str = None) : User tip (for Group Input sockets)
        - panel (str = None) : panel name (overrides tree panel if exists)
        - subtype (str in ('NONE', 'PERCENTAGE', 'FACTOR') = 'NONE') : sub type for group input
        - default_attribute (str = "") : default attribute name
        - default_input (str in ('VALUE', 'INDEX', 'ID_OR_INDEX') = 'VALUE') : default input
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option
        """
        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('Integer', integer=int(value))._out
            else:
                bsock = Tree.new_input('NodeSocketInt', name, value=value, panel=panel,
                    subtype                 = subtype,
                    min_value               = min,
                    max_value               = max,
                    description             = tip,
                    default_attribute_name  = default_attribute,
                    default_input           = default_input,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

        super().__init__(bsock)

    # ====================================================================================================
    # Default input constructors
    # ('VALUE', 'INDEX', 'ID_OR_INDEX')

    @classmethod
    def Index(cls, name="Index", tip=None, panel=None, hide_in_modifier=True):
        """ > Index Integer group input

        New <#Integer> input with Index as default value (default_input='INDEX')

        > [!NOTE]
        > By default, 'hide_in_modifier' is set to True

        Returns
        -------
        - Integer
        """
        return cls(value=None, name=name, tip=tip, panel=panel, default_input='INDEX', hide_in_modifier=hide_in_modifier)

    @classmethod
    def IdOrIndex(cls, name="ID or Index", tip=None, panel=None, hide_in_modifier=True):
        """ > ID or Index Integer group input

        New <#Integer> input with 'ID or Index' as default value (default_input='ID_OR_INDEX')

        > [!NOTE]
        > By default, 'hide_in_modifier' is set to True

        Returns
        -------
        - Integer
        """
        return cls(value=None, name=name, tip=tip, panel=panel, default_input='ID_OR_INDEX', hide_in_modifier=hide_in_modifier)

    # ====================================================================================================
    # Subtype constructors
    # ('NONE', 'PERCENTAGE', 'FACTOR')

    @classmethod
    def Percentage(cls, value=0, name='Percentage', min=0, max=100, tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Integer percentage group input

        New <#Integer> input with subtype 'PERCENTAGE'.

        Returns
        -------
        - Integer
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='PERCENTAGE',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value,
            panel=panel)

    @classmethod
    def Factor(cls, value=0, name='Factor', min=0, max=100, tip=None, panel=None,
        default_attribute="", default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False):
        """ > Integer factor group input

        New <#Integer> input with subtype 'FACTOR'.

        Returns
        -------
        - Integer
        """
        return cls(value=value, name=name, min=min, max=max, tip=tip, subtype='FACTOR',
            default_attribute=default_attribute, default_input=default_input, hide_value=hide_value, hide_in_modifier=hide_in_modifier, single_value=single_value,
            panel=panel)

    @classmethod
    def Random(cls, min=None, max=None, id=None, seed=None):
        return Node('Random Value', {'Min': min, 'Max': max, 'ID': id, 'Seed': seed}, data_type='INT')._out

    @classmethod
    def FromFloat(cls, float=None, rounding_mode='ROUND'):
        return Float(float).to_integer(rounding_mode)

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

    # ====================================================================================================
    # Operations

    # ----- Neg

    def __neg__(self):
        return self.negate()

    # ----- Abs

    def __abs__(self):
        return self.abs()

    # ----- Addition

    def __add__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vadd(self, other)
        elif utils.is_int_like(other):
            return self.add( other)
        else:
            return gnmath.add(self, other)

    def __radd__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vadd(other, self)
        elif utils.is_int_like(other):
            return self.add(other)
        else:
            return gnmath.add(other, self)

    def __iadd__(self, other):
        return self._jump(self.add(other))

    # ----- Subtraction

    def __sub__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vsubtract(self, other)
        elif utils.is_int_like(other):
            return self.subtract(other)
        else:
            return gnmath.subtract(self, other)

    def __rsub__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.vsubtract(other, self)
        elif utils.is_int_like(other):
            return gnmath.isubtract(other, self)
        else:
            return gnmath.subtract(other, self)

    def __isub__(self, other):
        return self._jump(self.subtract(other))

    # ----- Multiplication

    def __mul__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.scale(other, self)
        elif utils.is_int_like(other):
            return self.multiply(other)
        else:
            return gnmath.multiply(self, other)

    def __rmul__(self, other):
        from geonodes import gnmath
        if utils.is_vector_like(other):
            return gnmath.scale(other, self)
        elif utils.is_int_like(other):
            return gnmath.imultiply(other, self)
        else:
            return gnmath.multiply(other, self)

    def __imul__(self, other):
        return self._jump(self.multiply(other))

    # ----- Division

    def __floordiv__(self, other):
        return self.divide_floor(other)

    def __rfloordiv__(self, other):
        return Integer(other).divide_floor(self)

    def __ifloordiv__(self, other):
        return self._jump(self.divide_floor(other))

    # ----- Modulo

    def __mod__(self, other):
        return self.modulo(other)

    def __rmod__(self, other):
        return Integer(other).modulo(self)

    def __imod__(self, other):
        return self._jump(self.modulo(other))

    # ----- Power

    def __pow__(self, other):
        from geonodes import gnmath
        if utils.is_int_like(other):
            return self.power(other)
        else:
            return gnmath.power(self, other)

    def __rpow__(self, other):
        from geonodes import gnmath
        if utils.is_int_like(other):
            return Integer(other).power(self)
        else:
            return gnmath.power(other, self)

    def __ipow__(self, other):
        return self._jump(self.power(self, other))

    # ----- Division

    def __truediv__(self, other):
        from geonodes import Float
        return Float(self)/other

    def __rtruediv__(self, other):
        from geonodes import Float
        return other/Float(self)

    def __itruediv__(self, other):
        from geonodes import Float
        return Integer(Float(self)/other)

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
