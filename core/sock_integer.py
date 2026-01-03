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

from typing import Literal

from . import utils
from .socket_class import Socket
from .nodeclass import Node
from . import generated

class Integer(generated.Integer):

    SOCKET_TYPE = 'INT'

    def __init__(self,
        value = None,
        name    : str = None,
        min     : int = -2147483648,
        max     : int = 2147483647,
        tip     : str = '',
        panel   : str = "",
        **props):
        """ > Integer Input

        New <#Integer> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = 0) : Default value
        - name  (str = 'Integer') : Input socket name
        - min  (int = -2147483648) : Property min_value
        - max  (int = 2147483647) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - props (dic) : properties

        Returns
        -------
        - Integer
        """
        super().__init__(value, name, min=min, max=max, tip=tip, panel=panel, **props)


    # ====================================================================================================
    # Default input constructors
    # ('VALUE', 'INDEX', 'ID_OR_INDEX')

    @classmethod
    def Index(cls, name="Index", tip=None, panel="", hide_in_modifier=True):
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
    def IdOrIndex(cls, name="ID or Index", tip=None, panel="", hide_in_modifier=True):
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
    # Constructors

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
    
    # =============================================================================================================================
    # Bitwise
    # and, or, xor, not, shift, rotate
    # AND	&	__and__(self, other)	__iand__(self, other)
    # OR	|	__or__(self, other)	__ior__(self, other)
    # XOR	^	__xor__(self, other)	__ixor__(self, other)
    # NOT (bitwise)	~	__invert__(self)	(pas d'in-place)
    # Shift gauche	<<	__lshift__	__ilshift__
    # Shift droite	>>	__rshift__	__irshift__    

    def __invert__(self):
        return self.bw_not()
    

    def __and__(self, other):
        return self.bw_and(other)
    
    def __rand__(self, other):
        return Integer(other).bw_and(self)
    
    def __iand__(self, other):
        return self._jump(self.bw_and(other))
    

    def __or__(self, other):
        return self.bw_or(other)
    
    def __ror__(self, other):
        return Integer(other).bw_or(self)
    
    def __ior__(self, other):
        return self._jump(self.bw_or(other))


    def __xor__(self, other):
        return self.bw_xor(other)
    
    def __rxor__(self, other):
        return Integer(other).bw_xor(self)
    
    def __ixor__(self, other):
        return self._jump(self.bw_xor(other))


    def __lshift__(self, other):
        return self.bw_shift(other)
    
    def __ilshift__(self, other):
        return self._jump(self.bw_shift(other))

    def __rshift__(self, other):
        return self.bw_shift(-other)
    
    def __irshift__(self, other):
        return self._jump(self.bw_shift(-other))
    
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Integer

        with GeoNodes("Integer Test"):
            
            with Layout("Base"):
                a = Integer(123)
                a += Integer(name="Your entry")
                a *= Integer(1, name="Mul (1 def)")
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points.An_Int = a
                
                b = Integer("An Int") - a
                g.faces.store("Another integer", b)
                
            with Layout("Grid Attribute"):
                vol = g.to_volume()
                vol.store_named_grid("Int A", a)
            
            vol.out()

    
