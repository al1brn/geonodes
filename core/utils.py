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
import difflib
import numpy as np

from pprint import pprint
import bpy

from .sockettype import SocketType
from .scripterror import NodeError
from . import constants
from .blender import get_font

BUILD = False

# ====================================================================================================
# Socket classes
# ====================================================================================================

# This dict is filled at run time to provide
# socket_type -> Socket class conversion

SOCKET_CLASSES = {}
GEOMETRY_CLASSES = {}

# ====================================================================================================
# Break to exit with blocks
# ====================================================================================================

class Break(Exception):
    """ Exception used to exit a With context block.

    ``` python
    with GeoNodes("Break Demo"):
        Geometry().out()
        raise Break()

        # Not executed
        Float(10).out()
    ```
    """
    pass


# ====================================================================================================
# Get / delete a tree
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Get a tree, create it if it doesn't exist
# ----------------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------------

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
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Replace accents and replace non kw chars by '_'
# ----------------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------------

def snake_case(s: str, test_keyword=True) -> str:

    import keyword

    if s == "":
        return ""

    sc = only_kw_chars(s.lower())

    if sc[0] in "0123456789":
        sc = '_' + sc

    if test_keyword and (sc in keyword.kwlist):
        sc += '_'

    return sc

# ----------------------------------------------------------------------------------------------------
# Ensure socket name unicity
# ----------------------------------------------------------------------------------------------------

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

# ====================================================================================================
# Proximity
# ====================================================================================================

def prox_names(name, valids, n=3, cutoff=0.6):
    res = difflib.get_close_matches(name, valids, n=n, cutoff=cutoff)
    if not len(res):
        res = difflib.get_close_matches(snake_case(name), [snake_case(valid) for valid in valids], n=n, cutoff=cutoff)
    return res


# ====================================================================================================
# Conversion between socket_type and bl_idname
# - socket_type in ('FLOAT', 'INT', 'BOOLEAN',...)
# - bl_idname in ('NodeSocketFloat', 'NodeSocketInt', 'NodeSocketBoolean',...)
# ====================================================================================================

def socket_type_to_bl_idname(socket_type, halt=True):

    SPEC = {
        'BOOLEAN': 'NodeSocketBool',
        'INTEGER': 'NodeSocketInt',
        'RGBA'   : 'NodeSocketColor',
        'VALUE'  : 'NodeSocketFloat',
    }
    if socket_type.startswith('NodeSocket'):
        return socket_type
    
    elif socket_type in SPEC:
        return SPEC[socket_type]
    
    else:
        ns = 'NodeSocket' + socket_type.title()
        if ns not in constants.SOCKET_SUBTYPES:
            if halt:
                raise RuntimeError(f"The socket type '{socket_type}' is not valid.")
            else:
                return None
        
        return ns
    
def bl_idname_to_socket_type(bl_idname, halt = True):

    SPEC = {
        'NodeSocketBool'  : 'BOOLEAN',
        'NodeSocketFloat' : 'VALUE',
        'NodeSocketColor' : 'RGBA',
    }
    ST_SPEC = {
        'INTEGER' : 'INT',
        'COLOR'   : 'RGBA',
        'FLOAT'   : 'VALUE', 
    }

    blid = bl_idname
    if blid in constants.SOCKET_SUBTYPES:
        blid = constants.SOCKET_SUBTYPES[bl_idname]['nodesocket']

    if blid in SPEC:
        return SPEC[blid]
    
    if blid.startswith('NodeSocket'):
        st = blid[len('NodeSocket'):].upper()
    else:
        st = ST_SPEC.get(bl_idname, bl_idname)

    if st not in constants.CLASS_NAMES.keys():
        if halt:
            raise RuntimeError(f"The bl_idname '{bl_idname}' is not valid.")
        else:
            return None
    
    return st

# ====================================================================================================
# Sockets utilities
# ====================================================================================================

def get_bsocket(socket):
    return SocketType.get_bsocket(socket)
    if isinstance(socket, bpy.types.NodeSocket):
        return socket
    else:
        return getattr(socket, '_bsocket', None)
    
def is_empty_socket(value):
    return hasattr(value, '_bsocket') and hasattr(value, '_is_empty') and value._is_empty()
    
def is_socket(socket):
    return get_bsocket(socket) is not None

def is_free(socket):
    bsocket = get_bsocket(socket)
    return bsocket.is_multi_input or (not bsocket.is_linked)

    # Strangely is_output seems to bo not always reliable :-()
    if bsocket.is_output:
        return True
    else:
        return bsocket.is_multi_input or (not bsocket.is_linked)
    
