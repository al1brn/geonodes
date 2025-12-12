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

module : socket_class
---------------------
- Socket

This class is the base class for all data socket actually used in ***geonodes***.

The primary purpose of a socket is to maintain a reference to the output socket of
a node.

It implements fundamental mechanisms such as:
- caching nodes
- jump
- access to node
- node label and color
- access to interface tree for input socket

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

import bpy
import numpy as np

from .scripterror import NodeError
from .import utils
from .import blender
from . import constants
from .utils import Break
from .treeinterface import ItemPath
from .sockettype import SocketType
from .treeinterface import TreeInterface
from .treeclass import Tree
from .nodeclass import Node, Group, MenuNode
from .nodezone import ZoneNode,ZoneIterator

# =============================================================================================================================
# =============================================================================================================================
# Node cache interface
# =============================================================================================================================
# =============================================================================================================================

class NodeCache:

    __slots__ = ('_cached_nodes',)

    # ====================================================================================================
    # Cache mechanism
    # Nodes can be directly created or created through a cache mechanism
    # - node = Node(...)
    # - node = self._cache(...)
    # The cache is erased with _reset
    # The cache is optionnally erased when a jump occurs
    # It is up to the true class to call _cache_reset

    def _cache_reset(self):
        self._cached_nodes = {}

    def _cache(self, name, sockets={}, cache_name=None, **parameters):

        # build a node if not in cache

        if cache_name is None:
            cache_name = name

        # ----- Is the node already in cache
        node = self._cached_nodes.get(cache_name)
        if node is not None:
            return node

        # ----- No : we create it and put is in cache
        node = Node(name, sockets, **parameters)
        self._cached_nodes[cache_name] = node

        return node

# =============================================================================================================================
# =============================================================================================================================
# Data Socket root
# =============================================================================================================================
# =============================================================================================================================

