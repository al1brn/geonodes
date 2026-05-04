"""Tests for core/gizmoclass.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.gizmoclass import Gizmo


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
# Import checks

class TestGizmoImport:

    def test_gizmo_importable(self):
        import core.gizmoclass
        assert hasattr(core.gizmoclass, 'Gizmo')

    def test_no_utils_import(self):
        import core.gizmoclass
        assert not hasattr(core.gizmoclass, 'utils')


# ---------------------------------------------------------------------------
# Gizmo.dial

class TestGizmoDial:

    def test_dial_no_value(self):
        with Tree("_test_gizmo_dial_noarg", "GeometryNodeTree"):
            result = Gizmo.dial()
            assert result is not None

    def test_dial_with_value(self):
        with Tree("_test_gizmo_dial_val", "GeometryNodeTree"):
            result = Gizmo.dial(1.0)
            assert result is not None

    def test_dial_multiple_values(self):
        with Tree("_test_gizmo_dial_multi", "GeometryNodeTree"):
            result = Gizmo.dial(1.0, 2.0)
            assert result is not None

    def test_dial_color_id(self):
        with Tree("_test_gizmo_dial_color", "GeometryNodeTree"):
            result = Gizmo.dial(color_id='X')
            assert result is not None


# ---------------------------------------------------------------------------
# Gizmo.linear

class TestGizmoLinear:

    def test_linear_no_value(self):
        with Tree("_test_gizmo_lin_noarg", "GeometryNodeTree"):
            result = Gizmo.linear()
            assert result is not None

    def test_linear_with_value(self):
        with Tree("_test_gizmo_lin_val", "GeometryNodeTree"):
            result = Gizmo.linear(1.0)
            assert result is not None

    def test_linear_draw_style(self):
        with Tree("_test_gizmo_lin_style", "GeometryNodeTree"):
            result = Gizmo.linear(draw_style='BOX')
            assert result is not None


# ---------------------------------------------------------------------------
# Gizmo.transform — numpy bool broadcasting

class TestGizmoTransform:

    def test_transform_defaults(self):
        with Tree("_test_gizmo_tf_defaults", "GeometryNodeTree"):
            result = Gizmo.transform()
            assert result is not None

    def test_transform_scalar_bool(self):
        with Tree("_test_gizmo_tf_scalar", "GeometryNodeTree"):
            result = Gizmo.transform(use_rotation=False, use_scale=True, use_translation=True)
            assert result is not None

    def test_transform_tuple_bool(self):
        with Tree("_test_gizmo_tf_tuple", "GeometryNodeTree"):
            result = Gizmo.transform(
                use_rotation=(True, False, True),
                use_scale=(False, True, False),
                use_translation=(True, True, False),
            )
            assert result is not None

    def test_transform_with_value(self):
        with Tree("_test_gizmo_tf_val", "GeometryNodeTree"):
            result = Gizmo.transform(use_rotation=True)
            assert result is not None
