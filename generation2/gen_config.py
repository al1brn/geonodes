"""
Generate config dicts from current Blender version
"""

import bpy
import ast
from copy import deepcopy
from datetime import datetime
import textwrap
import inspect

from pathlib import Path
from pprint import pprint

from .node_dims import NODE_DIMS
from .node_info import NodeInfo
from .tree import Tree
from . import target_core, config

ALL = ['blender_version',
       # Hard coded
       'TREE_TYPES',
       'CLASS_NAMES', 'GEOMETRY_CLASSES', 'DOMAIN_CLASSES', 'ATTRIBUTE_CLASSES',
       'DATA_TYPE_HOMONYMS', 'AUTO_INPUT_TYPE_NODES', 'SOCKET_SHAPES',

       # Generated
       'SOCKETS', 'SOCKET_SUBTYPES', 'SOCKET_IDS',
       'NODE_INFO', 'NODE_NAMES', 'ONE_ITEMS_NODES', 
       'BUILTIN_GROUPS',
       ]

# Hard coded global
from .config import TREE_TYPES
from .config import CLASS_NAMES, GEOMETRY_CLASSES, DOMAIN_CLASSES, ATTRIBUTE_CLASSES
from .config import DATA_TYPE_HOMONYMS, AUTO_INPUT_TYPE_NODES, SOCKET_SHAPES

# Will be generated
SOCKETS             = {} # create_sockets_dicts
SOCKET_SUBTYPES     = {} # create_sockets_dicts
SOCKET_IDS          = {} # create_sockets_dicts
NODE_INFO           = {} # create_nodes_dicts
NODE_NAMES          = {} # create_nodes_dicts
ONE_ITEMS_NODES     = {} # create_nodes_dicts
BUILTIN_GROUPS      = {} # create_builtin_groups

# ====================================================================================================
# Module level globals
# ====================================================================================================

# Interface socket attributes
# These attributes are optional attribute used in socket constructors

_TREE_INTERFACE_SOCKET_PROPS = {

    # First ones
    'default_value'             : "default",
    'min_value'                 : "min",
    'max_value'                 : "max",
    'description'               : "tip",

    # Keyword arguments
    'default_input'             : "default_input",
    'force_non_field'           : "force_non_field",
    'hide_in_modifier'          : "hide_in_modifier",
    'hide_value'                : "hide_value",
    'is_panel_toggle'           : "is_panel_toggle",
    'layer_selection_field'     : "layer_selection",
    'menu_expanded'             : "menu_expanded",
    'optional_label'            : "optional_label",
    'structure_type'            : "shape",

    # Directly managed
    #'name',

    # Unexposed 
    #'attribute_domain',
    #'default_attribute_name',
}

# A working copy receives Blender's discovered subtype/shape choices.
#INPUT_SOCKETS_PROPS = deepcopy(config.INPUT_SOCKETS_PROPS)

# Blend files containing embedded groups
_BLEND_FILES = {
    'GeometryNodeTree' : ["geometry_nodes_essentials.blend", "procedural_hair_node_assets.blend"],
    'ShaderNodeTree' : ["shading_nodes_essentials.blend"],
}

# ====================================================================================================
# Utilities
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Get the enum 
# ----------------------------------------------------------------------------------------------------

def get_enum(obj, attr):
    token = "not found in "
    s = "Not enum"
    try:
        setattr(obj, attr, "OUPS")
    except TypeError as e:
        s = str(e)

    p = s.find(token)
    if p < 0:
        raise RuntimeError(f"{obj!r}.{attr} is not an enum")
    
    return eval(s[p + len(token):])

# ----------------------------------------------------------------------------------------------------
# Get type and default
# ----------------------------------------------------------------------------------------------------

def get_type_default(obj, attr):

    val = getattr(obj, attr)
    try:
        return get_enum(obj, attr), val
    except:
        return type(val).__name__, val

# ====================================================================================================
# Sockets
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Create sockets from Interface
# ----------------------------------------------------------------------------------------------------

