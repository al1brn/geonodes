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

from geonodes import colors
from .arrange import arrange

from typing import Any

try:
    import bpy
    import mathutils
except:
    pass


NODE_STD_ATTRS = [
   '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
   'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
   'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
   'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
   'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
   'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
   'show_texture', 'socket_value_update', 'type', 'update', 'use_clamp', 'use_custom_color',
   'width', 'width_hidden']


# =============================================================================================================================
# Socket wrapper
#
# Root class for DataSocket and Domain

class Socket:
    """ DataSocket root class
    
    :param socket: a node socket, or a instance of Socket
    :param node: The Node owning the socket. If None the owner is searched.
    :type socket: bpy.types.nodesocket, Socket
    :type node: Node
    
    This class is the base class wrapper of node sockets.
    
    To avoid confusion between wrapped Node and Socket with wrapper Node and Socket,
    the wrapped variables are prefixed by 'b':
        
    - **bnode** : a wrapped node (bpy.types.GeometryNode)
    - **bsocket** : a wrapped socket (bpy.types.NodeSocket)
    
    """ 
    
    # Socket class, sub class and domain data type from socket bl_idname    
        
    SOCKET_IDS = {
        'NodeSocketBool'        : ('Boolean',    '',             'BOOLEAN'), 

        'NodeSocketInt'         : ('Integer',    '',             'INT'), 
        'NodeSocketIntUnsigned' : ('Integer',    'Unsigned',     'INT'), 

        'NodeSocketFloat'       : ('Float',      '',             'FLOAT'), 
        'NodeSocketFloatFactor' : ('Float',      'Factor',       'FLOAT'),
        'NodeSocketFloatAngle'  : ('Float',      'Angle',        'FLOAT'), 
        'NodeSocketFloatDistance': ('Float',     'Distance',     'FLOAT'), 

        'NodeSocketVector'      : ('Vector',     '',             'FLOAT_VECTOR'), 
        'NodeSocketVectorEuler' : ('Vector',     'Rotation',     'FLOAT_VECTOR'),
        'NodeSocketVectorXYZ'   : ('Vector',     'xyz',          'FLOAT_VECTOR'), 
        'NodeSocketVectorTranslation' : ('Vector', 'Translation','FLOAT_VECTOR'), 

        'NodeSocketColor'       : ('Color',      '',             'FLOAT_COLOR'), 
        'NodeSocketString'      : ('String',     '',             'FLOAT_COLOR'), 

        'NodeSocketGeometry'    : ('Geometry',   '',              None), 

        'NodeSocketCollection'  : ('Collection', '',              None), 
        'NodeSocketImage'       : ('Image',      '',              None), 
        'NodeSocketMaterial'    : ('Material',   '',              None), 
        'NodeSocketObject'      : ('Object',     '',              None), 
        'NodeSocketTexture'     : ('Texture',    '',              None), 
    }
    
    # ----------------------------------------------------------------------------------------------------
    # > Socket initialization
    #
    # Arguments
    # ---------
    # - socket: a node socket or a Socket
    #   Passing a Socket instance as argument allows type casting
    #
    #   ```python
    #   value = Float(10.) # Float data class pointing on the output socket of node "Value"
    #   v = Vector(value)  # Cast the previous socket to Vector
    #   ```
    #
    # - node: the node owning the socket. If node is None, the initializer searchs for it in the list
    #  of existing nodes.
    #
    # - label: optional node label. Used to name the created Geometry Nodes.
    #

    def __init__(self, socket, node=None):
        
        # ----- A class Object doesn't have a constructor Node
        
        self.data_socket = socket # Used in domain. This is a DataSocket for sure.
        """ Used by domain"""
        
        self.bsocket = None
        """ The wrapped geometry node socket"""
        self.node    = None
        """ The owning node"""

        if socket is not None:
            if Socket.is_socket(socket):
                self.bsocket = socket.get_blender_socket()
    
            elif isinstance(socket, bpy.types.NodeSocket):
                self.bsocket = socket
                
            else:
                raise RuntimeError(f"A Socket instance needs a socket to be initialized, not {socket}.")
                
            if node is None:
                self.node = Tree.TREE.get_bnode_wrapper(self.bsocket.node)
            else:
                self.node = node
                
        # ----- Specific initialization
        
        self.init_socket()
        
        
    def __str__(self):
        snode = str(self.node)
        if self.is_output:
            return f"{snode}.{self.name}"
        else:
            return f"{self.name}.{snode}"
        
    def __repr__(self):
        return str(self)
    
    # ----------------------------------------------------------------------------------------------------
    # Called by init
    
    def init_socket(self):
        """ Complementary init
        
        Called at the end of initialization for further operations.
        """
        pass
    
    @staticmethod
    def is_socket(value):
        """ An alternative to isinstance(value, Socket)

        :param value: The value to test
        :type value: any
        :return: True if *value* is an instance of Socket
        :rtype: bool
        """
        return hasattr(value, 'get_blender_socket')

    
    @staticmethod
    def gives_bsocket(value):
        """ Test if the argument provides a valid output socket.
        
        :param value: The value to test
        :type value: any
        :return: True if *value* is or wraps a socket
        :rtype: bool
        
        Returns True if value is:
            
        - A Blender Geometry Node Socket
        - An instance of Socket        
        """
        
        return Socket.is_socket(value) or isinstance(value, bpy.types.NodeSocket)
    
    # ----------------------------------------------------------------------------------------------------
    # The Blender socket is used to link nodes
    # Rather than accessing it directly, one must use the method get_blender_socket
    # This method can be used to implement specific code before connection
    
    def get_blender_socket(self):
        """ Returns the property bsocket.
        
        :return: self.bsocket
        :rtype: bpy.types.NodeSocket
        """
        
        return self.bsocket
    
    @property
    def bl_idname(self):
        """ Shortcut for `self.bsocket.bl_idname`
        """
        return self.bsocket.bl_socket_idname if isinstance(self.bsocket, bpy.types.NodeSocketInterfaceGeometry) else self.bsocket.bl_idname
    
    @property
    def name(self):
        """ Shortcut for `self.bsocket.name`
        """
        return self.bsocket.name
        
    @property
    def is_output(self):
        """ Shortcut for `self.bsocket.is_output`
        """
        return self.bsocket.is_output
    
    @property
    def is_multi_input(self):
        """ Shortcut for `self.bsocket.is_multi_output`
        """
        return self.bsocket.is_multi_output
    
    @property
    def links(self):
        """ Shortcut for `self.bsocket.links`
        """
        return self.bsocket.links

    @property
    def bnode(self):
        """ Shortcut for `self.bsocket.node`
        """
        return self.bsocket.node
    
    @property
    def socket_index(self):
        """ Return the index of the socket within the list of node sockets.
        
        Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
        *node.outputs*.
        """
        
        if self.is_output:
            bsockets = self.bnode.outputs
        else:
            bsockets = self.bnode.inputs
            
        for index, bsocket in enumerate(bsockets):
            if self.bsocket == bsocket:
                return index
            
        raise RuntimeError(f"Impossible to find the index of socket {self} of node {self.node}")
        
    def connected_sockets(self):
        """ Returns the list of Socket instances linked to this socket.
        """ 
        
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
    def domain_data_type(value):
        """ Returns the domain to which the socket belongs
        
        :param value: The socket
        :type value: bpy.types.NodeSocket, Socket
        :return: Domain code in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
        :rtype: str
        
        .. list-table:: Correspondance table
           :widths: 30 20
           :header-rows: 1
        
           * - Socket bl_idname
             - Domain code
           * - NodeSocketBool
             - 'BOOLEAN'
           * - NodeSocketInt               
             - 'INT'
           * - NodeSocketIntUnsigned       
             - 'INT'
           * - NodeSocketFloat            
             - 'FLOAT'
           * - NodeSocketFloatFactor       
             - 'FLOAT'
           * - NodeSocketFloatAngle        
             - 'FLOAT'
           * - NodeSocketFloatDistance     
             - 'FLOAT'         
           * - NodeSocketVector            
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorEuler       
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorXYZ         
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorTranslation
             - 'FLOAT_VECTOR'
           * - NodeSocketColor      
             - 'FLOAT_COLOR'
           * - NodeSocketString           
             - 'FLOAT_COLOR'
        
        """
        
        class_dt = {
            'Boolean' : 'BOOLEAN',
            'Integer' : 'INT',
            'Float'   : 'FLOAT',
            'Vector'  : 'FLOAT_VECTOR',
            'Color'   : 'FLOAT_COLOR'
            }
        
        if value is None:
            return 'POINT'
        
        elif isinstance(value, str):
            if value in Socket.SOCKET_IDS:
                return Socket.SOCKET_IDS[socket.bl_idname][2]
            
            elif value in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN'):
                return value
            
            elif value in class_dt:
                return class_dt[value]
            
        else:
            if hasattr(value, 'bl_idname'):
                return Socket.SOCKET_IDS[value.bl_idname][2]
            
            cname = type(value).__name__
            if cname in class_dt:
                return class_dt[cname]
            
            if isinstance(value, bool):
                return 'BOOLEAN'
            
            elif isinstance(value, int):
                return 'INT'
            
            elif isinstance(value, float):
                return 'FLOAT'
            
            elif hasattr(value, '__len__'):
                if len(value) == 3:
                    return 'FLOAT_VECTOR'
                elif len(value) == 4:
                    return 'FLOAT_COLOR'
        
        raise RuntimeError(f"Unknown data type code: '{value}'")
    
    # ----------------------------------------------------------------------------------------------------
    # Class name from socket bl_idname
    
    @staticmethod
    def get_class_name(socket, with_sub_class = False):
        """ Get the DataSocket class name corresponding to the socket type and name.
        
        :param socket: The socket to determine the class of
        :param with_sub_class: Return the sub class if True
        :typ socket: bpy.types.NodeSocket, Socket
        :type with_sub_class: bool
        :return: The name of the class associated to the bl_idname of the socket
        :rtype: str
        
        .. list-table:: Correspondance table
           :widths: 30 20 20
           :header-rows: 1
           
           * - NodeSocket
             - class name
             - sub class name
           * - NodeSocketBool 
             - 'Boolean'
             - 
           * - NodeSocketInt 
             - 'Integer'
             - 
           * - NodeSocketIntUnsigned 
             - 'Integer'
             - 'Unsigned'
           * - NodeSocketFloat 
             - 'Float' 
             - 
           * - NodeSocketFloatFactor 
             - 'Float'
             - 'Factor'
           * - NodeSocketFloatAngle  
             - 'Float'
             - 'Angle'
           * - NodeSocketFloatDistance 
             - 'Float'
             - 'Distance'
           * - NodeSocketVector 
             - 'Vector'
             - 
           * - NodeSocketVectorEuler 
             - 'Vector'
             - 'Rotation'
           * - NodeSocketVectorXYZ 
             - 'Vector'
             - 'xyz'
           * - NodeSocketVectorTranslation 
             - 'Vector'
             - 'Translation'
           * - NodeSocketColor 
             - 'Color'
             - 
           * - NodeSocketString' 
             - 'String'
             - 
           * - NodeSocketCollection 
             - 'Collection'
             - 
           * - NodeSocketImage 
             - 'Image'
             - 
           * - NodeSocketMaterial 
             - 'Material'
             - 
           * - NodeSocketObject 
             - 'Object'
             - 
           * - NodeSocketTexture 
             - 'Texture'
             - 
           * - NodeSocketGeometry
             - 'Geometry'
             - 
          
          
        If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve'],
        the name is chosen as the class name.
        """
        bl_idname = socket.bl_idname
        class_name = Socket.SOCKET_IDS[bl_idname][0]
        name = socket.name
        
        if class_name == 'Geometry' and name in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve']:
            class_name = name
            
        if with_sub_class:
            return class_name, Socket.SOCKET_IDS[bl_idname][1]
        else:
            return class_name
        
    @staticmethod
    def get_bl_idname(class_name):
        """ Get the node socket bl_idname name from the Socket class
        
        :param class_name: The class name
        :type class_name: str
        :return: The bl_idname associated to this class name
        :rtype: str
        
        Used to create a new group input socket. Called in `DataClass.Input` method to determine
        which socket type must be created.
        
        Note that here the class_name argument accepts additional values which correspond to *sub classes*:
            
        .. list-table:: 
           :widths: 20 40
           :header-rows: 0
        
           * - Unsigned
             - Integer sub class (NodeSocketIntUnsigned)
           * - Factor
             - Float sub class (NodeSocketFloatFactor)
           * - Angle
             - Float sub class  (NodeSocketFloatAngle)
           * - Distance
             - Float sub class (NodeSocketFloatDistance)
           * - Rotation
             - Vector sub class (NodeSocketVectorEuler)
           * - xyz
             - Vector sub class (NodeSocketVectorXYZ)
           * - Translation
             - Vector sub class (NodeSocketVectorTranslation)
          
        These additional values allow to enter angle, distance, factor... as group input values.
        """
        
        if Socket.is_socket(class_name):
            class_name = type(class_name).__name__
        
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
        
        elif class_name in ['Xyz']:
            return 'NodeSocketVectorXYZ'
        
        elif class_name in ['Translation']:
            return 'NodeSocketVectorTranslation'

        
        elif class_name in ['Color']:
            return 'NodeSocketColor'
        
        elif class_name in ['String']:
            return 'NodeSocketString'
        
        elif class_name in ['Geometry', 'Mesh', 'Points', 'Instances', 'Volume', 'Curve', 'Spline']:
            return 'NodeSocketGeometry'
        
        elif class_name in ['Image']:
            return 'NodeSocketImage'
        
        elif class_name in ['Material']:
            return 'NodeSocketMaterial'
        
        elif class_name in ['Texture']:
            return 'NodeSocketTexture'
        
        elif class_name in ['Collection']:
            return 'NodeSocketCollection'
        
        elif class_name in ['Object']:
            return 'NodeSocketObject'
        

