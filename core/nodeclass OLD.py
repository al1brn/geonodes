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
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

import numpy as np
import bpy
from time import time

from . import blender
from .scripterror import NodeError
from . import constants
from . import utils
from .signature import Signature
from .treeclass import Tree
from .treeinterface import TreeInterface

# ====================================================================================================
# Node
# ====================================================================================================

class Node:
    def __init__(self, node_name, sockets={}, link_from=None, **parameters):
        """ Node wrapper.

        The node wrapper exposes input and output sockets and the node parameters.
        At creation time, input sockets are initialized with a dict using their name as key ;
        parameters are initialized as keyword arguments:

        > [!NOTE]
        > The most often, the name of the socket can be used as key in the initialization dict.
        > But in some cases, this doesn't apply:
        > - Several sockets can share the same names (example: 'Math' node has two 'Value' input socket)
        > - Display name is different from the python name (example: 'Math' node, operation 'COMPARE', actual name
        >   of 'Epsilon' socket is 'Value')

        In order to to handle these specific cases, the dict keys can be:
        - The index of the socket in the list
        - The 'identifier' of the socket

        When the sockets are initialized in there order, the values can be passed
        as a list rather than as a dict.

        ``` python
        with GeoNodes("Node initialization"):

            # Dict syntax to create a circle
            node = Node("Mesh Circle", {'Vertices': 32, 'Radius': 1.}, fill_type='NGON')

            # Dict syntax using the socket identifier as key on a node with homonym sockets
            node = Node("Math", {'Value': 2, 'Value_001': 2}, operation='ADD')

            # Dict key words can be socket index
            node = Node("Math", {0: 2, 1: 2}, operation='ADD')

            # A list of values can be used to initialize the sockets in the order they appear
            # Epsilon is initialized to .1
            node = Node("Math", [2., 2., .1], operation='COMPARE')
        ```

        Once initialized, the sockets can be accessed either as list items keyed by the sockets name,
        index or identifier or as node attribute using their snake case name.

        > [!IMPORTANT]
        > Setting and getting a socket:
        > - **Setting** a node socket is interpretated as plugging a value into an **input socket**
        > - **Getting** a node socket is interpretated as getting an **output socket**

        ``` python
        with GeoNodes("Getting and setting node sockets"):

            # Input geometry socket
            geo = Geometry()

            # Create the node
            node = Node("Extrude Mesh")

            # Change the parameter
            node.mode = 'EDGES'

            # Plug 'Geometry' socket with list item syntax
            node["Mesh"] = geo

            # Plug 'Selection' socket with ordered list syntax
            node["Selection"] = Boolean(True)

            # Plug 'Offset Scale' with snake case syntax
            node.offset_scale = 0.5

            # Read the output geometry : snake case syntax
            extruded_geo = node.mesh

            # Read the top selection : list syntax
            top_selection = node["Top"]

            # Read the side selection : index list syntax
            side_selection = node[2]

            # Use the sockets in another node
            top_selection |= side_selection

            # Connect to the group output geometry
            extruded_geo.out()
        ```

        > [!NOTE]
       >  The '_out' property returns the first enabled output socket

        Arguments
        ---------
        - node_name (str) : Node name
        - sockets (dict or list) : initialization values for the node input sockets
        - _items (dict = {}) : dynamic sockets to create
        - link_with (node | dict = None) : node to link into this tree (see <#link_from>)
        - **kwargs : node parameters initialization
        """

        # ----------------------------------------------------------------------------------------------------
        # Create the Node

        self._tree = Tree.current_tree()
        btree = self._tree._btree
        tree_type = btree.bl_idname

        bl_idname = utils.get_node_bl_idname(node_name, tree_type)

        # ----- Node Creation

        self._bnode = btree.nodes.new(type=bl_idname)
        self._bnode.select = False
        self._tree.check_node_validity(self._bnode)

        # ----------------------------------------------------------------------------------------------------
        # Node setup

        # Parameters first to configure the sockets
        self.set_parameters(**parameters)

        # Plug the sockets
        self.set_input_sockets(sockets)

        # ----------------------------------------------------------------------------------------------------
        # Register the node

        self._tree.register_node(self)

        # ----------------------------------------------------------------------------------------------------
        # Plug input node

        if link_from is not None:
            if isinstance(link_from, dict):
                self.link_from(**link_from)
            else:
                self.link_from(link_from, arguments={**sockets, **_items})

        # ----------------------------------------------------------------------------------------------------
        # Particular cases

        if node_name == 'Store Named Attribute':
            if 'Name' in sockets and 'data_type' in parameters:
                if isinstance(sockets['Name'], str):
                    self._tree.register_named_attribute(data_type=parameters['data_type'], attr_name=sockets['Name'])

    def __str__(self):
        return f"<Node '{self._bnode.name}' {self._bnode.bl_idname}>"

    def __repr__(self):
        s = str(self)
        s += "\nInputs\n"
        s += "\n   - ".join([bsock.name for bsock in self._bnode.inputs])
        s += "\nOutputs\n"
        s += "\n   - ".join([bsock.name for bsock in self._bnode.outputs])
        s += "\n"

        return s

    @property
    def _is_group_node(self):
        return self._bnode.bl_idname in ['GeometryNodeGroup', 'ShaderNodeGroup']

    @property
    def _tree_interface(self):
        if self._is_group_node:
            return TreeInterface(self._bnode.node_tree)
        else:
            return None
        
    # ====================================================================================================
    # Dynamic sockets
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Build the node signature
    # ----------------------------------------------------------------------------------------------------
    
    def get_signature(self, 
            include: list = None, 
            exclude: list = [], 
            exclude_linked: bool = False,
            enabled_only=False, 
            with_sockets: bool = False):
        """ Build the closure signature of the node.

        Closure signature is the tuple (input_signature, output_signature)

        Arguments
        ---------
        - include (list = None) : sockets to include
        - exclude (list = []) : sockets to exclude
        - exclude_linked (bool = False) : exclude linked node
        - enabled_only (bool = False) : ignore disabled sockets
        - with_socket (bool = False) : include sockets

        Returns
        -------
        - Signature
        """
        bnode = self._bnode
        return Signature.from_node(bnode, include=include, exclude=exclude, exclude_linked=exclude_linked, enabled_only=enabled_only, with_sockets=with_sockets)
    
    # ----------------------------------------------------------------------------------------------------
    # Set items from dict of {name: value} dict
    # ----------------------------------------------------------------------------------------------------

    def _set_items(self, items_name, named_sockets={}, clear=False, plug_items=True, **sockets):

        # items_name : name of xxx_items to use (auto otherwise)
        # named_sockets : sockets to create
        # clear : clear
        # plug_items : plug the sockets with the values or not
        # kwargs : sockets to create

        # ---------------------------------------------------------------------------
        # Merge the dicts

        #from pprint import pprint
        #print("NAMED")
        #pprint(named_sockets)
        #print("SOCKETS")
        #pprint(sockets)

        all_items = {**named_sockets, **sockets}
        if not len(all_items):
            return

        # ---------------------------------------------------------------------------
        # Node items property

        msg = None
        try:
            node_items = getattr(self._bnode, items_name)
        except Exception as e:
            msg = str(e)

        if msg is not None:
            raise NodeError(f"Error when initializing node '{self._bnode.name}: this node has no items collection named '{items_name}'."
                            " Impossible to create the sockets.",
                named_sockets=named_sockets)

        # ---------------------------------------------------------------------------
        # Clear if required

        if clear:
            node_items.clear()

        # ---------------------------------------------------------------------------
        # Plug / rename the existing sockets

        to_del = []
        for key, value in all_items.items():

            socket = self.by_name('INPUT', key, as_argument=False, halt=False)
            if socket is None:
                socket = self.by_name('INPUT', key, as_argument=True, halt=False)

            if socket is not None:
                if plug_items:
                    self.plug_value_into_socket(value, socket)
                to_del.append(key)

        for key in to_del:
            del all_items[key]

        # ---------------------------------------------------------------------------
        # Loop on the sockets to create

        for socket_name, socket_value in all_items.items():

            # 'new' method takes only one argument
            if self._bnode.bl_idname in ['GeometryNodeMenuSwitch']:
                sck = node_items.new(socket_name)

            # 'new' method takes two arguments
            else:
                input_type = 'GEOMETRY' if socket_value is None else utils.get_value_socket_type(socket_value)
                try:
                    sck = node_items.new(input_type, socket_name)
                except Exception as e:
                    raise NodeError(f"Node {self}, input_type: '{input_type}', socket name: {socket_name}", error=str(e))

            # ----- Plug

            if plug_items:
                self[sck.name] = socket_value

    # ====================================================================================================
    # Create a Socket from an output Blender NodeSocket
    # ====================================================================================================

    @staticmethod
    def data_socket(bsocket):
        socket_type = bsocket.type
        return utils.get_socket_class(bsocket.type, name=bsocket.name)(bsocket)


    # ----------------------------------------------------------------------------------------------------
    # Set the node parameters

    def set_parameters(self, **parameters):

        for param_name, param_value in parameters.items():
            if param_value is None:
                continue

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
    # Accessing the sockets by their name / identifier

    # ----------------------------------------------------------------------------------------------------
    # By identifier

    def by_identifier(self, in_out, identifier, halt=True):
        if in_out == 'INPUT':
            for bsock in self._bnode.inputs:
                if bsock.identifier == identifier:
                    return bsock

        elif in_out == 'OUTPUT':
            for bsock in self._bnode.outputs:
                if bsock.identifier == identifier:
                    return self.data_socket(bsock)

        if halt:
            raise NodeError(f"{in_out} socket with identifier '{identifier}' not found in node '{self._bnode.name}'")

        return None

    # ----------------------------------------------------------------------------------------------------
    # Dictionary socket names -> sockets

    def get_socket_names(self, in_out, enabled_only=True, as_argument=True):
        """ Build a dictionary keyed by the socket unique names

        The possible names are:
        - socket name
        - snake case version of the name

        These names are combined with the panel name:
        - panel name.socket name
        - snake case version of this path

        Once built, the homonyms are made unique by suffixing its order

        Arguments
        ---------
        - in_out : str in ('INPUT', 'OUTPUT')
        - enabled_only : use only enabled sockets

        Returns
        -------
        - dict : socket identifier -> list of possible names
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ----- Via TreeInterface if group node to take panels into account

        if self._is_group_node:
            interface = TreeInterface(self._bnode.node_tree)
            if True:
                signature = interface.get_signature(with_sockets=True)
                i_sockets = signature[in_out]
                res = {}
                for name, info in i_sockets.items():
                    key = utils.snake_case(name) if as_argument else name
                    res[key] = self.by_identifier(in_out, info['socket'].identifier)
                return res

            else:
                i_sockets = interface.get_sockets_names(in_out, python=as_argument)
                return {name: self.by_identifier(in_out, i_socket.identifier) for name, i_socket in i_sockets.items()}

        # ---- Not a group

        names    = []
        bsockets = []

        bsocks = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
        for bsock in bsocks:

            if bsock.type == 'CUSTOM':
               continue

            if enabled_only and not bsock.enabled:
                continue

            label = bsock.name if bsock.label == "" else bsock.label

            names.append(utils.snake_case(label) if as_argument else label)
            bsockets.append(bsock)

        names = utils.ensure_uniques(names, single_digit=True)

        if in_out == 'INPUT':
            return {name: bsocket for name, bsocket in zip(names, bsockets)}
        else:
            return {name: self.data_socket(bsocket) for name, bsocket in zip(names, bsockets)}

    # ----------------------------------------------------------------------------------------------------
    # Valid names

    def valid_names(self, in_out, enabled_only=True, as_argument=True):
        return list(self.get_socket_names(in_out, enabled_only=enabled_only, as_argument=as_argument).keys())

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its index, identifier or name

    def by_name(self, in_out, name, enabled_only=True, as_argument=True, candidates=False, halt=True):
        """ Get a socket by its name

        Arguments
        ---------
        - in_out (str) : str in ('INPUT', 'OUTPUT')
        - name (str) : searched named
        - enabled_only (bool = True) : consider only enabled sockets
        - as_argument (bool = True) : the name is argument or socket name
        - candidates (bool = False) : return all matching names (True) or the first one (False)
        - halt (bool = False) : raises an error if not found

        Returns
        -------
        - Node, Socket or list of sockets depending on the arguments
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ----------------------------------------------------------------------------------------------------
        # If candidates is True, we work with homonyms

        if candidates:
            bsockets = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
            matching = []
            for bsocket in bsockets:
                if not bsocket.enabled and enabled_only:
                    continue
                if bsocket.type == 'CUSTOM':
                    continue

                label = bsocket.name if bsocket.label == "" else bsocket.label

                if as_argument:
                    ok = utils.snake_case(label) == name
                else:
                    ok = label == name

                if ok:
                    if in_out == 'INPUT':
                        matching.append(bsocket)
                    else:
                        matching.append(self.data_socket(bsocket))

            return matching

        # ----------------------------------------------------------------------------------------------------
        # Only one socket wanted

        sockets = self.get_socket_names(in_out, enabled_only=enabled_only, as_argument=as_argument)

        socket = sockets.get(name)

        # ----- Trying with identifier
        if socket is None and not as_argument:
            socket = self.by_identifier(in_out, name, halt=False)

        # ----- Trying with disabled
        if socket is None:
            all_sockets = self.get_socket_names(in_out, enabled_only=False, as_argument=as_argument)
            socket = all_sockets.get(name)

        # ----- Error message
        if socket is None and halt:
            raise NodeError(f"{in_out} socket '{name}' not found in node '{self._bnode.name}'.", valids=list(sockets.keys()))

        # ----- What we have
        return socket

    # ====================================================================================================
    # Set an input socket and get an output socket

    def get(self, name, default=None):
        socket = self.by_name('OUTPUT', name, enabled_only=True, as_argument=False, candidates=False, halt=False)
        if socket is None:
            return self.by_name('OUTPUT', name, enabled_only=True, as_argument=True, candidates=False, halt=False)
        else:
            return socket

    def __getitem__(self, name):
        if isinstance(name, int):
            sockets = self.get_socket_names('OUTPUT')
            key = list(sockets.keys())[name]
            return sockets[key]

        else:
            return self.by_name('OUTPUT', name, as_argument=False)

    def __setitem__(self, name, value):
        if isinstance(name, int):
            sockets = self.get_socket_names('INPUT')
            key = list(sockets.keys())[name]
            self.plug_value_into_socket(value, sockets[key])

        else:
            bsocket = self.by_name('INPUT', name, as_argument=False)
            self.plug_value_into_socket(value, bsocket)

    # ====================================================================================================
    # Read a node attribute : it is an output socket

    def __getattr__(self, name):

        sbnode = type(self)

        if '_bnode' in self.__dict__:

            sbnode = f"'{self._bnode.name}'"

            # ----------------------------------------------------------------------------------------------------
            # The name of an output socket

            out_socket = self.by_name('OUTPUT', name, as_argument=True, halt=False)
            if out_socket is not None:
                return out_socket

            # ----------------------------------------------------------------------------------------------------
            # Peer socket

            if len(name) > 1 and name[-1] == '_' and name[-2] != '_':
                out_socket = self.by_name('OUTPUT', name[:-1], as_argument=True, halt=False)
                #out_socket = self.out_socket(name[:-1], halt=False)
                if out_socket is not None:
                    return out_socket

            # ----------------------------------------------------------------------------------------------------
            # Perhaps a confusion with default output socket

            def_out = self._out
            if def_out is not None and name in dir(def_out):
                node_name = self.__dict__['_bnode'].name
                print(f"CAUTION: the node '{node_name}' has no attribute '{name}', use socket '{utils.snake_case(def_out._bsocket.name)}' or '_out' instead")
                return getattr(def_out, name)

            # ----------------------------------------------------------------------------------------------------
            # No more hope: let's raise the error

            _ = self.by_name('OUTPUT', name, as_argument=True, halt=True)


        #raise AttributeError(f"Node parameter '{name}' not found.")
        raise NodeError(f"Attribute '{name}' of node '{sbnode}' is not found.", keyword=name)

    def __setattr__(self, name, value):

        #print("SET ATTR", name)

        if name in ['_tree', '_bnode', '_label', '_color', 'pin_gizmo'] or name in dir(self):
            super().__setattr__(name, value)
            return

        sbnode = ''
        if '_bnode' in self.__dict__:

            # ----- Set parameter

            bnode = self.__dict__['_bnode']
            sbnode = bnode.name
            if name not in ['color', 'label', 'width', 'height', 'dimensions', 'location', 'type'] and hasattr(bnode, name):
                if value is None:
                    NodeError(f"Collision between Custom socket name and node parameter '{name}'")

                setattr(bnode, name, value)
                return

            # ---- Link input node

            bsocket = self.by_name('INPUT', name, enabled_only=True, as_argument=True, halt=False)
            if bsocket is not None:
                self.plug_value_into_socket(value, bsocket)
                return

        #raise AttributeError(f"Node parameter '{name}' not found in '{sbnode}'.")
        raise NodeError(f"Node parameter or input socket '{name}' not found in '{sbnode}'.", keyword=name)

    # ----------------------------------------------------------------------------------------------------
    # Set the node sockets

    def set_input_sockets(self, sockets={}):

        # ----- Sockets is a list : very simple

        if isinstance(sockets, list):
            for index, value in enumerate(sockets):
                self.plug_value_into_socket(value, self._bnode.inputs[index])
            return

        # ----- Sockets is a dict

        for socket_name, socket_value in sockets.items():

            if socket_value is None:
                continue

            self[socket_name] = socket_value

    # =============================================================================================================================
    # List of socket identifiers from names

    def identified_bsockets(self, in_out, names=None):
        """ Returns a list of socket identifiers from names

        Names can be a list of socket names, arguments or identifiers
        if names is None, returns all the sockets

        It can also contain panel name. In that case, it includes all the socket
        within the panel.

        Arguments
        ---------
        - in_out (str) : str in ('INPUT', 'OUTPUT')
        - names (list of strs) : the names to convert
        """
        assert(in_out in ('INPUT', 'OUTPUT'))

        # ---------------------------------------------------------------------------
        # The list of enabled sockets

        bsockets = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
        sockets_dict = {}
        for bsocket in bsockets:
            if not bsocket.enabled or bsocket.type == 'CUSTOM':
                continue
            sockets_dict[bsocket.identifier] = bsocket

        if names is None:
            return sockets_dict

        if isinstance(names, str):
            names = [names]

        result = {}

        # ---------------------------------------------------------------------------
        # If the node is a Group, we use interface

        interface = self._tree_interface
        if interface is not None:

            py_names = [interface.user_name_to_python(name) for name in names]
            unique_names = interface.get_sockets_names(in_out, python=True)

            for py_name in py_names:
                i_socket = unique_names.get(py_name)
                if i_socket is not None:
                    result[i_socket.identifier] = bsockets[identifier]

            for identifier in bsockets.keys():
                if identifier in names:
                    result[identifier] = bsockets[identifier]

            return result

        # ---------------------------------------------------------------------------
        # The node is not a group
        # Names can contain identifier, name or argument
        # We build a dictionary:
        # identifier -> list of possible names

        # Initialize with identifier
        all_names = {}
        for identifier in sockets_dict.keys():
            all_names[identifier] = [identifier]

        # Complete with unique arg names
        sockets = self.get_socket_names(in_out, enabled_only=True, as_argument=True)
        for name, bsocket in sockets.items():
            if bsocket.identifier in all_names:
                all_names[bsocket.identifier].append(name)

        # Complete with unique socket names
        sockets = self.get_socket_names(in_out, enabled_only=True, as_argument=False)
        for name, bsocket in sockets.items():
            if bsocket.identifier in all_names:
                all_names[bsocket.identifier].append(name)

        # ----------------------------------------------------------------------------------------------------
        # Let's pick the requested names

        identifiers = {}
        for name in  names:
            identifier = None
            for id, names in all_names.items():
                if name in names:
                    identifier = id
                    break

            if identifier is None:
                raise NodeError(f"Node.identified_bsockets: '{name}' is not a {in_out} socket of node '{self._bnode.name}'",
                    valids=self.valid_names(in_out, as_argument=False))

            identifiers[identifier] = sockets_dict[identifier]

        return identifiers


    # =============================================================================================================================
    # Returns the first enabled output socket

    @property
    def _out(self):
        """ Returns the first enabled output socket.

        Returns
        -------
        - Socket : first enabled output socket
        """
        for bsock in self._bnode.outputs:
            if bsock.enabled and bsock.type != 'CUSTOM':
                return self.data_socket(bsock)
        return None

    # ====================================================================================================
    # Plug the output nodes

    def out(self, panel=""):
        for bsock in self._bnode.outputs:
            if bsock.enabled and bsock.type != 'CUSTOM':
                label = bsock.name if bsock.label == "" else bsock.label
                self.data_socket(bsock).out(label, panel=panel)
        return None


    # =============================================================================================================================
    # Create a node from a value with an output socket matching the target
    # Returns its output socket
    #
    # - int    -> Integer
    # - float  -> Value
    # - bool   -> Boolean
    # - str    -> String
    # - (3,)   -> Vector
    # - (4,)   -> Color
    # - (16,)  -> Matrix

    @staticmethod
    def InputNodeSocket(value):

        # ----- Nothing to return
        if value is None:
            return None

        # ----- It is already a bsocket
        bsocket = utils.get_bsocket(value)
        if bsocket is not None:
            return value

        # ----- Simple types

        # bool : before int because isinstance(True, int) == True
        if isinstance(value, bool):
            return Node('Boolean', boolean=value)._out

        elif isinstance(value, int):
            return Node('Integer', integer=value)._out

        elif isinstance(value, float):
            socket = Node('Value')._out
            socket._bsocket.default_value = value
            return socket

        elif isinstance(value, str):
            return Node('String', string=value)._out

        if not hasattr(value, '__len__'):
            raise NodeError(f"Impossible to create an input Node from the python value {value}")

        a = np.reshape(np.array(value, object), np.size(value))
        sockets = {i: a[i] for i in range(len(a))}

        if len(a) == 3:
            if utils.has_bsocket(value):
                return Node('Combine XYZ', sockets)._out
            else:
                return Node('Vector', vector=tuple(a))._out

        elif len(a) == 4:
            if utils.has_bsocket(value):
                return Node('Combine Color', sockets, sockets)._out
            else:
                return Node('Color', value=a)._out

        elif len(a) == 16:
            return Node('Combine Matrix', sockets)._out

        else:
            raise NodeError(f"Impossible to create an input Node from the array of shape {np.shape(value)}.", value=value)

    # =============================================================================================================================
    # Get an acceptable thing to set to an input socket
    # - If the value is a socket -> Nothing to do
    # - If the value is a python value:
    #   - If the input socket hides the value -> must be converted to an input node
    #   - Or is used to set the default_value to the input socket
    # - The value can be a dict with a function to do the job

    def plug_value_into_socket(self, value, in_socket):

        if value is None:
            return
        
        # ----------------------------------------------------------------------------------------------------
        # in_socket is defined by its name or index

        if isinstance(in_socket, (str, int)):
            in_socket = self.by_name('INPUT', in_socket)

        # ----------------------------------------------------------------------------------------------------
        # If the value is a dict, let it make the job
        # Can be used to dynamically create an output socket to be plugged into in_socket

        if isinstance(value, dict):
            value['create'](in_socket, *value.get('args', []))
            return

        # ----------------------------------------------------------------------------------------------------
        # In socket is multi input and value is a list

        if in_socket.is_multi_input and isinstance(value, list):
            for v in reversed(value):
                self.plug_value_into_socket(v, in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # If the value is a Node, we take its default output socket

        if '_bnode' in dir(value):
            value = value._out

        # ----------------------------------------------------------------------------------------------------
        # If the value is a domain, we take its geometry

        #if hasattr(value, '_geo'):
        if '_geo' in dir(value):
            value = value._geo

        # ----------------------------------------------------------------------------------------------------
        # We directly have a socket

        out_socket = utils.get_bsocket(value)
        if out_socket is not None:
            link = self._tree.link(out_socket, in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # We need to create a node if:
        # - in_socket.hide_value is True
        # - the value is an array containing sockets : vector((0, a, 1))

        socket_type = in_socket.type
        if in_socket.hide_value:
            self._tree.link(Node.InputNodeSocket(value)._bsocket, in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # We can use default value

        if socket_type in constants.ARRAY_TYPES:
            if socket_type == 'RGBA':
                a = utils.value_to_color(value)

            else:
                spec = constants.ARRAY_TYPES[socket_type]
                a = utils.value_to_array(value, spec['shape'])

            if utils.has_bsocket(a):
                self._tree.link(Node.InputNodeSocket(value)._bsocket, in_socket)
            else:
                try:
                    in_socket.default_value = list(a)

                except Exception as e:
                    raise NodeError(f"Impossible to use the value <{value}> (type: {type(value).__name__}) as default value for socket [{in_socket.node.name}]{in_socket.name}.",
                        node = in_socket.node.name,
                        in_socket= in_socket.name,
                        in_socket_type = in_socket.type,
                        value = value,
                        value_data_type = utils.get_value_socket_type(value),
                        array = a,
                        original_error = str(e),
                        )

        elif socket_type in ['BOOLEAN', 'INT', 'VALUE', 'STRING', 'FLOAT']:
            try:
                in_socket.default_value = value
            except TypeError as e:
                raise NodeError(f"Impossible to use the value [{value}] as default value for socket [{in_socket.node.name}]{in_socket.name}.",
                    node            = in_socket.node.name,
                    in_socket       = in_socket.name,
                    in_socket_type  = in_socket.type,
                    value           = value,
                    value_data_type = utils.get_value_socket_type(value),
                    original_error  = str(e),
                    )

        elif in_socket.type in ['OBJECT', 'COLLECTION', 'IMAGE', 'MATERIAL']:
            bobj = utils.get_blender_resource(in_socket.type, value)

            if bobj is not None:
                in_socket.default_value = bobj

        elif in_socket.type == 'MENU':
            if isinstance(value, str):
                in_socket.default_value = str(value)

            elif isinstance(value, (tuple, list)):
                name = value[0]
                panel = value[1] if len(value) == 2 else ""
                self.link_from(node='TREE', include=[name], create=True, panel=panel)
                #self._tree.link_nodes(self._tree.input_node, self, include=name, create=True, panel=panel)

            else:
                raise NodeError(f"Impossible to set the menu socket '{in_socket.name}' with value {value}.",
                    valid="Valid values are str with a valid menu item or a tuple or str with group input name and panel",
                    example="menu_name=('Name', 'Panel')")

        else:
            raise NodeError(f"Impossible to set the socket '{in_socket.name}' of type '{socket_type}' with value {value}.")

    # =============================================================================================================================
    # Plug selection socket

    def plug_selection(self, selection):
        if selection is None:
            return
        for bsocket in self._bnode.inputs:
            if bsocket.name == 'Selection':
                self.plug_value_into_socket(selection, bsocket)
                return

    # =============================================================================================================================
    # Link from
    # Plug another node into self
    # If the other node is None, the Tree input node is taken
    # Create is only valid in this case

    def link_from(self,
            node:      'Node | Tree | None | str' = 'TREE',
            include:   list[str] | str | None = None,
            exclude:   list[str] | str = [],
            arguments: dict['name': 'value'] = {},
            create:    bool = True,
            panel:     str = ""):
        """ Plug the output sockets of a node into the input sockets of the node.

        This method is used to connect several sockets in a compact syntax.

        If the node argument is None, the sockets are created in the Group Input node.
        Use 'include', 'exclude' and 'rename' arguments to control the connexions.

        > [!NOTE]
        > This function is called when initializing a node if the `link_from` argument is not None.
        > In that case, `link_argument` value is either the `node` argument or a dictionnary
        > of the `link_from` method arguments:

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
        - node : the node to get the outputs from. Use Group Input node if None
        - include : connects only the sockets in the list
        - exclude : exclude sockets in this list
        - arguments : arguments used at initialization time. Arguments which are defined in the list are ignored
        - create : create the output sockets in node if it is a 'Group Input Node'
        - panel : panel name to create, use tree default name if None

        Returns
        -------
        - Node : self
        """

        tree = self._tree

        # ----------------------------------------------------------------------------------------------------
        # Node with output sockets to plug

        if node is None:
            return self

        if (node == tree) or (str(node).upper() == 'TREE'):
            node = tree.input_node

        if isinstance(exclude, str):
            exclude = [exclude]
        else:
            exclude = list(exclude)

        for arg, value in arguments.items():
            if value is not None:
                exclude.append(arg)

        tree.link_nodes(from_node=node, to_node=self, include=include, exclude=exclude, create=create, panel=panel)

        return self


    # =============================================================================================================================
    # Color and label

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

    # =============================================================================================================================
    # Pin gizmo
    # The first input socket

    @property
    def pin_gizmo(self):
        return self._bnode.inputs[0].pin_gizmo

    @pin_gizmo.setter
    def pin_gizmo(self, value):
        self._bnode.inputs[0].pin_gizmo = value

# ====================================================================================================
# Group
# ====================================================================================================

class Group(Node):

    def __init__(self, group_name, sockets={}, link_from=None, **kwargs):
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
        - sockets (dict) : sockets initialization values
        - **kwargs (dict) : sockets  initialization with their snake_case name

        Returns
        -------
        - Node Group
        """

        tree = Tree.current_tree()

        # ----------------------------------------------------------------------------------------------------
        # Get the node group
        # ----------------------------------------------------------------------------------------------------

        spec = utils.get_available_groups(tree._btree.bl_idname).get(group_name, {})
        group_tree = blender.load_node_group(spec)
        if group_tree is None:
            raise NodeError(f"Impossible to find the group named '{group_name}'")

        # ----- Create the node group

        super().__init__('Group', sockets=sockets, node_tree=group_tree)

        for k, v in kwargs.items():
            setattr(self, k, v)

        # ----------------------------------------------------------------------------------------------------
        # Plug input node

        if link_from is not None:
            if isinstance(link_from, dict):
                self.link_from(**link_from)
            else:
                self.link_from(link_from, arguments={**sockets, **kwargs})

    @classmethod
    def Prefix(cls, prefix, group_name, sockets={}, **kwargs):
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
        return cls(f"{prefix} {group_name}", sockets=sockets, **kwargs)

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
# Specific nodes
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Color Ramp
# ----------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------
# Node Curves
# ----------------------------------------------------------------------------------------------------

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
    
# ----------------------------------------------------------------------------------------------------
# Node Menu
# ----------------------------------------------------------------------------------------------------

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




