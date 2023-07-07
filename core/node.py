#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:15:16 2022

@author: alain
"""

import sys
import itertools
from contextlib import contextmanager
import re

from pprint import pprint
import logging
logger = logging.getLogger('geonodes')

from geonodes.core import colors
from geonodes.core import context
from geonodes.core.socket import DataSocket

from typing import Any

try:
    import bpy
    import mathutils
except:
    pass


COLORS = {
    'Viewer': 'Dark green',
    }

# ====================================================================================================
# A tree node

class Node:
    """ The root class for Blender node wrappers.
    
    :param bl_idname: The node bl_idname
    :param name: The node name
    :param label: The node label
    :param node_color: The node color
    :type bl_idname: str
    :type name: str
    :type label: str
    :type node_color: triplet, str or mathutils.Color
    
    
    This class is basically intended to expose its constructor as a way to create
    the associated Geometry Node. In the following example, we create a Node
    supposingly have one single input socket named "geometry"
    
        
    .. code-block:: python
        
        my_node = Node(geometry=value, parameter='PARAM')
        
    **Nodes naming convention**    
    
    The Node sub classes are named according their Blender label with a **CamelCase** conversion,
    for instance:
        
    -  *Set Shade Smooth* --> ``SetShadeSmooth``
    -  *Split Edges* --> ``SplitEdges``
    -  *Normal* --> ``Normal``
    
    **Sockets naming convention**
    
    The node sockets are named after the Blender sockets names with a **snake_case** conversion,
    for instance:
        
    -  *Geometry* --> ``geometry``
    -  *Mesh 1* --> ``mesh_1``
    -  *Curve instances* --> ``curve_instances``
    
    For some nodes, (Math node for instance), several sockets can share the same name. In that case, the
    sockets are numbered, starting from 0:
        
    -  *Value* --> ``value0``
    -  *Value* --> ``value1``
    
    """
        
    def __init__(self, bl_idname, node_name, label=None, node_color=None):
        
        self.tree = context.tree
        """ The tree belonging the node."""
        
        self.tree.register_node(self)

        self.node_name = node_name
        """ Node name"""
        self.label_  = None
        if bl_idname == 'GeometryNodeGroup':
            self.bnode = self.tree.get_bnode(bl_idname, node_name)
        else:
            self.bnode = self.tree.get_bnode(bl_idname, label)
            
        self.bnode.name = str(self)
        self.label      = label
        """ Node label"""
        self.node_color = node_color

        self.inputs  = [DataSocket(bsocket, node=self) for bsocket in self.bnode.inputs]
        """ Input sockets list"""
        self.outputs = [DataSocket(bsocket, node=self) for bsocket in self.bnode.outputs]
        """ Output sockets list"""
        
        # ----- Field management
        
        #self.is_attribute = False
        #""" Initialized by method :func:`as_attribute`. Will be analyzed by :func:`check_attributes` to complete the Tree."""
        
        self.attr_bsocket = None
        """ The geometry socket to capture from """
        
        self.attr_domain = None
        """ The domain it is an attribute of """
        
        self.field_of_ = None
        """ A pointer to the owning domain. Used to implement transfer attribute."""
        
        # ----- Socket names
        # Sockets have a unique name
        # A name can cover several sockets for shared names
        # These dicts must be intialized by sub classes
        # They are used by __setattr__ and __getattr__

        self.insockets  = {}
        """ set: keys = unique names of input sockets, values: actual socket indices"""
        self.outsockets = {}
        """ set: keys = unique names of output sockets, values: actual socket indices"""
        
        # ----- We can force the class of output sockets (used for geometry)
        
        self.outsockets_classes = {}
        
        
    # ------------------------------------------------------------------------------------------
    # Node class signature
    
    @staticmethod
    def is_node():
        pass
    
    # ------------------------------------------------------------------------------------------
    # insockets and outsockets are initialized by generated code
    # Some nodes sucha as simulation input and output nodes can have sockets dynamically created
    # This method updates insockets and outsockets from sockets
    
    def update_inout_sockets(self):
        
        def snake(s):
            return s.lower().replace(' ', '_').replace('-', '_')

        self.inputs     = [DataSocket(bsocket, node=self) for bsocket in self.bnode.inputs if bsocket.bl_idname != 'NodeSocketVirtual']
        self.outputs    = [DataSocket(bsocket, node=self) for bsocket in self.bnode.outputs if bsocket.bl_idname != 'NodeSocketVirtual']

        self.insockets  = {snake(socket.name): index for index, socket in enumerate(self.inputs)}
        self.outsockets = {snake(socket.name): index for index, socket in enumerate(self.outputs)}

        
        #self.insockets  = {snake(bsocket.name): index for index, bsocket in enumerate(self.bnode.inputs) if bsocket.bl_idname != 'NodeSocketVirtual'}
        #self.outsockets = {snake(bsocket.name): index for index, bsocket in enumerate(self.bnode.outputs) if bsocket.bl_idname != 'NodeSocketVirtual'}
    
        
    # ------------------------------------------------------------------------------------------
    # Output socket by name
    
    def get_output_socket(self, name, class_name=None):

        #sock_ind = self.outsockets.get(name.lower())
        sock_ind = self.outsockets.get(name)
        if sock_ind is None:
            raise AttributeError(f"Node '{self}' has no output socket named '{name}'")
            
        ds = None
        if isinstance(sock_ind, int):
            ds = self.DataClass(self.bnode.outputs[sock_ind])
        else:
            for index in sock_ind:
                if self.bnode.outputs[index].enabled:
                    ds = self.DataClass(self.bnode.outputs[index])
                    break
                    
        if ds is None:
            raise AttributeError(f"Output socket error on node {self}: all socket named '{name}' are disabled")
            
        if class_name is None:
            class_name = self.outsockets_classes.get(name, None)
            
        if class_name is not None:
            if isinstance(class_name, str):
                ds = getattr(Node, class_name)(ds.bsocket)
            else:
                ds = class_name(ds.bsocket)
                        
        ds.attr_domain = self.attr_domain
        return ds

    # ------------------------------------------------------------------------------------------
    # Set an input socket
    # We are idiot proof and accept capitalized versions :-)
    # Input sockets are "write only"
        
    def set_input_socket(self, name, value):
        
        sock_ind = self.insockets.get(name)
        if sock_ind is None:
            raise AttributeError(f"Node '{self}' has no input socket named '{name}'")
            
        if isinstance(sock_ind, int):
            self.plug(sock_ind, value)
            return
        
        else:
            for index in sock_ind:
                if self.bnode.inputs[index].enabled:
                    self.plug(index, value)
                    return
                
            raise RuntimeError(f"Input socket error on node {self}: all socket named '{name}' are disabled")
        
        
    # ---------------------------------------------------------------------------
    # Output socket by index
    
    def get_datasocket(self, index):
        """ Get the data socket by its index.
        
        :param index: Index of the output socket to get
        :type index: int
        :return: The data socket at the given socket
        :rtype: DataSocket
        
        .. Note:: The index is the **user index**. It can differ from the **geometry node index** of the socket when
            several sockets share the same name. For instance the node *Random value* has several output sockets
            named *Value*. Only one is enabled at the same time. All these sockets share the same index, which is 0.
            The socket returned by ``get_datasocket`` is the one which is enabled.
            
        .. code-block:: python
        
            import geonodes as gn
            
            with gn.Tree("Geometry Nodes") as tree:
                
                # Node 'Random Value' initialized for FLOAT
                
                v = gn.Float.Random()
                
                # Let's explore the node
                 
                random_node = v.node
                
                # The actual output sockets of the geometry node
                # Note that we loop on bnode which is the wrapped node
                
                print("Actual sockets:")
                for i, bsocket in enumerate(random_node.bnode.outputs):
                    print(i, bsocket.name, bsocket.enabled)
                print()
            
                # All the socket share the same name and user index
                # The one whih is return is the enabled one
                    
                print("User sockets:")
                for key in random_node.outsockets:
                    socket = getattr(v.node, key)
                    print(key, socket.socket_index, socket.bl_idname)
                    
        .. code-block:: console
                    
            Actual sockets:
            0 Value False
            1 Value True
            2 Value False
            3 Value False
            
            User sockets:
            value 1 NodeSocketFloat                    
        
        """
        name = list(self.outsockets.keys())[index]
        return getattr(self, name)
        
    # ---------------------------------------------------------------------------
    # Let's make thing readable
    
    def __str__(self):
        return f"[{self.get_label()}]"
    
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
    # bl idname
    
    @property
    def bl_idname(self):
        """ Shortcut for ``self.bnode.bl_idname``
        """
        return self.bnode.bl_idname
    
    # ------------------------------------------------------------------------------------------
    # Class method to unitize a list of names
        
    @staticmethod
    def unitize(names):
        """ Utility to build unique names from a list with homonyms
        
        :param names: The list of names to unitize
        :type names: list of strs
        :return: list with the same number of names where homonyms are suffixed by their rank
        :rtype: list of strs
        """
        
        counts = {name: 0 for name in set(names)}
        unames = []
        for i, name in enumerate(names):
            if names.count(name) > 1:
                unames.append(f"{name}{counts[name]}")
                counts[name] += 1
            else:
                unames.append(name)
                
        return unames
    
    # ---------------------------------------------------------------------------
    # Node label
    
    def get_label(self):
        """ Build the node label
        
        If the label provided at initialization time is None, the node is labeled by concatening
        its unique id with its standard name.
        """
        return f"{self.node_id:2d} {self.node_name}" if self.label_ is None else f"{self.node_id:2d} {self.label_}"
    
    @property
    def label(self):
        """ Node label"""
        return self.label_
    
    @label.setter
    def label(self, value):
        self.label_ = value
        self.bnode.label = self.get_label()
        
    # ---------------------------------------------------------------------------
    # Chain label used when labeling chained nodes
    # eg: separate property of Vector is labeled: {chain_label}.separate
        
    @property
    def chain_label(self):
        """ Label to use when building chain labels"""
        if self.label is None:
            return str(self.node_id)
        else:
            return self.label
        
    # ---------------------------------------------------------------------------
    # The input geometry socket when exists
    
    @property
    def input_geometry_bsocket(self):
        """ The input geometry blender socket"""
        for bsocket in self.bnode.inputs:
            if bsocket.bl_idname == 'NodeSocketGeometry':
                return bsocket
        return None

    # ---------------------------------------------------------------------------
    # All the fed nodes (nodes connected to one output socket)
    
    @property
    def fed_nodes(self):
        """ List of the node with input sockets connected with this socket"""

        bnodes = []
        for bsocket in self.outputs:
            for link in bsocket.links:
                if link.to_node not in bnodes:
                    bnodes.append(link.to_node)

        nodes = []
        for bnode in bnodes:
            for node in self.tree.nodes:
                if node.bnode == bnode:
                    nodes.append(node)

        return nodes
    
    # ---------------------------------------------------------------------------
    # Node color
    
    @property
    def node_color(self):
        """ Noe color"""
        return self.bnode.color
    
    @node_color.setter
    def node_color(self, value):
        if value is None:
            self.bnode.use_custom_color = False
        else:
            self.bnode.use_custom_color = True
            self.bnode.color = colors.color(value)
            
    # ---------------------------------------------------------------------------
    # Check that an attribute is in the authorized list
    
    def check_enum_value(self, value, attr_name, attr_list, attr_default=None):
        if value in attr_list:
            return value
        
        msg = f"The attribute '{attr_name}' of node '{self.bnode.name}' accepts values in {attr_list}."
        
        if attr_default is None:
            raise AttributeError(f"Bad value '{value}'.\n{msg}")
        
        print(f"WARNING: {msg} Value '{value}' changed to default '{attr_default}'.")
        return attr_default
            

    # ---------------------------------------------------------------------------
    # Switch input sockets
    
    def switch_input_sockets(self, index0, index1):
        """ Utility method which switchs the links of two sockets.
        
        :param index0: The first index
        :param index1: The second index
        :type index0: int
        :typ index1: int
        
        Used when implementing operators __rxxx___
        """
        
        bsock0 = self.bnode.inputs[index0]
        bsock1 = self.bnode.inputs[index1]
        
        links0 = [link for link in bsock0.links]
        links1 = [link for link in bsock1.links]
        
        def0     = bsock0.default_value if hasattr(bsock0, 'default_value') else None
        def1     = bsock1.default_value if hasattr(bsock1, 'default_value') else None
        
        inps0 = [link.from_socket for link in links0]
        inps1 = [link.from_socket for link in links1]
        
        for link in itertools.chain(links0, links1):
            self.tree.btree.links.remove(link)
            
        if hasattr(bsock0, 'default_value') and def1 is not None:
            bsock0.default_value = def1
            
        if hasattr(bsock1, 'default_value') and def0 is not None:
            bsock1.default_value = def0
            
        for inp in inps1:
            self.tree.btree.links.new(inp, bsock0)
        for inp in inps0:
            self.tree.btree.links.new(inp, bsock1)
        

    # ---------------------------------------------------------------------------
    # Sockets plugged to an input socket
    
    def plugged(self, index):
        """ The liste of plugged sockets
        
        :param index: the index of the socket to consider
        :type index: int
        :return: The list of connected sockets
        :rtype: list of DataSockets
        """
        
        return self.inputs[index].connected_sockets()
    
    # ---------------------------------------------------------------------------
    # Link an output socket with the input socket of another node
    
    def plug(self, index, *values):
        """ Plug the values to the input socket whose index is provided.
        
        :param index: The index of the input sockets (a valid index for Node.inputs)
        :param values: Each value can be an acceptable default value for the socket
                 or an output socket 
        :type index: int
        :type values: list of values
        
        Since an input socket can be multi input, the values argument is a list.
        
        If the socket is multi input, the plug method is called once per provide value.
        If a value is None, nothing happens.
        
        A not None value can be:
            
        - either a valid valud for the socket (eg: 123 for Integer socket)
        - or an output socket of another Node
            
        When it is a socket, it can be a Blender socket or a DataSocket
        """
        
        # ----- Index can be a string
        
        valids = []
        if type(index) is str:
            for i, bsock in enumerate(self.bnode.inputs):
                
                if bsock.enabled:
                    valids.append((bsock.name, i))
                    if bsock.name.lower() == index.lower():
                        index = i
                        break

        if type(index) is str:
            raise RuntimeError(f"Invalid input socket name '{index}' for node {self}. Valid (names, index) are : {valids}.")
        
        context.plug_to_socket(self.bnode.inputs[index], *values)
        
    # ------------------------------------------------------------------------------------------
    # Plug all sockets with matching name
    
    def plug_node(self, node):
        """ Plug all the sockets of a node.
        
        :param node: The node whose output sockets will be plugged
        :type node: Node
        
        Plug the output sockets of node whose name match an input socket of self.
        
        """
        
        for index, iname in enumerate(self.insockets):
            if iname in node.outsockets:
                self.plug(index, getattr(node, iname))
        
    # ====================================================================================================
    # The node is an attribute
    
    @property
    def is_attribute(self):
        return self.attr_bsocket is not None
    
    @property
    def attr_domain_name(self):
        if self.attr_domain is None:
            return 'POINT'
        elif isinstance(self.attr_domain, str):
            return self.attr_domain
        else:
            return self.attr_domain.domain
    
    def as_attribute(self, geometry, domain='POINT'):
        """ Indicates that the node is an attribute.
        
        :param owning_socket: The owning socket it is an atribute of
        :param domain: The domain if 'Capture Attribute' is necessary
        :type owning_socket: DataSocket
        :type domain: str
        
        Set the property :attr:`is_atribute` to `True` to indicate that the socket
        is the attribute of a Geometry.
        The domain is stored in the property `domain`
        
        see :func:`Tree.check_attributes` 
        """
        
        if isinstance(geometry, bpy.types.NodeSocket):
            self.attr_bsocket = geometry
        else:
            self.attr_bsocket = geometry.bsocket
        self.attr_domain = domain
        
        return self
        
    # ----------------------------------------------------------------------------------------------------
    # List of the nodes which are connected through a GEOMETRY socket
    
    def connected_geometries(self):
        """ List of the connected geometries
        
        Explore the fowards links until finding a node with an input geometry.
        The resulting list will allow to determine if a 'Capture Attribute' is necessary.
        """
        
        def conns(node):
            
            def app(nds, nd):
                if nd not in nds:
                    nds.append(nd)
                    
            geo_nodes = []
            oth_nodes = []
            for socket in node.outputs:
                for link in socket.links:
                    nd = link.to_node
                    if link.to_socket.bl_idname == 'NodeSocketGeometry':
                        app(geo_nodes, nd)
                    else:
                        app(oth_nodes, nd)
                        
            for nd in oth_nodes:
                for n in conns(nd):
                    app(geo_nodes, n)
                    
            return geo_nodes
        
        return conns(self)
        
    # ----------------------------------------------------------------------------------------------------
    # The attribute is "solved" when it feeds capture or transfer attribute
    
    def attribute_is_solved(self):
        """ Check if the attribute is already solved.
        
        No need to insert a  *Capture Attribute* Node when the socket is already
        connected to nodes  *Capture Attribute* or  *Transfer Attribute*.
        
        see :func:`Tree.check_attributes` 
        """

        solvers = ['GeometryNodeCaptureAttribute', 'GeometryNodeAttributeTransfer']
        geos = self.connected_geometries()
        for node in geos:
            if node.bl_idname not in solvers:
                return False
            
        return True

    # ====================================================================================================
    # Node socket classes will be created in generated modules

    @staticmethod
    def Boolean(socket):
        """ Initialize a Boolean with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Boolean(socket)
    
    @staticmethod
    def Integer(socket):
        """ Initialize a Integer with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Integer(socket)
    
    @staticmethod
    def Float(socket):
        """ Initialize a Float with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Float(socket)
    
    @staticmethod
    def Vector(socket):
        """ Initialize a Vector with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Vector(socket)
    
    @staticmethod
    def Color(socket):
        """ Initialize a Color with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Color(socket)
    
    @staticmethod
    def String(socket):
        """ Initialize a String with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.String(socket)
    
    @staticmethod
    def Geometry(socket):
        """ Initialize a Geometry with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Geometry(socket)
    
    @staticmethod
    def Curve(socket):
        """ Initialize a Curve with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Curve(socket)
    
    @staticmethod
    def Mesh(socket):
        """ Initialize a Mesh with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Mesh(socket)
    
    @staticmethod
    def Points(socket):
        """ Initialize a Points with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Points(socket)
    
    @staticmethod
    def Instances(socket):
        """ Initialize a Instances with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Instances(socket)
    
    @staticmethod
    def Volume(socket):
        """ Initialize a Volume with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Volume(socket)
    
    @staticmethod
    def Curve(socket):
        """ Initialize a Curves with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Curve(socket)
    
    @staticmethod
    def Texture(socket):
        """ Initialize a Texture with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Texture(socket)
    
    @staticmethod
    def Material(socket):
        """ Initialize a Material with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Material(socket)
    
    @staticmethod
    def Image(socket):
        """ Initialize a Image with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Image(socket)
    
    @staticmethod
    def Collection(socket):
        """ Initialize a Collection with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Collection(socket)
    
    @staticmethod
    def Object(socket):
        """ Initialize a Object with a DataSocket"""
        from geonodes.nodes import classes as gn
        return gn.Object(socket)       
    
    @staticmethod
    def DataClass(socket):
        """ Initialize a DataClass of the property class from from the bl_idname of the socket"""
        class_name = DataSocket.get_class_name(socket)
        return getattr(Node, class_name)(socket)
        
    
