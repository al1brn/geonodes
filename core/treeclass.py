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
from .treeinterface import TreeInterface


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
# Layout

class Panel:
    def __init__(self, name: str):
        """ Socket panel

        All group input and output sockets will be created within the current panel

        ``` python
        with GeoNodes("Layout Demo"):

            # Socket outside a panel
            g = Geometry()

            with Panel("First Panel"):
                a = Float(10, "Float Socket")
                b = Float(20, "Another Float Socket")

            with Panel("Second Panel"):
                i = Integer(1, "Integer Socket")
                j = Integer(20 "Another Integer Socket")
        ```

        Arguments
        ---------
        - name : Panel title
        """

        self.tree = Tree.current_tree
        self.name = name

        self.push()

    def push(self):
        self.tree._panels.append(self.name)

    def pop(self):
        self.tree._panels.pop()

    def __enter__(self):
        return self

    def __exit__(self, type, exc_value, traceback):
        self.pop()


# =============================================================================================================================
# Tree

class Tree:

    STACK   = []

    _total_nodes = 0
    _total_links = 0
    _total_time  = 0.

    def __init__(self, tree_name: str, tree_type: str='GeometryNodeTree', clear: bool=True, fake_user: bool=False, is_group: bool=False, prefix: str | None=None):
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

        if prefix is not None:
            tree_name = f"{prefix} {tree_name}"

        self._btree  = None
        self._prefix = prefix

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
        self._panels  = []

        # ----- Named attributes

        self._named_attrs = {}

        # ----- Clear the tree

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
    # Check if the blender node is valid in the context
    #
    # Nodes specific to tools can't be inserted in modifiers

    def check_node_validity(self, bnode):
        pass

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

        # ----- Remove and arrange

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

        # ----- Create a function

        G.build_from_tree(self._btree, prefix=self._prefix)

    def __enter__(self):
        return self

    def __exit__(self, type, exc_value, traceback):

        self.pop()

        if isinstance(exc_value, Break):
            return True

    # =============================================================================================================================
    # Named attributes

    def register_named_attribute(self, data_type, attr_name=None, prop_name=None):

        if prop_name is None:
            prop_name = utils.get_prop_name(attr_name)

        self._named_attrs[prop_name] = data_type
        return prop_name

        from . import  Boolean, Integer, Float, Vector, Color, Matrix, Rotation
        classes = {'FLOAT': Float, 'INT': Integer, 'FLOAT_VECTOR': Vector, 'BOOLEAN': Boolean, 'FLOAT4X4': Matrix, 'QUATERNION': Rotation, 'FLOAT_COLOR': Color}

        self._named_attrs[prop_name] = classes[data_type]

    def get_named_attribute(self, attr_name=None, prop_name=None):

        #from geonodes import Float

        if prop_name is None:
            prop_name = utils.get_prop_name(attr_name)
        else:
            attr_name = utils.get_attr_name(prop_name)

        data_type = self._named_attrs.get(prop_name, None)
        if data_type is None:
            print(f"WARNING: named attribute '{attr_name}' ({prop_name}) is unknwon. Use Float.Named('{attr_name}') or Float('{attr_name}')to suppress this warning.")
            data_type = 'FLOAT'

        node = Node("Named Attribute", sockets={'Name': attr_name}, data_type=data_type)
        return node._out

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
            elif name == 'WARNING':
                return (.949, .574, .119)
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

    #"""
    def io_socket_exists(self, bl_idname, in_out='INPUT', name=None):

        for item in self._btree.interface.items_tree:
            if item.item_type != 'SOCKET' or item.in_out != in_out or item.socket_type != bl_idname:
                continue
            if name is None or (item.name == name) or (item.identifier == name):
                return item

        return None
    #"""

    # ----------------------------------------------------------------------------------------------------
    # First socket type

    """
    def first_io_socket_is_geometry(self, in_out='INPUT'):

        for item in self._btree.interface.items_tree:
            if item.item_type != 'SOCKET' or item.in_out != in_out:
                continue
            return item.socket_type == 'NodeSocketGeometry'

        return False
    """

    # ----------------------------------------------------------------------------------------------------
    # Create an new interface socket

    """
    def new_io_socket(self, bl_idname, in_out, name):
        return self._btree.interface.new_socket(name=name, in_out=in_out, socket_type=bl_idname)
    """

    # --------------------------------------------------------------------------------
    # Clear interface

    """
    def clear_io_sockets(self):
        self._btree.interface.clear()
    """

    # --------------------------------------------------------------------------------
    # Get the current panel

    @property
    def current_panel(self):
        if len(self._panels):
            return self._panels[-1]
        else:
            return ""

    # --------------------------------------------------------------------------------
    # Set the default value of an input socket

    def set_input_socket_default(self, socket, value=None):

        #self._interface.set_default_value(socket.identifier, value=value, update_socket=True)
        #return

        if value is None:
            return

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            return

        try:
            bsocket.default_value = value
        except:
            #return
            pass

        #io_socket = self.io_socket_exists(bsocket.bl_idname, in_out='INPUT', name=bsocket.identifier)

        io_socket = self._interface.get_in_socket(bsocket.name, halt=False)
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
    def new_input(cls, bl_idname: str, name: str, subtype: str='NONE',
                  value: 'Any' = None, min_value: float | int | None = None, max_value: float | int | None = None, description: str = ""):
        """ Create a new input socket.

        This is an **input socket** of the Tree, hence an **output socket** of the <&Group Input> node.

        Arguments
        ---------
            - bl_idname : socket bl_idname
            - name : Socket name
            - value : Default value
            - min_value : Minimum value
            - max_value : Maxium value
            - description : user tip

        Returns
        -------
            Socket
        """

        tree = cls.current_tree

        # ----- Input node

        input_node = tree.input_node

        # ----------------------------------------------------------------------------------------------------
        # Get or create

        io_socket = tree._interface.get_in_socket(name, halt = False, panel_name=tree.current_panel)

        if io_socket is None:
            io_socket = tree._interface.create_in_socket(name, socket_type=bl_idname, panel=tree.current_panel)
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

        from geonodes.core import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, String, Menu

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
    def __init__(self, node_name, sockets={}, _items={}, link_from=None, _keep=None, **parameters):
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

        self._tree = Tree.current_tree
        btree = self._tree._btree
        tree_type = btree.bl_idname

        bl_idname = utils.get_node_bl_idname(node_name, tree_type)

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

        # ----- Check the context

        self._tree.check_node_validity(self._bnode)

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

    # ----------------------------------------------------------------------------------------------------
    # Create dynamic sockets with collection xxx_items
    #
    # xxx_items can have default values which can be renamed

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

    def _set_items(self, _items={}, clear=False, plug_items=True, items_name=None, **kwargs):

        # _items : sockets to create
        # plug_items : plug the sockets with the values or not
        # items_name : name of xxx_items to use (auto otherwise)
        # kwargs : sockets to create

        # ---------------------------------------------------------------------------
        # Merge the dicts

        all_items = {**_items, **kwargs}
        if not len(all_items):
            return

        # ---------------------------------------------------------------------------
        # Node items property

        if items_name is None:
            if not self._has_items:
                raise NodeError(f"Error when initializing node '{self._bnode.name}: this node has no items. Impossible to create the sockets.",
                    _items=_items)

            node_items = self._items
        else:
            node_items = getattr(self._bnode, items_name)

        # ---------------------------------------------------------------------------
        # Clear if required

        if clear:
            node_items.clear()

        # ---------------------------------------------------------------------------
        # Plug / rename the existing sockets

        for item in node_items:

            key = None

            # names match

            if item.name in all_items.keys():
                key = item.name

            # No exact match : look for python name match or type match in the worst case

            else:
                match_type = None
                sock_name = utils.socket_name(item.name)
                for k, v in all_items.items():
                    if utils.socket_name(k) == sock_name:
                        key = k
                        break

                    if utils.get_socket_type(v, default='GEOMETRY') == item.socket_type:
                        match_type = k
                if key is None and match_type is not None:
                    key = match_type

            # We have a matching key

            if key is not None:

                #print(" - MATCHING KEY", key, "for", item.name, '|', [s.name for s in self._bnode.inputs])

                if plug_items:
                    self.plug_value_into_socket(all_items[key], self.in_socket(item.name))

                if key != item.name:
                    self._bnode.inputs[item.name].name = key
                    item.name = key

                del all_items[key]

        # ---------------------------------------------------------------------------
        # Loop on the sockets to create

        for socket_name, socket_value in all_items.items():

            # 'new' method takes only one argument
            if self._bnode.bl_idname in ['GeometryNodeMenuSwitch']:
                sck = node_items.new(socket_name)

            # 'new' method takes two arguments
            else:
                input_type = 'GEOMETRY' if socket_value is None else utils.get_input_type(socket_value)
                try:
                    sck = node_items.new(input_type, socket_name)
                except Exception as e:
                    raise NodeError(f"Node {self}, input_type: '{input_type}', socket name: {socket_name}", error=str(e))

            # ----- Plug

            if plug_items:
                self.plug_value_into_socket(socket_value, self.in_socket(sck.name))

    # ----------------------------------------------------------------------------------------------------
    # Create a Socket from an output Blender NodeSocket

    @staticmethod
    def data_socket(bsocket):

        socket_type = bsocket.type

        # ====================================================================================================
        # Geometry

        class_name = None

        if socket_type == 'GEOMETRY':
            socket_name = bsocket.name.lower()
            if socket_name == 'mesh':
                class_name = 'Mesh'
            elif socket_name in ['curve', 'curves']:
                class_name = 'Curve'
            elif socket_name in ['grease pencil', 'grease pencils']:
                class_name = 'GreasePencil'
            elif socket_name in ['instance', 'instances']:
                class_name = 'Instances'
            elif socket_name in ['points', 'point cloud']:
                class_name = 'Cloud'
            elif socket_name == 'volume':
                class_name = 'Volume'
            else:
                class_name = 'Geometry'
        else:
            class_name = constants.CLASS_NAMES[socket_type]

        exec(f"from geonodes import {class_name}", locals(), globals())
        return eval(f"{class_name}(bsocket)", locals(), globals())










        if Tree.is_geonodes:
            from . import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, Texture, String, Menu
            from . import Mesh, Curve, GreasePencil, Cloud, Volume, Instances

            socket_class = {
                'BOOLEAN': Boolean,
                'INT': Integer,
                'VALUE': Float,
                'VECTOR': Vector,
                'ROTATION': Rotation,
                'MATRIX': Matrix,
                'RGBA': Color,
                'STRING': String,
                'MENU': Menu,
                'GEOMETRY': Geometry,
                'MATERIAL': Material, 'IMAGE': Image, 'OBJECT': Object, 'COLLECTION': Collection, 'TEXTURE': Texture,
                }[socket_type]

            if socket_type == 'GEOMETRY':
                socket_name = bsocket.name.lower()
                if socket_name == 'mesh':
                    return Mesh(bsocket)
                elif socket_name in ['curve', 'curves']:
                    return Curve(bsocket)
                elif socket_name in ['grease pencil', 'grease pencils']:
                    return GreasePencil(bsocket)
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

        INT_ENABLED = True

        counter = 0
        ok_counter = False

        if isinstance(name, int):
            if INT_ENABLED:
                ok_counter = True
                counter = name
            else:
                return bsockets[name]

        disabled_bsocket = None
        bsocket = None
        for bsock in bsockets:
            match = False
            if ok_counter:
                match = counter == 0
            else:
                match = name in [bsock.name, bsock.identifier, utils.socket_name(bsock.name)]
                if not match and bsock.label is not None:
                    match = name == utils.socket_name(bsock.label)

            if match:
                if bsock.enabled:
                    bsocket = bsock
                    break
                else:
                    disabled_bsocket = bsock

            if bsock.enabled:
                counter -= 1

        if bsocket is None:
            if not ok_counter:
                bsocket = disabled_bsocket

        if halt and bsocket is None:
            valids = [f"{'x' if sock.enabled else 'o'} {sock.name}" for sock in bsockets]
            if disabled_bsocket is None:
                raise NodeError(f"Socket name '{name}' not found in node '{self._bnode.name}' ({self._bnode.bl_idname})", keyword=name, valids=valids)
            else:
                raise NodeError(f"Socket name '{name}' is disabled in node '{self._bnode.name}' ({self._bnode.bl_idname})", keyword=name, valids=valids)

        return bsocket

    def in_socket(self, name, halt=True):
        return self.inout_socket(name, self._bnode.inputs, halt=halt)

    def out_socket(self, name, halt=True):
        sock = self.inout_socket(name, self._bnode.outputs, halt=halt)
        if sock is None:
            return None
        else:
            return self.data_socket(sock)

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
            if bsock.enabled and bsock.type != 'CUSTOM':
                return self.data_socket(bsock)
        return None

    # ====================================================================================================
    # Read a node attribute : it is an output socket

    def __getattr__(self, name):

        sbnode = type(self)

        if '_bnode' in self.__dict__:

            sbnode = f"'{self._bnode.name}'"

            # The name can refer to an output socket
            out_socket = self.out_socket(name, halt=False)

            # Try with '_' suffix syntax
            if out_socket is None and len(name) > 1 and name[-1] == '_' and name[-2] != '_':
                out_socket = self.out_socket(name[:-1], halt=False)

            if out_socket is None:

                node_name = self.__dict__['_bnode'].name

                # Nope : this is not an output socket
                # Perhaps a confusion with the default output socket
                def_out = self._out
                if def_out is not None and name in dir(def_out):
                    print(f"CAUTION: the node '{node_name}' has no attribute '{name}', use socket '{utils.socket_name(def_out._bsocket.name)}' or '_out' instead")
                    return getattr(def_out, name)

                # No more hope: let's raise the error
                _ = self.out_socket(name)

            else:
                # OK : it is an output socket
                return out_socket

        #raise AttributeError(f"Node parameter '{name}' not found.")
        raise NodeError(f"Attribute '{name}' of node '{sbnode}' is not found.", keyword=name)

    def __setattr__(self, name, value):

        if name in ['_tree', '_bnode', '_label', '_color', 'pin_gizmo']:
            super().__setattr__(name, value)
            return

        sbnode = ''
        if '_bnode' in self.__dict__:

            # ----- Set parameter

            bnode = self.__dict__['_bnode']
            sbnode = bnode.name
            if name not in ['width', 'height', 'dimensions'] and hasattr(bnode, name):
                setattr(bnode, name, value)
                return

            # ---- Link input node

            in_socket = self.in_socket(name)
            if in_socket is not None:
                self.plug_value_into_socket(value, in_socket)
                return

        #raise AttributeError(f"Node parameter '{name}' not found in '{sbnode}'.")
        raise NodeError(f"Node parameter '{name}' not found in '{sbnode}'.", keyword=name)

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

        if '_bnode' in dir(value):
            value = value._out

        # ----------------------------------------------------------------------------------------------------
        # If the value is a domain, we take its geometry

        if hasattr(value, '_geo'):
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

    def link_from(self,
            node:      'Node | Tree | None | str' = 'TREE',
            include:   list[str] | str | None = None,
            exclude:   list[str] | str = [],
            rename:    dict[str: str] = {},
            arguments: dict['name': 'value'] = {},
            create:    bool =True,
            panel:     str | None = None):
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
        - rename : rename the sockets to the given names
        - arguments : arguments used at initialization time. Arguments which are defined in the liste are ignored
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

        create = create and node._bnode.bl_idname == 'NodeGroupInput'

        is_node_group = self._bnode.bl_idname == 'GeometryNodeGroup'

        # Tree interface of self as Group
        group_interface = None
        if is_node_group:
            group_interface = TreeInterface(self._bnode.node_tree)

        if False:
            print("LINK INPUT FROM", tree)
            print(" - node   ", node)
            print(" - include", include)
            print(" - exclude", exclude)
            print(" - rename ", rename)
            print(" - args   ", arguments)
            print(" - create ", create)

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

            # ----- In the arguments list

            val = None
            socket_name = in_socket.name
            pyname = utils.socket_name(socket_name)
            if socket_name in arguments.keys():
                val = arguments[socket_name]
            elif pyname in arguments:
                val = arguments[pyname]
            if val is not None:
                continue

            # ----- Socket name can be renamed

            identifier = in_socket.identifier
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

                    parent = group_interface.by_identifier(bsocket.identifier).parent
                    if parent is None:
                        panel = ""
                    else:
                        panel = parent.name

                    io_socket = tree._interface.create_in_socket(out_name, socket_type=bl_idname, panel=panel)

                    if hasattr(io_socket, 'subtype'):
                        io_socket.subtype = subtype

                    # ----- Linking before setting the parameters is necessary for menu sockets

                    tree.link(tree.input_node[io_socket.identifier], in_socket)

                    # ----- Min and Max from embedded tree interface

                    item = self._bnode.node_tree.interface.items_tree[in_socket.name]

                    if hasattr(item, 'default_value') and hasattr(io_socket, 'default_value'):
                        io_socket.default_value = item.default_value
                        #tree.input_node[io_socket.identifier].default_value = item.default_value

                    io_socket.description = item.description
                    if hasattr(io_socket, 'min_value') and hasattr(item, 'min_value'):
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
    # Pin gizmo
    # The first input socket

    @property
    def pin_gizmo(self):
        return self._bnode.inputs[0].pin_gizmo

    @pin_gizmo.setter
    def pin_gizmo(self, value):
        self._bnode.inputs[0].pin_gizmo = value

