"""Tests for core/sock_font.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_font import Font


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

class TestFontImport:

    def test_importable(self):
        import core.sock_font
        assert hasattr(core.sock_font, 'Font')

    def test_no_bpy_import(self):
        import core.sock_font
        assert not hasattr(core.sock_font, 'bpy')

    def test_no_utils_import(self):
        import core.sock_font
        assert not hasattr(core.sock_font, 'utils')

    def test_no_tree_import(self):
        import core.sock_font
        assert not hasattr(core.sock_font, 'Tree')

    def test_no_socket_import(self):
        import core.sock_font
        assert not hasattr(core.sock_font, 'Socket')

    def test_no_node_import(self):
        import core.sock_font
        assert not hasattr(core.sock_font, 'Node')

    def test_socket_type(self):
        assert Font.SOCKET_TYPE == 'FONT'


# ---------------------------------------------------------------------------
# Font creation

class TestFontCreation:

    def test_font_named_input(self):
        with Tree("_test_font_named", "GeometryNodeTree"):
            f = Font(None, name="My Font")
            assert f is not None

    def test_font_none_value(self):
        with Tree("_test_font_none", "GeometryNodeTree"):
            f = Font(None, name="My Font")
            assert f is not None

    def test_font_returns_font_type(self):
        with Tree("_test_font_type", "GeometryNodeTree"):
            f = Font(None, name="My Font")
            assert isinstance(f, Font)

    def test_font_bpy_data(self):
        # Blender always has at least the built-in font
        bfont = bpy.data.fonts[0]
        with Tree("_test_font_bpy", "GeometryNodeTree"):
            f = Font(bfont, name="My Font")
            assert f is not None

    def test_font_default_name(self):
        with Tree("_test_font_defname", "GeometryNodeTree"):
            f = Font(None, name="Font")
            assert isinstance(f, Font)


# ---------------------------------------------------------------------------
# enable_output method

class TestFontEnableOutput:

    def test_enable_output_creates_node(self):
        with Tree("_test_font_eo", "GeometryNodeTree"):
            f = Font(None, name="My Font")
            result = f.enable_output()
            assert result is not None

    def test_enable_output_returns_font(self):
        with Tree("_test_font_eo_type", "GeometryNodeTree"):
            f = Font(None, name="My Font")
            result = f.enable_output()
            assert isinstance(result, Font)

    def test_enable_output_with_bool(self):
        from core.sock_boolean import Boolean
        with Tree("_test_font_eo_bool", "GeometryNodeTree"):
            f = Font(None, name="My Font")
            b = Boolean(True)
            result = f.enable_output(enable=b)
            assert result is not None
