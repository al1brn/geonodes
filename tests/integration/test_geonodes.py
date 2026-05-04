"""Tests for core/geonodes.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.geonodes import GeoNodes


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture(autouse=True)
def clean_tree_stack():
    Tree.TREE_STACK.clear()
    yield
    Tree.TREE_STACK.clear()


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

class TestGeoNodesImport:

    def test_importable(self):
        import core.geonodes
        assert hasattr(core.geonodes, 'GeoNodes')

    def test_no_treeinterface_import(self):
        import core.geonodes
        assert not hasattr(core.geonodes, 'TreeInterface')

    def test_is_tree_subclass(self):
        assert issubclass(GeoNodes, Tree)


# ---------------------------------------------------------------------------
# GeoNodes creation

class TestGeoNodesCreation:

    def test_modifier_tree(self):
        with GeoNodes("_test_gn_mod") as tree:
            assert tree._btree.is_modifier is True

    def test_group_tree(self):
        with GeoNodes("_test_gn_grp", is_group=True) as tree:
            assert tree._btree.is_modifier is False

    def test_is_group_false_by_default(self):
        with GeoNodes("_test_gn_def") as tree:
            assert tree._is_group is False

    def test_is_group_true(self):
        with GeoNodes("_test_gn_isgrp", is_group=True) as tree:
            assert tree._is_group is True

    def test_tree_type(self):
        with GeoNodes("_test_gn_type") as tree:
            assert tree._btree.bl_idname == 'GeometryNodeTree'


# ---------------------------------------------------------------------------
# Tool

class TestGeoNodesTool:

    def test_tool_is_tool(self):
        with GeoNodes.Tool("_test_gn_tool") as tree:
            assert tree.is_tool is True

    def test_tool_object_mode(self):
        with GeoNodes.Tool("_test_gn_tool_om", object_mode=True) as tree:
            assert tree._btree.is_mode_object is True

    def test_tool_edit_mode(self):
        with GeoNodes.Tool("_test_gn_tool_em", edit_mode=True) as tree:
            assert tree._btree.is_mode_edit is True

    def test_tool_mesh_type(self):
        with GeoNodes.Tool("_test_gn_tool_mesh", mesh=True) as tree:
            assert tree._btree.is_type_mesh is True

    def test_modifier_is_not_tool(self):
        with GeoNodes("_test_gn_nottool") as tree:
            assert tree.is_tool is False


# ---------------------------------------------------------------------------
# Geometry I/O

class TestGeoNodesGeometry:

    def test_geometry_input(self):
        with GeoNodes("_test_gn_geoin") as tree:
            geo = tree.geometry
            assert geo is not None

    def test_geometry_output(self):
        with GeoNodes("_test_gn_geoout") as tree:
            geo = tree.geometry
            tree.geometry = geo

    def test_get_input_geometry_named(self):
        with GeoNodes("_test_gn_geoin_named") as tree:
            geo = tree.get_input_geometry(name="Geometry")
            assert geo is not None

    def test_set_output_geometry(self):
        with GeoNodes("_test_gn_geoset") as tree:
            geo = tree.geometry
            tree.set_output_geometry(geo)


# ---------------------------------------------------------------------------
# check_node_validity — tool vs modifier

class TestGeoNodesNodeValidity:

    def test_modifier_rejects_tool_only_nodes(self):
        from core.scripterror import NodeError
        from core import constants
        if not constants.TOOL_ONLY:
            pytest.skip("No TOOL_ONLY nodes defined")
        node_name = next(iter(constants.TOOL_ONLY))
        with pytest.raises(NodeError):
            with GeoNodes("_test_gn_toolonly") as tree:
                from core.nodeclass import Node
                Node(node_name)
