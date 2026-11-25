from .socket import Socket
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

Generated environment classes inherit from this shared root: Integer
the environment supplies the generated node methods.

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

from ..common import utils as utils
from .node import Node
class Integer(Socket):

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

        Parameters
        ----------
        value : object, default=0
            Default value

        name : str, default='Integer'
            Input socket name

        min : int, default=-2147483648
            Property min_value

        max : int, default=2147483647
            Property max_value

        tip : str, default=''
            Property description

        panel : str, optional
            Panel name default="".

        props : dic
            properties


        Returns
        -------
        Integer
        """
        super().__init__(value, name, min=min, max=max, tip=tip, panel=panel, **props)


    # ====================================================================================================
    # Default input constructors
    # ('VALUE', 'INDEX', 'ID_OR_INDEX')

    @classmethod
    def Index(cls, name="Index", tip=None, panel="", hide_in_modifier=True):
        """ > Index Integer group input

        New <#Integer> input with Index as default value (default_input='INDEX')

        !!! note
            By default, 'hide_in_modifier' is set to True

        Returns
        -------
        Integer
        """
        return cls(value=None, name=name, tip=tip, panel=panel, default_input='INDEX', hide_in_modifier=hide_in_modifier)

    @classmethod
    def IdOrIndex(cls, name="ID or Index", tip=None, panel="", hide_in_modifier=True):
        """ > ID or Index Integer group input

        New <#Integer> input with 'ID or Index' as default value (default_input='ID_OR_INDEX')

        !!! note
            By default, 'hide_in_modifier' is set to True

        Returns
        -------
        Integer
        """
        return cls(value=None, name=name, tip=tip, panel=panel, default_input='ID_OR_INDEX', hide_in_modifier=hide_in_modifier)

    # ====================================================================================================
    # Constructors

    @classmethod
    def FromFloat(cls, float=None, rounding_mode='ROUND'):
        from .float import Float
        return Float(float).to_integer(rounding_mode)

    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, b: "Float"=None, factor: "Float"=None, clamp_factor=None):
        """ > Mix

        > Node <&Node Mix>

        Parameters
        ----------
        b : Socket
            socket 'B' (B_Float)

        factor : Float
            socket 'Factor' (Factor_Float)

        clamp_factor : bool
            Node.clamp_factor

        Returns
        -------
        Socket
        """
        from .float import Float
        return Float(self).mix(b, factor=factor, clamp_factor=clamp_factor)
        #return Float(Node('Mix', named_sockets={'Factor': factor, 'A': self, 'B': b}, clamp_factor=clamp_factor, data_type='FLOAT')._out)

    # ====================================================================================================
    # Mixed-type operations; other operators are inherited from generated.Integer

    def __add__(self, other):
        from .. import gnmath
        if utils.is_vector_like(other):
            return gnmath.vadd(self, other)
        elif utils.is_int_like(other):
            return self.add( other)
        else:
            return gnmath.add(self, other)

    def __radd__(self, other):
        from .. import gnmath
        if utils.is_vector_like(other):
            return gnmath.vadd(other, self)
        elif utils.is_int_like(other):
            return self.add(other)
        else:
            return gnmath.add(other, self)

    def __sub__(self, other):
        from .. import gnmath
        if utils.is_vector_like(other):
            return gnmath.vsubtract(self, other)
        elif utils.is_int_like(other):
            return self.subtract(other)
        else:
            return gnmath.subtract(self, other)

    def __rsub__(self, other):
        from .. import gnmath
        if utils.is_vector_like(other):
            return gnmath.vsubtract(other, self)
        elif utils.is_int_like(other):
            return gnmath.isubtract(other, self)
        else:
            return gnmath.subtract(other, self)

    def __mul__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self.multiply_add(other[0], other[1])
        from .. import gnmath
        if utils.is_vector_like(other):
            return gnmath.scale(other, self)
        elif utils.is_int_like(other):
            return self.multiply(other)
        else:
            return gnmath.multiply(self, other)

    def __imul__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self._jump(self.multiply_add(other[0], other[1]))
        return self._jump(self.multiply(other))

    def __rmul__(self, other):
        from .. import gnmath
        if utils.is_vector_like(other):
            return gnmath.scale(other, self)
        elif utils.is_int_like(other):
            return gnmath.imultiply(other, self)
        else:
            return gnmath.multiply(other, self)

    def __pow__(self, other):
        from .. import gnmath
        if utils.is_int_like(other):
            return self.power(other)
        else:
            return gnmath.power(self, other)

    def __rpow__(self, other):
        from .. import gnmath
        if utils.is_int_like(other):
            return Integer(other).power(self)
        else:
            return gnmath.power(other, self)

    def __truediv__(self, other):
        from .float import Float
        return Float(self)/other

    def __rtruediv__(self, other):
        from .float import Float
        return other/Float(self)

    def __itruediv__(self, other):
        from .float import Float
        return Integer(Float(self)/other)

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

    
