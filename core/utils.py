"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : utils
--------------
- a set a utility functions

This module regroups all the global functions

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

import unicodedata
import numpy as np

from pprint import pprint
import bpy

from .scripterror import NodeError
from . import constants

BUILD = False

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
        print(f"CAUTION node '{node_name}': argument '{arg_name}' type ('{socket_type}') is not in {list(type_to_value.keys())}.")

    return list(type_to_value.values())[0]

# =============================================================================================================================
# Conversion of enum parameters
# e.g. : COSINE <-> cos
#
# These functions use SPEC_ENUM_PARAMS and ENUM_PARAMS dicts in constants

# -----------------------------------------------------------------------------------------------------------------------------
# Get enum param value from user value

def get_enum_param_value(user_value, node_name, param_name):
    """ Get the param value from a user value

    Arguments
    ---------
    - user_value (str) : user value for the param, e.g. 'cos'
    - node_name (str) : node name

    Returns
    -------
    - str or None : The parameter value, e.g. 'COSINE'
    """

    return user_value

    # =============================================================================================================================
    # IN PROGRESS
    # =============================================================================================================================


    if BUILD or param_name in ['domain', 'data_type', 'input_type']:
        return user_value


    user_value = snake_case(user_value)

    # ----------------------------------------------------------------------------------------------------
    # Very specific cases

    # Node 'Subdivision Surface':
    # - param uv_smooth: All <-> SMOOTH_ALL
    # - param boundary_smooth: All <-> ALL
    if node_name == 'Subdivision Surface':
        if user_value == 'all':
            if param_name == 'uv_smooth':
                return 'SMOOTH_ALL'
            elif param_name == 'boundary_smooth':
                return 'ALL'
            else:
                return None

    # Node 'Point Density':
    # - param point_source: ('PARTICLE_SYSTEM', 'OBJECT')
    # - param space: ('OBJECT', 'WORLD')
    if node_name == 'Point Density':
        if user_value in ['Object Vertices', 'Object Space']:
            return 'OBJECT'

    # ----------------------------------------------------------------------------------------------------
    # Nodes specific

    for node, specs in constants.SPEC_ENUM_PARAMS.items():
        if isinstance(node, tuple):
            if node_name not in node:
                continue
        else:
            if node != node_name:
                continue

        for k, v in specs.items():
            if snake_case(k) == user_value:
                return v


    for k, v in constants.ENUM_PARAMS.items():
        if snake_case(k) == user_value:
            return v

    return None

# -----------------------------------------------------------------------------------------------------------------------------
# Get the user enum value from a parameter value

def get_enum_param_user(param_value, node_name, param_name):
    """ Get the user value from a parameter value

    The user value is searched in two dicts:
    - SPEC_ENUM_PARAMS (user -> value) : specific nodes
    - ENUM_PARAMS (user -> value) : common to all nodes

    Arguments
    ---------
    - param_value (str) : enum value (e.g. 'COSINE')
    - node_name (str) : node name
    - user_case (bool = True) : return the user case version, snake_case otherwise

    Returns
    -------
    - list of strs : the user names (starting by specific if any), e.g. ["Cos", "Cosine"]
    """

    return param_value

    # =============================================================================================================================
    # IN PROGRESS
    # =============================================================================================================================


    if BUILD or param_name in ['domain', 'data_type', 'input_type']:
        return param_value

    # ----------------------------------------------------------------------------------------------------
    # Very Specific

    # Node 'Subdivision Surface':
    # - param uv_smooth: All <-> SMOOTH_ALL
    # - param boundary_smooth: All <-> ALL
    if node_name == 'Subdivision Surface':
        if param_value in ['SMOOTH_ALL', 'ALL']:
            return 'All'

    # Node 'Point Density':
    # - param point_source: ('PARTICLE_SYSTEM', 'OBJECT')
    # - param space: ('OBJECT', 'WORLD')
    if node_name == 'Point Density':
        if param_value == 'OBJECT':
            if param_name == 'point_source':
                return 'Object Vertices'
            elif param_name == 'space':
                return 'Object Space'
            else:
                return None
        elif param_value == 'WORLD':
            if param_name == 'space':
                return 'World Space'
            else:
                return None

    # ----------------------------------------------------------------------------------------------------
    # Specific to node

    for node, specs in constants.SPEC_ENUM_PARAMS.items():
        if isinstance(node, tuple):
            if node_name not in node:
                continue
        else:
            if node != node_name:
                continue

        for k, v in specs.items():
            if v == param_value:
                return k

    # ----------------------------------------------------------------------------------------------------
    # Shared

    for k, v in constants.ENUM_PARAMS.items():
        if v == param_value:
            return k

    raise Exception(f"get_enum_param_user: param value '{param_value}' ('{node_name}'.{param_name}) not solved")

# -----------------------------------------------------------------------------------------------------------------------------
# Get the valid user enum values

