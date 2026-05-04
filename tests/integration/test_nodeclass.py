"""Tests for core/nodeclass.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.nodeclass import Node, ColorRamp, NodeCurves, MenuNode, Group, G
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
# Node creation basics

class TestNodeCreation:

    def test_node_value_creates(self):
        with Tree("_test_nc_value", "GeometryNodeTree"):
            n = Node('Value')
            assert n is not None

    def test_node_out_is_socket(self):
        with Tree("_test_nc_out", "GeometryNodeTree"):
            n = Node('Value')
            assert n._out is not None

    def test_node_str(self):
        with Tree("_test_nc_str", "GeometryNodeTree"):
            n = Node('Value')
            assert 'Value' in str(n)

    def test_node_repr(self):
        with Tree("_test_nc_repr", "GeometryNodeTree"):
            n = Node('Value')
            r = repr(n)
            assert 'Inputs' in r and 'Outputs' in r

    def test_node_lc_returns_self(self):
        with Tree("_test_nc_lc", "GeometryNodeTree"):
            n = Node('Value')
            result = n._lc("Label")
            assert result is n

    def test_node_label_set(self):
        with Tree("_test_nc_label", "GeometryNodeTree"):
            n = Node('Value')
            n._lc("MyLabel")
            assert n._bnode.label == "MyLabel"


# ---------------------------------------------------------------------------
# set_parameter

class TestSetParameter:

    def test_set_parameter_enum_valid(self):
        with Tree("_test_nc_param_enum", "GeometryNodeTree"):
            n = Node('Math')
            n.set_parameter('operation', 'ADD')

    def test_set_parameter_invalid_raises(self):
        with Tree("_test_nc_param_bad", "GeometryNodeTree"):
            n = Node('Math')
            with pytest.raises(NodeError):
                n.set_parameter('nonexistent_param', 'foo')

    def test_set_parameter_none_is_noop(self):
        with Tree("_test_nc_param_none", "GeometryNodeTree"):
            n = Node('Math')
            result = n.set_parameter('operation', None)
            assert result == 'operation'


# ---------------------------------------------------------------------------
# socket_by_index / socket_by_name / socket_by_identifier

class TestSocketAccess:

    def test_socket_by_index_output(self):
        with Tree("_test_nc_sbi", "GeometryNodeTree"):
            n = Node('Math')
            sock = n.socket_by_index('OUTPUT', 0)
            assert sock is not None

    def test_getattr_output_socket(self):
        with Tree("_test_nc_getattr", "GeometryNodeTree"):
            n = Node('Math')
            sock = n.value
            assert sock is not None

    def test_getattr_unknown_raises(self):
        with Tree("_test_nc_getattr_bad", "GeometryNodeTree"):
            n = Node('Math')
            with pytest.raises(AttributeError):
                _ = n.nonexistent_socket_name_xyz


# ---------------------------------------------------------------------------
# set_input_socket

class TestSetInputSocket:

    def test_set_input_by_name(self):
        with Tree("_test_nc_set_in", "GeometryNodeTree"):
            n = Node('Math')
            n.set_input_socket('Value', 3.14)

    def test_set_input_via_setitem(self):
        with Tree("_test_nc_setitem", "GeometryNodeTree"):
            n = Node('Math')
            n['Value'] = 2.0

    def test_set_input_via_setattr(self):
        with Tree("_test_nc_setattr", "GeometryNodeTree"):
            n = Node('Math')
            n.value = 1.0


# ---------------------------------------------------------------------------
# Bug fix: ColorRamp.stops — self._bnode not self.node._bnode

class TestColorRamp:

    def test_color_ramp_creates(self):
        with Tree("_test_nc_cr_create", "GeometryNodeTree"):
            cr = ColorRamp(0.5)
            assert cr is not None

    def test_color_ramp_stops_getter_no_crash(self):
        with Tree("_test_nc_cr_stops_get", "GeometryNodeTree"):
            cr = ColorRamp(0.5)
            stops = cr.stops  # was: AttributeError via self.node._bnode
            assert isinstance(stops, list)

    def test_color_ramp_stops_setter(self):
        with Tree("_test_nc_cr_stops_set", "GeometryNodeTree"):
            cr = ColorRamp(0.5, stops=[0.1, 0.9])
            assert cr is not None

    def test_color_ramp_stops_with_colors(self):
        with Tree("_test_nc_cr_stops_color", "GeometryNodeTree"):
            cr = ColorRamp(0.5, stops=[(0.1, (1, 0, 0)), (0.9, (0, 0, 1))])
            assert cr is not None

    def test_color_ramp_interpolation(self):
        with Tree("_test_nc_cr_interp", "GeometryNodeTree"):
            cr = ColorRamp(0.5, interpolation='CONSTANT')
            assert cr.interpolation == 'CONSTANT'

    def test_color_ramp_out(self):
        with Tree("_test_nc_cr_out", "GeometryNodeTree"):
            cr = ColorRamp(0.5)
            assert cr._out is not None


# ---------------------------------------------------------------------------
# NodeCurves

class TestNodeCurves:

    def test_float_curve_creates(self):
        with Tree("_test_nc_fc_create", "GeometryNodeTree"):
            nc = NodeCurves('Float Curve')
            assert nc is not None

    def test_float_curve_get_curve(self):
        with Tree("_test_nc_fc_get", "GeometryNodeTree"):
            nc = NodeCurves('Float Curve')
            curve = nc.get_curve()
            assert isinstance(curve, list)

    def test_float_curve_set_curve(self):
        with Tree("_test_nc_fc_set", "GeometryNodeTree"):
            nc = NodeCurves('Float Curve')
            nc.set_curve([(0.0, 0.0), (1.0, 1.0)])


# ---------------------------------------------------------------------------
# duplicate_node

class TestDuplicateNode:

    def test_duplicate_creates_new_node(self):
        with Tree("_test_nc_dup", "GeometryNodeTree"):
            n = Node('Math')
            dup = n.duplicate_node()
            assert dup is not None
            assert dup is not n

    def test_duplicate_same_operation(self):
        with Tree("_test_nc_dup_op", "GeometryNodeTree"):
            n = Node('Math', operation='MULTIPLY')
            dup = n.duplicate_node()
            assert dup._bnode.operation == 'MULTIPLY'


# ---------------------------------------------------------------------------
# as_tuple

class TestAsTuple:

    def test_as_tuple_math(self):
        with Tree("_test_nc_tuple", "GeometryNodeTree"):
            n = Node('Math')
            t = n.as_tuple()
            assert isinstance(t, tuple)
            assert len(t) >= 1


# ---------------------------------------------------------------------------
# get_signature

class TestGetSignature:

    def test_get_signature_returns_signature(self):
        from core.signature import Signature
        with Tree("_test_nc_sig", "GeometryNodeTree"):
            n = Node('Math')
            sig = n.get_signature()
            assert isinstance(sig, Signature)