def get_default_name(socket):
    bsocket = get_bsocket(socket)
    if bsocket is None:
        return constants.NODE_CLASSES[get_value_socket_type(socket)]
    else:
        return bsocket.name

def get_socket_name(socket):
    
    bsocket = get_bsocket(socket)

    if socket is None:
        return None

    if bsocket.label in [None, ""]:
        return bsocket.name
    else:
        return bsocket.label

# ====================================================================================================
# Socket type from python value
# ====================================================================================================

def get_value_socket_type(value, restrict_to=None, default=None):

    socket_type = None

    # ---------------------------------------------------------------------------
    # It is a Socket
    # ---------------------------------------------------------------------------

    
    bsocket = get_bsocket(value)

    assert bsocket is None, "Test"

    if bsocket is not None:
        socket_type = bsocket.type

    # ---------------------------------------------------------------------------
    # A python type
    # ---------------------------------------------------------------------------

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
        raise RuntimeError(f"Impossible to get a socket type for value {value}")

    # ---------------------------------------------------------------------------
    # Restricted
    # ---------------------------------------------------------------------------

    if restrict_to is not None:
        if socket_type not in restrict_to:
            socket_type = default

    return socket_type

# ====================================================================================================
# Get items socket type
# ====================================================================================================

def get_items_socket_type(socket_type):
    """ Specific to node items socket type in new method.
    """
    if socket_type == 'VALUE':
        return 'FLOAT'
    else:
        return socket_type



# ====================================================================================================
# Get data_type
# ====================================================================================================

def get_input_type_OLD(value, restrict_to=None, default='FLOAT'):

    transco = {
        'VALUE': 'FLOAT',
    }

    itype = get_socket_type(value, restrict_to=restrict_to, default=default)
    return transco.get(itype, itype)
    

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


# ====================================================================================================
# Return socket info from
# - a socket
# - an interface item socket
# - a bl_idname
# - a socket type
# - a class name
# ====================================================================================================

def get_socket_info(value):

    # ----------------------------------------------------------------------------------------------------
    # Value is None
    # ----------------------------------------------------------------------------------------------------

    if value is None:
        return None

    # ----------------------------------------------------------------------------------------------------
    # Value is a socket
    # ----------------------------------------------------------------------------------------------------

    bsocket = get_bsocket(value)
    if bsocket is not None:
        return get_socket_info(bsocket.bl_idname)
    
    # ----------------------------------------------------------------------------------------------------
    # Value is an interface item
    # ----------------------------------------------------------------------------------------------------

    # TBD

    # ----------------------------------------------------------------------------------------------------
    # Value is a class name
    # ----------------------------------------------------------------------------------------------------

    if isinstance(value, type):
        return get_socket_info(type(value).__name__)

    # ----------------------------------------------------------------------------------------------------
    # Must be a str
    # ----------------------------------------------------------------------------------------------------

    if not isinstance(value, str):
        raise RuntimeError(f"Impossible to get socket info from value {value}.")
    
    # ----------------------------------------------------------------------------------------------------
    # value is socket type in 'GEOMETRY', 'INT',...
    # ----------------------------------------------------------------------------------------------------

    if value == 'INTEGER':
        value = 'INT'
    elif value == 'FLOAT':
        value = 'VALUE'
    elif value == 'COLOR':
        value = 'RGBA'

    if value in constants.CLASS_NAMES.keys():
        bl_idname = socket_type_to_bl_idname(value)
        return {
            'bl_idname'     : bl_idname,
            'sub_blid'      : bl_idname,
            'socket_type'   : value,
            'subtype'       : None,
            'dimensions'    : None,
            }
    
    # ----------------------------------------------------------------------------------------------------
    # value is a bl_idname name
    # ----------------------------------------------------------------------------------------------------

    if value in constants.SOCKET_SUBTYPES:
        spec = constants.SOCKET_SUBTYPES.get(value)
        return {
            'bl_idname'     : spec['nodesocket'],
            'sub_blid'      : value,
            'socket_type'   : bl_idname_to_socket_type(value),
            'subtype'       : spec['subtype'],
            'dimensions'    : spec['dimensions'],
        }
    
    # ----------------------------------------------------------------------------------------------------
    # value is a class_name
    # ----------------------------------------------------------------------------------------------------

    cname = value
    if cname in constants.GEOMETRY_CLASSES:
        cname = 'Geometry'

    for stype, name in constants.CLASS_NAMES.items():
        if name == cname:
            return get_socket_info(stype)
        
    # ----------------------------------------------------------------------------------------------------
    # value is a class_name
    # ----------------------------------------------------------------------------------------------------

    raise RuntimeError(f"Impossible to get socket info from '{value}'. Must be a socket type, a socket bl_idname or a class name.")

