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

module : treeclass
------------------
- Tree: the tree currently edited
- Node: base class to create a node

Note that to ease the scripting, nodes are created without refering explicity to a tree,
but get the tree in a stack of trees as the 'current tree'.

At creation time, Trees a psuh on top of a stack. current_tree allows to get
the current edited tree.

In addition, other classes are implemented:
- Layout        : Creates a Frame where the new nodes are placed into
- Panel         : Current panel into which placing the input and output nodes
- Group         : Node Group creation
- GroupF        : (deprecated) Utility class to call a group with python syntax
- G             : An advanced feature to expose Groups as python methods

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/01/18 # G as dynamic class
- update :   2025/03/27 # Blender 4.4 : panels can be nested
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.1"
__blender_version__ = "4.3.0"

import numpy as np
import bpy
from time import time

from .scripterror import NodeError
from . import treearrange
from . import constants
from . import utils
from . import blender
from .utils import Break
from .sockettype import SocketType
from .signature import Signature
from .treeinterface import ItemPath, TreeInterface

# ====================================================================================================
# Input / output panel
# ====================================================================================================

class Panel:
    def __init__(self, name: str, tip: str = "", default_closed: bool = False):
        """ Socket panel

        All group input and output sockets an panels will be created within the current panel

        Arguments
        ---------
        - name :panel title
        - tip : panel description
        - default_closed : closed by default
        """

        self.tree   = Tree.current_tree()
        self.path   = self.tree.get_panel(name)
        self.bpanel = None

        if self.tree._interface is not None:
            self.bpanel = self.tree._interface.get_panel(self.path, create=True)
            self.bpanel.description = tip

    def __str__(self):
        return self.path.path

    def push(self):
        self.tree.push_panel(self.path)

    def pop(self):
        self.tree.pop_panel()

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, type, exc_value, traceback):
        self.pop()

    # ====================================================================================================
    # Panel test
    # ====================================================================================================

    @staticmethod
    def _class_test():
        
        from geonodes import GeoNodes, Panel, Float, Mesh

        with GeoNodes("Panel Class Test"):
            
            # Create a top level socket
            a = Float(1, name="A")
            
            # Create in a panel using panel argument
            a += Float(2, name="B Panel", min=0, max=100, panel="Panel")
            
            # Create in a panel using Panel context
            with Panel("Panel"):
                a += Float(3, "C Panel")
                a += Float(4, "D Sub Panel", panel="Sub Panel")
                
            # Chaining panel names
            with Panel("Panel > Sub Panel"):
                a += Float(5, name="E Sub Panel")

            with Panel("Panel"):
                with Panel("Other"):
                    a += Float(6, name="F Other")
                    a += Float(7, name="G Last", panel="Last")
            
            a += Float(8, name="H Last", panel="Panel>Other>Last")
            
            # Creating homonyms
            with Panel("Panel_1"):
                a += Float(9, name="I 2nd Panel")
                
            with Panel("Panel_1"):
                with Panel("Sub Panel"):
                    a += Float(10, name="J 2nd Sub Panel")

            # Use the inputs
            Mesh.IcoSphere(radius=a/8).out()

# ====================================================================================================
# Layout
# ====================================================================================================

class Layout:
    def __init__(self, label=None, color=None):
        """ Node Frame

        All nodes created when a Layout is open are placed in this layout.
        If the 'color' argument is None, a random color is used

        ``` python
        with GeoNodes("Layout Demo"):

            with Layout("Some maths"):
                z = gnmath.atan2(nd.position.z, Vector((nd.position.x, nd.position.y, 0)).length)

            geo = Mesh()
            geo.points.offset = (0, 0, z)

            geo.out()
        ```

        Arguments
        ---------
        - label (str = None) : Layout title
        - color (blender color = None) : Layout color (randomly generated if None)
        """
        from .nodeclass import Node

        self.tree  = Tree.current_tree()
        self.frame = Node('Frame')
        self.title = label
        if color is not None:
            self.frame._bnode.use_custom_color = True
            self.frame._bnode.color = self.tree._get_color(color)

    @property
    def title(self):
        return self.frame._bnode.label
    
    @title.setter
    def title(self, value):
        if value is not None:
            self.frame._bnode.label = value

    def push(self):
        self.tree._layouts.append(self.frame._bnode)

    def pop(self):
        self.tree._layouts.pop()

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, type, exc_value, traceback):
        self.pop()

        if isinstance(exc_value, Break):
            return True
        

