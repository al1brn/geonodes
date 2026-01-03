"""
Generate config dicts from current Blender version
"""
print('-'*100)

import bpy
from datetime import datetime
import textwrap
import inspect

from pathlib import Path
from pprint import pprint

# ====================================================================================================
# Hard stuff
# ====================================================================================================

# These are simply copied to config
# This allow to expose these file to gen_auto

GEOMETRY_CLASSES  = ['Geometry', 'Mesh', 'Curve', 'Cloud', 'Instances', 'Volume', 'GrasePencil']
DOMAIN_CLASSES    = ['Domain', 'Point', 'Vertex', 'CloudPoint', 'SplinePoint', 'Face', 'Edge', 'Corner', 'Spline', 'Layer', 'Instance']
ATTRIBUTE_CLASSES = ['Boolean', 'Integer', 'Float', 'Vector', 'Color', 'Matrix', 'Rotation']
PYTHON_TYPES = {
    'Boolean'  : ('bool', False),
    'Integer'  : ('int', 0),
    'Float'    : ('float', 0.),
    'Vector'   : ('tuple', (0, 0, 0)),
    'Color'    : ('tuple', (1, 1, 1)),
    'Matrix'   : ('tuple', ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))),
    'Rotation' : ('tuple', (0, 0, 0)),
    'String'   : ('str', '""'),
}

# constants.__all__
ALL = ['blender_version', 'CLASS_NAMES', 'DATA_TYPE_HOMONYMS', 'SOCKETS', 'NODE_INFO', 'NODE_NAMES', 'SOCKET_SUBTYPES', 
       'GEOMETRY_CLASSES', 'DOMAIN_CLASSES', 'ATTRIBUTE_CLASSES', 'PYTHON_TYPES', 'INPUT_SOCKETS_PROPS',
       'BUILTIN_GROUPS', 'ONE_ITEMS_NODES', 'SEVERAL_ITEMS_NODES', 'SOCKET_IDS']

# ====================================================================================================
# Internal vars
# ====================================================================================================

TREE_TYPES = ('GeometryNodeTree', 'ShaderNodeTree')

TRANSCO = {
    'RGBA'   : 'Color',
    'INT'    : 'Integer',
    'VALUE'  : 'Float',
    'CUSTOM' : 'Input',
    }
    
BLID_TO_STYPE = {
    'NodeSocketBool'        : 'BOOLEAN', 
    'NodeSocketBundle'      : 'BUNDLE', 
    'NodeSocketClosure'     : 'CLOSURE', 
    'NodeSocketCollection'  : 'COLLECTION', 
    'NodeSocketColor'       : 'RGBA', 
    'NodeSocketFloat'       : 'VALUE', 
    'NodeSocketGeometry'    : 'GEOMETRY', 
    'NodeSocketImage'       : 'IMAGE', 
    'NodeSocketInt'         : 'INT', 
    'NodeSocketMaterial'    : 'MATERIAL', 
    'NodeSocketMatrix'      : 'MATRIX', 
    'NodeSocketMenu'        : 'MENU', 
    'NodeSocketObject'      : 'OBJECT', 
    'NodeSocketRotation'    : 'ROTATION', 
    'NodeSocketString'      : 'STRING', 
    'NodeSocketVector'      : 'VECTOR',
    
    'NodeSocketShader'      : 'SHADER',

    'NodSocketVirtual'      : 'CUSTOM',
    }
    
DATA_TYPE_HOMONYMS = {
    'INT8'          : 'INT',
    'INTEGER'       : 'INT',
    'FLOAT2'        : 'VECTOR',
    'FLOAT_VECTOR'  : 'VECTOR',
    'VECTOR_FLOAT'  : 'VECTOR',
    'TRANSFORM'     : 'MATRIX',
    'FLOAT4X4'      : 'MATRIX',
    'BYTE_COLOR'    : 'RGBA',
    'FLOAT_COLOR'   : 'RGBA',
    'COLOR'         : 'RGBA',
    'FLOAT'         : 'VALUE',
    'QUATERNION'    : 'ROTATION', 
}

# ====================================================================================================
# Tedious to manually build : all the input socket props
# subtype entry is automatically completed with update_input_sockets_props
# ====================================================================================================