def create_sockets(tree_type):
    """ Build three dicts

    The 3 dicts are then actually built by create_sockets_dicts
    
    SOCKETS : {
        socket_type : {
            nodesocket : socket bl_idname
            subtypes: tuple(subtyps)
            props : (
                name : (internal name, type, default),
            class_name : class name

    SOCKET_SUBTYPES : {
        typed socket bl_idname: {
            nodesocket  : main socket bl_idname
            socket_type : socket type
            subtype     : sub type
'           dimensions  : int | None

    SOCKET_IDS : {
        typed socket bl_idname : main socket bl_idname
    """

    with Tree(tree_type) as tree:

        # Initialization
        input_node = tree.btree.nodes.new(type='NodeGroupInput')
        
        # Get list of socket bl_idnames
        try:
            tree.btree.interface.new_socket(name="Toto", socket_type='ERR')
        except Exception as e:
            s = str(e)
            
        token = 'enum "ERR" not found in '
        p = s.find(token)
        blids = eval(s[p+len(token):])
        
        sockets = {}
        socket_subtypes = {}
        socket_ids = {}
        
        # Possible subtypes
        for blid in blids:
            
            # Interface socket
            sock = tree.btree.interface.new_socket(name=blid, socket_type=blid)
            
            # Corresponding Input socket
            in_sock = input_node.outputs[blid]

            # Properties
            props = {}
            for prop_name in dir(sock):
                if prop_name in _TREE_INTERFACE_SOCKET_PROPS:
                    ui_name = _TREE_INTERFACE_SOCKET_PROPS[prop_name]
                    props[ui_name] = (prop_name,) + get_type_default(sock, prop_name)

            # New entries in the dicts
            sockets[in_sock.type] = {
                'nodesocket'    : blid,
                'subtypes'      : (),
                'props'         : props,
                'class_name'    : config.CLASS_NAMES[in_sock.type],
            }

            socket_ids[blid] = blid
            socket_ids[config.CLASS_NAMES[in_sock.type]] = blid
            socket_ids[in_sock.type] = blid

            socket_subtypes[blid] = {
                'nodesocket'    : blid,
                'socket_type'   : in_sock.type,
                'subtype'       : getattr(sock, 'subtype', None),
                'dimensions'    : getattr(sock, 'dimensions', None),
            }

            # types socket bl_idnames
            if hasattr(sock, "subtype"):
                subtypes = get_enum(sock, 'subtype')

                sockets[in_sock.type]['subtypes'] = subtypes

                for subtype in subtypes:
                    sock.subtype = subtype
                    detailed_id = in_sock.bl_idname
                    
                    socket_ids[detailed_id] = blid
                    
                    socket_subtypes[in_sock.bl_idname] = {
                        'nodesocket'    : blid,
                        'socket_type'   : in_sock.type,
                        'subtype'       : subtype,
                        'dimensions'    : getattr(sock, 'dimensions', None),
                    }

        # We need to complete with virtual socket
        sockets['CUSTOM'] = {
            'nodesocket'    : 'NodeSocketVirtual',
            'subtypes'      : (),
            'props'         : {},
            'class_name'    : 'Input',
        }

        socket_ids['NodeSocketVirtual'] = 'NodeSocketVirtual'
        socket_ids['CUSTOM'] = 'NodeSocketVirtual'
        socket_ids['Input'] = 'NodeSocketVirtual'

        socket_subtypes['NodeSocketVirtual'] = {
            'nodesocket'  : 'NodeSocketVirtual',
            'socket_type' : 'CUSTOM',
            'subtype'     : None,
            'dimensions'  : None,
        }
                    
    return {
        'SOCKETS'         : sockets,
        'SOCKET_SUBTYPES' : socket_subtypes,
        'SOCKET_IDS'      : socket_ids,
    }

# ----------------------------------------------------------------------------------------------------
# Get sockets exposed by nodes which are not identified by create_sockets (create_sockets uses interface)
# ----------------------------------------------------------------------------------------------------

def get_unregistered_sockets(sockets, verbose=False):
    
    unregistered = set()

    def f(node):
        for bsock in list(node.bnode.inputs) + list(node.bnode.outputs):
            blid = bsock.bl_idname
            if blid in sockets:
                continue

            # hidden type not yet exposed
            if bsock.type not in config.CLASS_NAMES:
                continue

            unregistered.add((blid, bsock.type))

            if verbose:
                print(f"UNREGISTERED {tree_type} {blid:25s} : {node.name}.{bsock.name}")

    for tree_type in config.TREE_TYPES:
        NodeInfo.loop_on_nodes(f, tree_type=tree_type)

    return unregistered

# ----------------------------------------------------------------------------------------------------
# Create global sockets dicts
# ----------------------------------------------------------------------------------------------------

