"""Tests for core/sockettype.py."""
import pytest
import numpy as np
import bpy

from core.sockettype import SocketType
from core.scripterror import NodeError


# ---------------------------------------------------------------------------
# Construction depuis des types Python natifs

class TestSocketTypeFromPython:

    def test_from_bool(self):
        st = SocketType(True)
        assert st.full_socket_id == 'NodeSocketBool'

    def test_from_int(self):
        st = SocketType(42)
        assert st.full_socket_id == 'NodeSocketInt'

    def test_from_float(self):
        st = SocketType(3.14)
        assert st.full_socket_id == 'NodeSocketFloat'

    def test_from_string(self):
        st = SocketType("hello")
        assert st.full_socket_id == 'NodeSocketString'

    def test_from_array_3(self):
        st = SocketType([1.0, 2.0, 3.0])
        assert st.full_socket_id == 'NodeSocketVector'

    def test_from_array_4(self):
        st = SocketType([1.0, 2.0, 3.0, 1.0])
        assert st.full_socket_id == 'NodeSocketColor'

    def test_from_array_16(self):
        st = SocketType(np.eye(4).flatten())
        assert st.full_socket_id == 'NodeSocketMatrix'

    def test_from_array_wrong_size_raises(self):
        with pytest.raises(NodeError):
            SocketType([1.0, 2.0, 3.0, 4.0, 5.0])

    def test_from_none_defaults_to_geometry(self):
        st = SocketType(None)
        assert st.full_socket_id == 'NodeSocketGeometry'

    def test_from_socket_type_instance(self):
        st1 = SocketType(1.0)
        st2 = SocketType(st1)
        assert st2.full_socket_id == st1.full_socket_id


# ---------------------------------------------------------------------------
# Construction depuis une string (nom de type)

class TestSocketTypeFromString:

    def test_from_type_name_float(self):
        st = SocketType('VALUE')
        assert st.type == 'VALUE'

    def test_from_type_name_vector(self):
        st = SocketType('VECTOR')
        assert st.type == 'VECTOR'

    def test_from_type_name_bool(self):
        st = SocketType('BOOLEAN')
        assert st.type == 'BOOLEAN'


# ---------------------------------------------------------------------------
# Propriétés

class TestSocketTypeProperties:

    def test_type_float(self):
        assert SocketType(1.0).type == 'VALUE'

    def test_type_int(self):
        assert SocketType(1).type == 'INT'

    def test_type_bool(self):
        assert SocketType(True).type == 'BOOLEAN'

    def test_is_geometry(self):
        assert SocketType(None).is_geometry

    def test_is_not_geometry(self):
        assert not SocketType(1.0).is_geometry

    def test_is_vector(self):
        assert SocketType([1.0, 2.0, 3.0]).is_vector

    def test_class_name_float(self):
        assert SocketType(1.0).class_name == 'Float'

    def test_class_name_vector(self):
        assert SocketType([0, 0, 0]).class_name == 'Vector'

    def test_dimensions_vector_default(self):
        st = SocketType([1.0, 2.0, 3.0])
        assert st.dimensions == 3

    def test_dimensions_non_vector_is_none(self):
        st = SocketType(1.0)
        assert st.dimensions is None


# ---------------------------------------------------------------------------
# Égalité

class TestSocketTypeEquality:

    def test_equal_same_type(self):
        assert SocketType(1.0) == SocketType(2.0)

    def test_not_equal_different_type(self):
        assert SocketType(1.0) != SocketType(1)

    def test_equal_to_string(self):
        assert SocketType(1.0) == SocketType('VALUE')


# ---------------------------------------------------------------------------
# Subtype

class TestSocketTypeSubtype:

    def test_subtype_none_for_float(self):
        assert SocketType(1.0).subtype is None

    def test_subtype_set_angle(self):
        st = SocketType('VALUE')
        st.subtype = 'ANGLE'
        assert st.subtype == 'ANGLE'

    def test_subtype_reset_to_none(self):
        st = SocketType('VALUE')
        st.subtype = 'ANGLE'
        st.subtype = None
        assert st.subtype is None

    def test_invalid_subtype_raises(self):
        st = SocketType('VALUE')
        with pytest.raises(RuntimeError):
            st.subtype = 'INVALID_SUBTYPE_XYZ'


# ---------------------------------------------------------------------------
# Dimensions

class TestSocketTypeDimensions:

    def test_set_dimensions_2(self):
        st = SocketType([1.0, 2.0, 3.0])
        st.dimensions = 2
        assert st.dimensions == 2

    def test_set_dimensions_4(self):
        st = SocketType([1.0, 2.0, 3.0])
        st.dimensions = 4
        assert st.dimensions == 4

    def test_set_invalid_dimensions_raises(self):
        st = SocketType([1.0, 2.0, 3.0])
        with pytest.raises(AttributeError):
            st.dimensions = 5

    def test_set_dimensions_on_non_vector_raises(self):
        st = SocketType(1.0)
        with pytest.raises(AttributeError):
            st.dimensions = 2


# ---------------------------------------------------------------------------
# class_name_from_socket_name

class TestClassNameFromSocketName:

    @pytest.mark.parametrize("name,expected", [
        ("mesh",        "Mesh"),
        ("curve",       "Curve"),
        ("curves",      "Curve"),
        ("points",      "Cloud"),
        ("point cloud", "Cloud"),
        ("grease pencil","GreasePencil"),
        ("instances",   "Instances"),
        ("volume",      "Volume"),
        ("geometry",    "Geometry"),
        ("unknown_xyz", "Geometry"),
    ])
    def test_known_names(self, name, expected):
        assert SocketType.class_name_from_socket_name(name) == expected

    def test_volume_exact_match_only(self):
        # 'vol' ne doit pas matcher 'volume'
        assert SocketType.class_name_from_socket_name("vol") == "Geometry"


# ---------------------------------------------------------------------------
# check_* static methods (messages d'erreur interpolés)

class TestCheckMethods:

    def test_check_socket_id_valid(self):
        assert SocketType.check_socket_id('NodeSocketFloat') is True

    def test_check_socket_id_invalid_message_contains_value(self):
        with pytest.raises(RuntimeError, match="bad_socket_id"):
            SocketType.check_socket_id('bad_socket_id')

    def test_check_type_valid(self):
        assert SocketType.check_type('VALUE') is True

    def test_check_type_invalid_message_contains_value(self):
        with pytest.raises(RuntimeError, match="BAD_TYPE"):
            SocketType.check_type('BAD_TYPE')

    def test_check_class_name_valid(self):
        assert SocketType.check_class_name('Float') is True

    def test_check_class_name_invalid_message_contains_value(self):
        with pytest.raises(RuntimeError, match="BadClass"):
            SocketType.check_class_name('BadClass')
