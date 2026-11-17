"""
Face drawn with the node drawing API (`drawing.nodes`): the drawing is driven by modifier inputs.

Same face as `face_drawing.py` (one named layer per part), but the shapes are Geometry Nodes, so
Blink, Look, Vowel... can be keyframed on the modifier.

``` python
from geonodes.demos2 import face_nodes

face_nodes.demo()
```
"""

from geonodes import *
from geonodes.drawing.nodes import NodeDrawing
from .face import MOUTH_POSES, pose_value
from .face_drawing import UNIT


def demo(rebuild=False):

    Tree._init_package('Face')

    with GeoNodes("Face Drawing", rebuild=rebuild):

        blink   = Float(0.0, "Blink", 0, 1)
        look_x  = Float(0.0, "Look X", -1, 1)
        look_y  = Float(0.0, "Look Y", -1, 1)
        vowel   = Float(0.0, "Vowel", 0, 5)
        opening = Float(1.0, "Mouth Open", 0, 2)
        brow_up = Float(0.0, "Brow Raise", -1, 1)
        ink     = Color((0.13, 0.13, 0.13, 1.0), "Ink")
        lips    = Color((0.67, 0.2, 0.27, 1.0), "Lips")

        u = UNIT
        dr = NodeDrawing(scale=0.01)

        with dr.group("head", stroke=ink, width=3) as g:
            g.ellipse(0, 0, 0.9 * u, 1.0 * u)

        open_ratio = (1.0 - blink).clamp(0.05, 1.0)

        with dr.group("eyes", stroke=ink, width=3) as g:
            for side in (-1, 1):
                g.ellipse(0.45 * u * side, -0.25 * u, 0.2 * u, 0.2 * u * open_ratio)

        with dr.group("pupils", stroke=ink, fill=ink, width=1) as g:
            for side in (-1, 1):
                g.ellipse(0.45 * u * side + look_x * 0.08 * u, -0.25 * u - look_y * 0.08 * u * open_ratio,
                          0.07 * u, 0.07 * u * open_ratio)

        with dr.group("brows", stroke=ink, width=3) as g:
            for side in (-1, 1):
                cx = 0.45 * u * side
                y = -0.58 * u - brow_up * 0.1 * u
                g.path().M(cx - 0.2 * u, y).Q(cx, y - 0.12 * u, cx + 0.2 * u, y)

        with dr.group("mouth", stroke=ink, fill=lips, width=3) as g:
            g.ellipse(0, 0.35 * u, pose_value(vowel, 0) * u, (pose_value(vowel, 1) * opening).max(0.01) * u)

        dr.build().out()
