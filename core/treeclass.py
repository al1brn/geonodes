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
- Break         : Exit from with block
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
    def __init__(self, name: str, tip="", closed_by_default=False):
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

        self.tree._interface.create_panel(name=name, tip=tip, closed_by_default=closed_by_default)

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

    def __init__(self, tree_name: str, tree_type: str='GeometryNodeTree', clear: bool=True, fake_user: bool=False, is_group: bool=False, prefix: str = ""):
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

        if prefix is None:
            prefix =  ""

        prefix = str(prefix)
        if len(prefix):
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

        self._nodes     = [] # List of nodes
        self._layouts   = [] # Stack of layouts
        self._panels    = [] # Stack of panels

        # ----- Named attributes

        self._named_attrs = {}

        # ----- Clear the tree

        if clear:
            self.clear()

        # ----- Interface

        self._interface = None
        if self._is_group or tree_type == 'GeometryNodeTree':
            self._interface = TreeInterface(self._btree)
            self._interface.set_tip_delete()

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
        self._nodes.clear()
        self._btree.links.clear()
        self._btree.nodes.clear()

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

    def pop(self, clean=True):
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

        # ----- Remove from stack

        tree = Tree.STACK.pop()
        if tree != self:
            raise NodeError(f"Error in tree stack management")

        # ----- Clean the interface

        if clean and tree._interface is not None:
            tree._interface.clear(False)

        # ----- Arrange

        self.arrange()

        # ----- Stats

        duration = time() - self._start_time

        print(f"Tree '{self._btree.name}' built: {self._str_stats} in {duration:.1f} s")

        Tree._total_nodes += len(self._btree.nodes)
        Tree._total_links += len(self._btree.links)
        Tree._total_time  += duration

        # ----- Create a function

        #G.build_from_tree(self._btree, prefix=self._prefix)

    def __enter__(self):
        return self

    def __exit__(self, type, exc_value, traceback):

        # In case of error, the sockets are not cleaned

        is_break = isinstance(exc_value, Break)
        clean = is_break or (exc_value is None)

        self.pop(clean=clean)

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

        #if hasattr(out_socket, '_bsocket'):
        if '_bsocket' in dir(out_socket):
            out_socket = out_socket._bsocket

        #if hasattr(in_socket, '_bsocket'):
        if '_bsocket' in dir(in_socket):
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

    # =============================================================================================================================
    # Input / output sockets

    # ----------------------------------------------------------------------------------------------------
    # Get the current panel

    @property
    def current_panel(self):
        if len(self._panels):
            return self._panels[-1]
        else:
            return ""

    # ----------------------------------------------------------------------------------------------------
    # Get the socket panel

    def get_socket_panel(self, socket):
        bsocket = utils.get_bsocket(socket)
        return self._interface.by_identifier(bsocket.identifier).parent.name

    # ----------------------------------------------------------------------------------------------------
    # Get the existing sockets indexed by the full name (including the panel name)

    def get_socket_names(self, bsockets, bl_idname=None):
        keys  = []
        socks = []
        for bsocket in bsockets:
            if bsocket.type == 'CUSTOM':
                continue
            i_socket = self._interface.by_identifier(bsocket.identifier)

            if (bl_idname is None) or (i_socket.socket_type == bl_idname):
                label = bsocket.name if bsocket.label == "" else bsocket.label
                keys.append(utils.snake_case(self.get_socket_panel(bsocket) + '_' + label))
                socks.append(bsocket)

        return {key: bsocket for key, bsocket in zip(utils.ensure_uniques(keys, single_digit=True), socks)}

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

    # =============================================================================================================================
    # Create a new input socket

    @classmethod
    def new_input(cls, bl_idname, name, value=None, panel=None, force_create=False, **props):
        """ Create a new input socket.

        This is an **input socket** of the Tree, hence an **output socket** of the <&Group Input> node.

        Arguments
        ---------
            - bl_idname (str) : socket bl_idname
            - name (str): Socket name
            - value (Any = None) : Default value
            - panel (str = None) : Panel to place the socket in
            - force_create (bool = False) : create the socket even if an homonym exists
            - props : properties specific to interface socket

        Returns
        -------
            Socket
        """

        tree = cls.current_tree

        # ----- Input node

        input_node = tree.input_node

        # ----------------------------------------------------------------------------------------------------
        # Get or create the socket

        if panel is None:
            panel = tree.current_panel

        i_socket, set_value = tree._interface.get_create_socket('INPUT', name, bl_idname, panel=panel, force_create=force_create)
        out_socket = input_node[i_socket.identifier]

        # ----------------------------------------------------------------------------------------------------
        # Properties

        for prop_name, prop_value in props.items():
            if prop_value is None:
                if prop_name == 'description':
                    prop_value = ""
                else:
                    continue

            try:
                setattr(i_socket, prop_name, prop_value)

            except Exception as e:
                raise NodeError(f"Socket '{name}' creation error: impossible to set the socket property '{prop_name}' with value '{prop_value}'",
                    socket_type= bl_idname,
                    error_message = str(e),
                    **props)

        # ----------------------------------------------------------------------------------------------------
        # Let's set the default value if the socket is created
        # Note: if the socket already exists, we don't override its value

        if value is not None:
            def_value = utils.python_value_for_socket(value, utils.get_socket_type(out_socket))
            if (def_value is not None):
                if hasattr(i_socket, 'default_value'):
                    try:
                        i_socket.default_value = def_value
                    except Exception as e:
                        raise NodeError(f"Impossible to set the default value {value} <{def_value}> to socket of type '{bl_idname}'", error_message=str(e))

                    # ----------------------------------------------------------------------------------------------------
                    # TO BE CHECKED

                    if False:
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

    def new_output(self, bl_idname, name, panel=None, **props):
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

        if panel is None:
            panel = self.current_panel

        socket_type, subtype = constants.SOCKET_SUBTYPES[bl_idname]
        io_socket, created = self._interface.get_create_socket('OUTPUT', name, socket_type, panel=panel)
        if subtype is not None and 'subtype' not in props:
            io_socket.subtype = subtype

        # ----- Set the socket interface properties

        conv = constants.INTERFACE_SOCKET_PROPERTIES
        for prop_name, prop_value in props.items():
            if prop_name not in conv.values():
               raise NodeError(f"Invalid interface socket property: '{prop_name}' when creating socket '{name}' ({bl_idname}", keyword=prop_name)

            itf_name = list(conv.keys())[list(conv.values()).index(prop_name)]
            if not hasattr(io_socket, itf_name):
                raise NodeError(f"The socket '{name}' ('{bl_idname}' has not property '{itf_name}' ('{prop_name}')", keyword=prop_name)

            setattr(io_socket, itf_name, prop_value)

        return output_node._bnode.inputs[io_socket.identifier]


    # --------------------------------------------------------------------------------
    # Create a new input socket from an existing node input socket

    @classmethod
    def new_input_from_input_socket(cls, input_socket, name=None, panel=None, force_create=False):
        """ Create a new group input socket from an existing input socket.

        Arguments
        ---------
        - input_socket (socket) : a node input _insocket
        - name (str = None) : name of the group input socket to create
        - panel (str = None) : name of the panel
        - force_create (bool = False) : create even if a socket with the same name exists

        Returns
        -------
        - Socket
        """

        tree = Tree.current_tree

        # ----------------------------------------------------------------------------------------------------
        # Get the socket type and subtype

        bsocket = utils.get_bsocket(input_socket)
        if name is None:
            name = bsocket.name if bsocket.label == "" else bsocket.label

        bl_idname, subtype = constants.SOCKET_SUBTYPES[bsocket.bl_idname]

        # ----------------------------------------------------------------------------------------------------
        # Get the socket interface if exists

        i_source = None
        if hasattr(bsocket.node, 'node_tree'):
            interf = TreeInterface(bsocket.node.node_tree)
            i_source = interf.by_identifier(bsocket.identifier)
            if panel is None:
                panel = i_source.parent.name

        # ----------------------------------------------------------------------------------------------------
        # Create the new socket and link it

        socket = tree.new_input(bl_idname, name, panel=panel, force_create=force_create)
        tree.link(socket, input_socket)

        i_target = socket._interface_socket

        # ----------------------------------------------------------------------------------------------------
        # Copy the properties

        if i_source is not None:
            for prop_name in constants.INTERFACE_SOCKET_PROPERTIES:
                prop_value = getattr(i_source, prop_name, None)
                if prop_value is not None:
                    setattr(i_target, prop_name, prop_value)

        return socket

    # -----------------------------------------------------------------------------------------------------------------------------
    # Link two nodes

    def link_nodes(self, from_node, to_node, include=None, exclude=[], create=True, panel=None):
        """ Link two nodes

        If from_node is a Group Input node, the necessary sockets can be created if 'create' argument is True.

        Arguments
        ---------
        - from_node : the node to get the outputs from
        - to_node : the node to plug into
        - include (list = None) : connect only the sockets in the list (or panels)
        - exclude (list = []) : exclude sockets in this list (or panels)
        - create : create tree input sockets  (i.e. node output sockets) in from_node if it is a 'Group Input Node'
        - panel : panel name to create, use tree default name if None
        """

        # ----------------------------------------------------------------------------------------------------
        # From Node

        create = create and from_node._bnode.bl_idname == 'NodeGroupInput'
        from_interface = None
        if create:
            from_interface = from_node._tree._interface

        # ----------------------------------------------------------------------------------------------------
        # To Node can have an interface if it is a Group

        to_interface = None
        if to_node._is_group_node:
            to_interface = TreeInterface(to_node._bnode.node_tree)

        # ----------------------------------------------------------------------------------------------------
        # Start with a dict: identifier -> bsocket
        # Note : if include is None, all the enabled sockets are returned

        id_bsockets = to_node.identified_bsockets('INPUT', names=include)

        # ----------------------------------------------------------------------------------------------------
        # Exclude sockets in the exclusion list

        for id in to_node.identified_bsockets('INPUT', names=exclude).keys():
            del id_bsockets[id]

        # ----------------------------------------------------------------------------------------------------
        # Loop on the input sockets of to_node

        linked_ids = []
        for to_socket in id_bsockets.values():

            # ----- Already linked

            if to_socket.is_linked:
                continue

            # ----------------------------------------------------------------------------------------------------
            # Socket name and panel name

            from_name = utils.get_label(to_socket)

            if to_interface is None:
                from_panel = panel
            else:
                from_panel = to_interface.by_identifier(to_socket.identifier).parent.name
                if from_panel == "":
                    from_panel = panel
            if from_panel is None:
                from_panel = ""

            # ----------------------------------------------------------------------------------------------------
            # Look for an output socket of from_node with the proper name
            # CAUTION : when to_node has homonyms, we must create a different socket each time

            from_socket = None
            for bsocket in from_node._bnode.outputs:

                # Not the good name
                if utils.get_label(bsocket) != from_name:
                    continue

                # Not the good panel
                if from_interface is not None:
                    if from_interface.by_identifier(bsocket.identifier).parent.name != from_panel:
                        continue

                # Already used
                if bsocket.identifier in linked_ids:
                    continue

                # Not the proper type
                #socket_type, subtype = constants.SOCKET_SUBTYPES[to_socket.bl_idname]
                if bsocket.type != to_socket.type:
                    continue

                # We have it
                from_socket = from_node.data_socket(bsocket)
                if create:
                    from_socket._mark_for_delete(False)

                break

            # If it doesn't exist, we can create it
            if from_socket is None and create:
                from_socket = self.new_input_from_input_socket(to_socket, panel=from_panel, force_create=True)

                pos = from_socket._interface_socket.position

            # We link
            if from_socket is not None:
                self.link(from_socket, to_socket)

                # Not to reuse in case to_nodes have homonyms
                linked_ids.append(from_socket._bsocket.identifier)



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
                print(f"def FUNCTION(self,", ", ".join([utils.snake_case(sock.name) + f"={sock.default_value}" for sock in node.inputs]))
            else:
                print(f"def FUNCTION(self,", ", ".join([utils.snake_case(sock.name) + "=None" for sock in node.inputs]))

            sockets = ", ".join([f"'{sock.name}': {utils.snake_case(sock.name)}" for sock in node.inputs])
            print(f"Node('{node.name}', " + "{" + sockets + "}")
            print()

