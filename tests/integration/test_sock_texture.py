"""Tests for core/sock_texture.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_texture import Texture


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

class TestTextureImport:

    def test_importable(self):
        import core.sock_texture
        assert hasattr(core.sock_texture, 'Texture')

    def test_no_extra_imports(self):
        import core.sock_texture
        assert not hasattr(core.sock_texture, 'bpy')
        assert not hasattr(core.sock_texture, 'utils')
        assert not hasattr(core.sock_texture, 'Node')


# ---------------------------------------------------------------------------
# Texture factory methods — all return Color sockets

class TestTextureBrick:

    def test_brick_no_args(self):
        with Tree("_test_tex_brick", "GeometryNodeTree"):
            result = Texture.Brick()
            assert result is not None

    def test_brick_with_scale(self):
        with Tree("_test_tex_brick_sc", "GeometryNodeTree"):
            result = Texture.Brick(scale=5.0)
            assert result is not None


class TestTextureChecker:

    def test_checker_no_args(self):
        with Tree("_test_tex_checker", "GeometryNodeTree"):
            result = Texture.Checker()
            assert result is not None

    def test_checker_with_scale(self):
        with Tree("_test_tex_checker_sc", "GeometryNodeTree"):
            result = Texture.Checker(scale=2.0)
            assert result is not None


class TestTextureGabor:

    def test_gabor_no_args(self):
        with Tree("_test_tex_gabor", "GeometryNodeTree"):
            result = Texture.Gabor()
            assert result is not None


class TestTextureGradient:

    def test_gradient_no_args(self):
        with Tree("_test_tex_gradient", "GeometryNodeTree"):
            result = Texture.Gradient()
            assert result is not None


class TestTextureMagic:

    def test_magic_no_args(self):
        with Tree("_test_tex_magic", "GeometryNodeTree"):
            result = Texture.Magic()
            assert result is not None

    def test_magic_with_depth(self):
        with Tree("_test_tex_magic_d", "GeometryNodeTree"):
            result = Texture.Magic(turbulence_depth=3)
            assert result is not None


class TestTextureNoise:

    def test_noise_no_args(self):
        with Tree("_test_tex_noise", "GeometryNodeTree"):
            result = Texture.Noise()
            assert result is not None

    def test_noise_with_scale(self):
        with Tree("_test_tex_noise_sc", "GeometryNodeTree"):
            result = Texture.Noise(scale=3.0)
            assert result is not None


class TestTextureVoronoi:

    def test_voronoi_no_args(self):
        with Tree("_test_tex_voronoi", "GeometryNodeTree"):
            result = Texture.Voronoi()
            assert result is not None


class TestTextureWave:

    def test_wave_no_args(self):
        with Tree("_test_tex_wave", "GeometryNodeTree"):
            result = Texture.Wave()
            assert result is not None


class TestTextureWhiteNoise:

    def test_white_noise_no_args(self):
        with Tree("_test_tex_wn", "GeometryNodeTree"):
            result = Texture.WhiteNoise()
            assert result is not None
