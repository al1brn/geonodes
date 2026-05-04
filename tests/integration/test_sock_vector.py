"""Tests for core/sock_vector.py — requires Blender."""
import pytest
import math
import bpy

from core.treeclass import Tree
from core.sock_vector import Vector


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

class TestVectorImport:

    def test_importable(self):
        import core.sock_vector
        assert hasattr(core.sock_vector, 'Vector')

    def test_no_version_import(self):
        import core.sock_vector
        assert not hasattr(core.sock_vector, 'version')

    def test_no_numpy_import(self):
        import core.sock_vector
        assert not hasattr(core.sock_vector, 'np')

    def test_no_literal_import(self):
        import core.sock_vector
        assert not hasattr(core.sock_vector, 'Literal')

    def test_no_bpy_import(self):
        import core.sock_vector
        assert not hasattr(core.sock_vector, 'bpy')

    def test_no_tree_import(self):
        import core.sock_vector
        assert not hasattr(core.sock_vector, 'Tree')

    def test_no_socket_import(self):
        import core.sock_vector
        assert not hasattr(core.sock_vector, 'Socket')

    def test_socket_type(self):
        assert Vector.SOCKET_TYPE == 'VECTOR'


# ---------------------------------------------------------------------------
# Vector creation

class TestVectorCreation:

    def test_vector_default(self):
        with Tree("_test_vec_default", "GeometryNodeTree"):
            v = Vector()
            assert v is not None

    def test_vector_from_tuple(self):
        with Tree("_test_vec_tuple", "GeometryNodeTree"):
            v = Vector((1.0, 2.0, 3.0))
            assert v is not None

    def test_vector_named_input(self):
        with Tree("_test_vec_named", "GeometryNodeTree"):
            v = Vector(name="My Vector")
            assert v is not None

    def test_vector_returns_vector_type(self):
        with Tree("_test_vec_type", "GeometryNodeTree"):
            v = Vector()
            assert isinstance(v, Vector)

    def test_from_rotation(self):
        from core.sock_rotation import Rotation
        with Tree("_test_vec_fromrot", "GeometryNodeTree"):
            r = Rotation()
            result = Vector.FromRotation(r)
            assert result is not None

    def test_combine_xyz(self):
        with Tree("_test_vec_cxyz", "GeometryNodeTree"):
            result = Vector.CombineXYZ(x=1.0, y=2.0, z=3.0)
            assert result is not None


# ---------------------------------------------------------------------------
# Arithmetic operators

class TestVectorArith:

    def test_neg(self):
        with Tree("_test_vec_neg", "GeometryNodeTree"):
            result = -Vector((1, 2, 3))
            assert result is not None

    def test_abs_bug_fix(self):
        """Regression: __abs__ returned self.abs (bound method) instead of self.abs()."""
        with Tree("_test_vec_abs", "GeometryNodeTree"):
            result = abs(Vector((-1, -2, -3)))
            assert isinstance(result, Vector)

    def test_add(self):
        with Tree("_test_vec_add", "GeometryNodeTree"):
            result = Vector((1, 0, 0)) + Vector((0, 1, 0))
            assert result is not None

    def test_radd(self):
        with Tree("_test_vec_radd", "GeometryNodeTree"):
            result = (1, 0, 0) + Vector((0, 1, 0))
            assert result is not None

    def test_iadd(self):
        with Tree("_test_vec_iadd", "GeometryNodeTree"):
            v = Vector((1, 0, 0))
            v += Vector((0, 1, 0))
            assert v is not None

    def test_sub(self):
        with Tree("_test_vec_sub", "GeometryNodeTree"):
            result = Vector((1, 2, 3)) - Vector((1, 1, 1))
            assert result is not None

    def test_rsub(self):
        with Tree("_test_vec_rsub", "GeometryNodeTree"):
            result = (2, 3, 4) - Vector((1, 1, 1))
            assert result is not None

    def test_mul_scalar(self):
        with Tree("_test_vec_mul_s", "GeometryNodeTree"):
            result = Vector((1, 2, 3)) * 2.0
            assert result is not None

    def test_mul_vector(self):
        with Tree("_test_vec_mul_v", "GeometryNodeTree"):
            result = Vector((1, 2, 3)) * Vector((2, 2, 2))
            assert result is not None

    def test_rmul_scalar(self):
        with Tree("_test_vec_rmul_s", "GeometryNodeTree"):
            result = 2.0 * Vector((1, 2, 3))
            assert result is not None

    def test_truediv_scalar(self):
        with Tree("_test_vec_div_s", "GeometryNodeTree"):
            result = Vector((2, 4, 6)) / 2.0
            assert result is not None

    def test_truediv_vector(self):
        with Tree("_test_vec_div_v", "GeometryNodeTree"):
            result = Vector((2, 4, 6)) / Vector((1, 2, 3))
            assert result is not None

    def test_rtruediv(self):
        with Tree("_test_vec_rdiv", "GeometryNodeTree"):
            result = (2, 4, 6) / Vector((1, 2, 3))
            assert result is not None

    def test_mod(self):
        with Tree("_test_vec_mod", "GeometryNodeTree"):
            result = Vector((5, 7, 9)) % Vector((3, 3, 3))
            assert result is not None

    def test_matmul_dot(self):
        with Tree("_test_vec_mm_dot", "GeometryNodeTree"):
            result = Vector((1, 0, 0)) @ Vector((0, 1, 0))
            assert result is not None

    def test_pow_cross(self):
        with Tree("_test_vec_pow", "GeometryNodeTree"):
            result = Vector((1, 0, 0)) ** Vector((0, 1, 0))
            assert result is not None


