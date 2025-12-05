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
# Item Path
# ====================================================================================================

class ItemPath:

    def __init__(self, value: str | list | NodeTreeInterfaceItem):

        __slots__ = ['_path']

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

        if value is None:
            self._path = ""
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
            self._path = value.path

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

        # ---------------------------------------------------------------------------
        # Stack of panels
        # ---------------------------------------------------------------------------

        elif isinstance(value, list):
            self._path = ItemPath.stack_to_path(value)

        else:
            raise RuntimeError(f"ItemPath error: Impossible to initialize from {value}.")
        
    def __str__(self):
        return self.path
    
    @property
    def path(self):
        return self._path

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
    def python_path(self):
        return utils.snake_case(self.path)
    
    @property
    def python_long_name(self):
        return utils.snake_case(self.long_name)
    
    @property
    def parent(self):
        if self.path == "":
            return ItemPath(None)
        else:
            return ItemPath(self.stack[:-1])

    @property
    def name_rank(self):
        if self.path == "":
            return None, None
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
    # Operations
    # ====================================================================================================
    
    def join(self, other):
        
        other = ItemPath.to_item_path(other)
        if self.is_root:
            return other
        
        elif other.is_root:
            return self
        
        return ItemPath(">".join([self.path, ItemPath(other).path]))
    
    def equal_to(self, other):
        return self.path == ItemPath.to_item_path(other).path
    
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
        if parent_path.is_root:
            return self
        
        if self.path.startswith(parent_path.path):
            return ItemPath(self.path[len(parent_path.path):])
        else:
            return self
        
        parent = ItemPath(parent)
        if parent.is_root or self.is_root:
            return ItemPath(self)
        
        parent_path = parent.path
        if len(parent_path) > len(self.path):
            return ItemPath(self)
        
        if parent_path != self.path[:len(parent_path)]:
            return ItemPath(self)
        
        s = self.path[len(parent_path):].strip()
        if len(s) and s.startswith('>'):
            s = s[1:].strip()
            
        return ItemPath(s)
    
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
# Utility
# ====================================================================================================