INPUT_SOCKETS_PROPS = {
    'BOOLEAN': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),

        'default'           : ('default_value',         'bool', False),
        'default_attribute' : ('default_attribute_name','str', ""),

        'layer_selection'   : ('layer_selection_field', 'bool', False),
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'SINGLE'), 'AUTO'),        
        },
    'BUNDLE': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        },
    'CLOSURE': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        },
    'COLLECTION': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'object', None),
        },
    'RGBA': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'tuple', (0., 0., 0., 1.)),
        'default_attribute' : ('default_attribute_name','str', ""),
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE'), 'AUTO'),     
        },
    'VALUE': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'float', 0.),
        'default_attribute' : ('default_attribute_name','str', ""),
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'SINGLE'), 'AUTO'),     
        
        'min'               : ('min_value',             'float', -3.40282e+38),
        'max'               : ('max_value',             'float', 3.40282e+38),
        
        'subtype'           : ('subtype',               'str', 'NONE'),
        },
    'GEOMETRY': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        },
    'IMAGE': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'object', None),
        },
    'INT': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'int', 0),
        'default_attribute' : ('default_attribute_name','str', ""),
        'default_input'     : ('default_input',         ('VALUE', 'INDEX', 'ID_OR_INDEX'), 'VALUE'),
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'SINGLE'), 'AUTO'),     
        
        'min'               : ('min_value',             'int', -2147483648),
        'max'               : ('max_value',             'int', 2147483647),
        
        'subtype'           : ('subtype',               'str', 'NONE'),
        },
    'MATERIAL': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'object', None),
        },
    'MATRIX': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default_attribute' : ('default_attribute_name','str', ""),
        'default_input'     : ('default_input',         ('VALUE', 'INSTANCE_TRANSFORM'), 'VALUE'),
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE'), 'AUTO'),     
        },  
    'MENU': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'str', ""),
        'expanded'          : ('menu_expanded',         'bool', False),
        
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE'), 'AUTO'),     
        },
    'OBJECT': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'object', None),
        },
    'ROTATION': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'tuple', (0., 0., 0.)),
        'default_attribute' : ('default_attribute_name','str', ""),
        
        'shape'             : ('structure_type',        ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE'), 'AUTO'),     
        },
    'STRING': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'default'           : ('default_value',         'str', ""),
        
        'subtype'           : ('subtype',               'str', 'NONE'),
        },
    'VECTOR': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        
        'dimensions'        : ('dimensions',            'int', 3),
        
        'default'           : ('default_value',         'tuple', (0., 0., 0.)),
        'min'               : ('min_value',             'float', -3.40282e+38),
        'max'               : ('max_value',             'float', 3.40282e+38),        
        'default_attribute' : ('default_attribute_name','str', ""),
        'default_input'     : ('default_input',         ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT'), 'VALUE'),
        
        'shape'             : ('structure_type',         ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'SINGLE'), 'AUTO'),     

        'subtype'           : ('subtype',               'str', 'NONE'),
        },

    'SHADER': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        },

    'CUSTOM': {
        'tip'               : ('description',           'str', ""),
        'optional_label'    : ('optional_label',        'bool', False),
        'hide_value'        : ('hide_value',            'bool', False),
        'hide_in_modifier'  : ('hide_in_modifier',      'bool', False),
        },

    }

# ----------------------------------------------------------------------------------------------------
# Node default attributes
# ----------------------------------------------------------------------------------------------------

NODE_DEF_ATTRIBUTES = []


# ====================================================================================================
# Utilities
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Get the enum 
# ----------------------------------------------------------------------------------------------------

def get_enum(obj, attr):
    token = "not found in "
    try:
        setattr(obj, attr, "OUPS")
    except TypeError as e:
        s = str(e)
        p = s.find(token)
        return eval(s[p + len(token):])
    
    return None

# ----------------------------------------------------------------------------------------------------
# Get un working tree
# ----------------------------------------------------------------------------------------------------

