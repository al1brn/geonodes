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

module : sock_boolean
---------------------
- Boolean socket

This class inherits from Socket and from generated.Boolean
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
from . treeclass import Tree
from .nodeclass import Node
from . socket_class import Socket
from . import generated
from . scripterror import NodeError

# =============================================================================================================================
# Boolean

class Boolean(generated.Boolean):
    """ Boolean socket

    > [!CAUTION]
    > Boolean operations can't use python operator `and`, `or`,... use `&` `|` instead.


    ``` python
    from geonodes import *

    with GeoNodes("Boolean Test"):
        
        with Layout("Base"):
            a = Boolean(False, "False Entry")
            b = Boolean(True, "True Entry")
            # Constant
            c = Boolean(True)

            d = (a | b) & c
            d &= True
            
            d = d.bnot().warning("No output")
            
        with Layout("Named Attribute"):
            g = Mesh()
            g.points._Bool = a
            
            b = Boolean("Bool") | a
            g.faces.store("Another bool", b)

        with Layout("Grid Attribute"):
            vol = g.to_volume()
            vol.store_named_grid("Bool A", a)
        
        vol.enable_output(d).out()
    ```
    """

    SOCKET_TYPE = 'BOOLEAN'

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def __neg__(self):
        return self.bnot()

    def __or__(self, other):
        return self.bor(other)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.nimply(other)

    def __ror__(self, other):
        return self.bor(other)

    def __and__(self, other):
        return self.band(other)

    def __mul__(self, other):
        return self.band( other)

    def __rand__(self, other):
        return self.band(other)

    def __xor__(self, other):
        return self.xor(self)

    def __rxor__(self, other):
        return self.xor(other)

    # To avoid user errors

    def __bool__(self):
        raise NodeError(f"Boolean Socket is not a python bool. Use 'switch' method or operators & | ")
    
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Boolean

        with GeoNodes("Boolean Test"):
            
            with Layout("Base"):
                a = Boolean(False, "False Entry")
                b = Boolean(True, "True Entry")
                c = Boolean(True)

                d = (a | b) & c
                d &= True
                
                d = d.bnot().warning("No output")
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points._Bool = a
                
                b = Boolean("Bool") | a
                g.faces.store("Another bool", b)

            with Layout("Grid Attribute"):
                vol = g.to_volume()
                vol.store_named_grid("Bool A", a)
            
            vol.enable_output(d).out()



