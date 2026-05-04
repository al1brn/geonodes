"""Tests for core/blender.py — requires Blender."""
import pytest
import bpy
from pathlib import Path

from core.blender import (
    create_object,
    get_resource,
    get_font,
    get_resource_path,
    load_node_group,
)


# ---------------------------------------------------------------------------
# Helpers

@pytest.fixture(autouse=True)
def clean_test_objects():
    """Supprime les objets et leurs data blocks orphelins après chaque test."""
    yield
    for name in list(bpy.data.objects.keys()):
        if name.startswith("_test_"):
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.curves, bpy.data.pointclouds):
        for block in list(coll):
            if block.users == 0 and block.name.startswith("_test_"):
                coll.remove(block)


# ---------------------------------------------------------------------------
# create_object

class TestCreateObject:

    def test_creates_mesh_object(self):
        obj = create_object("_test_mesh")
        assert obj is not None
        assert obj.name == "_test_mesh"
        assert obj.type == "MESH"

    def test_creates_empty_object(self):
        obj = create_object("_test_empty", type="EMPTY")
        assert obj is not None
        assert obj.type == "EMPTY"

    def test_creates_curve_object(self):
        obj = create_object("_test_curve", type="CURVE")
        assert obj is not None
        assert obj.type == "CURVE"

    def test_idempotent_returns_existing(self):
        obj1 = create_object("_test_idem")
        obj2 = create_object("_test_idem")
        assert obj1 is obj2

    def test_object_linked_to_scene(self):
        obj = create_object("_test_linked")
        assert obj.name in bpy.context.collection.objects

    def test_unknown_type_raises(self):
        with pytest.raises(ValueError, match="unsupported type"):
            create_object("_test_badtype", type="ARMATURE")

    def test_curve_datablock_name_matches(self):
        obj = create_object("_test_curve_name", type="CURVE")
        assert obj.data.name == "_test_curve_name"


# ---------------------------------------------------------------------------
# get_resource

class TestGetResource:

    def test_none_returns_none(self):
        for socket_type in ["OBJECT", "COLLECTION", "IMAGE", "MATERIAL"]:
            assert get_resource(socket_type, None) is None

    def test_object_instance_passthrough(self):
        obj = create_object("_test_passthrough")
        result = get_resource("OBJECT", obj)
        assert result is obj

    def test_object_by_name(self):
        obj = create_object("_test_byname")
        result = get_resource("OBJECT", "_test_byname")
        assert result is obj

    def test_unknown_name_returns_none(self):
        result = get_resource("OBJECT", "_test_does_not_exist_xyz")
        assert result is None


# ---------------------------------------------------------------------------
# get_font

class TestGetFont:

    def test_none_returns_builtin_font(self):
        font = get_font(None)
        assert font is not None
        assert isinstance(font, bpy.types.VectorFont)

    def test_vectorfont_instance_passthrough(self):
        font = get_font(None)  # obtenir un vrai VectorFont
        result = get_font(font)
        assert result is font

    def test_unknown_name_falls_back_to_builtin(self):
        font = get_font("_font_inexistant_xyz")
        assert font is not None
        assert isinstance(font, bpy.types.VectorFont)


# ---------------------------------------------------------------------------
# get_resource_path

class TestGetResourcePath:

    @pytest.mark.parametrize("name", ["DATAFILES", "SCRIPTS", "PYTHON"])
    def test_returns_existing_path(self, name):
        path = get_resource_path(name)
        assert isinstance(path, Path)
        assert path.is_dir()


# ---------------------------------------------------------------------------
# load_node_group

class TestLoadNodeGroup:

    def test_none_returns_none(self):
        assert load_node_group(None) is None

    def test_empty_dict_returns_none(self):
        assert load_node_group({}) is None
