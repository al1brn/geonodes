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


from typing import Literal
import numpy as np

import bpy
from . import utils
from .treeclass import Tree
from .nodeclass import Node, ColorRamp, NodeCurves
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

        Aguments
        --------
        - value  (object = 0.0) : Default value
        - name  (str = 'Float') : Input socket name
        - min  (float = -3.40282e+38) : Property min_value
        - max  (float = 3.40282e+38) : Property max_value
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - props (dict) : properties

        Returns
        -------
        - Float
        """
        super().__init__(value, name, min=min, max=max, tip=tip, panel=panel, **props)

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
        node = NodeCurves('Float Curve', named_sockets={'Value': self, 'Factor': factor})
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