# =============================================================================================================================
# Node groups
#
# A Groups can be:
# - A user group with inuts and outputs
# - An input group with only outputs
# - An output group with only inputs
#
# Since the inputs are outputs these three classes need initializers for the socket names

# ----------------------------------------------------------------------------------------------------
# Root for node groups

class CustomGroup(Node):
    """ > Root for the three types of groups
    
    Build the insockets and outsockets dictionaries
    """
    
    def __init__(self, bl_idname, node_name, label=None, node_color=None):
        
        super().__init__(bl_idname, node_name, label=label, node_color=node_color)
        
        self.build_insockets()
        self.build_outsockets()
        
    @staticmethod
    def build_unames_dict(bsockets):
        
        # snake_case version of the sockets names
        sc_names = []
        for bsocket in bsockets:
            if bsocket.name != "":
                sc_names.append(CustomGroup.snake_case(bsocket.name))
        
        # Unique version (homonyms are suffxed)
        return {uname: i for i, uname in enumerate(Node.unitize(sc_names))}
        
    def build_insockets(self):
        self.inputs  = [DataSocket(bsocket, node=self) for bsocket in self.bnode.inputs]
        self.insockets = self.build_unames_dict(self.bnode.inputs)
        
    def build_outsockets(self):
        self.outputs = [DataSocket(bsocket, node=self) for bsocket in self.bnode.outputs]
        self.outsockets = self.build_unames_dict(self.bnode.outputs)
        
    @staticmethod
    def snake_case(name):
        return name.lower().replace(' ', '_')
        
    @staticmethod
    def unique_socket_name(name, dct, prefix=None):
        if name not in dct:
            return name
        
        for i in range(1, 100):
            uname = f"{name} {i}"
            if uname not in dct:
                return uname
            
        return name

        
    # ------------------------------------------------------------------------------------------
    # Access dynamically to the output sockets
    # We are idiot proof and accept capitalized versions :-)
    # Output sockets are "write only"
        
    def __getattr__(self, name):
        ds = None
        if name != 'outsockets':
            if hasattr(self, 'outsockets'):
                if name.lower() in self.outsockets:
                    sock_ind = self.outsockets[name.lower()]
                    if isinstance(sock_ind, int):
                        ds = self.DataClass(self.bnode.outputs[sock_ind])
                    else:
                        for index in sock_ind:
                            if self.bnode.outputs[index].enabled:
                                ds = self.DataClass(self.bnode.outputs[index])
                                break
                            
                        if ds is None:
                            raise AttributeError(f"Output socket error on node {self}: all socket named '{name}' are disabled")
                        
        if ds is None:
            raise AttributeError(f"'{type(self).__name__}' object has not attribute '{name}'")
        else:
            ds.attr_domain = self.attr_domain
            return ds

    # ------------------------------------------------------------------------------------------
    # Access dynamically to the input sockets
    # We are idiot proof and accept capitalized versions :-)
    # Input sockets are "write only"
        
    def __setattr__(self, name, value):
        if hasattr(self, 'insockets'):
            if name.lower() in self.insockets:
                sock_ind = self.insockets[name.lower()]
                if isinstance(sock_ind, int):
                    self.plug(sock_ind, value)
                    return
                else:
                    for index in sock_ind:
                        if self.bnode.inputs[index].enabled:
                            self.plug(index, value)
                            return
                    raise RuntimeError(f"Input socket error on node {self}: all socket named '{name}' are disabled")
            
        super().__setattr__(name, value)        
    

