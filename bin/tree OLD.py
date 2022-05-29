#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:45:39 2022

@author: alain
"""

from pprint import pprint

from geonodes import basenode, nodes, classes

from .basenode import Socket, SocketIn, Node

from .color import Color 
from .arrange import arrange

import bpy

# =============================================================================================================================
# Group input and output Nodes

# -----------------------------------------------------------------------------------------------------------------------------
# Input Group

class NodeGroupInput(Node):
    
    """ Node class NodeGroupInput

    Output sockets
    --------------
        0: geometry             Geometry

    """

    def __init__(self, is_modifier=True):
        
        super().__init__('NodeGroupInput', name='Group Input')

        if is_modifier:
            self.outputs.add(Socket (self, 'NodeSocketGeometry', 'geometry' ))

    """
    def __str__(self):
        
        s = "<Node 'GroupInput'"
        sep = " -> "
        for sock in self.outputs:
            s += f"{sep}{sock.name}"
            sep = ", "
        return s + ">"
    """
    def __repr__(self):
        s = "Node 'GroupInput'"
        for sock in self.outputs:
            s += f"\n   {sock.name:15s} : {type(sock).__name__}"
        return s + "\n"

    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def geometry(self):
        return Geometry(self.outputs[0])
    
    # --------------------------------------------------------------------------------
    # Create a new output socket
    
    def new_socket(self, bl_idname, value=None, name=None):

        # ---------------------------------------------------------------------------
        # Let's build the socket
            
        index = len(self.outputs)
        socket = self.outputs.add(Socket(self, bl_idname, name))
        socket.default_value = value
        
        # ---------------------------------------------------------------------------
        # Return the socket
        
        return self.outputs[index]
        
    # ----------------------------------------------------------------------------------------------------
    # Create the bnode input sockets
    
    def setup_bnode(self):
        
        binputs = self.btree.inputs
        outputs = self.outputs
        
        ok_inputs = len(outputs) == len(binputs)
        if ok_inputs:
            for i, sock in enumerate(outputs):
                if sock.bl_idname != binputs[i].bl_socket_idname or sock.name != binputs[i].name:
                    ok_inputs = False
                    break
                
        if not ok_inputs:
            binputs.clear()
            for i, sock in enumerate(outputs):
                binputs.new(type=sock.bl_idname, name=sock.name)
                if hasattr(sock, 'default_value') and hasattr(binputs[i], 'default_value'):
                    if sock.default_value is not None:
                        binputs[i].default_value = sock.default_value
                        print("BUG DEFAULT INPUT VALUE", sock.name, ":", sock.default_value, '-->', binputs[i].default_value)
                        
    
# -----------------------------------------------------------------------------------------------------------------------------
# Output Group
    
class NodeGroupOutput(Node):
    """ Node class NodeGroupOutput

    Input sockets
    -------------

        0: geometry             Geometry

    Parameters
    ----------

    """

    def __init__(self, is_modifier=True):

        super().__init__('NodeGroupOutput', name='Group Output')
        
        if is_modifier:
            self.inputs.add(SocketIn(self, 'NodeSocketGeometry'     , 'geometry'     ))
            
    """
    def __str__(self):
        s = "<Node 'GroupOutput'"
        sep = " : "
        for sock in self.inputs:
            s += f"{sep}{sock.name}"
            sep = ", "
        return s + ">"
    """

    def __repr__(self):
        s = "Node 'GroupOutput'"
        for sock in self.inputs:
            s += f"\n   {sock.name:1s} : {type(sock).__name__}"
        return s + "\n"

    # ----------------------------------------------------------------------------------------------------
    # Connect a socket
    
    def connect(self, node_socket, name=None):
        
        classes = {'Float'      : 'NodeSocketFloat',     
                   'Integer'    : 'NodeSocketInt',       
                   'Boolean'    : 'NodeSocketBool',      
                   'String'     : 'NodeSocketString',    
                   'Vector'     : 'NodeSocketVector',    
                   'Color'      : 'NodeSocketColor',     
                   'Geometry'   : 'NodeSocketGeometry',  
                   'Curve'      : 'NodeSocketGeometry',  
                   'Spline'     : 'NodeSocketGeometry',  
                   'Mesh'       : 'NodeSocketGeometry',  
                   'Points'     : 'NodeSocketGeometry',  
                   'Instances'  : 'NodeSocketGeometry',  
                   'Volume'     : 'NodeSocketGeometry',  
                   'Collection' : 'NodeSocketCollection',
                   'Object'     : 'NodeSocketObject',    
                   'Image'      : 'NodeSocketImage',     
                   'Material'   : 'NodeSocketMaterial',  
                   'Texture'    : 'NodeSocketTexture',
                   }
        
        index = len(self.inputs)
        blid = classes[type(node_socket).__name__]
        if name is None:
            name = type(node_socket).__name__
            
        socket = self.inputs.add(SocketIn(self, blid, name))
        self.inputs[index].link = node_socket
        
    # ----------------------------------------------------------------------------------------------------
    # Build the group output sockets
        
    def setup_bnode(self):
        boutputs = self.btree.outputs
        boutputs.clear()
        for i, sock in enumerate(self.inputs):
            boutputs.new(type=sock.bl_idname, name=sock.name)
            
            
# =============================================================================================================================
# A Layout

class Layout(basenode.Node):
    def __init__(self, name, label="Layout", color=None):
        super().__init__('NodeFrame', name)
        self.label  = label
        self.bcolor = color
        
    def __str__(self):
        return f"[Layout '{self.label}']"

# ====================================================================================================
# Tree of nodes
#
# basenode.Tree simply manages the list of nodes and the created trees
#
# Override this base class for the final behavior

class Tree(basenode.Tree):
            
    def __init__(self, name, is_modifier=True):
        
        super().__init__(name)
        
        self.is_modifier = is_modifier

        # The frames
        
        self.layouts = {}
        self.current_layout = None

        # Unique nodes
        
        self.group_input  = NodeGroupInput(is_modifier)
        self.group_output = NodeGroupOutput(is_modifier)
        self.viewer_      = None
        
        # Debug
        
        self.dirty = False
        
        
    # ----------------------------------------------------------------------------------------------------
    # Set current tree the this instance
            
    def set_tree(self):
        Tree.CURRENT = self
        
    # ----------------------------------------------------------------------------------------------------
    # One single viewer is possible
            
    @property
    def viewer(self):
        
        self.set_tree()
        
        if self.viewer_ is None:
            self.viewer_ = NodeViewer()
            
        return self.viewer_
    
    # ----------------------------------------------------------------------------------------------------
    # Frames management
    
    def open_layout(self, label="Layout", color=("yellow", 0.8, .3)):
        
        name = "Frame"
        if name in self.layouts:
            for i in range(1000):
                name = f"Frame {i}"
                if name not in self.layouts:
                    break
                
        layout = Layout(name, label, color)
        self.layouts[name]  = layout
        self.current_layout = layout
        return layout
    
    def close_layout(self):
        self.current_layout = None
        
    # ----------------------------------------------------------------------------------------------------
    # Register a node
    
    def register_node(self, node):
        super().register_node(node)
        node.layout = self.current_layout
        
    # ----------------------------------------------------------------------------------------------------
    # Input geometry
    
    def get_input_geometry(self, cls=None):
        if self.is_modifier:
            if cls is None:
                cls = classes.Geometry
            return cls(self.group_input.outputs[0])
        else:
            raise RuntimeError(f"Tree {self.name} is not a modifier, it doesn't have an input geometry.")
            
    @property
    def input_geometry(self):
        return self.get_input_geometry()
    
    # ----------------------------------------------------------------------------------------------------
    # Output geometry
    
    @property
    def output_geometry(self):
        if self.is_modifier:
            return self.group_output.inputs[0].link
        else:
            raise RuntimeError(f"Tree {self.name} is not a modifier, it doesn't have an output geometry.")
            
    @output_geometry.setter
    def output_geometry(self, value):
        if self.is_modifier:
            self.group_output.inputs[0].plug(value)
        else:
            raise RuntimeError(f"Tree {self.name} is not a modifier, it doesn't have an output geometry.")
    
    # ----------------------------------------------------------------------------------------------------
    # Implement input creation with specialized methods
    
    def new_input_socket(self, bl_idname, value=None, name="Input"):
        return self.group_input.new_socket(bl_idname, value=value, name=name)
    
    # ----------------------------------------------------------------------------------------------------
    # Add an output
    
    def add_output(self, node_socket, name=None):
        return self.group_output.connect(node_socket, name)
    
    # ====================================================================================================
    # Build the Blender nodes tree
    
    # ----------------------------------------------------------------------------------------------------
    # Get / create the blender tree
    
    @property
    def btree(self):
        btree = bpy.data.node_groups.get(self.name)
        if btree is None:
            btree = bpy.data.node_groups.new(self.name, 'GeometryNodeTree')
        return btree

    # ----------------------------------------------------------------------------------------------------
    # The nodes and links

    @property
    def bnodes(self):
        return self.btree.nodes

    @property
    def blinks(self):
        return self.btree.links

    # ----------------------------------------------------------------------------------------------------
    # A capture attribute node is created by an Attribute node when solving the attributes
    # This allow the algorithm to be written before implementation of nodes
    
    def create_capture_node(self, geometry=None, value=None, data_type=None, domain=None):
        
        # Hack for data type enums
        
        if data_type == 'VECTOR':
            data_type = 'FLOAT_VECTOR'
        elif data_type == 'INTEGER':
            data_type = 'INT'
        elif data_type == 'COLOR':
            data_type = 'FLOAT_COLOR'
        
        return nodes.NodeCaptureAttribute(geometry=geometry, value=value, data_type=data_type, domain=domain)
    
    # ----------------------------------------------------------------------------------------------------
    # Dirty build
    # Build dirty for debug
    
    def dirty_build(self, msg="", stop=False):
        
        if self.dirty:
            return
        
        self.dirty = True
        
        print()
        print('E'*80)
        print()
        
        print(f"Error when building the tree '{self.name}'. Blender nodes tree is incomplete.\n\n {msg}\n")
        print(repr(self))
        
        # ---------------------------------------------------------------------------
        # Reset all
        
        for node in self.nodes:
            node.bnode_ = None
        
        bnodes = self.bnodes
        bnodes.clear()

        blinks = self.blinks
        blinks.clear()

        # ---------------------------------------------------------------------------
        # Nodes
        
        for node in self.nodes:
            try:
                _ = node.bnode
            except:
                pass

        # ---------------------------------------------------------------------------
        # Links
            
        for link in self.links:
            try:
                self.blinks.new(link.socket_out.bsocket, link.socket_in.bsocket)
            except:
                pass

        # ---------------------------------------------------------------------------
        # Arrange
        
        arrange(self.name)
            
        # ---------------------------------------------------------------------------
        # Stop
            
        if stop:
            raise RuntimeError(msg)

    # ----------------------------------------------------------------------------------------------------
    # Builld the whole tree

    def build(self):
        
        # ---------------------------------------------------------------------------
        # Reset all
        
        for node in self.nodes:
            node.bnode_ = None
        
        bnodes = self.bnodes
        bnodes.clear()

        blinks = self.blinks
        blinks.clear()
        
        # ---------------------------------------------------------------------------
        # Put all the nodes which are prop or stack in the same layout
        
        # Work on a copy of the nodes to avoid changing the list
        # while creating layouts
        
        nodes = list(self.nodes)
        for node in nodes:
            
            depends = []
            for nd in nodes:
                if nd.stack_of == node or nd.prop_of == node:
                    depends.append(nd)
                    
            layout = node.layout
            if layout is None:
                if len(depends) > 1:
                    label = node.name if node.label is None else node.label
                    node.layout = self.open_layout(label, color="rose")

            layout = node.layout
            
            if layout is not None:
                for nd in depends:
                    if nd.layout is None:
                        nd.layout = layout
                        
        # ---------------------------------------------------------------------------
        # Solve the attribute nodes
        # Again, since the list of nodes can vary, we must work on the copy
        
        for node in nodes:
            node.solve()
        
        # ---------------------------------------------------------------------------
        # Start by building the group input and output nodes
        
        _ = self.group_input.bnode
        _ = self.group_output.bnode
        
        # ---------------------------------------------------------------------------
        # Build the nodes node connected to the group inputs and outputs
        
        for node in self.nodes:
            _ = node.bnode
            
        # ---------------------------------------------------------------------------
        # Build the links
        
        for link in self.links:
            self.blinks.new(link.socket_out.bsocket, link.socket_in.bsocket)
            
                
        # ---------------------------------------------------------------------------
        # Arrange
        
        arrange(self.name)
    



            
        
