"""Tests for core/scripterror.py — requires Blender."""
import pytest

from core.scripterror import NodeError, NodeAttributeError, is_in_core


# ---------------------------------------------------------------------------
# Import checks

class TestScripterrorImport:

    def test_importable(self):
        import core.scripterror
        assert hasattr(core.scripterror, 'NodeError')

    def test_no_pprint_import(self):
        import core.scripterror
        assert not hasattr(core.scripterror, 'pprint')

    def test_node_attribute_error_exported(self):
        import core.scripterror
        assert hasattr(core.scripterror, 'NodeAttributeError')

    def test_is_in_core_exported(self):
        import core.scripterror
        assert hasattr(core.scripterror, 'is_in_core')


# ---------------------------------------------------------------------------
# is_in_core

class TestIsInCore:

    def test_core_file(self):
        assert is_in_core("/some/path/geonodes/core/treeclass.py") is True

    def test_generated_file(self):
        assert is_in_core("/some/path/geonodes/core/generated/vector.py") is True

    def test_non_core_file(self):
        assert is_in_core("/some/path/geonodes/myScript.py") is False

    def test_user_file(self):
        assert is_in_core("/home/user/scripts/my_node_script.py") is False


# ---------------------------------------------------------------------------
# NodeError

class TestNodeError:

    def test_is_exception(self):
        assert issubclass(NodeError, Exception)

    def test_raise_and_catch(self):
        with pytest.raises(NodeError):
            raise NodeError("test error")

    def test_str_returns_string(self):
        err = NodeError("something went wrong")
        assert isinstance(str(err), str)

    def test_message_contains_text(self):
        err = NodeError("something went wrong")
        assert "something went wrong" in str(err)

    def test_no_message(self):
        err = NodeError()
        assert isinstance(str(err), str)

    def test_multiple_messages(self):
        err = NodeError("first", "second")
        s = str(err)
        assert "first" in s
        assert "second" in s

    def test_dict_message(self):
        err = NodeError({"key1": "val1", "key2": "val2"})
        s = str(err)
        assert "key1" in s
        assert "val1" in s

    def test_kwargs(self):
        err = NodeError("msg", param="value")
        s = str(err)
        assert "param" in s
        assert "value" in s

    def test_geometry_nodes_error_header(self):
        err = NodeError("test")
        assert "Geometry nodes error" in str(err)

    def test_keyword_none(self):
        err = NodeError("test", keyword=None)
        assert isinstance(str(err), str)


# ---------------------------------------------------------------------------
# NodeError.get_stack / find_keyword

class TestNodeErrorStack:

    def test_get_stack_returns_list(self):
        result = NodeError.get_stack()
        assert isinstance(result, list)

    def test_stack_items_have_keys(self):
        result = NodeError.get_stack()
        for item in result:
            assert 'file_name' in item
            assert 'lineno' in item
            assert 'code' in item

    def test_find_keyword_none_returns_none(self):
        result = NodeError.find_keyword(None)
        assert result is None

    def test_find_keyword_absent(self):
        result = NodeError.find_keyword("__this_keyword_does_not_exist_xyz__")
        assert result is None


# ---------------------------------------------------------------------------
# NodeAttributeError

class TestNodeAttributeError:

    def test_is_attribute_error(self):
        assert issubclass(NodeAttributeError, AttributeError)

    def test_raise_and_catch_as_attribute_error(self):
        with pytest.raises(AttributeError):
            raise NodeAttributeError("bad attr")

    def test_str_contains_geometry_nodes_error(self):
        err = NodeAttributeError("bad attr")
        assert "Geometry nodes error" in str(err)
