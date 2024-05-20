#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module


@author: alain.bernard
@email: alain@ligloo.net

-----

Geometry attributes.

Attributes are stored in 3 arrays, one per type (int, float, bool).

This avoids to multiply the number of arrays and the operations implied on them.
For instance, if a geometry has 1 float attribute, 1 vector attribute and 1 color attribute,
when one appends vertices, 3 append operations are required. These operations are grouped in a single one
on the array of floats.

"""

import numpy as np
if False:
    from geonodes.core.cached_array import CachedArray
    from geonodes.core import blender
else:
    from cached_array import CachedArray
    


# =============================================================================================================================
# Globa functions

DOMAINS = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
TYP_DTYPE = 0
TYP_SIZE  = 1
TYP_SHAPE = 2
TYP_NAME  = 3

TYPES   = {
    'FLOAT'         : (float,    1, (),   'value'),
    'INT'           : (int,      1, (),   'value'),
    'FLOAT_VECTOR'  : (float,    3, (3,), 'vector'),
    'FLOAT_COLOR'   : (float,    4, (4,), 'color'),
    'BYTE_COLOR'    : (np.byte,  4, (4,), 'color_srgb'),
    'STRING'        : None,
    'BOOLEAN'       : (bool,     1, (),   'value'),
    'FLOAT2'        : (float,    2, (2,), 'vector'),
    #'INT8'          : (np.int8,  1, (),   'value'),
    #'INT32_2D'      : (np.int32, 2, (2,), 'value'),
    'INT8'          : (int,      1, (),   'value'),
    'INT32_2D'      : (int,      2, (2,), 'value'),
    }

def attribute_dtype(data_type):
    """ The numpy data type of an attribute data type.

    Arguments
    ---------
        - data_type (str) : Blender attribute data type

    Returns
    -------
        - python type in [bool, int, float]
    """
    return TYPES[data_type][TYP_DTYPE]

def attribute_value_size(data_type):
    """ The size of an attribute data type.

    Arguments
    ---------
        - data_type (str) : Blender attribute data type

    Returns
    -------
        - size
    """
    return TYPES[data_type][TYP_SIZE]

def attribute_value_shape(data_type):
    """ The shape of an attribute data type.

    Arguments
    ---------
        - data_type (str) : Blender attribute data type

    Returns
    -------
        - shape
    """
    return TYPES[data_type][TYP_SHAPE]

def attribute_value_name(data_type):
    """ The value name of an attribute data type.

    The value name is the name of the blender attribute.

    Arguments
    ---------
        - data_type (str) : Blender attribute data type

    Returns
    -------
        - str
    """
    return TYPES[data_type][TYP_NAME]

def data_type_from_type(value):
    if isinstance(value, (int, np.int8, np.int16, np.int32, np.int64, np.byte)):
        return 'INT'

    elif isinstance(value, (float, np.float32, np.float64)):
        return 'FLOAT'

    elif isinstance(value, (bool, np.bool_)):
        return 'BOOL'

    elif isinstance(value, (list, tuple, np.ndarray)):
        data_type = data_type_from_type(value[0])
        if data_type == 'FLOAT':
            if len(value) == 3:
                return 'FLOAT_VECTOR'
            elif len(value) == 4:
                return 'FLOAT_COLOR'

    raise RuntimeError(f"Impossible to find an attribute data_type for value of type '{type(value)}': {value}")

# =============================================================================================================================
# Objects

# ----------------------------------------------------------------------------------------------------
# Attribute exists

def attribute_exists(spec, name):
    """ Test if an attribute exists.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name

    Returns
    -------
        - bool : True if exists, False otherwise
    """

    data = blender.get_data(spec)
    return data.attributes.get(name) is not None

# ----------------------------------------------------------------------------------------------------
# Attribute info

def get_attribute_info(spec, name):
    """ Get the attribute info.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name

    Returns
    -------
        - dict with attribute informations, None if the attribute doesn't exist
    """

    data = blender.get_data(spec)
    battr = data.attributes.get(name)
    if battr is None:
        return None

    return {
        'name'          : name,
        'data_type'     : battr.data_type,
        'domain'        : battr.domain,
        'value_name'    : attribute_value_name(battr.data_type),
        'value_size'    : attribute_value_size(battr.data_type),
        'value_shape'   : attribute_value_shape(battr.data_type),
        'count'         : len(battr.data),
        'battr'         : battr,
        }

# ----------------------------------------------------------------------------------------------------
# List of attributes

def get_attribute_names(spec):
    """ Get the name of the attributes of an object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data

    Returns
    -------
        - list of strs : attribute names
    """

    data = blender.get_data(spec)
    return list(data.attributes.keys())

# ----------------------------------------------------------------------------------------------------
# List of attributes

def get_attributes(spec):
    """ Get all the informations of the attributes of a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data

    Returns
    -------
        - dict of dicts : attribute informations.
    """

    data = blender.get_data(spec)
    return {name: get_attribute_info(data, name) for name in get_attribute_names(data)}

# ----------------------------------------------------------------------------------------------------
# Delete an attribute

def delete_attribute(spec, name):
    """ Delete an attribute.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
    """

    data = blender.get_data(spec)

    battr = data.attributes.get(name)
    if battr is not None:
        data.attributes.remove(battr)

# ----------------------------------------------------------------------------------------------------
# Create an attribute

def create_attribute(spec, name, data_type, domain='POINT', value=None):
    """ Create an attribute into a Blender object.

    Note that if the attribute already exists, it is deleted.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - data_type (str) : attribute data type
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """

    data = blender.get_data(spec)

    battr = data.attributes.get(name)
    if battr is None:
        data.attributes.new(name, type=data_type, domain=domain)

    if value is not None:
        set_attribute(data, name, value)


def create_float_attribute(spec, name, domain='POINT', value=None):
    """ Create a float attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """

    create_attribute(spec, name, data_type='FLOAT', domain=domain, value=value)

def create_int_attribute(spec, name, domain='POINT', value=None):
    """ Create an int attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='INT', domain=domain, value=value)