# ----------------------------------------------------------------------------------------------------
# A node group

class Group(CustomGroup):
    """ > Node group
    
    Node groups are dynamically built by reading the input and output sockets of the group.
    
    Input sockets are initialized in the keyword arguments.
    
    They can later on be initialized by the snake_case names
    """
    
    def __init__(self, node_name, **kwargs):
        
        if bpy.data.node_groups.get(node_name) is None:
            raise RuntimeError(f"The node group '{node_name}' doesn't exist")
        
        label, node_color = kwargs.get('label'), kwargs.get('node_color')
        if label is not None:
            a.pop('label')
        if node_color is not None:
            a.pop('node_color')
        
        super().__init__('GeometryNodeGroup', node_name, label=label, node_color=node_color)

        # But let's plug the values directly 
        
        for k, v in kwargs.items():
            index = self.insockets.get(k.lower())
            if index is None:
                raise AttributeError(f"The node group '{node_name}' has no input socket named '{k}'.")
            self.plug(index, v)
            
            
    def __call__(self, **kwargs):
        for k, v in kwargs.items():
            index = self.insockets.get(k.lower())
            if index is None:
                raise AttributeError(f"The node group '{node_name}' has no input socket named '{k}'.")
            self.plug(index, v)
        return self

    
# ----------------------------------------------------------------------------------------------------
# NodeGroupInput

