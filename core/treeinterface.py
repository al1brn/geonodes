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


import bpy
from . import blender
from . import utils
from . import constants
from .sockettype import SocketType
from .signature import Signature
from typing import Literal

from bpy.types import NodeTree, NodeTreeInterfaceSocket, NodeTreeInterfacePanel, NodeTreeInterfaceItem

import numpy as np
from . scripterror import NodeError

DELETION = '__deletion marker__'

IN_OUT = Literal['INPUT', 'OUPUT']
BOTH   = Literal['INPUT', 'OUPUT', 'BOTH']
ITYPE  = Literal['SOCKET', 'PANEL']

# ====================================================================================================
# Utilities
# ====================================================================================================

def check_in_out(in_out, both=False):
    if in_out in ('INPUT', 'OUTPUT'):
        return True
    elif in_out == 'BOTH' and both:
        return True
    
    raise RuntimeError(f"in_out argument '{in_out}' not in ('INPUT', 'OUTPUT')")
    

# ====================================================================================================
# Item Path
# ====================================================================================================

class ItemPath:

    def __init__(self, value: str | list | NodeTreeInterfaceItem):

        __slots__ = ('_path', '_socket_id')

        """ A panel name wraps the different ways to name a panel.

        A panel can be addressed:
        - with a path : Top Panel > Panel_1 > Sub Panel
        - with a list : [('Top Panel', 0), ('Panel', 1), ('Sub Panel', 0)]

        The class can be initialized from a NodeTreeInterfaceItem, from a path or
        from a list.

        Arguments
        ---------
        - value (str | list | NodeTreeInterfaceItem) : the panel to initiaize
        """

        self._path      = ""
        self._socket_id = None

        if value is None:
            return

        # ---------------------------------------------------------------------------
        # str : "top > sub_1 > another sub
        # ---------------------------------------------------------------------------

        if isinstance(value, str):

            # Make sure path is normalized
            self._path = ItemPath.stack_to_path(ItemPath.path_to_stack(value))
            
        # ---------------------------------------------------------------------------
        # ItemPath
        # ---------------------------------------------------------------------------
        
        elif isinstance(value, ItemPath):
            self._path      = value.path
            self._socket_id = value.socket_id

        # ---------------------------------------------------------------------------
        # Couple path, socket_id
        # ---------------------------------------------------------------------------
        
        elif isinstance(value, tuple) and len(value) == 2:
            self._path      = ItemPath(value[0]).path
            self._socket_id = None if value[1] is None else SocketType(value[1]).socket_id

        # ---------------------------------------------------------------------------
        # NodeTreeInterfaceItem
        # ---------------------------------------------------------------------------

        elif isinstance(value, NodeTreeInterfaceItem):

            # Up to the top
            stack = []

            cur_item = value
            while cur_item.index != -1:

                parent = cur_item.parent
                rank = 0
                for item in parent.interface_items:
                    if item == cur_item:
                        break

                    if item.name != cur_item.name or item.item_type != cur_item.item_type:
                        continue

                    if cur_item.item_type == 'SOCKET':
                        if item.in_out != cur_item.in_out or item.socket_type != cur_item.socket_type:
                            continue

                    rank += 1

                # Bottom of the list
                stack.insert(0, (item.name, rank))

                # Next
                cur_item = parent

            self._path = ItemPath.stack_to_path(stack)
            self._socket_id = None if value.item_type != 'SOCKET' else value.socket_type

        # ---------------------------------------------------------------------------
        # Stack of panels
        # ---------------------------------------------------------------------------

        elif isinstance(value, list):
            self._path = ItemPath.stack_to_path(value)

        else:
            raise NodeError(
                f"The value '{value}' can't be used as socket name.\n"
                "Make sure to use the right argument when calling the method."
                )
        
    def __str__(self):
        return self.path
    
    @property
    def path(self):
        return self._path
    
    @property
    def socket_id(self):
        return self._socket_id
    
    @property
    def key(self):
        if self._socket_id is None:
            return self.path
        else:
            return (self.path, self.socket_id)

    # ====================================================================================================
    # Conversions
    # ====================================================================================================

    @staticmethod
    def to_item_path(value):
        if isinstance(value, ItemPath):
            return value
        else:
            return ItemPath(value)

    # ----------------------------------------------------------------------------------------------------
    # Path to list of couples
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def path_to_stack(path: str) -> list:
        """ Return a list of (name, rank).

        Arguments
        ---------
        - path (str) : panel path

        Returns
        -------
        - list of couples (name, rank)
        """

        stack = []
        
        for token in path.split(">"):
            raw = token.strip()
            a = raw.split('_')
            rank = 0
            if len(a) > 1:
                n = a[-1]
                if n.isnumeric():
                    rank = int(n)
                    a.pop()
            
            name = "_".join(a)
            stack.append((name, rank))

        return stack
    
    # ----------------------------------------------------------------------------------------------------
    # Stack to path
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def stack_to_path(stack: list) -> str:
        """ Convert a stack of couples (name, rank) to path.

        Arguments
        ---------
        - stack (list) : stack of (name, rank)

        Returns
        -------
        - str : panel path
        """
        a = []
        for spec in stack:
            if isinstance(spec, str):
                s = spec.strip()
                if s != "":
                    a.append(spec.strip())

            elif isinstance(spec, tuple) and len(spec) == 2:
                name, rank = spec
                s = name.strip()
                if s == "":
                    continue

                if rank == 0:
                    a.append(s)
                else:
                    a.append(f"{s}_{rank}")
            else:
                raise RuntimeError(f"ItemPath error: invalid parent <{spec}> in stack {stack}.")
        
        return " > ".join(a)
    
    # ====================================================================================================
    # Properties
    # ====================================================================================================
    
    @property
    def is_root(self):
        return self.path == ""

    @property
    def stack(self):
        return ItemPath.path_to_stack(self.path)
    
    @property
    def long_name(self):
        """ Return the path as long name (without '>')
        """
        return " ".join([name for name, _ in self.stack])

    @property
    def ranked_long_name(self):
        """ Return the path as long name (without '>')
        """
        s = self.long_name
        _, rank = self.name_rank
        if rank > 0:
            return f"{s}_{rank}"
        else:
            return s
    
    @property
    def python_path(self):
        return utils.snake_case(self.path)
    
    @property
    def parent(self):
        if self.path == "":
            return ItemPath(None)
        else:
            return ItemPath(self.stack[:-1])

    @property
    def name_rank(self):
        if self.path == "":
            return None, 0
        else:
            return self.stack[-1]

    @property
    def name(self):
        return self.name_rank[0]
    
    def get_names(self, use_name: bool = True, use_python: bool = False):
        stack = self.stack
        names = []
        for i in reversed(range(len(stack))):
            name = ItemPath(stack[i:]).path
            if use_name:
                names.append(name)
            if use_python:
                names.append(utils.snake_case(name))

        return names
    
    # ====================================================================================================
    # Does the items match this path
    # ====================================================================================================

    def panel_matches(self, panel):
        if self.socket_id is not None:
            return False
        return self.name in (panel.name, utils.snake_case(panel.name))

    def socket_matches(self, socket):
        if self.name not in (socket.name, utils.snake_case(socket.name)):
            return False
        if self.socket_id is None:
            return True
        else:
            return self.socket_id == socket.socket_type

    # ====================================================================================================
    # Operations
    # ====================================================================================================
    
    def join(self, other):

        if self.socket_id is not None:
            raise RuntimeError(f"The path {self.key} is not a panel. Impossible to join with '{other}'.")
        
        other = ItemPath.to_item_path(other)
        if self.is_root:
            return other
        
        elif other.is_root:
            return self
        
        return ItemPath((">".join([self.path, ItemPath(other).path]), other.socket_id))
    
    def equal_to(self, other):
        return self.key == ItemPath.to_item_path(other).key
    
    def get_relative_to(self, parent):
        """ Get the path relative to the given parent.
        
        The parent path must be shorter that path and be equal.
        
        Arguments
        ---------
        - parent (ItemPath) : parent panel
        
        Returns
        -------
        - ItemPath : path relative to the parent
        """
        parent_path = ItemPath.to_item_path(parent)
        if parent.socket_id not in [None, ""]:
            raise RuntimeError(f"The path {parent_path.key} is not a panel. Impossible to get relative path of '{self}'.")

        if parent_path.is_root:
            return self
        
        if self.path.startswith(parent_path.path):
            return ItemPath((self.path[len(parent_path.path):], self.socket_id))
        else:
            return self

    
    # ====================================================================================================
    # Operations
    # ====================================================================================================
    
    def __add__(self, other):
        return self.join(other)
    
    def __radd__(self, other):
        return ItemPath.to_item_path(other).join(self)
    
    def __sub__(self, other):
        return self.get_relative_to(other)
    
    def __rsub__(self, other):
        return ItemPath.to_item_path(other).get_relative_to(self)
    
    def __eq__(self, other):
        return self.equal_to(other)
    
    def __neq__(self, other):
        return not self.equal_to(other)
    
