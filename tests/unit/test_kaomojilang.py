"""kaomojilang: stage 1 (text -> python), stage 2 (ast), runtime rules, the example file."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from geonodes.kaomojilang import run, run_file, translate, Shape, Stage1Error, Stage2Error, RunError  # noqa: E402
from geonodes.kaomojilang.stage1 import mangle_symbols, demangle  # noqa: E402
from geonodes.kaomojilang.runtime import ASPECT  # noqa: E402
from geonodes.drawing import flatten  # noqa: E402

EXAMPLE = os.path.join(os.path.dirname(__file__), "..", "..", "kaomojilang", "examples", "example.kmj")


# ----------------------------------------------------------------------------------------------------
# Stage 1
# ----------------------------------------------------------------------------------------------------

def test_mangle_symbols_outside_strings_and_comments():
    code, _ = mangle_symbols("def \u25a2(x='\u25a2'): # \u25a2")
    assert code == "def _u25a2_(x='\u25a2'): # \u25a2"
    assert demangle("_u25a2_") == "\u25a2"


def test_valid_unicode_letters_are_kept():
    assert mangle_symbols("\u0298 = 1")[0] == "\u0298 = 1"


def test_triple_quoted_text_is_untouched():
    r = translate("'''\n(^_^) \u25a2\n'''\nx = 1\n")
    assert "(^_^) \u25a2" in r.source and r.kaomoji == []


def test_grid_block_becomes_a_shape_call():
    r = translate("def sq(fill=red):\n    1    2\n\n    4    3\n")
    assert r.shapes == {"sq": "sq"}
    assert "def sq(fill=red, *, stroke=None, width=None, sizes=None, smooth=None, shift=None, rotate=None, scale=None):" in r.source
    assert "__shape__([(1, 4.0, 0, False), (2, 9.0, 0, False), (4, 4.0, 2, False), (3, 9.0, 2, False)], 'sq', {'fill': fill, " in r.source


def test_multi_digit_numbers_are_centered():
    r = translate("def s():\n    0\n   10\n")
    assert "(0, 4.0, 0, False)" in r.source and "(10, 3.5, 1, False)" in r.source       # '10' spans columns 3-4


def test_python_def_is_passed_through():
    r = translate("def f(a):\n    return a + 1\n")
    assert r.shapes == {} and "return a + 1" in r.source


def test_kaomoji_lines_and_labels():
    r = translate("x = 1\n\n\u0298\u203f\u0298\n## innocent face\n\nt(-_-t)\n##fuck it\n\n\u00af\\_(\u30c4)_/\u00af\n#shrug\n")
    assert [(t, l) for t, l, _ in r.kaomoji] == [("\u0298\u203f\u0298", "innocent face"),
                                                 ("t(-_-t)", "fuck it"),
                                                 ("\u00af\\_(\u30c4)_/\u00af", "shrug")]


def test_duplicate_number_in_a_drawing():
    with pytest.raises(Stage1Error, match="number 1 is used twice"):
        translate("def s():\n    1 2\n    1 3\n")


def test_unclosed_bracket_is_reported_where_it_opens():
    src = "x = 1\nanim = [f({1: g(a=r(), 2: g(a=r()})]\n\n'''\ndoc\n'''\n\n(^_^)\n##face\n"
    with pytest.raises(Stage1Error) as e:
        translate(src, "t.kmj")
    assert e.value.line == 2 and "never closed" in str(e.value)


def test_unclosed_triple_quote():
    with pytest.raises(Stage1Error, match="triple"):
        translate("x = 1\n'''never closed\n")


def test_malformed_def():
    with pytest.raises(Stage1Error, match="malformed def"):
        translate("def broken(:\n    1\n")


# ----------------------------------------------------------------------------------------------------
# Stage 2
# ----------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("src", [
    "import os\n",
    "x = ().__class__\n",
    "__shape__ = 1\n",
    "while True:\n    pass\n",
    "f = lambda: 1\n",
    "class A:\n    pass\n",
    "x = open('f')\n",
])
def test_validator_rejects_unsafe_code(src):
    with pytest.raises((Stage2Error, RunError)):
        run(src)


def test_syntax_error_reports_original_line():
    with pytest.raises(Stage2Error) as e:
        run("a = 1\n\nb = 1 +\n")
    assert e.value.line == 3


def test_runtime_error_maps_to_original_line():
    with pytest.raises(RunError) as e:
        run("a = 1\n\n\nb = undefined_name\n", "t.kmj")
    assert e.value.line == 4 and "NameError" in str(e.value)


def test_range_is_limited():
    with pytest.raises(RunError, match="limited"):
        run("x = [i for i in range(10000000)]\n")


# ----------------------------------------------------------------------------------------------------
# Runtime rules
# ----------------------------------------------------------------------------------------------------

def kinds(shape):
    return {p.id: p.kind for p in shape.parts}


def test_runs_and_kinds():
    src = ("def s():\n"
           "    1 2 3\n\n"
           "    10\n\n"
           "    20 21\n\n"
           "    30 31 32\n\n"
           "    41 42 43 44\n")
    assert kinds(run(src).call("s")) == {1: "polygon", 10: "point", 20: "line", 30: "smooth", 41: "polygon"}


def test_positions_use_columns_and_aspect_rows():
    s = run("def s():\n    1    2\n\n    4    3\n").call("s")
    assert s.parts[0].points == [(4.0, 0.0), (9.0, 0.0), (9.0, 2 * ASPECT), (4.0, 2 * ASPECT)]


def test_param_scalar_and_dict_per_part():
    src = ("def s(fill={1: red, '*': blue}, width=0.5, stroke=green):\n"
           "    1 2 3\n\n    11 12 13\n")
    p = {x.id: x for x in run(src).call("s").parts}
    assert p[1].fill == "red" and p[11].fill == "blue"
    assert p[1].width == 0.5 and p[1].stroke == "green"


def test_dict_argument_overlays_dict_default():
    src = "colors = {1: red, 11: blue}\ndef s(fill=colors):\n    1 2 3\n\n    11 12 13\n"
    prog = run(src)
    p = {x.id: x.fill for x in prog.call("s", {11: "green"}).parts}
    assert p == {1: "red", 11: "green"}
    p = {x.id: x.fill for x in prog.call("s", fill="pink").parts}
    assert p == {1: "pink", 11: "pink"}                      # a scalar replaces the default


def test_bad_number_parameter():
    with pytest.raises(RunError):
        run("def s(smooth='x'):\n    0 1 2\n").call("s")


def test_glyph_only_on_points():
    src = "def g():\n    0 1 2\n\ndef s(fill=None):\n    0 1 2\n"
    prog = run(src)
    with pytest.raises(RunError, match="single point"):
        prog.call("s", fill=prog.call("g"))


def _outline(shape, cell=10.0):
    strokes, warnings = flatten(shape.to_drawing(cell=cell, margin=0), resolution=16)
    assert not warnings
    return strokes


def test_smooth_one_on_a_square_is_a_circle():
    src = "def sq(smooth=1.0):\n    0       1\n\n\n\n    3       2\n"      # 8 columns x 4 rows = 8 x 8 units
    s, = _outline(run(src).call("sq"))
    assert s.closed
    cx = sum(p[0] for p in s.points) / len(s.points)
    cy = sum(p[1] for p in s.points) / len(s.points)
    radii = [math.hypot(x - cx, y - cy) for x, y in s.points]
    assert min(radii) == pytest.approx(40, rel=0.01) and max(radii) == pytest.approx(40, rel=0.01)    # 4 cells * 10 px


def test_smooth_zero_is_the_polygon_and_default_is_between():
    src = "def sq(smooth=0.0):\n    0       1\n\n\n\n    3       2\n"
    s, = _outline(run(src).call("sq"))
    assert len(s.points) == 4
    half, = _outline(run(src.replace("0.0", "0.5")).call("sq"))
    xs, ys = [p[0] for p in half.points], [p[1] for p in half.points]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    r = [math.hypot(x - cx, y - cy) for x, y in half.points]
    assert 40 < max(r) < 40 * math.sqrt(2) and min(r) >= 39.9           # between the circle and the corners


def test_open_shapes_are_not_filled():
    s, = _outline(run("def l(fill=red):\n    1 2\n").call("l"))
    assert not s.closed and s.fill is None


def test_point_default_is_a_black_dot_and_size_names():
    prog = run("def p(sizes={5: large}):\n    5\n")
    part = prog.call("p").parts[0]
    assert part.size == (2.5, 2.5) and part.kind == "point"
    s, = _outline(prog.call("p"))
    assert s.fill == (0, 0, 0, 1)


def test_glyph_is_stretched_to_size_box():
    src = ("def box():\n    0    1\n\n    3    2\n\n"                    # 5 wide, 4 tall: not square
           "def dot(fill=None, sizes={7: 6}):\n    7\n")
    prog = run(src)
    shape = prog.call("dot", fill={7: prog.call("box")})
    assert isinstance(shape.parts[0].fill, Shape)
    strokes, _ = flatten(shape.to_drawing(cell=1.0, margin=0))
    xs = [p[0] for p in strokes[0].points]
    ys = [p[1] for p in strokes[0].points]
    assert max(xs) - min(xs) == pytest.approx(6, abs=0.1) and max(ys) - min(ys) == pytest.approx(6, abs=0.1)


def test_symbol_names_work_for_defs_and_calls():
    src = "def \u25a2(fill=black, smooth=0.5):\n    0  1\n\n    3  2\n\nx = \u25a2(smooth=1.0)\n"
    prog = run(src)
    assert isinstance(prog["x"], Shape) and prog["x"].parts[0].smooth == 1.0
    assert "\u25a2" in prog.shape_names and isinstance(prog.call("\u25a2"), Shape)


def test_color_and_size_names_are_predefined():
    prog = run("a = [red, large, tiny]\n")
    assert prog["a"] == ["red", 2.5, 0.7]


def test_svg_output_and_layers():
    shape = run("def s():\n    0 1 2 3\n\n    10 11\n").call("s")
    svg = shape.to_svg()
    assert svg.startswith("<?xml") and 'id="p0"' in svg and 'id="p10"' in svg and "<path" in svg


# ----------------------------------------------------------------------------------------------------
# The example file
# ----------------------------------------------------------------------------------------------------

def test_example_file():
    prog = run_file(EXAMPLE)
    assert prog.shape_names == ["sqaure_example", "\u25a2", "smooth_face_example"]
    assert len(prog.kaomoji) == 105
    assert prog.kaomoji[0].text == "\u0298\u203f\u0298" and prog.kaomoji[0].label == "innocent face"
    face = prog.call("smooth_face_example")
    assert kinds(face) == {0: "smooth", 10: "smooth", 20: "smooth", 30: "point", 40: "point", 50: "line", 60: "line"}
    fills = {p.id: p.fill for p in face.parts}
    assert fills[0] == "yellow" and fills[10] == "white" and fills[30] == "black"
    assert {p.id: p.size for p in face.parts if p.kind == "point"} == {30: (2.5, 2.5), 40: (2.5, 2.5)}


def test_example_animation_frames_stamp_glyph_pupils():
    prog = run_file(EXAMPLE)
    frames = prog["anim_frames"]
    assert len(frames) == 10
    for f in frames:
        pupils = [p for p in f.parts if p.kind == "point"]
        assert all(isinstance(p.fill, Shape) for p in pupils)                  # replaced by the glyph
        assert {p.id: p.fill for p in f.parts}[0] == "yellow"                  # the rest of the colors are kept
    smooths = {f.parts[3].fill.parts[0].smooth for f in frames}
    assert len(smooths) > 1                                                    # random() differs per frame


def test_render_all_svgs(tmp_path):
    written = run_file(EXAMPLE).render_svgs(str(tmp_path))
    names = sorted(os.path.basename(p) for p in written)
    assert len(names) == 13 and "smooth_face_example.svg" in names and "anim_frames_009.svg" in names


# ----------------------------------------------------------------------------------------------------
# shift / rotate / scale, natural sizes, implicit parameters
# ----------------------------------------------------------------------------------------------------

LINE = "def l():\n    1 2\n"          # two points: (4, 0) and (6, 0)... see below


def line_points(shape, pid=1):
    return {p.id: p.points for p in shape.parts}[pid]


def test_every_drawing_accepts_the_standard_parameters():
    prog = run("def l():\n    1    2\n")
    s = prog.call("l", shift=(1, 1), rotate=0, scale=1, fill=None, stroke="red", width=1, sizes=None, smooth=0.1)
    part = s.parts[0]
    assert part.stroke == "red" and part.width == 1 and part.kind == "line"


def test_shift_is_in_columns_and_rows():
    prog = run("def l():\n    1    2\n")
    base = line_points(prog.call("l"))
    moved = line_points(prog.call("l", shift={1: (3, 2)}))
    assert [(x - bx, y - by) for (x, y), (bx, by) in zip(moved, base)] == [(3, 2 * ASPECT)] * 2


def test_rotate_is_clockwise_about_the_part_center():
    prog = run("def l():\n    1    2\n")
    (x0, y0), (x1, y1) = line_points(prog.call("l", rotate=90))
    assert x0 == pytest.approx(x1) and y0 < y1                  # the left end goes up (y down): clockwise
    cx, cy = [(a + b) / 2 for a, b in zip(*line_points(prog.call("l")))]
    assert (x0 + x1) / 2 == pytest.approx(cx) and (y0 + y1) / 2 == pytest.approx(cy)


def test_scale_number_and_pair():
    prog = run("def sq():\n    0    1\n\n    3    2\n")
    base = prog.call("sq").bbox()
    w, h = base[2] - base[0], base[3] - base[1]
    b = prog.call("sq", scale=(2, 0.5)).bbox()
    assert (b[2] - b[0], b[3] - b[1]) == pytest.approx((2 * w, 0.5 * h))
    b = prog.call("sq", scale=3).bbox()
    assert (b[2] - b[0], b[3] - b[1]) == pytest.approx((3 * w, 3 * h))


def test_scale_zero_hides_the_part():
    prog = run("def s():\n    0 1 2\n\n    10\n")
    shape = prog.call("s", scale={10: 0})
    assert [p.id for p in shape.parts if p.hidden] == [10]
    svg = shape.to_svg()
    assert 'id="p0"' in svg and 'id="p10"' not in svg


def test_dot_with_width_and_height_is_an_ellipse():
    svg = run("def d(sizes={5: (4, 2)}):\n    5\n").call("d").to_svg()
    assert "<ellipse" in svg and "<circle" not in svg


def test_stamped_drawing_keeps_its_natural_size_unless_sizes_says_otherwise():
    src = ("def box():\n    0    1\n\n    3    2\n\n"
           "def dot():\n    7\n")
    prog = run(src)
    box = prog.call("box")
    x0, y0, x1, y1 = box.bbox()
    natural = prog.call("dot", fill={7: box}).parts[0].size
    assert natural == pytest.approx((x1 - x0, y1 - y0))
    assert prog.call("dot", fill={7: box}, sizes={7: (2, 3)}).parts[0].size == (2, 3)
    assert prog.call("dot", fill={7: box}, scale={7: (2, 1)}).parts[0].size == pytest.approx((2 * (x1 - x0), y1 - y0))


def test_stamping_keeps_stroke_width_when_stretching():
    src = ("def flat():\n    0    1\n\n"                      # a line: no height
           "def dot(width=0.5):\n    7\n")
    prog = run(src)
    shape = prog.call("dot", fill={7: prog.call("flat")}, sizes={7: (10, 6)})
    strokes, _ = flatten(shape.to_drawing(cell=1.0, margin=0))
    assert strokes[0].width == pytest.approx(0.15, abs=1e-3)          # the line's own width, not stretched


def test_stamped_rotation():
    src = "def flat():\n    0    1\n\ndef dot():\n    7\n"
    prog = run(src)
    shape = prog.call("dot", fill={7: prog.call("flat")}, rotate=90, sizes={7: (10, 1)})
    pts = flatten(shape.to_drawing(cell=1.0, margin=0))[0][0].points
    assert pts[0][0] == pytest.approx(pts[1][0], abs=1e-6) and abs(pts[0][1] - pts[1][1]) == pytest.approx(10, abs=1e-3)


# ----------------------------------------------------------------------------------------------------
# face_anim.kmj
# ----------------------------------------------------------------------------------------------------

FACE_ANIM = os.path.join(os.path.dirname(__file__), "..", "..", "kaomojilang", "examples", "face_anim.kmj")


@pytest.fixture(scope="module")
def face_prog():
    return run_file(FACE_ANIM)


def eye_parts(shape, pid):
    return {p.id: p for p in shape.parts}[pid].fill.parts       # the stamped eye drawing


def test_face_is_symmetric(face_prog):
    face = face_prog.call("face")
    parts = {p.id: p for p in face.parts}
    axis = min(parts[0].points, key=lambda q: q[1])[0]                                # x of the top of the head
    for left, right in ((30, 40), (70, 80)):                                          # single points
        (xl, yl), (xr, yr) = parts[left].points[0], parts[right].points[0]
        assert yl == pytest.approx(yr) and xl + xr == pytest.approx(2 * axis)         # mirrored about the head axis
    (xl0, yl0), (xl1, yl1) = parts[10].points                                         # brows: the left end of one
    (xr0, yr0), (xr1, yr1) = parts[20].points                                         # mirrors the right end of the other
    assert yl0 == yl1 == yr0 == yr1
    assert xl0 + xr1 == pytest.approx(2 * axis) and xl1 + xr0 == pytest.approx(2 * axis)
    assert parts[0].kind == "smooth" and len([p for p in face.parts if p.id < 8]) == 1


def test_talk_poses_differ(face_prog):
    talk = face_prog["talk"]
    assert len(talk) == 6
    sizes = [tuple(round(v, 2) for v in {p.id: p for p in f.parts}[60].fill.bbox()) for f in talk]
    assert len(set(sizes)) == 6                                       # six different mouth shapes
    widths = {i: s[2] - s[0] for i, s in enumerate(sizes)}
    heights = {i: s[3] - s[1] for i, s in enumerate(sizes)}
    assert heights[1] > heights[3] and widths[3] > widths[1]          # A is open and tall, I is wide and thin
    assert widths[5] < widths[2]                                      # U is small, E is wide


def test_blink_squashes_and_hides_pupils(face_prog):
    blink = face_prog["blink"]
    heights = []
    for f in blink:
        eye = eye_parts(f, 30)
        outline = [p for p in eye if p.id == 0][0]
        ys = [y for _, y in outline.points]
        heights.append(max(ys) - min(ys))
    assert heights[0] > heights[1] > heights[2] < heights[3] < heights[4]
    assert heights[2] < 0.2 * heights[0]
    assert [p.hidden for p in eye_parts(blink[0], 30) if p.id == 10] == [False]
    assert [p.hidden for p in eye_parts(blink[2], 30) if p.id == 10] == [True]       # fully closed: no pupil


def test_look_moves_the_pupils(face_prog):
    look = face_prog["look"]
    px = [[p for p in eye_parts(f, 30) if p.id == 10][0].points[0][0] for f in look]
    assert px[1] < px[0] < px[4]                                       # left, center, right
    py = [[p for p in eye_parts(f, 30) if p.id == 10][0].points[0][1] for f in look]
    assert py[2] < py[0] < py[5]                                       # up (y down), center, down


def test_mood_brows_rotate_and_lift(face_prog):
    mood = face_prog["mood"]
    brow = lambda f, pid: {p.id: p for p in f.parts}[pid].points
    (lx0, ly0), (lx1, ly1) = brow(mood[3], 10)
    assert ly0 == pytest.approx(ly1)                                   # neutral: flat
    (ax0, ay0), (ax1, ay1) = brow(mood[1], 10)
    (bx0, by0), (bx1, by1) = brow(mood[2], 10)
    assert (ay0 - ay1) * (by0 - by1) < 0                               # opposite tilts
    assert brow(mood[0], 10)[0][1] < brow(mood[3], 10)[0][1]           # brows=0.5: raised


# ----------------------------------------------------------------------------------------------------
# open runs: a trailing ~
# ----------------------------------------------------------------------------------------------------

SMILE = "def smile(stroke=black):\n    0         2~\n\n      1\n"


def test_open_smooth_curve():
    shape = run(SMILE).call("smile")
    part = shape.parts[0]
    assert part.kind == "smooth" and part.open
    svg = shape.to_svg()
    assert "<path" in svg and "Z" not in svg.split("<path")[1].split("/>")[0]
    s, = flatten(shape.to_drawing(cell=1.0, margin=0))[0]
    assert not s.closed and s.fill is None
    (x0, y0), (x1, y1) = s.points[0], s.points[-1]
    assert (x0, y0) == pytest.approx((part.points[0][0], part.points[0][1])) and \
           (x1, y1) == pytest.approx((part.points[2][0], part.points[2][1]))          # ends are not rounded
    assert max(p[1] for p in s.points) > y0 + 1                                       # it dips down: a smile


def test_open_polyline_for_odd_ids():
    shape = run("def zig():\n    1 2 3~\n").call("zig")
    assert shape.parts[0].kind == "polygon" and shape.parts[0].open
    s, = flatten(shape.to_drawing(cell=1.0, margin=0))[0]
    assert not s.closed and len(s.points) == 3


def test_closed_remains_the_default():
    assert not run("def c():\n    1 2 3\n").call("c").parts[0].open


def test_marker_only_on_the_last_number_of_a_run():
    with pytest.raises(RunError, match="last number"):
        run("def bad():\n    0~ 1 2\n").call("bad")


def test_marker_must_follow_a_number():
    with pytest.raises(Stage1Error, match="right after a number"):
        translate("def bad():\n    0 1 ~ 2\n")


def test_marker_on_a_two_point_line_is_harmless():
    part = run("def l():\n    0 1~\n").call("l").parts[0]
    assert part.kind == "line" and not part.open


def test_open_curve_can_be_filled_if_asked():
    part = run("def f(fill=red):\n    0   2~\n\n      1\n").call("f").parts[0]
    assert part.fill == "red" and part.open


def test_open_curve_smooth_one_is_a_single_cubic_and_zero_a_polyline():
    src = "def smile(smooth=1.0):\n    0         2~\n\n      1\n"
    shape = run(src).call("smile")
    d = shape.to_svg().split(' d="')[1].split('"')[0]
    assert d.count("C") == 1 and "L" not in d                          # one smooth cubic from end to end
    straight = run(src).call("smile", smooth=0.0)
    d0 = straight.to_svg().split('points="')[0] if False else straight.to_svg()
    assert "<path" in d0 and "L" in d0.split(' d="')[1].split('"')[0]  # smooth = 0: straight segments
    # the cubic stays inside the control triangle and reaches below the end points (a smile)
    s, = flatten(shape.to_drawing(cell=1.0, margin=0))[0]
    ys = [p[1] for p in s.points]
    assert max(ys) > ys[0] + 0.5 and max(ys) < max(shape.parts[0].points[1][1], ys[0]) + 1e-6


def test_bear_example():
    import os
    path = os.path.join(os.path.dirname(__file__), "..", "..", "kaomojilang", "examples", "bear.kmj")
    prog = run_file(path)
    bear = prog.call("bear")
    ids = {p.id: p for p in bear.parts}
    assert ids[0].kind == "smooth" and not ids[0].open
    assert {11, 15, 20, 30, 40, 50, 60} <= set(ids)
    assert ids[11].kind == ids[15].kind == "point"                      # ears are dots, not a line
    assert ids[11].points[0][0] < ids[0].points[0][0] < ids[15].points[0][0]
    big = prog.call("bear", scale={11: 1.3, 15: 1.3})
    assert {p.id: p for p in big.parts}[11].size[0] > ids[11].size[0]
