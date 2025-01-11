from pathlib import Path
import bpy

from . node_explore import NodeInfo
from . import gen_auto_dicts
from . gen_auto_dicts import GEONODES, GEONODES_PROPS, SHADERNODES

# =============================================================================================================================
# Generate

def generate(folder):

    path = Path(folder) / "generated"
    gen = {}

    # ====================================================================================================
    # Loop on the tree types

    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:
        print("Generate for tree_type", tree_type)

        tree_name = 'GENERATE'
        tree = bpy.data.node_groups.get(tree_name)
        tree = bpy.data.node_groups.new(tree_name, type=tree_type)
        tree.nodes.clear()

        if tree_type == 'GeometryNodeTree':
            tree.is_modifier = True

            nodes  = GEONODES
            props  = GEONODES_PROPS
            static_nodes = 'nd'

        elif tree_type == 'ShaderNodeTree':

            nodes  = SHADERNODES
            props  = []

            static_nodes = 'snd'

        # ===== Nodes as methods

        for node_name, impls in nodes.items():

            tree.nodes.clear()
            node_info = NodeInfo(tree, node_name)

            for impl in impls:
                node_info.source_code(gen, **impl)

        # ===== Nodes as properties

        for prop in props:
            tree.nodes.clear()
            NodeInfo.property_code(tree, gen, **prop)

        # ===== Nodes as static classes

        NodeInfo.gen_static_nodes(gen, tree_type=tree_type, verbose=False)

    # ====================================================================================================
    # Loop on the tree types
    # Create the files

    print('='*100)

    imports = []
    for class_name, funcs in gen.items():

        print("Create file", class_name)
        if class_name in ['nd', 'snd']:
            module = f"static_{class_name}"
        else:
            module = class_name.lower()

        with open(path / f"{module}.py", 'w') as file:

            file.write("from .. socket_class import Socket\n")
            file.write("from .. treeclass import Node\n")
            file.write("from .. treeclass import utils\n")
            file.write("from .. scripterror import NodeError\n")
            file.write("\n")

            if class_name == 'gnmath':
                imports.append(f"from . import gnmath")

            elif class_name in ['nd', 'snd']:
                file.write(f"class {class_name}:\n\n")

                imports.append(f"from .{module} import {class_name}")

            else:
                file.write(f"class {class_name}(Socket):\n")
                file.write('    """"\n    $DOC SET hidden\n    """\n')

                imports.append(f"from .{module} import {class_name}")

            for name, code in funcs.items():
                file.write(code + "\n")

    # init file
    with open(path / "__init__.py", 'w') as file:
        file.write("\n".join(imports))

    print("Done")

# =============================================================================================================================
# Build the dictionnary of node name -> bl_idname

def build_implement_dict():
    """ Build the implementation dictionaries: node name -> list of dict

    - Copied the first time in gen_auto.py
    - Used to compare new version
    """

    def f(node_info, nodes):
        nodes[node_info.bnode.bl_idname] = node_info.bnode.name

    geo_nodes = {}
    snodes = {}

    for tree_type, nodes in [('GeometryNodeTree', geo_nodes), ('ShaderNodeTree', snodes)]:
        NodeInfo.loop(f, nodes, tree_type=tree_type)

    com_nodes = {}
    shd_nodes = {}
    for blid, node_name in snodes.items():
        if blid in geo_nodes:
            assert(node_name == geo_nodes[blid])
            com_nodes[blid] = node_name
        else:
            shd_nodes[blid] = node_name

    homos = []
    for blid, name in shd_nodes.items():
        for b, n in geo_nodes.items():
            if n == name:
                homos.append((name, b, blid))

    print(f"Geometry nodes: {len(geo_nodes)} nodes")
    print(f"Shader nodes  : {len(snodes)} nodes")
    print(f"Common nodes  : {len(com_nodes)} nodes")
    print(f"Shader only   : {len(shd_nodes)} nodes")
    print(f"Homonyms      : {len(homos)} nodes")
    for a, b, c in homos:
        print(f"{a:20s}: {b:30s} {c:30s}")

    # ===== Key words dict

    kws = {}
    for kw in dir(gen_auto_dicts):
        if kw.startswith('__'):
            continue
        s = getattr(gen_auto_dicts, kw)
        if not isinstance(s, str):
            continue
        kws[s] = kw

    def transco(dict_list):
        transcoded = []
        for d in dict_list:
            transcoded.append({kws.get(k, f'{k}'): v for k, v in d.items()})
        return transcoded

    # ===== Let's output

    print()
    print("="*80)
    print("Geometry Nodes and common to Shader")
    print()
    print("GEONODES = {")
    for name in geo_nodes.values():
        sname = f"'{name}'"
        print(f"{sname:28s}: ", end='')
        if False and name in GEONODES:
            item = transco(GEONODES[name])
            if True or len(item) == 1:
                print(str(item) + ',')
        else:
            print("[{}],")
    print("}")
    print()

    print("="*80)
    print("Shader Specific Nodes")
    print()
    print("SHADERNODES = {")
    for name in shd_nodes.values():
        sname = f"'{name}'"
        print(f"{sname:28s}:", "[{}],")
    print("}")
    print()
