#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : treestack
------------------
- get create trees according tree type
- StakedTree offering context management for with statement
- Node implementing roog method and context management for layouts
- Trees offering groups management

update : 2024/02/17
update : 2024/03/29
"""

import bpy
import mathutils
from pprint import pprint

from geonodes.nodes import constants
from geonodes.nodes import documentation
from geonodes.nodes import utils
from geonodes.nodes import sockets

# ====================================================================================================
# Get / delete a tree

# ----------------------------------------------------------------------------------------------------
# Get / Create a tree

def get_tree(name, tree_type='GeometryNodeTree', create=False, clear=False):
    """ Get or create a new nodes tree

    Arguments
    ---------
        - name (str) : Tree name
        - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
        - create (bool = False) : Create the tree if it doesn't exist
        - clear (bool = False) : Clear the tree if it exists

    Returns
    -------
        - Tree of type matching the request or None if it doesn't exist
    """

    btree = bpy.data.node_groups.get(name)
    if btree is None or btree.bl_idname != tree_type:
        if not create:
            return None
        btree = bpy.data.node_groups.new(name=name, type=tree_type)

    if clear:
        btree.nodes.clear()

    return btree

# ----------------------------------------------------------------------------------------------------
# Delete a tree

def del_tree(btree): #, tree_type='GeometryNodeTree'):

    """ Delete a tree

    Arguments
    ---------
        - btree (blender Tree or str : Tree or tree name
    """

    if isinstance(btree, str):
        btree = bpy.data.node_groups.get(name)

    if btree is not None:
        bpy.data.node_groups.remove(btree)

# ====================================================================================================
# Stacked Tree

class StackedTree:

    def __init__(self):
        self.nodes = {}

    # ====================================================================================================
    # Some methods

    def __str__(self):
        return f"<Tree '{self.btree.name}' ({self.TREE_TYPE}): {len(self.btree.nodes)} nodes and {len(self.btree.links)} links>"

    @property
    def _str_stats(self):
        return f"{len(self.btree.nodes)} nodes, {len(self.btree.links)} links"

    def clear(self):
        self.btree.nodes.clear()

    @staticmethod
    def current_tree():
        return constants.current_tree()

    # ====================================================================================================
    # Stacking the Tree

    def _stack_init(self):
        pass

    def _stack_done(self):
        pass

    class Break(Exception):
        pass

    def __enter__(self):
        constants.TREE_STACK.append(self)
        self._stack_init()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        constants.TREE_STACK.pop()
        constants.FRAME_STACK.clear()

        self.arrange()
        self._stack_done()

        print(f"Tree '{self.btree.name}' built: {self._str_stats}")

        if isinstance(exc_value, self.Break):
            return True

    # ====================================================================================================
    # List of nodes

    def _register_node(self, node):
        self.nodes[node.bnode.name] = node

    def _bsocket_node(self, bsocket):
        node = self.nodes.get(bsocket.node.name)
        if node is None:
            for node in self.nodes.values():
                if bsocket.node == node.bnode:
                    return node

            print("List of tree nodes:")
            for name, node in self.nodes.items():
                print(f"{name:20s}") #" : {node}")
            print()

            raise Exception(f"Tree {self} has no node owning the socket '{bsocket.name}' in Blender node '{bsocket.node.name}'.")
        else:
            return node

    # ====================================================================================================
    # Group of trees

    @classmethod
    def prefixed(cls, name):
        if name is None:
            return Prefixed(cls.TREE_TYPE)
        elif isinstance(name, str):
            return Prefixed(cls.TREE_TYPE, name)
        else:
            return Prefixed(cls.TREE_TYPE, name.prefix)


    # ====================================================================================================
    # Base input nodes

    def boolean(self, boolean, node_label=None, node_color=None):
        """ Boolean input
        class_name = Boolean
        """
        return self.Boolean(boolean, node_label=node_label, node_color=node_color).output_socket

    def color(self, color, node_label=None, node_color=None):
        """ A color socket either from CombineColor or from Color
        class_name = Color
        """

        c = utils.value_for(color, 'NodeSocketColor')
        if isinstance(c, sockets.Socket):
            c.node.node_label = node_label
            c.node.node_color = node_color
            return c

        node = self.Color(node_label=node_label, node_color=node_color)
        node.bnode.color = c
        return node.output_socket

    def rgb_a(self, v, w):
        with self.layout("V4", node_color=constants.V4_COLOR):
            try:
                return self.rgb(v.x, v.y, v.z, w)
            except:
                pass

        raise AttributeError(f"Method rgb_a requires a vector and a float. First item is not a vector: {v}")



    def integer(self, integer, node_label=None, node_color=None):
        """ Integer input
        class_name = Integer
        """
        return self.Integer(integer, node_label=node_label, node_color=node_color).output_socket

    def string(self, string, node_label=None, node_color=None):
        """ String input
        class_name = String
        """
        return self.String(string, node_label=node_label, node_color=node_color).output_socket

    def value(self, value, node_label=None, node_color=None):
        """ Value input
        class_name = Value
        """
        node = self.Value(node_label=node_label, node_color=node_color)
        node.bnode.outputs[0].default_value = utils.value_for(value, 'NodeSocketFloat')
        return node.output_socket

    def float(self, value, node_label=None, node_color=None):
        """ Value input
        class_name = Value
        """
        return self.value(value, node_label=node_label, node_color=node_color)

    def vector(self, vector, node_label=None, node_color=None):
        """ Vector input
        class_name = Vector
        """
        v = utils.value_for(vector, 'NodeSocketVector')
        if isinstance(v, sockets.Socket):
            v.node.node_label = node_label
            v.node.node_color = node_color
            return v

        node = self.Vector(node_label=node_label, node_color=node_color)
        node.bnode.vector = v
        return node.output_socket

    def image(self, image, node_label=None, node_color=None):
        """ Image input
        class_name = Image
        """
        image = self.Image._image_value(image)
        return self.Image(image, node_label=node_label, node_color=node_color).output_socket


    def material(self, material, node_label=None, node_color=None):
        """ Material input
        class_name = Material
        """
        material = self.Material._material_value(material)
        return self.Material(material, node_label=node_label, node_color=node_color).output_socket

    @property
    def active_camera(self):
        return self.ActiveCamera().active_camera


# ====================================================================================================
# Node created in the current tree

class Node(object):

    def __init__(self, bl_idname, node_label=None, node_color=None, **kwargs):

        self.tree = constants.current_tree()
        if isinstance(bl_idname, str):
            self.bnode = self.tree.btree.nodes.new(type=bl_idname)
        else:
            self.bnode = bl_idname

        self.node_label = node_label
        self.node_color = node_color

        if len(constants.FRAME_STACK):
            self.bnode.parent = constants.FRAME_STACK[-1].bnode

        self.inputs  = sockets.Sockets(self, True)
        self.outputs = sockets.Sockets(self, False)

        # ----- Register the node

        self.tree._register_node(self)

        # ----------------------------------------------------------------------------------------------------
        # Separate params and sockets

        in_socks = {}
        params   = {}
        for k, v in kwargs.items():
            if k in self.params:
                params[k] = v
            else:
                in_socks[k] = v

        # ----------------------------------------------------------------------------------------------------
        # Set the params

        for param_name, param_value in params.items():
            self._set_parameter(param_name, param_value)

        # ----------------------------------------------------------------------------------------------------
        # Now that params are initialized, sockets have proper names
        # Get the valid socket names

        bsockets = self.inputs.sockets_pynames(enabled_only=False, label='BOTH')

        virtuals = {}
        for socket_name, socket_value in in_socks.items():
            if socket_name in bsockets.keys():
                self._set_input_socket(socket_name, socket_value)
            elif socket_value is not None:
                virtuals[socket_name] = socket_value

        # ----------------------------------------------------------------------------------------------------
        # Virtual sockets

        if len(virtuals) > 0:
            if not self.has_virtual_sockets:
                self.bad_input_exception(list(virtuals.keys())[0])

            for socket_name, socket_value in virtuals.items():

                if socket_value is None:
                    stype = 'GEOMETRY'
                else:
                    stype = utils.get_value_socket_type(value)

                if stype == 'VALUE':
                    stype = 'FLOAT'

                self._items.new(socket_type=stype, name=socket_name)
                self._set_input_socket(socket_name, socket_value)

    def __init__OLD(self, bl_idname, node_label=None, node_color=None, **kwargs):

        self.tree = constants.current_tree()
        if isinstance(bl_idname, str):
            self.bnode = self.tree.btree.nodes.new(type=bl_idname)
        else:
            self.bnode = bl_idname

        self.node_label = node_label
        self.node_color = node_color

        if len(constants.FRAME_STACK):
            self.bnode.parent = constants.FRAME_STACK[-1].bnode

        self.inputs  = sockets.Sockets(self, True)
        self.outputs = sockets.Sockets(self, False)

        # ----- Virtual sockets

        if len(kwargs) and not self.has_virtual_sockets:

            for bsock in self.inputs.bsockets:
                print(bsock.name, bsock.label)


            self.bad_input_exception(list(kwargs.keys())[0])
            #raise Exception(f"Node '{self.bnode.name}' ({self.bnode.bl_idname}) has no virtual socket. Impossible to set up sockets {kwargs}")

        for name, value in kwargs.items():

            if value is None:
                stype = 'GEOMETRY'
            else:
                stype = utils.get_value_socket_type(value)

            if stype == 'VALUE':
                stype = 'FLOAT'

            self._items.new(socket_type=stype, name=name)

        # ----- Register the node

        self.tree._register_node(self)

        # ----- Set the sockets

        for name, value in kwargs.items():
            setattr(self, name, value)

    def __enter__(self):
        if self.bnode.bl_idname != 'NodeFrame':
            raise Exception(f"Only a node of type Frame can be the parent of new nodes, not node of type '{self.bnode.bl_idname}'")

        constants.FRAME_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        constants.FRAME_STACK.pop()

    def __str__(self):
        return f"<Node  {type(self).__name__} '{self.bnode.name}'>"

    # ====================================================================================================
    # Node label and color

    @property
    def node_label(self):
        if self.bnode.label == '':
            return self.bnode.name
        else:
            return self.bnode.label

    @node_label.setter
    def node_label(self, value):
        if value is None:
            return
        self.bnode.label = value

    @property
    def node_color(self):
        pass

    @node_color.setter
    def node_color(self, value):
        if value is None:
            self.bnode.use_custom_color = False
        else:
            self.bnode.use_custom_color = True
            self.bnode.color = value

    # ====================================================================================================
    # Parameter

    def _get_parameter(self, param):
        return getattr(self.bnode, param)

    def _set_parameter(self, param, value):
        if value is None:
            return

        try:
            setattr(self.bnode, param, value)

        except TypeError as e:

            s = str(e)
            msg = "not found in "
            i = s.find(msg)
            s = s[i+len(msg):]

            print('-'*80)
            print("Error when setting node parameter:")
            print(f"   Node     : {self.bnode.name}")
            print(f"   Parameter: {param}")
            print(f"   Value    : {value}")
            print(f"   Expected : {s}")
            print('-'*80)
            print()

            raise

    # ====================================================================================================
    # Sockets

    def bad_socket_exception(self, pyname, is_output=True):

        if is_output:
            valids = list(self.outputs.sockets_pynames(label='BOTH').keys())
        else:
            valids = list(self.inputs.sockets_pynames(label='BOTH').keys())

        print('-'*80)
        print(f"{'Output' if is_output else 'Input'} socket name error:")
        print(f"   Node               : {self}")
        print(f"   Wrong socket name  : {pyname}")
        print(f"   Valid socket names : {valids}")
        print('-'*80)
        print()

        raise AttributeError(f"{'Output' if is_output else 'Input'} socket name error: '{pyname}'")

    def bad_input_exception(self, name):

        print('-'*80)
        print("Node initialization error: wrong input socket or param name")
        print(f"   Node        : {self}")
        print(f"   Wrong name  : '{name}")
        print(f"   Valid names : {self.valid_inputs}")
        print(f"   Parameters  : {self.params}")
        print(f"   Sockets     : {sorted(list(self.inputs.sockets_pynames(enabled_only=False, label='BOTH').keys()))}")
        print('-'*80)
        print()

        raise AttributeError(f"Node initialization error: wrong input socket or param name: '{name}'")

    def _get_output_socket(self, pyname):
        bsock = self.outputs.sockets_pynames().get(pyname)
        if bsock is None:
            self.bad_socket_exception(pyname, is_output=True)

        return sockets.Socket(bsock)

    def _set_input_socket(self, pyname, value):

        if value is None:
            return

        bsock = self.inputs.sockets_pynames(label='BOTH').get(pyname)
        if bsock is None:
            bsock = self.inputs.sockets_pynames(enabled_only=False, label='BOTH').get(pyname)
            if bsock is None:
                self.bad_socket_exception(pyname, is_output=False)

        sockets.Socket(bsock)._set_value(value)

    def _set_multi_input(self, *args):
        mi_socket = self.inputs.get_multi_input_socket(halt=True)
        for arg in args:
            mi_socket._set_value(arg)

    @property
    def output_socket(self):
        return self.outputs.output

    # ====================================================================================================
    # Utilities

    @staticmethod
    def _color_value(value):
        return utils.value_for(value, 'NodeSocketColor')

    @staticmethod
    def _material_value(value):
        return utils.value_for(value, 'NodeSocketMaterial')

    @staticmethod
    def _image_value(value):
        return utils.value_for(value, 'NodeSocketImage')

    # ====================================================================================================
    # Dynamic sockets

    @property
    def has_virtual_sockets(self):
        return self.bl_idname in constants.HAS_VIRTUAL_SOCKETS

    @property
    def _items(self):
        return getattr(self.bnode, constants.HAS_VIRTUAL_SOCKETS.get(self.bl_idname))

    def __getattr__(self, name):

        outputs = self.__dict__.get('outputs')
        if outputs is not None: # and type(self).dynamic_out:
            bsocket = outputs.sockets_pynames(enabled_only=True, label='BOTH').get(name)
            if bsocket is not None:
                return sockets.Socket(bsocket)

        if outputs is None:
            raise AttributeError(f"Node '{self.bl_idname}' has no attribute named '{name}'")
        else:
            self.bad_socket_exception(name, is_output=True)

    def __setattr__(self, name, value):
        inputs = self.__dict__.get('inputs')
        if inputs is not None and type(self).dynamic_in:
            bsocket = inputs.sockets_pynames(enabled_only=True).get(name)
            if bsocket is not None:
                sockets.Socket(bsocket)._set_value(value)
                return

        super().__setattr__(name, value)

    def _input_socket_exists(self, name):
        return self.inputs.sockets_pynames(enabled_only=True).get(name) is not None

    # ====================================================================================================
    # Documentation

    @classmethod
    def print_doc(cls):
        documentation.print_doc(cls)

    # ====================================================================================================
    # Plug one node into another

    def plug_to(self, other):

        tree = constants.current_tree()

        outs = self.outputs.sockets_pynames(enabled_only=True)
        ins  = other.inputs.sockets_pynames(enabled_only=True)

        for out_key, out_bsock in outs.items():
            for in_key, in_bsock in ins.items():
                if in_key == out_key and in_bsock.bl_idname == out_bsock.bl_idname:
                    tree.btree.links.new(in_bsock, out_bsock)
                    break

    # ====================================================================================================
    # Uggly hacks

    @property
    def hue(self):
        if type(self).__name__ == 'SeparateColor' and self.bnode.mode in ['HSL', 'HSV']:
            return self.red
        else:
            # To raise an error message
            return self.__getattr__('hue')

    @property
    def saturation(self):
        if type(self).__name__ == 'SeparateColor' and self.bnode.mode in ['HSL', 'HSV']:
            return self.green
        else:
            # To raise an error message
            return self.__getattr__('saturation')

    @property
    def value(self):
        if type(self).__name__ == 'SeparateColor' and self.bnode.mode in ['HSV']:
            return self.blue
        else:
            # To raise an error message
            return self.__getattr__('value')

    @property
    def lightness(self):
        if type(self).__name__ == 'SeparateColor' and self.bnode.mode in ['HSL']:
            return self.blue
        else:
            # To raise an error message
            return self.__getattr__('lightness')

# ====================================================================================================
# Specific nodes

# ----------------------------------------------------------------------------------------------------
# Index Switch

class IndexSwitchNode(Node):
    def __init__(self, *args, index=None, data_type=None, node_label=None, node_color=None, **kwargs):
        """
        ``` python
        IndexSwitch(*args, index=None, data_type=None, node_label=None, node_color=None, **kwargs)
        ```

        ## Arguments
        - args (Sockets) : the sockets to pick into
        - index (integer Socket) : selection index
        - data_type (str=None) : type of value sockets. If None, data_type is deduced from kwargs data types
        - kwargs : socket name -> socket to select from

        > [!NOTE]
        > The total number of sockets is the sum of the number of items in args and in kwargs

        > [!CAUTION]
        > Keys of kwargs dict must be a socket number : '**_0**', '**_1**', '**_2**', ...

        ## Example

        In the following example, the node is initialized with a list of 3 geometries passed as non keyed arguments
        and one addtional geometry passed as keyed argument.

        ``` python
        with GeoNodes("Test") as tree:

            node = tree.IndexSwitch(
                tree.ico_sphere(), tree.cube(), tree.cone(),
                index = tree.integer_input("Shape", 0),
                _1 = tree.ig)

            tree.og = node.output
        ```
        """

        bnode = constants.current_tree().btree.nodes.new(type='GeometryNodeIndexSwitch')
        bnode.index_switch_items.clear()

        super().__init__(bnode, node_label=node_label, node_color=node_color)

        self.data_type = utils.get_type_from_sockets(list(args) + list(kwargs.values())) if data_type is None else data_type
        self.index = index

        # ----- Create the entries

        n = len(args) + len(kwargs)
        for _ in range(n):
            self.bnode.index_switch_items.new()

        # ----- Plug the entries

        plugged = []
        for k, v in kwargs.items():
            if not k[1:].isnumeric():
                raise Exception(f"Node 'Index Switch' initialization error: socket name '{k}' is not valid ; node needs socket named '_x' (x is the socket number)")
            setattr(self, k, v)
            plugged.append(int(k[1:]))

        for val in args:
            for i in range(n):
                if i not in plugged:
                    setattr(self, f"_{i}", val)
                    plugged.append(i)
                    break

    @property
    def index(self):
        return None

    @index.setter
    def index(self, value):
        sockets.Socket(self.inputs["Index"])._set_value(value)

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    def __setattr__(self, name, value):

        inputs = self.__dict__.get('inputs')
        if inputs is not None:
            if name[0] == '_' and name[1:].isnumeric():
                i = int(name[1:])
                bsocket = inputs.sockets_pynames(enabled_only=True).get(name)
                if bsocket is not None:
                    sockets.Socket(bsocket)._set_value(value)
                    return

        super().__setattr__(name, value)

# ----------------------------------------------------------------------------------------------------
# Menu Switch

class MenuSwitchNode(Node):

    def __init__(self, menu=None, data_type=None, node_label=None, node_color=None, **kwargs):
        """
        ``` python
        MenuSwitch(menu=None, data_type=None, node_label=None, node_color=None, **kwargs)
        ```

        ## Arguments
        - menu (Socket=None) : Socket Menu
        - data_type (str=None) : type of value sockets. If None, data_type is deduced from kwargs data types
        - kwargs : socket name -> socket to select from menu

        ## Default sockets

        In the editor, this node is created with predefined sockets name A and B.
        Here, there is no predefined sockets. The names can be freely chosen.

        ## Menu socket

        Generally, the menu socket is read from group input. There is two manners to create a group input dedicated
        to the menu socket.

        The first way is to explicitly create a menu socket with `tree.menu_input`. Since this method needs an
        existing socket, it must be created afterwards.

        As a reminder, input sockets are write only attributes. To get an input socket, it is necessary to use
        the `inputs` list.

        ``` python
        with GeoNodes("Test") as tree:
            switch_node = tree.MenuSwitch(sphere=tree.ico_sphere(), cube=tree.cube(), cone=tree.cone())
            # Input sockets are write only
            tree.menu_input("Shape", switch_node.inputs["Menu"])
            tree.og = switch_node.output
        ```

        Since there is only one input menu, it is possible to pass directly the node rather than its menu socket:

        ``` python
        with GeoNodes("Test") as tree:
            switch_node = tree.MenuSwitch(sphere=tree.ico_sphere(), cube=tree.cube(), cone=tree.cone())
            # menu_input method will take the first input menu socket
            tree.menu_input("Shape", switch_node)
            tree.og = switch_node.output
        ```

        ## Dynamic creation

        The other way to create the group menu socket is to use the method `input_for_socket` as value
        for the `menu` socket. This method accepts the name of the socket to create as an argument.
        The following code is equivalent as the two previous pieces:

        ``` python
        switch_node = tree.MenuSwitch(
            menu   = tree.input_for_socket("Shape"),
            sphere = tree.ico_sphere(),
            cube   = tree.cube(),
            cone   = tree.cone())

        tree.og = switch_node.output
        ```
        """

        bnode = constants.current_tree().btree.nodes.new(type='GeometryNodeMenuSwitch')
        bnode.enum_definition.enum_items.clear()

        super().__init__(bnode, node_label=node_label, node_color=node_color)

        self.data_type = utils.get_type_from_sockets(list(kwargs.values())) if data_type is None else data_type

        # ----- Create the entries

        for k in kwargs:
            self.bnode.enum_definition.enum_items.new(k)

        # ----- Plug the entries

        for k, v in kwargs.items():
            setattr(self, k.lower(), v)

        # ----- Set the menu

        self.menu = menu




    @property
    def menu(self):
        return None

    @menu.setter
    def menu(self, value):
        if value is not None:
            sockets.Socket(self.inputs["Menu"])._set_value(value)

    @property
    def data_type(self):
        return self.bnode.data_type

    @data_type.setter
    def data_type(self, value):
        self.bnode.data_type = value

    def __setattr__(self, name, value):

        inputs = self.__dict__.get('inputs')
        if inputs is not None:
            bsocket = inputs.sockets_pynames(enabled_only=True).get(name)
            if bsocket is not None:
                sockets.Socket(bsocket)._set_value(value)
                return

        super().__setattr__(name, value)




# ====================================================================================================
# A group of trees

class Prefixed:

    def __init__(self, tree_type, prefix=None):
        """ A group of trees.

        Names are prefixed.

        Arguments
        ----------
            - tree_type (str) : Tree bl_idname
            - prefix (str = None) : The prefix to use
        """

        self.tree_type = tree_type

        if prefix is None:
            self.prefix = ""
        elif isinstance(prefix, Prefixed):
            self.prefix = prefix.prefix
        else:
            self.prefix = prefix.strip() + " "

    def __str__(self):
        return f"<Group of trees prefixed by '{self.prefix.strip()}'>"

    def prefixed_name(self, name):
        """ Compute the prefixed name.

        Arguments
        ---------
            - name (str): the tree name

        Returns
        -------
            - str : prefixed name (str)
        """
        return self.prefix + name

    @staticmethod
    def python_name(name):
        """ The snake version of the prefixed name.

        The prefixed version is used as a function name to instantiate the custom group.

        Arguments
            - name (str): the tree name

        Returns
        -------
            - str = snake_case version of the prefixed name (str)
        """
        pname = name.lower().replace(' ', '_').replace('-','_')
        if pname[0].isnumeric():
            pname = '_' + pname
        return pname

    @property
    def trees(self):
        """ Gives the list of the [Tree](Tree.md) sharing the same prefix.

        Returns
        -------
            - dict : Trees sharing the same prefix (list)
        """
        if self.prefix == "":
            return {self.python_name(tree.name): tree for tree in bpy.data.node_groups if tree.bl_idname == self.tree_type}

        trees = {}
        for tree in bpy.data.node_groups:

            if tree.bl_idname != self.tree_type:
                continue

            if tree.name[:len(self.prefix)] == self.prefix:
                trees[self.python_name(tree.name[len(self.prefix):])] = tree

        return trees

    def __len__(self):
        return len(self.trees)

    def __getitem__(self, name):
        key = self.python_name(name)
        return self.trees.get(key)

    def clear(self):
        """ Delete all the **Trees** whose name has a given prefix.

        For instance, to delete all the **Geometry Nodes** whose name starts with 'Utils':
        """

        trees = self.trees
        for tree in trees.values():
            bpy.data.node_groups.remove(tree)

    # ----------------------------------------------------------------------------------------------------
    # Stats

    @property
    def _nodes_links_count(self):
        nodes = 0
        links = 0
        for tree in self.trees.values():
            reroutes = [node for node in tree.nodes if node.bl_idname in ['NodeReroute']]
            nodes += len(tree.nodes) - len(reroutes)
            links += len(tree.links) - len(reroutes)
        return nodes, links

    # ----------------------------------------------------------------------------------------------------
    # Call Group as tree attribute

    def __getattr__(self, name):

        tree = self.trees.get(self.python_name(name))
        if tree is None:
            print("TREES", list(self.trees.keys()))
            raise AttributeError(f"Tree named '{name}' not found in {self}")

        def f(*args, **kwargs):
            cur_tree = constants.current_tree()
            return cur_tree.group(tree.name, *args, **kwargs)

        return f

    # ----------------------------------------------------------------------------------------------------
    # Call with its user name

    def call(self, name, **kwargs):

        cur_tree = constants.current_tree()
        return cur_tree.group(self.prefixed_name(name), **kwargs)
