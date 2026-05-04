"""Tests for core/sock_float.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_float import Float


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


def make_float(tree_name, value=1.0):
    """Helper: open a tree and return a Float socket."""
    pass  # used inline below


# ---------------------------------------------------------------------------
# Import checks

class TestFloatImport:

    def test_importable(self):
        import core.sock_float
        assert hasattr(core.sock_float, 'Float')

    def test_no_literal_import(self):
        import core.sock_float
        assert not hasattr(core.sock_float, 'Literal')

    def test_no_numpy_import(self):
        import core.sock_float
        assert not hasattr(core.sock_float, 'np')

    def test_no_bpy_import(self):
        import core.sock_float
        assert not hasattr(core.sock_float, 'bpy')

    def test_no_tree_import(self):
        import core.sock_float
        assert not hasattr(core.sock_float, 'Tree')

    def test_no_socket_import(self):
        import core.sock_float
        assert not hasattr(core.sock_float, 'Socket')

    def test_socket_type(self):
        assert Float.SOCKET_TYPE == 'VALUE'


# ---------------------------------------------------------------------------
# Float creation

class TestFloatCreation:

    def test_float_constant(self):
        with Tree("_test_flt_const", "GeometryNodeTree"):
            f = Float(3.14)
            assert f is not None

    def test_float_named_input(self):
        with Tree("_test_flt_named", "GeometryNodeTree"):
            f = Float(1.0, name="MyFloat")
            assert f is not None

    def test_float_returns_float_type(self):
        with Tree("_test_flt_type", "GeometryNodeTree"):
            f = Float(1.0)
            assert isinstance(f, Float)

    def test_float_min_max(self):
        with Tree("_test_flt_minmax", "GeometryNodeTree"):
            f = Float(0.5, name="Clamped", min=0.0, max=1.0)
            assert f is not None


# ---------------------------------------------------------------------------
# mix and color_ramp

class TestFloatMixColorRamp:

    def test_mix_creates_node(self):
        with Tree("_test_flt_mix", "GeometryNodeTree"):
            a = Float(1.0)
            b = Float(2.0)
            result = a.mix(other=b)
            assert result is not None

    def test_color_ramp_creates_node(self):
        with Tree("_test_flt_cr", "GeometryNodeTree"):
            f = Float(0.5)
            result = f.color_ramp()
            assert result is not None

    def test_color_ramp_with_stops(self):
        with Tree("_test_flt_cr_stops", "GeometryNodeTree"):
            f = Float(0.5)
            result = f.color_ramp(stops=[(0.0, (1, 0, 0)), (1.0, (0, 0, 1))])
            assert result is not None

    def test_curve_creates_node(self):
        with Tree("_test_flt_curve", "GeometryNodeTree"):
            f = Float(0.5)
            result = f.curve()
            assert result is not None

    def test_curve_with_points(self):
        with Tree("_test_flt_curve_pts", "GeometryNodeTree"):
            f = Float(0.5)
            result = f.curve(curve=[(0.0, 0.0), (1.0, 1.0)])
            assert result is not None


# ---------------------------------------------------------------------------
# Arithmetic operators — scalar operands

class TestFloatArithScalar:

    def test_neg(self):
        with Tree("_test_flt_neg", "GeometryNodeTree"):
            result = -Float(1.0)
            assert result is not None

    def test_abs(self):
        with Tree("_test_flt_abs", "GeometryNodeTree"):
            result = abs(Float(-1.0))
            assert result is not None

    def test_add(self):
        with Tree("_test_flt_add", "GeometryNodeTree"):
            result = Float(1.0) + Float(2.0)
            assert result is not None

    def test_radd(self):
        with Tree("_test_flt_radd", "GeometryNodeTree"):
            result = 1.0 + Float(2.0)
            assert result is not None

    def test_iadd(self):
        with Tree("_test_flt_iadd", "GeometryNodeTree"):
            f = Float(1.0)
            f += Float(2.0)
            assert f is not None

    def test_sub(self):
        with Tree("_test_flt_sub", "GeometryNodeTree"):
            result = Float(3.0) - Float(1.0)
            assert result is not None

    def test_rsub(self):
        with Tree("_test_flt_rsub", "GeometryNodeTree"):
            result = 3.0 - Float(1.0)
            assert result is not None

    def test_mul(self):
        with Tree("_test_flt_mul", "GeometryNodeTree"):
            result = Float(2.0) * Float(3.0)
            assert result is not None

    def test_rmul(self):
        with Tree("_test_flt_rmul", "GeometryNodeTree"):
            result = 2.0 * Float(3.0)
            assert result is not None

    def test_truediv(self):
        with Tree("_test_flt_div", "GeometryNodeTree"):
            result = Float(6.0) / Float(2.0)
            assert result is not None

    def test_rtruediv(self):
        with Tree("_test_flt_rdiv", "GeometryNodeTree"):
            result = 6.0 / Float(2.0)
            assert result is not None

    def test_mod(self):
        with Tree("_test_flt_mod", "GeometryNodeTree"):
            result = Float(5.0) % Float(3.0)
            assert result is not None

    def test_pow(self):
        with Tree("_test_flt_pow", "GeometryNodeTree"):
            result = Float(2.0) ** Float(3.0)
            assert result is not None

    def test_rpow(self):
        with Tree("_test_flt_rpow", "GeometryNodeTree"):
            result = 2.0 ** Float(3.0)
            assert result is not None


# ---------------------------------------------------------------------------
# Arithmetic operators — vector operands (tuple form)
#
# Note: Vector(float_socket) conversion is broken in Socket.__init__ (pre-existing),
# so float OP vec calls like __add__, __sub__, __mod__ (which do Vector(self).add(vec))
# crash with RecursionError when self is a Float socket.
#
# The operations that DO work are those that call Vector(other) where other is already
# vector-like (a tuple or Vector socket), NOT Vector(self) where self is Float.
#
# Bug fixed: __rtruediv__ was Vector(self).divide(other) — Float socket as first arg
#            → crashed with RecursionError for (1,2,3) / float_socket
#            Fixed to: Vector(other).divide(self) — works correctly

class TestFloatArithVector:

    def test_mul_tuple_vector(self):
        """float * (1,2,3) → Vector(other).scale(self) — works (other is tuple)."""
        with Tree("_test_flt_mul_tup", "GeometryNodeTree"):
            f = Float(2.0)
            result = f * (1, 2, 3)
            assert result is not None

    def test_rmul_tuple_vector(self):
        """(1,2,3) * float → Vector(other).scale(self) — works."""
        with Tree("_test_flt_rmul_tup", "GeometryNodeTree"):
            f = Float(2.0)
            result = (1, 2, 3) * f  # calls Float.__rmul__
            assert result is not None

    def test_truediv_tuple_vector(self):
        """float / (1,2,3) → Vector((1,2,3)).divide(float) — works."""
        with Tree("_test_flt_div_tup", "GeometryNodeTree"):
            f = Float(2.0)
            result = f / (4, 6, 8)
            assert result is not None

    def test_rtruediv_tuple_vector_fixed(self):
        """Bug fix: (1,2,3) / float was Vector(float).divide(vec) → crashed.
        Fixed to Vector(other).divide(self) = Vector((1,2,3)).divide(float) → works."""
        with Tree("_test_flt_rdiv_tup", "GeometryNodeTree"):
            f = Float(2.0)
            result = (4, 6, 8) / f  # calls Float.__rtruediv__
            assert result is not None

    def test_rtruediv_socket_vector_fixed(self):
        """Bug fix: vec_socket / float was Vector(float_socket).divide(vec) → RecursionError.
        Fixed to Vector(vec_socket).divide(float) → works."""
        from core.sock_vector import Vector
        with Tree("_test_flt_rdiv_sock", "GeometryNodeTree"):
            f = Float(2.0)
            v = Vector((4, 6, 8))
            result = v / f  # Python: v.__truediv__(f) or f.__rtruediv__(v)
            assert result is not None


# ---------------------------------------------------------------------------
# Comparison operators

class TestFloatComparison:

    def test_ge(self):
        with Tree("_test_flt_ge", "GeometryNodeTree"):
            result = Float(2.0) >= Float(1.0)
            assert result is not None

    def test_gt(self):
        with Tree("_test_flt_gt", "GeometryNodeTree"):
            result = Float(2.0) > Float(1.0)
            assert result is not None

    def test_le(self):
        with Tree("_test_flt_le", "GeometryNodeTree"):
            result = Float(1.0) <= Float(2.0)
            assert result is not None

    def test_lt(self):
        with Tree("_test_flt_lt", "GeometryNodeTree"):
            result = Float(1.0) < Float(2.0)
            assert result is not None

    def test_eq(self):
        with Tree("_test_flt_eq", "GeometryNodeTree"):
            result = Float(1.0) == Float(1.0)
            assert result is not None

    def test_ne(self):
        with Tree("_test_flt_ne", "GeometryNodeTree"):
            result = Float(1.0) != Float(2.0)
            assert result is not None


# ---------------------------------------------------------------------------
# Rounding operators

class TestFloatRounding:

    def test_round(self):
        with Tree("_test_flt_round", "GeometryNodeTree"):
            result = round(Float(1.7))
            assert result is not None

    def test_floor(self):
        with Tree("_test_flt_floor", "GeometryNodeTree"):
            import math
            result = math.floor(Float(1.7))
            assert result is not None

    def test_ceil(self):
        with Tree("_test_flt_ceil", "GeometryNodeTree"):
            import math
            result = math.ceil(Float(1.2))
            assert result is not None

    def test_trunc(self):
        with Tree("_test_flt_trunc", "GeometryNodeTree"):
            import math
            result = math.trunc(Float(1.9))
            assert result is not None


# ---------------------------------------------------------------------------
# out() method

class TestFloatOut:

    def test_out_geometry_tree(self):
        with Tree("_test_flt_out_geo", "GeometryNodeTree"):
            Float(1.0).out("MyFloat")

    def test_out_shader_group(self):
        with Tree("_test_flt_out_shgrp", "ShaderNodeTree", is_group=True):
            Float(1.0).out("MyFloat")
