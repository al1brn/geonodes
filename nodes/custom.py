#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:19:44 2024

@author: alain
"""

from geopy.nodes import constants
from geopy.nodes import utils

CUSTOM = {bl_id: {} for bl_id in constants.TREE_BL_IDS.values()}

def get_custom(tree_type, class_name, create=False):
    cm = CUSTOM[tree_type]
    d = cm.get(class_name)
    if d is None and create:
        d = {}
        cm[class_name] = d
    return d



def add_function(class_name, name,
                 target      = None,  # tuple of / or : None (Global), str or 'SOCKET'
                 self_socket = None,  # Static if None
                 use_enabled = False,
                 node_label  = True,
                 node_return = "node",
                 domain      = None,
                 loops       = None,
                 debug       = None,
                 descr       = None,
                 tree_class  = "GeoNodes",
                 **kwargs):
    
    methods = get_custom(constants.TREE_BL_IDS[tree_class], class_name, create=True)
    
    if name in methods:
        print(f"CAUTION: method {name} added twice for class {class_name}, target: {target}.")
        
    if loops is not None and target != 'SOCKET':
        for key in loops:
            if key.upper() not in name:
                raise AttributeError(f"Custom function error: the function name template {name} should contain {key.upper()} for distinct function names with loops {loops}.")
        
    methods[name] = {
        'target'      : target,
        'self_socket' : self_socket,
        'use_enabled' : use_enabled,
        'node_label'  : node_label,
        'node_return' : node_return,
        'domain'      : domain,
        'loops'       : [] if loops is None else list(loops),
        'debug'       : debug,
        'descr'       : descr,
        'kwargs'      : {**kwargs},
        'descr'       : descr,
        }
    
    
# =============================================================================================================================
# Maths
    
add_function("Math", "OPERATION", ('Float', 'Int', None),
             self_socket = 'value',
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['operation'],
             descr       = "value=self",
             )

add_function("VectorMath", "OPERATION", 'Vect',
             self_socket = 'vector',
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['operation'],
             descr       = "vector=self",
             )

add_function("BooleanMath", "OPERATION", ('Bool', None),
             self_socket = 'boolean',
             use_enabled = True,
             node_return = "node.boolean",
             loops       = ['operation'],
             descr       = "boolean=self",
             )

add_function("Mix", "mix_BLEND_TYPE", 'Col',
                 self_socket = 'a',
                 use_enabled = True,
                 node_return = "node.result",
                 loops       = ['blend_type'],
                 data_type   = 'RGBA',
                 descr       = "a=self",
                 )

add_function("Mix", "mix", 'SOCKET',
                 self_socket = 'a',
                 use_enabled = True,
                 node_return = "node.result",
                 loops       = ['data_type'],
                 descr       = "a=self",
                 )

add_function("Compare", "OPERATION", 'SOCKET',
                 self_socket = 'a',
                 use_enabled = True,
                 node_return = "node.result",
                 loops       = ['data_type', 'operation'],
                 descr       = "a=self",
                 )

add_function("Switch", "switch", 'SOCKET',
                 self_socket = 'false',
                 use_enabled = True,
                 node_return = "node.output",
                 loops       = ['input_type'],
                 descr       = "false=self",
             )

# =============================================================================================================================
# Named attributes

add_function("StoreNamedAttribute", "store_named_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "self.jump(node.geometry)",
             domain      = 'domain',
             loops       = ['data_type'],
             )

add_function("NamedAttribute", "named_DATA_TYPE", None,
             self_socket = None,
             node_return = "node.attribute",
             loops       = ['data_type'],
             )

add_function("CaptureAttribute", "capture_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "self.jump(node.geometry).node.attribute",
             domain      = 'domain',
             loops       = ['data_type'],
             )


# =============================================================================================================================
# Mesh Boolean

add_function("MeshBoolean", "difference", "Geometry",
             self_socket = 'mesh_1',
             use_enabled = True,
             node_return = "node.mesh",
             operation   = 'DIFFERENCE',
             descr       = "mesh_1=self, mesh_2=args",
             )

add_function("MeshBoolean", "intersect", "Geometry",
             self_socket = 'mesh_2',
             use_enabled = True,
             node_return = "node.mesh",
             operation   = 'INTERSECT',
             descr       = "mesh=geometry + args",
             )

add_function("MeshBoolean", "union", "Geometry",
             self_socket = 'mesh_2',
             use_enabled = True,
             node_return = "node.mesh",
             operation   = 'UNION',
             descr       = "mesh=geometry + args",
             )


# =============================================================================================================================
# Mesh methods
    
add_function("SampleIndex", "sample_index_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "node.output_socket",
             domain      = 'domain',
             loops       = ['data_type'],
             )
    





