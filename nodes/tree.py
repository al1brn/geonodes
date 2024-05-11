#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:55:10 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : tree
-------------
- Tree root class
- GeoNodes for Geometry Nodes trees
- Shader for Shader Nodes trees
- Compositor for Compositor Nodes Trees
- Texture for Texture Nodes Trees

update : 2024/02/17
update : 2024/03/29
"""

from pprint import pprint

import numpy as np

import bpy
from geonodes.nodes import documentation
from geonodes.nodes import constants
from geonodes.nodes import utils
from geonodes.nodes import treestack
from geonodes.nodes import sockets
from geonodes.nodes.treestack import StackedTree, Prefixed
from geonodes.nodes.sockets import Socket, Sockets
from geonodes.nodes import nodeinfo

from geonodes.nodes.treearrange import arrange


# ====================================================================================================
# A tree

class Tree(StackedTree):

    pi = 3.1415926535898

    # ====================================================================================================
    # Initialization

    def __new__(cls, *args, **kwargs):
        """ Initialize dynamic classes if the class is not yet initialized
        """

        if not cls.INIT:

            cls._setup()

            #nodeinfo.tree_class_setup(cls) #.TREE_TYPE)

            #cls.INIT = True

        return StackedTree.__new__(cls)

    # ----------------------------------------------------------------------------------------------------
    # init

    def __init__(self, name, create=True, clear=True, fake_user=False, is_group=False, prefix=None):
        """ Tree of Nodes.

        Arguments
        ---------
            - name (str) : Tree name
            - create (bool = True) : create the tree if it doesn't exist
            - clear (bool = False) : erase the existing nodes
            - is_group (bool = False) : initialize as a ground
            - prefix (str = None) : prefix to use in the name
        """

        super().__init__()

        self.is_group = is_group

        # ----- Load the btree

        if isinstance(name, str):
            name = self.prefixed(prefix).prefixed_name(name)
            self.btree = treestack.get_tree(name, self.TREE_TYPE, create=create, clear=False)

        else:
            self.btree = name

        if hasattr(self.btree, 'is_modifier'):
            self.btree.is_modifier = not self.is_group

        self.btree.use_fake_user = fake_user

        if clear:
            self.clear()

    # ====================================================================================================
    # setup the class

    @classmethod
    def _setup(cls):
        nodeinfo.tree_class_setup(cls) #.TREE_TYPE)
        cls.INIT = True


    # ====================================================================================================
    # For debug

    @classmethod
    def _reset(cls):
        #cls.INIT = False
        constants.reset()

    # ====================================================================================================
    # Arrange

    def arrange(self):
        """ Arrange the nodes.
        """

        arrange(self.btree)
        return self

    # ====================================================================================================
    # Get a node by its bl_idname

    def get_node(self, bl_idname, create=True):
        """ Get a node by its bl_idname, optionaly create it if it doesn't exist.

        Arguments
        ---------
            - bl_idname (str) : node bl_idname
            - create (bool = True) : create the node if it doesn't exist

        Returns
        -------
            - Node or None if not found
        """

        for node in self.nodes.values():
            if node.bl_idname == bl_idname:
                return node

        if create:
            return constants.get_node_class(self.TREE_TYPE, bl_idname)()
        else:
            return None

    def get_nodes(self, bl_idname):
        """ Get all the nodes of a given bl_idname.

        Arguments
        ---------
            - bl_idname (str) : node bl_idname

        Returns
        -------
            - list of Node
        """

        nodes = []
        for node in self.nodes.values():
            if node.bl_idname == bl_idname:
                nodes.append(node)
        return nodes

    # ====================================================================================================
    # Tree inputs / outputs

    @property
    def input_node(self):
        """ Tree input Node

        Returns
        -------
            - Node or None
        """

        return None

    @property
    def output_node(self):
        """ Tree output Node

        Returns
        -------
            - Node or None
        """
        return None

    # ----------------------------------------------------------------------------------------------------
    # Check if an interface socket exists

    def io_socket_exists(self, bl_idname, in_out='INPUT', name=None):

        for item in self.btree.interface.items_tree:
            if item.item_type != 'SOCKET' or item.in_out != in_out or item.socket_type != bl_idname:
                continue
            if name is None or item.name == name:
                return item

        return None

    # ----------------------------------------------------------------------------------------------------
    # Create an new interface socket

    def new_io_socket(self, bl_idname, in_out, name):
        return self.btree.interface.new_socket(name=name, in_out=in_out, socket_type=bl_idname)

    # --------------------------------------------------------------------------------
    # Clear interface

    def clear_io_sockets(self):
        self.btree.interface.clear()

    # --------------------------------------------------------------------------------
    # Create a new input socket

    def new_input(self, bl_idname, name, subtype='NONE',
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

        # ----- Input node

        input_node = self.input_node

        # ----- Socket class

        socket_class = constants.get_socket_class_from_bl_idname(self.TREE_TYPE, bl_idname)

        # ----------------------------------------------------------------------------------------------------
        # Get or create

        io_socket = self.io_socket_exists(bl_idname, 'INPUT', name)

        if io_socket is None:
            io_socket = self.new_io_socket(bl_idname, 'INPUT', name)
            set_value = True
        else:
            set_value = False

        if hasattr(io_socket, 'subtype'):
            io_socket.subtype = subtype
        socket = socket_class(input_node.bnode.outputs[io_socket.identifier])

        # ----------------------------------------------------------------------------------------------------
        # Let's apply the constraints

        if min_value is not None:
            io_socket.min_value = min_value

        if max_value is not None:
            io_socket.max_value = max_value

        io_socket.description = description

        # ----------------------------------------------------------------------------------------------------
        # Let's set the value if the socket is created
        # Note: if the socket already exists, we don't override its value

        if (value is not None) and set_value:

            v = utils.value_for(value, bl_idname)

            msg1 = None
            msg2 = None
            try:
                io_socket.default_value = v
            except Exception as e:
                msg1 = str(e)

            try:
                socket.bsocket.default_value = v
            except Exception as e:
                msg2 = str(e)

            if msg1 is not None:
                print("CAUTION 1", name, socket.bsocket.bl_idname, io_socket.bl_socket_idname, ">", msg1)
                #print(dir(self.tree.btree.inputs[index]))

            if msg2 is not None:
                print("CAUTION 2", name, socket.bsocket.bl_idname, io_socket.bl_socket_idname, ">", msg2)

            # ---------------------------------------------------------------------------
            # Set the default value to all modifiers using it
            #
            # The tree inputs store the default value of the sockets
            # The values themselves are stored in properties in the object modifiers
            # The modifier property is key by the tree input identifier

            for obj in bpy.data.objects:
                for mod in obj.modifiers:
                    if isinstance(mod, bpy.types.NodesModifier):
                        if mod.node_group == self.btree:
                            mod[io_socket.identifier] = value

        return socket

    # --------------------------------------------------------------------------------
    # Create a new input socket

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

        # ----- Socket class

        socket_class = constants.nodesocket_classes()[bl_idname]

        # ----------------------------------------------------------------------------------------------------
        # Get or create

        io_socket = self.io_socket_exists(bl_idname, 'OUTPUT', name)

        if io_socket is None:
            io_socket = self.new_io_socket(bl_idname, 'OUTPUT', name)

        return socket_class(output_node.bnode.inputs[io_socket.identifier])

    # ----------------------------------------------------------------------------------------------------
    # Socket to output

    def to_output(self, socket, name=None):
        """ Plug a socket to an output socket.

        Arguments
        ---------
            - socket (Socket) : the socket to plug to the output
            - name (str = None) : output socket name
        """

        # ----------------------------------------------------------------------------------------------------
        # Get or create

        bl_idname = utils.nodesocket_main_class(socket.bsocket.bl_idname)

        io_socket = self.io_socket_exists(bl_idname, 'OUTPUT', name)

        if io_socket is None:
            io_socket = self.new_io_socket(bl_idname, 'OUTPUT', name)

        if True:
            socket_class = constants.get_socket_class(socket.bsocket.type)
            out_socket = socket_class(self.output_node.bnode.inputs[io_socket.identifier])
            out_socket._set_value(socket)

        else:
            socket_class = constants.nodesocket_classes()[bl_idname]
            out_socket = socket_class(self.output_node.bnode.inputs[io_socket.identifier])
            out_socket._set_value(socket)


    # ====================================================================================================
    # Short cuts

    def bool_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketBool', name, value=value, description=description)

    def boolean_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketBool', name, value=value, description=description)

    # ----- Float subtypes

    def float_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, value=value, min_value=min_value, max_value=max_value, description=description)

    def value_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, value=value, min_value=min_value, max_value=max_value, description=description)

    def percentage_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, subtype='PERCENTAGE', value=value, min_value=min_value, max_value=max_value, description=description)

    def factor_input(self, name, value=None, min_value=0, max_value=1, description=""):
        return self.new_input('NodeSocketFloat', name, subtype='FACTOR', value=value, min_value=min_value, max_value=max_value, description=description)

    def angle_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, subtype='ANGLE', value=value, min_value=min_value, max_value=max_value, description=description)

    def time_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, subtype='TIME', value=value, min_value=min_value, max_value=max_value, description=description)

    def time_absolute_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, subtype='TIME_ABSOLUTE', value=value, min_value=min_value, max_value=max_value, description=description)

    def distance_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketFloat', name, subtype='DISTANCE', value=value, min_value=min_value, max_value=max_value, description=description)

    # ----- Integer subtypes

    def int_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketInt', name, value=value, min_value=min_value, max_value=max_value, description=description)

    def integer_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketInt', name, value=value, min_value=min_value, max_value=max_value, description=description)

    def int_factor_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketInt', name, subtype='FACTOR', value=value, min_value=min_value, max_value=max_value, description=description)

    def int_percentage_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketInt', name, subtype='PERCENTAGE', value=value, min_value=min_value, max_value=max_value, description=description)

    # ----- Vector subtypes

    def vector_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, value=value, min_value=min_value, max_value=max_value, description=description)

    def translation_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, subtype='TRANSLATION', value=value, min_value=min_value, max_value=max_value, description=description)

    def direction_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, subtype='DIRECTION', value=value, min_value=min_value, max_value=max_value, description=description)

    def velocity_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, subtype='VELOCITY', value=value, min_value=min_value, max_value=max_value, description=description)

    def acceleration_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, subtype='ACCELERATION', value=value, min_value=min_value, max_value=max_value, description=description)

    def euler_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, subtype='EULER', value=value, min_value=min_value, max_value=max_value, description=description)

    def xyz_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketVector', name, subtype='XYZ', value=value, min_value=min_value, max_value=max_value, description=description)

    # ----- Other inputs

    def rotation_input(self, name, value=None, min_value=None, max_value=None, description=""):
        return self.new_input('NodeSocketRotation', name, value=value, min_value=min_value, max_value=max_value, description=description)

    def string_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketString', name, value=value, description=description)

    def color_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketColor', name, value=value, description=description)

    def geometry_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketGeometry', name, value=value, description=description)

    def collection_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketCollection', name, value=value, description=description)

    def image_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketImage', name, value=value, description=description)

    def material_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketMaterial', name, value=value, description=description)

    def object_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketObject', name, value=value, description=description)

    def texture_input(self, name, value=None, description=""):
        return self.new_input('NodeSocketTexture', name, value=value, description=description)

    # ----- Menu input

    def menu_input(self, name, value, description=""):
        out_socket = self.new_input('NodeSocketMenu', name, description=description)
        out_socket.plug_in(value)
        return out_socket

    # ----------------------------------------------------------------------------------------------------
    # Create a socket from an input socket

    def input_from_socket(self, socket, name=None):

        if name is None:
            name = socket.bsocket.name
        blid = socket.bsocket.bl_idname

        io_socket = self.io_socket_exists(blid, 'INPUT', name)
        if io_socket is None:
            interface = self.btree.interface
            io_socket = interface.new_socket(name, in_out='INPUT', socket_type=blid)

        io_socket.from_socket(socket.node.bnode, socket.bsocket)

        socket_class = constants.get_socket_class_from_bl_idname(self.TREE_TYPE, blid)
        return socket_class(self.input_node.bnode.outputs[io_socket.identifier])

    def inputs_from_node(self, node, exclude=None, include=None):

        sockets = []

        for socket in node.inputs:
            name = socket.bsocket.name
            if exclude is not None and name in exclude:
                continue
            if include is not None and name not in include:
                continue

            sockets.append(self.input_from_socket(socket))

        return sockets

    # ----------------------------------------------------------------------------------------------------
    # Create dynamically an group input socket as an argument of node creation
    #
    # Use syntax:
    # node = tree.Node(value=tree.input_for_socket("Parameter"))
    #
    # Implemented

    def input_for_socket(self, name=None):

        def create_func(socket):
            return self.input_from_socket(socket, name=name)

        return create_func

    # ====================================================================================================
    # Group management

    @staticmethod
    def prefixed_name(name, prefix):
        if prefix is None or prefix == "":
            return name
        if prefix[-1] == ' ':
            return prefix + name
        else:
            return prefix + ' ' + name

    @classmethod
    def get_group_btree(cls, name, prefix=None):
        name = cls.prefixed_name(name, prefix)
        btree = bpy.data.node_groups.get(name)
        if btree.bl_idname != cls.TREE_TYPE:
            return None
        else:
            return btree

    @classmethod
    def get_group_btrees(cls, prefix):

        btrees = []

        if prefix is None or prefix == "":
            return btrees

        pref = prefix if prefix[-1] == " " else prefix + " "
        for btree in bpy.data.node_groups:
            if btree.bl_idname != cls.TREE_TYPE:
                continue
            if btree.name[:len(pref)] == pref:
                btrees.append(btree)

        return btrees

    @classmethod
    def clear_group(cls, prefix):
        btrees = cls.get_group_btrees(prefix)
        for btree in btrees:
            bpy.data.node_groups.remove(btree)

    def group(self, name, *args, **kwargs):

        # ----- Get the tree

        group_tree = bpy.data.node_groups.get(name)
        if group_tree is None:
            raise AttributeError(f"Impossible to find the group named '{name}'")

        # ----- Create the node group

        node = self.Group()

        # Name Group will change
        del self.nodes[node.bnode.name]

        node.bnode.name = group_tree.name
        node.bnode.node_tree = group_tree

        # Register with new name
        self._register_node(node)

        # ----- Set the input sockets

        all_kwargs = {}
        keys = list(node.inputs.socket_names)
        for i, value in enumerate(args):
            if i >= len(keys):
                raise AttributeError(f"Node Group '{name}' error: the number of args ({len(args)}) is greater than the number of sockets: {keys}")
            all_kwargs[keys[i]] = value

        for k, v in kwargs.items():
            if k in all_kwargs:
                raise AttributeError(f"Node Group '{name}' error: key argument {k} is already set with arg={all_kwargs[k]}")
            all_kwargs[k] = v

        for k, v in all_kwargs.items():
            if not node._input_socket_exists(k):
                raise AttributeError(f"Node group '{name}' error: no input socket named '{k}' in {keys}")
            setattr(node, k, v)

        return node

    # ====================================================================================================
    # For reference

    def insert(self, link, node):

        sock0, sock3 = link.from_socket, link.to_socket
        sock1, sock2 = node.in_sockets.first_compatible(sock0), node.out_sockets.first_compatible(sock3)

        if sock1 is None or sock2 is None:
            raise Exception(f"Tree insert error: impossible to insert the node into link: {node}")

        self.btree.links.remove(link)
        self.btree.links.new(sock0, sock1)
        self.btree.links.new(sock2, sock3)

        self.arrange()

    # ====================================================================================================
    # Buiild the full doc

    @staticmethod
    def build_doc(folder):

        from geonodes.nodes import dynamic

        if not GeoNodes.INIT:
            GeoNodes._setup()
        if not Shader.INIT:
            Shader._setup()
        if not Compositor.INIT:
            Compositor._setup()

        dynamic.print_md_doc(folder)


# ====================================================================================================
# Geometry Nodes Tree

class GeoNodes(Tree):

    INIT = False
    TREE_TYPE = 'GeometryNodeTree'

    # ====================================================================================================
    # Ensure input and output geometry sockets exist

    def _stack_init(self):

        super()._stack_init()

        if not self.is_group:
            _ = self.input_geometry
            _ = self.output_geometry

    # ====================================================================================================
    # Input and output nodes

    @property
    def input_node(self):
        return self.get_node('NodeGroupInput', create=True)

    @property
    def output_node(self):
        return self.get_node('NodeGroupOutput', create=True)

    # ====================================================================================================
    # Input and output geometries

    @property
    def input_geometry(self):

        if self.is_group:
            return None

        io_socket = self.io_socket_exists('NodeSocketGeometry', 'INPUT')
        if io_socket is None:
            io_socket = self.new_io_socket('NodeSocketGeometry', 'INPUT', 'Geometry')

        # ----- As the first

        self.btree.interface.move(io_socket, 0)

        return self.GEOMETRY(self.input_node.bnode.outputs[io_socket.identifier])


    @property
    def output_geometry(self):

        if self.is_group:
            return None

        io_socket = self.io_socket_exists('NodeSocketGeometry', 'OUTPUT')
        if io_socket is None:
            io_socket = self.new_io_socket('NodeSocketGeometry', 'OUTPUT', 'Geometry')

        # ----- As the first

        self.btree.interface.move(io_socket, 0)

        return self.GEOMETRY(self.output_node.bnode.inputs[io_socket.identifier])

        # OLD

        return constants.nodesocket_classes()['NodeSocketGeometry'](self.output_node.bnode.inputs[io_socket.identifier])

    @output_geometry.setter
    def output_geometry(self, value):
        self.output_geometry._set_value(value)

    @property
    def ig(self):
        return self.input_geometry

    @property
    def og(self):
        return self.output_geometry

    @og.setter
    def og(self, value):
        self.output_geometry = value


    @property
    def geometry(self):
        return self.input_geometry

    @geometry.setter
    def geometry(self, value):
        self.output_geometry = value

    # ====================================================================================================
    # Frame

    def layout(self, node_label="Frame", node_color=(.1, .2, .2), label_size=None):
        return self.Frame(label_size=label_size, node_label=node_label, node_color=node_color)

    # ====================================================================================================
    # Simulation and Repeat

    def simulation(self, **kwargs):
        from geonodes.nodes.zones import Simulation

        return Simulation(**kwargs)

    def repeat(self, iterations=1, **kwargs):
        from geonodes.nodes.zones import Repeat

        return Repeat(iterations=iterations, **kwargs)

# ====================================================================================================
# Shader Tree

class Shader(Tree):

    INIT = False
    TREE_TYPE = 'ShaderNodeTree'

    def __init__(self, name, create=True, fake_user=True, is_group=False, prefix=None):

        self.material = None
        if is_group:
            super().__init__(name, create=create, clear=True, is_group=True)

        else:
            mat = bpy.data.materials.get(name)
            if mat is None:
                mat = bpy.data.materials.new(name)

            mat.use_nodes = True
            super().__init__(mat.node_tree, create=False, clear=True, is_group=False)
            self.material = mat

    # ====================================================================================================
    # Input and output nodes

    @property
    def input_node(self):
        if self.is_group:
            return self.get_node('NodeGroupInput', create=True)
        else:
            raise AttributeError(f"Shader '{self.name}' has not input node.")

    @property
    def output_node(self):
        if self.is_group:
            return self.get_node('NodeGroupOutput', create=True)
        else:
            return self.get_node('ShaderNodeOutputMaterial', create=True)

    # ====================================================================================================
    # Tree output

    @property
    def output_surface(self):
        raise AttributeError(f"Material 'output_surface' is write only")

    @output_surface.setter
    def output_surface(self, value):
        self.output_node.surface = value

    @property
    def output_volume(self):
        raise AttributeError(f"Material 'output_volume' is write only")

    @output_volume.setter
    def output_volume(self, value):
        self.output_node.volume = value

    @property
    def output_displacement(self):
        raise AttributeError(f"Material 'output_displacement' is write only")

    @output_displacement.setter
    def output_displacement(self, value):
        self.output_node.displacement = value

# ====================================================================================================
# Compositor Tree

class Compositor(Tree):

    INIT = False
    TREE_TYPE = 'CompositorNodeTree'

    def __init__(self, name=None, create=True, clear=True, fake_user=True, is_group=False, prefix=None):

        if is_group:
            if name is None:
                name = "Group"
            super().__init__(name, create=create, clear=clear, fake_user=fake_user, is_group=True, prefix=None)
            self.scene = None

        else:
            if name is None:
                name = bpy.context.scene.name
            scene = bpy.data.scenes.get(name)
            if scene is None:
                raise AttributeError(f"Scene '{name}' not found in {list(bpy.data.scenes.keys())} for Compositor initialization.")

            scene.use_nodes = True
            super().__init__(scene.node_tree, create=create, clear=clear, fake_user=False, is_group=False)
            self.scene = scene

    # ====================================================================================================
    # Input and output nodes

    @property
    def input_node(self):
        if self.is_group:
            return self.get_node('NodeGroupInput', create=True)
        else:
            return self.get_node('CompositorNodeRLayers', create=True)

    @property
    def output_node(self):
        if self.is_group:
            return self.get_node('NodeGroupOutput', create=True)
        else:
            return self.get_node('CompositorNodeComposite', create=True)

    # ====================================================================================================
    # Tree output

    @property
    def use_alpha(self):
        return self.output_node.use_alpha

    @use_alpha.setter
    def use_alpha(self, value):
        self.output_node.use_alpha = value

    @property
    def output_image(self):
        raise AttributeError(f"Image 'output_image' is write only")

    @output_image.setter
    def output_image(self, value):
        self.output_node.image = value

    @property
    def output_alpha(self):
        raise AttributeError(f"Image 'output_alpha' is write only")

    @output_alpha.setter
    def output_alpha(self, value):
        self.output_node.alpha = value

# ====================================================================================================
# Compositor Tree

class TextureLegacy(Tree):

    INIT = False
    TREE_TYPE = 'TextureNodeTree'

    def __init__(self, name, create=True, clear=True, fake_user=True, is_group=False, prefix=None):

        if is_group:
            if name is None:
                name = "Group"
            super().__init__(name, create=create, clear=clear, fake_user=fake_user, is_group=True, prefix=None)
            self.texture = None

        else:
            texture = bpy.data.textures.get(name)
            if texture is None:
                if create:
                    texture = bpy.data.textures.new(name)
                else:
                    raise AttributeError(f"Texture named '{name}' not found.")

            texture.use_nodes = True
            super().__init__(texture.node_tree, create=False, clear=clear, fake_user=False, is_group=False)
            self.texture = texture

    # ====================================================================================================
    # Input and output nodes

    @property
    def input_node(self):
        if self.is_group:
            return self.get_node('NodeGroupInput', create=True)
        else:
            return self.get_node('CompositorNodeRLayers', create=True)

    @property
    def output_node(self):
        if self.is_group:
            return self.get_node('NodeGroupOutput', create=True)
        else:
            return self.get_node('CompositorNodeComposite', create=True)

    # ====================================================================================================
    # Tree output

    @property
    def use_alpha(self):
        return self.output_node.use_alpha

    @use_alpha.setter
    def use_alpha(self, value):
        self.output_node.use_alpha = value

    @property
    def output_image(self):
        raise AttributeError(f"Image 'output_image' is write only")

    @output_image.setter
    def output_image(self, value):
        self.output_node.image = value

    @property
    def output_alpha(self):
        raise AttributeError(f"Image 'output_alpha' is write only")

    @output_alpha.setter
    def output_alpha(self, value):
        self.output_node.alpha = value
