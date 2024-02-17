#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:14:33 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : constants
------------------
- low level constants uses by dynamic nodes generator
- dictionaries used to register the class created dynamically

update : 2024/02/17
"""

from pprint import pprint

# ====================================================================================================
# Import statement to include in dynamic source code

CONSTANTS_IMPORT_STMT  = "from geonodes.nodes import constants\n"
CONST_MODULE           = "constants"
IMPORT_STMT            = "from geonodes.nodes.constants import"

BASE_NODE              = "StackedNode"
IMPORT_BASE_NODE       = f"\tfrom geonodes.nodes.treestack import {BASE_NODE}\n"

CUR_TREE               = "current_tree"
IMPORT_TREE            = f"\tfrom geonodes.nodes.constants import {CUR_TREE}\n"

# ====================================================================================================
# Tree stack
#
# One tree can be edited at a time.
# The current tree is stacked
# The method constants.current_tree() returns the current tree

TREE_STACK  = []
FRAME_STACK = []

def current_tree(bl_idname=None):
    if len(TREE_STACK):
        return TREE_STACK[-1]
    else:
        raise Exception(f"Tree stack is empty: not Tree has been initialized. Impossible to create node '{bl_idname}'.")
        
def current_tree_type(bl_idname=None):
    return type(current_tree(bl_idname).btree).__name__

# ====================================================================================================
# Standard node attribute names which are not properties

TREE_BL_IDS = {
    'GeoNodes'   : 'GeometryNodeTree',
    'Shader'     : 'ShaderNodeTree',
    'Compositor' : 'CompositorNodeTree',
    'Texture'    : 'TextureNodeTree',
    }

# ====================================================================================================
# Standard node attribute names which are not properties

STANDARD_NODE_ATTRS = [
   '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
   'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
   'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
   'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
   'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
   'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
   'show_texture', 'socket_value_update', 'type', 'update', 'use_custom_color',
   'width', 'width_hidden']

# ====================================================================================================
# Gives the Blender socket type from a python type or a node socket type

BLENDER_SOCKET_CLASSES = {
    bool            : 'NodeSocketBool',
    int             : 'NodeSocketInt',
    float           : 'NodeSocketFloat',
    str             : 'NodeSocketString',
    
    'BOOLEAN'       : 'NodeSocketBool',
    'INT'           : 'NodeSocketInt',
    'FLOAT'         : 'NodeSocketFloat',
    'VECTOR'        : 'NodeSocketVector',
    'COLOR'         : 'NodeSocketColor',
    'STRING'        : 'NodeSocketString',
    
    'GEOMETRY'      : 'NodeSocketGeometry',
    
    'COLLECTION'    : 'NodeSocketCollection',
    'IMAGE'         : 'NodeSocketImage',
    'MATERIAL'      : 'NodeSocketMaterial',
    'OBJECT'        : 'NodeSocketObject',
    'TEXTURE'       : 'NodeSocketTexture',
    }

# ====================================================================================================
# Internal class name for socket types

SOCKET_CLASS_NAMES = {
    'CUSTOM'     : 'Custom',
    'VALUE'      : 'Float', 
    'INT'        : 'Int', 
    'BOOLEAN'    : 'Bool', 
    'VECTOR'     : 'Vect', 
    'ROTATION'   : 'Rot', 
    'STRING'     : 'Str', 
    'RGBA'       : 'Col', 
    'SHADER'     : 'Shader',
    'OBJECT'     : 'Object', 
    'IMAGE'      : 'Img', 
    'GEOMETRY'   : 'Geometry', 
    'COLLECTION' : 'Collection', 
    'TEXTURE'    : 'Texture', 
    'MATERIAL'   : 'Mat'    
    }

# ====================================================================================================
# Constant nodes
# Nodes implemented as method
# b = tree.boolean(True)

CONSTANT_NODES = {
    'Boolean':  'boolean',
    'Color':    'color',
    'Image':    'image',
    'Integer':  'integer',
    'Material': 'material',
    'String':   'string',
    'Value':    'value',
    'Vector':   'vector',
    }

# ====================================================================================================
# Nodes which are not implemented as input nodes


NO_INPUT_NODES = list(CONSTANT_NODES.keys()) + [
    'GroupOutput',
    'GroupInput',
    'SimulationInput',
    'Group',
    ]

# ====================================================================================================
# Nodes with in / out custom sockets

CUSTOM_INPUT_SOCKETS = [
    'GeometryNodeGroup', 
    'GeometryNodeSimulationInput', 
    'GeometryNodeSimulationOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatInput',
    ]

CUSTOM_OUTPUT_SOCKETS = [
    'GeometryNodeGroup', 
    'GeometryNodeSimulationInput', 
    'GeometryNodeSimulationOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatOutput',
    ]

# ====================================================================================================
# Dynamically created arrays
# 2-level dictionaries : one dictionary per tree type
#    'CompositorNodeTree' 
#    'TextureNodeTree'    
#    'GeometryNodeTree'   
#    'ShaderNodeTree'    

# ----- Valid NodeSocket classes
# Dictionnaries : NodeSocket.bl_idname -> Dynamic Socket class

NODESOCKET_CLASSES = {}

# ----- Socket classes
# Dictionaries : NodeSocket.type str --> Dynamic Socket class

SOCKET_CLASSES = {}

# ----- Node classes
# Dictionnaries : bl_idname str --> Dynamic Node Class

NODE_CLASSES = {}

# ----- All dynamic classes and functions

TREE_DICTS = {}

# ---- Transparent access for the current tree

def dynamic_dict(DICT, tree_type):
    if tree_type is None:
        tree_type = current_tree_type()
    d = DICT.get(tree_type)
    if d is None:
        d = {}
        DICT[tree_type] = d
    return d

def nodesocket_classes(tree_type=None):
    """ Returns the dictionary registring the node socket classes.
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        
    Returns
    -------
        - dict
    """
    
    return dynamic_dict(NODESOCKET_CLASSES, tree_type)

def socket_classes(tree_type=None):
    """ Returns the dictionary registring the socket classes.
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        
    Returns
    -------
        - dict
    """
    
    return dynamic_dict(SOCKET_CLASSES, tree_type)

def node_classes(tree_type=None):
    """ Returns the dictionary registring the node classes.
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        
    Returns
    -------
        - dict
    """
    
    return dynamic_dict(NODE_CLASSES, tree_type)

def tree_dict(tree_type=None):
    """ Returns the global dictionary registring all the dynamic classes and functions.
    
    Arguments
    ---------
        - tree_type (str) : valid blender tree type
        
    Returns
    -------
        - dict
    """
    
    return dynamic_dict(TREE_DICTS, tree_type)
        
            
        
        
    
    
        
        
        
    
    
    
    
    








