"""Runtime: numbered grids -> shapes -> drawsvg elements -> SVG or Grease Pencil.

Rules (see SPEC.md)
-------------------
- Numbers are grouped in runs of consecutive values (3, 4, 5 ...). The first number is the id of the part.
- 1 point -> dot (or a glyph stamped at the point), 2 points -> line,
  3+ points: odd id -> closed polygon, even id -> smooth closed curve.
- A `~` right after the last number of a run (`4~`) leaves it open: an open polyline (odd id) or an
  open smooth curve (even id), e.g. a smile.
- Position: x = column, y = row * ASPECT (text rows are taller than columns).
- Parameters fill / stroke / width / sizes / smooth / shift / rotate / scale are a value or a dict
  {part id: value, '*': default}. shift = (columns, rows), rotate = degrees (clockwise, about the part
  center), scale = factor or (sx, sy) about the part center (for a dot or a stamped drawing: its size);
  scale 0 hides the part.
- A dict passed to a parameter whose default is a dict is overlaid on that default.
- A Shape used as a `fill` value of a single point is stamped at the point: at its natural size, or
  stretched to the `sizes` of that point (a number or (width, height)).
"""

import inspect
import math
from dataclasses import dataclass, field

from ..drawing import draw
from ..drawing.flatten import NAMED_COLORS

ASPECT = 2.0
KAPPA = 0.5522847498307936          # cubic handle length for a quarter circle
DEFAULT_WIDTH = 0.15                # stroke width, in grid columns
DEFAULT_SMOOTH = 0.5
DEFAULT_SIZE = 1.5

SIZES = {"tiny": 0.7, "small": 1.0, "medium": 1.5, "large": 2.5, "huge": 4.0}
COLORS = {name: name for name in NAMED_COLORS}
COLORS["none"] = "none"

PARAMS = ("fill", "stroke", "width", "sizes", "smooth", "shift", "rotate", "scale")


class ShapeError(Exception):
    pass


# ====================================================================================================
# Data
# ====================================================================================================

@dataclass
class Part:
    id: int
    kind: str                      # 'point' | 'line' | 'polygon' | 'smooth'
    points: list                   # [(x, y)] in grid units (y already multiplied by ASPECT)
    fill: object = None            # color, or a Shape (glyph) for points
    stroke: object = "black"
    width: float = DEFAULT_WIDTH
    smooth: float = DEFAULT_SMOOTH
    size: tuple = (DEFAULT_SIZE, DEFAULT_SIZE)     # (width, height) of a dot / stamped glyph
    angle: float = 0.0                             # rotation in degrees (stamped glyphs)
    hidden: bool = False
    open: bool = False                             # 3+ points not closed (marked with `~`)

    def extent(self):
        xs, ys = [p[0] for p in self.points], [p[1] for p in self.points]
        rx, ry = (self.size[0] / 2, self.size[1] / 2) if self.kind == "point" else (0.0, 0.0)
        return min(xs) - rx, min(ys) - ry, max(xs) + rx, max(ys) + ry


def pick(value, key, default):
    """Value of a per-part parameter: scalar, or dict {id: value, '*': default}."""
    if isinstance(value, dict):
        if key in value:
            return value[key]
        return value.get("*", default)
    return default if value is None else value


def defaults_of(fn):
    return {k: v.default for k, v in inspect.signature(fn).parameters.items() if v.default is not v.empty}


