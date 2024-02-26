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
- StackedNode implementing roog method and context management for layouts
- Trees offering groups management

update : 2024/02/17
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

def del_tree(name, tree_type='GeometryNodeTree'):

    """ Delete a tree
    
    Arguments
    ---------
        - name (str) : Tree name
        - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
    """
    
    btree = get_tree(name, tree_type=tree_type)
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
    
    def clear(self):
        self.btree.nodes.clear()

    # ====================================================================================================
    # Stacking the Tree
    
    def _stack_init(self):
        pass

    def _stack_done(self):
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
    # Base input nodes
    
    def boolean(self, boolean, node_label=None, node_color=None):
        """ Boolean input
        class_name = Boolean
        """
        return self.Boolean(boolean, node_label=node_label, node_color=node_color).boolean
    
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
    
    
    def integer(self, integer, node_label=None, node_color=None):
        """ Integer input
        class_name = Integer
        """
        return self.Integer(integer, node_label=node_label, node_color=node_color).integer
    
    def string(self, string, node_label=None, node_color=None):
        """ String input
        class_name = String
        """
        return self.String(string, node_label=node_label, node_color=node_color).string

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
        return self.Image(image, node_label=node_label, node_color=node_color).image
    
    
    def material(self, material, node_label=None, node_color=None):
        """ Material input
        class_name = Material
        """
        material = self.Material._material_value(material)
        return self.Material(material, node_label=node_label, node_color=node_color).material
    
        
        
# ====================================================================================================
# Node created in the current tree

class StackedNode(object):
    
    def __init__(self, bl_idname, node_label=None, node_color=None):
        
        self.tree  = constants.current_tree()
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
        
        self.tree._register_node(self)
        
        
    def __enter__(self):
        if self.bnode.bl_idname != 'NodeFrame':
            raise Exception(f"Only a node of type Frame can be the parent of new nodes, not node of type '{self.bnode.bl_idname}'")
            
        constants.FRAME_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        constants.FRAME_STACK.pop()
        
    def __str__(self):
        return f"<Node  '{self.node_label}' ({self.bnode.name})>"
        
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
        if value is not None:
            setattr(self.bnode, param, value)
            
    # ----------------------------------------------------------------------------------------------------
    # component : ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')
    # mode ('ALL', 'EDGE_FACE', 'ONLY_FACE') DeleteGeometry
    # mode ('VERTICES', 'EDGES', 'FACES') ExtrudeMesh
    # mode ('VERTICES', 'EDGES', 'FACES', 'CORNERS') MeshToPoints
    # target_element ('POINTS', 'EDGES', 'FACES') GeometryProximity
            
    @classmethod
    def _get_domain_value(cls, domain, default):
        
        if domain is None or cls.DOMAIN_VALUES is None:
            return default
        
        def get_value(values):
            for val in values:
                if val in cls.DOMAIN_VALUES:
                    return val
            print(f"CAUTION: domain '{domain}' not valid for node '{type(self).__name__}', valid values are: {values}. Default '{default}' is used")
            return default
        
        if domain == 'POINT':
            return get_value(['POINT', 'POINTS', 'MESH', 'VERTICES', 'ALL'])
        
        elif domain == 'CLOUD':
            return get_value(['POINTCLOUD'])
        
        elif domain == 'EDGE':
            return get_value(['EDGE', 'EDGES', 'EDGE_FACE'])
        
        elif domain == 'FACE':
            return get_value(['FACE', 'FACES', 'ONLY_FACE'])
        
        elif domain == 'CORNER':
            return get_value(['CORNER', ' CORNERS'])
        
        elif domain == 'CURVE':
            return get_value(['CURVE', 'CURVES'])
        
        elif domain == 'SPLINE':
            return get_value(['SPLINE', 'SPLINES'])
        
        elif domain == 'INSTANCE':
            return get_value(['INSTANCE', 'INSTANCES'])
        
        else:
            raise AttributeError(f"Domain {domain} not valid")

            
    # ====================================================================================================
    # Sockets
    
    def _get_output_socket(self, pyname):
        bsock = self.outputs.sockets_pynames().get(pyname)
        if bsock is None:
            raise AttributeError(f"Socket error: {self}. No output socket named {pyname} in list: {list(self.outputs.sockets_pynames().keys())}")
        return sockets.Socket(bsock)
    
    def _set_input_socket(self, pyname, value):
        
        if value is None:
            return

        bsock = self.inputs.sockets_pynames().get(pyname)
        if bsock is None:
            bsock = self.inputs.sockets_pynames(enabled_only=False).get(pyname)
            if bsock is None:
                raise AttributeError(f"Socket error: {self}. No inpout socket named {pyname} in list: {list(self.inputs.sockets_pynames(enabled_only=False).keys())}")
                
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
    
    def __getattr__(self, name):
        
        # ----- Why ?
        # I don't know why the 2 lines below is required !
        #if name in type(self).__dict__:
        #    return type(self).__dict__[name]
        
        outputs = self.__dict__.get('outputs')
        if outputs is not None and type(self).dynamic_out:
            bsocket = outputs.sockets_pynames(enabled_only=True).get(name)
            if bsocket is not None:
                return sockets.Socket(bsocket)
            
        raise AttributeError(f"Node {self} has no output socket named '{name}'")
    
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
# A group of trees

class Trees:
    
    def __init__(self, prefix=None):
        """ A group of trees.
        
        Names are prefixed.
        
        Arguments
        ----------
            - prefix (str = None) : The prefix to use
        """
        if isinstance(prefix, Trees):
            self.prefix = prefix.prefix
        else:
            self.prefix = "" if prefix is None else prefix.strip() + " "
        
    def __str__(self):
        return f"<Group of trees prefixed: {self.prefix.strip()}>"
    
    @property
    def tree_type(self):
        return constants.current_tree().TREE_TYPE

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
        """ Delete all the **Geometry Nodes** whose name has a given prefix.
        
        For instance, to delete all the **Geometry Nodes** whose name starts with 'Utils':
        
        """
        trees = self.trees
        for tree in trees.values():
            bpy.data.node_groups.remove(tree)
            
    # ----------------------------------------------------------------------------------------------------
    # Call Group as tree attribute
    
    def __getattr__(self, name):
        
        tree = self.trees.get(self.python_name(name))
        if tree is None:
            print("TREES", list(self.trees.keys()))
            raise AttributeError(f"Tree named '{name}' not found in {self}")
            
        def f(**kwargs):
            cur_tree = constants.current_tree()
            return cur_tree.group(tree.name, **kwargs)
        
        return f
    
        
    
    

        
        
        
      
