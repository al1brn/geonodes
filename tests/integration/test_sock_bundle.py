"""Tests for core/sock_bundle.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_bundle import Bundle
from core.signature import Signature


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

class TestBundleImport:

    def test_importable(self):
        import core.sock_bundle
        assert hasattr(core.sock_bundle, 'Bundle')

    def test_no_numpy_import(self):
        import core.sock_bundle
        assert not hasattr(core.sock_bundle, 'np')

    def test_no_bpy_import(self):
        import core.sock_bundle
        assert not hasattr(core.sock_bundle, 'bpy')

    def test_no_utils_import(self):
        import core.sock_bundle
        assert not hasattr(core.sock_bundle, 'utils')

    def test_no_tree_import(self):
        import core.sock_bundle
        assert not hasattr(core.sock_bundle, 'Tree')

    def test_no_socket_import(self):
        import core.sock_bundle
        assert not hasattr(core.sock_bundle, 'Socket')

    def test_socket_type(self):
        assert Bundle.SOCKET_TYPE == 'BUNDLE'


# ---------------------------------------------------------------------------
# Bundle.Combine

class TestBundleCombine:

    def test_combine_with_dict(self):
        with Tree("_test_bundle_combine_dict", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0, 'B': 2.0})
            assert b is not None

    def test_combine_with_kwargs(self):
        with Tree("_test_bundle_combine_kw", "GeometryNodeTree"):
            b = Bundle.Combine(x=1.0, y=2.0)
            assert b is not None

    def test_combine_empty(self):
        with Tree("_test_bundle_combine_empty", "GeometryNodeTree"):
            b = Bundle.Combine()
            assert b is not None

    def test_combine_returns_bundle(self):
        with Tree("_test_bundle_type", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0})
            assert isinstance(b, Bundle)


# ---------------------------------------------------------------------------
# _is_combine property

class TestBundleIsCombine:

    def test_combine_bundle_is_combine(self):
        with Tree("_test_bundle_is_combine", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0})
            assert b._is_combine is True

    def test_joined_bundle_is_not_combine(self):
        with Tree("_test_bundle_joined_not_combine", "GeometryNodeTree"):
            b1 = Bundle.Combine({'A': 1.0})
            b2 = Bundle.Combine({'B': 2.0})
            joined = b1 + b2
            assert joined._is_combine is False


# ---------------------------------------------------------------------------
# get_signature

class TestBundleGetSignature:

    def test_get_signature_returns_signature(self):
        with Tree("_test_bundle_sig", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0, 'B': 2.0})
            sig = b.get_signature()
            assert isinstance(sig, Signature)

    def test_get_signature_non_combine_raises(self):
        with Tree("_test_bundle_sig_bad", "GeometryNodeTree"):
            b1 = Bundle.Combine({'A': 1.0})
            b2 = Bundle.Combine({'B': 2.0})
            joined = b1 + b2
            with pytest.raises(RuntimeError):
                joined.get_signature()


# ---------------------------------------------------------------------------
# separate

class TestBundleSeparate:

    def test_separate_returns_node(self):
        from core.nodeclass import Node
        with Tree("_test_bundle_sep", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0})
            node = b.separate()
            assert node is not None
            assert isinstance(node, Node)

    def test_separate_with_explicit_signature(self):
        with Tree("_test_bundle_sep_sig", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0})
            sig = b.get_signature()
            node = b.separate(signature=sig)
            assert node is not None

    def test_separate_no_signature_uses_combine(self):
        with Tree("_test_bundle_sep_auto", "GeometryNodeTree"):
            b = Bundle.Combine({'A': 1.0, 'B': 2.0})
            node = b.separate()  # should auto-detect signature from Combine
            assert node is not None


# ---------------------------------------------------------------------------
# __add__ (join)

class TestBundleAdd:

    def test_add_creates_bundle(self):
        with Tree("_test_bundle_add", "GeometryNodeTree"):
            b1 = Bundle.Combine({'A': 1.0})
            b2 = Bundle.Combine({'B': 2.0})
            result = b1 + b2
            assert result is not None
            assert isinstance(result, Bundle)

    def test_add_three_bundles(self):
        with Tree("_test_bundle_add3", "GeometryNodeTree"):
            b1 = Bundle.Combine({'A': 1.0})
            b2 = Bundle.Combine({'B': 2.0})
            b3 = Bundle.Combine({'C': 3.0})
            result = b1 + b2 + b3
            assert result is not None
