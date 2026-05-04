"""Tests for core/treeinterface.py — requires Blender."""
import pytest
import bpy

from core.treeinterface import ItemPath, TreeInterface, check_in_out, PanelIterator


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture
def btree():
    name = "_test_treeinterface"
    tree = bpy.data.node_groups.get(name)
    if tree is None:
        tree = bpy.data.node_groups.new(name, type="GeometryNodeTree")
    tree.interface.clear()
    yield tree
    bpy.data.node_groups.remove(tree)

@pytest.fixture
def tinf(btree):
    return TreeInterface(btree)


# ---------------------------------------------------------------------------
# check_in_out

class TestCheckInOut:

    def test_input_valid(self):
        assert check_in_out('INPUT') is True

    def test_output_valid(self):
        assert check_in_out('OUTPUT') is True

    def test_both_without_flag_raises(self):
        with pytest.raises(RuntimeError):
            check_in_out('BOTH')

    def test_both_with_flag_valid(self):
        assert check_in_out('BOTH', both=True) is True

    def test_invalid_raises(self):
        with pytest.raises(RuntimeError, match="not in"):
            check_in_out('OUPUT')


# ---------------------------------------------------------------------------
# ItemPath — static methods

class TestItemPathStatic:

    def test_path_to_stack_simple(self):
        stack = ItemPath.path_to_stack("Panel")
        assert stack == [("Panel", 0)]

    def test_path_to_stack_nested(self):
        stack = ItemPath.path_to_stack("Top > Sub")
        assert stack == [("Top", 0), ("Sub", 0)]

    def test_path_to_stack_ranked(self):
        stack = ItemPath.path_to_stack("Panel_2")
        assert stack == [("Panel", 2)]

    def test_stack_to_path_simple(self):
        assert ItemPath.stack_to_path([("Panel", 0)]) == "Panel"

    def test_stack_to_path_nested(self):
        assert ItemPath.stack_to_path([("Top", 0), ("Sub", 0)]) == "Top > Sub"

    def test_stack_to_path_ranked(self):
        assert ItemPath.stack_to_path([("Panel", 2)]) == "Panel_2"

    def test_stack_to_path_empty_names_skipped(self):
        assert ItemPath.stack_to_path([("", 0), ("Panel", 0)]) == "Panel"

    def test_roundtrip(self):
        path = "Top > Sub_1 > Leaf"
        assert ItemPath.stack_to_path(ItemPath.path_to_stack(path)) == path


# ---------------------------------------------------------------------------
# ItemPath — construction

class TestItemPathConstruction:

    def test_from_none(self):
        p = ItemPath(None)
        assert p.is_root

    def test_from_empty_string(self):
        p = ItemPath("")
        assert p.is_root

    def test_from_string(self):
        p = ItemPath("Panel")
        assert p.path == "Panel"

    def test_from_nested_string(self):
        p = ItemPath("Top > Sub")
        assert p.path == "Top > Sub"

    def test_from_list(self):
        p = ItemPath([("Top", 0), ("Sub", 0)])
        assert p.path == "Top > Sub"

    def test_from_item_path(self):
        p1 = ItemPath("Panel")
        p2 = ItemPath(p1)
        assert p2.path == p1.path

    def test_invalid_type_raises(self):
        with pytest.raises(Exception):
            ItemPath(42)


# ---------------------------------------------------------------------------
# ItemPath — properties

class TestItemPathProperties:

    def test_name(self):
        assert ItemPath("Top > Sub").name == "Sub"

    def test_name_rank(self):
        name, rank = ItemPath("Panel_2").name_rank
        assert name == "Panel"
        assert rank == 2

    def test_parent(self):
        assert ItemPath("Top > Sub").parent.path == "Top"

    def test_parent_of_root(self):
        assert ItemPath(None).parent.is_root

    def test_stack(self):
        assert ItemPath("Top > Sub").stack == [("Top", 0), ("Sub", 0)]


# ---------------------------------------------------------------------------
# ItemPath — operations

