"""Tests for core/sock_object.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_object import Object


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

class TestObjectImport:

    def test_importable(self):
        import core.sock_object
        assert hasattr(core.sock_object, 'Object')

    def test_no_bpy_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'bpy')

    def test_no_constants_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'constants')

    def test_no_utils_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'utils')

    def test_no_tree_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'Tree')

    def test_no_node_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'Node')

    def test_no_socket_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'Socket')

    def test_no_blender_import(self):
        import core.sock_object
        assert not hasattr(core.sock_object, 'blender')

    def test_socket_type(self):
        assert Object.SOCKET_TYPE == 'OBJECT'


# ---------------------------------------------------------------------------
# Object creation

class TestObjectCreation:

    def test_object_named_input(self):
        with Tree("_test_obj_named", "GeometryNodeTree"):
            o = Object(name="My Object")
            assert o is not None

    def test_object_none_value(self):
        with Tree("_test_obj_none", "GeometryNodeTree"):
            o = Object(None, name="My Object")
            assert o is not None

    def test_object_returns_object_type(self):
        with Tree("_test_obj_type", "GeometryNodeTree"):
            o = Object(name="My Object")
            assert isinstance(o, Object)

    def test_object_bpy_data(self):
        # Use the default scene camera or create a mesh object
        obj = bpy.data.objects.new("_test_obj_bpy", None)
        bpy.context.scene.collection.objects.link(obj)
        try:
            with Tree("_test_obj_bpyref", "GeometryNodeTree"):
                o = Object(obj, name="My Object")
                assert o is not None
        finally:
            bpy.data.objects.remove(obj)

    def test_self_constructor(self):
        with Tree("_test_obj_self", "GeometryNodeTree"):
            o = Object.Self()
            assert o is not None

    def test_active_camera_constructor(self):
        with Tree("_test_obj_cam", "GeometryNodeTree"):
            o = Object.ActiveCamera()
            assert o is not None


# ---------------------------------------------------------------------------
# info method

class TestObjectInfo:

    def test_info_creates_node(self):
        with Tree("_test_obj_info", "GeometryNodeTree"):
            o = Object(name="My Object")
            result = o.info()
            assert result is not None

    def test_info_transform_space(self):
        with Tree("_test_obj_info_ts", "GeometryNodeTree"):
            o = Object(name="My Object")
            result = o.info(transform_space='RELATIVE')
            assert result is not None

    def test_camera_info_creates_node(self):
        with Tree("_test_obj_caminfo", "GeometryNodeTree"):
            o = Object(name="My Object")
            result = o.camera_info()
            assert result is not None


# ---------------------------------------------------------------------------
# enable_output method

class TestObjectEnableOutput:

    def test_enable_output_creates_node(self):
        with Tree("_test_obj_eo", "GeometryNodeTree"):
            o = Object(name="My Object")
            result = o.enable_output()
            assert result is not None

    def test_enable_output_returns_object(self):
        with Tree("_test_obj_eo_type", "GeometryNodeTree"):
            o = Object(name="My Object")
            result = o.enable_output()
            assert isinstance(result, Object)