def get_tree(tree_type):

    name = f"Temp {tree_type}"
    tree = None

    if tree_type == 'ShaderNodeTree':
        
        material = bpy.data.materials.new(name)
        #material.use_nodes = True
        tree = material.node_tree
    
    elif tree_type == 'GeometryNodeTree':
        
        tree = bpy.data.node_groups.get(name)
        if tree is not None:
            bpy.data.node_groups.remove(tree)
            
        tree = bpy.data.node_groups.new(name=name, type=tree_type)
        
    else:
        assert False, f"Shouldn't happen '{tree_type}'"


    # ----- Initialize NODE_DEF_ATTRIBUTES

    if not len(NODE_DEF_ATTRIBUTES):
        ref_node = tree.nodes.new(type='ShaderNodeValue')
        for name in dir(ref_node):
            NODE_DEF_ATTRIBUTES.append(name)

        NODE_DEF_ATTRIBUTES.append('active_item')
        NODE_DEF_ATTRIBUTES.append('active_index')

    # ----- Done
        
    tree.interface.clear()
    tree.nodes.clear()
    
    return tree

# ----------------------------------------------------------------------------------------------------
# All input sockets
# Used to check INPUT_SOCKETS_PROPS dict
# ----------------------------------------------------------------------------------------------------

def create_all_input_sockets(tree_name):

    tree = get_tree('GeometryNodeTree')
    intf = tree.interface
    intf.clear()

    for tp in dir(bpy.types):
        try:
            intf.new_socket(tp, in_out='INPUT', socket_type=tp)
        except:
            pass

# ----------------------------------------------------------------------------------------------------
# Conversion socket.bl_idname <-> socket.type
# ----------------------------------------------------------------------------------------------------

def to_blid(stype):
    for k, v in BLID_TO_STYPE.items():
        if v == stype:
            return k
    assert False, f"Bad stype: {stype}"

def to_stype(blid):
    return BLID_TO_STYPE[blid]

# ----------------------------------------------------------------------------------------------------
# Get the valid node socket types
# ----------------------------------------------------------------------------------------------------
    
def get_interface_socket_blids(tree):
    
    interface = tree.interface
    serr = "ERROR"
    try:
        item = interface.new_socket("Nope", in_out='INPUT', socket_type=serr)
    except TypeError as e:
        s = str(e)
        p = s.find(serr)
        nodesockets = eval(s[p + 20:])
    
    return nodesockets

# ----------------------------------------------------------------------------------------------------
# Get the interface sockets specific properties
# ----------------------------------------------------------------------------------------------------

def update_input_sockets_props(tree):
    
    nodesockets = get_interface_socket_blids(tree)
    tree.interface.clear()
    
    for blid in nodesockets:
        
        stype = to_stype(blid)
        item = tree.interface.new_socket(stype, in_out='INPUT', socket_type=blid)

        if stype not in INPUT_SOCKETS_PROPS:
            raise RuntimeError(f"The dict INPUT_SOCKET_PROPS doesn't contain entry for node socket {blid} (socket_type: {stype}).")
        
        props = INPUT_SOCKETS_PROPS[stype]

        # Check that the properties exist
        for p in props.values():
            assert p[0] in dir(item), f"Oups: {item.socket_type} {p}"

        # Get the subtypes
        if 'subtype' in props:
            vals = get_enum(item, 'subtype')
            props['subtype'] = ('subtype', vals, props['subtype'][2])

        # Get the subtypes
        if 'shape' in props:
            vals = get_enum(item, 'structure_type')
            props['shape'] = ('structure_type', vals, props['shape'][2])

# ----------------------------------------------------------------------------------------------------
# Print the input and output sockets names for getting the right Geometry class
# ----------------------------------------------------------------------------------------------------

def print_geometry_names():

    tree = get_tree('GeometryNodeTree')
    in_names = set()
    out_names = set()

    for tp in dir(bpy.types):
        try:
            node = tree.nodes.new(type=tp)
        except:
            continue
        
        for sock in node.inputs:
            if sock.type == 'GEOMETRY':
                in_names.add(sock.name)
                
        for sock in node.outputs:
            if sock.type == 'GEOMETRY':
                out_names.add(sock.name)
                
        tree.nodes.remove(node)

    print('-'*100)
    print("Sockets names for Geometry sockets classes\n")
                
    print("Input sockets:", in_names)
    print("OUtput sockets:", out_names)
    print()

# ====================================================================================================
# NODE NAMES
# ====================================================================================================

def get_node_names():

    NODE_NAMES  = {}

    for tree_type in TREE_TYPES:

        tree = get_tree(tree_type)
        
        NODE_NAMES[tree_type] = {}
        for tp in dir(bpy.types):
            try:
                node = tree.nodes.new(type=tp)
            except:
                continue
            
            NODE_NAMES[tree_type][node.name] = node.bl_idname
            
        tree.nodes.clear()
        
    return NODE_NAMES

