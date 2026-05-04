"""Tests for core/nodezone.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.nodezone import ZoneNode, ZoneIterator, repeat, simulation, SIMULATION, REPEAT, FOR_EACH, CLOSURE


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
# ZoneNode invalid zone_id

class TestZoneNodeValidation:

    def test_invalid_zone_id_raises(self):
        with Tree("_test_zone_invalid", "GeometryNodeTree"):
            with pytest.raises(AttributeError, match="not valid"):
                ZoneNode("BadZone", Value=1.0)

    def test_simulation_no_args_raises(self):
        with Tree("_test_zone_sim_noarg", "GeometryNodeTree"):
            with pytest.raises(Exception):
                ZoneNode.Simulation()

    def test_repeat_no_socket_raises(self):
        with Tree("_test_zone_rep_noarg", "GeometryNodeTree"):
            with pytest.raises(Exception):
                ZoneNode.Repeat(3)


# ---------------------------------------------------------------------------
# Repeat zone

class TestRepeatZone:

    def test_repeat_creates_output_node(self):
        with Tree("_test_repeat_out", "GeometryNodeTree"):
            node = ZoneNode.Repeat(3, Value=1.0)
            assert node is not None
            assert node._bnode.bl_idname == 'GeometryNodeRepeatOutput'

    def test_repeat_creates_paired_input_node(self):
        with Tree("_test_repeat_pair", "GeometryNodeTree"):
            node = ZoneNode.Repeat(3, Value=1.0)
            assert node._is_paired_output
            assert node._paired_input_node is not None
            assert node._paired_input_node._is_paired_input

    def test_repeat_input_node_bl_idname(self):
        with Tree("_test_repeat_inode", "GeometryNodeTree"):
            node = ZoneNode.Repeat(3, Value=1.0)
            assert node._paired_input_node._bnode.bl_idname == 'GeometryNodeRepeatInput'

    def test_repeat_zone_id(self):
        with Tree("_test_repeat_zoneid", "GeometryNodeTree"):
            node = ZoneNode.Repeat(3, Value=1.0)
            assert node._zone_id == REPEAT

    def test_repeat_classmethod(self):
        with Tree("_test_repeat_cls", "GeometryNodeTree"):
            node = ZoneNode.Repeat(5, Value=2.0)
            assert node._bnode.bl_idname == 'GeometryNodeRepeatOutput'


# ---------------------------------------------------------------------------
# Simulation zone

class TestSimulationZone:

    def test_simulation_creates_output_node(self):
        with Tree("_test_sim_out", "GeometryNodeTree"):
            node = ZoneNode.Simulation(Value=1.0)
            assert node is not None
            assert node._bnode.bl_idname == 'GeometryNodeSimulationOutput'

    def test_simulation_creates_paired_input_node(self):
        with Tree("_test_sim_pair", "GeometryNodeTree"):
            node = ZoneNode.Simulation(Value=1.0)
            assert node._is_paired_output
            assert node._paired_input_node is not None

    def test_simulation_input_node_bl_idname(self):
        with Tree("_test_sim_inode", "GeometryNodeTree"):
            node = ZoneNode.Simulation(Value=1.0)
            assert node._paired_input_node._bnode.bl_idname == 'GeometryNodeSimulationInput'

    def test_simulation_zone_id(self):
        with Tree("_test_sim_zoneid", "GeometryNodeTree"):
            node = ZoneNode.Simulation(Value=1.0)
            assert node._zone_id == SIMULATION


# ---------------------------------------------------------------------------
# ZoneIterator construction

class TestZoneIteratorConstruction:

    def test_zoneiterator_rejects_closure(self):
        with Tree("_test_zi_closure", "GeometryNodeTree"):
            node = ZoneNode.Closure()
            with pytest.raises(RuntimeError):
                ZoneIterator(None, node)

    def test_zoneiterator_rejects_non_zone_node(self):
        from core.nodeclass import Node
        with Tree("_test_zi_notzone", "GeometryNodeTree"):
            node = Node('Math')
            with pytest.raises(RuntimeError):
                ZoneIterator(None, node)

    def test_zoneiterator_accepts_repeat(self):
        with Tree("_test_zi_rep", "GeometryNodeTree"):
            node = ZoneNode.Repeat(3, Value=1.0)
            zi = ZoneIterator(None, node)
            assert zi._name == REPEAT

    def test_zoneiterator_accepts_simulation(self):
        with Tree("_test_zi_sim", "GeometryNodeTree"):
            node = ZoneNode.Simulation(Value=1.0)
            zi = ZoneIterator(None, node)
            assert zi._name == SIMULATION


# ---------------------------------------------------------------------------
# repeat / simulation global functions

class TestGlobalFunctions:

    def test_repeat_function_returns_iterator(self):
        with Tree("_test_gfunc_rep", "GeometryNodeTree"):
            zi = repeat(3, Value=1.0)
            assert isinstance(zi, ZoneIterator)
            assert zi._name == REPEAT

    def test_simulation_function_returns_iterator(self):
        with Tree("_test_gfunc_sim", "GeometryNodeTree"):
            zi = simulation(Value=1.0)
            assert isinstance(zi, ZoneIterator)
            assert zi._name == SIMULATION


# ---------------------------------------------------------------------------
# for-loop iteration

class TestZoneIteration:

    def test_repeat_for_loop_executes_body(self):
        with Tree("_test_iter_rep", "GeometryNodeTree"):
            executed = False
            for rep in repeat(3, Value=1.0):
                executed = True
            assert executed

    def test_simulation_for_loop_executes_body(self):
        with Tree("_test_iter_sim", "GeometryNodeTree"):
            executed = False
            for sim in simulation(Value=1.0):
                executed = True
            assert executed

    def test_repeat_loop_done_after_exit(self):
        with Tree("_test_iter_done", "GeometryNodeTree"):
            zi = repeat(3, Value=1.0)
            for rep in zi:
                pass
            assert zi._done is True
            assert zi._in_zone is False
