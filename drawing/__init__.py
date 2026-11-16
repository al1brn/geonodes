"""Vector drawing API: write SVG with drawsvg, or Grease Pencil with the same code.

    from geonodes.drawing import draw, to_grease_pencil

    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Circle(0, 0, 80, fill='none', stroke='black', stroke_width=4))
    d.save_svg('face.svg')                    # SVG
    to_grease_pencil(d, gp_data, frame=1)     # Grease Pencil strokes

`draw` is the vendored drawsvg package (MIT, see drawing/drawsvg/LICENSE.txt).
`flatten` does not use bpy. Curves (paths, arcs, ellipses) are kept as cubic Beziers: Grease Pencil
strokes get one point per anchor with handles (`bezier=False` samples polylines instead).
"""

from . import drawsvg as draw
from .flatten import Anchor, Stroke, flatten, parse_color, parse_transform

__all__ = ['draw', 'Anchor', 'Stroke', 'flatten', 'parse_color', 'parse_transform', 'to_grease_pencil']


def to_grease_pencil(*args, **kwargs):
    """See drawing.grease.to_grease_pencil (imports bpy lazily)."""
    from .grease import to_grease_pencil as _impl
    return _impl(*args, **kwargs)
