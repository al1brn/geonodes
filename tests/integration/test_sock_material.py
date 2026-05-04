"""Tests for core/sock_material.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_material import Material


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

class TestMaterialImport:

    def test_importable(self):
        import core.sock_material
        assert hasattr(core.sock_material, 'Material')

    def test_no_bpy_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'bpy')

    def test_no_constants_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'constants')

    def test_no_utils_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'utils')

    def test_no_tree_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'Tree')

    def test_no_node_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'Node')

    def test_no_socket_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'Socket')

    def test_no_blender_import(self):
        import core.sock_material
        assert not hasattr(core.sock_material, 'blender')

    def test_socket_type(self):
        assert Material.SOCKET_TYPE == 'MATERIAL'


# ---------------------------------------------------------------------------
# Material creation

class TestMaterialCreation:

    def test_material_named_input(self):
        with Tree("_test_mat_named", "GeometryNodeTree"):
            m = Material(name="My Material")
            assert m is not None

    def test_material_none_value(self):
        with Tree("_test_mat_none", "GeometryNodeTree"):
            m = Material(None, name="My Material")
            assert m is not None

    def test_material_returns_material_type(self):
        with Tree("_test_mat_type", "GeometryNodeTree"):
            m = Material(name="My Material")
            assert isinstance(m, Material)

    def test_material_bpy_data(self):
        mat = bpy.data.materials.new("_test_mat_bpy")
        try:
            with Tree("_test_mat_bpyref", "GeometryNodeTree"):
                m = Material(mat, name="My Material")
                assert m is not None
        finally:
            bpy.data.materials.remove(mat)


# ---------------------------------------------------------------------------
# enable_output method

class TestMaterialEnableOutput:

    def test_enable_output_creates_node(self):
        with Tree("_test_mat_eo", "GeometryNodeTree"):
            m = Material(name="My Material")
            result = m.enable_output()
            assert result is not None

    def test_enable_output_returns_material(self):
        with Tree("_test_mat_eo_type", "GeometryNodeTree"):
            m = Material(name="My Material")
            result = m.enable_output()
            assert isinstance(result, Material)

    def test_enable_output_with_bool(self):
        from core.sock_boolean import Boolean
        with Tree("_test_mat_eo_bool", "GeometryNodeTree"):
            m = Material(name="My Material")
            b = Boolean(True)
            result = m.enable_output(enable=b)
            assert result is not None