# ====================================================================================================
# Wrap a NodeSocket into its class
# ====================================================================================================

def request_empty(value) -> bool:
    """ Value is equal to constant EMPTY_SOCKET
    """
    return isinstance(value, str) and value == constants.EMPTY_SOCKET

# ----------------------------------------------------------------------------------------------------
# Get the socket class
# ----------------------------------------------------------------------------------------------------

def get_socket_class(socket_type, name=None):

    socket_type = SocketType(socket_type)
    stype = socket_type.type

    if stype == 'GEOMETRY':
    
        if name is None:
            return SOCKET_CLASSES[stype]
        
        name = name.lower()

        # 5.0.0 socket names
        # IN : {'Geometry', 'Target Geometry', 'Volume', 'A', 'Points', 'Curves', 'Instances', 
        # 'True', 'Profile Curve', 'False', 'Guide Curves', 'Mesh 1', 'Mesh', '0', 
        # 'Grease Pencil', 'B', 'Mesh 2', 'Curve', '1', 'Instance'}
        # OUT: {'Points', 'Convex Hull', 'Element', 'Curves', 'Bounding Box', 
        # 'Geometry', 'Output', 'Inverted', 'Instances', 'Selection', 'Transform', 
        # 'Dual Mesh', 'Curve Instances', 'Mesh', 'Volume', 'Curve', 'Point Cloud', 'Grease Pencil'}
        
        if name in ('mesh', 'convex hull', 'bounding box', 'dual mesh') or name.startswith('Mesh'):
            class_name = 'Mesh'
        elif name in ('curve', 'curves', 'profile curve', 'guide curve'):
            class_name = 'Curve'
        elif name in ('points', 'point cloud', 'cloud'):
            class_name = 'Cloud'
        elif name in ('grease pencil',):
            class_name = 'GreasePencil'
        elif name in ('instance', 'instances', 'curve instances'):
            class_name = 'Instances'
        elif name in ('volume'):
            class_name = 'Volume'
        else:
            class_name = 'Geometry'

        return GEOMETRY_CLASSES[class_name]

    elif stype not in SOCKET_CLASSES.keys():
        if stype == socket_type:
            raise TypeError(f"socket_type '{socket_type}' not found in {list(SOCKET_CLASSES.keys())}.")
        else:
            raise TypeError(f"Node socket '{socket_type}' ({stype}) not found in {list(SOCKET_CLASSES.keys())}.")

    return SOCKET_CLASSES[stype]

# ----------------------------------------------------------------------------------------------------
# To socket
# ----------------------------------------------------------------------------------------------------

def to_socket(socket):
    bsocket = get_bsocket(socket)
    if bsocket is None:
        return get_socket_class(get_value_socket_type(socket))(socket)
    else:
        return get_socket_class(bsocket.type, name=bsocket.name)(bsocket)
    
# ----------------------------------------------------------------------------------------------------
# Socket sub type
# ----------------------------------------------------------------------------------------------------
    
def get_socket_subtype(bl_idname):
    info = get_socket_info(bl_idname)
    return info['socket_type'], info['subtype'], info['dimensions']

def get_socket_bl_idname(bl_idname):
    info = get_socket_info(bl_idname)
    return info['bl_idname'], info['subtype'], info['dimensions']


# ====================================================================================================
# Node bl_idname <-> user name
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Get a node bl_idname from a name
# ----------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------
# User name from bl_idname
# ----------------------------------------------------------------------------------------------------

def get_node_name(tree_type, bl_idname):
    return list(constants.NODE_NAMES[tree_type].keys())[list(constants.NODE_NAMES[tree_type].values()).index(bl_idname)]

# ----------------------------------------------------------------------------------------------------
# data_type argument can be derived from the argument passed to the node
# ----------------------------------------------------------------------------------------------------

def get_data_type_from_argument(tree_type: str, bl_idname: str, argument):
    """ Compute data_type Node argument

    data_type argument is derived from the type of the passed argument.

    Attribute
    ---------
    - tree_type (str) : tree type
    - bl_idname (str) : node bl_idname
    - argument (Any) : the argument the derive data_type from
    - arg_name (str = None) : in case of an error

    Returns
    -------
    - str : valid value for data_type
    """
    return SocketType(argument).get_node_data_type(tree_type, bl_idname, halt=False)


