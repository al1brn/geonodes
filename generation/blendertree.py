#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : blendertree
--------------------
- Create and delete trees
- Loops on nodes

classes
-------


functions
---------
- get_tree          : get or create a tree of the given type
- del_tree          : delete the tree
- loop_on_nodes     : loop on all the possible nodes and run a function for each
- gen_SOCKET_TYPES  : create the dict SOCKET_TYPES
- gen_NODE_NAMES    : create the dict NODE_NAMES
- gen_maths         : legacy - used once
- gen_boolean_math  : legacy - used once
- gen_vector_math   : legacy - used once
- gen_int_compare   : legacy - used once

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import bpy
from pprint import pprint

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

    if btree is not None:
        bpy.data.node_groups.remove(btree)

# =============================================================================================================================
# Loop on nodes
# - func : function of template lambda(bnode, **kwargs)

def loop_on_nodes(func, tree_type='GeometryNodeTree', **kwargs):

    btree = get_tree("Dump", tree_type=tree_type, create=True)
    btree.nodes.clear()

    for type_name in dir(bpy.types):

        try:
            bnode = btree.nodes.new(type=type_name)
        except RuntimeError as e:
            continue

        if 'legacy' in bnode.name.lower():
            continue

        func(bnode, **kwargs)

    del_tree(btree)

# =============================================================================================================================
# Build the dictionnary of socket types -> list of socket node

def gen_SOCKET_TYPES(tree_type='GeometryNodeTree'):

    types = {}

    def f(bnode):
        for sockets in [bnode.inputs, bnode.outputs]:
            for sock in sockets:
                if sock.type not in types.keys():
                    types[sock.type] = [sock.bl_idname]
                elif sock.bl_idname not in types[sock.type]:
                    types[sock.type].append(sock.bl_idname)

    loop_on_nodes(f, tree_type=tree_type)

    pprint(types)

# =============================================================================================================================
# Build the dictionnary of node name -> bl_idname

def gen_NODE_NAMES(tree_type='GeometryNodeTree'):

    names = {}

    def f(bnode):
        names[bnode.name.lower()] = bnode.bl_idname

    loop_on_nodes(f, tree_type)

    print('-'*100)
    print(f"{len(names)} NODE NAMES for", tree_type)
    print()
    for k, v in names.items():
        sk = f"'{k}'"
        print(f"    {sk:25s} : '{v}',")
    print()

    #pprint(names)

# =============================================================================================================================
# Some legacy generators

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
