#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:45:39 2022

@author: alain
"""

from geonodes.core.node import DataSocket, Tree, Node
from geonodes import nodes

import logging
logger = logging.getLogger('geonodes')

from typing import Any, Union


try:
    import bpy
except:
    pass

# =============================================================================================================================
# The base classes

# -----------------------------------------------------------------------------------------------------------------------------
# Boolean

class Boolean(DataSocket):
    """ DataSocket Boolean
    
    Args:
        value: Initial value
        label: Node label
    
    The Boolean initializer can take a python value as argument:      
        
    .. code-block:: python

        a = Boolean(True) # a is the output socket of the input node Boolean initialized at True
    
    To get a Boolean value from the group input (see [Input constructor](#input)):
        
    .. code-block:: python

        a = Boolean.Input(True, "Option")
        
    
    Python _bool_ operators such as ``and``, ``or`` or ``if ... else:  ...`` don't work on Boolean
    sockets. Rather use use either a global function or a method of Boolean:
        
    .. code-block:: python
    
        a = Boolean(False) # Two Boolean sockets
        b = Boolean(True)
        
        # Wrong:
        
        c = a and b # a and b transtyped to bool with bool(). c is not a Boolean but a bool
        print(type(c))  # returns <class 'bool'>
        
        # Correct
        
        c = a.b_and(b)
        print(type(c)) # returns <class 'Boolean'W
    
    Operator ``*``, ``+`` and ``-`` can be used for respectively ``and``, ``or`` and ``not``:
        

    .. code-block:: python
    
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
    
    """
    
    def __init__(self, value: bool = False, label: str = None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Boolean(bool(value), label=label)
            super().__init__(node.boolean, node)
    
    @classmethod
    def Input(cls, value: bool = False, name: str = "Boolean", description: str = ""):
        """ Create a Boolean input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Boolean: The Boolean data socket
        """
        
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
    
    def add(self, value1=None, node_label = None, node_color = None):
        """ Add two values.
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value1 is a Vector or a Color, VectorMath node is used rather than Math.
        """
        
        from geonodes import nodes
        
        if self.is_vector(value1):
            return nodes.VectorMath(vector0=self, vector1=value1, operation='ADD', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value1, operation='ADD', label=node_label, node_color=node_color).value

    def subtract(self, value1=None, node_label = None, node_color = None):
        """ Subtract two values.
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value1 is a Vector or a Color, VectorMath node is used rather than Math.
        """

        from geonodes import nodes
        
        if self.is_vector(value1):
            return nodes.VectorMath(vector0=self, vector1=value1, operation='SUBTRACT', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color).value

    def multiply(self, value1=None, node_label = None, node_color = None):
        """ Multiply two values.
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value1 is a Vector or a Color, VectorMath node is used rather than Math.
        """

        from geonodes import nodes
        
        if self.is_vector(value1):
            return nodes.VectorMath(vector0=self, vector1=value1, operation='MULTIPLY', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color).value

    def divide(self, value1=None, node_label = None, node_color = None):
        """ Divide two values.
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value1 is a Vector or a Color, VectorMath node is used rather than Math.
        """

        from geonodes import nodes
        
        if self.is_vector(value1):
            return nodes.VectorMath(vector0=self, vector1=value1, operation='DIVIDE', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color).value
    
    
    
    
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
    """ Integer DataSocket
    
    Args:
        value: Initial value
        label: Node label
        
    """
    
    def __init__(self, value=0, label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Integer(int(value))
            super().__init__(node.integer, node, label=label)
    
    @classmethod
    def Input(cls, value: int = 0, name: str = "Integer", min_value: int = None, max_value: int = None, description: str = ""):
        """ Create an Integer input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Integer: The Integer data socket
        """
        
        return cls(Tree.TREE.new_input('Integer', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    

    @classmethod
    def Unsigned(cls, value: int = 0, name: str = "Unsigned", min_value: int = 0, max_value: int = None, description: str = ""):
        """ Create an Unisgned Integer input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Integer: The Integer data socket
        """
        return cls(Tree.TREE.new_input('Unsigned', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    

# -----------------------------------------------------------------------------------------------------------------------------
# Float

class Float(IntFloat):
    """ Float DataSocket
    
    Args:
        value: Initial value
        label: Node label        
    """
    
    def __init__(self, value=0., label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Value(label=label)
            node.bnode.outputs[0].default_value = float(value)
            super().__init__(node.value, node)
    
    @classmethod
    def Input(cls, value: float = 0., name: str = "Float", min_value: float = None, max_value: float = None, description: str =""):
        """ Create a Float input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        """
        
        return cls(Tree.TREE.new_input('Float', value=value, name=name, min_value=min_value, max_value=max_value, description=description))
        
    @classmethod
    def Angle(cls, value=0., name="Angle", min_value: float = None, max_value: float = None, description: str =""):
        """ Create an Angle input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        """
        
        return cls(Tree.TREE.new_input('Angle', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    
        
    @classmethod
    def Factor(cls, value=0., name="Factor", min_value: float = 0., max_value: float = 1., description: str =""):
        """ Create a Factor input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        """
        
        return cls(Tree.TREE.new_input('Factor', value=value, name=name, min_value=min_value, max_value=max_value, description=description))
        
    @classmethod
    def Distance(cls, value=0., name="Distance", min_value: float = None, max_value: float = None, description: str =""):
        """ Create a Distance input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        """
        
        return cls(Tree.TREE.new_input('Distance', value=value, name=name, min_value=min_value, max_value=max_value, description=description))    

# -----------------------------------------------------------------------------------------------------------------------------
# String

class String(DataSocket):
    """ String DataSocket
    
    Args:
        value: Initial value
        label: Node label        
        
    String supports python slicing:
        
    .. code-block:: python
    
        s = String("ABCDEFGHIJK")
        
        a = s[3]   # Returns String("A")
        a = s[:3]  # Returns String("ABC")
        a = s[3:6] # Returns String("DEF")
        
        i = Integer(6)
        j = Integer(9)

        a = s[i:j] # Returns String("GHI")
    
    """
    
    def __init__(self, value: str = "Text", label: str = None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.String(str(value), label=label)
            super().__init__(node.string, node)
    
    @classmethod
    def Input(cls, value: str = "Text", name: str = "String", description: str = ""):
        """ Create a String input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Float: The Float data socket
        """
        return cls(Tree.TREE.new_input('String', value=value, name=name, description=description))
    
    @staticmethod
    def Tab(cls):
        """ The ``tab`` special character
        """
        return nodes.SpecialCharacters().tab
    
    @staticmethod
    def LineBreak(cls):
        """ The ``line break`` special character
        """
        return nodes.SpecialCharacters().line_break
    
    @staticmethod
    def Value(value: Float = None, decimals: Integer = None):
        """ String constructor : initialize a String from a numeric value
        
        Args:
            value: Value to convert
            decimals: Number of decimals
            
        .. code-block:: python
        
            s = String.Value(Float(12.34), decimal=2)
        
        .. blid:: FunctionNodeValueToString
        
        """
        return nodes.ValueToString(value=value, decimals=decimals).string
    
    def join_strings(self, *strings, delimiter = None):
        """ Join strings with a delimiter
        
        Args:
            strings (str, String): List of strings to join
            delimiter (str, String): Delimiter between the strings
            
        Returns:
            String: strings joined with the delimiter
            
        Note
        ----
            Here, the ``self`` String is used as the first String to join.
            In the methode :func:`join`, ``self`` acts as the delimiter.
            
            
        Example
        -------
            .. code-block:: python
            
                s0 = String("Demo")
                s1 = String("ABC")
                s2 = String("BCD")
                delimiter = String(", ")
                
                s = s0.join_strings(s1, s2, "EFG", delimiter=delimiter)
                
                # Is equivalent to the more *pythonic*:
                    
                s = delimiter.join(s0, s1, s2, "EFG")
        
        .. blid:: GeometryNodeStringJoin
        """
        
        import geonodes as gn
        
        strs = [self] + list(strings)
        for i, s in enumerate(strs):
            if isinstance(s, str):
                strs[i] = gn.String(s)

        return self.stack(nodes.JoinStrings(*reversed(strs), delimiter=delimiter))
    
    def join(self, *strings):
        """ Join strings using self as a delimiter
        
        Args:
            strings (str, String): Strings to join
            
        Returns:
            String: The strings joined with ``self`` as as delimiter.
            
        Note
        ----
            This method works the same as the python ``str.join()`` method. See :func:`join_strings` for
            another implementation.
        
            
        Example
        -------
            .. code-block:: python
            
                s0 = String("Demo")
                s1 = String("ABC")
                s2 = String("BCD")
                delimiter = String(", ")
                
                s = s0.join_strings(s1, s2, "EFG", delimiter=delimiter)
                
                # Is equivalent to the more *pythonic*:
                    
                s = delimiter.join(s0, s1, s2, "EFG")
        
        .. blid:: GeometryNodeStringJoin        
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
    """ Vector DataSocket
    
    Args:
        value (float, triplet, DataSocket): Initial value
        label (str): Node label
        
    Vector exposes properties: `x`, `y` and `z`:
        
    .. code-block: python
    
        v = Vector()
        v.x = 1
        v.y = 2
        
        geometry.verts.offset = v
        
        # The vertices have been translated of (1, 2, 0)
    
    """
    
    
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
            
        # ----- x, y, z components can be accessed individually
        
        self.x_ = None
        self.y_ = None
        self.z_ = None
            
        # ----- Hack for implementing vector += value in set_position(offset=value)
        # See domains and fields
        
        self.offset_setter = None
            
    @classmethod
    def Input(cls, value = (0, 0, 0), name: str = "Vector", description: str = ""):
        """ Create a Vector input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Vector: The Vector data socket
        """
        
        return cls(Tree.TREE.new_input('Vector', value=value, name=name, description=description))
        
    @classmethod
    def Rotation(cls, value = (0, 0, 0), name: str = "Rotation", description: str = ""):
        """ Create a Rotation input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Vector: The Vector data socket
        """
        return cls(Tree.TREE.new_input('Rotation', value=value, name=name, description=description))
        
    @classmethod
    def Translation(cls, value =(0, 0, 0), name: str = "Translation", description: str = ""):
        """ Create a Translation input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Vector: The Vector data socket
        """
        return cls(Tree.TREE.new_input('Translation', value=value, name=name, description=description))
        
    @classmethod
    def VectorXYZ(cls, value = (0, 0, 0), name: str = "VectorXYZ", description: str = ""):
        """ Create a Vector XYZ input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Vector: The Vector data socket
        """
        return cls(Tree.TREE.new_input('Xyz', value=value, name=name, description=description))
    
    # ---------------------------------------------------------------------------
    # x, y and z components
    
    @property
    def x(self):
        if self.x_ is None:
            return self.separate.x
        else:
            return self.x_
        
    @x.setter
    def x(self, value):
        self.x_ = value
        
    @property
    def y(self):
        if self.y_ is None:
            return self.separate.y
        else:
            return self.y_
        
    @y.setter
    def y(self, value):
        self.y_ = value
        
    @property
    def z(self):
        if self.z_ is None:
            return self.separate.z
        else:
            return self.z_
        
    @z.setter
    def z(self, value):
        self.z_ = value

    # ---------------------------------------------------------------------------
    # The x, y, z components can be changed individually. If it is the case
    # the vector must be combined before being used
    
    def get_blender_socket(self):
        """ Overrides the standard behavior of :class:DataSocket super class
        
        If the `x`, `y`, `z` properties have been read or modified, a *Combine XYZ* node is necessary
        to recompose the Vector.
        
        .. blid:: ShaderNodeCombineXYZ
        """
        
        if self.separate_ is None and self.x_ is None and self.y_ is None and self.z_ is None:
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
    
    # ---------------------------------------------------------------------------
    # Spherical
    
    def spherical(self, center=(0, 0, 0)):
        
        import geonodes as gn
        
        with self.node.tree.layout("Spherical coordinates"):
        
            v = self - center
            rho = v.length()
    
            z = v.z
            v.z = 0
            r = v.length()
            
            theta = v.y.arctan2(v.x)
            phi   = z.arctan2(r)
            
            return gn.Vector((rho, theta, phi))
    
    
    
# -----------------------------------------------------------------------------------------------------------------------------
# Color

class Color(DataSocket):
    """ Vector DataSocket
    
    Args:
        value (float, triplet, DataSocket): Initial value
        label (str): Node label
        
    Color exposes properties: `r`, `g` and `b`:
        
    .. code-block: python
    
        c = Color()
        c.r = .5
        c.g = .2
        
        
    Color supports some operators:
        
    +------------------------+----------------------------------+
    |         `+`            | add colors                       |
    +------------------------+----------------------------------+
    |         `*`            | mulitply colors                  |
    +------------------------+----------------------------------+
    |         `-`            | subtract colors                  |
    +------------------------+----------------------------------+
    |         `/`            | divide colors                    |
    +------------------------+----------------------------------+
    |         `%`            | mix colors                       |
    +------------------------+----------------------------------+
    
    """
    
    
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
                
        # ----- r, g, b components can be accessed individually
        
        self.r_ = None
        self.g_ = None
        self.b_ = None
                
    
    @classmethod
    def Input(cls, value="blank", name: str = "Color", description: str = ""):
        """ Create a Color input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            description: User tip
            
        Returns:
            Color: The Color data socket
        """
        
        return cls(Tree.TREE.new_input('Color', value=value, name=name, description=description))
    
    # ---------------------------------------------------------------------------
    # r, g and b components
    
    @property
    def r(self):
        if self.r_ is None:
            return self.separate.r
        else:
            return self.r_
        
    @r.setter
    def r(self, value):
        self.r_ = value
        
    @property
    def g(self):
        if self.g_ is None:
            return self.separate.g
        else:
            return self.g_
        
    @g.setter
    def g(self, value):
        self.g_ = value
        
    @property
    def b(self):
        if self.b_ is None:
            return self.separate.b
        else:
            return self.b_
        
    @b.setter
    def b(self, value):
        self.b_ = value    
    
    # ---------------------------------------------------------------------------
    # The r, g, b components can be changed individually. If it is the case
    # the color must be combined before being used
    
    def get_blender_socket(self):
        """ Overrides the standard behavior of :class:DataSocket super class
        
        If the `r`, `g`, `b` properties have been read or modified, a *Combine RGB* node is necessary
        to recompose the Color.
        
        .. blid:: ShaderNodeCombineRGB
        """
        
        if self.separate_ is None and self.r_ is None and self.g_ is None and self.b_ is None:
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
    """ Geometry DataSocket
    
    Geometry supports the ``+`` operator acting as method :func:`Geometry.join`.
    
    .. code-block:: python
    
        geo1 = Geometry.Input("geometry to join")
        tree.output_geometry = tree.input_geometry + geo1
    
    """
    
    def __init__(self, socket, node=None, label=None):
        
        from geonodes.core.domains import Point
        
        self.points = Point(self) # Initialized befor super().__init__ which can override points
        
        super().__init__(socket, node=node, label=label)
    
    
    def reset_properties(self):
        
        super().reset_properties()
        
        
    @property
    def component_OLD(self):
        """ Component in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'VOLUME')
        
        return 'GEOMETRY' if not determined
        """
        
        table = {'Geometry': 'GEOMETRY', 'Mesh': 'MESH', 'Curve': 'CURVE', 'Spline': 'CURVE', 'Instances': 'INSTANCES', 'Points': 'POINTCLOUD', 'Volume': 'VOLUME'}

        tp = tp(self.data_socket)
        if tp in table:
            return table[tp]
        else:
            raise Exception(f"INTERNAL ERROR: not component name for {type(self)}")
            
    @classmethod
    def Input(cls, name: str = None, description: str = ""):
        """ Create a Geometry input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Geometry: The Geometry data socket
            
        Note
        ----
            This method create a new input socket in the Group Input node. To get the **default** input geometry,
            use :attr:`Tree.input_geometry`.
            
        """
        if name is None:
            name = cls.__name__
        return cls(Tree.TREE.new_input('Geometry', name=name, description=description))
    
    @classmethod
    def FromCollection(cls, collection=None, separate_children: bool = None, reset_children: bool = None, transform_space: str = 'ORIGINAL'):
        """ Get the geometry from a collection
        
        .. blid:: GeometryNodeCollectionInfo
        """
        if isinstance(collection, str):
            coll = bpy.data.collection[collection]
        else:
            coll = collection
        return cls(nodes.CollectionInfo(collection=coll, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).outputs[0])
    

    # -----------------------------------------------------------------------------------------------------------------------------
    # Join operators
    
    def __add__(self, other):
        if self.node.bl_idname == 'GeometryNodeJoinGeometry':
            self.node.plug(0, other)
            return self
        return self.join(other)
    
    def __radd__(self, other):
        return other.join(self.socket)
    
    #def __iadd__(self, other):
    #    if self.node.bl_idname == 'GeometryNodeJoinGeometry':
    #        self.node.plug(0, other)
    #        return self
    #    return self.stack(self.add(other).node)
    
    # ----------------------------------------------------------------------------------------------------
    # Duplicate the geometry
    
    def duplicate(self, count: int = 10, realize: bool = True):
        """ Duplicate the geometry
        
        Args:
            count: Number of instances to create
            realize: True to realize the instances
            
        Returns:
            Instances or Geometry
            
        The duplication is performed by instantiating the geometry along the vertices
        of a Mesh Line initialized with `count` points.
        
        The operator ``*`` can be used to operate this method with `realize = True`:
            
        .. code-block::
            
            curves = curve * 10
            
            # is equivalent to
            
            curves = curve.duplicate(10, realize=True)
            
        """
        
        import geonodes as gn
        
        with self.node.tree.layout(f"Duplicate * {count}", color='GENE'):
            line = gn.Mesh.Line(count=count)
            insts = gn.Points(line).instance_on_points(instance=self)
            if realize:
                return type(self)(insts.realize())
            else:
                return insts
            
    def __mul__(self, other):
        if isinstance(other, int) or self.is_socket(other):
            return self.duplicate(count=other)
        
        raise Exception(f"A geometry can only be multiplied by an int")
        
    # ----------------------------------------------------------------------------------------------------
    # Visualize the handles
    
    def show_handles(self):
        """ Generate a mesh and cloud points to visualize the control points and handles
        
        Returns:
            Geometry: The geometry can be joined to the output
            
        Example:
            
            .. code-block:: python
            
                curve = ... # Curve initialization
                
                visu = curve.show_handles()
                
                tree.output_geometry = curve + visu
            
        """
        
        import geonodes as gn
        
        if type(self).__name__ != 'Curve':
            raise Exception (f"‘{self}.show_handles: this method is only for Curve, not {type(self).__name__} ")
            
        with self.node.tree.layout("show handles", color='GENE'):

            n  = self.points.count
            
            vs = gn.Mesh.Line(offset=(1, 0, 0), count=n)
            vs.edges.delete_edges_faces()
            #vs.verts.extrude(offset=self.points.lefts(True).transfer_index)

            vs.verts.position = self.points.position.index_transfer()
            vs.verts.extrude(offset=self.points.handle_positions(True).left.index_transfer())
            
            ctl = vs
                
            vs = gn.Mesh.Line(offset=(1, 0, 0), count=n)
            vs.edges.delete_edges_faces()

            vs.verts.position = self.points.position.index_transfer()
            vs.verts.extrude(offset=self.points.handle_positions(True).right.index_transfer())
            
            ctl = ctl + vs
            pts = gn.Mesh(ctl).to_points(radius=0.005)
                
            return self.join(ctl, pts)
        
        
        
    

# -----------------------------------------------------------------------------------------------------------------------------
# Collection

class Collection(DataSocket):
    """ Collection DataSocket
    
    Args
        bcoll (bpt.types.Collection, str): NodeSocketCollection, Collection or collection name    
    """
    
    def __init__(self, bcoll):
        if isinstance(bcoll, bpy.types.NodeSocketCollection):
            super().__init__(bcoll)
        else:
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
        """ Create a Collection input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Collection: The Collection data socket
        """
        
        return cls(Tree.TREE.new_input('Collection', name = name, description = description))
            
            
# -----------------------------------------------------------------------------------------------------------------------------
# Object

class Object(DataSocket):
    """ Collection DataSocket
    
    Args
        obj (bpt.types.Object, str): NodeSocketObject or Object or object name    
    """
    
    def __init__(self, obj=None):
        if isinstance(obj, bpy.types.NodeSocketObject) or self.is_socket(obj):
            super().__init__(obj)
        else:
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
        """ Create an Object input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Object: The Object data socket
        """
        
        return cls(Tree.TREE.new_input('Object', name=name, description=description))
            
# -----------------------------------------------------------------------------------------------------------------------------
# Material

class Material(DataSocket):
    """ Material DataSocket
    """

    @classmethod
    def Material(cls, name: str = None):
        """ Create a Material
        
        Args:
            name: Material name
        """
        if type(name) is str:
            mat = bpy.data.materials[name]
        else:
            mat = name
        return cls(mat).material

    
    @classmethod
    def Input(cls, name="Material", description=""):
        """ Create a Material input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Material: The Material data socket
        """
        
        return cls(Tree.TREE.new_input('Material', name=name, description=description))
    
# -----------------------------------------------------------------------------------------------------------------------------
# Other classes

class Texture(DataSocket):

    @classmethod
    def Input(cls, name="Texture", description=""):
        """ Create a Texture input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Texture: The Texture data socket
        """
        
        return cls(Tree.TREE.new_input('Texture', name=name, description=description))
    
class Image(DataSocket):
    
    @classmethod
    def Input(cls, name="Image", description=""):
        """ Create an Image input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Image: The Image data socket
        """
        
        return cls(Tree.TREE.new_input('Image', name=name, description=description))
    
            
            
        
            
            


    
               
                
                



            
        
