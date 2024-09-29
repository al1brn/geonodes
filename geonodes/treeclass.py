#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : treeclass
------------------
Provides the two major classes:
- Tree: the tree currently edited
- Node: base class to create a node

Note that to ease the scripting, nodes are created without refering explicity to a tree,
but get the tree in a stack of trees as the 'current tree'.

This allows the syntax:

```python
my_node = Node(...)
````

rather than:
``` python
my_node = tree.Node(...)
```

Pushing and poping the stack of tree is made with context management:

``` python
with Tree("Geometry Nodes"):
    my_node = Node(...)

# The following line raises an error:
node_error = Node(...)
```

classes
-------
- Break         : Exit from with block
- Layout        : Creates a Frame where the new nodes are placed into
- Tree          : The tree to build
- Node          : Node creation in the current Tree and Layout
- Group         : Node Group creation
- GroupF        : Utility class to call a group with python syntax

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import numpy as np
import bpy
from time import time

from .scripterror import NodeError
from . import treearrange
from . import constants
from . import utils

# =============================================================================================================================
# Break to exit with blocks

class Break(Exception):
    """ Exception used to exit a With context block.

    ``` python
    with GeoNodes("Break Demo"):
        Geometry().out()
        raise Break()

        # Not executed
        Float(10).out()
    ```
    """
    pass

# =============================================================================================================================
# Layout

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

        self.tree  = Tree.current_tree
        self.frame = Node('Frame')
        self.frame._label = label
        self.frame._color = self.tree._get_color(color)

        self.push()

    def push(self):
        self.tree._layouts.append(self.frame._bnode)

    def pop(self):
        self.tree._layouts.pop()

    def __enter__(self):
        return self

    def __exit__(self, type, exc_value, traceback):
        self.pop()

        if isinstance(exc_value, Break):
            return True


# =============================================================================================================================
# Tree

class Tree:

    STACK   = []

    _total_nodes = 0
    _total_links = 0
    _total_time  = 0.

    def __init__(self, tree_name, tree_type='GeometryNodeTree', clear=True, fake_user=False, is_group=False, prefix=None):
        """ Root class for <!GeoNodes> and <!ShaderNodes> trees.

        The system manages a stack of Trees. When a Tree is created, it is placed at the top of the stack
        and becomes the current tree.
        The Tree is poped from the stack with the method <#pop>.

        Better use the context management syntax:

        ``` python
        with GeoNodes("My Tree"):

            # Get the current tree
            tree = Tree.current_tree

            pass

        # Returns None
        tree = Tree.current_tree
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

        Arguments
        ---------
        - tree_name (str) : tree name
        - tree_type (str = 'GeometryNodeTree') : tree type in ('GeometryNodeTree', 'ShaderNodeTree')
        - clear (bool = True) : clear the current tree
        - fake_user (bool = False) : fake user flag
        - is_group (bool = False) : Group or not
        - prefix (str=None) : str prefix to add at the beging of the tree name
        """

        if prefix is not None:
            tree_name = f"{prefix} {tree_name}"

        self._btree = None

        # ----------------------------------------------------------------------------------------------------
        # Shader Node tree is a property of the Material

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

        if self._btree is None:
            self._btree = utils.get_tree(tree_name, tree_type=tree_type, create=True)
            self._btree.use_fake_user = fake_user

        self._is_group = is_group

        # ----- Management lists

        self._nodes   = []
        self._keeps   = {}
        self._layouts = []

        if clear:
            self.clear()

        # ----- Random generator for random colors

        self._rng = np.random.default_rng(0)

        # ----- Becomes the current tree

        self.push()

    # =============================================================================================================================
    # Remove node groups

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
    # Access to the blender tree

    @classmethod
    @property
    def current_tree(cls):
        """ > Get the Current Tree.

        Returns None if no Tree is currently open

        Returns
        -------
        - Tree : current tree
        """

        if not cls.STACK:
            #raise NodeError(f"No tree is open")
            #print("CAUTION: not tree is open")
            return None
        return cls.STACK[-1]

    # ====================================================================================================
    # Some methods

    def __str__(self):
        return f"<Tree '{self._btree.name}' ({type(self).__name__}): {len(self._btree.nodes)} nodes and {len(self._btree.links)} links>"

    @classmethod
    def _reset_counters(cls):
        cls._total_nodes = 0
        cls._total_links = 0
        cls._total_time  = 0.

    @classmethod
    def _display_counter(cls, title):
        print(f"{title}: {Tree._total_nodes} nodes, {Tree._total_links} links in {Tree._total_time:.1f} s")

    @classmethod
    @property
    def is_geonodes(cls):
        """ > Current Tree is Geometry Nodes.

        Returns
        -------
        - True if Tree is GeoNodes, False otherwise
        """

        return cls.current_tree._btree.bl_idname == 'GeometryNodeTree'

    @classmethod
    @property
    def is_shader(cls):
        """ > Current Tree is Shader Nodes.

        Returns
        -------
        - True if Tree is ShaderNodes, False otherwise
        """

        return cls.current_tree._btree.bl_idname == 'ShaderNodeTree'

    @classmethod
    @property
    def is_compositor(cls):
        return cls.current_tree._btree.bl_idname == 'CompositorNodeTree'

    @property
    def _str_stats(self):
        return f"{len(self._btree.nodes)} nodes, {len(self._btree.links)} links"

    def clear(self):
        """ Clear the content of the Tree.

        Remove all the nodes in the Tree.
        """

        to_clear = []
        self._keeps.clear()
        self._nodes.clear()
        for bnode in self._btree.nodes:
            if bnode.label is not None and bnode.label[:4] == 'KEEP':
                self._keeps[bnode.bl_idname + '-' + bnode.label[5:]] = bnode
            else:
                to_clear.append(bnode)

        self._btree.links.clear()
        for bnode in to_clear:
            self._btree.nodes.remove(bnode)

    def register_node(self, node):
        self._nodes.append(node)
        if len(self._layouts):
            node._bnode.parent = self._layouts[-1]
        return node

    # ----------------------------------------------------------------------------------------------------
    # Context manager

    def push(self):
        """ > Make this tree the current one

        > [!IMPORTANT]
        > This methods shouldn't be called directly, better use a **with** context block.

        ``` python
        with Tree("My Name"):
            pass
        ```
        """
        Tree.STACK.append(self)
        self._start_time = time()

    def pop(self):
        """ > Remove this tree from the stack

        > [!IMPORTANT]
        > This methods shouldn't be called directly, better use a **with** context block.

        Calls <#arrange> to arrange the location of the nodes.

        Raises
        ------
        - NodeError : if this tree is not the current one

        ``` python
        with Tree("My Name"):
            pass
        ```
        """
        tree = Tree.STACK.pop()
        if tree != self:
            raise NodeError(f"Error in tree stack management")

        self.arrange()

        # ----- Stats

        duration = time() - self._start_time

        print(f"Tree '{self._btree.name}' built: {self._str_stats} in {duration:.1f} s")

        Tree._total_nodes += len(self._btree.nodes)
        Tree._total_links += len(self._btree.links)
        Tree._total_time  += duration

    def __enter__(self):
        return self

    def __exit__(self, type, exc_value, traceback):

        self.pop()

        if isinstance(exc_value, Break):
            return True

    # =============================================================================================================================
    # Arranges nodes

    def arrange(self):
        """ > Arrange the nodes in the editor.

        Try to arrange properly the nodes from left to right.

        This method is called when the Tree is poped from the stack.

        Returns
        -------
        - None
        """

        treearrange.arrange(self._btree)

    # =============================================================================================================================
    # Node colors

    @staticmethod
    def _get_color(name):
        rng = Tree.current_tree._rng
        if name is None:
            return tuple(rng.uniform(0., .7, 3))
        elif isinstance(name, str):
            if name in ['OP', 'OPERATION']:
                return (.406, .541, .608)
            elif name == 'KEEP':
                return (.324, .147, .159)
            elif name == 'MACRO':
                return (.261, .963, .409)
            elif name == 'AUTO_GEN':
                return (.583, .229, .963)
            else:
                raise Exception(f"Non referenced color", name)
        else:
            return name

    # =============================================================================================================================
    # Create a link

    def link(self, out_socket, in_socket):
        """ > Create a link between two sockets.

        Arguments
        ---------
        - out_socket (socket) : a node output socket
        - in_socket (socket) : input socket from another node

        Returns
        -------
        - Link
        """

        if hasattr(out_socket, '_bsocket'):
            out_socket = out_socket._bsocket

        if hasattr(in_socket, '_bsocket'):
            in_socket = in_socket._bsocket

        return self._btree.links.new(out_socket, in_socket)

    # =============================================================================================================================
    # Tree Input / Output

    @property
    def input_node(self):
        """ > Return a <&Node Group Input> node

        If the node doesn't already exist, it is created.

        Returns
        -------
        - Node
        """

        for node in self._nodes:
            if node._bnode.bl_idname ==  'NodeGroupInput':
                return node
        return Node('NodeGroupInput')

    @property
    def output_node(self):
        """ Returns a <&Node Group Output> node

        If the node doesn't already exist, it is created.

        Returns
        -------
        - Node
        """

        for node in self._nodes:
            if node._bnode.bl_idname ==  'NodeGroupOutput':
                return node
        return Node('NodeGroupOutput')

    # ----------------------------------------------------------------------------------------------------
    # Check if an interface socket exists

    def io_socket_exists(self, bl_idname, in_out='INPUT', name=None):

        for item in self._btree.interface.items_tree:
            if item.item_type != 'SOCKET' or item.in_out != in_out or item.socket_type != bl_idname:
                continue
            if name is None or (item.name == name) or (item.identifier == name):
                return item

        return None

    # ----------------------------------------------------------------------------------------------------
    # First socket type

    def first_io_socket_is_geometry(self, in_out='INPUT'):

        for item in self._btree.interface.items_tree:
            if item.item_type != 'SOCKET' or item.in_out != in_out:
                continue
            return item.socket_type == 'NodeSocketGeometry'

        return False

    # ----------------------------------------------------------------------------------------------------
    # Create an new interface socket

    def new_io_socket(self, bl_idname, in_out, name):
        return self._btree.interface.new_socket(name=name, in_out=in_out, socket_type=bl_idname)

    # --------------------------------------------------------------------------------
    # Clear interface

    def clear_io_sockets(self):
        self._btree.interface.clear()

    # --------------------------------------------------------------------------------
    # Set the default value of an input socket

    def set_input_socket_default(self, socket, value=None):
        if value is None:
            return

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            return

        try:
            bsocket.default_value = value
        except:
            return

        io_socket = self.io_socket_exists(bsocket.bl_idname, in_out='INPUT', name=bsocket.identifier)
        if io_socket is None:
            return

        if not hasattr(io_socket, 'default_value'):
            return

        try:
            io_socket.default_value = value
        except:
            return

    # --------------------------------------------------------------------------------
    # Create a new input socket

    @classmethod
    def new_input(cls, bl_idname, name, subtype='NONE',
                  value = None, min_value = None, max_value = None, description = ""):
        """ Create a new input socket.

        This is an **input socket** of the Tree, hence an **output socket** of the <&Group Input> node.

        Arguments
        ---------
            - bl_idname (str) : socket bl_idname
            - name (str) : Socket name
            - value (any = None) : Default value
            - min_value (any = None) : Minimum value
            - max_value (any = None) : Maxium value
            - description (str = None) : user tip

        Returns
        -------
            Socket
        """

        tree = cls.current_tree

        # ----- Input node

        input_node = tree.input_node

        # ----------------------------------------------------------------------------------------------------
        # Get or create

        io_socket = tree.io_socket_exists(bl_idname, 'INPUT', name)

        if io_socket is None:
            io_socket = tree.new_io_socket(bl_idname, 'INPUT', name)
            set_value = True
        else:
            set_value = False

        if hasattr(io_socket, 'subtype'):
            io_socket.subtype = subtype

        out_socket = tree.input_node[io_socket.identifier]

        # ----------------------------------------------------------------------------------------------------
        # Attributes

        if description is not None:
            io_socket.description = description

        if min_value is not None and hasattr(io_socket, 'min_value'):
            io_socket.min_value = min_value

        if max_value is not None and hasattr(io_socket, 'max_value'):
            io_socket.max_value = max_value

        # ----------------------------------------------------------------------------------------------------
        # Let's set the value if the socket is created
        # Note: if the socket already exists, we don't override its value

        def_value = utils.python_value_for_socket(value, utils.get_socket_type(out_socket))
        if (def_value is not None):

            try:
                io_socket.default_value = def_value
            except Exception as e:
                raise NodeError(f"Impossible to set the default value {value} <{def_value}> to io_socket of type '{bl_idname}'", error_message=str(e))

            try:
                out_socket._bsocket.default_value = def_value
            except Exception as e:
                raise NodeError(f"Impossible to set the default value {value} <{def_value}> to socket of type '{out_socket.SOCKET_TYPE}'", error_message=str(e))

            # ---------------------------------------------------------------------------
            # Set the default value to all modifiers using it

            if set_value:
                for obj in bpy.data.objects:
                    for mod in obj.modifiers:
                        if isinstance(mod, bpy.types.NodesModifier):
                            if mod.node_group == tree._btree:
                                try:
                                    mod[io_socket.identifier] = def_value
                                except:
                                    raise NodeError(f"Impossible to set the default value {value} <{def_value}> to existing modifier socket '{io_socket.identifier}', socket type: '{out_socket.SOCKET_TYPE}'", error_message=str(e))

        return out_socket

    # --------------------------------------------------------------------------------
    # Create a new output socket

    def new_output(self, bl_idname, name):
        """ Create a new output socket.

        This is an **output socket** of the Tree, hence an input socket of the <&Group Output> node.

        Arguments
        ---------
            - bl_idname (str) : socket bl_idname
            - name (str) : Socket name

        Returns
        -------
            Socket
        """

        # ----- Input node

        output_node = self.output_node

        # ----------------------------------------------------------------------------------------------------
        # Get or create

        io_socket = self.io_socket_exists(bl_idname, 'OUTPUT', name)

        if io_socket is None:
            io_socket = self.new_io_socket(bl_idname, 'OUTPUT', name)

        return output_node._bnode.inputs[io_socket.identifier]

    # --------------------------------------------------------------------------------
    # Create a new input socket from an existing node input socket

    @classmethod
    def new_input_from_input_socket(cls, input_socket, name=None):
        """ Create a new group input socket from an existing input socket.

        Arguments
        ---------
        - input_socket (socket) : a node input _insocket
        - name (str = None) : name of the group input socket to create

        Returns
        -------
        - Socket
        """

        tree = Tree.current_tree

        bsocket = utils.get_bsocket(input_socket)
        if name is None:
            name = bsocket.name

        bl_idname, subtype = constants.SOCKET_SUBTYPES[bsocket.bl_idname]

        io_socket = tree.new_io_socket(bl_idname, 'INPUT', name)
        if hasattr(io_socket, 'subtype'):
            io_socket.subtype = subtype

        io_socket.default_value = bsocket.default_value
        io_socket.description   = bsocket.description

        # ----- Min and Max values are attributes of default property

        if 'default_value' in bsocket.bl_rna.properties:
            default_prop = bsocket.bl_rna.properties['default_value']
            if hasattr(io_socket, 'min_value'):
                io_socket.min_value = default_prop.hard_min
                io_socket.max_value = default_prop.hard_max

        return tree.input_node[io_socket.identifier]

    # =============================================================================================================================
    # Create a node which contains a python value

    @staticmethod
    def get_data_socket_class(socket_type):

        from geonodes.geonodes import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, String, Menu

        socket_class = {'BOOLEAN': Boolean, 'INT': Integer, 'VALUE': Float, 'VECTOR': Vector, 'ROTATION': Rotation, 'MATRIX': Matrix, 'RGBA': Color,
            'STRING': String, 'MENU': Menu,
                'GEOMETRY': Geometry,
                'MATERIAL': Material, 'IMAGE': Image, 'OBJECT': Object, 'COLLECTION': Collection,
            }.get(socket_type, None)

        if socket_class is None:
            raise NodeError(f"No socket class is implemented for socket°type '{socket_type}'")
        else:
            return socket_class

    @classmethod
    def value_to_socket(cls, value):

        if value is None:
            return None
        return Tree.get_data_socket_class(utils.get_socket_type(value))(value)

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
                print(f"def FUNCTION(self,", ", ".join([utils.socket_name(sock.name) + f"={sock.default_value}" for sock in node.inputs]))
            else:
                print(f"def FUNCTION(self,", ", ".join([utils.socket_name(sock.name) + "=None" for sock in node.inputs]))

            sockets = ", ".join([f"'{sock.name}': {utils.socket_name(sock.name)}" for sock in node.inputs])
            print(f"Node('{node.name}', " + "{" + sockets + "}")
            print()


# =============================================================================================================================
# Node

class Node:
    def __init__(self, node_name, sockets={}, _items={}, _keep=None, **parameters):
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
        - **kwargs : node parameters initialization
        """

        # ----------------------------------------------------------------------------------------------------
        # Create the Node

        self._tree = Tree.current_tree
        btree = self._tree._btree
        tree_type = btree.bl_idname

        lower_name = node_name.lower()
        if lower_name in constants.NODE_NAMES[tree_type]:
            bl_idname = constants.NODE_NAMES[tree_type][lower_name]
        else:
            for tt in constants.NODE_NAMES.keys():
                if tt == tree_type:
                    continue
                if lower_name in constants.NODE_NAMES[tt]:
                    raise NodeError(f"Node '{node_name}' is a node of tree '{tt}', it doesn't exit for tree '{tree_type}'")

            bl_idname = node_name

        # ----------------------------------------------------------------------------------------------------
        # Node keeping

        keeped_node = None
        if _keep is not None:
            keep_key = bl_idname + '-' + _keep
            keeped_node = self._tree._keeps.get(keep_key)
            self._tree._keeps[keep_key] = None

        # ----- We create it or reuse it

        if keeped_node is None:
            self._bnode = btree.nodes.new(type=bl_idname)
            self._bnode.select = False
        else:
            self._bnode = keeped_node

        # ----- Let's keep it for next time

        if _keep is not None:
            self._label = "KEEP " + _keep
            self._color = Tree._get_color('KEEP')

        # ----------------------------------------------------------------------------------------------------
        # Node setup

        # Parameters first to configure the sockets

        self.set_parameters(**parameters)

        # Dynamic sockets

        self._set_items(_items)

        # Plug the sockets

        self.set_input_sockets(sockets)

        # ----------------------------------------------------------------------------------------------------
        # Register the node

        self._tree.register_node(self)

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

    # ----------------------------------------------------------------------------------------------------
    # Dynamic nodes have a property xxx_items and a property active_item

    @property
    def _has_items(self):
        return 'active_item' in dir(self._bnode)

    @property
    def _items(self):
        if self._has_items:
            for name in dir(self._bnode):
                if name[-6:] == '_items':
                    return getattr(self._bnode, name)
            raise NodeError(f"Node '{self._bnode.name}' has no items !")
        else:
            return None

    def _set_items(self, _items={}, clear=True, **kwargs):
        if len(_items) == 0 and len(kwargs) == 0:
            return

        if not self._has_items:
            raise NodeError(f"Error when initializing node '{self._bnode.name}: this node has no items. Impossible to create the sockets.",
                _items=_items)

        all_items = {**_items, **kwargs}

        node_items = self._items
        if clear:
            node_items.clear()

        for socket_name, socket_value in all_items.items():

            # ----- Create

            # 'new' method takes only one argument
            if self._bnode.bl_idname in ['GeometryNodeMenuSwitch']:
                sck = node_items.new(socket_name)

            # 'new' method takes two arguments
            else:
                input_type = 'GEOMETRY' if socket_value is None else utils.get_input_type(socket_value)
                sck = node_items.new(input_type, socket_name)

            # ----- Plug

            self.plug_value_into_socket(socket_value, self.in_socket(sck.name))

    # ----------------------------------------------------------------------------------------------------
    # Create a Socket from an output Blender NodeSocket

    @staticmethod
    def data_socket(bsocket):

        socket_type = bsocket.type

        if Tree.is_geonodes:
            #from .geonodes import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, Texture, String, Menu
            #from .geonodes import Mesh, Curve, Cloud, Volume, Instances
            from . import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, Texture, String, Menu
            from . import Mesh, Curve, Cloud, Volume, Instances

            socket_class = {'BOOLEAN': Boolean, 'INT': Integer, 'VALUE': Float, 'VECTOR': Vector, 'ROTATION': Rotation, 'MATRIX': Matrix, 'RGBA': Color,
                'STRING': String, 'MENU': Menu,
                    'GEOMETRY': Geometry,
                    'MATERIAL': Material, 'IMAGE': Image, 'OBJECT': Object, 'COLLECTION': Collection, 'TEXTURE': Texture,
                }[socket_type]

            if socket_type == 'GEOMETRY':
                socket_name = bsocket.name.lower()
                if socket_name == 'mesh':
                    return Mesh(bsocket)
                elif socket_name in ['curve', 'curves']:
                    return Curve(bsocket)
                elif socket_name in ['instance', 'instances']:
                    return Instances(bsocket)
                elif socket_name in ['points', 'point cloud']:
                    return Cloud(bsocket)
                elif socket_name == 'volume':
                    return Volume(bsocket)

        elif Tree.is_shader:
            from geonodes import Float, Vector, Color, String, Shader

            socket_class = {'VALUE': Float, 'VECTOR': Vector, 'RGBA': Color, 'STRING': String, 'SHADER': Shader,
                }[socket_type]

        else:
            raise Exception("Not normal")

        return socket_class(bsocket)

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

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its index, identifier or name

    def inout_socket(self, name, bsockets, halt):

        if isinstance(name, int):
            return bsockets[name]

        disabled_bsocket = None
        bsocket = None
        for bsock in bsockets:
            if name in [bsock.name, bsock.identifier, utils.socket_name(bsock.name)]:
                if bsock.enabled:
                    bsocket = bsock
                    break
                else:
                    disabled_bsocket = bsock

        if bsocket is None:
            bsocket = disabled_bsocket

        if halt and bsocket is None:
            valids = [f"{'x' if sock.enabled else 'o'} {sock.name}" for sock in bsockets]
            if disabled_bsocket is None:
                raise NodeError(f"Socket name '{name}' not found in node '{self._bnode.name}' ({self._bnode.bl_idname})", valids=valids)
            else:
                raise NodeError(f"Socket name '{name}' is disabled in node '{self._bnode.name}' ({self._bnode.bl_idname})", valids=valids)

        return bsocket

    def in_socket(self, name, halt=True):
        return self.inout_socket(name, self._bnode.inputs, halt=halt)

    def out_socket(self, name, halt=True):
        return self.data_socket(self.inout_socket(name, self._bnode.outputs, halt=halt))

    # ----------------------------------------------------------------------------------------------------
    # Set the node sockets

    def set_input_sockets(self, sockets={}):

        # ----- Sockets is a list --> let's transform into a dict

        if isinstance(sockets, list):
            sockets = {i: value for i, value in enumerate(sockets)}

        for socket_name, socket_value in sockets.items():

            if socket_value is None:
                continue

            in_socket = self.in_socket(socket_name)
            self.plug_value_into_socket(socket_value, in_socket)

    # ----------------------------------------------------------------------------------------------------
    # Set an input socket and Get an output socket

    def __getitem__(self, name):
        return self.out_socket(name)

    def __setitem__(self, name, value):
        self.plug_value_into_socket(value, self.in_socket(name))

    @property
    def _out(self):
        """ Returns the first enabled output socket.

        Returns
        -------
        - Socket : first enabled output socket
        """

        for bsock in self._bnode.outputs:
            if bsock.enabled:
                return self.data_socket(bsock)
        return None

    # ====================================================================================================
    # Read a node attribute : it is an output socket

    def __getattr__(self, name):
        if '_bnode' in self.__dict__:
            out_socket = self.out_socket(name)
            if out_socket is None:
                raise AttributeError(f"Node parameter '{name}' not found in '{self.__dict__['_bnode'].name}'.")
            else:
                return out_socket

        raise AttributeError(f"Node parameter '{name}' not found.")

    def __setattr__(self, name, value):

        if name in ['_tree', '_bnode', '_label', '_color']:
            super().__setattr__(name, value)
            return

        sbnode = ''
        if '_bnode' in self.__dict__:

            # ----- Set parameter

            bnode = self.__dict__['_bnode']
            sbnode = bnode.name
            if hasattr(bnode, name):
                setattr(bnode, name, value)
                return

            # ---- Link input node

            in_socket = self.in_socket(name)
            if in_socket is not None:
                self.plug_value_into_socket(value, in_socket)
                return

        raise AttributeError(f"Node parameter '{name}' not found in '{sbnode}'.")

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

        if isinstance(value, int):
            return Node('Integer', integer=value)._out

        elif isinstance(value, float):
            socket = Node('Value')._out
            socket._bsocket.default_value = value
            return socket

        elif isinstance(value, bool):
            return Node('Boolean', boolean=value)._out

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
    #   - If the input socket hide the value -> must be converted to an input node
    #   - Or is used to set the default_value to the input socket

    def plug_value_into_socket(self, value, in_socket):

        if value is None:
            return

        # ----------------------------------------------------------------------------------------------------
        # in_socket is defined by its name or index

        if isinstance(in_socket, (str, int)):
            in_socket = self.in_socket(in_socket)

        # ----------------------------------------------------------------------------------------------------
        # In socket is multi input and value is a list

        if in_socket.is_multi_input and isinstance(value, list):
            for v in reversed(value):
                self.plug_value_into_socket(v, in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # If the value is a Node, we take its default output socket

        if hasattr(value, '_bnode'):
            value = value._out

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
            #self._tree.link(Tree.value_to_socket(value), in_socket)
            self._tree.link(Node.InputNodeSocket(value)._bsocket, in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # We can use default value

        if socket_type in constants.ARRAY_TYPES:
            if socket_type == 'RGBA' and np.shape(value)==(3,):
                a = (value[0], value[1], value[2], 1)
            else:
                spec = constants.ARRAY_TYPES[socket_type]
                a = utils.value_to_array(value, spec['shape'])

            if utils.has_bsocket(a):
                #self._tree.link(self._tree.InputSocket(socket_type, value)._bsocket)
                self._tree.link(Node.InputNodeSocket(value)._bsocket, in_socket)
            else:
                try:
                    in_socket.default_value = list(a)
                except TypeError as e:
                    raise NodeError(f"Impossible to use the value [{value}] as default value for socket [{in_socket.node.name}]{in_socket.name}.",
                        node = in_socket.node.name,
                        in_socket= in_socket.name,
                        in_socket_type = in_socket.type,
                        value = value,
                        value_data_type = utils.get_input_type(value),
                        array = a,
                        original_error = str(e),
                        )

        elif socket_type in ['BOOLEAN', 'INT', 'VALUE', 'STRING']:
            try:
                in_socket.default_value = value
            except TypeError as e:
                raise NodeError(f"Impossible to use the value [{value}] as default value for socket [{in_socket.node.name}]{in_socket.name}.",
                    node = in_socket.node.name,
                    in_socket= in_socket.name,
                    in_socket_type = in_socket.type,
                    value = value,
                    value_data_type = utils.get_input_type(value),
                    original_error = str(e),
                    )

        elif in_socket.type in ['OBJECT', 'COLLECTION', 'IMAGE', 'MATERIAL']:
            bobj = utils.get_blender_resource(in_socket.type, value)

            if bobj is not None:
                in_socket.default_value = bobj

        elif in_socket.type == 'MENU':
            in_socket.default_value = str(value)

        else:
            raise NodeError(f"Impossible to set the socket '{in_socket.name}' of type '{socket_type}' with value {value}.")


    # =============================================================================================================================
    # Utilities

    def plug_selection(self, selection):
        if selection is None:
            return
        for bsocket in self._bnode.inputs:
            if bsocket.name == 'Selection':
                self.plug_value_into_socket(selection, bsocket)
                return

    # -----------------------------------------------------------------------------------------------------------------------------
    # Transform a list of socket keys (name or index or identifier) in a list of identifier

    def socket_keys_to_identifiers(self, names, use_inputs=True):

        if names is None:
            return None

        if len(names) == 0:
            return names

        bsockets = self._bnode.inputs if use_inputs else self._bnode.outputs
        transcode = {}
        remain = [key for key in names]

        for i, bsocket in enumerate(bsockets):
            ok = False
            for k in (i, bsocket.identifier, bsocket.name):
                if k in remain:
                    transcode[k] = bsocket.identifier
                    del remain[remain.index(k)]
                    ok = True
                if ok:
                    break

        if len(remain):
            raise NodeError(f"Socket name or identifier error: no socket named {remain} in node '{self._bnode.name}'",
                valids=[bsock.identifier for bsock in bsockets])

        if isinstance(names, list):
            return list(transcode.values())
        else:
            return {transcode[key]: value for key, value in names.items()}

    # -----------------------------------------------------------------------------------------------------------------------------
    # Plug another node into self
    # If the other node is None, the Tree input node is taken
    # Create is only valid in this case

    def plug_node_into(self, node=None, include=None, exclude=[], rename={}, create=True):
        """ Plug the output sockets of a node into the input sockets of the node.

        This method is used to connect several sockets in a compact syntax.

        If the node argument is None, the sockets are created in the Group Input node.
        Use 'include', 'exclude' and 'rename' arguments to control the connexions.

        ``` python
        with GeoNodes("Connect several sockets"):

            # Node with 'Value' output socket
            a = Node("Grid")

            # Create Group inputs to feed the node
            # 'Size X' and 'Size Y' are created in the group input not
            # 'Vertices X' and 'Vertices Y' are connected to the same 'Vertices' which is created
            a.plug_node_into(rename={'Vertices X': 'Vertices', 'Vertices Y': 'Vertices'})

            a = Node("Math")

            # Connect the 'Value' output socket to the 'Value' input socket
            # The third socket is exclude by its index
            # Input values are renamed 'First' and 'Second'
            a.plug_node_into(exclude=2, rename={'Value': 'First', 'Value_001': 'Second'})

            b = Node("Math", operation='SQRT')

            # Plug the previous math node on a single socket
            b.plug_node_into(a, include='Value')
        ```

        Arguments
        ---------
        - node (Node = None) : the node to get the outputs from. Use Group Input node if None
        - include (list of strs = None) : connects only the sockets in the list
        - exclude (list of strs = []) : exclude sockets in this list
        - rename (dict = {}) : rename the sockets to the given names

        Returns
        -------
        - Node : self
        """

        tree = self._tree

        # ----------------------------------------------------------------------------------------------------
        # Node with output sockets to plug

        if node is None:
            node = tree.input_node
        else:
            create = False

        is_node_group = self._bnode.bl_idname == 'GeometryNodeGroup'

        # ----------------------------------------------------------------------------------------------------
        # Make sure we have the sockets identifiers

        if isinstance(include, (str, int)):
            include = [include]
        if isinstance(exclude, (str, int)):
            exclude = [exclude]

        include = self.socket_keys_to_identifiers(include)
        exclude = self.socket_keys_to_identifiers(exclude)
        rename  = self.socket_keys_to_identifiers(rename)

        # ----------------------------------------------------------------------------------------------------
        # Loop on the input sockets of self

        for in_socket in self._bnode.inputs:

            if in_socket.type == 'CUSTOM':
                continue

            # ----- Already linked

            if in_socket.is_linked:
                continue

            # ----- Socket name can be renamed

            identifier  = in_socket.identifier
            if identifier in rename.keys():
                out_name = rename[identifier]
            else:
                out_name = in_socket.name

            # ----- Look for an output socket of same name and type

            out_socket = None
            for out_sock in node._bnode.outputs:
                if out_sock.name == out_name and out_sock.type == in_socket.type:
                    out_socket = out_sock
                    break
            if out_socket is None and not create:
                continue

            # ----- Must be in the sockets to include

            if include is not None and identifier not in include:
                if identifier not in rename.keys():
                    continue

            # ----- Must not be in the sockets to exclude

            if identifier in exclude:
                continue

            # ----------------------------------------------------------------------------------------------------
            # If the out_socket doesn't exist we create it

            if out_socket is None:

                # ----- Group : we create from the interface

                if is_node_group:

                    bsocket = utils.get_bsocket(in_socket)
                    bl_idname, subtype = constants.SOCKET_SUBTYPES[bsocket.bl_idname]

                    io_socket = tree.new_io_socket(bl_idname, 'INPUT', out_name)
                    if hasattr(io_socket, 'subtype'):
                        io_socket.subtype = subtype

                    # ----- Linking before setting the parameters is necessary for menu sockets

                    tree.link(tree.input_node[io_socket.identifier], in_socket)

                    # ----- Min and Max from embedded tree interface

                    item = self._bnode.node_tree.interface.items_tree[in_socket.name]
                    tree.set_input_socket_default(tree.input_node[io_socket.identifier], item.default_value)

                    io_socket.description = item.description
                    if hasattr(io_socket, 'min_value'):
                        io_socket.min_value = item.min_value
                        io_socket.max_value = item.max_value

                # ----- Not a Group : we create from the socket

                else:
                    out_socket = Tree.new_input_from_input_socket(in_socket, name=out_name)
                    tree.link(out_socket, in_socket)

            # ----------------------------------------------------------------------------------------------------
            # The out_socket exists : we can plug it

            else:
                tree.link(out_socket, in_socket)

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
# Group

class Group(Node):

    def __init__(self, group_name, sockets={}, **kwargs):
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

        # ----- Get the tree

        group_tree = bpy.data.node_groups.get(group_name)
        if group_tree is None:
            raise NodeError(f"Impossible to find the group named '{group_name}'")

        # ----- Create the node group

        super().__init__('Group', sockets=sockets, node_tree=group_tree)

        for k, v in kwargs.items():
            setattr(self, k, v)

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

    @staticmethod
    def call(group_name, sockets={}, **kwargs):
        return Group(group_name, sockets, **kwargs)

    def __getattr__(self, name):
        name = self._prefix + name

        for group_name in bpy.data.node_groups.keys():

            if utils.socket_name(group_name) == name:

                def f(sockets={}, **kwargs):
                    return Group(group_name, sockets, **kwargs)

                return f

        raise AttributeError(f"Impossible to find the group named '{name}'")
