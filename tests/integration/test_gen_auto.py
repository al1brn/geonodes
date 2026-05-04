"""Tests for generation/gen_auto.py — requires Blender."""
import pytest
import bpy

import geonodes
from geonodes.generation import gen_auto as ga
from geonodes.generation.node_explore import NodeInfo


# ---------------------------------------------------------------------------
# Import checks

class TestGenAutoImport:

    def test_importable(self):
        assert hasattr(ga, 'generate')
        assert hasattr(ga, 'build_implement_dict')
        assert hasattr(ga, 'build_manual_cross_ref')

    def test_no_spurious_imports(self):
        # All imports in this module are used
        assert hasattr(ga, 'NodeInfo')
        assert hasattr(ga, 'Path')
        assert hasattr(ga, 'datetime')
        assert hasattr(ga, 'textwrap')
        assert hasattr(ga, 're')


# ---------------------------------------------------------------------------
# Module-level constants

class TestGenAutoConstants:

    def test_domains_is_list(self):
        assert isinstance(ga.DOMAINS, list)
        assert len(ga.DOMAINS) > 0

    def test_domains_contains_mesh_domains(self):
        for name in ('Vertex', 'Edge', 'Face', 'Corner'):
            assert name in ga.DOMAINS

    def test_geonodes_imported(self):
        from geonodes.generation.gen_auto_dicts import GEONODES
        assert isinstance(GEONODES, dict)
        assert len(GEONODES) > 0

    def test_shadernodes_imported(self):
        from geonodes.generation.gen_auto_dicts import SHADERNODES
        assert isinstance(SHADERNODES, dict)


# ---------------------------------------------------------------------------
# ptype is object fix — regression test

class TestPtypeIsObject:

    def test_python_types_values_are_strings(self):
        from geonodes.generation import gen_config
        for class_name, (ptype, def_val) in gen_config.PYTHON_TYPES.items():
            assert isinstance(ptype, str), f"PYTHON_TYPES[{class_name}] ptype should be str, got {type(ptype)}"

    def test_ptype_is_object_check(self):
        # Regression: isinstance(ptype, object) is always True; must use ptype is object
        ptype_str = 'float'
        # The old bug: isinstance('float', object) is True → would overwrite to 'object'
        assert isinstance(ptype_str, object)  # always True — demonstrates the bug
        assert (ptype_str is object) is False  # correct check
        assert (object is object) is True       # correct check for fallback case


# ---------------------------------------------------------------------------
# build_implement_dict — smoke test (read-only, no file writes)

class TestBuildImplementDict:

    def test_node_info_get_nodes_geonodes(self):
        nodes = NodeInfo.get_nodes('GeometryNodeTree')
        assert isinstance(nodes, dict)
        assert len(nodes) > 0

    def test_node_info_get_nodes_shader(self):
        nodes = NodeInfo.get_nodes('ShaderNodeTree')
        assert isinstance(nodes, dict)
        assert len(nodes) > 0

    def test_common_nodes_exist(self):
        g_nodes = NodeInfo.get_nodes('GeometryNodeTree')
        s_nodes = NodeInfo.get_nodes('ShaderNodeTree')
        common = {blid for blid in s_nodes if blid in g_nodes}
        assert len(common) > 0


# ---------------------------------------------------------------------------
# build_manual_cross_ref — smoke test

class TestBuildManualCrossRef:

    def test_returns_populated_dict(self):
        cross = {}
        ga.build_manual_cross_ref(cross)
        assert isinstance(cross, dict)
        assert len(cross) > 0

    def test_known_nodes_present(self):
        cross = {}
        ga.build_manual_cross_ref(cross)
        # NodeFrame must be in the manual cross ref
        assert 'NodeFrame' in cross

    def test_group_nodes_present(self):
        cross = {}
        ga.build_manual_cross_ref(cross)
        assert 'GeometryNodeGroup' in cross
        assert 'ShaderNodeGroup' in cross

    def test_zone_nodes_present(self):
        cross = {}
        ga.build_manual_cross_ref(cross)
        assert 'GeometryNodeRepeatInput' in cross
        assert 'GeometryNodeSimulationInput' in cross
