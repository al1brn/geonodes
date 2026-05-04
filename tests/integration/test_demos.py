"""Smoke tests for demos/ — requires Blender.

Each test: run the demo, verify no exception, verify key trees exist.
Cleanup: all node groups / materials created during the test are removed.
"""
import pytest
import bpy

from core.treeclass import Tree


# ---------------------------------------------------------------------------
# Fixtures

@pytest.fixture(autouse=True)
def clean_tree_stack():
    Tree.TREE_STACK.clear()
    yield
    Tree.TREE_STACK.clear()


@pytest.fixture
def clean_after():
    """Remove node groups and materials created during the test."""
    before_groups = set(bpy.data.node_groups.keys())
    before_mats   = set(bpy.data.materials.keys())
    yield
    for name in list(bpy.data.node_groups.keys()):
        if name not in before_groups:
            try:
                bpy.data.node_groups.remove(bpy.data.node_groups[name])
            except Exception:
                pass
    for name in list(bpy.data.materials.keys()):
        if name not in before_mats:
            try:
                bpy.data.materials.remove(bpy.data.materials[name])
            except Exception:
                pass


def assert_tree(name):
    tree = bpy.data.node_groups.get(name)
    assert tree is not None, f"Node group '{name}' was not created"
    assert len(tree.nodes) > 0, f"Node group '{name}' is empty"


def assert_material(name):
    mat = bpy.data.materials.get(name)
    assert mat is not None, f"Material '{name}' was not created"


# ---------------------------------------------------------------------------
# Simple / fast demos

class TestDemoExamples:

    def test_runs(self, clean_after):
        from geonodes.demos import examples
        examples.demo()

    def test_hello_world_tree(self, clean_after):
        from geonodes.demos import examples
        examples.demo()
        assert_tree("Doc Hello World")

    def test_several_trees_created(self, clean_after):
        from geonodes.demos import examples
        before = set(bpy.data.node_groups.keys())
        examples.demo()
        after = set(bpy.data.node_groups.keys())
        assert len(after - before) >= 5


class TestDemoGizmo:

    def test_runs(self, clean_after):
        from geonodes.demos import gizmo
        gizmo.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import gizmo
        gizmo.demo()
        assert_tree("Gizmo Demo")


class TestDemoGravity:

    def test_runs(self, clean_after):
        from geonodes.demos import gravity
        gravity.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import gravity
        gravity.demo()
        assert_tree("Gravity")


class TestDemoSimulation:

    def test_runs(self, clean_after):
        from geonodes.demos import simulation
        simulation.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import simulation
        simulation.demo()
        assert_tree("Transformation")


class TestDemoCurly:

    def test_runs(self, clean_after):
        from geonodes.demos import curly
        curly.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import curly
        curly.demo()
        assert_tree("Frise")


class TestDemoRandom:

    def test_runs(self, clean_after):
        from geonodes.demos import random
        random.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import random
        random.demo()
        assert_tree("Random Uniform Value")


class TestDemoRain:

    def test_single_wave_runs(self, clean_after):
        from geonodes.demos import rain
        rain.single_wave()

    def test_single_wave_tree(self, clean_after):
        from geonodes.demos import rain
        rain.single_wave()
        assert_tree("Single Wave")

    def test_demo_runs(self, clean_after):
        from geonodes.demos import rain
        rain.demo()

    def test_demo_tree(self, clean_after):
        from geonodes.demos import rain
        rain.demo()
        assert_tree("Rain")


class TestDemoFractal:

    def test_runs(self, clean_after):
        from geonodes.demos import fractal
        fractal.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import fractal
        fractal.demo()
        assert_tree("Fractal Mesh")


class TestDemoUtilities:

    def test_runs(self, clean_after):
        from geonodes import GeoNodes
        from geonodes.demos import utilities
        with GeoNodes("_test_dichotomy_host", is_group=True):
            utilities.dichotomy()

    def test_tree_created(self, clean_after):
        from geonodes import GeoNodes
        from geonodes.demos import utilities
        with GeoNodes("_test_dichotomy_host2", is_group=True):
            utilities.dichotomy()
        assert_tree("Dichotomy")


# ---------------------------------------------------------------------------
# Medium demos

class TestDemoForest:

    def test_runs(self, clean_after):
        from geonodes.demos import forest
        forest.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import forest
        forest.demo()
        assert_tree("Forest")


class TestDemoArrows:

    def test_runs(self, clean_after):
        from geonodes.demos import arrows
        arrows.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import arrows
        arrows.demo()
        assert_tree("Arrows")


class TestDemoShaders:

    def test_runs(self, clean_after):
        from geonodes.demos import shaders
        shaders.demo()

    def test_material_created(self, clean_after):
        from geonodes.demos import shaders
        shaders.demo()
        assert_material("Wood")


class TestDemoTopology:

    def test_runs(self, clean_after):
        from geonodes.demos import topology
        topology.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import topology
        topology.demo()
        assert_tree("Topology Indices")


class TestDemoExplosion:

    def test_runs(self, clean_after):
        from geonodes.demos import explosion
        explosion.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import explosion
        explosion.demo()
        assert_tree("Kinematics Demo")


# ---------------------------------------------------------------------------
# Heavy demos

class TestDemoCamCulling:

    def test_runs(self, clean_after):
        from geonodes.demos import cam_culling
        cam_culling.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import cam_culling
        cam_culling.demo()
        assert_tree("Camera Demo")


class TestDemoCounters:

    def test_runs(self, clean_after):
        from geonodes.demos import counters
        counters.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import counters
        counters.demo()
        assert_tree("Counter Digital")


class TestDemoFourd:

    def test_runs_and_creates_shader(self, clean_after):
        from geonodes.demos import fourd
        fourd.demo()
        assert_material("4D Surface")


class TestDemoFurniture:

    def test_runs_and_creates_tree(self, clean_after):
        from geonodes.demos import furniture
        furniture.demo()
        assert_tree("Base Stock")


class TestDemoObserver:

    def test_runs(self, clean_after):
        from geonodes.demos import observer
        observer.demo()

    def test_tree_created(self, clean_after):
        from geonodes.demos import observer
        observer.demo()
        assert_tree("Hand")


