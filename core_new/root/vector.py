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

module : sock_vector
--------------------
- Vector socket

Generated environment classes inherit from this shared root: Vector
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
from .node import Node, NodeCurves
from .tree import Layout
class Vector(Socket):
    """ Vector Socket.

    `x`, `y`, `z` components can be addressed individually using their properties.
    The `xyz` property returns the triplet of the components.

    A Vector can be created using a triplet or even a single float or Float.

    Use methods Percentage, Factor, Translation, Direction, Velocity, Acceleration, Euler or Xyz
    to create input sockets with a subtype.

    ``` python
    from geonodes import GeoNodes, Mesh, Layout, Rotation, Vector, G, Float, Input, pi

    with GeoNodes("Vector Test") as tree:
        
        with Layout("Base"):
            a = Vector()
            a += Vector((1, 2, 3))
            a *= Vector(7, name="Vector")
            a = a.mix(Vector.Translation(1, name="Translate"), factor=Input("Factor", subtype="Percentage", default=.5, min=0, max=100))
            
        with Layout("Named Attribute"):
            g = Mesh()
            g.points.The_Vector = a
            
            a = Vector("The Vector")
            a += G().combine_cylindrical(r=10, phi=Input("Phi", subtype="Angle"), z=3)
            g.points.The_Vector = a

        with Layout("Working with components"):
            
            # Getting one of the components
            cx = a.x
            
            # Alternative to separate_xyz
            x, y, z = a.xyz

            # Building from tripler
            a += (x**2, y + cx, z-1)

        a.separate_xyz().out(panel="xyz")
        
        g.out()
        ```    
    """

    SOCKET_TYPE = 'VECTOR'

    # ====================================================================================================
    # short cuts
    # ====================================================================================================

    @property
    def xyz(self):
        """ Shortcut for separate_xyz

        returns
        -------
        - python triplet (x, y, z)

        @node Separate XYZ
        """
        node = self.separate_xyz()
        return (node.x, node.y, node.z)

    @property
    def x(self):
        """ Get the x component

        @node Separate XYZ
        @output X
        """
        return self.separate_xyz().x

    @property
    def y(self):
        """ Get the y component

        @node Separate XYZ
        @output Y
        """
        return self.separate_xyz().x

    @property
    def z(self):
        """ Get the z component

        @node Separate XYZ
        @output 2
        """
        return self.separate_xyz().x



    @classmethod
    def FromList(cls, value):
        """ > Constructor node <&Node Combine XYZ>

        Create a vector from the first three items of a Float list. The items
        are connected respectively to the X, Y and Z inputs of the node.

        ``` python
        components = Float.List(1, 2, 3)
        vector = Vector.FromList(components)
        ```

        Parameters
        ----------
        value : Float
            List containing the vector components.

        Returns
        -------
        Vector
            Vector built from the list items.
        """
        with Layout("Vector.FromList"):
            return value.to_node_inputs(Node("Combine XYZ"))._out

    # ====================================================================================================
    # Mix

    @classmethod
    def Mix(cls, a=None, b=None, factor=None, clamp_factor=True):
        """ > Method <&Node Mix>

        > [NOTE]
        > Selects uniform or component-wise mixing from the factor type

        Information
        -----------
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'factor_mode' : 'UNIFORM' or 'NON_UNIFORM' depending on factor argument

        Parameters
        ----------
        a : Vector
            socket 'B' (id: B_Vector)

        b : Vector
            socket 'B' (id: B_Vector)

        factor : Float or Vector
            socket 'Factor'

        clamp_factor : bool
            parameter 'clamp_factor'


        Returns
        -------
        Vector
        """
        if utils.is_vector_like(factor):
            return Node('Mix', a=a, b=b, factor=factor, clamp_factor=clamp_factor, data_type='VECTOR', factor_mode='NON_UNIFORM')._out
        else:
            return Node('Mix', a=a, b=b, factor=factor, clamp_factor=clamp_factor, data_type='VECTOR', factor_mode='UNIFORM')._out

    def mix(self, b=None, factor=None, clamp_factor=True):
        """ > Method <&Node Mix>

        > [NOTE]
        > Selects uniform or component-wise mixing from the factor type

        Information
        -----------
        - Socket 'A' : self
        - Parameter 'blend_type' : 'MIX'
        - Parameter 'clamp_result' : False
        - Parameter 'data_type' : 'VECTOR'
        - Parameter 'factor_mode' : 'UNIFORM' or 'NON_UNIFORM' depending on factor argument

        Parameters
        ----------
        b : Vector
            socket 'B' (id: B_Vector)

        factor : Float or Vector
            socket 'Factor'

        clamp_factor : bool
            parameter 'clamp_factor'


        Returns
        -------
        Vector
        """
        return self.__class__.Mix(self, b, factor=factor, clamp_factor=clamp_factor)

    # ====================================================================================================
    # Curves

    def curves(self, fac=None, curves=None):
        """ > Node <&Node Vector Curves>

        A curve is defined by a list of 3-tuples (not list):

        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR'), default='AUTO'

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Vector      | `self`  |

        Parameters
        ----------
        fac : Float
            socket 'Fac' (id: Fac)

        curves : list[list[tuple[float, float, str]]]
            curves points

        Returns
        -------
        Vector
        """
        node = NodeCurves('Vector Curves', named_sockets={'Vector': self, 'Fac': fac})
        node.set_curves(curves)
        return node._out

    # ====================================================================================================
    # To list

    def separate_to_list(self):
        """ > Node <&Node Separate XYZ>

        Separate the vector into its X, Y and Z components and collect them
        into a Float list, in that order.

        This is a shortcut combining <!Vector#separate_xyz> with
        <!Node#_outputs_to_list>.

        ``` python
        components = vector.separate_to_list()

        x = components[0]
        y = components[1]
        z = components[2]
        ```

        Returns
        -------
        Float
            List containing the X, Y and Z components.
        """
        with Layout("Vector.separate_to_list"):
            return self.separate_xyz()._outputs_to_list()

    # Multiplication and multiply-add

    def __mul__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return self.multiply_add(other[0], other[1])
        if utils.is_value_like(other):
            return self.scale(other)
        return self.multiply(other)

    def __imul__(self, other):
        return self._jump(self * other)

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Rotation, Vector, G, Float, Input, pi

        with GeoNodes("Vector Test") as tree:
            
            with Layout("Base"):
                a = Vector()
                a += Vector((1, 2, 3))
                a *= Vector(7, name="Vector")
                a = a.mix(Vector.Translation(1, name="Translate"), factor=Input("Factor", subtype="Percentage", default=.5, min=0, max=100))
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points.The_Vector = a
                
                a = Vector("The Vector")
                a += G().combine_cylindrical(r=10, phi=Input("Phi", subtype="Angle"), z=3)
                g.points.The_Vector = a

            with Layout("Working with components"):
                
                # Getting one of the components
                cx = a.x
                
                # Alternative to separate_xyz
                x, y, z = a.xyz

                # Building from tripler
                a += (x**2, y + cx, z-1)

            a.separate_xyz().out(panel="xyz")
            
            g.out()
                
