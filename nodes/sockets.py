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
"""

from pprint import pprint

import numpy as np

import bpy
from geonodes.nodes import constants
from geonodes.nodes import utils


# ====================================================================================================
# Socket Class
# Wrap a blender NodeSocket instance or a python value which can be used to initialize an input socket

class Socket:

    def __new__(cls, bsocket):
        
        if cls == Socket:
            if isinstance(bsocket, bpy.types.NodeSocket):
                sock_type = bsocket.type
                
            elif isinstance(bsocket, Socket):
                sock_type = bsocket._socket_type
                
            else:
                sock_type = utils.get_value_socket_type(bsocket)
                
            socket_class = constants.socket_classes().get(sock_type)
            
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

    def __str__(self):
        if self._is_socket:
            return f"[Socket '{self.bsocket.name}' ({'output' if self._is_output else 'input'}) of type '{self._socket_type}' from node {self.node}]"
        else:
            return f"[Socket value {self._value} of type '{self._socket_type}']"
    
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
        return self
    
    # ====================================================================================================
    # Set value
        
    def _set_value(self, value):
        
        if self._is_output:
            raise AttributeError(f"Impossible to set value to an output socket {self}")
        
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
            in_bsocket = utils.value_for(def_value, self.bsocket.bl_idname)
            if isinstance(in_bsocket, Socket):
                in_bsocket = in_bsocket.bsocket
            else:
                if in_bsocket is not None:
                    self.bsocket.default_value = in_bsocket
                in_bsocket = None
                
        if in_bsocket is not None:
            link = self.node.tree.btree.links.new(in_bsocket, self.bsocket, verify_limits=True)

    # ====================================================================================================
    # Operations
    
    def _op_error(self, operation):
        raise Exception(f"Operation error: operation '{operation}' not implemented for socket type '{self._socket_type}'")
    
    # ----- Addition
    
    def __add__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT', 'VECTOR', 'ROTATION']:
            return self.add(other)
        
        elif stype == 'BOOLEAN':
            return self.bor(other)
        
        elif stype == 'STRING':
            return self.join_strings(other)
        
        elif stype == 'RGBA':
            return self.mix_color(other, blend_type='ADD')
        
        elif stype == 'GEOMETRY':
            return self.join_geometry(other)
        
        else:
            self.op_error('ADD')
            
    def __radd__(self, other):
        return type(self).Value(other) + self
    
    def __iadd__(self, other):
        return self.jump(self + other)
        
    # ----- Subtract

    def __sub__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT', 'VECTOR', 'ROTATION', 'RGBA']:
            return self.subtract(other)
            
        else:
            self.op_error('SUBTRACT')
            
    def __rsub__(self, other):
        return type(self)(other) - self
    
    def __isub__(self, other):
        return self.jump(self - other)
        
    # ----- Multiplication
    
    def __mul__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT']:
            if isinstance(other, Socket):
                if other._socket_type in ['VECTOR', 'ROTATION']:
                    return other * self
                
            return self.multiply(other)
        
        elif stype in ['VECTOR', 'ROTATION']:
            other_is_value = isinstance(other, (int, float, np.int_, np.float_))
            if isinstance(other, Socket) and other._socket_type in ['VALUE', 'INT']:
                other_is_value = True
                
            if other_is_value:
                return self.scale(other)
            else:
                return self.multiply(other)
            
        elif stype == 'BOOLEAN':
            return self.band(other)
        
        elif stype == 'RGBA':
            return self.multiply(other)
        
        else:
            self.op_error('MULTIPLY')
            
    def __rmul__(self, other):
        return type(self)(other) * self
    
    def __imul__(self, other):
        return self.jump(self * other)
    
    # ----- Negative
    
    def __neg__(self):
        return self * -1
    
    # ----- Division

    def __truediv__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT']:
            return self.divide(other)
        
        elif stype in ['VECTOR', 'ROTATION']:
            return self.divide(other)
            
        elif stype == 'RGBA':
            return self.divide(other)
        
        else:
            self.op_error('DIVIDE')
            
    def __rtruediv__(self, other):
        return type(self)(other) / self
    
    def __itruediv__(self, other):
        return self.jump(self / other)

    # ----- Division

    def __floordiv__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT']:
            return self.divide(other)
        
        elif stype in ['VECTOR', 'ROTATION']:
            return self.divice(other)
            
        elif stype == 'RGBA':
            return self.divide(other)
        
        else:
            self.op_error('DIVIDE')
            
    def __rfloordiv__(self, other):
        return type(self)(other) // self
    
    def __ifloordiv__(self, other):
        return self.jump(self // other)
    
    # ----- Modulo

    def __mod__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT']:
            return self.mod(other)
        
        elif stype == 'RGBA':
            if isinstance(other, tuple) and len(other) == 2:
                self.mix(factor=other[1], b=other[0])
            else:
                return self.mix(other)
        
        else:
            self.op_error('MODULO')
            
    def __rmod__(self, other):
        return type(self)(other) % self
    
    def __imod__(self, other):
        return self.jump(self % other)
    
    # ----- Power
    
    def __pow__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT']:
            return self.math(other, operation='POWER')
        
        else:
            self.op_error('POWER')
            
    def __rpow__(self, other):
        return type(self)(other) ** self
    
    def __ipow__(self, other):
        return self.jump(self ** other)    
    
    # ----- Mat mul
    
    def __matmul__(self, other):
        stype = self._socket_type
        
        if stype in ['VALUE', 'INT']:
            if isinstance(other, tuple) and len(other) == 2:
                return self.multiply_add(other[0], other[1])
            else:
                return self.multiply_add(other)
        
        elif stype in ['VECTOR', 'ROTATION']:
            return self.dot(other)
        
        else:
            self.op_error('MAT MUL')
            
    def __rmatmul__(self, other):
        return type(self)(other) @ self
    
    def __imatmul__(self, other):
        return self.jump(self @ other)    
    
        
        
        
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
        
        return [bsock for bsock in self.bsockets if bsock.enabled and self.pyname(bsock.name) == py_name]
    
    # ----------------------------------------------------------------------------------------------------
    # Python names
    #
    # Return dict : py_name : number of sockets with this name
    
    def sockets_pynames(self, enabled_only=True):
        
        bsocks = {}
        counts = {}
        for bsock in self.bsockets:
            if enabled_only and (not bsock.enabled):
                continue
            
            if bsock.bl_idname == 'NodeSocketVirtual':
                continue

            pyname = self.pyname(bsock.name)
            if pyname in counts.keys():
                counts[pyname] += 1
                bsocks[f"{pyname}_{counts[pyname]}"] = bsock
            else:
                counts[pyname] = 0
                bsocks[pyname] = bsock
                
        return bsocks
    
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
            
            pyname = self.pyname(bsock.name)
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
        
    def enabled_counts(self, max_counts=None):
        counts = {}
        for bsocket in self.bsockets:
            if bsocket.enabled and bsocket.name != "":
                pyname = utils.socket_name(bsocket.name)
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
            pyname = utils.socket_name(bsocket.name)
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
# Geometry socket

class Domain:
    def __init__(self, geometry, domain_name):
        self.geometry    = geometry
        self.domain_name = domain_name
        
    def jump(self, socket):
        return self.geometry.jump(socket)

class Geometry(Socket):
    def __init__(self, bsocket):
        super().__init__(bsocket)
        self._selection = None
        
        for domain_name in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'SPLINE', 'INSTANCE'):
            setattr(self, domain_name, Domain(self, domain_name))
            
    def __getitem__(self, index):
        self._selection = index
        return self
    
    def _get_selection(self, selection):
        
        sel = self._selection
        if sel is None:
            return selection
        
        self._selection = None
        if selection is None:
            return sel
        
        return constants.current_tree().band(sel, selection, node_label="[sel] and selection")
        

        
    
    
        
    
