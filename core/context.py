#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:54:06 2022

@author: alain
"""

# ====================================================================================================
# Provides global variable with
# - the current tree
# - the current layout
#
# These variables are managed by class Tree

import bpy
import logging
logger = logging.getLogger('geonodes')


tree   = None

# ====================================================================================================
# Utilities

def check_tree(title=""):
    if tree is None:
        raise Exception(f"{title}.\nNo current tree. Make sure to initialize a tree with instruction:\n\nwith gn.Tree('tree name') as tree:\n")

def create_node(blid, title=""):
    
    check_tree(title)
    
    node = tree.btree.nodes.new(blid)
    node.parent = tree.cur_frame
    
    return node

# ----------------------------------------------------------------------------------------------------
# Create node from value

def integer_node(value):
    node = create_node('FunctionNodeInputInt', 'Integer node creation')
    node.integer = int(value)
    return node

def boolean_node(value):
    node = create_node('FunctionNodeInputBool', 'Boolean node creation')
    node.boolean = bool(value)
    return node

def float_node(value):
    node = create_node('ShaderNodeValue', 'Float node creation')
    node.outputs[0].default_value = float(value)
    return node

def string_node(value):
    node = create_node('FunctionNodeInputString', 'String node creation')
    node.string = str(value)
    return node

def vector_node(value):
    
    check_tree("Combine XYZ node creation")
    
    if hasattr(value, '__len__'):
        if len(value) == 3:
            vector = value
            
        elif len(value) == 4:
            vector = tuple(value[:3])
            
        elif len(value) == 1:
            vector = (value[0],) * 3
    
        else:
            raise Exception(f"Impossible to create a 'Combine XYZ' node from vector {value} with {len(value)} items.")
    else:
        vector = (value,)*3
        
    node = create_node('ShaderNodeCombineXYZ', 'Combine XYY node creation')
    for i, v in enumerate(vector):
        if hasattr(v, 'get_blender_socket'):
            tree.btree.links.new(v.get_blender_socket(), node.inputs[i])
        else:
            node.inputs[i].default_value = v
            
    return node

def color_node(value):
    
    check_tree("Combine Color node creation")
    
    if hasattr(value, '__len__'):
        if len(value) == 3:
            vector = tuple(value) + (1.,)
            
        elif len(value) == 4:
            vector = value
            
        elif len(value) == 1:
            vector = (value[0],) * 4
            
        else:
            raise Exception(f"Impossible to create a 'Combine Color' node from vector {value} with {len(value)} items.")
    else:
        vector = (value,) * 4
        
    node = create_node('FunctionNodeCombineColor', 'Combine color node creation')
    for i, v in enumerate(vector):
        if hasattr(v, 'get_blender_socket'):
            tree.btree.links.new(v.get_blender_socket(), node.inputs[i])
        else:
            node.inputs[i].default_value = v
            
    return node

# =============================================================================================================================
# Plug values to a blender socket

def plug_to_socket(socket, *values):
    """ Plug the values to the input Blender socket.
    
    Args:
        - socket (Socket or bpy.types.NodeSocket): in the input socket to plug into
        - *values: values or output sockets.More than one values can be passed
          if the input socket is multi input.

    This method is the one which links an output socket of a node to the input
    socket of another one.
    
    If the socket is multi input, the plug method is called once per provided value.
    If a value is None, nothing happens.
    
    A not None value can be:
    - either a valid value for the socket (eg: 123 for Integer socket)
    - or an output socket of another Node
        
    When it is a socket, it can be a Blender socket or a DataSocket
    """

    # ====================================================================================================
    # Let's have a not None single value to plug
    
    # We work on a blender socket
    
    if isinstance(socket, bpy.types.NodeSocket):
        bsocket = socket
        
    elif hasattr(socket, 'get_blender_socket'):
        bsocket = socket.get_blender_socket()
        
    elif hasattr(socket, 'outputs'):
        names = [sock.name for sock in socket.outputs if sock.enabled]
        raise Exception(f"plug_to_socket ERROR: the socket argument must be a socket, not a node.\n" +
                        "You certainly want to plug one output socket of Node {socket}: {names}.")
    else:
        raise Exception(f"plug_to_socket ERROR: the socket argument must be a socket, not {socket} of type '{type(socket).__name__}'.\n")
    
    # ---- Just ot be sure :-)
    
    if bsocket.is_output:
        raise Exception(f"plug_to_socket ERROR: the socket argument must be an input socket, not an output socket {bsocket}")
    
    # ----- Nothing to plug

    if len(values) == 0:
        return

    # -----If several output sockets to plug, let's loop on the list
    
    if len(values) > 1:
        if not bsocket.is_multi_input:
            raise Exception(f"plug_to_socket ERROR: the input socket {bsocket} is not multi input: impossible to plug multiple sockets: {values}.")
            
        for v in values:
            plug_to_socket(bsocket, v)
            
        return
    
    # ----- Let's make sure the only one thing to plug is not None
    
    value = values[0]
    if value is None:
        return        
    
    # ====================================================================================================
    # Ok now: value is the only one thing to plug
    # It can be:
    # - a value
    # - a geonode output socket
    # - a blender output socket
    
    # ----------------------------------------------------------------------------------------------------
    # Let's get the blender socket if it is the case
    
    out_socket = None
    
    # ----- A Blender socket
    
    if isinstance(value, bpy.types.NodeSocket):
        out_socket = value
        
    # ----- A geonodes DataSocket
        
    elif hasattr(value, 'get_blender_socket'):
        
        out_socket = value.get_blender_socket()
        
        if False:
            # Node is None: particular cases
            
            if value.node is None:
                if hasattr(value, 'bobject'):        # An object socket not connected to input
                    value = value.bobject
                    
                elif hasattr(value, 'bcollection'):  # Same for colleciton
                    value = value.bcollection
                    
                else:
                    raise RuntimeError("Impossible to plug a socket with a None Node: {value}.")
            else:
                out_socket = value.get_blender_socket()
            
    # ----------------------------------------------------------------------------------------------------
    # It is actually a blender socket, let's plug it
    
    if out_socket is not None:
        
        tree.btree.links.new(bsocket, out_socket, verify_limits=True)
        
        return

    # ====================================================================================================
    # Value is a python value
    # - either a simple type (str, int, bool, float)
    # - or a tuple
    # - or a Blender type such as Image, Texture, Object...
    #
    # Some checks are required to see if we have to transform the value into a socket
    
    # ----------------------------------------------------------------------------------------------------
    # We have to plug a Color or a Vector
    
    ndim = None
    if hasattr(bsocket, 'default_value') and hasattr(bsocket.default_value, '__len__'):
        ndim = len(bsocket.default_value)
        
    if ndim is not None:
        
        # Broadcast 1 --> 3
        if not hasattr(value, '__len__'):
            value = (value,) * ndim
            
        # Color --> Vector
        elif ndim == 3 and len(value) == 4:
            value = (value[0], value[1], value[2])
            
        # Vector --> Color
        elif ndim == 4 and len(value) == 3:
            value += (value[0], value[1], value[2], 1.)
            
        # ----- Transform a triplet (a, b, c) where one value is a socket to a vector
        # This is necessarily done if hide_value is True
        
        to_vector = False
        
        for v in value:
            if hasattr(v, 'get_blender_socket'):
                to_vector = True
                break
            
        if to_vector or bsocket.hide_value:
            
            if ndim == 3:
                node = vector_node(value)
            else:
                node = color_node(value)
                
            plug_to_socket(bsocket, node.outputs[0])
                
            return
        
    # ----------------------------------------------------------------------------------------------------
    # The value is str, it can be the name of the Blender resource to plug
    
    if isinstance(value, str):
        
        # ----- Material
        
        if isinstance(bsocket, bpy.types.NodeSocketMaterial):
            try:
                value = bpy.data.materials[value]
            except:
                raise RuntimeError(f"Material '{value}' not found.")
                
        # ----- Collection
        
        elif isinstance(bsocket, bpy.types.NodeSocketCollection):
            try:
                value = bpy.data.collections[value]
            except:
                raise RuntimeError(f"Collection '{value}' not found.")
                
        # ----- Object
        
        elif isinstance(bsocket, bpy.types.NodeSocketObject):
            try:
                value = bpy.data.objects[value]
            except:
                raise RuntimeError(f"Object '{value}' not found.")
                
        # ----- Image
        
        elif isinstance(bsocket, bpy.types.NodeSocketImage):
            try:
                value = bpy.data.images[value]
            except:
                raise RuntimeError(f"Image '{value}' not found.")
                
        # ----- Texture
        
        elif isinstance(bsocket, bpy.types.NodeSocketTexture):
            try:
                value = bpy.data.textures[value]
            except:
                raise RuntimeError(f"Texture '{value}' not found.")
                
    # ----------------------------------------------------------------------------------------------------
    # If hide_value is True, changing default_value is useless, we need to use a socket
    # This test need to be done only for simple values since:
    # - Vector and Color are already done
    # - Blender resources have not 'python type' equivalent, but the name which is done
    
    if bsocket.hide_value:
        
        if isinstance(value, int):
            plug_to_socket(bsocket, integer_node(value).outputs[0])
            return

        if isinstance(value, bool):
            plug_to_socket(bsocket, boolean_node(value).outputs[0])
            return

        if isinstance(value, float):
            plug_to_socket(bsocket, float_node(value).outputs[0])
            return

        if isinstance(value, str):
            plug_to_socket(bsocket, string_node(value).outputs[0])
            return

    # ----------------------------------------------------------------------------------------------------
    # Multi input not manageeable with values
    
    if bsocket.is_multi_input:
        raise RuntimeError(f"The socket {bsocket} is multi input. Impossible to plug the value {value}.")
        
    # ----------------------------------------------------------------------------------------------------
    # One can easily try to plug a node, rather than a socket, let's give detailed information
    
    if hasattr(value, 'is_node'):
        print("-"*80)
        print("It is not possible to plug a Node to a socket!")
        print(f"You tried to plug the node {value} to the socket '{bsocket.name}' of type '{bsocket.bl_idname}'.")
        print("You certainly want to plug one of the output sockets of the node. The output socket(s) are:")
        for i, name in enumerate(value.outsockets):
            print(f"   - {i}: {name}")
        print("-"*80)
        print()
        
        raise RuntimeError(f"Impossible the plug the node {value} to the socket '{bsocket.name}'. See details above.")

    # ----------------------------------------------------------------------------------------------------
    # We can try to plug the value into the default value
    
    ok = True
    try:
        bsocket.default_value = value

    except Exception as e:
        msg = str(e)
        ok = False
        
    if not ok:
        logging.critical(f"Impossible to plug the value '{value}' to the socket '{bsocket.name}' of node '{bsocket.node.name}'")
        logging.critical(f"    The value type is: {type(value)}")
        logging.critical(f"    The expected type for socket default value is: {type(bsocket.default_value)}")
        logging.critical(f"    Default value len: {len(bsocket.default_value) if hasattr(bsocket.default_value, '__len__') else 'no length'}")
        logging.critical(f"    Error message: {msg}")
        logging.critical("")
        
        raise RuntimeError(f"Impossible to set the default value {value} to socket {bsocket}.\n Error: {msg}")
        
# ====================================================================================================
# Dump a tree

def dump_tree(tree):
    def node_name(node):
        try:
            return node.name
        except AttributeError as e:
            return type(node).__name__
    
    def slink(link):
        s0 = f"{node_name(link.from_node)}.{link.from_socket.name}"
        s1 = f"{node_name(link.to_node)}.{link.to_socket.name}"
        return f"{s0:30s} --> {s1}"
    
    nodes = [node_name(node)for node in tree.nodes]
    links = [slink(link) for link in tree.links]
    node_links = []
    
    for node in tree.nodes:
        in_links = [] 
        for socket in node.inputs:
            for link in socket.links:
                in_links.append(link)
        out_links = [] 
        for socket in node.outputs:
            for link in socket.links:
                out_links.append(link)
        node_links.append( (node_name(node), in_links, out_links) )
        
    return sorted(nodes), sorted(links), sorted(node_links, key=lambda a: a[0])

def changes_in_tree(tree, previous):
    
    current = dump_tree(tree)
    
    keys = {
        'add_nodes': (current[0],  previous[0]),
        'del_nodes': (previous[0], current[0]),
        'add_links': (current[1],  previous[1]),
        'del_links': (previous[1], current[1]),
        }
        
    diffs = {}
    for key, (loop_list, ref_list) in keys.items():
        changes = []
        for line in loop_list:
            if not line in ref_list:
                changes.append(line)
        diffs[key] = changes
        
                
    return diffs
        

# ====================================================================================================
# Debug

class TestTree:
    def __init__(self, tree_name="Geometry nodes"):
        
        global tree
        
        self.btree = bpy.data.node_groups.get(tree_name)
        if self.btree is None:
            self.btree = bpy.node_groups.new(tree_name, type='GeometryNodeTree')
        self.cur_frame = None
        
        tree = self
        
    @staticmethod
    def test():
        TestTree("Test")
        
        integer_node(10)
        boolean_node(True)
        string_node("String")
        float_node(3.14)
        
        vector_node(10)
        vector_node((1, 2, 3))
        vector_node((11, 12, 13, 14))
        
        color_node(10)
        color_node((1, 2, 3))
        color_node((11, 12, 13, 14))
        


