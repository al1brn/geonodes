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
    """
    
    The Boolean initializer can take a python value as argument:        

    ```python
    a = Boolean(True) # a is the output socket of the input node Boolean initialized at True
    ```
    
    To get a Boolean value from the group input (see [Input constructor](#input)):
        
    ```python
    a = Boolean.Input(True, "Option")
    ```
        
    
    Python _bool_ operators such as ```and```, ```or``` or ```if ... else:  ...``` don't work on Boolean
    sockets. For each _bool_, one can use either a global function or a method of Boolean:
        
    ```python
    
    a = Boolean(False) # Two Boolean sockets
    b = Boolean(True)
    
    # Wrong:
    
    c = a and b # a and b transtyped to bool with bool(). c is not a Boolean but a bool
    print(type(c))  # returns <class 'bool'>
    
    # Correct
    
    c = a.b_and(b)
    print(type(c)) # returns <class 'Boolean'W
    
    ```
    
    Since, the python _bool_ operators, can't be used, the operator *, + and - can be used:
        

    ```python
    
    a = Boolean(False)
    b = Boolean(True)
    
    _ = a + b  # a or b
    _ = -a     # not a
    _ = a * b  # a and b
    
    # These operators also work with bool types
    
    _ = a * True  # a and True. True can be replaced by a bool variables computed elsewhere
    
    # Self change is also possible
    
    a *= b
    
    # a is now the output socket of the Boolean node math performing a and operation
    # between a and b
    
    
    ```
    
    """
    
    def __init__(self, value=False, label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Boolean(bool(value), label=label)
            super().__init__(node.boolean, node)
    
    @classmethod
    def Input(cls, value=False, name="Boolean", description=""):
        return cls(Tree.TREE.new_input('Boolean', value=value, name=name, description=description))
    
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
    def Input(cls, value=0, name="Integer", min_value=None, max_value=None, description=""):
        return cls(Tree.TREE.new_input('Integer', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    

    @classmethod
    def Unsigned(cls, value=0, name="Unsigned", min_value=0, max_value=None, description=""):
        return cls(Tree.TREE.new_input('Unsigned', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    

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
    def Input(cls, value="Text", name="String", description=""):
        return cls(Tree.TREE.new_input('String', value=value, name=name, description=description))
    
    @staticmethod
    def Tab(cls):
        return nodes.SpecialCharacters().tab
    
    @staticmethod
    def LineBreak(cls):
        return nodes.SpecialCharacters().line_break
    
    @staticmethod
    def Value(value=None, decimals=None):
        """ Initialize a String with a value
        
        <blid FunctionNodeValueToString>
        
        Parameters
        ----------
            - value: Value
                The value to convert
            - decimals: Integer
                The number fo decimals
        
        ```python
        s = gn.String.Value(...)
        ```
        """
        return nodes.ValueToString(value=value, decimals=decimals).string
    
    def join_strings(self, *strings, delimiter=None):
        """ Join strings with a delimiter
        
        <blid GeometryNodeStringJoin>
        
        This method must not be confused with ``delimiter.join(*strings)``.
            
        Parameters
        ----------
            - strings : array of Strings
            - delimiter : String
                The delimiter between the joined strings
            
        Returns
        -------
        String
            
        Example
        -------
            
        ```python
        s.join(s0, s1, s2, delimiter="-")
        ```
        """
        
        import geonodes as gn
        
        strs = [self] + list(strings)
        for i, s in enumerate(strs):
            if isinstance(s, str):
                strs[i] = gn.String(s)

        return self.stack(nodes.JoinStrings(*reversed(strs), delimiter=delimiter))
    
    def join(self, *strings):
        """ Join strings with the same use as in python
        
        <blid GeometryNodeStringJoin>
        
        This method must not be confused with ``string.join_strings(*strings, delimiter)``.
        ``join`` behaves as the homonym python str method
            
        Parameters
        ----------
            - strings: array of Strings
            
        Returns
        -------
        String
            
        Example
        -------
            
        ```python
        delimiter = gn.String("-")
        s = delimiter.join(s0, s1, s2)        
        ```
        """
        
        strs = list(strings)
        for i, s in enumerate(strs):
            if isinstance(s, str):
                strs[i] = gn.String(s)
        
        return nodes.JoinStrings(*reversed(strs), delimiter=self).string
    
    def __add__(self, other):
        return nodes.JoinStrings(other, self).string

    def __radd__(self, other):
        return nodes.JoinStrings(self, other).string
    
    def __iadd__(self, other):
        return self.join_strings(other)
    
    def __getitem__(self, index):
        if isinstance(index, int) or self.is_socket(index):
            return self.slice(position=index, length=1, node_label=f"{self}[{index}]")
        
        elif isinstance(index, slice):
            if index.start is None:
                return self.slice(position=0, length=index.stop, node_label=f"{self}[:{index.stop}]")
            elif index.stop is None:
                return self.slice(position=index.start, length=999, node_label=f"{self}[{index.start}:]")
            else:
                return self.slice(position=index.start, length=index.stop-index.start, node_label=f"{self}[{index.start}:{index.stop}]")
            
        else:
            raise Exceptionf(f"String[]: invalid index: {index}. INdex must be int or slice")
                
            
                
            
        
                
            
    
    
    
    
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
            
        # ----- Hack for implementing vector += value in set_position(offset=value)
        # See domains and fields
        
        self.offset_setter = None
            
    @classmethod
    def Input(cls, value=(0, 0, 0), name="Vector", description=""):
        return cls(Tree.TREE.new_input('Vector', value=value, name=name, description=description))
        
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
        if self.offset_setter is None:
            return self.stack(self.add(other).node)
        
        # ----- Hack to implement set_position(offeset = other)
        # see domain Point and fields Position and Handle
        
        self.offset_setter(other)
        return None
    

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
    def Input(cls, value="blank", name="Color", description=""):
        return cls(Tree.TREE.new_input('Color', value=value, name=name, description=description))
    
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
    
    def reset_properties(self):
        super().reset_properties()
        
    @property
    def component(self):
        """ > Component in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'VOLUME')
        
        return 'GEOMETRY' if not determined
        """
        
        table = {'Geometry': 'GEOMETRY', 'Mesh': 'MESH', 'Curve': 'CURVE', 'Spline': 'Curve', 'Instances': 'INSTANCES', 'Points': 'POINTCLOUD', 'Volume': 'VOLUME'}

        tp = tp(self.data_socket)
        if tp in table:
            return table[tp]
        else:
            raise Exception(f"INTERNAL ERROR: not component name for {type(self)}")
            
    @classmethod
    def Input(cls, name=None, description=""):
        if name is None:
            name = cls.__name__
        return cls(Tree.TREE.new_input('Geometry', name=name, description=description))
    
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
    
    # ----------------------------------------------------------------------------------------------------
    # Duplicate the geometry
    
    def duplicate(self, count=10, realize=True):
        
        import geonodes as gn
        
        with self.node.tree.layout(f"Duplicate * {count}", color='GENE'):
            line = gn.Mesh.Line(count=count)
            insts = gn.Points(line).instance_on_points(instance=self)
            if realize:
                return insts.realize()
            else:
                return insts
            
    def __mul__(self, other):
        if isinstance(other, int) or self.is_socket(other):
            return self.duplicate(count=other)
        
        raise Exception(f"A geometry can only be multiplied by an int")
        
    # ----------------------------------------------------------------------------------------------------
    # Visualize the handles
    
    def show_handles(self):
        
        import geonodes as gn
        
        if type(self).__name__ != 'Curve':
            raise Exception (f"‘{self}.show_handles: this method is only for Curve, not {type(self).__name__} ")
            
        with self.node.tree.layout("show handles", color='GENE'):

            n  = self.points.count
            
            vs = gn.Mesh.Line(offset=(1, 0, 0), count=n)
            vs.edges.delete_edges_faces()
            vs.verts.position = self.points.position.transfer_index
            vs.verts.extrude(offset=self.points.lefts(True).transfer_index)
            
            ctl = vs
                
            vs = gn.Mesh.Line(offset=(1, 0, 0), count=n)
            vs.edges.delete_edges_faces()
            vs.verts.position = self.points.position.transfer_index
            vs.verts.extrude(offset=self.points.rights(True).transfer_index)
            
            ctl = ctl + vs
            pts = gn.Mesh(ctl).to_points(radius=0.005)
                
            return self.join(ctl, pts)
        
    

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
    def Input(cls, name="Collection", description=""):
        return cls(Tree.TREE.new_input('Collection', name=name, description=description))
            
            
# -----------------------------------------------------------------------------------------------------------------------------
# Object

class Object(DataSocket):
    
    def __init__(self, obj=None):
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
    def Input(cls, name="Object", description=""):
        return cls(Tree.TREE.new_input('Object', name=name, description=description))
    
        
            
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
    def Input(cls, name="Material", description=""):
        return cls(Tree.TREE.new_input('Material', name=name, description=description))
    
# -----------------------------------------------------------------------------------------------------------------------------
# Other classes

class Texture(DataSocket):

    @classmethod
    def Input(cls, name="Texture", description=""):
        return cls(Tree.TREE.new_input('Texture', name=name, description=description))
    
class Image(DataSocket):
    
    @classmethod
    def Input(cls, name="Image", description=""):
        return cls(Tree.TREE.new_input('Image', name=name, description=description))
    
            
            
        
            
            


    
               
                
                



            
        
