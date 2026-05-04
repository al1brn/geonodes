"""Tests for core/socket_class.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.nodeclass import Node
from core.socket_class import Socket, NodeCache
from core import constants


# ---------------------------------------------------------------------------
# Minimal concrete Socket subclass for testing

class FloatSocket(Socket):
    SOCKET_TYPE = 'VALUE'

class IntSocket(Socket):
    SOCKET_TYPE = 'INT'

class BoolSocket(Socket):
    SOCKET_TYPE = 'BOOLEAN'

class VectorSocket(Socket):
    SOCKET_TYPE = 'VECTOR'


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
# NodeCache

class TestNodeCache:

    def test_cache_reset_clears_dict(self):
        cache = NodeCache()
        cache._cached_nodes = {'x': object()}
        cache._cache_reset()
        assert cache._cached_nodes == {}


# ---------------------------------------------------------------------------
# Socket.Empty

class TestSocketEmpty:

    def test_empty_socket_is_empty(self):
        with Tree("_test_sock_empty", "GeometryNodeTree"):
            s = FloatSocket.Empty()
            assert s._is_empty()

    def test_empty_socket_str(self):
        with Tree("_test_sock_empty_str", "GeometryNodeTree"):
            s = FloatSocket.Empty()
            assert "Empty" in str(s)

    def test_non_empty_socket_is_not_empty(self):
        with Tree("_test_sock_not_empty", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            assert not s._is_empty()


# ---------------------------------------------------------------------------
# Socket construction from Node

class TestSocketFromNode:

    def test_socket_from_node_out(self):
        with Tree("_test_sock_node_out", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            assert s._bsocket is not None

    def test_socket_wraps_node(self):
        with Tree("_test_sock_wraps", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            assert s.node is node

    def test_socket_from_node_object(self):
        with Tree("_test_sock_from_node", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node)
            assert s._bsocket is not None


# ---------------------------------------------------------------------------
# Socket._is_empty

class TestSocketIsEmpty:

    def test_is_empty_halts_with_message(self):
        with Tree("_test_sock_halt", "GeometryNodeTree"):
            from core.scripterror import NodeError
            s = FloatSocket.Empty()
            with pytest.raises(NodeError, match="halt"):
                s._is_empty("halt message")

    def test_is_empty_returns_true_silently(self):
        with Tree("_test_sock_silent", "GeometryNodeTree"):
            s = FloatSocket.Empty()
            assert s._is_empty() is True

    def test_is_empty_false_for_real_socket(self):
        with Tree("_test_sock_false", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            assert s._is_empty() is False


# ---------------------------------------------------------------------------
# user_label property

class TestUserLabel:

    def test_set_user_label(self):
        with Tree("_test_ul_set", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            s.user_label = "MyLabel"
            assert s.user_label == "MyLabel"

    def test_user_label_stored_in_description(self):
        with Tree("_test_ul_desc", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            s.user_label = "TestLabel"
            assert s._bsocket.description == "UL TestLabel"

    def test_user_label_none_no_crash(self):
        with Tree("_test_ul_none", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            s.user_label = None  # should not raise

    def test_ul_method_chains(self):
        with Tree("_test_ul_chain", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            result = s._ul("ChainLabel")
            assert result is s


# ---------------------------------------------------------------------------
# _lc method

class TestLcMethod:

    def test_lc_returns_self(self):
        with Tree("_test_lc_self", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            result = s._lc("MyLabel")
            assert result is s

    def test_lc_sets_node_label(self):
        with Tree("_test_lc_label", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            s._lc("TestLabel")
            assert node._label == "TestLabel"

    def test_lc_group_input_returns_self(self):
        with Tree("_test_lc_gi", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            # Create an input socket so we have something to wrap
            sock = in_node.create_socket('OUTPUT', 'VALUE', 'Value')
            s = FloatSocket(sock)
            result = s._lc("Label")
            assert result is s

    def test_lc_chaining(self):
        with Tree("_test_lc_chain", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            result = s._lc("A")._lc("B")
            assert result is s


# ---------------------------------------------------------------------------
# _jump

class TestJump:

    def test_jump_changes_bsocket(self):
        with Tree("_test_jump", "GeometryNodeTree"):
            node1 = Node('Value')
            node2 = Node('Value')
            s = FloatSocket(node1._out)
            original = s._bsocket
            s._jump(node2._out)
            assert s._bsocket is not original

    def test_jump_invalid_socket_raises(self):
        from core.scripterror import NodeError
        with Tree("_test_jump_invalid", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            with pytest.raises(NodeError):
                s._jump("not_a_socket")


# ---------------------------------------------------------------------------
# _socket_type

class TestSocketType:

    def test_socket_type_value(self):
        with Tree("_test_st_value", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            assert s._socket_type.type == 'VALUE'

    def test_socket_type_int(self):
        with Tree("_test_st_int", "GeometryNodeTree"):
            node = Node('Integer')
            s = IntSocket(node._out)
            assert s._socket_type.type == 'INT'


# ---------------------------------------------------------------------------
# Socket.Empty with default value

class TestSocketEmptyValue:

    def test_empty_with_none(self):
        with Tree("_test_ev_none", "GeometryNodeTree"):
            s = FloatSocket.Empty(None)
            assert s._is_empty()

    def test_empty_with_value(self):
        with Tree("_test_ev_val", "GeometryNodeTree"):
            s = FloatSocket.Empty(3.14)
            assert s._is_empty()


# ---------------------------------------------------------------------------
# _name

class TestSocketName:

    def test_empty_socket_name(self):
        with Tree("_test_sname_empty", "GeometryNodeTree"):
            s = FloatSocket.Empty()
            assert s._name == "<EMPTY SOCKET>"

    def test_real_socket_name(self):
        with Tree("_test_sname_real", "GeometryNodeTree"):
            node = Node('Value')
            s = FloatSocket(node._out)
            assert isinstance(s._name, str)
