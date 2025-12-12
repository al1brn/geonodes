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

module : sock_bundle
---------------------
- Bundle socket

This class inherits from Socket

updates
-------
- creation : 2022/11/15
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"


import numpy as np

import bpy
from . import utils
from .signature import Signature
from .treeclass import Tree
from .nodeclass import Node
from .socket_class import Socket
from . import generated

# ====================================================================================================
# Bundle class
# ====================================================================================================

class Bundle(generated.Bundle):

    SOCKET_TYPE = 'BUNDLE'

    # ====================================================================================================
    # Get the signature
    # ====================================================================================================

    @property
    def _is_combine(self):
        return self._bsocket.node.bl_idname == 'NodeCombineBundle'


    # ====================================================================================================
    # Get the signature
    # ====================================================================================================

    def get_signature(self, with_sockets: bool = False):
        """ Build the closure signature of the node.

        Arguments
        ---------
        - with_sockets (bool = False) : include sockets

        Returns
        -------
        - Signature
        """
        if self._is_combine:
            return Signature(self.node.get_signature(with_sockets=with_sockets).inputs)
        else:
            raise RuntimeError(f"The Bundle socket {self} doesn't come from a 'Combine Bundle' node. Impossible to get its signature.")
    
    # ====================================================================================================
    # Separate
    # ====================================================================================================

    def separate(self, signature: Signature = None):
        """ > Node <&Node Separate Bundle>

        Separate the bundle.
        """

        # ----------------------------------------------------------------------------------------------------
        # Create the node
        # ----------------------------------------------------------------------------------------------------

        node = Node('Separate Bundle', {'Bundle': self})

        # ----------------------------------------------------------------------------------------------------
        # Applies the signature
        # ----------------------------------------------------------------------------------------------------

        if signature is None and self._is_combine:
            signature = self.get_signature()

        if signature is not None:
            node.set_signature('OUTPUT', signature)

        return node

    # ====================================================================================================
    # Operators
    # ====================================================================================================

    def __add__(self, other):
        return self.join(other)
    
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @staticmethod
    def _class_test():
    
        from geonodes import GeoNodes, Geometry, Mesh, Layout, Integer, Bundle

        with GeoNodes("Bundle Test") as tree:

            # One way to combine a new bundle
            
            with Layout("Combining from dict"):
                bundle1 = Bundle.Combine({"Float": 1., "Integer": Integer(2), "Name": "Bundle 1", "Geometry": Geometry()})
            
            # Adding entries
                
            with bundle1:
                Mesh.Cube().out("Mesh 1")
                Mesh.IcoSphere().out("Mesh 2")

            # Get the signature

            sig1 = bundle1.get_signature()

            # Second bundle with its signature
            
            bundle2 = Bundle.Combine({"Geometry": Mesh.UVSphere()}, A=1, B=2)
            sig2 = bundle2.get_signature()
            
            # Join the bundles
            # Raises info on duplicate keys
            
            bundle = bundle1 + bundle2
            
            # Extract geometry from bundle
            # Add the signatures to separate properly
            node = bundle.separate(signature=sig1 + sig2)
           
            node.out()

    

