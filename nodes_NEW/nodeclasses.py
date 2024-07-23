#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : tree
------------------
- Tree root class

Methods which are independant of the tree type

created : 2024/07/21
"""

# ====================================================================================================
# Nodes

NODES = {
    # ----------------------------------------------------------------------------------------------------
    # Input nodes

    'Boolean' : {
        'blid': 'FunctionNodeInputBool',
        'prms': {'boolean': bool},
        'inss': {},
        'outs': {'boolean': 'Boolean'},
        },

    'Color' : {
        'blid': 'FunctionNodeInputColor',
        'prms': {'value': 'COLOR'},
        'inss': {},
        'outs': {'color': 'Color'},
        },

    'Image' : {
        'blid': 'GeometryNodeInputImage',
        'prms': {'image': 'IMAGE'},
        'inss': {},
        'outs': {'image': 'Image'},
        },

    'Integer' : {
        'blid': 'FunctionNodeInputInt',
        'prms': {'integer': int},
        'inss': {},
        'outs': {'integer': 'Integer'},
        },

    'Material' : {
        'blid': 'GeometryNodeInputMaterial',
        'prms': {'material': 'MATERIAL'},
        'inss': {},
        'outs': {'material': 'Material'},
        },

    'Rotation' : {
        'blid': 'FunctionNodeInputRotation',
        'prms': {'rotation_euler': 'Rotation'},
        'inss': {},
        'outs': {'rotation': 'Rotation'},
        },

    'String' : {
        'blid': 'FunctionNodeInputString',
        'prms': {'string': str},
        'inss': {},
        'outs': {'string': 'String'},
        },

    'Value' : {
        'blid': 'ShaderNodeValue',
        'prms': {},
        'inss': {},
        'outs': {'value': 'Value'},
        },

    'Vector' : {
        'blid': 'FunctionNodeInputVector',
        'prms': {'vector': 'Vector'},
        'inss': {},
        'outs': {'vector': 'Vector'},
        },

    'ActiveCamera' : {
        'blid': 'GeometryNodeInputActiveCamera',
        'prms': {},
        'inss': {},
        'outs': {'active_camera': 0},
        },

    'ImageInfo' : {
        'blid': 'GeometryNodeImageInfo',
        'prms': {},
        'inss': {'image': 0, 'frame': 1},
        'outs': {'width': 0, 'height': 1, 'has_alpha': 2, 'frame_count': 3, 'FPS': 4, 'fps': 4},
        },

    'CollectionInfo' : {
        'blid': 'GeometryNodeCollectionInfo',
        'prms': {'transform_space': ('ORIGINAL', 'RELATIVE')},
        'inss': {'collection': 0, 'separate_children': 1, 'reset_children': 2},
        'outs': {'instances': 0},
        },

    'ObjectInfo' : {
        'blid': 'GeometryNodeObjectInfo',
        'prms': {'transform_space': ('ORIGINAL', 'RELATIVE')},
        'inss': {'object': 0, 'as_instance': 1},
        'outs': {'transform': 0, 'location': 1, 'rotation': 2, 'scale': 3, 'geometry': 4},
        },

    'IsViewport' : {
        'blid': 'GeometryNodeIsViewport',
        'prms': {},
        'inss': {},
        'outs': {'is_viewport': 0},
        },

    'SceneTime' : {
        'blid': 'GeometryNodeInputSceneTime',
        'prms': {},
        'inss': {},
        'outs': {'seconds': 0, 'frame': 1},
        },

    'SelfObject' : {
        'blid': 'GeometryNodeSelfObject',
        'prms': {},
        'inss': {},
        'outs': {'self_object': 0},
        },

    # ----------------------------------------------------------------------------------------------------
    # Geometry read

    'ID' : {
        'blid' : 'GeometryNodeInputID',
        'prms' : {},
        'inss' : {},
        'outs' : {'ID' : 0},
    },
    'Index' : {
        'blid' : 'GeometryNodeInputIndex',
        'prms' : {},
        'inss' : {},
        'outs' : {'index' : 0},
    },
    'NamedAttribute' : {
        'blid' : 'GeometryNodeInputNamedAttribute',
        'prms' : {'data_type' : ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')},
        'inss' : {'name' : 0},
        'outs' : {'attribute' : 0, 'exists' : 1},
    },
    'Normal' : {
        'blid' : 'GeometryNodeInputNormal',
        'prms' : {},
        'inss' : {},
        'outs' : {'normal' : 0},
    },
    'Position' : {
        'blid' : 'GeometryNodeInputPosition',
        'prms' : {},
        'inss' : {},
        'outs' : {'position' : 0},
    },
    'Radius' : {
        'blid' : 'GeometryNodeInputRadius',
        'prms' : {},
        'inss' : {},
        'outs' : {'radius' : 0},
    },

    # ----------------------------------------------------------------------------------------------------
    # Sample

    'GeometryProximity' : {
        'blid' : 'GeometryNodeProximity',
        'prms' : {'target_element': ('POINTS', 'EDGES', 'FACES')},
        'inss' : {'geometry' : 0, 'group_id' : 1, 'sample_position' : 2, 'sample_group_id' : 3},
        'outs' : {'position' : 0, 'distance' : 1, 'is_valid' : 2},
    },
    'IndexOfNearest' : {
        'blid' : 'GeometryNodeIndexOfNearest',
        'prms' : {},
        'inss' : {'position' : 0, 'group_id' : 1},
        'outs' : {'index' : 0, 'has_neighbor' : 1},
    },
    'Raycast' : {
        'blid' : 'GeometryNodeRaycast',
        'prms' : {
            'data_type' : ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'),
            'mapping'   : ('INTERPOLATED', 'NEAREST')},
        'inss' : {'target_geometry' : 0, 'attribute' : 1, 'source_position' : 2, 'ray_direction' : 3, 'ray_length' : 4},
        'outs' : {'is_hit' : 0, 'hit_position' : 1, 'hit_normal' : 2, 'hit_distance' : 3, 'attribute' : 4},
    },
    'SampleIndex' : {
        'blid' : 'GeometryNodeSampleIndex',
        'prms' : {
            'data_type' : ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'),
            'domain'    : ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE'),
            'clamp'     : None,
            },
        'inss' : {'geometry' : 0, 'value' : 1, 'index' : 2},
        'outs' : {'value' : 0},
    },
    'SampleNearest' : {
        'blid' : 'GeometryNodeSampleNearest',
        'prms' : {'domain' : ('POINT', 'EDGE', 'FACE', 'CORNER')},
        'inss' : {'geometry' : 0, 'sample_position' : 1},
        'outs' : {'index' : 0},
    },

    # ----------------------------------------------------------------------------------------------------
    # Math Node

    'Math': {
        'blid': 'ShaderNodeMath',
        'prms': {
            'operation' : {
                'ADD'               : {'args' : ['value', 'value_1']},
                'SUBTRACT'          : {'args' : ['value', 'value_1']},
                'MULTIPLY'          : {'args' : ['value', 'value_1']},
                'DIVIDE'            : {'args' : ['value', 'value_1']},
                'MULTIPLY_ADD'      : {'args' : ['value', 'multiplier', 'addend']},
                'POWER'             : {'args' : ['base', 'exponent']},
                'LOGARITHM'         : {'args' : ['value'], 'short': 'log'},
                'SQRT'              : {'args' : ['value']},
                'INVERSE_SQRT'      : {'args' : ['value']},
                'ABSOLUTE'          : {'args' : ['value'], 'short': 'abs'},
                'EXPONENT'          : {'args' : ['value'], 'short': 'exp'},
                'MINIMUM'           : {'args' : ['value', 'value_1'], 'short': 'min'},
                'MAXIMUM'           : {'args' : ['value', 'value_1'], 'short': 'max'},
                'LESS_THAN'         : {'args' : ['value', 'value_1', 'threshold']},
                'GREATER_THAN'      : {'args' : ['value', 'value_1', 'threshold']},
                'SIGN'              : {'args' : ['value']},
                'COMPARE'           : {'args' : ['value', 'value_1', 'epsilon']},
                'SMOOTH_MIN'        : {'args' : ['value', 'value_1', 'distance']},
                'SMOOTH_MAX'        : {'args' : ['value', 'value_1', 'distance']},
                'ROUND'             : {'args' : ['value']},
                'FLOOR'             : {'args' : ['value']},
                'CEIL'              : {'args' : ['value']},
                'TRUNC'             : {'args' : ['value']},
                'FRACT'             : {'args' : ['value']},
                'MODULO'            : {'args' : ['value', 'value_1']},
                'FLOORED_MODULO'    : {'args' : ['value', 'value_1']},
                'WRAP'              : {'args' : ['value', 'max', 'min']},
                'SNAP'              : {'args' : ['value', 'increment']},
                'PINGPONG'          : {'args' : ['value', 'scale']},
                'SINE'              : {'args' : ['value'], 'short': 'sin'},
                'COSINE'            : {'args' : ['value'], 'short': 'cos'},
                'TANGENT'           : {'args' : ['value'], 'short': 'tan'},
                'ARCSINE'           : {'args' : ['value'], 'short': 'asin'},
                'ARCCOSINE'         : {'args' : ['value'], 'short': 'acos'},
                'ARCTANGENT'        : {'args' : ['value'], 'short': 'atan'},
                'ARCTAN2'           : {'args' : ['value', 'value_1'], 'short': 'atan2'},
                'SINH'              : {'args' : ['value']},
                'COSH'              : {'args' : ['value']},
                'TANH'              : {'args' : ['value']},
                'RADIANS'           : {'args' : ['value']},
                'DEGREES'           : {'args' : ['value']},
                },
            'use_clamp': bool,
        },
        'inss': {
            'value'      : 'Value',
            'value_1'    : 'Value_001',
            'multiplier' : 'Value_001',
            'max'        : 'Value_001',
            'base'       : 'Value',
            'epsilon'    : 'Value_002',
            'addend'     : 'Value_002',
            'distance'   : 'Value_002',
            'exponent'   : 'Value_002',
            'threshold'  : 'Value_002',
            'min'        : 'Value_002',
            'scale'      : 'Value_002',
        },
        'outs': {'value': 'Value'},
    }
}



# ====================================================================================================
# Source code generator

# ----------------------------------------------------------------------------------------------------
# Generate comments

def gen_comment(title, node_name, arguments={}, returns=None, tab="\t\t"):

    yield f"{tab}\"\"\" {title}\n"

    yield f"{tab}Node '{node_name}' ({NODES[node_name]['blid']})\n"
    if len(arguments):
        yield f"{tab}Arguments"
        yield f"{tab}---------"
        for k, v in arguments.items():
            yield f"{tab}- {k} : {v}"
        yield ""

    yield f"{tab}Returns"
    yield f"{tab}-------"
    if returns is None:
        yield f"{tab}Node"
    else:
        yield f"{tab}{returns}"

    yield f"{tab}\"\"\"\n"

# ----------------------------------------------------------------------------------------------------
# Global math operations

def gen_math(as_method=True):

    print("="*100)
    print()

    imports = []

    tab_def = "    " if as_method else ""
    tab = tab_def + "    "
    sself = "self, " if as_method else ""

    for operation, args in NODES['Math']['prms']['operation'].items():
        sheader = ", ".join([f"{name}=None" for name in args['args']])
        snode   = ", ".join([f"{name}={name}" for name in args['args']])
        opname = args.get('short')
        if opname is None:
            opname = operation.lower()
        imports.append(opname)

        print(f"{tab_def}def {opname}({sself}{sheader}, use_clamp=None):")
        for line in gen_comment(f"Math operation {operation}", 'Math', arguments={name: name for name in args['args']}, returns='value', tab=tab):
            print(line)

        print(f"{tab}return Node('Math', {snode}, use_clamp=use_clamp, operation='{operation}').value")
        print()

    #print()
    #print(f"from geonodes.nodes.globalfunctions import {', '.join(imports)}")
