"""Tests for core/utils.py."""
import pytest
import numpy as np

from core.utils import (
    only_kw_chars,
    CamelCase,
    snake_case,
    ensure_uniques,
    prox_names,
    value_to_array,
    get_dim_vector,
    is_vector_like,
    is_color_like,
    is_matrix_like,
    is_value_like,
    is_int_like,
    has_bsocket,
    request_empty,
    get_socket_name,
    is_named_attr,
    get_attr_name,
    get_prop_name,
    get_label,
    socket_type_to_bl_idname,
    bl_idname_to_socket_type,
    get_items_socket_type,
)
from core import constants
from core.scripterror import NodeError


# ---------------------------------------------------------------------------
# only_kw_chars

class TestOnlyKwChars:

    def test_plain_ascii(self):
        assert only_kw_chars("hello") == "hello"

    def test_accents_replaced(self):
        assert only_kw_chars("éàü") == "eau"

    def test_spaces_become_underscore(self):
        assert only_kw_chars("hello world") == "hello_world"

    def test_no_double_underscore(self):
        result = only_kw_chars("a  b")
        assert "__" not in result

    def test_special_chars_become_underscore(self):
        result = only_kw_chars("a-b.c")
        assert result == "a_b_c"

    def test_empty_string(self):
        assert only_kw_chars("") == ""


# ---------------------------------------------------------------------------
# CamelCase

class TestCamelCase:

    def test_simple(self):
        assert CamelCase("hello world") == "HelloWorld"

    def test_empty_returns_none(self):
        assert CamelCase("") is None

    def test_rgb_preserved(self):
        assert CamelCase("RGB color") == "RGBColor"

    def test_bsdf_preserved(self):
        assert CamelCase("principled BSDF") == "PrincipledBSDF"

    def test_digit_prefix_escaped(self):
        result = CamelCase("3D view")
        assert result[0] == "_"


# ---------------------------------------------------------------------------
# snake_case

class TestSnakeCase:

    def test_simple(self):
        assert snake_case("Hello World") == "hello_world"

    def test_empty(self):
        assert snake_case("") == ""

    def test_python_keyword_escaped(self):
        assert snake_case("for") == "for_"
        assert snake_case("class") == "class_"

    def test_no_keyword_escape_when_disabled(self):
        assert snake_case("for", test_keyword=False) == "for"

    def test_digit_prefix_escaped(self):
        assert snake_case("3d")[0] == "_"


# ---------------------------------------------------------------------------
# ensure_uniques

class TestEnsureUniques:

    def test_no_duplicates_unchanged(self):
        assert ensure_uniques(["a", "b", "c"]) == ["a", "b", "c"]

    def test_duplicate_gets_index(self):
        result = ensure_uniques(["x", "x"])
        assert result[0] == "x"
        assert result[1] == "x_001"

    def test_triple_duplicate(self):
        result = ensure_uniques(["x", "x", "x"])
        assert result == ["x", "x_001", "x_002"]

    def test_single_digit_mode(self):
        result = ensure_uniques(["x", "x"], single_digit=True)
        assert result[1] == "x_1"

    def test_empty_list(self):
        assert ensure_uniques([]) == []


# ---------------------------------------------------------------------------
# prox_names

class TestProxNames:

    def test_exact_match(self):
        result = prox_names("hello", ["hello", "world"])
        assert "hello" in result

    def test_close_match(self):
        result = prox_names("helo", ["hello", "world"])
        assert len(result) > 0

    def test_no_match(self):
        result = prox_names("xyz123", ["hello", "world"])
        assert result == []


# ---------------------------------------------------------------------------
# value_to_array

class TestValueToArray:

    def test_scalar_to_vector3(self):
        a = value_to_array(1.0, (3,))
        assert a.shape == (3,)
        assert np.all(a == 1.0)

    def test_list_to_array(self):
        a = value_to_array([1.0, 2.0, 3.0], (3,))
        assert a.shape == (3,)

    def test_wrong_size_raises(self):
        with pytest.raises(NodeError):
            value_to_array([1.0, 2.0], (3,))

    def test_scalar_to_matrix(self):
        a = value_to_array(0.0, (4, 4))
        assert a.shape == (4, 4)


# ---------------------------------------------------------------------------
# get_dim_vector

