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

module : treeinterface
----------------------
- TreeInterface class

This module implements the TreeInterface class to
manage Tree input and output sockets creation and ordering.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/03/26 : panels can be sub panels
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


import bpy
from . import utils
from . import constants

from bpy.types import NodeTreeInterfaceSocket, NodeTreeInterfacePanel, NodeTreeInterfaceItem

import numpy as np

from . scripterror import NodeError

DELETION = '__deletion marker__'

# =============================================================================================================================
# Iterate on a tree of Interface Sockets

class SocketsIterator:
    def __init__(self, item, panels, sockets):
        self.panels  = panels
        self.sockets = sockets

        self.start_item  = item
        self.current     = item

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            if self.current is None:
                raise StopIteration

            ret_item = self.current

            if len(self.current) > 0:
                self.current = self.current[0]

            else:
                next_item = self.current.next_item
                while next_item is None:
                    if self.current.is_top or self.current == self.start_item:
                        break

                    self.current = self.current.parent
                    next_item = self.current.next_item

                self.current = next_item

            if (ret_item.is_panel and self.panels) or (ret_item.is_socket and self.sockets):
                return ret_item

# =============================================================================================================================
# Input ot output sockets organized as a tree

class InterfaceSockets(list):
    """ Read the panels structure into a tree of panels / sockets

    Allow to build unique names for sockets
    """
    def __init__(self, btree, in_out, bitem=None, parent=None):
        super().__init__(self)
        self.btree      = btree
        self.in_out     = in_out
        self.bitem      = bitem
        self.parent     = parent
        self._selected  = False

        if self.is_panel:
            for bitm in self.btree.interface.items_tree:
                parent_name = bitm.parent.name
                if bitm.item_type == 'PANEL' or (bitm.item_type == 'SOCKET' and bitm.in_out == in_out):
                    if (self.bitem is None and parent_name == "") or (self.bitem == bitm.parent):
                        self.append(InterfaceSockets(self.btree, in_out, bitm, parent=self))

        else:
            assert(self.bitem.in_out == in_out)

    def __str__(self):
        if self.is_top:
            return f"<Sockets '{btree.name}'  {self.in_out}>"
        else:
            return f"<{self.bitem.item_type} '{self.bitem.name}'>"

    def __repr__(self):
        if self.is_panel:
            if self.bitem is None:
                s = f"{self.in_out} sockets of Tree '{self.btree.name}'"
            else:
                s = f"> {self.bitem.name} ({self.path(python=True)})"

            for item in self:
                s += "\n  " + "\n  ".join(repr(item).split("\n"))
            return s

        else:
            return f"{self.bitem.name} ({self.unique_names(python=True)[0]})"

    # ====================================================================================================
    # Selection

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value
        for item in self:
            item.selected = value

    @property
    def selected_parents(self):
        if self.is_top or (not self.parent.selected):
            return []

        parents = self.parent.selected_parents
        parents.append(self.parent)

        return parents

    @property
    def selected_path(self):
        items = self.selected_parents + [self]
        path = ""
        for item in items:
            if item.bitem is None:
                continue
            if path == "":
                path = item.bitem.name
            else:
                path += ' > ' + item.bitem.name
        return path

    # ====================================================================================================
    # Socket

    @property
    def socket(self):
        """ Get the Socket from an input/output node

        Returns
        -------
        - Socket : socket corresponding to the interface item or None if a Panel
        """

        from . treeclass import Tree
        tree = Tree.current_tree

        if self.is_panel:
            return None

        elif self.in_out == 'INPUT':
            node = tree.input_node
            return node.data_socket(node._bnode.outputs[self.bitem.identifier])

        else:
            node = tree.output_node
            return node.data_socket(node._bnode.inputs[self.bitem.identifier])

    # ====================================================================================================
    # Comparizon of two items

    def __eq__(self, other):
        """ Compare an interface socket with another one
        """
        if self.bitem is None:
            return other.bitem is None
        elif other.bitem is None:
            return False
        else:
            return self.bitem.index == other.bitem.index

    # ====================================================================================================
    # Panel of Socket

    @property
    def is_panel(self):
        """ The current interface item is a Panel
        """
        return self.bitem is None or self.bitem.item_type == 'PANEL'

    @property
    def is_socket(self):
        """ The current interface item is as Socket
        """
        if self.bitem is None:
            return False
        else:
            return self.bitem.item_type == 'SOCKET'

    def is_like(self, other):
        """ Test if the two items are of same type: panel or socket

        Returns
        -------
        - Boolean : True if both share the same item_type
        """
        return (self.is_panel and other.is_panel) or (self.is_socket and other.is_socket)

    # ====================================================================================================
    # Tree navigation

    @property
    def is_top(self):
        """ The item is top of tree
        """
        return self.parent is None

    @property
    def top(self):
        """ Get the top of the tree
        """
        if self.is_top:
            return self
        else:
            return self.parent.top

    @property
    def next_item(self):
        """ Next item in the Parent
        """
        if self.is_top:
            return None

        index = None
        for i, itm in enumerate(self.parent):
            if itm == self:
                index = i
                break

        assert(index is not None)

        if index < len(self.parent)-1:
            return self.parent[index + 1]
        else:
            return None

    def search_bitem(self, bitem):
        if bitem is None:
            return self.top

        for item in self.iterate():
            if item.bitem is None:
                continue
            if item.bitem.index == bitem.index:
                return item

        return None

    def top_selected(self):
        if self.is_top:
            return self

        if self.parent.selected:
            return self.parent.top_selected
        else:
            return self

    # ====================================================================================================
    # Iterator

    def iterate(self, panels=True, sockets=True):
        """ Returns an Iterator starting at this item

        Arguments
        ---------
        - panels (bool = True) : include panels
        - sockets (bool = True) : include sockets
        """
        return SocketsIterator(self, panels, sockets)

    # ====================================================================================================
    # Naming

    # ----------------------------------------------------------------------------------------------------
    # Conversion user name to python name

    @staticmethod
    def user_name_to_python(name: str, python: bool = True):
        """ Convert a user into a python name

        In a user name, '>' is used as separatot in the paths.
        In a python, names are lowered and seperated by '_' character

        For instance, "Panel > Socket" is transformed into "panel_socket"

        Arguments
        ---------
        - name : user name
        - python : keep name if False

        Returns
        -------
        - str : python name
        """
        return '_'.join([utils.snake_case(s.strip()) for s in name.split('>')]) if python else name.strip()

    # ----------------------------------------------------------------------------------------------------
    # Disambiguation rank

    def rank(self, absolute=False):
        """ Rank of the same type of items sharing the same name

        Ranking can be computed:
        - absolute : between panels and sockets
        - relative : within panels and within sockets

        This rank is used for disambiguation between homonyms
        - Panel : 0
          - Socket : 0
          - Socket : 1
        - Panel : 1
        - Ambigous (P) : 0
          - Socket : 0
        - Ambiguous (S) : 1 if absolute 0 otherwise

        Arguments
        ---------
        - absolute (bool = False) : absolute disambiguation

        Returns
        -------
        - int : rank in homonyms
        """
        if self.is_top:
            return 0

        name = utils.snake_case(self.bitem.name)

        count = 0
        for i, item in enumerate(self.parent):
            if item == self:
                return count

            # +1 if same name and absolute or same type
            if (absolute or self.is_like(item)) and (utils.snake_case(item.bitem.name) == name):
                count += 1

        assert(False)

    # ----------------------------------------------------------------------------------------------------
    # User name

    def name(self, absolute: bool = False, python: bool = False):
        """ The unique name within its parent panel

        The rank if added if not 0:
        - Socket -> "Socket"
        - Socket -> "Socket 1"

        Arguments
        ---------
        - absolute : absolute disambiguation
        - python : python name rather than user name

        Returns
        -------
        - str : user name
        """
        if self.is_top:
            return ""

        rank = self.rank(absolute)
        return self.user_name_to_python(self.bitem.name + ("" if rank == 0 else f" {rank}"), python)

    # ----------------------------------------------------------------------------------------------------
    # Full path

    def path(self, absolute: bool = False, python: bool = False):
        """ Build the full path of the item

        The path is built by joining the names of the parent panels with '>' character:
        - Socket -> "Socket"
        - Socket -> "Socket 1"
        - Panel -> "Panel"
          - Socket -> "Panel > Socket"
          - Socket -> "Panel > Socket 1"
        - Panel -> "Panel 2"
          - Socket -> "Panel 2 > Socket"
          - Socket -> "Panel 2 > Socket 1"

        Arguments
        ---------
        - absolute : absolute disambiguation
        - python : python name rather than user name

        Returns
        -------
        - str : item full path
        """
        if self.is_top:
            return ""

        name = self.name(absolute)
        if self.parent.is_top:
            return self.user_name_to_python(name, python)
        else:
            return self.user_name_to_python(self.parent.path(absolute) + " > " + name, python)

    # ----------------------------------------------------------------------------------------------------
    # List of acceptable paths

    def paths(self, absolute: bool = False, python: bool = False):
        """ Returns a list with all the user paths

        - Socket -> ["Socket"]
        - Panel -> ["Panel"]
          - Socket -> ["Socket", "Panel ,> Socket"]
          - Socket -> ["Socket 1", "Panel > Socket 1"]
          - Panel -> ["Panel", "Panel > Panel"]
            - Socket -> ["Socket", "Panel > Socket", "Panel > Panel > Socket 1"]
            - Socket -> ["Socket 1", "Panel > Socket 1", "Panel > Panel > Socket 1"]

        The lower the index is, the more homonyms could exist. The last
        name is always unique.

        Arguments
        ---------
        - absolute : absolute disambiguation
        - python : python name rather than user name

        Returns
        -------
        - list : list of user paths
        """
        if self.is_top:
            return [""]

        names = [self.name(absolute)]
        parent = self.parent
        while not parent.is_top:
            names.append(parent.name(absolute) + ' > ' + names[-1])
            parent = parent.parent

        return [self.user_name_to_python(name, python) for name in names]

    # ----------------------------------------------------------------------------------------------------
    # List of unique user names

    def unique_names(self, absolute: bool = False, python: bool = False):
        """ Returns the list of unique user paths

        Remove the names from `user_paths` which have homonyms:
        - Socket -> ["Socket"]
        - Panel -> ["Panel"]
            - Socket -> ["Panel > Socket"]
            - Socket -> [Socket 1", "Panel > Socket 1"]
            - Other -> ["Other", "Panel > Other"]
            - Panel -> ["Panel > Panel"]
              - Socket -> ["Panel > Panel > Socket"]
              - Unique -> ["Unique", "Panel > Unique", "Panel > Panel > Unique"]

        This list is used to allow naming a socket using different paths.

        Arguments
        ---------
        - absolute : absolute disambiguation
        - python : python name rather than user name

        Returns
        -------
        - list : list of unique paths
        """
        if self.is_top:
            return ""

        # ----- All the possible names

        names = self.paths(absolute, python)
        last_name = names[-1]

        # ----- Return the single name if attached to top

        if self.parent.is_top:
            return names

        # ----- Remove the homonyms

        for item in self.top.iterate(sockets=self.is_socket or absolute, panels=self.is_panel or absolute):
            if item == self:
                continue

            item_names = item.paths(absolute, python)

            to_remove = []
            for name in names:
                if name in item_names:
                    to_remove.append(name)
            for name in to_remove:
                names.remove(name)

        if not len(names):
            names = [last_name]

        return names

    # ----------------------------------------------------------------------------------------------------
    # Name matches the possible names

    def match_name(self, name: str, absolute: bool = False):
        """ The name provided in argument matches one of the possible names

        Arguments
        ---------
        - name : name to test
        - absolute : absolute disambiguation

        Returns
        -------
        - bool : true if matches
        """
        python_name = self.user_name_to_python(name)
        return python_name in self.unique_names(absolute, python=True)

    # ====================================================================================================
    # Get an item by its name

    def by_name(self, name: str, sockets: bool = True, panels: bool = True, halt: bool = False):
        """ Get an interface socket using a path

        The provided name is searched in the `unique_names` lists of the items.

        Arguments
        ---------
        - name : socket or panel name
        - sockets : search a socket
        - panels : search a panel
        - halt : raise an error if not found

        Return
        ------
        - InterfaceSocket : None if not found
        """
        python_name = self.user_name_to_python(name)

        absolute = panels and sockets
        for item in self.iterate(sockets=sockets, panels=panels):
            if python_name in item.unique_names(absolute, python=True):
                return item

        if halt:
            raise NodeError(f"'{name}' is not a valid socket / panel name for tree '{self.btree.name}'", valids=repr(self))

        return None

    # ====================================================================================================
    # Find an item in a tree

    def find_in_other_tree(self, btree, parent=None):
        """ Find the item in a tre

        Used with another Tree to see if a socket must be created

        Arguments
        ---------
        - btree (NodeTreeInterface) : the tree into which searching the item
        - parent (NodeTreeInterfacePanel = None) : the panel into which searching the item

        Returns
        -------
        - NodeTreeInterfaceItem : the item found the tree, None if not found
        """

        if self.is_top:
            return None

        #if not self.parent.is_top:
        #    parent = self.parent.find_in_other_tree(btree)
        #    if parent is None:
        #       return None

        for item in btree.interface.items_tree:

            if parent is None:
                if item.parent.name != "":
                    continue
            else:
                if item.parent.index != parent.index:
                    continue

            if item.name != self.bitem.name:
                continue
            if item.item_type != self.bitem.item_type:
                continue
            if item.item_type == 'SOCKET':
                if item.in_out != self.bitem.in_out:
                    continue
                if item.bl_socket_idname != self.bitem.bl_socket_idname:
                    continue

            return item

        return None

    # =============================================================================================================================
    # Copy socket attributes to another one

    @classmethod
    def copy_item_attributes(cls, source_item, target_item):
        """ Copy socket attributes to another one

        Used when created an input socket to feed a group input socket

        Arguments
        ---------
        - source_item (NodeTreeInterfaceItem) : the source
        - target_item (NodeTreeInterfaceItem) : the target

        Returns
        -------
        - NodeTreeInterfaceItem : the target item
        """

        for prop_name in constants.INTERFACE_SOCKET_PROPERTIES:
            prop_value = getattr(source_item, prop_name, None)
            if prop_value is not None:
                setattr(target_item, prop_name, prop_value)

        return target_item

    # =============================================================================================================================
    # Create in a tree

    def create_in_tree(self, btree, parent=None):
        """ Create the socket or panel and sub panels / sockets into a tree

        Arguments
        ---------
        - btree (NodeTreeInterface) : the tree into which creating the item
        - parent (NodeTreeInterfacePanel = None) : the panel into which createing the item

        Returns
        -------
        - NodeTreeInterfaceItem : the created item, or found item if already exists
        """

        interface = btree.interface

        if not self.is_top:
            item = self.find_in_other_tree(btree, parent=parent)
            if item is None:
                if self.is_panel:
                    item = interface.new_panel(self.bitem.name)
                    if parent is not None:
                        interface.move_to_parent(item, parent, 999)
                else:
                    item = interface.new_socket(self.bitem.name, in_out=self.in_out, socket_type=self.bitem.socket_type, parent=parent)

            self.copy_item_attributes(self.bitem, item)

            if self.is_socket:
                return item

            parent = item

        # ----- Children creation

        for item in self:
            item.create_in_tree(btree, parent=parent)

        return parent

