#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov  3 09:36:21 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Python to nodes module

Tree Class
"""

from pprint import pprint

import numpy as np

import bpy
from geopy.nodes import constants
from geopy.nodes import utils
from geopy.nodes import treestack
from geopy.nodes import sockets
from geopy.nodes.treestack import StackedTree, StackedNode, Trees
from geopy.nodes.sockets import Socket, Sockets
from geopy.nodes import nodeinfo

from geopy.nodes.treearrange import arrange


# ====================================================================================================
# A tree

class Tree(StackedTree):
    
    # ====================================================================================================
    # Initialization
    
    def __new__(cls, *args, **kwargs):
        """ Initialize dynamic classes if the class is not yet initialized
        """
        
        if not cls.INIT:
            nodeinfo.tree_class_setup(cls.TREE_TYPE)
            
            for name, obj in constants.tree_dict(cls.TREE_TYPE).items():
                setattr(cls, name, obj)
                
            cls.INIT = True
            
        return StackedTree.__new__(cls)

    # ----------------------------------------------------------------------------------------------------
    # init
    
    def __init__(self, name, create=True, clear=True, fake_user=True, is_group=False, prefix=None, names=None):
        """ Tree of Nodes.
        
        The Tree can be initialized with a dictionary the set the dynamic classes.
        This avoids to prefix the classes and functions with the tree class.
        
        ``` python
        # No names dictionary : classes are read from tree
        with Tree("Test", names=None) as tree:
            a = tree.Math()
            
        # Provides the locals dictionary
        with Tree("Test", names=locals()) as tree:
            a = Math()
        ```
        
        Arguments
        ---------
            - name (str) : Tree name
            - create (bool = True) : create the tree if it doesn't exist
            - clear (bool = False) : erase the existing nodes
            - is_group (bool = False) : initialize as a ground
            - prefix (str = None) : prefix to use in the name
            - names (dict=None) : locals dict where to create the dynamic classes
        """
        
        super().__init__()
        
        self.is_group = is_group
            
        # ----- Load the btree
        
        if isinstance(name, str):
            name = Trees(prefix).prefixed_name(name)
            self.btree = treestack.get_tree(name, self.TREE_TYPE, create=create, clear=False)
        else:
            self.btree = name
            
        if hasattr(self.btree, 'is_modifier'):
            self.btree.is_modifier = not self.is_group
        self.btree.use_fake_user = fake_user
            
        if clear:
            self.clear()
            
        if names is not None:
            nodeinfo.tree_import(self.TREE_TYPE, names)
            
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
            return constants.node_classes()[bl_idname]()
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
        
        socket_class = constants.nodesocket_classes()[bl_idname]
        
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
            
        socket_class = constants.nodesocket_classes()[bl_idname]
        out_socket = socket_class(self.output_node.bnode.inputs[io_socket.identifier])
        out_socket._set_value(socket)
    
    
    # ====================================================================================================
    # Short cuts
    
    def bool_input(self, name, value=None, description=""):
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
        print("BTREES", btrees)
        for btree in btrees:
            bpy.data.node_groups.remove(btree)
            
    def group(self, name, prefix=None, **kwargs):
        
        # ----- Get the tree
        
        group_tree = Trees(prefix).trees.get(Trees.python_name(name))
        if group_tree is None:
            raise AttributeError(f"Impossible to find the group named '{self.prefixed_name(name, prefix)}'")
            
        # ----- Create the node group
        
        node = self.Group()
        node.bnode.name = group_tree.name
        node.bnode.node_tree = group_tree
        
        for k, v in kwargs.items():
            if not node._input_socket_exists(k):
                raise AttributeError(f"Node group {node} has no input socket named '{k}' in {list(node.inputs.sockets_pynames().keys())}")
            setattr(node, k, v)
            
        return node








class Tree_OLD(StackedTree):

    def __init__(self, name, create=True, clear=False, is_group=False):
        
        if not self.INIT:
            self.class_setup()
        
        self.is_group = is_group
            
        if isinstance(name, str):
            self.btree = utils.get_tree(name, self.tree_type, create=create, clear=False)
        else:
            self.btree = name
            
        self.btree.is_modifier = not self.is_group
            
        if clear:
            self.clear()
            
    def clear(self):
        self.btree.nodes.clear()

    # ====================================================================================================
    # Str
        
    def __str__(self):
        return f"<Tree '{self.btree.name}' ({self.tree_type}): {len(self.btree.nodes)} nodes and {len(self.btree.links)} links>"

    # ====================================================================================================
    # Class Initialization
    # - add node creation methods
            
    @classmethod
    def class_setup(cls):
        
        btree = utils.get_tree("GEOPY - Temp", tree_type=cls.tree_type, create=True, clear=True)
    
        for type_name in dir(bpy.types):
            try:
                bnode = btree.nodes.new(type=type_name)
            except RuntimeError as e:
                continue
            
            if 'legacy' in bnode.name.lower():
                continue
            
            cls.create_node_class(btree, bnode)  
                
        utils.del_tree(btree.name)
        
        cls.INIT = True        





    # ====================================================================================================
    # Has user input / output
    
    # Node access
        
    def node_OLD(self, node_name, node_label=None, node_color=None, **kwargs):
        node = Node(self, self.btree.nodes.new(type=self.get_type_name(node_name)), node_label=node_label, node_color=node_color, **kwargs)
        self.arrange()
        return node
    
    def new_node(self, bl_idname, node_label=None, node_color=None, **kwargs):
        node = Node(self, self.btree.nodes.new(type=bl_idname), node_label=node_label, node_color=node_color, **kwargs)
        self.arrange()
        return node
    
    def get_nodes(self, node_name):
        return [Node(self, bnode) for bnode in self.btree.nodes if self.get_type_name(node_name) == bnode.bl_idname]
    
    def get_create(self, node_name, **kwargs):
        cands = self.get_nodes(node_name)
        if len(cands) == 0:
            return self.node(node_name, **kwargs)
        return Node(self, cands[0].bnode, **kwargs)

    # ====================================================================================================
    # Clear
    
    @staticmethod
    def clear_inout(inouts, keep_first=False):
        ios = [io for io in inouts]
        if keep_first:
            ios = ios[1:]
            
        for io in ios:
            inouts.remove(io)

    def clear(self):
        self.btree.nodes.clear()
        
    # ====================================================================================================
    # Get the socket type NodeSocketBool, NodeSocketInt,... from data type 'BOOLEAN', 'FLOAT' or a python type
    
    @classmethod
    def get_socket_type(cls, socket_type):
        if isinstance(socket_type, str):
            socket_type = socket_type.upper()
            
        if socket_type in cls.SOCKET_TYPES.keys():
            return cls.SOCKET_TYPES[socket_type]
        else:
            return socket_type

    # ====================================================================================================
    # Tree inputs / outputs
    
    def new_input(self, name, socket_type, value=None):
        inp = self.btree.inputs.new(name=name, type=Tree.get_socket_type(socket_type))
        inp.default_value = utils.value_for(value, socket_type)
    
    def new_output(self, name, socket_type, value=None):
        outp = self.btree.outputs.new(name=name, type=Tree.get_socket_type(socket_type))
        outp.default_value = utils.value_for(value, socket_type)
        
    # ----------------------------------------------------------------------------------------------------
    # Connect an Group input to the input socket of a Node
        
    def input_from(self, socket, name=None):
        
        # ----- Group input Node
        in_node = self.group_input
        if in_node is None:
            return
        
        # ----- Create the new Group Input
        inp = self.btree.inputs.new(name=socket.name if name is None else name, type=socket.bl_idname)
        inp.default_value = socket.default_value
        
        # ----- It is the last one in the input Node
        for in_socket in reversed(in_node.bnode.outputs):
            if in_socket.bl_idname == 'NodeSocketVirtual':
                continue
            in_socket.default_value = socket.default_value
            self.link(in_socket, socket)
            return
        
    # ----------------------------------------------------------------------------------------------------
    # Connect the output of a node to a group output
        
    def output_from(self, socket, name=None):

        # ----- Group input Node
        out_node = self.group_output
        if out_node is None:
            return
        
        # ----- Create the new Group Input
        outp = self.btree.outputs.new(name=socket.name if name is None else name, type=socket.bl_idname)
        outp.default_value = socket.default_value
        
        # ----- It is the last one in the input Node
        for out_socket in reversed(out_node.bnode.inputs):
            if out_socket.bl_idname == 'NodeSocketVirtual':
                continue
            out_socket.default_value = socket.default_value
            self.link(socket, out_socket)
            return
        
    # ----------------------------------------------------------------------------------------------------
    # Get the input / output from a name
        
    def get_input(self, name, socket_type=None):
        for inp in self.btree.inputs:
            if inp.name != name:
                continue
            if socket_type is not None:
                if socket_type.upper() != inp.type:
                    continue
            return inp
        return None
    
    def get_output(self, name, socket_type=None):
        for outp in self.btree.outputs:
            if outp.name != name:
                continue
            if socket_type is not None:
                if socket_type.upper() != outp.type:
                    continue
            return outp
        return None
    
    # ====================================================================================================
    # Add a link
    
    def link(self, in_socket, out_socket):
        link = self.btree.links.new(in_socket, out_socket, verify_limits=True)
        self.arrange()
        return link
    
    def set_socket(self, socket, value):
        if value is None:
            return

        if isinstance(value, bpy.types.NodeSocket):
            if socket.is_output:
                self.btree.links.new(value, socket, verify_limits = True)
            else:
                self.btree.links.new(socket, value, verify_limits = True)
            self.arrange()
        else:
            socket.default_value = utils.value_for(value, socket.bl_idname)
    
    # ====================================================================================================
    # Insert a node in a link
    
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
    # Common input nodes
    
    """
    def boolean(self, value=True, **kwargs):
        node = self.new_node('FunctionNodeInputBool', **kwargs)
        node.boolean = value
        return node._boolean
    
    """
    def int(self, value=0, **kwargs):
        node = self.new_node('FunctionNodeInputInt', **kwargs)
        node.integer = value
        return node._integer
    
    def float(self, value=True, **kwargs):
        node = self.new_node('ShaderNodeValue', **kwargs)
        self.set_socket(node._value, value)
        return node._value
    
    def string(self, value="", **kwargs):
        node = self.new_node('FunctionNodeInputString', **kwargs)
        node.string=value
        return node._string
        
    def vector(self, value=(0, 0, 0), **kwargs):
        node = self.new_node('FunctionNodeInputVector', **kwargs)
        node.vector=Vector(value)
        return node._vector
    
    def rgb(self, value=(.9, .9, .9, 1), **kwargs):
        node = self.new_node('FunctionNodeInputInt', **kwargs)
        self.set_socket(node._color, value)
        return node._color
        
    # ====================================================================================================
    # Some common operations
    
    @property
    def frame(self):
        return self.node("Scene Time")._frame
    
    @property
    def seconds(self):
        return self.node("Scene Time")._seconds
    
    def math(self, a, b=None, operation='ADD'):
        return self.node("Math", value_0_ = a, value_1_ = b, operation=operation).output
        
    def vector_math(self, a, b=None, operation='ADD'):
        return self.node("Vector Math", vector_0_ = a, vector_1_ = b, operation=operation).output
        
    def mix_color(self, a, b=None, factor=.5):
        return self.node("Mix", a = a, b = b, factor=factor, data_type='RGBA').output
        
    def mix_float(self, a, b=None, factor=.5):
        return self.node("Mix", a = a, b = b, factor=factor, data_type='FLOAT').output

    def mix_vector(self, a, b=None, factor=.5):
        return self.node("Mix", a = a, b = b, factor=factor, data_type='VECTOR').output
        
        
# ====================================================================================================
# Geometry Nodes Tree

class Shader(Tree):

    INIT = False
    TREE_TYPE = 'ShaderNodeTree'
    
    def __init__(self, name, create=True, fake_user=True, is_group=False, prefix=None, names=None):
        
        self.material = None
        if is_group:
            super().__init__(name, create=create, clear=True, is_group=True, names=names)
            
        else:
            mat = bpy.data.materials.get(name)
            if mat is None:
                mat = bpy.data.materials.new(name)
                
            mat.use_nodes = True
            super().__init__(mat.node_tree, create=False, clear=True, is_group=False, names=names)
            self.material = mat
            
    # ====================================================================================================
    # Tree output    

    @property
    def output_node(self):
        return self.get_node('ShaderNodeOutputMaterial', create=True)
    
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
        
        return constants.nodesocket_classes()['NodeSocketGeometry'](self.input_node.bnode.outputs[io_socket.identifier])
            
        
    @property
    def output_geometry(self):

        if self.is_group:
            return None
        
        io_socket = self.io_socket_exists('NodeSocketGeometry', 'OUTPUT')
        if io_socket is None:
            io_socket = self.new_io_socket('NodeSocketGeometry', 'OUTPUT', 'Geometry')
            
        # ----- As the first
        
        self.btree.interface.move(io_socket, 0)
        
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
    
    # ====================================================================================================
    # Frame
    
    def layout(self, label="Frame", color=None, label_size=None):
        return self.Frame(label_size=label_size, node_label=label, node_color=color)

    # ====================================================================================================
    # Some usefull Trees
    
    @classmethod
    def IcoSpheres(cls, name="IcoSpheres", size=.1, scale=.01, material=None):
        
        tree = cls(name=name, create=True, clear=True)
        
        to_points = tree.node("Mesh to Points", mesh=tree.ig)
        ico = tree.node("Ico Sphere", size=size)
        tree.input_from(cube.size, name="Size")
        #rot = tree.node("Random", data_type='FLOAT_VECTOR', max=2*np.pi, seed=tree.frame)
        insts = tree.node("Instance on points", points=tree.ig, instance=ico.output)
        
        link = tree.link(insts.output, tree.og)
        
        mat = tree.node("Set Material", material=material)
        tree.input_from(mat.material)
        
        tree.insert(link, mat)
        
        return tree
    
    @classmethod
    def Particles(cls, name="Particles", size=.1, scale=.01, material=None):
        
        tree = cls(name=name, create=True, clear=True)
        
        to_points = tree.node("Mesh to Points", mesh=tree.ig)
        cube = tree.node("Cube", size=size)
        tree.input_from(cube.size, name="Size")
        rot = tree.node("Random", data_type='FLOAT_VECTOR', max=2*np.pi, seed=tree.frame)
        insts = tree.node("Instance on points", points=to_points.output, instance=cube.output, rotation=rot.output)
        
        link = tree.link(insts.output, tree.og)
        
        mat = tree.node("Set Material", material=material)
        tree.input_from(mat.material)
        
        tree.insert(link, mat)
        
        return tree
    
    @classmethod
    def Smoke(cls, name="To Smoke", radius=2, material=None):
        tree = cls(name, create=True, clear=True)
        
        to_points = tree.node("Mesh to Points", mesh=tree.ig)
        to_vol    = tree.node("Points to Volume", points=to_points.output, radius=radius)

        tree.input_from(to_vol.density)
        tree.input_from(to_vol.voxel_amount)
        tree.input_from(to_vol.radius)
        
        link = tree.link(to_vol.output, tree.og)
        
        mat = tree.node("Set Material", material=material)
        tree.input_from(mat.material)
        
        tree.insert(link, mat)
        
        
        return tree
    
# ====================================================================================================
# Demo

def demo():
    
    # ----- Shader
    
    shader = Shader("Demo", clear=False)
    bsdf = shader.get_create("Principled BSDF",
            metallic=.5, 
            roughness=1,
            )
    bsdf.base_color_ = (0, 1, 0, 1)
    
    shader.surface = bsdf.output
    
    # ----- Geometry nodes
    
    tree = GeoNodes("Demo", clear=True)
    spiral = tree.node("Spiral", resolution=128, rotations=tree.float(3))
    prof   = tree.node("Curve Circle", resolution=8, radius=.1)
    to_mesh = tree.node("Curve to Mesh", curve=spiral.output, profile_curve=prof._curve)
    link = tree.link(to_mesh.output, tree.output_geometry)
    
    tree.insert(link, tree.node("Set Material", material = shader.material, selection=tree.boolean(True)))
        