def get_enum_param_users(param_values, node_name, param_name, user_case=True):
    """ Get all the users values

    Used in dynamic generation code
    """

    users = [get_enum_param_user(value, node_name, param_name) for value in param_values]
    if not user_case:
        users = [snake_case(v) for v in users]

    # ====================================================================================================
    # Check the consistency

    for u in users:
        v = get_enum_param_value(u, node_name, param_name)
        if v not in param_values:
            raise Exception(f"get_enum_param_users> node: '{node_name}', param: '{param_name}', user: '{u}', value: {v} not in {param_values}")

    return users

# -----------------------------------------------------------------------------------------------------------------------------
# Check the validity of an enum arg

def check_enum_arg(node_name: str, arg_name: str, arg_value: str, meth_name: str, valids: tuple) -> bool:
    """ Check the value of an enum param

    Raises
    ------
    - NodeError : if arg_value is not in valids

    Arguments
    ---------
    - node_name : node name
    - param_name : parameter name
    - arg_name : argument name
    - arg_value : argument value
    - meth_name : method name
    - valids : tuple of valid values

    Returns
    -------
    - bool : True
    """

    # Argument value can be the parameter value

    if arg_value in valids:
        return True

    # It can be the user version

    param_value = get_enum_param_value(arg_value, node_name, arg_name)
    if param_value in valids:
        return True

    raise NodeError(f"Parameter error: '{arg_value}' is not a valid value for argument '{arg_name}' in method '{meth_name}'.",
        keyword = arg_value,
        valids = get_enum_param_users(valids, node_name, arg_name, user_case=True),
        parameter_values = valids)

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

# =============================================================================================================================
# Node or socket label

def get_label(obj):
    if obj.label == "" or obj.label is None:
        return obj.name
    else:
        return obj.label


# =============================================================================================================================
# Node 'Color Ramp' utilities

def color_ramp_get_stops(bnode, as_str=False):

    stops = []
    elements = bnode.color_ramp.elements
    for element in elements:
        c = element.color
        stops.append((element.position, tuple([v for v in c])))

    if as_str:
        a = []
        for x, c in stops:
            sc = ", ".join([f"{v:.3f}" for v in c])
            a.append(f"({x:.3f}, ({sc}))")
        return "[" + ", ".join(a) + "]"

    return stops

def color_ramp_set_stops(bnode, *stops):
    """ Set the color ramp stops

    Arguments
    ---------
    - bnode : color ramp node
    - stops : list of tuple (position, color)
    """

    if len(stops) == 0:
        return

    elements = bnode.color_ramp.elements
    for i, stop in enumerate(stops):
        position : float
        color    : tuple = None
        if isinstance(stop, (tuple, list)):
            if len(stop) == 2:
                position = stop[0]
                color    = stop[1]
            else:
                raise NodeError(f"ColorRamp set_stops error: stops must be tuple(position, color) or single position, not {stop}")

        else:
            position = stop

        if color is not None:
            if hasattr(color, '__len__'):
                if len(color) == 3:
                    color = color + (1,)
            else:
                color = tuple(np.resize(color, 3)) + (1,)

        if i < len(elements):
            elements[i].position = position
        else:
            elements.new(position)

        if color is not None:
            elements[i].color = color

    for i in range(len(stops), len(elements)):
        elements.remove(elements[-1])

# =============================================================================================================================
# Node curves utilities

# -----------------------------------------------------------------------------------------------------------------------------
# Conversion of a single curve into a list of tuples:
# - x
# - y
# - handle_type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

def curve_to_list(curve, as_str=False):
    points = []
    for point in curve.points:
        points.append((point.location[0], point.location[1], point.handle_type))

    if as_str:
        return "[" + ", ".join([f"({x:.3f}, {y:.3f}, '{ht}')" for (x, y, ht) in points]) + "]"

    return points

# -----------------------------------------------------------------------------------------------------------------------------
# Conversion of a collection of curves into an list of list of tuples

def curves_to_list(curves, as_str=False):
    a = []
    for curve in curves:
        a.append(curve_to_list(curve, as_str=as_str))

    if as_str:
        return "[" + ",\n".join(a) + "]"

    return a

# -----------------------------------------------------------------------------------------------------------------------------
# Set a list to set up curves

def list_to_curves(points_list, curves):

    if len(points_list) == 0:
        return
    if isinstance(points_list[0], tuple):
        points_list = [points_list]

    for i_curve, curve in enumerate(curves):
        if i_curve >= len(points_list):
            break

        points = points_list[i_curve]


        for i, point in enumerate(points):
            if i < len(curve.points):
                x, y = curve.points[i].location
                ht = curve.points[i].handle_type
            else:
                x, y, ht = 0, 0, 'AUTO'

            if len(point) == 3:
                x, y, ht = point
            elif len(point) == 2:
                x, y = point
            else:
                raise Exception(f"'{point}' is not valid to set up a point in a curve. Expected is (float, floar, handle_type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR') )")

            if ht not in ('AUTO', 'AUTO_CLAMPED', 'VECTOR'):
                raise Exception(f"'{ht}' is not a valid handle type to set up a point in a curve. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')")

            if i >= len(curve.points):
                curve.points.new(x, y)
            else:
                curve.points[i].location = (x, y)

            curve.points[i].handle_type = ht

        if len(points) >= len(curve.points):
            to_del = [p for p in curve.points[len(points):]]
            for p in to_del:
                curve.points.remove(p)
