#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
-----------------------------------------------------

module : utils
------------------
- base utils

create : 2024/07/23
"""

import unicodedata
import numpy as np

from pprint import pprint
import bpy

from geonodes.structured import constants

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

    assert(name != "")

    return prefix_figure(remove_accents(clean(name, '_').lower()))

    if name == 'ID':
        return 'ID'
    else:
        return prefix_figure(remove_accents(clean(name, '_').lower()))


# =============================================================================================================================
# Get / delete a tree

# ----------------------------------------------------------------------------------------------------
# Get / Create a tree

def get_tree(name, tree_type='GeometryNodeTree', create=False, clear=False):
    """ Get or create a new nodes tree

    Arguments
    ---------
        - name (str) : Tree name
        - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
        - create (bool = False) : Create the tree if it doesn't exist
        - clear (bool = False) : Clear the tree if it exists

    Returns
    -------
        - Tree of type matching the request or None if it doesn't exist
    """

    btree = bpy.data.node_groups.get(name)
    if btree is None or btree.bl_idname != tree_type:
        if not create:
            return None
        btree = bpy.data.node_groups.new(name=name, type=tree_type)

    if clear:
        btree.nodes.clear()

    return btree

# ----------------------------------------------------------------------------------------------------
# Delete a tree

def del_tree(btree): #, tree_type='GeometryNodeTree'):

    """ Delete a tree

    Arguments
    ---------
        - btree (blender Tree or str : Tree or tree name
    """

    if isinstance(btree, str):
        btree = bpy.data.node_groups.get(name)

    if btree is not None:
        bpy.data.node_groups.remove(btree)

# =============================================================================================================================
# Get a blender socket from either a Blender NodeSocket or a DataSocket

def get_bsocket(value):
    if isinstance(value, bpy.types.NodeSocket):
        return value
    else:
        return getattr(value, '_bsocket', None)

# =============================================================================================================================
# Get Value socket type

def get_value_socket_type(value):

    # ----- None : let's suppose it is for Geometry

    if value is None:
        return None

    # ----- It is a DataSocket

    if hasattr(value, '_bsocket'):
        return value.SOCKET_TYPE

    # ----- A Blender node socket

    elif isinstance(value, bpy.types.NodeSocket):
        return value.type

    # ----- Ok, it is a python type

    elif isinstance(value, bool):
        return 'BOOLEAN'

    elif isinstance(value, int):
        return 'INT'

    elif isinstance(value, float):
        return 'VALUE'

    elif isinstance(value, str):
        return 'STRING'

    elif isinstance(value, bpy.types.Object):
        return 'OBJECT'

    elif isinstance(value, bpy.types.Material):
        return 'MATERIAL'

    elif isinstance(value, bpy.types.Image):
        return 'IMAGE'

    elif isinstance(value, bpy.types.Collection):
        return 'COLLECTION'

    elif np.shape(value) != ():
        size = np.size(value)
        if size == 3:
            return 'VECTOR'
        elif size == 4:
            return 'RGBA'
        elif size == 16:
            return 'MATRIX'
        else:
            raise NodeError(f"Value shape is {np.shape(value)} which is incorrect")

    else:
        return None

def get_value_data_type_1(value):
    socket_type = get_value_socket_type(value)
    if socket_type is None:
        return None
    else:
        return constants.DATA_TYPES_1.get(socket_type)

def get_value_data_type_2(value):
    socket_type = get_value_socket_type(value)
    if socket_type is None:
        return None
    else:
        return constants.DATA_TYPES_2.get(socket_type)


# =============================================================================================================================
# Loop on nodes
# - func : function of template lambda(bnode, **kwargs)

def loop_on_nodes(func, **kwargs):

    btree = get_tree("Dump", create=True, clear=True)

    for type_name in dir(bpy.types):

        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue

        if 'legacy' in bnode.name.lower():
            continue

        func(bnode, **kwargs)

    Tree.del_tree(btree)

# =============================================================================================================================
# Build the dictionnary of socket types -> list of socket node

def print_sockets():

    types = {}

    def f(bnode):
        for sockets in [bnode.inputs, bnode.outputs]:
            for sock in sockets:
                if sock.type not in types.keys():
                    types[sock.type] = [sock.bl_idname]
                elif sock.bl_idname not in types[sock.type]:
                    types[sock.type].append(sock.bl_idname)

    loop_on_nodes(f)

    pprint(types)

# =============================================================================================================================
# Build the dictionnary of node name -> bl_idname

@staticmethod
def print_node_names():

    names = {}

    def f(bnode):
        names[bnode.name.lower()] = type_name

    loop_on_nodes(f)

    pprint(names)

def gen_math():
    MATH_OPS = [
        'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', ('LOGARITHM', 'log'), 'SQRT', 'INVERSE_SQRT',
        ('ABSOLUTE', 'abs'), 'EXPONENT', ('MINIMUM', 'min'), ('MAXIMUM', 'max'), 'LESS_THAN', 'GREATER_THAN', 'SIGN',
        'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO',
        'WRAP', 'SNAP', 'PINGPONG',
        ('SINE', 'sin'), ('COSINE', 'cos'), ('TANGENT', 'tan'), ('ARCSINE', 'asin'), ('ARCCOSINE', 'acos'), ('ARCTANGENT', 'atan'), ('ARCTAN2', 'atan2'), 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES',
        ]

    for item in MATH_OPS:
        if isinstance(item, str):
            name = item.lower()
            op   = item
        else:
            op, name = item

        print(f"def {name}(value, other, use_clamp=None):")
        print("    return Node(\"Math\", " + "{0: value, 1: other}" + f", use_clamp=use_clamp, operation='{op}')._out")
        print()

def gen_boolean_math():

    OPS = [('AND', 'band', 2), ('OR', 'bor', 2), ('NOT', 'bnot', 1), 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY']

    for item in OPS:
        if isinstance(item, str):
            name  = item.lower()
            op    = item
            count = 2
        else:
            op, name, count = item

        if count == 1:
            print(f"def {name}(value):")
            print("    return Node(\"Boolean Math\", " + "{0: value}" + f", operation='{op}')._out")
        else:
            print(f"def {name}(value, other):")
            print("    return Node(\"Boolean Math\", " + "{0: value, 1: other}" + f", operation='{op}')._out")

        print()

def gen_vector_math():

    OPS = [('ADD', 'vadd', 2), ('SUBTRACT', 'vsubtract', 2), ('MULTIPLY', 'vmultiply', 2), ('DIVIDE', 'vdivide', 2),
            ('MULTIPLY_ADD', 'vmultiply_add', 2), 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT',
           'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', ('LENGTH', 'length', 1), 'SCALE', ('NORMALIZE', 'normalize', 1),
           ('ABSOLUTE', 'babs', 1), ('MINIMUM', 'vmin', 2), ('MAXIMUM', 'vmax', 2), ('FLOOR', 'vfloor', 1), ('CEIL', 'vceil', 1),
           ('FRACTION', 'vfraction', 1), ('MODULO', 'vmodulo', 2), ('WRAP', 'vwrap', 2), ('SNAP', 'vsnap', 2),
           ('SINE', 'vsin', 1), ('COSINE', 'vcos', 1), ('TANGENT', 'vtan', 1)]

    for item in OPS:
        if isinstance(item, str):
            name  = item.lower()
            op    = item
            count = 2
        else:
            op, name, count = item

        if count == 1:
            print(f"def {name}(value):")
            print("    return Node(\"Vector Math\", " + "{0: value}" + f", operation='{op}')._out")
        else:
            print(f"def {name}(value, other):")
            print("    return Node(\"Vector Math\", " + "{0: value, 1: other}" + f", operation='{op}')._out")

        print()

def gen_int_compare():

    OPS = ['LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL']

    for item in OPS:
        name  = item.lower()
        op    = item

        print(f"def {name}(self, other):")
        print("    return Node(\"Compare\", " + "{'A': self, 'B': other}" + f", operation='{op}', data_type='INT')._out")
        print()



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
# Get a Blender Data resource

def get_blender_resource(socket_type, value):

    spec = {
        'OBJECT':     {'coll': bpy.data.objects,     'type': bpy.types.Object},
        'COLLECTION': {'coll': bpy.data.collections, 'type': bpy.types.Collection},
        'IMAGE':      {'coll': bpy.data.images,      'type': bpy.types.Image},
        'MATERIAL':   {'coll': bpy.data.materials,   'type': bpy.types.Material},
        }[socket_type]

    if isinstance(value, spec['type']):
        return value
    else:
        return spec['coll'].get(value)
