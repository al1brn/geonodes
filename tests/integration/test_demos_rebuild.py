"""Regression tests for reusable demo builders; requires Blender."""
from contextlib import contextmanager

import bpy

from geonodes.core.treeclass import Tree
from geonodes.demos import common, counters


@contextmanager
def cleanup_created_data():
    groups = set(bpy.data.node_groups.keys())
    materials = set(bpy.data.materials.keys())
    try:
        yield
    finally:
        for group in list(bpy.data.node_groups):
            if group.name not in groups:
                bpy.data.node_groups.remove(group)
        for material in list(bpy.data.materials):
            if material.name not in materials:
                bpy.data.materials.remove(material)


def snapshot():
    return {
        tree.name: (tuple(node.as_pointer() for node in tree.nodes),
                    tuple((item.identifier, item.name) for item in tree.interface.items_tree),
                    len(tree.links))
        for tree in bpy.data.node_groups
    }


def test_common_preserves_existing_and_rebuilds_missing():
    with cleanup_created_data():
        common.demo()
        before = snapshot()
        common.demo()
        assert snapshot() == before
        bpy.data.node_groups.remove(bpy.data.node_groups['Particles in a Box'])
        kept = snapshot()
        common.demo()
        assert 'Particles in a Box' in bpy.data.node_groups
        assert all(snapshot()[name] == value for name, value in kept.items())
        bpy.data.node_groups.remove(bpy.data.node_groups['.String to Curves'])
        common.demo()
        assert '.String to Curves' in bpy.data.node_groups
        assert not Tree.TREE_STACK
        tree = bpy.data.node_groups['.Vector Input']
        tree.nodes.new('NodeFrame').name = '_rebuild_sentinel'
        common.demo(rebuild=True)
        assert tree.nodes.get('_rebuild_sentinel') is None
        assert not Tree.TREE_STACK


def test_counters_creates_missing_groups_when_material_exists():
    with cleanup_created_data():
        counters.demo()
        before = snapshot()
        counters.demo()
        assert snapshot() == before
        material = bpy.data.materials['Box']
        material_nodes = tuple(node.as_pointer() for node in material.node_tree.nodes)
        bpy.data.node_groups.remove(bpy.data.node_groups['Rounded Box'])
        counters.demo()
        assert 'Rounded Box' in bpy.data.node_groups
        assert tuple(node.as_pointer() for node in material.node_tree.nodes) == material_nodes
        assert not Tree.TREE_STACK