def create_bool_attribute(spec, name, domain='POINT', value=None):
    """ Create a bool attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='BOOLEAN', domain=domain, value=value)

def create_vector_attribute(spec, name, domain='POINT', value=None):
    """ Create a vector attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='FLOAT_VECTOR', domain=domain, value=value)

def create_vector2_attribute(spec, name, domain='CORNER', value=None):
    """ Create a vector2 attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='FLOAT2', domain=domain, value=value)

def create_color_attribute(spec, name, domain='POINT', value=None):
    """ Create a float color attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='FLOAT_COLOR', domain=domain, value=value)

def create_rgb_color_attribute(spec, name, domain='POINT', value=None):
    """ Create a rgb color attribute into a Blender object.

    Arguments
    ---------
        - spec (str or data) : valid spec for object or data
        - name (str) : attribute name
        - domain (str='POINT') : domain of creation
        - value (any=None) : default value
    """
    create_attribute(spec, name, data_type='BYTE_COLOR', domain=domain, value=value)

# ----------------------------------------------------------------------------------------------------
# Get the attribute value

def get_attribute(spec, name):

    data  = blender.get_data(spec)
    battr = data.attributes[name]
    n     = len(battr.data)

    value_size = attribute_value_size(battr.data_type)
    value_name = attribute_value_name(battr.data_type)

    a = np.empty(n*value_size)
    battr.data.foreach_get(value_name, a)

    return np.reshape(a, (n,) + attribute_value_shape(battr.data_type))

# ----------------------------------------------------------------------------------------------------
# Set attribute value

