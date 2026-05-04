"""Tests for core/geometry_class.py and core/geometries.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.nodeclass import Node
from core.geometry_class import Geometry
from core.geometries import Mesh, Curve, Cloud, Instances, GreasePencil, Volume
from core.domains import Vertex, Edge, Face, Corner, SplinePoint, Spline, CloudPoint, Instance, Layer


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


def make_geo_sock(tree_name, geo_class=None):
    """Helper: open a tree, create a GEOMETRY input socket, wrap with geo_class."""
    tree = Tree(tree_name, "GeometryNodeTree").__enter__()
    sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
    cls = geo_class if geo_class is not None else Geometry
    return tree, cls(sock)


# ---------------------------------------------------------------------------
# geometry_class — Geometry base

class TestGeometryBase:

    def test_geometry_importable(self):
        import core.geometry_class
        assert hasattr(core.geometry_class, 'Geometry')

    def test_no_arguments_import(self):
        import core.geometry_class
        assert not hasattr(core.geometry_class, 'Arguments')

    def test_out_old_removed(self):
        assert not hasattr(Geometry, 'out_OLD')

    def test_geometry_socket_type(self):
        assert Geometry.SOCKET_TYPE == 'GEOMETRY'

    def test_geometry_geo_is_self(self):
        with Tree("_test_geo_self", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = Geometry(sock)
            assert geo._geo is geo

    def test_geometry_selection_initially_none(self):
        with Tree("_test_geo_sel", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            geo = Geometry(sock)
            assert geo._selection is None

    def test_geometry_add_returns_geometry(self):
        with Tree("_test_geo_add", "GeometryNodeTree") as tree:
            s1 = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo1')
            s2 = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo2')
            geo1 = Geometry(s1)
            geo2 = Geometry(s2)
            result = geo1 + geo2
            assert isinstance(result, Geometry)

    def test_geometry_iadd_updates_socket(self):
        with Tree("_test_geo_iadd", "GeometryNodeTree") as tree:
            s1 = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo1')
            s2 = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo2')
            geo1 = Geometry(s1)
            geo2 = Geometry(s2)
            original_sock = geo1._bsocket
            geo1 += geo2
            assert geo1._bsocket is not original_sock


# ---------------------------------------------------------------------------
# geometries — import smoke test

class TestGeometriesImport:

    def test_no_arguments_import(self):
        import core.geometries
        assert not hasattr(core.geometries, 'Arguments')

    def test_mesh_importable(self):
        assert Mesh is not None

    def test_curve_importable(self):
        assert Curve is not None

    def test_cloud_importable(self):
        assert Cloud is not None

    def test_instances_importable(self):
        assert Instances is not None

    def test_grease_pencil_importable(self):
        assert GreasePencil is not None

    def test_volume_importable(self):
        assert Volume is not None


# ---------------------------------------------------------------------------
# Mesh domains

class TestMeshDomains:

    def _make_mesh(self, tree):
        sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
        return Mesh(sock)

    def test_mesh_has_points(self):
        with Tree("_test_mesh_pts", "GeometryNodeTree") as tree:
            mesh = self._make_mesh(tree)
            assert isinstance(mesh.points, Vertex)

    def test_mesh_has_edges(self):
        with Tree("_test_mesh_edges", "GeometryNodeTree") as tree:
            mesh = self._make_mesh(tree)
            assert isinstance(mesh.edges, Edge)

    def test_mesh_has_faces(self):
        with Tree("_test_mesh_faces", "GeometryNodeTree") as tree:
            mesh = self._make_mesh(tree)
            assert isinstance(mesh.faces, Face)

    def test_mesh_has_corners(self):
        with Tree("_test_mesh_corners", "GeometryNodeTree") as tree:
            mesh = self._make_mesh(tree)
            assert isinstance(mesh.corners, Corner)

    def test_mesh_points_geo_is_mesh(self):
        with Tree("_test_mesh_dom_geo", "GeometryNodeTree") as tree:
            mesh = self._make_mesh(tree)
            assert mesh.points._geo is mesh

    def test_mesh_jump_resets_domains(self):
        with Tree("_test_mesh_jump_reset", "GeometryNodeTree") as tree:
            s1 = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo1')
            s2 = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geo2')
            mesh = Mesh(s1)
            old_points = mesh.points
            mesh._jump(s2)
            assert mesh.points is not old_points


# ---------------------------------------------------------------------------
# Mesh boolean operators

class TestMeshOperators:

    def _make_mesh(self, tree, name='Geometry'):
        sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', name)
        return Mesh(sock)

    def test_mesh_sub_returns_mesh(self):
        with Tree("_test_mesh_sub", "GeometryNodeTree") as tree:
            m1 = self._make_mesh(tree, 'Geo1')
            m2 = self._make_mesh(tree, 'Geo2')
            result = m1 - m2
            assert isinstance(result, Mesh)

    def test_mesh_truediv_returns_mesh(self):
        with Tree("_test_mesh_div", "GeometryNodeTree") as tree:
            m1 = self._make_mesh(tree, 'Geo1')
            m2 = self._make_mesh(tree, 'Geo2')
            result = m1 / m2
            assert isinstance(result, Mesh)

    def test_mesh_mul_returns_mesh(self):
        with Tree("_test_mesh_mul", "GeometryNodeTree") as tree:
            m1 = self._make_mesh(tree, 'Geo1')
            m2 = self._make_mesh(tree, 'Geo2')
            result = m1 * m2
            assert isinstance(result, Mesh)


# ---------------------------------------------------------------------------
# Curve domains

class TestCurveDomains:

    def _make_curve(self, tree):
        sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
        return Curve(sock)

    def test_curve_has_points(self):
        with Tree("_test_curve_pts", "GeometryNodeTree") as tree:
            curve = self._make_curve(tree)
            assert isinstance(curve.points, SplinePoint)

    def test_curve_has_splines(self):
        with Tree("_test_curve_splines", "GeometryNodeTree") as tree:
            curve = self._make_curve(tree)
            assert isinstance(curve.splines, Spline)

    def test_curve_points_geo_is_curve(self):
        with Tree("_test_curve_dom_geo", "GeometryNodeTree") as tree:
            curve = self._make_curve(tree)
            assert curve.points._geo is curve


# ---------------------------------------------------------------------------
# Cloud domains

class TestCloudDomains:

    def test_cloud_has_points(self):
        with Tree("_test_cloud_pts", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            cloud = Cloud(sock)
            assert isinstance(cloud.points, CloudPoint)

    def test_cloud_points_geo_is_cloud(self):
        with Tree("_test_cloud_dom_geo", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            cloud = Cloud(sock)
            assert cloud.points._geo is cloud


# ---------------------------------------------------------------------------
# Instances domains

class TestInstancesDomains:

    def test_instances_has_insts(self):
        with Tree("_test_inst_insts", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            insts = Instances(sock)
            assert isinstance(insts.insts, Instance)

    def test_instances_insts_geo_is_instances(self):
        with Tree("_test_inst_dom_geo", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            insts = Instances(sock)
            assert insts.insts._geo is insts


# ---------------------------------------------------------------------------
# GreasePencil domains

class TestGreasePencilDomains:

    def test_greasepencil_has_layers(self):
        with Tree("_test_gp_layers", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            gp = GreasePencil(sock)
            assert isinstance(gp.layers, Layer)

    def test_greasepencil_layers_geo_is_gp(self):
        with Tree("_test_gp_dom_geo", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            gp = GreasePencil(sock)
            assert gp.layers._geo is gp


# ---------------------------------------------------------------------------
# Volume (no domains)

class TestVolume:

    def test_volume_creates(self):
        with Tree("_test_vol_create", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            vol = Volume(sock)
            assert vol is not None

    def test_volume_is_geometry(self):
        with Tree("_test_vol_geo", "GeometryNodeTree") as tree:
            sock = tree.input_node.create_socket('OUTPUT', 'GEOMETRY', 'Geometry')
            vol = Volume(sock)
            assert isinstance(vol, Geometry)