# ====================================================================================================
# CLASS NAMES
# ====================================================================================================

def get_sockets():
    
    SOCKETS = {}
    
    for tree_type in TREE_TYPES:
        
        tree = get_tree(tree_type)
        
        # ---------------------------------------------------------------------------
        # From sockets in the nodes
        # ---------------------------------------------------------------------------
        
        for tp in dir(bpy.types):
            try:
                node = tree.nodes.new(type=tp)
            except:
                continue
            
            for socket in [sock for sock in node.inputs] + [sock for sock in node.outputs]:
                stype = socket.type
                #if stype == 'CUSTOM':
                #    continue
                
                if stype not in SOCKETS:
                    SOCKETS[stype] = {
                        'class_name': TRANSCO.get(stype, stype.title()),
                    }
                    for tt in TREE_TYPES:
                        SOCKETS[stype][tt] = None
                        
                SOCKETS[stype][tree_type] = socket.bl_idname
                SOCKETS[stype]['nodesocket'] = socket.bl_idname
            
        # ---------------------------------------------------------------------------
        # From interface
        # ---------------------------------------------------------------------------
        
        update_input_sockets_props(tree)
        
        for k in INPUT_SOCKETS_PROPS.keys():
            if k not in SOCKETS.keys():
                print(f"CAUTION> {tree_type}: Socket type {k} in INPUT_SOCKET_PROPS is not in SOCKETS")
        for k in SOCKETS.keys():
            if k not in INPUT_SOCKETS_PROPS.keys():
                print(f"CAUTION> {tree_type}: Socket type {k} in SOCKETS is not in INPUT_SOCKET_PROPS")
                
        for stype, d in SOCKETS.items():
            prop = INPUT_SOCKETS_PROPS.get(stype)
            if prop is None:
                continue
            d['props'] = prop
            d['subtypes'] = prop.get('subtype', (None, (), None))[1]
            d[tree_type] = to_blid(stype)
        
    return SOCKETS

# ====================================================================================================
# Get info on nodes
# ====================================================================================================

