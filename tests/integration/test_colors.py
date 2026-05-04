"""Tests for core/colors.py — requires Blender (mathutils.Color)."""
import pytest
from mathutils import Color

from core.colors import str_to_color_tuple, to_color_tuple, to_hexa, linear_rgb, SysColor
from core.scripterror import NodeError


# ---------------------------------------------------------------------------
# linear_rgb

class TestLinearRgb:

    def test_low_value(self):
        assert linear_rgb(0.0) == pytest.approx(0.0)

    def test_threshold_boundary(self):
        assert linear_rgb(0.04045) == pytest.approx(0.04045 / 12.92, rel=1e-4)

    def test_high_value(self):
        result = linear_rgb(1.0)
        assert result == pytest.approx(1.0, rel=1e-4)


# ---------------------------------------------------------------------------
# str_to_color_tuple

class TestStrToColorTuple:

    def test_known_name_red(self):
        assert str_to_color_tuple("red") == (1.0, 0.0, 0.0, 1.0)

    def test_known_name_black(self):
        assert str_to_color_tuple("black") == (0.0, 0.0, 0.0, 1.0)

    def test_known_name_white(self):
        assert str_to_color_tuple("white") == (1.0, 1.0, 1.0, 1.0)

    def test_known_name_indianred(self):
        result = str_to_color_tuple("indianred")
        assert result is not None

    def test_known_name_indigo(self):
        result = str_to_color_tuple("indigo")
        assert result is not None

    def test_case_insensitive(self):
        assert str_to_color_tuple("RED") == str_to_color_tuple("red")

    def test_hex_6_chars(self):
        r, g, b, a = str_to_color_tuple("#ff0000")
        assert r == pytest.approx(1.0, abs=0.01)
        assert g == pytest.approx(0.0, abs=0.01)
        assert b == pytest.approx(0.0, abs=0.01)
        assert a == 1.0

    def test_hex_8_chars_with_alpha(self):
        r, g, b, a = str_to_color_tuple("#ff000080")
        assert r == pytest.approx(1.0, abs=0.01)
        assert a == pytest.approx(0.502, abs=0.01)

    def test_hex_0x_prefix(self):
        result = str_to_color_tuple("0xff0000")
        assert result is not None
        assert result[0] == pytest.approx(1.0, abs=0.01)

    def test_invalid_returns_none(self):
        assert str_to_color_tuple("notacolor") is None

    def test_wrong_length_returns_none(self):
        assert str_to_color_tuple("#fff") is None


# ---------------------------------------------------------------------------
# to_color_tuple

class TestToColorTuple:

    def test_none_returns_none(self):
        assert to_color_tuple(None) is None

    def test_color_instance(self):
        c = Color((0.5, 0.25, 0.1))
        result = to_color_tuple(c)
        assert result == pytest.approx((0.5, 0.25, 0.1, 1.0), abs=1e-5)

    def test_list_3_values(self):
        result = to_color_tuple([0.5, 0.5, 0.5])
        assert len(result) == 4
        assert result[3] == 1.0

    def test_list_4_values(self):
        result = to_color_tuple([0.1, 0.2, 0.3, 0.4])
        assert len(result) == 4

    def test_list_1_value_broadcasts(self):
        result = to_color_tuple([0.5])
        assert result == pytest.approx((0.5, 0.5, 0.5, 1.0))

    def test_list_wrong_length_raises(self):
        with pytest.raises(NodeError):
            to_color_tuple([0.1, 0.2])

    def test_string_valid(self):
        result = to_color_tuple("red")
        assert result[0] == pytest.approx(1.0)

    def test_string_invalid_raises(self):
        with pytest.raises(NodeError):
            to_color_tuple("notacolor")

    def test_float_scalar(self):
        result = to_color_tuple(0.5)
        assert result == pytest.approx((0.5, 0.5, 0.5, 1.0))

    def test_unconvertible_raises(self):
        with pytest.raises(NodeError):
            to_color_tuple(object())


# ---------------------------------------------------------------------------
# to_hexa

class TestToHexa:

    def test_red_with_alpha(self):
        assert to_hexa((1.0, 0.0, 0.0, 1.0)) == "#FF0000FF"

    def test_red_without_alpha(self):
        assert to_hexa((1.0, 0.0, 0.0, 1.0), with_alpha=False) == "#FF0000"

    def test_black(self):
        assert to_hexa((0.0, 0.0, 0.0, 1.0)) == "#000000FF"

    def test_clamps_above_one(self):
        result = to_hexa((1.5, 0.0, 0.0, 1.0))
        assert result == "#FF0000FF"

    def test_clamps_below_zero(self):
        result = to_hexa((-0.5, 0.0, 0.0, 1.0))
        assert result == "#000000FF"

    def test_uppercase(self):
        result = to_hexa((0.0, 0.502, 0.0, 1.0))
        assert result == result.upper()


# ---------------------------------------------------------------------------
# SysColor

class TestSysColor:

    def test_from_string(self):
        c = SysColor("red")
        assert not c.is_none
        assert c.rgba[0] == pytest.approx(1.0)

    def test_from_none(self):
        c = SysColor(None)
        assert c.is_none

    def test_rgb_is_3_tuple(self):
        c = SysColor("red")
        assert len(c.rgb) == 3

    def test_rgba_is_4_tuple(self):
        c = SysColor("red")
        assert len(c.rgba) == 4

    def test_hexa_with_alpha(self):
        c = SysColor("red")
        assert c.hexa(True) == "#FF0000FF"

    def test_hexa_without_alpha(self):
        c = SysColor("red")
        assert c.hexa(False) == "#FF0000"

    def test_str_returns_hexa(self):
        c = SysColor("red")
        assert str(c) == "#FF0000FF"

    def test_str_none_color(self):
        c = SysColor(None)
        assert str(c) == "<No Color>"

    def test_bcolor_is_mathutils_color(self):
        c = SysColor("red")
        assert isinstance(c.bcolor, Color)

    def test_hexa_none_returns_none(self):
        c = SysColor(None)
        assert c.hexa() is None