def get_path_type(value):
    if isinstance(value, tuple) and len(value) == 2:
        return ItemPath(value[0]), SocketType(value[1])
    else:
        return ItemPath(value), None



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
        socket = self.get_socket(socket_path.name, TreeInterface.BIN_PANEL, socket_type=socket_type)
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
                raise TypeError(f"create_socket error: socket property '{prop}' is invalid: '{prop}' not in {self.socket_props[socket_type.socket_id]}.")

            # Could fail for default_value (Menu for instance)
            try:
                setattr(socket, prop, value)
            except:
                pass

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
            # ---------------------------------------------------------------------------

            if created and hasattr(socket, 'default_value'):
                for mod in blender.get_geonodes_modifiers(self.btree):
                    try:
                        mod[socket.identifier] = socket.default_value
                    except Exception as e:
                        print(f"Info: impossible to set default value {socket.default_value} to modifier for socket '{socket.name}': {str(e)}")
                            
        return socket
    
    # ----------------------------------------------------------------------------------------------------
    # Get the interface signature
    # ----------------------------------------------------------------------------------------------------

    def get_sockets(self,
            in_out: IN_OUT,
            *,
            include: list = None,
            exclude: list = [],
            enabled_only : bool = True,
            free_only: bool = False,
            parent: NodeTreeInterfaceSocket = None, 
        ):
        """ Get sockets

        Attributes
        ----------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - include (list = None) : limit sockets to list
        - exclude (list = []) : exclude sockets from list
        - enabled_only (bool = True) : only enabled sockets
        - free_only (bool = False) : only free sockets
        - parent (NodeTreeInterfacePanel = None) : path up to the parent

        Returns
        -------
        - list of sockets
        """
        parent_path = ItemPath(parent)

        # ---------------------------------------------------------------------------
        # Inclusions and exclusions
        # ---------------------------------------------------------------------------

        # Panels to include
        incl_panels = None
        incl_sockets = None
        if include is not None:
            for s in include:
                spath, stype = get_path_type(s)
                if stype is None:
                    panel = self.get_panel(spath, parent=parent, create=False)
                    if panel is not None:
                        if incl_panels is None:
                            incl_panels = []
                        incl_panels.append(panel)
                        continue

                if incl_sockets is None:
                    incl_sockets = []
                incl_sockets.append(s)

        # Panels to exclude
        excl_panels = []
        excl_sockets = []
        for s in exclude:
            spath, stype = get_path_type(s)
            if stype is None:
                panel = self.get_panel(ItemPath(parent) + spath)
                if panel is not None:
                    excl_panels.append(panel)
                    continue

            excl_sockets.append(s)

        # ---------------------------------------------------------------------------
        # Douple loop input and output then items
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

            rel_path = ItemPath(socket) - parent_path
            names = rel_path.get_names(True, True)

            ok = True
            for s in excl_sockets:
                spath, stype = get_path_type(s)
                if socket.identifier == spath or spath in names:
                    ok = False
                if stype is not None and socket.socket_type != stype.socket_id:
                    ok = False
                
            if not ok:
                continue

            if incl_sockets is not None:
                ok = False
                for s in incl_sockets:
                    spath, stype = get_path_type(s)
                    if socket.identifier == spath or spath in names:
                        ok = True
                        break
                    if stype is not None and socket.socket_type != stype.socket_id:
                        ok = True
                        break

                if not ok:
                    continue

            # ---------------------------------------------------------------------------
            # Socket conditions
            # ---------------------------------------------------------------------------

            if enabled_only or free_only:
                nsock = self.get_node_socket(socket)
                if nsock is not None:
                    if enabled_only and not nsock.enabled:
                        continue
                    if free_only and not utils.is_free(nsock):
                        continue

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
        sockets = []
        parent = self.get_panel(parent)
        parent_path = ItemPath(parent)
        for socket in self.iterate(in_out, socket_type=socket_type, panels=False, parent=parent):
            if True:
                if name in (ItemPath(socket) - parent_path).get_names(True):
                    sockets.append(socket)
            else:
                names = self.get_python_names(socket, parent=parent)
                if name in names:
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


    # ----------------------------------------------------------------------------------------------------
    # Does a socket name match a user name
    # ----------------------------------------------------------------------------------------------------

    def socket_matches_name_OLD(self, socket: NodeTreeInterfaceSocket, name: str, parent: (NodeTreeInterfacePanel | str) = None):
        """ Test if a socket matches a name.

        The provided name can be a socket name or a panel name. In that later case, the match is
        True if the socket belongs to the panel.

        The match is searched only in the parent panel.

        Arguments
        ---------
        - socket NodeTreeInterfaceSocket) : the socket to test
        - name (str) : socket or panel name to test
        - parent (str | NodeTreeInterfacePanel = None) : the parent panel

        Returns
        -------
        - True if match
        """
        
        # Test if it is a socket
        for s in self.get_socket_by_python_name(socket.in_out, name, parent=parent, return_all=True):
            if s == socket:
                return True
            
        # The name could be a panel
        panel = self.get_panel_by_python_name(name, parent = parent)
        if panel is None:
            return False
        else:
            return self.belongs_to(socket, panel)
    
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

        if use_bin:
            del_panel = self.get_panel(self.BIN_PANEL, create=True)
            for item in self.iterate("BOTH", panels=False):
                self.btree.interface.move_to_parent(item, del_panel, 9999)

            for panel in self.iterate(sockets=False):
                if panel.name == self.BIN_PANEL:
                    continue
                self.btree.interface.remove(panel)

        else:
            self.btree.interface.clear()

    # ----------------------------------------------------------------------------------------------------
    # Get an previously deleted socket back to a panel
    # ----------------------------------------------------------------------------------------------------

    def get_from_bin_OLD(self, in_out: IN_OUT, name: str, socket_type: str | SocketType):
        """ Get a socket from the bin.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - name (str) : name of the socket to create
        - socket_type (str | SocketType) : a valid socket type ('NodeSocketFloat', 'NodeSocketInt', ...)

        Returns
        -------
        - NodeTreeInterfaceSocket : None if not found
        """
        del_panel = self.get_panel(self.BIN_PANEL)
        if del_panel is None:
            return None
        
        socket_type = SocketType(socket_type)
        for item in self.iterate(in_out, panels=False, parent=del_panel, sub_panels=False, ignore_bin=False):
            if item.name == name and item.socket_type == socket_type:
                return item

        return None
    
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

    def get_node_socket(self, item):

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
                p = item.parent
                ok = False
                while p is not None:
                    ok = p.index == parent_index
                    if ok:
                        break
                    p = p.parent
                if not ok:
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
    # Item rank
    # ----------------------------------------------------------------------------------------------------

    def get_item_rank_OLD(self, item):
        """ Get item rank

        Count the number of homonyms in its parent panel

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item

        Returns
        -------
        - int
        """
        count = None
        in_out = 'BOTH' if item.item_type == 'PANEL' else item.in_out
        for other in self.iterate(in_out, sockets=item.item_type=='SOCKET', panels=item.item_type=='PANEL', parent=item.parent):
            if other.name == item.name:
                if count is None:
                    count = 0
                else:
                    count += 1

                if other.index == item.index:
                    return count
                
        assert False, "Algo error"

    # ----------------------------------------------------------------------------------------------------
    # Get all the possible python names of a socket
    # ----------------------------------------------------------------------------------------------------

    def get_python_names_OLD(self, item: NodeTreeInterfaceItem, parent: NodeTreeInterfacePanel = None):
        """ Build the list of all the possible python names.

        The possible names are built from the item name and the names of the parent panels.
        At each step, the name is suffixed with its rank if it is not 0.

        For instance the second socket Float in panel Panel returns:
        `["float", "float_1", "float_001", "panel_float", "panel_float_1", "panel_float_001"]

        The hierarchy stops when the parent is reached

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item
        - parent (NodeTreeInterfacePanel = None) : the top parent

        Returns
        -------
        - list of strs : the possible pyton names
        """

        name = utils.snake_case(item.name)
        rank = self.get_item_rank(item)

        levels = []
        if rank == 0:
            levels.append([name])
        else:
            levels.append([f"{name}_{rank}", f"{name}_{rank:03d}"])

        all_names = [*levels[0]]

        cur = item.parent
        while True:
            if cur.index == -1:
                break

            if parent is not None and cur.index == parent.index:
                break
            
            cur_name = utils.snake_case(cur.name)
            cur_rank = self.get_item_rank(cur)

            new_level = []
            for n in levels[-1]:
                sep = "" if n.startswith('_') else '_'
                
                new_level.append(f"{cur_name}{sep}{n}")

                if cur_rank != 0:
                    new_level.append(f"{cur_name}_{cur_rank}{sep}{n}")
                    new_level.append(f"{cur_name}_{cur_rank:03d}{sep}{n}")

            levels.append(new_level)
            all_names.extend(new_level)

            cur = cur.parent

        return all_names
    
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
    # Get the panels list
    # ----------------------------------------------------------------------------------------------------

    def get_parents_OLD(self, item, parent: NodeTreeInterfacePanel = None):
        """ Return the list of parent panels

        The list is made of a dicts `{'name', 'index', 'rank', 'tip'}`

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item
        - parent (NodeTreeInterfacePanel = None) : up to the parent

        Returns
        -------
        - list of dicts
        """
        if item.parent.index == -1:
            return []
        
        if (parent is not None) and (item.parent.index == parent.index):
            return []
        
        return self.get_parents(item.parent) + [{
            'name'  : item.parent.name, 
            'index' : item.parent.index, 
            'rank'  : self.get_item_rank(item.parent),
            'tip'   : item.parent.description
            }]
    
    # ----------------------------------------------------------------------------------------------------
    # Create panels from panels list
    # ----------------------------------------------------------------------------------------------------
    
    def create_parents_OLD(self, panels, parent: NodeTreeInterfacePanel = None):
        """ Return the list of parent panels

        The list is made of a dicts `{'name', 'index', 'rank', 'tip'}`

        Arguments
        ---------
        - panels (list of dicst) : the panels to create
        - parent (NodeTreeInterfacePanel = None) : within the parent

        Returns
        -------
        - NodeTreeInterfacePanel : the last panel in the hierarchy
        """

        parent = parent
        for d in panels:
            name, rank = d['name'], d['rank']
            #ranked = name if rank == 0 else f"{name}_{rank}"

            new_parent = None
            for panel in self.iterate(sockets=False, parent=parent):
                if panel.name != name:
                    continue

                if rank == 0:
                    new_parent = panel
                    break

                rank -= 1

            if new_parent is None:
                for _ in range(rank + 1):
                    new_parent = self.create_panel(name, parent=parent, tip=d['tip'])

            parent = new_parent

        return parent
    
    # ----------------------------------------------------------------------------------------------------
    # Get the path of an item
    # ----------------------------------------------------------------------------------------------------

    def get_item_path_OLD(self, item, separator = " > "):
        """ Get the full path of an item
        """
        return TreeInterface.parents_to_list(self.get_parents(item), separator=separator)

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
        _, rank = path.name_rank
        
        d = {
            'name'       : path.path,
            'identifier' : socket.identifier,
            'type'       : socket.socket_type,
            'props'      : {prop_name: getattr(socket, prop_name) for prop_name in self.socket_props[socket.socket_type]},
        }
        if with_socket:
            d['isocket'] = socket
            d['socket']  = self.get_node_socket(socket)

        return d

        # OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD 


        # ---------------------------------------------------------------------------
        # Panel and Socket
        # ---------------------------------------------------------------------------

        panels = self.get_parents(item, parent=parent)
        panel = " > ".join([p['name'] for p in panels])

        d = {
            'full'       : True,
            'name'       : item.name,
            'index'      : item.index,
            'rank'       : self.get_item_rank(item),
            'tip'        : item.description,
            'panels'     : panels,
            'panel'      : panel,
            'identifier' : item.identifier,
        }

        if item.item_type == 'PANEL':
            return d
        
        # ---------------------------------------------------------------------------
        # Additional sockets properties
        # ---------------------------------------------------------------------------

        d['socket_id'] = item.full_socket_id
        d['props'] = {prop_name: getattr(item, prop_name) for prop_name in self.socket_props[item.socket_type]}

        if with_socket:
            bsock = self.get_node_socket(item)
            if bsock is not None:
                d['socket'] = bsock

        return d
    
    # ----------------------------------------------------------------------------------------------------
    # Get the interface signature
    # ----------------------------------------------------------------------------------------------------

    def get_signature(self, 
            *,
            include         : list = None,
            exclude         : list = [],
            enabled_only    : bool = True,
            free_only       : bool = False,
            parent          : NodeTreeInterfaceSocket = None, 
            with_sockets    : bool = False):
        """ Get the closure signature

        Attributes
        ----------
        - include (list = None) : limit sockets to list
        - exclude (list = []) : exclude sockets from list
        - enabled_only (bool = True) : only enabled sockets
        - free_only (bool = False) : only free sockets
        - parent (NodeTreeInterfacePanel = None) : path up to the parent
        - with_sockets (bool = False) : include socket in the dict

        Returns
        -------
        - Signature
        """

        parent_path = ItemPath(parent)

        signature = Signature()
        for in_out in ['INPUT', 'OUTPUT']:

            sockets = self.get_sockets(in_out, include=include, exclude=exclude, enabled_only=enabled_only, free_only=free_only, parent=parent)
            sig = {(ItemPath(socket).path, socket.socket_type): self.get_socket_dict(socket, with_socket=with_sockets) for socket in sockets}

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
 
            for key, d in sig.items():

                # The key can be a couple (path, socket_type) or path only
                if isinstance(key, tuple):
                    socket_path = ItemPath(key[0])
                    socket_type = SocketType(key[1])
                else:
                    socket_path = ItemPath(key)
                    socket_type = SocketType(d['socket_type'])

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


                







            
        

        