class GroupInput(CustomGroup):
    
    """ Node *Group input*
    
    Args:
        check_input_geometry: True for modifier
        
    
    Note that the **output** sockets of this node are the **input** sockets of the group.
    
    For modifiers, the first socket must be a geometry socket: this is the gemetry of the object on which the modifier
    applies. Make sure that this socket exists.
    
    This node is created by the Tree at initialization time. 
    
    """

    def __init__(self, check_input_geometry: bool):
        
        super().__init__('NodeGroupInput', 'Group Input')
        
        self.bsockets = self.bnode.outputs
        
        if check_input_geometry:
            ok = False
            ok_virtual = False
            for index, bsocket in enumerate(self.bnode.outputs):
                if bsocket.bl_idname == 'NodeSocketVirtual':
                    ok_virtual = True
                    break

                elif bsocket.bl_idname == 'NodeSocketGeometry':
                    ok = index == 0
                    break
                
            if not ok:
                if ok_virtual and len(self.tree.btree.inputs) > 0:
                    while len(self.tree.btree.inputs) > 0 and self.tree.btree.inputs[0].bl_socket_idname != 'NodeSocketVirtual':
                        self.tree.btree.inputs.remove(self.tree.btree.inputs[0])
                
                self.tree.btree.inputs.new(type='NodeSocketGeometry', name="Geometry")
                self.build_insockets()
                
    # --------------------------------------------------------------------------------
    # Input socket by their name
    
    def __getitem__(self, name):
        return getattr(self, CustomGroup.snake_case(name))
        
    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def input_geometry(self) -> Node:
        """ The default input geometry sockets.
        
        Returns:
            Geometry: The input geometry socket
        """
            
        
        try:
            sock0 = self.bnode.outputs[0]
            if sock0.bl_idname in ['NodeSocketGeometry', 'NodeSocketVirtual']:
                return Node.Geometry(sock0)
            else:
                geo = self.new_socket('Geometry')
                for index, bsock in enumerate(self.bnode.outputs):
                    if bsock.geometry == "Geometry":
                        self.bnode.outputs.move(index, 0)
                        logger.error("GEONODES> Blender error: the method 'outputs.move' doesn't work. You must move yourself the input geometry in first position...")
                
                return Node.Geometry(geo)

        except AttributeError as e:
            raise RuntimeError("GroupInput.input_geometry error: " + str(e), sys.exc_info()[2])
    
    # --------------------------------------------------------------------------------
    # Create a new input socket
    
    def new_socket(self, class_name: str, value: Any = None, name: str = None, 
                   min_value: Any = None, max_value: Any = None, description: str = "") -> DataSocket:
        """ Create a new input ocket.
        
        Args:
            class_name : the type of socket to create
            value : Default value (when relevant)
            name : Socket name
            min_value : Minimum value
            max_value : Maxium value
            description : user tip
            
        Returns:
            DataSocket : A data socket of class *class_name*
            
        Note
        ----
            The created socket is an **input** socket for the whole tree, i.e. an **output** socket for this node.

        """
        # ----- Default name if None
        
        if name is None:
            name = class_name
            
        # ----------------------------------------------------------------------------------------------------
        # Does the socket already exist ?
        
        search_blid  = DataSocket.get_bl_idname(class_name)
        socket_input = None
        socket       = None
        set_value    = True
        
        for index, inp in enumerate(self.tree.btree.inputs):
            if inp.name == name and inp.bl_socket_idname == search_blid:
                socket_input = inp
                socket       = self.outputs[index]
                set_value    = False
                break

        # ----------------------------------------------------------------------------------------------------
        # Let's create it
        
        if socket_input is None:
            
            socket_input = self.tree.btree.inputs.new(type=DataSocket.get_bl_idname(class_name), name=name)
            self.build_outsockets()
            
            for sock in self.outputs:
                if sock.bsocket.identifier == socket_input.identifier:
                    socket = sock
                    break
                
        # ----------------------------------------------------------------------------------------------------
        # Let's apply the constraints
            
        if min_value is not None:
            socket_input.min_value = min_value
            
        if max_value is not None:
            socket_input.max_value = max_value
            
        socket_input.description = description
        
        # ----------------------------------------------------------------------------------------------------
        # Let's set the value if the socket is created
        # Note: if the socket already exists, we don't override its value
        
        if (value is not None) and set_value:
            
            if DataSocket.is_socket(value):
                value.plug(socket)
                
            else:
                v = socket.convert_python_type(value)
                msg1 = None
                msg2 = None
                try:
                    socket_input.default_value = v
                except Exception as e:
                    msg1 = str(e)

                try:
                    socket.bsocket.default_value = v
                except Exception as e:
                    msg2 = str(e)
                    
                if msg1 is not None:
                    print("CAUTION 1", name, socket.bl_idname, socket_input.bl_socket_idname, ">", msg1)
                    #print(dir(self.tree.btree.inputs[index]))
                    
                if msg2 is not None:
                    print("CAUTION 2", name, socket.bl_idname, socket_input.bl_socket_idname, ">", msg2)
                    
                #if msg is not None:
                #    raise RuntimeError(f"Impossible to set the default value '{value}' to the group input socket '{name}'.\n {msg}")
                    
            # ---------------------------------------------------------------------------
            # Set the default value to all modifiers using it
            #
            # The tree inputs store the default value of the sockets
            # The values themselves are stored in properties in the object modifiers
            # The modifier property is key by the tree input identifier
            
            for obj in bpy.data.objects:
                for mod in obj.modifiers:
                    if isinstance(mod, bpy.types.NodesModifier):
                        if mod.node_group == self.tree.btree:
                            mod[socket_input.identifier] = value
                            
        return socket        
        

            