# =============================================================================================================================
# Node

class Node:
    def __init__(self, node_name, sockets={}, _items={}, link_from=None, **parameters):
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

        # ----- Node Creation

        self._bnode = btree.nodes.new(type=bl_idname)
        self._bnode.select = False
        self._tree.check_node_validity(self._bnode)

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

    @property
    def _is_group_node(self):
        return self._bnode.bl_idname in ['GeometryNodeGroup', 'ShaderNodeGroup']

    @property
    def _tree_interface(self):
        if self._is_group_node:
            return TreeInterface(self._bnode.node_tree)
        else:
            return None

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

        if True:
            to_del = []
            for key, value in all_items.items():

                socket = self.by_name('INPUT', key, as_argument=False, halt=False)
                if socket is None:
                    socket = self.by_name('INPUT', key, as_argument=True, halt=False)

                if socket is not None:
                    if plug_items:
                        self.plug_value_into_socket(all_items[item.name], socket)
                    to_del.append(key)

            for key in to_del:
                del all_items[key]

        else:
            for item in node_items:

                key = None

                # Names match

                if item.name in all_items.keys():
                    key = item.name

                # No exact match : look for python name match or type match in the worst case

                else:
                    match_type = None
                    sock_name = utils.snake_case(item.name)
                    for k, v in all_items.items():
                        if utils.snake_case(k) == sock_name:
                            key = k
                            break

                        if utils.get_socket_type(v, default='GEOMETRY') == item.socket_type:
                            match_type = k

                    if key is None and match_type is not None:
                        key = match_type

                # We have a matching key

                if key is not None:

                    if plug_items:
                        #self.plug_value_into_socket(all_items[key], self.in_socket(item.name))
                        self.plug_value_into_socket(all_items[key], self[item.name])

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
                self[sck.name] = socket_value

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

    def get_socket_names(self, in_out, only_enabled=True, as_argument=True):
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
        - only_enabled : use only enabled sockets

        Returns
        -------
        - dict : socket identifier -> list of possible names
        """

        assert(in_out in ('INPUT', 'OUTPUT'))

        # ----- Via TreeInterface if group node to take panels into account

        if self._is_group_node:
            interface = TreeInterface(self._bnode.node_tree)
            i_sockets = interface.get_unique_names(in_out, as_argument=as_argument)
            return {name: self.by_identifier(in_out, i_socket.identifier) for name, i_socket in i_sockets.items()}

        # ---- Not a group

        names    = []
        bsockets = []

        bsocks = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
        for bsock in bsocks:

            if bsock.type == 'CUSTOM':
               continue

            if only_enabled and not bsock.enabled:
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

    def valid_names(self, in_out, only_enabled=True, as_argument=True):
        return list(self.get_socket_names(in_out, only_enabled=only_enabled, as_argument=as_argument).keys())

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its index, identifier or name

    def by_name(self, in_out, name, only_enabled=True, as_argument=True, candidates=False, halt=True):
        """ Get a socket by its name

        Arguments
        ---------
        - in_out (str) : str in ('INPUT', 'OUTPUT')
        - name (str) : searched named
        - only_enabled (bool = True) : consider only enabled sockets
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
                if not bsocket.enabled and only_enabled:
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

        sockets = self.get_socket_names(in_out, only_enabled=only_enabled, as_argument=as_argument)

        socket = sockets.get(name)

        # ----- Trying with identifier
        if socket is None and not as_argument:
            socket = self.by_identifier(in_out, name, halt=False)

        # ----- Trying with disabled
        if socket is None:
            all_sockets = self.get_socket_names(in_out, only_enabled=False, as_argument=as_argument)
            socket = all_sockets.get(name)

        # ----- Error message
        if socket is None and halt:
            raise NodeError(f"{in_out} socket '{name}' not found in node '{self._bnode.name}'.", valids=list(sockets.keys()))

        # ----- What we have
        return socket

    # ====================================================================================================
    # Set an input socket and get an output socket

    def get(self, name, default=None):
        socket = self.by_name('OUTPUT', name, only_enabled=True, as_argument=False, candidates=False, halt=False)
        if socket is None:
            return self.by_name('OUTPUT', name, only_enabled=True, as_argument=True, candidates=False, halt=False)
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

        if name in ['_tree', '_bnode', '_label', '_color', 'pin_gizmo'] or name in dir(self):
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

            bsocket = self.by_name('INPUT', name, only_enabled=True, as_argument=True, halt=False)
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
    # Returns the first enabled output socket

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

        # Full dict
        bsockets = self._bnode.inputs if in_out == 'INPUT' else self._bnode.outputs
        sockets_dict = {}
        for bsocket in bsockets:
            if not bsocket.enabled or bsocket.type == 'CUSTOM':
                continue
            sockets_dict[bsocket.identifier] = bsocket

        if names is None:
            return sockets_dict

        # Normalize
        if isinstance(names, str):
            names = [names]

        # Interface
        interface = self._tree_interface

        # ----------------------------------------------------------------------------------------------------
        # Extract the panels from the names

        if interface is not None:
            old_names = names
            names = []

            for name in old_names:
                panel = interface.get_panel(name, halt=False)
                if panel is None:
                    names.append(name)
                else:
                    uniques = interface.get_unique_names(in_out, as_argument=False, include_homonyms='NO')
                    for unique_name, socket in uniques.items():
                        if socket.parent == panel:
                            names.append(unique_name)

        # ----------------------------------------------------------------------------------------------------
        # Names can contain identifier, name or argument
        # We build a dictionary:
        # identifier -> list of possible names

        # Initialize with identifier
        all_names = {}
        for identifier in sockets_dict.keys():
            all_names[identifier] = [identifier]

        # Complete with unique arg names
        sockets = self.get_socket_names(in_out, only_enabled=True, as_argument=True)
        for name, bsocket in sockets.items():
            if bsocket.identifier in all_names:
                all_names[bsocket.identifier].append(name)

        # Complete with unique socket names
        sockets = self.get_socket_names(in_out, only_enabled=True, as_argument=False)
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

    def out(self):
        for bsock in self._bnode.outputs:
            if bsock.enabled and bsock.type != 'CUSTOM':
                label = bsock.name if bsock.label == "" else bsock.label
                self.data_socket(bsock).out(label)
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

    def plug_value_into_socket(self, value, in_socket):

        if value is None:
            return

        # ----------------------------------------------------------------------------------------------------
        # in_socket is defined by its name or index

        if isinstance(in_socket, (str, int)):
            in_socket = self.by_name('INPUT', in_socket)

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

                except Exception as e:
                    raise NodeError(f"Impossible to use the value <{value}> (type: {type(value).__name__}) as default value for socket [{in_socket.node.name}]{in_socket.name}.",
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
    # Plug another node into self
    # If the other node is None, the Tree input node is taken
    # Create is only valid in this case

    def link_from(self,
            node:      'Node | Tree | None | str' = 'TREE',
            include:   list[str] | str | None = None,
            exclude:   list[str] | str = [],
            #rename:    dict[str: str] = {},
            arguments: dict['name': 'value'] = {},
            create:    bool = True,
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

# =============================================================================================================================
# G to expose groups as functions

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

        # ----- Input node

        socks, homos = TreeInterface(btree).get_unique_names('INPUT', as_argument=True, include_homonyms='SEPARATE')

        sock_names = list(socks.keys())
        sock_names.extend(list(homos.keys()))
        sock_names.append('link_from')

        # ----- Create the function

        header = [f"{arg}=None"  for arg in sock_names]
        call   = [f"{arg}={arg}" for arg in sock_names]

        s = f"def {func_name}(" + ", ".join(header) + "):\n"
        s += f"\treturn Group('{btree.name}', " + ", ".join(call) + ")._out\n\n"
        #s += f"G.{func_name} = {func_name}\n"
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
            print(f"Function created ({f}):\n    {func_name}(" + ", ".join([sname for sname in sock_names if sname != 'link_from']) + ")")

        #return getattr(G, func_name)
        return f

    # ====================================================================================================
    # Get a tree by its snake case name

    def __getattr__(self, name):

        tree_type = Tree.current_tree._btree.type

        target = utils.snake_case(self.prefix + name)

        for btree in bpy.data.node_groups:
            if btree.type != tree_type:
                continue

            if utils.snake_case(btree.name) == target:
                return self.build_function(btree)

        raise AttributeError(f"Group '{target}' not found")


class G_OLD:
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
    VERBOSE = False

    @staticmethod
    def create_prefix(name):
        f_prefix = utils.snake_case(name)
        name = name.replace("'", r"\'")
        if not hasattr(G, f_prefix):
            s = f"class PREFIX_{f_prefix}:\n\tname='{name}'\n\t_name='{f_prefix}'\n"
            s += f"G.{f_prefix} = PREFIX_{f_prefix}"
            exec(s)

        if G.VERBOSE:
            print(f"Prefix created: G.{f_prefix} ('{name}')")

        return getattr(G, f_prefix)

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
            func_name = utils.snake_case(btree.name)
            target = "G"
            f_prefix = ""

        else:
            assert(len(btree.name) > len(prefix) + 1)
            assert(btree.name.startswith(prefix))

            pref = G.create_prefix(prefix)
            f_prefix = pref._name
            target = f"G.{f_prefix}"
            func_name = utils.snake_case(btree.name[len(prefix) + 1:])
            f_prefix += "_"

        # ----- Input node

        socks, homos = TreeInterface(btree).get_unique_names('INPUT', as_argument=True, include_homonyms='SEPARATE')

        sock_names = list(socks.keys())
        sock_names.extend(list(homos.keys()))
        sock_names.append('link_from')

        # ----- Create the function

        header = [f"{arg}=None"  for arg in sock_names]
        call   = [f"{arg}={arg}" for arg in sock_names]

        s = f"def G_{f_prefix}{func_name}(" + ", ".join(header) + "):\n"
        s += f"\treturn Group('{btree.name}', " + ", ".join(call) + ")._out\n\n"
        s += f"{target}.{func_name} = G_{f_prefix}{func_name}\n"

        # DEBUG
        if False:
            print('-'*100)
            print(s)
            print('-'*100)

        exec(s)

        if G.VERBOSE:
            print(f"Prefix method created: {target}.{func_name}(" + ", ".join([sname for sname in sock_names if sname != 'link_from']) + ")")


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

            if utils.snake_case(group_name) == name:

                def f(sockets={}, **kwargs):
                    return Group(group_name, sockets, **kwargs)

                return f

        raise AttributeError(f"Impossible to find the group named '{name}'")


# =============================================================================================================================
# Specific nodes

# -----------------------------------------------------------------------------------------------------------------------------
# Color Ramp

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
        self.interpolation = interpolation
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

# -----------------------------------------------------------------------------------------------------------------------------
# Color Ramp

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