class Socket(NodeCache):

    __slots__ = NodeCache.__slots__ + ('_tree', '_bsocket', '_layout', '_use_layout')

    SOCKET_TYPE = None

    # ====================================================================================================
    # Initialization
    # ====================================================================================================

    def __init__(self, 
            socket  = None, 
            name    : str = None, 
            tip     : str = '',
            panel   : str = "",                 
            **props):
        """ > The output socket of a <!Node>

        **Socket** is the base class for data classes such as <!Float>, <!Image> or <!Geometry>.

        It refers to an **output** socket of a <!Node>. A socket can be set to the **input** socket
        of another <!Node> to create a link between the two nodes:

        ``` python
        # cube is the output socket 'Mesh' of the node 'Cube'
        cube = Node("Cube").mesh

        # cube is set the to socket 'geometry' of node 'Set Position'
        node = Node("Set Position")
        node.geometry = cube
        ```

        > [!IMPORTANT]
        > You can access to the other output sockets of the node in two different ways:
        > - using <#node> attribute
        > - using ***peer socket** naming convention where the **snake_case** name of
        >.  the other sockets is suffixed by '_'

        The example below shows how to access the to 'UV Map' socket of node <*Node Cube>:

        ``` python
        # cube is the output socket 'Mesh' of the node 'Cube'
        cube = Mesh.Cube()

        # Getting 'UV Map' through the node
        uv_map = cube.node.uv_map

        # Or using the 'peer socket' naming convention
        uv_map = cuve.uv_map_
        ```

        Arguments
        ---------
        - socket (NodeSocket) : the output socket to wrap
        """

        # ---------------------------------------------------------------------------
        # Attributes
        # ---------------------------------------------------------------------------

        self._layout      = None
        self._use_layout  = True
        self._tree = Tree.current_tree()
        self._bsocket = None
        self._reset()

        # ---------------------------------------------------------------------------
        # Empty socket
        # ---------------------------------------------------------------------------

        if utils.request_empty(socket):
            return
        
        # ---------------------------------------------------------------------------
        # Named attribute
        # But Color because string can be the initial value of a color
        # ---------------------------------------------------------------------------

        socktype = self._socket_type
        cname = socktype.class_name

        if isinstance(socket, str) and (cname in constants.ATTRIBUTE_CLASSES) and (cname != 'Color'):
            self._bsocket = self.Named(socket)._bsocket
            return
        
        # ---------------------------------------------------------------------------
        # Let's get the socket
        # ---------------------------------------------------------------------------

        self._bsocket = utils.get_bsocket(socket)
        if self._bsocket is not None:
            return
        
        # ---------------------------------------------------------------------------
        # No name: we create from a constant Node
        # The socket argument is the value to set
        # ---------------------------------------------------------------------------

        if name is None:
            if socktype == 'GEOMETRY':
                new_socket = self.Input(None, halt=False)
                if new_socket is None:
                    new_socket = self.NewInput("Geometry")
                self._bsocket = new_socket._bsocket
                
            else:
                self._bsocket = self.Constant(socket)._bsocket

        # ---------------------------------------------------------------------------
        # With a name, we request the creation from current input
        # ---------------------------------------------------------------------------

        else:
            # Socket can be the default value
            if socket is not None:

                if 'default' not in constants.SOCKETS[self._socket_type.type]['props']:
                    raise NodeError(f"The {self._socket_type()} socket doesn't accept default value. <{socket}> is not valid.")
                
                # Perhaps it is given in the props
                def_key = 'default' if 'default' in props else None
                if def_key is None:
                    def_key = 'default_value' if 'default_value' in props else None

                if def_key is None:
                    props = {'default_value': socket, **props}

            new_socket = self.NewInput(name, tip=tip, panel=panel, **props)
            self._bsocket = new_socket._bsocket
            self._use_layout = new_socket._use_layout


    # ====================================================================================================
    # Constructors
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # An empty socket
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Empty(cls, value = None):
        """ Create an empty socket.
        
        An empty socket is used temporarily as an input for nodes with dynamic sockets:

        ``` python
            # 10 iterations starting from an empty geometry
            for rep in Geometry.Repeat(10):
                pass
            result = rep.geometry
        ```

        Arguments
        ---------
        - value (Any = None) : default value
        """
        socket = cls(constants.EMPTY_SOCKET)
        socket._bsocket = SocketType(cls.SOCKET_TYPE).get_default_from_value(value)
        return socket
    
    # ----------------------------------------------------------------------------------------------------
    # Named attribute
    # ----------------------------------------------------------------------------------------------------
    
    @classmethod
    def Named(cls, name):
        """ > Node <&Node Named Attribute>

        Information
        -----------
        - Parameter 'data_type' : 'BOOLEAN'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        if SocketType(cls.SOCKET_TYPE).class_name not in constants.ATTRIBUTE_CLASSES:
            raise NodeError(
                f"The class {SocketType(cls.SOCKET_TYPE).class_name} is not an attribute.\n"
                f"Attribute classes are: {constants.ATTRIBUTE_CLASSES}")
        
        node = Node('Named Attribute', name=name)
        data_type = SocketType(cls.SOCKET_TYPE).get_node_data_type(
            tree_type = node._tree._._btree.bl_idname,
            bl_idname = node._bnode.bl_idname,
            halt = True)

        node._data_type = data_type

        return node._out
    
    # ----------------------------------------------------------------------------------------------------
    # An existing group input socket (output socket of input node)
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Input(cls, name: str, panel: str = "", halt: bool = True):
        """ Get an exist input socket from its name and panel.

        > [!NOTE]
        > The "input" socket here is an "output" socket of the current input node

        To create a input socket use NewInput.

        If the 'name' argument is None, the first socket of the proper type is returned.

        Raises
        ------
        - NodeError if socket is not found and halt is requested

        Arguments
        ---------
        - name (str | None) : socket name
        - panel (str = "") : panel name
        - halt (bool = True) : raises an error if not found

        Returns
        -------
        - Socket
        """
        in_node = Tree.current_tree().get_input_node()

        include = None if name is None else [name]
        bsockets = in_node.get_sockets('OUTPUT', include=include, panel=panel)

        for _, bsock in bsockets:
            if SocketType(bsock).type == cls.SOCKET_TYPE:
                return cls(bsock._bsocket)
        
        if halt:
            sname = "" if name is None else f" named '{name}'"
            raise NodeError(
                f"There is no {SocketType(cls.SOCKET_TYPE).class_name} input socket{sname}.\n"
                f"Available sockets are : {[bsock[0] for bsock in in_node.get_sockets()]}.")
        
        return None
    
        #full_name = ItemPath(panel) + ItemPath(name)
        #return cls(Tree.current_tree().get_input_node().socket_by_name('OUTPUT', full_name.path, None))

    # ----------------------------------------------------------------------------------------------------
    # Create a new input socket from the current I/O contexte
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def NewInput(cls, name: str, tip: str = "", panel: str = "", **props):
        """ Create an new input socket

        > [!NOTE]
        > The "input" socket here is an "output" socket of the current input node

        To get an existing input socket use Input.

        Raises
        ------
        - NodeError if socket is not found

        Arguments
        ---------
        - name : socket name
        - panel : panel name

        Returns
        -------
        - Socket
        """
        value = props.get('default', props.get('default_value'))
        if value is None:
            return cls._create_input_socket(name = name, tip = tip, panel = panel, **props)
        else:
            value = SocketType(cls.SOCKET_TYPE).get_default_from_value(value)
            return cls._create_input_socket(value = value, name = name, tip = tip, panel = panel, **props)
        
    # ----------------------------------------------------------------------------------------------------
    # Create a socket from a constant Node
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Constant(cls, value: None):
        """ Create an input socket from a constant Node.
        """

        # ---------------------------------------------------------------------------
        # Ensure array
        # ---------------------------------------------------------------------------

        def get_shaped(v, *shapes):
            r = np.ravel(v)
            shape = np.shape(r)
            if shape in shapes:
                return tuple(r)
            
            if shape == (1,):
                return tuple(np.resize(r, shapes[0]))
            
            raise NodeError(
                f"The value <{v}> can't be transformed in a valid initial value for {SocketType(cls.SOCKET_TYPE).class_name}."
            )
        
        # ---------------------------------------------------------------------------
        # Does the array contain sockets
        # ---------------------------------------------------------------------------

        def has_sockets(a):
            for v in a:
                if SocketType.get_bsocket(v) is not None:
                    return True
            return False
        
        # ---------------------------------------------------------------------------
        # Default value
        # ---------------------------------------------------------------------------

        socket_type = SocketType(cls.SOCKET_TYPE)
        if cls.SOCKET_TYPE not in ['RGBA', 'VECTOR', 'ROTATION', 'MATRIX']:
            def_val = socket_type.get_default_from_value(value)

        # ---------------------------------------------------------------------------
        # Depending on the socket type
        # ---------------------------------------------------------------------------

        if cls.SOCKET_TYPE == 'BOOLEAN':
            return Node('Boolean', boolean=def_val)._out

        elif cls.SOCKET_TYPE == 'BUNDLE':
            return Node("Combine Bundle")._out
        
        elif cls.SOCKET_TYPE == 'CLOSURE':
            socket = ZoneNode("Closure", None).closure
            socket._use_layout = False
            return socket

        elif cls.SOCKET_TYPE == 'COLLECTION':
            return Node('Collection', collection=def_val)._out
        
        elif cls.SOCKET_TYPE == 'RGBA':

            if value is None:
                a = (0, 0, 0, 1)
            else:
                a = get_shaped(value, (4,), (3,))

            if has_sockets:
                if Tree.is_geonodes():
                    node = Node('Combine Color', {0: a[0], 1: a[1], 2:a[2]})
                    if len(a) == 4:
                        node.alpha = a[3]
                    return node._out
                else:
                    return Node('Combine Color', {0: a[0], 1: a[1], 2:a[2]})._out

            else:
                def_val = SocketType('COLOR').get_default_from_value(a)
                if Tree.is_geonodes(col):
                    return Node('Color', value=def_val)._out

                else:
                    socket = Node('Color')._out
                    socket._bsocket.default_value = def_val
                    return socket

        elif cls.SOCKET_TYPE == 'IMAGE':
            return Node('Image', image=def_val)._out
        
        elif cls.SOCKET_TYPE == 'INT':
            return Node('Integer', integer=def_val)._out
        
        elif cls.SOCKET_TYPE == 'MATERIAL':
            return Node('Material', material=def_val)._out
        
        elif cls.SOCKET_TYPE == 'MATRIX':

            if value is None:
                a = (1, 0, 0, 0,   0, 1, 0, 0,   0, 0, 1, 0,   0, 0, 0, 1)
            else:
                a = get_shaped(value, (16,))

            return Node('Combine Matrix', named_sockets = {i: a[i] for i in range(16)})._out
        
        elif cls.SOCKET_TYPE == 'MENU':
            return Node('Menu Switch')._out
        
        elif cls.SOCKET_TYPE == 'OBJECT':
            return Node('Integer', object=def_val)._out
        
        elif cls.SOCKET_TYPE == 'ROTATION':

            if value is None:
                a = (0, 0, 0)
            else:
                a = get_shaped(value, (3,))

            if has_sockets(a):
                return Node('Combine XYZ', x=a[0], y=a[1], z=a[2])._out.to_rotation()
            else:
                return Node('Rotation', rotation_euler=a)._out
        
        elif cls.SOCKET_TYPE == 'STRING':
            return Node('String', string=def_val)._out
        
        elif cls.SOCKET_TYPE == 'VALUE':
            node = Node('Value')
            node._bnode.outputs[0].default_value = def_val
            return node._out
        
        elif cls.SOCKET_TYPE == 'VECTOR':

            if value is None:
                a = (0, 0, 0)
            else:
                a = get_shaped(value, (3,))

            if has_sockets(a):
                return Node('Combine XYZ', x=a[0], y=a[1], z=a[2])._out
            else:
                return Node('Vector', vector=a)._out
            
        elif cls.SOCKET_TYPE == 'GEOMETRY':
            raise NodeError(f"There is no node to create a Geometry. Use explicit constructors such as 'Mesh.Cube()', 'Curve.Spiral()' or 'Cloud.Points().")
            
        else:
            assert False, f"Shouldn't happen {socket_type}"

    # ====================================================================================================
    # Emptyness
    # ====================================================================================================

    def _is_empty(self, halt_message: str = None):
        if isinstance(self._bsocket, bpy.types.NodeSocket):
            return False
        
        if halt_message is None:
            return True
        else:
            raise NodeError(f"Empty socket error:\n{halt_message}")
        
    # ====================================================================================================
    # Utilities
    # ====================================================================================================

    @property
    def _socket_type(self):
        return SocketType(self.SOCKET_TYPE)

    def __str__(self):
        if self._is_empty():
            return f"<{self._socket_type.class_name}: Empty>"
        else:
            return f"<{self._socket_type.class_name}: [{self.node._bnode.name}].'{self._bsocket.name}'>"
    
    def _reset(self):
        self._cache_reset()

    # ----------------------------------------------------------------------------------------------------
    # Jump to another output socket
    # ----------------------------------------------------------------------------------------------------

    def _jump(self, socket, reset=True):

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Socket error: Impossible to jump to socket {socket}")
        
        self._bsocket = bsocket
        if reset:
            self._reset()

        return self
    
    # ----------------------------------------------------------------------------------------------------
    # Geometry from domain
    # ----------------------------------------------------------------------------------------------------

    @property
    def _domain_to_geometry(self):
        return self

    # ----------------------------------------------------------------------------------------------------
    # Get the interface socket (for Group node or tree input / output)
    # ----------------------------------------------------------------------------------------------------

    @property
    def _interface_socket(self):
        """ Return the interface socket if exists

        An interface socket exists when the socket a tree input or output socket or
        when it is the socket of a group

        Returns
        -------
        - Interface Socket
        """
        if self.node.use_interface:
            return self.node._interface._use_interface(self._bsocket.identifier)
        
        return None

    # ----------------------------------------------------------------------------------------------------
    # Name or label
    # ----------------------------------------------------------------------------------------------------

    @property
    def node(self):

        self._is_empty(f"There is not Node")

        # Not yet initialized
        if not hasattr(self, '_bsocket'):
            return None
        
        for node in self._tree._nodes:
            if node._bnode == self._bsocket.node:
                return node
            
        assert False, f"Shouldn't happen, {self._bsocket=}, {self._bsocket.node=}"

    # ----------------------------------------------------------------------------------------------------
    # Name or label
    # ----------------------------------------------------------------------------------------------------

    @property
    def _name(self):
        """ Return the name or the label

        Returns
        -------
        - str : default is ""
        """
        if self._is_empty():
            return "<EMPTY SOCKET>"
        return utils.get_socket_name(self._bsocket)

    # ----------------------------------------------------------------------------------------------------
    # Get the panel name
    # ----------------------------------------------------------------------------------------------------

    @property
    def _panel_name(self):
        """ Return the name of the panel

        Returns
        -------
        - str : default is ""
        """
        i_socket = self._interface_socket
        if i_socket is None:
            return ""
        
        names = []
        cur = i_socket
        while True:
            if cur.parent.name == "":
                break
            names.append(cur.parent.name)
            cur = cur.parent

        return " > ".join(reversed(names))

    # ====================================================================================================
    # Default value property
    # ====================================================================================================

    @property
    def default_value(self):
        if not hasattr(self._bsocket, 'default_value'):
            raise NodeError(f"Socket {self} has not default value.")
        
        return self._bsocket.default_value
    
    @default_value.setter
    def default_value(self, value):
        if not hasattr(self._bsocket, 'default_value'):
            raise NodeError(f"Socket {self} has not default value.")
        
        self._bsocket.default_value = value

        # ----- Interface
        i_socket = self._interface_socket
        if i_socket is not None:
            i_socket.default_value = value

    # ====================================================================================================
    # Getting the socket from nodes
    # ====================================================================================================


    
    # ----------------------------------------------------------------------------------------------------
    # Get an existing socket from current input node
    # Contrarilty to Input, doesn't raise an error
    # ----------------------------------------------------------------------------------------------------
        
    def _get_bsocket_from_input(self, name: str = None) -> bpy.types.NodeSocket:
        """ Get the availble input socket if any.

        The socket is get a an OUTPUT socket of the current input.

        Arguments
        ---------
        - name (str = None) : name filter

        Returns
        -------
        - Socket : or None if not found
        """
        in_node = self._tree.get_input_node()

        include = None if name is None else [name]

        bsockets = in_node.get_sockets('OUTPUT', include=include)
        for _, bsock in bsockets:
            if SocketType(bsock).type == self.SOCKET_TYPE:
                return bsock._bsocket
        else:
            return None
        

    # ====================================================================================================
    # Grid
    # ====================================================================================================

    @property
    def is_grid(self):
        """ bool property
        
        Returns True if socket is a grid (inferred_structure_type == 'GRID').
        """
        if self._is_empty():
            return False
        return self._bsocket.inferred_structure_type == 'GRID'

    # ====================================================================================================
    # Owning node
    # ====================================================================================================

    @property
    def node_color(self):
        """ Node color

        Returns
        -------
        - mathutils.Color
        """
        return self.node._color

    @node_color.setter
    def node_color(self, value):
        self.node._color = value

    @property
    def node_label(self):
        """ Node Label

        Returns
        -------
        - str
        """
        return self.node._label

    @node_label.setter
    def node_label(self, value):
        self.node._label = value

    # To chain in a short way
    def _lc(self, label=None, color=None):
        """ Set node label and color.

        This method returns self to be chained to as socket:

        ``` python
        with GeoNodes("Node label and color"):
            Geometry().out()

            a = Float(10)._lc("Var a")
            b = Float(10)._lc("Var b")
            c = (a + b)._lc("a + b", (1, 0, 0))
        ```

        Arguments
        ---------
        - label (str = None) : node label
        - color (color = None) : node color

        Returns
        -------
        - self
        """
        self.node_label = label
        self.node_color = color
        return self

    def _lcop(self, label=None):
        return self._lc(label=label, color='OPERATION')

    # =============================================================================================================================
    # Link node from
    # =============================================================================================================================

    def link_from(self, **params):
        self.node.link_from(**params)
        return self

    # =============================================================================================================================
    # Gizmo
    # =============================================================================================================================

    @property
    def pin_gizmo(self):
        self._is_empty("No gizmo is possible.")
        return self._bsocket.pin_gizmo

    @pin_gizmo.setter
    def pin_gizmo(self, value):
        self._is_empty("No gizmo is possible.")
        self._bsocket.pin_gizmo = value

    # ====================================================================================================
    # A dynamic attribute can be:
    # - a peer socket : an output socket of the owning node
    # - a group method
    # To avoid names collision, the attribute name can be suffixed by '_' which is ignored
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get attr
    # ----------------------------------------------------------------------------------------------------

    def __getattr__(self, name):

        self._is_empty(f"Impossible to get an attribute from an empty socket (name: '{name}')")

        # Ignore the ending '_' char
        true_name = name
        if name[-1] == '_':
            true_name = name[:-1]
            if true_name == "" or true_name[-1] == '_':
                raise AttributeError(f"Socket {self} doesn't have peer socket named '{name}'")
            
        sc_name = utils.snake_case(true_name)
            
        # ---------------------------------------------------------------------------
        # Another node output socket
        # ---------------------------------------------------------------------------
            
        socket = self.node.get_socket('OUTPUT', true_name, None, halt=False)
        if socket is not None:
            return socket
        
        # ---------------------------------------------------------------------------
        # A group
        # ---------------------------------------------------------------------------

        trees = utils.get_available_groups(self.node._tree._btree.bl_idname)
        node_tree = None
        for group_name, spec in trees.items():
            if utils.snake_case(group_name) == sc_name:
                node_tree = blender.load_node_group(spec)
                break

        if node_tree is not None:

            def group_call(named_sockets={}, **sockets):
                
                all_sockets = {**named_sockets, **sockets}

                new_sockets = {**named_sockets}

                check_selec = 'Selection' not in all_sockets and 'selection' not in all_sockets and self._socket_type == 'GEOMETRY'

                interf = TreeInterface(node_tree)
                socks = interf.get_sockets('INPUT')
                for isock, sock in enumerate(socks):

                    # Current socket is the proper type
                    if SocketType(sock) == self._socket_type:
                        if sock.name not in all_sockets and utils.snake_case(sock.name) not in all_sockets:

                            # Set value to self
                            new_sockets[sock.name] = self

                            # Selection following a Geometry 
                            if check_selec and isock < len(socks) - 1:
                                next_sock = socks[isock + 1]
                                if next_sock.name == 'Selection' and SocketType(next_sock) == 'BOOLEAN':
                                    new_sockets['Selection'] = self.get_selection()
                            break

                return Group(node_tree.name, named_sockets = new_sockets, **sockets)._out
            
            # Returns the function creating the group with the proper arguments
            return group_call
        
        # ---------------------------------------------------------------------------
        # Error message
        # ---------------------------------------------------------------------------

        is_node = true_name in dir(self.node)

        node_names = list(set([sock.name for sock in self.node._bnode.outputs]))
        tree_names = list(trees.keys())

        node_prox = utils.prox_names(true_name, node_names)
        tree_prox = utils.prox_names(true_name, tree_names)

        if is_node:
            msg = f"Perhaps you want to call the node method '{true_name}', use syntax: 'socket.node.{true_name}(...)' instead of 'socket.{true_name}'"
        elif len(node_prox):
            msg = f"Perhaps you wanted to access the peer socket '{node_prox[0]}' ({utils.snake_case(node_prox[0])})"
        elif len(tree_prox):
            msg = f"Perhaps you wanted to call the group '{tree_prox[0]}' ({utils.snake_case(tree_prox[0])})"
        else:
            msg = f"If you try to access a peer socket, the node sockets are given below:\n{repr(self.node)}"

        raise NodeError(f"{type(self).__name__} socket doesn't have an attribute named '{name}'.\n{msg}")

    

    # ====================================================================================================
    # Test a value in a list
    # ====================================================================================================

    @staticmethod
    def check_in_list(value, valids, context=""):
        if value in valids:
            return True
        raise NodeError(f"{context} value error: '{value}' is not valid.", valids=valids)
    
    # ====================================================================================================
    # To output
    # ====================================================================================================

    def out(self, name: str = None, panel: str = "", **props):
        """ Plug the value to the Group Output Node.

        ``` python
        with GeoNodes("Plug to group output"):
            # Create a cube
            geo = Mesh.Cube()
            # To Group Output geometry as socket named "Cube"
            geo.out("Cube")
        ```

        The "Do nothing" modifier is simply ``` Geometry().out() ```

        Arguments
        ---------
        - name (str = None) : socket name

        Returns
        -------
        - None
        """
        self._is_empty(f"Impossible to link an empty socket (name: '{name}').")

        out_node = self._tree.get_output_node()
        out_node.set_input_socket(name=name, value=self, create=True, panel=panel, **props)

    # ====================================================================================================
    # Context management
    # ====================================================================================================

    def _push(self):

        from .treeclass import Layout

        self.node._push()

        # Push a Layout dedicated this context
        # (will be removed by arrange if no node is created)
        if self._use_layout:
            self._layout = Layout()
            self._layout.push()

    def _pop(self, error: bool = False):

        self.node._pop(error)

        # Pop inout capture and layout
        if self._use_layout:
            self._layout.pop()

    def __enter__(self):
        self._push()
        return self
    
    def __exit__(self, type, exc_value, traceback):
        ok = exc_value is None or isinstance(exc_value, Break)
        self._pop(not ok)
    
    # ====================================================================================================
    # Menu Switch
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constructor version
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def MenuSwitch(cls, 
                   named_sockets    : dict = {},
                   default_menu     : str = None,
                   **sockets):
        """ > Node <&Node Menu Switch>

        The items of the Menu Switch node are provided in the 'items' dict.

        Arguments
        ---------
        - named_sockets (dict = {}) : sockets to create
        - default_menu (str = None) : default menu value
        - sockets (dict) : items

        Returns
        -------
        - Socket
        """
        node = MenuNode('Menu Switch',
                named_sockets = named_sockets,
                data_type = SocketType(cls.SOCKET_TYPE).type,
                default_menu = default_menu,
                **sockets)
        
        return cls(node._out)
    
    # ----------------------------------------------------------------------------------------------------
    # Method version
    # ----------------------------------------------------------------------------------------------------

    def menu_switch(self,
                self_name       : str = 'Self', 
                named_sockets   : dict = {},
                default_menu    : str = None,
                **sockets):
        """ > Node <&Node Menu Switch>

        [&NO_JUMP]

        Self is connected to the first menu item with the name provided as argument.

        The items of the Menu Switch node are provided in the 'items' dict.
        An group input socket named after the 'name' argument is linked to menu selector.

        Arguments
        ---------
        - named_sockets (dict = {}) : sockets to create
        - default_menu (str = None) : default menu value
        - sockets (dict) : items

        Returns
        -------
        - Socket
        """        
        return self.MenuSwitch(named_sockets = {self_name: self, **named_sockets}, default_menu=default_menu, **sockets)
    
    # ====================================================================================================
    # Index Switch
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constructor version
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def IndexSwitch(cls, *values, index = None, default_index: int = 0):
        """ > Node <&Node Index Switch>

        ``` python
        with GeoNodes("IndexSwitch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=tree.new_input("Geometry index", default_value=2))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer = None) : socket 'Index' (Index)
        - defaut_index (int = 0) : default idex

        Returns
        -------
        - Socket
        """
        #return IndexSwitchNode(*values, index=index, data_type=cls.input_type())._out
        return MenuNode('Index Switch', 
                        {str(i): value for i, value in enumerate(values)}, 
                        data_type=cls.SOCKET_TYPE, 
                        Index=index,
                        default_menu = default_index)._out
    
    # ----------------------------------------------------------------------------------------------------
    # Method version
    # ----------------------------------------------------------------------------------------------------

    def index_switch(self, *values, index = None, default_index: int = 0):
        """ > Node <&Node Index Switch>

        ``` python
        with GeoNodes("index_switch demo") as tree:

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = geo.index_switch(cube, sphere, cone, index=tree.new_input("Geometry index", default_value=2))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer = None) : socket 'Index' (Index)
        - defaut_index (int = 0) : default idex

        Returns
        -------
        - Socket
        """
        return self.IndexSwitch(self, *values, index=index, default_index=default_index)
    
    # ====================================================================================================
    # Switch
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constructor version
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Switch(cls, condition=None, false=None, true=None):
        """ > Node <&Node Switch>

        ``` python
        with GeoNodes("Switch demo"):

            # Two possible geometries
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()

            # Select
            geo = Geometry.Switch(Boolean(True, "Use Sphere"), cube, sphere)

            # To group output
            geo.out()
        ```

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - false : socket 'False' (False)
        - true : socket 'True' (True)

        Returns
        -------
        - Socket
        """
        input_type = SocketType(cls.SOCKET_TYPE).items_type
        return Node('Switch', {'Switch': condition, 'False': false, 'True': true}, input_type=input_type)._out

    # ----------------------------------------------------------------------------------------------------
    # Method version
    # ----------------------------------------------------------------------------------------------------

    def switch(self, condition=None, true=None):
        """ > Node <&Node Switch>

        [&NO_JUMP]

        Self is connected to 'false' socket.

        ``` python
        with GeoNodes("Switch demo"):

            choice = Boolean(True, "Use Sphere")

            # Two possible geometries
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()

            # Select
            geo = cube.switch(choice, sphere)

            # To group output
            geo.out()
        ```

        Information
        -----------
        - Socket 'False' : self

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - true : socket 'True' (True)

        Returns
        -------
        - Socket
        """
        return self.Switch(condition=condition, false=self, true=true)
    
    # ----------------------------------------------------------------------------------------------------
    # Alternative method version
    # ----------------------------------------------------------------------------------------------------

    def switch_false(self, condition=None, false=None):
        """ > Node <&Node Switch>

        [&NO_JUMP]

        Self is connected to 'true' socket.

        > [!IMPORTANT]
        > This methods behaves the inverse of <#switch> : self is connected to "True" socket and  the argument to "False", socket

        > [!NOTE]
        > This method is mainly provided to cover the case when 'False' socket is None

        ``` python
        with GeoNodes("Switch demo"):

            geo = Geometry()

            show_geometry = Boolean(False, "Merge with Cube")

            cube = Mesh.Cube()

            geo += cube.switch_false(show_geometry)

            # Is equivalent to
            geo += Geometry.Switch(show_geometry, None, cube)

            # To group output
            geo.out()
        ```

        > [!NOTE]
        > This method let self socket unchanged. To set self socket to the result

        Information
        -----------
        - Socket 'True' : self

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - false : socket 'False' (False)

        Returns
        -------
        - Socket
        """
        return self.Switch(condition=condition, false=false, true=self)
    
    # ====================================================================================================
    # Loops
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Repeat
    # ----------------------------------------------------------------------------------------------------

    def repeat(self, iterations=1, named_sockets: dict={}, **sockets):
        """ Repeat zone

        Arguments
        ---------
        - Iteration (Integer = 1) : iteration socket
        - named_socket (dict) : named sockets
        - sockets (dict) : other sockets

        Returns
        -------
        - ZoneIterator
        """
        node = ZoneNode("Repeat", self, named_sockets=named_sockets, Iterations=iterations, **sockets)
        return ZoneIterator(self, node)
    
    @classmethod
    def Repeat(cls, iterations=1, named_sockets: dict={}, **sockets):
        """ Repeat zone

        Arguments
        ---------
        - Iteration (Integer = 1) : iteration socket
        - named_socket (dict) : named sockets
        - sockets (dict) : other sockets

        Returns
        -------
        - ZoneIterator
        """
        return cls.Empty().repeat(iterations, named_sockets=named_sockets, **sockets)
    
    # ----------------------------------------------------------------------------------------------------
    # Simulation
    # ----------------------------------------------------------------------------------------------------

    def simulation(self, named_sockets: dict={}, **sockets):
        """ Simulation zone

        Arguments
        ---------
        - named_socket (dict) : named sockets
        - sockets (dict) : other sockets

        Returns
        -------
        - ZoneIterator
        """
        node = ZoneNode("Simulation", self, named_sockets=named_sockets, **sockets)
        return ZoneIterator(self, node)

    # ====================================================================================================
    # Class Test
    # ====================================================================================================

    @staticmethod
    def _class_test():

        from .utils import SOCKET_CLASSES
        from .geonodes import GeoNodes
        from .geometry_class import Geometry
        from .sock_float import Float
        from .treeclass import Layout
        from .sock_color import Color
        from .sock_rotation import Rotation
        from .sock_vector import Vector
        from .sock_matrix import Matrix

        with GeoNodes("Socket Class Test") as tree:

            # Create inputs
            for stype, klass in SOCKET_CLASSES.items():
                if stype == 'SHADER':
                    continue
                class_name = klass.__name__
                a = klass(name=class_name)

            # Getting existing inputs
            for stype, klass in SOCKET_CLASSES.items():
                if stype in ['SHADER', 'MENU']:
                    continue
                class_name = klass.__name__
                klass.Input(class_name).out(f"Out {class_name}")

            # Constants
            with Layout("Constants"):
                for stype, klass in SOCKET_CLASSES.items():
                    if stype == 'SHADER':
                        continue
                    a = klass()

            # Arrays
            with Layout("Colors"):
                Color(.8).out(panel="Color")
                Color((.1, .2, .3)).out(panel="Color")
                Color((.1, .2, .3, .4)).out(panel="Color")
                Color(Float(.89)).out(panel="Color")
                Color((Float(.5), 0, 0)).out(panel="Color")
                Color((0, Float(.5), 1)).out(panel="Color")
                Color((Float(.5), Float(.5), Float(.5), Float(.5))).out(panel="Color")

            with Layout("Vector"):
                Vector(.8).out(panel="Vector")
                Vector((.1, .2, .3)).out(panel="Vector")
                Vector(Float(.89)).out(panel="Vector")
                Vector((Float(.5), 0, 0)).out(panel="Vector")
                Vector((0, Float(.5), 1)).out(panel="Vector")
                Vector((Float(.5), Float(.5), Float(.5))).out(panel="Vector")

            with Layout("Rotation"):
                Rotation(.8).out(panel="Rotation")
                Rotation((.1, .2, .3)).out(panel="Rotation")
                Rotation(Float(.89)).out(panel="Rotation")
                Rotation((Float(.5), 0, 0)).out(panel="Rotation")
                Rotation((0, Float(.5), 1)).out(panel="Rotation")
                Rotation((Float(.5), Float(.5), Float(.5))).out(panel="Rotation")

            with Layout("Matrix"):
                Matrix(.8).out(panel="Matrix")
                Matrix([i for i in range(16)]).out(panel="Matrix")
                Matrix([Float(i) for i in range(16)]).out(panel="Matrix")




# ====================================================================================================
# Input socket
# ====================================================================================================

class Input(Socket):

    __slots__ = Socket.__slots__ + ('name', 'panel', 'props')

    SOCKET_TYPE = 'CUSTOM'

    def __init__(self, name: str = None, panel: str = "", **props):
        """ Input Socket wrapping an output virtual socket.

        When plugging to the input socket of a Node, a New socket is creaated.

        Arguments
        ---------
        - name (str = None) : the name to give to the output
        - panel (str = "") : the panel to create if possible
        - props (dict) : socket properties
        """

        innode = Tree.current_tree().get_input_node()

        bsocket = None
        for bsock in innode._bnode.outputs:
            if bsock.type == 'CUSTOM':
                bsocket = bsock
                break

        if bsocket is None:
            raise RuntimeError(f"Impossible to initialize an Input socket: no output virtual socket found in node {innode}.")
        
        super().__init__(bsocket)

        self.name  = name
        self.panel = panel
        self.props = {**props}



