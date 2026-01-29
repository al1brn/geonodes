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
from .colors import SysColor
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
    def __init__(self, name: str, tip: str = "", default_closed: bool = False, create_layout: bool = False):
        """ Socket panel

        All group input and output sockets an panels will be created within the current panel

        Arguments
        ---------
        - name :panel title
        - tip : panel description
        - default_closed : closed by default
        """

        self.tree   = Tree.current_tree()
        self.name   = name
        self.path   = self.tree.get_panel(name)
        self.bpanel = None
        self.create_layout = create_layout

        if self.tree._interface is not None:
            self.bpanel = self.tree._interface.get_panel(self.path, default_closed=default_closed, create=True)
            self.bpanel.description = tip

    def __str__(self):
        return self.path.path

    def push(self):
        self.tree.push_panel(self.path)
        if self.create_layout:
            self.layout = Layout(self.name)
            self.layout.push()

    def pop(self):
        if self.create_layout:
            self.layout.pop()
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
        color = Tree._get_color(value)
        if color.is_none:
            self.bnode.use_custom_color = False
        else:
            self.bnode.use_custom_color = True
            self.bnode.color = color.bcolor

        return


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

    def __init__(self,
            tree_name        : str, 
            tree_type        : str   = 'GeometryNodeTree',
            *,
            fake_user        : bool  = False, 
            is_group         : bool  = False, 
            prefix           : str   = "",
            replace_material : bool  = False):
        
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
        > - it will be replaced if it is a tree scripted with **geonodes**
        > - it will be renamed if it is not the case
        > This avoids to accidentally delete a manually created tree.

        > [!CAUTION]
        > This doesn't work with shaders embedded in a Material. It is why the argument `replace_material` is set to False
        > by default when creating a Shader. Hence, an existing material is not replaced by a geonodes scripts
        > except if you change the default value of `replace_material` argument to True.

        ``` python
        # Create the material if it doesn't exist
        # Do nothing if it already exists
        with ShaderNodes("My Material"):
            pass
            
        # Replace the existing material
        with ShaderNodes("My Material", replace_material=True):
            pass
        ```

        > [!NOTE]
        > `prefix` argument is added at the begining of the name.

        ``` python
        # The two following modifiers have the same name

        with GeoNodes("My Modifier", prefix="Utils"):
            pass
            
        with GeoNodes("Utils My Modifier"):
            pass
        ````

        The `prefix` is usefull for big projects with numerous Groups and when you want the Groups to be sorted by their name.
        You can then use the special class `G` to call the groups as python functions:

        ``` python
        # Prefix
        util = "Util"
        math = "Math"

        # Util Change Shape
        with GeoNodes("Change Shape", prefix=util):
            pass
            
        # Util Rotate
        with GeoNodes("Rotate", prefix=util):
            pass
            
        # Math Multiply
        with GeoNodes("Multiply", prefix=math)
            pass
            
        # Math Divide
        with GeoNodes("Divide", prefix=math)
            pass
            
        # Call the groups
        with GeoNodes("My Modifier"):
            # Call a math group with the special class G
            a = G(math).divide(...)
        ```

        Arguments
        ---------
        - tree_name : tree name
        - tree_type (str in in ('GeometryNodeTree', 'ShaderNodeTree') = 'GeometryNodeTree'): tree type 
        - fake_user (bool = False) : fake user flag
        - is_group (bool = False) : Group or not
        - prefix (str = "") : prefix to add at the begining of the tree name
        - replace_material (bool = False) : replace the existing matertial if True
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

        self.ignore = False

        if tree_type == 'ShaderNodeTree':

            self._material = None
            if not is_group:
                self._material = bpy.data.materials.get(tree_name)

                if self._material is None:
                    self._material = bpy.data.materials.new(tree_name)
                else:
                    if not replace_material:
                        self._material = bpy.data.materials.new("GN TEMP MATERIAL")
                        self.ignore = True

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
        self._kept_nodes = []
        self._nodes      = [] # List of nodes
        self._mod_vals   = {} # To restore modifiers values when necessary (menus)

        # ---------------------------------------------------------------------------
        # Clear / Keep the tree
        # ---------------------------------------------------------------------------

        # Store the current value of each input socket
        if tree_type == 'GeometryNodeTree' or self._is_group:
            for bnode in self._btree.nodes:
                if bnode.bl_idname != 'NodeGroupInput':
                    continue

                for name, mod in self.get_modifiers().items():
                    values = {}
                    for bsock in bnode.outputs:
                        values[(bsock.name, bsock.bl_idname)] = mod.get(bsock.identifier)
                    self._mod_vals[name] = values

                break

        # Clear tree
        self.clear(keep_nodes=False)

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
        # ---------------------------------------------------------------------------
        # Ignore changes
        # ---------------------------------------------------------------------------

        if self.ignore:
            print(f"CHANGES IGNORED : Material '{self._btree.name}' already exists. Use 'replace_material=True' to overwite it.")

            assert self._btree.bl_idname == 'ShaderNodeTree'
            assert self._material is not None

            bpy.data.materials.remove(self._material)
            self._btree = None

            return
        
        # ---------------------------------------------------------------------------
        # Finalize
        # ---------------------------------------------------------------------------

        # Remove kept nodes
        for bnode in self._kept_nodes:
            self._btree.nodes.remove(bnode)

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

                    if False: # True for DEBUG
                        continue

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
        if self._btree.bl_idname == 'ShaderNodeTree' and self._material is not None:
            name = f"Material '{self._material.name}'"
        else:
            name = f"Tree '{self._btree.name}'"
        
        print(f"{name} built: {self._str_stats}, warnings: {warnings}")

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

    def clear(self, keep_nodes: bool = True):
        """ Clear the content of the Tree.

        Remove all the nodes in the Tree.
        """
        self._nodes.clear()

        # Keep menu switch nodes to preserver input links
        # They will be deleted at the end

        if keep_nodes:
            del_nodes = []
            self._kept_nodes = []
            for bnode in self._btree.nodes:
                if bnode.bl_idname in ['GeometryNodeMenuSwitch', 'NodeGroupInput']:
                    self._kept_nodes.append(bnode)
                else:
                    del_nodes.append(bnode)

            for bnode in del_nodes:
                self._btree.nodes.remove(bnode)

        else:
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
    def _get_color(value):

        if value is None:
            rng = Tree.current_tree()._rng
            value = tuple(rng.uniform(0., .7, 3))

        elif isinstance(value, str):
            if value in ['OP', 'OPERATION']:
                value = (.406, .541, .608)
            elif value == 'MACRO':
                value = (.261, .963, .409)
            elif value == 'AUTO_GEN':
                value = (.583, .229, .963)
            elif value == 'WARNING':
                value = (.949, .574, .119)
            else:
                return SysColor(value)
            
        return SysColor(value)

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

            if node._bnode.bl_idname in (
                'NodeGroupInput', 'GeometryNodeWarning',
                'GeometryNodeGizmoDial', 'GeometryNodeGizmoLinear', 'GeometryNodeGizmoTransform',
                ):
                continue

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
                    if bsock.name in ["Skip"]:
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
            #node._bnode.label = f"DEAD END {i + 1}"
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

            for i, (node, names) in enumerate(unlinkeds):
                node._bnode.label = f"UPDATE MISSING {i + 1}"
                utils.set_node_warning(node._bnode)

                print()
                print(node)
                #node._bnode.label = f"DEAD END {i + 1}"
                print("Unlinked sockets:", names)
                if node._stack is not None:
                    print(tab + tab.join(node._stack[1:]))

        # Total number of warnings

        return len(dead_ends) + len(unlinkeds)
    
    # ====================================================================================================
    # Create a method calling this Group
    # ====================================================================================================

    def add_method(self, 
        target_class    : type, 
        func_name       : str = None,
        self_attr       : str = None, 
        ret_class       : type = None, 
        **fixed):
        """ Add a method calling the Group.

        Arguments
        ---------
        - target_class (type) : class to add the method to
        - func_name (str = None) : name of the method to create (snae case version of group name if None)
        - self_attr (str = None) : self name attribute name
        - ret_class (type = None) : class to use to transtype the output socket
        - fixed (dict) : fixed values for sockets        
        """
        from .nodeclass import Group

        group_name = self._btree.name
        if self._prefix != "":
            group_name = group_name[len(self._prefix) + 1:]

        Group.add_method(group_name, target_class,
            func_name       = func_name,
            self_attr       = self_attr, 
            ret_class       = ret_class, 
            prefix          = self._prefix,
            **fixed)

    
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