# ---------------------------------------------------------------------------
# Rounding operators — bug fixes

class TestVectorRounding:

    def test_floor_bug_fix(self):
        """Regression: __floor__ returned self.floor (bound method) instead of self.floor()."""
        with Tree("_test_vec_floor", "GeometryNodeTree"):
            result = math.floor(Vector((1.7, 2.9, 3.1)))
            assert isinstance(result, Vector)

    def test_ceil_bug_fix(self):
        """Regression: __ceil__ returned self.ceil (bound method) instead of self.ceil()."""
        with Tree("_test_vec_ceil", "GeometryNodeTree"):
            result = math.ceil(Vector((1.2, 2.4, 3.6)))
            assert isinstance(result, Vector)


# ---------------------------------------------------------------------------
# mix and curves

class TestVectorMixCurves:

    def test_mix_uniform(self):
        with Tree("_test_vec_mix_u", "GeometryNodeTree"):
            a = Vector((1, 0, 0))
            b = Vector((0, 1, 0))
            result = a.mix(b, factor=0.5)
            assert result is not None

    def test_mix_non_uniform(self):
        with Tree("_test_vec_mix_nu", "GeometryNodeTree"):
            a = Vector((1, 0, 0))
            b = Vector((0, 1, 0))
            result = a.mix(b, factor=(0.5, 0.5, 0.5))
            assert result is not None

    def test_curves(self):
        with Tree("_test_vec_curves", "GeometryNodeTree"):
            v = Vector()
            result = v.curves()
            assert result is not None


# ---------------------------------------------------------------------------
# Component access

class TestVectorComponents:

    def test_x_component(self):
        with Tree("_test_vec_x", "GeometryNodeTree"):
            v = Vector((1, 2, 3))
            result = v.x
            assert result is not None

    def test_y_component(self):
        with Tree("_test_vec_y", "GeometryNodeTree"):
            v = Vector((1, 2, 3))
            result = v.y
            assert result is not None

    def test_z_component(self):
        with Tree("_test_vec_z", "GeometryNodeTree"):
            v = Vector((1, 2, 3))
            result = v.z
            assert result is not None

    def test_xyz_tuple(self):
        with Tree("_test_vec_xyz", "GeometryNodeTree"):
            v = Vector((1, 2, 3))
            x, y, z = v.xyz
            assert x is not None
            assert y is not None
            assert z is not None

    def test_separate_xyz(self):
        with Tree("_test_vec_sep", "GeometryNodeTree"):
            v = Vector((1, 2, 3))
            result = v.separate_xyz()
            assert result is not None


# ---------------------------------------------------------------------------
# Shader-only methods (ShaderNodeTree)

class TestVectorShaderMethods:

    def test_tangent(self):
        with Tree("_test_vec_tangent", "ShaderNodeTree"):
            result = Vector.Tangent()
            assert result is not None

    def test_uv_map(self):
        with Tree("_test_vec_uvmap", "ShaderNodeTree"):
            result = Vector.UVMap()
            assert result is not None

    def test_bump(self):
        with Tree("_test_vec_bump", "ShaderNodeTree"):
            v = Vector.NormalMap()
            result = v.bump()
            assert result is not None

    def test_mapping(self):
        with Tree("_test_vec_mapping", "ShaderNodeTree"):
            v = Vector.UVMap()
            result = v.mapping()
            assert result is not None

    def test_normal_bug_fix(self):
        """Regression: normal() had undefined variable 'normal' → NameError."""
        with Tree("_test_vec_normal", "ShaderNodeTree"):
            v = Vector.NormalMap()
            result = v.normal()
            assert result is not None

    def test_normal_map(self):
        with Tree("_test_vec_nmap", "ShaderNodeTree"):
            result = Vector.NormalMap()
            assert result is not None

    def test_vector_displacement(self):
        with Tree("_test_vec_vdisp", "ShaderNodeTree"):
            v = Vector.NormalMap()
            result = v.vector_displacement()
            assert result is not None

    def test_transform(self):
        with Tree("_test_vec_transform", "ShaderNodeTree"):
            v = Vector.UVMap()
            result = v.transform()
            assert result is not None
