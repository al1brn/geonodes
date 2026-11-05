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

module : sock_float
---------------------
- Float socket

Generated environment classes inherit from this shared root: Float
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
from .node import Node, ColorRamp, NodeCurves
# magic methods
# __add__ __radd__ __iadd__ __sub__  __mul__ __matmul__ __truediv____floordiv__ __mod__ __divmod__ __pow__
# __lshift__ __rshift__ __and__ __xor__ __or__
# __neg__ __pos__ __abs__ __invert__
# __complex__ __int__	__float__ __index__
# __round__	__trunc__ __floor__	 __ceil__

# =============================================================================================================================
# Root for Integer and Float
# =============================================================================================================================

class Float(Socket):

    SOCKET_TYPE = 'VALUE'

    def __init__(self,
        value   = None,
        name    : str = None,
        min     : float = -3.40282e+38,
        max     : float = 3.40282e+38,
        tip     : str = '',
        panel   : str = "",
        **props):
        """ > Float Input

        New <#Float> input with subtype 'NONE'.

        Use methods Percentage, Factor, Angle, Time, TimeAbsolute, Distance, WaveLength, ColorTemperature or Frequency
        to create input sockets with a subtype.

        Parameters
        ----------
        value : object, default=0.0
            Default value

        name : str, default='Float'
            Input socket name

        min : float, default=-3.40282e+38
            Property min_value

        max : float, default=3.40282e+38
            Property max_value

        tip : str, default=''
            Property description

        panel : str, optional
            Panel name default="".

        props : dict
            properties


        Returns
        -------
        Float
        """
        super().__init__(value, name, min=min, max=max, tip=tip, panel=panel, **props)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Mix(cls, a=None, b=None, factor=None, clamp_factor=None):
        """ > Mix

        > Node <&Node Mix>

        Parameters
        ----------
        a : Float
            first Float

        b : Float
            second Float

        factor : Float
            socket 'Factor' (Factor_Float)

        clamp_factor : bool
            Node.clamp_factor

        Returns
        -------
        Float
        """
        return Node('Mix', named_sockets={'Factor': factor, 'A': a, 'B': b}, clamp_factor=clamp_factor, data_type='FLOAT')._out

    # ====================================================================================================
    # Methods

    def color_ramp(self, stops=None, interpolation='LINEAR'):
        """ > Color Ramp

        > Node <&Node Color Ramp>

        Parameters
        ----------

        stops : list[tuple[float, tuple]]
            Stops made of (float, color as tuple of floats)

        interpolation : {'EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT'}


        Returns
        -------
        Color
        """
        return ColorRamp(fac=self, stops=stops, interpolation=interpolation)._out

    # ====================================================================================================
    # Float curve

    def curve(self, factor=None, curve=None):
        """ > Node <&Node Float Curve>

        A curve is defined by a list of 3-tuples (not list):

        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR'), default='AUTO'

        Information
        -----------
        - Socket 'Value' : self

        Parameters
        ----------
        factor : Float
            socket 'Factor' (id: Factor)

        curve : list[tuple[float, float, str]]
            Curve points
        
        Returns
        -------
        Float
        """
        node = NodeCurves('Float Curve', named_sockets={'Value': self, 'Factor': factor})
        node.set_curves(curve)
        return node._out

    # ====================================================================================================
    # Short cuts

    def interpolate(self, to_min=0.0, to_max=1.0, type='Linear'):
        return self.map_range(to_min=to_min, to_max=to_max, interpolation_type=type)

    # ====================================================================================================
    # Mixed-type operations; other operators are inherited from generated.Float

    def __add__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(self).add(other)
        return self.add(other)

    def __radd__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).add(self)
        return self.add(other)

    def __sub__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(self).subtract(other)
        return self.subtract(other)

    def __rsub__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).subtract(self)
        return Float(other).subtract(self)

    def __mul__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self.multiply_add(other[0], other[1])
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).scale(self)
        return self.multiply(other)

    def __imul__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self._jump(self.multiply_add(other[0], other[1]))
        return self._jump(self.multiply(other))

    def __rmul__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).scale(self)
        return self.multiply(other)

    def __truediv__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).divide(self)
        return self.divide(other)

    def __rtruediv__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).divide(self)
        return Float(other).divide(self)

    def __mod__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(self).modulo(other)
        return self.modulo(other)

    def __rmod__(self, other):
        from .vector import Vector
        if utils.is_vector_like(other):
            return Vector(other).modulo(self)
        return Float(other).modulo(self)

    # ====================================================================================================
    # Output


    def thickness_out(self, target='ALL'):
        self._tree.set_thickness(self, target=target)

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Float

        with GeoNodes("Float Test"):
            
            with Layout("Base"):
                a = Float(3.14)
                a += Float(name="Your entry")
                a *= Float(1., name="Mul (1 def)")
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points.A_Float = a
                
                b = Float("A Float") - a
                g.faces.store("Another float", b)
                
            with Layout("Grid Attribute"):
                vol = g.to_volume()
                vol.store_named_grid("Float A", a)
            
            vol.out()
