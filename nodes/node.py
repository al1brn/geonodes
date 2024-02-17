#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov  3 09:36:21 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Python to nodes module

Node

"""

import bpy
from geopy.nodes import utils
from geopy.nodes import sockets
from geopy.nodes.sockets import Sockets

# ====================================================================================================
# List of available nodes per tree type
# Nodes are initialized when an instance of Tree is called

NODES = {
    'CompositorNodeTree' : None,
    'TextureNodeTree'    : None, 
    'GeometryNodeTree'   : None, 
    'ShaderNodeTree'     : None,        
    }


# ====================================================================================================
# Analyze a node
#
# Nodes are analyzed once per tree

class NodeInfo:

    STD_ATTRS = [
       '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
       'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
       'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
       'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
       'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
       'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
       'show_texture', 'socket_value_update', 'type', 'update', 'use_custom_color',
       'width', 'width_hidden']
    
    def __init__(self, btree, bnode):
        
        self.bl_idname   = bnode.bl_idname
        self.name        = bnode.name
        self.python_name = utils.snake_case(bnode.name)
        self.class_name  = f"{bnode.name} class".title().replace(' ', '')
        self.in_socket   = None
        self.out_socket  = None
        self.int_links   = []
        self.params      = [name for name in dir(bnode) if name not in NodeInfo.STD_ATTRS]
        self.prm_defs    = {name: getattr(bnode, name) for name in self.params}
        self.in_socks    = [(utils.snake_case(bsock.name), bsock.enabled, bsock.type) for bsock in bnode.inputs]
        self.out_socks   = [(utils.snake_case(bsock.name), bsock.enabled, bsock.type) for bsock in bnode.outputs]
        
        # ====================================================================================================
        # Sockets
        
        # ----- Force internal links by connecting output sockets to the input sockets
        
        for out_socket in bnode.outputs:
            for in_socket in bnode.inputs:
                if in_socket.type == out_socket.type:
                    blink = btree.links.new(in_socket, out_socket, verify_limits=True)
                    
        # ----- Capture the internal links which are set when muting the node

        bnode.mute = True
        for link in bnode.internal_links:
            self.int_links.append([link.from_socket.name, link.to_socket.name])
            
            # ----- Add a method to the sockets dictionary
            
            method = lambda slf, *args, **kwargs: sockets.socket_call_node(slf, slf.tree, self.python_name, self.int_links[-1][0], self.int_links[1][1], *args, **kwargs)
            sockets.add_socket_method(type(btree).__name__, link.from_socket.type, self.python_name, method)
            
        if len(self.int_links):
            self.in_socket  = self.int_links[0][0]
            self.out_socket = self.int_links[0][1]
            
            
        elif len(bnode.outputs):
            self.out_socket = bnode.outputs[0]

        # ====================================================================================================
        # Attributes
        
        # TBD
        
    # ====================================================================================================
    # Detailed info
    
    def __repr__(self):
        tab = "   "
        s  = f"Node {self.name}, python name: {self.python_name}\n"
        s += "\nParameters"
        s += "\n----------"
        if len(self.params) == 0:
            s += "\n{tab}None"
        else:
            for k, v  in self.prm_defs.items():
                s += f"\n{tab}{k:12s} = {v}"
        s += "\n"
        
        s += "\nInput sockets"
        s += "\n-------------"
        for sck in self.in_socks:
            s += f"\n{tab}{sck[0]:12s} {'X' if sck[1] else '-'} {sck[2]}"
        s += "\n"
        
        s += "\nOutput sockets"
        s += "\n--------------"
        for sck in self.out_socks:
            s += f"\n{tab}{sck[0]:12s} {'X' if sck[1] else '-'} {sck[2]}"
        s += "\n"
        
        return s
        
    # ----------------------------------------------------------------------------------------------------
    # Get a snapshot of the node
    #
    # sockets enablement
    # parameters possible values
    
    def get_snapshot(self):
        ins  = {socket.enabled for socket in self.bnode.inputs}
        outs = {socket.enabled for socket in self.bnode.outputs}
        attrs = {}
        for name in self.params:
            
            attrs[name] = None
            
            v = getattr(self.bnode, name)
            if isinstance(v, str):
                try:
                    setattr(self.bnode, name, 'ERROR')
                    
                except TypeError as e:
                    msg = str(e)
                    i = msg.find('enum "ERROR" not found in')
                    if i > 0:
                        attrs[name] = eval(msg[i+26:])
                        
        return ins, outs, attrs

    # ----------------------------------------------------------------------------------------------------
    # Socket call
    #
    # A socket can create a node when it is one of its internal links
    #
    # For instance a mesh output socket can call "set_material(self, material)" where
    # self is used as to output socket linked to the mesh input socket of the node.
    
    def socket_call(self):
        pass



# ====================================================================================================
# Tree

class Tree:
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
        
    def __str__(self):
        return f"<Tree '{self.tree_type}': '{self.btree.name}'>"
        
    # ====================================================================================================
    # Create a node
    #
    # Called by methods dynamically created, for instance:
    #
    # def set_material(self, *args, node_label=None, node_color=None, **kwargs):
    #    return self.create_node('Tree.SetMaterialClass', *args, node_label=None, node_color=None, **kwargs)
    
    def create_node(self, class_name, *args, node_label=None, node_color=None, **kwargs):
        # Note that in the following line, 'self' argument is for tree=self
        return getattr(self, class_name)(self, *args, node_label=None, node_color=None, **kwargs)

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
    # Create the methods to create a node
    
    @classmethod
    def create_node_class(cls, btree, bnode):
        
        node_info = NodeInfo(btree, bnode)
        
        # ----------------------------------------------------------------------------------------------------
        # Node initialization
        
        exec(f"""
