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

from . import utils

# =============================================================================================================================
# Interface for Geometry and Domain
# =============================================================================================================================

class Geom:

    """ Interface for Geometry and Domain.

    Child classes must implement properties:
    - _geo : pointing on the actuel Geometry instant
    - _selection : value of selection socket
    - _raw_sel : 


    Implement auto selection mechanism.
    """

    # ====================================================================================================
    # Returns the Geometry type (Mesh, Curve,...)
    # ====================================================================================================

    @property
    def _geo_type(self):
        return type(self._geo)
    
    # ====================================================================================================
    # Selection mechanism
    # ====================================================================================================

    # ----- Set the selection
    # Domain array index can be:
    # - a boolean
    # - an int -> int == index
    # - a tuple of ints -> or on (int == index)
    # - a slice -> index matches the slice

    # ----------------------------------------------------------------------------------------------------
    # Set the selection with the argument
    # Will be consumed later
    # ----------------------------------------------------------------------------------------------------

    def __getitem__(self, selection):
        self._selection = selection
        return self

    # ----------------------------------------------------------------------------------------------------
    # Consume the selection
    # ----------------------------------------------------------------------------------------------------

    def get_selection(self):

        from .generated import static_nd as nd
        from .treeclass import Layout
    
        selection = self._selection
        self._selection = None

        if selection is None:
            return None
        
        # ---------------------------------------------------------------------------
        # Slice
        # ---------------------------------------------------------------------------

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

        # ---------------------------------------------------------------------------
        # Tuple
        # ---------------------------------------------------------------------------

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

        # ---------------------------------------------------------------------------
        # Index
        # ---------------------------------------------------------------------------

        else:
            socket_type = utils.get_value_socket_type(selection)
            if socket_type in ['INT', 'VALUE', 'FLOAT']:
                with Layout(f"selection = []", color='AUTO_GEN'):
                    selection = nd.index.equal(selection)

        return selection

