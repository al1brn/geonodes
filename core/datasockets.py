#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:45:39 2022

@author: alain
"""

from geonodes.core.socket import DataSocket
from geonodes.core.node import Node
from geonodes.core.tree import Tree

from geonodes.nodes import nodes

import logging
logger = logging.getLogger('geonodes')


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
    
    The Boolean initializer can take a python value as argument:      
        
    ```python
    a = Boolean(True) # a is the output socket of the input node Boolean initialized at True
    ```
    
    To get a Boolean value from the group input (see [Input constructor](#input)):
        
    ```python
    a = Boolean.Input(True, "Option")
    ```
    
    Python _bool_ operators such as ``and``, ``or`` or ``if ... else:  ...`` don't work on Boolean
    sockets. Rather use use either a global function or a method of Boolean:
        
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
    
    Operator ``*``, ``+`` and ``-`` can be used for respectively ``and``, ``or`` and ``not``:
        
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
    
    def __init__(self, value = False, label = None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Boolean(bool(value), label=label)
            super().__init__(node.boolean, node)
    
    @classmethod
    def Input(cls, value = False, name = "Boolean", description = ""):
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
    
    def add(self, value=None, node_label = None, node_color = None):
        """ Add two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        """
        
        from geonodes import nodes
        
        if self.is_vector(value):
            return nodes.VectorMath(vector0=self, vector1=value, operation='ADD', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value, operation='ADD', label=node_label, node_color=node_color).value

    def subtract(self, value=None, node_label = None, node_color = None):
        """ Subtract two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        """

        from geonodes import nodes
        
        if self.is_vector(value):
            return nodes.VectorMath(vector0=self, vector1=value, operation='SUBTRACT', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value, operation='SUBTRACT', label=node_label, node_color=node_color).value
    
    def sub(self, value=None, node_label = None, node_color = None):
        return self.subtract(value=value)

    def multiply(self, value=None, node_label = None, node_color = None):
        """ Multiply two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        """

        from geonodes import nodes
        
        if self.is_vector(value):
            return nodes.VectorMath(vector0=value, scale=self, operation='SCALE', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value, operation='MULTIPLY', label=node_label, node_color=node_color).value
    
    def mul(self, value=None, node_label = None, node_color = None):
        return self.multiply(value=value)

    def divide(self, value=None, node_label = None, node_color = None):
        """ Divide two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        """

        from geonodes import nodes
        
        if self.is_vector(value):
            return nodes.VectorMath(vector0=self, vector1=value, operation='DIVIDE', label=node_label, node_color=node_color).vector

        return nodes.Math(value0=self, value1=value, operation='DIVIDE', label=node_label, node_color=node_color).value
    
    def div(self, value=None, node_label = None, node_color = None):
        return self.divide(value=value)
    
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
    """
    
    def __init__(self, value=0, label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Integer(int(value))
            super().__init__(node.integer, node, label=label)
    
    @classmethod
    def Input(cls, value = 0, name = "Integer", min_value = None, max_value = None, description = ""):
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
    def Unsigned(cls, value = 0, name = "Unsigned", min_value = 0, max_value = None, description = ""):
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
    
    """
    
    def __init__(self, value=0., label=None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.Value(label=label)
            node.bnode.outputs[0].default_value = float(value)
            super().__init__(node.value, node)
    
    @classmethod
    def Input(cls, value = 0., name = "Float", min_value = None, max_value = None, description =""):
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
    def Angle(cls, value=0., name="Angle", min_value = None, max_value = None, description =""):
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
    def Factor(cls, value=0., name="Factor", min_value = 0., max_value = 1., description =""):
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
    def Distance(cls, value=0., name="Distance", min_value = None, max_value = None, description =""):
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
    String supports python slicing:
        
    ```python
    s = String("ABCDEFGHIJK")
    
    a = s[3]   # Returns String("A")
    a = s[:3]  # Returns String("ABC")
    a = s[3:6] # Returns String("DEF")
    
    i = Integer(6)
    j = Integer(9)

    a = s[i:j] # Returns String("GHI")
    ```
    """
    
    def __init__(self, value = "Text", label = None):
        if DataSocket.gives_bsocket(value):
            super().__init__(value, label=label)
        else:
            node = nodes.String(str(value), label=label)
            super().__init__(node.string, node)
    
    @classmethod
    def Input(cls, value = "Text", name = "String", description = ""):
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
    def Value(value = None, decimals = None):
        """ String constructor : initialize a String from a numeric value
        
        Args:
            value: Value to convert
            decimals: Number of decimals
            
        ```python
        s = String.Value(Float(12.34), decimal=2)
        
        """
        return nodes.ValueToString(value=value, decimals=decimals).string
    
    def join_strings(self, *strings, delimiter = None):
        """ Join strings with a delimiter
        
        Args:
            strings (str, String): List of strings to join
            delimiter (str, String): Delimiter between the strings
            
        Returns:
            String: strings joined with the delimiter
            
        > Note: Here, the `self` String is used as the first String to join.
          In the method `join`, `self` acts as the delimiter.
          
        **Example**
        
        ```python
        s0 = String("Demo")
        s1 = String("ABC")
        s2 = String("BCD")
        delimiter = String(", ")
        
        s = s0.join_strings(s1, s2, "EFG", delimiter=delimiter)
        
        # Is equivalent to the more *pythonic*:
            
        s = delimiter.join(s0, s1, s2, "EFG")    
        ```
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
            
        > Note: This method works the same as the python ``str.join()`` method. See :func:`join_strings` for
          another implementation.
        
            
        **Example**

        ```python
        s0 = String("Demo")
        s1 = String("ABC")
        s2 = String("BCD")
        delimiter = String(", ")
        
        s = s0.join_strings(s1, s2, "EFG", delimiter=delimiter)
        
        # Is equivalent to the more *pythonic*:
            
        s = delimiter.join(s0, s1, s2, "EFG")    
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
    """ Vector DataSocket
    
    Vector exposes properties: `x`, `y` and `z`:
        
    ```python
    v = Vector()
    v.x = 1
    v.y = 2
    
    # Translate the vertices have been translated of (1, 2, 0)
    geometry.verts.offset = v    
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
    def Input(cls, value = (0, 0, 0), name = "Vector", description = ""):
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
    def Rotation(cls, value = (0, 0, 0), name = "Rotation", description = ""):
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
    def Translation(cls, value =(0, 0, 0), name = "Translation", description = ""):
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
    def VectorXYZ(cls, value = (0, 0, 0), name = "VectorXYZ", description = ""):
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
        """
        
        if hasattr(self, 'bypass_gbs') or ((not hasattr(self, '_c_separate')) and self.x_ is None and self.y_ is None and self.z_ is None):
            return super().get_blender_socket()
        
        else:
            self.bypass_gbs = True
            node = nodes.CombineXyz(x=self.x, y=self.y, z=self.z, label=f"{self.node.chain_label}.combine")
            self.stack(node)
            del self.bypass_gbs
            
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
    """ Color DataSocket
    
    Args:
        value (float, triplet, DataSocket): Initial value
        label (str): Node label
        
    Color exposes properties: `red`, `green` and `blue`, `hue`, `value`, 'lightness`, 'saturation` and `alpha`:
        
    ```python
    c = Color()
    c.red = .5
    c.saturation = .2
    ```
        
        
    Color supports some operators:
        
    |    Operator            | Mix mode    | Method                             |
    |------------------------|-------------|------------------------------------|
    |         `+`            | ADD         | [mix_add](#mix_add)                |
    |         `*`            | MULTIPLY    | [mix_multiply](#mix_multiply)      |
    |         `-`            | DIFFERENCE  | [mix_difference](#mix_difference)  |
    |         `/`            | DIVIDE      | [mix_divide](#mix_divide)          |
    |         `%`            | MIX         | [mix](#mix)                        |
    
    """
    
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix',              ),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_darken',       blend_type="'DARKEN'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_multiply',     blend_type="'MULTIPLY'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_burn',         blend_type="'BURN'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_lighten',      blend_type="'LIGHTEN'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_screen',       blend_type="'SCREEN'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_dodge',        blend_type="'DODGE'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_add',          blend_type="'ADD'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_overlay',      blend_type="'OVERLAY'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_soft_light',   blend_type="'SOFT_LIGHT'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_linear_light', blend_type="'LINEAR_LIGHT'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_difference',   blend_type="'DIFFERENCE'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_subtract',     blend_type="'SUBTRACT'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_divide',       blend_type="'DIVIDE'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_hue',          blend_type="'HUE'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_saturation',   blend_type="'SATURATION'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_color',        blend_type="'COLOR'"),
            Method(ret_socket='result', a='self', data_type="'RGBA'", factor_mode="'UNIFORM'", arg_rename={'b':'color'}, fname='mix_value',        blend_type="'VALUE'"),
    
    
    
    
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
                    if len(value) not in (3, 4):
                        raise RuntimeError(f"A Color must be initialized with arrays of 3 or 4 items, not {len(value)}: {value}")
                    
                    if len(value) == 3:
                        r, g, b = value
                        a = 1
                    else:
                        r, g, b, a = value
                        
                else:
                    r, g, b, a = (value, value, value, 1)
                
                node = nodes.CombineColor(red=r, green=g, blue=b, alpha=a, mode='RGB', label=label)
                super().__init__(node.color, node)
                
        # ----- r, g, b components can be accessed individually
        # SeparateRGB is deprecated in Blender 3.3
        
        #self.r_ = None
        #self.g_ = None
        #self.b_ = None
        
        # Cache
        
        self.reset_cache()
        
        
    def reset_cache(self):
        
        self._separate_RGB = None # 3 possible read modes
        self._separate_HSV = None
        self._separate_HSL = None
        
        self._red          = None # RGB Components
        self._green        = None
        self._blue         = None
        
        self._hue          = None # HSV components
        self._saturation   = None
        self._value        = None
        
        self._lightness    = None # L component
        
        self._alpha        = None # Alpha component
        
                
    
    @classmethod
    def Input(cls, value=None, name = "Color", description = ""):
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
    # DEPRECATED : separate_RGB is replaced by separate_color
    

    # ---------------------------------------------------------------------------
    # Is modified
    
    @property
    def rgb_modified(self):
        return (self._red is not None) or (self._green is not None) or (self._blue is not None)
    
    @property
    def hs_modified(self):
        return (self._hue is not None) or (self._saturation is not None)
    
    @property
    def v_modified(self):
        return self._value is not None
    
    @property
    def l_modified(self):
        return self._lightness is not None
    
    @property
    def a_modified(self):
        return self._alpha is not None
    
    @property
    def is_modified(self):
        return self.rgb_modified or self.hs_modified or self.v_modified or self.l_modified or self.a_modified

    
    # ---------------------------------------------------------------------------
    # Recompose the nodes from its modified components
    #
    # If for_mode is not in RGB, HSV, HSL, the recomposition is forced
    
    def recompose(self, for_modes=()):
        
        if hasattr(self, 'no_loop'):
            return
        
        # ---------------------------------------------------------------------------
        # What is the current modified mode ?
        
        # ----- lightness: HSL mode
        
        if self.l_modified:
            cur_mode = ('HSL',)
            
        # ----- value: HSV mode
            
        elif self.v_modified:
            cur_mode = ('HSV',)
            
        # ----- hue, saturation : HSL or HSV
                
        elif self.hs_modified:
            cur_mode = ('HSV', 'HSL')
                
        # ----- rgb
            
        elif self.rgb_modified:
            cur_mode = ('RGB',)
            
        # ----- alpha
        
        elif self.a_modified:
            cur_mode = ('RGB', 'HSV', 'HSL')
            
        # ----- No modification
        
        else:
            return self
        
        # ---------------------------------------------------------------------------
        # Is the current mode compatible with the target modes
        
        if hasattr(for_modes, '__len__'):
            for mode in for_modes:
                if mode in cur_mode:
                    return self
        else:
            if for_modes in cur_mode:
                return self
            
        # ---------------------------------------------------------------------------
        # We have to recompose the color
        
        self.no_loop = True
        
        mode = cur_mode[0]
        
        if mode == 'RGB':
            node = nodes.CombineColor(red=self.red, green=self.green, blue=self.blue, alpha=self.alpha, mode='RGB')
        
        elif mode == 'HSV':
            node = nodes.CombineColor(red=self.hue, green=self.saturation, blue=self.value, alpha=self.alpha, mode='HSV')

        else:
            node = nodes.CombineColor(red=self.hue, green=self.saturation, blue=self.lightness, alpha=self.alpha, mode='HSL')
            
        del self.no_loop
        
        self.reset_cache()
            
        return self.stack(node)
                
    # ---------------------------------------------------------------------------
    # Separate color
    
    def separate(self, mode='RGB'):
        
        self.recompose(for_modes=mode)
        
        if mode == 'RGB':
            if self._separate_RGB is None:
                self._separate_RGB = self.separate_color(mode=mode)
                
            return self._separate_RGB
        
        elif mode == 'HSV':
            if self._separate_HSV is None:
                self._separate_HSV = self.separate_color(mode=mode)
                
            return self._separate_HSV
            
        elif mode == 'HSL':
            if self._separate_HSL is None:
                self._separate_HSL = self.separate_color(mode=mode)
                
            return self._separate_HSL
        
    # ---------------------------------------------------------------------------
    # 3 possible separations
    
    @property
    def separate_RGB(self):
        """ Separate RGB
        
        Returns:
            node with sockets red, green, blue, alpha
        """
        return self.separate('RGB')
        
    @property
    def separate_HSV(self):
        """ Separate HSV
        
        Returns:
            node with sockets hue, saturation, value, alpha
        """
        return self.separate('HSV')
        
    @property
    def separate_HSL(self):
        """ Separate HSL
        
        Returns:
            node with sockets hue, saturation, lightness, alpha
        """
        return self.separate('HSL')
    
        
    # ---------------------------------------------------------------------------
    # The indivividual components
    # CAUTION : node input sockets are named red, green, blue for all modes
    
    # ----- RGB
    
    @property
    def red(self):
        """ Red compenent
        """
        self.recompose('RGB')
        
        if self._red is None:
            return self.separate('RGB').red
        else:
            return self._red
        
    @red.setter
    def red(self, value):
        self._red = value
        
    @property
    def green(self):
        """ Green compenent
        """
        self.recompose('RGB')
        
        if self._green is None:
            return self.separate('RGB').green
        else:
            return self._green
        
    @green.setter
    def green(self, value):
        self._green = value
        
    @property
    def blue(self):
        """ Blue compenent
        """
        self.recompose('RGB')
        
        if self._blue is None:
            return self.separate('RGB').blue
        else:
            return self._blue
        
    @blue.setter
    def blue(self, value):
        self._blue = value
        
    # ----- HSV
    
    @property
    def hue(self):
        """ Hue compenent
        """
        
        self.recompose(('HSV', 'HSL'))
        
        if self._hue is None:
            if self._separate_HSL is None:
                return self.separate('HSV').red
            else:
                return self._separate_HSL.red
        else:
            return self._hue
        
    @hue.setter
    def hue(self, value):
        self._hue = value
        
    @property
    def saturation(self):
        """ Saturation compenent
        """
        self.recompose(('HSV', 'HSL'))
        
        if self._saturation is None:
            if self._separate_HSL is None:
                return self.separate('HSV').green
            else:
                return self._separate_HSL.green
                
        else:
            return self._saturation
        
    @saturation.setter
    def saturation(self, value):
        self._saturation = value
        
    @property
    def value(self):
        """ Value compenent
        """
        self.recompose('HSV')
        
        if self._value is None:
            return self.separate('HSV').blue
        else:
            return self._value
        
    @value.setter
    def value(self, value):
        self._value = value
        
    # ----- Lightness
    
    @property
    def lightness(self):
        """ Lightness compenent
        """
        self.recompose('HSL')
        
        if self._lightness is None:
            return self.separate('HSL').blue
        else:
            return self._lightness
        
    @lightness.setter
    def lightness(self, value):
        self._lightness = value
    
    
    # ----- Alpha
    
    @property
    def alpha(self):
        """ Alpha compenent
        """
        if self._alpha is None:
            
            if self._separate_HSV is not None:
                return self._separate_HSV.alpha
            
            if self._separate_HSL is not None:
                return self._separate_HSL.alpha

            return self.separate('RGB').alpha
                
        else:
            return self._alpha
        
    @alpha.setter
    def alpha(self, value):
        self._alpha = value
    
    # ---------------------------------------------------------------------------
    # The r, g, b components can be changed individually. If it is the case
    # the color must be combined before being used
    
    def get_blender_socket(self):
        """ Overrides the standard behavior of :class:DataSocket super class
        
        If the `r`, `g`, `b` properties have been read or modified, a *Combine RGB* node is necessary
        to recompose the Color.
        
        .. blid:: ShaderNodeCombineRGB
        """
        
        if not self.is_modified or hasattr(self, 'bypass_gbs'):
            return super().get_blender_socket()
        
        self.bypass_gbs = True # To avoid infinite loop
        self.recompose()
        del self.bypass_gbs
            
        return super().get_blender_socket()
        
            
        
        if hasattr(self, 'bypass_gbs') or (self.separate_ is None and self.r_ is None and self.g_ is None and self.b_ is None):
            return super().get_blender_socket()
        
        else:
            self.bypass_gbs = True
            node = nodes.CombineRgb(r=self.r, g=self.g, b=self.b, label=f"{self.node.chain_label}.combine")
            self.stack(node)
            del self.bypass_gbs
            
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
    
    In Blender, there is only one type of *geometry* socket. Sub classes [Mesh](mesh.md), [Curve](Curve.md),
    [Points](Points.md), [Instances](Instances.md) and [Volume](Volume.md) are introduced by **geonodes**.
    Each sub class implement the nodes creation which are specific to them.
    
    For instance, the node *'Extrude Mesh'* is specific to meshes. This node is implemented by the method
    `extrude` of class [Mesh](Mesh.md#extrude):
                              
    ```python
    top, side = mesh.extrude()
    ```
    
    Some **Geometry** sub classes can have methods with the same name but are based on different nodes:
        
    ```python
    points_1 = mesh.to_points()  # Create a 'Mesh to Points' node
    points_2 = curve.to_points() # Create a 'Curve to Points' node
    ```
    
    ### Initialization
    
    There is no constructor returnig of geometry of type **Geometry**. Constructors are class methods of
    sub classes implementing their specific primitive nodes:

    ```python
    cube     = Mesh.Cube()      # node 'Cube'
    circle_1 = Mesh.Circle()    # node 'Mesh Circle'
    circle_2 = Curve.Circle()   # node 'Curve Circle'
    volume   = Volume.Cube()    # node 'Volume Cube'
    ```
    
    **Geometry** is the type of the input geometry which can be read from the property `input_geometry` of
    the [Tree](Tree.md#input_geometry). If a modifier is dedicated to meshes, one must type cast the
    input geometry to the desired type:
               
    ```python
    with Tree("Geometry Nodes") as tree:
        geometry = tree.input_geometry # class Geometry
        mesh = Mesh(tree.ig)           # type cast to Mesh (ig is the short version of input_geometry)
    ```
    
    ### Components
    
    The components of **Geometry** can be accessed via dedicated properties. This is an alternative
    to typecasting the input geometry.
        
    ```python
    geo = tree.ig
    mesh = geo.mesh_component    # Socket 'Mesh' of node 'Separate Components'
    vol  = geo.volume_component  # Socket 'Volume' of node 'Separated Components'
    ```
    
    ### Joining
    
    **Geometry** supports the ``+`` operator acting as method [join](#join). In the following example,
    the tree returns the joining of a cube and a sphere:
    
    ```python
    cube = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    tree.output_geometry = cube + sphere
    ```
    """
    
    def __init__(self, socket, node=None, label=None):
        
        #from geonodes.nodes import domains
        
        #self.points = Vertex(self) # Initialized before super().__init__ which can override points
        
        super().__init__(socket, node=node, label=label)
    
    
    def init_domains(self):

        from geonodes.nodes import domains

        super().init_domains()
        
        type_name = type(self).__name__
        if type_name == 'Mesh':
            self.verts   = domains.Vertex(self)
            self.edges   = domains.Edge(self)
            self.faces   = domains.Face(self)
            self.corners = domains.Corner(self)
            self.points  = self.verts
            
        elif type_name == 'Curve':
            self.points  = domains.ControlPoint(self)
            self.splines = domains.Spline(self)
            
        elif type_name == 'Points':
            self.points  = domains.CloudPoint(self)
            
        elif type_name == 'Instances':
            self.insts  = domains.Instance(self)
            
        else:
            # Points must exist!
            self.points  = domains.CloudPoint(self)
            
    # ----------------------------------------------------------------------------------------------------
    # Set a node an attribute of the 
    
    def attribute_node(self, node, domain='POINT'):
        return node.as_attribute(owning_socket=self, domain=domain)
        
            
    @classmethod
    def Input(cls, name = None, description = ""):
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
    # Instantiate the geometry
    
    def instantiate(self, count = 1, realize = False):
        """ Instantiate the geometry
        
        Args:
            count: Number of instances to create
            realize: True to realize the instances
            
        Returns:
            Instances or Geometry
            
        The duplication is performed by instantiating the geometry along the vertices
        of a Mesh Line initialized with `count` points.
        
        The operator ``*`` can be used to operate this method with `realize = False`:
            
        .. code-block::
            
            curves = curve * 10
            
            # is equivalent to
            
            curves = curve.duplicate(10, realize=False)
            
        """
        
        import geonodes as gn
        
        with self.node.tree.layout(f"Instantiate({count}, {realize})", color='GENE'):
            line = gn.Mesh.Line(count=count)
            insts = gn.Points(line).instance_on_points(instance=self)
            if realize:
                return type(self)(insts.realize())
            else:
                return insts
            
    def __mul__(self, count):
        return self.instantiate(count=count, realize=False)
        
    def __imul__(self, count):
        return type(self)(self.instantiate(count=count, realize=True))
        
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
        if isinstance(bcoll, bpy.types.NodeSocketCollection) or self.is_socket(bcoll):
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
    def Input(cls, value=None, name="Collection", description=""):
        """ Create a Collection input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Collection: The Collection data socket
        """
        
        return cls(Tree.TREE.new_input('Collection', name = name, value=value, description = description))
            
            
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
    def Input(cls, value=None, name="Object", description=""):
        """ Create an Object input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Object: The Object data socket
        """
        
        return cls(Tree.TREE.new_input('Object', name=name, value=value, description=description))
            
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
    def Input(cls, value=None, name="Material", description=""):
        """ Create a Material input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Material: The Material data socket
        """
        
        return cls(Tree.TREE.new_input('Material', name=name, value=value, description=description))
    
# -----------------------------------------------------------------------------------------------------------------------------
# Other classes

class Texture(DataSocket):

    @classmethod
    def Input(cls, value=None, name="Texture", description=""):
        """ Create a Texture input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Texture: The Texture data socket
        """
        
        return cls(Tree.TREE.new_input('Texture', name=name, value=value, description=description))
    
class Image(DataSocket):
    
    @classmethod
    def Input(cls, value = None, name="Image", description=""):
        """ Create an Image input socket in the Group Input Node
        
        Args:
            name: The socket name
            description: User tip
            
        Returns:
            Image: The Image data socket
        """
        
        return cls(Tree.TREE.new_input('Image', name=name, value=value, description=description))
    
            
            
        
            
            


    
               
                
                



            
        
