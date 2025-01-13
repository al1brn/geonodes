from pathlib import Path
import bpy

from . node_explore import NodeInfo
from . import gen_auto_dicts
from . gen_auto_dicts import GEONODES, GEONODES_PROPS, SHADERNODES
from .. core import constants

from pprint import pprint, pformat

# =============================================================================================================================
# Build manual cross references

def build_manual_cross_ref(cross):

    def get_ni(name, tree_type):
        node_info = NodeInfo.Load(name, tree_type=tree_type)
        bl_idname = node_info.bnode.bl_idname
        cross[bl_idname] = {}

        return node_info, cross[bl_idname]

    # ----------------------------------------------------------------------------------------------------
    # Geometry nodes

    tree_type = 'GeometryNodeTree'

    # ----- Menu Switch

    node_info, node_cross = get_ni("Menu Switch", tree_type)
    signature = "(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None, panel=None, hide_value=False, hide_in_modifier=False, single_value=False)"
    node_cross['Socket'] = [
        {
        'func_name'         : 'MenuSwitch',
        'is_classmethod'    : True,
        'returns'           : 'OUT',
        'signature'         : signature,
        'sample_class'      : 'Geometry',
        }, {
        'func_name'         : 'menu_switch',
        'returns'           : 'OUT',
        'signature'         : signature,
        'sample_class'      : 'Geometry',
        }]

    # ----- Index Switch

    node_info, node_cross = get_ni("Index Switch", tree_type)
    signature = "(*values, index=0)"
    node_cross['Socket'] = [
        {
        'func_name'         : 'IndexSwitch',
        'is_classmethod'    : True,
        'returns'           : 'OUT',
        'signature'         : signature,
        'sample_class'      : 'Geometry',
        }, {
        'func_name'         : 'index_switch',
        'returns'           : 'OUT',
        'signature'         : signature,
        'sample_class'      : 'Geometry',
        }]

    # ----- Index Switch

    node_info, node_cross = get_ni("Switch", tree_type)
    node_cross['Socket'] = [
        {
        'func_name'         : 'Switch',
        'is_classmethod'    : True,
        'returns'           : 'OUT',
        'signature'         : "(condition=None, false=None, true=None)",
        'sample_class'      : 'Geometry',
        }, {
        'func_name'         : 'switch',
        'returns'           : 'OUT',
        'signature'         : "(condition=None, true=None)",
        'sample_class'      : 'Geometry',
        }]

    # ----- Capture attribute

    node_info, node_cross = get_ni("Capture Attribute", tree_type)
    signature = "(attribute=None, **attributes)"
    returns = "Node (if several arguments) or Socket (if only one argument)"
    node_cross['Domain'] = [
        {
        'func_name'         : 'capture_attribute',
        'returns'           : returns,
        'signature'         : signature,
        }, {
        'func_name'         : 'capture',
        'returns'           : returns,
        'signature'         : signature,
        }]

    # ----- Zones

    cross['GeometryNodeForeachGeometryElementInput'] = {'Domain': [{
        'help': "# Used in a 'with' context block, for instance:\n"
                "with Mesh.Cube().points.for_each(position=nd.position) as feel:\n\n"
                "    cube = Mesh.Cube(size=.1)\n"
                "    cube.transform(translation=feel.position)\n"
                "    feel.generated.geometry = cube\n\n"
                "feel.generated.geometry.out()\n"
    }]}
    cross['GeometryNodeForeachGeometryElementOutput'] = cross['GeometryNodeForeachGeometryElementInput']

    # ----- Repeat

    cross['GeometryNodeRepeatInput'] = {'Repeat': [{
        'help': "# Used in a 'with' context block, for instance:\n"
                "with Repeat(mesh=Mesh.Cube(size=2), z=1., size=1., iterations=7) as rep:\n\n"
                "    # join a smaller cube on top\n"
                "    small_cube = Mesh.Cube(size=rep.size).transform(translation=(0, 0, rep.z + rep.size/2))\n"
                "    rep.mesh += small_cube\n"
                "    # update loop parameters\n"
                "    rep.z += rep.size\n"
                "    rep.size /= 2\n\n"
                "rep.mesh.out()\n"
    }]}
    cross['GeometryNodeRepeatOutput'] = cross['GeometryNodeRepeatInput']

    # ----- Simulation

    cross['GeometryNodeSimulationInput'] = {'Simulation': [{
        'help': "# Used in a 'with' context block, for instance:\n"
                "with Simulation(mesh=Mesh.Cube(), speed=Vector.Random(-1, 1, seed=0)) as sim:\n\n"
                "    speed = sim.mesh.points.capture(sim.speed)\n"
                "    sim.mesh.position += speed*sim.delta_time\n"
                "    sim.speed = speed * .95\n\n"
                "sim.mesh.out()"
    }]}
    cross['GeometryNodeSimulationOutput'] = cross['GeometryNodeSimulationInput']

    # ----- Frame

    cross['NodeFrame'] = {'Layout': [{
        'help': "# Frames are created through a 'with' context block, for instance:\n"
                "with Layout(\"Nodes will be created in the frame\"):\n"
                "    a = Float(2)\n"
                "    b = Float(2)\n"
                "    c = a + b\n"
    }]}

    # ----- Group

    cross['GeometryNodeGroup'] = {'Group': [{
        'help': '# The first parameter is the name of an existing group:\n'
                '# Sockets can be set either by a dict or using keyword attributes\n\n'
                '# Let\'s create a sample group\n'
                'with GeoNodes("Sample Function"):\n\n'
                '    v = Float(0, "A Value")\n'
                '    i = Integer(1, "An Integer")\n'
                '    (v + i).out()\n\n'
                '# Let\'s call the function\n'
                'with GeoNodes("Calling the Function"):\n\n'
                '    v = Group("Sample Function", {"A Value": 123}, an_integer=99)\n'
    }]}
    cross['ShaderNodeGroup'] = cross['GeometryNodeGroup']


