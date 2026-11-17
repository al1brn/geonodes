"""kaomojilang -> Grease Pencil (requires Blender >= 5.x)."""
import os
import sys

import bpy
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from geonodes.kaomojilang import run_file, frames_to_grease_pencil  # noqa: E402

EXAMPLE = os.path.join(os.path.dirname(__file__), "..", "..", "kaomojilang", "examples", "example.kmj")


@pytest.fixture
def gp():
    data = bpy.data.grease_pencils.new("kl")
    yield data
    bpy.data.grease_pencils.remove(data)


def test_face_layers_follow_the_part_ids(gp):
    face = run_file(EXAMPLE).call("smooth_face_example")
    face.to_grease_pencil(gp)
    assert [l.name for l in gp.layers] == ['p0', 'p10', 'p20', 'p30', 'p40', 'p50', 'p60']
    head = gp.layers['p0'].frames[0].drawing.strokes[0]
    assert head.cyclic and head.curve_type == 2                       # smooth closed shape -> Bezier stroke
    assert tuple(head.fill_color) == pytest.approx((1.0, 1.0, 0.0, 1.0), abs=1e-3)
    nose = gp.layers['p50'].frames[0].drawing.strokes[0]
    assert not nose.cyclic and len(nose.points) == 2


def test_animation_frames_become_keyframes(gp):
    prog = run_file(EXAMPLE)
    frames_to_grease_pencil(prog["anim_frames"], gp, start=1, step=2)
    assert [f.frame_number for f in gp.layers['p0'].frames] == list(range(1, 21, 2))
    # same framing for all frames: the head does not move between keyframes
    heads = [tuple(f.drawing.strokes[0].points[0].position) for f in gp.layers['p0'].frames]
    assert all(h == pytest.approx(heads[0], abs=1e-6) for h in heads)
    # the pupils are glyphs: one cyclic stroke each, and they differ from frame to frame
    pupils = [tuple(round(c, 4) for c in f.drawing.strokes[0].points[0].handle_right.position)
              for f in gp.layers['p30'].frames]
    assert len(set(pupils)) > 1


def test_square_glyph_vs_circle_glyph(gp):
    prog = run_file(EXAMPLE)
    square = prog.call("\u25a2", smooth=0.0)
    circle = prog.call("\u25a2", smooth=1.0)
    square.to_grease_pencil(gp, frame=1)
    circle.to_grease_pencil(gp, frame=2)
    strokes = [f.drawing.strokes[0] for f in gp.layers[0].frames]
    assert strokes[0].curve_type == 1 and len(strokes[0].points) == 4      # polygon
    assert strokes[1].curve_type == 2 and len(strokes[1].points) == 4      # circle: 4 Bezier anchors


# ----------------------------------------------------------------------------------------------------
# face_anim.kmj as Grease Pencil animation
# ----------------------------------------------------------------------------------------------------

from geonodes.kaomojilang import run  # noqa: E402

FACE_ANIM = os.path.join(os.path.dirname(__file__), "..", "..", "kaomojilang", "examples", "face_anim.kmj")


def strokes_at(gp, layer, frame):
    return next(f for f in gp.layers[layer].frames if f.frame_number == frame).drawing.strokes


def test_talk_animation_keyframes(gp):
    prog = run_file(FACE_ANIM)
    frames_to_grease_pencil(prog["talk"], gp, start=1, step=4)
    assert [f.frame_number for f in gp.layers['p60'].frames] == [1, 5, 9, 13, 17, 21]
    # the mouth layer: rest is a polyline (a line), the vowels are cyclic Bezier shapes
    rest = strokes_at(gp, 'p60', 1)[0]
    assert not rest.cyclic and len(rest.points) == 2
    for frame in (5, 9, 13, 17, 21):
        s = strokes_at(gp, 'p60', frame)[0]
        assert s.cyclic and s.curve_type == 2
    # the vowels have different extents
    def width(frame):
        xs = [p.position[0] for p in strokes_at(gp, 'p60', frame)[0].points]
        return max(xs) - min(xs)
    assert width(13) > width(5) > width(21)              # I wider than A, A wider than U


def test_blink_hides_the_pupil_in_the_closed_frame(gp):
    prog = run_file(FACE_ANIM)
    frames_to_grease_pencil(prog["blink"], gp, start=1, step=1)
    counts = [len(strokes_at(gp, 'p30', n)) for n in range(1, 6)]
    assert counts == [2, 2, 1, 2, 2]                      # eye outline + pupil, except fully closed


def test_a_hidden_part_gets_an_empty_keyframe(gp):
    src = ("def two():\n    0 1 2\n\n    10 11 12\n")
    prog = run(src)
    shapes = [prog.call("two"), prog.call("two", scale={10: 0}), prog.call("two")]
    frames_to_grease_pencil(shapes, gp, start=1, step=1)
    frames = {f.frame_number: len(f.drawing.strokes) for f in gp.layers['p10'].frames}
    assert frames == {1: 1, 2: 0, 3: 1}                   # frame 2 is an explicit empty drawing
    assert {f.frame_number: len(f.drawing.strokes) for f in gp.layers['p0'].frames} == {1: 1, 2: 1, 3: 1}


def test_look_moves_the_pupil_stroke(gp):
    prog = run_file(FACE_ANIM)
    frames_to_grease_pencil(prog["look"], gp, start=1, step=1)
    def pupil_x(n):
        strokes = strokes_at(gp, 'p30', n)
        pupil = strokes[-1]                               # the last stroke of the eye layer is the pupil
        return sum(p.position[0] for p in pupil.points) / len(pupil.points)
    assert pupil_x(2) < pupil_x(1) < pupil_x(5)


def test_open_smile_is_an_open_bezier_stroke(gp):
    prog = run("def smile():\n    0         2~\n\n      1\n")
    prog.call("smile").to_grease_pencil(gp)
    s = gp.layers['p0'].frames[0].drawing.strokes[0]
    assert not s.cyclic and s.curve_type == 2
    xs = [p.position[0] for p in s.points]
    assert xs[0] == pytest.approx(-xs[-1], abs=1e-6)                      # symmetric end points
