#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:15:16 2022

@author: alain
"""

import bpy
import itertools
from pprint import pprint
import logging
logger = logging.getLogger('geonodes')

from .color import Color
from .arrange import arrange

# =============================================================================================================================
# Data socket: a root for data classes

class DataSocket:
    """ Wrap a node socket to provide the root class for data.
    
    Basically stores the node and the Blender socket it represents.
    
    Children classes are Boolean, Integer, Float, Geometry...
    """

    def __init__(self, socket, node=None):
        
        if isinstance(socket, DataSocket):
            self.bsocket = socket.get_blender_socket()
        elif isinstance(socket, bpy.types.NodeSocket):
            self.bsocket = socket
        else:
            raise RuntimeError(f"A DataSocket instance needs a socket to be initialized, not {socket}.")
            
        if node is None:
            self.node = Tree.TREE.get_bnode_wrapper(self.bsocket.node)
        else:
            self.node = node
        
    def __str__(self):
        snode = str(self.node)
        if self.is_output:
            return f"{snode}.{self.name}"
        else:
            return f"{self.name}.{snode}"
        
    def __repr__(self):
        return str(self)
    
    @property
    def bl_idname(self):
        return self.bsocket.bl_socket_idname if isinstance(self.bsocket, bpy.types.NodeSocketInterfaceGeometry) else self.bsocket.bl_idname
        
    
    @property
    def name(self):
        return self.bsocket.name
        
    @property
    def is_output(self):
        return self.bsocket.is_output
    
    @property
    def is_multi_input(self):
        return self.bsocket.is_multi_output
    
    @property
    def links(self):
        return self.bsocket.links

    @property
    def bnode(self):
        return self.bsocket.node
    
    @property
    def index(self):
        if self.is_output:
            bsockets = self.bnode.outputs
        else:
            bsockets = self.bnode.inputs
            
        for index, bsocket in enumerate(bsockets):
            if self.bsocket == bsocket:
                return index
            
        raise RuntimeError(f"Impossible to find the index of socket {self} of node {self.node}")
        
    def connected_sockets(self):
        sockets = []
        for link in self.links:
            if self.is_output:
                bsocket = link.to_socket
            else:
                bsocket = link.from_socket
            sockets.append(self.node.tree.get_bsocket_wrapper(bsocket))
        return sockets
    
    # ----------------------------------------------------------------------------------------------------
    # Class name from socket bl_idname
    
    @staticmethod
    def get_class_name(socket, with_sub_class = False):
        blids = {
            'NodeSocketBool'        : ('Boolean',    ''), 
    
            'NodeSocketInt'         : ('Integer',    ''), 
            'NodeSocketIntUnsigned' : ('Integer',    'Unsigned'), 
    
            'NodeSocketFloat'       : ('Float',      ''), 
            'NodeSocketFloatFactor' : ('Float',      'Factor'),
            'NodeSocketFloatAngle'  : ('Float',      'Angle'), 
            'NodeSocketFloatDistance': ('Float',     'Distance'), 
    
            'NodeSocketVector'      : ('Vector',     ''), 
            'NodeSocketVectorEuler' : ('Vector',     'Rotation'),
            'NodeSocketVectorXYZ'   : ('Vector',     'xyz'), 
            'NodeSocketVectorTranslation' : ('Vector', 'Translation'), 
    
            'NodeSocketColor'       : ('Color',      ''), 
            'NodeSocketString'      : ('String',     ''), 
    
            'NodeSocketGeometry'    : ('Geometry',   ''), 
    
            'NodeSocketCollection'  : ('Collection', ''), 
            'NodeSocketImage'       : ('Image',      ''), 
            'NodeSocketMaterial'    : ('Material',   ''), 
            'NodeSocketObject'      : ('Object',     ''), 
            'NodeSocketTexture'     : ('Texture',    ''), 
            'NodeSocketVirtual'     : ('Virtual',    ''),
            }
        
        bl_idname = socket.bl_socket_idname if isinstance(socket, bpy.types.NodeSocketInterfaceGeometry) else socket.bl_idname
        class_name = blids[bl_idname][0]
        name = socket.name
        
        if class_name == 'Geometry' and name in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve']:
            class_name = name
            
        if with_sub_class:
            return class_name, blids[bl_idname][1]
        else:
            return class_name
        
    @staticmethod
    def get_bl_idname(class_name):
        
        if class_name in ['Boolean']:
            return 'NodeSocketBool'
        
        
        elif class_name in ['Integer']:
            return 'NodeSocketInt'
        
        elif class_name in ['Unsigned']:
            return 'NodeSocketIntUnsigned'
        
        
        elif class_name in ['Float']:
            return 'NodeSocketFloat'
        
        elif class_name in ['Factor']:
            return 'NodeSocketFloatFactor'
        
        elif class_name in ['Angle']:
            return 'NodeSocketFloatAngle'
        
        elif class_name in ['Distance']:
            return 'NodeSocketFloatDistance'

        
        elif class_name in ['Vector']:
            return 'NodeSocketVector'
        
        elif class_name in ['Rotation']:
            return 'NodeSocketVectorEuler'
        
        elif class_name in ['xyz']:
            return 'NodeSocketVectorXYZ'
        
        elif class_name in ['Translation']:
            return 'NodeSocketVectorTranslation'

        
        elif class_name in ['Color']:
            return 'NodeSocketColor'
        
        elif class_name in ['String']:
            return 'NodeSocketString'
        
        elif class_name in ['Geometry', 'Mesh', 'Points', 'Instances', 'Volume', 'Curve', 'Spline']:
            return 'NodeSocketGeometry'
        
        elif class_name in ['Material']:
            return 'NodeSocketImage'
        
        elif class_name in ['Image']:
            return 'NodeSocketMaterial'
        
        elif class_name in ['Texture']:
            return 'NodeSocketTexture'
        
        elif class_name in ['Collection']:
            return 'NodeSocketCollection'
        
        elif class_name in ['Object']:
            return 'NodeSocketObject'

    
    # ----------------------------------------------------------------------------------------------------
    # The Blender socket is used to link nodes
    # Rather than accessing it directly, one must use the method get_blender_socket
    # This method can be used to implement specific code before connection
    
    def get_blender_socket(self):
        return self.bsocket
    
    # ----------------------------------------------------------------------------------------------------
    # The DataSocket can have properties
    # Reset the properties to None
    # It is called at initialization time to create the properties
    #
    # class Vector(...):
    #     def __init__(self, ...):
    #         ...
    #         self.reset_properties()
    #         ...
    #
    #     def reset_properties(self):
    #         super().reset_properties()
    #         self.separate_ = None      # Created by property self.seperate() with node NodeSeparateXyz
    
    def reset_properties(self):
        pass
    
    # ----------------------------------------------------------------------------------------------------
    # Stack behavior is used to change the Blender socket, allowing the syntax:
    #
    #     ...
    #     mesh = Mesh.UvShere()
    #     mesh.set_shade_smooth()
    #     ...
    #
    # rarher than:
    #
    #     ...
    #     mesh = Mesh.UvShere()
    #     mesh = mesh.set_shade_smooth()
    #     ...
    #
    # Only nodes with a single output socket can be stacked
    
    def stack(self, node):
        self.node    = node
        self.bsocket = node.output_sockets[0].bsocket
        self.reset_properties()
        return self

# =============================================================================================================================
# Nodes tree    

class Tree:
    """ Wrap a Blender NodeTree
    
    Initialization
    --------------
        At initialization time, the existing nodes can be deleted or kept. Use clear=True
        to erase the existing nodes.
        If the nodes are not erased, they are kept in the list 'old_bnodes'.
        
    Node creation
    -------------
        Each time a new node is required, use the method 'Tree.get_bnode'.
        This method check if a node exists in the old_nodes list.
        This allows nodes with user parameter such as 'Color Ramp' to be preserved
        between to runs.
        
    Current Tree
    ------------
        The current tree is store in the class property TREE of the class Tree.
    """
    
    TREE = None
    
    def __init__(self, tree_name, clear=False):
        """ Initialize a new tree
        
        Arguments
        ---------
            tree_name: str
                the name of the tree
            clear: bool, default is False
                earase the existing nodes
        """

        self.btree  = bpy.data.node_groups[tree_name]
        self.btree.links.clear()

        self.old_bnodes = []
        if clear:
            self.btree.nodes.clear()
        else:
            for bnode in self.btree.nodes:
                self.old_bnodes.append(bnode)
            
        self.nodes  = []
        self.node_id = 0
        self.activate()
        
        # ----- Input and outputs
        
        self.group_input  = NodeGroupInput()
        self.group_output = NodeGroupOutput()
        
    @property
    def input_geometry(self):
        return self.group_input.input_geometry
        
    @property
    def output_geometry(self):
        return self.group_output.output_geometry
    
    @output_geometry.setter
    def output_geometry(self, value):
        self.group_output.plug(0, value)
        
    # ----------------------------------------------------------------------------------------------------
    # Get / create a Blender node
        
    def get_bnode(self, bl_idname, label=None):
        """ Get or create a new Blender node in the tree.
        
        The former nodes are stored in old_bnodes. The list is scanned to find a node
        with the proper bl_idname. If label is not Node, the node label must match exactly
        the provided label.
        
        This allows to keep the user parameters defined in nodes such as Color Ramp.
        
        Arguments
        ---------
            bl_idname: str
                A valid node bl_idname
            label: str, optional
                The label of the node.
        
        Returns
        -------
            A blender node
        """
        
        found = None

        for bnode in self.old_bnodes:
            if bnode.bl_idname == bl_idname:
                if label is None:
                    found = bnode
                    break
                elif bnode.label == label:
                    found = bnode
                    break

        if found is None:
            bnode = self.btree.nodes.new(bl_idname)
        else:
            bnode = found
            self.old_bnodes.remove(bnode)
        
        if label is not None:
            bnode.label = label
            
        bnode.select = False
        
        return bnode
                        
        
    def activate(self):
        """ Set this tree as the current one.
        """
        
        Tree.TREE = self
        
    def register_node(self, node):
        """ Register the node passed in argument in the tree.
        
        When registered, a unique node id is provided to the node.
        This allows the users to more clearly distinguish the nodes.
        
        Arguments
        ---------
            node: Node
        """
        
        self.node_id += 1
        node.node_id = self.node_id
        self.nodes.append(node)
        return node
    
    # ---------------------------------------------------------------------------
    # Get the node wrapper of a blender node
    
    def get_bnode_wrapper(self, bnode):
        """ Get the Node instance wrapping the Blender node passed in argument.
        
        Arguments
        ---------
            bnode: Blender node
            
        Returns
        -------
            Node
            
        Raises
        ------
            Error if not found
        """
        
        for node in self.nodes:
            if node.bnode == bnode:
                return node
        raise RuntimeError(f"Impossible to find the wrapper node of Blender node {bnode}.")
            
    def get_bsocket_wrapper(self, bsocket):
        """ Get the DataSocket instance wrapping the Blender socket passed in argument.
        
        Arguments
        ---------
            bsocket: Blender socket
            
        Returns
        -------
            DataSocket
            
        Raises
        ------
            Error if not found
        """
        
        node = self.get_bnode_wrapper(bsocket.node)
        for socket in itertools.chain(node.inputs, node.outputs):
            if socket.bsocket == bsocket:
                return socket
        raise RuntimeError(f"Impossible to find the wrapper socket of Blender socket {bsocket}, of node {node}.")
            
        
    
# ---------------------------------------------------------------------------
# A Node    

class Node:
    def __init__(self, bl_idname, name, label=None):
        """ The root class for Blender node wrappers.
        
        This root class gives birth to children classes, one per valid bl_idname.
        
        Arguments
        ---------
            bl_idname: str
                A valid node bl_idname
            name: str
                The name to user for the node
            lavel: str, optional
                The node label
        """
        
        self.tree = Tree.TREE
        self.tree.register_node(self)

        self.name    = name
        self.label   = label
        self.bnode   = self.tree.get_bnode(bl_idname, label) #self.tree.bnodes.new(bl_idname)
        self.bnode.name = str(self)

        self.inputs  = [DataSocket(bsocket, node=self) for bsocket in self.bnode.inputs]
        self.outputs = [DataSocket(bsocket, node=self) for bsocket in self.bnode.outputs]
        
    @property
    def node_label(self):
        """ Node label
        
        If no label is provided the label is the concatenation of the id and the name.
        Otherwise, it is the label
        """
        return f"{self.node_id:2d} {self.name if self.label is None else self.label}"
        
    def __str__(self):
        return f"[{self.node_label}]"
    
    def __repr__(self):
        s = f"<Node {str(self)}:\n"
        s += "inputs:\n"
        for ds in self.inputs:
            s += f"   {ds.name} {ds.connected_sockets()}"
            if hasattr(ds.bsocket, "default_value"):
                s += f" ({ds.bsocket.default_value})"
            s += "\n"
        s += "outputs:\n"
        for ds in self.outputs:
            s += f"   {ds.name} {ds.connected_sockets()}\n"
        return s + ">"

    # ---------------------------------------------------------------------------
    # Sockets plugged to an input socket
    
    def plugged(self, index):
        return self.inputs[index].connected_sockets()
    
    # ---------------------------------------------------------------------------
    # Link an output socket with the input socket of another node
    
    def plug(self, index, *values):
        """ Plug the values to the input socket whose index is provided.
        
        Since an input socket can be multi input, the values argument is a list.
        
        If the socket is multi input, the plug method is called once per provide value.
        If a value is None, nothing happens.
        
        A not None value can be:
            - either a valid valud for the socket (eg: 123 for Integer socket)
            - or an output socket of another Node
            
        When it is a socket, it can be a Blender socker or a DataSocket
        
        Arguments
        ---------
            index: int
                The index of the input sockets (a valid index for Node.inputs)
            *values: list of values
                Each value can be an acceptable default value for the socket
                or an output socket 
        """
        
        # ---------------------------------------------------------------------------
        # Nothing to plug

        if len(values) == 0:
            return

        # ---------------------------------------------------------------------------
        # The blender input socket to plug into
        
        in_socket = self.bnode.inputs[index]
        
        # ---------------------------------------------------------------------------
        # If several output sockets to plugn let's loop on the list
        
        if len(values) > 1:
            if not in_socket.is_multi_input:
                raise RuntimeError(f"Input socket {str(in_socket)} is not multi input: impossible to plug multiple sockets: {values}.")
            for v in values:
                self.plug(index, v)
            return
        
        # ---------------------------------------------------------------------------
        # Ok now: only one thing to plug.
        # It can be a value or a socket (or directly a blender output socket)
        
        # ----- Let's suppress the existing links
        
        #if not in_socket.is_multi_input:
        #    links = [link for link in self.bnode.links]
        #    for link in links:
        #        self.node.tree.links.remove(links) 
        
        value = values[0]
        out_socket = None
        if isinstance(value, bpy.types.NodeSocket):
            out_socket = value
        elif hasattr(value, 'get_blender_socket'):
            out_socket = value.get_blender_socket()
            
        # ----- It is a value
        # Let's put it in the default_value of the input socket
            
        if out_socket is None:
            if in_socket.is_multi_input:
                raise RuntimeError(f"The socket {str(in_socket)} is multi input. Impossible to plug the value {value}.")
            
            if value is not None:
                ok = True
                try:
                    in_socket.default_value = value
                except Exception as e:
                    msg = str(e)
                    ok = False
                    
                if not ok:
                    raise RuntimeError(f"Impossible to set the default value {value} to socket {str(in_socket)}.\n {msg}")
                
        else:
            self.tree.btree.links.new(in_socket, out_socket, verify_limits=True)
            
        arrange(self.tree.btree.name)
            
    # ====================================================================================================
    # Node socket classes will be created in generated modules
    
    @staticmethod
    def Boolean(socket):
        import geonodes as gn
        return gn.Boolean(socket)
    
    @staticmethod
    def Integer(socket):
        import geonodes as gn
        return gn.Integer(socket)
    
    @staticmethod
    def Float(socket):
        import geonodes as gn
        return gn.Float(socket)
    
    @staticmethod
    def Vector(socket):
        import geonodes as gn
        return gn.Vector(socket)
    
    @staticmethod
    def Color(socket):
        import geonodes as gn
        return gn.Color(socket)
    
    @staticmethod
    def String(socket):
        import geonodes as gn
        return gn.String(socket)
    
    @staticmethod
    def Geometry(socket):
        import geonodes as gn
        return gn.Geometry(socket)
    
    @staticmethod
    def Spline(socket):
        import geonodes as gn
        return gn.Spline(socket)
    
    @staticmethod
    def Curve(socket):
        import geonodes as gn
        return gn.Curve(socket)
    
    @staticmethod
    def Mesh(socket):
        import geonodes as gn
        return gn.Mesh(socket)
    
    @staticmethod
    def Points(socket):
        import geonodes as gn
        return gn.Points(socket)
    
    @staticmethod
    def Instances(socket):
        import geonodes as gn
        return gn.Instances(socket)
    
    @staticmethod
    def Volume(socket):
        import geonodes as gn
        return gn.Volume(socket)
    
    @staticmethod
    def Texture(socket):
        import geonodes as gn
        return gn.Texture(socket)
    
    @staticmethod
    def Material(socket):
        import geonodes as gn
        return gn.Material(socket)
    
    @staticmethod
    def Image(socket):
        import geonodes as gn
        return gn.Image(socket)
    
    @staticmethod
    def Collection(socket):
        import geonodes as gn
        return gn.Collection(socket)
    
    @staticmethod
    def Object(socket):
        import geonodes as gn
        return gn.Object(socket)       
    
    @staticmethod
    def DataClass(socket):
        class_name = DataSocket.get_class_name(socket)
        return getattr(Node, class_name)(socket)
        
    
# =============================================================================================================================
# Node groups input and output

class NodeGroup(Node):
    
    # --------------------------------------------------------------------------------
    # Build the input names to avoid duplicates
    
    def update_sock_names(self, bsockets):
        
        if hasattr(self, 'sock_names'):
            for name in self.sock_names:
                delattr(self, name)
    
        self.sock_names = []
        for bsocket in bsockets:
            if bsocket.bl_idname != 'NodeSocketVirtual':
                self.sock_names.append(bsocket.name)
                
        def count_name(name):
            count = 0
            for bsocket in bsockets:
                if bsocket.name == name:
                    count += 1
            return count
                    
        def name_order(name, index):
            count = 0
            for i, bsocket in enumerate(bsockets):
                if bsocket.name == name:
                    if i == index:
                        return count
                    else:
                        count += 1
                        
        for index in range(len(self.sock_names)):
            name = self.sock_names[index]
            if count_name(name) > 1:
                self.sock_names[index] += str(name_order(name, index))
                
        for i, name in enumerate(self.sock_names):
            setattr(self, name, Node.DataClass(bsockets[i]))
    
    
# ----------------------------------------------------------------------------------------------------
# Node NodeGroupInput for NodeGroupInput

class NodeGroupInput(NodeGroup):

    def __init__(self):
        
        super().__init__('NodeGroupInput', 'Group Input')
        
        #self.tree    = tree
        #self.bnode   = tree.get_bnode('NodeGroupInput', 'Group Input')
        self.sockets = self.bnode.outputs
        
        
        self.update_sock_names(self.sockets)
        
        
    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def input_geometry(self):
        return Node.Geometry(self.bnode.outputs[0])
    
    # --------------------------------------------------------------------------------
    # Create a new output socket
    
    def new_socket(self, class_name, value=None, name=None):
        
        if name is None:
            name = class_name
            
        # ----- Look for an existing socket with the proper name
        
        for bsocket in self.bnode.outputs:
            cname, subclass = DataSocket.get_class_name(bsocket, True)
            if (cname == class_name or subclass == class_name) and bsocket.name == name:
                return Node.DataClass(bsocket)

        # ----- Let's create it
        
        self.tree.btree.inputs.new(type=DataSocket.get_bl_idname(class_name), name=name)
        
        self.update_sock_names(self.sockets)
        
        
        return getattr(self, self.sock_names[-1])
            
# ----------------------------------------------------------------------------------------------------
# Node NodeGroupOutput for NodeGroupOutput

class NodeGroupOutput(NodeGroup):
    
    def __init__(self):
        
        super().__init__('NodeGroupOutput', 'Group Output')
        
        self.sockets = self.bnode.inputs
        
        self.update_sock_names(self.sockets)
        
        
    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def output_geometry(self):
        return Node.Geometry(self.bnode.inputs[0])
    
    # --------------------------------------------------------------------------------
    # Create a new output socket
    
    def new_socket(self, class_name, value=None, name=None):
        
        if name is None:
            name = class_name
            
        # ----- Look for an existing socket with the proper name
        
        for bsocket in self.bnode.inputs:
            cname, subclass = DataSocket.get_class_name(bsocket, True)
            if (cname == class_name or subclass == class_name) and bsocket.name == name:
                return Node.DataClass(bsocket)

        # ----- Let's create it
        
        self.tree.btree.outputs.new(type=DataSocket.get_bl_idname(class_name), name=name)
        
        self.update_sock_names(self.sockets)
        
        
        return getattr(self, self.sock_names[-1])    
    
    
        