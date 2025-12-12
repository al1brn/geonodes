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

module : geometry_class
-----------------------
- Geometry class

Geometry class inherits from Socket.
Subclasses of Geometry represent the different types of Geometries: Mesh, Curve...

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


from .nodeclass import Node
from . import utils
from .socket_class import Socket
from .geom import Geom
from . import generated
from .treeinterface import ItemPath

# ====================================================================================================
# Geometry class
# ====================================================================================================

class Geometry(generated.Geometry, Geom):

    __slots__ = Socket.__slots__ + ('_geo', '_selection')

    SOCKET_TYPE = 'GEOMETRY'

    def __init__(self,
        value               : Socket = None, 
        name                : str = None,
        tip                 : str = '',
        panel               : str = "",
        **props,
    ):
        """ Socket of type 'GEOMETRY'.

        If value is None, a Group Input socket of type Geometry is created.
        When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

        ``` python
        geometry = Geometry() # Default group input geometry
        geometry = Geometry(name="Mesh") # Input group geometry
        ```

        Arguments
        ---------
        - value (Socket = None) : initial value
        - name (str = None) : Create an Group Input socket with the provided str
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - props (dict) : input properties
        """

        # ---------------------------------------------------------------------------
        # Geom interface
        # ---------------------------------------------------------------------------

        self._geo       = self
        self._selection = None

        super().__init__(value, name=name, tip=tip, panel=panel, **props)
        
    # ====================================================================================================
    # Geometry Operations
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Bake
    # ----------------------------------------------------------------------------------------------------

    def bake(self, **kwargs):
        """ Node <&Node Bake>

        [&JUMP]

        Returns
        -------
        - Geometry : self
        """

        node = Node('Bake', {'Geometry': self})

        items = node._bnode.bake_items
        for name, value in kwargs.items():
            items.new(utils.get_value_socket_type(value), name)

        return self._jump(node._out)

    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def __add__(self, other):
        if isinstance(other, tuple):
            return type(self).Join(self, *other)

        elif isinstance(other, type(self)):
            return type(self).Join(self, other)

        else:
            return Geometry.Join(self, other)
        
