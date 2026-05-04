"""Tests for core/domains.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.nodeclass import Node
from core.geometries import Mesh, Curve, Cloud, Instances, GreasePencil
from core.domains import (
    Point, Vertex, SplinePoint, CloudPoint,
    Face, Edge, Corner, Spline, Layer, Instance,
)
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


def geo_sock(tree, socket_type='GEOMETRY', name='Geometry'):
    return tree.input_node.create_socket('OUTPUT', socket_type, name)


# ---------------------------------------------------------------------------
# Import / dead code checks

class TestDomainsImport:

    def test_domains_importable(self):
        import core.domains
        assert hasattr(core.domains, 'Vertex')

    def test_no_constants_import(self):
        import core.domains
        assert not hasattr(core.domains, 'constants')

    def test_no_utils_import(self):
        import core.domains
        assert not hasattr(core.domains, 'utils')


# ---------------------------------------------------------------------------
# DOMAIN_NAME values

class TestDomainNames:

    def test_vertex_domain_name(self):
        assert Vertex.DOMAIN_NAME == 'POINT'

    def test_splinepoint_domain_name(self):
        assert SplinePoint.DOMAIN_NAME == 'POINT'

    def test_cloudpoint_domain_name(self):
        assert CloudPoint.DOMAIN_NAME == 'POINT'

    def test_face_domain_name(self):
        assert Face.DOMAIN_NAME == 'FACE'

    def test_edge_domain_name(self):
        assert Edge.DOMAIN_NAME == 'EDGE'

    def test_corner_domain_name(self):
        assert Corner.DOMAIN_NAME == 'CORNER'

    def test_spline_domain_name(self):
        assert Spline.DOMAIN_NAME == 'CURVE'

    def test_layer_domain_name(self):
        assert Layer.DOMAIN_NAME == 'LAYER'

    def test_instance_domain_name(self):
        assert Instance.DOMAIN_NAME == 'INSTANCE'


# ---------------------------------------------------------------------------
# count properties (smoke-test: node is created without error)

class TestCountProperties:

    def test_vertex_count_creates_node(self):
        with Tree("_test_dom_vtx_count", "GeometryNodeTree") as tree:
            mesh = Mesh(geo_sock(tree))
            _ = mesh.points.count

    def test_face_count_creates_node(self):
        with Tree("_test_dom_face_count", "GeometryNodeTree") as tree:
            mesh = Mesh(geo_sock(tree))
            _ = mesh.faces.count

    def test_edge_count_creates_node(self):
        with Tree("_test_dom_edge_count", "GeometryNodeTree") as tree:
            mesh = Mesh(geo_sock(tree))
            _ = mesh.edges.count

    def test_corner_count_creates_node(self):
        with Tree("_test_dom_corner_count", "GeometryNodeTree") as tree:
            mesh = Mesh(geo_sock(tree))
            _ = mesh.corners.count

    def test_spline_count_creates_node(self):
        with Tree("_test_dom_spline_count", "GeometryNodeTree") as tree:
            curve = Curve(geo_sock(tree))
            _ = curve.splines.count

    def test_cloudpoint_count_creates_node(self):
        with Tree("_test_dom_cloud_count", "GeometryNodeTree") as tree:
            cloud = Cloud(geo_sock(tree))
            _ = cloud.points.count

    def test_instance_count_creates_node(self):
        with Tree("_test_dom_inst_count", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            _ = insts.insts.count

    def test_layer_count_creates_node(self):
        with Tree("_test_dom_layer_count", "GeometryNodeTree") as tree:
            gp = GreasePencil(geo_sock(tree))
            _ = gp.layers.count


# ---------------------------------------------------------------------------
# Edge.to_face_groups

class TestEdgeToFaceGroups:

    def test_to_face_groups_creates_node(self):
        with Tree("_test_dom_tfg", "GeometryNodeTree") as tree:
            mesh = Mesh(geo_sock(tree))
            result = mesh.edges.to_face_groups
            assert result is not None


# ---------------------------------------------------------------------------
# Instance.scale setter — validation (was broken: k not in keys is None)

class TestInstanceScaleSetter:

    def test_scale_setter_scalar_no_error(self):
        with Tree("_test_inst_scale_scalar", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            insts.insts.scale = 1.0  # should not raise

    def test_scale_setter_dict_valid_key(self):
        with Tree("_test_inst_scale_dict_ok", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            insts.insts.scale = {'Scale': 2.0}  # valid key — should not raise

    def test_scale_setter_dict_invalid_key_raises(self):
        with Tree("_test_inst_scale_dict_bad", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            with pytest.raises(NodeError):
                insts.insts.scale = {'BadKey': 2.0}  # was never raised before fix

    def test_scale_getter_creates_node(self):
        with Tree("_test_inst_scale_get", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            result = insts.insts.scale
            assert result is not None


# ---------------------------------------------------------------------------
# Instance.rotation setter — validation

class TestInstanceRotationSetter:

    def test_rotation_setter_scalar_no_error(self):
        with Tree("_test_inst_rot_scalar", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            insts.insts.rotation = (0, 0, 0)  # should not raise

    def test_rotation_setter_dict_valid_key(self):
        with Tree("_test_inst_rot_dict_ok", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            insts.insts.rotation = {'Rotation': (0, 0, 0)}  # valid key

    def test_rotation_setter_dict_invalid_key_raises(self):
        with Tree("_test_inst_rot_dict_bad", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            with pytest.raises(NodeError):
                insts.insts.rotation = {'BadKey': (0, 0, 0)}

    def test_rotation_getter_creates_node(self):
        with Tree("_test_inst_rot_get", "GeometryNodeTree") as tree:
            insts = Instances(geo_sock(tree))
            result = insts.insts.rotation
            assert result is not None
