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

from typing import Literal
import numpy as np
import bpy
from time import time

from . import blender
from .scripterror import NodeError
from . import constants
from . import utils
from .sockettype import SocketType
from .utils import Break
from .signature import Signature
from .treeclass import Tree
from .treeinterface import TreeInterface

IN_OUT = Literal['INPUT', 'OUTPUT']

# ====================================================================================================
# Node
# ====================================================================================================

class Node:
    __slots__ = [
        '_tree', '_bnode', '_has_dyn_in', '_has_dyn_out',
        '_has_items', '_items',
        '_use_interface', '_interface', '_interface_in_out',
        '_is_paired_input', '_is_paired_output', '_paired_input_node', '_paired_output_node',
        ]
    
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
        self._is_paired_input = False

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
        # Node with both in / out items
        # ----------------------------------------------------------------------------------------------------

        elif bl_idname == 'NodeEvaluateClosure':
            self._has_dyn_in  = True
            self._has_dyn_out = True
            self._has_items   = True
            self._items['INPUT']  = self._bnode.input_items
            self._items['OUTPUT'] = self._bnode.output_items

        # ----------------------------------------------------------------------------------------------------
        # Paired nodes
        #
        # When creating a paired output node, the corresponding input node is also created
        # and both are paired.
        #
        # The two nodes can have dynamic sockets as described below
        #
        #   Zone          Input Node          Output Node
        #   ----------    ------------        ------------
        #   Repeat          dyn_out                x
        #   Simulation      dyn_out                x
        #   For Each        dyn_out              dyn_in (two panels)
        #   Closure         dyn_out              dyn_in
        # ----------------------------------------------------------------------------------------------------

        elif bl_idname in [
            'GeometryNodeRepeatInput',
            'GeometryNodeSimulationInput',
            'GeometryNodeForeachGeometryElementInput',
            'NodeClosureInput',
            ]:

            # ---------------------------------------------------------------------------
            # Consume output_node parameter
            # ---------------------------------------------------------------------------

            output_node = parameters.get('output_node')
            if output_node is None:
                raise NodeError(f"The node '{node_name}' must be initialized with a valid 'output_node' argument.")
            
            parameters = {k: v for k, v in parameters.items() if k != 'output_node'}
            
            # Pairing

            self._is_paired_input = True
            self._paired_output_node = output_node
            self._bnode.pair_with_output(output_node._bnode)

            # ---------------------------------------------------------------------------
            # Repeat, Simulation
            #
            # - Input Node  : dynamic inputs to feed zone entry
            # - Output Node : no dynamic sockets

            """
            ``` python
            
            geo = Geometry()
            for sim in geo.simulation(Float=0.0):
            
                # Reading output socket from input node 
                a = sim.Float

                # Create an new zone input socket
                b = Float(1, name="Another Float")

                # Outing the computation
                a.out() # First free: Float
                b.out() # First free: Another Float

                # Outing the geometry
                geo.out()

            # Outside the context, geo is now the output socket of the output node
            geo.out()

            # Other output sockets are peer of geo socket
            a = geo.Float_ # P
            ```
            """

            self._has_dyn_out = True
            self._has_items = True

            if bl_idname == 'GeometryNodeRepeatInput':
                self._items['OUTPUT'] = self._paired_output_node._bnode.repeat_items

            elif bl_idname == 'GeometryNodeSimulationInput':
                self._items['OUTPUT'] = self._paired_output_node._bnode.state_items

            # ---------------------------------------------------------------------------
            # For each element
            #
            # - Input Node  : dynamic inputs to feed zone entry
            # - Output Node : dynamic inputs sockets
            #
            # Output sockets can be created
            # - Main (default) : with panel other than Generated
            # - Generated : when panel argument is Generated
            #
            # for feel in mesh.faces[sel].for_each_element(i=0):
            #     Float(1, name="Float") # Create a new input socket in input node
            #     f = feel.float         # Output socket of input node
            #     i = feel.i             # Same
            #     f.out("Float")         # Create output socket in Main panel
            #     feel.element.out(panel="Generated")  # Link to output socket in Generated panel
            #
            # geo.out()                  # Outside the zone plug to group output
            # ---------------------------------------------------------------------------

            elif bl_idname == 'GeometryNodeForeachGeometryElementInput':
                # ['generation_items', 'input_items', 'main_items'],
                self._items['OUTPUT'] = self._paired_output_node._bnode.input_items

            # ---------------------------------------------------------------------------
            # Closure
            #
            # - Input Node  : dynamic outputs as closure input
            # - Output Node : dynamic inputs as closure output
            #
            # with Closure() as closure:
            #     f = Float(3.14, "Pi") # Closure input
            #     f.out("Float")        # Closure output
            #
            # closure.out()             # To Group output
            # ---------------------------------------------------------------------------
            
            elif bl_idname == 'NodeClosureInput':
                self._items['OUTPUT'] = self._paired_output_node._bnode.input_items

        # Paired output used to create the pair
                
        elif bl_idname in [
            'GeometryNodeRepeatOutput',
            'GeometryNodeSimulationOutput',
            'GeometryNodeForeachGeometryElementOutput',
            'NodeClosureOutput',
            ]:

            # Create the paired input node
            self._is_paired_output = True
            self._paired_input_node = Node(bl_idname[:-6] + 'Input', named_sockets, output_node = self, **parameters)

            # Consumed by input node
            named_sockets = {}
            parameters = {}

            # For Each zone : input sockets can be created in two panels
            if bl_idname == 'GeometryNodeForeachGeometryElementOutput':
                self._has_dyn_in = True
                self._has_items  = True
                # Two panels
                self._items['INPUT'] = {
                    "Main":      self._bnode.main_items,
                    "Generated": self._bnode.generation_items,
                }

            # Closure zone
            elif bl_idname == 'NodeClosureOutput':
                self._has_dyn_in = True
                self._has_items  = True
                self._items['INPUT'] = self._bnode.output_items

        assert not (self._use_interface and self._has_items), f"Stange Node [{self._bnode.name}] with interface and items."
        
        # ----------------------------------------------------------------------------------------------------
        # Parameters / sockets
        # ----------------------------------------------------------------------------------------------------

        node_info = constants.NODE_INFO[tree_type][bl_idname]

        params = {}
        sockets = {}
        for name, value in parameters.items():
            if name in node_info['params']:
                params[name] = value
            else:
                sockets[name] = value

        # Parameters first to configure the sockets
        self.set_parameters(**params)

        # Plug the sockets
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

    def socket_by_identifier(self, in_out: IN_OUT, identifier: str, halt: bool = True):
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
    # Dictionary socket names -> sockets
    # ----------------------------------------------------------------------------------------------------

    def get_sockets(self, 
            in_out: IN_OUT, 
            include: list = None,
            exclude: list = [],
            enabled_only: bool = True,
            free_only: bool = False) -> dict:
        """ Build a dictionary keyed by the socket unique names

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - enabled_only : (bool = True) : ignore disabled sockets
        - free_only : (bool = False) : ignore linked sockets

        Returns
        -------
        - dict : name -> socket
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ====================================================================================================
        # Get from tree interface
        # ====================================================================================================

        if self._use_interface:

            intf_in_out = self._interface_in_out[in_out]
            if in_out is None:
                return {}
            isocks = self._interface.get_shortest_names(intf_in_out)

            sockets = {}
            for name, isock in isocks.items():
                socket = self.socket_by_identifier(in_out, isock.identifier)

                # enabled only
                if (not socket.enabled) and enabled_only:
                    continue

                # free only
                if free_only and not utils.is_free(socket):
                    continue

                # include list
                if include is not None:
                    keep = False
                    for name in include:
                        if intf_in_out.socket_matches_name(isock, name):
                            keep = True
                            break
                    if not keep:
                        continue

                # exclude list
                keep = True
                for name in exclude:
                    if intf_in_out.socket_matches_name(isock, name):
                        keep = False
                        break
                if not keep:
                    continue

                # We can keep it
                sockets[name] = socket

            return sockets

        # ====================================================================================================
        # No tree interface
        # ====================================================================================================

        is_in = in_out == 'INPUT'
        bsockets = self._bnode.inputs if is_in else self._bnode.outputs

        # ---------------------------------------------------------------------------
        # First pass : consider as one socket all the sockets with the same name
        # but with different types and only of them enabled
        # ---------------------------------------------------------------------------

        groups = {}
        for bsocket in bsockets:
            if bsocket.type == 'CUSTOM':
                continue

            name = utils.get_socket_name(bsocket)
            if name not in groups:
                groups[name] = {'count': 0, 'enabled': 0, 'bl_idnames': set(), 'bsockets': []}
            groups[name]['count'] += 1
            if bsocket.enabled:
                groups[name]['enabled'] += 1
            groups[name]['bl_idnames'].add(bsocket.bl_idname)
            groups[name]['bsockets'].append(bsocket)

        homonyms = {}
        for name, d in groups.items():
            if d['count'] == 1:
                continue
            if d['enabled'] != 1:
                continue
            if len(d['bl_idnames']) != d['count']:
                continue
            homonyms[name] = {'bsockets': d['bsockets']}
            for bsocket in d['bsockets']:
                if bsocket.enabled:
                    homonyms[name]['enabled'] = bsocket

        # ---------------------------------------------------------------------------
        # Build the socket dict keyed by snake case names
        # ---------------------------------------------------------------------------

        sockets = {}
        names   = {}
        for bsocket in bsockets:

            if bsocket.type == 'CUSTOM':
                continue

            name = utils.get_socket_name(bsocket)
            if not bsocket.enabled:
                if enabled_only:
                    continue
                if name in homonyms:
                    continue

            key = name
            if name in names:
                key = f"{name}_{names[name]}"
                names[name] += 1
            else:
                names[name] = 1

            # free only
            if free_only and not utils.is_free(bsocket):
                continue

            socket_name = utils.get_socket_name(bsocket)
            socket_names = [socket_name, utils.snake_case(socket_name)]

            # include list
            if include is not None:
                keep = False
                for name in include:
                    if name in socket_names:
                        keep = True
                        break
                if not keep:
                    continue

            # exclude list
            keep = True
            for name in exclude:
                if name in socket_names:
                    keep = False
                    break
            if not keep:
                continue

            # We can keep it            
            if is_in:
                sockets[key] = bsocket
            else:
                sockets[key] = utils.to_socket(bsocket)

        return sockets
    
    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its index
    # ----------------------------------------------------------------------------------------------------

    def socket_by_index(self, in_out: IN_OUT, index: int, enabled_only: bool = True, halt: bool = True):
        """ Get a socket by its index

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - index (int) : socket index
        - enabled_only : (bool = True) : ignore disabled sockets
        - halt (bool = True) : raises an error if not found

        Raises
        ------
        - IndexError if index is incorrect

        Returns
        -------
        - Socket
        """
        sockets = self.get_sockets(in_out, enabled_only=enabled_only)
        keys = list(sockets.keys())
        if index < len(list):
            return sockets[keys[index]]
        
        if halt:
            raise IndexError(f"Index error ({index}) for {in_out} socket in Node {self}, sockets are {keys}.")
        
        return None
    
    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its name
    # ----------------------------------------------------------------------------------------------------

    def socket_by_name(self, in_out: IN_OUT, name: str, enabled_only: bool = True, free_only: bool = False, halt: bool = True):
        """ Get a socket by its index

        Get a socket by its name. Valid names are:
        - The socket name possibly suffixed by its rank (e.g. `value_1` for second socket named Value)
        - The python version

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - name (str) : socket name
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
                isocks = self._interface.get_socket_by_python_name(intf_in_out, name, parent=self._tree.get_panel(), return_all=True)

                # Look for the first one matching the conditions
                for isock in isocks:
                    socket = self.socket_by_identifier(isock.identifier)

                    if not free_only:
                        return socket
                    if not utils.is_free(socket):
                        continue

                    return socket
                
            if halt:
                valids = {} if intf_in_out is None else list(self.get_sockets(intf_in_out).keys())
                raise AttributeError(f"Node '{self._bnode.name}' doesn't own a {intf_in_out} socket named '{name}'. Valid names are {valids}.")

            return None

        # ====================================================================================================
        # No tree interface
        # ====================================================================================================

        sockets = self.get_sockets(in_out, enabled_only=enabled_only, free_only=free_only)
        sc_name = utils.snake_case(name)
        for key, socket in sockets.items():
            if key == name or sc_name == utils.snake_case(key):
                return socket
            
        if halt:
            raise AttributeError(f"Node '{self._bnode.name}' doesn't own a {in_out} socket named '{name}'. Valid names are {list(sockets.keys())}")
        
        return None

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by something
    # ----------------------------------------------------------------------------------------------------

    def get_socket(self, in_out: IN_OUT, something, enabled_only: bool = True, free_only: bool = False, halt: bool = True):
        """ Get a socket by a reference

        Arguments
        ---------
        - in_out (str in ('INPUT', 'OUTPUT')) : input or output sockets
        - something (str | int | Socket) : socket index, name, identifier or the socket itself
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
            return self.socket_by_index(in_out, something, enabled_only=enabled_only, halt=halt)
        
        # Let's try the identifier
        socket = self.socket_by_identifier(in_out, something, halt=False)
        if socket is not None:
            return socket
        
        # Utltimately : the socket name
        return self.socket_by_name(in_out, something, enabled_only=enabled_only, free_only=free_only, halt = halt)
    
    # ====================================================================================================
    # Create a new socket from a socket 
    # ====================================================================================================

    def create_from_socket(self, in_out: IN_OUT, socket, name: str = None, panel: str="", **props):
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
            full_name = name if panel == "" else panel + " " + name
            self._items[in_out].new(SocketType(bsocket).items_type, full_name)
            #self._items[in_out].new(utils.get_items_socket_type(bsocket.type), full_name)

            sockets = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
            created = sockets[-2]

        # ---------------------------------------------------------------------------
        # Link and return
        # ---------------------------------------------------------------------------

        if bsocket.is_output:
            self._tree.link(bsocket, created)
        else:
            self._tree.link(created, bsocket)

        return created
    
    # ====================================================================================================
    # Create a new socket
    # ====================================================================================================

    def create_socket(self, in_out: IN_OUT, socket_type: str | SocketType, name: str, panel: str="", **props):
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
        assert socket_type is not None

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
            full_name = name if panel == "" else panel + " " + name
            #self._items[in_out].new(utils.get_items_socket_type(stype), full_name)
            self._items[in_out].new(socket_type.items_type, full_name)
            io_socks = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs

            #socket = io_socks[self._items_offset + len(self._items[in_out]) - 1]
            socket = io_socks[-2]

        return socket
    
    # ====================================================================================================
    # Set an input socket
    # ====================================================================================================

    def set_input_socket(self, name: str | int, value, create: bool = True, panel: str="", **props):
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

        # ===========================================================================
        # Name is None: value must be a socket
        # ===========================================================================

        if name is None:
            bsocket = utils.get_bsocket(value)
            if bsocket is None:
                raise NodeError(f"Error when setting an input socket to node {self}: the value must be a socket when name is none ! {value} is not a Socket.")
            
            # ----- First free input socket

            for socket in self.get_sockets('INPUT', free_only=True).values():

                if socket.type == bsocket.type:
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

        create_socket = create and self._has_dyn_in
        socket = self.get_socket('INPUT', name, free_only=True, halt=not create_socket)

        # ---------------------------------------------------------------------------
        # Create the dynamic socket
        # ---------------------------------------------------------------------------

        if socket is None:

            if isinstance(value, dict):
                raise RuntimeError(f"Impossible to create an input socket in node {self} with forward creation: type is unknown.")

            # The value is a socket, we create from it and link them

            if utils.get_bsocket(value) is not None:
                return self.create_from_socket('INPUT', value, name=name, panel=panel, **props)
            
            # The value is not a socket, we create from its python type

            #if value is None:
            #    socket_type = 'GEOMETRY'
            #else:
            #    socket_type = utils.get_value_socket_type(value)

            socket_type = SocketType(value)
            socket = self.create_socket('INPUT', socket_type, name=name, panel=panel, **props)

        # ===========================================================================
        # Set a value to the socket
        # ===========================================================================

        if value is None:
            return socket

        # ---------------------------------------------------------------------------
        # If the value is a dict, let it make the job
        # Can be used to dynamically create an output socket to be plugged into in_socket
        # ---------------------------------------------------------------------------

        if isinstance(value, dict):
            value['create'](socket, *value.get('args', []))
            return socket

        # ---------------------------------------------------------------------------
        # In socket is multi input and value is a list
        # ---------------------------------------------------------------------------

        if socket.is_multi_input and isinstance(value, list):
            for v in reversed(value):
                self.set_input_socket(socket, v)
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

        #socket_type = socket.type
        socket_type = SocketType(socket)
        if socket.hide_value:
            #self._tree.link(Node.InputNodeSocket(value)._bsocket, socket)
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

            if utils.has_bsocket(a):
                self._tree.link(Node.InputNodeSocket(value)._bsocket, socket)

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

    # ----------------------------------------------------------------------------------------------------
    # Get an attribute : searching into output sockets
    # ----------------------------------------------------------------------------------------------------

    def __getattr__(self, name):

        print(f"Debug Node.__getattr__, getting:", name)
        return self.get_socket('OUTPUT', name)
        #return self.get_output_socket(name)

    def __setattr__(self, name, value):

        #if name in ['_tree', '_bnode', '_label', '_color', 'pin_gizmo'] or name in dir(self):
        #if name.startswith('_') or (name in self.__dict__) or name == 'pin_gizmo':
        if name in Node.__slots__:
            super().__setattr__(name, value)
            return

        self.set_input_socket(name, value)

    # ====================================================================================================
    # Returns the first enabled output socket
    # ====================================================================================================

    @property
    def _out(self):
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
    # Signature
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get the signature
    # ----------------------------------------------------------------------------------------------------

    def get_signature(self, 
            include: list = None, 
            exclude: list = [], 
            enabled_only=False, 
            free_only: bool = False,
            with_sockets: bool = False) -> Signature:
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
            for name, socket in node_sockets.items():

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

    def set_signature(self, in_out: Literal['INPUT', 'OUTPUT', 'BOTH'], signature: Signature, panel: str = ""):
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

            for name, spec in sockets.items():
                socket = sockets.get('socket')

                if socket is None:
                    stype = spec.get('bl_idname', spec.get('socket_type', 'VALUE'))
                    print("CREATION", io, name, stype)
                    created[io][name] = self.create_socket(io, stype, name=name, panel=panel)
                else:
                    created[io][name] = self.create_from_socket(io, socket, name=name, panel=panel)

        return created
    
    # ====================================================================================================
    # Plug the node
    # ====================================================================================================

    def out(self, panel=""):
        """ Plug the output sockets to the current tree output.

        Arguments
        ---------
        - panel (str = "") : panel to use
        """
        for name, socket in self.get_sockets('OUTPUT').items():
            socket.out(name, panel=panel)

    # ====================================================================================================
    # Link input from another node
    # ====================================================================================================

    def link_inputs(self, from_node = None, include: list =  None, exclude = [], panel: str = ""):
        """ Link input socket from another node

        if from_node is None, the current input node is taken.
        Input sockets already linked are ignored

        If from node is able to create output sockets, they are created, otherwise only the sockets
        with matchin names and types are linked.

        Arguments
        ---------
        - from_node (Node) : node to get output sockets from
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - panel (str = "") : panel name to create in from_node
        """

        if from_node is None:
            from_node = self._tree.get_input_node()

        in_sockets = self.get_sockets(
            'INPUT',
            include         = include,
            exclude         = exclude,
            enabled_only    = True,
            free_only       = True,
            )
        
        print("LINK INPUTS", in_sockets)
        
        links = []
        
        for name, in_socket in in_sockets.items():

            print("LINK INPUTS", name, in_socket)

            out_socket = from_node.socket_by_name('OUTPUT', name, enabled_only=True, halt=False)
            if out_socket is None:
                if from_node._has_dyn_out:
                    out_socket = from_node.create_from_socket('OUTPUT', in_socket, panel=panel)
                    links.append((out_socket, in_socket))
            else:
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

        # Nothing for paired input node
        if self._is_paired_input:
            return

        # Becomes the output node
        self._tree._output_stack.append(self)

        # Becomes input node is possible
        if self._has_dyn_out:
            self._tree._input_stack.append(self)

        # Also stacks its pair input node
        if self._is_paired_output:
            
            assert not self._has_dyn_out, f"Shouldn't happen {self}"

            if self._paired_input_node._has_dyn_out:
                self._tree._input_stack.append(self._paired_input_node)

    # ----------------------------------------------------------------------------------------------------
    # Pop capturing sockets in/out
    # ----------------------------------------------------------------------------------------------------

    def _pop(self, error: bool = False):

        # Nothing for paired input node
        if self._is_paired_input:
            return

        assert self._tree._output_stack.pop() == self

        # Becomes input node is possible
        if self._has_dyn_out:
            assert self._tree._input_stack.pop == self

        # Also stacks its pair input node
        if self._is_paired_output:
            
            if self._paired_input_node._has_dyn_out:
                assert self._tree._input_stack.pop() == self._paired_input_node

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

        The clas G provides a functional interface for the node. You simply use the snake case version
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
        sock_names = [utils.snake_case(name) for name in signature.inputs.keys()]

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
        print("DEBUG", self._bnode, self._bnode.color_ramp)
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
    
# ====================================================================================================
# Node Menu
# ====================================================================================================

class MenuNode(Node):
    def __init__(self, 
            named_sockets: dict = {},
            menu = None,
            default_value: str | int = None,
            data_type: str = None,
            **sockets):
        """ > Node <&Node Menu Switch>

        Arguments
        ---------
        - named_sockets (dict = {}) : sockets to create
        - menu (Socket | str = None) : socket to plug in
        - default_value (str | int) : default value
        - data_type (str = None): data type, auto if None
        - sockets (dict) : items
        """

        items = {**named_sockets, **sockets}

        # Not empty list of items
        #if not len(items):
        #    items = {'A': None, 'B': None}

        # Auto data_type
        if data_type is None:
            data_type = utils.get_value_socket_type(list(items.values())[0])

        # Default_value
        index = None
        if default_value is None:
            if len(items):
                index = 0
                default_value = list(items.keys())[0]
        else:
            for i, sdef in enumerate(items.keys()):
                if sdef == default_value:
                    index = i
                    break
        if index is not None:
            default_value = list(items.keys())[index]

        # Super init
        super().__init__('Menu Switch', data_type=data_type)

        # Set the items
        self._bnode.enum_items.clear()
        self._set_items('enum_items', named_sockets=items)

        # Default value
        if default_value is not None:
            self._bnode.inputs[0].default_value = default_value

        # Menu value
        if menu is not None:
            self.menu = menu

    # ====================================================================================================
    # Connect to an input socket
    # ====================================================================================================

    def create_menu_input_socket(self, name="Menu", tip="", panel="", **props):
        """ Create an group input socket and connect it to the Nenu socket.

        Arguments
        ---------
        - name (str = Menu) : group input socket name
        - tip (str = "") : input socket tip
        - panel (str = "") : panel where to create the input socket
        - props (dict) : input socket properties

        Returns
        -------
        - Socket : the created socket
        """

        # Get the default value for the input socket
        default_value = self._bnode.inputs[0].default_value
        index = 1
        for i, sname in enumerate(self._bnode.inputs[1:]):
            if sname == default_value:
                index = 1 + i
                break
        default_value = self._bnode.inputs[index].name

        socket = Tree.current_tree().create_input_from_socket(
            input_socket   = self._bnode.inputs[0],
            name           = name,
            panel          = panel,
            description    = tip,
            **props)
        
        return socket
    
    # ----------------------------------------------------------------------------------------------------
    # Set the menu default value
    # ----------------------------------------------------------------------------------------------------

    def set_default_value(self, name: str):
        """ Set index default value

        Set the default value or the input index socket.
        If the socket is linked to a socket, also set its default value.

        Arguments
        ---------
        - index (str) : default value
        """

        from . import blender

        items = self._bnode.enum_items
        index = None
        names = []
        for i, item in enumerate(items):
            names.append(item.name)
            if item.name == name:
                index = i
                break
        if index is None:
            raise NodeError(f"Menu Switch set_default_value error: item '{name}' not found in {names}.")

        menu_bsocket = self._bnode.inputs[0]
        menu_bsocket.default_value = name

        # Socket linked to the node index
        if menu_bsocket.is_linked:

            # Change linked socket default value
            linked_bsocket = menu_bsocket.links[0].from_socket
            if hasattr(linked_bsocket, 'default_value'):
                linked_bsocket.default_value = name

            # Modifiers value has been reset to None
            ident = linked_bsocket.identifier
            for mod in blender.get_geonodes_modifiers(self._tree._btree):
                if mod.get(ident):
                    mod[ident] = index + 2
    
# ----------------------------------------------------------------------------------------------------
# Index Switch node
# ----------------------------------------------------------------------------------------------------

class IndexSwitchNode(Node):
    def __init__(self, *values, index=None, data_type=None):
        """ > Node <&Node Index Switch>

        ``` python
        with GeoNodes("Index Switch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=Integer(2, 'Index'))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer) : socket 'Index' (Index)

        Returns
        -------
        - Socket
        """

        # Auto data_type
        if data_type is None:
            data_type = utils.get_value_socket_type(values[0])

        # Super init
        super().__init__('Index Switch', data_type=data_type)

        # Create / set the sockets
        enum_items = self._bnode.index_switch_items
        enum_items.clear()
        for i, item in enumerate(list(values)):
            enum_items.new()
            self[1 + i] = item

        # Plug the index
        self.index = index

    # ----------------------------------------------------------------------------------------------------
    # Set the index default value
    # ----------------------------------------------------------------------------------------------------

    def set_default_value(self, index: int = 0):
        """ Set index default value

        Set the default value or the input index socket.
        If the socket is linked to a socket, also set its default value.

        Arguments
        ---------
        - index (int = 0) : default value
        """

        from . import blender

        items = self._bnode.index_switch_items
        index = max(0, min(len(items) - 1, index))

        index_bsocket = self._bnode.inputs[0]
        index_bsocket.default_value = index

        # Socket linked to the node index
        if index_bsocket.is_linked:

            # Change linked socket default value
            linked_bsocket = index_bsocket.links[0].from_socket
            if hasattr(linked_bsocket, 'default_value'):
                linked_bsocket.default_value = index

            # Modifiers value has been reset to None
            ident = linked_bsocket.identifier
            for mod in blender.get_geonodes_modifiers(self._tree._btree):
                if mod.get(ident):
                    mod[ident] = self.current_index + 2

    # ----------------------------------------------------------------------------------------------------
    # Items has been modifier
    # ----------------------------------------------------------------------------------------------------

    def _add_item(self, value, default=False):
        """ Update linked socket max value
        """

        from .sock_integer import Integer

        items = self._bnode.index_switch_items

        index = len(items)
        items.new()

        self[index + 1] = value
        if default or index == 0:
            self.set_default_value(index)

        # ----- Update max value

        index_bsocket = self._bnode.inputs[0]
        if index_bsocket.is_linked:
            linked_bsocket = index_bsocket.links[0].from_socket
            if hasattr(linked_bsocket, 'max_value'):
                linked_bsocket.max_value = index
            isocket = Integer(linked_bsocket)._interface_socket
            if (isocket is not None) and hasattr(isocket, 'max_value'):
                isocket.max_value = index

        return index




