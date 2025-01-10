#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC hidden

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : utils
--------------
- utilities

classes
-------


functions
---------
- remove_accents    : remove accents from a string
- clean             : clean a string
- prefix_figure     : prefix a string by '_' if it is a number, e.g. : '3D Cursor' -> _3d_cursor
- get_bsocket       : get a blender socket from a value which can be a Socket or a blender.types.NodeSocket
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
- python_value_for_socket : build a python value acceptable as socket default value

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import unicodedata
import numpy as np

from pprint import pprint
import bpy

from .scripterror import NodeError
from . import constants

# =============================================================================================================================
# Get / delete a tree

# ----------------------------------------------------------------------------------------------------
# Get a tree, create it if it doesn't exist

def get_tree(name, tree_type='GeometryNodeTree', create=True):
    """ Get or create a new nodes tree

    Arguments
    ---------
        - name (str) : Tree name
        - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
        - create (bool = False) : Create the tree if it doesn't exist

    Returns
    -------
        - Tree of type matching the request or None if it doesn't exist
    """

    # -----------------------------------------------------------------------------------------------------------------------------
    # Loop on the synonyms

    for i in range(10):
        if i == 0:
            name_i = name
        else:
            name_i = f"{name}.{i:03}"

        btree = bpy.data.node_groups.get(name_i)
        if btree is not None and btree.bl_idname == tree_type and btree.description=='GEONODES':
            return btree

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create the new tree

    if not create:
        return None

    btree = bpy.data.node_groups.new(name=name, type=tree_type)
    btree.description = 'GEONODES'

    return btree

# ----------------------------------------------------------------------------------------------------
# Delete a tree

def del_tree(btree):

    """ Delete a tree

    Arguments
    ---------
        - btree (blender Tree or str : Tree or tree name
    """

    if isinstance(btree, str):
        btree = bpy.data.node_groups.get(btree)

    if btree is not None and btree.description=='GEONODES':
        bpy.data.node_groups.remove(btree)

# ====================================================================================================
# Litteral to python name

# ----------------------------------------------------------------------------------------------------
# Replace accents and replace non kw chars by '_'

def only_kw_chars(s):

    accents = {'à': 'a', 'â': 'a', 'À': 'A', 'Â': 'A',
               'é': 'e', 'è': 'e', 'ê':'e', 'ë': 'e', 'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
               'î': 'i', 'Î': 'I',
               'ô': 'o', 'Ô': 'O',
               'û': 'u', 'ü': 'u', 'ù': 'u', 'Ù': 'U', 'Û': 'U', 'Ü': 'U'}

    valids = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"

    cleaned = ""
    last = ""
    for c in s:
        # Remove accents
        ch = accents.get(c, c)

        # Append if valid
        if ch in valids:
            cleaned += ch
            last = ch

        # Otherwise add a _ char, avoiding doing it twice
        elif last != '_':
            cleaned += '_'
            last = '_'

    # Remove '__' sequences

    for i in range(10):
        p = cleaned.find('__')
        if p < 0:
            break
        cleaned = cleaned.replace('__', '_')

    return cleaned

# ----------------------------------------------------------------------------------------------------
# Camel version of a string

def CamelCase(s):

    if s == "":
        return None

    title = ""
    for w in s.split(' '):
        if w in ['RGB', 'HSL', 'HSV', 'BSDF']:
            title += w
        else:
            title += w.title()


    cc = only_kw_chars(title)

    cc = cc.replace('_', '')
    if cc[0] in "0123456789":
        cc = "_" + cc

    return cc

# ----------------------------------------------------------------------------------------------------
# Snake case version of a string

def snake_case(s) -> str:
    if s == "":
        return ""

    sc = only_kw_chars(s.lower())

    if sc[0] in "0123456789":
        sc = '_' + sc

    return sc

# ----------------------------------------------------------------------------------------------------
# Ensure socket name unicity

def ensure_uniques(names: list[str], single_digit: bool = False):
    """ Build a list of unique names from a list

    Doublons are suffixed by an index:
    - ['key', 'key', 'other'] -> ['key', 'key_001', 'other']

    Arguments
    ---------
    - names : list of names with possible doublons
    - single_digit : 'key_1' rather that 'key_001'

    Returns
    -------
    - list of str : doublons are suffixed by an index
    """
    homos  = {}
    uniques = []
    for name in names:
        count = homos.get(name)
        if count is None:
            uniques.append(name)
            homos[name] = 1
        else:
            if single_digit:
                uniques.append(f"{name}_{count:d}")
            else:
                uniques.append(f"{name}_{count:03d}")
            homos[name] = count + 1
    return uniques

# =============================================================================================================================
# Get a node bl_idname from a name

def get_node_bl_idname(node_name, tree_type, halt=True):

    bl_idname = ""

    # Node name is good
    if node_name in constants.NODE_NAMES[tree_type]:
        return constants.NODE_NAMES[tree_type][node_name]

    # Could be the bl_idname
    if node_name in constants.NODE_NAMES[tree_type].values():
        return node_name

    # Perhaps lower / upper case problem
    for nn, blid in constants.NODE_NAMES[tree_type].items():
        if nn.lower() == node_name.lower():
            print(f"CAUTION: node name '{node_name}' doesn't match any node name. Lower case matching is taken: {nn}")
            return blid

    # Error :(
    if not halt:
        return None

    for tt in constants.NODE_NAMES.keys():
        if tt == tree_type:
            continue
        if node_name in constants.NODE_NAMES[tt]:
            raise NodeError(f"Node '{node_name}' is a node of tree '{tt}', it doesn't exist for tree '{tree_type}'")

    raise NodeError(f"Node '{node_name}' doesn't exist")


