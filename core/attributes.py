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
- Attributes

This class encapsulates geometry attributes methdos

updates
-------
- creation : 2027/07/20
"""

from .scripterror import NodeError

# ====================================================================================================
# Helper class for Geometry attributes
# ====================================================================================================

class Attribute:
    
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
        """ Geometry Attribute helper

        Parameters
        ----------
        name : str
            attribute name

        data_type : str | value
            attribute data_type

        domain : str | Domain
            domain where to store the named attribute

        prefix : name prefix
            name prefix
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

        self.data_type = data_type

    # ----------------------------------------------------------------------------------------------------
    # str
    # ----------------------------------------------------------------------------------------------------
            
    def __str__(self):
        return f"<Attribute: {self.geometry}.{self.name}, domain: {self.domain}, type: {self.data_type}>"

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

        geometry = None
        domain_name = None

        if value is None:
            return None, None

        elif hasattr(value, 'DOMAIN_NAME'):
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
    def ensure_data_type(self):
        if self.data_type is None:
            self.data_type = 'Float'
        return self.data_type
    
    # ====================================================================================================
    # Setting and getting
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Getting
    # ----------------------------------------------------------------------------------------------------
            
    def get(self):

        from .nodeclass import Node

        if self._value is None:
            self._value = Node('Named Attribute', 
            {'Name': self.name}, 
            data_type = Attribute.DT_SET[self.ensure_data_type],
            )._out._lc(self.name)
            
        return self._value

    # ----------------------------------------------------------------------------------------------------
    # Setting
    # ----------------------------------------------------------------------------------------------------
        
    def set(self, value=None, domain=None):

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
            data_type = Attribute.DT_SET[self.ensure_data_type],
            )._out
            
        if self.geometry is not None:
            self.geometry._jump(socket)

        self._value = None
            
        return self
    
    @property
    def value(self):
        return self.get()
    
    @value.setter
    def value(self, value):
        self.set(value)

    # ====================================================================================================
    # Remove
    # ====================================================================================================

    def remove(self, all=False):
        self._check_geometry(f"Impossible to remove named attribute '{self.name}'")

        if all and self.prefix is not None:
            self.geometry.remove_named_attribute(pattern_mode='WildCard', name=f"{self.prefix} *")
        else:
            self.geometry.remove_named_attribute(pattern_mode='Exact', name=self.name)

    # ====================================================================================================
    # Rename
    # ====================================================================================================

    def rename(self, name, prefix=False, overwrite=None):
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
       

    

        

    
 
