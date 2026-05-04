"""Tests for core/sock_closure.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_closure import Closure
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

class TestClosureImport:

    def test_importable(self):
        import core.sock_closure
        assert hasattr(core.sock_closure, 'Closure')

    def test_no_numpy_import(self):
        import core.sock_closure
        assert not hasattr(core.sock_closure, 'np')

    def test_no_node_error_import(self):
        import core.sock_closure
        assert not hasattr(core.sock_closure, 'NodeError')

    def test_no_utils_import(self):
        import core.sock_closure
        assert not hasattr(core.sock_closure, 'utils')

    def test_no_zone_node_import(self):
        import core.sock_closure
        assert not hasattr(core.sock_closure, 'ZoneNode')

    def test_no_socket_import(self):
        import core.sock_closure
        assert not hasattr(core.sock_closure, 'Socket')

    def test_socket_type(self):
        assert Closure.SOCKET_TYPE == 'CLOSURE'


# ---------------------------------------------------------------------------
# Closure zone — with syntax

class TestClosureZone:

    def test_closure_zone_creates(self):
        with Tree("_test_cl_zone_create", "GeometryNodeTree"):
            with Closure() as cl:
                pass
            assert cl is not None

    def test_closure_has_zone_true(self):
        with Tree("_test_cl_has_zone_true", "GeometryNodeTree"):
            with Closure() as cl:
                pass
            assert cl._has_zone is True

    def test_closure_zone_with_output(self):
        from core.sock_float import Float
        with Tree("_test_cl_zone_output", "GeometryNodeTree"):
            with Closure() as cl:
                Float(3.14).out("Pi")
            assert cl is not None


# ---------------------------------------------------------------------------
# Closure input (no zone)

class TestClosureInput:

    def test_closure_input_creates(self):
        with Tree("_test_cl_input", "GeometryNodeTree"):
            cl = Closure(None, name="My Closure")
            assert cl is not None

    def test_closure_input_has_zone_false(self):
        with Tree("_test_cl_input_no_zone", "GeometryNodeTree"):
            cl = Closure(None, name="My Closure")
            assert cl._has_zone is False


# ---------------------------------------------------------------------------
# get_signature

class TestClosureGetSignature:

    def test_get_signature_zone_returns_signature(self):
        from core.sock_float import Float
        with Tree("_test_cl_sig", "GeometryNodeTree"):
            with Closure() as cl:
                Float(3.14, "Pi").out("Result")
            sig = cl.get_signature()
            assert isinstance(sig, Signature)

    def test_get_signature_no_zone_raises(self):
        with Tree("_test_cl_sig_bad", "GeometryNodeTree"):
            cl = Closure(None, name="My Closure")
            with pytest.raises(RuntimeError):
                cl.get_signature()


# ---------------------------------------------------------------------------
# evaluate

class TestClosureEvaluate:

    def test_evaluate_zone_no_args(self):
        from core.sock_float import Float
        with Tree("_test_cl_eval_noargs", "GeometryNodeTree"):
            with Closure() as cl:
                Float(3.14).out("Pi")
            result = cl.evaluate()
            assert result is not None

    def test_evaluate_zone_returns_socket(self):
        from core.sock_float import Float
        from core.socket_class import Socket
        with Tree("_test_cl_eval_sock", "GeometryNodeTree"):
            with Closure() as cl:
                Float(3.14).out("Pi")
            result = cl.evaluate()
            assert isinstance(result, Socket)

    def test_evaluate_with_explicit_signature(self):
        from core.sock_float import Float
        with Tree("_test_cl_eval_sig", "GeometryNodeTree"):
            with Closure() as cl:
                Float(3.14, "Pi").out("Result")
            sig = cl.get_signature()
            # Second closure (tree input) evaluated with the signature
            cl2 = Closure(None, name="Other Closure")
            result = cl2.evaluate(signature=sig)
            assert result is not None


# ---------------------------------------------------------------------------
# __call__ (delegates to evaluate)

class TestClosureCall:

    def test_call_delegates_to_evaluate(self):
        from core.sock_float import Float
        with Tree("_test_cl_call", "GeometryNodeTree"):
            with Closure() as cl:
                Float(1.0).out("Val")
            result = cl()
            assert result is not None
