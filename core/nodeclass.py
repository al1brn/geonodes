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

module : nodeclass
------------------
- Node: base class to create a node


updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/01/18 # G as dynamic class
- update :   2025/03/27 # Blender 4.4 : panels can be nested
- update :   2025/11/20 # Blender 5.0
- update :   2025/11/30 # New structure
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

import numpy as np
import bpy

from . import blender
from .scripterror import NodeError
from . import constants
from . import utils
from .sockettype import SocketType
from .utils import Break
from .signature import Signature
from .treeclass import Tree
from .treeinterface import ItemPath, TreeInterface

from typing import TYPE_CHECKING, Literal, Any

class Node: ...
class Socket: ...

IN_OUT = Literal['INPUT', 'OUTPUT']

# ====================================================================================================
# Sockets
# ====================================================================================================

class Sockets:

    __slots__ = ('node_sockets', 'homonyms', 'multi_names', 'multi_type')

    def __init__(self, node_sockets: bpy.types.bpy_prop_collection):
        """ This class wrap Node inputs and outputs collection.
        """

        self.node_sockets = node_sockets
        self.multi_names = []
        self.multi_type  = None

        # ---------------------------------------------------------------------------
        # Detect the homonyms
        # Consider as one socket all the sockets with the same name
        # but with different types and only of them enabled
        # ---------------------------------------------------------------------------

        groups = {}
        for bsocket in node_sockets:
            if bsocket.type == 'CUSTOM':
                continue

            if bsocket.is_multi_input:
                self.multi_names.append(bsocket.name)
                self.multi_names.append(utils.snake_case(bsocket.name))
                self.multi_type = SocketType(bsocket)

            name = utils.get_socket_name(bsocket)
            if name not in groups:
                groups[name] = {'count': 0, 'enabled': 0, 'socket_ids': set(), 'bsockets': []}
            groups[name]['count'] += 1
            if bsocket.enabled:
                groups[name]['enabled'] += 1
            groups[name]['socket_ids'].add(bsocket.bl_idname)
            groups[name]['bsockets'].append(bsocket)

        self.homonyms = []
        for name, d in groups.items():
            # A group is made with more than one socket
            if d['count'] == 1:
                continue

            # One socket only must be enabled
            if d['enabled'] != 1:
                continue

            # The number of socket ids must match the number of sockets in the group
            if len(d['socket_ids']) != d['count']:
                continue

            # We have an homonym
            self.homonyms.append(name)

    # ====================================================================================================
    # Get the list of sockets
    # ====================================================================================================

    @property
    def named_sockets(self) -> list[(str, Socket)]:
        """ Returns list of couples (unique name, socket)

        Returns
        -------
        - list of (name, socket)
        """
        keys  = {}
        sockets = []
        for socket in self.node_sockets:

            if socket.type == 'CUSTOM' or not socket.enabled:
                continue

            socket_name = utils.get_socket_name(socket)

            key = (socket_name, socket.type)
            if key in keys:
                keys[key] += 1
                unique = f"{socket_name}_{keys[key]}"
            else:
                keys[key] = 0
                unique = socket_name

            sockets.append((unique, utils.to_socket(socket) if socket.is_output else socket))

        return sockets
    
    def __iter__(self):
        return ((name, socket) for name, socket in self.named_sockets)
    
    @property
    def names(self) -> list[str]:
        return [d[0] for d in self.named_sockets]
    
    @property
    def keys(self) -> list[(str, str)]:
        return [(unique, socket.type) for unique, socket in self]
    
    # ====================================================================================================
    # By index
    # ====================================================================================================

    def by_index(self, index: int) -> Socket:
        return self.named_sockets[index]
    
    def by_identifier(self, identifier: str) -> Socket:
        for socket in self.node_sockets:
            if socket.identifier == identifier:
                return socket
        return None
            
    def by_name(self, name) -> Socket:

        if isinstance(name, tuple) and len(name) == 2:
            stype = SocketType(name[1]).type
            name  = name[0]
        else:
            stype = None

        for unique, socket in self:
            if name not in [unique, utils.snake_case(unique)]:
                continue
            if stype is not None and stype != socket.type:
                continue

            return socket
        
        return None
    
    def __getitem__(self, index) -> Socket:
        socket = None
        if isinstance(index, (int, np.int32, np.int64)):
            socket = self.by_index(index)
        elif isinstance(index, str) or isinstance(index, tuple):
            if isinstance(index, str):
                socket = self.by_identifier(index)
            if socket is None:
                socket = self.by_name(index)
        if socket is None:
            raise IndexError(f"Index {index} not valid in sockets {self.names}.")
        return socket

# ====================================================================================================
# Node
# ====================================================================================================

