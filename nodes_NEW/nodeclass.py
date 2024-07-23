#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : nodeclass
------------------
- Node root class

created : 2024/07/21
"""

import bpy

from geonodes.nodes.scripterror import NodeError
from geonodes.nodes import constants
from geonodes.nodes.socketclass import Socket, InputSocket
from geonodes.nodes.nodeclasses import NODES

# ====================================================================================================
# Node root class

class Node:

    def __init__(self, node_name, node_label=None, node_color=None, **kwargs):

        self._tree = constants.CURRENT_TREE

        node_dict = NODES[node_name]
        self._node_name   = node_name
        self._bnode       = self._tree.btree.nodes.new(node_dict['blid'])

        self._tree._register_node(self)

        self._parameters  = node_dict['prms']
        self._in_sockets  = node_dict['inss']
        self._out_sockets = node_dict['outs']

        # ----- Label and color

        if node_label is not None:
            self._bnode.label = node_label

        if node_color is not None:
            self._bnode.use_custom_color = True
            self._bnode.color = node_color

        # ----- Node parameters first

        sockets = {}
        for k, v in kwargs.items():
            if k in self._parameters:
                setattr(self, k, v)
            else:
                sockets[k] = v

        # ----- Node sockets then

        for k, v in sockets.items():
            setattr(self, k, v)


    def __str__(self):
        return f"[{self._bnode.name}]"

    # ====================================================================================================
    # Get an output socket

    def get_socket(self, identifier):

        if isinstance(identifier, int):
            bsocket = self._bnode.outputs[identifier]
        else:
            bsocket = self._bnode.outputs.get(identifier)

        if bsocket is None:
            for bsock in self._bnode.outputs:
                if bsock.name == identifier:
                    bsocket = bsock
                    break

        if bsocket is None:
            raise ('TBD')

        return Socket.get_socket(bsocket)

    # ====================================================================================================
    # Set an input socket

    def set_input_socket(self, bsocket, value):

        if value is None:
            return

        # ----------------------------------------------------------------------------------------------------
        # A socket to link

        if hasattr(value, '_bsocket'):
            link = self._tree.btree.links.new(value._bsocket, bsocket, verify_limits=True)
            return

        # ----------------------------------------------------------------------------------------------------
        # A value to set as default value

        socket_type = bsocket.type

        if socket_type == 'VALUE':
            try:
                v = float(value)
            except:
                v = None

        elif socket_type == 'INT':
            try:
                v = int(value)
            except:
                v = None

        elif socket_type == 'BOOLEAN':
            try:
                v = bool(value)
            except:
                v = None

        elif socket_type in ['VECTOR', 'ROTATION']:
            if hasattr(value, '__len__') and len(value) == 3:
                v = value
            else:
                try:
                    v = float(value)
                    v = (v, v, v)
                except:
                    v = None

        elif socket_type == 'STRING':
            try:
                v = str(value)
            except:
                v = None

        elif socket_type == 'RGBA':
            if hasattr(value, '__len__') and len(value) in [3, 4]:
                if len(value) == 4:
                    v = value
                else:
                    v = (v[0], v[1], v[2], 1)
            else:
                try:
                    v = float(value)
                    v = (v, v, v, v)
                except:
                    v = None

        elif socket_type in ['SHADER', 'GEOMETRY']:
            v = None

        elif socket_type == 'OBJECT':

            if isinstance(value, bpy.types.Object):
                v = value
            elif isinstance(value, str):
                v = bpy.data.objects.get(value)
                if v is None:
                    raise NodeError(f"Impossible to find the object named '{value}'")

        elif socket_type == 'IMAGE':

            if isinstance(value, bpy.types.Image):
                v = value
            elif isinstance(value, str):
                v = bpy.data.images.get(value)
                if v is None:
                    raise NodeError(f"Impossible to find the image named '{value}'")

        elif socket_type == 'COLLECTION':

            if isinstance(value, bpy.types.Collection):
                v = value
            elif isinstance(value, str):
                v = bpy.data.collections.get(value)
                if v is None:
                    raise NodeError(f"Impossible to find the collection named '{value}'")

        elif socket_type == 'TEXTURE':

            if isinstance(value, bpy.types.Texture):
                v = value
            elif isinstance(value, str):
                v = bpy.data.textures.get(value)
                if v is None:
                    raise NodeError(f"Impossible to find the texture named '{value}'")

        elif socket_type == 'MATERIAL':

            if isinstance(value, bpy.types.Material):
                v = value
            elif isinstance(value, str):
                v = bpy.data.images.get(value)
                if v is None:
                    raise NodeError(f"Impossible to find the material named '{value}'")

        elif socket_type == 'MENU':

            raise Exception("TBD")

        else:
            raise Exception(f"Sorry, the socket type '{socket_type}' is not yet supported")

        # ----------------------------------------------------------------------------------------------------
        # Sadly : no default value is possible

        if v is None:
            raise NodeError(f"Error when setting socket '{bsocket.name}': impossible to convert the value <{value}> to socket type '{socket_type}'")

        # ----------------------------------------------------------------------------------------------------
        # We set the default value

        try:
            bsocket.default_value = v
        except:
            raise NodeError(f"Error when setting socket '{bsocket.name}' of socket type '{socket_type}' with default value <{v}>")

    # ====================================================================================================
    # Set an attribute

    def __setattr__(self, name, value):

        # ----- Parameter

        if '_parameters' in self.__dict__:
            parameters = self.__dict__['_parameters']
            if name in parameters:
                if value is not None:
                    setattr(self._bnode, name, value)
                return

        if '_in_sockets' in self.__dict__:
            in_sockets = self.__dict__['_in_sockets']
            if name in in_sockets:
                if value is not None:
                    self.set_input_socket(self._bnode.inputs[in_sockets[name]], value)
                return

        super().__setattr__(name, value)

    # ====================================================================================================
    # Get an attribute

    def __getattr__(self, name):

        if '_out_sockets' in self.__dict__:
            out_sockets = self.__dict__['_out_sockets']
            if name in out_sockets:
                return self.get_socket(out_sockets[name])

        raise NodeError(f"Output socket '{name}' not defined for node '{self._bnode.name}'")





class BooleanNode(Node):

    def init(self, value=None):
        pass

    @property
    def output(self):
        return Boolean()