def set_attribute(spec, name, value):

    data  = blender.get_data(spec)
    battr = data.attributes[name]
    n     = len(battr.data)

    value_size = attribute_value_size(battr.data_type)
    value_name = attribute_value_name(battr.data_type)

    if n*value_size == np.size(value):
        battr.data.foreach_set(value_name, np.reshape(value, np.size(value)))

    else:
        nvalues = np.size(value)//value_size
        if n % nvalues != 0:
            raise Exception(f"Set Attribute Error: Object attribute '{name}' len is {n} (size={n*value_size}). Impossible to set with value of shape {np.shape(value)} (size={np.size(value)}).")

        item_size = n//nvalues
        a = np.empty((nvalues, item_size, value_size), dtype=attribute_dtype(battr.data_type))
        a[:] = np.reshape(value, (nvalues, 1, value_size))

        #print(f"set_attribute:  {name}, {n:}: ({nvalues=}, {item_size=}, {value_size=}) <-- {value_name=}, {np.size(value)=}, {np.shape(value)=}, {value.dtype=}")

        battr.data.foreach_set(value_name, np.reshape(a, np.size(a)))

# =============================================================================================================================
# Attribute info

class AttrInfo:

    VALID_DTYPES = [float, int, bool]

    def __init__(self, data_type, offset, default, transfer=True):
        """ Managed how an attribute is mapped on the attributes arrays

        Arguments
        ---------
            - data_type (str) : the attribute data type
            - offset (int) : index of the attribute in the array
            - default (any) : default value
        """

        self.data_type   = data_type
        self.dtype       = attribute_dtype(data_type)
        self.array_index = AttrInfo.dtype_index(data_type)

        self.offset      = offset
        self.size        = attribute_value_size(data_type)
        self.slc         = offset if self.size == 1 else slice(offset, offset + self.size)

        self.default     = default
        self.transfer    = transfer

    @classmethod
    def dtype_index(cls, data_type):
        dtype = attribute_dtype(data_type)
        if dtype not in cls.VALID_DTYPES:
            raise Exception(f"Points Attribute data_type '{data_type}' of dtype {dtype.__name__} not supported.")
        return cls.VALID_DTYPES.index(dtype)

    def __str__(self):
        return f"{self.dtype.__name__} ({self.size}), slice: {self.slc}, default: {self.default}"

    def clone(self):
        return AttrInfo(self.data_type, self.offset, self.default, transfer=self.transfer)

    # ====================================================================================================
    # Serialization

    def as_dict(self):
        return {
            'data_type' : self.data_type,
            'offset'    : self.offset,
            'default'   : self.default,
            'transfer'  : self.transfer,
            }

# =============================================================================================================================
# Geometry attributes

