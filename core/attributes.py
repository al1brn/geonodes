#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module


@author: alain.bernard
@email: alain@ligloo.net

-----

Geometry attributes.

Attributes are stored in 3 arrays, one per type (int, float, bool).

For instance, if a geometry has 1 float attribute, 1 vector attribute and 1 color attribute,
when one appends vertices, 3 append operations are required. These operations are grouped in a single one
on the array of floats.

"""

import numpy as np

# =============================================================================================================================
# Global functions

DOMAINS = ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

TYPES = {
    'FLOAT'         : {'dtype': float,  'size': 1, 'shape': (),   'name': 'value'},
    'INT'           : {'dtype': int,    'size': 1, 'shape': (),   'name': 'value'},
    'FLOAT_VECTOR'  : {'dtype': float,  'size': 3, 'shape': (3,), 'name': 'vector'},
    'FLOAT_COLOR'   : {'dtype': float,  'size': 4, 'shape': (4,), 'name': 'color'},
    'BYTE_COLOR'    : {'dtype': 'u1',   'size': 4, 'shape': (4,), 'name': 'color_srgb'},
    'STRING'        : {'dtype': 'U128', 'size': 0, 'shape': (),   'name': 'value'},
    'BOOLEAN'       : {'dtype': bool,   'size': 1, 'shape': (),   'name': 'value'},
    'FLOAT2'        : {'dtype': float,  'size': 2, 'shape': (2,), 'name': 'vector'},
    'INT8'          : {'dtype': int,    'size': 1, 'shape': (),   'name': 'value'},
    'INT32_2D'      : {'dtype': int,    'size': 2, 'shape': (2,), 'name': 'value'},
    }

# =============================================================================================================================
# Dynamic Record Array

class DynamicRecArray(object):
    """ Dynamic structured array

    A structured array with cache management to optimize record appending.
    """

    # ====================================================================================================
    # Initialization

    def __init__(self, dtype=None):

        self._length = 0

        if dtype is None:
            self._data = None
        else:
            self._data = np.zeros(0, dtype=np.dtype(dtype))

    # ====================================================================================================
    # Array interface

    def __str__(self):
        if self._data is None:
            return "<DynamicRecArray None>"
        return f"<DynamicRecArray: names: {self.names}, records: {len(self)} >"

    # ----------------------------------------------------------------------------------------------------
    # dtype

    @property
    def dtype(self):
        """ Array structured dtype

        Returns the dtype property of the structured array.
        """

        if self._data is None:
            return None
        else:
            return self._data.dtype

    @property
    def names(self):
        """ Column names.

        Returns the names property of the structured array.
        """

        if self._data is None:
            return []
        else:
            return self._data.dtype.names

    def attr_size(self, name):
        try:
            shape = self._data[name].shape
            if len(shape) == 1:
                return 1
            else:
                return shape[-1]
        except:
            print(f"Error with attribute name '{name}' in {self}")
            raise


    @property
    def data(self):
        """ The structured array.

        Returns the structured array with the proper length.
        """

        return self._data[:self._length]

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        return self._data[:self._length][index]

    def __setitem__(self, index, value):
        self._data[:self._length][index] = value

    # ====================================================================================================
    # Add a field

    def new_field(self, name, dtype, shape=None, data=None):
        """ Add a field to the structured array.

        Arguments
        ---------
            - name (str) : field name
            - dtype (type) : a valid numpy dtype
            - shape (tuple = None) : the shape of the field
            - data (any = None) : value to set to the newly created field
        """

        field_type = [(name, dtype) if shape is None else (name, dtype, shape)]
        if self.dtype is None:
            new_dtype = field_type
        else:
            new_dtype = self.dtype.descr + field_type

        size = 10 if self._data is None else len(self._data)

        new_data = np.zeros(size, new_dtype)
        if data is not None and self._length > 0:
            new_data[name][:self._length] = data

        if self._data is not None:
            for fname in self._data.dtype.names:
                new_data[fname] = self._data[fname]
            del self._data

        self._data = new_data

    # ====================================================================================================
    # Append a single record

    def append(self, rec, count=1):
        """ Append a single record

        Arguments
        ---------
            - rec : list of values to set
            - count (int = 1) : number of times to append the record
        """

        size = len(self._data)
        new_length = self._length + count
        if new_length > size:
            size = int(1.5*new_length)
            self._data = np.resize(self._data, size)

        if count == 1:
            self._data[self._length] = rec
        else:
            for i, name in enumerate(self.names):
                try:
                    self._data[name][self._length:new_length] = rec[i]
                except:
                    print('-'*100)
                    print("DynamicRecArray append error")
                    print(f"Name   : {name} ({i})")
                    print(f"Slice  : {self._length}:{new_length}")
                    print(f"Rec[i] : {rec[i]}")
                    print()

                    raise
            #self._data[self._length:new_length] = np.reshape(rec, (1, len(rec)))

        self._length = new_length

    # ====================================================================================================
    # Append several records

    def extend(self, recs):
        """ Extends with a list of records

        Arguments
        ---------
            - recs : list of list of values to set
        """

        size = len(self._data)
        new_length = self._length + len(recs)
        if new_length > size:
            size = int(1.5*new_length)
            self._data = np.resize(self._data, size)

        self._data[self._length:new_length] = recs
        self._length = new_length

    # ====================================================================================================
    # Multiply

    def multiply(self, count):
        """ Duplicate the array several times.

        numpy.resize is used in order to copy the values into the extended array.

        Before : [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        After  : [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 2, 3), (4, 5, 6), (7, 8, 9), ..., (1, 2, 3), (4, 5, 6), (7, 8, 9)]

        Arguments
        ---------
            - count (int) : number of times to multiply the array
        """

        if count <= 1 or len(self) == 0:
            return

        new_length = self._length*count
        new_size   = new_length

        self._data   = np.resize(self._data[:self._length], new_size)
        self._length = new_length

    # ====================================================================================================
    # Delete items

    def delete(self, index):
        """ Delete a selection of items.

        Arguments
        ---------
            - index (np.array index) : items to delete
        """

        self._data = np.delete(self._data[:self._length], index)
        self._length = len(self._data)


# =============================================================================================================================
# Geometry attributes

class Attributes(DynamicRecArray):

    # ----------------------------------------------------------------------------------------------------
    # Initialization

    def __init__(self, domain):
        """ Manages named attributes for a domain.

        Arguments
        ---------
            - domaine (str) : domain name
        """

        super().__init__()
        self.domain = domain
        self.infos  = {}

    # ----------------------------------------------------------------------------------------------------
    # Content

    def __str__(self):
        s = f"<Attributes: {len(self.names)}, entries: {len(self)}:"
        for name, info in self.infos.items():
            s += f"\n   - {name:10s}: {info['data_type']:12s} transfer {'True ' if info['transfer'] else 'False'} default: {info['default']}"
        return s + "\n>"

    # ====================================================================================================
    # Serialization

    def as_dict(self):
        return {
            'domain' : self.domain,
            'data'   : self._data,
            'length' : self._length,
            'infos'  : {name: {**info} for name, info in self.infos.items()},
            }

    @classmethod
    def FromDict(cls, d):

        attrs         = cls(domain=d['domain'])
        attrs._data   = d['data']
        attrs._length = d['length']
        attrs.infos   = {name: {**info} for name, info in d['infos'].items()}

        return attrs

    # ====================================================================================================
    # Create a new attribute

    # ----------------------------------------------------------------------------------------------------
    # New attribute

    def new(self, name, data_type, default, transfer=True):
        """ Create a new attribute.

        This method is called by more user friendly methods *new_float*, *new_bool*, *new_int*,...

        *data_type* is the Geometry Nodes data type, not a python or numpy.dtype value.


        Arguments
        ---------
            - name (str) : attribute name
            - data_type (str) : Geometry Nodes data type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'STRING', 'BOOLEAN', 'FLOAT2', 'INT8', 'INT32_2D')
            - default (any) : Default value when a new item is created
            - transfer (bool = True) : transfer the attribute to the object
        """

        # ----- Already exists

        if name in self.names:
            return

        # ----- Convert in numpy dtype and create the new field

        self.new_field(name, dtype=TYPES[data_type]['dtype'], shape=TYPES[data_type]['shape'], data=default)

        self.infos[name] = {
            'data_type' : data_type,
            'default'   : default,
            'transfer'  : transfer,
            }

        # ----- ID

        if name == 'ID':
            if len(self):
                self['ID'] = np.arange(len(self))

    # ----------------------------------------------------------------------------------------------------
    # Copy specifications of an attribute from other attributes

    def copy_attribute(self, other, name):
        """ Copy the specifications of an attribute from another Attributes.

        Note that only the attributes info are copied, not the values.

        Arguments
        ---------
            - other (Attributes) : Where to copy from
            - name (str) : attribute name
        """

        info = other.infos[name]
        self.new(name, **info)

    # ----------------------------------------------------------------------------------------------------
    # From concatenation form

    def from_concat(self, concat, default=None, transfer=True):
        """ Create a new attribute from concatenated form

        Arguments
        ---------
            - concat (str) : concatenation of data_type and name separated by '_' char, ex: 'FLOAT_length'
            - default (any = None) : default value
            - transfer (bool = True) : transfer the attribute to object
        """

        split = concat.split('_')
        data_type = split[0]
        if len(split) < 2 or data_type not in TYPES.keys():
            raise AttributeError(f"Attributes.from_concat error: 'concat' argument is not valid '{concat}'. It must be 'DATATYPE_name")

        name = concat[len(data_type) + 1:] # for FLOAT_my_name
        if default is None:
            shape = attribute_value_shape(data_type)
            if shape == ():
                default = 0
            else:
                default = np.zeros(shape, int)

        self.new(name, data_type, default, transfer=transfer)

    # ----------------------------------------------------------------------------------------------------
    # User friendly versions

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

    def new_string(self, name, default="", transfer=True):
        self.new(name, 'STRING', default, transfer=transfer)

    def new_byte_color(self, name, default=(0., 0., 0.), transfer=True):
        self.new(name, 'BYTE_COLOR', default, transfer=transfer)

    def new_int8(self, name, default=(0., 0., 0.), transfer=True):
        self.new(name, 'INT8', default, transfer=transfer)

    def new_int32_2d(self, name, default=(0., 0., 0.), transfer=True):
        self.new(name, 'INT32_2D', default, transfer=transfer)

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
        self._length = 0

    # ====================================================================================================
    # Clone / copy

    # ----------------------------------------------------------------------------------------------------
    # Clone to another instance

    def clone(self):
        """ Clone the attributes.
        """

        attrs = Attributes(domain=self.domain)

        attrs.infos = {name: {**info} for name, info in self.infos.items()}
        if self._data is not None:
            attrs._data   = np.array(self._data)
            attrs.size    = self.size
            attrs._length = self._length

        if hasattr(self, 'ID'):
            attrs.ID = self.ID

        return attrs

    # ----------------------------------------------------------------------------------------------------
    # Clone the definitions only

    def copy_definitions(self, other):
        """ Copy the attributes specifications from another.

        Note that only the attributes info are copied, not the values.

        Arguments:
            - attributes (Attributes) : the attributes to create
        """

        for name, info in other.infos.items():
            if name not in self.names:
                self.new(name, **info)

    #def get_selection(self, index):
    #
    #    return self[index]

    # ----------------------------------------------------------------------------------------------------
    # Copy attributes from another instance

    def copy_from(self, other, selection=None, exclude=[], include=None, only_new=False):
        """ Copy fields from another instance.

        Arguments
        ---------
            - other (Attributes) : the Attributes instance to copy fields from
            - selection (array selection) : selection to apply to other to match the number of items of self
            - exclude (list = []) : field names to exclude
            - include (list = None) : limit field names to this list
            - only_new (bool = False) : copy only fields that don't exist
        """

        # ----- Copy the attribites

        for name, info in other.infos.items():
            if name in exclude:
                continue
            if include is not None and name not in include:
                continue
            if only_new and name in self.names:
                continue

            self.new(name, **info)

            if selection is None:
                self[name] = other[name]
            else:
                self[name] = other[name][selection]

    # ====================================================================================================
    # Join
    # Join other Attributes
    # - add non existing attributes with their default values
    # - add new items

    def join(self, other):

        if len(other) == 0:
            return

        # ----- Copy the new attributes

        self.copy_definitions(other)

        # ----- Add the items from other attributes

        index0 = self._length
        self.add(len(other))
        index1 = self._length

        # ----- Copy the attributes

        for name in other.names:
            self[name][index0:index1] = other[name]

        # ----- Return indices to the added items

        return slice(index0, index1)

    # ====================================================================================================
    # Read / write a Blender object

    # ----------------------------------------------------------------------------------------------------
    # Read mesh attributes

    def from_object(self, spec):
        """ Read the object attributes.

        Arguments
        ---------
            - spec (str or mesh) : the mesh to set the attributes to
        """

        from geonodes.core import blender

        data = blender.get_data(spec)
        for name, binfo in blender.get_attributes(data).items():

            if binfo['domain'] != self.domain:
                continue

            name = binfo['name']
            if name[0] == '.':
                continue

            if not self.exists(name):
                self.new(name, binfo['data_type'], 0, transfer=True)

            self[name] = blender.get_attribute(data, name)

    # ----------------------------------------------------------------------------------------------------
    # Assign to blender mesh

    def to_object(self, spec, update=False):
        """ Transfer the attributes to a blender mesh object.

        Arguments
        ---------
            - spec (str or mesh) : the mesh to set the attributes to
            - attributes (array of st = None) : the attributes to transfer (all if None)
            - update (bool=False) : update the attributes values without trying to create them
        """

        from geonodes.core import blender

        data = blender.get_data(spec)

        for name, info in self.infos.items():

            if not info['transfer']:
                continue

            if info['data_type'] == 'STRING':
                pass

            if update:
                blender.set_attribute(data, name, self[name])
            else:
                blender.create_attribute(data, name, info['data_type'], domain=self.domain, value=np.array(self[name]))

    # ====================================================================================================
    # Read / write content

    # ----------------------------------------------------------------------------------------------------
    # Number of attributes

    @property
    def attr_count(self):
        """ Number of attributes.
        """
        return len(self.infos)

    # ----------------------------------------------------------------------------------------------------
    # Default record

    @property
    def default_record(self):
        return tuple([info['default'] for info in self.infos.values()])

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

    def attribute_dtype_OLD(self, name):
        """ The type of an attribute.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - type : attribute type
        """
        return self.infos[name].dtype

    def attribute_size_OLD(self, name):
        """ The size of an attribute.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - int : attribute size
        """
        return self.infos[name].size

    def attribute_shape_OLD(self, name):
        """ The shape of an attribute.

        Arguments
        ---------
            - name (str) : attribute name to test

        Returns
        -------
            - tuple : attribute shape
        """
        return TYPES[self.infos[name].data_type]['shape']

    # ----------------------------------------------------------------------------------------------------
    # Get set the values

    def get_attr_slice_OLD(self, name):
        info = self.infos.get(name)
        if info is None:
            raise AttributeError(f"Attributes {self.domain}: attribute '{name}' doesn't exist!")

        return info.slc

    def __getitem__OLD(self, name):
        info = self.infos.get(name)
        if info is None:
            raise AttributeError(f"Attributes {self.domain}: attribute '{name}' doesn't exist!")

        return self.arrays[info.array_index][..., info.slc]

    def __setitem__OLD(self, name, value):
        info = self.infos.get(name)
        if info is None:
            raise AttributeError(f"Attributes : attribute '{name}' doesn't exist!")

        self.arrays[info.array_index][..., info.slc] = value

    def set_selection_OLD(self, selection, attributes):
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
    # Add items

    @staticmethod
    def python_name(name):
        return name.replace(' ', '_')

    def add(self, count=None, **attrs):
        """ Add items.

        Arguments
        ---------
            - count (int=None) : number of items to add. Count is taken form attrs len if None
            - **attrs (attribute name: value) : value to set to the newly created items
        """

        # ----- Count the number of records to add based on the attributes shapes
        # The attributes can broadcasted to the number of created vectors

        if count is None:
            count = 0
            for attr_name in self.names:
                pyname = Attributes.python_name(attr_name)
                if pyname in attrs.keys():
                    n = np.size(attrs[pyname]) // self.attr_size(attr_name)
                    count = max(n, count)

        if count < 1:
            return

        # ----- Add the new records with their default value

        #print("ATTRIBUTES ADD")
        #print("self\n", self)
        #print("RECORD\n", self.default_record)
        #print()

        index = len(self)
        self.append(self.default_record, count=count)

        # ----- Set the new values

        dones = set()
        for attr_name in self.names:
            pyname = Attributes.python_name(attr_name)
            if pyname in attrs.keys():
                try:
                    self[index:index+count][attr_name] = attrs[pyname]
                except:
                    print('-'*80)
                    print("Attribute.add error:")
                    print(f"  name         : '{attr_name}', pyname: '{pyname}'")
                    print(f"  info         : {self.infos[pyname]}")
                    print(f"  len(self)    : {len(self)}")
                    print(f"  set at       : {index}:{index + count}")
                    print(f"  shape(value) : {np.shape(attrs[pyname])}")
                    print('-'*80)
                    print()
                    raise

                dones.add(pyname)

        # ----- Unknown attributes

        diff = set(attrs.keys()).difference(dones)
        if len(diff):
            raise AttributeError(f"Attributes.add error: '{self.domain}' has no attributes named '{diff}'.")

        # ----- Return indices on the created items

        return np.arange(index, index + count)

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
        attrs.new_string(    "string",     "STR")
        attrs.new_byte_color("byte color", (0, 127, 128, 255))
        attrs.new_int8(      "int 8",      32)
        attrs.new_int32_2d(  "int32 x 2",  (12, 13))

        attrs.add(8,
            int    = np.arange(8),
            float  = np.linspace(10, 17, 8),
            string = [f"string {i}" for i in range(8)],
            )
        attrs[0]   = (0, 0., False, (0, 0, 0), (0., 0., 0., 0.), (0, 0), "ZERO", (0, 0, 0, 0), 0, (0, 0))
        attrs[1:3] = (1, 1., False, (1, 1, 1), (1., 1., 1., 1.), (1, 1), "ONE",  (1, 1, 1, 1), 1, (1, 1))

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
    # Squeeze the cached arrays

    def squeeze_OLD(self):
        for a in self.arrays:
            if a is not None:
                a.squeeze()

    # ====================================================================================================
    # Shape keys

    @property
    def float_array_OLD(self):
        """ Get the array of float attributes.

        Returns
        -------
            - array of floats
        """

        return self.arrays[self.FLOAT]

# =============================================================================================================================
# Convert python type to data_type

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


# ====================================================================================================
# Vectors with attributes

class AttrVectors(Attributes):
    def __init__(self, vectors=None, **kwargs):

        super().__init__("VECTORS")

        self.new_vector("co")
        if vectors is not None:
            if np.shape(vectors) == (3,):
                self.add(count=1, co=vectors)
            else:
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

def test(ok_blender=False):

    def dump(title, attrs):
        print('-'*50)
        print(title)
        print(attrs)
        print()
        print(attrs.data)
        print()

    attrs = Attributes.TestAttributes()

    dump("Attributes test", attrs)

    # ----- Dict

    d = attrs.as_dict()
    other = Attributes.FromDict(d)
    other.equal_test("To / from dict")

    # ----- Copy attributes

    other = Attributes('POINT')
    for name in attrs.names:
        other.copy_attribute(attrs, name)

    other.add(count=len(attrs))
    other[:] = attrs
    other.equal_test("Copy attribute")


    # ----- Blender

    if ok_blender:
        cube = blender.create_mesh_object("Cube")
        attrs.to_object("Cube")

    print("Test done")

def test_avects():
    avects = AttrVectors(np.arange(12).reshape(4, 3), w=1.)
    avects.add_vectors(np.ones((2, 3)), w=19)
    avects.new_vector("Moment", (1, 0, 0))

    print(avects)
    print(avects[:])
    print(avects.w)
    print(avects.co)


#test_avects()



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
#performances(100000)
