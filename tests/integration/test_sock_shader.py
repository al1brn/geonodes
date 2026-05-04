"""Tests for core/sock_shader.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_shader import Shader, VolumeShader, ShaderRoot


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

class TestShaderImport:

    def test_shader_importable(self):
        import core.sock_shader
        assert hasattr(core.sock_shader, 'Shader')

    def test_volumeshader_importable(self):
        import core.sock_shader
        assert hasattr(core.sock_shader, 'VolumeShader')

    def test_no_numpy_import(self):
        import core.sock_shader
        assert not hasattr(core.sock_shader, 'np')

    def test_no_bpy_import(self):
        import core.sock_shader
        assert not hasattr(core.sock_shader, 'bpy')

    def test_no_tree_import(self):
        import core.sock_shader
        assert not hasattr(core.sock_shader, 'Tree')

    def test_no_node_import(self):
        import core.sock_shader
        assert not hasattr(core.sock_shader, 'Node')

    def test_socket_type(self):
        assert Shader.SOCKET_TYPE == 'SHADER'


# ---------------------------------------------------------------------------
# Shader creation (requires ShaderNodeTree group)

class TestShaderCreation:

    def test_shader_named_input(self):
        with Tree("_test_shd_named", "ShaderNodeTree", is_group=True):
            s = Shader(name="My Shader")
            assert s is not None

    def test_shader_returns_shader_type(self):
        with Tree("_test_shd_type", "ShaderNodeTree", is_group=True):
            s = Shader(name="My Shader")
            assert isinstance(s, Shader)

    def test_shader_diffuse(self):
        with Tree("_test_shd_diffuse", "ShaderNodeTree"):
            s = Shader.Diffuse()
            assert s is not None

    def test_shader_emission(self):
        with Tree("_test_shd_emission", "ShaderNodeTree"):
            s = Shader.Emission()
            assert s is not None

    def test_shader_principled(self):
        with Tree("_test_shd_principled", "ShaderNodeTree"):
            s = Shader.Principled()
            assert s is not None

    def test_shader_transparent(self):
        with Tree("_test_shd_transp", "ShaderNodeTree"):
            s = Shader.Transparent()
            assert s is not None

    def test_shader_holdout(self):
        with Tree("_test_shd_holdout", "ShaderNodeTree"):
            s = Shader.Holdout()
            assert s is not None


# ---------------------------------------------------------------------------
# ShaderRoot operators

class TestShaderRootOperators:

    def test_add(self):
        with Tree("_test_shd_add", "ShaderNodeTree"):
            a = Shader.Diffuse()
            b = Shader.Emission()
            result = a + b
            assert result is not None

    def test_mul_shader(self):
        with Tree("_test_shd_mul", "ShaderNodeTree"):
            a = Shader.Diffuse()
            b = Shader.Transparent()
            result = a * b
            assert result is not None

    def test_mul_tuple_fac(self):
        """(shader, fac) tuple form → mix with factor."""
        with Tree("_test_shd_mul_tup", "ShaderNodeTree"):
            a = Shader.Diffuse()
            b = Shader.Transparent()
            result = a * (b, 0.5)
            assert result is not None


# ---------------------------------------------------------------------------
# Shader.out()

class TestShaderOut:

    def test_out_shader_group(self):
        with Tree("_test_shd_out_grp", "ShaderNodeTree", is_group=True):
            s = Shader(name="My Shader")
            s.out("MyShader")


# ---------------------------------------------------------------------------
# VolumeShader

class TestVolumeShader:

    def test_absorption(self):
        with Tree("_test_vol_abs", "ShaderNodeTree"):
            v = VolumeShader.Absorption()
            assert v is not None

    def test_scatter(self):
        with Tree("_test_vol_scat", "ShaderNodeTree"):
            v = VolumeShader.Scatter()
            assert v is not None

    def test_principled(self):
        with Tree("_test_vol_princ", "ShaderNodeTree"):
            v = VolumeShader.Principled()
            assert v is not None

    def test_out_volume_group(self):
        with Tree("_test_vol_out_grp", "ShaderNodeTree", is_group=True):
            v = VolumeShader.Absorption()
            v.out("MyVolume")