# ====================================================================================================
# Tree Interface
# ====================================================================================================

class TreeInterface:

    BIN_PANEL = "SOCKETS_BIN"

    SOCKET_TYPES = {'GeometryNodeTree': [], 'ShaderNodeTree': []}
    SOCKET_PROPS = {'GeometryNodeTree': {}, 'ShaderNodeTree': {}}
    SYNOMNYMS = {
        'default'           : 'default_value',
        'default_attribute' : 'default_attribute_name',
        'tip'               : 'description',
        'min'               : 'min_value',
        'max'               : 'max_value',
        'layer_selection'   : 'layer_selection_field',
        'shape'             : 'structure_type',
        'expanded'          : 'menu_expanded',
    }

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
        self.items_tree = btree.interface.items_tree

        self._dynamic_init()

    # ====================================================================================================
    # Dynamic initialization
    # ====================================================================================================

    def _dynamic_init(self):

        if len(TreeInterface.SOCKET_TYPES[self.btree.bl_idname]):
            return
        
        for d in constants.SOCKETS.values():
            for tt in ('GeometryNodeTree', 'ShaderNodeTree'):
                if d[tt] is not None:
                    TreeInterface.SOCKET_TYPES[tt].append(d[tt])
                    TreeInterface.SOCKET_PROPS[tt][d[tt]] = [prop[0] for prop in d['props'].values()]
        
    @property
    def socket_types(self):
        return self.SOCKET_TYPES[self.btree.bl_idname]

    @property
    def socket_props(self):
        return self.SOCKET_PROPS[self.btree.bl_idname]
    
    @classmethod
    def get_prop_name(cls, prop):
        return cls.SYNOMNYMS.get(prop, prop)

    # ====================================================================================================
    # Dunder methods
    # ====================================================================================================

    def __str__(self):
        return f"<TreeInterface for tree '{self.btree.name}'>"

    def __repr__(self):
        return str(self)

    # ====================================================================================================
    # Panels
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get / create a panel
    # ----------------------------------------------------------------------------------------------------

    def get_panel(self, 
            path    : str | NodeTreeInterfacePanel = "", 
            create  : bool = False):
        """ Get a panel by its name.

        If create is True, the panel is created.
        > [!NOTE]
        > The panel is created only if the parent panels exist

        > [!NOTE]
        > - If the name is `None`, returns `None'.
        > - If If the name is empty, returns the parent panel.

        Both the name and the parent name use `'>'` char as a separator between parent panel names.

        > [!NOTE]
        > When several panels share the same name within a parent, the name can be suffixed by its order
        > starting from 0, for exemple:
        > - First : `"Panel"`
        > - Second : `"Panel_1"`
        > - Third : `"Panel_2`"

        ``` python
        tinf = TreeInterface(...)

        # Create a top panel named "Top"
        panel = tinf.create_panel("Top")

        # Create an homonym "Top"
        panel = tinf.create_panel("Top")

        # Create a sub panel named "Sub"
        sub = tinf.create_panel("Sub", parent="Top")

        # Create a sub panel named "Sub" in the second panel
        sub = tinf.create_panel("Sub 2", parent="Top_1")

        # Get the top panel named "Top"
        panel = tinf.get_panel("Top")

        # Get the sub panel Sub within Panel
        sub_panel = tinf.get_panel("Sub", parent="Top")
        sub_panel = tinf.get_panel("Sub", parent=panel)
        sub_panel = tinf.get_panel("Top_1 > Sub")
        ``` 

        Arguments
        ---------
        - name (str | NodeTreeInterfacePanel = "") : name of the panel
        - parent (str | NodeTreeInterfacePanel = None) : parent panel
        - create (bool = False) : create the panel if is doesn't exist

        Returns
        -------
        - NodeTreeInterfacePanel : None if not found or impossible to create

        """
        # ---------------------------------------------------------------------------
        # Simple cases
        # ---------------------------------------------------------------------------

        if isinstance(path, NodeTreeInterfacePanel):
            return path

        panel_path = ItemPath(path)
        if panel_path.is_root:
            return None

        # ---------------------------------------------------------------------------
        # Loop on the stack
        # ---------------------------------------------------------------------------

        panel_stack = panel_path.stack
        parent_panel = None
        items = self.items_tree
        parent_index = -1

        for name, rank in panel_stack:
            
            # ---------------------------------------------------------------------------
            # Search the rank-th item with the target name
            # ---------------------------------------------------------------------------

            count = rank
            found = None

            for item in items:
                if (item.item_type != 'PANEL') or (item.parent.index != parent_index):
                    continue

                if item.name == name:
                    if count == 0:
                        found = item
                        break
                    count -= 1

            # ---------------------------------------------------------------------------
            # Create if if not found
            # ---------------------------------------------------------------------------

            if found is None:
                if not create:
                    return None
                
                for i in range(count + 1):
                    found = self.btree.interface.new_panel(name)
                    self.btree.interface.move_to_parent(found, parent_panel, 9999)

            # ---------------------------------------------------------------------------
            # Next
            # ---------------------------------------------------------------------------

            parent_panel = found
            items = parent_panel.interface_items
            parent_index = parent_panel.index

        return parent_panel
    
    # ----------------------------------------------------------------------------------------------------
    # Create a panel
    # ----------------------------------------------------------------------------------------------------

    def create_panel(self, 
            name    : str, 
            parent  : str | NodeTreeInterfacePanel = None,
            tip     : str = ""):
        """ Create a new panel within a parent panel.

        Arguments
        ---------
        - name (str) : name of the panel to create
        - parent (str | NodeTreeInterfacePanel = None) : the panel wehre to create the panel
        - tip (str = "") : panel description

        Returns
        -------
        - NodeTreeInterfacePanel : the created panel
        """

        if ItemPath(name).is_root:
            raise AttributeError(f"To create a Panel, a name must be provide.")

        panel_path = ItemPath(parent) + ItemPath(name)
        parent_panel = self.get_panel(panel_path.parent)

        new_panel = self.btree.interface.new_panel(name)
        self.btree.interface.move_to_parent(new_panel, parent_panel, 9999)
        new_panel.description = tip

        return new_panel
    
    # ----------------------------------------------------------------------------------------------------
    # Check if an item belongs to a parent
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def belongs_to(item: NodeTreeInterfaceItem, parent: NodeTreeInterfacePanel=None):
        """ Check if an item belongs to a parent panel

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item to test
        - parent (NodeTreeInterfacePanel = None) : the panel to test

        Returns
        -------
        - True if item is in the panel hierarchy
        """
        parent_path = ItemPath(parent)
        if parent_path.is_root:
            return True

        return ItemPath(item).path.startswith(parent_path.path)
    
    # ====================================================================================================
    # Sockets
    # ====================================================================================================
    
    # ----------------------------------------------------------------------------------------------------
    # Get a socket
    # ----------------------------------------------------------------------------------------------------

    def get_socket(self, 
            in_out      : IN_OUT,
            name        : str | NodeTreeInterfaceSocket, 
            socket_type : str,
            parent      : str | NodeTreeInterfacePanel = None,
            ):
        
        """ Get a socket by its name.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - name (str | NodeTreeInterfaceSocket) : the socket to retrieve
        - socket_type (str) : socket type
        - parent (str | NodeTreeInterfacePanel = None) : the parent panel
        """
        check_in_out(in_out)

        if ItemPath(name).is_root:
            raise AttributeError(f"A name must be provided to get a socket.")
        
        # ---------------------------------------------------------------------------
        # Get the parent panel
        # ---------------------------------------------------------------------------
        
        socket_path = ItemPath(parent) + ItemPath(name)

        if len(socket_path.stack) > 1:
            parent_panel = self.get_panel(socket_path.parent)
            if parent_panel is None:
                return None
            items = parent_panel.interface_items
            parent_index = parent_panel.index
        else:
            items = self.items_tree
            parent_index = -1

        # ---------------------------------------------------------------------------
        # Get the socket within parent
        # ---------------------------------------------------------------------------

        name, rank = socket_path.name_rank
        count = rank
        found = None
        for item in items:

            if (item.item_type != 'SOCKET') or (item.parent.index != parent_index):
                continue
            if item.in_out != in_out:
                continue
            if socket_type is not None:
                if SocketType(socket_type) != item.socket_type:
                    continue

            if item.name == name:
                if count == 0:
                    found = item
                    break
                count -= 1

        return found

    # ----------------------------------------------------------------------------------------------------
    # Create a socket
    # ----------------------------------------------------------------------------------------------------

    def create_socket(self, 
            in_out      : IN_OUT,
            name        : str, 
            socket_type : str | SocketType,
            parent      : str | NodeTreeInterfacePanel = None,
            from_socket : bpy.types.NodeSocket = None,
            **props):
        """ Create a new socket.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - name (str) : name of the socket to create
        - socket_type (str | SocketType) : a valid socket type
        - parent (str | NodeTreeInterfacePanel = None) : the parent panel where to create the socket
        - from_socket (NodeSocket = None) : an existing socket to configure the created socket
        - props (dict) : properties specific to the socket type

        Returns
        -------
        - NodeTreeInterfaceSocket : the created sockets
        """
        check_in_out(in_out)


        NO_MODIFIER_UPDATE = ['NodeSocketMenu']

        # ---------------------------------------------------------------------------
        # Arguments checks
        # ---------------------------------------------------------------------------

        if ItemPath(name).is_root:
            raise AttributeError(f"A name must be provided to get a socket.")
        
        if socket_type is None:
            if from_socket is None:
                raise NodeError(f"create_socket error: None 'socket_type' requires a  valid 'from_socket' argument.")
            
            socket_type = SocketType(from_socket)            
        else:
            socket_type = SocketType(socket_type)

        # ---------------------------------------------------------------------------
        # Creation / recover from bin
        # ---------------------------------------------------------------------------
        
        socket_path = ItemPath(parent) + ItemPath(name)
        parent_panel = self.get_panel(socket_path.parent, create=True)

        # Try to recover from bin
        socket = self.get_socket(in_out, socket_path.name, socket_type=socket_type, parent=TreeInterface.BIN_PANEL)
        created = False

        # Not found, let's create it
        if socket is None:
            socket = self.btree.interface.new_socket(socket_path.name, in_out=in_out, socket_type=socket_type.socket_id, parent=parent_panel)
            created = True

        # Last position in the parent panel
        self.btree.interface.move_to_parent(socket, parent_panel, 9999)

        # ---------------------------------------------------------------------------
        # Properties
        # ---------------------------------------------------------------------------

        if from_socket is not None:
            socket.from_socket(from_socket.node, from_socket)

        for prop, value in props.items():
            
            # Synonyms
            prop = self.get_prop_name(prop)

            if value is None:
                continue

            if prop == 'tip':
                prop = 'description'

            if prop not in self.socket_props[socket_type.socket_id]:
                raise TypeError(f"create_socket error ('{name}', {socket_type}) : socket property '{prop}' is invalid: '{prop}' not in {self.socket_props[socket_type.socket_id]}.")
            
            # Ease the use of subtype
            if prop == 'subtype':
                socket_type.subtype = value
                value = socket_type.subtype

            # Could fail for default_value (Menu for instance)
            if value is not None:
                try:
                    setattr(socket, prop, value)
                except TypeError as e:
                    enums = utils.get_enum_from_string(str(e))
                    if str(value).upper() in enums:
                        setattr(socket, prop, str(value).upper())
                    else:
                        if len(enums):
                            s = f", acceptaed values are {enums}"
                        else:
                            s = ""

                        raise NodeError(
                            f"An error occurred when creating the {SocketType(socket_type).class_name} socket '{name}' .\n"
                            f"The property '{prop}' doesn't accept the value '{value}'{s}.\n{str(e)}\n")

        # ---------------------------------------------------------------------------
        # Update socket default value
        # ---------------------------------------------------------------------------

        if hasattr(socket, 'default_value'):

            # ---------------------------------------------------------------------------
            # Update default value in input node
            # ---------------------------------------------------------------------------

            for node in self.btree.nodes:
                if node.bl_idname != 'NodeGroupInput':
                    continue
                for bsock in node.outputs:
                    if bsock.identifier == socket.identifier:
                        # Could fail for menus
                        try:
                            bsock.default_value = socket.default_value
                        except:
                            pass
                        break
                break

            # ---------------------------------------------------------------------------
            # If created, we must set the modifier value to default value
            # Done when exiting the tree
            # ---------------------------------------------------------------------------

            #if created and hasattr(socket, 'default_value') and socket.socket_type not in NO_MODIFIER_UPDATE:
            #    for mod in blender.get_geonodes_modifiers(self.btree):
            #        try:
            #            mod[socket.identifier] = socket.default_value
            #        except Exception as e:
            #            print(f"Info: impossible to set default value {socket.default_value} to modifier for socket '{socket.name}': {str(e)}")
                            
        return socket
    
    # ----------------------------------------------------------------------------------------------------
    # Get the sockets
    # ----------------------------------------------------------------------------------------------------

    def get_sockets(self,
            in_out: IN_OUT,
            *,
            include: list = None,
            exclude: list = [],
            enabled_only : bool = True,
            #free_only: bool = False,
            parent: NodeTreeInterfaceSocket = None, 
        ):
        """ Get sockets

        Attributes
        ----------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - include (list = None) : limit sockets to list
        - exclude (list = []) : exclude sockets from list
        - enabled_only (bool = True) : only enabled sockets
        - parent (NodeTreeInterfacePanel = None) : path up to the parent

        Returns
        -------
        - list of sockets
        """
        check_in_out(in_out)

        parent_path = ItemPath(parent)

        # ---------------------------------------------------------------------------
        # Panel inclusions and exclusions
        # ---------------------------------------------------------------------------

        # Panels to include
        incl_panels, incl_sockets = None, None

        if include is not None:
            
            incl_panels, incl_sockets = [], []

            for key in include:

                key_path = ItemPath(key)

                if key_path.socket_id is None:
                    panel = self.get_panel(parent_path + key_path, create=False)
                    if panel is not None:
                        incl_panels.append(panel)
                        continue

                socket = self.get_socket(in_out, parent_path + key_path, None)
                if socket is not None:
                    incl_sockets.append(socket.index)
            
            if not len(incl_panels):
                incl_panels = None
            if not len(incl_sockets):
                incl_sockets = None

        # Panels to exclude
        excl_panels, excl_sockets = [], []

        for key in exclude:
            
            key_path = ItemPath(key)

            if key_path.socket_id is None:
                panel = self.get_panel(parent_path + key_path, create=False)
                if panel is not None:
                    excl_panels.append(panel)
                    continue

            socket_path = parent_path + key_path
            socket = self.get_socket(in_out, socket_path.path, socket_path.socket_id)
            if socket is not None:
                excl_sockets.append(socket.index)

        # ---------------------------------------------------------------------------
        # Loop on sockets
        # ---------------------------------------------------------------------------

        sockets = []
        for socket in self.iterate(in_out, panels=False, parent=parent):

            # ---------------------------------------------------------------------------
            # Panel Exclusion / inclusion conditions
            # ---------------------------------------------------------------------------

            ok = True
            for panel in excl_panels:
                if self.belongs_to(socket, panel):
                    ok = False
                    break

            if not ok:
                continue

            if incl_panels is not None:
                ok = False
                for panel in incl_panels:
                    if self.belongs_to(socket, panel):
                        ok = True
                        break
                if not ok:
                    continue

            # ---------------------------------------------------------------------------
            # Socket Exclusion / inclusion conditions
            # ---------------------------------------------------------------------------

            if socket.index in excl_sockets:
                continue

            if (incl_sockets is not None) and (socket.index not in incl_sockets):
                continue

            # ---------------------------------------------------------------------------
            # Socket conditions
            # ---------------------------------------------------------------------------

            #if enabled_only or free_only:
            #    nsock = self.get_node_socket(socket)

            #    if nsock is not None:
            #        if enabled_only and not nsock.enabled:
            #            continue
            #        if in_out == 'INPUT' and free_only and not utils.is_free(nsock):
            #            continue

            # ---------------------------------------------------------------------------
            # We can add it in the list
            # ---------------------------------------------------------------------------

            sockets.append(socket)

        return sockets
        
    
    # ====================================================================================================
    # Input and output geometry
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Geometry input socket
    # ----------------------------------------------------------------------------------------------------

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
        for socket in self.iterate('INPUT', panels=False):
            if socket.socket_type == 'NodeSocketGeometry':
                if not first:
                    self.btree.interface.move_to_parent(socket, None, 0)

                return socket

            first = False

        # ----- Not found, let's create it if required

        if not create:
            return None

        socket = self.create_socket('INPUT', name, 'NodeSocketGeometry')

        self.btree.interface.move_to_parent(socket, None, 0)

        return socket
    
    # ----------------------------------------------------------------------------------------------------
    # Geometry output socket
    # ----------------------------------------------------------------------------------------------------

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
        for socket in self.iterate('OUTPUT', panels=False):

            if socket.socket_type == 'NodeSocketGeometry':
                if not first:
                    self.btree.interface.move_to_parent(socket, None, 0)

                return socket

            first = False

        socket = self.create_socket('OUTPUT', name, 'NodeSocketGeometry')

        self.btree.interface.move_to_parent(socket, None, 0)

        return socket    
    
    # ====================================================================================================
    # Get by python name
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its python name
    # ----------------------------------------------------------------------------------------------------

    def get_socket_by_python_name(self, 
            in_out: IN_OUT, 
            name: str, 
            socket_type: str,
            *,
            parent: (NodeTreeInterfacePanel | str) = None,
            return_all: bool = False):
        """ Get a socket by its python name.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - name (str) : the python name
        - socket_type (str) : socket type
        - parent (str | NodeTreeInterfacePanel = None) : the parent panel
        - return_all (bool = False) : return all candidates

        Returns
        -------
        - NodeTreeInterfaceSocket : None if not found
        - list of NodeTreeInterfaceSocket is return_all is True
        """

        check_in_out(in_out)

        sockets = []
        parent = self.get_panel(parent)
        parent_path = ItemPath(parent)
        for socket in self.iterate(in_out, socket_type=socket_type, panels=False, parent=parent):
            if name in (ItemPath(socket) - parent_path).get_names(True, True):
                sockets.append(socket)

        if return_all:
            return sockets
        elif not len(sockets):
            return None
        else:
            return sockets[0]
    
    # ----------------------------------------------------------------------------------------------------
    # Get a panel by its python name
    # ----------------------------------------------------------------------------------------------------

    def get_panel_by_python_name(self,
            name: str,
            parent: (NodeTreeInterfacePanel | str) = None):
        """ Get a panel by its python name.

        Arguments
        ---------
        - name (str) : the python name
        - parent (str | NodeTreeInterfacePanel = None) : the parent panel

        Returns
        -------
        - NodeTreeInterfacePanel : None if not found
        """
        #parent = self.get_panel(parent)
        parent_path = ItemPath(parent)
        for panel in self.iterate(sockets=False, parent=parent):
            if True:
                if name in (ItemPath(panel) - parent_path).get_names(True):
                    return panel
            else:
                names = self.get_python_names(panel, parent=parent)
                if name in names:
                    return panel

        return None
    
    # ----------------------------------------------------------------------------------------------------
    # By identifier
    # ----------------------------------------------------------------------------------------------------

    def by_identifier(self, identifier):
        for item in self.iterate(panels=False):
            if item.identifier == identifier:
                return item
        return None


    # ====================================================================================================
    # Deletion
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Clear the interface
    # ----------------------------------------------------------------------------------------------------

    def clear(self, use_bin=True):
        """ Clear the interface.

        The sockets are not actually deleted but moved to a bin named "SOCKETS_BIN".
        When a socket is created, the method first searchs into the bin if there is as socket
        with the required named and type. In that case, the socket is taken back from the bin.

        To finalize the clearing, call 'clear_deleted` method.

        ``` python
        tinf = TreeInterface(...)

        # Clear the interface using a bin
        tinf.clear(use_bin=True)
        
        # Socket is either actually created or moved from bin
        socket = tinf.create_socket(...)
        
        # Empty the bin
        tinf.empty_bin()
        ````

        Arguments
        ---------
        - use_bin (bool=True) : move the sockets to a bin if True
        """

        CLEAR = ['NodeSocketMenu']

        if use_bin:
            del_panel = self.get_panel(self.BIN_PANEL, create=True)
            for item in self.iterate("BOTH", panels=False):
                if item.socket_type in CLEAR:
                    self.btree.interface.remove(item)
                else:
                    self.btree.interface.move_to_parent(item, del_panel, 9999)

            for panel in self.iterate(sockets=False):
                if panel.name == self.BIN_PANEL:
                    continue
                self.btree.interface.remove(panel)

        else:
            self.btree.interface.clear()

    # ----------------------------------------------------------------------------------------------------
    # Clear the deleted sockets
    # ----------------------------------------------------------------------------------------------------
    
    def empty_bin(self):
        """ Empty bin.

        Empty the bin.
        """

        del_panel = self.get_panel(self.BIN_PANEL)
        if del_panel is None:
            return
        
        for item in self.iterate("BOTH", panels=False, parent=del_panel, sub_panels=False, ignore_bin=False):
            self.btree.interface.remove(item)

        self.btree.interface.remove(del_panel)

        
    # ====================================================================================================
    # Utilities
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get the associated node socket
    # ----------------------------------------------------------------------------------------------------

    def get_node_socket_OLD(self, item):

        if item.in_out == 'INPUT':
            for node in self.btree.nodes:
                if node.bl_idname != 'NodeGroupInput':
                    continue
                
                for bsock in node.outputs:
                    if bsock.identifier == item.identifier:
                        return bsock
            return None

        elif item.in_out == 'OUTPUT':
            for node in self.btree.nodes:
                if node.bl_idname != 'NodeGroupOutput':
                    continue
                
                for bsock in node.inputs:
                    if bsock.identifier == item.identifier:
                        return bsock
            return None        

        assert False, f"Shouln't happen: {item}"

    # ----------------------------------------------------------------------------------------------------
    # Iterator
    # ----------------------------------------------------------------------------------------------------

    def iterate(self,
                in_out      : BOTH = 'BOTH',
                *,
                sockets     : bool = True,
                socket_type : str = None,
                panels      : bool = True, 
                parent      : NodeTreeInterfacePanel = None,
                sub_panels  : bool = True,
                ignore_bin  : bool = True):
        """ Iterate over sockets and or panels.

        > [!NOTE]
        > The methods return the list of items and not a true Iterator

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT', 'BOTH')) : filter on sockets input / output
        - sockets (bool = True) : iterate of sockets
        - panels (bool = True) : iterate of panels
        - parent (NodeTreeInterfacePanel = None) : iterate on items within this parent
        - sub_panels (bool = True) : iterate in sub panels of the parent
        - ignore_bin (bool = True) : ignore sockets in bin

        Returns
        -------
        - list
        """

        check_in_out(in_out, both=True)

        if socket_type is not None:
            socket_type = SocketType(socket_type).socket_id
        
        items = []
        parent_index = -1 if parent is None else parent.index

        for item in self.items_tree:

            # ---------------------------------------------------------------------------
            # Socket / Panel filter
            # ---------------------------------------------------------------------------

            # Panel
            if item.item_type == 'PANEL':
                if not panels:
                    continue

            # Socket
            else:
                if not sockets:
                    continue
                if in_out not in [item.in_out, 'BOTH']:
                    continue
                if socket_type is not None and item.socket_type != socket_type:
                    continue
                if ignore_bin and item.parent.name == TreeInterface.BIN_PANEL:
                    continue

            # ---------------------------------------------------------------------------
            # Parent filter
            # ---------------------------------------------------------------------------

            if sub_panels:
                if not self.belongs_to(item, parent):
                    continue
            else:
                if item.parent.index != parent_index:
                    continue

            # ---------------------------------------------------------------------------
            # Got one !
            # ---------------------------------------------------------------------------

            items.append(item)

        # We've got our list
        return items

    # ----------------------------------------------------------------------------------------------------
    # Get the shortest names
    # ----------------------------------------------------------------------------------------------------

    def get_shortest_names(self, in_out: IN_OUT):
        """ Return the sockets index by their shortest name.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT', 'BOTH')) : filter on sockets input / output

        Returns
        -------
        - dict : shortest name -> socket
        """
        check_in_out(in_out)

        items = [item for item in self.iterate(in_out, panels=False)]
        all_names = [ItemPath(item).get_names(False, True) for item in items]

        sockets = []

        for index, (item, names) in enumerate(zip(items, all_names)):
            ok = False
            shortest = names[-1]
            has_homonym = False
            for candidate in reversed(names[:-1]):
                for iother, other in enumerate(all_names):
                    if iother == index:
                        continue
                    if candidate in other:
                        has_homonym = True
                        break
                if not has_homonym:
                    shortest = candidate

            sockets.append((shortest, item))

        return sockets
    
    # ====================================================================================================
    # Signature
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # An item to dict
    # ----------------------------------------------------------------------------------------------------

    def get_socket_dict(self,
            socket      : NodeTreeInterfaceItem, 
            parent      : NodeTreeInterfacePanel = None, 
            with_socket : bool = False):
        """ Build a dict from item.

        The dict can be used to create sockets with the same setup.

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item
        - parent (NodeTreeInterfacePanel = None) : path up to the parent
        - with_socket (bool = False) : include the NodeSocket

        Returns
        -------
        - dict
        """
        path = ItemPath(socket) - ItemPath(parent)
        name = path.name
        
        d = {
            'name'       : name,
            'path'       : path.path,
            'identifier' : socket.identifier,
            'socket_id'  : socket.socket_type,
            'props'      : {prop_name: getattr(socket, prop_name) for prop_name in self.socket_props[socket.socket_type]},
        }
        if with_socket:
            d['isocket'] = socket
            #d['socket']  = self.get_node_socket(socket)

        return d
   
    # ----------------------------------------------------------------------------------------------------
    # Get the interface signature
    # ----------------------------------------------------------------------------------------------------

    def get_signature(self, 
            *,
            include      : list = None,
            exclude      : list = [],
            enabled_only : bool = True,
            #free_only    : bool = False,
            parent       : NodeTreeInterfaceSocket = None, 
            with_sockets : bool = False):
        """ Get the closure signature

        Attributes
        ----------
        - include (list = None) : limit sockets to list
        - exclude (list = []) : exclude sockets from list
        - enabled_only (bool = True) : only enabled sockets
        - parent (NodeTreeInterfacePanel = None) : path up to the parent
        - with_sockets (bool = False) : include socket in the dict

        Returns
        -------
        - Signature
        """

        parent_path = ItemPath(parent)

        signature = Signature()
        for in_out in ['INPUT', 'OUTPUT']:

            #sockets = self.get_sockets(in_out, include=include, exclude=exclude, enabled_only=enabled_only, free_only=free_only, parent=parent)
            sockets = self.get_sockets(in_out, include=include, exclude=exclude, enabled_only=enabled_only, parent=parent)
            sig = []
            for socket in sockets:
                d = self

            sig = [self.get_socket_dict(socket, with_socket=with_sockets) for socket in sockets]

            signature[in_out] = sig

        return signature
    
    # ----------------------------------------------------------------------------------------------------
    # Set the signature
    # ----------------------------------------------------------------------------------------------------

    def set_signature(self, signature, reuse: bool = True, parent: NodeTreeInterfacePanel=None):
        """ Set a signature.

        The returns dict contains two lists keyed by 'INPUT' and 'OUPUT'. The two values
        are lists of couple (creation dict, created socket).

        Arguments
        ---------
        - signature (Signature) : the signature to set
        - reuse (bool = True) : doesn't create a socket if it already exists
        - parent (NodeTreeInterfacePanel) : the parent where to create the signature

        Returns
        -------
        - dict of two lists of couples (dict, created sockets)
        """

        created = {}

        for in_out, sig in zip(['INPUT', 'OUTPUT'], Signature(signature)):

            created[in_out] = []
 
            for d in sig:

                socket_path = ItemPath(d.get('path', d['name']))
                socket_type = SocketType(d.get('socket_type', d.get('socket_id')))

                # Reuse
                socket = None
                if reuse:
                    socket = self.get_socket(in_out, socket_path, socket_type, parent=parent)

                # Create
                if socket is None:
                    socket = self.create_socket(in_out, socket_path, socket_type, parent=parent, **d.get('props', {}))

                created[in_out].append(socket)

        return created
    
    # ----------------------------------------------------------------------------------------------------
    # Set input signature
    # ----------------------------------------------------------------------------------------------------

    def set_input_signature(self, signature, reuse: bool = True, parent: NodeTreeInterfacePanel=None):
        """ Set a signature.

        Arguments
        ---------
        - signature (Signature) : the signature to set
        - reuse (bool = True) : doesn't create a socket if it already exists
        - parent (NodeTreeInterfacePanel) : the parent where to create the signature

        Returns
        -------
        - list of couples (creation dict, created sockets)
        """
        signature = Signature(signature)
        return self.set_signature(Signature(signature.sockets), reuse=reuse, parent=parent)['INPUT']

    # ----------------------------------------------------------------------------------------------------
    # Set output signature
    # ----------------------------------------------------------------------------------------------------

    def set_output_signature(self, signature, reuse: bool = True, parent: NodeTreeInterfacePanel=None):
        """ Set a signature.

        Arguments
        ---------
        - signature (Signature) : the signature to set
        - reuse (bool = True) : doesn't create a socket if it already exists
        - parent (NodeTreeInterfacePanel) : the parent where to create the signature

        Returns
        -------
        - list of couples (creation dict, created sockets)
        """
        signature = Signature(signature)
        return self.set_signature(Signature({}, signature.sockets), reuse=reuse, parent=parent)['OUTPUT']
    
    # ====================================================================================================
    # Class test
    # ====================================================================================================

    def _class_test():
        
        tree_name = "Interface Test"
        tree = bpy.data.node_groups.get(tree_name)
        if tree is None:
            tree = bpy.data.node_groups.new("GeometryNodeTree", tree_name)
        tree.nodes.clear()
        tree.interface.clear()
        intf = TreeInterface(tree)
        
        def check(value, target):
            ok = ItemPath(value).path == target
            if ok:            
                print(f"ok  > '{ItemPath(value)}'")
            else:
                print(f"ERR> '{ItemPath(value)}', expected '{target}'")
                
        def check_vals(a, b):
            ok = a == b
            if ok:            
                print(f"ok  > {a}")
            else:
                print(f"ERR> {a}, expected {b}")
            
                
        # --------------------------------------------------------------------------------
        # PanelS
        # --------------------------------------------------------------------------------
            
        check(intf.get_panel(""), "")
        check(intf.get_panel("NO PANEL"), "")
        check(intf.get_panel("Panel", create=True), "Panel")
        check(intf.get_panel("Panel", create=False), "Panel")
        check(intf.get_panel("New Panel>Sub>", create=True), "New Panel > Sub")
        check(intf.get_panel("New Panel>>Sub", create=False), "New Panel > Sub")
        check(intf.get_panel("Panel>Sub_2", create=True), "Panel > Sub_2")
        check(intf.get_panel("Panel>Sub_2", create=False), "Panel > Sub_2")
        check(intf.get_panel(">>New Panel>>>>Sub_1>Again", create=True), "New Panel > Sub_1 > Again")
        check(intf.get_panel("New Panel>Sub_1>Again", create=False), "New Panel > Sub_1 > Again")
        
        check(intf.create_panel("Again", "New Panel>Sub_1", tip="Second Again"), "New Panel > Sub_1 > Again_1")
        check(intf.create_panel("Again", "New Panel>Sub_1", tip="Second Again"), "New Panel > Sub_1 > Again_2")
        
        # --------------------------------------------------------------------------------
        # Sockets
        # --------------------------------------------------------------------------------
        
        check(intf.get_socket('INPUT', "Test", "Float"), "")
        check(intf.create_socket('INPUT', "Float", "Float"), "Float")
        check(intf.get_socket('INPUT', "Float", "Float"), "Float")
        check(intf.get_socket('INPUT', "Float", "String"), "")
        
        check(intf.create_socket('INPUT', "Float", "Float"), "Float_1")
        
        check(intf.get_socket('INPUT', "Test", "Float", parent="Sockets"), "")
        check(intf.create_socket('INPUT', "Float", "Float", parent="Sockets"), "Sockets > Float")
        check(intf.get_socket('INPUT', "Float", "Float", parent="Sockets"), "Sockets > Float")
        check(intf.get_socket('INPUT', "Float", "String", parent="Sockets"), "")
        
        check(intf.create_socket('INPUT', "Float", "Float", parent="Sockets"), "Sockets > Float_1")

        # --------------------------------------------------------------------------------
        # Signature
        # --------------------------------------------------------------------------------
        
        a = tuple(intf.get_signature().input_keys)
        check_vals(a, (('Float', 'NodeSocketFloat'), ('Float_1', 'NodeSocketFloat'), ('Sockets > Float', 'NodeSocketFloat'), ('Sockets > Float_1', 'NodeSocketFloat')))

        # --------------------------------------------------------------------------------
        # Naming
        # --------------------------------------------------------------------------------
        
        tree.interface.clear()
        tree.nodes.new('NodeGroupInput')
        tree.nodes.new('NodeGroupOutput')
        
        print("\nCreating sockets")
        
        sock0 = intf.create_socket('INPUT', "Value", "Float")           # value
        sock1 = intf.create_socket('INPUT', "Value", "String")          # value
        sock2 = intf.create_socket('INPUT', "Value", "Float", "Panel")  # panel_value
        sock3 = intf.create_socket('INPUT', "Value", "Float", "Panel")  # panel_value_1
        sock4 = intf.create_socket('INPUT', "Value", "String", "Panel") # panel_value
        sock5 = intf.create_socket('INPUT', "Value", "String", "Panel") # panel_value_1
        sock6 = intf.create_socket('INPUT', "Float", "Float", "Panel")  # float
        
        sockets = intf.get_shortest_names('INPUT')
        a = tuple([name for name, _ in sockets])
        check_vals(a, ('value',  'value',  'panel_value',  'panel_value_1',  'panel_value',  'panel_value_1',  'float'))
        
        a = tuple(intf.get_signature().input_keys)
        check_vals(a, (
            ('Value', 'NodeSocketFloat'),
            ('Value', 'NodeSocketString'), 
            ('Panel > Value', 'NodeSocketFloat'), 
            ('Panel > Value_1', 'NodeSocketFloat'), 
            ('Panel > Value', 'NodeSocketString'), 
            ('Panel > Value_1', 'NodeSocketString'), 
            ('Panel > Float', 'NodeSocketFloat')))
            
        # --------------------------------------------------------------------------------
        # Signature
        # -------------------------------------\n-----------------------------------------

        print("\nSetting signature")
        
        tree.interface.clear()
        intf.create_socket('INPUT', "Geometry", 'Geometry')
        intf.create_socket('INPUT', "Float", 'Float')
        intf.create_socket('INPUT', "Integer", 'Integer')

        intf.create_socket('OUTPUT', "Geometry", 'Geometry')
        
        sig0 = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig0.input_keys)
        check_vals(a, (('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt')))

        intf.set_input_signature(sig0.inputs, reuse=True)
        sig = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig.input_keys)
        check_vals(a,  (('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt')))

        intf.set_input_signature(sig0.inputs, reuse=False)
        sig = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig.input_keys)
        check_vals(a, (
            ('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt'),
            ('Float_1', 'NodeSocketFloat'), ('Integer_1', 'NodeSocketInt')))
        
        intf.set_input_signature(sig0.inputs, parent="Panel")
        sig = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig.input_keys)
        target = (
            ('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt'), 
            ('Float_1', 'NodeSocketFloat'), ('Integer_1', 'NodeSocketInt'), 
            ('Panel > Float', 'NodeSocketFloat'), ('Panel > Integer', 'NodeSocketInt'))
        check_vals(a, target)
        
        intf.set_output_signature(sig0.inputs)
        sig = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig.output_keys)
        check_vals(a, (('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt')))
        
        intf.set_output_signature(sig0.inputs, reuse=True)
        sig = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig.output_keys)
        check_vals(a, (('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt')))
        
        intf.set_output_signature(sig0.inputs, parent="Panel")
        sig = intf.get_signature(exclude=["Geometry"])
        a = tuple(sig.output_keys)
        check_vals(a, (
            ('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt'),
            ('Panel > Float', 'NodeSocketFloat'), ('Panel > Integer', 'NodeSocketInt')))
        
        sig = intf.get_signature(include=["Panel"])
        a = tuple(sig.output_keys)
        check_vals(a, (('Panel > Float', 'NodeSocketFloat'), ('Panel > Integer', 'NodeSocketInt')))
        
        sig = intf.get_signature(exclude=["Panel", "Geometry"])
        a = tuple(sig.output_keys)
        check_vals(a, (('Float', 'NodeSocketFloat'), ('Integer', 'NodeSocketInt')))
        
        sig = intf.get_signature(include=["Panel"])
        a = tuple(sig.output_keys)
        check_vals(a, (('Panel > Float', 'NodeSocketFloat'), ('Panel > Integer', 'NodeSocketInt')))
        
        sig = intf.get_signature(parent="Panel")
        a = tuple(sig.output_keys)
        check_vals(a, (('Panel > Float', 'NodeSocketFloat'), ('Panel > Integer', 'NodeSocketInt')))
        
