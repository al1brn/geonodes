"""Tests for core/sock_matrix.py — requires Blender."""
import pytest
import bpy

from core.treeclass import Tree
from core.sock_matrix import Matrix


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

class TestMatrixImport:

    def test_importable(self):
        import core.sock_matrix
        assert hasattr(core.sock_matrix, 'Matrix')

    def test_no_literal_import(self):
        import core.sock_matrix
        assert not hasattr(core.sock_matrix, 'Literal')

    def test_no_version_import(self):
        import core.sock_matrix
        assert not hasattr(core.sock_matrix, 'version')

    def test_no_numpy_import(self):
        import core.sock_matrix
        assert not hasattr(core.sock_matrix, 'np')

    def test_no_bpy_import(self):
        import core.sock_matrix
        assert not hasattr(core.sock_matrix, 'bpy')

    def test_no_socket_import(self):
        import core.sock_matrix
        assert not hasattr(core.sock_matrix, 'Socket')

    def test_no_tree_import(self):
        import core.sock_matrix
        assert not hasattr(core.sock_matrix, 'Tree')

    def test_socket_type(self):
        assert Matrix.SOCKET_TYPE == 'MATRIX'


# ---------------------------------------------------------------------------
# Matrix creation

class TestMatrixCreation:

    def test_matrix_default(self):
        with Tree("_test_mat_default", "GeometryNodeTree"):
            m = Matrix()
            assert m is not None

    def test_matrix_named_input(self):
        with Tree("_test_mat_named", "GeometryNodeTree"):
            m = Matrix(name="My Matrix")
            assert m is not None

    def test_matrix_from_array(self):
        with Tree("_test_mat_array", "GeometryNodeTree"):
            m = Matrix.FromArray([0]*16)
            assert m is not None

    def test_matrix_returns_matrix_type(self):
        with Tree("_test_mat_type", "GeometryNodeTree"):
            m = Matrix()
            assert isinstance(m, Matrix)

    def test_combine_transform(self):
        with Tree("_test_mat_ct", "GeometryNodeTree"):
            m = Matrix.CombineTransform((1, 0, 0), (0, 0, 0), (1, 1, 1))
            assert m is not None


# ---------------------------------------------------------------------------
# Operators

class TestMatrixOperators:

    def test_invert(self):
        with Tree("_test_mat_inv", "GeometryNodeTree"):
            result = ~Matrix()
            assert result is not None

    def test_matmul_matrix(self):
        with Tree("_test_mat_mm", "GeometryNodeTree"):
            a = Matrix()
            b = Matrix()
            result = a @ b
            assert result is not None

    def test_matmul_vector(self):
        with Tree("_test_mat_mv", "GeometryNodeTree"):
            from core.sock_vector import Vector
            m = Matrix()
            v = Vector((1, 0, 0))
            result = m @ v
            assert result is not None

    def test_matmul_tuple(self):
        with Tree("_test_mat_mt", "GeometryNodeTree"):
            m = Matrix()
            result = m @ (1, 0, 0)
            assert result is not None


# ---------------------------------------------------------------------------
# Utility methods

class TestMatrixUtilities:

    def test_as_tuple(self):
        with Tree("_test_mat_astup", "GeometryNodeTree"):
            m = Matrix()
            result = m.as_tuple
            assert result is not None

    def test_get_col(self):
        with Tree("_test_mat_getcol", "GeometryNodeTree"):
            m = Matrix()
            result = m.get_col(0)
            assert result is not None

    def test_get_row(self):
        with Tree("_test_mat_getrow", "GeometryNodeTree"):
            m = Matrix()
            result = m.get_row(0)
            assert result is not None

    def test_set_col_bug_fix(self):
        """Regression: set_col used Layout without importing it → NameError."""
        with Tree("_test_mat_setcol", "GeometryNodeTree"):
            m = Matrix()
            from core.sock_vector import Vector
            col = (Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((0, 0, 0)))
            result = m.set_col(0, col)
            assert result is not None

    def test_set_row_bug_fix(self):
        """Regression: set_row used Layout without importing it → NameError."""
        with Tree("_test_mat_setrow", "GeometryNodeTree"):
            m = Matrix()
            from core.sock_vector import Vector
            row = (Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((0, 0, 0)))
            result = m.set_row(0, row)
            assert result is not None

    def test_determinant(self):
        with Tree("_test_mat_det", "GeometryNodeTree"):
            m = Matrix()
            result = m.determinant()
            assert result is not None

    def test_transpose(self):
        with Tree("_test_mat_transp", "GeometryNodeTree"):
            m = Matrix()
            result = m.transpose()
            assert result is not None

    def test_trs(self):
        with Tree("_test_mat_trs", "GeometryNodeTree"):
            m = Matrix()
            result = m.trs
            assert result is not None

    def test_translation(self):
        with Tree("_test_mat_trans", "GeometryNodeTree"):
            m = Matrix()
            result = m.translation
            assert result is not None