def get_data_type_argument(tree_type, bl_idname, socket_type):
    dts = constants.NODE_DATA_TYPES[tree_type][bl_idname]
    if socket_type in dts:
        return dts[socket_type]
    raise RuntimeError(f"Socket type '{socket_type}' is not valid for data_type attribute in node {bl_idname}. Valids are {list(dts.keys())}")


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
        raise NodeError(f"The value {value} with shape {np.shape(a)} (size: {np.size(a)}) can't be reshaped into {shape} (size: {np.prod(shape).astype(int)})")

def get_dim_vector(value, dims):
    if dims is None:
        if value is None:
            return (0., 0., 0.)
        elif hasattr(value, '__len__'):
            n = min(4, max(2, len(value)))
            return tuple(value_to_array(value, (n,)))
        else:
            return tuple(value_to_array(value, (3,)))
    else:
        dims = min(4, max(2, dims))
        if value is None:
            return (0.,)*dims
        else:
            return tuple(value_to_array(value, (dims,)))
        

# ====================================================================================================
# Node groups
# ====================================================================================================

def get_available_groups(tree_type: str) -> dict:
        
    groups = {}
    for ng in bpy.data.node_groups:
        if ng.bl_idname != tree_type:
            continue
        groups[ng.name] = {'group': ng, 'source': 'node_groups'}

    for group_name, file_name in constants.BUILTIN_GROUPS[tree_type].items():
        groups[group_name] = {'source': 'built_in', 'file_name': file_name}

    for name, spec in groups.items():
        spec['tree_type'] = tree_type
        spec['name'] = name

    return groups

def find_snake_case_name(sc_name: str, raw_names: list):
    """ Find the snake case version of a nam in a list of raw names.
    """

    for raw_name in raw_names:
        if snake_case(raw_name) == sc_name:
            return raw_name
        
    return None

def get_enum_from_string(s):
    token = "not found in "
    p = s.find(token)
    if p < 0:
        return ()
    else:
        return eval(s[p + len(token):])


def get_enums(obj, attr):
    token = "not found in "
    try:
        setattr(obj, attr, "OUPS")
    except TypeError as e:
        s = str(e)
        p = s.find(token)
        return eval(s[p + len(token):])
    
    assert False, f"Shouldn't happen, {obj=}, {attr=}"

def get_menu_enums(menu):
    assert menu.bl_idname == 'NodeSocketMenu'
    return get_enums(menu, 'default_value')

# ====================================================================================================
# Value to color
# ====================================================================================================

def value_to_color(value):
    return SocketType('COLOR').get_default_from_value(value)


# =============================================================================================================================
# Some utilities

def is_vector_like(value):
    return SocketType(value).type in ['RGBA', 'VECTOR', 'ROTATION']

def is_color_like(value):
    return SocketType(value).type in ['RGBA', 'VECTOR']

def is_matrix_like(value):
    return SocketType(value).type in ['MATRIX']

def is_value_like(value):
    return SocketType(value).type in ['FLOAT', 'INT', 'BOOLEAN']

def is_int_like(value):
    return SocketType(value).type in ['INT', 'BOOLEAN']

def has_bsocket(value):
    if get_bsocket(value) is not None:
        return True

    if not hasattr(value, '__len__'):
        return False

    for item in value:
        if get_bsocket(item) is not None:
            return True

    return False


def check_link(link, halt=False):

    if link is None:
        return False

    def ssock(sock):
        sock.node.use_custom_color = True
        sock.node.color = (1, 0, 0)
        return f"[{sock.node.name}].'{sock.name}'"

    if link.is_valid:
        return True
    
    if halt:
        raise RuntimeError(f"Invalid link from {ssock(link.from_socket)} to {ssock(link.to_socket)}")
    else:
        print(f"Caution: Invalid link from {ssock(link.from_socket)} to {ssock(link.to_socket)}")

    return False



# =============================================================================================================================
# Get a python value compatible with socket default_value

def python_value_for_socket(value, socket_type):

    from . import blender

    if value is None:
        return None
    
    bsock = get_bsocket(value)
    if bsock is not None:
        return getattr(bsock, 'default_value')
    
    socket_type = bl_idname_to_socket_type(socket_type)

    if socket_type in ['BOOLEAN', 'BOOL']:
        return bool(value)

    elif socket_type == 'INT':
        return int(value)

    elif socket_type in ['VALUE', 'FLOAT']:
        return float(value)

    elif socket_type in ['VECTOR', 'ROTATION']:
        return value_to_array(value, (3,))

    elif socket_type in ['RGBA', 'COLOR']:
        return value_to_color(value)

    elif socket_type in ['STRING', 'MENU']:
        return str(value)

    elif socket_type in ['COLLECTION', 'OBJECT', 'IMAGE', 'MATERIAL']:
        return blender.get_resource(socket_type, value)

    else:
        raise NodeError(f"python_value_for_socket error: impossible to build a value from '{value}' for socket '{socket_type}'")


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
    if isinstance(attr_name, str):
        return "_" + attr_name.replace(' ', '_')
    else:
        return None

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