# =============================================================================================================================
# > Root for data classes
#
# DataSocket refers to an output socket of a Geometry Node.
#
# ```python 
# DataSocket.bsocket # The output socket of a Geometry Node
# ```
#
# Methods of DataSocket instances are implemented with nodes. The output socket refered by
# the DataSocket instance is linked to an input socket of the method node.
#
# For instance:
# 
# ```python
# geo = Mesh.UVSphere()  # geo refers to the output socket of the node "Mesh UVSphere"
# geo.set_shade_smooth() # the previous output socket is linked to the input socket of
#                        # the node "Set Shade Smooth"
# ````
#
# Properties
# ----------
#
# - node: The node owning the output socket. The Blender Geometry Node itself is a property of node
#
#   ```python
#   node = a_data_socket.node # The Node class wrapping the Geometry Node
#   blender_node = node.bnode # The Blender geometry node
#   ```
#
# - bsocket: The Blender output socket 


class DataSocket(Socket):
    """ Geometry wrapper: root class for data sockets: Boolean, Integer, Geometry, Curve, Object,...
    
    :param socket: a node socket, or a instance of Socket
    :param node: The Node owning the socket. If None the owner is searched.
    :param label: The label to use for the geometry node
    :type socket: bpy.types.nodesocket, Socket
    :type node: Node
    :type label: str
    
    **Type casting**
    
    Passing a DataSocket instance as argument allows type casting
    
    :example:
        
    .. code-block:: python

        value = Float(10.) # Float data class pointing on the output socket of node "Value"
        v = Vector(value)  # Cast the previous socket to Vector
    
    """

    def __init__(self, socket, node=None, label=None):
        
        super().__init__(socket, node)
            
        if self.node is not None and label is not None:
            self.node.label = label
        
        # ----- Reset creates the place holder for properties
        
        self.reset_properties()
        
        # ----- Set by Field
        
        self.field_of = None
        """ Used by field to implement transfer attribute mechanism. This property is set to all node output sockets."""
    
    @property
    def node_chain_label(self):
        """ Shortcut for *self.node.chain_label*
        """
        if self.node is None:
            return ""
        else:
            return self.node.chain_label

    # ----------------------------------------------------------------------------------------------------
    # Initialize the geometry domains:
    # - Mesh
    #     - Vertex
    #     - Edge
    #     - Face
    #     - Face corner
    # - Curve
    #     - Point
    #     - Spline
    # - Point cloud
    #     - Point
    # - Instances
    #
    
    def init_domains(self):
        """ Initialize the geometry domains
        
        To be overloaded by sub classes.        
        """
        pass
    
    # ----------------------------------------------------------------------------------------------------
    
    def reset_properties(self):
        """ Reset the properties
        
        Properties such as components are cached.
        
        After a node is called, the wrapped socket changes and this makes the cache obsolete.
        After a change, the cache is erased.
        
        :example:
        
        .. code-block:: python
    
            class Vector(...):
                def __init__(self, ...):
                     ...
                     self.reset_properties()
                     ...
            
                 def reset_properties(self):
                     super().reset_properties()
                     self.separate_ = None      # Created by property self.seperate() with node SeparateXyz

        
        """
        
        self.init_domains()
    
    # ----------------------------------------------------------------------------------------------------
    # Utility changing the output sockets refered by the DataSocket instance
    
    def stack(self, node):
        """ Change the wrapped socket
        
        :param node: The new node owning the output socket to wrap
        :type node: Node
        :return: self
        
        Methods are implemented in two modes:
        
        - Creation
        - Transformation
        
        In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.
        
        In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
        After the method returns, the calling DataSocket instance refers to a new Blender output socket.
        The stack method changes the socket the instance refers to and reinitialize properties
        
        .. code-block:: python

            # 1. Creation mode
            # 
            # to_mesh method creates a new mesh from a curve.
            # The curve instance refers to the same output node socket
            # We need to get the result of the method in a new variable
            
            new_mesh = curve.to_mesh(profile_curve=circle)
            
            # 2. Transformation mode
            #
            # set_shade_smooth method transforms the mesh.
            # After the call, the mesh instance refers to the output socket of the
            # newly created node "Set Shade Smooth". There is no need to get the result
            # of the method.
            
            mesh.set_shade_smooth()
            
            # Note that a transformation method returns self and so, the following line
            # is equivallent:
            
            mesh = mesh.set_shade_smooth()
        
        """
        
        self.node    = node
        self.bsocket = node.bnode.outputs[0]
        self.reset_properties()

        return self

    # ----------------------------------------------------------------------------------------------------
    # Plug (for input sockets only)
    
    @staticmethod
    def plug_bsocket(bsocket, *values):
        """ Plug the values to the input Blender socket.
        
        :param bsocket: The input socket to plug into 
        :param values: The output sockets. More than one values can be passed
            if the input socket is multi input.
        :type bsocket: bpy.types.NodeSocket, Socket
        :type values: array of bpy.types.NodeSocket, Socket, values

        .. warning:: bsocket must be an **input socket** and values must be **output sockets-like**.
        
        This static method is called by the DataClass method :func:`plug`.
        
        This method is the one which links an output socket of a node to the input
        socket of another one.
        
        If the socket is multi input, the plug method is called once per provided value.
        If a value is None, nothing happens.
        
        A not None value can be:
            
        - either a valid value for the socket (eg: 123 for Integer socket)
        - or an output socket of another Node
            
        When it is a socket, it can be a Blender socket or a DataSocket
        """
        
        if bsocket.is_output:
            raise RuntimeError(f"Method 'plug' can only be used with input sockets, not {bsocket}.")
        
        # ---------------------------------------------------------------------------
        # Nothing to plug

        if len(values) == 0:
            return

        # ---------------------------------------------------------------------------
        # If several output sockets to plugn let's loop on the list
        
        if len(values) > 1:
            if not bsocket.is_multi_input:
                raise RuntimeError(f"Input socket {bsocket} is not multi input: impossible to plug multiple sockets: {values}.")
            for v in values:
                DataSocket.plug_bsocket(bsocket, v)
            return
        
        # ---------------------------------------------------------------------------
        # Ok now: only one thing to plug.
        # It can be a value or a socket (or directly a blender output socket)
        
        # ----- Let's suppress the existing links
        
        #if not is_multi_input:
        #    links = [link for link in self.bnode.links]
        #    for link in links:
        #        self.node.tree.links.remove(links) 
        
        value = values[0]
        if value is None:
            return
        
        out_socket = None
        if isinstance(value, bpy.types.NodeSocket):
            out_socket = value
        elif Socket.is_socket(value):
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
            
        # ----- It is a value
        # Let's put it in the default_value of the input socket
            
        if out_socket is None:
            
            if bsocket.is_multi_input:
                raise RuntimeError(f"The socket {bsocket} is multi input. Impossible to plug the value {value}.")
                
            # ----- Vector / Color hack: a single value is broadcasted in a triplet
            
            if hasattr(bsocket, 'default_value') and hasattr(bsocket.default_value, '__len__'):
                
                # Broadcast 1 --> 3
                if not hasattr(value, '__len__'):
                    value = (value,) * len(bsocket.default_value)
                    
                # Color --> Vector
                elif len(bsocket.default_value) == 3 and len(value) == 4:
                    value = (value[0], value[1], value[2])
                    
                # ----- Hack : transform a triplet (a, b, c) with a component
                # which is a socket to a Vector
                
                to_vector = False
                
                # bsocket with hide_value == True doesn't accept a default-value
                if bsocket.hide_value:
                    to_vector = True
                    
                for v in value:
                    if Socket.is_socket(v):
                        to_vector = True
                        break
                    
                if to_vector:
                    from geonodes import Vector
                    DataSocket.plug_bsocket(bsocket, Vector((value)).bsocket)
                    return
                
            # ----- Socket material hack : replace the name of the material by the material
            
            if isinstance(bsocket, bpy.types.NodeSocketMaterial):
                if type(value) is str:
                    try:
                        value = bpy.data.materials[value]
                    except:
                        raise RuntimeError(f"Material '{value}' not found.")
            
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
                
        else:
            # Check that multi doesn't feed single
            # sockets shapes = [‘CIRCLE’, ‘SQUARE’, ‘DIAMOND’, ‘CIRCLE_DOT’, ‘SQUARE_DOT’, ‘DIAMOND_DOT’]
            
            #if out_socket.display_shape == 'DIAMOND' and bsocket.display_shape == 'CIRCLE':
            #    logging.error(f"Link error: the socket '{out_socket.node.name}'.'{out_socket.name}' is ‘DIAMOND’. " +
            #    f"It can't be linked with the socket '{bsocket.node.name}'.'{bsocket.name}' which is CIRCLE.")
            
            
            Tree.TREE.btree.links.new(bsocket, out_socket, verify_limits=True)
            
            #print(out_socket, bsocket, Tree.TREE.group_output.inputs[0].bsocket)
            
            outs = Tree.TREE.group_output.inputs
                
            
    # ----------------------------------------------------------------------------------------------------
    # Plug (for input sockets only)
            
    def plug(self, *values):
        """ Plug values in the socket (input sockets only)
        
        :param values: The output sockets. More than one values can be passed
            if the input socket is multi input.
        :type values: array of bpy.types.NodeSocket, Socket, values
        
        see :func:`plug_bsocket`
        """
        DataSocket.plug_bsocket(self.bsocket, *values)
        
    # ----------------------------------------------------------------------------------------------------
    # To group output (for output sockets only)
    
    def to_output(self, name=None):
        """ Plug the data socket to the group output
        
        :param name: The name to give to the modifier output
        :type name: str
        
        The socket is added to the outputs of the geometry nodes tree.
        
        .. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.
        
        """
        if not self.is_output:
            raise RuntimeError(f"The socket '{str(self)}' is not an output socket. It can't be sent to group output.")
        self.node.tree.group_output.to_output(self, self.name if name is None else name)
        
    # ----------------------------------------------------------------------------------------------------
    # To viewer (for output sockets only)
        
    def view(self):
        """ Link the data socket to the viewer
        
        If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.
        
        If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
        accordingly.
        """
        if not self.is_output:
            raise RuntimeError(f"The socket '{str(self)}' is not an output socket. It can't be connected to the viewer.")
        self.node.tree.view(self)
        
    # ----------------------------------------------------------------------------------------------------
    # Reroute
    
    def reroute(self):
        """ Reroute all output links
        """
        links = self.bsocket.links
        if not links:
            return
        
        btree = self.node.tree.btree
        node = btree.nodes.new('NodeReroute')
        node.parent = self.node.tree.cur_frame
        btree.links.new(self.bsocket, node.inputs[0])
        
        sockets = [link.to_socket for link in links]
        for link in links:
            btree.links.remove(link)
        
        for socket in sockets:
            btree.links.new(node.outputs[0], socket)

    # ----------------------------------------------------------------------------------------------------
    # Transfer are steered by the Field it belongs to
    
    def index_transfer(self, index=None):
        if self.field_of is None:
            raise Exception(f"{type(self).__name__}.index_transfer: the socket {self} is not a field.")
        return self.field_of.index_transfer(attribute=self, index=index)
    
    def nearest_transfer(self, source_position=None):
        if self.field_of is None:
            raise Exception(f"{type(self).__name__}.nearest_transfer: the socket {self} is not a field.")
        return self.field_of.nearest_transfer(attribute=self, source_position=source_position)
    
    def nearest_face_transfer(self, source_position=None):
        if self.field_of is None:
            raise Exception(f"{type(self).__name__}.nearest_face_transfer: the socket {self} is not a field.")
        return self.field_of.nearest_face_transfer(attribute=self, source_position=source_position)
            
    

