#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:45:39 2022

@author: alain
"""

from geonodes.core.node import DataSocket, Tree, Node
from geonodes import nodes

import bpy

import logging
logger = logging.getLogger('geonodes')


# =============================================================================================================================
# The base classes

# -----------------------------------------------------------------------------------------------------------------------------
# Boolean

class Boolean(DataSocket):
    
    def __init__(self, value=False, label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Boolean(bool(value), label=label)
            super().__init__(node.boolean, node)
    
    @classmethod
    def Input(cls, value=False, name="Boolean"):
        return cls(Tree.TREE.new_input('Boolean', value=value, name=name))
    
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

class IntFloat(DataSocket):
    
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
        return self.subtract(other)
    
    def __rsub__(self, other):
        ret = self.subtract(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __isub__(self, other):
        return self.stack(self.subtract(other).node)
    
    
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
    
    def __init__(self, value=0, label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Integer(int(value))
            super().__init__(node.integer, node, label=label)
    
    @classmethod
    def Input(cls, value=0, name="Integer"):
        return cls(Tree.TREE.new_input('Integer', value=value, name=name))    

    @classmethod
    def Unsigned(cls, value=0, name="Unsigned"):
        return cls(Tree.TREE.new_input('Unsigned', value=value, name=name))    

# -----------------------------------------------------------------------------------------------------------------------------
# Float

class Float(IntFloat):
    
    def __init__(self, value=0., label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Value(label=label)
            node.bnode.outputs[0].default_value = float(value)
            super().__init__(node.value, node)
    
    @classmethod
    def Input(cls, value=0., name="Float", min_value=None, max_value=None, description=""):
        return cls(Tree.TREE.new_input('Float', value=value, name=name, min_value=min_value, max_value=max_value, description=description))
        
    @classmethod
    def Angle(cls, value=0., name="Angle", min_value=None, max_value=None, description=""):
        return cls(Tree.TREE.new_input('Angle', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    
        
    @classmethod
    def Factor(cls, value=0., name="Factor", min_value=0, max_value=1, description=""):
        return cls(Tree.TREE.new_input('Factor', value=value, name=name, min_value=min_value, max_value=max_value, description=description))
        
    @classmethod
    def Distance(cls, value=0., name="Distance", min_value=None, max_value=None, description=""):
        return cls(Tree.TREE.new_input('Distance', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    

# -----------------------------------------------------------------------------------------------------------------------------
# String

class String(DataSocket):
    
    def __init__(self, value="Text", label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.String(str(value), label=label)
            super().__init__(node.string, node)
    
    @classmethod
    def Input(cls, value="Text", name="String"):
        return cls(Tree.TREE.new_input('String', value=value, name=name))
    
    @classmethod
    def Tab(cls):
        return cls(nodes.SpecialCharacters().tab)
    
    @classmethod
    def LineBreak(cls):
        return cls(nodes.SpecialCharacters().line_break)
    
    def __add__(self, other):
        return String(nodes.JoinStrings(self, other).outputs[0])

    def __radd__(self, other):
        return String(nodes.JoinStrings(other, self).outputs[0])
    
    def __iadd__(self, other):
        return self.stack(nodes.JoinStrings(self, other))
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Vector

class Vector(DataSocket):
    
    def __init__(self, value=(0., 0., 0.), label=None):
        
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
            
        else:
            if isinstance(value, (list, tuple)):
                if len(value) != 3:
                    raise RuntimeError(f"A Vector must be initialized with arrays of 3 items, not {len(value)}: {value}")
                x, y, z = value
            else:
                x, y, z = (value, value, value)
                
            node = nodes.CombineXyz(x=x, y=y, z=z, label=label)

            super().__init__(node.vector, node)
            
    @classmethod
    def Input(cls, value=(0, 0, 0), name="Vector"):
        return cls(Tree.TREE.new_input('Vector', value=value, name=name))
        
    @classmethod
    def Rotation(cls, value=(0, 0, 0), name="Rotation"):
        return cls(Tree.TREE.new_input('Rotation', value=value, name=name))
        
    @classmethod
    def Translation(cls, value=(0, 0, 0), name="Translation"):
        return cls(Tree.TREE.new_input('Translation', value=value, name=name))
        
    @classmethod
    def VectorXYZ(cls, value=(0, 0, 0), name="VectorXYZ"):
        return cls(Tree.TREE.new_input('Xyz', value=value, name=name))
    
    # ---------------------------------------------------------------------------
    # The x, y, z components can be changed individually. If it is the case
    # the vector must be combined before being used
    
    def get_blender_socket(self):
        
        if self.separate_ is None:
            return super().get_blender_socket()
        
        else:
            node = nodes.CombineXyz(x=self.x, y=self.y, z=self.z, label=f"{self.node.chain_label}.combine")
            self.stack(node)
            return super().get_blender_socket()
        
    # ---------------------------------------------------------------------------
    # Vector operators
    
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
        return self.subtract(other)
    
    def __rsub__(self, other):
        ret = self.subtract(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __isub__(self, other):
        return self.stack(self.subtract(other).node)
    
    
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
    
# -----------------------------------------------------------------------------------------------------------------------------
# Color

class Color(DataSocket):
    
    def __init__(self, value=None, label=None):

        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
            
        else:
            if value is None:
                node = nodes.Color()
                node.label = label
                super().__init__(node.color, node)

            else:
                if isinstance(value, (list, tuple)):
                    if len(value) != 3:
                        raise RuntimeError(f"A Color must be initialized with arrays of 3 items, not {len(value)}: {value}")
                    r, g, b = value
                else:
                    r, g, b = (value, value, value)
                
                node = nodes.CombineRgb(r=r, g=g, b=b, label=label)
                super().__init__(node.image, node)
    
    @classmethod
    def Input(cls, name="Color"):
        return cls(Tree.TREE.new_input('Color', value=value, name=name))
    
    # ---------------------------------------------------------------------------
    # The r, g, b components can be changed individually. If it is the case
    # the color must be combined before being used
    
    def get_blender_socket(self):
        if self.separate_ is None:
            return super().get_blender_socket()
        
        else:
            node = nodes.CombineRgb(r=self.r, g=self.g, b=self.b, label=f"{self.node.chain_label}.combine")
            self.stack(node)
            return super().get_blender_socket()
        
    # ---------------------------------------------------------------------------
    # Color operators
    # just for fun
    
    def __neg__(self):
        return 1. - self


    def __add__(self, other):
        return self.add(other)
    
    def __radd__(self, other):
        ret = self.add(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __iadd__(self, other):
        return self.stack(self.add(other).node)
    

    def __sub__(self, other):
        return self.subtract(other)
    
    def __rsub__(self, other):
        ret = self.subtract(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __isub__(self, other):
        return self.stack(self.subtract(other).node)
    
    
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
        return self.mix(other)
    
    def __rmod__(self, other):
        ret = self.mix(other)
        ret.node.switch_input_sockets(0, 1)
        return ret
    
    def __imod__(self, other):
        return self.stack(self.mix(other).node)        
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Geometry

class Geometry(DataSocket):
    
    @classmethod
    def Input(cls, name=None):
        if name is None:
            name = cls.__name__
        return cls(Tree.TREE.new_input('Geometry', name=name))
    
    @classmethod
    def FromCollection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        if isinstance(collection, str):
            coll = bpy.data.collection[collection]
        else:
            coll = collection
        return cls(nodes.CollectionInfo(collection=coll, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).outputs[0])
    
    def __add__(self, other):
        if self.node.bl_idname == 'GeometryNodeJoinGeometry':
            self.node.plug(0, other)
            return self
        return self.join(other)
    
    def __radd__(self, other):
        return other.join(self.socket)
    
    def __iadd__(self, other):
        if self.node.bl_idname == 'GeometryNodeJoinGeometry':
            self.node.plug(0, other)
            return self
        return self.stack(self.add(other).node)
    

# -----------------------------------------------------------------------------------------------------------------------------
# Collection

class Collection(DataSocket):
    
    def __init__(self, bcoll):
        super().__init__(None)
        self.bcollection = Collection.blender_collection(bcoll)
    
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
        return cls(Tree.TREE.new_input('Collection', name=name))
            
            
# -----------------------------------------------------------------------------------------------------------------------------
# Object

class Object(DataSocket):
    
    def __init__(self, obj):
        super().__init__(None)
        self.bobject = Object.blender_object(obj)
        
    
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
        return cls(Tree.TREE.new_input('Object', name=name))
    
        
            
# -----------------------------------------------------------------------------------------------------------------------------
# Material

class Material(DataSocket):

    @classmethod
    def Material(cls, name=None):
        if type(name) is str:
            mat = bpy.data.materials[name]
        else:
            mat = name
        return cls(mat).material

    
    @classmethod
    def Input(cls, name="Material"):
        return cls(Tree.TREE.new_input('Material', name=name))
    
# -----------------------------------------------------------------------------------------------------------------------------
# Other classes

class Texture(DataSocket):

    @classmethod
    def Input(cls, name="Texture"):
        return cls(Tree.TREE.new_input('Texture', name=name))
    
class Image(DataSocket):
    
    @classmethod
    def Input(cls, name="Image"):
        return cls(Tree.TREE.new_input('Image', name=name))
    
            
            
        
            
            


    
               
                
                



            
        