def get_node_info(sockets):
    
    NODE_INFO = {}
    for tree_type in TREE_TYPES:
        
        tree = get_tree(tree_type)

        NODE_INFO[tree_type] = {}
        for tp in dir(bpy.types):
            try:
                node = tree.nodes.new(type=tp)
            except:
                continue

            node_info = {
                'name'          : node.name,
                'params'        : {},
                'items'         : [], 
                'menu_sockets'  : {},
                'inputs'        : {}, 
                'outputs'       : {}, 
                'has_custom_in' : False,
                'has_custom_out': False,
            }

            # ----------------------------------------------------------------------------------------------------
            # Input sockets
            # ----------------------------------------------------------------------------------------------------

            for socket in node.inputs:

                # Virtual socket
                if socket.type == 'CUSTOM':
                    node_info['has_custom_in'] = True
                    continue

                # Register the socket
                node_info['inputs'][socket.identifier] = {
                    'name'          : socket.name,
                    'label'         : socket.label,
                    'bl_idname'     : socket.bl_idname,
                    'socket_type'   : socket.type,
                    #'default'       : getattr(socket, 'default_value', None),
                }

                # Menu socket
                if socket.type == 'MENU':

                    enums = None
                    token = "not found in "
                    try:
                        socket.default_value = "NOT A VALUE FOR SURE"
                    except TypeError as e:
                        s = str(e)
                        p = s.find(token)
                        enums = eval(s[p + len(token):])

                    node_info['menu_sockets'][socket.identifier] = {'default': socket.default_value, 'values': enums}

            # ----------------------------------------------------------------------------------------------------
            # Output sockets
            # ----------------------------------------------------------------------------------------------------

            for socket in node.outputs:

                # Virtual socket
                if socket.type == 'CUSTOM':
                    node_info['has_custom_out'] = True
                    continue

                # Register the socket
                node_info['outputs'][socket.identifier] = {
                    'name'          : socket.name,
                    'label'         : socket.label,
                    'bl_idname'     : socket.bl_idname,
                    'socket_type'   : socket.type,
                    #'default'       : str(getattr(socket, 'default_value', None)),
                }

            # ----------------------------------------------------------------------------------------------------
            # Parameters
            # ----------------------------------------------------------------------------------------------------

            for name in dir(node):
                if name in NODE_DEF_ATTRIBUTES:
                    continue

                if name[-6:] == '_items':
                    node_info['items'].append(name)
                    continue

                # Specific ignored
                if name in ['legacy_corner_normals', 'use_legacy_normal']:
                    continue

                # Must be settable
                try:
                    setattr(node, name, getattr(node, name))
                except:
                    continue

                # Param type
                param_type = type(getattr(node, name)).__name__

                # Min info
                node_info['params'][name] = {
                    'default': getattr(node, name) if param_type in ('bool', 'int', 'float', 'str', 'tuple') else None,
                    'type' : param_type,
                    'enum' : None
                }

                # Enums
                if param_type == 'str':
                    node_info['params'][name]['enum'] = get_enum(node, name)            

            # ---------------------------------------------------------------------------
            # data_type parameter
            # ---------------------------------------------------------------------------
            
            if 'data_type' in node_info['params']:

                if tp == 'GeometryNodeStoreNamedAttribute': # Missiong: INT8, FLOAT2, QUATERNION, BYTE_COLOR
                    # ('FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'INT8', 'FLOAT2', 'BYTE_COLOR')
                    convert = {
                        'VALUE'      : 'FLOAT',
                        'INT'        : 'INT',
                        'BOOLEAN'    : 'BOOLEAN',
                        'VECTOR'     : 'FLOAT_VECTOR',
                        'MATRIX'     : 'FLOAT4X4',
                        'RGBA'       : 'FLOAT_COLOR',
                        'ROTATION'   : 'QUATERNION',
                    }
                else:
                    convert = {}
                    for dt in node_info['params']['data_type']['enum']:
                        if dt in sockets.keys():
                            key = dt
                            #convert[dt] = dt
                        elif dt in DATA_TYPE_HOMONYMS:
                            key = DATA_TYPE_HOMONYMS[dt]
                            #convert[DATA_TYPE_HOMONYMS[dt]] = dt
                        else:
                            raise RuntimeError(f"Unknown data type '{dt}' in node [{node.name}]. Enums: {node_info['params']['data_type']['enum']}.")
                        
                        if key in convert:
                            print(f"bl_idname", tp, ", convert\n", node_info['params']['data_type']['enum'])
                            assert False, "Must be done manually"
                        convert[key] = dt

                node_info['data_type'] = convert

            NODE_INFO[tree_type][node.bl_idname] = node_info
        
    return NODE_INFO

# ====================================================================================================
# Socket sub types
# ====================================================================================================

def get_socket_subtypes(nodesockets):
    
    special = {
        'TimeAbsolute'      : 'TIME_ABSOLUTE',
        'ColoreTemperature' : 'COLOR_TEMPERATURE',
        'FilePath'          : 'FILE_PATH',
    }
    
    sns = "NodeSocket"
    
    SOCKET_SUBTYPES = {}
    for tp in dir(bpy.types):

        if not tp.startswith(sns) or tp in [sns, "NodeSocketStandard", "NodeSocketTexture"]: #, "NodeSocketVirtual"]:
            continue

        # ------------------------------------------------------------
        # Virtual socket
        # ------------------------------------------------------------

        if tp == 'NodeSocketVirtual':
            SOCKET_SUBTYPES[tp] = {
                'nodesocket' : tp,
                'subtype'    : None,
                'dimensions' : None,
                'socket_type': None,
                }
            continue
        
        # ------------------------------------------------------------
        # Non virtual
        # ------------------------------------------------------------
        
        base = None
        for nodesocket in nodesockets:
            if tp.startswith(nodesocket):
                base = nodesocket
                break
            
        if base is None:
            raise RuntimeError(f"Impossible to get the base socket of f{tp}")
            
        if tp == base:
            subtype = None
            ndims   = None
            
        else:            
            subtype = tp[len(base):]
            ndims = None
            if subtype[-1] == 'D':
                ndims   = int(subtype[-2])
                subtype = subtype[:-2]
                
            subtype = special.get(subtype, subtype.upper())

        socket_type = base[len('NodeSocket'):].upper()
        socket_type = {
            'BOOL': 'BOOLEAN',
            'COLOR': 'RGBA',
            'FLOAT': 'VALUE',
        }.get(socket_type, socket_type)
                
        SOCKET_SUBTYPES[tp] = {
            'nodesocket' : base,
            'subtype'    : subtype,
            'dimensions' : ndims,
            'socket_type': socket_type,
            }
        
    return SOCKET_SUBTYPES
        


