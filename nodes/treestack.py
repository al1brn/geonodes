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

from geonodes.nodes import constants
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
            raise Exception(f"Tree {self} has no node owning the socket '{bsocket.name}' in Blender node '{bsocket.node.name}'.")
        else:
            return node
        
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
        
        tree = self.trees.get(name)
        if tree is None:
            raise AttributeError(f"Tree named '{name}' not found in {self}")
            
        def f(**kwargs):
            cur_tree = constants.current_tree()
            return cur_tree.group(tree.name, **kwargs)
        
        return f
    
        
    
    

        
        
        
      