"""Tests for core/sock_color.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_color import Color


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

class TestColorImport:

    def test_importable(self):
        import core.sock_color
        assert hasattr(core.sock_color, 'Color')

    def test_no_literal_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'Literal')

    def test_no_colors_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'colors')

    def test_no_utils_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'utils')

    def test_no_sockettype_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'SocketType')

    def test_no_nodeerror_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'NodeError')

    def test_no_tree_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'Tree')

    def test_no_socket_import(self):
        import core.sock_color
        assert not hasattr(core.sock_color, 'Socket')

    def test_socket_type(self):
        assert Color.SOCKET_TYPE == 'RGBA'


# ---------------------------------------------------------------------------
# Color creation

class TestColorCreation:

    def test_color_default(self):
        with Tree("_test_col_default", "GeometryNodeTree"):
            c = Color()
            assert c is not None

    def test_color_from_tuple(self):
        with Tree("_test_col_tuple", "GeometryNodeTree"):
            c = Color((1.0, 0.0, 0.0))
            assert c is not None

    def test_color_from_rgba_tuple(self):
        with Tree("_test_col_rgba", "GeometryNodeTree"):
            c = Color((0.2, 0.4, 0.6, 1.0))
            assert c is not None

    def test_color_from_name_str(self):
        with Tree("_test_col_named", "GeometryNodeTree"):
            c = Color(name="My Color")
            assert c is not None

    def test_color_returns_color_type(self):
        with Tree("_test_col_type", "GeometryNodeTree"):
            c = Color()
            assert isinstance(c, Color)


# ---------------------------------------------------------------------------
# ColorRamp classmethod

class TestColorColorRamp:

    def test_colorramp_no_args(self):
        with Tree("_test_col_cr_noarg", "GeometryNodeTree"):
            result = Color.ColorRamp()
            assert result is not None

    def test_colorramp_with_fac(self):
        from core.sock_float import Float
        with Tree("_test_col_cr_fac", "GeometryNodeTree"):
            f = Float(0.5)
            result = Color.ColorRamp(fac=f)
            assert result is not None

    def test_colorramp_with_stops(self):
        with Tree("_test_col_cr_stops", "GeometryNodeTree"):
            result = Color.ColorRamp(stops=[(0.0, (1, 0, 0)), (1.0, (0, 0, 1))])
            assert result is not None

    def test_colorramp_returns_color(self):
        with Tree("_test_col_cr_type", "GeometryNodeTree"):
            result = Color.ColorRamp()
            assert isinstance(result, Color)


# ---------------------------------------------------------------------------
# curves method

class TestColorCurves:

    def test_curves_no_args(self):
        with Tree("_test_col_curves_noarg", "GeometryNodeTree"):
            c = Color()
            result = c.curves()
            assert result is not None

    def test_curves_with_points(self):
        with Tree("_test_col_curves_pts", "GeometryNodeTree"):
            c = Color()
            result = c.curves(curves=[[(0.0, 0.0), (1.0, 1.0)]])
            assert result is not None

    def test_curves_with_fac(self):
        from core.sock_float import Float
        with Tree("_test_col_curves_fac", "GeometryNodeTree"):
            c = Color()
            f = Float(0.5)
            result = c.curves(fac=f)
            assert result is not None


# ---------------------------------------------------------------------------
# Shader-specific methods (ShaderNodeTree)

class TestColorShaderMethods:

    def test_blackbody_creates_node(self):
        with Tree("_test_col_blackbody", "ShaderNodeTree"):
            result = Color.Blackbody()
            assert result is not None

    def test_wavelength_creates_node(self):
        with Tree("_test_col_wavelength", "ShaderNodeTree"):
            result = Color.Wavelength()
            assert result is not None

    def test_to_bw_creates_node(self):
        with Tree("_test_col_tobw", "ShaderNodeTree"):
            c = Color()
            result = c.to_bw
            assert result is not None

    def test_brightness_contrast(self):
        with Tree("_test_col_bc", "ShaderNodeTree"):
            c = Color()
            result = c.brightness_contrast()
            assert result is not None

    def test_gamma_creates_node(self):
        with Tree("_test_col_gamma", "ShaderNodeTree"):
            c = Color()
            result = c.gamma()
            assert result is not None

    def test_hue_saturation_value(self):
        with Tree("_test_col_hsv", "ShaderNodeTree"):
            c = Color()
            result = c.hue_saturation_value()
            assert result is not None

    def test_invert_creates_node(self):
        with Tree("_test_col_invert", "ShaderNodeTree"):
            c = Color()
            result = c.invert()
            assert result is not None

    def test_ambient_occlusion(self):
        with Tree("_test_col_ao", "ShaderNodeTree"):
            c = Color()
            result = c.ambient_occlusion()
            assert result is not None

    def test_color_attribute(self):
        with Tree("_test_col_attr", "ShaderNodeTree"):
            result = Color.Attribute("MyAttr")
            assert result is not None


# ---------------------------------------------------------------------------
# out() method — GeometryNodeTree (standard socket output)

class TestColorOut:

    def test_out_geometry_tree(self):
        with Tree("_test_col_out_geo", "GeometryNodeTree"):
            c = Color()
            c.out("MyColor")  # should create group output socket

    def test_out_shader_group(self):
        with Tree("_test_col_out_shgrp", "ShaderNodeTree", is_group=True):
            c = Color()
            c.out("MyColor")  # group shader: standard socket output
