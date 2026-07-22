"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : attributes
-------------------
- Attribute

Helper for reading, transforming and storing named geometry attributes.

updates
-------
- creation : 2027/07/20
"""

from .scripterror import NodeError

# ====================================================================================================
# Helper class for Geometry attributes
# ====================================================================================================

class Attribute:
    """Helper for a named attribute stored on a geometry.

    ``Attribute`` complements the standard named-attribute methods exposed by
    geometries and domains. It keeps the attribute name, domain, data type and
    geometry together, and lets the attribute be used much like a socket in an
    expression.

    An instance is normally created with ``Domain.get`` or ``Geometry.get``,
    rather than by calling this constructor directly.

    Typical usage
    -------------
    Create a face attribute of type ``Vector`` and store a value:

    ``` python
        mesh = Mesh()
        attr = mesh.faces.get("My Vector", Vector)
        attr.set((0, 0, 1))
    ```

    The same operation can be written through the ``value`` property. Reading
    the property creates a Named Attribute node; assigning it creates a Store
    Named Attribute node:

    ``` python
        attr = mesh.faces.get("My Vector", Vector)

        vector_field = attr.value
        attr.value = vector_field.normalize()
    ```

    Read an existing integer attribute, build an expression and store its
    cached result:

    ``` python
        attr = mesh.faces.get("My Integer", Integer)
        attr = attr ** 2
        attr = attr + 1
        attr.set()
    ```

    Attributes can be combined with sockets, constants, or other attributes.
    The resulting field remains cached until ``set()`` is called:

    ``` python
        weight = mesh.points.get("Weight", Float)
        factor = mesh.points.get("Factor", Float)

        weight = weight * factor + 0.25
        weight.set()
    ```

    Non-in-place operators cache their result on the helper. Calling
    ``set`` without a value stores that cached result. In-place operators
    write their result to the geometry immediately:

    ``` python
        attr += 1
        attr *= 2
    ```

    Named attributes can also be removed or renamed:

    ``` python
        attr.rename("My Renamed Integer")
        attr.remove()
    ```

    Parameters
    ----------
    name : str
        Name of the attribute.
    data_type : type | str | value, optional
        Socket type used to read and store the attribute. For example,
        ``Float``, ``Integer`` or ``Vector``.
    domain : str | Domain | Geometry, optional
        Attribute domain, optionally carrying the geometry on which the
        attribute is stored. The default domain is ``Point``.
    prefix : str, optional
        Prefix prepended to the stored attribute name.

    Notes
    -----
    ``Attribute`` represents Geometry Nodes fields; it does not read or modify
    Blender mesh attribute data directly from Python.
    """
    
    DOMAINS = {
        'Point'     : 'POINT', 
        'Edge'      : 'EDGE', 
        'Face'      : 'FACE', 
        'Corner'    : 'CORNER', 
        'Spline'    : 'CURVE', 
        'Instance'  : 'INSTANCE', 
        'Layer'     : 'LAYER'}
        
    DT_SET = {
        'Float'         : 'FLOAT',
        'Integer'       : 'INT',
        'Boolean'       : 'BOOLEAN',
        'Vector'        : 'FLOAT_VECTOR', 
        'Color'         : 'FLOAT_COLOR', 
        'Quaternion'    : 'QUATERNION', 
        '4x4 Matrix'    : 'FLOAT4X4', 
        '8Bit Integer'  : 'INT8', 
        '2D Vector'     : 'FLOAT2', 
        '4D Vector'     : 'FLOAT4',
        'Byte Color'    : 'BYTE_COLOR',
        }
    DT_GET = {
        'Float'         : 'FLOAT',
        'Integer'       : 'INT',
        'Boolean'       : 'BOOLEAN',
        'Vector'        : 'FLOAT_VECTOR', 
        'Color'         : 'FLOAT_COLOR', 
        'Quaternion'    : 'QUATERNION', 
        '4x4 Matrix'    : 'FLOAT4X4', 
        '8Bit Integer'  : 'INT',            #'INT8', 
        '2D Vector'     : 'FLOAT_VECTOR',   #'FLOAT2', 
        '4D Vector'     : 'FLOAT_VECTOR',   #'FLOAT4',
        'Byte Color'    : 'COLOR',          #'BYTE_COLOR',
        }
    
    def __init__(self, name, data_type=None, domain=None, prefix=None):
        """Create a named geometry-attribute helper.

        Parameters
        ----------
        name : str
            Name of the attribute.
        data_type : type | str | value, optional
            Socket type used to read and store the attribute.
        domain : str | Domain | Geometry, optional
            Attribute domain and, when supplied by a domain or geometry
            instance, the geometry on which the attribute is stored.
        prefix : str, optional
            Prefix prepended to the stored attribute name.
        """

        self._value = None

        # Name with prefix

        self.prefix    = prefix
        self._name     = None
        self.name      = name

        # Geometry and domain
        
        self.geometry     = None
        self._domain_name = None
        self.domain       = domain

        # data type

        self._data_type = None
        self.data_type = data_type

    # ----------------------------------------------------------------------------------------------------
    # str
    # ----------------------------------------------------------------------------------------------------
            
    def __str__(self):
        return f"<Attribute: {self.geometry}.{self.name}, domain: {self.domain_name}, type: {self.data_type}>"

    # ----------------------------------------------------------------------------------------------------
    # Error if geometry is not defined
    # ----------------------------------------------------------------------------------------------------

    def _check_geometry(self, message):
        if self.geometry is None:
            raise NodeError(f"Attribute.geometry is None, {message}")
        
    # ----------------------------------------------------------------------------------------------------
    # Name
    # ----------------------------------------------------------------------------------------------------

    @property
    def name(self):
        if self.prefix is None:
            return self._name
        else:
            return f"{self.prefix} {self._name}"
        
    @name.setter
    def name(self, value):
        self._name = value

    # ----------------------------------------------------------------------------------------------------
    # Geometry and domain
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def _get_geo_domain(cls, value):

        from .geometry_class import Geometry
        from .domain_class import Domain

        geometry = None
        domain_name = None

        if value is None:
            return None, None

        elif isinstance(value, Domain):
            geometry = value._geo
            domain_name = value.DOMAIN_NAME.title()

        elif isinstance(value, Geometry):
            geometry = value

        elif isinstance(value, str):
            domain_name = value

        else:
            raise NodeError(f"Value <{value}> is not a valid domain for named Attribute.")
        
        if domain_name is None:
            return geometry, None
        
        # Domain name
        
        if domain_name == 'Face Corner':
            domain_name = 'Corner'
        elif domain_name == 'Curve':
            domain_name = 'Spline'
            
        if domain_name not in Attribute.DOMAINS:
            raise ValueError(f"Attribute.domain name error: '{domain_name}' not in {Attribute.DOMAINS}")
            
        return geometry, domain_name

    @property
    def domain_name(self):
        if self._domain_name is None:
            return 'Point'
        else:
            return self._domain_name
        
    @domain_name.setter
    def domain_name(self, value):

        _, domain_name = self._get_geo_domain(value)
        self._domain_name = domain_name
            
    @property
    def domain(self):
        raise Exception(f"Attribute.domain is write only. {self}")
        return None
        
    @domain.setter
    def domain(self, value):

        geometry, domain_name = self._get_geo_domain(value)
        if geometry is not None:
            self.geometry = geometry
        if domain_name is not None:
            self.domain_name = domain_name
        
    # ----------------------------------------------------------------------------------------------------
    # Data type
    # ----------------------------------------------------------------------------------------------------
        
    @classmethod
    def _get_data_type(cls, value):

        from .sockettype import SocketType

        if value is None:
            return None
        
        dt = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')

        for i, data_type in enumerate(list(Attribute.DT_SET.values())):
            if data_type == dt:
                return list(Attribute.DT_SET.keys())[i]
        
        return None
    
    @property
    def data_type(self):
        if self._data_type is None:
            self._data_type = 'Float'
        return self._data_type
    
    @data_type.setter
    def data_type(self, value):
        self._data_type = self._get_data_type(value)
    
    # ====================================================================================================
    # Setting and getting
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Getting
    # ----------------------------------------------------------------------------------------------------
            
    def get(self):
        """Return the attribute as a Geometry Nodes field socket.

        > Node <&Node Named Attribute>

        The Named Attribute node is created lazily. Its output is cached until
        ``set`` writes a value and clears the cache.

        Returns
        -------
        Socket
            Field socket containing the named attribute value.
        """

        from .nodeclass import Node

        if self._value is None:
            self._value = Node('Named Attribute', 
            {'Name': self.name}, 
            data_type = Attribute.DT_SET[self.data_type],
            )._out._lc(self.name)
            
        return self._value

    # ----------------------------------------------------------------------------------------------------
    # Setting
    # ----------------------------------------------------------------------------------------------------
        
    def set(self, value=None, domain=None):
        """Store a value in the named attribute.

        > Node <&Node Store Named Attribute>

        If ``value`` is omitted, the result cached by the latest non-in-place
        operation is stored. In-place operators such as ``+=`` call this method
        automatically.

        Parameters
        ----------
        value : value | Socket, optional
            Value or field to store. When omitted, use the cached value.
        domain : str | Domain | Geometry, optional
            Override the geometry or domain configured on this helper. Passing
            a ``Domain`` also applies that domain's selection.

        Returns
        -------
        Attribute
            This helper, with its cached value cleared.
        """

        from .nodeclass import Node

        if value is None:
            value = self._value
        if self.data_type is None:
            self.data_type = self._get_data_type(value)

        selection = None

        geo, dn = self._get_geo_domain(domain)
        if geo is not None:
            self.geometry = geo
            selection = domain.get_selection()
        if dn is not None:
            self.domain_name = dn

        socket = Node('Store Named Attribute', {
            'Geometry': self.geometry,
            'Selection': selection,
            'Name': self.name,
            'value': value},
            domain = self.domain_name,
            data_type = Attribute.DT_SET[self.data_type],
            )._out
            
        if self.geometry is not None:
            self.geometry._jump(socket)

        self._value = None
            
        return self
    
    @property
    def value(self):
        """Read or store the named attribute value.

        Getter
        ------
        > Node <&Node Named Attribute>

        Reading ``value`` calls ``get()``. It creates a Named Attribute node
        when the field is not already cached, then returns its output socket:

        ``` python
            field = attr.value
        ```

        Setter
        ------
        > Node <&Node Store Named Attribute>

        Assigning ``value`` calls ``set()``. It creates a Store Named Attribute
        node and updates the geometry attached to this helper:

        ``` python
            attr.value = field
        ```

        Returns
        -------
        Socket
            The Named Attribute field socket when the property is read.
        """
        return self.get()
    
    @value.setter
    def value(self, value):
        self.set(value)

    # ====================================================================================================
    # Remove
    # ====================================================================================================

    def remove(self, all=False):
        """Remove the named attribute from the geometry.

        > Node <&Node Remove Named Attribute>

        Parameters
        ----------
        all : bool, default=False
            If true and this helper has a prefix, remove every attribute whose
            name starts with that prefix. Otherwise remove only this attribute.

        Raises
        ------
        NodeError
            If no geometry is attached to the helper.
        """
        self._check_geometry(f"Impossible to remove named attribute '{self.name}'")

        if all and self.prefix is not None:
            self.geometry.remove_named_attribute(pattern_mode='WildCard', name=f"{self.prefix} *")
        else:
            self.geometry.remove_named_attribute(pattern_mode='Exact', name=self.name)

    # ====================================================================================================
    # Rename
    # ====================================================================================================

    def rename(self, name, prefix=False, overwrite=None):
        """Rename the attribute on the geometry.

        > Node <&Node Rename Attribute>

        Parameters
        ----------
        name : str
            New attribute name, or new prefix when ``prefix`` is true.
        prefix : bool, default=False
            Rename all attributes sharing this helper's prefix instead of only
            the current attribute.
        overwrite : bool, optional
            Value passed to the Rename Attribute node's overwrite input.

        Raises
        ------
        NodeError
            If no geometry is attached to the helper.
        """
        self._check_geometry(f"Impossible to rename attribute '{self.name}'")

        if prefix:
            self.geometry.rename_attribute(mode='Prefix', old=self.prefix, new=name, overwrite=overwrite)
            self.prefix = name
        else:

            if self.prefix is None:
                new_name = name
            else:
                new_name = f"{self.prefix} {name}"
            self.geometry.rename_attribute(mode='Single', old=self.name, new=new_name, overwrite=overwrite)
            self.prefix = None
            self.name = name
    
    # ====================================================================================================
    # Operations
    # ====================================================================================================

    def _set_value(self, value):
        self._value = value
        return self

    @classmethod
    def _aget(cls, other):
        if isinstance(other, Attribute):
            return other.get()
        else:
            return other

    # ----- Neg

    def __neg__(self):
        return self._set_value(self.get().multiply(-1))

    # ----- Abs

    def __abs__(self):
        return self._set_value(self.get().abs())

    # ----- Addition

    def __add__(self, other):
        return self._set_value(self.get() + self._aget(other))
    
    def __radd__(self, other):
        return self._set_value(self._aget(other) + self.get())
    
    def __iadd__(self, other):
        return self.set(self.get() + self._aget(other))

    # ----- Subtraction

    def __sub__(self, other):
        return self._set_value(self.get() - self._aget(other))
    
    def __rsub__(self, other):
        return self._set_value(self._aget(other) - self.get())
    
    def __isub__(self, other):
        return self.set(self.get() - self._aget(other))

    # ----- Multiplication

    def __mul__(self, other):
        return self._set_value(self.get() * self._aget(other))
    
    def __rmul__(self, other):
        return self._set_value(self._aget(other) * self.get())
    
    def __imul__(self, other):
        return self.set(self.get() * self._aget(other))

    # ----- Division

    def __truediv__(self, other):
        return self._set_value(self.get() / self._aget(other))
    
    def __rtruediv__(self, other):
        return self._set_value(self._aget(other) / self.get())
    
    def __itruediv__(self, other):
        return self.set(self.get() / self._aget(other))

    # ----- Modulo

    def __mod__(self, other):
        return self._set_value(self.get() % self._aget(other))
    
    def _rmod__(self, other):
        return self._set_value(self._aget(other) % self.get())
    
    def __imod__(self, other):
        return self.set(self.get() % self._aget(other))

    # ----- Power

    def __pow__(self, other):
        return self._set_value(self.get() ** self._aget(other))
    
    def __rpow__(self, other):
        return self._set_value(self._aget(other) ** self.get())
    
    def __ipow__(self, other):
        return self.set(self.get() ** self._aget(other))

    # ----- Operations

    def __round__(self):
        return self._set_value(self.get().round())

    def __trunc__(self):
        return self._set_value(self.get().trunc())

    def __floor__(self):
        return self._set_value(self.get().floor())

    def __ceil__(self):
        return self._set_value(self.get().ceil())

    # =============================================================================================================================
    # Comparison
    # __eq__ __ne__ __lt__ __gt__ __le__ __ge__

    def __ge__(self, other):
        return self._set_value(self.get().greater_equal(self._aget(other)))

    def __gt__(self, other):
        return self._set_value(self.get().greater_than(self._aget(other)))

    def __le__(self, other):
        return self._set_value(self.get().less_equal(self._aget(other)))

    def __lt__(self, other):
        return self._set_value(self.get().less_than(self._aget(other)))

    def __eq__(self, other):
        return self._set_value(self.get().equal(self._aget(other)))

    def __ne__(self, other):
        return self._set_value(self.get().not_equal(self._aget(other)))
    
    # =============================================================================================================================
    # Boolean specific
    
    def __or__(self, other):
        return self._set_value(self.get().bor(self._aget(other)))

    def __ror__(self, other):
        return self._set_value(self.get().bor(self._aget(other)))

    def __and__(self, other):
        return self._set_value(self.get().band(self._aget(other)))

    def __rand__(self, other):
        return self._set_value(self.get().band(self._aget(other)))

    def __xor__(self, other):
        return self.get()._set_value(self.get().xor(self._aget(other)))

    def __rxor__(self, other):
        return self._set_value(self.get().xor(self._aget(other)))

    # To avoid user errors

    def __bool__(self):
        raise NodeError(f"Attribute is not a python bool : {self}")

    # ====================================================================================================
    # Class test
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Float, Integer, Vector

        with GeoNodes("Attribute Test"):

            mesh = Mesh()

            # Create attributes and store explicit values.
            with Layout("Create and set"):
                direction = mesh.faces.get("My Vector", Vector)
                direction.set((0, 0, 1))

                weight = mesh.points.get("Weight", Float)
                weight.value = 0.5

            # Read an attribute as a field, cache operations, then store the
            # cached result with set().
            with Layout("Cached operations"):
                counter = mesh.faces.get("My Integer", Integer)
                counter = counter**2
                counter = counter + 1
                counter.set()

            # In-place operations store their result immediately.
            with Layout("In-place operations"):
                counter += 1
                counter *= 2

            # Attribute helpers can be created from Geometry as well as Domain.
            with Layout("Geometry helper"):
                factor = mesh.get("Factor", Float, domain="Face")
                factor.set(direction.value.length())

            # Rename and remove attributes from the geometry.
            with Layout("Rename and remove"):
                temporary = mesh.points.get("Temporary", Float)
                temporary.set(1.0)
                temporary.rename("Renamed")
                temporary.remove()

            # Get Attribute Names with both domain and data-type filters.
            names = mesh.faces.get_attribute_names(Vector)

            mesh.out()
            names.out("Face Vector Attributes")
       

    

        

    
 
