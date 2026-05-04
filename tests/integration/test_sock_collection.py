"""Tests for core/sock_collection.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_collection import Collection


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

class TestCollectionImport:

    def test_importable(self):
        import core.sock_collection
        assert hasattr(core.sock_collection, 'Collection')

    def test_no_bpy_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'bpy')

    def test_no_constants_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'constants')

    def test_no_utils_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'utils')

    def test_no_tree_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'Tree')

    def test_no_node_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'Node')

    def test_no_socket_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'Socket')

    def test_no_blender_import(self):
        import core.sock_collection
        assert not hasattr(core.sock_collection, 'blender')

    def test_socket_type(self):
        assert Collection.SOCKET_TYPE == 'COLLECTION'


# ---------------------------------------------------------------------------
# Collection creation

class TestCollectionCreation:

    def test_collection_input_by_name(self):
        with Tree("_test_coll_name", "GeometryNodeTree"):
            c = Collection(name="My Collection")
            assert c is not None

    def test_collection_none_value(self):
        with Tree("_test_coll_none", "GeometryNodeTree"):
            c = Collection(None, name="My Collection")
            assert c is not None

    def test_collection_bpy_data(self):
        coll = bpy.data.collections.new("_test_coll_bpy")
        try:
            with Tree("_test_coll_bpy_ref", "GeometryNodeTree"):
                c = Collection(coll)
                assert c is not None
        finally:
            bpy.data.collections.remove(coll)

    def test_collection_returns_collection_type(self):
        with Tree("_test_coll_type", "GeometryNodeTree"):
            c = Collection(name="My Collection")
            assert isinstance(c, Collection)


# ---------------------------------------------------------------------------
# info method (from generated.Collection)

class TestCollectionInfo:

    def test_info_creates_node(self):
        with Tree("_test_coll_info", "GeometryNodeTree"):
            c = Collection(name="My Collection")
            result = c.info()
            assert result is not None

    def test_info_separate_children(self):
        with Tree("_test_coll_info_sep", "GeometryNodeTree"):
            c = Collection(name="My Collection")
            result = c.info(separate_children=True)
            assert result is not None

    def test_info_transform_space(self):
        with Tree("_test_coll_info_ts", "GeometryNodeTree"):
            c = Collection(name="My Collection")
            result = c.info(transform_space='RELATIVE')
            assert result is not None
