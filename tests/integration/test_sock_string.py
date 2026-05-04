"""Tests for core/sock_string.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_string import String


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

class TestStringImport:

    def test_importable(self):
        import core.sock_string
        assert hasattr(core.sock_string, 'String')

    def test_no_literal_import(self):
        import core.sock_string
        assert not hasattr(core.sock_string, 'Literal')

    def test_no_blender_import(self):
        import core.sock_string
        assert not hasattr(core.sock_string, 'blender')

    def test_socket_type(self):
        assert String.SOCKET_TYPE == 'STRING'


# ---------------------------------------------------------------------------
# String creation

class TestStringCreation:

    def test_string_constant(self):
        with Tree("_test_str_const", "GeometryNodeTree"):
            s = String("hello")
            assert s is not None

    def test_string_named_input(self):
        with Tree("_test_str_named", "GeometryNodeTree"):
            s = String(name="My String")
            assert s is not None

    def test_string_returns_string_type(self):
        with Tree("_test_str_type", "GeometryNodeTree"):
            s = String("hello")
            assert isinstance(s, String)


# ---------------------------------------------------------------------------
# Operators

class TestStringOperators:

    def test_add_string(self):
        with Tree("_test_str_add", "GeometryNodeTree"):
            a = String("hello")
            b = String("world")
            result = a + b
            assert result is not None

    def test_add_tuple(self):
        with Tree("_test_str_add_tup", "GeometryNodeTree"):
            a = String("a")
            b = String("b")
            c = String("c")
            result = a + (b, c)
            assert result is not None

    def test_radd(self):
        with Tree("_test_str_radd", "GeometryNodeTree"):
            s = String("world")
            result = "hello" + s
            assert result is not None

    def test_iadd(self):
        with Tree("_test_str_iadd", "GeometryNodeTree"):
            s = String("hello")
            s += String("world")
            assert s is not None

    def test_mul(self):
        with Tree("_test_str_mul", "GeometryNodeTree"):
            a = String("a")
            b = String("b")
            result = a * b
            assert result is not None

    def test_mul_tuple(self):
        with Tree("_test_str_mul_tup", "GeometryNodeTree"):
            a = String("a")
            b = String("b")
            c = String("c")
            result = a * (b, c)
            assert result is not None

    def test_imul_bug_fix(self):
        """Regression: __imul__ returned join result without _jump → in-place didn't update socket."""
        with Tree("_test_str_imul", "GeometryNodeTree"):
            s = String("hello")
            original_id = id(s)
            s *= String("world")
            assert s is not None
            # After _jump, s should still be a String (not the raw join result)
            assert isinstance(s, String)


# ---------------------------------------------------------------------------
# String methods

class TestStringMethods:

    def test_replace(self):
        with Tree("_test_str_replace", "GeometryNodeTree"):
            s = String("hello world")
            result = s.replace("hello", "bye")
            assert result is not None

    def test_slice(self):
        with Tree("_test_str_slice", "GeometryNodeTree"):
            s = String("hello")
            result = s.slice(position=0, length=3)
            assert result is not None

    def test_length(self):
        with Tree("_test_str_length", "GeometryNodeTree"):
            s = String("hello")
            result = s.length()
            assert result is not None

    def test_to_float(self):
        with Tree("_test_str_tofloat", "GeometryNodeTree"):
            s = String("3.14")
            result = s.to_float()
            assert result is not None

    def test_to_integer(self):
        with Tree("_test_str_toint", "GeometryNodeTree"):
            s = String("42")
            result = s.to_integer()
            assert result is not None

    def test_join(self):
        with Tree("_test_str_join", "GeometryNodeTree"):
            a = String("a")
            b = String("b")
            result = a.join(b)
            assert result is not None

    def test_Join_classmethod(self):
        with Tree("_test_str_Join", "GeometryNodeTree"):
            a = String("a")
            b = String("b")
            c = String("c")
            result = String.Join(a, b, c, delimiter="/")
            assert result is not None

    def test_equal(self):
        with Tree("_test_str_eq", "GeometryNodeTree"):
            a = String("a")
            b = String("b")
            result = a.equal(b)
            assert result is not None

    def test_find_in_string(self):
        with Tree("_test_str_find", "GeometryNodeTree"):
            s = String("hello world")
            result = s.find_in_string("world")
            assert result is not None

    def test_enable_output(self):
        with Tree("_test_str_eo", "GeometryNodeTree"):
            s = String("hello")
            result = s.enable_output()
            assert result is not None
