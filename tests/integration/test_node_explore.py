"""Tests for generation/node_explore.py — requires Blender."""
import pytest
import bpy

import geonodes  # ensures the geonodes package is fully initialised before relative imports
from geonodes.generation import node_explore as ne
from geonodes.generation.node_explore import NodeInfo, NodeParam
from geonodes.generation import blendertree


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture
def gn_btree():
    btree = blendertree.get_tree("_test_ne_tree", tree_type='GeometryNodeTree', create=True)
    btree.nodes.clear()
    yield btree
    blendertree.del_tree(btree)


@pytest.fixture
def sh_btree():
    btree = blendertree.get_tree("_test_ne_sh_tree", tree_type='ShaderNodeTree', create=True)
    btree.nodes.clear()
    yield btree
    blendertree.del_tree(btree)


# ---------------------------------------------------------------------------
# Import checks

class TestNodeExploreImport:

    def test_importable(self):
        assert hasattr(ne, 'NodeInfo')
        assert hasattr(ne, 'NodeParam')

    def test_no_path_import(self):
        assert not hasattr(ne, 'Path')

    def test_pprint_present(self):
        assert hasattr(ne, 'pprint')

    def test_pformat_present(self):
        assert hasattr(ne, 'pformat')

    def test_inspect_present(self):
        assert hasattr(ne, 'inspect')


# ---------------------------------------------------------------------------
# NodeParam

class TestNodeParam:

    def test_parameter_returns_none_for_ignore(self, gn_btree):
        bnode = gn_btree.nodes.new(type='ShaderNodeValue')
        result = NodeParam.Parameter(bnode, 'color_ramp')
        gn_btree.nodes.remove(bnode)
        assert result is None

    def test_parameter_returns_none_for_object(self, gn_btree):
        bnode = gn_btree.nodes.new(type='ShaderNodeValue')
        result = NodeParam.Parameter(bnode, 'color')
        gn_btree.nodes.remove(bnode)
        # color is an object-type attr, should return None
        assert result is None

    def test_parameter_for_value(self, gn_btree):
        bnode = gn_btree.nodes.new(type='ShaderNodeValue')
        # width is a float attribute
        result = NodeParam.Parameter(bnode, 'width')
        gn_btree.nodes.remove(bnode)
        assert result is not None

    def test_param_str(self, gn_btree):
        bnode = gn_btree.nodes.new(type='ShaderNodeValue')
        result = NodeParam.Parameter(bnode, 'width')
        gn_btree.nodes.remove(bnode)
        assert isinstance(str(result), str)

    def test_get_enum_list_non_enum(self, gn_btree):
        bnode = gn_btree.nodes.new(type='ShaderNodeValue')
        param = NodeParam.Parameter(bnode, 'width')
        gn_btree.nodes.remove(bnode)
        if param is not None:
            assert param.param_type != 'ENUM'


# ---------------------------------------------------------------------------
# NodeInfo creation

class TestNodeInfoCreation:

    def test_wrap_by_bnode(self, gn_btree):
        bnode = gn_btree.nodes.new(type='GeometryNodeInputPosition')
        info = NodeInfo(gn_btree, bnode)
        assert info is not None
        assert info.bnode is bnode

    def test_wrap_by_name(self, gn_btree):
        info = NodeInfo(gn_btree, 'Position')
        assert info is not None

    def test_is_gnodes(self, gn_btree):
        info = NodeInfo(gn_btree, 'Position')
        assert info.is_gnodes is True
        assert info.is_shader is False

    def test_is_shader(self, sh_btree):
        bnode = sh_btree.nodes.new(type='ShaderNodeValue')
        info = NodeInfo(sh_btree, bnode)
        assert info.is_shader is True
        assert info.is_gnodes is False

    def test_params_is_dict(self, gn_btree):
        bnode = gn_btree.nodes.new(type='GeometryNodeInputPosition')
        info = NodeInfo(gn_btree, bnode)
        assert isinstance(info.params, dict)

    def test_enum_params_is_dict(self, gn_btree):
        bnode = gn_btree.nodes.new(type='GeometryNodeInputPosition')
        info = NodeInfo(gn_btree, bnode)
        assert isinstance(info.enum_params, dict)


# ---------------------------------------------------------------------------
# NodeInfo sockets

class TestNodeInfoSockets:

    def test_input_sockets(self, gn_btree):
        info = NodeInfo(gn_btree, 'Set Position')
        sockets = info.get_in_sockets()
        assert isinstance(sockets, list)

    def test_enabled_input_sockets(self, gn_btree):
        info = NodeInfo(gn_btree, 'Set Position')
        assert isinstance(info.enabled_input_sockets, dict)

    def test_enabled_output_sockets(self, gn_btree):
        info = NodeInfo(gn_btree, 'Set Position')
        assert isinstance(info.enabled_output_sockets, dict)

    def test_get_input_socket(self, gn_btree):
        info = NodeInfo(gn_btree, 'Set Position')
        socket = info.get_input_socket('Geometry')
        assert socket is not None


# ---------------------------------------------------------------------------
# NodeInfo.get_nodes — scans the full node set

class TestNodeInfoGetNodes:

    def test_get_nodes_geonodes(self):
        nodes = NodeInfo.get_nodes('GeometryNodeTree')
        assert isinstance(nodes, dict)
        assert len(nodes) > 0

    def test_get_nodes_shader(self):
        nodes = NodeInfo.get_nodes('ShaderNodeTree')
        assert isinstance(nodes, dict)
        assert len(nodes) > 0

    def test_nodes_have_string_values(self):
        nodes = NodeInfo.get_nodes('GeometryNodeTree')
        for blid, name in nodes.items():
            assert isinstance(blid, str)
            assert isinstance(name, str)

    def test_position_node_present(self):
        nodes = NodeInfo.get_nodes('GeometryNodeTree')
        assert 'GeometryNodeInputPosition' in nodes


# ---------------------------------------------------------------------------
# NodeInfo.get_data_type_sockets

class TestNodeInfoGetDataTypeSockets:

    def test_returns_none_for_position(self, gn_btree):
        info = NodeInfo(gn_btree, 'Position')
        result = info.get_data_type_sockets()
        assert result is None

    def test_returns_dict_for_random_value(self, gn_btree):
        info = NodeInfo(gn_btree, 'Random Value')
        result = info.get_data_type_sockets()
        assert result is not None
        assert isinstance(result, dict)
        assert 'param_name' in result
        assert 'in_sockets' in result
        assert 'out_sockets' in result
        assert 'value_to_type' in result
