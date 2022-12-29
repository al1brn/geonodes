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

from geonodes.core import context

import bpy

# =============================================================================================================================
# Socket wrapper
#
# Root class for DataSocket and Domain

class Socket:
    """ Socket root class
    
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
        """
        Args:
            - socket (bpy.types.SocketNode): the socket to wrap
            - node (Node): the belonging node
        """
        
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
                self.node = context.tree.TREE.get_bnode_wrapper(self.bsocket.node)
            else:
                self.node = node
                
        # ----- Specific initialization
        
        self.init_socket()
        
        
    def __str__(self):
        
        if self.node is None:
            return f"<Socket {type(self).__name__} '{self.name}' on None Node>"
        
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
        
        Args:
            - value (any): The value to test
            
        Returns:
            is a socket (bool)
        """
        return hasattr(value, 'get_blender_socket')

    
    @staticmethod
    def is_vector(value):
        """ Determine is the parameter is a vector.
        
        Args:
            - value (any): The value to test
            
        Returns:
            is a socket (bool)
        """
        
        if Socket.is_socket(value):
            return Socket.get_class_name(value) in ['Vector', 'Color']
        
        elif hasattr(value, '__len__'):
            return True
        
        else:
            return False
    
    @staticmethod
    def gives_bsocket(value):
        """ Test if the argument provides a valid output socket.
        
        Args:
            - value (any): The value to test
            
        Returns:
            value is bpy.types.NodeSocket or Socket (bool)
        """
        
        return Socket.is_socket(value) or isinstance(value, bpy.types.NodeSocket)

    # ----------------------------------------------------------------------------------------------------
    # Is it an group input socket
    
    @property
    def is_input_socket(self):
        return self.node is not None and self.node.bl_idname == 'NodeGroupInput'
    
    def new_node(self):
        if self.is_input_socket:
            return GroupInput(check_input_geometry=False)
        else:
            return None

    def new_instance(self, node=None):
        if node is None:
            node = self.new_node()
            
        if node is None:
            return self
        else:
            return type(self)(node.outputs[self.socket_index])
    
    # ----------------------------------------------------------------------------------------------------
    # The Blender socket is used to link nodes
    # Rather than accessing it directly, one must use the method get_blender_socket
    # This method can be used to implement specific code before connection
    
    def get_blender_socket(self):
        """ Returns the property bsocket.
        
        Returns:
            bsocket (bpy.types.NodeSocket)
        """
        
        return self.bsocket
    
    @property
    def bl_idname(self):
        """ Shortcut for `self.bsocket.bl_idname`
        
        Returns:
            socket bl_idname (str)
        """
        return self.bsocket.bl_socket_idname if isinstance(self.bsocket, bpy.types.NodeSocketInterfaceGeometry) else self.bsocket.bl_idname
    
    @property
    def name(self):
        """ Shortcut for `self.bsocket.name`
        
        Returns:
            socket name (str)
        """
        return self.bsocket.name
        
    @property
    def is_output(self):
        """ Shortcut for `self.bsocket.is_output`
        
        Returns:
            is an aoutput socket (bool)
        """
        return self.bsocket.is_output
    
    @property
    def is_multi_input(self):
        """ Shortcut for `self.bsocket.is_multi_output`
        
        Returns:
            is multi input socket (bool)
        """
        return self.bsocket.is_multi_output
    
    @property
    def links(self):
        """ Shortcut for `self.bsocket.links`      
        
        Returns:
            list of links (list)
        """
        return self.bsocket.links

    @property
    def bnode(self):
        """ Shortcut for `self.bsocket.node`
        
        Returns:
            Blender node (bpy.types.Node)
        """
        return self.bsocket.node
    
    @property
    def socket_index(self):
        """ Return the index of the socket within the list of node sockets.
        
        Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
        *node.outputs*.
        
        Returns:
            socket index (int)
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
        
        Returns:
            list of connected sockets (list of Sockets)
        """ 
        
        sockets = []
        for link in self.links:
            if self.is_output:
                bsocket = link.to_socket
            else:
                bsocket = link.from_socket
            sockets.append(self.node.tree.get_bsocket_wrapper(bsocket))
        return sockets
    
    @property
    def is_plugged(self):
        """ Indicates if the socket is connected or not.
        
        Raise an exception if called on an output socket.
        
        Returns:
            is plugged (bool)
        """
        if self.is_input:
            return bool(self.connected_sockets)
        else:
            raise Exception(f"No 'is_plugged' property for output sockets: {self}")
    
    # ----------------------------------------------------------------------------------------------------
    # Data type from 
    
    @staticmethod
    def value_data_type(value, default='FLOAT', color='FLOAT_COLOR'):
        """ Returns the data type to which the socket belongs.
        
        This methods is used to compute the **data_type** value in nodes accepting multitype values.
        
        |    Socket                     |    data_type    |
        |-------------------------------|-----------------|
        | NodeSocketBool                | 'BOOLEAN'       |
        | NodeSocketInt                 | 'INT'           |
        | NodeSocketIntUnsigned         | 'INT'           |
        | NodeSocketFloat               | 'FLOAT'         |
        | NodeSocketFloatFactor         | 'FLOAT'         |
        | NodeSocketFloatAngle          | 'FLOAT'         |
        | NodeSocketFloatDistance       | 'FLOAT'         |
        | NodeSocketVector              | 'FLOAT_VECTOR'  |
        | NodeSocketVectorEuler         | 'FLOAT_VECTOR'  |
        | NodeSocketVectorXYZ           | 'FLOAT_VECTOR'  |
        | NodeSocketVectorTranslation   | 'FLOAT_VECTOR'  |
        | NodeSocketColor               | color           |                
        
        Args:
            - value (any): the value to analyze
            - default (str): default data_type
            - color (str): code for color data_type
            
        Returns:
            the data type of the value

        """
        
        class_dt = {
            'Boolean' : 'BOOLEAN',
            'Integer' : 'INT',
            'Float'   : 'FLOAT',
            'Vector'  : 'FLOAT_VECTOR',
            'Color'   : color
            }
        
        if value is None:
            return default
        
        elif isinstance(value, str):
            if value in Socket.SOCKET_IDS:
                return Socket.SOCKET_IDS[socket.bl_idname][2]
            
            elif value in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN'):
                return value
            
            elif value in ['FLOAT_COLOR', 'BYTE_COLOR']:
                return color
            
            elif value in class_dt:
                return class_dt[value]
            
        else:
            cname = type(value).__name__
            if cname in class_dt:
                return class_dt[cname]
            
            if hasattr(value, 'bl_idname'):
                return Socket.SOCKET_IDS[value.bl_idname][2]
            
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
                    return color
                
    # ----------------------------------------------------------------------------------------------------
    # Convert a python value to a type matching the one of the socket
    
    @staticmethod
    def python_type_to_socket(value, bl_idname, raise_exception=True):
        """ Convert a python value to a value which can be plug in the socket.
        
        The following table gives the conversion rules:
            
        | Socket type       | Conversion                                                    |
        |-------------------|---------------------------------------------------------------|
        | Boolean           | bool(value)                                                   |
        | Integer           | int(value)                                                    |
        | Float             | float(value)                                                  |
        | Vector            | A triplet or the value if compatible (mathutils.Vector,...)   |
        | Color             | A quadruplet or the value if compatible (mathutils.Color,...) |
        | String            | str(value)                                                    |
        | Collection        | value is value is a collection, bpy.data.collections[value] otherwise |
        | Object            | value is value is an object, bpy.data.objects[value] otherwise        |
        | Image             | value is value is an image, bpy.data.images[value] otherwise          |
        | Texture           | value is value is a texture, bpy.data.textures[value] otherwise       |
        | Material          | value is value is a material, bpy.data.materials[value] otherwise     |
        
        This method allows in particular to refer to Blender resources by their name:
            
        ```python
        # Set a material to a mesh
        mesh.faces.material = "Material"
        
        # Is equivalent to
        mesh.faces.material = bpy.data.materials["Material"]
        ```
        
        Args:
            value (any): the value to convert
            bl_idname (str): the socket bl_idname
            raise_exception (bool): False to avod raising an exception in case of error.
        """
        
        import bpy.types
        import mathutils
        
        if value is None:
            return None
        
        if bl_idname == 'NodeSocketBool':
            return bool(value)
        
        elif bl_idname in ['NodeSocketInt', 'NodeSocketIntUnsigned']:
            return int(value)
        
        elif bl_idname in ['NodeSocketFloat', 'NodeSocketFloatFactor', 'NodeSocketFloatAngle', 'NodeSocketFloatDistance']:
            return float(value)
        
        elif bl_idname in ['NodeSocketVector', 'NodeSocketVectorEuler', 'NodeSocketVectorXYZ', 'NodeSocketVectorTranslation']:
            if isinstance(value, (mathutils.Vector, mathutils.Euler)):
                return value
            
            if hasattr(value, '__len__'):
                if len(value) == 1:
                    return (value[0],)*3
                elif len(value) == 4:
                    return tuple(value[:3])
                else:
                    return value
            else:
                return (value,)*3
        
        elif bl_idname == 'NodeSocketColor':

            if isinstance(value, mathutils.Color):
                return value
            
            if hasattr(value, '__len__'):
                if len(value) == 1:
                    return (value[0],)*4
                elif len(value) == 3:
                    return value + (1,)
                else:
                    return value
            else:
                return (value,)*4
        
        elif bl_idname == 'NodeSocketString':
            return str(value)
        
        elif bl_idname == 'NodeSocketCollection':
            if isinstance(value, bpy.types.Collection):
                return value
            
            obj = bpy.data.collections.get(value)
            if obj is None and raise_exception:
                raise Exception(f"Collection named '{value}' not found.")
            return obj
        
        elif bl_idname == 'NodeSocketImage':
            if isinstance(value, bpy.types.Image):
                return value
            
            obj = bpy.data.images.get(value)
            if obj is None and raise_exception:
                raise Exception(f"Image named '{value}' not found.")
            return obj
        
        elif bl_idname == 'NodeSocketMaterial':
            if isinstance(value, bpy.types.Material):
                return value
            
            obj = bpy.data.materials.get(value)
            if obj is None and raise_exception:
                raise Exception(f"Material named '{value}' not found.")
            return obj
        
        elif bl_idname == 'NodeSocketObject':
            if isinstance(value, bpy.types.Object):
                return value
            
            obj = bpy.data.objects.get(value)
            if obj is None and raise_exception:
                raise Exception(f"Object named '{value}' not found.")
            return obj
        
        elif bl_idname == 'NodeSocketTexture':
            if isinstance(value, bpy.types.Texture):
                return value
            
            obj = bpy.data.textures.get(value)
            if obj is None and raise_exception:
                raise Exception(f"Texture named '{value}' not found.")
            return obj
        
        elif bl_idname == 'NodeSocketGeometry':
            if raise_exception:
                raise Exception(f"Impossible to convert {value} to a geometry socket value")
            return None
        
        else:
            raise Exception(f"Impossible to initialize socket '{self.name}' of type {self.bl_idname} with value {value}.")
                
                
    # ----------------------------------------------------------------------------------------------------
    # Convert a python value to a type matching the one of the socket
    # Doesn't take DataSocket as input
    # Used in socket input when exact matching is required
    
    def convert_python_type(self, value, raise_exception=True):
        return self.python_type_to_socket(value, self.bl_idname, raise_exception=raise_exception)

    # ----------------------------------------------------------------------------------------------------
    # Class name from socket bl_idname
    
    @staticmethod
    def get_class_name(socket, with_sub_class = False):
        """ Get the DataSocket class name corresponding to the socket type and name.
        
        | Socket bl_idname              | Geondes class name    | Sub class             |
        |-------------------------------|-----------------------|-----------------------|
        | NodeSocketBool                | Boolean               | None                  |
        | NodeSocketInt                 | Integer               | None                  |
        | NodeSocketIntUnsigned         | Integer               | NoUnsigned            |
        | NodeSocketFloat               | Float                 | None                  |
        | NodeSocketFloatFactor         | Float                 | Factor                |
        | NodeSocketFloatAngle          | Float                 | Angle                 |
        | NodeSocketFloatDistance       | Float                 | Distance              |
        | NodeSocketVector              | Vector                | None                  |
        | NodeSocketVectorEuler         | Vector                | Rotation              |
        | NodeSocketVectorXYZ           | Vector                | xyz                   |
        | NodeSocketVectorTranslation   | Vector                | Translation           |
        | NodeSocketColor               | Color                 | None                  |
        | NodeSocketString              | String                | None                  |
        | NodeSocketCollection          | Collection            | None                  |
        | NodeSocketImage               | Image                 | None                  |
        | NodeSocketMaterial            | Material              | None                  |
        | NodeSocketObject              | Object                | None                  |
        | NodeSocketTexture             | Texture               | None                  |
        | NodeSocketGeometry            | Geometry              | None                  |
        
        If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
        the name is chosen as the class name.
        
        Args:
            - socket (bpy.type.NodeSocket): the socket to use
            - with_sub_class (bool): return as as second value the sub type of the socket
                
        """
        bl_idname = socket.bl_idname
        class_name = Socket.SOCKET_IDS[bl_idname][0]
        name = socket.name
        
        if class_name == 'Geometry' and name in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve']:
            class_name = name
            
        if class_name == 'Curves':
            class_name = 'Curve'
            
        if name == 'Point Cloud':
            class_name = 'Points'
            
        if with_sub_class:
            return class_name, Socket.SOCKET_IDS[bl_idname][1]
        else:
            return class_name
        
    @staticmethod
    def get_bl_idname(class_name):
        """ Get the node socket bl_idname name from the Socket class

        Used to create a new group input socket. Called in `DataClass.Input` method to determine
        which socket type must be created.
        
        Note that here the class_name argument accepts additional values which correspond to **sub classes**:
            
        | Sub class                 | bl_idname                     |
        |---------------------------|-------------------------------|
        | Unsigned                  | NodeSocketIntUnsigned         |
        | Factor                    | NodeSocketFloatFactor         |
        | Angle                     | NodeSocketFloatAngle          |
        | Distance                  | NodeSocketFloatDistance       |
        | Rotation                  | NodeSocketVectorEuler         |
        | xyz                       | NodeSocketVectorXYZ           |
        | Translation               | NodeSocketVectorTranslation   |
          
        These additional values allow to enter angle, distance, factor... as group input values.
        
        Args:
            - class_name (str): the name of the class
            
        Returns:
            bl_idname (str)
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
    """ Wrapper of a node socket.
    
    **DataSocket** represents the data (Geometry, Value, String, Material...) associated to a node socket.
    
    **DataSocket** is the base class for actual data sockets:
    - [Geometry](Geometry.md)
    - [Boolean](Boolean.md)
    - [Integer](Integer.md)
    - [Float](Float.md)
    - [Vector](Vector.md)
    - [Color](Color.md)
    - [String](String.md)
    - [Collection](Collection.md)
    - [Object](Object.md)
    - [Material](Material.md)
    - [Texture](Texture.md)
    - [Image](IMage.md)
        
    **DataSockets** are created by input nodes, for instance, in the following example, `cube` is a **Mesh** **DataSocket**
    wrapping the output socket of the Blender Node *'Cube'*:    
        
    ```python
    cube = Mesh.Cube()
    ```
    
    Some methods change the node socket wrapped by the **DataSocket** instance. For instance, in the following example
    the `cube` **DataSocket**:
    - before the call, wraps the output socket of the Blender Node *'Cube'*
    - after the call, wraps the output socket of the Blender Node *'Set Shade Smooth'*
        
    ```python
    cube.set_shade_smooth(True)
    ```
    
    Some methods return a new **DataSocket** instance:
        
    ```python
    volume = cube.to_volume()
    ```
    
    ### Attributes
    
    Attribute **DataSockets** keep a reference to the geometry they are an attribute of. By analyzing, the use
    of attribute sockets, it is possible to automatically generate a *'Capture Attribute'* node when necessary.
    
    In the example below, the `index` variable of type [Integer](Integer.md) (a sub class of **DataSocket**) keeps
    a reference of the `cube` geometry as being the geometry it is the index of (also see [Domain](Domain.md) for
    the `verts` property):
        
    ```python
    index = cube.verts.index
    ```
    
    Depending on how `index` will be used, a 'Capture Attribute' node will be generated on the `cube` wrapped
    socket if necessary.
    """

    def __init__(self, socket, node=None, label=None):
        """
        Args:
            - socket (bpy.types.NodeSocket or DataSocket): the socket to wrap
            - node (Node): the node owning the socket
            - label (str): the label to use for the node            
        """
        
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
        """
        
        self.init_domains()
    
    # ----------------------------------------------------------------------------------------------------
    # Utility changing the output sockets refered by the DataSocket instance
    
    def stack(self, node, socket_name=None):
        """ Change the wrapped socket
        
        After the call, **the DataSocket** instance wraps a different socket, typically in a newly created node.
        This is an internally used by the **geonodes** engine.
        
        In the following example, the `mesh`
        
        ```python
        
        # After the following instruction, mesh wraps the output socket of the Cube node
        mesh = Mesh.Cube()
        
        # After the following instruction, mesh wraps the output socket of the Set Shade Smooth node
        mesh.set_shade_smooth(True)
        ```
        
            
        Args:
            node (Node): the new node
            socket_name (str): name of the outpout socket in the node. If None, takes the first output socket of the node.
            
        Returns:
            self        
        """
        
        self.node = node
        if socket_name is None:
            self.bsocket = node.bnode.outputs[0]
        else:
            self.bsocket = getattr(node, socket_name).bsocket
        self.reset_properties()

        return self

    # ----------------------------------------------------------------------------------------------------
    # Plug (for input sockets only)
            
    def plug(self, *values):
        """ Plug values in the socket (input sockets only)
        
        Args:
            - values (any): The output sockets. More than one values can be passed if the input socket is multi input.
            
        Returns:
            None
        """
        context.plug_to_socket(self.bsocket, *values)
        
    # ----------------------------------------------------------------------------------------------------
    # To group output (for output sockets only)
    
    def to_output(self, name=None):
        """ Create a new output socket in the Tree and plug the **DataSocket** to it.

        The socket is added to the outputs of the geometry nodes tree.
        
        > Note: To define a data socket as the result geometry of the tree, use the property `output_geometry` of 
          the current [Tree](Tree.md#output_geometry).
        
        The created socket can be read from within another [Tree](Tree.md) by:
            - creating a [Group](Group.md): `node = Group(tree_name, **kwargs)`
            - using the snake_case version of the socket: `ver = node.socket_name`
        
        Args:
            - name (str): User name of the socket
            
        Returns:
            None
        """
        if not self.is_output:
            raise RuntimeError(f"The socket '{str(self)}' is not an input socket. It can't be sent to group output.")
        self.node.tree.group_output.to_output(self, self.name if name is None else name)
        
    # ----------------------------------------------------------------------------------------------------
    # To viewer (for output sockets only)
        
    def view(self, domain='AUTO', label=None, node_color=None):
        if not self.is_output:
            raise RuntimeError(f"The socket '{str(self)}' is not an output socket. It can't be connected to the viewer.")
        return self.node.tree.view(self, domain=domain, label=label, node_color=node_color)
        
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

        
        
    
    
        