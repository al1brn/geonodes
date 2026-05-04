"""Tests for core/domain_class.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.nodeclass import Node
from core.domain_class import Domain
from core.geometry_class import Geometry
from core.scripterror import NodeError


# ---------------------------------------------------------------------------
# Minimal concrete classes for testing

class TestGeometry(Geometry):
    SOCKET_TYPE = 'GEOMETRY'

_store_calls = []

class TestDomain(Domain):
    DOMAIN_NAME = 'POINT'

    def store_named_attribute(self, name, value, **kwargs):
        _store_calls.append((name, value))


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


@pytest.fixture
def geo_and_domain():
    """Provide a real geometry socket + domain inside a tree."""
    tree_name = "_test_domain_ctx"
    with Tree(tree_name, "GeometryNodeTree") as tree:
        # NodeGroupInput output[0] is the geometry socket
        in_node = tree.input_node
        sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
        geo = TestGeometry(sock)
        dom = TestDomain(geo)
        yield geo, dom


# ---------------------------------------------------------------------------
# Module import (catches the deleted broken import)

class TestModuleImport:

    def test_domain_class_importable(self):
        import core.domain_class
        assert hasattr(core.domain_class, 'Domain')

    def test_no_arguments_import(self):
        import core.domain_class
        assert not hasattr(core.domain_class, 'Arguments')

    def test_old_method_removed(self):
        assert not hasattr(Domain, 'data_type_from_value_OLD')


# ---------------------------------------------------------------------------
# Domain construction

class TestDomainConstruction:

    def test_domain_has_geo(self):
        with Tree("_test_dom_geo", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            assert dom._geo is geo

    def test_domain_selection_initially_none(self):
        with Tree("_test_dom_sel", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            assert dom._selection is None

    def test_domain_has_domain_name(self):
        assert TestDomain.DOMAIN_NAME == 'POINT'

    def test_domain_str(self):
        with Tree("_test_dom_str", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            s = str(dom)
            assert 'POINT' in s


# ---------------------------------------------------------------------------
# Domain.get_selection

class TestGetSelection:

    def test_no_selection_returns_none(self):
        with Tree("_test_dom_getsel", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            assert dom.get_selection() is None

    def test_geo_selection_propagates(self):
        with Tree("_test_dom_geosel", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            geo_sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            bool_sock = in_node.create_socket('OUTPUT', 'BOOLEAN', 'Selection')

            from core.socket_class import Socket
            class BoolSock(Socket):
                SOCKET_TYPE = 'BOOLEAN'

            geo = TestGeometry(geo_sock)
            sel = BoolSock(bool_sock)
            geo[sel]
            dom = TestDomain(geo)
            result = dom.get_selection()
            assert result is not None


# ---------------------------------------------------------------------------
# Domain.__setattr__

class TestDomainSetAttr:

    def test_slot_attr_sets_directly(self):
        with Tree("_test_dom_slot", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            dom._selection = None  # slot attr — should not raise

    def test_uppercase_attr_calls_store_named(self):
        _store_calls.clear()
        with Tree("_test_dom_upper", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            dom.MyAttribute = 1.0
            assert _store_calls == [("MyAttribute", 1.0)]

    def test_lowercase_attr_raises_node_error(self):
        with Tree("_test_dom_lower", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            with pytest.raises(NodeError):
                dom.bad_attr = 1.0

    def test_underscore_attr_raises_node_error(self):
        with Tree("_test_dom_under", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = TestGeometry(sock)
            dom = TestDomain(geo)
            with pytest.raises(NodeError):
                dom._unknown = 1.0


# ---------------------------------------------------------------------------
# Domain._jump delegates to geometry

class TestDomainJump:

    def test_jump_delegates_to_geo(self):
        with Tree("_test_dom_jump", "GeometryNodeTree") as tree:
            in_node = tree.input_node
            sock1 = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo1')
            sock2 = in_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo2')
            geo = TestGeometry(sock1)
            dom = TestDomain(geo)
            dom._jump(sock2)
            assert geo._bsocket is not sock1
