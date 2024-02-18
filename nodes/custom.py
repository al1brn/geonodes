#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:19:44 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : custom
---------------
Depending on their sockets, nodes can be automaticalley implemented as class socket methods.
The custom functions defined more accurate ways to implement nodes using add_function function:

update : 2024/02/17
"""

from geonodes.nodes import constants
from geonodes.nodes import utils

CUSTOM = {bl_id: {} for bl_id in constants.TREE_BL_IDS.values()}

# =============================================================================================================================
# Get the custom functions declared for a node class name

def get_custom(tree_type, class_name, create=False):
    """ Get the custome functions defined for a Node.
    
    Arguments
    ---------
        - tree_type (str = 'GeometryNodeTree') : tree type in ('CompositorNodeTree', 'TextureNodeTree', 'GeometryNodeTree', 'ShaderNodeTree')
        - class_name : a node class name
        - create (bool = True) : create the dictionaty entry if if doesn't exist
        
    Returns
    -------
        - dict
    """
        
    cm = CUSTOM[tree_type]
    d = cm.get(class_name)
    if d is None and create:
        d = {}
        cm[class_name] = d
    return d

# =============================================================================================================================
# Declare a custom function for a node class name

def add_function(class_name, name,
                 target       = None,  # tuple of / or : None (Global), str or 'SOCKET'
                 self_socket  = None,  # Static if None
                 use_enabled  = False,
                 node_label   = True,
                 node_return  = "node",
                 domain       = None,
                 loops        = None,
                 debug        = None,
                 descr        = None,
                 tree_classes = None,
                 **kwargs):
    
    """ Declare a custom function for a node class name.
    
    Can be use to create as many functions as they are possible values for a node parameter.
    For instance, the node Math can give birth to one global function and one method per possible value of the operation parameter:
        - operation = 'SINE' -> sin global function, Float.sin method
        - operation = 'COSINE' -> cos global function, Float.sin method
        
    When the name of the function depends upon the value of a parameter, use the capitalized named of the parameter in the name.
    For instance:
        - node Math : name = 'OPERATION'
        - node StoreNamedAttribute : name = 'store_named_DATA_TYPE'
        
    The parameters to loop on are given in the loops argument.
    
    The following example create the Geometry and Domain method: store_named_float, store_named, vector, store_named_color,...
        
    ```python
    add_function("StoreNamedAttribute", "store_named_DATA_TYPE", "Geometry",
                 self_socket = 'geometry',
                 use_enabled = True,
                 node_return = "self.jump(node.geometry)",
                 domain      = 'domain',
                 loops       = ['data_type'],
             )
    ```
    
        
    Arguments
    ---------
        - class_name  : Node class name
        - name : name of the function to create. Can contain name temps such as func_DATA_TYPE -->  func_float, func_vector, ...
        - target (str = None) : socket class. Global function if None
        - self_socket (str = None) : Node socket to plug self to
        - use_enabled (bool = False) : Get the enabled sockets rather than all the possible sockets
        - node_label (bool = True) : add node_label and node_color arguments
        - node_return (str = "node") : return statement. By default, returns the node. Use node_return = node.output_socket to return the socket
        - domain (str = None) : name of the domain parameter. If not None, create a function for the Domain class (target should be Geometry)
        - loops (list = None) : list of parameters to loop on. One function is created per parameter possible values
        - debug (str = None) : python source code to insert for debug
        - descr (str = None) : description string
        - tree_type (str = "GeoNodes") : str in 'GeoNodes', 'Shader', 'Compositor', 'Texture'
        - kwargs : keys, values for parameter to set
        
    """
    
    if tree_classes is None:
        tree_classes = ("GeoNodes", "Shader")
    elif isinstance(tree_classes, str):
        tree_classes = (tree_classes,)
    
    for tree_class in tree_classes:
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

for tree_classes in ['GeoNodes', ('Shader', 'Compositor', 'Texture')]:
    if tree_classes == 'GeoNodes':
        targets = ('Float', 'Int', None)
    else:
        targets = ('Float', None)
    
    add_function("Math", "OPERATION", targets,
                 self_socket  = 'value',
                 use_enabled  = True,
                 node_return  = "node.output_socket",
                 loops        = ['operation'],
                 descr        = "value=self",
                 tree_classes = tree_classes,
                 )

add_function("VectorMath", "OPERATION", 'Vect',
             self_socket = 'vector',
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['operation'],
             descr       = "vector=self",
             )

add_function("SeparateXYZ", "xyz", 'Vect',
             self_socket = 'vector',
             descr       = "Shortcut for Vect.separate_xyz",
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

add_function("RandomValue", "random_DATA_TYPE", None,
                 self_socket = None,
                 use_enabled = True,
                 node_return = "node.value",
                 loops       = ['data_type'],
                 descr       = None,
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
# Geometry methods
    
add_function("SampleIndex", "sample_index_DATA_TYPE", "Geometry",
             self_socket = 'geometry',
             use_enabled = True,
             node_return = "node.output_socket",
             domain      = 'domain',
             loops       = ['data_type'],
             )

# =============================================================================================================================
# Shader nodes

add_function("CombineColor", "combine_MODE", None,
             self_socket = None,
             use_enabled = True,
             node_return = "node.output_socket",
             loops       = ['mode'],
             )

    





