"""Tests for core/constants.py."""
import pytest
from core import constants


# ---------------------------------------------------------------------------
# Structure de ARRAY_TYPES

class TestArrayTypes:

    def test_required_keys_present(self):
        required = {'shape', 'combine', 'init'}
        for name, spec in constants.ARRAY_TYPES.items():
            missing = required - spec.keys()
            assert not missing, f"ARRAY_TYPES['{name}'] manque : {missing}"

    def test_shapes_are_tuples(self):
        for name, spec in constants.ARRAY_TYPES.items():
            assert isinstance(spec['shape'], tuple), f"ARRAY_TYPES['{name}']['shape'] doit être un tuple"

    def test_known_entries_exist(self):
        for key in ('VECTOR', 'ROTATION', 'RGBA', 'MATRIX'):
            assert key in constants.ARRAY_TYPES

    def test_vector_shape(self):
        assert constants.ARRAY_TYPES['VECTOR']['shape'] == (3,)

    def test_rgba_shape(self):
        assert constants.ARRAY_TYPES['RGBA']['shape'] == (4,)

    def test_matrix_shape(self):
        assert constants.ARRAY_TYPES['MATRIX']['shape'] == (16,)


# ---------------------------------------------------------------------------
# Structure de PAIRED_NODES

class TestPairedNodes:

    def test_values_are_strings(self):
        for k, v in constants.PAIRED_NODES.items():
            assert isinstance(v, str), f"PAIRED_NODES['{k}'] doit être une str"

    def test_no_self_pairing(self):
        for k, v in constants.PAIRED_NODES.items():
            assert k != v, f"PAIRED_NODES['{k}'] pointe sur lui-même"

    def test_known_pairs(self):
        assert 'GeometryNodeRepeatOutput' in constants.PAIRED_NODES
        assert constants.PAIRED_NODES['GeometryNodeRepeatOutput'] == 'GeometryNodeRepeatInput'


# ---------------------------------------------------------------------------
# Structure de NODE_WITH_IN_ITEMS

class TestNodeWithInItems:

    def test_values_are_strings(self):
        for k, v in constants.NODE_WITH_IN_ITEMS.items():
            assert isinstance(v, str), f"NODE_WITH_IN_ITEMS['{k}'] doit être une str"


# ---------------------------------------------------------------------------
# TOOL_ONLY / MODIFIER_ONLY

class TestToolAndModifierOnly:

    def test_no_overlap(self):
        overlap = set(constants.TOOL_ONLY) & set(constants.MODIFIER_ONLY)
        assert not overlap, f"Nœuds présents dans TOOL_ONLY et MODIFIER_ONLY : {overlap}"


# ---------------------------------------------------------------------------
# Constantes scalaires

class TestScalarConstants:

    def test_global_debug_is_bool(self):
        assert isinstance(constants.GLOBAL_DEBUG, bool)

    def test_global_debug_off_by_default(self):
        assert constants.GLOBAL_DEBUG is False

    def test_empty_socket_is_str(self):
        assert isinstance(constants.EMPTY_SOCKET, str)
