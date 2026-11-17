"""
Face drawn with the drawing API (drawsvg), exported as SVG or as Grease Pencil keyframes.

Unlike `face.py` (live geometry nodes driven by modifier inputs), this builds
one drawing per pose: the same code gives a preview SVG and Grease Pencil frames.

``` python
from geonodes.demos2 import face_drawing

face_drawing.save_svgs("/tmp/face")          # one SVG per vowel
gp = face_drawing.demo()                     # Grease Pencil data, one keyframe per pose
```
"""

import bpy

from geonodes.drawing import draw, to_grease_pencil
from .face import MOUTH_POSES

VOWELS = ["rest", "A", "E", "I", "O", "U"]
UNIT = 100          # SVG units; the head is 90 wide, 100 tall (as in face.py)
INK = "#222"


def face_drawing(vowel=0, blink=0.0, look=(0.0, 0.0)):
    """Draw one pose. vowel: index in VOWELS, blink: 0..1, look: (x, y) in [-1, 1]."""
    d = draw.Drawing(2 * UNIT, 2.4 * UNIT, origin='center')
    kw = dict(fill='none', stroke=INK, stroke_width=3)

    head = draw.Group(id='head')
    head.append(draw.Ellipse(0, 0, 0.9 * UNIT, 1.0 * UNIT, **kw))
    d.append(head)

    open_ratio = max(0.05, 1.0 - blink)
    eyes, pupils = draw.Group(id='eyes'), draw.Group(id='pupils')
    for side in (-1, 1):
        cx, cy = 0.45 * UNIT * side, -0.25 * UNIT
        eyes.append(draw.Ellipse(cx, cy, 0.2 * UNIT, 0.2 * UNIT * open_ratio, **kw))
        pupils.append(draw.Ellipse(
            cx + look[0] * 0.08 * UNIT, cy - look[1] * 0.08 * UNIT * open_ratio,
            0.07 * UNIT, 0.07 * UNIT * open_ratio, fill=INK, stroke='none'))
    d.append(eyes)
    d.append(pupils)

    brows = draw.Group(id='brows')
    for side in (-1, 1):
        cx, y = 0.45 * UNIT * side, -0.58 * UNIT
        brows.append(draw.Path(fill='none', stroke=INK, stroke_width=3)
                     .M(cx - 0.2 * UNIT, y).Q(cx, y - 0.12 * UNIT, cx + 0.2 * UNIT, y))
    d.append(brows)

    hw, hh = MOUTH_POSES[vowel]
    mouth = draw.Group(id='mouth')
    mouth.append(draw.Ellipse(0, 0.35 * UNIT, hw * UNIT, max(hh, 0.01) * UNIT,
                              fill='#aa3344', stroke=INK, stroke_width=3))
    d.append(mouth)
    return d


def save_svgs(folder):
    import os
    os.makedirs(folder, exist_ok=True)
    for i, name in enumerate(VOWELS):
        face_drawing(vowel=i).save_svg(os.path.join(folder, f"vowel_{name}.svg"))


def demo(name="Face", step=10):
    """Vowel poses at frames 1, 1+step, ... then a blink."""
    gp = bpy.data.grease_pencils.new(name)
    for i in range(len(VOWELS)):
        to_grease_pencil(face_drawing(vowel=i), gp, frame=1 + i * step)
    last = 1 + len(VOWELS) * step
    to_grease_pencil(face_drawing(blink=1.0), gp, frame=last)
    to_grease_pencil(face_drawing(), gp, frame=last + 2)
    return gp