class Node:
    __slots__ = (
        '_tree', '_bnode', '_inputs', '_outputs',
        '_has_dyn_in', '_has_dyn_out',
        '_has_items', '_items',
        '_use_interface', '_interface', '_interface_in_out',
        '_is_paired_input', '_is_paired_output', '_paired_input_node', '_paired_output_node',
    )
    
    def __init__(self, node_name: str, named_sockets: dict = {}, **parameters):
        """ Node wrapper.

        A node can have dynamic sockets in two ways:
        - _has_items : with an items collection
        - _use_interface : with a NodeTree

        Attributes
        ----------
        - _tree (bpy.types.NodeTree): the tree the node belongs to
        - _bnode (bpy.types.Node): the Blender wrapped Node
        - _has_dyn_in (bool) : able to create dynamic input sockets
        - _has_dyn_out (bool) : able to create dynamic output sockets
        - _has_items (bool) : has at least one collection of dynamic items
        - _items (dict['INPUT', 'OUTPUT']) : items collections or None
        - _use_interface (bool) : the node dynamic sockets are managed with a NodeTree interface
        - _interface (TreeInterface) : interface of the node if it exists
        _ _interface_in_out (dict['INPUT', 'OUTPUT']) : in_out argument to access the Tree
        - _is_paired_input (bool) : the node is the input node of a zone of paired nodes
        - _is_paired_output (bool) : the node is the output node of a zone of paired nodes
        - _paired_input_node (Node) : paired input node
        - _paired_output_node (Node) : paired output node

        > [!NOTE]
        > NodeTree interface is used for Group Input and Output nodes and for Group node.
        > - Group Node : the input sockets are interface sockets for the TreeNode
        > - Group Input Node : the output sockets are input sockets of the interface
        > - Group Output Node : the input sockets are output sockets of the interface

        > [!NOTE]
        >  The '_out' property returns the first enabled output socket

        Arguments
        ---------
        - node_name (str) : Node name
        - named_sockets (dict = {}) : initialization values for the node input sockets
        - **parameters : node parameters and sockets
        """

        # ----------------------------------------------------------------------------------------------------
        # Create the node
        # ----------------------------------------------------------------------------------------------------

        self._tree = Tree.current_tree()

        btree = self._tree._btree
        tree_type = btree.bl_idname

        bl_idname = utils.get_node_bl_idname(node_name, tree_type)

        self._bnode = btree.nodes.new(type=bl_idname)
        self._bnode.select = False
        self._tree.check_node_validity(self._bnode)

        self._inputs  = Sockets(self._bnode.inputs)
        self._outputs = Sockets(self._bnode.outputs)

        # ----------------------------------------------------------------------------------------------------
        # Dynamic sockets with items
        # ----------------------------------------------------------------------------------------------------

        # Able to create sockets
        self._has_dyn_in  = False
        self._has_dyn_out = False

        # Has items
        self._has_items = bl_idname in constants.ONE_ITEMS_NODES
        self._items = {'INPUT': None, 'OUTPUT': None}

        # Paired nodes
        self._is_paired_output = False
        self._is_paired_input  = False

        if self._has_items:
            items = getattr(self._bnode, constants.ONE_ITEMS_NODES[bl_idname])
            items.clear()

            found = False
            for in_out, socks in zip(('INPUT', 'OUTPUT'), (self._bnode.inputs, self._bnode.outputs)):
                for i, sock in enumerate(socks):
                    if sock.type == 'CUSTOM':
                        found = True
                        self._items[in_out] = items
                        break
                if found:
                    break

            assert found, f"Algo error for node [{node_name}], no custom sockets for items '{constants.ONE_ITEMS_NODES[bl_idname]}'."

            self._has_dyn_in  = self._items['INPUT'] is not None
            self._has_dyn_out = self._items['OUTPUT'] is not None

        # ----------------------------------------------------------------------------------------------------
        # Parameters / sockets
        # ----------------------------------------------------------------------------------------------------

        node_info = constants.NODE_INFO[tree_type][bl_idname]

        params  = {}
        sockets = {}
        for name, value in parameters.items():
            if name in node_info['params']:
                params[name] = value
            else:
                sockets[name] = value

        # Parameters first to configure the node
        self.set_parameters(**params)

        # ----------------------------------------------------------------------------------------------------
        # Dynamic sockets with NodeTree
        # ----------------------------------------------------------------------------------------------------

        self._use_interface = False

        if bl_idname == 'NodeGroupInput':

            self._use_interface = True

            self._interface = TreeInterface(self._tree._btree)
            self._interface_in_out  = {'INPUT': None, 'OUTPUT': 'INPUT'}
            self._has_dyn_out = True

        elif bl_idname == 'NodeGroupOutput':

            self._use_interface = True

            self._interface = TreeInterface(self._tree._btree)
            self._interface_in_out  = {'INPUT': 'OUTPUT', 'OUTPUT': None}
            self._has_dyn_in = True

        elif bl_idname == 'ShaderNodeGroup':

            node_tree = parameters.get('node_tree')
            if node_tree is None:
                raise NodeError(f"The node 'Group' must be initialized with a valid 'node_tree' argument.")
            
            self._bnode.node_tree = node_tree

            self._use_interface = True

            self._interface = TreeInterface(self._bnode.node_tree.interface)
            self._interface_in_out  = {'INPUT': 'INPUT', 'OUTPUT': 'OUTPUT'}
            self._has_dyn_in = True
            self._has_dyn_out = True

        # ----------------------------------------------------------------------------------------------------
        # Group Node
        # Read only interface
        # ----------------------------------------------------------------------------------------------------

        elif bl_idname == 'GeometryNodeGroup':

            self._use_interface = True

            self._interface = TreeInterface(self._bnode.node_tree)
            self._interface_in_out  = {'INPUT': 'INPUT', 'OUTPUT': 'OUTPUT'}

        # ----------------------------------------------------------------------------------------------------
        # Node with both in / out items
        # ----------------------------------------------------------------------------------------------------

        elif bl_idname == 'NodeEvaluateClosure':
            self._has_dyn_in  = True
            self._has_dyn_out = True
            self._has_items   = True
            self._items['INPUT']  = self._bnode.input_items
            self._items['OUTPUT'] = self._bnode.output_items

        assert not (self._use_interface and self._has_items), f"Stange Node [{self._bnode.name}] with interface and items."
        
        # ----------------------------------------------------------------------------------------------------
        # Set the sockets
        # ----------------------------------------------------------------------------------------------------

        if bl_idname == 'GeometryNodeMenuSwitch':
            menu_value = None
            for name, value in {**named_sockets, **sockets}.items():
                if name.lower() == 'menu':
                    menu_value = value
                    continue
                self.set_input_socket(name, value)

            if menu_value is not None:
                self.set_input_socket("Menu", menu_value)

        else:
            for name, value in {**named_sockets, **sockets}.items():
                self.set_input_socket(name, value)

        # ----------------------------------------------------------------------------------------------------
        # Register the node
        # ----------------------------------------------------------------------------------------------------

        self._tree.register_node(self)
    
    # ====================================================================================================
    # Dump
    # ====================================================================================================

    def __str__(self):
        if self._has_dyn_in:
            sio = " IO" if self._has_dyn_out else " I"
        else:
            sio = " O" if self._has_dyn_out else ""

        return f"<Node{sio} '{self._bnode.name}' {self._bnode.bl_idname}>"

    def __repr__(self):
        s = str(self)
        s += "\nInputs\n"
        s += "\n   - ".join([bsock.name for bsock in self._bnode.inputs])
        s += "\nOutputs\n"
        s += "\n   - ".join([bsock.name for bsock in self._bnode.outputs])
        s += "\n"

        return s

    # ====================================================================================================
    # Set the node parameters
    # ====================================================================================================

    def set_parameters(self, **parameters):

        for param_name, param_value in parameters.items():

            if param_value is None:
                continue

            # data_type argument
            if param_name == 'data_type':
                param_value = SocketType(param_value).get_node_data_type(self._tree._btree.bl_idname, self._bnode.bl_idname)

            # Domain can be specified by a domain class for a node without domain parameter
            if param_name == 'domain' and not hasattr(self._bnode, 'domain'):
                continue

            try:
                setattr(self._bnode, param_name, param_value)

            except AttributeError as ae:
                print(f"Set Node Parameter error: Node: '{self._bnode.name}', attribute: '{param_name}', value: {param_value}")
                raise ae

            except TypeError as type_e:
                s = str(type_e)
                mark = "not found in "
                i = s.find(mark)
                if i > 0:
                    raise NodeError(f"Node parameter error: '{param_value}' is not a valid value for {param_name}.",
                        node = self._bnode.name,
                        parameter = param_name,
                        valid_values = s[i + len(mark):],
                    )
                else:
                    raise type_e
                
    # ====================================================================================================
    # Accessing the sockets by their name, index or identifier
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # By identifier
    # ----------------------------------------------------------------------------------------------------

    def socket_by_identifier(self,
        in_out      : IN_OUT, 
        identifier  : str, 
        halt        : bool = True,
        ) -> Socket:
        if in_out == 'INPUT':
            for bsock in self._bnode.inputs:
                if bsock.identifier == identifier:
                    return bsock

        elif in_out == 'OUTPUT':
            for bsock in self._bnode.outputs:
                if bsock.identifier == identifier:
                    return utils.to_socket(bsock)

        if halt:
            raise NodeError(f"{in_out} socket with identifier '{identifier}' not found in node '{self._bnode.name}'")

        return None

    # ----------------------------------------------------------------------------------------------------
    # List of sockets
    # ----------------------------------------------------------------------------------------------------

    def get_sockets(self, 
            in_out       : IN_OUT, 
            include      : list = None,
            exclude      : list = [],
            enabled_only : bool = True,
            free_only    : bool = False,
            panel        : str = "") -> list[(str, Socket)]:
        """ Build a list of sockets.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - enabled_only : (bool = True) : ignore disabled sockets
        - free_only : (bool = False) : ignore linked sockets

        Returns
        -------
        - list of sockets
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ====================================================================================================
        # Get from tree interface
        # ====================================================================================================

        if self._use_interface:

            intf_in_out = self._interface_in_out[in_out]
            if intf_in_out is None:
                return []
            
            isocks = self._interface.get_sockets(
                intf_in_out, 
                include      = include,
                exclude      = exclude,
                enabled_only = enabled_only,
                free_only    = free_only,
                parent       = panel,
            )

            sockets = []
            for isock in isocks:
                path = ItemPath(isock) - ItemPath(panel)
                if in_out == 'INPUT':
                    socket = self._bnode.inputs[isock.identifier]
                else:
                    socket = utils.to_socket(self._bnode.outputs[isock.identifier])
                sockets.append((path.path, socket))
            
            return sockets

                

            return [(d['path'], d['socket']) for d in isocks]

        # ====================================================================================================
        # No tree interface
        # ====================================================================================================

        sockets = []

        socks = self._inputs if in_out == 'INPUT' else self._outputs

        panel_path = ItemPath(panel).ranked_long_name

        for name, socket in socks:

            if free_only and not utils.is_free(socket):
                continue

            if panel_path != "" and not name.startswith(panel_path):
                continue

            names = (name, utils.snake_case(name))
            if include is not None:
                ok = False
                for iname in include:
                    if iname in names:
                        ok = True
                        break
                if not ok:
                    continue

            ok = True
            for iname in exclude:
                if iname in names:
                    ok = False
                    break
            if not ok:
                continue

            sockets.append((name, socket))

        return sockets
    
    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its index
    # ----------------------------------------------------------------------------------------------------

    def socket_by_index(self, 
            in_out       : IN_OUT, 
            index        : int, 
            enabled_only : bool = True) -> Socket:
        """ Get a socket by its index

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - index (int) : socket index
        - enabled_only : (bool = True) : ignore disabled sockets

        Raises
        ------
        - IndexError if index is incorrect

        Returns
        -------
        - Socket
        """
        sockets = self.get_sockets(in_out, enabled_only=enabled_only)
        return sockets[index][1]
    
    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its name
    # ----------------------------------------------------------------------------------------------------

    def socket_by_name(self, 
            in_out       : IN_OUT, 
            name         : str, 
            socket_type  : str, 
            enabled_only : bool = True, 
            free_only    : bool = False, 
            halt         : bool = True) -> Socket:
        """ Get a socket by its index

        Get a socket by its name. Valid names are:
        - The socket name possibly suffixed by its rank (e.g. `value_1` for second socket named Value)
        - The python version

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - name (str) : socket name
        - socket_type (str) : socket_type
        - enabled_only : (bool = True) : ignore disabled sockets
        - free_only (bool = False) : ignore linked sockets
        - halt (bool = True) : raises an error if not found

        Raises
        ------
        - AttributeError if name not found

        Returns
        -------
        - Socket
        """

        # ====================================================================================================
        # Get from tree interface
        # ====================================================================================================

        if self._use_interface:

            intf_in_out = self._interface_in_out[in_out]
            if intf_in_out is not None:

                # All the interface socket matching the provided name
                # First With type
                isocks = self._interface.get_socket_by_python_name(
                    intf_in_out, name, socket_type, parent=self._tree.get_panel(), return_all=True)
                
                # Second without type
                if not len(isocks):
                    isocks = self._interface.get_socket_by_python_name(
                        intf_in_out, name, None, parent=self._tree.get_panel(), return_all=True)
                
                # Look for the first one matching the conditions
                for isock in isocks:
                    socket = self.socket_by_identifier(in_out, isock.identifier)
                    bsocket = utils.get_bsocket(socket)

                    if enabled_only and not bsocket.enabled:
                        continue

                    if not free_only:
                        if not utils.is_free(socket):
                            continue

                    return socket
                
            if halt:
                if intf_in_out is None:
                    valids = []
                else:
                    valids = [s.name for s in self._interface.get_sockets(intf_in_out)]

                raise AttributeError(f"Node '{self._bnode.name}' doesn't own an {intf_in_out} socket named '{name}'.\nValids are {valids}")

            return None

        # ====================================================================================================
        # No tree interface
        # ====================================================================================================

        path = ItemPath(name).ranked_long_name

        socks = self._inputs if in_out == 'INPUT' else self._outputs
        socket = socks.by_name(path)

        if socket is None:
            if halt:
                raise AttributeError(f"Node '{self._bnode.name}' doesn't own an {in_out} socket named '{name}'. Valid names are {socks.names}")
            
        return socket


    # ----------------------------------------------------------------------------------------------------
    # Get a socket by something
    # ----------------------------------------------------------------------------------------------------

    def get_socket(self, 
            in_out       : IN_OUT, 
            something    : str | int | Socket, 
            socket_type  : str,
            enabled_only : bool = True, 
            free_only    : bool = False, 
            halt         : bool = True) -> Socket:
        """ Get a socket by a reference

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - something (str | int | Socket) : socket index, name, identifier or the socket itself
        - socket_type (str) : socket type
        - enabled_only : (bool = True) : ignore disabled sockets
        - free_only (bool = False) : ignore linked sockets
        - halt (bool = True) : raises an error if not found

        Returns
        -------
        - Socket if found
        """

        # The result is provided
        socket = utils.get_bsocket(something)
        if socket is not None:
            return socket
        
        # By its index
        if isinstance(something, int):
            return self.socket_by_index(in_out, something, enabled_only=enabled_only)
        
        # Let's try the identifier
        socket = self.socket_by_identifier(in_out, something, halt=False)
        if socket is not None:
            return socket
        
        # Utltimately : the socket name
        return self.socket_by_name(in_out, something, socket_type, enabled_only=enabled_only, free_only=free_only, halt = halt)
    
    # ====================================================================================================
    # Create a new socket from a socket 
    # ====================================================================================================

    def create_from_socket(self,
            in_out  : IN_OUT, 
            socket  : Socket,
            name    : str = None, 
            panel   : str="", **props) -> Socket:
        """ Create a new socket from a socket and link them

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUPUT')) : input or output socket
        - socket (Socket | bpy.types.NodeSocket) : socket to create from
        - panel (str = "") : creation panel
        - props (dict) : additional properties

        Raises
        ------
        - NodeError if impossible to create the socket

        Returns
        -------
        - Socket : the created socket
        """

        # ---------------------------------------------------------------------------
        # Creation must be possible
        # ---------------------------------------------------------------------------

        assert in_out in ('INPUT', 'OUTPUT')

        if (in_out == 'INPUT' and not self._has_dyn_in) or (in_out == 'OUTPUT' and not self._has_dyn_out):
            raise NodeError(f"Impossible to create a {in_out} socket for node {self} (name '{name}').")
        
        bsocket = SocketType.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Invalid socket: {socket}.")
        
        if name is None:
            name = utils.get_default_name(socket)

        # ---------------------------------------------------------------------------
        # Tree interface
        # ---------------------------------------------------------------------------

        if self._use_interface:

            intf_in_out = self._interface_in_out[in_out]
            if intf_in_out is None:
                assert False, f"Shouldn't happen"

            isock = self._interface.create_socket(intf_in_out, name, socket_type=None, parent=self._tree.get_panel(panel), from_socket=bsocket, **props)
            if isock is None:
                raise NodeError(f"Impossible to create the {intf_in_out} socket named in Node {self}", name=name, **props)
            
            created = self.socket_by_identifier(in_out, isock.identifier)        
        
        # ---------------------------------------------------------------------------
        # Items
        # ---------------------------------------------------------------------------

        else:
            full_name = (ItemPath(panel) + name).long_name
            items_type = SocketType(bsocket).items_type

            # No arguments
            if self._bnode.bl_idname in ['GeometryNodeIndexSwitch']:
                self._items[in_out].new()

            # Name only
            elif self._bnode.bl_idname in ['GeometryNodeMenuSwitch']:
                self._items[in_out].new(full_name)

            # For each
            elif self._bnode.bl_idname == 'GeometryNodeForeachGeometryElementOutput':
                if utils.snake_case(panel) == "main":
                    items = self._bnode.main_items
                else:
                    items = self._bnode.generation_items
                items.new(items_type, full_name)

            # Name and data type
            else:
                try:
                    self._items[in_out].new(items_type, full_name)
                except Exception as e:
                    raise RuntimeError(f"Node ({self._bnode.bl_idname}), Socket type: '{items_type}': {str(e)}")

            sockets = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
            created = sockets[-2]

        # ---------------------------------------------------------------------------
        # Link and return
        # ---------------------------------------------------------------------------

        if bsocket.is_output:
            self._tree.link(bsocket, created)
        else:
            self._tree.link(created, bsocket)

        self._update()

        return created
    
    # ====================================================================================================
    # Create a new socket
    # ====================================================================================================

    def create_socket(self, 
            in_out      : IN_OUT, 
            socket_type : str | SocketType, 
            name        : str, 
            panel       : str="",
            **props) -> Socket:
        """ Create a new socket.

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUPUT')) : input or output socket
        - socket_type (str | Socket) : type of socket to create
        - panel (str = "") : creation panel
        - props (dict) : additional properties

        Raises
        ------
        - NodeError if impossible to create the socket

        Returns
        -------
        - Socket (output) or bpy.types.NodeSocket (input) : the created socket
        """

        # ---------------------------------------------------------------------------
        # Creation must be possible
        # ---------------------------------------------------------------------------

        assert in_out in ('INPUT', 'OUTPUT')
        if socket_type is None:
            assert self._bnode.bl_idname in constants.AUTO_INPUT_TYPE_NODES
            socket_type = SocketType(self._bnode.data_type)

        if (in_out == 'INPUT' and not self._has_dyn_in) or (in_out == 'OUTPUT' and not self._has_dyn_out):            
            raise NodeError(f"Impossible to create a {in_out} socket for node {self} (name '{name}').")
        
        # ---------------------------------------------------------------------------
        # Socket type and sub type
        # ---------------------------------------------------------------------------

        socket_type = SocketType(socket_type)
        creation_props = socket_type.set_props({**props})

        # ---------------------------------------------------------------------------
        # Tree interface
        # ---------------------------------------------------------------------------

        if self._use_interface:

            intf_in_out = self._interface_in_out[in_out]
            if intf_in_out is None:
                assert False, f"Shouldn't happen"

            isock = self._interface.create_socket(intf_in_out, name, socket_type, parent=self._tree.get_panel(panel), **creation_props)
            if isock is None:
                raise NodeError(f"Impossible to create the {intf_in_out} socket named in Node {self}", name=name, stype=stype, **creation_props)
            
            socket = self.socket_by_identifier(in_out, isock.identifier)

        # ---------------------------------------------------------------------------
        # Items
        # ---------------------------------------------------------------------------

        else:

            # For each
            if self._bnode.bl_idname == 'GeometryNodeForeachGeometryElementOutput':
                if utils.snake_case(panel) == "main":
                    items = self._bnode.main_items
                else:
                    items = self._bnode.generation_items
            else:
                items = self._items[in_out]

            full_name = (ItemPath(panel) + name).long_name
            if self._bnode.bl_idname in ['GeometryNodeMenuSwitch']:
                items.new(full_name)
            else:
                try:
                    items.new(socket_type.items_type, full_name)
                except Exception as e:
                    raise RuntimeError(f"Node.create_socket: [{self._bnode.bl_idname}], type: {socket_type.class_name}, name: {full_name}.\n{str(e)}")

            io_socks = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
            socket = io_socks[-2]

            # Default on input socket for paired input nodes
            if in_out == 'OUTPUT' and self._is_paired_input:
                def_val = props.get('default', props.get('default_value', None))
                if def_val is not None:
                    try:
                        self._inputs.by_name(full_name).default_value = def_val
                    except Exception as e:
                        pass
                        #raise RuntimeError(f"Erreor setting default val <{def_val}>, Node {self}, {name=}, {full_name=}: {str(e)}")


        self._update()

        return socket
    
    # ====================================================================================================
    # Set an input socket
    # ====================================================================================================

    def set_input_socket(self, 
            name    : str | int, 
            value   : Any, 
            create  : bool = True, 
            panel   : str="", **props):
        """ Set a value to an input socket.

        If name is None (for instance when called by Socket.out()):
        - The first free input socket of the proper type is chosen
        - If not found, a socket is created when possible

        Arguments
        ---------
        - name (Socket | str | int | None) : socket name of socket index
        - value (Socket or any value) : value to set to the socket
        - create (bool = True) : create the value (only for node with dynamic input sockets)
        - panel (str = "") : creation panel
        - props (dict) : additional properties (ignored)

        Raises
        ------
        - AttributeError or IndexError if not found

        Returns
        -------
        - The input socket
        """

        # ----------------------------------------------------------------------------------------------------
        # Multi input socket set with a list of value
        # ----------------------------------------------------------------------------------------------------

        is_multi = name in self._inputs.multi_names
        if is_multi and isinstance(value, list):
            sockets = []
            for v in value:
                sockets.append(self.set_input_socket(name, v, create=False, panel=panel))
            return sockets

        # ----------------------------------------------------------------------------------------------------
        # The input is not a list of values
        # ----------------------------------------------------------------------------------------------------

        if value is None:
            return
        value_socket_type = SocketType(value)
        
        # ===========================================================================
        # Name is the index
        # ===========================================================================

        if isinstance(name, int):
            name = utils.get_socket_name(self._bnode.inputs[name])

        # ===========================================================================
        # Virtual socket : the input socket must exist (or auto data type)
        # ===========================================================================

        if value_socket_type.is_virtual:

            auto = self._bnode.bl_idname in constants.AUTO_INPUT_TYPE_NODES
            halt = name is not None and not auto

            if name is None:
                full_name = None
            else:
                full_name = (ItemPath(panel) + name).path

            # The socket must exist
            in_socket = self.get_socket('INPUT', full_name, value_socket_type, free_only=True, halt=halt)

            # However, if auto data type we can create it
            if in_socket is None and auto:
                in_socket = self.create_socket('INPUT', None, name=name, panel=panel, **props)

            # Error
            if in_socket is None:
                raise RuntimeError(f"Impossible plug an new Input to new Output socket.")

            # Create / link the output socket
            out_socket = value.node.create_from_socket('OUTPUT', in_socket, name=value.name, panel=value.panel, **value.props)

            self._update()

            return in_socket
        
        # ===========================================================================
        # Name is None: value must be a socket
        # ===========================================================================

        if name is None:
            if self._bnode.bl_idname == 'GeometryNodeIndexSwitch':
                name = str(len(self._bnode.index_switch_items) + 1)

        if name is None:

            bsocket = utils.get_bsocket(value)
            if bsocket is None:
                raise NodeError(f"Error when setting an input socket to node {self}: the value must be a socket when name is none ! {value} is not a Socket.")
            
            # ----- First free input socket

            for _, socket in self.get_sockets('INPUT', free_only=True, panel=panel):
                if socket.type == value_socket_type.type: #bsocket.type:
                    self._tree.link(value, socket)
                    return socket
                
            # ----- Not found : let's try to create it

            if not (create and self._has_dyn_in):
                raise NodeError(f"Error when setting an input socket to node {self}: no free input socket found for socket {value} of type: {bsocket.type}.")
            
            name = utils.get_default_name(bsocket)

        # ===========================================================================
        # Name is not None
        # ===========================================================================

        # ---------------------------------------------------------------------------
        # Get the input socket by its name
        # ---------------------------------------------------------------------------

        full_name = (ItemPath(panel) + name).path

        create_socket = create and self._has_dyn_in        
        socket = self.get_socket('INPUT', full_name, value_socket_type, free_only=True, halt=not create_socket)

        # ---------------------------------------------------------------------------
        # Create the dynamic socket
        # ---------------------------------------------------------------------------

        if socket is None:

            if isinstance(value, dict):
                raise RuntimeError(f"Impossible to create an input socket in node {self} with forward creation: type is unknown.")

            # The value is a socket, we create from it and link them

            if utils.get_bsocket(value) is not None:
                return self.create_from_socket('INPUT', value, name=name, panel=panel, **props)

            socket_type = SocketType(value)
            socket = self.create_socket('INPUT', socket_type, name=name, panel=panel, **props)

        # ===========================================================================
        # Set a value to the socket
        # ===========================================================================

        if value is None:
            return socket

        # ---------------------------------------------------------------------------
        # If the value is a Node, we take its default output socket
        # ---------------------------------------------------------------------------

        if '_bnode' in dir(value):
            value = value._out

        # ---------------------------------------------------------------------------
        # If the value is a domain, we take its geometry
        # ---------------------------------------------------------------------------

        if '_geo' in dir(value):
            value = value._geo

        # ---------------------------------------------------------------------------
        # We directly have a socket
        # ---------------------------------------------------------------------------

        out_socket = utils.get_bsocket(value)
        if out_socket is not None:
            self._tree.link(out_socket, socket)
            return socket

        # ---------------------------------------------------------------------------
        # We need to create a node if:
        # - in_socket.hide_value is True
        # - the value is an array containing sockets : vector((0, a, 1))
        # ---------------------------------------------------------------------------

        socket_type = SocketType(socket)
        if socket.hide_value:
            self._tree.link(utils.to_socket(value)._bsocket, socket)
            return socket

        # ---------------------------------------------------------------------------
        # Setting according to the socket type
        # ---------------------------------------------------------------------------

        if socket_type.type in constants.ARRAY_TYPES:

            assert hasattr(socket, 'default_value')

            if socket_type.type == 'RGBA':
                a = utils.value_to_color(value)

            else:
                spec = constants.ARRAY_TYPES[socket_type.type]
                a = utils.value_to_array(value, spec['shape'])

            # There is a bsocket in the array
            if utils.has_bsocket(a):
                v = utils.get_socket_class(socket_type)(a)
                self._tree.link(v, socket)

            else:
                try:
                    socket.default_value = list(a)
                except Exception as e:
                    raise TypeError(f"Impossible to set input socket [{socket.node.name}]{socket.name} with value <{value}>. {str(e)}")

        elif socket_type.class_name in ['Boolean', 'Integer', 'Float', 'String']:
            try:
                socket.default_value = value
            except Exception as e:
                raise TypeError(f"Impossible to set input socket [{socket.node.name}]{socket.name} with value <{value}>. {str(e)}")

        elif socket.type in ['OBJECT', 'COLLECTION', 'IMAGE', 'MATERIAL']:

            bobj = utils.get_blender_resource(socket.type, value)

            if bobj is not None:
                socket.default_value = bobj

        elif socket.type == 'MENU':
            try:
                socket.default_value = str(value)
            except Exception as e:
                raise TypeError(f"Impossible to set menu [{socket.node.name}]{socket.name} with value <{value}>. {str(e)}")

            if self._use_interface:
                isock = self._interface.by_identifier(socket.identifier)
                isock.default_value = socket.default_value

        else:
            raise TypeError(f"Impossible to set input socket [{socket.node.name}]{socket.name} with value <{value}>. Unsupported socket type '{socket.type}'.")
        
        return socket

    # ====================================================================================================
    # Item access
    # ====================================================================================================

    def __getitem__(self, name):
        return self.get_socket('OUTPUT', name)
        #return self.get_output_socket(name)
    
    def __setitem__(self, name, value):
        self.set_input_socket(name, value)

    # ====================================================================================================
    # Attribute
    # ====================================================================================================

    def __getattr__(self, name):
        return self.get_socket('OUTPUT', name, None)

    def __setattr__(self, name, value):
        if name in self.__slots__ or name in dir(Node):
            super().__setattr__(name, value)
            return

        self.set_input_socket(name, value)

    # ====================================================================================================
    # Returns the first enabled output socket
    # ====================================================================================================

    @property
    def _out(self) -> Socket:
        """ Returns the first enabled output socket.

        Returns
        -------
        - Socket : first enabled output socket
        """
        for bsock in self._bnode.outputs:
            if bsock.enabled and bsock.type != 'CUSTOM':
                return utils.to_socket(bsock)
        return None
    
    # ====================================================================================================
    # Update
    # ====================================================================================================

    def _get_interface_socket(self, node_socket: bpy.types.NodeSocket):
        if not node_socket.is_linked:
            return None
        
        input_node = node_socket.links[0].from_node
        if input_node.bl_idname != 'NodeGroupInput':
            return
        
        input_socket = node_socket.links[0].from_socket
        return TreeInterface(self._tree._btree).by_identifier(input_socket.identifier)

    def _update(self):
        """ Update node config after changes
        """

        if self._bnode.bl_idname == 'GeometryNodeIndexSwitch':
            intf_sock = self._get_interface_socket(self._bnode.inputs[0])
            if intf_sock is not None:
                intf_sock.max_value = len(self._bnode.index_switch_items) - 1

        elif self._bnode.bl_idname == 'GeometryNodeMenuSwitch':

            enums = [item.name for item in self._bnode.enum_items]

            if len(enums):
                def_val = enums[0]
                sock = self._bnode.inputs[0]
                if sock.default_value == '':
                    sock.default_value = def_val
                else:
                    def_val = sock.default_value

                def_index = enums.index(def_val)

                intf_sock = self._get_interface_socket(sock)
                if intf_sock is not None:
                    if intf_sock.default_value == '':
                        intf_sock.default_value = def_val

                    for mod in blender.get_geonodes_modifiers(self._tree._btree):
                        if mod.get(intf_sock.identifier):
                            mod[intf_sock.identifier] = def_index + 2


    # ====================================================================================================
    # Signature
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get the signature
    # ----------------------------------------------------------------------------------------------------

    def get_signature(self, 
            include      : list = None, 
            exclude      : list = [], 
            enabled_only : bool = False, 
            free_only    : bool = False,
            with_sockets : bool = False) -> Signature:
        """ Build the signature of the node.

        Arguments
        ---------
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - enabled_only : (bool = True) : ignore disabled sockets
        - free_only : (bool = False) : ignore linked sockets
        - with_socket (bool = False) : include sockets

        Returns
        -------
        - Signature
        """

        sigs = []
        for in_out in ('INPUT', 'OUTPUT'):

            node_sockets = self.get_sockets(
                in_out, 
                include         = include, 
                exclude         = exclude, 
                enabled_only    = enabled_only, 
                free_only       = free_only)

            sig = {}
            #for name, socket in node_sockets.items():
            for name, socket in node_sockets:

                bsocket = utils.get_bsocket(socket)

                sig[name] = {
                    'socket_type' : SocketType(bsocket),
                    'identifier'  : bsocket.identifier,
                }
                
                if with_sockets:
                    sig[name]['socket'] = socket

            sigs.append(sig)

        return Signature(*sigs)

    # ----------------------------------------------------------------------------------------------------
    # Set input signature
    # ----------------------------------------------------------------------------------------------------

    def set_signature(self, 
        in_out      : Literal['INPUT', 'OUTPUT', 'BOTH'],
        signature   : Signature,
        panel       : str = ""):
        """ Set the signature .

        Arguments
        ---------
        - in_out (str in ('INPUT, 'OUTPUT', 'BOTH')) : input or output sockets or both
        - signature (Signature) : the signature to apply
        - panel (str = "") : the panel where to create the sockets

        Returns
        -------
        - dict of created sockets
        """

        sigs = {}
        if in_out == 'INPUT':
            sigs['INPUT'] = signature.sockets
        elif in_out == 'OUTPUT':
            sigs['OUTPUT'] = signature.sockets
        else:
            sigs['INPUT'] = signature.inputs
            sigs['OUTPUT'] = signature.outputs

        created = {}

        for io, sockets in sigs.items():
            
            created[io] = {}

            for spec in sockets: #.items():
                name = spec['name']
                socket = spec.get('socket')

                if socket is None:
                    stype = spec.get('bl_idname', spec.get('socket_type', 'VALUE'))
                    created[io][name] = self.create_socket(io, stype, name=name, panel=panel)
                else:
                    created[io][name] = self.create_from_socket(io, socket, name=name, panel=panel)

        return created
    
    # ====================================================================================================
    # Plug the node
    # ====================================================================================================

    def out(self, panel: str = ""):
        """ Plug the output sockets to the current tree output.

        Arguments
        ---------
        - panel (str = "") : panel to use
        """
        print("WHAT ?", self)
        self.link_outputs(None, to_panel=panel)
        #for name, socket in self.get_sockets('OUTPUT'):
        #    socket.out(name, panel=panel)

    # ====================================================================================================
    # Link input from another node
    # ====================================================================================================

    def link_inputs(self,
        from_node   : Node = None,
        from_panel  : str = "",
        *,
        include     : list =  None,
        exclude     : list  = [],
        panel       : str = "",
        ):
        """ Link input socket from another node

        if from_node is None, the current input node is taken.
        Input sockets already linked are ignored

        If from node is able to create output sockets, they are created, otherwise only the sockets
        with matchin names and types are linked.

        Arguments
        ---------
        - from_node (Node = None) : node to get output sockets from
        - from_panel (str = "") : the panel to use in from_node
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - panel (str = "") : panel to select input socket in
        """

        # ---------------------------------------------------------------------------
        # The list of input sockets to link
        # ---------------------------------------------------------------------------

        if from_node is None:
            from_node = self._tree.get_input_node()

        in_sockets = self.get_sockets(
            'INPUT',
            include      = include,
            exclude      = exclude,
            enabled_only = True,
            free_only    = True,
            panel        = panel,
            )
        
        # ---------------------------------------------------------------------------
        # Create the links
        # ---------------------------------------------------------------------------
        
        links = []
        
        for name, in_socket in in_sockets:

            path = ItemPath(from_panel) + name

            out_socket = from_node.socket_by_name('OUTPUT', path, SocketType(in_socket).type, halt=False)

            if out_socket is None:
                if from_node._has_dyn_out:
                    out_socket = from_node.create_from_socket('OUTPUT', in_socket, name=path)

            if out_socket is not None:
                self._tree.link(out_socket, in_socket)
                links.append((out_socket, in_socket))

        return links
    
    # ====================================================================================================
    # Link input from another node
    # ====================================================================================================

    def link_outputs(self,
        to_node     : Node = None,
        to_panel    : str = "",
        *,
        include     : list =  None,
        exclude     : list  = [],
        panel       : str = "",
        ):
        """ Link output socket to another node

        if to_node is None, the current output node is taken.

        If from node is able to create output sockets, they are created, otherwise only the sockets
        with matchin names and types are linked.

        Arguments
        ---------
        - to_node (Node = None) : node to plug into
        - to_panel (str = "") : the panel to use in to_node
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - panel (str = "") : panel to select input socket in
        """

        # ---------------------------------------------------------------------------
        # The list of output sockets to link
        # ---------------------------------------------------------------------------

        if to_node is None:
            to_node = self._tree.get_output_node()

        out_sockets = self.get_sockets(
            'OUTPUT',
            include      = include,
            exclude      = exclude,
            enabled_only = True,
            panel        = panel,
            )
        
        # ---------------------------------------------------------------------------
        # Create the links
        # ---------------------------------------------------------------------------
        
        links = []
        
        for name, out_socket in out_sockets:

            path = (ItemPath(to_panel) + name).path

            in_socket = to_node.socket_by_name('INPUT', path, SocketType(out_socket).type, halt=False)

            if in_socket is None:
                if to_node._has_dyn_in:
                    in_socket = to_node.create_from_socket('INPUT', out_socket, name=path)

            if in_socket is not None:
                self._tree.link(out_socket, in_socket)
                links.append((out_socket, in_socket))

        return links

    # ====================================================================================================
    # Color and label
    # ====================================================================================================

    @property
    def _color(self):
        return self._bnode.color

    @_color.setter
    def _color(self, value):
        print("?????? COLOR")
        if value is None:
            self._bnode.use_custom_color = False
            return

        if isinstance(value, str):
            value = Tree._get_color(value)

        self._bnode.use_custom_color = True
        self._bnode.color = value

    @property
    def _label(self):
        return self._bnode.label

    @_label.setter
    def _label(self, value):
        if value is None:
            return
        self._bnode.label = value

    # ====================================================================================================
    # Pin gizmo
    # The first input socket
    # ====================================================================================================

    @property
    def pin_gizmo(self):
        return self._bnode.inputs[0].pin_gizmo

    @pin_gizmo.setter
    def pin_gizmo(self, value):
        self._bnode.inputs[0].pin_gizmo = value

    # ====================================================================================================
    # Context management
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Push for capturing socket.out() and possibly zone input creation
    # ----------------------------------------------------------------------------------------------------

    def _push(self):

        # Becomes the output node
        self._tree._output_stack.append(self)

        # Becomes input node is possible
        if self._has_dyn_out:
            self._tree._input_stack.append(self)

    # ----------------------------------------------------------------------------------------------------
    # Pop capturing sockets in/out
    # ----------------------------------------------------------------------------------------------------

    def _pop(self, error: bool = False):

        assert self._tree._output_stack.pop() == self

        # Was input node
        if self._has_dyn_out:
            assert self._tree._input_stack.pop() == self

    # ----------------------------------------------------------------------------------------------------
    # Context management
    # ----------------------------------------------------------------------------------------------------

    def __enter__(self):
        self._push()
        return self

    def __exit__(self, type, exc_value, traceback):

        ok = exc_value is None or isinstance(exc_value, Break)

        self._pop(not ok)

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Node, Group, Closure, Group, Layout, Bundle
        
        group_name = "Group Demo"

        # ---------------------------------------------------------------------------
        # Group
        # ---------------------------------------------------------------------------
        
        with GeoNodes(group_name, is_group=True):
            
            # Link with two input values both named "Value"
            # Panel: Math
            node0 = Node('Math')
            node0._bnode.label = "A: From 'Add'"
            node0.link_inputs(None, "Add")
            
            # Link another Add node
            node1 = Node('Math')
            node1._bnode.label = "B: From A & 'Add'"
            node1.link_inputs(node0)            
            node1.link_inputs(None, "Add")
            node1.link_outputs(None, "Add")
            
            # A new math with "Value", "Multiplier", "Addend"
            node = Node('Math', operation='MULTIPLY_ADD')
            node._bnode.label = "C: panel 'Mul Add"
            node.link_inputs(None, "Mul Add", )
            node.link_inputs(None, "Mul Add")
            node.link_outputs(None, "Mul Add")

        # ---------------------------------------------------------------------------
        # Modifier
        # ---------------------------------------------------------------------------

        with GeoNodes("Node Class Test") as tree:
            
            with Layout("In/Out linked to Group", color=(.3, .1, .1)):
                node = Node('Raycast')
                node.link_inputs(None)            
                node.link_outputs(None)
                
            with Layout("In/Out linked to panel named \"Second\"", color=(.1, .4, .1)):                
                node = Node('Raycast')
                node.link_inputs(None, "Second")            
                node.link_outputs(None, "Second")
                
            with Layout("Filtering inputs and outputs sockets", color=(.1, .1, .4)):
                node = Node('Raycast')
                node.link_inputs(None, "Filtered", exclude=["Source Position", "Ray Direction"])
                node.link_outputs(None, "Filtered", include=["Hit Position"])
                
            with Layout("Node embedded in a closure", color=(.4, .1, .4)):
                with Closure() as cl:
                    node = Node('Raycast')
                    node.link_inputs(None, "Raycast", exclude=["Interpolation", ])
                    node.link_outputs(None, "Raycast", include=["Is Hit", "Hit Position"])
                    
                cl.out()
                    
            with Layout("Node feeding a Bundle", color=(.1, .4, .4)):
                with Bundle() as b:
                    node = Node('Raycast')
                    node.out()
                    
                b.out()
                
            with Layout("Create Separate Bundle from a Node", color=(.1, .4, .4)):
                b = Bundle(name="Bundle")
                with b.separate():
                    node = Node('Raycast')
                    node.link_inputs(None, exclude=["Interpolation"])
                    
            with Layout("Linking a Node Group"):
                g = Group(group_name)
                g.link_inputs(None, "Group 'Add'", panel="Add")
                g.link_outputs(None, "Group 'Mul Add'", panel="Mul Add")
                g.link_outputs(None, "Group 'Add New'", panel="Add")
                
                with Layout("To a Closure"):
                    with Closure() as cl:
                        g = Group(group_name)
                        g.link_inputs(None)
                        g.link_outputs(None)
                        
                cl.out()

            with Layout("Built in Group"):
                g = Group("Curve to Tube")
                g.link_inputs(None, "Tube")
                g.link_outputs(None, "Tube")

# ====================================================================================================
# Zone Iterator
# ====================================================================================================

class ZoneIterator:

    SIMULATION = "Simulation"
    REPEAT     = "Repeat"
    FOR_EACH   = "For Each Element"

    __slots__ = ('_socket', '_input_node', '_output_node', '_name', '_done', '_in_zone')

    def __init__(self, socket: Socket, node: Node):
        """ Wrap the nodes creation within a zone.

        The ZoneIterator wraps a pair of nodes forming a zone : Simulation, Repeat, For Each, Closure.

        The iteration contains exactly one iteration in order to generate the nodes only once.

        The first call to __next__ method pushes the input and output nodes in order to capture inputs and outputs.
        The second call pops the i/o capture and raises StopIteration.

        The iterator returns itself as it exposes the nodes sockets:
        - During the iteration, the input sockets are the ones of the output node and the output sockets are
          the ones of the input node.
        - Outside the iteration, the input sockets are the ones of the input node and the output sockets are
          the ones of the output node.

        ``` python
        geo = Geometry()
        for sim in geo.simulation(A=1.0):
            
            # Output sockets come from input node
            a = sim.a

            # Sockets creation is captured
            # A new simulation socket named B is created
            b = Float(2.0, name="B")

            # Input sockets come from output node
            sim.a = a + b

            # Output is captured
            sim.b = a - b
            
            # No socket C was created
            try:
                sim.c = 0
            except AttributeError:
                print("An error is raised when accessing a non existing socket")

            # Within the loop, geo socket comes from input node
            # 
            geo.position += a

            # Default output geometry is in output node
            geo.out()

        # Outside the loop, geometry is now the output node output geometry
        # The zone output sockets can be accessed from simulation
        geo.position += sim.a

        geo.out()
        ```

        Arguments
        ---------
        - socket (Socket) : the socket to loop on
        - node (Node) : a valid zone output node
        """

        node_id       = node._bnode.bl_idname

        if node_id == 'GeometryNodeRepeatOutput':
            self._name = ZoneIterator.REPEAT

        elif node_id == 'GeometryNodeSimulationOutput':
            self._name = ZoneIterator.SIMULATION

        elif node_id == 'GeometryNodeForeachGeometryElementOutput':
            self._name = ZoneIterator.FOR_EACH

        else:
            raise RuntimeError(f"ZoneIterator must be initialized with a 'Repeat', 'Simulation' or 'For Each Element' output node, not {node}.")

        self._socket        = socket
        self._output_node   = node
        self._input_node    = node._paired_input_node
        self._done          = False
        self._in_zone       = False

    def __str__(self):
        return f"<ZoneIterator {self._name}, in_zone: {self._in_zone}, done: {self._done}>"

    # ====================================================================================================
    # Iteration
    # ====================================================================================================

    def __iter__(self):

        self._done = False
        self._output_node._push_paired()

        if self._socket is not None:

            if self._name == ZoneIterator.REPEAT:
                self._socket._jump(self._input_node._bnode.outputs[1])

            elif self._name == ZoneIterator.SIMULATION:
                self._socket._jump(self._input_node._bnode.outputs[1])

            elif self._name == ZoneIterator.FOR_EACH:
                self._socket._jump(self._input_node._bnode.outputs[1])

            else:
                assert False

        return self

    def __next__(self):
        if self._done:
            self._output_node._pop_paired()
            self._socket._jump(self._output_node._out)
            self._in_zone = False

            raise StopIteration
        
        else:
            self._done = True
            self._in_zone = True
            return self
        
    # ====================================================================================================
    # Attributes
    # ====================================================================================================

    def __setattr__(self, name, value):
        if name in ZoneIterator.__slots__:
            super().__setattr__(name, value)
            return
        
        if self._in_zone:
            setattr(self._output_node, name, value)
        else:
            setattr(self._input_node, name, value)

    def __getattr__(self, name):
        if self._in_zone:
            return getattr(self._input_node, name)
        else:
            return getattr(self._output_node, name)

          

# ====================================================================================================
# Group
# ====================================================================================================

class Group(Node):

    def __init__(self, group_name: str, named_sockets: dict = {}, **sockets):
        """ Node Group

        > Node <&Node Group>

        Create a node 'Group' with the tree provided with 'group_name' argument.

        The sockets can be initialized either using the sockets dictionary or using they snake_case name
        as kwargs arguments.

        ``` python
        # Create a utility group
        with GeoNodes("Add two values", is_group=True):

            a = Float(0, "a")
            b = Float(0, "b")

            (a + b).out("Sum")

        # A node calling the utility group
        with GeoNodes("Call a group"):

            Geometry().out()

            c = Group("Add two values", {'a': Float(10, 'a'), 'b': Float(10, 'b')}).sum
            node = Group("Add two values")

            node.a = 100
            node.b = 200

            c.out("c")
            node._out.out("d")
        ```

        Arguments
        ---------
        - group_name (str) : name of the group to use
        - named_sockets (dict) : sockets initialization values
        - **sockets (dict) : sockets  initialization with their snake_case name

        Returns
        -------
        - Node Group
        """

        tree = Tree.current_tree()

        # ----------------------------------------------------------------------------------------------------
        # Get the node group by its name
        # ----------------------------------------------------------------------------------------------------

        spec = utils.get_available_groups(tree._btree.bl_idname).get(group_name, {})
        node_tree = blender.load_node_group(spec)
        if node_tree is None:
            raise NodeError(f"Impossible to find the group named '{group_name}'")
        
        # ----------------------------------------------------------------------------------------------------
        # Super init
        # ----------------------------------------------------------------------------------------------------

        super().__init__('Group', named_sockets=named_sockets, node_tree=node_tree, **sockets)



    # ----------------------------------------------------------------------------------------------------
    # Prefixed instantiation
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Prefix(cls, prefix, group_name, named_sockets={}, **sockets):
        """ Call a Group with a prefixed named.

        > Node <&Node Group>

        Using a prefix for groups of the same type can be usefull in big projects with
        a lot of groups.

        ``` python
        # Prefix used to identifiy utility groups
        UTIL = "UTIL"

        # Create a group utility
        with GeoNodes("Add two values", prefix=UTIL, is_group=True):

            a = Float(0, "a")
            b = Float(0, "b")

            (a + b).out("Sum")

        with GeoNodes("Call a group"):

            Geometry().out()

            # Call the the prefixed utility
            c = Group.Prefix(UTIL, "Add two values", {'a': Float(10, 'a'), 'b': Float(10, 'b')}).sum

            # Call the the prefixed utility
            node = Group.Prefix(UTIL, "Add two values")

            node.a = 100
            node.b = 200

            c.out("c")
            node._out.out("d")
        ```

        Arguments
        ---------
        - prefix (str) : prefix
        - group_name (str) : name of the group to use
        - sockets (dict) : sockets initialization values
        - **kwargs (dict) : sockets  initialization with their snake_case name

        Returns
        -------
        - Node Group
        """
        return cls(f"{prefix} {group_name}", named_sockets=sockets, **sockets)

# ====================================================================================================
# G to expose groups as functions
# ====================================================================================================

class G:

    VERBOSE = False

    def __init__(self, prefix: str = "", verbose: bool = False):
        """ Group functional call

        This class is provided to expose ***Group*** nodes as functions with keyword arguments.

        For instance, let's create a group with 3 input sockets named `Geometry`, `Position` and `Parameter` in
        this order:


        ``` python
        with GeoNodes("Deform Function"):
            geo = Geometry()
            pos = Vector.Position()
            param = Float(0, "Parameter")
            # ...
            geo.out()
        ```

        To use this group in another tree, you can write:

        ``` python
        with GeoNodes("Modifier"):

            node = Group("Deform Function", {'geometry': Mesh.Cube(), 'position': (1, 2, 3), 'parameter': 3.14})

            # or

            node = Group("Deform Function", geometry=Mesh.Cube(), position = nd.position, parameter = 3.14)
        ```

        The class G provides a functional interface for the node. You simply use the snake case version
        of the node name:

        ``` python
        my_geo = G().deform_function(Mesh.Cube(), position=nd.position, parameter=3.14)

        # NOTE: the first output socket is returned
        # If you need the node, simply use:

        node = my_geo.node
        ```

        As for any function or method, you can omit the argument names if you are sure of the order of the
        sockets. This is for instance the case for the `Geometry` socket which remains the first.

        #### Prefixes

        In big projects, you may want to prefix your groups and modifiers to structure them.
        The ***G*** class accepts prefix and use it to build the full name of the tree you are looking for.

        The code above could be replaced by:

        ``` python
        my_geo = G("Deform").function(Mesh.Cube(), position=nd.position, parameter=3.14)
        ```

        This allows to regroup modifiers of the same family in a kind of meta class:

        ``` python
        # Prefix for deform modifiers
        deform = Group("Deform")

        with Group("Function 1", prefix=deform):
            pass

        with Group("Function 2", prefix=deform):
            pass

        with Group("Function 3", prefix=deform):
            pass

        with Group("Main"):

            geo = Geometry()
            geo = deform.function_1(geo)
            geo = deform.function_2(geo)
            geo = deform.function_3(geo)

            geo.out()
        ```

        Arguments
        ---------
        - prefix : prefix to use when searching a tree
        - verbose : print the function header in the console
        """
        if prefix is None:
            self.prefix = ""
        else:
            self.prefix = str(prefix)
            if len(self.prefix):
                self.prefix += " "
        self.verbose = verbose

    # ====================================================================================================
    # Str returns a string to be compatible with prefix argument in Tree initialization

    def __str__(self):
        if self.prefix == "":
            return ""
        else:
            return self.prefix[:-1]

    # ====================================================================================================
    # Build a function from a node

    def build_function(self, btree):
        """ Dynamically create a function to call the tree as Group

        The name of the function is the snake case version of the tree name.

        Arguments
        ---------
        - btree (Blender GeometryNodeTree | ShaderNodeTree) : the tree
        - prefix (str = "") : function prefix

        Returns
        -------
        - None
        """

        func_name = utils.snake_case(btree.name)

        # ---------------------------------------------------------------------------
        # Arguments from signature
        # ---------------------------------------------------------------------------

        signature = TreeInterface(btree).get_signature()
        #sock_names = [utils.snake_case(name) for name in signature.inputs.keys()]
        sock_names = [utils.snake_case(d['name']) for d in signature.inputs]

        if False:
            # ----- Input node

            socks, homos = TreeInterface(btree).get_sockets_names('INPUT', python=True, homonyms='SEPARATE')

            sock_names = list(socks.keys())
            sock_names.extend(list(homos.keys()))
            sock_names.append('link_from')

        # ----- Create the function

        header = [f"{arg}=None"  for arg in sock_names]
        call   = [f"{arg}={arg}" for arg in sock_names]

        s = f"def {func_name}(" + ", ".join(header) + "):\n"
        s += f"\treturn Group('{btree.name}', " + ", ".join(call) + ")._out\n\n"
        s += f"f = {func_name}\n"

        # DEBUG
        if False:
            print('-'*100)
            print(s)
            print('-'*100)

        d = {'f': None}
        exec(s, globals(), d)
        f = d['f']

        if G.VERBOSE or self.verbose:
            print('-'*100)
            print(f"Function created ({f}):\n    {func_name}(" + ", ".join([sname for sname in sock_names if sname != 'link_from']) + ")")
            print()
            print(s)
            print()

        #return getattr(G, func_name)
        return f

    # ====================================================================================================
    # Get a tree by its snake case name

    def __getattr__(self, name):

        tree_type = Tree.current_tree()._btree.bl_idname
        groups = utils.get_available_groups(tree_type)

        target = utils.snake_case(self.prefix + name)
        group_name = utils.find_snake_case_name(target, list(groups.keys()))
        if group_name is None:
            raise AttributeError(f"Group '{self.prefix + name}' not found")
        
        group = blender.load_node_group(groups[group_name])
        return self.build_function(group)


# ====================================================================================================
# GroupF
# ====================================================================================================

class GroupF:
    """ Utility class exposing Groups as python functions.

    This class provides an alternative to 'Group' to call groups. The snake case version of the group name is
    used as method name of an instance of GroupF: ``` Group("Group Name") ``` is replaced by
    ``` GroupF().group_name() ```.

    If the group is uses a prefix, the prefix is passed as init argument in GroupF : ``` GroupF(prefix).group_name() ```.

    The arguments can be passed either using the socket names in a dict or as kwargs arguments.

    ``` python
    # Prefix used to identifiy utility groups
    UTIL = "UTIL"

    # Create a group utility
    with GeoNodes("Subtract two values", is_group=True):

        a = Float(0, "a")
        b = Float(0, "b")

        (a + b).out("Diff")


    # Create a prefixed group utility
    with GeoNodes("Add two values", prefix=UTIL, is_group=True):

        a = Float(0, "a")
        b = Float(0, "b")

        (a + b).out("Sum")

    with GeoNodes("Gourp function call"):

        Geometry().out()

        a = Float(10, "a")
        b = Float(20, "b")

        # Call the the utility
        c = GroupF().subtract_two_values({'a': a}, b=b)._out

        # Call the the prefixed utility
        d = GroupF(UTIL).add_two_values(a=a, b=b)._out

        c.out("c")
        d.out("d")
    ```
    """

    def __init__(self, prefix=None):
        if prefix is None:
            self._prefix = ""
        else:
            self._prefix = prefix.lower() + '_'

        print("GroupF is deprecated. Use G insted")

    @staticmethod
    def call(group_name, sockets={}, link_from=None, **kwargs):
        print("GroupF is deprecated. Use G insted")
        return Group(group_name, sockets, link_from=link_from, **kwargs)

    def __getattr__(self, name):
        name = self._prefix + name

        for group_name in bpy.data.node_groups.keys():

            if utils.snake_case(group_name) == name:

                def f(sockets={}, **kwargs):
                    return Group(group_name, sockets, **kwargs)

                return f

        raise AttributeError(f"Impossible to find the group named '{name}'")


# ====================================================================================================
# ====================================================================================================
# Specific nodes
# ====================================================================================================
# ====================================================================================================

# ====================================================================================================
# Color Ramp
# ====================================================================================================

class ColorRamp(Node):
    def __init__(self, fac=None, stops=None, interpolation='LINEAR'):
        """ Node <&Node Color Ramp>

        Exposes utilities to manage the color ramp

        ``` python
        ramp1 = Float(.5).color_ramp(stops=[.1, .9])
        ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
        ```

        Arguments
        ---------
        - fac (Float = None)
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)
        - interpolation in ('EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT')
        """
        super().__init__('Color Ramp', {'Fac': fac})
        self.color_ramp.interpolation = interpolation
        #self.interpolation = interpolation
        self.stops = stops

    @property
    def color_ramp(self):
        """ Returns the node color_ramp structure

        Returns
        -------
        - bpy.types.ColorRamp
        """
        return self._bnode.color_ramp

    @property
    def interpolation(self):
        """ Node color_ramp interpolation

        Returns
        -------
        - str
        """
        return self.color_ramp.interpolation

    @interpolation.setter
    def interpolation(self, interpolation):
        utils.check_enum_arg(arg_name='interpolation', arg_value=interpolation, meth_name='interpolation',
            valids=('EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT'))
        self.color_ramp.interpolation = interpolation

    @property
    def stops(self):
        """ Get the list of stops

        Returns
        -------
        - list of tuples : (float, color)
        """
        return utils.color_ramp_get_stops(self.node._bnode, as_str=False)

    @stops.setter
    def stops(self, stops):
        """ Set the color ramp stops

        ``` python
        ramp =

        Arguments
        ---------
        - stops : list of tuple (position, color)
        """
        if stops is not None:
            self.set_stops(*stops)

    def set_stops(self, *stops):
        if len(stops) == 0:
            return

        elements = self.color_ramp.elements
        for i, stop in enumerate(stops):

            position : float
            color    : tuple = None
            if isinstance(stop, (tuple, list)):
                if len(stop) == 2:
                    position = stop[0]
                    color    = stop[1]
                else:
                    raise NodeError(f"ColorRamp set_stops error: stops must be tuple(position, color) or single position, not {stop}")

            else:
                position = stop

            if color is not None:
                if hasattr(color, '__len__'):
                    if len(color) == 3:
                        color = color + (1,)
                else:
                    color = tuple(np.resize(color, 3)) + (1,)

            if i < len(elements):
                elements[i].position = position
            else:
                elements.new(position)

            if color is not None:
                elements[i].color = color

        for i in range(len(stops), len(elements)):
            elements.remove(elements[-1])

# ====================================================================================================
# Node Curves
# ====================================================================================================

class NodeCurves(Node):

    # =============================================================================================================================
    # Set / Get the curves

    # -----------------------------------------------------------------------------------------------------------------------------
    # curve 0 (for Float Curve)

    def get_curve(self):
        """ Get the Float Curve as a list of tuples

        Each tuple is a triplet
        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Returns
        -------
        - list of 3-tuples : float, float, str in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')
        """
        return self.get_curves()[0]

    def set_curve(self, curve):
        """ Set the Float Curve as a list of tuples

        > [!NOTE]
        > handle_type is optional, its default value is 'AUTO'. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Arguments
        ---------
        - curves : list of 3-tuples (x, y, handle_type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR'))

        Returns
        -------
        - self
        """
        self.set_curves([curve])
        return self

    # -----------------------------------------------------------------------------------------------------------------------------
    # All curves (for Color Curves and Vector Curves)

    def get_curves(self):
        """ Get the curves as a list of list of tuples

        Each tuple is a triplet
        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Returns
        -------
        - list of lists of triplets
        """
        return utils.curves_to_list(self.node._bnode.mapping.curves)

    def set_curves(self, curves):
        """ Set the curves points position

        > [!NOTE]
        > handle_type is optional, its default value is 'AUTO'. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Arguments
        ---------
        - curves : list of 3-tuples (x, y, handle_type) or list of such lists

        Returns
        -------
        - self
        """
        if curves is not None:
            utils.list_to_curves(curves, self.node._bnode.mapping.curves)
        return self
    


