"""drawing.flatten — pure geometry, no Grease Pencil involved."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from geonodes.drawing import draw, flatten, parse_color, parse_transform  # noqa: E402
from geonodes.drawing.flatten import path_to_subpaths, mat_apply  # noqa: E402


def test_parse_color():
    assert parse_color('none') is None
    assert parse_color('#f00') == (1.0, 0.0, 0.0, 1.0)
    assert parse_color('rgb(0, 255, 0)') == (0.0, 1.0, 0.0, 1.0)
    assert parse_color('orange')[0] == 1.0
    with pytest.raises(ValueError):
        parse_color('notacolor')


def test_transform_order():
    m = parse_transform('translate(10,0) scale(2)')
    assert mat_apply(m, 1, 1) == (12, 2)          # scale first, then translate
    x, y = mat_apply(parse_transform('rotate(90)'), 1, 0)
    assert (round(x, 9), round(y, 9)) == (0, 1)


def test_path_lines_and_close():
    (pts, closed), = path_to_subpaths('M0,0 L10,0 L10,10 Z')
    assert closed and pts == [(0, 0), (10, 0), (10, 10)]


def test_path_relative_and_hv():
    (pts, _), = path_to_subpaths('M1,1 h4 v3 l-1,1')
    assert pts == [(1, 1), (5, 1), (5, 4), (4, 5)]


def test_path_implicit_lineto_and_multiple_subpaths():
    subs = path_to_subpaths('M0,0 10,0 10,10 M50,50 L60,60')
    assert len(subs) == 2 and subs[0][0][-1] == (10, 10)


def test_quadratic_endpoints():
    (pts, _), = path_to_subpaths('M0,0 Q5,10 10,0', resolution=8)
    assert pts[0] == (0, 0) and pts[-1] == (10, 0) and len(pts) == 9
    assert max(p[1] for p in pts) == pytest.approx(5.0)   # apex of the parabola


def test_cubic_and_smooth():
    (pts, _), = path_to_subpaths('M0,0 C0,10 10,10 10,0 S20,-10 20,0', resolution=4)
    assert pts[-1] == (20, 0)


@pytest.mark.parametrize("sweep", [0, 1])
def test_arc_stays_on_circle(sweep):
    (pts, _), = path_to_subpaths(f'M10,0 A10,10 0 0,{sweep} -10,0', resolution=8)
    assert pts[-1] == (-10, 0)
    for x, y in pts:
        assert math.hypot(x, y) == pytest.approx(10, abs=1e-6)
    # sweep flag decides which half circle is used
    assert (max(p[1] for p in pts) > 5) == bool(sweep)


def test_circle_and_group_layers():
    d = draw.Drawing(100, 100, origin='center')
    g = draw.Group(id='eyes', transform='translate(5,5)')
    g.append(draw.Circle(0, 0, 10, fill='red', stroke='black', stroke_width=2))
    d.append(g)
    d.append(draw.Rectangle(0, 0, 4, 2, fill='none', stroke='blue'))
    strokes, warnings = flatten(d, resolution=4)
    assert not warnings
    assert [s.layer for s in strokes] == ['eyes', 'Drawing']
    c = strokes[0]
    assert c.closed and c.stroke == (0, 0, 0, 1) and c.fill == (1, 0, 0, 1) and c.width == 2
    xs = [p[0] for p in c.points]
    assert min(xs) == pytest.approx(-5) and max(xs) == pytest.approx(15)
    assert strokes[1].fill is None


def test_style_inheritance_and_scale_width():
    d = draw.Drawing(10, 10)
    g = draw.Group(id='g', stroke='red', stroke_width=2, transform='scale(3)')
    g.append(draw.Line(0, 0, 1, 1))
    d.append(g)
    s, = flatten(d)[0]
    assert s.stroke == (1, 0, 0, 1) and s.width == pytest.approx(6) and not s.closed


def test_unsupported_reported():
    d = draw.Drawing(10, 10)
    d.append(draw.Text('hi', 5, 0, 0))
    strokes, warnings = flatten(d)
    assert not strokes and 'Text' in warnings[0]


# ----------------------------------------------------------------------------------------------------
# Bezier output

from geonodes.drawing.flatten import path_to_beziers, ellipse_beziers, sample_bezier  # noqa: E402


def test_bezier_straight_segments_have_no_handles():
    (anchors, closed), = path_to_beziers('M0,0 L10,0 L10,10')
    assert not closed and len(anchors) == 3
    assert all(a.hl == a.p and a.hr == a.p for a in anchors)


def test_bezier_cubic_handles():
    (anchors, _), = path_to_beziers('M0,0 C0,10 10,10 10,0')
    assert anchors[0].hr == (0, 10) and anchors[1].hl == (10, 10) and anchors[1].hr == (10, 0)


def test_bezier_quadratic_is_raised_to_cubic():
    (anchors, _), = path_to_beziers('M0,0 Q5,10 10,0')
    assert anchors[0].hr == pytest.approx((10 / 3, 20 / 3))
    assert anchors[1].hl == pytest.approx((20 / 3, 20 / 3))
    pts = sample_bezier(anchors, False, resolution=10)
    assert max(p[1] for p in pts) == pytest.approx(5.0)       # same apex as the quadratic


@pytest.mark.parametrize("rot", [0, 30])
def test_bezier_arc_matches_circle(rot):
    (anchors, _), = path_to_beziers(f'M10,0 A10,10 {rot} 1,1 -10,0 A10,10 0 0,1 10,0')
    assert len(anchors) >= 4
    for x, y in sample_bezier(anchors, False, resolution=16):
        assert math.hypot(x, y) == pytest.approx(10, abs=0.02)


def test_bezier_elliptical_arc_matches_ellipse():
    (anchors, _), = path_to_beziers('M20,0 A20,10 0 1,1 -20,0 A20,10 0 1,1 20,0 Z')
    for x, y in sample_bezier(anchors, True, resolution=16):
        assert (x / 20) ** 2 + (y / 10) ** 2 == pytest.approx(1, abs=0.01)


def test_bezier_closed_path_merges_duplicate_end():
    (anchors, closed), = path_to_beziers('M0,0 C0,10 10,10 10,0 C10,-10 0,-10 0,0 Z')
    assert closed and len(anchors) == 2
    assert anchors[0].hl == (0, -10)          # incoming handle moved to the first anchor


def test_ellipse_beziers():
    anchors = ellipse_beziers(1, 2, 10, 5)
    assert len(anchors) == 4
    for x, y in sample_bezier(anchors, True, resolution=16):
        assert ((x - 1) / 10) ** 2 + ((y - 2) / 5) ** 2 == pytest.approx(1, abs=0.001)


def test_flatten_strokes_carry_transformed_bezier():
    d = draw.Drawing(10, 10)
    d.append(draw.Group(id='g', transform='translate(100,0)'))
    g = d.elements[0]
    g.append(draw.Path(stroke='black', fill='none').M(0, 0).C(0, 5, 5, 5, 5, 0))
    s, = flatten(d)[0]
    assert s.bezier[0].p == (100, 0) and s.bezier[0].hr == (100, 5)
    assert len(s.points) > 2
