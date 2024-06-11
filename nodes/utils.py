#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:14:33 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : utils
--------------
- low level utilities

update : 2024/02/17
update : 2024/03/29
"""

from pprint import pprint

import numpy as np

import bpy
import mathutils

from geonodes.nodes import constants


# ====================================================================================================
# Get the params of a node

def get_node_params(bnode):
    return [name for name in dir(bnode) if name not in STANDARD_NODE_ATTRS]

# ====================================================================================================
# Print stack

def print_stack(count=3):

    import traceback

    EXCL = 3

    tb = traceback.extract_stack()
    for i, t in enumerate(tb):
        if i > len(tb) - EXCL:
            continue
        print(f"{i:2d} ", t.filename)
        print(f"   {t.lineno:4d}:", t.line)

    return




# ====================================================================================================
# Add a rank to a list of arguments to get list of unique keys

def add_rank_OLD(args):
    counts = {}
    keys = []
    for arg in args:
        if arg in counts:
            counts[arg] += 1
            keys.append(f"{arg}_{counts[arg]}")
        else:
            counts[arg] = 0
            keys.append(arg)
    return keys

# ====================================================================================================
# Transform user name in python name

def clean(s, rep=' '):
    for c in ['/', ':', '-', '.',' ']:
        s = s.replace(c, rep)
    return s

def prefix_figure(name):
    if name[0].isnumeric():
        return "_" + name
    else:
        return name

def node_class_name(name):

    assert(name != "")

    #if name == 'ID':
    #    return 'Id'

    if name == 'ColorRamp':
        return 'ColorRamp'

    else:
        words = clean(name, ' ').split(' ')
        for i in range(len(words)):
            if words[i].upper() != words[i]:
                words[i] = words[i].title()
        return prefix_figure(''.join(words))

def node_method(name):

    assert(name != "")

    #if name == 'ID':
    #    return 'ID'

    if name == 'ColorRamp':
        return 'color_ramp'

    else:
        return prefix_figure(clean(name, '_').lower())

def socket_name(name):

    assert(name != "")

    if name == 'ID':
        return 'ID'
    else:
        return prefix_figure(clean(name, '_').lower())

def operation_name(name):

    rename = {
        'cosine'        : 'cos',
        'sine'          : 'sin',
        'tangent'       : 'tan',
        'cross_product' : 'cross',
        'dot_product'   : 'dot',
        'modulo'        : 'mod',
        'arcsine'       : 'arcsin',
        'arccosine'     : 'arccos',
        'arctangent'    : 'arctan',
        'logarithm'     : 'log',
        'exponent'      : 'exp',
        'minimum'       : 'min',
        'maximum'       : 'max',
        'absolute'      : 'abs',
        'fraction'      : 'frac',
        'and'           : 'band',
        'or'            : 'bor',
        'not'           : 'bnot',
        'color'         : 'blend_color',
        'value'         : 'blend_value',
        }

    assert(name != "")

    s = name.lower().replace(' ', '_').replace('-', '_')
    return rename.get(s, s)

def data_type_name(name, all_names=None):

    # 'QUATERNION', 'ROTATION', 'VECTOR', 'INT', 'FLOAT_COLOR', 'STRING', 'RGBA',
    # 'FLOAT_VECTOR', 'BYTE_COLOR', 'FLOAT2', 'BOOLEAN', 'FLOAT'

    VECTORS = ['VECTOR', 'FLOAT_VECTOR']
    COLORS  = ['RGBA', 'FLOAT_COLOR', 'BYTE_COLOR']

    if all_names is None:
        return name.lower()

    if name in VECTORS:
        if VECTORS[0] in all_names and VECTORS[1] in all_names:
            return name.lower()
        else:
            return 'vector'

    elif name in COLORS:
        count = 0
        if COLORS[0] in all_names: count += 1
        if COLORS[1] in all_names: count += 1
        if COLORS[2] in all_names: count += 1

        if count > 1:
            return name.lower()
        else:
            return 'color'

    return name.lower()


# ====================================================================================================
# Valid value

def value_for(value, socket_type):
    """ Convert a value to a valid value for the socket type

    The value must be a python value : int, bool, tuple, Vector

    Arguments
    ---------
        - value (any) : the value to convert
        - socket_type (str) : a valid NodeSocket bl_idname

    Returns
    -------
        - a value which can be plugged into the socket of the given type
    """

    if value is None:
        return None

    if hasattr(value, 'bnode'):

        print_stack()

        outs = value.output_socket
        print(f"Caution {value} variable is used rather than one of its sockets. Used socket: {outs}.")
        return outs

    if socket_type in ['NodeSocketBool']:
        return bool(value)

    elif socket_type in ['NodeSocketInt', 'NodeSocketIntUnsigned', 'NodeSocketIntFactor', 'NodeSocketIntPercentage']:
        return int(value)

    elif socket_type in ['NodeSocketFloat', 'NodeSocketFloatFactor', 'NodeSocketFloatAngle', 'NodeSocketFloatDistance',
                         'NodeSocketFloatPercentage', 'NodeSocketFloatTime', 'NodeSocketFloatTimeAbsolute', 'NodeSocketFloatUnsigned']:

        try:
            return float(value)
        except:
            pass

        raise Exception(f"Impossible to convert the value {value} for the socket {socket_type}")

    elif socket_type in ['NodeSocketVector', 'NodeSocketVectorEuler', 'NodeSocketVectorXYZ', 'NodeSocketVectorTranslation', 'NodeSocketVectorAcceleration',
                         'NodeSocketVectorDirection', 'NodeSocketVectorVelocity', 'NodeSocketRotation']:
        if isinstance(value, mathutils.Vector):
            return value

        elif np.shape(value) == ():
            v = (value, value, value)
            #return Vector((value, value, value))

        else:
            v = value
            #return Vector(value)

        try:
            return mathutils.Vector(v)
        except:
            pass

        return constants.current_tree().CombineXYZ(v[0], v[1], v[2]).output_socket

    elif socket_type in ['NodeSocketColor']:

        if isinstance(value, mathutils.Color):
            return (value.r, value.g, value.b, 1.)

        elif np.shape(value) == ():
            v = (value, value, value, 1.)

        elif len(value) == 3:
            v = tuple(value) + (1.,)

        else:
            v = value

        try:
            return mathutils.Color(v)
        except:
            pass

        return constants.current_tree().CombineColor(v[0], v[1], v[2], v[3]).output_socket


    elif socket_type in ['NodeSocketString']:
        return str(value)

    elif socket_type in ['NodeSocketGeometry']:
        return value

    elif socket_type in ['NodeSocketCollection']:
        if isinstance(value, str):
            return bpy.data.collections[value]
        else:
            return value

    elif socket_type in ['NodeSocketImage']:
        if isinstance(value, str):
            return bpy.data.images[value]
        else:
            return value

    elif socket_type in ['NodeSocketMaterial']:
        if isinstance(value, str):
            return bpy.data.materials[value]
        else:
            return value

    elif socket_type in ['NodeSocketObject']:
        if isinstance(value, str):
            return bpy.data.objects[value]
        else:
            return value

    elif socket_type in ['NodeSocketTexture']:
        if isinstance(value, str):
            return bpy.data.objects[value]
        else:
            return value

    else:
        raise Exception(f"Unknown socket type: {socket_type}")

# ====================================================================================================
# interface socket class
#
# Get the main class of a sub class

def nodesocket_main_class(bl_idname):

    if bl_idname in ['NodeSocketInt', 'NodeSocketIntUnsigned', 'NodeSocketIntFactor', 'NodeSocketIntPercentage']:
        return 'NodeSocketInt'

    elif bl_idname in ['NodeSocketFloat', 'NodeSocketFloatFactor', 'NodeSocketFloatAngle', 'NodeSocketFloatDistance',
                         'NodeSocketFloatPercentage', 'NodeSocketFloatTime', 'NodeSocketFloatTimeAbsolute', 'NodeSocketFloatUnsigned']:
        return 'NodeSocketFloat'

    elif bl_idname in ['NodeSocketVector', 'NodeSocketVectorEuler', 'NodeSocketVectorXYZ', 'NodeSocketVectorTranslation', 'NodeSocketVectorAcceleration',
                         'NodeSocketVectorDirection', 'NodeSocketVectorVelocity']:
        return 'NodeSocketVector'
    else:
        return bl_idname

# ====================================================================================================
# Get the tree node type from a python value
# This allows to manage constants as an output Socket
# The value is used to initialized an input socket rather that linking an actual output socket

def get_value_socket_type(value):

    if value is None:
        return 'GEOMETRY'

    if hasattr(value, 'bsocket'):
        return type(value).__name__

    if isinstance(value, (float, np.float_, np.float64, np.float32)):
        return 'VALUE'
    elif isinstance(value, (bool, np.bool_)):
        return 'BOOLEAN'
    elif isinstance(value, (int, np.int_, np.int32, np.int64, np.int8)):
        return 'INT'
    elif isinstance(value, str):
        return 'STRING'

    elif hasattr(value, '__len__'):
        if len(value) == 3:
            return 'VECTOR'
        else:
            return 'RGBA'

    elif isinstance(value, bpy.types.Object):
        return 'OBJECT'
    elif isinstance(value, bpy.types.Collection):
        return 'COLLECTION'
    elif isinstance(value, bpy.types.Texture):
        return 'TEXTURE'
    elif isinstance(value, bpy.types.Image):
        return 'IMAGE'
    elif isinstance(value, bpy.types.Material):
        return 'MATERIAL'

    elif hasattr(value, 'bnode'):

        print_stack()

        stype = value.output_socket.bsocket.type
        print(f"Caution {value} variable is used rather than one of its sockets in {list(value.outputs.sockets_pynames().keys())}. '{stype}' returned.")
        return stype

    elif hasattr(value, 'bsocket'):
        return value.bsocket.type

    else:
        raise Exception(f"Python value '{value}' of type {type(value).__name__} doesn't match any socket type in {constants.all_socket_classes(constants.get_tree_type())}")

def get_type_from_sockets(value):
    if isinstance(value, list):
        stypes = {}
        imax   = 0
        res    = 'GEOMETRY'
        for v in value:
            stype = get_value_socket_type(v)
            if stype in stypes:
                stypes[stype] += 1
            else:
                stypes[stype] = 1
            if imax < stypes[stype]:
                imax = stypes[stype]
                res  = stype
        return res
    else:
        return get_value_socket_type(value)

# ====================================================================================================
# Socket bl_idname from a value

def socket_bl_idname_from_value(value):
    if isinstance(value, bpy.types.NodeSocket):
        return nodesocket_main_class(value.bl_idname)
    elif hasattr(value, 'bnode'):
        return nodesocket_main_class(value.bnode.bl_idname)
    else:
        bl_id = constants.BLENDER_SOCKET_CLASSES.get(get_value_socket_type(value))
        if bl_id is None:
            raise AttributeError(f"Impossible to find a socket type for the value {value}")
        return bl_id


# ====================================================================================================
# Convert a list of socket names into header arguments

def decrease_arg_rank(args, key):

    def decrease(arg):

        if arg == key:
            return 'self'

        if arg[:len(key)] != key:
            return arg

        if arg[-2] == '_' and arg[-1].isnumeric():
            rank = int(arg[-1])
            if rank == 1:
                return arg[:-2]
            else:
                return f"{arg[:-1]}{rank-1}"
        else:
            return arg

    return {arg: decrease(arg) for arg in args}

def list_to_args(args, self_key=None):

    if self_key is None:
        args_ = []
    else:
        args_ = ['self']

    args_ += [f"{arg}=None" for arg in decrease_arg_rank(args, self_key).values() if arg != 'self']

    return ", ".join(args_)

def list_to_call_header(args, self_key=None):

    args_ = [f"{arg_name}={arg_val}" for arg_name, arg_val in decrease_arg_rank(args, self_key).items()]
    return ", ".join(args_)

# ====================================================================================================
# Source code initialization string

def python_constant(value, keep_lower=True):

    if isinstance(value, str):
        # TOKEN
        if value.upper() == value or (not keep_lower):
            return f"'{value}'"
        # Source code
        else:
            return value

    elif isinstance(value, mathutils.Vector):
        return f"({value.x}, {value.y}, {value.z})"

    else:
        s = str(value)
        if s[0] == '<':
            return 'None'
        else:
            return s

# ====================================================================================================
# Compile function

def compile_f(code, function_name='f', names=None):
    if False:
        print("COMPILE_F")
        print('='*50)
        print(code)
        print('='*50)

    exec(code, names, locals())

    return locals()[function_name]

def getter(code, name='f'):
    return f"def {name}(self):\n\t{code}\n"

def setter(code, name='f'):
    return f"def {name}(self, value):\n\t{code}\n"

# ====================================================================================================
# Get the enum list of a node

def get_enum_list(bnode, param_name):

    value = getattr(bnode, param_name)
    if not isinstance(value, str):
        return None

    try:
        setattr(bnode, param_name, 'ERROR')
    except TypeError as e:
        msg = str(e)
        i = msg.find('enum "ERROR" not found in')
        if i <= 0:
            return None

        vals = eval(msg[i+26:])

        # Only one possible value : ('VALUE') is evaluated as a str, not a singleton of a str
        if isinstance(vals, str):
            vals = (vals,)
        return vals


    return None

# ====================================================================================================
# Input socket order
# put the selection socket in last position

def input_sockets_order(sockets):
    if 'selection' in sockets:
        return [key for key in sockets if key != 'selection'] + ['selection']
    elif isinstance(sockets, dict):
        return list(sockets.keys())
    else:
        return sockets
