#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:45:39 2022

@author: alain
"""


from pprint import pprint

import bpy
      
from .color import Color

import logging
logger = logging.getLogger('geonodes')

# ====================================================================================================
# Tree
#
# A tree is a set of nodes belonging to the same group.
#
# The Tree class manages the current Tree into which newly created Nodes are stored

class Tree:

    TREES   = {}
    CURRENT = None

    # ----------------------------------------------------------------------------------------------------
    # Static methods to manage trees
    
    @staticmethod
    def current():
        if Tree.CURRENT is None:
            raise RuntimeError("No current Tree is defined. Ensure to create a Tree before using nodes.")
        return Tree.CURRENT
        
    @staticmethod
    def register(node):
        Tree.current().register_node(node)
        node.tree = Tree.CURRENT
        return node
    
    # ----------------------------------------------------------------------------------------------------
    # content
    
    def __repr__(self):
        s = "-"*30 + "\n"
        s += f"Tree '{self.name}'\n"

        s += f"Nodes ({len(self.nodes)}):\n"
        for i, node in enumerate(self.nodes):
            s += f"   {i:2d} {str(node)}\n"
        
        s += f"Links ({len(self.links)}):\n"
        for i, link in enumerate(self.links):
            s += f"   {i:2d} {str(link)}\n"

        return s + "\n"
    
        
    # ----------------------------------------------------------------------------------------------------
    # A tree instance
    
    def __init__(self, name):
        
        self.name      = name
        self.unique_id = 0
        self.nodes     = []
        self.links     = []
        
        Tree.TREES[name] = self
        self.set_current()
        
    # ----------------------------------------------------------------------------------------------------
    # Set current tree the this instance
            
    def set_current(self):
        Tree.CURRENT = self

    # ----------------------------------------------------------------------------------------------------
    # Register a node
    
    def register_node(self, node):
        self.unique_id += 1
        node.unique_id = self.unique_id
        self.nodes.append(node)
        
# =============================================================================================================================
# A link : from a socket out to a socket in

class Link:
    def __init__(self, socket_out, socket_in):
        logger.debug(f"Linking: {socket_out} ==> {socket_in}")

        self.socket_out = socket_out
        self.socket_in  = socket_in
        if not self.socket_out.is_output:
            raise RuntimeError(f"Link error: the socket {socket_out} is an input socket, not an output socket!")
        if self.socket_in.is_output:
            raise RuntimeError(f"Link error: the socket {socket_in} is an output socket, not an input socket!")
            
        
    @staticmethod
    def check(socket):
        # Socket can be an instance of future data class having a sockety attribute
        
        if hasattr(socket, 'socket'):
            return Link.check(socket.socket)
        
        if not (hasattr(socket, 'node') and hasattr(socket, 'index')):
            raise RuntimeError(f"The socket {socket} is not valid: it doesn't have 'node' and 'index' properties.")

        if socket is None:
            print("...", socket)
            print("...", type(socket))
            raise RuntimeError("Socket must not be None to build a link between two nodes.")

        if socket.node is None or socket.index is None:
            print("...", socket)
            print("...", type(socket))
            raise RuntimeError(f"Invalid socket: {socket}. 'node' and 'index' attribute must not be None.")
            
        return socket
    
    def __str__(self):
        return f"<Link: {str(self.socket_out)} --> {str(self.socket_in)}>"
    
    def __repr__(self):
        return str(self)
    
    @property
    def socket_out(self):
        return self.socket_out_
    
    @socket_out.setter
    def socket_out(self, value):
        self.socket_out_ = self.check(value)
        
    @property
    def socket_in(self):
        return self.socket_in_
    
    @socket_in.setter
    def socket_in(self, value):
        self.socket_in_ = self.check(value)
        
    @property
    def node_out(self):
        return self.socket_out.node
    
    @property
    def node_in(self):
        return self.soket_in.node
    
    @property
    def index_out(self):
        return self.socket_out.index
    
    @property
    def index_in(self):
        return self.socket_in.index
        
    def is_node_out(self, node):
        return self.node_out == node
    
    def is_node_in(self, node):
        return self.node_in == node
        

# =============================================================================================================================
# Sockets

# ----------------------------------------------------------------------------------------------------
# Socket

class Socket:
    def __init__(self, node, bl_idname, name, is_output=True):
        self.node      = node
        self.index     = None
        self.is_output = is_output

        self.bl_idname = bl_idname
        self.name      = name
        
        self.has_default_value = bl_idname not in ['NodeSocketGeometry']
        self.default_value     = None
        
    # ---------------------------------------------------------------------------
    # Comparizon
    # Not that this algorithm could make a socket out equal to a socekt in
    # Hope it will never happen, sich a comparizon would be an algorithem error
    
    #def __eq__(self, other):
    #    return self.node == other.node and self.index == other.index
    
    # ---------------------------------------------------------------------------
    # str
    
    def __str__(self):
        if self.is_output:
            return f"{str(self.node)}->{self.name}"
        else:
            return f"{self.name}->{str(self.node)}"
        
    # ---------------------------------------------------------------------------
    # The socket is a vector
    
    @property
    def is_vector(self):
        return self.bl_idname in ['NodeSocketVector', 'NodeSocketVectorEuler', 'NodeSocketVectorTranslation', 'NodeSocketVectorXYZ']
    
    # ---------------------------------------------------------------------------
    # All the links with this socket
    
    @property
    def links(self):
        links = []
        if self.is_output:
            for link in self.node.tree.links:
                if link.socket_out == self:
                    links.append(link)
        else:
            for link in self.node.tree.links:
                if link.socket_in == self:
                    links.append(link)
        return links
    
    # ---------------------------------------------------------------------------
    # Connected sockets
    
    @property
    def connected_sockets(self):
        if self.is_output:
            return [link.socket_in for link in self.links]
        else:
            return [link.socket_out for link in self.links]
    
    # ---------------------------------------------------------------------------
    # Connect to another socket
    
    def link_with(self, socket):
        if self.is_output:
            self.node.tree.links.append(Link(self, socket))
        else:
            self.node.tree.links.append(Link(socket, self))
            
    # ---------------------------------------------------------------------------
    # The blender socket
    
    @property
    def bsocket(self):
        if self.is_output:
            return self.node.bnode.outputs[self.index]
        else:
            return self.node.bnode.inputs[self.index]
            
        
# ----------------------------------------------------------------------------------------------------
# Socket in
       
class SocketIn(Socket):
    
    def __init__(self, node, bl_idname, name, is_multi_input=False):
        
        super().__init__(node=node, bl_idname=bl_idname, name=name, is_output=False)
        
        self.is_multi_input = is_multi_input
    
    def plug(self, sockets):
        
        if sockets is None:
            return

        if not isinstance(sockets, (tuple, list)):
            sockets = [sockets]
        
        # ---------------------------------------------------------------------------
        # Empty list: nothing to do
        
        if len(sockets) == 0:
            return
        
        # ---------------------------------------------------------------------------
        # Multi input
        
        if self.is_multi_input:
            
            for socket in sockets:
                self.link_with(socket)
                
        elif len(sockets) > 1:
            raise RuntimeError(f"Socket {self} is not multi inputs. Impossible to plug several sockets: {sockets}.")
            
        else:
            socket = sockets[0]
            
            # ----- socket can be a data class (such as Geometry)
            
            if hasattr(socket, 'connector'):
                socket = socket.connector
                
            # ----- socket can be a data class (such as Geometry)
                
            if isinstance(socket, Socket):
                links = self.links
                if links:
                    links[0].socket_out = socket
                else:
                    self.link_with(socket)
            else:
                self.default_value = socket
       
# ----------------------------------------------------------------------------------------------------
# A list of sockets

class Sockets(list):
   
    def add(self, socket):
        socket.index = len(self)
        self.append(socket)
        return socket
    
    @property
    def connected_sockets(self):
        sockets = []
        for socket in self:
            sockets.extend(socket.connected_sockets)
        return sockets

# =============================================================================================================================
# A Node

class Node:
    
    PARAMETERS = []
    
    def __init__(self, bl_idname, name):
        
        # ----- Set the node in the current tree
        # ----- Initialization

        self.bl_idname = bl_idname
        self.name      = name
        self.implement = True
        
        self.inputs  = Sockets()
        self.outputs = Sockets()
        
        self.socket_in_name  = None
        self.socket_out_name = None
        self.input_geometry_socket  = None
        self.output_geometry_socket = None

        self.stack_of    = None
        self.prop_of     = None
        
        # ----- Attribute management
        
        self.is_attribute = False
        
        # ----- Blender node control
        
        self.bnode_    = None
        self.label_    = None
        self.bcolor    = None
        self.layout    = None
        
        # ----- Register the node
        
        self.unique_id = -1
        Tree.register(self)
        
        logger.debug(f"Node creation: {str(self)}")
        
        
    def __str__(self):
        return f"[{self.label}]"
        #return f"[{type(self).__name__} '{self.label}']"

            
    @property
    def socket_in(self):
        if self.socket_in_name is None:
            return None
        else:
            return getattr(self, self.socket_in_name)
        
    @property
    def socket_out(self):
        if self.socket_out_name is None:
            return None
        else:
            return getattr(self, self.socket_out_name)
        
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
    
    # ====================================================================================================
    # A socket with all outputs
    
    def output_sockets(self):
        class Sockets:
            pass
        sockets = Sockets()
        for name in self.output_socket_names:
            setattr(sockets, name, geatattr(self, name))
        return sockets

    # ====================================================================================================
    # Check parameters
    
    def check_parameters(self):
        pass

    # ====================================================================================================
    # Has an input geometry socket
    
    @property
    def has_input_geometry_socket(self):
        return self.input_geometry_socket is not None
    
    @property
    def has_output_geometry_socket(self):
        return self.output_geometry_socket is not None
        
    # ====================================================================================================
    # Label
    
    @property
    def label(self):
        return f"{self.unique_id:2} {self.name}" if self.label_ is None else self.label_
    
    @label.setter
    def label(self, value):
        self.label_ = value
    
    # ====================================================================================================
    # Blender nodes creation
    
    @property
    def btree(self):
        return self.tree.btree
    
    @property
    def bnodes(self):
        return self.btree.nodes
    
    @property
    def blinks(self):
        return self.btree.links
    
    # ====================================================================================================
    # Switch two input sockets
    # Use with caution....
    
    def switch_input_sockets(self, index0, index1):
        socket0 = self.inputs[index0]
        socket1 = self.inputs[index1]
        links0  = socket0.links
        links1  = socket1.links
        
        for link in links0:
            link.socket_in = socket1
        for link in links1:
            link.socket_in = socket0
            
        v = socket0.default_value
        socket0.default_value = socket1.default_value
        socket1.default_value = v
    
    
    # ====================================================================================================
    # Before building, solve will do some stuff
    # Used by capture attribute node to decide the best implementation
    
    def solve(self):
        pass
        
    # ====================================================================================================
    # Update the display bnode
    
    @property
    def updated_bnode(self):
        if self.bcolor is None:
            self.bnode_.use_custom_color = False
        else:
            self.bnode_.use_custom_color = True
            self.bnode_.color = Color.Color(self.bcolor)
            
        return self.bnode_

    # ----------------------------------------------------------------------------------------------------
    # Specific bnode set up (input and output groups)
    
    def setup_bnode(self):
        pass
    
    # ----------------------------------------------------------------------------------------------------
    # Build the node
    
    @property
    def bnode(self):
        
        if not self.implement:
            return None
        
        # ----- Already exist
        
        if self.bnode_ is not None:
            return self.updated_bnode
        
        # ---------------------------------------------------------------------------
        # ----- Create the tree node
        
        bnode = self.bnodes.new(self.bl_idname)
        bnode.select = False
        self.bnode_ = bnode
        
        # ----- Color
        
        if self.bcolor is not None:
            self.bnode_.use_custom_color = True
            self.bnode_.color = Color.Color(self.bcolor)
        
        # ----- Label
        
        bnode.label = self.label
            
        # ----- For frame, set the text size
        
        if self.bl_idname == 'NodeFrame':
            bnode.label_size = 42
            
        # ----- Put in a frame
        
        if self.layout is not None:
            bnode.parent = self.layout.bnode
                
        # ---------------------------------------------------------------------------
        # ----- Set up
        
        self.setup_bnode()
                
        # ---------------------------------------------------------------------------
        # ----- Parameters
        
        for attr in self.PARAMETERS:
            v = getattr(self, attr)
            if v is not None:
                aname = attr[:-1] if attr[-1] == '_' else attr
                setattr(bnode, aname, v)
                
        # ---------------------------------------------------------------------------
        # ----- Sockets default values
        
        for i, sock in enumerate(self.outputs):
            if sock.has_default_value and sock.default_value is not None:
                try:
                    bnode.outputs[i].default_value = sock.default_value
                except:
                    pass
                
                if type(self).__name__ == 'NodeInputVector':
                    bnode.vector = sock.default_value

        # ---------------------------------------------------------------------------
        # ----- Input socket default values
        
        for i_sock, socket in enumerate(self.inputs):

            bsock_in = bnode.inputs[i_sock]
            
            if socket.has_default_value and socket.default_value is not None and hasattr(bsock_in, 'default_value'):
                
                # ----- Hack for Vector
                
                if type(socket.default_value) in [int, float] and socket.is_vector:
                    socket.default_value = (socket.default_value, socket.default_value, socket.default_value)
                    
                # ----- Set the default value
                
                try:
                    bsock_in.default_value = socket.default_value
                except:
                    logger.warning(f"blender link setting: error on socket {socket} when setting its default value '{socket.default_value}' to Blender socket '{bsock_in.name}'.")
                    #print(f"CAUTION: error when setting default value {socket.default_value} to socket {bsock_in} of node {self}.")
                    
                    
        # ----- Done
        
        bnode.update()
                
        return bnode
    
# =============================================================================================================================
# Attribute is a complementary interface for attribute nodes
# at implementation, they can decide to insert a NodeCaptureAttribute in the flow of geometry
#
# The Attribute interface relies on:
# - owner_socket : The socket it an attribute of
# - data_type    : used to create the attrbut ecapture node
# - domain       : used to create the attrbut ecapture node

class Attribute(Node):
    
    def __init__(self, bl_idname, name, owner_socket, data_type, domain):
        
        super().__init__(bl_idname, name)
        
        self.is_attribute = True
        self.owner_socket = owner_socket
        self.data_type    = data_type
        self.domain       = domain
    
    # ---------------------------------------------------------------------------
    # Solves the attribute for the outputs sockets of this Node
    
    def solve(self):
        
        # ---------------------------------------------------------------------------
        # A node attaribute can have several socket out. Each of them is solved
        # independantly
        
        for socket_out in self.outputs:
            
            # ---------------------------------------------------------------------------
            # Find all the nodes fed by the attribute and having a geometry input socket
            # fed_nodes will contain the first nodes with a geometry input which are
            # reached the the links starting from the current socket_out
            
            def build_fed_nodes(from_node = None, fed_nodes=None):
                
                # ----- Initialize the result list
                
                if from_node is None:
                    from_node = self
                    fed_nodes = []
                    outputs   = [socket_out]
                else:
                    outputs   = from_node.outputs

                # ----- Loop on the links
                    
                for socket in outputs:
                    for sock in socket.connected_sockets:
                        if sock.node.has_input_geometry_socket:
                            if not sock.node in fed_nodes:
                                fed_nodes.append(sock.node)
                        else:
                            build_fed_nodes(sock.node, fed_nodes)
                
                return fed_nodes
            
            # ---------------------------------------------------------------------------
            # For all the fed nodes, see if one of them is indirecly connected to the
            # owner node. If at least one exists, the Capture Node will be created
            
            def find_owner(node, steps=0):
                
                if not node.has_input_geometry_socket:
                    return None, steps, f"The node {str(node)} has no input geometry socket. Impossible to find the node {str(self.owner_socket.node)}."
                
                for link in node.input_geometry_socket.links:
                    if link.socket_out == self.owner_socket:
                        return link, steps, None
                    else:
                        return find_owner(link.node_out, steps=steps + 1)
                            
                return None, steps, f"The input socket '{node.input_geometry_socket.name}' of node {str(node)} is not connected to an input geometry."
            
            # ---------------------------------------------------------------------------
            # Search for fed nodes
            
            fed_nodes = build_fed_nodes()
            if not fed_nodes:
                return
            
            # ---------------------------------------------------------------------------
            # For each fed node, check that the owner feeds the input geometry
            
            as_capture = False
            for node in fed_nodes:
                
                serror = f"NODE ATTRIBUTE ERROR: the node {node} has a socket connected to attribute {self}, but the geometry node {self.owner_socket.node} can't be found in the input chain of geometry.\n"
                
                ins_link, steps, msg = find_owner(node)
                
                if ins_link is None:
                    self.tree.dirty_build(f"{serror}\n{msg}")
                    raise RuntimeError(f"{serror}\n{msg}")
                    
                if steps > 0:
                    as_capture = True
                    break
                    
            # ---------------------------------------------------------------------------
            # Implement as a capture attribute node
            #
            # The node is insert in the link coming from the find owner loop
            #
            # - At creation, its input geometry takes link.socket_out
            # - Then, the link.socket_in takes the node geometry as input
            #
            # The current sockout is replaced by capture.attribute
            
            if as_capture:
                
                # ---------------------------------------------------------------------------
                # Create the capture node with owner as geometry input
                
                capture = self.tree.create_capture_node(geometry=ins_link.socket_out, value=None, data_type=self.data_type, domain=self.domain)

                capture.layout = ins_link.node_out.layout
                self.layout    = ins_link.node_out.layout
                
                
                #capture.layout  = self.layout
                capture.label   = self.label
                capture.bcolor  = self.bcolor
                
                # ---------------------------------------------------------------------------
                # The output geometry of the capture node must be plugged to the node
                # the current socket is plugged to
                
                ins_link.socket_out = capture.geometry

                # ---------------------------------------------------------------------------
                # All the link coming out of this node must now be link to the newly
                # created capture node
                
                links = socket_out.links
                for link in links:
                    link.socket_out = capture.attribute
                    
                # ---------------------------------------------------------------------------
                # Then, the input socket value is plugged with the current_socket out
                # This is done at the end to avoid auto plug in the previous loop
                
                capture.ivalue = socket_out
                
                
                
                    
                
                


    
    
    
    
            
        