class TestGetDimVector:

    def test_none_value_returns_zeros(self):
        result = get_dim_vector(None, 3)
        assert result == (0., 0., 0.)

    def test_scalar_broadcasts(self):
        result = get_dim_vector(1.0, 3)
        assert len(result) == 3

    def test_dims_none_uses_len(self):
        result = get_dim_vector([1.0, 2.0, 3.0], None)
        assert len(result) == 3


# ---------------------------------------------------------------------------
# is_*_like

class TestIsLike:

    def test_is_vector_like_vector(self):
        assert is_vector_like([1.0, 2.0, 3.0])

    def test_is_vector_like_float_false(self):
        assert not is_vector_like(1.0)

    def test_is_color_like_rgba(self):
        assert is_color_like([1.0, 0.0, 0.0, 1.0])

    def test_is_matrix_like(self):
        assert is_matrix_like(np.eye(4).flatten())

    def test_is_value_like_float(self):
        assert is_value_like(1.0)

    def test_is_value_like_int(self):
        assert is_value_like(1)

    def test_is_value_like_bool(self):
        assert is_value_like(True)

    def test_is_value_like_vector_false(self):
        assert not is_value_like([1.0, 2.0, 3.0])

    def test_is_int_like_int(self):
        assert is_int_like(1)

    def test_is_int_like_bool(self):
        assert is_int_like(True)

    def test_is_int_like_float_false(self):
        assert not is_int_like(1.0)


# ---------------------------------------------------------------------------
# has_bsocket

class TestHasBsocket:

    def test_plain_value_false(self):
        assert not has_bsocket(1.0)

    def test_list_of_plain_values_false(self):
        assert not has_bsocket([1.0, 2.0, 3.0])


# ---------------------------------------------------------------------------
# request_empty

class TestRequestEmpty:

    def test_empty_socket_constant(self):
        assert request_empty(constants.EMPTY_SOCKET)

    def test_other_string_false(self):
        assert not request_empty("something_else")

    def test_non_string_false(self):
        assert not request_empty(None)
        assert not request_empty(42)


# ---------------------------------------------------------------------------
# get_socket_name

class TestGetSocketName:

    def test_none_returns_none(self):
        assert get_socket_name(None) is None


# ---------------------------------------------------------------------------
# Named attribute utilities

class TestNamedAttr:

    def test_is_named_attr_valid(self):
        assert is_named_attr("_Position")
        assert is_named_attr("_MyAttr")

    def test_is_named_attr_invalid(self):
        assert not is_named_attr("position")
        assert not is_named_attr("_position")   # lowercase after _
        assert not is_named_attr("_P")          # too short (len <= 2)

    def test_get_attr_name(self):
        assert get_attr_name("_Position") == "Position"
        assert get_attr_name("_My_Attr") == "My Attr"

    def test_get_attr_name_invalid(self):
        assert get_attr_name("position") is None
        assert get_attr_name("_") is None

    def test_get_prop_name(self):
        assert get_prop_name("My Attr") == "_My_Attr"

    def test_get_prop_name_non_string(self):
        assert get_prop_name(42) is None


# ---------------------------------------------------------------------------
# get_items_socket_type

class TestGetItemsSocketType:

    def test_value_becomes_float(self):
        assert get_items_socket_type('VALUE') == 'FLOAT'

    def test_other_unchanged(self):
        assert get_items_socket_type('INT') == 'INT'
        assert get_items_socket_type('VECTOR') == 'VECTOR'


# ---------------------------------------------------------------------------
# socket_type_to_bl_idname / bl_idname_to_socket_type

class TestSocketTypeConversions:

    def test_socket_type_to_bl_idname_boolean(self):
        assert socket_type_to_bl_idname('BOOLEAN') == 'NodeSocketBool'

    def test_socket_type_to_bl_idname_rgba(self):
        assert socket_type_to_bl_idname('RGBA') == 'NodeSocketColor'

    def test_socket_type_to_bl_idname_passthrough(self):
        assert socket_type_to_bl_idname('NodeSocketFloat') == 'NodeSocketFloat'

    def test_socket_type_to_bl_idname_invalid_raises(self):
        with pytest.raises(RuntimeError):
            socket_type_to_bl_idname('INVALID_XYZ')

    def test_bl_idname_to_socket_type_bool(self):
        assert bl_idname_to_socket_type('NodeSocketBool') == 'BOOLEAN'

    def test_bl_idname_to_socket_type_color(self):
        assert bl_idname_to_socket_type('NodeSocketColor') == 'RGBA'
