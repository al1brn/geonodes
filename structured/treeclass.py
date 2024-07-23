#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
-----------------------------------------------------

module : treeclass
------------------
- Tree class
- Node class

create : 2024/07/22
"""

import bpy

from geonodes.structured.scripterror import NodeError
from geonodes.structured import treearrange
from geonodes.structured import constants
from geonodes.structured import utils


ARRAY_TYPES = {
    'VECTOR'  : {'shape': (3,),  'combine': 'Combine XYZ',    'init': 'Vector',   'param': 'vector'},
    'ROTATION': {'shape': (3,),  'combine': 'Combine XYZ',    'init': 'Rotation', 'param': 'rotation'},
    'RGBA'    : {'shape': (4,),  'combine': 'Combine Color',  'init': 'Color',    'param': 'color'},
    'MATRIX'  : {'shape': (16,), 'combine': 'Combine Matrix', 'init': None},
}

# =============================================================================================================================
# Tree

class Tree:

    STACK     = []
    TREE_TYPE = None

    class Break(Exception):
        pass

    def __init__(self, name, create=True, clear=False):
        self._btree     = utils.get_tree(name, create=create, clear=clear)
        self.NODE_NAMES = constants.NODE_NAMES
        self._nodes     = []

    # ====================================================================================================
    # Some methods

    def __str__(self):
        return f"<Tree '{self._btree.name}' ({self.TREE_TYPE}): {len(self._btree.nodes)} nodes and {len(self._btree.links)} links>"

    @property
    def _str_stats(self):
        return f"{len(self._btree.nodes)} nodes, {len(self._btree.links)} links"

    def clear(self):
        self._btree.nodes.clear()

    def _register_node(self, node):
        self._nodes.append(node)

    # ----------------------------------------------------------------------------------------------------
    # Context manager

    def push(self):
        Tree.STACK.append(self)

    def pop(self):
        tree = Tree.STACK.pop()
        if tree != self:
            raise NodeError(f"Error in tree stack management")

    @classmethod
    @property
    def CURRENT(cls):
        return Tree.STACK[-1]

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, type, exc_value, traceback):

        self.pop()
        self.arrange()

        print(f"Tree '{self._btree.name}' built: {self._str_stats}")

        if isinstance(exc_value, self.Break):
            return True

    def arrange(self):
        treearrange.arrange(self._btree)

    # =============================================================================================================================
    # Create a link

    def link(self, out_socket, in_socket):

        if hasattr(out_socket, '_bsocket'):
            out_socket = out_socket._bsocket

        if hasattr(in_socket, '_bsocket'):
            in_socket = in_socket._bsocket

        return self._btree.links.new(out_socket, in_socket)

    # =============================================================================================================================
    # Input Nodes

    def InputBSocket(self, socket_type, value=None):

        # ----------------------------------------------------------------------------------------------------
        # The value is already a socket

        bsock = utils.get_bsocket(value)
        if bsock is not None:
            return bsock

        # ----------------------------------------------------------------------------------------------------
        # Simple types (no array)

        if socket_type == 'BOOLEAN':
            return Node('Boolean', boolean=value)._out

        elif socket_type == 'INT':
            return Node('Integer', integer=value)._out

        elif socket_type == 'VALUE':
            out_socket = Node('Value')._out
            out_socket._bsocket.default_value = float(value)
            return out_socket

        elif socket_type == 'STRING':
            return Node('String', string=str(value))._out

        elif socket_type in ['IMAGE', 'MATERIAL']:
            res = utils.get_blender_resource(socket_type, value)
            if res is not None:
                if socket_type == 'IMAGE':
                    return Node('Image', image=res)._out
                else:
                    return Node('Material', material=res)._out

        # ----------------------------------------------------------------------------------------------------
        # Array types
        # Value in the array can contain a socket

        elif socket_type in ARRAY_TYPES:

            spec = ARRAY_TYPES[socket_type]
            a = utils.value_to_array(value, spec['shape'])

            # Combine if not Init Node (for instance Matrix)
            combine = spec['init'] is None

            # Combine if the list contains at least one socket
            for item in a:
                if utils.get_bsocket(item) is not None:
                    combine = True
                    break

            if combine:
                return Node(spec['combine'], {i: a[i] for i in range(len(a))})._out
            else:
                return Node(spec['init'], **{spec['param']: tuple(a)})._out


        # ----------------------------------------------------------------------------------------------------
        # Array types
        # Value in the array can contain a socket

        else:
            raise NodeError(f"No Input Node exists for socket type '{socket_type}'")


    # =============================================================================================================================
    # Data type

    @staticmethod
    def _get_data_type(value):
        if value is None:
            return None

        if isinstance(value, DataSocket):
            return value.DATA_TYPE
        elif isinstance(value, bool):
            return 'BOOLEAN'
        elif isinstance(value, int):
            return 'INT'
        elif isinstance(value, float):
            return 'FLOAT'
        elif isinstance(value, (list, tuple)):
            if len(value) == 3:
                return 'FLOAT_VECTOR'
            elif len(value) == 4:
                return 'COLOR'
        return None


# =============================================================================================================================
# Node

class Node:
    def __init__(self, name, sockets={}, **parameters):

        self._tree = Tree.CURRENT
        btree = self._tree._btree

        node_name = name.lower()
        if node_name in self._tree.NODE_NAMES:
            bl_idname = self._tree.NODE_NAMES[node_name]
        else:
            bl_idname = name

        self._bnode = btree.nodes.new(type=bl_idname)

        # ---------------------------------------------------------------------------
        # Set the parameters

        self.set_parameters(**parameters)

        # ---------------------------------------------------------------------------
        # Set the sockets

        self.set_input_sockets(sockets)

        # ---------------------------------------------------------------------------
        # Register

        self._tree._register_node(self)

    @property
    def _btree(self):
        return self._tree._btree

    # ----------------------------------------------------------------------------------------------------
    # Create a DataSocket from an output Blender NodeSocket

    @staticmethod
    def data_socket(bsocket):
        from geonodes.structured.booleanclass import Boolean
        from geonodes.structured.floatclass import Integer, Float
        from geonodes.structured.vectorclass import Vector, Rotation
        from geonodes.structured.geometryclass import Geometry

        return {'BOOLEAN': Boolean, 'INT': Integer, 'VALUE': Float, 'VECTOR': Vector, 'ROTATION': Rotation, 'GEOMETRY': Geometry,
            }[bsocket.type](bsocket)

    # ----------------------------------------------------------------------------------------------------
    # Set the node parameters

    def set_parameters(self, **parameters):

        for param_name, param_value in parameters.items():
            if param_value is None:
                continue

            setattr(self._bnode, param_name, param_value)

    # ----------------------------------------------------------------------------------------------------
    # Get a socket by its index, identifier or name

    def inout_socket(self, name, bsockets):

        if isinstance(name, int):
            return bsockets[name]

        try:
            bsocket = bsockets[name]
        except:
            bsocket = None
            for bsock in bsockets:
                if not bsock.enabled:
                    continue

                if bsock.name == bsocket or utils.socket_name(bsock.name) == name:
                    bsocket = bsock
                    break

        if bsocket is None:
            raise Exception(f"Socket name '{name}' not found in node '{self._bnode.name}' ({self._bnode.bl_idname})")

        return bsocket

    def in_socket(self, name):
        return self.inout_socket(name, self._bnode.inputs)

    def out_socket(self, name):
        return self.data_socket(self.inout_socket(name, self._bnode.outputs))

    # ----------------------------------------------------------------------------------------------------
    # Set the node sockets

    def set_input_sockets(self, sockets={}):

        for socket_name, socket_value in sockets.items():

            if socket_value is None:
                continue

            in_socket = self.in_socket(socket_name)
            self.plug_value_into_socket(socket_value, in_socket)

    # ----------------------------------------------------------------------------------------------------
    # Set an input socket and Get an output socket

    def __getitem__(self, name):
        return self.out_socket(name)

    def __setitem__(self, name, value):
        self.plug_value_into_socket(value, self.in_socket(name))

    @property
    def _out(self):
        for bsock in self._bnode.outputs:
            if bsock.enabled:
                return self.data_socket(bsock)
        return None

    # ====================================================================================================
    # Read a node attribute : it is an output socket

    def __getattr__(self, name):
        if '_bnode' in self.__dict__:
            out_socket = self.out_socket(name)
            if out_socket is None:
                raise AttributeError(f"Node parameter '{name}' not found in '{self.__dict__['_bnode'].name}'.")
            else:
                return out_socket

        raise AttributeError(f"Node parameter '{name}' not found.")

        # OLD OLD OLD OLD OLD OLD OLD

        sbnode = ''
        if '_bnode' in self.__dict__:
            bnode = self.__dict__['_bnode']
            sbnode = bnode.name
            if hasattr(bnode, name):
                return getattr(bnode, name)

        raise AttributeError(f"Node parameter '{name}' not found in '{sbnode}'.")

    def __setattr__(self, name, value):
        sbnode = ''
        if '_bnode' in self.__dict__:

            # ----- Set parameter

            bnode = self.__dict__['_bnode']
            sbnode = bnode.name
            if hasattr(bnode, name):
                setattr(bnode, name, value)
                return

            # ---- Link input node

            in_socket = self.in_socket(name)
            if in_socket is not None:
                self.plug_value_into_socket(value, in_socket)
                return

        if name not in ['_tree', '_bnode']:
            raise AttributeError(f"Node parameter '{name}' not found in '{sbnode}'.")
        else:
            super().__setattr__(name, value)

    # =============================================================================================================================
    # Get an acceptable thing to set to an input socket
    # - If the value is a socket -> Nothing to do
    # - If the value is a python value:
    #   - If the input socket hide the value -> must be converted to an input node
    #   - Or is used to set the default_value to the input socket

    def plug_value_into_socket(self, value, in_socket):

        if value is None:
            return

        # ----------------------------------------------------------------------------------------------------
        # If the value is a Node, we take its default output socket

        if hasattr(value, '_bnode'):
            value = value._out

        # ----------------------------------------------------------------------------------------------------
        # We directly have a socket

        out_socket = utils.get_bsocket(value)
        if out_socket is not None:
            self._tree.link(out_socket, in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # We need to create a node if:
        # - in_socket.hide_value is True
        # - the value is an array containing sockets : vector((0, a, 1))

        socket_type = in_socket.type

        if in_socket.hide_value:
            self._tree.link(self._tree.InputBSocket(socket_type, value), in_socket)
            return

        # ----------------------------------------------------------------------------------------------------
        # We can use default value

        if socket_type in ARRAY_TYPES:
            spec = ARRAY_TYPES[socket_type]
            a = utils.value_to_array(value, spec['shape'])
            use_node = False
            for item in a:
                if utils.get_bsocket(item) is not None:
                    use_node = True
                    break

            if use_node:
                self._tree.link(self._tree.InputBSocket(socket_type, value))
            else:
                in_socket.default_value = list(a)

        elif socket_type in ['BOOLEAN', 'INT', 'VALUE', 'STRING']:
            in_socket.default_value = value

        elif in_socket.type in ['OBJECT', 'COLLECTION', 'IMAGE', 'MATERIAL']:
            bobj = utils.get_blender_resource(in_socket.type, value)

            if bobj is not None:
                in_socket.default_value = bobj

        else:
            raise NodeError(f"Impossible to set the socket '{in_socket.name}' of type '{socket_type}' with value {value}.")
