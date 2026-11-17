"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demo face
------------------

Animated cartoon face drawn with Grease Pencil.

The face is built from curves converted with `Curve.to_grease_pencil`.
All the animation is driven by modifier inputs which can be keyframed:

- Blink       : 0 = eyes open, 1 = eyes closed
- Look X / Y  : where the pupils look at, in [-1, 1]
- Vowel       : mouth pose, 0 = rest, 1 = A, 2 = E, 3 = I, 4 = O, 5 = U.
                Non integer values blend the two neighbouring poses.
- Mouth Open  : global scale of the mouth opening
- Brow Raise  : eyebrows height

> Modifiers:
> - Face

``` python
from geonodes.demos2 import face

face.demo()
```
"""

from geonodes import *

# ====================================================================================================
# Mouth poses
# ====================================================================================================

# (half width, half height) of the mouth ellipse for each pose
# index:  0 rest, 1 A, 2 E, 3 I, 4 O, 5 U

MOUTH_POSES = [
    (0.30, 0.02),   # rest
    (0.30, 0.28),   # A : wide open
    (0.36, 0.14),   # E : wide, half open
    (0.40, 0.05),   # I : wide, nearly closed
    (0.18, 0.24),   # O : round
    (0.12, 0.12),   # U : small round
]


def pose_value(vowel, column):
    """Blend the poses with triangular weights around each integer value."""
    total = None
    for i, pose in enumerate(MOUTH_POSES):
        weight = (1.0 - abs(vowel - i)).clamp(0.0, 1.0)
        term = weight * pose[column]
        total = term if total is None else total + term
    return total


# ====================================================================================================
# Parts
# ====================================================================================================

def ellipse(rx, ry, center=(0, 0, 0), resolution=32):
    """Ellipse curve in the XZ plane (the face looks toward -Y)."""
    circle = Curve.Circle(resolution=resolution, radius=1.0)
    # Circle is in the XY plane: rotate to XZ
    circle = circle.transform(rotation=(pi/2, 0, 0))
    return circle.transform(translation=center, scale=(rx, 1.0, ry))


def eye(side, blink, look_x, look_y):
    """One eye: lid outline (squashed by blink) and pupil following the look."""
    cx = 0.45 * side

    # Outline: blink squashes the eye vertically, leaving a thin line
    open_ratio = (1.0 - blink).clamp(0.05, 1.0)
    outline = ellipse(0.2, 0.2 * open_ratio, center=(cx, 0, 0.25))

    # Pupil can't leave the eye, and hides when the eye is almost closed
    pupil_pos = (cx + look_x * 0.08, -0.01, 0.25 + look_y * 0.08 * open_ratio)
    pupil = ellipse(0.07, 0.07 * open_ratio, center=pupil_pos, resolution=16)
    return outline, pupil


def brow(side, raise_):
    cx = 0.45 * side
    z = 0.58 + raise_ * 0.1
    brow = Curve.QuadraticBezier(
        resolution = 12,
        start  = (cx - 0.2, 0, z),
        middle = (cx,       0, z + 0.06),
        end    = (cx + 0.2, 0, z),
    )
    return brow


def mouth(vowel, openness):
    hw = pose_value(vowel, 0)
    hh = pose_value(vowel, 1) * openness
    return ellipse(hw, hh.max(0.01), center=(0, 0, -0.35), resolution=24)


# ====================================================================================================
# Face modifier
# ====================================================================================================

def demo(rebuild=False):

    Tree._init_package('Face')

    with GeoNodes("Face", rebuild=rebuild):

        blink   = Float(0.0, "Blink", 0, 1)
        look_x  = Float(0.0, "Look X", -1, 1)
        look_y  = Float(0.0, "Look Y", -1, 1)
        vowel   = Float(0.0, "Vowel", 0, 5)
        opening = Float(1.0, "Mouth Open", 0, 2)
        brow_up = Float(0.0, "Brow Raise", -1, 1)

        stroke  = Color((0.05, 0.05, 0.05, 1.0), "Stroke Color")

        with Layout("Head"):
            head = ellipse(0.9, 1.0, resolution=48).to_grease_pencil(instances_as_layers=False)

        with Layout("Eyes"):
            l_out, l_pupil = eye(-1, blink, look_x, look_y)
            r_out, r_pupil = eye(+1, blink, look_x, look_y)
            eyes = Curve(l_out).join(r_out).to_grease_pencil(instances_as_layers=False)
            pupils = Curve(l_pupil).join(r_pupil).to_grease_pencil(instances_as_layers=False)

        with Layout("Brows"):
            brows = brow(-1, brow_up).join(brow(+1, brow_up)).to_grease_pencil(instances_as_layers=False)

        with Layout("Mouth"):
            mouth_gp = mouth(vowel, opening).to_grease_pencil(instances_as_layers=False)

        with Layout("Assemble"):
            face = head.join(eyes, pupils, brows, mouth_gp)
            face.set_grease_pencil_color(color=stroke, opacity=1.0, mode='STROKE')

        face.out()