def build_shape(grid, name, params, defaults, aspect=ASPECT):
    """`__shape__`: called by the code generated for every drawing def."""
    p = {}
    for key, value in params.items():
        default = defaults.get(key)
        p[key] = {**default, **value} if isinstance(value, dict) and isinstance(default, dict) else value

    cells, open_marks = {}, set()
    for item in grid:
        number, x, row = item[:3]
        cells[number] = (x, row * aspect)
        if len(item) > 3 and item[3]:
            open_marks.add(number)
    numbers = sorted(cells)
    runs = []
    for n in numbers:
        if runs and n == runs[-1][-1] + 1:
            runs[-1].append(n)
        else:
            runs.append([n])

    parts = []
    for run in runs:
        pid = run[0]
        pts = [cells[n] for n in run]
        misplaced = [n for n in run[:-1] if n in open_marks]
        if misplaced:
            raise ShapeError(f"{name}: '~' on {misplaced[0]}: it can only mark the last number of a run "
                             f"(here {run[-1]})")
        is_open = run[-1] in open_marks and len(run) >= 3
        kind = "point" if len(pts) == 1 else "line" if len(pts) == 2 else "polygon" if pid % 2 else "smooth"
        fill = pick(p.get("fill"), pid, None)
        if isinstance(fill, Shape) and kind != "point":
            raise ShapeError(f"{name}: a shape can only be stamped on a single point, not on part {pid}")
        stroke = pick(p.get("stroke"), pid, "black")
        smooth = pick(p.get("smooth"), pid, DEFAULT_SMOOTH)
        size = pick(p.get("sizes"), pid, None)
        width = pick(p.get("width"), pid, DEFAULT_WIDTH)
        shift = pick(p.get("shift"), pid, (0, 0))
        rotate = pick(p.get("rotate"), pid, 0.0)
        scale = pick(p.get("scale"), pid, 1.0)
        for label, v in (("smooth", smooth), ("width", width), ("rotate", rotate)):
            if not isinstance(v, (int, float)):
                raise ShapeError(f"{name}: '{label}' of part {pid} must be a number, got {v!r}")
        hidden = isinstance(scale, (int, float)) and scale == 0
        if isinstance(scale, (int, float)):
            scale = (scale, scale)
        if not (isinstance(scale, (tuple, list)) and len(scale) == 2 and all(isinstance(v, (int, float)) for v in scale)):
            raise ShapeError(f"{name}: 'scale' of part {pid} must be a number or (sx, sy), got {scale!r}")
        if not (isinstance(shift, (tuple, list)) and len(shift) == 2 and all(isinstance(v, (int, float)) for v in shift)):
            raise ShapeError(f"{name}: 'shift' of part {pid} must be (columns, rows), got {shift!r}")
        if size is None:                                   # natural size: the stamped drawing's, or a default dot
            if isinstance(fill, Shape):
                x0, y0, x1, y1 = fill.bbox()
                size = (x1 - x0, y1 - y0)
            else:
                size = DEFAULT_SIZE
        if isinstance(size, (int, float)):
            size = (size, size)
        if not (isinstance(size, (tuple, list)) and len(size) == 2 and all(isinstance(v, (int, float)) for v in size)):
            raise ShapeError(f"{name}: 'sizes' of part {pid} must be a number or (width, height), got {size!r}")
        dx, dy = shift[0], shift[1] * aspect
        if kind == "point":
            pts = [(pts[0][0] + dx, pts[0][1] + dy)]
            size = (size[0] * scale[0], size[1] * scale[1])
        else:
            cx = sum(q[0] for q in pts) / len(pts)
            cy = sum(q[1] for q in pts) / len(pts)
            ca, sa = math.cos(math.radians(rotate)), math.sin(math.radians(rotate))
            local = [((q[0] - cx) * scale[0], (q[1] - cy) * scale[1]) for q in pts]
            pts = [(cx + u * ca - v * sa + dx, cy + u * sa + v * ca + dy) for u, v in local]
        parts.append(Part(pid, kind, pts, fill, stroke, float(width), min(1.0, max(0.0, float(smooth))),
                          (float(size[0]), float(size[1])), float(rotate) if kind == "point" else 0.0, hidden,
                          is_open))
    return Shape(name, parts)


# ====================================================================================================
# Geometry
# ====================================================================================================

def _r(v):
    return round(v, 4)