# =============================================================================================================================
# Nodes tree    

class Tree:
    """ Wrap a Blender NodeTree
    
    :param tree_name: Name of the tree (index in ``bpy.data.node_groups``)
    :param clear: delete the existing nodes
    :param group: the tree node is not for a Geometry Node modifier but for a Group
    :type tree_name: str
    :type clear: bool
    :type group: bool
    
    
    A tree class encapsulates a Blender NodeTree:
        
    .. code-block:: python

        blender_tree = tree.btree # The Blender NodeTree

    
    Nodes are created by data sockets methods. In case of an error, the user can see the state of
    the tree when the script stops.
    
    **Creation / closure**
    
    Once the tree is completed, the :func:`arrange` method tries to place the nodes in a readable shape.
    Hence, building a tree is made between the two instructions:
        
    - ``tree = Tree(tree_name)`` : creation / opening of the Blender NodeTree
    - ``tree.close()`` : arrange the nodes
    
    It is recommended to use the ``with`` context:
        
    .. code-block:: python

        with Tree("Geometry Nodes") as tree:
            # ... nodes creation

    
    **The TREE static property**
    
    The TREE static attribute of class Tree maintains the current active Tree, i.e. the tree into which
    creating the new nodes. There is only one single *open* tree at a time.
    The method :func:`activate` set the tree as the current one.
    At creation time, a Tree instance becomes the current one.
    
    **Layouts**
    
    For a better clarity of the resulting tree, it is possible to put the newly created nodes in a layout.
    At creation time, one can define both the layout label and color.
    The layout creation makes use of the ``with`` context (see :func:`layout`):
        
    .. code-block:: python

        with Tree("Geometry Node") as tree:
            
            # Nodes created here are placed directly on the tree background
            
            with tree.layout("Some tricky computation", color="green"):
                
                # Nodes created here are placed in the current layout
                
                with tree.layout("The most difficult part", color="red"):
                    
                    # Layouts can be imbricated
                    
            # Back to standard creation
    
    **Initialization**
    
    At initialization time, the existing nodes can be deleted or kept. Use ``clear=True``
    to erase all the existing nodes.
      
    The nodes which are kept are the ones which can not be configured by script, for instance
    the  *Float Curve* or  *ColorRamp* nodes. These nodes are reused when instancied in the script.
    This allows not to loose nodes tuning.
        
    """
    
    KEEPS = ['GeometryNodeImageTexture', 'GeometryNodeInputMaterial', 'GeometryNodeStringToCurves', 'ShaderNodeFloatCurve',
             'ShaderNodeFloatCurve', 'ShaderNodeValToRGB', 'ShaderNodeVectorCurve', 'FunctionNodeInputColor']
    
    TREE = None
    
    def __init__(self, tree_name, clear=False, group=False):
        
        if bpy.data.node_groups.get(tree_name) is None:
            bpy.data.node_groups.new(tree_name, type='GeometryNodeTree')

        self.btree = bpy.data.node_groups[tree_name]
        """ The geometry tree nodes"""
        
        # ---------------------------------------------------------------------------
        # Capture the configuration of the nodes
        # TO BE IMPROVED!
        
        class ONode:
            def __init__(self, bnode):
                match = re.search(r"\[\s*(\d+)", bnode.name)
                if match is None:
                    self.index = bnode.name
                else:
                    self.index = int(match.group(1))
                self.name  = bnode.name
                self.label = bnode.label
                self.args  = self.get_args(bnode)
                
            def __str__(self):
                return f"<{self.name}: {self.label}>\n"

            def __repr__(self):
                return str(self)
            
            def get_args(self, bnode):
                a = []
                for socket in bnode.inputs:
                    if not socket.enabled:
                        continue
                    
                    if socket.links:
                        continue
                    
                    try:
                        value = socket.default_value
                    except:
                        continue
                        
                    name = socket.name.lower().replace(' ', '_')
                    if isinstance(value, str):
                        a.append(f"{name}='{value}'")
                    else:
                        a.append(f"{name}={value}")
                        
                for attr in dir(bnode):
                    if attr[:2] == '__' or attr in NODE_STD_ATTRS:
                        continue
                    
                    try:
                        value = getattr(bnode, attr)
                    except:
                        continue
                    
                    name = attr.lower().replace(' ', '_')
                    if isinstance(value, str):
                        a.append(f"{name}='{value}'")
                    else:
                        a.append(f"{name}={value}")
                        
                return ", ".join(a)
            
        self.previous = {}
        """ Keep a list of the existing nodes before removing them"""
        for bnode in self.btree.nodes:
            onode = ONode(bnode)
            self.previous[onode.index] = onode
            
        # ---------------------------------------------------------------------------
        # Clear the tree
        
        self.btree.links.clear()

        self.old_bnodes = []
        """ The old nodes which are not deleted"""
        
        if clear:
            self.btree.nodes.clear()
        else:
            rems = []
            for bnode in self.btree.nodes:
                if bnode.bl_idname in Tree.KEEPS:
                    self.old_bnodes.append(bnode)
                else:
                    rems.append(bnode)
                    
            for bnode in rems:
                self.btree.nodes.remove(bnode)
            del rems
            
        self.nodes  = []
        """ List of the created nodes"""
        self.node_id = 0
        """ Node id counter. Incremented at each node registration"""
        self.activate()

        self.capture_attributes = True
        """ Flag to capture the attributes or not (see :func:`check_attributes`)"""
        
        # ----- Layouts stack
        
        self.layouts = []
        """ Stack of layouts (see :func:`layout`)"""
        self.util_color = "dark_green"
        """ Color code for internal layouts"""
        self.gene_color = "dark_orange"
        """ Color code for internal layouts"""
        self.auto_color = "dark_rose"
        """ Color code for internal layouts"""
        
        # ----- Input and outputs
        
        self.group_input  = GroupInput(check_input_geometry=not group)
        """ The 'Group Input' node"""
        self.group_output = GroupOutput(check_output_geometry=not group)
        """ The 'Group Output' node"""
        
        # ----- Viewer
        
        self.viewer = None
        """ The 'Viewer' node"""
        self.scene_ = None

        # ----- Reset the colors carroussel
        
        colors.reset()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.close()
        
    # ----------------------------------------------------------------------------------------------------
    # Get / create a Blender node
        
    def get_bnode(self, bl_idname, label=None):
        """ Get an existing, or create a new, Blender node in the tree.
        
        :param bl_idname: The node bl_idname
        :param label: Node label
        :type bl_idname: str
        :type name: str
        :return: A geometry node
        :rtype: bpy.types.GeometryNode
        
        
        At initialization time, some nodes (the ones which can be changed by UX) are kept
        in ``old_bnodes`` list. Before creating a new node, this list is scaned to find a node
        of the proper type and the proper label.
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
            # Group: the label is used to pass the group name
            if bl_idname == 'GeometryNodeGroup':
                bnode.node_tree = bpy.data.node_groups.get(label)
        else:
            bnode = found
            self.old_bnodes.remove(bnode)
        
            if label is not None:
                bnode.label = label
            
        bnode.select = False
        bnode.parent = self.cur_frame
        
        return bnode
                        
        
    def activate(self):
        """ Set this tree as the current one.
        
        The Tree class property ``TREE`` is set to ``self``
        """
        
        Tree.TREE = self
        
    def register_node(self, node):
        """ Register the node passed in parameter in the current tree.
        
        :param node: The node to register
        :type node: Node
        :return: The node
        :rtype: Node
        
        When registered, a unique id is provided to the node.
        This allows the users to more clearly distinguish the nodes.
        
        """
        
        self.node_id += 1
        node.node_id = self.node_id
        self.nodes.append(node)
        return node
    
    # ---------------------------------------------------------------------------
    # Get the node wrapper of a blender node
    
    def get_bnode_wrapper(self, bnode):
        """ Get the Node instance wrapping the Blender node passed in argument.
        
        :param bnode: The geometry node to look the warpper of
        :type bnode: bpy.types.NodeSocket
        :return: The wrapping node
        :rtype: Node
        :raise: Exception if the wrapper is not found
        """
        
        for node in self.nodes:
            if node.bnode == bnode:
                return node
        raise Exception(f"Impossible to find the wrapper node of Blender node {bnode}.")
            
    def get_bsocket_wrapper(self, bsocket):
        """ Get the DataSocket instance wrapping the Blender socket passed in argument.
        
        :param bsocket: The blender socket to search the werapper of
        :type bsocket: bpy.types.NodeSocket
        :return: The node wrapping the socket
        :rtype: Node
        :raise: Exception if not found
        
        """
        
        node = self.get_bnode_wrapper(bsocket.node)
        for socket in itertools.chain(node.inputs, node.outputs):
            if socket.bsocket == bsocket:
                return socket
        raise RuntimeError(f"Impossible to find the wrapper socket of Blender socket {bsocket}, of node {node}.")
        
    # ----------------------------------------------------------------------------------------------------
    # Input output interface
    
    @property
    def input_geometry(self):
        """ The group input geometry.
        
        .. code-block:: python
        
            my_geometry = tree.input_geometry
        
        """
        return self.group_input.input_geometry
    
    @property
    def ig(self):
        """ Shortcut for :attr:`input_geometry`
        """
        return self.input_geometry
        
    @property
    def output_geometry(self):
        """ The group output geometry.
        
        .. code-block:: python
        
            tree.output_geometry = my_geometry 
        
        """
        return self.group_output.output_geometry
    
    @output_geometry.setter
    def output_geometry(self, value):
        self.group_output.output_geometry.plug(value)
        
    @property
    def og(self):
        """ Shortcut for :attr:`output_geometry`.
        """
        return self.output_geometry
        
    @og.setter
    def og(self, value):
        self.output_geometry = value
        
        
    def new_input(self, class_name, value=None, name=None, min_value=None, max_value=None, description=""):
        """ Create a new input socket.
        
        :param class_name: Class name of the value to get
        :param value: Initial value
        :param min_value: Minimum value
        :param max_value: Maximum value
        :param description: User type
        :type class_name: str
        :type value: Depending on the class
        :type min_value: Depending on the class
        :type max_value: Depending on the class
        :type description: str
        :return: A data socket
        :rtype: As defined by class_name
        
        .. code-block:: python
        
            res = tree.new_input('Integer', 10, "Resolution", min_value=2, max_value=100, descriptioo="Grid resolution")
        
        Don't use it directly, better call the constructor ``Input`` of data classes.
        
        .. code-block:: python
        
            res = Integer.Input(10, "Resolution", min_value=2, max_value=100, descriptioo="Grid resolution")
            
        """
        return self.group_input.new_socket(class_name=class_name, value=value, name=name, min_value=min_value, max_value=max_value, description=description)
    
    def to_output(self, socket):
        """ Create a new output socket linked to the data class.
        
        :param socket: The data socket to plug as group output
        :type socket: DataSocket

        .. code-block:: python
        
            tree.to_output(value)
        
        Don't use it directly, better call method ``to_output`` of data classes.
        
        .. code-block:: python
        
            value.to_output()

        """
        self.group_output.to_output(socket)
        
    # ----------------------------------------------------------------------------------------------------
    # Viewer
    
    def view(self, geometry=None, socket=None):
        """ Connect a data socket to the viewer.
        
        :param geometry: The geometry to connect to the viewer
        :param socket: The attribute to connect to the viewer
        :type geometry: Geometry
        :type socket: Value
        
        You can also call ``DataSocket.view()``
        
        The `Tree.view` method reuses the Viewer node if already exists.
        """
        
        if self.viewer is None:
            self.viewer = Viewer()
            
        self.viewer.plug_socket(geometry)
        self.viewer.plug_socket(socket)
        
    # ----------------------------------------------------------------------------------------------------
    # Scene
    
    @property
    def scene(self):
        """ Maintain a single instance of the node :class:`SceneTime`.
        """
        if self.scene_ is None:
            self.scene_ = SceneTime()
        return self.scene_
        
    @property
    def frame(self):
        """ The "Scene Time" output socket "frame".
        
        Used for animation:

        .. code-block:: python
        
            with Tree("Geometry Nodes") as tree:
                height = tree.frame / 10 # a value which is a tenth of the current frame 
            
        """
        return self.scene.frame
    
    @property
    def seconds(self):
        """ The "Scene Time" output socket "seconds".
        
        Used for animation:
            
        .. code-block:: python
        
            with Tree("Geometry Nodes") as tree:
                time = tree.seconds.sqrt() # a value which is the square root of the time

        """
        return self.scene.seconds

    # ----------------------------------------------------------------------------------------------------
    # Layouts
    
    @contextmanager
    def layout(self, label="Layout", color=None):
        """ Create a new layout where the newly created nodes will be placed.
        
        :param label: The layout label
        :param color: The color of the layout
        :type label: str
        :type color: triplet, str or mathutils.Color
        
        To be used in a `with` block:
            
        .. code-block:: python
        
            with tree.layout("My layout"): # Create a layout
                mesh = Mesh.UVSphere() # The node is parented in the layout
                
            mesh.set_shade_smooth() # "Set Shade Smooth" node is created in the tree backrgound

        """
        
        if isinstance(color, str):
            if color.upper() == 'UTIL':
                color = self.util_color
            elif color.upper() == 'GENE':
                color = self.gene_color
            elif color.upper() == 'AUTO':
                color = self.auto_color
        
        try:
            layout = Frame(label=label, color=color)
            self.layouts.append(layout)
            yield layout
        finally:
            self.layouts.pop()
            
    @property
    def cur_frame(self):
        """ Get the current layout for the newly created nodes.
        """
        if self.layouts:
            return self.layouts[-1].bnode
        else:
            return None
    
    # ----------------------------------------------------------------------------------------------------
    # Check attributes
    
    def check_attributes(self):
        """ Check the attributes
        
        This utility function is called when closing the tree to "solve" the attribute input nodes,
        i.e. to determine if a 'Capture Attribute' node is required.
        
        In **geonodes**, attributes are initialized as properties of a geometry.
        For instance, in the following piece of code, the node 'Position' is to be the *position*
        of the vertices of my_mesh:
            
        .. code-block:: python
        
            v = my_mesh.verts.position  # Create the node 'Position'
            
        To actually get these vertices, a 'Capture Attribute' can be necessary. This is determined
        by `check_attribute` method.
        
        The insertion is made with the following algorithm
        
        1. Check if capture is needed
        
           for each fed node:
               
           - if the node has an input geometry:
               
             - if the input geometry is the expected one:
                 
               - ok
               
             - else
             
               - insertion is needed
               
           - else:
               
             - continue exploration with the nodes fed by this node
        
        2. If insertion is needed
        
           - Create the 'Capture Attribute' node
           - Set the proper parameters
           - Input geometry with the owning socket
           - Output geometry to the sockets the owning socket was linked to
           - Output attribute to the sockets the attribute was connected to
           
         
        Note that by initializing an attribute with geometry and domain, we have what we need to insert
        a 'Capture Attribute' node:
            
        .. code-block:: python
        
            # Get the position of the vertices of my_mesh
        
            v = my_mesh.verts.position
            
            # Create the capture node
            
            capture_node = nodes.CaptureNode(
                geometry  = my_mesh,
                value     = (output socket of Position node),
                data_type = 'VECTOR',  # We deal with position which is a Vector
                domain    = 'POINT',   # my_mesh.verts.position  --> 'POINT'
                                       # my_mesh.edges.position  --> 'EDGE'
                                       # my_mesh.faces.position  --> 'FACE'
                )
           
        """
        
        
        from geonodes import Geometry
        
        attr_nodes = []
        for node in self.nodes:
            if node.is_attribute:
                attr_nodes.append(node)
                
        for attr_node in attr_nodes:
            
            # ---------------------------------------------------------------------------
            # ----- Check if the fed nodes with geometry input are ok
            
            security  = []
            def check_geo_nodes(node):
                for nd in node.fed_nodes:
                    
                    bsocket = nd.input_geometry_bsocket

                    logging.debug("CHECKING", attr_node, nd, '-->', bsocket)

                    if bsocket is None:
                        if nd in security:
                            continue
                        
                            #attr_node.node_color = "red"
                            #node.node_color = "red"
                            #nd.node_color = "red"
                            #raise RuntimeError(f"Error when checking the attribute node {attr_node}, apparently, the tree loops on node {nd} {nd.bnode}")
                        security.append(nd)
                        
                        if not check_geo_nodes(nd):
                            return False
                        
                    else:
                        
                        # ----- Normally one single input
                        
                        for link in bsocket.links:
                            if link.from_socket != attr_node.owning_bsocket:
                                return False
                
                return True
            
                        
            if check_geo_nodes(attr_node):
                continue
            
            # ---------------------------------------------------------------------------
            # ----- A capture node is required
            
            # ----- Store the links to reroute
            
            # Geometry
            
            geo_links  = attr_node.owning_bsocket.links
            
            # Attribute
            
            attr_links   = None
            output_index = 0
            for index, bsocket in enumerate(attr_node.bnode.outputs):
                links = bsocket.links
                if links:
                    if attr_links is not None:
                        self.arrange()
                        attr_node.node_color = "red"
                        raise RuntimeError(f"Error when inserting a capture node. The attribute node '{attr_node}' has several output sockets which are connected.")
                        
                    attr_links   = links
                    output_index = index
                
            if attr_links is None:
                raise RuntimeError("Algo error !")
                
            # ----- Capture node creation in the proper frame
            
            data_type = DataSocket.SOCKET_IDS[attr_node.bnode.outputs[output_index].bl_idname][2]
            
            print("CAPTURE", attr_node.domain)
            
            capt_node = Geometry(attr_node.owning_bsocket).capture_attribute(value=attr_node.outputs[output_index], data_type=data_type, domain=attr_node.domain)
            capt_node.bnode.parent = attr_node.bnode.parent
            
            # ----- Links rerouting
            
            # Geometry
            
            for link in geo_links:
                to_socket = link.to_socket
                self.btree.links.remove(link)
                self.btree.links.new(capt_node.bnode.outputs[0], to_socket)
                
            # Attribute
            
            for index, bsocket in enumerate(capt_node.bnode.outputs):
                if index > 0 and bsocket.enabled:
                    out_bsocket = bsocket
                    break
            
            for link in attr_links:
                to_socket = link.to_socket
                self.btree.links.remove(link)
                self.btree.links.new(out_bsocket, to_socket)
                        
     
    # ---------------------------------------------------------------------------
    # Get the parameter previously changed in a node
    
    def prev_node(self, index):
        """ Utility which prints the configuration of a node in the console.
        
        :param index: The unique id of the node to print
        :type index: int
        
        When a node is tweaked to obtain the expected result, the changes will be lost
        next time the script will be run. By calling `prev_node` the parameters are printed
        in the console and can be copied/pasted.
    
        """
        onode = self.previous.get(index)
        if onode is None:
            print(f"No previous node with index {index}")
        else:
            print(f"Previous node {onode.name}:\n{onode.args}\n")
    
    # ----------------------------------------------------------------------------------------------------
    # Arrange the nodes
    
    def arrange(self):
        """ Arrange the created nodes in the tree background for more lisibility
        """ 
        arrange(self.btree.name)    

    # ----------------------------------------------------------------------------------------------------
    # Close the tree
    #
    # Called by __exit__
    
    def close(self):
        """ Call to indicate that the tree is completed and that it can be finalized
        
        Two actions are performed:
            
        - Insertion of "Capture Attribute" nodes for attributes which require it,
          see :func:`check_attributes`.
        - Nodes arrangement, see :func:`arrange`.   
                                           
        """
        if self.capture_attributes:
            self.check_attributes()
            
        self.arrange()

    
# ---------------------------------------------------------------------------
# A Node    

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
        
    def __init__(self, bl_idname, name, label=None, node_color=None):
        
        self.tree = Tree.TREE
        """ The tree belonging the node."""
        
        self.tree.register_node(self)

        self.name    = name
        """ Node name"""
        self.label_  = None
        if bl_idname == 'GeometryNodeGroup':
            self.bnode = self.tree.get_bnode(bl_idname, name)
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
        
        # ----- Set by method as_attribute
        
        self.is_attribute = False
        """ Initialized by method :func:`as_attribute`. Will be analyzed by :func:`check_attributes` to complete the Tree."""
        
        # ----- Set by field for all output sockets
        
        self.field_of = None
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
        
    # ------------------------------------------------------------------------------------------
    # Access to the output sockets
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
            ds.field_of = self.field_of
            return ds

    # ------------------------------------------------------------------------------------------
    # Access to the input sockets
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
        return f"{self.node_id:2d} {self.name}" if self.label_ is None else f"{self.node_id:2d} {self.label_}"
    
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
        
        DataSocket.plug_bsocket(self.bnode.inputs[index], *values)
        
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
    
    def as_attribute(self, owning_socket, domain='POINT'): #, data_type='FLOAT'):
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
        
        self.is_attribute = True
        if isinstance(owning_socket, bpy.types.NodeSocket):
            self.owning_bsocket = owning_socket
        else:
            self.owning_bsocket = owning_socket.bsocket
        self.domain = domain
        
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
    
    """
    @staticmethod
    def DataSocket(socket):
        if socket.bl_idname == 'NodeSocketBool':
            return Node.Boolean(socket)
        
        elif socket.bl_idname == 'NodeSocketInt':
            return Node.Integer(socket)
        
        elif socket.bl_idname == 'NodeSocketIntUnsigned':
            return Node.Integer(socket)
        
        elif socket.bl_idname == 'NodeSocketFloat':
            return Node.Float(socket)
        
        elif socket.bl_idname == 'NodeSocketFloatFactor':
            return Node.Float(socket)
        
        elif socket.bl_idname == 'NodeSocketFloatAngle':
            return Node.Float(socket)
        
        elif socket.bl_idname == 'NodeSocketFloatDistance':
            return Node.Float(socket)
        
        elif socket.bl_idname == 'NodeSocketVector':
            return Node.Vector(socket)
        
        elif socket.bl_idname == 'NodeSocketVectorEuler':
            return Node.Vector(socket)
        
        elif socket.bl_idname == 'NodeSocketVectorXYZ':
            return Node.Vector(socket)
        
        elif socket.bl_idname == 'NodeSocketVectorTranslation':
            return Node.Vector(socket)
        
        elif socket.bl_idname == 'NodeSocketColor':
            return Node.Color(socket)
        
        elif socket.bl_idname == 'NodeSocketString':
            return Node.String(socket)
        
        elif socket.bl_idname == 'NodeSocketGeometry':
            return Node.Geometry(socket)
        
        elif socket.bl_idname == 'NodeSocketCollection':
            return Node.Collection(socket)
        
        elif socket.bl_idname == 'NodeSocketImage':
            return Node.Image(socket)
        
        elif socket.bl_idname == 'NodeSocketMaterial':
            return Node.Material(socket)
        
        elif socket.bl_idname == 'NodeSocketObject':
            return Node.Object(socket)
        
        elif socket.bl_idname == 'NodeSocketTexture':
            return Node.Texture(socket)
        
        raise RuntimeError(f"Unknown bl_idname for socket '{socket.name}': '{socket.bl_idname}'")
    """
    
    @staticmethod
    def Boolean(socket):
        """ Initialize a Boolean with a DataSocket"""
        import geonodes as gn
        return gn.Boolean(socket)
    
    @staticmethod
    def Integer(socket):
        """ Initialize a Integer with a DataSocket"""
        import geonodes as gn
        return gn.Integer(socket)
    
    @staticmethod
    def Float(socket):
        """ Initialize a Float with a DataSocket"""
        import geonodes as gn
        return gn.Float(socket)
    
    @staticmethod
    def Vector(socket):
        """ Initialize a Vector with a DataSocket"""
        import geonodes as gn
        return gn.Vector(socket)
    
    @staticmethod
    def Color(socket):
        """ Initialize a Color with a DataSocket"""
        import geonodes as gn
        return gn.Color(socket)
    
    @staticmethod
    def String(socket):
        """ Initialize a String with a DataSocket"""
        import geonodes as gn
        return gn.String(socket)
    
    @staticmethod
    def Geometry(socket):
        """ Initialize a Geometry with a DataSocket"""
        import geonodes as gn
        return gn.Geometry(socket)
    
    @staticmethod
    def Curve(socket):
        """ Initialize a Curve with a DataSocket"""
        import geonodes as gn
        return gn.Curve(socket)
    
    @staticmethod
    def Mesh(socket):
        """ Initialize a Mesh with a DataSocket"""
        import geonodes as gn
        return gn.Mesh(socket)
    
    @staticmethod
    def Points(socket):
        """ Initialize a Points with a DataSocket"""
        import geonodes as gn
        return gn.Points(socket)
    
    @staticmethod
    def Instances(socket):
        """ Initialize a Instances with a DataSocket"""
        import geonodes as gn
        return gn.Instances(socket)
    
    @staticmethod
    def Volume(socket):
        """ Initialize a Volume with a DataSocket"""
        import geonodes as gn
        return gn.Volume(socket)
    
    @staticmethod
    def Texture(socket):
        """ Initialize a Texture with a DataSocket"""
        import geonodes as gn
        return gn.Texture(socket)
    
    @staticmethod
    def Material(socket):
        """ Initialize a Material with a DataSocket"""
        import geonodes as gn
        return gn.Material(socket)
    
    @staticmethod
    def Image(socket):
        """ Initialize a Image with a DataSocket"""
        import geonodes as gn
        return gn.Image(socket)
    
    @staticmethod
    def Collection(socket):
        """ Initialize a Collection with a DataSocket"""
        import geonodes as gn
        return gn.Collection(socket)
    
    @staticmethod
    def Object(socket):
        """ Initialize a Object with a DataSocket"""
        import geonodes as gn
        return gn.Object(socket)       
    
    @staticmethod
    def DataClass(socket):
        """ Initialize a DataClass of the propert class from from the bl_idname of the socket"""
        class_name = DataSocket.get_class_name(socket)
        return getattr(Node, class_name)(socket)
        
    
# =============================================================================================================================
# Node groups
#
# Node groups are
# - user groups with inuts and outputs
# - input group with only outputs
# - output group with only inputs
#
# Since the inputs are outputs these three classes need initializers for the socket names

# ----------------------------------------------------------------------------------------------------
# Root for node groups

class CustomGroup(Node):
    """ > Root for the three types of groups
    
    Build the insockets and outsockets dictionaries
    """
    
    def __init__(self, bl_idname, name, label=None, node_color=None):
        
        super().__init__(bl_idname, name, label=label, node_color=node_color)
        
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
        
        if name in dct:
            if prefix is None:
                pref_name = name
            else:
                pref_name = f"{prefix} {name}"
        else:
            return name
            
        uname = pref_name
        for i in range(100): # Should be enough :-)
            if uname in dct:
                uname = f"{pref_name} {i}"
            else:
                return uname
            
        raise RuntimeError(f"You have so many sockets named '{pref_name}' that we have to stop that!")

# ----------------------------------------------------------------------------------------------------
# A node group

class Group(CustomGroup):
    """ > Node group
    
    Node groups are dynamically built by reading the input and output sockets of the group.
    
    Input sockets are initialized in the keyword arguments.
    
    They can later on be initialized by the snake_case names
    """
    
    def __init__(self, name, **kwargs):
        
        if bpy.data.node_groups.get(name) is None:
            raise RuntimeError(f"The node group '{name}' doesn't exist")
        
        label, node_color = kwargs.get('label'), kwargs.get('node_color')
        if label is not None:
            a.pop('label')
        if node_color is not None:
            a.pop('node_color')
        
        super().__init__('GeometryNodeGroup', name, label=label, node_color=node_color)

        # But let's plug the values directly 
        
        for k, v in kwargs.items():
            index = self.insockets.get(k.lower())
            if index is None:
                raise AttributeError(f"The node group '{name}' has no input socket named '{k}'.")
            self.plug(k, v)

    
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
                    while len(self.tree.btree.inputs) > 0 and self.tree.btree.inputs[0].bl_idname != 'NodeSocketVirtual':
                        self.tree.btree.inputs[0].remove(0)
                
                self.tree.btree.inputs.new(type='NodeSocketGeometry', name="Geometry")
                self.build_insockets()
        
        
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
                    if bsock.name == "Geometry":
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
        
        if name is None:
            name = class_name
            
        # ----- Look for an existing socket with the proper name
        
        socket    = None
        existing  = False
        for socket_index, bsocket in enumerate(self.bnode.outputs):
            
            # No virtual socket
            if bsocket.bl_idname == 'NodeSocketVirtual':
                continue
            
            cname, subclass = DataSocket.get_class_name(bsocket, True)
            if (cname == class_name or subclass == class_name) and bsocket.name == name:
                
                inp = self.tree.btree.inputs[socket_index]
                
                socket = Node.DataClass(bsocket)
                existing = True
                
                if min_value is not None and inp.min_value != min_value:
                    inp.min_value = min_value

                if max_value is not None and inp.max_value != max_value:
                    inp.max_value = max_value

                if inp.description != description:
                    inp.description = description
                    
                break
            
        # ----- Let's create it
            
        if socket is None:
            
            # ----- The name can be uses by other sockets which don't have the same class !
            
            name = CustomGroup.unique_socket_name(name, self.outsockets, prefix=class_name)
                
            # ----- Let's create the input
            
            new_input = self.tree.btree.inputs.new(type=DataSocket.get_bl_idname(class_name), name=name)
            
            if min_value is not None:
                new_input.min_value = min_value
                
            if max_value is not None:
                new_input.max_value = max_value
                
            new_input.description = description
            
            self.build_outsockets()
            
            sc_name = self.snake_case(name)
            index  = self.outsockets[sc_name]
            socket = getattr(self, sc_name)
            
            
        # ----- Let's set the value
        # Note: if the socket already exists, we don't override its value
        
        if value is not None:
            
            if Socket.is_socket(value):
                value.plug(socket)
                
            elif not existing:
                
                if class_name == 'Vector':
                    if hasattr(value, '__len__'):
                        if len(value) == 4:
                            value = mathutils.Vector((value[0], value[1], value[2]))
                        else:
                            value = mathutils.Vector(value)
                    else:
                        value = mathutils.Vector((value,)*3)
                
                elif class_name == 'Color':
                    if hasattr(value, '__len__'):
                        if len(value) == 3:
                            value = value + (1,)
                    else:
                        value = Vector((value,)*3 + (1,))
                
                msg = None
                try:
                    self.tree.btree.inputs[index].default_value = value
                    socket.bsocket.default_value = value
                    
                except Exception as e:
                    msg = str(e)
                    
                if msg is not None:
                    raise RuntimeError(f"Impossible to set the default value '{value}' to the group input socket '{name}'.\n {msg}")
                    
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
                                mod[new_input.identifier] = value
                                
        # ----- Return the newly created socket
        
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
                    while len(self.tree.btree.outputs) > 0 and self.tree.btree.outputs[0].bl_idname != 'NodeSocketVirtual':
                        self.tree.btree.outputs.remove(0)
                        
                self.tree.btree.outputs.new(type='NodeSocketGeometry', name="Geometry")
                self.build_insockets()
        
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
                    
                self.bnode.inputs.move(index, 0)
                logger.error("GEONODES> Blender error: the method 'inputs.move' doesn't work. You must move yourself the outputs geometry in first position...")
                
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
        
        index  = self.outsockets[name]
        self.plug(index, socket)
        
# =============================================================================================================================
# Unique nodes        

# ----------------------------------------------------------------------------------------------------
# Node NodeViewer for GeometryNodeViewer

class Viewer(Node):
    """ Node *Viewer*
    
    Args:
        geometry: The geometry to view
        value: The value to view
        data_type: The value data_type in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']

        
    .. blid:: GeometryNodeViewer

    """

    def __init__(self, geometry: DataSocket = None, value: Any = None, data_type: str = 'FLOAT', label: str = None):

        super().__init__('GeometryNodeViewer', name='Viewer', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        
        self.insockets  = {'geometry': 0, 'value': [1, 2, 3, 4, 5]}
        
        self.geometry = geometry
        self.value    = value

        
    def plug_socket(self, socket: DataSocket):
        """ Plug a socket into the viewer.
        
        Args:
            socket: The data socket to plug
            
        """
        
        if socket is None:
            return
        
        class_name = DataSocket.get_class_name(socket, False)
        
        if class_name in ['Geometry', 'Mesh', 'Curve', 'Spline', 'Points', 'Volume', 'Instances']:
            self.geometry = socket
        
        else:
            if class_name == 'Boolean':
                self.bnode.data_type = 'BOOLEAN'
                
            elif class_name == 'Integer':
                self.bnode.data_type = 'INT'
                
            elif class_name == 'Float':
                self.bnode.data_type = 'FLOAT'
                
            elif class_name == 'Vector':
                self.bnode.data_type = 'FLOAT_VECTOR'
                
            elif class_name == 'Color':
                self.bnode.data_type = 'FLOAT_COLOR'
                
            else:
                raise RuntimeError(f"Impossible to connect the socket {socket} to the viewer. Class {class_name} is not viewable.")
                
            self.value = socket
        
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

        super().__init__('NodeFrame', name='Frame', label=label)
        if color is None:
            color = colors.next_color()
        self.node_color = color

        # Parameters

        self.bnode.label_size      = label_size
        self.bnode.shrink          = shrink
        
    def get_label(self):
        """ Build the node label
        
        If the label provided at initialization time is None, the node is labeled by concatening
        its unique id with its standard name.
        """
        return f"{self.node_id:2d} {self.name}" if self.label_ is None else f"{self.label_}"
        
        
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

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time', label=label)

        # Output sockets

        self.outsockets = {'seconds': 0, 'frame': 1}
        
        

        
        
        
        
        
        
    
    
        