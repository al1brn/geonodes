"""Tests for core/treearrange.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree as CoreTree
from core.geonodes import GeoNodes
import core.treearrange as ta


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture(autouse=True)
def clean_tree_stack():
    CoreTree.TREE_STACK.clear()
    yield
    CoreTree.TREE_STACK.clear()


@pytest.fixture(autouse=True)
def clean_test_groups():
    yield
    for name in list(bpy.data.node_groups.keys()):
        if name.startswith("_test_"):
            grp = bpy.data.node_groups.get(name)
            if grp is not None:
                bpy.data.node_groups.remove(grp)


# ---------------------------------------------------------------------------
# Import checks

class TestTreeArrangeImport:

    def test_importable(self):
        assert hasattr(ta, 'Tree')
        assert hasattr(ta, 'Node')
        assert hasattr(ta, 'Link')
        assert hasattr(ta, 'arrange')

    def test_no_vector_import(self):
        assert not hasattr(ta, 'Vector')

    def test_no_bool_property_import(self):
        assert not hasattr(ta, 'BoolProperty')

    def test_no_literal_import(self):
        assert not hasattr(ta, 'Literal')

    def test_no_list_import(self):
        assert not hasattr(ta, 'List')


# ---------------------------------------------------------------------------
# Tree wrapper creation

class TestTreeArrangeTreeCreation:

    def test_wrap_btree(self):
        with GeoNodes("_test_arr_basic") as tree:
            pass
        btree = bpy.data.node_groups.get("_test_arr_basic")
        assert btree is not None
        wrap = ta.Tree(btree)
        assert wrap is not None

    def test_wrap_by_name(self):
        with GeoNodes("_test_arr_name") as tree:
            pass
        wrap = ta.Tree("_test_arr_name")
        assert wrap is not None

    def test_nodes_dict(self):
        with GeoNodes("_test_arr_nodes") as tree:
            pass
        wrap = ta.Tree("_test_arr_nodes")
        assert isinstance(wrap.nodes, dict)

    def test_links_list(self):
        with GeoNodes("_test_arr_links") as tree:
            pass
        wrap = ta.Tree("_test_arr_links")
        assert isinstance(wrap.links, list)


# ---------------------------------------------------------------------------
# Node wrapper

class TestTreeArrangeNode:

    def test_node_name(self):
        with GeoNodes("_test_arr_nname") as tree:
            pass
        wrap = ta.Tree("_test_arr_nname")
        for node in wrap.nodes.values():
            assert isinstance(node.name, str)

    def test_node_is_frame(self):
        with GeoNodes("_test_arr_frame") as tree:
            pass
        wrap = ta.Tree("_test_arr_frame")
        for node in wrap.nodes.values():
            assert isinstance(node.is_frame, bool)

    def test_node_is_reroute(self):
        with GeoNodes("_test_arr_reroute") as tree:
            pass
        wrap = ta.Tree("_test_arr_reroute")
        for node in wrap.nodes.values():
            assert isinstance(node.is_reroute, bool)

    def test_node_counter_returns_int(self):
        with GeoNodes("_test_arr_counter") as tree:
            pass
        wrap = ta.Tree("_test_arr_counter")
        wrap.build_hierarchy()
        for node in wrap.nodes.values():
            assert isinstance(node.counter, int)

    def test_node_is_child_of_callable(self):
        with GeoNodes("_test_arr_childof") as tree:
            pass
        wrap = ta.Tree("_test_arr_childof")
        nodes = list(wrap.nodes.values())
        if len(nodes) >= 2:
            result = nodes[0].is_child_of(nodes[1])
            assert isinstance(result, bool)


# ---------------------------------------------------------------------------
# arrange() smoke test

class TestTreeArrangeArrange:

    def test_arrange_empty_tree(self):
        with GeoNodes("_test_arr_empty") as tree:
            pass
        ta.arrange(bpy.data.node_groups["_test_arr_empty"])

    def test_arrange_with_geometry(self):
        with GeoNodes("_test_arr_geo") as tree:
            geo = tree.geometry
            tree.geometry = geo
        ta.arrange(bpy.data.node_groups["_test_arr_geo"])

    def test_arrange_single_input(self):
        with GeoNodes("_test_arr_si") as tree:
            geo = tree.geometry
            tree.geometry = geo
        ta.arrange(bpy.data.node_groups["_test_arr_si"], single_input=True)

    def test_arrange_no_reroutes(self):
        with GeoNodes("_test_arr_nr") as tree:
            geo = tree.geometry
            tree.geometry = geo
        ta.arrange(bpy.data.node_groups["_test_arr_nr"], reroutes=False)


# ---------------------------------------------------------------------------
# build_hierarchy

class TestTreeArrangeBuildHierarchy:

    def test_build_hierarchy(self):
        with GeoNodes("_test_arr_hier") as tree:
            geo = tree.geometry
            tree.geometry = geo
        wrap = ta.Tree("_test_arr_hier")
        wrap.build_hierarchy()
        assert isinstance(wrap.children, list)

    def test_children_are_nodes(self):
        with GeoNodes("_test_arr_hier2") as tree:
            geo = tree.geometry
            tree.geometry = geo
        wrap = ta.Tree("_test_arr_hier2")
        wrap.build_hierarchy()
        for child in wrap.children:
            assert isinstance(child, ta.Node)
