"""Tests for core/signature.py."""
import pytest
from core.signature import Signature


# ---------------------------------------------------------------------------
# Construction

class TestSignatureConstruction:

    def test_empty(self):
        s = Signature()
        assert s.inputs == []
        assert s.outputs == []

    def test_from_none(self):
        s = Signature(None, None)
        assert s.inputs == []
        assert s.outputs == []

    def test_from_lists(self):
        inputs = [{'name': 'A', 'socket_type': 'NodeSocketFloat'}]
        s = Signature(inputs)
        assert len(s.inputs) == 1
        assert s.inputs[0]['name'] == 'A'

    def test_from_signature(self):
        s1 = Signature([{'name': 'A', 'socket_type': 'NodeSocketFloat'}])
        s2 = Signature(s1)
        assert s2.inputs[0]['name'] == 'A'
        assert s2.outputs == []

    def test_from_dict(self):
        s = Signature({'Value': 'NodeSocketFloat'})
        assert len(s.inputs) == 1
        assert s.inputs[0]['name'] == 'Value'

    def test_from_dict_with_socket_type(self):
        s = Signature({'Value': {'socket_type': 'NodeSocketFloat', 'name': 'Value'}})
        assert s.inputs[0]['name'] == 'Value'

    def test_inputs_and_outputs(self):
        inp = [{'name': 'In', 'socket_type': 'NodeSocketFloat'}]
        out = [{'name': 'Out', 'socket_type': 'NodeSocketFloat'}]
        s = Signature(inp, out)
        assert len(s.inputs) == 1
        assert len(s.outputs) == 1


# ---------------------------------------------------------------------------
# Names and keys

class TestSignatureNames:

    def test_input_names(self):
        s = Signature({'A': 'NodeSocketFloat', 'B': 'NodeSocketInt'})
        assert s.input_names == ['A', 'B']

    def test_output_names(self):
        s = Signature(None, {'Out': 'NodeSocketFloat'})
        assert s.output_names == ['Out']

    def test_input_keys_contain_socket_id(self):
        s = Signature({'Val': 'NodeSocketFloat'})
        keys = s.input_keys
        assert len(keys) == 1
        path, socket_id = keys[0]
        assert path == 'Val'
        assert socket_id == 'NodeSocketFloat'


# ---------------------------------------------------------------------------
# Indexing (dict-like behaviour)

class TestSignatureIndexing:

    def test_getitem_by_index(self):
        inp = [{'name': 'A', 'socket_type': 'NodeSocketFloat'}]
        out = [{'name': 'B', 'socket_type': 'NodeSocketFloat'}]
        s = Signature(inp, out)
        assert s[0] is s.inputs
        assert s[1] is s.outputs

    def test_getitem_by_key(self):
        s = Signature([{'name': 'A', 'socket_type': 'NodeSocketFloat'}])
        assert s['INPUT'] is s.inputs
        assert s['OUTPUT'] is s.outputs

    def test_setitem_input(self):
        s = Signature()
        s['INPUT'] = [{'name': 'X', 'socket_type': 'NodeSocketFloat'}]
        assert s.inputs[0]['name'] == 'X'

    def test_getitem_invalid_raises(self):
        with pytest.raises(IndexError):
            _ = Signature()[99]

    def test_len_is_2(self):
        assert len(Signature()) == 2

    def test_iter_yields_inputs_then_outputs(self):
        inp = [{'name': 'A', 'socket_type': 'NodeSocketFloat'}]
        out = [{'name': 'B', 'socket_type': 'NodeSocketFloat'}]
        s = Signature(inp, out)
        items = list(s)
        assert items[0] is s.inputs
        assert items[1] is s.outputs


# ---------------------------------------------------------------------------
# sockets property

class TestSignatureSockets:

    def test_sockets_returns_inputs_when_non_empty(self):
        s = Signature({'A': 'NodeSocketFloat'}, {'B': 'NodeSocketFloat'})
        assert s.sockets is s.inputs

    def test_sockets_returns_outputs_when_inputs_empty(self):
        s = Signature(None, {'B': 'NodeSocketFloat'})
        assert s.sockets is s.outputs


# ---------------------------------------------------------------------------
# switch

class TestSignatureSwitch:

    def test_switch_swaps_inputs_outputs(self):
        s = Signature({'A': 'NodeSocketFloat'}, {'B': 'NodeSocketFloat'})
        inp_before = s.inputs
        out_before = s.outputs
        s.switch()
        assert s.inputs is out_before
        assert s.outputs is inp_before


# ---------------------------------------------------------------------------
# join

class TestSignatureJoin:

    def test_join_merges_inputs(self):
        s1 = Signature({'A': 'NodeSocketFloat'})
        s2 = Signature({'B': 'NodeSocketFloat'})
        result = s1.join(s2)
        assert len(result.inputs) == 2

    def test_join_merges_outputs(self):
        s1 = Signature(None, {'A': 'NodeSocketFloat'})
        s2 = Signature(None, {'B': 'NodeSocketFloat'})
        result = s1.join(s2)
        assert len(result.outputs) == 2

    def test_join_deduplicates(self):
        s1 = Signature({'A': 'NodeSocketFloat'})
        s2 = Signature({'A': 'NodeSocketFloat'})
        result = s1.join(s2)
        assert len(result.inputs) == 1

    def test_add_operator(self):
        s1 = Signature({'A': 'NodeSocketFloat'})
        s2 = Signature({'B': 'NodeSocketFloat'})
        result = s1 + s2
        assert len(result.inputs) == 2


# ---------------------------------------------------------------------------
# _load_value — error handling

class TestSignatureLoadValueErrors:

    def test_non_dict_in_list_raises(self):
        with pytest.raises(RuntimeError):
            Signature(["not_a_dict"])

    def test_dict_without_socket_type_raises(self):
        with pytest.raises(RuntimeError):
            Signature([{'name': 'X'}])

    def test_error_message_contains_name(self):
        with pytest.raises(RuntimeError, match="X"):
            Signature([{'name': 'X'}])