def node_init(self, tree, *args, node_label=None, node_color=None, **kwargs):
    Node.__init__(self, tree, '{bnode.bl_idname}', node_label=node_label, node_color=node_color, **kwargs)
            """)
    
        # ----------------------------------------------------------------------------------------------------
        # Class Creation
        
        node_class = type(node_info.class_name, (Node,), {
            '__init__'  : locals()['node_init'],
            'params'    : list(node_info.params),
            'node_info' : node_info,
            })

        # ----------------------------------------------------------------------------------------------------
        # Instance
        
        def tree_create_node(self, *args, node_label=None, node_color=None, **kwargs):
            return self.create_node(node_info.class_name, *args, node_label=node_label, node_color=node_color, **kwargs)
            #return getattr(self, node_info.class_name)(tree=self, node_label=node_label, node_color=node_color, **kwargs)
        
        # ----------------------------------------------------------------------------------------------------
        # Add a method which return a node
        
        setattr(cls, node_info.class_name, node_class)
        setattr(cls, f"{node_info.python_name}", tree_create_node)
    
        

class CompositorTree(Tree):
    tree_type = 'CompositorNodeTree'
    INIT = False

class TextureTree(Tree):
    tree_type = 'TextureNodeTree'
    INIT = False

class GeoNodesTree(Tree):
    tree_type = 'GeometryNodeTree'
    INIT = False

class ShaderTree(Tree):
    tree_type = 'ShaderNodeTree'
    INIT = False

# ====================================================================================================
# A Node

class Node(StackedNode):
    
    def __new__(cls, *args, **kwargs):
        cur_tt = current_tree_type()
        
        if cls.tree_type != cur_tt:
            if cls.tree_type is not None:
                for attr_name in NODE_METHODS[cls.tree_type].keys():
                    delattr(cls, attr_name)
                    
            cls.tree_type = cur_tt
            for attr_name, value in NODE_METHODS[cls.tree_type].items():
                setattr(cls, attr_name, value)
                
        return StackedNode.__new__(cls, *args, **kwargs)
    
    

    def __init__(self, tree, bl_idname, *args, node_label=None, node_color=None, **kwargs):
        """ Create a Node.
        
        Arguments
        ---------
            - tree ()
            - bl_idname : node identifier
            - args : sockets for multi input sockets
            - node_label (str = None) : the label to set
            - node_color (color = None) : the color to use
            - **kwargs : Node parameters and input sockets initializations
        """
        
        self.tree        = tree
        self.bnode       = tree.btree.nodes.new(type=bl_idname)
        self.node_label  = node_label
        self.node_color  = node_color
        
        self.in_sockets  = Sockets(self, True)
        self.out_sockets = Sockets(self, False)
        
        # Last attribute
        self.initialized = True
        
        # ----- Set the attributes because they can change the sockets enablement
        
        sockets = []
        for key, value in kwargs.items():
            if key in self.params:
                setattr(self, key, value)
            else:
                sockets.append(key)
                
        # ----- Set the multi-input socket
        
        if len(args):
            mi_socket = self.in_sockets.get_multi_input_socket(halt=True)
            for arg in args:
                mi_socket = arg

        # ----- Set the sockets
        
        for key in sockets:
            setattr(self, key, kwargs[key])
        
    def __str__(self):
        return f"<Node '{self.bnode.name}'>"
        
        attrs = []
        for k in self.attributes:
            attrs.append(f"{k}: {getattr(self, k)}")
        return f"<Node '{self.node_label}': inputs: {self.in_sockets}, attributes: {','.join(attrs)}, outputs: {self.out_sockets}>"
    
    def __repr__(self):
        s  = f"Node '{self.bnode.name}' - '{self.node_label}'"
        s += f"\n Attributes: {self.attributes}"
        s += f"\n Input sockets:  [socket.name for socket in self.bnode.inputs]"
        s += f"\n Output sockets: [socket.name for socket in self.bnode.outputs]"
        return s + "\n"
        
    
    # =============================================================================================================================
    # Type of tree
    
    @property
    def tree_type(self):
        return self.tree.tree_type
        
    # =============================================================================================================================
    # Node label and color
        
    @property
    def node_label(self):
        s = self.bnode.label
        if s is None or s == "":
            return self.bnode.name
        else:
            return s
    
    @node_label.setter
    def node_label(self, value):
        if value is None:
            return
        self.bnode.label = value
    
    @property
    def node_color(self):
        return self.bnode.color
    
    @node_color.setter
    def node_color(self, value):
        if value is None:
            return
        self.bnode.color = value
        
    # =============================================================================================================================
    # blender node attributes

    def __setattr__(self, name, value):
        if self.__dict__.get('initialized') is None:
            super().__setattr__(name, value)
            return
        
        if name in self.node_info.params:
            setattr(self.bnode, name, value)
        else:
            self.in_sockets[name] = value
        
    def __getattr__(self, name):
        out_sockets = self.__dict__.get('out_sockets')
        if out_sockets is None:
            raise AttributeError(f"Node class has no attribute named '{name}'.")
            
        return out_sockets[name]
        

    # =============================================================================================================================
    # Input and output sockets by name
    # In / out sockets
    
    def in_socket(self, name=None, index=None):
        if is_instance(name, str):
            skey = snake_case(name)
            if index is not None:
                name += f"_{index}"
            skey += '_'
        else:
            skey = name
            
        return self.in_sockets[skey]
    
    def out_socket(self, name=None, index=None):
        if isinstance(name, str):
            skey = snake_case(name)
            if index is not None:
                name += f"_{index}"
            skey = '_' + skey
        else:
            skey = name
        return self.out_sockets[skey]
    
    # =============================================================================================================================
    # Default input / output
    
    @property
    def input(self):
        return self.in_sockets[0]
    
    @property
    def output(self):
        return self.out_sockets[0]

# ====================================================================================================
# Create Node classes

def create_node_class(tree_type, btree, bnode):
    
    attributes = [name for name in dir(bnode) if name not in Node.STD_ATTRS]
    node_name  = utils.snake_case(bnode.name)
    
    # ----------------------------------------------------------------------------------------------------
    # Node initialization
    
    exec(f"""
