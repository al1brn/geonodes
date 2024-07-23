# Explore nodes

from pprint import pprint

import geonodes as gn
from geonodes.nodes import constants
from geonodes.nodes import utils
from geonodes.nodes import treestack
from geonodes.nodes import nodeinfo

def node_detail(bl_idname):

    btree = treestack.get_tree("Explore", tree_type='GeometryNodeTree', create=True, clear=True)
    bnode = btree.nodes.new(bl_idname)
    node_info = nodeinfo.NodeInfo(btree, bnode)

    print('-'*100)
    print("Node detail")
    print()
    #print(repr(node_info))

    print("bl_idname  :", bl_idname)
    print("class_name :", node_info.class_name)
    print("parameters :", node_info.params)
    pprint(node_info.prm_defs)
    print()
    print("Input sockets :", node_info.inputs)
    print("Output sockets:", node_info.outputs)


    return node_info

def undocumented():
    with gn.GeoNodes("Explore") as tree:
        pass

    print("="*100)
    print("Undocumented nodes")
    print()
    for k, v in constants.NON_DOCUMENTED_NODES.items():
        if k in constants.DEPRECATED:
            continue
        print(f"{k:35s} : {v}")
    print()

def create_undocumented():
    print("with gn.GeoNodes(\"Undocumented\") as tree:")
    for k, v in constants.NON_DOCUMENTED_NODES.items():
        if k in constants.DEPRECATED:
            continue
        name = v.split("(")[0].strip()
        print(f"    tree.{name}()")
    print()