# =============================================================================================================================
# Get a blender socket from either a Blender NodeSocket or a Socket

def get_bsocket(value):
    if isinstance(value, bpy.types.NodeSocket):
        return value
    else:
        return getattr(value, '_bsocket', None)

# =============================================================================================================================
# Get Value socket type

def get_socket_type(value, restrict_to=None, default=None):

    # ----- It is a Socket

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
        if type(value).__name__ == 'method':
            try:
                fname = value.__name__
                prop = f": '{fname}()'"
            except:
                fname = str(value)
                prop = ""
            raise NodeError(f"Socket error: trying to use method '{fname}' as value. You certainly forgot parenthesis{prop}.", keyword=fname, valids=restrict_to)
        else:
            raise NodeError(f"Socket error: type of value [{value}] ({type(value).__name__}) is not valid.", valids=restrict_to)
    else:
        return socket_type

def get_node_data_type(node_name, tree_type, value, default=None):

    blid = get_node_bl_idname(node_name, tree_type)
    valids = list(constants.NODE_DATA_TYPES[blid].values())[0]

    socket_type = get_socket_type(value)
    if socket_type in valids.keys():
        return valids[socket_type]

    if default is None:
        raise NodeError(f"Node '{node_name}' doesn't accept '{socket_type}' data type, only {list(valids)}")

    return default


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
# Select the proper data type in the provided dict
# Used in generated source code

def get_argument_data_type(argument, type_to_value, node_name=None, arg_name=None):
    if argument is None:
        return list(type_to_value.values())[0]

    socket_type = get_socket_type(argument)
    if socket_type in type_to_value:
        return type_to_value[socket_type]

    if node_name is not None and arg_name is not None:
        print(f"CAUTION node '{node_name}': argument '{arg_name}' type ('{socket_type}') is not in {list(type_to_value).keys()}.")

    return list(type_to_value.values())[0]

# =============================================================================================================================
# Create a numpy array of the correct shape

def value_to_array(value, shape):

    a = np.array(value, object)

    if np.shape(a) in [(), (1,)]:
        return np.resize(a, shape)

    if np.size(a) == np.prod(shape).astype(int):
        return np.reshape(a, shape)
    else:
        raise Exception(f"The value {value} with shape {np.shape(a)} (size: {np.size(a)}) can't be reshaped into {shape} (size: {np.prod(shape).astype(int)})")




    try:
        return np.reshape(a, shape)
    except:
        raise Exception(f"The value {value} with shape {np.shape(a)} can't be reshaped into {shape}")

# =============================================================================================================================
# Some utilities

def is_vector_like(value):

    return get_input_type(value) in ['RGBA', 'VECTOR', 'ROTATION']

def is_color_like(value):
    return get_input_type(value) in ['RGBA', 'VECTOR']

def is_matrix_like(value):
    return get_input_type(value) in ['MATRIX']

def is_value_like(value):
    return get_input_type(value) in ['FLOAT', 'INT', 'BOOLEAN']

def is_int_like(value):
    return get_input_type(value) in ['INT', 'BOOLEAN']

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
        'TEXTURE':    {'coll': bpy.data.textures,    'type': bpy.types.Texture},
        }[socket_type]

    if value is None:
        return None

    if isinstance(value, spec['type']):
        return value
    else:
        return spec['coll'].get(value)

def get_object(value):
    return get_blender_resource('OBJECT', value)

# =============================================================================================================================
# Get a python value compatible with socket default_value

def python_value_for_socket(value, socket_type):

    if value is None:
        return None

    if socket_type == 'BOOLEAN':
        return bool(value)

    elif socket_type == 'INT':
        return int(value)

    elif socket_type == 'VALUE':
        return float(value)

    elif socket_type in ['VECTOR', 'ROTATION']:
        return value_to_array(value, (3,))

    elif socket_type == 'RGBA':
        if hasattr(value, '__len__'):
            if len(value) == 3:
                return (value[0], value[1], value[2], 1)
            else:
                return value
        else:
            return (value, value, value, 1)

    elif socket_type in ['STRING', 'MENU']:
        return str(value)

    elif socket_type in ['COLLECTION', 'OBJECT', 'IMAGE', 'MATERIAL']:
        return get_blender_resource(socket_type, value)

    else:
        raise NodeError(f"python_value_for_socket error: impossible to build a value from [{value}] for socket '{socket_type}'")

# =============================================================================================================================
# Named attribute utilities

def is_named_attr(prop_name):
    return len(prop_name) > 2 and (prop_name[0] == '_') and (prop_name[1].upper() == prop_name[1])

def get_attr_name(prop_name):
    if len(prop_name) < 2:
        return None
    if prop_name[0] != "_":
        return None
    if prop_name[1].upper() != prop_name[1]:
        return None

    return prop_name[1:].replace('_', ' ')

def get_prop_name(attr_name):
    return "_" + attr_name.replace(' ', '_')