def create_sockets_dicts():
    """ Build the 3 dicts for all tree_types
    """

    for tree_type in TREE_TYPES:
        
        dicts = create_sockets(tree_type)

        for k, v in dicts['SOCKETS'].items():
            if k not in SOCKETS:
                SOCKETS[k] = v
            SOCKETS[k][tree_type] = SOCKETS[k]['nodesocket']

        for k, v in dicts['SOCKET_SUBTYPES'].items():
            if k not in SOCKET_SUBTYPES:
                SOCKET_SUBTYPES[k] = v

        SOCKET_IDS.update(dicts['SOCKET_IDS'])

        # complete SOCKET_IDS
        for cn in GEOMETRY_CLASSES + DOMAIN_CLASSES:
            SOCKET_IDS[cn] = 'NodeSocketGeometry'

        for name, stype in DATA_TYPE_HOMONYMS.items():
            SOCKET_IDS[name] = SOCKET_IDS[stype]

    # Unregistered sockets
    for blid, socket_type in get_unregistered_sockets(SOCKET_IDS, verbose=False):

        SOCKET_IDS[blid] = SOCKET_IDS[socket_type]

        if blid.endswith('2D'):
            dims=2
        elif blid.endswith('3D'):
            dims = 3
        else:
            dims = None

        SOCKET_SUBTYPES[blid] = {
            'nodesocket'  : SOCKET_IDS[socket_type],
            'socket_type' : socket_type,
            'subtype'     : None,
            'dimensions'  : dims,
        }

# ====================================================================================================
# Nodes
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Print the input and output sockets names for getting the right Geometry class
# ----------------------------------------------------------------------------------------------------

def print_geometry_names():

    with Tree('GeometryNodeTree') as tree_context:
        tree = tree_context.btree
        in_names = set()
        out_names = set()

        for tp in tree_context.nodes.values():
            node = tree_context.create_node(tp)
        
            for sock in node.inputs:
                if sock.type == 'GEOMETRY':
                    in_names.add(sock.name)
                
            for sock in node.outputs:
                if sock.type == 'GEOMETRY':
                    out_names.add(sock.name)
                
            tree.nodes.remove(node)

            print("Sockets names for Geometry sockets classes\n")
                
        print("Input sockets:", in_names)
        print("Output sockets:", out_names)
        print()

# ----------------------------------------------------------------------------------------------------
# Get info on nodes
# ----------------------------------------------------------------------------------------------------

def create_nodes_dicts():
    """ Build NODE_NAMES, NODE_INFO, ONE_ITEMS_NODES dicts
    """

    def f(node: NodeInfo):

        if node.bl_idname in config.DEPRECATED_NODES:
            return

        # NODE_NAMES
        NODE_NAMES[node.tree_type][node.name] = node.bl_idname

        # NODE_INFO
        if node.bl_idname not in NODE_INFO:
            NODE_INFO[node.bl_idname] = node.node_info_entry

        # ONE_ITEMS_NODES
        if len(NODE_INFO[node.bl_idname]['items']) == 1:
            ONE_ITEMS_NODES[node.bl_idname] = NODE_INFO[node.bl_idname]['items'][0]

    for tree_type in config.TREE_TYPES:
        NODE_NAMES[tree_type] = {}
        NodeInfo.loop_on_nodes(f, tree_type=tree_type)

# ====================================================================================================
# Builtin groups
# ====================================================================================================

def create_builtin_groups():

    root = Path(bpy.utils.system_resource('DATAFILES')) / "assets/nodes"
    assert root.is_dir(), f"DATAFILES {str(root)} doesn't exist."

    for tree_type, blend_files in _BLEND_FILES.items():
        groups = {}
        for file_name in blend_files:
            with bpy.data.libraries.load(str(root / file_name)) as (data_from, data_to):
                for ng in list(data_from.node_groups):
                    groups[ng] = file_name

        BUILTIN_GROUPS[tree_type] = groups

# ====================================================================================================
# Build
# ====================================================================================================

def build():

    create_sockets_dicts()
    create_nodes_dicts()
    create_builtin_groups()


# ====================================================================================================
# Compare versions
# ====================================================================================================