# =============================================================================================================================
# Group

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

        # ----- Get the tree

        group_tree = bpy.data.node_groups.get(group_name)
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

class G:
    """ Group functional call

    This weird class is empty but two static methods aimed at building dynamic static functions.

    For each built Tree, a function is created in class G (for Groups).
    To call the created group, the function syntax can be used rather than instantiating the Group Node.

    Let's suppose we have the following group.

    ``` python
    with GeoNodes("Translate Geometry"):
        v = Vector(0, "Translation")
        factor = Float.Factor(1, "Factor")

        Geometry().transform(translation=v*factor).out()
    ```

    The created group can be called in another tree following the two possible syntax:

    ``` python
    with GeoNodes("Calling a Group"):

        geo = Geometry()

        # ----- Instantiate a node Group by its name

        geo = Group("Translate Geometry", geometry=geo).geometry

        # Or with parameters

        geo = Group("Translate Geometry", geometry=geo, translation=(1, 0, 0), factor=.5).geometry


        # ----- Function call

        geo = G.translate_geometry(geo)

        # Or with parameters
        # be sure of the sockets order if you don't use keyword argument syntax

        geo = G.translate_geometry(geo, (1, 0, 0), .5)
    ```

    """
    @staticmethod
    def build_from_tree(btree, prefix=""):
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
        # ----- Target

        if prefix is None:
            prefix = ""

        if prefix == "":
            func_name = utils.socket_name(btree.name)
            target = "G"
        else:
            assert(len(btree.name) > len(prefix) + 1)
            assert(btree.name.startswith(prefix))

            prefix = prefix.lower()
            target = f"G.{prefix}"
            if not hasattr(G, prefix):
                s = f"class PREFIX_{prefix}:\n\tpass\n"
                s += f"G.{prefix} = PREFIX_{prefix}"
                exec(s)

            func_name = utils.socket_name(btree.name[len(prefix) + 1:])
            prefix += "_"

        # ----- Input node

        sock_names = []
        for bnode in btree.nodes:
            if bnode.bl_idname == 'NodeGroupInput':
                sock_names = [utils.socket_name(bsock.name) for bsock in bnode.outputs if bsock.type != 'CUSTOM']
                break
        sock_names = TreeInterface.ensure_uniques(sock_names, single_digit=True)
        sock_names.append('link_from')

        # ----- Create the function

        header = [f"{arg}=None"  for arg in sock_names]
        call   = [f"{arg}={arg}" for arg in sock_names]

        s = f"def G_{prefix}{func_name}(" + ", ".join(header) + "):\n"
        s += f"\treturn Group('{btree.name}', " + ", ".join(call) + ")._out\n\n"
        #s += f"setattr({target}, '{func_name}', G_{prefix}{func_name})\n"
        s += f"{target}.{func_name} = G_{prefix}{func_name}\n"

        # DEBUG
        if False:
            print('-'*100)
            print(s)
            print('-'*100)

        exec(s)


    @staticmethod
    def build_functions(prefixes = []):
        """ Dynamically create a function for each node group

        Arguments
        ---------
        - prefixes (list of strs = []) : function prefixes

        Returns
        -------
        - None
        """

        for btree in bpy.data.node_groups:
            name = btree.name
            prefix = None
            for p in prefixes:
                if name.startswith(p + " "):
                    prefix = p
                    break

            G.build_from_tree(btree, prefix=prefix)



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

            if utils.socket_name(group_name) == name:

                def f(sockets={}, **kwargs):
                    return Group(group_name, sockets, **kwargs)

                return f

        raise AttributeError(f"Impossible to find the group named '{name}'")


# =============================================================================================================================
# Specific nodes

class ColorRamp(Node):
    def __init__(self, fac=None, stops=None):
        """ Color ramp node

        > Node <&Node Color Ramp>

        Exposes utilities to manage the color ramp

        ``` python
        ramp1 = Float(.5).color_ramp(stops=[.1, .9])
        ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
        ```

        Arguments
        ---------
        - fac (Float = None)
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)
        """
        super().__init__('Color Ramp', {'Fac': fac})
        if stops is not None:
            self.set_stops(*stops)

    @property
    def color_ramp(self):
        """ Returns the node color_ramp structure

        Returns
        -------
        - bpy.types.ColorRamp
        """
        return self._bnode.color_ramp

    def set_stops(self, *stops):
        """ Set the color ramp stops

        ``` python
        ramp =

        Arguments
        ---------
        - stops : list of tuple (position, color)
        """

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