# ====================================================================================================
# Builtin groups
# ====================================================================================================

def get_builtin_groups():

    BLEND_FILES = {
        'GeometryNodeTree' : ["geometry_nodes_essentials.blend", "procedural_hair_node_assets.blend"],
        'ShaderNodeTree' : ["shading_nodes_essentials.blend"],
    }

    root = Path(bpy.utils.system_resource('DATAFILES')) / "assets/nodes"
    assert root.is_dir(), f"DATAFILES {str(root)} doesn't exist."

    BUILTIN_GROUPS = {}
    for tree_type, blend_files in BLEND_FILES.items():
        groups = {}
        for file_name in blend_files:
            with bpy.data.libraries.load(str(root / file_name)) as (data_from, data_to):
                for ng in list(data_from.node_groups):
                    groups[ng] = file_name

        BUILTIN_GROUPS[tree_type] = groups

    return BUILTIN_GROUPS


# ====================================================================================================
# Global vars
# ====================================================================================================


SOCKETS = get_sockets()
NODE_NAMES = get_node_names()
NODE_INFO = get_node_info(SOCKETS)

# List of base nodesockets
NODESOCKETS = []
for socket in SOCKETS.values():
    nodesocket = socket['GeometryNodeTree']
    if nodesocket is None:
        nodesocket = socket['ShaderNodeTree']
    NODESOCKETS.append(nodesocket)

SOCKET_SUBTYPES = get_socket_subtypes(NODESOCKETS)
BUILTIN_GROUPS = get_builtin_groups()

# ----------------------------------------------------------------------------------------------------
# Derived lists
# ----------------------------------------------------------------------------------------------------

ONE_ITEMS_NODES = {}
SEVERAL_ITEMS_NODES = {}

for tt in TREE_TYPES:
    for blid, info in NODE_INFO[tt].items():
        # Ignore paired nodes
        if blid in ['GeometryNodeRepeatOutput', 'GeometryNodeSimulationOutput']:
            continue

        if len(info['items']) == 1:
            ONE_ITEMS_NODES[blid] = info['items'][0]

        if len(info['items']) > 1:
            SEVERAL_ITEMS_NODES[blid] = info['items']


CLASS_NAMES = {}
for stype, d in SOCKETS.items():
    CLASS_NAMES[stype] = d['class_name']

# ----------------------------------------------------------------------------------------------------
# Socket Types (derived from global)
# ----------------------------------------------------------------------------------------------------

def get_socket_ids():

    SOCKET_IDS = {}

    # ---------------------------------------------------------------------------
    # Full socket ids
    # ---------------------------------------------------------------------------

    for full_socket_id, full_spec in SOCKET_SUBTYPES.items():
        SOCKET_IDS[full_socket_id] = full_socket_id

    # ---------------------------------------------------------------------------
    # Socket types
    # ---------------------------------------------------------------------------

    for stype, spec in SOCKETS.items():
        SOCKET_IDS[stype] = spec['nodesocket']

    # ---------------------------------------------------------------------------
    # Class Names
    # ---------------------------------------------------------------------------

    for sid, class_name in CLASS_NAMES.items():
        SOCKET_IDS[class_name] = SOCKET_IDS[sid]

    for class_name in GEOMETRY_CLASSES:
        SOCKET_IDS[class_name] = 'NodeSocketGeometry'

    for class_name in DOMAIN_CLASSES:
        SOCKET_IDS[class_name] = 'NodeSocketGeometry'

    # ---------------------------------------------------------------------------
    # Complementary
    # ---------------------------------------------------------------------------

    for homo, stype in DATA_TYPE_HOMONYMS.items():
        SOCKET_IDS[homo] = SOCKET_IDS[stype]    

    #SOCKET_IDS['CUSTOM'] = 'NodeSocketVirtual'
    #SOCKET_IDS['NodeSocketVirtual'] = 'NodeSocketVirtual'

    return SOCKET_IDS