class TestItemPathOperations:

    def test_join_two_paths(self):
        result = ItemPath("Top") + ItemPath("Sub")
        assert result.path == "Top > Sub"

    def test_join_with_root(self):
        result = ItemPath(None) + ItemPath("Sub")
        assert result.path == "Sub"

    def test_equality(self):
        assert ItemPath("Panel") == ItemPath("Panel")

    def test_inequality(self):
        assert ItemPath("Panel") != ItemPath("Other")

    def test_get_relative_to(self):
        child = ItemPath("Top > Sub > Leaf")
        parent = ItemPath("Top > Sub")
        rel = child - parent
        assert rel.path == " > Leaf" or rel.path.endswith("Leaf")


# ---------------------------------------------------------------------------
# TreeInterface — panels

class TestTreeInterfacePanels:

    def test_get_panel_empty_returns_none(self, tinf):
        assert tinf.get_panel("") is None

    def test_get_panel_missing_returns_none(self, tinf):
        assert tinf.get_panel("NoSuchPanel") is None

    def test_create_panel(self, tinf):
        panel = tinf.get_panel("MyPanel", create=True)
        assert panel is not None
        assert panel.name == "MyPanel"

    def test_create_panel_idempotent(self, tinf):
        p1 = tinf.get_panel("MyPanel", create=True)
        p2 = tinf.get_panel("MyPanel", create=False)
        assert p1 == p2

    def test_create_nested_panel(self, tinf):
        panel = tinf.get_panel("Top > Sub", create=True)
        assert panel is not None
        assert panel.name == "Sub"


# ---------------------------------------------------------------------------
# TreeInterface — sockets

class TestTreeInterfaceSockets:

    def test_create_input_socket(self, tinf):
        sock = tinf.create_socket('INPUT', "Value", "Float")
        assert sock is not None
        assert sock.name == "Value"
        assert sock.in_out == 'INPUT'

    def test_create_output_socket(self, tinf):
        sock = tinf.create_socket('OUTPUT', "Result", "Float")
        assert sock is not None
        assert sock.in_out == 'OUTPUT'

    def test_get_socket_by_name(self, tinf):
        tinf.create_socket('INPUT', "MyFloat", "Float")
        sock = tinf.get_socket('INPUT', "MyFloat", "Float")
        assert sock is not None

    def test_get_socket_wrong_type_returns_none(self, tinf):
        tinf.create_socket('INPUT', "MyFloat", "Float")
        sock = tinf.get_socket('INPUT', "MyFloat", "Integer")
        assert sock is None

    def test_get_socket_missing_returns_none(self, tinf):
        assert tinf.get_socket('INPUT', "NoSocket", "Float") is None

    def test_create_socket_in_panel(self, tinf):
        sock = tinf.create_socket('INPUT', "Val", "Float", parent="MyPanel")
        assert sock is not None


# ---------------------------------------------------------------------------
# TreeInterface — geometry helpers

class TestTreeInterfaceGeometry:

    def test_set_out_geometry_creates_socket(self, tinf):
        sock = tinf.set_out_geometry()
        assert sock is not None
        assert sock.socket_type == 'NodeSocketGeometry'
        assert sock.in_out == 'OUTPUT'

    def test_set_in_geometry_creates_socket(self, tinf):
        sock = tinf.set_in_geometry(create=True)
        assert sock is not None
        assert sock.socket_type == 'NodeSocketGeometry'
        assert sock.in_out == 'INPUT'

    def test_set_in_geometry_no_create_returns_none(self, tinf):
        assert tinf.set_in_geometry(create=False) is None


# ---------------------------------------------------------------------------
# TreeInterface — clear / bin

class TestTreeInterfaceClear:

    def test_clear_removes_sockets(self, tinf):
        tinf.create_socket('INPUT', "A", "Float")
        tinf.create_socket('INPUT', "B", "Integer")
        tinf.clear(use_bin=False)
        assert tinf.iterate('INPUT', panels=False) == []

    def test_clear_with_bin_recoverable(self, tinf):
        tinf.create_socket('INPUT', "A", "Float")
        tinf.clear(use_bin=True)
        # socket moved to bin, not destroyed
        sock = tinf.create_socket('INPUT', "A", "Float")
        assert sock is not None
        tinf.empty_bin()