# ====================================================================================================
# Tree
# ====================================================================================================

class Tree:

    _total_nodes = 0
    _total_links = 0

    TREE_STACK = []

    def __init__(self, tree_name: str, tree_type: str='GeometryNodeTree', clear: bool=True, fake_user: bool=False, is_group: bool=False, prefix: str = ""):
        """ Root class for <!GeoNodes> and <!ShaderNodes> trees.

        The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
        and becomes the current tree.
        The Tree is poped from the stack with the method <#pop>.

        Better use the context management syntax:

        ``` python
        with GeoNodes("My Tree") as tree:

            pass

        ```

        > [!IMPORTANT]
        > Trees scripted with **geonodes** are kept distinct from manually created trees by putting the
        > marker string _'GEONODES'_ in the description attribute. If you initialize a Tree with the
        > name of an existing tree:
        > - it will be cleared if it is a tree scripted with **geonodes**
        > - it will be renamed if it is not the case
        > This avoids to accidentally delete a manually created tree.

        > [!CAUTION]
        > This doesn't work with materials embedded shaders. So, make sure not to override
        > a existing shader when instantiating a new <!ShaderNodes>.

        The 'panel' argument is the default name to use when the tree is called from another tree using method <#link_from>.

        Arguments
        ---------
        - tree_name : tree name
        - tree_type : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
        - clear : clear the current tree
        - fake_user : fake user flag
        - is_group : Group or not
        - prefix : str prefix to add at the beging of the tree name
        """
        self._btree = None

        # In / out nodes cache
        self._input_node  = None
        self._output_node = None

        # ---------------------------------------------------------------------------
        # Stacks
        # ---------------------------------------------------------------------------

        self._panels        = [ItemPath(None)]
        #self._capture_inout = []
        self._layouts       = []

        # Input / output socket creation are performed by node with dynamic
        # sockets (either with items or with tree_node)
        # By default, these are input_node and output_node
        # This behavior can be overloaded using input and output stacks
        
        self._output_stack  = []
        self._input_stack   = []

        # Exit error
        self._exit_error = False

        # Prefix
        if prefix is None:
            prefix =  ""

        prefix = str(prefix)
        if len(prefix):
            tree_name = f"{prefix} {tree_name}"
        self._prefix = prefix

        # ----------------------------------------------------------------------------------------------------
        # Shader Node tree is a property of the Material
        # ----------------------------------------------------------------------------------------------------

        if tree_type == 'ShaderNodeTree':

            self._material = None
            if not is_group:
                self._material = bpy.data.materials.get(tree_name)

                if self._material is None:
                    self._material = bpy.data.materials.new(tree_name)

                self._material.use_nodes = True
                self._btree = self._material.node_tree
                self._material.use_fake_user = fake_user

        # ----------------------------------------------------------------------------------------------------
        # Get the tree nodes from node_groups
        # ----------------------------------------------------------------------------------------------------

        if self._btree is None:
            self._btree = utils.get_tree(tree_name, tree_type=tree_type, create=True)
            self._btree.use_fake_user = fake_user

        self._is_group = is_group

        # Managed lists
        self._nodes = [] # List of nodes

        # Clear the tree
        if clear:
            self.clear()

        # Interface
        self._interface = None
        if self._is_group or tree_type == 'GeometryNodeTree':
            self._interface = TreeInterface(self._btree)
            self._interface.clear(use_bin=True)

        # Random generator for random colors
        self._rng = np.random.default_rng(0)

    # ====================================================================================================
    # Stack of trees
    # ====================================================================================================

    @staticmethod
    def current_tree():
        """ > Get the Current Tree.

        Returns None if no tree is currently open

        Returns
        -------
        - Tree : current tree or None
        """
        if len(Tree.TREE_STACK):
            return Tree.TREE_STACK[-1]
        else:
            return None
        
    # ----------------------------------------------------------------------------------------------------
    # Push the current tree zone
    # ----------------------------------------------------------------------------------------------------

    def push(self):
        """ > Make this tree zone the current one

        > [!IMPORTANT]
        > This methods shouldn't be called directly, better use a **with** context block.

        ``` python
        with Tree("My Name"):
            pass
        ```
        """
        Tree.TREE_STACK.append(self)
        return self

    # ----------------------------------------------------------------------------------------------------
    # Pop from the stack
    # ----------------------------------------------------------------------------------------------------

    def pop(self):
        """ > Remove this tree from the stack

        > [!IMPORTANT]
        > This methods shouldn't be called directly, better use a **with** context block.

        Raises
        ------
        - NodeError : if this tree is not the current one

        ``` python
        with Tree("My Name"):
            pass
        ```
        """
        # Remove from stack
        tree = Tree.TREE_STACK.pop()
        if tree != self:
            raise RuntimeError(f"Error in tree stack management")

        # Empty the interface bin

        if not self._exit_error and self._interface is not None:
            self._interface.empty_bin()

        # Arrange the nodes
        self.arrange()

        # Stats
        print(f"Tree '{self._btree.name}' built: {self._str_stats}")

        Tree._total_nodes += len(self._btree.nodes)
        Tree._total_links += len(self._btree.links)        

    # ----------------------------------------------------------------------------------------------------
    # Context management
    # ----------------------------------------------------------------------------------------------------

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, type, exc_value, traceback):

        # In case of error, the sockets are not cleaned
        if not isinstance(exc_value, Break):
            self._exit_error = exc_value is not None

        self.pop()

        if isinstance(exc_value, Break):
            return True

    # ====================================================================================================
    # Remove node groups
    # ====================================================================================================

    @staticmethod
    def remove_groups(names=None, prefix=None, geonodes=True, shadernodes=True):
        """ > Remove Groups created by GeoNodes.

        > [!IMPORTANT]
        > This method can only remove groups created by **GeoNodes**.

        Arguments
        ---------
        - names (str or list of strs = None) : name of the node groups to remove (all if None)
        - prefix (str = None) : name prefix for the groups to delete
        - geonodes (bool = True) : remove geometry nodes groups
        - shaderndes (bool = True) : remove shader nodes groups

        Returns
        -------
        - None
        """

        groups = []
        if prefix is None:
            prefix_ = ""
        else:
            prefix_ = prefix + ' '

        tree_types = []
        if geonodes:
            tree_types.append('GeometryNodeTree')
        if shadernodes:
            tree_types.append('ShaderNodeTree')

        for group in bpy.data.node_groups:
            if group.bl_idname not in tree_types:
                continue

            if not group.description.startswith('GEONODES'):
                continue

            if prefix is not None and group.name[:len(prefix_)] != prefix_:
                continue

            if names is None:
                pass
            elif isinstance(names, str):
                if group.name != prefix_ + names:
                    continue
            elif isinstance(names, list):
                ok = False
                for name in names:
                    if group.name == prefix_ + name:
                        ok = True
                        break
                if not ok:
                    continue
            else:
                raise Exception(f"Argument names '{names}' is not valid: None, str or list of strs expected")

            groups.append(group)

        print("Remove node groups")
        for group in groups:
            print(' -', group.name)
            bpy.data.node_groups.remove(group)

        print(f"{len(groups)} node groups removed")

    # ====================================================================================================
    # Check if the blender node is valid in the context
    #
    # Nodes specific to tools can't be inserted in modifiers
    # ====================================================================================================

    def check_node_validity(self, bnode):
        pass

    # ====================================================================================================
    # Counters
    # ====================================================================================================

    def __str__(self):
        return f"<Tree '{self._btree.name}' ({type(self).__name__}): {len(self._btree.nodes)} nodes and {len(self._btree.links)} links>"
    
    @staticmethod
    def _btree_repr(btree):
        s = ""

        sepa = "\n   - "

        s += "\nInputs:"
        in_node, out_node = None, None
        for node in btree.nodes:
            if node.bl_idname == 'NodeGroupInput':
                in_node = node
            if node.bl_idname == 'NodeGroupOutput':
                out_node = node

        if in_node is not None:
            a = []
            for sock in in_node.outputs:
                name = f"[{sock.name}]"
                if not sock.enabled:
                    name += "( d)"
                if sock.is_linked:
                    name += " -> " + sock.links[0].to_socket.name
                a.append(name)

            s += sepa + sepa.join(a)

        s += "\nOutputs:"
        if out_node is not None:
            a = []
            for sock in out_node.inputs:
                name = f"[{sock.name}]"
                if not sock.enabled:
                    name += "( d)"
                if sock.is_linked:
                    name = sock.links[0].from_socket.name + " -> " + name
                a.append(name)
            s += sepa + sepa.join(a) + "\n"

        return s + "\n"

    
    def __repr__(self):
        return str(self) + "\n" + Tree._btree_repr(self._btree)

    @classmethod
    def _reset_counters(cls):
        cls._total_nodes = 0
        cls._total_links = 0
        cls._total_time  = 0.

    @classmethod
    def _display_counter(cls, title):
        print(f"{title}: {Tree._total_nodes} nodes, {Tree._total_links} links in {Tree._total_time:.1f} s")

    @property
    def _str_stats(self):
        return f"{len(self._btree.nodes)} nodes, {len(self._btree.links)} links"

    # ====================================================================================================
    # Types of tree
    # ====================================================================================================

    @classmethod
    def is_geonodes(cls):
        """ > Current Tree is Geometry Nodes.

        Returns
        -------
        - True if Tree is GeoNodes, False otherwise
        """
        return cls.current_tree()._btree.bl_idname == 'GeometryNodeTree'

    @classmethod
    def is_shader(cls):
        """ > Current Tree is Shader Nodes.

        Returns
        -------
        - True if Tree is ShaderNodes, False otherwise
        """
        return cls.current_tree()._btree.bl_idname == 'ShaderNodeTree'

    @classmethod
    def is_compositor(cls):
        return cls.current_tree()._btree.bl_idname == 'CompositorNodeTree'
    
    # ====================================================================================================
    # Panel
    # ====================================================================================================

    def get_panel(self, sub_panel: str = ""):
        return self._panels[-1] + ItemPath.to_item_path(sub_panel)
    
    def push_panel(self, new_panel: str):
        self._panels.append(ItemPath.to_item_path(new_panel))

    def pop_panel(self):
        self._panels.pop()
        assert len(self._panels) >= 1, f"Error in pushing / poping tree panels."
    
    # ====================================================================================================
    # Nodes
    # ====================================================================================================

    def clear(self):
        """ Clear the content of the Tree.

        Remove all the nodes in the Tree.
        """
        to_clear = []
        self._nodes.clear()
        self._btree.links.clear()
        self._btree.nodes.clear()

    def register_node(self, node):
        self._nodes.append(node)
        if len(self._layouts) and node._bnode.bl_idname != 'NodeGroupOutput':
            node._bnode.parent = self._layouts[-1]
        return node


    # ====================================================================================================
    # Sockets creation
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Set the default value of an input socket
    # ----------------------------------------------------------------------------------------------------

    def set_input_socket_default(self, socket, value=None):

        if value is None:
            return

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            return

        try:
            bsocket.default_value = value
        except:
            pass

        io_socket = self._interface.by_identifier(bsocket.identifier)
        if io_socket is None:
            return

        if not hasattr(io_socket, 'default_value'):
            return

        try:
            io_socket.default_value = value
        except:
            return    

    # ----------------------------------------------------------------------------------------------------
    # Create an input socket
    # ----------------------------------------------------------------------------------------------------

    def create_input_socket(self, bl_idname, name, panel="", **props):
        """ Create a new input socket.

        This is an **input socket** of the zone, hence an **output socket** of the input node.

        Arguments
        ---------
            - bl_idname (str) : socket bl_idname
            - name (str): Socket name
            - panel (str = "") : Panel to place the socket in
            - props : properties specific to interface socket

        Returns
        -------
            Socket
        """
        input_node = self.get_input_node()
        socket = input_node.create_socket('OUTPUT', bl_idname, name, panel=panel, **props)

        return socket
            

    # ----------------------------------------------------------------------------------------------------
    # Create a new output socket
    # ----------------------------------------------------------------------------------------------------

    def create_output_socket_OLD(self, socket, name=None, panel="", **props):
        """ Create a new output socket.

        This is an **output socket** of the Tree, hence an input socket of the <&Group Output> node.

        Arguments
        ---------
        - socket (socket) : socket
        - name (str) : Socket name
        - panel (str = "") : Panel name

        Returns
        -------
            Socket
        """
        if len(self._capture_inout):
            out_socket = self._capture_inout[-1].create_output_socket(socket, name=name, panel=panel, **props)
            if out_socket is not None:
                return out_socket

        # ---------------------------------------------------------------------------
        # NodeSocket from argument
        # ---------------------------------------------------------------------------

        bsocket = utils.get_bsocket(socket)
        assert bsocket is not None, f"Strange {socket=}, {name=}"
        bl_idname = bsocket.bl_idname
        
        s_sub = constants.SOCKET_SUBTYPES[bl_idname]
        socket_type, subtype = s_sub['nodesocket'], s_sub['subtype']
        #socket_type, subtype = constants.SOCKET_SUBTYPES[bl_idname]
        if name is None:
            name = bsocket.name if bsocket.label == "" else bsocket.label

        # ---------------------------------------------------------------------------
        # Create in the panel
        # ---------------------------------------------------------------------------

        bpanel = self.get_bpanel(panel)
        io_socket = self._interface.create_socket('OUTPUT', name, socket_type, parent=bpanel, **props)

        # Subtype if not provided
        if subtype is not None and 'subtype' not in props:
            io_socket.subtype = subtype

        # ---------------------------------------------------------------------------
        # Create the link
        # ---------------------------------------------------------------------------

        in_socket = self.output_node.socket_by_identifier('INPUT', io_socket.identifier)
        self.link(in_socket, socket)

    # ----------------------------------------------------------------------------------------------------
    # Create a new input socket from an existing node input socket
    # ----------------------------------------------------------------------------------------------------

    def create_input_from_socket_OLD(self, input_socket, name=None, panel="", **props):
        """ Create a new group input socket from an existing input socket.

        Arguments
        ---------
        - input_socket (socket) : a node input _insocket
        - name (str = None) : name of the group input socket to create
        - panel (str = "") : name of the panel
        - props (dict) : input socket properties

        Returns
        -------
        - Socket
        """
        if len(self._capture_inout):
            socket = self._capture_inout[-1].create_input_from_socket(input_socket, name=name, panel=panel, **props)
            if socket is not None:
                return socket

        # ---------------------------------------------------------------------------
        # Create the socket in the parent panel
        # ---------------------------------------------------------------------------

        bsocket = utils.get_bsocket(input_socket)
        io_socket = self._interface.create_socket('INPUT', 
            name        = name, 
            socket_type = bsocket.bl_idname, 
            parent      = self.get_bpanel(panel),
            from_socket = bsocket,
            **props)

        # ---------------------------------------------------------------------------
        # Link with the provided socket
        # ---------------------------------------------------------------------------

        socket = utils.to_socket(self.input_node.socket_by_identifier('OUTPUT', io_socket.identifier))

        if bsocket.type == 'MENU' and bsocket.node.bl_idname == 'GeometryNodeMenuSwitch':
            self.link_menu(socket, input_socket)
        else:
            self.link(socket, input_socket)

        return socket
    
    # ====================================================================================================
    # Get the signature
    # ====================================================================================================

    def get_signature(self, include: list = None, exclude: list = [], enabled_only=True, with_sockets: bool = False):
        """ Build the closure signature of the tree.

        The closure signature is the tuple made of the outpout signature of the input node
        and the input signature of the output node

        Returns
        -------
        - Signature
        """
        return Signature(
            Signature.from_node(
                self.input_node, 
                include         = include, 
                exclude         = exclude, 
                enabled_only    = enabled_only, 
                with_sockets    = with_sockets).outputs,
            Signature.from_node(
                self.output_node, 
                enabled_only    = enabled_only, 
                with_sockets    = with_sockets).inputs)

    # ====================================================================================================
    # Arranges nodes
    # ====================================================================================================

    def arrange(self):
        """ > Arrange the nodes in the editor.

        Try to arrange properly the nodes from left to right.

        This method is called when the Tree is poped from the stack.

        Returns
        -------
        - None
        """

        treearrange.arrange(self._btree)

    # ====================================================================================================
    # Node colors
    # ====================================================================================================

    @staticmethod
    def _get_color(name):
        if isinstance(name, tuple):
            return name
        
        rng = Tree.current_tree()._rng
        if name is None:
            return tuple(rng.uniform(0., .7, 3))
        elif isinstance(name, str):
            if name in ['OP', 'OPERATION']:
                return (.406, .541, .608)
            elif name == 'MACRO':
                return (.261, .963, .409)
            elif name == 'AUTO_GEN':
                return (.583, .229, .963)
            elif name == 'WARNING':
                return (.949, .574, .119)
            else:
                raise Exception(f"Non referenced color", name)
        else:
            return name

    # ====================================================================================================
    # Create a link
    # ====================================================================================================

    def link(self, out_socket, in_socket, handle_dynamic_sockets=False):
        """ > Create a link between two sockets.

        Arguments
        ---------
        - out_socket (socket) : a node output socket
        - in_socket (socket) : input socket from another node

        Returns
        -------
        - Link
        """

        #if hasattr(out_socket, '_bsocket'):
        if '_bsocket' in dir(out_socket):
            out_socket = out_socket._bsocket

        #if hasattr(in_socket, '_bsocket'):
        if '_bsocket' in dir(in_socket):
            in_socket = in_socket._bsocket

        link = self._btree.links.new(out_socket, in_socket, handle_dynamic_sockets=handle_dynamic_sockets)

        utils.check_link(link)
        utils.check_zones(self._btree)

        # ---------------------------------------------------------------------------
        # Menu
        # ---------------------------------------------------------------------------

        if True:
            out_socket = utils.get_bsocket(out_socket)
            in_socket = utils.get_bsocket(in_socket)

            if out_socket.bl_idname == 'NodeSocketMenu' and in_socket.bl_idname == 'NodeSocketMenu':

                enums = utils.get_menu_enums(out_socket)
                if len(enums):
                    def_value = in_socket.default_value
                    if def_value == "":
                        def_value = out_socket.default_value
                        if def_value == "":
                            def_value = enums[0]

                    in_socket.default_value = def_value
                    index = list(enums).index(def_value) + 1

                    # Update modifiers with default value index
                    for mod in blender.get_geonodes_modifiers(self._btree):
                        mod[out_socket.identifier] = index

        return link
    
    # ====================================================================================================
    # Link menu
    # ====================================================================================================

    def link_menu(self, out_socket, in_socket, default_value=None):

        return self.link(out_socket, in_socket)


    # ====================================================================================================
    # Tree Input / Output
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Default input node
    # ----------------------------------------------------------------------------------------------------

    @property
    def input_node(self):
        """ > Return a <&Node Group Input> node

        If the node doesn't already exist, it is created.

        Returns
        -------
        - Node
        """
        from .nodeclass import Node

        for node in self._nodes:
            if node._bnode.bl_idname ==  'NodeGroupInput':
                return node
            
        return Node('NodeGroupInput')
    
    # ----------------------------------------------------------------------------------------------------
    # Default output node
    # ----------------------------------------------------------------------------------------------------

    @property
    def output_node(self):
        """ Returns a <&Node Group Output> node

        If the node doesn't already exist, it is created.

        Returns
        -------
        - Node
        """
        from .nodeclass import Node

        for node in self._nodes:
            if node._bnode.bl_idname ==  'NodeGroupOutput':
                return node
            
        return Node('NodeGroupOutput')
    
    # ----------------------------------------------------------------------------------------------------
    # Using stack
    # ----------------------------------------------------------------------------------------------------

    def get_input_node(self):
        if len(self._input_stack):
            return self._input_stack[-1]
        else:
            return self.input_node
        
    def get_output_node(self):
        if len(self._output_stack):
            return self._output_stack[-1]
        else:
            return self.output_node
    
    # ====================================================================================================
    # Get an existing input socket
    # ====================================================================================================

    def get_in_socket(self, name: str, panel: str = ""):
        """ Get an existing socket within a panel

        Arguments
        ---------
        - name (str) : name of the socket
        - panel (str = "") : panel name

        Returns
        -------
        - Socket : None if not found
        """
        parent = self.get_bpanel(panel)
        item = self._interface.get_socket('INPUT', name, parent=parent)

        if item is None:
            raise RuntimeError(f"Socket input socket '{name}' not found in tree '{self._btree.name}'.")

        return self.input_node.socket_by_identifier('OUTPUT', item.identifier)
    

    # ====================================================================================================
    # Link two nodes
    # ====================================================================================================

    def link_nodes(self, from_node, to_node, include=None, exclude=[], create=True, panel=""):
        """ Link two nodes

        If from_node is a Group Input node, the necessary sockets can be created if 'create' argument is True.

        Arguments
        ---------
        - from_node : the node to get the outputs from (i.e. tree Input Node)
        - to_node : the node to plug into
        - include (list = None) : connect only the sockets in the list (or panels)
        - exclude (list = []) : exclude sockets in this list (or panels)
        - create : create tree input sockets  (i.e. node output sockets) in from_node if it is a 'Group Input Node'
        - panel (str = ""): panel name to create, use tree default name if None
        """

        # ----------------------------------------------------------------------------------------------------
        # If from group input, we can use TreeInterface

        if from_node._bnode.bl_idname == 'NodeGroupInput':
            from_interface = from_node._tree._interface
            from_interface.create_from_node(node=to_node._bnode, include=include, exclude=exclude, create=create, input_node=from_node._bnode, panel=panel)
            return

        # ----------------------------------------------------------------------------------------------------
        # We feed from a node which is not a Group Node

        # ----- The available output sockets

        counters = {}
        out_sockets = {}
        for out_socket in from_node._bnode.outputs:
            if not out_socket.enabled:
                continue

            name = out_socket.name if (out_socket.label is None or out_socket.label == "") else out_socket.label
            name = utils.snake_case(name)
            if name in counters:
                rank = counters[name]
                counters[name] += 1
                name += f"_{rank}"
            else:
                rank = 0
                counters[name] = 1

            out_sockets[name] = out_socket

        # ----- Loop on the input sockets

        counters = {}
        for in_socket in to_node._bnode.inputs:
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

            if name not in out_sockets:
                continue

            # ----- In include or exclude

            if (include is not None) and (name not in include):
                continue
            if name in exclude:
                continue

            # ----- We can link

            link = self._btree.links.new(in_socket, out_sockets[name])
            utils.check_link(link)

        utils.check_zones(self._btree)

    # ====================================================================================================
    # Dict of modifiers using this tree
    # ====================================================================================================

    def get_modifiers(self):
        return blender.get_geondes_modifiers(self._btree)

    # =============================================================================================================================
    # Dump content

    def dump(self):
        for bnode in self._btree.nodes:
            print(f"Node '{bnode.name}' ({bnode.bl_idname})")
            print("Inputs")
            for bsock in bnode.inputs:
                print(f"   - {bsock.name:20s} : {bsock.bl_idname}")
            print("Outputs")
            for bsock in bnode.outputs:
                print(f"   - {bsock.name:20s} : {bsock.bl_idname}")
            print()

    def gen_node_headers(self, default_values=True):
        for node in self._btree.nodes:
            if default_values:
                print(f"def FUNCTION(self,", ", ".join([utils.snake_case(sock.name) + f"={sock.default_value}" for sock in node.inputs]))
            else:
                print(f"def FUNCTION(self,", ", ".join([utils.snake_case(sock.name) + "=None" for sock in node.inputs]))

            sockets = ", ".join([f"'{sock.name}': {utils.snake_case(sock.name)}" for sock in node.inputs])
            print(f"Node('{node.name}', " + "{" + sockets + "}")
            print()

