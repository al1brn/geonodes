#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:45:39 2022

@author: alain
"""

from geonodes import nodes
from .basenode import Tree, Node, Socket

import bpy

import logging
logger = logging.getLogger('geonodes')

# =============================================================================================================================
# When a node return more than one sockets, the sockets are put in a dedicated class

class Sockets:
    def __init__(self, **kwargs):
        
        self.names = list(kwargs.keys())
        for k, w in kwargs.items():
            setattr(self, k, w)

        logger.debug(f"Sockets: node: {getattr(self, self.names[0]).node}, sockets: {str(self)}")
        
    def __str__(self):
        s = "["
        sep = ""
        for name in self.names:
            v = getattr(self, name)
            s += f"{sep}{name} ({type(v).__name__})"
            sep = ", "
        s += "]"
        return s
        


# ====================================================================================================
# NodeSocket manages a couple (node, socket) with additional nodes as properties
# It manages a stack for nodes which keep the class 
#
# Note that the nodes which are stacked have only one output socket with the proper class
    
    
class NodeSocket:
    
    def __init__(self, socket):
        
        if isinstance(socket, NodeSocket):
            self.socket = socket.socket
        
        elif isinstance(socket, Socket):
            self.socket = socket
            
        elif socket is None:
            self.socket = None
            
        else:
            print("Invalid socket:", socket)
            print("type:          ", type(socket))
            raise RuntimeError(f"Invalid socket {socket} to intialize data class.")
        
        # The nodes stack
        
        self.stack_  = []
        
        # The nodes stack
        
        self.field_of = None
        

    # ----------------------------------------------------------------------------------------------------
    # Access to node and index
    
    @property
    def node(self):
        if self.socket is None:
            return None
        else:
            return self.socket.node

    @property
    def socket_index(self):
        if self.socket is None:
            return None
        else:
            return self.socket.index
        
    # ----------------------------------------------------------------------------------------------------
    # Create a new group input
    
    @classmethod
    def Input(cls, bl_idname, value, name):
        return cls(Tree.current().new_input_socket(bl_idname, value=value, name=name))

    # ----------------------------------------------------------------------------------------------------
    # Stack management
    
    def stack(self, node):
        if isinstance(node, NodeSocket):
            logger.critical(node)
            logger.critical(type(node))
            raise RuntimeError(f"Internal error")
        self.stack_.append(node)
        node.stack_of = self.node
        
        logger.debug(f"Stack: {str(self)}")
        
        return self

    @property
    def top(self):
        if self.stack_:
            return self.stack_[-1]
        else:
            return self
    
    # ----------------------------------------------------------------------------------------------------
    # Connector
    #
    # By buildind a specific couple (node, socket), the object can be modified without changing the
    # connection link
    
    @property
    def connector(self):
        if self.stack_:
            return self.top.outputs[0]
        elif self.socket is None:
            return None
        else:
            return self.socket
    
    # ----------------------------------------------------------------------------------------------------
    # Pretty string
    
    def __str__(self):

        if self.node is None:
            return f"<type(self).__name__ with no node>"

        s = f"<{type(self).__name__} {str(self.node)}.{self.socket.name}"
        if self.stack_:
            s += f" stack ({len(self.stack_)}, top: {self.top})"
        
        return s + ">"

    def __repr__(self):
        
        def snode(node, indent=""):
            s = ""
            for line in repr(node).split("\n"):
                s += indent + line + "\n"
            return s
        
        s = f"[{type(self).__name__}:\n"
        
        if self.node is None:
            s += "with no node\n"
        else:
            s += f"socket {self.socket} of node:\n"
            s += snode(self.node) + "\n"
        
        if self.stack_:
            s += "::::: Stack of {len(self.stack_) nodes:}\n"
            for i, node in enumerate(self.stack_):
                s += f"{i}: " + snode(node, "   ")
        else:
            s += "::::: Empty stack"
            
        return s + "]"     
    
    # ----------------------------------------------------------------------------------------------------
    # Node label
    
    @property
    def node_label(self):
        if self.stack_:
            return self.top.label
        elif self.node is None:
            return None
        else:
            return self.node.label
    
    @node_label.setter
    def node_label(self, value):
        if self.stack_:
            self.top.label = value
        elif self.node is None:
            raise RuntimeError(f"Impossible to set the lable of '{self}' which has no node.")
        else:
            self.node.label = value
            
# =============================================================================================================================
# The base classes

# -----------------------------------------------------------------------------------------------------------------------------
# Boolean

class Boolean(NodeSocket):
    
    def __init__(self, value=False):
        if isinstance(value, (Socket, NodeSocket)):
            super().__init__(value)
        else:
            node = nodes.NodeBoolean(bool(value))
            super().__init__(node.boolean)
    
    @classmethod
    def Input(cls, value=False, name="Boolean"):
        return cls(Tree.current().new_input_socket('NodeSocketBool', value=value, name=name))
    
    
    def __add__(self, other):
        return self.b_or(other)
    
    def __radd__(self, other):
        ret = self.add(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __iadd__(self, other):
        return self.stack(self.b_or(other).node)
    
    def __mul__(self, other):
        return self.b_and(other)
    
    def __rmul__(self, other):
        ret = self.b_and(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
        
        return self.b_and(other)
    
    def __imul__(self, other):
        return self.stack(self.b_and(other).node)
    
    def __neg__(self):
        return self.b_not()

# -----------------------------------------------------------------------------------------------------------------------------
# Shared by Integer, Float and Vector

class IntFloat(NodeSocket):
    
    def __neg__(self):
        return self.multiply(-1)
    

    def __add__(self, other):
        return self.add(other)
    
    def __radd__(self, other):
        ret = self.add(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __iadd__(self, other):
        return self.stack(self.add(other).node)
    

    def __sub__(self, other):
        return self.substract(other)
    
    def __rsub__(self, other):
        ret = self.substract(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __isub__(self, other):
        return self.stack(self.substract(other).node)
    
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __rmul__(self, other):
        ret = self.multiply(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __imul__(self, other):
        return self.stack(self.multiply(other).node)

    
    def __truediv__(self, other):
        return self.divide(other)
    
    def __rtruediv__(self, other):
        ret = self.divide(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __itruediv__(self, other):
        return self.stack(self.divide(other).node)
    

    def __mod__(self, other):
        return self.modulo(other)
    
    def __rmod__(self, other):
        ret = self.modulo(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __imod__(self, other):
        return self.stack(self.modulo(other).node)
    
    
    def __pow__(self, other):
        return self.pow(other)
    
    def __rpow__(self, other):
        ret = self.pow(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    

# -----------------------------------------------------------------------------------------------------------------------------
# Integer
    
class Integer(IntFloat):
    
    def __init__(self, value=0):
        if isinstance(value, (Socket, NodeSocket)):
            super().__init__(value)
        else:
            node = nodes.NodeInteger(int(value))
            super().__init__(node.integer)
    
    @classmethod
    def Input(cls, value=0, name="Integer"):
        return cls(Tree.current().new_input_socket('NodeSocketInt', value=value, name=name))

    @classmethod
    def Unsigned(cls, value=0, name="Unsigned"):
        return cls(Tree.current().new_input_socket('NodeSocketIntUnsigned', value=value, name=name))

# -----------------------------------------------------------------------------------------------------------------------------
# Float

class Float(IntFloat):
    
    def __init__(self, value=0.):
        if isinstance(value, (Socket, NodeSocket)):
            super().__init__(value)
        else:
            node = nodes.NodeValue(float(value))
            super().__init__(node.value)
    
    @classmethod
    def Input(cls, value=0., name="Float"):
        return cls(Tree.current().new_input_socket('NodeSocketFloat', value=value, name=name))
        
    @classmethod
    def Angle(cls, value=0., name="Angle"):
        return cls(Tree.current().new_input_socket('NodeSocketFloatAngle', value=value, name=name))
        
    @classmethod
    def Factor(cls, value=0., name="Factor"):
        return cls(Tree.current().new_input_socket('NodeSocketFloatFactor', value=value, name=name))
        
    @classmethod
    def Distance(cls, value=0., name="Distance"):
        return cls(Tree.current().new_input_socket('NodeSocketFloatDistance', value=value, name=name))

# -----------------------------------------------------------------------------------------------------------------------------
# String

class String(NodeSocket):
    
    def __init__(self, value="Text"):
        if isinstance(value, (Socket, NodeSocket)):
            super().__init__(value)
        else:
            node = nodes.NodeString(str(value))
            super().__init__(node.string)
    
    @classmethod
    def Input(cls, value="Text", name="String"):
        return cls(Tree.current().new_input_socket('NodeSocketString', value=value, name=name))
    
    @classmethod
    def Tab(cls):
        return cls(nodes.NodeSpecialCharacters().tab)
    
    @classmethod
    def LineBreak(cls):
        return cls(nodes.NodeSpecialCharacters().line_break)
    
    def __add__(self, other):
        return String(nodes.NodeJoinStrings(self, other).outputs[0])

    def __radd__(self, other):
        return String(nodes.NodeJoinStrings(other, self).outputs[0])
    
    def __iadd__(self, other):
        return self.stack(nodes.NodeJoinStrings(self, other))
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Vector

class Vector(IntFloat):
    
    def __init__(self, value=(0., 0., 0.)):
        if isinstance(value, (Socket, NodeSocket)):
            super().__init__(value)
        else:
            if not hasattr(value, '__len__'):
                value = (value, value, value)
            node = nodes.NodeVector(value)
            super().__init__(node.vector)
            

    def __neg__(self):
        return self.multiply(-1)
    

    def __add__(self, other):
        return self.add(other)
    
    def __radd__(self, other):
        ret = self.add(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __iadd__(self, other):
        return self.stack(self.add(other).node)
    

    def __sub__(self, other):
        return self.substract(other)
    
    def __rsub__(self, other):
        ret = self.substract(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __isub__(self, other):
        return self.stack(self.substract(other).node)
    
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __rmul__(self, other):
        ret = self.multiply(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __imul__(self, other):
        return self.stack(self.multiply(other).node)

    
    def __truediv__(self, other):
        return self.divide(other)
    
    def __rtruediv__(self, other):
        ret = self.divide(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __itruediv__(self, other):
        return self.stack(self.divide(other).node)
    

    def __mod__(self, other):
        return self.modulo(other)
    
    def __rmod__(self, other):
        ret = self.modulo(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __imod__(self, other):
        return self.stack(self.modulo(other).node)
            
    
    @classmethod
    def Input(cls, value=(0, 0, 0), name="Vector"):
        return cls(Tree.current().new_input_socket('NodeSocketVector', value=value, name=name))
        
    @classmethod
    def Rotation(cls, value=(0, 0, 0), name="Rotation"):
        return cls(Tree.current().new_input_socket('NodeSocketVectorEuler', value=value, name=name))
        
    @classmethod
    def Translation(cls, value=(0, 0, 0), name="Translation"):
        return cls(Tree.current().new_input_socket('NodeSocketVectorTranslation', value=value, name=name))
        
    @classmethod
    def VectorXYZ(cls, value=(0, 0, 0), name="VectorXYZ"):
        return cls(Tree.current().new_input_socket('NodeSocketVectorXYZ', value=value, name=name))
        
    @property
    def connector(self):
        if hasattr(self.top, 'separate_'):
            self.stack(nodes.NodeCombineXYZ(self.top.x, self.top.y, self.top.z))
        return super().connector

# -----------------------------------------------------------------------------------------------------------------------------
# Color

class Color(IntFloat):
    
    def __init__(self, value=None):
        if isinstance(value, (Socket, NodeSocket)):
            super().__init__(value)
        else:
            node = nodes.NodeVector()
            super().__init__(node.vector)
    
    
    @classmethod
    def Input(cls, name="Color"):
        return cls(Tree.current().new_input_socket('NodeSocketColor', name=name))
    
    @property
    def connector(self):
        if hasattr(self.top, 'separate_'):
            self.stack(node.NodeCombineRGB(self.top.r, self.top.g, self.top.b))
        return super().connector
    
# -----------------------------------------------------------------------------------------------------------------------------
# Geometry

class Geometry(NodeSocket):
    
    @classmethod
    def Input(cls, name=None):
        if name is None:
            name = cls.__name__
        return cls(Tree.current().new_input_socket('NodeSocketGeometry', name=name))
    
    @classmethod
    def FromCollection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        if isinstance(collection, str):
            coll = bpy.data.collection[collection]
        else:
            coll = collection
        return cls(nodes.NodeCollectionInfo(collection=coll, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).outputs[0])
    
    def __add__(self, other):
        return self.join(other.socket)
    
    def __radd__(self, other):
        return other.join(self.socket)
    
    def __iadd__(self, other):
        return self.stack(self.add(other).node)
    

# -----------------------------------------------------------------------------------------------------------------------------
# Collection

class Collection(NodeSocket):
    
    @staticmethod
    def blender_collection(coll):
        if type(coll) is str:
            name = coll
            coll = bpy.data.collections.get(name)
            if coll is None:
                raise RuntimeError(f"Collection '{name}' doesn't exist.")
        return coll
    
    @classmethod
    def Input(cls, name="Collection"):
        return cls(Tree.current().new_input_socket('NodeSocketCollection', name=name))
            
            
# -----------------------------------------------------------------------------------------------------------------------------
# Object

class Object(NodeSocket):
    
    @staticmethod
    def blender_object(obj):
        if type(obj) is str:
            name = obj
            obj = bpy.data.objects.get(name)
            if obj is None:
                raise RuntimeError(f"Object '{name}' doesn't exist.")
        return obj
    
    @classmethod
    def Input(cls, name="Object"):
        return cls(Tree.current().new_input_socket('NodeSocketObject', name=name))
            
            
# -----------------------------------------------------------------------------------------------------------------------------
# Material

class Material(NodeSocket):

    @classmethod
    def Material(cls, name=None):
        if type(name) is str:
            mat = bpy.data.materials[name]
        else:
            mat = name
        return cls(mat).material

    
    @classmethod
    def Input(cls, name="Material"):
        return cls(Tree.current().new_input_socket('NodeSocketMaterial',  name=name))
    
# -----------------------------------------------------------------------------------------------------------------------------
# Other classes

class Texture(NodeSocket):

    @classmethod
    def Input(cls, name="Texture"):
        return cls(Tree.current().new_input_socket('NodeSocketTexture', name=name))
    
class Image(NodeSocket):
    
    @classmethod
    def Input(cls, name="Image"):
        return cls(Tree.current().new_input_socket('NodeSocketImage', name=name))
    
            
            
        
            
            


    
               
                
                



            
        