# ----------------------------------------------------------------------------------------------------
# NodeGroupOutput

class GroupOutput(CustomGroup):
    """ Node *Group Output*
    
    Args:
        check_output_geometry: True for modifier
    
    Note
    ----
        The **input** sockets of this node are the **output** sockets of the group.
        
    This node is created by the Tree at initialization time. 
    
    .. blid:: NodeGroupOutput
    
    """
    
    def __init__(self, check_output_geometry: bool):
        
        super().__init__('NodeGroupOutput', 'Group Output')
        
        self.bsockets = self.bnode.inputs
        
        if check_output_geometry:
            ok = False
            ok_virtual = False
            for index, bsocket in enumerate(self.bnode.inputs):
                if bsocket.bl_idname == 'NodeSocketVirtual':
                    ok_virtual = True
                    break

                elif bsocket.bl_idname == 'NodeSocketGeometry':
                    ok = index == 0
                    break

                else:
                    break
                
            if not ok:
                if ok_virtual and len(self.tree.btree.outputs) > 0:
                    while len(self.tree.btree.outputs) > 0 and self.tree.btree.outputs[0].bl_socket_idname != 'NodeSocketVirtual':
                        self.tree.btree.outputs.remove(self.tree.btree.outputs[0])
                        
                self.tree.btree.outputs.new(type='NodeSocketGeometry', name="Geometry")
                self.build_outsockets()
                
                
        
    # --------------------------------------------------------------------------------
    # Default geometry input node

    @property
    def output_geometry(self):
        """ The output geometry socket of the tree.
        
        Returns:
            Geometry: The output geometry
        
        For a tree modifier, the first output socket of the group must be a geometry.
        
        """
        try:
            sock0 = self.bnode.inputs[0]
            if sock0.bl_idname == 'NodeSocketGeometry':
                return Node.Geometry(sock0)
            
            else:
                geo   = None
                for i, sock in enumerate(self.bnode.inputs):
                    if sock.name == "Geometry":
                        geo   = sock
                        break
                    
                if geo is None:
                    self.tree.btree.outputs.new(type='NodeSocketGeometry', name="Geometry")

                    self.build_insockets()
                
                index = self.insockets["geometry"]
                geo   = self.inputs[index]
                    
                #self.bnode.inputs.move(index, 0)
                #logger.error("GEONODES> Blender error: the method 'inputs.move' doesn't work. You must move yourself the outputs geometry in first position...")
                
                return Node.Geometry(geo)
                #return getattr(self, "geometry")

        except AttributeError as e:
            raise RuntimeError("GroupInput.input_geometry error: " + str(e), sys.exc_info()[2])
        
        #return Node.Geometry(self.bnode.inputs[0])
    
    # --------------------------------------------------------------------------------
    # Create a new output socket
    
    def to_output(self, socket: DataSocket, name: str = None):
        """ Plug the socket as an output of the tree.
        
        Args:
            socket: The socket to plug
            name: The name to display
            
        """
        
        class_name, sub_class = DataSocket.get_class_name(socket, True)
        if sub_class != '':
            class_name = sub_class
            
        if name is None:
            name = class_name
            
        # ----- Look for an existing socket with the proper name
        
        for index, bsocket in enumerate(self.bnode.inputs):
            
            if bsocket.bl_idname != socket.bl_idname:
                continue
            
            if bsocket.name == name:
                self.plug(index, socket)
                return

        # ----- Let's create it
        
        name = CustomGroup.unique_socket_name(name, self.insockets, prefix=class_name)
        
        bsocket = self.tree.btree.outputs.new(type=DataSocket.get_bl_idname(class_name), name=name)

        self.build_insockets()
        name = self.snake_case(name)
        
        index  = self.insockets[name]
        self.plug(index, socket)
        