SOCKET_IDS = get_socket_ids()

# ====================================================================================================
# Write the config file
# ====================================================================================================

def write_header(f, title):
    f.write('#' + '-'*80 + "\n")
    f.write("# " + title + "\n")
    f.write('#' + '-'*80 + "\n\n")
    
def write_file(path):

    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur_ver = bpy.app.version_string.replace('.', '_').replace(" ", "_")
    fname = f"config_{cur_ver}.py"

    print(f"Writing config file {fname} @ {time_stamp} (path: {str(path)})")

    with open(path / fname, 'w') as f:
        
        f.write(f"# GeoNodes configuration\n")
        f.write(f"# Blender {bpy.app.version}\n")
        f.write(f"# Generated {time_stamp}\n\n")
        f.write("\n")
        f.write(f"blender_version = {bpy.app.version}\n\n")
        
        f.write(f"__all__ = {ALL}\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Hard stuff
        # ----------------------------------------------------------------------------------------------------

        write_header(f, f"Classes lists")
        f.write(f"GEOMETRY_CLASSES = {GEOMETRY_CLASSES}\n")
        f.write(f"DOMAIN_CLASSES = {DOMAIN_CLASSES}\n")
        f.write(f"ATTRIBUTE_CLASSES = {ATTRIBUTE_CLASSES}\n")

        f.write("\n")
        f.write(f"PYTHON_TYPES = ")
        pprint(PYTHON_TYPES, stream=f)
        f.write("\n")

        # ----------------------------------------------------------------------------------------------------
        # Class names
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Socket type to class name")
        f.write("CLASS_NAMES = ")
        pprint(CLASS_NAMES, stream=f)
        f.write("\n\n")

        f.write("DATA_TYPE_HOMONYMS = ")
        pprint(DATA_TYPE_HOMONYMS, stream=f)
        f.write("\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Socket ids
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Sockets ids for SocketType class")
        f.write("SOCKET_IDS = ")
        pprint(SOCKET_IDS, stream=f)
        f.write("\n\n")
        
        # ----------------------------------------------------------------------------------------------------
        # Sockets
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Sockets details")
        f.write("SOCKETS = ")
        pprint(SOCKETS, stream=f)
        f.write("\n\n")
        
        # ----------------------------------------------------------------------------------------------------
        # Socket sub types
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Get base socket bl_idname and subtype from full node socket")
        f.write("SOCKET_SUBTYPES = ")
        pprint(SOCKET_SUBTYPES, stream=f)
        f.write("\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Builtin groups
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Builtin groups")
        f.write("BUILTIN_GROUPS = ")
        pprint(BUILTIN_GROUPS, stream=f)
        f.write("\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Nodes with items
        # ----------------------------------------------------------------------------------------------------

        write_header(f, "Nodes with items")
        f.write("ONE_ITEMS_NODES = ")
        pprint(ONE_ITEMS_NODES, stream=f)
        f.write("\n\n")

        f.write("SEVERAL_ITEMS_NODES = ")
        pprint(SEVERAL_ITEMS_NODES, stream=f)
        f.write("\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Input sockets properties
        # ----------------------------------------------------------------------------------------------------

        write_header(f, "Input sockets properties")
        f.write("INPUT_SOCKETS_PROPS = ")
        pprint(INPUT_SOCKETS_PROPS, stream=f)
        f.write("\n\n")
        
        # ----------------------------------------------------------------------------------------------------
        # Node names
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Node names to bl_idname")

        for tree_type, nodes in NODE_NAMES.items():
            f.write(f"# {tree_type:16s} : {len(nodes)} nodes\n")
        f.write("\n")
        
        f.write("NODE_NAMES = {\n")
        for tree_type, nodes in NODE_NAMES.items():
            
            f.write(f"    '{tree_type}' : "+ "{\n")
        
            for name, blid in nodes.items():
                sname = f"'{name}'"
                f.write(f"        {sname:30s} : '{blid}',\n")
                
            f.write("    },\n\n")
            
        f.write("}\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Info on nodes
        # ----------------------------------------------------------------------------------------------------
        
        f.write("NODE_INFO = ")
        pprint(NODE_INFO, stream=f)
        f.write("\n\n")
        


def test():
    path = Path("/Users/alain/Documents/blender/scripts/modules/geonodes/core")
    write_file(path)


