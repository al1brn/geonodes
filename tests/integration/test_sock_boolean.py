"""Tests for core/sock_boolean.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_boolean import Boolean
from core.scripterror import NodeError


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

class TestBooleanImport:

    def test_importable(self):
        import core.sock_boolean
        assert hasattr(core.sock_boolean, 'Boolean')

    def test_no_utils_import(self):
        import core.sock_boolean
        assert not hasattr(core.sock_boolean, 'utils')

    def test_no_tree_import(self):
        import core.sock_boolean
        assert not hasattr(core.sock_boolean, 'Tree')

    def test_no_node_import(self):
        import core.sock_boolean
        assert not hasattr(core.sock_boolean, 'Node')

    def test_no_socket_import(self):
        import core.sock_boolean
        assert not hasattr(core.sock_boolean, 'Socket')


# ---------------------------------------------------------------------------
# Boolean creation

class TestBooleanCreation:

    def test_boolean_constant_true(self):
        with Tree("_test_bool_const_true", "GeometryNodeTree") as tree:
            b = Boolean(True)
            assert b is not None

    def test_boolean_constant_false(self):
        with Tree("_test_bool_const_false", "GeometryNodeTree") as tree:
            b = Boolean(False)
            assert b is not None

    def test_boolean_input(self):
        with Tree("_test_bool_input", "GeometryNodeTree") as tree:
            b = Boolean(True, "MyBool")
            assert b is not None

    def test_socket_type(self):
        assert Boolean.SOCKET_TYPE == 'BOOLEAN'


# ---------------------------------------------------------------------------
# Unary operator

class TestBooleanNeg:

    def test_neg_creates_node(self):
        with Tree("_test_bool_neg", "GeometryNodeTree") as tree:
            a = Boolean(True)
            result = -a
            assert result is not None


# ---------------------------------------------------------------------------
# Binary operators

class TestBooleanOr:

    def test_or_creates_node(self):
        with Tree("_test_bool_or", "GeometryNodeTree") as tree:
            a = Boolean(True)
            b = Boolean(False)
            result = a | b
            assert result is not None

    def test_ror_creates_node(self):
        with Tree("_test_bool_ror", "GeometryNodeTree") as tree:
            a = Boolean(True)
            result = True | a
            assert result is not None


class TestBooleanAnd:

    def test_and_creates_node(self):
        with Tree("_test_bool_and", "GeometryNodeTree") as tree:
            a = Boolean(True)
            b = Boolean(False)
            result = a & b
            assert result is not None

    def test_rand_creates_node(self):
        with Tree("_test_bool_rand", "GeometryNodeTree") as tree:
            a = Boolean(True)
            result = True & a
            assert result is not None

    def test_mul_creates_node(self):
        with Tree("_test_bool_mul", "GeometryNodeTree") as tree:
            a = Boolean(True)
            b = Boolean(False)
            result = a * b
            assert result is not None


class TestBooleanAdd:

    def test_add_creates_node(self):
        with Tree("_test_bool_add", "GeometryNodeTree") as tree:
            a = Boolean(True)
            b = Boolean(False)
            result = a + b
            assert result is not None


class TestBooleanSub:

    def test_sub_creates_node(self):
        with Tree("_test_bool_sub", "GeometryNodeTree") as tree:
            a = Boolean(True)
            b = Boolean(False)
            result = a - b
            assert result is not None


# ---------------------------------------------------------------------------
# Bug fix: __xor__ was calling self.xor(self) instead of self.xor(other)

class TestBooleanXor:

    def test_xor_creates_node(self):
        with Tree("_test_bool_xor", "GeometryNodeTree") as tree:
            a = Boolean(True)
            b = Boolean(False)
            result = a ^ b
            assert result is not None

    def test_rxor_creates_node(self):
        with Tree("_test_bool_rxor", "GeometryNodeTree") as tree:
            a = Boolean(True)
            result = True ^ a
            assert result is not None

    def test_xor_uses_other_not_self(self):
        with Tree("_test_bool_xor_operand", "GeometryNodeTree") as tree:
            a = Boolean(True, "A")
            b = Boolean(False, "B")
            result = a ^ b
            # result.node is the geonodes Node wrapper; ._bnode is the Blender node
            bnode = result.node._bnode
            # Both inputs must be linked (bug: self.xor(self) links both to same socket)
            assert bnode.inputs[0].is_linked
            assert bnode.inputs[1].is_linked
            # The two linked sockets must differ (fix: other, not self)
            in0_from = bnode.inputs[0].links[0].from_socket
            in1_from = bnode.inputs[1].links[0].from_socket
            assert in0_from != in1_from


# ---------------------------------------------------------------------------
# __bool__ raises NodeError

class TestBooleanPythonBool:

    def test_bool_raises(self):
        with Tree("_test_bool_pyval", "GeometryNodeTree") as tree:
            b = Boolean(True)
            with pytest.raises(NodeError):
                _ = bool(b)

    def test_bool_not_raises(self):
        with Tree("_test_bool_not", "GeometryNodeTree") as tree:
            b = Boolean(True)
            with pytest.raises(NodeError):
                _ = not b