def node_init(self, *args, node_label=None, node_color=None, **kwargs):
    print("Node init")
    new_bnode = self.btree.nodes.new(type='{bnode.bl_idname}')
    super().__init__(self, *args, new_bnode, node_label=node_label, node_color=node_color, **kwargs)
         """)

    # ----------------------------------------------------------------------------------------------------
    # Node str
    
    def node_str(self):
        return f"<Node '{bnode.name}'>"
        
    # ----------------------------------------------------------------------------------------------------
    # Node repr
    
    def node_repr(self):
        s  = f"Node '{bnode.name}' - 'self.node_label'"
        s += f"\n Attributes: {attributes}"
        s += f"\n Input sockets:  [socket.name for socket in node.inputs]"
        s += f"\n Output sockets: [socket.name for socket in node.outputs]"
        return s + "\n"

    # ----------------------------------------------------------------------------------------------------
    # Class Creation
    
    exec(f"""
def node_class(self):
    return type('{node_name}_class', (Node,), {
        '__init__' : locals()['node_init'],
        }
         """)
    
    @property
    def node_class(self):
        return type(f"{node_name}_class", (Node, ), {
            '__init__' : locals()['node_init'],
            })
            
    # ----------------------------------------------------------------------------------------------------
    # Instance
    
    def node_instance(self, *args, node_label=None, node_color=None, **kwargs):
        return getattr(self, f"{node_name}_class")(*args, node_label=node_label, node_color=node_color, **kwargs)

    # ----------------------------------------------------------------------------------------------------
    # Add a method which return a node
    
    root = ROOTS[tree_type]
    setattr(root, f"{node_name}", node_instance)

            
# ====================================================================================================
# Build the list of available nodes

def build_nodes_list(tree_type):
    
    NODES[tree_type] = {}
        
    btree = utils.get_tree("GEOPY - Temp", tree_type=tree_type, create=True, clear=True)

    for type_name in dir(bpy.types):
        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue
        
        if 'legacy' in bnode.name.lower():
            continue
        
        #NODES[tree_type][bnode.name.lower().strip()] = (type_name, bnode.name)
        NODES[tree_type][bnode.name.lower().strip()] = NodeInfo(bnode, btree)
        
        create_node_class(tree_type, btree, bnode)  
            
    utils.del_tree(btree.name)
    
    #pprint(sorted([v[0] for v in NODES[tree_type].values()]))
    



# ====================================================================================================
# Get node info from its python method name

def get_node_info(tree_type, python_name, halt=True):
    
    # ----- List of (bl_idname, node name)
    
    nodes = NODES[tree_type]
    if nodes is None:
        build_nodes_list(tree_type)
        nodes = NODES[tree_type]
        
    # ----- Node python key
            
    key = python_name.lower().replace('_', ' ')
    
    # ----- Exact match
    
    node_info = nodes.get(key)
    if node_info is not None:
        return node_info
    
    # ----- Look for candidates
        
    cands = {}
    for k, ns in nodes.items():
        if k[:len(key)] == key:
            cands[k] = ns
            
    if len(cands) == 1:
        return list(cands.values())[0]
    
    if not halt:
        return None
    
    if len(cands) == 0:
        raise AttributeError(f"{tree_type} node name error: impossible to find a Node named '{python_name}'")
        
    raise AttributeError(f"{tree_type} node name error: the node name '{python_name}' is ambigous. Several possibilities exist: {[n for (t, n) in cands.values()]}")
        
  # ====================================================================================================
  # Get a node bl_idname from its python method name

def get_node_blidname(tree_type, python_name):
      
    return get_node_info(tree_type, python_name, halt=True).bl_idname

    
    
    