class OLD_TUFF:


    # ----------------------------------------------------------------------------------------------------
    # Socket associated to the item
    # ----------------------------------------------------------------------------------------------------

    def get_item_socket(self, item):
        """ Get item socket

        Count the number of homonyms in its parent panel

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item

        Returns
        -------
        - NodeSocket
        """
        if item.item_type != 'PANEL':
            return None

        if self.in_out == 'INPUT':
            for node in self.btree.nodes:
                if node.bl_idname == 'NodeGroupInput':
                    for socket in node.inputs:
                        if socket.identifier == item.identifier:
                            return socket
        else:
            for node in self.btree.nodes:
                if node.bl_idname == 'NodeGroupOutput':
                    for socket in node.outputs:
                        if socket.identifier == item.identifier:
                            return socket
                        
        return None


    # ====================================================================================================
    # Access to items
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its identifier
    # ----------------------------------------------------------------------------------------------------

    def get_item_by_identifier(self, identifier: str):
        """ Return a socket by its identifier

        Arguments
        ---------
        - identifier (str) : socket identifier

        Returns
        -------
        - NodeTreeInterfaceSocket : socket or raises an error if not found
        """
        for item in self.iterate(None, panels=False):
            if item.identifier == identifier:
                return item

        raise NodeError(f"TreeInterface.by_identifier error: '{identifier}' not found in tree '{self.btree.name}'.")

    # ----------------------------------------------------------------------------------------------------
    # Get an item by its name, rank and panel
    # ----------------------------------------------------------------------------------------------------

    def get_item_by_name_rank(self, in_out: IN_OUT, name: str, rank: int = 0, is_panel=False, parent: NodeTreeInterfacePanel = None):
        """ Get an itme by its name, rank and panel

        Returns None if not found

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - name (str) : item's name
        - rank (int = 0) : rank within the panel
        - is_panel (bool = False) : panel or socket
        - parent (NodeTreeInterfacePanel = None) : parent panel to explore

        Returns
        -------
        - NodeTreeInterfacePanel | NodeTreeInterfaceSocket
        """

        count = 0
        for item in self.iterate(in_out=in_out, sockets=not is_panel, panels=is_panel, parent=parent):
            if item.name != name:
                continue
            if count == rank:
                return item
            count += 1

        return None

    # ----------------------------------------------------------------------------------------------------
    # Get item by path
    # ----------------------------------------------------------------------------------------------------

    def get_item_by_path(self, in_out: IN_OUT, path):
        """ Get item by its absolute path
        """
        for item in self.iterate(in_out):
            if self.get_item_names(item)['path'] == path:
                return item
            
        return None





    # ----------------------------------------------------------------------------------------------------
    # Create panel from list of panels
    # ----------------------------------------------------------------------------------------------------

    def create_panel_from_list(self, in_out: IN_OUT, panels: list):
        """ Create a panel from list

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output socket
        - panels (list of dicts) : hierarchical list of panels

        Returns
        -------
        - NodeTreeInterfacePanel
        """

        # Nothing to do
        if not len(panels):
            return None

        parent = None
        for d in panels:
            name = d['name']
            rank = d['rank']

            while (panel := self.get_item_by_name_rank(in_out, name, rank=rank, is_panel=True, parent=parent)) is None:
                panel = self.btree.interface.new_panel(name, in_out=in_out)
                panel.description = d['tip']
                if parent is not None:
                    self.btree.interface.move_to_parent(panel, parent, 9999)
            parent = panel

        return parent
    

    
    # ----------------------------------------------------------------------------------------------------
    # Set signature
    # ----------------------------------------------------------------------------------------------------

    def set_signature(self, in_out: IN_OUT, signature: Signature):
        """ Set a signature
        
        Arguments
        ---------
        - in_out (str) : input or output
        - signature: Signature
        """

        items = []
        for key, d in signature.sockets.items():
            # Full signature (with panels)
            if d.get('full', False):
                
                # Create the parent panels
                parent = self.create_panel_from_list(self, in_out=in_out, panels= d['panels'])

                # Create the item
                item = self.btree.interface.new_socket(d['name'], in_out=in_out, socket_type=d['item_type'])
                if parent is not None:
                    self.btree.interface.move_to_parent(item, parent, 9999)

                socket = self.get_item_socket(items)

                for name, value in d['props'].items():
                    try:
                        setattr(socket, name, value)
                    except Exception as e:
                        print(f"Warning set_signature: error when setting property {name}={value}, {str(e)}.")

            # Limited signature
            else:
                item = self.btree.interface.new_socket(key, in_out=in_out, socket_type=d['item_type'])


    # ====================================================================================================
    # Name utilities
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Convert user name to python name
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def user_name_to_python(name: str, python: bool = True):
        """ Convert a user into a python name

        In a user name, '>' is used as separator in the paths.
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
    # Get the item names
    # ----------------------------------------------------------------------------------------------------

    def get_item_names(self, item: NodeTreeInterfaceItem):
        """ Return a dict with the possible names of the item

        The dict contains 3 strs:
        - name : the raw name of the item (e.g.: Integer)
        - ranked : the name followed by its rank if if different from 0 (e.g.: Integer_001)
        - path : absolute path (e.g.: Panel_002 > Integer_001)

        Arguments
        ---------
        - item (NodeTreeInterfaceItem) : the item

        Returns
        -------
        - dict of strs: name, ranked, absolute
        """

        rank = self.get_item_rank(item)
        ranked = item.name if rank == 0 else f"{item.name}_{rank:03d}"
        d = {'name': 'item.name', 'rank': rank, 'ranked': ranked}
        if item.parent.name == "":
            d['path'] = ranked
        else:
            d['path'] = self.get_item_names(item.parent)['absolute'] + " > " + ranked

        return d
    
    # ====================================================================================================
    # Deletion
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Mark for deletion
    # ----------------------------------------------------------------------------------------------------

    def mark_for_deletion(self):
        """ Mark all sockets to be deleted

        Set the `description` attribute with as specific value
        """
        for item in self.iterate(None, sockets=True, panels=True):
            item.description = DELETION

    # ----------------------------------------------------------------------------------------------------
    # Clear marked for deletion
    # ----------------------------------------------------------------------------------------------------

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
            for item in self.iterate(None, sockets=True, panels=True):
                if item.description == DELETION:
                    to_delete.append(item)

            for item in to_delete:
                self.btree.interface.remove(item)

    # ----------------------------------------------------------------------------------------------------
    # Move panel as last 'NOT DELETED"
    # ----------------------------------------------------------------------------------------------------

    def move_before_deleted(self, moved_item):
        """ Move the item as the last 'NOT DELETED' item in its parent list

        Arguments
        ---------
        - moved_item (NodeTreeInterfaceItem) : the item to move as last NOT DELETED position
        """

        to_move = []
        for item in self.iterate(moved_item.in_out, parent=moved_item.parent):
            if item.description != DELETION:
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
    
    # ====================================================================================================
    # Get / create panel
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get / create an existing panel
    # ----------------------------------------------------------------------------------------------------

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

    def get_socket_OLD(self, in_out: str, name: str, halt=True):
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
            bl_idname   = item.socket_type,
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

        socket = self.create_socket('INPUT', name, 'NodeSocketGeometry')

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
                    self.btree.interface.move_to_parent(socket, None, 0)

                if socket.description == DELETION:
                    socket.description = ""

                return socket

            first = False

        socket = self.create_socket('OUTPUT', name, 'NodeSocketGeometry')

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

                socket_type = constants.SOCKET_SUBTYPES[in_socket.bl_idname]['nodesocket']
                new_socket = self.create_socket('INPUT', in_socket.name, bl_idname=socket_type, panel=panel, rank=rank)
                #InterfaceSockets.copy_item_attributes(item.bitem, new_socket)

                if input_node is not None:
                    out_socket = input_node.outputs[new_socket.identifier]
                    link = self.btree.links.new(in_socket, out_socket)
                    utils.check_link(link)

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
                new_socket = self.create_socket('INPUT', full_name, bl_idname=item.bitem.socket_type, panel=panel)

                # ----- Link the node
                # NOTE: must be done BEFORE copying attributes to make sure menus are initialized
                # when setting default_value

                if input_node is not None:
                    in_socket  = node.inputs[item.bitem.identifier]
                    out_socket = input_node.outputs[new_socket.identifier]
                    link = self.btree.links.new(in_socket, out_socket)
                    utils.check_link(link)


                InterfaceSockets.copy_item_attributes(item.bitem, new_socket)

    # ====================================================================================================
    # Signatures
    # ====================================================================================================

    def closure_signature(self):

        return (self.input_sockets.get_signature(), self.output_sockets.get_signature())
    
    def set_signature(self, signature):

        for in_out, sig in zip(('INPUT', 'OUTPUT'), signature):
            for name, d in sig.sockets.items():
                # Reduced
                if d.get('name') is None:
                    socket = self.btree.interface.new_socket(name, in_out=in_out, socket_type=d['item_type'])

                # Full
                else:
                    parent = self.create_panel_from_list(in_out, d['panels'])
                    item = self.btree.interface.new_socket(d['name'], in_out=in_out, socket_type=d['item_type'], parent=parent)

                    if parent is not None:
                        self.btree.interface.move_to_parent(item, parent, 9999)