# =============================================================================================================================
# Generate

def generate(folder):

    path = Path(folder) / "generated"

    # ====================================================================================================
    # Gen collects generation
    #
    # gen['source'] : dict[class_name -> dict[function_name -> source_code]]
    # gen['cross']  : dict[bl_idname -> dict['class_name', 'func_name', 'signature', 'decorators']]

    gen = {'source': {}, 'cross': {}}

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
    for class_name, funcs in gen['source'].items():

        print("Create file", class_name)
        if class_name in ['nd', 'snd']:
            module = f"static_{class_name}"
        else:
            module = class_name.lower()

        with open(path / f"{module}.py", 'w') as file:

            file.write("from .. socket_class import Socket\n")
            file.write("from .. treeclass import Node, ColorRamp, NodeCurves\n")
            file.write("from .. treeclass import utils\n")
            file.write("from .. scripterror import NodeError\n")
            file.write("\n")

            if class_name == 'gnmath':
                imports.append(f"from . import gnmath")

            elif class_name in ['nd', 'snd']:
                file.write(f"class {class_name}:\n")
                file.write( '    """" Static class\n\n')
                file.write( "    Exposes all nodes as static methods:\n\n")
                file.write( "    ``` python\n")
                file.write(f"    a = {class_name}.math(1, 2, operation='ADD')\n")
                file.write( "    ```\n")
                file.write( '    """\n\n')


                imports.append(f"from .{module} import {class_name}")

            else:
                file.write(f"class {class_name}(Socket):\n")
                file.write('    """"\n    $DOC SET hidden\n    """\n')

                imports.append(f"from .{module} import {class_name}")

            for name, code in funcs.items():
                file.write(code + "\n")

    # Init file
    with open(path / "__init__.py", 'w') as file:
        file.write("\n".join(imports))

    # ----------------------------------------------------------------------------------------------------
    # Complete auto reference with manual implementation

    cross = gen['cross']

    build_manual_cross_ref(cross)

    # Cross reference
    with open(path / "cross_reference.py", 'w') as file:
        file.write("CROSS_REF = ")
        file.write(pformat(cross))


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