def smooth_closed_path(points, smooth, **style):
    """Closed path through the (rounded) corners of `points`.

    Each corner is replaced by a cubic from A (a fraction t = smooth / 2 of the way toward the previous
    point) to B (toward the next one), the corner being the control polygon: smooth = 1 on a square
    gives a circle, smooth = 0 the polygon itself.
    """
    n = len(points)
    t = 0.5 * smooth
    corners = []
    for i, p in enumerate(points):
        prev, nxt = points[i - 1], points[(i + 1) % n]
        a = (p[0] + t * (prev[0] - p[0]), p[1] + t * (prev[1] - p[1]))
        b = (p[0] + t * (nxt[0] - p[0]), p[1] + t * (nxt[1] - p[1]))
        corners.append((a, p, b))
    path = draw.Path(**style)
    path.M(_r(corners[0][2][0]), _r(corners[0][2][1]))
    cur = corners[0][2]
    for a, p, b in corners[1:] + corners[:1]:
        if (_r(a[0]), _r(a[1])) != (_r(cur[0]), _r(cur[1])):
            path.L(_r(a[0]), _r(a[1]))
        c1 = (a[0] + KAPPA * (p[0] - a[0]), a[1] + KAPPA * (p[1] - a[1]))
        c2 = (b[0] + KAPPA * (p[0] - b[0]), b[1] + KAPPA * (p[1] - b[1]))
        path.C(_r(c1[0]), _r(c1[1]), _r(c2[0]), _r(c2[1]), _r(b[0]), _r(b[1]))
        cur = b
    return path.Z()


def smooth_open_path(points, smooth, **style):
    """Open path: the end points stay where they are, the corners in between are rounded as in
    `smooth_closed_path`. A corner next to a free end may use that whole end segment (fraction `smooth`
    instead of `smooth / 2`), so smooth = 1 on three points is a single smooth cubic."""
    n = len(points)
    path = draw.Path(**style)
    path.M(_r(points[0][0]), _r(points[0][1]))
    cur = points[0]

    def line_to(q):
        nonlocal cur
        if (_r(q[0]), _r(q[1])) != (_r(cur[0]), _r(cur[1])):
            path.L(_r(q[0]), _r(q[1]))
            cur = q

    for i in range(1, n - 1):
        p, prev, nxt = points[i], points[i - 1], points[i + 1]
        fa = smooth if i - 1 == 0 else 0.5 * smooth
        fb = smooth if i + 1 == n - 1 else 0.5 * smooth
        a = (p[0] + fa * (prev[0] - p[0]), p[1] + fa * (prev[1] - p[1]))
        b = (p[0] + fb * (nxt[0] - p[0]), p[1] + fb * (nxt[1] - p[1]))
        line_to(a)
        c1 = (a[0] + KAPPA * (p[0] - a[0]), a[1] + KAPPA * (p[1] - a[1]))
        c2 = (b[0] + KAPPA * (p[0] - b[0]), b[1] + KAPPA * (p[1] - b[1]))
        path.C(_r(c1[0]), _r(c1[1]), _r(c2[0]), _r(c2[1]), _r(b[0]), _r(b[1]))
        cur = b
    line_to(points[-1])
    return path


def _color(c, default="none"):
    return default if c is None else c