def compare_versions(old_module):

    # ---------------------------------------------------------------------------
    # Compare two dicts
    # ---------------------------------------------------------------------------

    def compare_dicts(old_dict, new_dict, tab=""):

        # Node layout dimensions do not affect version compatibility.
        if isinstance(old_dict, dict) and isinstance(new_dict, dict):
            old_dict = {k: v for k, v in old_dict.items() if k != 'dims'}
            new_dict = {k: v for k, v in new_dict.items() if k != 'dims'}

        lines = []

        # Lengths are the same ?

        old_n = len(old_dict)
        new_n = len(new_dict)
        if old_n != new_n:
            lines.append(f"{tab}Lengths are diff: old: {old_n}, new: {new_n}")

        # Type list

        if isinstance(old_dict, list):
            for i in range(len(old_dict)):
                if i >= len(new_dict):
                    lines.append(f"{tab}Item i: <{old_dict[i]}> doesn't exist in new list")
                elif old_dict[i] != new_dict[i]:
                    lines.append(f"{tab}Item i: old <{old_dict[i]}> doesn't match new <{new_dict[i]}>")

            return lines

        # Type dict

        for k, old_v in old_dict.items():
            if k not in new_dict:
                lines.append(f"{tab}Key '{k}': doesn't exist in new dict")
                continue

            new_v = new_dict[k]
            if isinstance(new_v, dict):
                sub_lines = compare_dicts(old_v, new_v, tab=tab + "   ")
                if len(sub_lines):
                    lines.append(f"{tab}Key '{k}': dicts are different")
                    for l in sub_lines:
                        lines.append("   " + l)
                
            else:
                # Hack = 5.0 -> 5.1 : label property from "" to name
                if k == 'label':
                    continue

                if new_v != old_v:
                    lines.append(f"{tab}Key '{k}': value has changed: old: <{old_v}> -> new: <{new_v}>")

        for k in new_dict:
            if k not in old_dict:
                lines.append(f"{tab}Key '{k}': new key in new dict")

        return lines
    
    # ---------------------------------------------------------------------------
    # Compare two global dicts
    # ---------------------------------------------------------------------------

    def compare_global(name, old_dict, new_dict):
        lines = compare_dicts(old_dict, new_dict)
        if lines:
            print(f"{name:20s}: changes...")
            print("\n".join(lines))
            print()
        else:
            print(f"{name:20s}: ok")
        

    # ---------------------------------------------------------------------------
    # Compare with old version
    # ---------------------------------------------------------------------------

    print('\n'*3)
    print("="*100)
    print('Compare old to new version...')
    print("="*100)
    print()

    compare_global("GEOMETRY_CLASSES",      old_module.config.GEOMETRY_CLASSES,    config.GEOMETRY_CLASSES)
    compare_global("DOMAIN_CLASSES",        old_module.config.DOMAIN_CLASSES,      config.DOMAIN_CLASSES)
    compare_global("ATTRIBUTE_CLASSES",     old_module.config.ATTRIBUTE_CLASSES,   config.ATTRIBUTE_CLASSES)
    compare_global("ATTRIBUTE_CLASSES",     old_module.config.ATTRIBUTE_CLASSES,   config.ATTRIBUTE_CLASSES)

    compare_global("CLASS_NAMES",           old_module.CLASS_NAMES,         CLASS_NAMES)
    compare_global("DATA_TYPE_HOMONYMS",    old_module.config.DATA_TYPE_HOMONYMS,  config.DATA_TYPE_HOMONYMS)

    compare_global("SOCKET_IDS",            old_module.SOCKET_IDS,          SOCKET_IDS)
    compare_global("SOCKETS",               old_module.SOCKETS,             SOCKETS)
    compare_global("SOCKET_SUBTYPES",       old_module.SOCKET_SUBTYPES,     SOCKET_SUBTYPES)

    compare_global("BUILTIN_GROUPS",        old_module.BUILTIN_GROUPS,      BUILTIN_GROUPS)
    compare_global("ONE_ITEMS_NODES",       old_module.ONE_ITEMS_NODES,     ONE_ITEMS_NODES)
    compare_global("SEVERAL_ITEMS_NODES",   old_module.SEVERAL_ITEMS_NODES, SEVERAL_ITEMS_NODES)

    compare_global("INPUT_SOCKETS_PROPS",   old_module.INPUT_SOCKETS_PROPS, INPUT_SOCKETS_PROPS)
    compare_global("NODE_NAMES",            old_module.NODE_NAMES,          NODE_NAMES)
    compare_global("NODE_INFO",             old_module.NODE_INFO,           NODE_INFO)

    print('='*100)
    for tt in ['GeometryNodeTree', 'ShaderNodeTree']:
        print(f"\n{tt} new nodes:")
        print('-'*40)

        for k in NODE_NAMES[tt]:
            if k not in old_module.NODE_NAMES[tt]:
                print("-", k)

    print()
    print('='*100)

    
    print()
    print("Done")

