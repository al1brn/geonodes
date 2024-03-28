#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:36:21 2023

@author: alain
"""

import bpy
from mathutils import Vector, Color
import numpy as np

from geonodes.core.treearrange import arrange


# ====================================================================================================
# Get a node tree

def get_tree(name, tree_type='GeometryNodeTree', create=False, clear=False):
    
    #type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
    
    tree = bpy.data.node_groups.get(name)
    if tree is None:
        if not create:
            return None
        tree = bpy.data.node_groups.new(name=name, type=tree_type)
        
    if clear:
        tree.nodes.clear()
        
    return tree

def del_tree(name):
    tree = get_tree(name)
    if tree is not None:
        bpy.data.node_groups.remove(tree)
        
def snake_case(name):
    if name == 'ID':
        return name
    elif name == 'ColorRamp':
        return 'color_ramp'
    else:
        return name.lower().replace(' ', '_')
    
# ----------------------------------------------------------------------------------------------------
# Explode a socket key into : name, index, in or out
    
def x_sock_key(skey):
    
    # _foo   : 'Foo' output socket
    # bar_   : 'Bar' input socket
    # _foo_1 : Second enabled output socket named 'Foo'
    # bar_1_ : Second enabled input socket named 'Bar'
    
    # ----- In / Out
    
    skey = skey.lower()
    
    is_in = None
    if skey[0] == '_':
        skey = skey[1:]
        is_in = False
    elif skey[-1] == '_':
        skey = skey[:-1]
        is_in = True
        
    # ----- Order in the homonyms
    
    if skey[-2] == '_' and skey[-1].isdigit():
        return skey[:-2], int(skey[-1]), is_in
    else:
        return skey, 0, is_in
    
# ----------------------------------------------------------------------------------------------------
# make sure a socket key is in or out

def io_sock_key(name):
    
    skey = snake_case(name)
    
    if skey[0] == '_' or skey[-1] == '_':
        return skey
    else:
        return skey + '_'
    
# ====================================================================================================
# valid value

def value_for(value, socket_type):
    if value is None:
        return value
    
    if socket_type in ['NodeSocketBool']:
        return bool(value)
    
    elif socket_type in ['NodeSocketInt', 'NodeSocketIntUnsigned', 'NodeSocketIntFactor', 'NodeSocketIntPercentage']:
        return int(value)
    
    elif socket_type in ['NodeSocketFloat', 'NodeSocketFloatFactor', 'NodeSocketFloatAngle', 'NodeSocketFloatDistance', 
                         'NodeSocketFloatPercentage', 'NodeSocketFloatTime', 'NodeSocketFloatTimeAbsolute', 'NodeSocketFloatUnsigned']:
        return float(value)
    
    elif socket_type in ['NodeSocketVector', 'NodeSocketVectorEuler', 'NodeSocketVectorXYZ', 'NodeSocketVectorTranslation', 'NodeSocketVectorAcceleration',
                         'NodeSocketVectorDirection', 'NodeSocketVectorVelocity']:
        if isinstance(value, Vector):
            return value
        elif np.shape(value) == ():
            return Vector((value, value, value))
        else:
            return Vector(value)
    
    elif socket_type in ['NodeSocketColor']:
        if isinstance(value, Color):
            return (value.r, value.g, value.b, 1)
        elif np.shape(value) == ():
            return (value, value, value, 1)
        elif len(value) == 3:
            return tuple(value) + (1.,)
        else:
            return value
    
    elif socket_type in ['NodeSocketString']:
        return value
    
    elif socket_type in ['NodeSocketGeometry']:
        return value
    
    elif socket_type in ['NodeSocketCollection']:
        if isinstance(value, str):
            return bpy.data.collections[value]
        else:
            return value
    
    elif socket_type in ['NodeSocketImage']:
        if isinstance(value, str):
            return bpy.data.images[value]
        else:
            return value
    
    elif socket_type in ['NodeSocketMaterial']:
        if isinstance(value, str):
            return bpy.data.materials[value]
        else:
            return value
    
    elif socket_type in ['NodeSocketObject']:
        if isinstance(value, str):
            return bpy.data.objects[value]
        else:
            return value
    
    elif socket_type in ['NodeSocketTexture']:
        if isinstance(value, str):
            return bpy.data.objects[value]
        else:
            return value
        
    else:
        raise Exception(f"Unknown socket type: {socket_type}")
    
    
# ====================================================================================================
# List of sockets

class Sockets:
    def __init__(self, bnode, is_input=True):
        self.bnode    = bnode
        self.is_input = is_input
        self.sockets  = bnode.inputs if is_input else bnode.outputs

    def __str__(self):
        return f"{list(self.keyed_sockets.keys())}"
    
    def __len__(self):
        return len(self.enabled_sockets)
    
    def __getitem__(self, index):
        return self.get_socket(index)
        
    # ----------------------------------------------------------------------------------------------------
    # List of enabled sockets
    
    @property
    def enabled_sockets(self):
        return [sock for sock in self.sockets if sock.enabled]

    # ----------------------------------------------------------------------------------------------------
    # Dict 
    
    @property
    def keyed_sockets(self):
        
        # ----- Count the homonyms
        
        esocks = self.enabled_sockets
        counts = {}
        for sock in esocks:
            key = snake_case(sock.name)
            if key in counts.keys():
                counts[key] += 1
            else:
                counts[key] = 0
        
        # ----- Build the keyed sockets
        
        pref, suff = ('', '_') if self.is_input else ('_', '')
        indices = {key: 0 for key in counts.keys()}
        ksocks  = {}
        for sock in esocks:
            key = snake_case(sock.name)
            if counts[key] == 0:
                scount = ''
            else:
                scount = f"_{indices[key]}"
                indices[key] += 1
            
            name = f"{pref}{key}{scount}{suff}"
            ksocks[name] = sock
            
        return ksocks
    
    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its name
        
    def get_socket(self, name=None):
        
        if name is None:
            return self.enabled_sockets[0]
        
        elif isinstance(name, (int, np.int32, np.int64)):
            return self.enabled_sockets[name]
        
        elif isinstance(name, str):
            skey = io_sock_key(name) if self.is_input else snake_case(name)
            ksocks = self.keyed_sockets
            sock = ksocks.get(skey)
            if sock is not None:
                return sock
            
        raise AttributeError(f"Socket named '{name}' not found : {str(self)}")

    # ----------------------------------------------------------------------------------------------------
    # First socket compatible with the typme of another socket
        
    def first_compatible(self, socket):
        for sock in self.sockets:
            if not sock.enabled:
                continue
            
            if socket.type in ['INT', 'FLOAT'] and sock in ['INT', 'FLOAT']:
                return sock
            
            if socket.type == sock.type:
                return sock
            
        return None
    
# ====================================================================================================
# A Node

class Node:

    STD_ATTRS = [
       '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
       'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
       'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
       'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
       'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
       'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
       'show_texture', 'socket_value_update', 'type', 'update', 'use_custom_color',
       'width', 'width_hidden']
    
    def __init__(self, tree, bnode, node_label=None, node_color=None, **kwargs):
        
        self.tree        = tree
        self.bnode       = bnode
        self.node_label  = node_label
        self.node_color  = node_color
        
        self.in_sockets  = Sockets(self.bnode, True)
        self.out_sockets = Sockets(self.bnode, False)
        
        self.attributes  = [name for name in dir(bnode) if name not in Node.STD_ATTRS]
        
        # ----- Initialize the input sockets
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            #socket = self.in_sockets[key]
            #self.tree.set_socket(socket, value)
        
    def __str__(self):
        attrs = []
        for k in self.attributes:
            attrs.append(f"{k}: {getattr(self, k)}")
        return f"<Node '{self.node_label}': inputs: {self.in_sockets}, attributes: {','.join(attrs)}, outputs: {self.out_sockets}>"
    
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

    # ----------------------------------------------------------------------------------------------------
    # Get attribute

    def __getattr__(self, name):
        
        bnode       = self.__dict__.get('bnode')
        attributes  = self.__dict__.get('attributes')
        
        # ----- Name can be a blender node attribute
        
        if bnode is not None and attributes is not None and name in attributes:
            return getattr(bnode, name)
        
        # ----- It can be the name of a socket
        
        # Ensure there is _ in suffix or prefix
        skey = io_sock_key(name)
        
        # Input or output socket
        is_in = skey[-1] == '_'
        if is_in:
            sockets = self.__dict__.get('in_sockets')
        else:
            sockets = self.__dict__.get('out_sockets')
            
        try:
            return sockets[skey]
        except AttributeError:
            pass
        
        # ----- This is an error
        
        ksocks = self.__dict__.get('in_sockets')
        s = "" if ksocks is None else str(ksocks.keyed_sockets.keys())
        ksocks = self.__dict__.get('out_sockets')
        if ksocks is not None:
            s += str(ksocks.keyed_sockets.keys())
        
        raise AttributeError(f"Node Attribute Error: Node '{bnode.name}' doesn't have '{name}' attribute.\n{s}")

    # ----------------------------------------------------------------------------------------------------
    # Set attribute

    def __setattr__(self, name, value):
        
        bnode       = self.__dict__.get('bnode')
        attributes  = self.__dict__.get('attributes')
        
        # ----- Name of a blender node attribute
        
        if bnode is not None and attributes is not None:
            if name in attributes:
                try:
                    setattr(bnode, name, value)
                except TypeError as e:
                    raise TypeError(f"Value '{value}' for node '{self.node_label}' attribute '{name}' is not valid.\nValid values are {str(e)[54:]}\n\n")
                return

        # ----- Name of a socket
        
        # Ensure there is _ in suffix or prefix
        skey = io_sock_key(name)
        
        # Input or output socket
        is_in = skey[-1] == '_'
        if is_in:
            sockets = self.__dict__.get('in_sockets')
        else:
            sockets = self.__dict__.get('out_sockets')
            
        if sockets is not None:
            try:
                socket = sockets[skey]
            except AttributeError:
                socket = None
                    
            if socket is not None:
                self.tree.set_socket(socket, value)
                return
        
        # ----- Let's try to display a proper error message to avoid the let the user think he has properly set a Node attribute
                    
        if not name in ['tree', 'bnode', 'in_sockets', 'out_sockets', 'attributes', 'node_label', 'node_color']:
            raise TypeError(f"Node attribute '{name}' is not valid.\nAttributes: {self.__dict__.get('attributes')}\nBlender Node: {dir(bnode)}")
            
        # ----- Nothing abnormal
            
        super().__setattr__(name, value)

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
# A tree

class Tree:
    
    NODES = {
        'CompositorNodeTree' : None,
        'TextureNodeTree'    : None, 
        'GeometryNodeTree'   : None, 
        'ShaderNodeTree'     : None,        
        }
    
    SOCKET_TYPES = {
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
    
    
    def __init__(self, tree_type, name, create=True, clear=False, is_group=False):
        
        self.tree_type = tree_type
        self.is_group  = is_group
        if self.node_types is None:
            Tree.init_nodes(tree_type)
            
        if isinstance(name, str):
            self.btree = get_tree(name, tree_type, create=create, clear=False)
        else:
            self.btree = name
            
        if clear:
            self.clear()

    # ====================================================================================================
    # Str
        
    def __str__(self):
        return f"<Tree: {len(self.btree.nodes)} nodes and {len(self.btree.links)} links>"
    
    # ====================================================================================================
    # Dict : node user name --> node type
    
    # ----------------------------------------------------------------------------------------------------
    # Dictionary of the tree type

    @property
    def node_types(self):
        return self.NODES[self.tree_type]

    # ----------------------------------------------------------------------------------------------------
    # Init the dictionary of the tree type
            
    @classmethod
    def init_nodes(cls, tree_type):
        cls.NODES[tree_type] = {}
        
        btree = get_tree("GEOPY - Temp", tree_type=tree_type, create=True, clear=True)

        for type_name in dir(bpy.types):
            try:
                bnode = btree.nodes.new(type=type_name)
            except RuntimeError as e:
                continue
            
            if 'legacy' in bnode.name.lower():
                continue
            
            cls.NODES[tree_type][bnode.name.lower().strip()] = (type_name, bnode.name)
            
        del_tree(btree.name)
        
    # ----------------------------------------------------------------------------------------------------
    # Get the node bl_idname from the user node name
        
    def get_type_name(self, name, halt=True):
        
        key = name.lower().strip()
        
        node_spec = self.node_types.get(key)
        if node_spec is not None:
            return node_spec[0]
        
        cands = {}
        for k, ns in self.node_types.items():
            if k[:len(key)] == key:
                cands[k] = ns
                
        if len(cands) == 1:
            return list(cands.values())[0][0]
        
        if not halt:
            return None

        if len(cands) == 0:
            raise Exception(f"Tree node name error: node name '{name}' doesn't exist")
            
        raise Exception(f"Tree node name error: the node name '{name}' is ambigous. Several possibilities exist: {[n for (t, n) in cands.values()]}")

    # ====================================================================================================
    # Has user input / output
    
    @property
    def group_input(self):
        return None
        
    @property
    def group_output(self):
        return None

    # ====================================================================================================
    # Arrange

    def arrange(self):
        arrange(self.btree)
        return self
        
    # ====================================================================================================
    # Node access
        
    def node(self, node_name, node_label=None, node_color=None, **kwargs):
        node = Node(self, self.btree.nodes.new(type=self.get_type_name(node_name)), node_label=node_label, node_color=node_color, **kwargs)
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
        inp.default_value = value_for(value, socket_type)
    
    def new_output(self, name, socket_type, value=None):
        outp = self.btree.outputs.new(name=name, type=Tree.get_socket_type(socket_type))
        outp.default_value = value_for(value, socket_type)
        
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
            socket.default_value = value_for(value, socket.bl_idname)
    
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
    
    def boolean(self, value=True, **kwargs):
        node = self.node("Boolean", **kwargs)
        node.boolean = value
        return node._boolean
    
    def int(self, value=0, **kwargs):
        node = self.node("Integer", **kwargs)
        node.integer = value
        return node._integer
    
    def float(self, value=True, **kwargs):
        node = self.node("Value", **kwargs)
        self.set_socket(node._value, value)
        return node._value
    
    def string(self, value="", **kwargs):
        node = self.node("String", **kwargs)
        node.string=value
        return node._string
        
    def vector(self, value=(0, 0, 0), **kwargs):
        node = self.node("Vector", **kwargs)
        node.vector=Vector(value)
        return node._vector
    
    def rgb(self, value=(.9, .9, .9, 1), **kwargs):
        node = self.node("RGB", **kwargs)
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
    def __init__(self, name, create=True, clear=False, is_group=False):
        
        self.material = None
        if is_group:
            super().__init__('ShaderNodeTree', name, create=create, clear=clear, is_group=True)
            
        else:
            mat = bpy.data.materials.get(name)
            if mat is None:
                mat = bpy.data.materials.new(name)
                
            mat.use_nodes = True
            super().__init__('ShaderNodeTree', mat.node_tree, create=False, clear=clear, is_group=False)
            self.material = mat
            
    def clear(self):
        super().clear()
        
        if self.is_group:
            Tree.clear_inout(self.btree.inputs, False)
            Tree.clear_inout(self.btree.outputs, False)
        
            
    # ====================================================================================================
    # Material output            
            
    @property
    def output_material(self):
        for node in self.btree.nodes:
            if node.bl_idname == 'ShaderNodeOutputMaterial':
                return Node(self, node)
        
        return self.node("Material Output")
    
    @property
    def surface(self):
        return self.output_material.surface_
        
    @surface.setter
    def surface(self, value):
        self.set_socket(self.output_material.surface_, value)
        
    @property
    def volume(self):
        return self.output_material.volume_
        
    @volume.setter
    def volume(self, value):
        self.set_socket(self.output_material.volume_, value)
        
    @property
    def displacement(self):
        return self.output_material.displacement_
        
    @displacement.setter
    def displacement(self, value):
        self.set_socket(self.output_material.displacement_, value)
        
    # ====================================================================================================
    # Some usefull Trees
    
    @classmethod
    def ImageTexture(cls, image, name="Image Texture", clear=False, **kwargs):
        
        tree = cls(name, create=True, clear=clear)
        
        img = tree.get_create("Image Texture", vector=tree.get_create("Texture Coordinate")._uv)
        img.bnode.image = image

        bsdf = tree.get_create("Principled BSDF", base_color=img._color)
        for k, v in kwargs.items():
            setattr(bsdf, k, v)
        
        tree.link(bsdf.output, tree.surface)
        
        return tree.arrange()
        
    
    @classmethod
    def Smoke(cls, name="Smoke"):
        tree = cls(name, create=True, clear=True)
        
        vol = tree.get_create("Principled Volume", color=(.5, 1, .1))
        tree.link(vol.output, tree.volume)
        
        return tree
    
        
# ====================================================================================================
# Geometry Nodes Tree

class GeoNodes(Tree):
    
    def __init__(self, name, create=True, clear=False, is_group=False):
        
        super().__init__('GeometryNodeTree', name, create=create, clear=clear, is_group=is_group)
        
        self.btree.is_modifier = True
        
        self.input_node  = None
        self.output_node = None
        
        for bnode in self.btree.nodes:
            if bnode.bl_idname == 'NodeGroupInput':
                self.input_node = Node(self, bnode)
            if bnode.bl_idname == 'NodeGroupOutput':
                self.output_node = Node(self, bnode)
                
        if self.input_node is None:
            self.input_node = self.node("Group Input")
        if self.output_node is None:
            self.output_node = self.node("Group Output")
            
        if not is_group:
            _ = self.input_geometry
            _ = self.output_geometry
            
    def clear(self):
        super().clear()
        
        # OLD VERSION ?
        #Tree.clear_inout(self.btree.inputs,  keep_first = not self.is_group)
        #Tree.clear_inout(self.btree.outputs, keep_first = not self.is_group)

    # ====================================================================================================
    # Input and output nodes
        
    @property
    def group_input(self):
        return self.get_create("Group Input")
        
    @property
    def group_output(self):
        return self.get_create("Group Output")
            
    # ====================================================================================================
    # Input and output geometries
    
    @property
    def input_geometry(self):
        
        for item in self.btree.interface.items_tree:
            if item.item_type != 'SOCKET':
                continue
            if item.socket_type == 'NodeSocketGeometry' and item.in_out == 'INPUT':
                return self.input_node.bnode.outputs[item.identifier]
            
        # ----- Create the input geometry
            
        new_socket = self.btree.interface.new_socket(name='Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
        return self.input_node.bnode.outputs[new_socket.identifier]
        
    @property
    def output_geometry(self):
        
        for item in self.btree.interface.items_tree:
            if item.item_type != 'SOCKET':
                continue
            if item.socket_type == 'NodeSocketGeometry' and item.in_out == 'OUTPUT':
                return self.output_node.bnode.inputs[item.identifier]
            
        # ----- Create the input geometry
            
        new_socket = self.btree.interface.new_socket(name='Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')
        return self.output_node.bnode.inputs[new_socket.identifier]
    
    @property
    def ig(self):
        return self.input_geometry
    
    @property
    def og(self):
        return self.output_geometry
    
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
        






