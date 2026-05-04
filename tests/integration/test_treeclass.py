"""Tests for core/treeclass.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree, Layout, Panel


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture(autouse=True)
def clean_tree_stack():
    """Ensure tree stack is empty before and after each test."""
    Tree.TREE_STACK.clear()
    yield
    Tree.TREE_STACK.clear()


@pytest.fixture(autouse=True)
def clean_test_groups():
    """Remove node groups created during tests."""
    yield
    for name in list(bpy.data.node_groups.keys()):
        if name.startswith("_test_"):
            grp = bpy.data.node_groups.get(name)
            if grp is not None:
                bpy.data.node_groups.remove(grp)
    for mat in list(bpy.data.materials.keys()):
        if mat.startswith("_test_"):
            m = bpy.data.materials.get(mat)
            if m is not None:
                bpy.data.materials.remove(m)


# ---------------------------------------------------------------------------
# Tree stack

class TestTreeStack:

    def test_current_tree_none_when_empty(self):
        assert Tree.current_tree() is None

    def test_push_makes_current(self):
        with Tree("_test_stack_push", "GeometryNodeTree") as tree:
            assert Tree.current_tree() is tree

    def test_pop_restores_stack(self):
        with Tree("_test_stack_pop", "GeometryNodeTree"):
            pass
        assert Tree.current_tree() is None

    def test_nested_trees_stack_order(self):
        with Tree("_test_outer", "GeometryNodeTree") as outer:
            with Tree("_test_inner", "GeometryNodeTree") as inner:
                assert Tree.current_tree() is inner
            assert Tree.current_tree() is outer

    def test_tree_stack_len_while_open(self):
        with Tree("_test_stack_len", "GeometryNodeTree"):
            assert len(Tree.TREE_STACK) == 1


# ---------------------------------------------------------------------------
# _has_tree

class TestHasTree:

    def test_geonodes_has_tree_true(self):
        with Tree("_test_hastree_geo", "GeometryNodeTree") as tree:
            assert tree._has_tree is True

    def test_shader_group_has_tree_true(self):
        with Tree("_test_hastree_shader_grp", "ShaderNodeTree", is_group=True) as tree:
            assert tree._has_tree is True

    def test_shader_non_group_has_tree_false(self):
        with Tree("_test_hastree_shader_nogrp", "ShaderNodeTree", is_group=False) as tree:
            assert tree._has_tree is False

    def test_has_tree_returns_bool_not_none(self):
        with Tree("_test_hastree_none", "GeometryNodeTree") as tree:
            result = tree._has_tree
            assert result is not None


# ---------------------------------------------------------------------------
# Tree creation

class TestTreeCreation:

    def test_tree_creates_btree(self):
        with Tree("_test_create", "GeometryNodeTree") as tree:
            assert tree._btree is not None

    def test_tree_name_in_node_groups(self):
        with Tree("_test_name", "GeometryNodeTree"):
            assert bpy.data.node_groups.get("_test_name") is not None

    def test_tree_with_prefix(self):
        with Tree("_test_prefix_name", "GeometryNodeTree", prefix="_pfx") as tree:
            assert tree._btree.name == "_pfx _test_prefix_name"

    def test_tree_fake_user(self):
        with Tree("_test_fakeuser", "GeometryNodeTree", fake_user=True) as tree:
            assert tree._btree.use_fake_user is True

    def test_tree_nodes_dict_is_dict(self):
        with Tree("_test_nodes_dict", "GeometryNodeTree") as tree:
            assert isinstance(tree._nodes, dict)

    def test_tree_layouts_empty_on_start(self):
        with Tree("_test_layouts", "GeometryNodeTree") as tree:
            assert tree._layouts == []


# ---------------------------------------------------------------------------
# Layout

class TestLayout:

    def test_layout_context_push_pop(self):
        with Tree("_test_layout_ctx", "GeometryNodeTree") as tree:
            with Layout("My Layout") as layout:
                assert layout in tree._layouts
            assert layout not in tree._layouts

    def test_layout_title(self):
        with Tree("_test_layout_title", "GeometryNodeTree"):
            with Layout("TitleTest") as layout:
                assert layout.title == "TitleTest"

    def test_layout_transparent_when_none_title(self):
        with Tree("_test_layout_transparent", "GeometryNodeTree"):
            with Layout(None) as layout:
                assert layout.transparent is True

    def test_layout_not_transparent_with_title(self):
        with Tree("_test_layout_not_transparent", "GeometryNodeTree"):
            with Layout("Some Title") as layout:
                assert layout.transparent is False

    def test_nested_layouts(self):
        with Tree("_test_layout_nested", "GeometryNodeTree") as tree:
            with Layout("Outer") as outer:
                with Layout("Inner") as inner:
                    assert len(tree._layouts) == 2
                assert len(tree._layouts) == 1

    def test_layout_bnode_created(self):
        with Tree("_test_layout_bnode", "GeometryNodeTree"):
            with Layout("Frame") as layout:
                assert layout.bnode is not None
                assert layout.bnode.bl_idname == 'NodeFrame'


# ---------------------------------------------------------------------------
# Panel path management

class TestTreePanels:

    def test_get_panel_default_root(self):
        with Tree("_test_panel_root", "GeometryNodeTree") as tree:
            path = tree.get_panel("")
            assert path.is_root

    def test_push_pop_panel(self):
        with Tree("_test_panel_pushpop", "GeometryNodeTree") as tree:
            from core.treeinterface import ItemPath
            tree.push_panel(ItemPath("MyPanel"))
            assert not tree._panels[-1].is_root
            tree.pop_panel()
            assert tree._panels[-1].is_root

    def test_panel_stack_has_root_at_start(self):
        with Tree("_test_panel_stack", "GeometryNodeTree") as tree:
            assert len(tree._panels) == 1
            assert tree._panels[0].is_root


# ---------------------------------------------------------------------------
# Tree.clear

class TestTreeClear:

    def test_clear_no_keep(self):
        with Tree("_test_clear_no_keep", "GeometryNodeTree") as tree:
            tree.clear(keep_nodes=False)
            assert len(tree._btree.nodes) == 0
            assert len(tree._btree.links) == 0

    def test_nodes_dict_cleared(self):
        with Tree("_test_clear_nodes_dict", "GeometryNodeTree") as tree:
            tree.clear(keep_nodes=False)
            assert len(tree._nodes) == 0


# ---------------------------------------------------------------------------
# Tree.is_geonodes / is_shader

class TestTreeTypeDetection:

    def test_is_geonodes_true_for_geo_tree(self):
        with Tree("_test_type_geo", "GeometryNodeTree") as tree:
            assert Tree.is_geonodes() is True
            assert Tree.is_shader() is False

    def test_is_shader_true_for_shader_group(self):
        with Tree("_test_type_shader", "ShaderNodeTree", is_group=True) as tree:
            assert Tree.is_shader() is True
            assert Tree.is_geonodes() is False