# ====================================================================================================
# Write the config file
# ====================================================================================================

def write_header(f, title):
    f.write('#' + '-'*80 + "\n")
    f.write("# " + title + "\n")
    f.write('#' + '-'*80 + "\n\n")

def write_simple_dict(f, name, d):
    l = max([len(k) for k in d]) + 2
    f.write(f"{name} = {{\n")
    for k, v in d.items():
        f.write(f"   {k!r:{l}s} : {v!r},\n")
    f.write("}\n\n")

def write_dict(f, name, main_dict):

    tab = "    "

    def w(indent, d):
        if len(d) == 0:
            f.write("\n")
            return
        
        l = max([len(k) for k in d]) + 2
        for k, v in d.items():
            f.write(tab*indent + f"{k!r:{l}s} : ")
            if isinstance(v, dict):
                if not len(v):
                    f.write("{},\n")
                else:
                    f.write("{\n")
                    w(indent + 1, v)
                    f.write(tab*indent + "},\n")
            else:
                f.write(f"{v!r},\n")

    f.write(f"{name} = {{\n")
    w(1, main_dict)
    f.write("}\n\n")

    
def write_file(path=None, *, new=True):
    """Write the current Blender configuration to core_new (or core)."""
    if not SOCKETS:
        build()
    path = target_core(path, new=new)

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
        # Tree
        # ----------------------------------------------------------------------------------------------------

        write_header(f, f"Trees")
        f.write(f"TREE_TYPES = {TREE_TYPES}\n")
        f.write("\n")

        # ----------------------------------------------------------------------------------------------------
        # Classes
        # ----------------------------------------------------------------------------------------------------

        write_header(f, f"Classes lists")
        write_simple_dict(f, 'CLASS_NAMES', CLASS_NAMES)
        f.write("\n\n")


        f.write(f"GEOMETRY_CLASSES = {GEOMETRY_CLASSES}\n")
        f.write(f"DOMAIN_CLASSES = {DOMAIN_CLASSES}\n")
        f.write(f"ATTRIBUTE_CLASSES = {ATTRIBUTE_CLASSES}\n")
        f.write("\n")

        # ----------------------------------------------------------------------------------------------------
        # Sockets
        # ----------------------------------------------------------------------------------------------------

        f.write(f"SOCKET_SHAPES = {SOCKET_SHAPES}\n\n")

        write_header(f, "Sockets")
        write_simple_dict(f, "DATA_TYPE_HOMONYMS", DATA_TYPE_HOMONYMS)
        write_simple_dict(f, "SOCKET_IDS", SOCKET_IDS)

        # ----------------------------------------------------------------------------------------------------
        # Sockets
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Sockets details")
        write_dict(f, "SOCKETS", SOCKETS)
        
        # ----------------------------------------------------------------------------------------------------
        # Socket sub types
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Get base socket bl_idname and subtype from full node socket")
        write_dict(f, "SOCKET_SUBTYPES", SOCKET_SUBTYPES)

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
        write_dict(f, "ONE_ITEMS_NODES", ONE_ITEMS_NODES)
        
        f.write("AUTO_INPUT_TYPE_NODES = ")
        pprint(AUTO_INPUT_TYPE_NODES, stream=f)
        f.write("\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Node names
        # ----------------------------------------------------------------------------------------------------
        
        write_header(f, "Node names to bl_idname")

        for tree_type, nodes in NODE_NAMES.items():
            f.write(f"# {tree_type:16s} : {len(nodes)} nodes\n")
        f.write("\n")

        write_dict(f, "NODE_NAMES", NODE_NAMES)

        # ----------------------------------------------------------------------------------------------------
        # Info on nodes
        # ----------------------------------------------------------------------------------------------------

        write_header(f, "Node info")        
        write_dict(f, "NODE_INFO", NODE_INFO)

def test(*, new=True):
    write_file(new=new)


