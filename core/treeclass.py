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
    def __init__(self, title: str = "", color: str = None, node = None):
        """ Node Frame

        All nodes created when a Layout is open are placed in this layout.
        If the 'color' argument is None, a random color is used

        If the node argument is None, the layout parent is the current layout, otherwise,
        the layout becomes the parent of the node and the previous parent of the node
        becomes the layout parent.

        ``` python
        with GeoNodes("Layout Demo"):

            with Layout("Some maths"):
                a = Integer(1) + 1

            geo = Mesh()
            geo.points.offset = (0, 0, a)

            geo.out()
        ```

        Arguments
        ---------
        - title (str = "") : Layout title
        - color (blender color = None) : Layout color (randomly generated if None)
        - node (Node = None) : the layout is inserted as direct parent of the node
        """

        self.tree  = Tree.current_tree()
        self.bnode = self.tree._btree.nodes.new('NodeFrame')
        self.bnode.select = False
        self.transparent = title is None
        if not self.transparent:
            self.title = title

        self.color = self.tree._get_color(color)

        # Parent from the stack
        if len(self.tree._layouts):
            self.bnode.parent = self.tree._layouts[-1].bnode

        # There is a node to become the parent of
        if node is not None:

            # The node parent can override the current parent
            if node._bnode.parent is not None:
                self.bnode.parent = node._bnode.parent

            # Include the node
            self.include_node(node)

    def __str__(self):
        nodes = [n for n in self.tree._nodes if n._bnode.parent == self.bnode]
        return f"<Layout '{self.title}', {len(nodes)} nodes>"

    # ====================================================================================================
    # Include a node
    # ====================================================================================================

    def include_node(self, node):
        if node._bnode.bl_idname not in ('NodeGroupOutput',):
            if self.transparent:
                node._bnode.parent = self.bnode.parent
            else:
                node._bnode.parent = self.bnode

    # ====================================================================================================
    # Title / color
    # ====================================================================================================

    @property
    def title(self):
        return self.bnode.label
    
    @title.setter
    def title(self, value):
        if value is not None:
            self.bnode.label = value

    @property
    def color(self):
        return self.bnode.color
    
    @color.setter
    def color(self, value):
        if value is None:
            self.bnode.use_custom_color = False
        else:
            if isinstance(value, str):
                value = Tree._get_color(value)

            self.bnode.use_custom_color = True
            self.bnode.color = value

    # ====================================================================================================
    # Context
    # ====================================================================================================

    def push(self):
        self.tree._layouts.append(self)

    def pop(self):
        assert self.tree._layouts.pop() == self, f"Shouldn't happen with Layout '{self.title}'"

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

        self._panels  = [ItemPath(None)]
        self._layouts = []

        # Input / output socket creation are performed by node with dynamic
        # sockets (either with items or with tree_node)
        # By default, these are input_node and output_node
        # This behavior can be overloaded using input and output stacks
        
        self._output_stack  = []
        self._input_stack   = []

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
        self._nodes = []    # List of nodes
        self._mod_vals = {} # To restore modifiers values when necessary (menus)


        # ---------------------------------------------------------------------------
        # Clear the tree
        # ---------------------------------------------------------------------------

        if clear:

            # Store the current value of each input socket
            if tree_type == 'GeometryNodeTree' or self._is_group:
                for bnode in self._btree.nodes:
                    if bnode.bl_idname != 'NodeGroupInput':
                        continue

                    for name, mod in blender.get_geonodes_modifiers(self._btree).items():
                        values = {}
                        for bsock in bnode.outputs:
                            values[(bsock.name, bsock.bl_idname)] = mod.get(bsock.identifier)
                        self._mod_vals[name] = values

                    break

            # Clear
            self.clear()

        # ---------------------------------------------------------------------------
        # Interface
        # ---------------------------------------------------------------------------

        self._interface = None
        if self._is_group or tree_type == 'GeometryNodeTree':
            self._interface = TreeInterface(self._btree)
            self._interface.clear(use_bin=True)

        # ---------------------------------------------------------------------------
        # Random generator for random colors
        # ---------------------------------------------------------------------------

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

    def pop(self, error=False):
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

        # Adjust menu inputs
        if self._has_tree and not error:
            for node in self._nodes:
                if '_default_menu' in node.__slots__:
                    node._tree_is_completed(self._mod_vals)

            innode = self.input_node
            for bsock in innode._bnode.outputs:
                if bsock.type != 'MENU' or not bsock.is_linked:
                    continue
                isock = self._interface.by_identifier(bsock.identifier)
                enums = list(utils.get_enums(isock, 'default_value'))
                if not len(enums):
                    continue

                for mod in self.get_modifiers().values():
                    cur_val = mod.get(bsock.identifier)
                    if cur_val is not None and (cur_val < 2 or cur_val > len(enums) + 2):
                        mod[bsock.identifier] = enums.index(isock.default_value) + 2


        # Check dead ends
        warnings = 0
        if not error:
            warnings = self.check_warnings()

        # Remove from stack
        tree = Tree.TREE_STACK.pop()
        if tree != self:
            raise RuntimeError(f"Error in tree stack management")

        # Empty the interface bin
        if (not error) and self._interface is not None:
            self._interface.empty_bin()

        # Last node in error
        if error and len(self._nodes):
            for node in reversed(self._nodes):
                if node._bnode.bl_idname in ['NodeGroupOutput', 'NodeGroupInput']:
                    continue
                utils.set_node_error(node._bnode)
                break

        # Arrange the nodes
        self.arrange()

        # Stats
        print(f"Tree '{self._btree.name}' built: {self._str_stats}, warnings: {warnings}")

        Tree._total_nodes += len(self._btree.nodes)
        Tree._total_links += len(self._btree.links)        

    # ----------------------------------------------------------------------------------------------------
    # Context management
    # ----------------------------------------------------------------------------------------------------

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, type, exc_value, traceback):

        ok = exc_value is None or isinstance(exc_value, Break)

        self.pop(not ok)

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
        if len(self._layouts):
            self._layouts[-1].include_node(node)

        node._stack = NodeError.stack_lines()

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
        def_val = props.get('default_value')
        if def_val is not None:
            try:
                utils.get_bsocket(socket).default_value = def_val
            except Exception as e:
                print(f"WARNING Tree.create_input_socket: {str(e)}")

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
                return utils.value_to_color(name)
                #raise Exception(f"Non referenced color", name)
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

        return link

    # ====================================================================================================
    # Tree Input / Output
    # ====================================================================================================

    @property
    def _has_tree(self):
        if self.is_geonodes():
            return True
        elif self.is_shader():
            return self._is_group 

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
    # Dict of modifiers using this tree
    # ====================================================================================================

    def get_modifiers(self):
        return blender.get_geonodes_modifiers(self._btree)
    
    # ====================================================================================================
    # Check warnings
    # ====================================================================================================

    def check_warnings(self):

        from .nodezone import ZoneNode

        tab = "\n   | " 
        
        count = 0

        dead_ends = []
        unlinkeds = []

        for node in self._nodes:

            # ---------------------------------------------------------------------------
            # Dead ends
            # ---------------------------------------------------------------------------

            is_linked = False
            n = 0
            for bsock in node._bnode.outputs:
                if bsock.is_linked:
                    is_linked = True
                    break
                n += 1

            if not is_linked and n > 0:
                dead_ends.append((node))

            # ---------------------------------------------------------------------------
            # Unlinked zone output nodes
            # ---------------------------------------------------------------------------

            if isinstance(node, ZoneNode):
                unlinked = []
                for bsock in node._bnode.inputs:
                    if bsock.type == 'CUSTOM':
                        continue
                    if not bsock.is_linked:
                        unlinked.append(bsock.name)

                if len(unlinked):
                    unlinkeds.append((node, unlinked))

        # ---------------------------------------------------------------------------
        # Display
        # ---------------------------------------------------------------------------

        if len(dead_ends):
            print()
            print("-"*100)
            print(f"The following node{' is' if len(dead_ends) == 1 else 's are'} not connected")

        for i, node in enumerate(dead_ends):
            node._bnode.label = f"DEAD END {i + 1}"
            utils.set_node_warning(node._bnode)

            print()
            print(node)
            if node._stack is not None:
                print(tab + tab.join(node._stack[1:]))

        if len(unlinkeds):
            print()
            print("-"*100)
            print(f"The output node of the following zone{' is' if len(unlinkeds) == 1 else 's are'} missing input links.")
            print("The variables uses in the loop are not updated.")
            print()
            print("="*50)
            print("# Example with no warning:")
            print("geo = Geometry()")
            print("for rep in geo.repeat(10, value=1.):")
            print("    a = rep.value + 1")
            print("    rep.value = a    # Update value" )
            print("    geo.out()        # Update geometry")            
            print("geo.out() # Simulated geometry to Group output")
            print()
            print("# Raises warnings for 'value' and 'geometry' sockets")
            print("for rep in geo.repeat(10, value=1.):")
            print("    pass")
            print("="*50)

            for i, (node, names) in enumerate(unlinkeds):
                node._bnode.label = f"UPDATE MISSING {i + 1}"
                utils.set_node_warning(node._bnode)

                print()
                print(node)
                print("Unlinked sockets:", names)
                if node._stack is not None:
                    print(tab + tab.join(node._stack[1:]))

        # Total number of warnings

        return len(dead_ends) + len(unlinkeds)
    
    # ====================================================================================================
    # Dump content
    # ====================================================================================================


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

