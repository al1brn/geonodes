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


from inspect import Arguments
import bpy

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Tree, Node, Layout
from .socket_class import NodeCache, Socket
from . import generated

# =============================================================================================================================
# =============================================================================================================================
# Interface for Geometry and Domain
# =============================================================================================================================
# =============================================================================================================================

class GeoBase:
    """ Base class for Geometry and Domain.

    Implement auto selection mechanism.
    """

    @property
    def _geo_type(self):
        return type(self._geo)

    # ====================================================================================================
    # Selection mechanism

    # ----- Selection socket is used once

    @property
    def _raw_sel(self):
        if '_selection' in self.__dict__:
            sel = self._selection
            self._selection = sel
            return sel
        else:
            return None

    @property
    def _sel(self):

        from geonodes import nd

        selection = self._raw_sel

        # No selection
        if selection is None:
            return None

        if isinstance(selection, slice):
            with Layout(f"selection = {selection}", color='AUTO_GEN'):
                if selection.start is None:
                    selection = nd.index.less_than(selection.stop)
                elif selection.stop is None:
                    selection = nd.index.greater_equal(selection.start)
                else:
                    a = (selection.start + selection.stop)/2
                    dist = a - selection.start + .1
                    selection = Float(nd.index).equal(a, epsilon=dist)

        elif isinstance(selection, tuple):
            with Layout(f"selection = tuple", color='AUTO_GEN'):
                sel = None
                idx = nd.index
                for item in selection:
                    if sel is None:
                        sel = idx.equal(item)
                    else:
                        sel |= idx.equal(item)

                selection = sel

        else:
            socket_type = utils.get_socket_type(selection)
            if socket_type in ['INT', 'VALUE', 'FLOAT']:
                with Layout(f"selection = []", color='AUTO_GEN'):
                    selection = nd.index.equal(selection)

        self._selection = None

        return selection

    # ----- Set the selection
    # Domain array index can be:
    # - a boolean
    # - an int -> int == index
    # - a tuple of ints -> or on (int == index)
    # - a slice -> index matches the slice

    def __getitem__(self, selection):
        # ----- Store the selection value
        # The selection is supposed to be a Boolean
        # If an Integer, a slice or a tuple, it is transformed into a boolean through _sel function
        # The _raw_sel function returns the passed value without transformation

        self._unlock()
        self._selection = selection
        self._lock()
        return self

# =============================================================================================================================
# Geometry class

class Geometry(generated.Geometry, GeoBase):

    SOCKET_TYPE = 'GEOMETRY'

    def __init__(self, value=None, name=None, tip=None, panel=None,
        hide_value=False, hide_in_modifier=False):
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
        - tip (str = None) : User tip (for Group Input sockets)
        - panel (str = None) : panel name (overrides tree panel if exists)
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        """

        bsock = utils.get_bsocket(value)

        # ---------------------------------------------------------------------------
        # This is not a socket : let's get the geometry as Group Input

        if bsock is None:

            tree = Tree.current_tree

            # ----- Name is None:
            # - group : we read the socket from its default name
            # - modifier : input geometry

            if name is None:
                name = type(self).__name__

            bsock = Tree.new_input('NodeSocketGeometry', name, panel=panel,
                description             = tip,
                hide_value              = hide_value,
                hide_in_modifier        = hide_in_modifier,
            )

        super().__init__(bsock)

    @property
    def _geo(self):
        return self

    # ====================================================================================================
    # Geometry Operations

    # ----------------------------------------------------------------------------------------------------
    # Bake

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
            items.new(utils.get_input_type(value), name)

        return self._jump(node._out)

    # ====================================================================================================
    # Operations

    def __add__(self, other):
        if isinstance(other, tuple):
            return type(self).Join(self, *other)

        elif isinstance(other, type(self)):
            return type(self).Join(self, other)

        else:
            return Geometry.Join(self, other)
