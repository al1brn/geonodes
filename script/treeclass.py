#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
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

functions
---------

updates
-------
- creation : 2024/07/23
"""

import numpy as np
import bpy

from .scripterror import NodeError
from . import treearrange
from . import constants
from . import utils
from . import blendertree

# =============================================================================================================================
# Break to exit with blocks

class Break(Exception):
    pass

# =============================================================================================================================
# Layout

class Layout:
    def __init__(self, label=None, color=None):
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

    def __init__(self, tree_name, tree_type='GeometryNodeTree', clear=True, fake_user=False, is_group=False, prefix=None):

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
            self._btree = blendertree.get_tree(tree_name, tree_type=tree_type, create=True)
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
        if not cls.STACK:
            raise NodeError(f"No tree is open")
        return cls.STACK[-1]

    #@property
    #def NODE_NAMES(self):
    #    return constants.NODE_NAMES[self._btree.bl_idname]

    # ----------------------------------------------------------------------------------------------------
    # Gen code utility

    @property
    def _node_infos(self):
        from .node_explore import NodeInfo
        return [NodeInfo(self._btree, bnode) for bnode in self._btree.nodes]

    # ====================================================================================================
    # Some methods

    def __str__(self):
        return f"<Tree '{self._btree.name}' ({type(self).__name__}): {len(self._btree.nodes)} nodes and {len(self._btree.links)} links>"

    @classmethod
    def _reset_counters(cls):
        cls._total_nodes = 0
        cls._total_links = 0

    @classmethod
    @property
    def is_geonodes(cls):
        return cls.current_tree._btree.bl_idname == 'GeometryNodeTree'

    @classmethod
    @property
    def is_shader(cls):
        return cls.current_tree._btree.bl_idname == 'ShaderNodeTree'

    @classmethod
    @property
    def is_compositor(cls):
        return cls.current_tree._btree.bl_idname == 'CompositorNodeTree'

    @property
    def _str_stats(self):
        return f"{len(self._btree.nodes)} nodes, {len(self._btree.links)} links"

    def clear(self):
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
        Tree.STACK.append(self)

    def pop(self):
        tree = Tree.STACK.pop()
        if tree != self:
            raise NodeError(f"Error in tree stack management")

        self.arrange()

        print(f"Tree '{self._btree.name}' built: {self._str_stats}")

        Tree._total_nodes += len(self._btree.nodes)
        Tree._total_links += len(self._btree.links)

    def __enter__(self):
        return self

    def __exit__(self, type, exc_value, traceback):

        self.pop()

        if isinstance(exc_value, Break):
            return True


    # =============================================================================================================================
    # Arranges nodes

    def arrange(self):
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

        if hasattr(out_socket, '_bsocket'):
            out_socket = out_socket._bsocket

        if hasattr(in_socket, '_bsocket'):
            in_socket = in_socket._bsocket

        return self._btree.links.new(out_socket, in_socket)

    # =============================================================================================================================
    # Tree Input / Output

    @property
    def input_node(self):
        for node in self._nodes:
            if node._bnode.bl_idname ==  'NodeGroupInput':
                return node
        return Node('NodeGroupInput')

    @property
    def output_node(self):
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

        This is an input socket of the tree, then an output socket of the input node.

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

        This is an output socket of the tree, then an input socket of the input node.

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

        from geonodes.script import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, String, Menu

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
    def __init__(self, node_name, sockets={}, _keep=None, **parameters):

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

        # ----- Is the node kept from previous version

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

        # ----- Configuration
        # Parameters first to configure the sockets

        self.set_parameters(**parameters)
        self.set_input_sockets(sockets)

        # ----- Register the node

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
    # Create a DataSocket from an output Blender NodeSocket

    @staticmethod
    def data_socket(bsocket):

        socket_type = bsocket.type

        if Tree.is_geonodes:
            from .geonodes import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, Geometry, Material, Image, Object, Collection, String, Menu
            from .geonodes import Mesh, Curve, Cloud, Volume, Instances


            socket_class = {'BOOLEAN': Boolean, 'INT': Integer, 'VALUE': Float, 'VECTOR': Vector, 'ROTATION': Rotation, 'MATRIX': Matrix, 'RGBA': Color,
                'STRING': String, 'MENU': Menu,
                    'GEOMETRY': Geometry,
                    'MATERIAL': Material, 'IMAGE': Image, 'OBJECT': Object, 'COLLECTION': Collection,
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
            from .shadernodes import Float, Vector, Rotation, Color, String, Shader

            socket_class = {'VALUE': Float, 'VECTOR': Vector, 'ROTATION': Rotation, 'RGBA': Color, 'STRING': String, 'SHADER': Shader,
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

        try:
            bsocket = bsockets[name]
        except:
            bsocket = None
            for bsock in bsockets:
                if not bsock.enabled:
                    continue

                if bsock.name == bsocket or utils.socket_name(bsock.name) == name:
                    bsocket = bsock
                    break

        if halt and bsocket is None:
            raise NodeError(f"Socket name '{name}' not found in node '{self._bnode.name}' ({self._bnode.bl_idname})",
                valids = [sock.name for sock in bsockets])

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
            for v in value:
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
            self._tree.link(out_socket, in_socket)
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
    # Plug another node into self
    # If the other node is None, the Tree input node is taken
    # Create is only valid in this case

    def plug_node_into(self, node=None, include=None, exclude={}, rename={}, create=True):

        tree = self._tree

        # ----------------------------------------------------------------------------------------------------
        # Node with output sockets to plug

        if node is None:
            node = tree.input_node
        else:
            create = False

        is_node_group = self._bnode.bl_idname == 'GeometryNodeGroup'

        # ----------------------------------------------------------------------------------------------------
        # Loop on the input sockets of self

        for in_socket in self._bnode.inputs:

            if in_socket.type == 'CUSTOM':
                continue

            # ----- Already linked

            if in_socket.is_linked:
                continue

            # ----- Socket name can be remapped

            socket_name = in_socket.name
            if socket_name in rename.keys():
                out_name = rename[socket_name]
            else:
                out_name = socket_name

            # ----- Look for an output socket of same name and type

            out_socket = None
            for out_sock in node._bnode.outputs:
                if out_sock.name == out_name and out_sock.type == in_socket.type:
                    out_socket = out_sock
                    break
            if out_socket is None and not create:
                continue

            # ----- Must be in the sockets to include

            if include is not None and socket_name not in include:
                if not socket_name in rename.keys():
                    continue

            # ----- Must not be in the sockets to exclude

            if socket_name in exclude:
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

        Create a node 'Group' with the tree provided with 'group_name' argument.

        The sockets can be initialized either using the sockets dictionary or using they snake_case name
        as kwargs arguments.

        ``` python
        # Call a group by initializing the sockets with their name
        node = Group("Group Name", sockets={'Geometry': Geometry(), 'Value': 1, 'Factor': 2})

        # Call the group by initializing the sockets with their snake_case name
        node = Group("Group Name", geometry=Geometry, value=1, factor=2)

        # Get the result from the group computation

        res_geo = node.geometry
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
        return cls(f"{prefix} {group_name}", sockets=sockets, **kwargs)

class GroupF:

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
