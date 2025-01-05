""" Analyse the gaps between the current geonodes version and the last Blender version

- new nodes, types, socket types
- deprecated nodes
- diffrences
"""

import inspect
from pprint import pprint

import bpy
from .node_explore import NodeInfo
from ..core import constants
from ..core import utils

# =============================================================================================================================
# List of Sockets

def new_sockets():

    socket_types = set()

    def func(node_info):
        for socks in [node_info.bnode.inputs, node_info.bnode.inputs]:
            for sock in socks:
                socket_types.add(sock.type)

    print("::::: New sockets\n")
    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:

        socket_types.clear()
        NodeInfo.loop(func, tree_type=tree_type)

        print(f"{tree_type} ({len(socket_types)} sockets):")
        count = 0

        for socket_type in socket_types:
            if socket_type not in constants.VALID_SOCKET_TYPES[tree_type]:
                print("- ", socket_type)
                count += 1
        print(f"{count} found")
        print()

# =============================================================================================================================
# New Nodes

def new_nodes():

    nodes = {}

    def func(node_info):
        nodes[node_info.bnode.bl_idname] = node_info.bnode.name

    print("::::: New nodes\n")
    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:

        nodes.clear()
        NodeInfo.loop(func, tree_type=tree_type)

        print(f"{tree_type} ({len(nodes)} nodes):")
        count = 0

        for blid, name in nodes.items():
            if blid not in constants.NODE_NAMES[tree_type].values():
                print(f"- {blid:35s} : {name}")
                count += 1
        print(f"{count} found")
        print()

# =============================================================================================================================
# Deprecated Nodes

def deprecated_nodes():

    nodes = {}

    def func(node_info):
        nodes[node_info.bnode.bl_idname] = node_info.bnode.name

    print("::::: Deprecated nodes\n")
    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:

        nodes.clear()
        NodeInfo.loop(func, tree_type=tree_type)

        current = constants.NODE_NAMES[tree_type].values()

        print(f"{tree_type} (Blender: {len(nodes)} vs current: {len(current)} nodes):")
        count = 0

        for blid in current:
            if blid not in nodes:
                print(f"- {blid:35s}")
                count += 1
        print(f"{count} found")
        print()

# =============================================================================================================================
# Read the spec from static class

def get_static_method(tree_type, name):

    from geonodes import nd, snd

    module = nd if tree_type=='GeometryNodeTree' else snd

    method = getattr(module, name, None)
    if method is None:
        return None

    args = inspect.getfullargspec(method)


    if False:
        pprint(inspect.getsourcelines(method))

        lines = [line.strip() for line in inspect.getsourcelines(method)[0]]
        for line in lines:
            if line.startswith("node ="):
                print("> ", line)


    code = inspect.getsource(method)
    code = code.replace('node = Node', 'node = CAPTURE')
    code = "class Test:\n" + code + f"\n\nTest.{name}()\n"

    def CAPTURE(name, sockets={}, **kwargs):
        print("TOP")
        print(name)
        print(sockets)
        pprint(kwargs)

    print(code)

    exec(code, locals(), globals())

    print("INSPECT", inspect.signature(method))

# =============================================================================================================================
# Static classes

def node_changes():

    def func(node_info):
        sockets = node_info.get_sockets()
        params  = node_info.get_parameters()

        meth_name = utils.snake_case(node_info.bnode.name)
        print(node_info.bnode.name, meth_name)
        return



        print(node_info.bnode.name, node_info.signature('CLASS'))
        print(node_info.bnode.name, node_info.signature('METHOD'))

        if False:
            print('---', node_info.bnode.name)
            pprint(sockets)
            pprint(params)
            print()

    print("::::: Node changes\n")
    for tree_type in ['GeometryNodeTree', 'ShaderNodeTree']:

        NodeInfo.loop(func, tree_type=tree_type)