class Attributes:

    FLOAT = 0
    INT   = 1
    BOOL  = 2

    # ----------------------------------------------------------------------------------------------------
    # Initialization

    def __init__(self, domain, cache=1000):
        """ Manages named attributes for a domain.

        Arguments
        ---------
            - cache (int=1000) : size of the cache
        """

        self.domain = domain
        self.infos  = {}
        self.arrays = [None, None, None] # Float array, Int array, Bool array
        self.dims   = [0, 0, 0]
        self.cache  = cache

    # ====================================================================================================
    # Serialization

    def as_dict(self):
        return {
            'domain' : self.domain,
            'infos'  : {name: info.as_dict() for name, info in self.infos.items()},
            'arrays' : [None if ca is None else ca.a for ca in self.arrays],
            'dims'   : self.dims,
            'cache'  : self.cache,
            }

    @classmethod
    def FromDict(cls, d):
        attrs = cls(domain=d['domain'], cache=d['cache'])
        attrs.dims = d['dims']

        # Arrays

        for i, a in enumerate(d['arrays']):
            if a is not None:
                attrs.arrays[i] = CachedArray.FromArray(a, cache=attrs.cache)

        # Attributes

        for name, attr_d in d['infos'].items():
            attrs.infos[name] = AttrInfo(**attr_d)

        # Done

        return attrs

    # ====================================================================================================
    # Create a new attribute

    def new(self, name, data_type, default, transfer=True):

        # ----- Already exists

        if name in self.infos:
            return

        # ----- Create the entry in the dictionary

        array_index = AttrInfo.dtype_index(data_type)

        info = AttrInfo(data_type, self.dims[array_index], default, transfer=transfer)
        self.infos[name] = info
        self.dims[array_index] += info.size

        # ----- Create / update the array if exists

        new_a = np.empty((len(self), info.size), info.dtype)
        if np.size(new_a) != 0:
            new_a[:] = default

        ca = self.arrays[array_index]
        if ca is None:
            self.arrays[array_index] = CachedArray.FromArray(new_a, cache=self.cache)
        else:
            ca.squeeze()
            ca._a = np.append(ca._a, new_a, axis=-1)

        # ----- ID

        if name == 'ID':
            self.ID = len(self)
            if self.ID:
                self['ID'] = np.arange(len(self))

        if False:
            print("ATTRIBUTE new", name, np.shape(self.arrays[array_index].a))

    def copy_attribute(self, attributes, name):
        """ Copy the specifications of an attribute from another Attributes.

        Note that only the attributes info are copied, not the values.

        Arguments
        ---------
            - attributes (Attributes) : Where to copy from
            - name (str) : attribute name
        """

        info = attributes.infos[name]
        self.new(name, info.data_type, info.default, transfer=info.transfer)

    # ----------------------------------------------------------------------------------------------------
    # From concatenation form

    def from_concat(self, concat, default=None, transfer=True):
        split = concat.split('_')
        data_type = split[0]
        if len(split) < 2 or data_type not in TYPES.keys():
            raise AttributeError(f"Attributes.from_concat error: 'concat' argument is not valid '{concat}'. It must be 'DATATYPE_name")

        name = concat[len(data_type)+1:]
        if default is None:
            shape = attribute_value_shape(data_type)
            if shape == ():
                default = 0
            else:
                default = np.zeros(shape, int)
        self.new(name, data_type, default, transfer=transfer)

    # ----------------------------------------------------------------------------------------------------
    # User friendly version

    def new_float(self, name, default=0., transfer=True):
        """ Create a new attribute of type FLOAT -> float.

        Arguments
        ---------
            - name (str) : attribute name
            - default (float=0) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new(name, 'FLOAT', default, transfer=transfer)

    def new_vector(self, name, default=(0., 0., 0.), transfer=True):
        """ Create a new attribute of type FLOAT_VECTOR -> array of 3 floats.

        Arguments
        ---------
            - name (str) : attribute name
            - default (tuple=(0, 0, 0)) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new(name, 'FLOAT_VECTOR', default, transfer=transfer)

    def new_int(self, name, default=0, transfer=True):
        """ Create a new attribute of type INT -> int.

        Arguments
        ---------
            - name (str) : attribute name
            - default (int=0) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new(name, 'INT', default, transfer=transfer)

    def new_bool(self, name, default=False, transfer=True):
        """ Create a new attribute of type BOOLEAN -> bool.

        Arguments
        ---------
            - name (str) : attribute name
            - default (bool=False) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new(name, 'BOOLEAN', default, transfer=transfer)

    def new_color(self, name, default=(0.5, 0.5, 0.5, 1.), transfer=True):
        """ Create a new attribute of type FLOAT_COLOR -> array of 4 floats.

        Arguments
        ---------
            - name (str) : attribute name
            - default (tuple=(0, 0, 0, 1)) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new(name, 'FLOAT_COLOR', default, transfer=transfer)

    def new_vector2(self, name, default=(0., 0.), transfer=True):
        """ Create a new attribute of type FLOAT2 -> array of 2 floats.

        Arguments
        ---------
            - name (str) : attribute name
            - default tuple=(0, 0)) : default value
            - transfer (bool=True) : transfer the attribute to the Blender mesh
        """

        self.new(name, 'FLOAT2', default, transfer=transfer)

    # ----- LATER

    def new_byte_color(self, name, default=(0., 0., 0.), transfer=True):
        raise Exception(f"Not yet implemented")
        self.new_attr(name, 'BYTE_COLOR', default, transfer=transfer)

    def new_int8(self, name, default=(0., 0., 0.), transfer=True):
        raise Exception(f"Not yet implemented")
        self.new_attr(name, 'INT8', default, transfer=transfer)

    def new_int32_2d(self, name, default=(0., 0., 0.), transfer=True):
        raise Exception(f"Not yet implemented")
        self.new_attr(name, 'INT32_2D', default, transfer=transfer)

    # ====================================================================================================
    # Reset to default values

    def reset(self):
        """ Reset the attributes to their default values.
        """

        for name, info in self.infos.items():
            if name == 'ID':
                self.ID = len(self)
                self[name] = range(self.ID)
            else:
                self[name] = info.default

    # ====================================================================================================
    # Clear : remove items

    def clear(self):
        for ca in self.arrays:
            if ca is not None:
                ca.clear()

    # ====================================================================================================
    # Clone / copy

    def clone(self):
        """ Clone the attributes.
        """

        attrs = Attributes(domain=self.domain, cache=self.cache)

        attrs.infos  = {name: info.clone() for name, info in self.infos.items()}
        attrs.arrays = [None if ca is None else ca.clone() for ca in self.arrays]
        attrs.dims   = list(self.dims)

        if hasattr(self, 'ID'):
            attrs.ID = self.ID

        return attrs

    def copy_definitions(self, attributes):
        """ Copy the attributes specifications from another.

        Note that only the attributes info are copied, not the values.

        Arguments:
            - attributes (Attributes) : the attributes to create
        """

        for name, info in attributes.infos.items():
            self.new(name, info.data_type, info.default, transfer=info.transfer)

    def get_selection(self, index):

        attrs = Attributes(domain=self.domain, cache=self.cache)

        attrs.infos  = {name: info.clone() for name, info in self.infos.items()}
        attrs.arrays = [None if ca is None else CachedArray.FromArray(ca[index], cache=self.cache) for ca in self.arrays]
        attrs.dims   = list(self.dims)

        if hasattr(self, 'ID'):
            attrs.ID = self.ID

        return attrs

    def copy_from(self, other, selection=None, exclude=[], only_new=False):

        # ----- Copy the non excluded names

        for name, info in other.infos.items():
            if name in exclude:
                continue
            if only_new and name in self.names:
                continue

            self.new(name, info.data_type, info.default, transfer=info.transfer)

            if selection is None:
                self[name] = other[name]
            else:
                self[name] = other[name][selection]

    # ====================================================================================================
    # Append other attributes

    def append(self, other):

        # ----- Copy the attribute

        self.copy_definitions(other)

        # ----- Quick move if attributes are the same
        # Check only the names! error could occur if same name are implemented differently

        if list(self.infos.keys()) == list(other.infos.keys()):
            for array_index, ca in enumerate(self.arrays):
                if ca is None:
                    continue
                ca.extend(len(other), other.arrays[array_index].a)

        # ----- Per attribute

        else:
            offset = len(self)
            for array_index, ca in enumerate(self.arrays):
                if ca is None:
                    continue
                ca.extend(len(other))

            for name in other.infos.keys():
                try:
                    self[name][offset:offset + len(other)] = other[name]
                    #ca.a[offset:offset + len(other)] = other[name]

                except Exception as e:
                    print('-'*60)
                    print(f"Attriutes error: name: {name}, {np.shape(ca.a)=}{np.shape(ca.a[offset:offset + len(other)])=}, {np.shape(other[name])=}")
                    print(self)
                    print("other")
                    print(other)
                    print()

                    raise e

    # ====================================================================================================
    # Multiply

    def multiply(self, count):
        if count <= 1:
            return

        n = len(self)
        for array_index, ca in enumerate(self.arrays):
            if ca is None:
                continue
            ca.extend((count - 1)*n, np.resize(ca.a, ((count - 1)*n, self.dims[array_index])))

    # ====================================================================================================
    # Read mesh attributes

    def from_object(self, spec):
        """ Read the object attributes.

        Arguments
        ---------
            - spec (str or mesh) : the mesh to set the attributes to
        """

        data = blender.get_data(spec)
        for name, binfo in get_attributes(data).items():

            if binfo['domain'] != self.domain:
                continue

            name = binfo['name']
            if name[0] == '.':
                continue

            if not self.exists(name):
                self.new(name, binfo['data_type'], 0, transfer=True)

            self[name] = get_attribute(data, name)

    # ====================================================================================================
    # Assign to blender mesh

    def to_object(self, spec, update=False):
        """ Transfer the attributes to a blender mesh object.

        Arguments
        ---------
            - spec (str or mesh) : the mesh to set the attributes to
            - attributes (array of st = None) : the attributes to transfer (all if None)
            - update (bool=False) : update the attributes values without trying to create them
        """

        data = blender.get_data(spec)

        for name, info in self.infos.items():

            if not info.transfer:
                continue

            if update:
                set_attribute(data, name, self[name])
            else:
                create_attribute(data, name, info.data_type, domain=self.domain, value=np.array(self[name]))

    # ----------------------------------------------------------------------------------------------------
    # Content

    def __str__(self):
        s = f"<Attributes: len {len(self)}, entries {self.attr_count}, cache: {self.cache}:"
        for name, info in self.infos.items():
            s += f"\n   - {name:10s}: {str(info)}"
        s += f"\narrays: {[np.shape(a) for a in self.arrays]}"
        return s + "\n>"

    # ====================================================================================================
    # Shape

    def __len__(self):
        for ca in self.arrays:
            if ca is not None:
                return len(ca)
        return 0

    # ====================================================================================================
    # Read / write content

    @property
    def names(self):
        return list(self.infos.keys())

    @property
    def attr_count(self):
        """ Number of attributes.
        """
        return len(self.infos)

    def default_item(self, array_index):
        if self.arrays[array_index] is None:
            return None

        item = np.zeros(self.dims[array_index], self.arrays[array_index]._a.dtype)
        for info in self.infos.values():
            if info.array_index == array_index:
                item[info.slc] = info.default

        return item

    # ----------------------------------------------------------------------------------------------------
    # Does an attribute exist

    def exists(self, name):
        """ Test if an attribute name exists.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - bool : True if exists
        """

        return name in self.infos

    def attribute_dtype(self, name):
        """ The type of an attribute.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - type : attribute type
        """
        return self.infos[name].dtype

    def attribute_size(self, name):
        """ The size of an attribute.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - int : attribute size
        """
        return self.infos[name].size

    def attribute_shape(self, name):
        """ The shape of an attribute.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - tuple : attribute shape
        """
        return TYPES[self.infos[name].data_type][TYP_SHAPE]

    # ----------------------------------------------------------------------------------------------------
    # Get set the values

    def get_attr_slice(self, name):
        info = self.infos.get(name)
        if info is None:
            raise AttributeError(f"Attributes {self.domain}: attribute '{name}' doesn't exist!")

        return info.slc

    def __getitem__(self, name):
        info = self.infos.get(name)
        if info is None:
            raise AttributeError(f"Attributes {self.domain}: attribute '{name}' doesn't exist!")

        return self.arrays[info.array_index][..., info.slc]

    def __setitem__(self, name, value):
        info = self.infos.get(name)
        if info is None:
            raise AttributeError(f"Attributes : attribute '{name}' doesn't exist!")

        self.arrays[info.array_index][..., info.slc] = value

    def set_selection(self, selection, attributes):
        """ Set value for a selection of indices from other attributes.

        Arguments
        ---------
            - selection (np.array selection) : items to set
            - attributes (Attributes) : values to read the value from
        """

        for self_a, other_a in zip(self.arrays, attributes.arrays):
            if self_a is None:
                continue
            self_a[selection] = other_a

    # ====================================================================================================
    # Read grouped attributes
    # A vector 4 is stored as a vector and a second float attribute just after
    # To read the vector 4 as once, need to override the default mechanism
    # Use with car

    def over_get(self, name, size, selection=None):
        info = self.infos.get(name)

        if selection is None:
            return self.arrays[info.array_index][..., info.offset:info.offset + size]
        else:
            return self.arrays[info.array_index][selection, ..., info.offset:info.offset + size]

    def over_set(self, name, size, value, selection=None):
        info = self.infos.get(name)
        if selection is None:
            self.arrays[info.array_index][..., info.offset:info.offset + size] = value
        else:
            self.arrays[info.array_index][selection, ..., info.offset:info.offset + size] = value


    # ====================================================================================================
    # Delete items

    def delete(self, selection):
        """ Delete a selection of items.

        Arguments
        ---------
            - selection (np.array selection) : items to delete
        """

        for attr_type, ca in enumerate(self.arrays):
            if ca is None:
                continue

            ca.delete(selection)


    # ====================================================================================================
    # Add items

    def add(self, count, **attrs):
        """ Add items.

        Arguments
        ---------
            - Number of items to add
            - **attrs (attribute name: value) : value to set to the newly created items
        """

        # ----- Increase the arrays

        offset = len(self)
        for array_index, ca in enumerate(self.arrays):
            if ca is None:
                continue
            ca.extend(count, self.default_item(array_index))

        # ----- Set the values passed in argument
        # The attributes can be for anoter domain, no error if it doesn't exist

        for name, value in attrs.items():
            if not self.exists(name):
                raise AttributeError(f"Attribute '{name}' not defined in the domain ‘{self.domain}‘.")

            if hasattr(value, '__call__'):
                v = value(count)
            else:
                v = value

            if True:
                self[name][offset:] = v
            else:
                try:
                    self[name][offset:] = v

                except Exception as e:
                    print("."*10, "Attribute.add error:")
                    print(f"  {name=}: {offset=}")
                    print(f"  {len(self)=}")
                    print(f"  {np.shape(v)=}")
                    print(f"  {np.shape(self[name][offset:])}")
                    print("."*10)
                    print()
                    raise e

        # ----- Return indices on the created items

        return np.arange(offset, offset+count)

    # ====================================================================================================
    # Squeeze the cached arrays

    def squeeze(self):
        for a in self.arrays:
            if a is not None:
                a.squeeze()

    # ====================================================================================================
    # Shape keys

    @property
    def float_array(self):
        """ Get the array of float attributes.

        Returns
        -------
            - array of floats
        """

        return self.arrays[self.FLOAT]
    
    # ====================================================================================================
    # Demo
    
    @classmethod
    def TestAttributes(cls):
        attrs = cls('POINT')
        
        attrs.new_int(       "int",        1)
        attrs.new_float(     "float",      3.14)
        attrs.new_bool(      "bool",       True)
        attrs.new_vector(    "vector",     (1, 2, 3))
        attrs.new_color(     "color",      (.1, .2, .3, .4))
        attrs.new_vector2(   "vector2",    (8, 9))
        #attrs.new_string(    "string",     "STR")
        #attrs.new_byte_color("byte color", (0, 127, 128, 255))
        #attrs.new_int8(      "int 8",      32)
        #attrs.new_int32_2d(  "int32 x 2",  (12, 13))
        
        attrs.add(8,
            int    = np.arange(8), 
            float  = np.linspace(10, 17, 8),
            #string = [f"string {i}" for i in range(8)],
            )
        
        print(attrs)
        #attrs[0]   = (0, 0., False, (0, 0, 0), (0., 0., 0., 0.), (0, 0))
        #attrs[1:3] = (1, 1., False, (1, 1, 1), (1., 1., 1., 1.), (1, 1))
        
        return attrs
    
    def equal_test(self, message="", ref=None):
        
        if ref is None:
            ref = self.TestAttributes()
        
        def diff(error_message):
            print('-'*100)
            print("Array is different from TestAttributes:", error_message)
            print()
            print(self)
            print()
            print(self[:])
            print('-'*100)
            raise Exception(message)
        
        for name in ref.names:

            if name not in self.names:
                diff(f"'{name}' attribute not found")

            if len(ref[name]) != len(self[name]):
                diff(f"length of {name} is different: ref={len(ref[name])},  self={len(other[name])}")
                
            if np.sum(ref[name] == self[name]) != np.size(ref[name]):
                diff(f"items of {name} are different:\n{ref[name]}\n{self[name]}")
        


# ====================================================================================================
# Vectors with attributes

class AttrVectors(Attributes):
    def __init__(self, vectors=None, cache=1000, **kwargs):

        super().__init__("VECTORS", cache=cache)

        self.new_vector("co")
        if vectors is not None:
            self.add(count=len(vectors), co=vectors)

        n = len(self)
        for k, v in kwargs.items():

            # ----- Value or first array item to have the attribute type
            # CAUTION : there is ambiguity to interpret a vector type attribute
            # when its length is the number of items at initialization:
            #    AttrVectors(vectors.shape=(3, 3), attribute.shape=(3,))
            #    1. can be one float attribute per vector
            #    2. or a vector attribute initialized at a single value
            # The following algorothm uses interpretation 1.
            # When interpretation 2. is required, uses:
            #    AttrVectors(vectors.shape=(3, 3), attribute.shape=(1, 3))

            ok_set = False
            # Value is a vector
            if hasattr(v, '__len__'):
                # Array is empty : type is vector
                if n == 0:
                    item = v

                # 2d-array : array of vectors
                elif len(np.shape(v)) == 2:
                    ok_set = True
                    item = v[0]

                # Array length is the number of vectors: array of items
                elif len(v) == n:
                    ok_set = True
                    item = v[0]

                # v is the item
                else:
                    item = v

            else:
                item = v

            # ----- Create the attribute

            if isinstance(item, bool):
                self.new_bool(k, default=item)
            elif isinstance(item, int):
                self.new_int(k, default=item)
            elif isinstance(item, float):
                self.new_float(k, default=item)
            elif hasattr(item, '__len__') and not isinstance(item, str) and len(item) in [3, 4]:
                if len(item) == 3:
                    self.new_vector(k, default=item)
                else:
                    self.new_color(k, default=item)
            else:
                raise Exception(f"AttrVectors init error: unsopported type for attribute '{k}', must be int, float, bool or vector, not {type(item)}.")

            # ----- Initialize the attribute

            if ok_set:
                setattr(self, k, v)

    def add_vectors(self, vectors, **attrs):
        if vectors is None or len(vectors) == 0:
            return None

        return super().add(len(vectors), co=vectors, **attrs)

    def __getattr__(self, name):

        infos = self.__dict__.get("infos")
        if infos is not None:
            if name in infos:
                return self[name]

        raise AttributeError(f"AttrVectors error: unknown attribute named '{name}'")

    def __setattr__(self, name, value):
        infos = self.__dict__.get("infos")
        if infos is None:
            super().__setattr__(name, value)
        else:
            if name in infos:
                self[name] = value
            else:
                return super().__setattr__(name, value)


# ====================================================================================================
# Test

def test():

    attrs = Attributes('DOMAIN')

    attrs.new_int("int_attr", 1)
    attrs.new_float("float_attr", 3.14)
    attrs.new_bool("bool_attr", True)
    attrs.new_vector("vect_attr", (1, 2, 3))
    attrs.new_color("col_attr", (.1, .2, .3, .9))
    attrs.new_vector2("uv_attr", (8, 9))

    attrs.add(8)

    attrs["int_attr"][6:] = 9
    print("INT ", attrs["int_attr"], ", exp: 1, 1, 1, 1, 1, 1, 9, 9")

    attrs["vect_attr"][6:] = (9, 9, 9)
    print("VECT", attrs["vect_attr"], ", exp: (1, 2, 3) x 6, (9, 9, 9), (9, 9, 9)")

    attrs["bool_attr"][6:] = False
    print("BOOL", attrs["bool_attr"], ", exp: False x 6, True, True")

    print("Attributes test")
    print(attrs)

    #cube = blender.create_mesh_object("Cube")
    #attrs.to_object("Cube")
    
def performances(count=10000):
    
    from time import time
    
    attrs = Attributes.TestAttributes()
    
    print("Performance test")
    
    t0 = time()
    for i in range(count):
        if i % 1000 == 0:
            print(f"{i//1000:3d}k: {len(attrs)}")
        attrs.add(8)
    t1 = time()
    
    print(f"Time {t1 - t0:.1f} s")



    
#test()
performances(100000)