# =============================================================================================================================
# Nodes required by Tree

# ----------------------------------------------------------------------------------------------------
# Node NodeFrame for NodeFrame

class Frame(Node):
    """ Node *Frame*
    
    Args:
        label: The frame label
        label_size: The font size for the label
        color: A valid color spec
        shrink: Shrink the Frame
        
    Note that *Frame* is the internal name for *Layouts*
    
    .. blid:: NodeFrame
    """

    def __init__(self, label: str = "Layout", label_size: int = 16, color: Any = None, shrink: bool = True):

        super().__init__('NodeFrame', 'Frame', label=label)
        if color is None:
            color = colors.next_color()
        self.node_color = color

        # Parameters

        self.bnode.label_size  = label_size
        self.bnode.shrink      = shrink
        self.ok_capture_inputs = False
        
    def get_label(self):
        """ Build the node label
        
        If the label provided at initialization time is None, the node is labeled by concatening
        its unique id with its standard name.
        """
        return f"{self.node_id:2d} {self.node_name}" if self.label_ is None else f"{self.label_}"
        
        
    @property
    def label_size(self):
        return self.bnode.label_size

    @label_size.setter
    def label_size(self, value):
        self.bnode.label_size = value

    @property
    def shrink(self):
        return self.bnode.shrink

    @shrink.setter
    def shrink(self, value):
        self.bnode.shrink = value

    # ---------------------------------------------------------------------------
    # The nodes within the frame
    
    @property
    def children(self):
        return [node for node in self.tree.nodes if node.bnode.parent == self.bnode]
        
    # ---------------------------------------------------------------------------
    # Capture the inputs
    # replace all the links from group input to one node internally by a
    # link with a new instance of group input
    #
    # Note : deals only with blender nodes and links
    # It is transparent for the script
    
    def capture_inputs(self):
        
        tree   = self.tree.btree
        frame  = self.bnode
        nodes  = []
        inputs = []
        
        group_input = self.tree.group_input.bnode
        frame_input = None
        
        # ----- Put the nodes in the chilren list
        
        for node in tree.nodes:
            if node.parent == frame:
                if node.bl_idname == 'NodeGroupInput':
                    frame_input = node
                else:
                    nodes.append(node)
                    
        # ----- Get all the incoming links
                
        links = []
        for link in tree.links:
            if link.from_node == group_input and link.to_node in nodes:
                links.append(link)
                
        if not links:
            return
        
        if frame_input is None:
            frame_input = tree.nodes.new(type='NodeGroupInput')
            frame_input.parent = frame
            
        for link in links:
            from_socket = None
            to_socket   = link.to_socket
            
            for i_sock, socket in enumerate(group_input.outputs):
                if socket == link.from_socket:
                    from_socket = frame_input.outputs[i_sock]
                    break
                
            tree.links.remove(link)
            tree.links.new(from_socket, to_socket)
        
        
# ----------------------------------------------------------------------------------------------------
# Scene

class SceneTime(Node):
    """ Node *Scene Time* ()
    
    Args:
        label: The node label
        
    Provides the *seconds* and *frame* value for animation.
    
    The :attr:`Tree.scene` property maintains an instance of this node:
    
    .. code-block:: python
    
        time = tree.scene.seconds
        frame_number = tree.scene.frame
        
    .. blid: GeometryNodeInputSceneTime
    """

    def __init__(self, label: str = None):
        """ Iniitialisation """

        super().__init__('GeometryNodeInputSceneTime', 'Scene Time', label=label)

        # Output sockets

        self.outsockets = {'seconds': 0, 'frame': 1}
        
        

        
        
        
        
        
        
    
    
        