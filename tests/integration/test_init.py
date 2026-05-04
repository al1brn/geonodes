"""Tests for geonodes/__init__.py and core/__init__.py — requires Blender."""
import pytest
import math
import bpy

from core.treeclass import Tree


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture(autouse=True)
def clean_tree_stack():
    Tree.TREE_STACK.clear()
    yield
    Tree.TREE_STACK.clear()


# ---------------------------------------------------------------------------
# geonodes top-level package

class TestGeonodesPackage:

    def test_importable(self):
        import geonodes
        assert geonodes is not None

    def test_exports_geo_nodes_class(self):
        import geonodes
        assert hasattr(geonodes, 'GeoNodes')

    def test_exports_shader_nodes_class(self):
        import geonodes
        assert hasattr(geonodes, 'ShaderNodes')

    def test_exports_tree(self):
        import geonodes
        assert hasattr(geonodes, 'Tree')

    def test_exports_node(self):
        import geonodes
        assert hasattr(geonodes, 'Node')

    def test_exports_socket_types(self):
        import geonodes
        for name in ('Boolean', 'Float', 'Integer', 'Vector', 'Rotation',
                     'Matrix', 'Color', 'String', 'Shader', 'VolumeShader'):
            assert hasattr(geonodes, name), f"geonodes.{name} missing"

    def test_exports_geometry_types(self):
        import geonodes
        for name in ('Geometry', 'Mesh', 'Curve', 'Cloud', 'Instances',
                     'GreasePencil', 'Volume'):
            assert hasattr(geonodes, name), f"geonodes.{name} missing"

    def test_exports_nd(self):
        import geonodes
        assert hasattr(geonodes, 'nd')

    def test_exports_snd(self):
        import geonodes
        assert hasattr(geonodes, 'snd')

    def test_exports_gnmath(self):
        import geonodes
        assert hasattr(geonodes, 'gnmath')

    def test_exports_layout(self):
        import geonodes
        assert hasattr(geonodes, 'Layout')

    def test_exports_group(self):
        import geonodes
        assert hasattr(geonodes, 'Group')


# ---------------------------------------------------------------------------
# Math constants in geonodes

class TestGeonodesMathConstants:

    def test_pi(self):
        import geonodes
        assert abs(geonodes.pi - math.pi) < 1e-10

    def test_tau(self):
        import geonodes
        assert abs(geonodes.tau - 2 * math.pi) < 1e-10

    def test_halfpi(self):
        import geonodes
        assert abs(geonodes.halfpi - math.pi / 2) < 1e-10

    def test_e(self):
        import geonodes
        assert abs(geonodes.e - math.e) < 1e-10

    def test_d30(self):
        import geonodes
        assert abs(geonodes.d30 - math.pi / 6) < 1e-10

    def test_d45(self):
        import geonodes
        assert abs(geonodes.d45 - math.pi / 4) < 1e-10

    def test_d60(self):
        import geonodes
        assert abs(geonodes.d60 - math.pi / 3) < 1e-10

    def test_d90(self):
        import geonodes
        assert abs(geonodes.d90 - math.pi / 2) < 1e-10

    def test_d180(self):
        import geonodes
        assert abs(geonodes.d180 - math.pi) < 1e-10

    def test_d360(self):
        import geonodes
        assert abs(geonodes.d360 - 2 * math.pi) < 1e-10


# ---------------------------------------------------------------------------
# core package

class TestCorePackage:

    def test_importable(self):
        import core
        assert core is not None

    def test_production_flag(self):
        import core
        assert core.PRODUCTION is True

    def test_version_string(self):
        import core
        assert isinstance(core.version, str)
        assert len(core.version) > 0

    def test_math_constants(self):
        import core
        assert abs(core.pi - math.pi) < 1e-10

    def test_exports_socket_classes(self):
        import core
        assert hasattr(core, 'Boolean')
        assert hasattr(core, 'Float')
        assert hasattr(core, 'Integer')
        assert hasattr(core, 'Vector')


# ---------------------------------------------------------------------------
# SOCKET_CLASSES dict

class TestSocketClassesDict:

    def test_socket_classes_populated(self):
        from core.utils import SOCKET_CLASSES
        assert len(SOCKET_CLASSES) > 0

    def test_geometry_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.geometry_class import Geometry
        assert SOCKET_CLASSES.get('GEOMETRY') is Geometry

    def test_boolean_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_boolean import Boolean
        assert SOCKET_CLASSES.get('BOOLEAN') is Boolean

    def test_float_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_float import Float
        assert SOCKET_CLASSES.get('VALUE') is Float

    def test_integer_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_integer import Integer
        assert SOCKET_CLASSES.get('INT') is Integer

    def test_vector_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_vector import Vector
        assert SOCKET_CLASSES.get('VECTOR') is Vector

    def test_color_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_color import Color
        assert SOCKET_CLASSES.get('RGBA') is Color

    def test_string_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_string import String
        assert SOCKET_CLASSES.get('STRING') is String

    def test_shader_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_shader import Shader
        assert SOCKET_CLASSES.get('SHADER') is Shader

    def test_rotation_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_rotation import Rotation
        assert SOCKET_CLASSES.get('ROTATION') is Rotation

    def test_matrix_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_matrix import Matrix
        assert SOCKET_CLASSES.get('MATRIX') is Matrix

    def test_image_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_image import Image
        assert SOCKET_CLASSES.get('IMAGE') is Image

    def test_object_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_object import Object
        assert SOCKET_CLASSES.get('OBJECT') is Object

    def test_material_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_material import Material
        assert SOCKET_CLASSES.get('MATERIAL') is Material

    def test_collection_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_collection import Collection
        assert SOCKET_CLASSES.get('COLLECTION') is Collection

    def test_font_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_font import Font
        assert SOCKET_CLASSES.get('FONT') is Font

    def test_menu_registered(self):
        from core.utils import SOCKET_CLASSES
        from core.sock_menu import Menu
        assert SOCKET_CLASSES.get('MENU') is Menu


# ---------------------------------------------------------------------------
# GEOMETRY_CLASSES dict

class TestGeometryClassesDict:

    def test_geometry_classes_populated(self):
        from core.utils import GEOMETRY_CLASSES
        assert len(GEOMETRY_CLASSES) > 0

    def test_geometry_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometry_class import Geometry
        assert GEOMETRY_CLASSES.get('Geometry') is Geometry

    def test_mesh_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometries import Mesh
        assert GEOMETRY_CLASSES.get('Mesh') is Mesh

    def test_curve_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometries import Curve
        assert GEOMETRY_CLASSES.get('Curve') is Curve

    def test_cloud_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometries import Cloud
        assert GEOMETRY_CLASSES.get('Cloud') is Cloud

    def test_instances_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometries import Instances
        assert GEOMETRY_CLASSES.get('Instances') is Instances

    def test_greasepencil_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometries import GreasePencil
        assert GEOMETRY_CLASSES.get('GreasePencil') is GreasePencil

    def test_volume_registered(self):
        from core.utils import GEOMETRY_CLASSES
        from core.geometries import Volume
        assert GEOMETRY_CLASSES.get('Volume') is Volume
