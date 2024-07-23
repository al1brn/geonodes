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
- Socket root class

created : 2024/07/21
"""

from geonodes.nodes.scripterror import NodeError
from geonodes.nodes import constants

# ====================================================================================================
# Socket Class
# Wrap a blender NodeSocket instance or a python value which can be used to initialize an input socket

class Socket:

    def __init__(self, bsocket):
        self._tree    = constants.CURRENT_TREE
        self._bsocket = bsocket


    @property
    def node(self):
        return self._tree._bsocket_node(self._bsocket)

    def __str__(self):
        return f"{type(self).__name__}: '{self._bsocket.name}', type: '{self._bsocket.type}', node: {self.node}"

    @staticmethod
    def get_socket(bsocket):
        from geonodes.nodes.socketclasses import Boolean, Integer, Float, Vector, Rotation, String, Color
        from geonodes.nodes.socketclasses import Geometry, Image, Texture, Object, Collection, Material
        from geonodes.nodes.socketclasses import Shader, Menu, Matrix

        TYPES = {
            'VALUE'      : Float,
            'INT'        : Integer,
            'BOOLEAN'    : Boolean,
            'VECTOR'     : Vector,
            'ROTATION'   : Rotation,
            'STRING'     : String,
            'RGBA'       : Color,
            'SHADER'     : Shader,
            'OBJECT'     : Object,
            'IMAGE'      : Image,
            'GEOMETRY'   : Geometry,
            'COLLECTION' : Collection,
            'TEXTURE'    : Texture,
            'MATERIAL'   : Material,
            'MENU'       : Menu,
            'MATRIX'     : Matrix,
        }

        if bsocket.type in TYPES:
            return TYPES[bsocket.type](bsocket)

        raise NodeError(f"Sorry: node socket type '{bsocket.type}' not yet supported")


class InputSocket:

    def __init__(self, bsocket):
        self._tree    = constants.CURRENT_TREE
        self._bsocket = bsocket

    def set_value(self, value):
        if isinstance(value, Socket):
            link = self._tree.btree.links.new(self._bsocket, value._bsocket, verify_limits=True)
        else:
            raise Exception("TBD")



class OLD:
    @property
    def data_type(self):
        return self._bsocket.type




    def __str__(self):
        if self._is_socket:
            return f"[Socket '{get_bsock_name(self.bsocket)}' ({'output' if self._is_output else 'input'}) of type '{self._socket_type}' from node {self.node}]"
        else:
            return f"[Socket value {self._value} of type '{self._socket_type}']"

    # ====================================================================================================
    # Clone

    @property
    def clone(self):
        return Socket(self.bsocket)

    # ====================================================================================================
    # Tree (run time only)

    @property
    def tree(self):
        from geonodes.nodes.constants import current_tree
        return current_tree()

    # ====================================================================================================
    # Some properties

    @property
    def _is_socket(self):
        return self.bsocket is not None

    @property
    def _is_value(self):
        return self.bsocket is None

    @property
    def _socket_type(self):
        return type(self).__name__

        if self.bsocket is None:
            return utils.get_value_socket_type(self._value)
        else:
            return self.bsocket.type

    @property
    def _is_output(self):
        if self.bsocket is None:
            return True
        else:
            return self.bsocket.is_output

    # ====================================================================================================
    # To tree output

    def to_output(self, name=None):
        constants.current_tree().to_output(self, name=name)

    # ====================================================================================================
    # Jump to next node

    def jump(self, socket):
        self.node    = socket.node
        self.bsocket = socket.bsocket
        self._value  = None
        self._sub_nodes.clear()

        return self

    # ====================================================================================================
    # Set value

    def _set_value(self, value):

        if self._is_output:
            raise NodeError(f"Impossible to set value to an output socket {self}")

        # ----- Value is a function : creation of an input socket

        if type(value).__name__ == 'function':
            value(self).plug_in(self)
            return

        # ----- Value is value or a socket

        in_bsocket = None
        def_value  = None

        if isinstance(value, bpy.types.NodeSocket):
            in_bsocket = value

        elif isinstance(value, Socket):
            in_bsocket = value.bsocket
            def_value  = value._value

        else:
            def_value = value

        if in_bsocket is None:

            # ----- Menu

            if self.bsocket.type == 'MENU':
                if def_value is None:
                    return
                try:
                    self.bsocket.default_value = value
                except:
                    raise NodeError(f"Value '{value}' is not a valid item for the menu {self}")

                # NOT SURE ITS OLD. Perhaps bugged ??
                if False:
                    enum_items = self.bsocket.node.enum_definition.enum_items
                    for i, item in enumerate(enum_items):
                        if get_bsock_name(item).lower() == str(def_value).lower():
                            self.bsocket.default_value = get_bsock_name(item)
                            return
                    raise NodeError(f"Invalid item name for Socket Menu: '{str(def_value)}' not in {[get_bsock_name(item) for item in enum_items]}")

            # ----- Something else

            else:
                in_bsocket = utils.value_for(def_value, self.bsocket.bl_idname)
                if isinstance(in_bsocket, Socket):
                    in_bsocket = in_bsocket.bsocket
                else:
                    if in_bsocket is not None:
                        self.bsocket.default_value = in_bsocket
                    in_bsocket = None

        if in_bsocket is not None:
            link = self.tree.btree.links.new(in_bsocket, self.bsocket, verify_limits=True)

    # ====================================================================================================
    # Plug into

    def plug_in(self, value):

        bsock = None
        bnode = None

        if isinstance(value, bpy.types.Node):
            bnode = value

        elif hasattr(value, 'bnode'):
            bnode = value.bnode

        elif isinstance(value, bpy.types.NodeSocket):
            bsock = value

        elif isinstance(value, Socket):
            bsock = value.bsocket

        else:
            raise NodeError(f"Impossible to plug the socket {self}. Value '{value}' should be an input socket.")

        if bsock is not None:
            if (not bsock.is_output) and bsock.type == self.bsocket.type:
                self.tree.btree.links.new(self.bsocket, bsock, verify_limits=True)
                return
            bnode = bsock.node

        if bnode is not None:
            for bsock in bnode.inputs:
                if not bsock.enabled:
                    continue

                if bsock.type == self.bsocket.type:
                    self.tree.btree.links.new(self.bsocket, bsock, verify_limits=True)
                    return

        raise NodeError(f"Impossible to plug the socket {self} in {value}. No input socket of the same type ({self.bsocket.type}) found.")

    # =============================================================================================================================
    # Comparison

    def __lt__(self, other):
        return self.tree.Compare(a=self, b=other, operation='LESS_THAN', data_type=self.DATA_TYPE, node_color=OP_COL).result

    def __le__(self, other):
        return self.tree.Compare(a=self, b=other, operation='LESS_EQUAL', data_type=self.DATA_TYPE, node_color=OP_COL).result

    def __gt__(self, other):
        return self.tree.Compare(a=self, b=other, operation='GREATER_THAN', data_type=self.DATA_TYPE, node_color=OP_COL).result

    def __ge__(self, other):
        return self.tree.Compare(a=self, b=other, operation='GREATER_EQUAL', data_type=self.DATA_TYPE, node_color=OP_COL).result

    def __eq__(self, other):
        return self.tree.Compare(a=self, b=other, operation='EQUAL', data_type=self.DATA_TYPE, node_color=OP_COL).result

    def __ne__(self, other):
        return self.tree.Compare(a=self, b=other, operation='NOT_EQUAL', data_type=self.DATA_TYPE, node_color=OP_COL).result

    # ====================================================================================================
    # Helper

    @classmethod
    def print_doc(cls, member_name=None):
        documentation.print_doc(cls, member_name=member_name)