# =============================================================================================================================
# Zones consistency checks

def set_node_error(bnode):
    bnode.use_custom_color = True
    bnode.color = (1, 0, 0)
    return bnode

def set_node_warning(bnode):
    bnode.use_custom_color = True
    bnode.color = (1.000, 0.580, 0.125)
    return bnode


# -----------------------------------------------------------------------------------------------------------------------------
# Feeding nodes

def feeding_nodes(bnode: 'Blender Node') -> list:
    """ Get all the nodes feeding a node

    A "feeding" node is a node connected directly or indirectly to at least one input socket.

    Arguments
    ---------
    - bnode : the node the get the feeding nodes

    Returns
    -------
    - list of Nodes : the nodes feeding the argument
    """

    def trace(bnode, feeders):
        for in_sock in bnode.inputs:
            for link in in_sock.links:

                n = link.from_node

                if n.name == bnode.name:
                    bnode.color = (1, 0, 0)
                    raise Exception(f"Node '{bnode.name}' is linked to himself")

                if n not in feeders:
                    feeders.append(n)
                    trace(n, feeders)

    feeders = []

    trace(bnode, feeders)

    return feeders

# -----------------------------------------------------------------------------------------------------------------------------
# Nodes which are fed

def fed_nodes(bnode: 'Blender Node') -> bool:
    """ Get all the nodes which are fed by the node argument

    A "feeding" node is a node connected directly or indirectly to at least one input socket.

    Arguments
    ---------
    - bnode : the node the get the fed nodes

    Returns
    -------
    - list of Nodes : the nodes fed by the argument
    """

    def trace(bnode, feds):
        for out_sock in bnode.outputs:
            for link in out_sock.links:

                n = link.to_node

                if n.name == bnode.name:
                    bnode.color = (1, 0, 0)
                    raise Exception(f"Node '{bnode.name}' is linked to himself")


                if n not in feds:
                    feds.append(n)
                    trace(n, feds)

    feds = []

    trace(bnode, feds)

    return feds

# -----------------------------------------------------------------------------------------------------------------------------
# Nodes fed by a zone input node

def zone_inner_nodes(zone_input):
    """ Nodes within a zone

    A node is in the zone if the zone input node feeds the node AND the node feeds the zone output node
    """

    def trace(bnode, inners):
        for out_sock in bnode.outputs:
            for link in out_sock.links:

                n = link.to_node
                if n in inners:
                    continue

                if n.name == zone_input.paired_output.name:
                    continue

                inners.append(n)
                trace(n, inners)

        return inners

    return trace(zone_input, [])


# -----------------------------------------------------------------------------------------------------------------------------
# Check nodes which raise problem for zones

def check_zones(btree: 'Blender Tree') -> bool:
    """ Check the zones are consistent

    A problem is raised if a node is fed by zone input and:
    - either feeds a node fed by the zone output
    - or feeds the tree output

    Arguments
    ---------
    - btree : the tree to work with

    Raises
    ------
    - NodeError in case of a problem

    Returns
    -------
    - bool : True
    """

    # ----- Loop on the zones

    for zone_input in btree.nodes:

        # Only input zone nodes
        zone_output = getattr(zone_input, 'paired_output', None)
        if zone_output is None:
            continue

        # Nodes fed by zone input
        inners = zone_inner_nodes(zone_input)

        # Nodes fed by zone output
        outers = fed_nodes(zone_output)

        # Loop on the inner nodes
        for node in inners:
            # Error 1 : Group output is fed by zone input
            if node.bl_idname == 'NodeGroupOutput':
                set_node_error(zone_input)
                set_node_error(node)

                raise NodeError("Zone input node is connected to group output")

            # Error 2 : inner node also fed by zone output node
            if node in outers:
                set_node_error(zone_input)
                set_node_error(zone_output)
                set_node_error(node)
                raise NodeError(
                    "A node belonging to a zone is linked outside the zone.\n"
                    f"Zone : {zone_input.bl_idname} -> {zone_output.bl_idname}\n"
                    f"Wrongly linked Node : {node.name} ({node.label})."
                )

    return True
