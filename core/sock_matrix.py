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

from typing import Literal

from sys import version
import numpy as np

import bpy
from . import utils
from .sockettype import SocketType
from .treeclass import Tree
from .nodeclass import Node
from .socket_class import Socket
from . import generated

class Matrix(generated.Matrix):

    SOCKET_TYPE = 'MATRIX'

    # ====================================================================================================
    # Constructors

    @classmethod
    def FromArray(cls, array):
        """ > Constructor node <&Node Combine Matrix>

        Arguments
        ---------
        - array (array of size 16) : 16 values to use as matrix components

        Returns
        -------
        - Matrix
        """
        a = utils.value_to_array(array, (16,))
        return Node('Combine Matrix', list(a))._out

    # ====================================================================================================
    # Operations

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
                vals = M0.separate
                M1 = Matrix(vals)
                
                M @= M1
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points.A_Matrix = M
                
                b = M1 @ Matrix("A Matrix")
                g.faces.store("Another matrix", b)
                
            g.out()
 
                

