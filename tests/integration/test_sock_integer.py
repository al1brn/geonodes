"""Tests for core/sock_integer.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_integer import Integer


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

class TestIntegerImport:

    def test_importable(self):
        import core.sock_integer
        assert hasattr(core.sock_integer, 'Integer')

    def test_no_literal_import(self):
        import core.sock_integer
        assert not hasattr(core.sock_integer, 'Literal')

    def test_no_socket_import(self):
        import core.sock_integer
        assert not hasattr(core.sock_integer, 'Socket')

    def test_socket_type(self):
        assert Integer.SOCKET_TYPE == 'INT'


# ---------------------------------------------------------------------------
# Integer creation

class TestIntegerCreation:

    def test_integer_constant(self):
        with Tree("_test_int_const", "GeometryNodeTree"):
            i = Integer(42)
            assert i is not None

    def test_integer_named_input(self):
        with Tree("_test_int_named", "GeometryNodeTree"):
            i = Integer(1, name="MyInt")
            assert i is not None

    def test_integer_returns_integer_type(self):
        with Tree("_test_int_type", "GeometryNodeTree"):
            i = Integer(1)
            assert isinstance(i, Integer)

    def test_integer_min_max(self):
        with Tree("_test_int_minmax", "GeometryNodeTree"):
            i = Integer(5, name="Clamped", min=0, max=10)
            assert i is not None

    def test_integer_index(self):
        with Tree("_test_int_index", "GeometryNodeTree"):
            i = Integer.Index()
            assert i is not None

    def test_integer_id_or_index(self):
        with Tree("_test_int_idoridx", "GeometryNodeTree"):
            i = Integer.IdOrIndex()
            assert i is not None

    def test_from_float(self):
        from core.sock_float import Float
        with Tree("_test_int_fromfloat", "GeometryNodeTree"):
            result = Integer.FromFloat(Float(3.7))
            assert result is not None


# ---------------------------------------------------------------------------
# mix method

class TestIntegerMix:

    def test_mix_creates_node(self):
        with Tree("_test_int_mix", "GeometryNodeTree"):
            a = Integer(1)
            b = Integer(2)
            result = a.mix(other=b)
            assert result is not None


# ---------------------------------------------------------------------------
# Arithmetic operators — scalar

class TestIntegerArithScalar:

    def test_neg(self):
        with Tree("_test_int_neg", "GeometryNodeTree"):
            result = -Integer(1)
            assert result is not None

    def test_abs(self):
        with Tree("_test_int_abs", "GeometryNodeTree"):
            result = abs(Integer(-1))
            assert result is not None

    def test_add(self):
        with Tree("_test_int_add", "GeometryNodeTree"):
            result = Integer(1) + Integer(2)
            assert result is not None

    def test_radd(self):
        with Tree("_test_int_radd", "GeometryNodeTree"):
            result = 1 + Integer(2)
            assert result is not None

    def test_iadd(self):
        with Tree("_test_int_iadd", "GeometryNodeTree"):
            i = Integer(1)
            i += Integer(2)
            assert i is not None

    def test_sub(self):
        with Tree("_test_int_sub", "GeometryNodeTree"):
            result = Integer(3) - Integer(1)
            assert result is not None

    def test_rsub(self):
        with Tree("_test_int_rsub", "GeometryNodeTree"):
            result = 3 - Integer(1)
            assert result is not None

    def test_mul(self):
        with Tree("_test_int_mul", "GeometryNodeTree"):
            result = Integer(2) * Integer(3)
            assert result is not None

    def test_rmul(self):
        with Tree("_test_int_rmul", "GeometryNodeTree"):
            result = 2 * Integer(3)
            assert result is not None

    def test_floordiv(self):
        with Tree("_test_int_floordiv", "GeometryNodeTree"):
            result = Integer(6) // Integer(2)
            assert result is not None

    def test_rfloordiv(self):
        with Tree("_test_int_rfloordiv", "GeometryNodeTree"):
            result = 6 // Integer(2)
            assert result is not None

    def test_mod(self):
        with Tree("_test_int_mod", "GeometryNodeTree"):
            result = Integer(5) % Integer(3)
            assert result is not None

    def test_rmod(self):
        with Tree("_test_int_rmod", "GeometryNodeTree"):
            result = 5 % Integer(3)
            assert result is not None

    def test_pow(self):
        with Tree("_test_int_pow", "GeometryNodeTree"):
            result = Integer(2) ** Integer(3)
            assert result is not None

    def test_rpow(self):
        with Tree("_test_int_rpow", "GeometryNodeTree"):
            result = 2 ** Integer(3)
            assert result is not None

    def test_ipow_bug_fix(self):
        """Regression: __ipow__ was self.power(self, other) — self passed twice."""
        with Tree("_test_int_ipow", "GeometryNodeTree"):
            i = Integer(2)
            i **= Integer(3)
            assert i is not None


# ---------------------------------------------------------------------------
# True division — promotes to Float

class TestIntegerTruediv:

    def test_truediv_returns_result(self):
        with Tree("_test_int_tdiv", "GeometryNodeTree"):
            result = Integer(6) / Integer(2)
            assert result is not None

    def test_rtruediv_returns_result(self):
        with Tree("_test_int_rtdiv", "GeometryNodeTree"):
            result = 6 / Integer(2)
            assert result is not None


# ---------------------------------------------------------------------------
# Comparison operators

class TestIntegerComparison:

    def test_ge(self):
        with Tree("_test_int_ge", "GeometryNodeTree"):
            result = Integer(2) >= Integer(1)
            assert result is not None

    def test_gt(self):
        with Tree("_test_int_gt", "GeometryNodeTree"):
            result = Integer(2) > Integer(1)
            assert result is not None

    def test_le(self):
        with Tree("_test_int_le", "GeometryNodeTree"):
            result = Integer(1) <= Integer(2)
            assert result is not None

    def test_lt(self):
        with Tree("_test_int_lt", "GeometryNodeTree"):
            result = Integer(1) < Integer(2)
            assert result is not None

    def test_eq(self):
        with Tree("_test_int_eq", "GeometryNodeTree"):
            result = Integer(1) == Integer(1)
            assert result is not None

    def test_ne(self):
        with Tree("_test_int_ne", "GeometryNodeTree"):
            result = Integer(1) != Integer(2)
            assert result is not None


# ---------------------------------------------------------------------------
# Bitwise operators

class TestIntegerBitwise:

    def test_invert(self):
        with Tree("_test_int_inv", "GeometryNodeTree"):
            result = ~Integer(5)
            assert result is not None

    def test_and(self):
        with Tree("_test_int_and", "GeometryNodeTree"):
            result = Integer(6) & Integer(3)
            assert result is not None

    def test_rand(self):
        with Tree("_test_int_rand", "GeometryNodeTree"):
            result = 6 & Integer(3)
            assert result is not None

    def test_or(self):
        with Tree("_test_int_or", "GeometryNodeTree"):
            result = Integer(6) | Integer(3)
            assert result is not None

    def test_ror(self):
        with Tree("_test_int_ror", "GeometryNodeTree"):
            result = 6 | Integer(3)
            assert result is not None

    def test_xor(self):
        with Tree("_test_int_xor", "GeometryNodeTree"):
            result = Integer(6) ^ Integer(3)
            assert result is not None

    def test_rxor(self):
        with Tree("_test_int_rxor", "GeometryNodeTree"):
            result = 6 ^ Integer(3)
            assert result is not None

    def test_lshift(self):
        with Tree("_test_int_lshift", "GeometryNodeTree"):
            result = Integer(1) << Integer(2)
            assert result is not None

    def test_rshift(self):
        with Tree("_test_int_rshift", "GeometryNodeTree"):
            result = Integer(8) >> Integer(2)
            assert result is not None


# ---------------------------------------------------------------------------
# Vector arithmetic (tuple form) — uses gnmath

class TestIntegerArithVector:

    def test_add_tuple(self):
        with Tree("_test_int_add_tup", "GeometryNodeTree"):
            result = Integer(1) + (1, 2, 3)
            assert result is not None

    def test_sub_tuple(self):
        with Tree("_test_int_sub_tup", "GeometryNodeTree"):
            result = Integer(1) - (1, 2, 3)
            assert result is not None

    def test_mul_tuple(self):
        with Tree("_test_int_mul_tup", "GeometryNodeTree"):
            result = Integer(2) * (1, 2, 3)
            assert result is not None
