"""Tests for core/sock_image.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_image import Image


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

class TestImageImport:

    def test_importable(self):
        import core.sock_image
        assert hasattr(core.sock_image, 'Image')

    def test_no_bpy_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'bpy')

    def test_no_constants_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'constants')

    def test_no_utils_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'utils')

    def test_no_tree_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'Tree')

    def test_no_node_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'Node')

    def test_no_socket_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'Socket')

    def test_no_blender_import(self):
        import core.sock_image
        assert not hasattr(core.sock_image, 'blender')

    def test_socket_type(self):
        assert Image.SOCKET_TYPE == 'IMAGE'


# ---------------------------------------------------------------------------
# Image creation

class TestImageCreation:

    def test_image_named_input(self):
        with Tree("_test_img_named", "GeometryNodeTree"):
            img = Image(name="My Image")
            assert img is not None

    def test_image_none_value(self):
        with Tree("_test_img_none", "GeometryNodeTree"):
            img = Image(None, name="My Image")
            assert img is not None

    def test_image_returns_image_type(self):
        with Tree("_test_img_type", "GeometryNodeTree"):
            img = Image(name="My Image")
            assert isinstance(img, Image)

    def test_image_bpy_data(self):
        bimg = bpy.data.images.new("_test_img_bpy", 4, 4)
        try:
            with Tree("_test_img_bpyref", "GeometryNodeTree"):
                img = Image(bimg, name="My Image")
                assert img is not None
        finally:
            bpy.data.images.remove(bimg)


# ---------------------------------------------------------------------------
# info method

class TestImageInfo:

    def test_info_creates_node(self):
        with Tree("_test_img_info", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.info()
            assert result is not None

    def test_width_creates_node(self):
        with Tree("_test_img_width", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.width()
            assert result is not None

    def test_height_creates_node(self):
        with Tree("_test_img_height", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.height()
            assert result is not None

    def test_has_alpha_creates_node(self):
        with Tree("_test_img_alpha", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.has_alpha()
            assert result is not None

    def test_frame_count_creates_node(self):
        with Tree("_test_img_fc", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.frame_count()
            assert result is not None

    def test_fps_creates_node(self):
        with Tree("_test_img_fps", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.fps()
            assert result is not None


# ---------------------------------------------------------------------------
# image_texture method

class TestImageTexture:

    def test_image_texture_creates_node(self):
        with Tree("_test_img_tex", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.image_texture()
            assert result is not None

    def test_image_texture_with_extension(self):
        with Tree("_test_img_tex_ext", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.image_texture(extension='EXTEND')
            assert result is not None

    def test_image_texture_with_interpolation(self):
        with Tree("_test_img_tex_interp", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.image_texture(interpolation='Closest')
            assert result is not None


# ---------------------------------------------------------------------------
# enable_output method

class TestImageEnableOutput:

    def test_enable_output_creates_node(self):
        with Tree("_test_img_eo", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.enable_output()
            assert result is not None

    def test_enable_output_returns_image(self):
        with Tree("_test_img_eo_type", "GeometryNodeTree"):
            img = Image(name="My Image")
            result = img.enable_output()
            assert isinstance(result, Image)