@dataclass
class Shape:
    name: str
    parts: list = field(default_factory=list)

    # ----- geometry ---------------------------------------------------------------------------------

    def bbox(self):
        ext = [p.extent() for p in self.parts]
        return (min(e[0] for e in ext), min(e[1] for e in ext), max(e[2] for e in ext), max(e[3] for e in ext))

    def __repr__(self):
        return f"<Shape {self.name}: {', '.join(f'{p.id}:{p.kind}' for p in self.parts)}>"

    # ----- drawsvg elements -------------------------------------------------------------------------

    def _part_elements(self, part, width_factor=1.0):
        stroke = _color(part.stroke)
        style = dict(stroke=stroke, stroke_width=_r(part.width * width_factor))
        pts = part.points
        if part.kind == "point":
            (x, y), (w, h) = pts[0], part.size
            if isinstance(part.fill, Shape):
                return [self._glyph(part.fill, x, y, w, h, width_factor, part.angle)]
            fill = part.fill if part.fill is not None else (stroke if stroke != "none" else "black")
            if abs(w - h) < 1e-9:
                return [draw.Circle(_r(x), _r(y), _r(w / 2), fill=fill, **style)]
            return [draw.Ellipse(_r(x), _r(y), _r(w / 2), _r(h / 2), fill=fill, **style)]
        if part.kind == "line":
            return [draw.Line(_r(pts[0][0]), _r(pts[0][1]), _r(pts[1][0]), _r(pts[1][1]), fill="none", **style)]
        fill = _color(part.fill)
        if part.kind == "polygon" or part.smooth <= 1e-9:
            flat = [_r(v) for p in pts for v in p]
            return [draw.Lines(*flat, close=not part.open, fill=fill, **style)]
        if part.open:
            return [smooth_open_path(pts, part.smooth, fill=fill, **style)]
        return [smooth_closed_path(pts, part.smooth, fill=fill, **style)]

    def _glyph(self, glyph, x, y, w, h, width_factor=1.0, angle=0.0):
        """Stamp `glyph` centered at (x, y), stretched to a w x h box. A flat axis (a line) is not stretched,
        and stroke widths keep their size (they are divided by the stretch)."""
        gx0, gy0, gx1, gy1 = glyph.bbox()
        gw, gh = gx1 - gx0, gy1 - gy0
        sx = w / gw if gw > 1e-9 else 1.0
        sy = h / gh if gh > 1e-9 else 1.0
        rot = f"rotate({_r(angle)}) " if angle else ""
        tr = (f"translate({_r(x)} {_r(y)}) {rot}scale({_r(sx)} {_r(sy)}) "
              f"translate({_r(-(gx0 + gx1) / 2)} {_r(-(gy0 + gy1) / 2)})")
        group = draw.Group(transform=tr)
        compensate = width_factor / (abs(sx * sy) ** 0.5)
        for part in glyph.parts:
            if part.hidden:
                continue
            for e in self._part_elements(part, compensate):
                group.append(e)
        return group

    def to_drawing(self, cell=10.0, margin=1.0, bbox=None):
        """A drawsvg Drawing (cell = pixels per grid column). One top-level Group `p<id>` per part:
        they become the Grease Pencil layers."""
        x0, y0, x1, y1 = bbox or self.bbox()
        x0, y0, x1, y1 = x0 - margin, y0 - margin, x1 + margin, y1 + margin
        d = draw.Drawing((x1 - x0) * cell, (y1 - y0) * cell, origin=(x0 * cell, y0 * cell))
        for part in self.parts:
            if part.hidden:
                continue
            g = draw.Group(id=f"p{part.id}", transform=f"scale({cell})")
            for e in self._part_elements(part):
                g.append(e)
            d.append(g)
        return d

    def to_svg(self, **kw):
        return self.to_drawing(**kw).as_svg()

    def save_svg(self, path, **kw):
        self.to_drawing(**kw).save_svg(path)

    def to_grease_pencil(self, gp=None, frame=1, cell=10.0, margin=1.0, bbox=None, **kw):
        from ..drawing import to_grease_pencil
        return to_grease_pencil(self.to_drawing(cell=cell, margin=margin, bbox=bbox), gp, frame=frame, **kw)


def union_bbox(shapes):
    boxes = [s.bbox() for s in shapes]
    return (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))


def frames_to_grease_pencil(shapes, gp=None, start=1, step=1, cell=10.0, margin=1.0, name="Kaomoji", **kw):
    """One keyframe per shape (same framing for all of them, so the picture does not jump)."""
    import bpy
    shapes = list(shapes)
    gp = gp or bpy.data.grease_pencils.new(name)
    box = union_bbox(shapes)
    numbers = [start + k * step for k in range(len(shapes))]
    for n, s in zip(numbers, shapes):
        s.to_grease_pencil(gp, frame=n, cell=cell, margin=margin, bbox=box, **kw)
    # a layer without a keyframe keeps showing its previous drawing: add empty keyframes (hidden parts)
    for layer in gp.layers:
        have = {f.frame_number for f in layer.frames}
        for n in numbers:
            if n not in have:
                layer.frames.new(n)
    return gp
