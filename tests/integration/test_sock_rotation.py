"""Tests for core/sock_rotation.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_rotation import Rotation


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

class TestRotationImport:

    def test_importable(self):
        import core.sock_rotation
        assert hasattr(core.sock_rotation, 'Rotation')

    def test_no_bpy_import(self):
        import core.sock_rotation
        assert not hasattr(core.sock_rotation, 'bpy')

    def test_no_literal_import(self):
        import core.sock_rotation
        assert not hasattr(core.sock_rotation, 'Literal')

    def test_no_utils_import(self):
        import core.sock_rotation
        assert not hasattr(core.sock_rotation, 'utils')

    def test_no_node_import(self):
        import core.sock_rotation
        assert not hasattr(core.sock_rotation, 'Node')

    def test_no_socket_import(self):
        import core.sock_rotation
        assert not hasattr(core.sock_rotation, 'Socket')

    def test_socket_type(self):
        assert Rotation.SOCKET_TYPE == 'ROTATION'


# ---------------------------------------------------------------------------
# Rotation creation

class TestRotationCreation:

    def test_rotation_default(self):
        with Tree("_test_rot_default", "GeometryNodeTree"):
            r = Rotation()
            assert r is not None

    def test_rotation_from_tuple(self):
        with Tree("_test_rot_tuple", "GeometryNodeTree"):
            r = Rotation((1.0, 0.0, 0.0))
            assert r is not None

    def test_rotation_named_input(self):
        with Tree("_test_rot_named", "GeometryNodeTree"):
            r = Rotation(name="My Rotation")
            assert r is not None

    def test_rotation_returns_rotation_type(self):
        with Tree("_test_rot_type", "GeometryNodeTree"):
            r = Rotation()
            assert isinstance(r, Rotation)

    def test_from_euler(self):
        with Tree("_test_rot_euler", "GeometryNodeTree"):
            r = Rotation.FromEuler((0.0, 0.0, 1.57))
            assert r is not None

    def test_from_axis_angle(self):
        with Tree("_test_rot_axang", "GeometryNodeTree"):
            r = Rotation.FromAxisAngle(axis=(0, 0, 1), angle=1.57)
            assert r is not None

    def test_from_quaternion(self):
        with Tree("_test_rot_quat", "GeometryNodeTree"):
            r = Rotation.FromQuaternion(w=1.0, x=0.0, y=0.0, z=0.0)
            assert r is not None


# ---------------------------------------------------------------------------
# Operators

class TestRotationOperators:

    def test_invert(self):
        with Tree("_test_rot_inv", "GeometryNodeTree"):
            result = ~Rotation()
            assert result is not None

    def test_matmul_rotation(self):
        """@ with Rotation → rotate_global."""
        with Tree("_test_rot_mm_rot", "GeometryNodeTree"):
            a = Rotation()
            b = Rotation()
            result = a @ b
            assert result is not None

    def test_matmul_vector(self):
        """@ with Vector → rotate_vector."""
        from core.sock_vector import Vector
        with Tree("_test_rot_mm_vec", "GeometryNodeTree"):
            r = Rotation()
            v = Vector((1, 0, 0))
            result = r @ v
            assert result is not None

    def test_matmul_tuple(self):
        """@ with tuple → rotate_vector."""
        with Tree("_test_rot_mm_tup", "GeometryNodeTree"):
            r = Rotation()
            result = r @ (1, 0, 0)
            assert result is not None


# ---------------------------------------------------------------------------
# Key methods

class TestRotationMethods:

    def test_rotate(self):
        with Tree("_test_rot_rotate", "GeometryNodeTree"):
            a = Rotation()
            b = Rotation()
            result = a.rotate(b)
            assert result is not None

    def test_rotate_global(self):
        with Tree("_test_rot_global", "GeometryNodeTree"):
            a = Rotation()
            b = Rotation()
            result = a.rotate_global(b)
            assert result is not None

    def test_rotate_local(self):
        with Tree("_test_rot_local", "GeometryNodeTree"):
            a = Rotation()
            b = Rotation()
            result = a.rotate_local(b)
            assert result is not None

    def test_rotate_vector(self):
        with Tree("_test_rot_rotvec", "GeometryNodeTree"):
            from core.sock_vector import Vector
            r = Rotation()
            v = Vector((1, 0, 0))
            result = r.rotate_vector(v)
            assert result is not None

    def test_to_euler(self):
        with Tree("_test_rot_euler_out", "GeometryNodeTree"):
            r = Rotation()
            result = r.to_euler()
            assert result is not None

    def test_to_quaternion(self):
        with Tree("_test_rot_quat_out", "GeometryNodeTree"):
            r = Rotation()
            result = r.to_quaternion()
            assert result is not None

    def test_to_axis_angle(self):
        with Tree("_test_rot_axang_out", "GeometryNodeTree"):
            r = Rotation()
            result = r.to_axis_angle()
            assert result is not None

    def test_align_to_vector(self):
        with Tree("_test_rot_align", "GeometryNodeTree"):
            r = Rotation()
            result = r.align_to_vector((0, 0, 1))
            assert result is not None
