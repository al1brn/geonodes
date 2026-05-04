"""Tests for core/sock_menu.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_menu import Menu


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

class TestMenuImport:

    def test_importable(self):
        import core.sock_menu
        assert hasattr(core.sock_menu, 'Menu')

    def test_no_literal_import(self):
        import core.sock_menu
        assert not hasattr(core.sock_menu, 'Literal')

    def test_no_nodeerror_import(self):
        import core.sock_menu
        assert not hasattr(core.sock_menu, 'NodeError')

    def test_no_utils_import(self):
        import core.sock_menu
        assert not hasattr(core.sock_menu, 'utils')

    def test_no_tree_import(self):
        import core.sock_menu
        assert not hasattr(core.sock_menu, 'Tree')

    def test_no_socket_import(self):
        import core.sock_menu
        assert not hasattr(core.sock_menu, 'Socket')

    def test_socket_type(self):
        assert Menu.SOCKET_TYPE == 'MENU'


# ---------------------------------------------------------------------------
# Menu creation

class TestMenuCreation:

    def test_menu_named_input(self):
        with Tree("_test_menu_named", "GeometryNodeTree"):
            m = Menu(name="My Menu")
            assert m is not None

    def test_menu_none_value(self):
        with Tree("_test_menu_none", "GeometryNodeTree"):
            m = Menu(None, name="My Menu")
            assert m is not None

    def test_menu_returns_menu_type(self):
        with Tree("_test_menu_type", "GeometryNodeTree"):
            m = Menu(name="My Menu")
            assert isinstance(m, Menu)


# ---------------------------------------------------------------------------
# enable_output method

class TestMenuEnableOutput:

    def test_enable_output_creates_node(self):
        with Tree("_test_menu_eo", "GeometryNodeTree"):
            m = Menu(name="My Menu")
            result = m.enable_output()
            assert result is not None

    def test_enable_output_returns_menu(self):
        with Tree("_test_menu_eo_type", "GeometryNodeTree"):
            m = Menu(name="My Menu")
            result = m.enable_output()
            assert isinstance(result, Menu)

    def test_enable_output_with_bool(self):
        from core.sock_boolean import Boolean
        with Tree("_test_menu_eo_bool", "GeometryNodeTree"):
            m = Menu(name="My Menu")
            b = Boolean(True)
            result = m.enable_output(enable=b)
            assert result is not None
