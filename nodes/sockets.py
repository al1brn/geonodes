#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:14:33 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : sockets
----------------
- Socket wrapper
- Sockets wrapper
- Domain class
- Geometry root class

Socket and Sockets are used both for dynamic nodes building and running.

update : 2024/02/17
update : 2024/03/29
"""

USE_LABEL = True
def get_bsock_name(bsock):
    if USE_LABEL and bsock.label != '':
        return bsock.label
    else:
        return bsock.name

#get_bsock_name = lambda bsock: bsock.label if USE_LABEL else bsock.name


import inspect

from pprint import pprint

import numpy as np

import bpy
from geonodes.nodes import constants
from geonodes.nodes import utils
from geonodes.nodes import documentation

OP_COL = constants.NODE_COLORS['operator']

# ====================================================================================================
# Socket Class
# Wrap a blender NodeSocket instance or a python value which can be used to initialize an input socket

class Socket:

    DATA_TYPE = None

    def __new__(cls, bsocket):

        if cls == Socket:

            if isinstance(bsocket, bpy.types.NodeSocket):
                sock_type = bsocket.type

            elif isinstance(bsocket, Socket):
                sock_type = bsocket._socket_type

            else:
                sock_type = utils.get_value_socket_type(bsocket)

            #socket_class = constants.socket_classes().get(sock_type)
            socket_class = constants.get_socket_class(sock_type)

        else:
            socket_class = None

        if socket_class is None:
            return object.__new__(cls)
        else:
            return object.__new__(socket_class)

    def __init__(self, bsocket):

        if isinstance(bsocket, bpy.types.NodeSocket):
            self.node    = constants.current_tree()._bsocket_node(bsocket)
            self.bsocket = bsocket
            self._value  = None

        elif isinstance(bsocket, Socket):
            self.node    = bsocket.node
            self.bsocket = bsocket.bsocket
            self._value  = bsocket._value

        else:
            self.node    = None
            self.bsocket = None
            self._value  = bsocket


        # ----- Used to cache SeparateXYZ or SeparateColor

        self._sub_nodes = {}


    def __str__(self):
        if self._is_socket:
            return f"[Socket '{get_bsock_name(self.bsocket)}' ({'output' if self._is_output else 'input'}) of type '{self._socket_type}' from node {self.node}]"
        else:
            return f"[Socket value {self._value} of type '{self._socket_type}']"

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
            raise AttributeError(f"Impossible to set value to an output socket {self}")

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
                    raise AttributeError(f"Value '{value}' is not a valid item for the menu {self}")

                # NOT SURE ITS OLD. Perhaps bugged ??
                if False:
                    enum_items = self.bsocket.node.enum_definition.enum_items
                    for i, item in enumerate(enum_items):
                        if get_bsock_name(item).lower() == str(def_value).lower():
                            self.bsocket.default_value = get_bsock_name(item)
                            return
                    raise Exception(f"Invalid item name for Socket Menu: '{str(def_value)}' not in {[get_bsock_name(item) for item in enum_items]}")

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
            raise Exception(f"Impossible to plug the socket {self}. Value '{value}' should be an input socket.")

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

        raise Exception(f"Impossible to plug the socket {self} in {value}. No input socket of the same type ({self.bsocket.type}) found.")

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

# ====================================================================================================
# List of sockets

class Sockets:
    """ A list of Sockets.

    If several sockets share the same name, their key name must be suffixed with '_i'.

    Example
    -------
        - First 'value' socket : value or value_0
        - Second 'value' socket : value_1
    """

    def __init__(self, node, is_input):
        """ List of Node sockets

        Arguments
        ---------
            - node (Node) : the node to read the sockets from
            - is_input (bool) : input sockets (True) or output sockets (False)
        """

        self.node        = node
        self.is_input    = is_input
        self.bsockets    = node.bnode.inputs if is_input else node.bnode.outputs
        self.has_virtual = False
        if is_input:
            self.has_multi = False

        for bsock in self.bsockets:
            if bsock.bl_idname == 'NodeSocketVirtual':
                self.has_virtual = True
            if bsock.is_multi_input:
                self.has_multi = True

    def __str__(self):
        return str(self.sockets_pynames(False).keys())

    # ====================================================================================================
    # Python name from socket name

    @staticmethod
    def pyname(name):
        return utils.socket_name(name)

    # ====================================================================================================
    # List of sockets

    # ----------------------------------------------------------------------------------------------------
    # All enabled sockets

    @property
    def enabled_bsockets(self):
        """ Get the list of sockets which are enabled.

        Returns
        -------
            - list of Blender NodeSocket
        """

        return [bsock for bsock in self.bsockets if bsock.enabled and bsock.bl_idname != 'NodeSocketVirtual']

    # ----------------------------------------------------------------------------------------------------
    # Enabled sockets of a given name

    def enabled_homonyms(self, py_name):
        """ Get the list of enabled sockets matching a gven name.

        Returns
        -------
            - list of Blender NodeSocket
        """

        return [bsock for bsock in self.bsockets if bsock.enabled and self.pyname(get_bsock_name(bsock)) == py_name]

    # ----------------------------------------------------------------------------------------------------
    # Python names
    # Return the python name of sockets with suffix index when several socket share the same name

    def sockets_pynames(self, enabled_only=True, label='NAME'):

        bsocks = {}
        counts = {}
        for bsock in self.bsockets:
            if enabled_only and (not bsock.enabled):
                continue

            if bsock.bl_idname == 'NodeSocketVirtual':
                continue

            if label == 'NAME':
                labels = {self.pyname(bsock.name)}
            elif label == 'LABEL':
                labels = [self.pyname(get_bsock_name(bsock))]
            elif label == 'BOTH':
                labels = {self.pyname(bsock.name), self.pyname(get_bsock_name(bsock))}
            else:
                raise AttributeError(f"socket_pynames error: invalif 'label' argument ('{label}'). Must be in ('NAME', 'LABEL', 'BOTH')")

            for pyname in labels:
                if pyname in counts.keys():
                    counts[pyname] += 1
                    bsocks[f"{pyname}_{counts[pyname]}"] = bsock
                else:
                    counts[pyname] = 0
                    bsocks[pyname] = bsock

        return bsocks

    # ----------------------------------------------------------------------------------------------------
    # Valid socket names
    # For customizable sockets

    @property
    def socket_names(self):
        return [self.pyname(get_bsock_name(bsock)) for bsock in self.bsockets if bsock.enabled and bsock.bl_idname != 'NodeSocketVirtual']

    # ----------------------------------------------------------------------------------------------------
    # Socket documentation
    # return dict : socket : list of socket types

    def sockets_doc(self, enabled_only=True):

        doc    = {}
        counts = {}
        for bsock in self.bsockets:
            if enabled_only and (not bsock.enabled):
                continue

            if bsock.bl_idname == 'NodeSocketVirtual':
                continue

            pyname = self.pyname(get_bsock_name(bsock))
            stype  = constants.SOCKET_CLASS_NAMES[bsock.type]
            if pyname in counts:
                counts[pyname] += 1
                doc[f"{pyname}_{counts[pyname]}"] = stype
            else:
                counts[pyname] = 0
                doc[pyname] = stype

        return doc

    # ====================================================================================================
    # Get a socket by its rank, identifier of python name

    def get_bsocket(self, index):
        """ Get a socket by its name.

        If socket name is None, return the first enabled one.
        If the name is an integer, it is interpreted as the index of in the
        list of enabled sockets.

        Arguments
        ---------
            - name (str=None or int) : socket name

        Returns
        -------
            - Blender NodeSocket
        """

        if index is None:
            return self.enabled_bsockets[0]

        elif isinstance(index, (int, np.int_)):
            return self.enabled_bsockets[index]

        elif isinstance(index, str):

            # ----- Identifier ?

            bsock = self.bsockets.get(index)
            if bsock is not None:
                return bsock

            # ----- Python name

            bsock = self.sockets_pynames(enabled_only=False).get(index)
            if bsock is not None:
                return bsock

            if False: # OLD
                # ----- Pyton name

                pyname = index
                rank = 0

                if len(pyname) > 2 and pyname[-2] == '_' and pyname[-1].isnumeric():
                    rank = int(pyname[-1])
                    pyname = pyname[:-2]

                homs = self.enabled_homonyms(pyname)
                if len(homs) > rank:
                    return homs[rank]

        raise AttributeError(f"Socket named '{index}' not found : {str(self)}, node params: {self.node.params}")


    # ====================================================================================================
    # List of sockets

    def __len__(self):
        return len(self.enabled_bsockets)

    def __getitem__(self, index):
        return Socket(self.get_bsocket(index))

    def __setitem__(self, index, value):
        self[index]._set_value(value)

    # ====================================================================================================
    # Count the number of enabled sockets with the same name

    def enabled_counts(self, max_counts=None, ignore_disabled=False):
        counts = {}
        for bsocket in self.bsockets:
            if (bsocket.enabled or ignore_disabled) and get_bsock_name(bsocket) != "":
                pyname = utils.socket_name(get_bsock_name(bsocket))
                if pyname in counts.keys():
                    counts[pyname] += 1
                else:
                    counts[pyname] = 1

        if max_counts is None:
            return counts

        for key, count in counts.items():
            if key in max_counts.keys():
                max_counts[key] = max(count, max_counts[key])
            else:
                max_counts[key] = count

        return max_counts

    # ====================================================================================================
    # Count the number of sockets with the same name

    def names_counts(self):
        counts = {}
        for bsocket in self.bsockets:
            pyname = utils.socket_name(get_bsock_name(bsocket))
            if pyname in counts:
                counts[pyname] += 1
            else:
                counts[pyname] = 1
        return counts

    # ====================================================================================================
    # Get the multi-input socket if exists

    def get_multi_input_socket(self, halt=True):
        for bsocket in self.bsockets:
            if bsocket.is_multi_input:
                return Socket(bsocket)

        if halt:
            raise AttributeError(f"Node {self.node} has no multi input socket")
        else:
            return None

    # ====================================================================================================
    # First socket compatible with the type of another socket

    def first_compatible(self, socket):
        """ Get the first socket compatible with the given socket.

        Arguments
        ---------
            - socket (Blender NodeSocket) : a socket to connect to the node

        Returns
        -------
            - A socket compatible with the given socket. None if not found
        """

        bsocket = socket.bsocket if isinstance(socket, Socket) else socket

        for bsock in self.sockets:
            if not sock.enabled:
                continue

            if bsocket.type in ['INT', 'FLOAT'] and sock.type in ['INT', 'FLOAT']:
                return sock

            if bsocket.type == bsock.type:
                return Socket(self.node, bsock)

        return None

    # ====================================================================================================
    # Output

    @property
    def output(self):
        for bsock in self.bsockets:
            if bsock.enabled:
                return Socket(bsock)
        return None

    # ====================================================================================================
    # Access to a socket by its type
    # Allow to manage nodes such as CombineColor or SeparateColor
    # Color sockets has the same type RGBA but have different name : Image for compositor and Color for Shaders

    def socket_of_type(self, socket_type, rank=0, halt=True):
        count = rank
        if isinstance(socket_type, tuple):
            types = socket_type
        else:
            types = (socket_type,)

        for bsocket in self.bsockets:
            if bsocket.type in types:
                if count == 0:
                    return Socket(bsocket)
                count -= 1

        if halt:
            raise AttributeError(f"Impossible to find a socket of type '{socket_type}' (rank {rank}) in sockets {[get_bsock_name(bs) for bs in self.bsockets]}.")
        else:
            return None

# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# COMMON TO INT AND VALUE

class INT_VALUE(Socket):

    def __neg__(self):
        return self.tree.Math(self, -1, operation='MULTIPLY', node_color=OP_COL).value

    # ----- Addition

    def __add__(self, other):
        dtype = utils.get_value_socket_type(other)
        if dtype in ['VECTOR', 'ROTATION']:
            return self.tree.VectorMath(self, other, operation='ADD', node_color=OP_COL).vector

        return self.tree.Math(self, other, operation='ADD', node_color=OP_COL).value

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self.jump(self.tree.Math(self, other, operation='ADD', node_color=OP_COL).value)

    # ----- Subtraction

    def __sub__(self, other):
        dtype = utils.get_value_socket_type(other)
        if dtype in ['VECTOR', 'ROTATION']:
            return self.tree.VectorMath(self, other, operation='SUBTRACT', node_color=OP_COL).vector

        return self.tree.Math(self, other, operation='SUBTRACT', node_color=OP_COL).value

    def __rsub__(self, other):
        dtype = utils.get_value_socket_type(other)
        if dtype in ['VECTOR', 'ROTATION']:
            return self.tree.VectorMath(other, self, operation='SUBTRACT', node_color=OP_COL).vector

        return self.tree.Math(other, self, operation='SUBTRACT', node_color=OP_COL).value

    def __isub__(self, other):
        return self.jump(self.tree.Math(self, other, operation='SUBTRACT', node_color=OP_COL).value)

    # ----- Multiplication

    def __mul__(self, other):
        dtype = utils.get_value_socket_type(other)
        if dtype in ['VECTOR', 'ROTATION']:
            return self.tree.VectorMath(other, scale=self, operation='SCALE', node_color=OP_COL).vector

        return self.tree.Math(self, other, operation='MULTIPLY', node_color=OP_COL).value

    def __rmul__(self, other):
        return self*other

    def __imul__(self, other):
        return self.jump(self.tree.Math(self, other, operation='MULTIPLY', node_color=OP_COL).value)

    # ----- Division

    def __truediv__(self, other):
        return self.tree.Math(self, other, operation='DIVIDE', node_color=OP_COL).value

    def __rtruediv__(self, other):
        return self.tree.Math(other, self, operation='DIVIDE', node_color=OP_COL).value

    def __itruediv__(self, other):
        return self.jump(self / other)

    # ----- Modulo

    def __mod__(self, other):
        return self.tree.Math(self, other, operation='MODULO', node_color=OP_COL).value

    def __rmod__(self, other):
        return self.tree.Math(other, self, operation='MODULO', node_color=OP_COL).value

    def __imod__(self, other):
        return self.jump(self % other)

    # ----- Power

    def __pow__(self, other):
        return self.tree.Math(self, other, operation='POWER', node_color=OP_COL).value

    def __rpow__(self, other):
        return self.tree.Math(other, self, operation='POWER', node_color=OP_COL).value

    def __ipow__(self, other):
        return self.jump(self ** other)

class INT(INT_VALUE):
    DATA_TYPE = 'INT'

class VALUE(INT_VALUE):
    DATA_TYPE = 'FLOAT'

# ----------------------------------------------------------------------------------------------------
# Vector / Rotation

class VECTOR_ROT(Socket):

    # ----------------------------------------------------------------------------------------------------
    # Vector

    @property
    def _xyz(self):
        xyz = self._sub_nodes.get('xyz')
        if xyz is None:
            xyz = self.tree.SeparateXYZ(vector=self, node_color=OP_COL)
            self._sub_nodes['xyz'] = xyz
        return xyz

    @property
    def x(self):
        return self._xyz.x

    @property
    def y(self):
        return self._xyz.y

    @property
    def z(self):
        return self._xyz.z

    # ----------------------------------------------------------------------------------------------------
    # Operations

    def __neg__(self):
        return self.tree.VectorMath(self, scale=-1, operation='SCALE').vector

    # ----- Addition

    def __add__(self, other):
        dtype = utils.get_value_socket_type(other)

        return self.tree.VectorMath(self, other, operation='ADD', node_color=OP_COL).vector

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self.jump(self.tree.VectorMath(self, other, operation='ADD', node_color=OP_COL).vector)

    # ----- Subtraction

    def __sub__(self, other):
        dtype = utils.get_value_socket_type(other)

        return self.tree.VectorMath(self, other, operation='SUBTRACT', node_color=OP_COL).vector

    def __rsub__(self, other):
        dtype = utils.get_value_socket_type(other)

        return self.tree.VectorMath(other, self, operation='SUBTRACT', node_color=OP_COL).vector

    def __isub__(self, other):
        return self.jump(self.tree.VectorMath(self, other, operation='SUBTRACT', node_color=OP_COL).vector)

    # ----- Multiplication

    def __mul__(self, other):
        dtype = utils.get_value_socket_type(other)
        if dtype == 'VECTOR':
            return self.tree.VectorMath(self, other, operation='MULTIPLY', node_color=OP_COL).vector
        else:
            return self.tree.VectorMath(self, scale=other, operation='SCALE').vector

    def __rmul__(self, other):
        dtype = utils.get_value_socket_type(other)
        if dtype == 'VECTOR':
            return self.tree.VectorMath(other, self, operation='MULTIPLY', node_color=OP_COL).vector
        else:
            return self.tree.VectorMath(self, scale=other, operation='SCALE', node_color=OP_COL).vector

    def __imul__(self, other):
        return self.jump(self * other)

    # ----- Division

    def __truediv__(self, other):
        return self.tree.VectorMath(self, other, operation='DIVIDE', node_color=OP_COL).vector

    def __rtruediv__(self, other):
        return self.tree.VectorMath(other, self, operation='DIVIDE', node_color=OP_COL).vector

    def __itruediv__(self, other):
        return self.jump(self / other)

    # ----- Modulo

    def __mod__(self, other):
        return self.tree.VectorMath(self, other, operation='MODULO', node_color=OP_COL).value

    def __rmod__(self, other):
        return self.tree.VectorMath(other, self, operation='MODULO', node_color=OP_COL).value

    def __imod__(self, other):
        return self.jump(self % other)

class VECTOR(VECTOR_ROT):
    DATA_TYPE = 'VECTOR'

class ROTATION(VECTOR_ROT):
    DATA_TYPE = 'ROTATION'

# ----------------------------------------------------------------------------------------------------
# Menu

class MENU(Socket):
    DATA_TYPE = 'MENU'

# ----------------------------------------------------------------------------------------------------
# Boolean

class BOOLEAN(Socket):
    DATA_TYPE = 'BOOLEAN'

    # ----- Not

    def __neg__(self):
        return self.tree.BooleanMath(self, operation='NOT', node_color=OP_COL).boolean

    # ----- Or

    def __add__(self, other):
        return self.tree.BooleanMath(self, other, operation='OR', node_color=OP_COL).boolean

    def __radd__(self, other):
        return self.tree.BooleanMath(other, self, operation='OR', node_color=OP_COL).boolean

    def __iadd__(self, other):
        return self.jump(self + other)

    def __or__(self, other):
        return self.tree.BooleanMath(self, other, operation='OR', node_color=OP_COL).boolean

    def __ror__(self, other):
        return self.tree.BooleanMath(other, self, operation='OR', node_color=OP_COL).boolean

    def __ior__(self, other):
        return self.jump(self + other)

    # ----- And

    def __mul__(self, other):
        return self.tree.BooleanMath(self, other, operation='AND', node_color=OP_COL).boolean

    def __rmul__(self, other):
        return self.tree.BooleanMath(other, self, operation='AND', node_color=OP_COL).boolean

    def __imul__(self, other):
        return self.jump(self * other)

    def __and__(self, other):
        return self.tree.BooleanMath(self, other, operation='AND', node_color=OP_COL).boolean

    def __rand__(self, other):
        return self.tree.BooleanMath(other, self, operation='AND', node_color=OP_COL).boolean

    def __iand__(self, other):
        return self.jump(self * other)

    # ----- Xor : DOESN'T EXIST YET

    """
    def __xor__(self, other):
        return self.tree.BooleanMath(self, other, operation='XOR', node_color=OP_COL).boolean

    def __rxor__(self, other):
        return self.tree.BooleanMath(other, self, operation='XOR', node_color=OP_COL).boolean

    def __ixor__(self, other):
        return self.jump(self * other)
    """


# ----------------------------------------------------------------------------------------------------
# String

class STRING(Socket):
    DATA_TYPE = 'STRING'


    # ----- Concat

    def __add__(self, other):

        if self.node.bnode.bl_idname == 'GeometryNodeJoinStrings':
            self.node.strings = other
            return self

        if hasattr(other, 'bsocket'):
            if other.node.bnode.bl_idname == 'GeometryNodeJoinStrings':
                other.node.geometry = self
                return other
        else:
            return self.tree.JoinStrings(self, other, node_color=OP_COL).strings

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self.jump(self + other)

# ----------------------------------------------------------------------------------------------------
# RGBA : maths are used for V4 vector

class RGBA(Socket):
    DATA_TYPE = 'RGBA'

    # ----------------------------------------------------------------------------------------------------
    # Color

    @property
    def rgb(self):
        rgb = self._sub_nodes.get('rgb')
        if rgb is None:
            if True:
                rgb = self.tree.SeparateColor(mode='RGB', node_color=OP_COL)
                # Compositor : color is named Image, otherwise Color
                rgb.inputs.socket_of_type('RGBA')._set_value(self)
            else:
                rgb = self.tree.SeparateColor(color=self, mode='RGB', node_color=OP_COL)
            self._sub_nodes['rgb'] = rgb
        return rgb

    @property
    def hsv(self):
        hsv = self._sub_nodes.get('hsv')
        if hsv is None:
            hsv = self.tree.SeparateColor(color=self, mode='HSV', node_color=OP_COL)
            self._sub_nodes['hsv'] = hsv
        return hsv

    @property
    def hsl(self):
        hsl = self._sub_nodes.get('hsl')
        if hsl is None:
            hsl = self.tree.SeparateColor(color=self, mode='HSL', node_color=OP_COL)
            self._sub_nodes['hsl'] = hsl
        return hsl

    @property
    def r(self):
        return self.rgb.red

    @property
    def g(self):
        return self.rgb.green

    @property
    def b(self):
        return self.rgb.blue

    @property
    def red(self):
        return self.rgb.red

    @property
    def green(self):
        return self.rgb.green

    @property
    def blue(self):
        return self.rgb.blue

    @property
    def alpha(self):
        for sep_name in ['rgb', 'hsv', 'hsl']:
            sep = self._sub_nodes.get(sep_name)
            if sep is not None:
                return sep.alpha

        return self.rgb.alpha

    @property
    def hue(self):
        for sep_name in ['hsv', 'hsl']:
            sep = self._sub_nodes.get(sep_name)
            if sep is not None:
                return sep.hue

        return self.hsv.hue

    @property
    def saturation(self):
        for sep_name in ['hsv', 'hsl']:
            sep = self._sub_nodes.get(sep_name)
            if sep is not None:
                return sep.saturation

        return self.hsv.saturation

    @property
    def value(self):
        return self.hsv.value

    @property
    def lightness(self):
        return self.hsl.lightness

# ====================================================================================================
# Geometry socket

class GEOMETRY(Socket):
    DATA_TYPE = 'GEOMETRY'

    def __init__(self, bsocket):
        super().__init__(bsocket)
        self._selection = None
        self._domain    = None

        #for domain_name in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'SPLINE', 'INSTANCE'):
        #    setattr(self, domain_name, Domain(self, domain_name))

    def jump(self, socket):
        self._selection = None
        self._domain    = None
        return super().jump(socket)

    # ----------------------------------------------------------------------------------------------------
    # Domains

    @property
    def POINT(self):
        self._domain = 'POINT'
        return self

    @property
    def CLOUD(self):
        self._domain = 'CLOUD'
        return self

    @property
    def EDGE(self):
        self._domain = 'EDGE'
        return self

    @property
    def FACE(self):
        self._domain = 'FACE'
        return self

    @property
    def CORNER(self):
        self._domain = 'CORNER'
        return self

    @property
    def CURVE(self):
        self._domain = 'CURVE'
        return self

    @property
    def SPLINE(self):
        self._domain = 'SPLINE'
        return self

    @property
    def INSTANCE(self):
        self._domain = 'INSTANCE'
        return self

    def _get_domain(self, default, DOMAIN_VALUES):

        if True:
            domain = self._domain
            self._domain = None

            if False:
                print(f"GEOMETRY._get_domain({default}, {DOMAIN_VALUES}): // _domain={domain}")

            if domain is None or DOMAIN_VALUES is None:
                return default

            # ----- Sub

            def get_value(values):
                for val in values:
                    if val in DOMAIN_VALUES:
                        return val
                print(f"CAUTION: domain '{domain}' not valid, valid values are: {values}. Default '{default}' is used")
                return default

            # ----- Switch

            if domain == 'POINT':
                return get_value(['POINT', 'POINTS', 'MESH', 'VERTICES', 'ALL'])

            elif domain == 'CLOUD':
                return get_value(['POINTCLOUD'])

            elif domain == 'EDGE':
                return get_value(['EDGE', 'EDGES', 'EDGE_FACE'])

            elif domain == 'FACE':
                return get_value(['FACE', 'FACES', 'ONLY_FACE'])

            elif domain == 'CORNER':
                return get_value(['CORNER', ' CORNERS'])

            elif domain == 'CURVE':
                return get_value(['CURVE', 'CURVES'])

            elif domain == 'SPLINE':
                return get_value(['SPLINE', 'SPLINES'])

            elif domain == 'INSTANCE':
                return get_value(['INSTANCE', 'INSTANCES'])

            else:
                raise AttributeError(f"Domain {domain} not valid")

        else:
            if False:
                print(f"{type(self).__name__}._get_domain(default={default}) // _domain={self._domain} -> ({type(self.node).__name__}) = {self.node._get_domain_value(self._domain, default)} //", self.node.DOMAIN_VALUES)
            _domain = self._domain
            self._domain = None

            return self.node._get_domain_value(_domain, default)


    # ----------------------------------------------------------------------------------------------------
    # Syntax geometry[sel].xxx() -> xxx(selection=sel)

    def __getitem__(self, index):
        self._selection = index
        return self

    def _get_selection(self, selection):

        gen_color = constants.NODE_COLORS['gen']

        # ----- No selection, we return the default

        if self._selection is None:
            return selection

        # ----- Selection valid only once

        _selection = self._selection
        self._selection = None

        # ----- If _selection is int or slice, we generated comparizon nodes with index

        tree = constants.current_tree()

        if isinstance(_selection, slice):

            with tree.layout(f"Slice [{_selection.start}:{_selection.stop}]", node_color=gen_color):

                if _selection.start is None:
                    # [:]
                    if _selection.stop is None:
                        _selection = None
                    # [:10]
                    else:
                        _selection = tree.Index(node_color=gen_color).index.less_than(_selection.stop, node_color=gen_color)
                else:
                    # [10:]
                    if _selection.stop is None:
                        _selection = tree.Index(node_color=gen_color).index.greater_equal(_selection.start, node_color=gen_color)
                    # [10:20]
                    else:
                        half = (_selection.stop  - _selection.start)/2 + .1
                        mid  = (_selection.start + _selection.stop)/2

                        _selection = tree.Compare(tree.Index(node_color=gen_color).index, mid, epsilon=half, operation='EQUAL', data_type='FLOAT', node_color=gen_color).result


        elif utils.get_value_socket_type(_selection) in ['INT', 'VALUE']:
            _selection = tree.Index().index.equal(_selection, node_color=gen_color)

        if selection is None:
            return _selection

        return tree.band(_selection, selection, node_color=constants.NODE_COLORS['gen'])

    # ----------------------------------------------------------------------------------------------------
    # UVMap

    @property
    def uv_map(self):
        return self.CORNER.named_vector("UVMap")

    @uv_map.setter
    def uv_map(self, vector):
        return self.CORNER.store_named_float2("UVMap", vector)

    # ----------------------------------------------------------------------------------------------------
    # Operations

    # ----- Addition

    def __add__(self, other):
        return self.tree.JoinGeometry(self, other, node_color=OP_COL).geometry


    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self.jump(self + other)

    # ----- Subtract

    def __sub__(self, other):
        return self.tree.MeshBoolean(self, other, operation='DIFFERENCE', node_color=OP_COL).mesh

    def __isub__(self, other):
        return self.jump(self - other)
