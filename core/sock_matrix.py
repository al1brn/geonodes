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

module : sock_matrix
--------------------
- Matrix socket

This class inherits from Socket and from generated.Matrix
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

from . import utils
from .sockettype import SocketType
from .treeclass import Layout
from .nodeclass import Node
from . import generated

class Matrix(generated.Matrix):
    """ Matrix Socket.

    You can easily pass from a python 16-items list of tuple to a Matrix.

    The Matrix default constructor accepts such as list as initialization argument:

    ``` python
    M = Matrix([0]*16)
    ```

    You can decompose a Matrix directly to a 16-tuple with the property `as_tuple`:

    ``` python
    m = Matrix().as_tuple
    ```

    ``` python
    from geonodes import GeoNodes, Mesh, Layout, Matrix

    with GeoNodes("Matrix Test"):
        
        with Layout("Base"):
            M0 = Matrix()
            M1 = Matrix(name="Your Matrix")
            M = M0 @ M1
            M @= Matrix.CombineTransform((1, 2, 3), (4, 5, 6), (7, 8, 9))
            
        with Layout("Combine"):
            M0 = Matrix([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            vals = M0.as_tuple
            M1 = Matrix(vals)
            
            M @= M1

        with Layout("Named Attribute"):
            g = Mesh()
            g.points.A_Matrix = M
            
            b = M1 @ Matrix("A Matrix")
            g.faces.store("Another matrix", b)
            
        g.out()
    ```
    """

    SOCKET_TYPE = 'MATRIX'

    # ====================================================================================================
    # Constructors

    @classmethod
    def FromArray(cls, array):
        """ > Constructor node <&Node Combine Matrix>

        Parameters
        ----------
        array : array of size 16
            16 values to use as matrix components


        Returns
        -------
        Matrix
        """
        a = utils.value_to_array(array, (16,))
        names = [f"Column {c} Row {r}" for c in range(1, 5) for r in range(1, 5)]
        return Node('Combine Matrix', dict(zip(names, a)))._out

    @classmethod
    def FromList(cls, value):
        """ > Constructor node <&Node Combine Matrix>

        Create a matrix from the first sixteen items of a Float list. Items
        are connected column by column, with the four rows of each column in
        succession.

        ``` python
        components = Float.List(*range(16))
        matrix = Matrix.FromList(components)
        ```

        Parameters
        ----------
        value : Float
            List containing the sixteen matrix components.

        Returns
        -------
        Matrix
            Matrix built from the list items.
        """
        with Layout("Matrix.FromList"):
            return value.to_node_inputs(Node("Combine Matrix"))._out

    def separate_to_list(self):
        """ > Node <&Node Separate Matrix>

        Separate the matrix into its sixteen components and collect them into
        a Float list. Components are ordered column by column, with the four
        rows of each column in succession.

        This is a shortcut combining <!Matrix#separate_matrix> with
        <!Node#_outputs_to_list>.

        ``` python
        components = matrix.separate_to_list()

        column_1_row_1 = components[0]
        column_4_row_4 = components[15]
        ```

        Returns
        -------
        Float
            List containing the sixteen matrix components.
        """
        with Layout("Matrix.separate_to_list"):
            return self.separate_matrix()._outputs_to_list()

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def __invert__(self):
        return self.invert()

    def __matmul__(self, other):

        data_type = SocketType(other).type
        if data_type not in ['MATRIX', 'VECTOR']:
            data_type = 'VECTOR'

        if data_type == 'MATRIX':
            return self.multiply(Matrix(other))._lcop()
        else:
            return self.transform_point(other)._lcop()
        
    # ====================================================================================================
    # Utilities
    # ====================================================================================================

    def get_col(self, index=0):
        m = self.as_tuple
        return tuple(m[index*4:(index+1)*4])
    
    def get_row(self, index=0):
        m = self.as_tuple
        return (m[index], m[4+index], m[8+index], m[12 + index])
    
    def set_col(self, index, col):
        with Layout(f"Set Column {index}", color='MACRO'):
            m = list(self.as_tuple)
            m[index*4:(index+1)*4] = col
            M = Matrix(m)
            return self._jump(M)

    def set_row(self, index, row):
        with Layout(f"Set Row {index}", color='MACRO'):
            m = list(self.as_tuple)
            m[index], m[4+index], m[8+index], m[12 + index] = row    
            M = Matrix(m)
            return self._jump(M)
        
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Matrix

        with GeoNodes("Matrix Test"):
            
            with Layout("Base"):
                M0 = Matrix()
                M1 = Matrix(name="Your Matrix")
                M = M0 @ M1
                M @= Matrix.CombineTransform((1, 2, 3), (4, 5, 6), (7, 8, 9))
                
            with Layout("Combine"):
                M0 = Matrix([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
                vals = M0.as_tuple
                M1 = Matrix(vals)
                
                M @= M1

            with Layout("Named Attribute"):
                g = Mesh()
                g.points.A_Matrix = M
                
                b = M1 @ Matrix("A Matrix")
                g.faces.store("Another matrix", b)
                
            g.out()
 
                
