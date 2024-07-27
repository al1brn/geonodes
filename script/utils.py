#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : utils
--------------
- base utils

classes
-------


functions
---------
- remove_accents    : remove accents from a string
- clean             : clean a string
- prefix_figure     : prefix a string by '_' if it is a number, e.g. : '3D Cursor' -> _3d_cursor
- socket_name       : transform a user name in snake case python name, e.g. : "Color Ramp" -> 'color_ramp'
- get_bsocket       : get a blender socket from a value which can be a DataSocket or a blender.types.NodeSocket
- get_socket_type   : get a socket type in SOCKET_TYPES.keys() from either a socket or a value
- get_data_type     : get a data type in DATA_TYPES from either a socket or a value
- get_input_type    : get an input type in INPUT_TYPES from either a socket or a value
- value_to_array    : convert a value into an array of the given shape. Raises an error if not possible
- is_vector_like    : socket type is a vector
- is_color_like     : socket type is a color
- is_matrix_like    : socket type is a matrix
- is_value_like     : socket type is a value
- has_bsocket       : value is a socket or a tuple with sockets
- get_blender_resource : get a Blender ressource its name, e.g. = get_blender_resource('MATERIAL', "Material") -> bpy.materials.get("Material")

updates
-------
- creation : 2024/07/23
"""

import unicodedata
import numpy as np

from pprint import pprint
import bpy

from .scripterror import NodeError
from . import constants

# ====================================================================================================
# Litteral to python name

# ----------------------------------------------------------------------------------------------------
# Remove accents

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode('utf-8')

# ----------------------------------------------------------------------------------------------------
# Clean

def clean(s, rep=' '):
    for c in ['/', ':', '-', '.',' ']:
        s = s.replace(c, rep)
    return s

# ----------------------------------------------------------------------------------------------------
# Add a _ prefix is name starts with a figure

def prefix_figure(name):
    if name[0].isnumeric():
        return "_" + name
    else:
        return name

def socket_name(name):

    if name == "":
        return None

    return prefix_figure(remove_accents(clean(name, '_').lower()))

    if name == 'ID':
        return 'ID'
    else:
        return prefix_figure(remove_accents(clean(name, '_').lower()))

# =============================================================================================================================
# Get a blender socket from either a Blender NodeSocket or a DataSocket

def get_bsocket(value):
    if isinstance(value, bpy.types.NodeSocket):
        return value
    else:
        return getattr(value, '_bsocket', None)

# =============================================================================================================================
# Get Value socket type

def get_socket_type(value, restrict_to=None, default=None):

    # ----- It is a DataSocket

    socket_type = default
    if hasattr(value, 'SOCKET_TYPE'):
        socket_type = value.SOCKET_TYPE

    # ----- A Blender node socket

    elif isinstance(value, bpy.types.NodeSocket):
        socket_type = value.type

    # ----- Ok, it is a python type

    elif isinstance(value, bool):
        socket_type = 'BOOLEAN'

    elif isinstance(value, int):
        socket_type = 'INT'

    elif isinstance(value, float):
        socket_type = 'VALUE'

    elif isinstance(value, str):
        socket_type = 'STRING'

    elif isinstance(value, bpy.types.Object):
        socket_type = 'OBJECT'

    elif isinstance(value, bpy.types.Material):
        socket_type = 'MATERIAL'

    elif isinstance(value, bpy.types.Image):
        socket_type = 'IMAGE'

    elif isinstance(value, bpy.types.Collection):
        socket_type = 'COLLECTION'

    elif np.shape(value) != ():
        size = np.size(value)
        if size == 3:
            socket_type = 'VECTOR'
        elif size == 4:
            socket_type = 'RGBA'
        elif size == 16:
            socket_type = 'MATRIX'
        else:
            raise NodeError(f"Value shape is {np.shape(value)} which is incorrect")

    else:
        socket_type = default

    if restrict_to is not None:
        if socket_type not in restrict_to:
            socket_type = default

    if socket_type is None:
        raise NodeError(f"Socket type of value [{value}] is not valid for operation", valids=restrict_to)
    else:
        return socket_type

def get_data_type(value, restrict_to=None, default='FLOAT'):

    if value is None:
        data_type = default
        socket_type = 'NONE'

    else:
        socket_type = get_socket_type(value)

        data_type = constants.DATA_TYPES.get(socket_type)
        if data_type is not None and restrict_to is not None:
            if data_type not in restrict_to:
                data_type = default

        if data_type is None:
            data_type = default

    if data_type is None:
        raise NodeError(f"Socket type '{socket_type}' has not a valid data type for the node", valid_types=restrict_to)
    else:
        return data_type

def get_input_type(value, restrict_to=None, default='FLOAT'):

    if value is None:
        input_type = default
        socket_type = 'NONE'

    else:
        socket_type = get_socket_type(value)

        input_type = constants.INPUT_TYPES.get(socket_type)
        if input_type is not None and restrict_to is not None:
            if input_type not in restrict_to:
                input_type = default

        if input_type is None:
            input_type = default

    if input_type is None:
        raise NodeError(f"Socket type '{socket_type}' has not a valid input type for the node", valid_types=restrict_to)
    else:
        return input_type

# =============================================================================================================================
# Create a numpy array of the correct shape

def value_to_array(value, shape):

    a = np.array(value, object)

    if np.shape(a) in [(), (1,)]:
        return np.resize(a, shape)

    try:
        return np.reshape(a, shape)
    except:
        raise Exception(f"The value {value} with shape {np.shape(a)} can't be reshaped into {shape}")

# =============================================================================================================================
# Some utilities

def is_vector_like(value):
    return get_socket_type(value) in ['VECTOR', 'ROTATION']

def is_color_like(value):
    return get_socket_type(value) in ['COLOR']

def is_matrix_like(value):
    return get_socket_type(value) in ['MATRIX']

def is_value_like(value):
    return get_socket_type(value) in ['FLOAT', 'INT', 'BOOLEAN']

def has_bsocket(value):
    if get_bsocket(value) is not None:
        return True

    if not hasattr(value, '__len__'):
        return False

    for item in value:
        if get_bsocket(item) is not None:
            return True

    return False



# =============================================================================================================================
# Get a Blender Data resource

def get_blender_resource(socket_type, value):

    spec = {
        'OBJECT':     {'coll': bpy.data.objects,     'type': bpy.types.Object},
        'COLLECTION': {'coll': bpy.data.collections, 'type': bpy.types.Collection},
        'IMAGE':      {'coll': bpy.data.images,      'type': bpy.types.Image},
        'MATERIAL':   {'coll': bpy.data.materials,   'type': bpy.types.Material},
        }[socket_type]

    if value is None:
        return None

    if isinstance(value, spec['type']):
        return value
    else:
        return spec['coll'].get(value)