# =============================================================================================================================
# Tree Interface

class TreeInterface:
    def __init__(self, btree):
        """ Encapsulate the Blender NodeTreeInterface class

        This class is used to ease creation and duplication of trees of sockets

        The process of creating a Tree makes use of the following methods:
        - mark_for_deletion : all panels and sockets will be deleted when the tree will be finished
        - create input / output sockets : deletion markers are removed
        - set_in_geometry : make sure the input geometry is first
        - set_out_geometry : make sure output geometry exists and is first
        - clear : remove unused input and output sockets

        Tree inputs can be created from another node inputs
        """
        self.btree = btree

    # ====================================================================================================
    # Conversion user name to python name

    @staticmethod
    def user_name_to_python(name: str, python: bool = True):
        """ Convert a user into a python name

        In a user name, '>' is used as separatot in the paths.
        In a python, names are lowered and seperated by '_' character

        For instance, "Panel > Socket" is transformed into "panel_socket"

        Arguments
        ---------
        - name : user name
        - python : keep name if False

        Returns
        -------
        - str : python name
        """
        return InterfaceSockets.user_name_to_python(name, python)

    # ====================================================================================================
    # Sockets organized in tree to build the names and paths

    @property
    def input_sockets(self):
        """ Input Sockets Tree

        Returns
        -------
        - SocketsTree
        """
        return InterfaceSockets(self.btree, 'INPUT')

    @property
    def output_sockets(self):
        """ Output Sockets Tree

        Returns
        -------
        - SocketsTree
        """
        return InterfaceSockets(self.btree, 'OUTPUT')

    def sockets(self, in_out):
        if in_out == 'INPUT':
            return self.input_sockets
        elif in_out == 'OUTPUT':
            return self.output_sockets
        else:
            assert(False)

    def sockets_for(self, bitem):
        assert(bitem is not None)
        if bitem.item_type == 'PANEL' or bitem.in_out == 'INPUT':
            return self.input_sockets
        else:
            return self.output_sockets

    # ====================================================================================================
    # Repr

    def __repr__(self):
        return repr(self.input_sockets)

    # ====================================================================================================
    # Clearing

    def mark_for_deletion(self):
        """ Mark all sockets to be deleted

        Set the `description` attribute with as specific value
        """
        # STRANGELY: for item in self.btree.interface.items_tree can return None
        # Need to loop on list index !!!
        for i in range(len(self.btree.interface.items_tree)):
            item = self.btree.interface.items_tree[i]
            if item is None:
                continue
            item.description = DELETION

    def clear(self, all=True):
        """ Clear all sockets

        Arguments
        ---------
        - all (bool = True) : all the sockets, only marked as DELETION
        """
        if all:
            self.btree.interface.clear()

        else:
            to_delete = []
            for item in self.btree.interface.items_tree:
                if item.description == DELETION:
                    to_delete.append(item)
            for item in to_delete:
                self.btree.interface.remove(item)

    # ====================================================================================================
    # Get a socket by its identifier

    def by_identifier(self, identifier: str):
        """ Return a socket by its identifier

        Arguments
        ---------
        - identifier : socket identifier

        Returns
        -------
        - NodeTreeInterfaceSocket : socket or raises an error if not found
        """
        if isinstance(identifier, NodeTreeInterfaceSocket):
            assert(identifier in self.btree.interface.items_tree)
            return identifier

        for item in self.btree.interface.items_tree:
            if (item.item_type == 'SOCKET') and (item.identifier == identifier):
                return item

        raise NodeError(f"TreeInterface socket with identifier '{identifier}' not found in tree '{self.btree.name}'.")

    # ====================================================================================================
    # Names

    def get_name(self, bitem: 'str | item', path: bool = False, absolute: bool = False, python: bool = False):
        """ Get the user name of an item

        Arguments
        ---------
        - bitem : the item or item identifier
        - path : return full path if True
        - absolute : absolute disambiguation
        - python : returns python name rather than user name

        Returns
        -------
        - str : item name or path
        """
        if bitem is None:
            return ""

        if isinstance(bitem, str):
            bitem = self.by_identifier(bitem)

        item = self.sockets_for(bitem).search_bitem(bitem)
        if path:
            name = item.path(absolute, python)
        else:
            name = item.name(absolute, python)

        return name

    # ====================================================================================================
    # Move panel as last 'NOT DELETED"

    def move_before_deleted(self, bitem):
        """ Move the item as the last 'NOT DELETED' item in its parent list

        Arguments
        ---------
        - bitem (NodeTreeInterfaceItem) : the item to move as last NOT DELETED position
        """

        to_move = []
        for item in self.btree.interface.items_tree:
            if item.description != DELETION:
                continue
            if bitem.parent.name == "":
                if item.parent.name != "":
                    continue
            else:
                if item.parent.name == "":
                    continue
                if item.parent.index != bitem.parent.index:
                    continue

            to_move.append(item)

        for item in to_move:
            self.btree.interface.move(item, 999)

    # ====================================================================================================
    # Panels

    # ----------------------------------------------------------------------------------------------------
    # Get an existing panel

    def get_panel(self, name: str, parent: str = "", halt: bool = True):
        """ Get a panel by its name

        Arguments
        ---------
        - name : panel name
        - parent : panel name
        - halt : raise an exception if not found

        Raises
        ------
        - AttributeError : if panel not found

        Returns
        -------
        - NodeTreeInterfacePanel
        """
        if name == "":
            return None

        if parent != "":
            name = parent + ' > ' + name

        return self.input_sockets.by_name(name, sockets=False, panels = True, halt = halt).bitem

    # ----------------------------------------------------------------------------------------------------
    # Get / create an existing panel

    def create_panel(self, name: str, tip: str = "", default_closed: bool = False, panel: str | NodeTreeInterfacePanel = ""):
        """ Create a panel

        > [!NOTE]
        > The panel is not created if a panel with the same path already exists

        Arguments
        ---------
        - name : panel name or NodeTreeInterfacePanel
        - tip : description
        - default_closed (bool=False) : closed by default
        - panel : panel where to place the new panel (panel path or NodeTreeInterfacePanel)

        Returns
        -------
        - NodeTreeInterfacePanel
        """
        if isinstance(name, NodeTreeInterfacePanel):
            return name

        # ----- Ensure target parent panel exists
        parent_panel = None
        if isinstance(panel, str):
            if panel == "":
                parent_panel = None
            else:
                parent_panel = self.create_panel(panel)
        else:
            if panel is not None:
                assert(isinstance(panel, NodeTreeInterfacePanel))
            parent_panel = panel

        # ----- Name is empty, nothing to do
        if isinstance(name, str) and (name == ""):
            return parent_panel

        # ----- Creation loop
        for panel_name in [s.strip() for s in name.split(">")]:

            # ----- Search if a panel named panel_name exists in current parent_panel
            found = None
            for item in self.btree.interface.items_tree:
                if item.item_type != 'PANEL' or item.name != panel_name:
                    continue
                if parent_panel is None:
                    if item.parent.name != "":
                        continue
                else:
                    if item.parent.index != parent_panel.index:
                        continue

                found = item
                if found.description == DELETION:
                    found.description = ""
                break

            # ----- Not found, create a new panel
            if found is None:
                found = self.btree.interface.new_panel(panel_name)
                if parent_panel is not None:
                    self.btree.interface.move_to_parent(found, parent_panel, 9999)

            # ----- Found / created panel is the new parent
            parent_panel = found
            self.move_before_deleted(parent_panel)

        # ----- Last parent is the required panel

        parent_panel.description = tip
        parent_panel.default_closed = default_closed

        return parent_panel

    # ====================================================================================================
    # Sockets

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its socket name

    def get_socket(self, in_out: str, name: str, halt=True):
        """ Get the socket by its name

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - name (str) : searched named
        - halt (bool = False) : raises an error if not found

        Returns
        -------
        - NodeTreeInterfaceSocket
        """
        sockets = self.sockets(in_out)
        item = sockets.by_name(name, halt=halt, panels=False)
        if item is None:
            return None
        else:
            return item.bitem

    # ----------------------------------------------------------------------------------------------------
    # Get or create a socket

    def create_socket(self, in_out: str, name: str, socket_type: str,
            panel: str = "", force_create: bool = False, rank: int = 0):
        """ Get a socket or create it if it doesn't exist

        The panel where to create / search the socket is specified both in the name and
        with the panel argument. The full socket path is : panel > name

        The `rank` argument allows to create a socket even if a socket of the same name and
        type already exists.

        > [!IMPORTANT]
        > The method returns a couple (NodeTreeInterfaceSocket, created) to indicate
        > if the socket has been created or not. This is used by the caller to decide
        > if additional initialization stuff is required.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT') : input or output
        - name : name or path for socket
        - socket_type : socket type
        - panel : panel name
        - force_create : create the socket even if an homonym exists
        - rank : rank of the socket to create

        Returns
        -------
        - couple (NodeTreeInterfaceSocket, created) : Socket and True if created
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ----------------------------------------------------------------------------------------------------
        # Ensure target panel exists

        parent_panel = self.create_panel(panel)
        parent_path = self.get_name(parent_panel, path=True, absolute=False, python=False)

        # ----------------------------------------------------------------------------------------------------
        # Does the socket already exist ?

        # Full path
        ranked_name = name if rank == 0 else name + f" {rank}"
        path_name = ranked_name if parent_path == "" else parent_path + " > " + ranked_name

        # Get the socket if exists
        exists = self.get_socket(in_out, path_name, halt=False)

        # Done if not force_create
        if (exists is not None) and (not force_create):
            socket = exists
            if socket.description == DELETION:
                socket.description = ""
            self.move_before_deleted(socket)

            return socket, False

        # ----------------------------------------------------------------------------------------------------
        # We have to create it, let's make sure the parent panels exist

        names = [s.strip() for s in ranked_name.split('>')]
        parent_panel = self.create_panel(' > '.join(names[:-1]), panel=parent_panel)

        # ----- Let's create the socket in the parent panel

        ranked_name = names[-1]
        if rank == 0:
            name = ranked_name
        else:
            name = ranked_name[:-len(str(rank))].strip()

        socket = self.btree.interface.new_socket(name, in_out=in_out, socket_type=socket_type, parent=parent_panel)
        self.move_before_deleted(socket)

        return socket, True

    # ====================================================================================================
    # Naming utilities

    # ----------------------------------------------------------------------------------------------------
    # Get socket names

    def get_sockets_names(self, in_out: str, python: bool = False, homonyms: str = 'MERGE'):
        """ Returns the dictionary of argument names to use in a python function.

        This function is used to define the calling function arguments or user names in dicts.

        > [!IMPORTANT]
        > Several names are possible if we take into account the paths. The shortes name
        > is privilegied and is considered as the default name. Other possible names are
        > returned in homonyms. Names and homonyms are operated thourgh the `homonyms` argument.

        The example below is with `python=True`:
        - Socket -> "socket"
        - Ambiguous (S) -> "ambiguous"
        - Panel
          - Socket -> "panel_socket"
          - Other -> "other", homonyms = "panel_other"
        - Ambiguous (P)
          - Socket -> "ambiguous_socket" (and not ambiguous_1_socket)

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - python : python name rather than user name
        - homonyms (str in ('NO', 'SEPARATE', 'MERGE')) : how to manage names and homonyms

        Returns
        -------
        - dict (argument_name -> identifier) or couple of dicts : arguments names with optional homonyms names
        """

        names = {}
        homos = {}
        sockets = self.sockets(in_out)
        for item in sockets.iterate(panels=False):
            uniques = item.unique_names(False, python)
            names[uniques[0]] = item.bitem
            for name in uniques[1:]:
                homos[name] = item.bitem

        if homonyms == 'MERGE':
            return {**names, **homos}
        elif homonyms == 'NO':
            return names
        elif homonyms == 'SEPARATE':
            return names, homos
        else:
            raise TypeError(f"get_socket_names error: 'homonyms' argument must be in ('MERGE', 'NO', 'SEPARATE')")

    # ----------------------------------------------------------------------------------------------------
    # Get the panel of a socket

    def get_socket_panel_path(self, identifier: str, python: bool = False):
        """ Get the panel path of the socket

        Arguments
        ---------
        - identifier : socket identifier
        - python : python name rather than user name

        Returns
        -------
        - str : path of the socket
        """

        socket = self.by_identifier(identifier)
        if socket.parent.name == "":
            return ""

        sockets = self.sockets_for(socket)
        return sockets.search_bitem(socket.parent).path(absolute=False, python=python)

    # ====================================================================================================
    # Copy panel / socket into another tree

    def copy_to(self, item, target_tree, panel: str = ""):
        """ Copy socket / panel into another tree

        > [!NOTE]
        > If item is None, only the panel is created

        Arguments
        ---------
        - item (NodeTreeInterfaceitem) : the item to copy
        - target_tree (NodeTree) : the tree to create in
        - panel : panel in the target tree

        Returns
        -------
        - NodeTreeInterfaceItem : the created item
        """

        target_ti = TreeInterface(target_tree)

        # ----- Get the hierarchy of parent panels

        parents = []
        parent = item.parent
        while parent.name != "":
            parents.append(parent)
            parent = parent.parent

        # ----- Create in the parent panels
        target_panel = panel
        for parent in reversed(parents):
            target_ti.create_panel(parent.name, tip=parent.description, default_closed=parent.default_closed, panel=target_panel)
            if target_panel == "":
                target_panel = parent.name
            else:
                target_panel += " > " + parent.name

        # ----- Create the socket
        new_socket = target_ti.create_socket(
            in_out      = item.in_out,
            name        = item.name,
            socket_type = item.socket_type,
            panel       = target_panel)

        InterfaceSockets.copy_item_attributes(item, new_socket)

        return new_socket

    # ====================================================================================================
    # Ensure geometry in

    def set_in_geometry(self, name: str | None = None, create: bool = False):
        """ Ensure that the Geometry input socket is the first

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        - create : create the socket if it doesn't exist

        Returns
        -------
        - Geometry socket
        """

        if name is None:
            name = "Geometry"

        # ------ Look for an input geometry socket
        # Put it in first place if exists

        first = True
        for socket in self.btree.interface.items_tree:
            if socket.item_type == 'PANEL' or socket.in_out == 'OUTPUT':
                continue
            if socket.socket_type == 'NodeSocketGeometry':
                if not first:
                    self.btree.interface.move_to_parent(socket, None, 0)

                return socket

            first = False

        # ----- Not found, let's create it if required

        if not create:
            return None

        socket, _ = self.create_socket('INPUT', name, 'NodeSocketGeometry')

        self.btree.interface.move_to_parent(socket, None, 0)

        return socket

    # ----------------------------------------------------------------------------------------------------
    # Ensure geometry out

    def set_out_geometry(self, name=None):
        """ Make sure the tree has an output geometry and that it is the first one

        If the tree has no output Geometry socket, one is created

        Arguments
        ---------
        - name : socket name, 'Geometry' if None

        Returns
        -------
        - Geometry socket
        """

        if name is None:
            name = 'Geometry'

        first = True
        for socket in self.btree.interface.items_tree:
            if socket.item_type == 'PANEL' or socket.in_out == 'INPUT':
                continue

            if socket.socket_type == 'NodeSocketGeometry':
                if not first:
                    self.btree.move_to_parent(socket, None, 0)

                if socket.description == DELETION:
                    socket.description = ""

                return socket

            first = False

        socket, _ = self.create_socket('OUTPUT', name, 'NodeSocketGeometry')

        print(socket, socket.in_out)
        self.btree.interface.move_to_parent(socket, None, 0)

        return socket

    # =============================================================================================================================
    # Link from node

    def create_from_node(self,
            node        : 'Node',
            include     : list[str] | str = None,
            exclude     : list[str] | str = [],
            create      : bool            = True,
            input_node  : 'Node'          = None,
            panel       : str             = ""):
        """ Plug the output sockets of an input node into the input sockets of the provided node.

        The primary purpose is to create one input socket in the tree for each input socket of the
        provided node.

        If the `input_node` is provided, the created / existing sockets are plugged into the node.

        `include` and èxclude` arguments allow to limit to (`include`) or exclude some (`exclude`)
        sockets.

        > [!NOTE]
        > `include` and `exclude` contain paths for Panel or Socket. When it is a Panel, all the content
        > is included / excluded.

        If `create` argument is False, no socket is created. In that case, only existing entries in `input_node`
        are linked to the node. If `input_node` is None, nothing appends !

        `panel` argument defines the panel where to create the sockets.

        ``` python
        with GeoNodes("Connect several sockets"):

            # Node with 'Value' output socket
            a = Node("Grid")

            # Create Group inputs to feed the node
            # 'Size X' and 'Size Y' are created in the group input not
            # 'Vertices X' and 'Vertices Y' are connected to the same 'Vertices' which is created
            a.link_from(rename={'Vertices X': 'Vertices', 'Vertices Y': 'Vertices'})

            a = Node("Math")

            # Connect the 'Value' output socket to the 'Value' input socket
            # The third socket is exclude by its index
            # Input values are renamed 'First' and 'Second'
            a.link_from(exclude=2, rename={'Value': 'First', 'Value_001': 'Second'})

            b = Node("Math", operation='SQRT')

            # Plug the previous math node on a single socket
            b.link_from(a, include='Value')

        # Call this method when creating a group
        # Note: the previous Group is called using functional syntax with G class

        with GeoNodes("Create default"):

            # Create the sockets in the input and connect them to Group input

            a = G.connect_several_sockets(link_from='TREE')

        with GeoNodes("Create selection"):

            # Create the sockets in the input and connect them to Group input

            a = G.connect_several_sockets(link_from={'exclude': ["Size X", "Size Y"], 'rename': {"Vertices": "Count"}})
        ```

        Arguments
        ---------
        - node : the node to copy input sockets from
        - include : connects only the sockets in the list
        - exclude : exclude sockets in this list
        - create : create the output sockets in node if it is a 'Group Input Node'
        - input_node : an Group Input Node of the tree to link sockets from
        - panel : panel name to create, use tree default name if None
        """

        if node is None:
            return

        # ----------------------------------------------------------------------------------------------------
        # Include and exclude as lists

        if include is not None and isinstance(include, str):
            include = [include]
        if isinstance(exclude, str):
            exclude = [exclude]

        # ----------------------------------------------------------------------------------------------------
        # If the node as no tree (not a Group Node), we simply connect to the node input sockets

        target_tree = getattr(node, 'node_tree', None)

        if target_tree is None:
            counters = {}
            for in_socket in node.inputs:
                if not in_socket.enabled:
                    continue

                # ----- Rank of the name

                name = in_socket.name if (in_socket.label is None or in_socket.label == "") else in_socket.label
                name = utils.snake_case(name)
                if name in counters:
                    rank = counters[name]
                    counters[name] += 1
                    name += f"_{rank}"
                else:
                    rank = 0
                    counters[name] = 1

                # ----- In include or exclude

                if (include is not None) and (name not in include):
                    continue
                if name in exclude:
                    continue

                # ----- Create the socket

                socket_type = constants.SOCKET_SUBTYPES[in_socket.bl_idname][0]
                new_socket, _ = self.create_socket('INPUT', in_socket.name, socket_type=socket_type, panel=panel, rank=rank)
                #InterfaceSockets.copy_item_attributes(item.bitem, new_socket)

                if input_node is not None:
                    out_socket = input_node.outputs[new_socket.identifier]
                    self.btree.links.new(in_socket, out_socket)

            return

        # ----------------------------------------------------------------------------------------------------
        # The node is a group, we use a TreeInterface

        target_interface = TreeInterface(target_tree)
        sockets = target_interface.input_sockets

        # Include list

        if include is None:
            sockets.selected = True
        else:
            sockets.selected = False
            for name in include:
                sockets.by_name(name, halt=True).selected = True

        # Exclude list

        for name in exclude:
            sockets.by_name(name, halt=True).selected = False

        # ----- Create the sockets for the selection

        for item in sockets.iterate():
            if item.is_top or not item.selected:
                continue

            full_name = item.selected_path
            if item.is_panel:
                new_panel = self.create_panel(full_name, tip=item.bitem.description, default_closed=item.bitem.default_closed, panel=panel)
            else:
                new_socket, _ = self.create_socket('INPUT', full_name, socket_type=item.bitem.socket_type, panel=panel)
                InterfaceSockets.copy_item_attributes(item.bitem, new_socket)

                if input_node is not None:
                    in_socket  = node.inputs[item.bitem.identifier]
                    out_socket = input_node.outputs[new_socket.identifier]
                    self.btree.links.new(in_socket, out_socket)

    # =============================================================================================================================
    # Tests

    @classmethod
    def get_test_btree(cls, name):
        btree = bpy.data.node_groups.get(name)
        if btree is None:
            btree =  bpy.data.node_groups.new(name, type='GeometryNodeTree')
            btree.is_modifier = True
        return btree

    @classmethod
    def get_test_node(cls, btree, bl_idname):
        for node in btree.nodes:
            if node.bl_idname == bl_idname:
                return node
        return btree.nodes.new(bl_idname)

    @classmethod
    def test_panels(cls, tree_name="Test Panels"):

        btree = cls.get_test_btree(tree_name)
        btree.nodes.clear()
        ti = cls(btree)
        ti.clear(True)

        print('-'*60)
        print("Test Panels")
        print()

        panel1 = ti.create_panel("First")
        panel2 = ti.create_panel("Second")
        panel3 = ti.create_panel("Sub", panel="First")
        panel4 = ti.create_panel("Sub", panel=panel2)
        panel5 = ti.create_panel("New > Panel", panel="First")

        ti.set_out_geometry()

        print(repr(ti.input_sockets))
        print()

    @classmethod
    def test_sockets(cls, tree_name="Test Sockets"):

        btree = cls.get_test_btree(tree_name)
        btree.nodes.clear()
        ti = cls(btree)
        ti.clear(True)

        print('-'*60)
        print("Test Sockets")
        print()

        ti.create_socket('INPUT', "Socket", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Socket", 'NodeSocketFloat', rank=1)
        ti.create_socket('INPUT', "Socket", 'NodeSocketFloat', panel="Panel")
        ti.create_socket('INPUT', "Other > Socket", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Other > Socket", 'NodeSocketFloat', panel="Panel")
        ti.create_socket('INPUT', "Panel > Other > Single", 'NodeSocketFloat')

        ti.set_out_geometry()

        print(repr(ti.input_sockets))
        print()

        print("Accessing sockets...")
        for name in ['socket', 'Socket', 'socket_1', 'Socket 1', 'other_socket', 'Other > Socket',
            'single', 'Single', 'other_single', 'Other > Single', 'panel_other_single', 'Panel>Other>Single']:
                socket = ti.get_socket('INPUT', name)
                print(f"{name:20s} -> {ti.get_name(socket, path=True)}")

        print()
        print("Accessing panels...")
        for name in ['Panel', 'panel', 'Other', 'other', 'Panel > Other', 'panel_other']:
            panel = ti.get_panel(name)
            print(f"{name:20s} -> {ti.get_name(panel, path=True)}")




    @classmethod
    def test_changes(cls, tree_name="Test Changes"):

        btree = cls.get_test_btree(tree_name)
        btree.nodes.clear()
        ti = cls(btree)
        ti.clear(True)

        print('-'*60)
        print("Test Changes")
        print()

        ti.create_socket('INPUT', "Socket C", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Socket B", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Socket A", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Panel > Socket C", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Panel > Socket B", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Panel > Socket A", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Other > Socket C", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Other > Socket B", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Other > Socket A", 'NodeSocketFloat')

        ti.set_out_geometry()

        ti.mark_for_deletion()
        ti.create_socket('INPUT', "Other > Socket A", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Other > Socket C", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Panel > Socket A", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Panel > Socket C", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Socket A", 'NodeSocketFloat')
        ti.create_socket('INPUT', "Socket C", 'NodeSocketFloat')

        ti.clear(False)

        print(repr(ti.input_sockets))
        print()

    @classmethod
    def test_links(cls, tree_name="Test Links"):

        btree = cls.get_test_btree(tree_name)
        btree.nodes.clear()
        ti = cls(btree)
        ti.clear(True)

        print('-'*60)
        print("Test Links")
        print()

        input_node = btree.nodes.new(type='NodeGroupInput')

        node = btree.nodes.new(type='ShaderNodeMath')
        ti.create_from_node(node=node, include=None, exclude=[], create=True, input_node=input_node)

        node = btree.nodes.new(type='ShaderNodeMath')
        ti.create_from_node(node=node, include=None, exclude=[], create=True, input_node=input_node, panel='Math')

        # ----- Group

        sub_tree = cls.get_test_btree(tree_name + ' SUB')
        sub_tree.nodes.clear()
        sub_ti = cls(sub_tree)
        sub_ti.clear(True)

        sub_ti.create_socket('INPUT', "Socket A", 'NodeSocketFloat')
        sub_ti.create_socket('INPUT', "Socket B", 'NodeSocketFloat')
        sub_ti.create_socket('INPUT', "Panel > Socket A", 'NodeSocketFloat')
        sub_ti.create_socket('INPUT', "Panel > Socket B", 'NodeSocketFloat')

        sub_ti.set_out_geometry()

        # ----- Link with group

        node = btree.nodes.new(type='GeometryNodeGroup')
        node.node_tree = sub_tree
        ti.create_from_node(node=node, include=None, exclude=[], create=True, input_node=input_node)

        node = btree.nodes.new(type='GeometryNodeGroup')
        node.node_tree = sub_tree
        ti.create_from_node(node=node, include='Panel', exclude=[], create=True, input_node=input_node, panel='Include')

        node = btree.nodes.new(type='GeometryNodeGroup')
        node.node_tree = sub_tree
        ti.create_from_node(node=node, include=None, exclude='Panel', create=True, input_node=input_node, panel='Exclude')

        node = btree.nodes.new(type='GeometryNodeGroup')
        node.node_tree = sub_tree
        ti.create_from_node(node=node, include='Panel', exclude='panel_socket_b', create=True, input_node=input_node, panel='Sockets')

        print(repr(ti.input_sockets))
        print()

















# =============================================================================================================================
# Tree Interface

class TreeInterface_OLD:

    def __init__(self, btree):
        """ Acces to tree interface

        This class allows to create and manage panels and socket interface

        Arguments
        ---------
        - btree : Blender Tree
        """
        self.btree = btree

    def __str__(self):
        in_count = len([item for item in self.btree.interface.items_tree if item.item_type == 'SOCKET' and item.in_out == 'INPUT'])
        out_count = len([item for item in self.btree.interface.items_tree if item.item_type == 'SOCKET' and item.in_out == 'OUTPUT'])
        panel_count = len([item for item in self.btree.interface.items_tree if item.item_type == 'PANEL'])
        return f"<TreeInterface of '{self.btree.name}': {panel_count} panel(s), {in_count} input socket(s), {out_count} output socket(s)>"

    def __repr__(self):
        s = f"{str(self)}\n- "

        names = self.get_unique_names('INPUT', False)
        s += "\n- ".join(names)

        return s + "\n"

    # ====================================================================================================
    # Clearing

    def clear(self, all=True):
        """ Clear all sockets
        """
        if all:
            self.btree.interface.clear()

        else:
            to_delete = []
            for item in self.btree.interface.items_tree:
                if item.description == DELETION:
                    to_delete.append(item)
            for item in to_delete:
                self.btree.interface.remove(item)

    def set_tip_delete(self):
        """ Mark all sockets to be deleted
        """
        for item in self.btree.interface.items_tree:
            if item is None:
                continue
            item.description = DELETION

    # ====================================================================================================
    # Utilities

    #def move_socket_to(self, socket, index):
    def move_to(self, item, index, parent=None):
        """ NodeTreeInterface move and move_to_parent are apparently bugged
        (At least they behave strangely)

        From Blender 4.4 : a panel can be moved and not only a socket

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : item to move
        - index (int) : target index within its parent
        - parent (NodeTreeInterfacePanel = None) : where to move the item, None to stay withi the current paren

        Returns
        -------
        - NodeTreeInterfaceItem : the moved item
        """

        # ----------------------------------------------------------------------------------------------------
        # Change the parent if the parent is provided

        if parent is not None:
            self.btree.interface.move_to_parent(item, parent, 0)
            if index == 0:
                return item

        # ----------------------------------------------------------------------------------------------------
        # Move within the parent

        parent = item.parent
        if (item.item_type == 'PANEL') or (item.item_type == 'SOCKET' and item.in_out == 'INPUT'):
            items = [itm for itm in self.btree.interface.items_tree if itm.item_type == 'PANEL' or itm.in_out == 'INPUT']
        else:
            items = [itm for itm in self.btree.interface.items_tree if itm.item_type != 'PANEL' and itm.in_out == 'OUTPUT']

        print("ITEMS", items)

        cur_index = items.index(item)
        if cur_index == index:
            return item

        del items[cur_index]
        items.insert(index, item)

        for itm in reversed(items):
            if parent is None:
                self.btree.interface.move(itm, 0)
            else:
                self.btree.interface.move_to_parent(itm, parent, 0)

        return item

        # OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD

        parent = socket.parent
        panel = parent.name
        sockets = self.get_items('SOCKET', socket.in_out, panel=panel)

        cur_index = sockets.index(socket)
        if cur_index == index:
            return socket

        del sockets[cur_index]
        sockets.insert(index, socket)

        for sock in reversed(sockets):
            if parent is None:
                self.btree.interface.move(sock, 0)
            else:
                self.btree.interface.move_to_parent(sock, parent, 0)

        return socket

    # ====================================================================================================
    # Unique names

    def get_unique_names(self, in_out, as_argument=True, include_homonyms='MERGE'):
        """ Get the unique names of the sockets

        Sockets and panels can share the same names. To avoid homonyms, the names are suffixed
        by an index when necessary.
        Sockets can be prefixed by the name of their panel.

        Panel prefix is not mandatory if there is no homonym at top level.

        Imagine we have the following structure:
        - Integer : integer (or _integer)
        - Float : float (or _float)
        - Integer : integer_1 (or _integer_1)
        - Panel : panel
          - String : string (the only socket named String, panel_string is also valid)
          - Integer : panel_integer
          - Float : panel_float
          - Boolean : panel_boolean (because Boolean exists in another panel)
        - Panel : panel_1
          - Integer : panel_1_integer
          - Integer : panel_1_integer_1
          - Boolean : panel_1_boolean

        > [!NOTE]
        > geonodes doesn't create panels sharing the same name. But a Group can be created where
        > it is the case.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - as_argument (bool = True) : return snake_case rather than keeping caps
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ----------------------------------------------------------------------------------------------------
        # snake_case or not

        def snake_case(name):
            if as_argument:
                return utils.snake_case(name)
            else:
                return name

        sepa = '_' if as_argument else ' > '

        # ----------------------------------------------------------------------------------------------------
        # Let's start by naming the panels

        names  = [""]
        panels = [None]
        for item in self.btree.interface.items_tree:

            if item.item_type != 'PANEL':
                continue

            names.append(snake_case(item.name))
            panels.append(item)

        panel_names = {k: v for k, v in zip(utils.ensure_uniques(names, single_digit=True), panels)}

        # ----------------------------------------------------------------------------------------------------
        # List of the sockets in each panel

        panels = {}
        for panel_name, panel in panel_names.items():

            socket_names = []
            sockets      = []
            for item in self.btree.interface.items_tree:
                if item.item_type != 'SOCKET' or item.in_out != in_out:
                    continue
                if (panel_name == "" and item.parent.name != ""):
                    continue
                if panel_name != "" and item.parent != panel:
                    continue

                socket_names.append(snake_case(item.name))
                sockets.append(item)

            panels[panel_name] = {'raw_sc': socket_names, 'uniques': utils.ensure_uniques(socket_names, single_digit=True), 'sockets': sockets}

        # ----------------------------------------------------------------------------------------------------
        # Final dictionary with two entries per socket
        # - The short version without panel prefix (when possible)
        # - The long version with panel prefix

        names = {}
        homonyms = {}
        for panel_name, dicts in panels.items():
            for raw_sc, unique, socket in zip(dicts['raw_sc'], dicts['uniques'], dicts['sockets']):

                if panel_name == "":
                    names[unique] = socket
                    if as_argument:
                        homo = snake_case(sepa + unique)
                        # Could be equal when socket starts with a figure
                        if homo != unique:
                            homonyms[homo] = socket

                else:
                    # Short version ?
                    single = True
                    for p_name, p_dicts in panels.items():
                        if p_name == panel_name:
                            continue
                        if unique in p_dicts['uniques']:
                            single = False
                            break

                    if single:
                        names[unique] = socket
                        # Could be equal if unique starts with a figure
                        homo = snake_case(panel_name + sepa + unique)
                        if homo not in names:
                            homonyms[homo] = socket
                    else:
                        names[snake_case(panel_name + sepa + unique)] = socket

        if include_homonyms == 'MERGE':
            return {**names, **homonyms}
        elif include_homonyms == 'NO':
            return names
        elif include_homonyms == 'SEPARATE':
            return names, homonyms
        else:
            raise TypeError(f"include_homonyms must be in ('MERGE', 'NO', 'SEPARATE')")

    # ====================================================================================================
    # Get individual items

    # ----------------------------------------------------------------------------------------------------
    # Get a panel by its name

    def get_panel(self, name: str, halt: bool = True):
        """ Get a panel by its name

        Arguments
        ---------
        - name : panel name, can be true name or the snake case version
        - halt : raise an exception if not found

        Raises
        ------
        - AttributeError : if panel not found

        Returns
        -------
        - panel
        """
        if name == "" or name is None:
            return None

        panels = []
        for item in self.btree.interface.items_tree:
            if item.item_type == 'PANEL':
                if item.name == name:
                    return item
                panels.append(item.name)

        if halt:
            raise AttributeError(f"Panel '{name}' not found in {panels}")

        return None

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its identifier

    def by_identifier(self, identifier):
        for item in self.btree.interface.items_tree:
            if item.item_type == 'SOCKET' and item.identifier == identifier:
                return item

        raise NodeError(f"TreeInterface socket with identifier '{identifier}' not found in tree '{self.btree.name}'.")

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its socket name

    def by_name(self, in_out, name, as_argument=True, halt=True):
        """ Get the socket by its name

        Arguments
        ---------
        - in_out (str) : str in ('INPUT', 'OUTPUT')
        - name (str) : searched named
        - as_argument (bool = True) : the name is argument or socket name
        - halt (bool = False) : raises an error if not found

        Returns
        -------
        - Node, Interface socket or list of sockets depending on the arguments
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        if as_argument:
            socket_name = name

        else:
            parts = name.split('>')
            if len(parts) == 2:
                socket_name = parts[0].strip() + ' > ' + parts[1].strip()
            else:
                socket_name = name

        names = self.get_unique_names(in_out=in_out, as_argument=as_argument)
        socket = names.get(socket_name)

        if socket is None and halt:
            raise NodeError(f"{in_out} socket '{name}' not found in '{self.btree.name}'.", valids=list(names.keys()))

        return socket

    # ====================================================================================================
    # Get or create a socket

    def get_create_socket(self, in_out, name, socket_type, panel="", force_create=False):
        """ Get a socket or create it if if doesn't exist

        Returns
        -------
        - couple socket, created : Socket and True if created
        """
        assert(in_out in ('INPUT', 'OUTPUT'))

        if panel is None:
            panel = ""

        # ----------------------------------------------------------------------------------------------------
        # Ensure the panel exists

        parent = self.create_panel(panel)
        if parent is not None:
            parent.description = ""

        # ----------------------------------------------------------------------------------------------------
        # Search the name in the list of sockets

        insertion_index = 0
        socket_index = None
        socket = None

        index = 0
        for item in self.btree.interface.items_tree:
            if item.item_type == 'PANEL' or item.in_out != in_out:
                continue
            if item.parent.name != panel:
                continue

            # ----- Found
            if (not force_create) and (item.name == name) and (item.socket_type == socket_type):
                socket_index = index
                socket = item
                if insertion_index is None:
                    insertion_index = socket_index
                break

            # ---- First unused entry
            if item.description != DELETION:
                insertion_index += 1

        # ----------------------------------------------------------------------------------------------------
        # Not found : we create it

        if socket is None:
            socket = self.btree.interface.new_socket(name, in_out=in_out, socket_type=socket_type, parent=parent)
            created = True
        else:
            # Suppress the deletion marker
            socket.description = ""
            created = False

        if socket.description == DELETION:
            socket.description = ""

        # ----------------------------------------------------------------------------------------------------
        # Let's locate the socket at the right position

        if True:
            self.move_to(socket, insertion_index)
        else:
            self.move_socket_to(socket, insertion_index)

        # ----------------------------------------------------------------------------------------------------
        # Done

        return socket, created

    # ====================================================================================================
    # Get list of items

    # ----------------------------------------------------------------------------------------------------
    # Get items of a certain category

    def get_items(self, item_type, in_out, panel = None):
        """ Get items matching the criteria passed in arguments

        Arguments
        ---------
        - item_type (str in ('PANEL', 'SOCKET')) : item type
        - in_out (str in ('INPUT', 'OUTPUT') : Input or output for sockets
        - panel (panel name) : the panel the items belong to

        Returns
        -------
        - list : list of items
        """
        items = []
        for item in self.btree.interface.items_tree:

            if item.item_type != item_type:
                continue

            if item_type == 'SOCKET':
                if item.in_out != in_out:
                    continue

                if panel is not None:
                    if isinstance(panel, str):
                        if item.parent.name != panel:
                            continue
                    elif item.parent != panel:
                        continue

            items.append(item)

        return items

    # ====================================================================================================
    # Create a panel

    def create_panel(self, name: str, tip: str="", closed_by_default=False):
        """ Create a panel

        > [!NOTE]
        > The panel is not created if a panel with the same name already exists

        Arguments
        ---------
        - name : panel name
        - tip : description

        Returns
        -------
        - Panel
        """
        if name is None or name == "":
            return None

        panel = self.get_panel(name, halt=False)
        if panel is not None:
            panel.default_closed = closed_by_default
            return panel

        return self.btree.interface.new_panel(name, description=tip, default_closed=closed_by_default)

    # ====================================================================================================
    # Ensure geometry in

    def set_in_geometry(self, name: str | None = None, create: bool = False):
        """ Ensure that the Geometry input socket is the first

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        - create : create the socket if it doesn't exist
        """

        if name is None:
            name = "Geometry"

        sockets = self.get_items('SOCKET', 'INPUT', panel="")
        geo = None
        for socket in sockets:
            if socket.socket_type == 'NodeSocketGeometry':
                geo = socket
                break

        if geo is None:
            if not create:
                return None
            geo, _ = self.get_create_socket('INPUT', name, 'NodeSocketGeometry', panel="")

        self.btree.interface.move_to_parent(geo, None, 0)
        return geo

    # ----------------------------------------------------------------------------------------------------
    # Ensure geometry out

    def set_out_geometry(self, name=None):
        """ Make sure the tree has an output geometry and that it is the first one

        If the tree has no output Geometry socket, one is created

        Arguments
        ---------
        - name : socket name, 'Geometry' if None
        """
        for nm, s in self.get_unique_names('OUTPUT', as_argument=False, include_homonyms='NO').items():
            if s.socket_type == 'NodeSocketGeometry':
                if name is None or nm == name:
                    if True:
                        self.move_to(s, 0)
                    else:
                        self.move_socket_to(s, 0)
                    if s.description == DELETION:
                        s.description = ""
                    return

        if name is None:
            name = "Geometry"

        geo, _ = self.get_create_socket('OUTPUT', name, 'NodeSocketGeometry', panel="")
        self.btree.interface.move_to_parent(geo, None, 0)
        return geo

    # ====================================================================================================
    # Tests

    def demo_create_all_sockets(self):

        blids = ('NodeSocketString', 'NodeSocketBool', 'NodeSocketMaterial', 'NodeSocketVector', 'NodeSocketInt', 'NodeSocketMenu',
            'NodeSocketCollection', 'NodeSocketGeometry', 'NodeSocketTexture', 'NodeSocketFloat', 'NodeSocketColor',
            'NodeSocketObject', 'NodeSocketRotation', 'NodeSocketMatrix', 'NodeSocketImage')

        out_sockets={}
        for blid in blids:
            out_sockets[blid] = self.create_in_socket(blid[10:], blid)

        input_node = self.btree.nodes.get('Group Input')

        # ===== Menu

        if input_node is not None:
            menu_node   = self.btree.nodes.new('GeometryNodeMenuSwitch')
            menu_socket = input_node.outputs['Menu']
            self.btree.links.new(menu_socket, menu_node.inputs[0])
