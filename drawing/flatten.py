"""Flatten a drawsvg Drawing into polylines (pure Python: this module does not use bpy).

Supported: Path / Lines / Line / Arc, Circle, Ellipse, Rectangle, Group and
`transform` attributes (matrix, translate, scale, rotate, skewX, skewY),
inherited stroke / fill / stroke-width / opacity.
Not supported (reported in `warnings`): Use, Text, Image, ArcLine, gradients.

Coordinates are returned as in the SVG (y pointing down).
"""

import math
import re
from dataclasses import dataclass, field

from . import drawsvg as ds
from .drawsvg import elements as el

# ====================================================================================================
# Colors
# ====================================================================================================

NAMED_COLORS = {
    'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 128, 0),
    'lime': (0, 255, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0), 'cyan': (0, 255, 255),
    'aqua': (0, 255, 255), 'magenta': (255, 0, 255), 'fuchsia': (255, 0, 255),
    'gray': (128, 128, 128), 'grey': (128, 128, 128), 'silver': (192, 192, 192),
    'maroon': (128, 0, 0), 'olive': (128, 128, 0), 'navy': (0, 0, 128), 'purple': (128, 0, 128),
    'teal': (0, 128, 128), 'orange': (255, 165, 0), 'pink': (255, 192, 203),
    'brown': (165, 42, 42), 'gold': (255, 215, 0),
}


def parse_color(value):
    """CSS color -> (r, g, b, a) floats in [0, 1], or None for 'none' / unset."""
    if value is None:
        return None
    if isinstance(value, (tuple, list)):
        v = list(value) + [1.0] * (4 - len(value))
        return tuple(float(x) for x in v[:4])
    s = str(value).strip().lower()
    if s in ('none', 'transparent', ''):
        return None
    if s.startswith('#'):
        h = s[1:]
        if len(h) in (3, 4):
            h = ''.join(c * 2 for c in h)
        if len(h) in (6, 8):
            r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
            a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
            return (r, g, b, a)
    m = re.fullmatch(r'rgba?\(([^)]*)\)', s)
    if m:
        parts = [p.strip() for p in re.split(r'[,\s/]+', m.group(1).strip()) if p.strip()]

        def chan(p):
            return float(p[:-1]) / 100 if p.endswith('%') else float(p) / 255

        r, g, b = (chan(p) for p in parts[:3])
        a = 1.0
        if len(parts) > 3:
            a = float(parts[3][:-1]) / 100 if parts[3].endswith('%') else float(parts[3])
        return (r, g, b, a)
    if s in NAMED_COLORS:
        r, g, b = NAMED_COLORS[s]
        return (r / 255, g / 255, b / 255, 1.0)
    raise ValueError(f"Unsupported color: {value!r}")


# ====================================================================================================
# Transforms: affine matrices (a, b, c, d, e, f) as in SVG
# ====================================================================================================

IDENTITY = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def mat_mul(m, n):
    """m * n: n is applied first."""
    a1, b1, c1, d1, e1, f1 = m
    a2, b2, c2, d2, e2, f2 = n
    return (a1 * a2 + c1 * b2, b1 * a2 + d1 * b2,
            a1 * c2 + c1 * d2, b1 * c2 + d1 * d2,
            a1 * e2 + c1 * f2 + e1, b1 * e2 + d1 * f2 + f1)


def mat_apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


_NUM = r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?'


def parse_transform(text):
    """SVG transform attribute -> matrix."""
    m = IDENTITY
    if not text:
        return m
    for name, args in re.findall(r'(\w+)\s*\(([^)]*)\)', str(text)):
        v = [float(x) for x in re.findall(_NUM, args)]
        if name == 'matrix' and len(v) == 6:
            t = tuple(v)
        elif name == 'translate':
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0.0)
        elif name == 'scale':
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif name == 'rotate':
            r = math.radians(v[0])
            c, s = math.cos(r), math.sin(r)
            t = (c, s, -s, c, 0, 0)
            if len(v) == 3:
                t = mat_mul(mat_mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        elif name == 'skewX':
            t = (1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        elif name == 'skewY':
            t = (1, math.tan(math.radians(v[0])), 0, 1, 0, 0)
        else:
            raise ValueError(f"Unsupported transform: {name}({args})")
        m = mat_mul(m, t)
    return m


# ====================================================================================================
# Path geometry
# ====================================================================================================

_PATH_TOKEN = re.compile(r'([MmLlHhVvCcSsQqTtAaZz])|(' + _NUM + r')')
_ARITY = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'C': 6, 'S': 4, 'Q': 4, 'T': 2, 'A': 7, 'Z': 0}


def _tokens(d):
    # Arc flags may be glued ("a1 1 0 01 5 5"): handled by reading numbers lazily
    return [m.group(0) for m in _PATH_TOKEN.finditer(d)]


def _arc_center(x1, y1, rx, ry, phi, large, sweep, x2, y2):
    """Endpoint arc -> (cx, cy, rx, ry, t1, dt) (center parameterization)."""
    rx, ry = abs(rx), abs(ry)
    p = math.radians(phi)
    cp, sp = math.cos(p), math.sin(p)
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    x1p, y1p = cp * dx + sp * dy, -sp * dx + cp * dy
    lam = (x1p / rx) ** 2 + (y1p / ry) ** 2
    if lam > 1:
        s = math.sqrt(lam)
        rx, ry = rx * s, ry * s
    num = rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    co = math.sqrt(max(0.0, num / den)) if den else 0.0
    if bool(large) == bool(sweep):
        co = -co
    cxp, cyp = co * rx * y1p / ry, -co * ry * x1p / rx
    cx = cp * cxp - sp * cyp + (x1 + x2) / 2
    cy = sp * cxp + cp * cyp + (y1 + y2) / 2

    def ang(ux, uy, vx, vy):
        a = math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
        return a

    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not sweep and dt > 0:
        dt -= 2 * math.pi
    elif sweep and dt < 0:
        dt += 2 * math.pi
    return cx, cy, rx, ry, t1, dt


def _arc_points(x1, y1, rx, ry, phi, large, sweep, x2, y2, n):
    """Endpoint arc -> list of points (excluding start, including end)."""
    if (x1, y1) == (x2, y2):
        return []
    if rx == 0 or ry == 0:
        return [(x2, y2)]
    cx, cy, rx, ry, t1, dt = _arc_center(x1, y1, rx, ry, phi, large, sweep, x2, y2)
    cp, sp = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    count = max(2, int(math.ceil(n * abs(dt) / (math.pi / 2))))
    pts = []
    for i in range(1, count + 1):
        t = t1 + dt * i / count
        x = cp * rx * math.cos(t) - sp * ry * math.sin(t) + cx
        y = sp * rx * math.cos(t) + cp * ry * math.sin(t) + cy
        pts.append((x, y))
    pts[-1] = (x2, y2)
    return pts


def _arc_cubics(x1, y1, rx, ry, phi, large, sweep, x2, y2):
    """Endpoint arc -> list of cubic segments (c1, c2, end), each spanning at most 90 degrees."""
    if (x1, y1) == (x2, y2):
        return []
    if rx == 0 or ry == 0:
        return [((x1, y1), (x2, y2), (x2, y2))]
    cx, cy, rx, ry, t1, dt = _arc_center(x1, y1, rx, ry, phi, large, sweep, x2, y2)
    p = math.radians(phi)
    cp, sp = math.cos(p), math.sin(p)

    def pt(t):
        return (cp * rx * math.cos(t) - sp * ry * math.sin(t) + cx,
                sp * rx * math.cos(t) + cp * ry * math.sin(t) + cy)

    def der(t):
        return (-cp * rx * math.sin(t) - sp * ry * math.cos(t),
                -sp * rx * math.sin(t) + cp * ry * math.cos(t))

    count = max(1, int(math.ceil(abs(dt) / (math.pi / 2) - 1e-9)))
    step = dt / count
    k = 4.0 / 3.0 * math.tan(step / 4)
    out = []
    for i in range(count):
        ta, tb = t1 + step * i, t1 + step * (i + 1)
        a, b = pt(ta), pt(tb)
        da, db = der(ta), der(tb)
        end = (x2, y2) if i == count - 1 else b
        out.append(((a[0] + k * da[0], a[1] + k * da[1]), (b[0] - k * db[0], b[1] - k * db[1]), end))
    return out


def path_events(d):
    """SVG path data -> absolute events: ('M', p) ('L', p) ('C', c1, c2, e) ('A', rx, ry, rot, large, sweep, e) ('Z',).

    Quadratics are raised to cubics; H / V / relative / smooth commands are resolved.
    """
    toks = _tokens(d)
    i = 0
    cmd = None
    x = y = 0.0
    sx = sy = 0.0
    last_c2 = last_q = None
    started = False

    def num():
        nonlocal i
        v = float(toks[i])
        i += 1
        return v

    while i < len(toks):
        t = toks[i]
        if re.fullmatch(r'[A-Za-z]', t):
            cmd = t
            i += 1
            if cmd in 'Zz':
                yield ('Z',)
                x, y = sx, sy
                started = False
                last_c2 = last_q = None
                continue
        elif cmd is None:
            raise ValueError("Path data must start with a command")
        up = cmd.upper()
        rel = cmd.islower()
        ox, oy = (x, y) if rel else (0.0, 0.0)
        if up == 'M':
            x, y = num() + ox, num() + oy
            sx, sy = x, y
            started = True
            yield ('M', (x, y))
            cmd = 'l' if rel else 'L'   # implicit lineto
            last_c2 = last_q = None
            continue
        if not started:
            yield ('M', (x, y))
            started = True
        if up == 'L':
            x, y = num() + ox, num() + oy
            yield ('L', (x, y))
            last_c2 = last_q = None
        elif up == 'H':
            x = num() + (x if rel else 0.0)
            yield ('L', (x, y))
            last_c2 = last_q = None
        elif up == 'V':
            y = num() + (y if rel else 0.0)
            yield ('L', (x, y))
            last_c2 = last_q = None
        elif up in 'CS':
            if up == 'C':
                c1 = (num() + ox, num() + oy)
            else:
                c1 = (2 * x - last_c2[0], 2 * y - last_c2[1]) if last_c2 else (x, y)
            c2 = (num() + ox, num() + oy)
            e = (num() + ox, num() + oy)
            yield ('C', c1, c2, e)
            x, y = e
            last_c2, last_q = c2, None
        elif up in 'QT':
            if up == 'Q':
                q = (num() + ox, num() + oy)
            else:
                q = (2 * x - last_q[0], 2 * y - last_q[1]) if last_q else (x, y)
            e = (num() + ox, num() + oy)
            c1 = (x + 2 / 3 * (q[0] - x), y + 2 / 3 * (q[1] - y))
            c2 = (e[0] + 2 / 3 * (q[0] - e[0]), e[1] + 2 / 3 * (q[1] - e[1]))
            yield ('C', c1, c2, e)
            x, y = e
            last_q, last_c2 = q, None
        elif up == 'A':
            rx, ry, rot = num(), num(), num()
            large, sweep = num(), num()
            e = (num() + ox, num() + oy)
            yield ('A', rx, ry, rot, large, sweep, e)
            x, y = e
            last_c2 = last_q = None
        else:
            raise ValueError(f"Unknown path command {cmd!r}")


def path_to_subpaths(d, resolution=16):
    """SVG path data -> list of (points, closed), curves sampled to polylines."""
    subs, pts = [], []

    def finish(closed):
        nonlocal pts
        if len(pts) > 1 or (pts and closed):
            subs.append((pts, closed))
        pts = []

    for ev in path_events(d):
        kind = ev[0]
        if kind == 'M':
            finish(False)
            pts = [ev[1]]
        elif kind == 'Z':
            finish(True)
        elif kind == 'L':
            pts.append(ev[1])
        elif kind == 'C':
            x, y = pts[-1]
            _, c1, c2, e = ev
            for k in range(1, resolution + 1):
                u = k / resolution
                a, b, c, dd = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
                pts.append((a * x + b * c1[0] + c * c2[0] + dd * e[0],
                            a * y + b * c1[1] + c * c2[1] + dd * e[1]))
        elif kind == 'A':
            _, rx, ry, rot, large, sweep, e = ev
            x, y = pts[-1]
            pts.extend(_arc_points(x, y, rx, ry, rot, large, sweep, e[0], e[1], resolution))
    finish(False)
    return subs


@dataclass
class Anchor:
    """Bezier anchor: position and the absolute positions of its two handles."""
    p: tuple
    hl: tuple = None
    hr: tuple = None

    def __post_init__(self):
        self.hl = self.hl or self.p
        self.hr = self.hr or self.p


def path_to_beziers(d):
    """SVG path data -> list of (anchors, closed) with cubic Bezier handles.

    Straight segments keep both handles on the anchor. When a closed sub-path ends on its
    start point, the last anchor is merged into the first one.
    """
    subs, cur = [], []

    def finish(closed):
        nonlocal cur
        if closed and len(cur) > 1 and cur[-1].p == cur[0].p:
            cur[0].hl = cur[-1].hl
            cur.pop()
        if len(cur) > 1 or (cur and closed):
            subs.append((cur, closed))
        cur = []

    for ev in path_events(d):
        kind = ev[0]
        if kind == 'M':
            finish(False)
            cur = [Anchor(ev[1])]
        elif kind == 'Z':
            finish(True)
        elif kind == 'L':
            cur.append(Anchor(ev[1]))
        elif kind == 'C':
            _, c1, c2, e = ev
            cur[-1].hr = c1
            cur.append(Anchor(e, hl=c2))
        elif kind == 'A':
            _, rx, ry, rot, large, sweep, e = ev
            x, y = cur[-1].p
            for c1, c2, end in _arc_cubics(x, y, rx, ry, rot, large, sweep, e[0], e[1]):
                cur[-1].hr = c1
                cur.append(Anchor(end, hl=c2))
    finish(False)
    return subs


KAPPA = 4.0 / 3.0 * (math.sqrt(2) - 1)


def ellipse_beziers(cx, cy, rx, ry):
    """Closed ellipse as four cubic segments (anchors at the extremities)."""
    kx, ky = rx * KAPPA, ry * KAPPA
    return [
        Anchor((cx + rx, cy), hl=(cx + rx, cy - ky), hr=(cx + rx, cy + ky)),
        Anchor((cx, cy + ry), hl=(cx + kx, cy + ry), hr=(cx - kx, cy + ry)),
        Anchor((cx - rx, cy), hl=(cx - rx, cy + ky), hr=(cx - rx, cy - ky)),
        Anchor((cx, cy - ry), hl=(cx - kx, cy - ry), hr=(cx + kx, cy - ry)),
    ]


def sample_bezier(anchors, closed, resolution=16):
    """Anchors -> polyline (the closing segment is implicit for closed shapes)."""
    pts = [anchors[0].p]
    pairs = list(zip(anchors, anchors[1:]))
    if closed and len(anchors) > 1:
        pairs.append((anchors[-1], anchors[0]))
    for a, b in pairs:
        if a.hr == a.p and b.hl == b.p:
            pts.append(b.p)
            continue
        for k in range(1, resolution + 1):
            u = k / resolution
            w = ((1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3)
            pts.append((w[0] * a.p[0] + w[1] * a.hr[0] + w[2] * b.hl[0] + w[3] * b.p[0],
                        w[0] * a.p[1] + w[1] * a.hr[1] + w[2] * b.hl[1] + w[3] * b.p[1]))
    if closed and len(pts) > 1 and pts[-1] == pts[0]:
        pts.pop()
    return pts


def _ellipse_points(cx, cy, rx, ry, n):
    return [(cx + rx * math.cos(2 * math.pi * k / n), cy + ry * math.sin(2 * math.pi * k / n))
            for k in range(n)]


# ====================================================================================================
# Flattening
# ====================================================================================================

@dataclass
class Stroke:
    """A polyline with its style. Coordinates in SVG space (y down)."""
    points: list
    closed: bool = False
    stroke: tuple = None        # RGBA or None
    fill: tuple = None          # RGBA or None
    width: float = 1.0
    layer: str = 'Drawing'
    id: str = None
    bezier: list = None         # list of Anchor (same shape as `points`, with handles)


@dataclass
class _Style:
    stroke: object = None
    fill: object = 'black'
    width: float = 1.0
    opacity: float = 1.0


def _num_attr(args, key, default=0.0):
    v = args.get(key, default)
    return default if v is None else float(v)


def flatten(drawing, resolution=16, default_layer='Drawing'):
    """Return (strokes, warnings). Top level Groups become layers (named by `id`).

    Each Stroke has `points` (curves sampled to `resolution` segments) and `bezier` (anchors with handles).
    """
    strokes, warnings = [], []
    elems = drawing.elements if hasattr(drawing, 'elements') else list(drawing)

    def walk(elem, matrix, style, layer):
        args = getattr(elem, 'args', {})
        if args.get('display') == 'none' or args.get('visibility') == 'hidden':
            return
        if 'transform' in args:
            matrix = mat_mul(matrix, parse_transform(args['transform']))
        st = _Style(
            stroke=args.get('stroke', style.stroke),
            fill=args.get('fill', style.fill),
            width=_num_attr(args, 'stroke-width', style.width),
            opacity=style.opacity * _num_attr(args, 'opacity', 1.0))

        if isinstance(elem, el.Group):
            for child in elem.children:
                walk(child, matrix, st, layer)
            return

        shapes = []   # (anchors, closed)
        if isinstance(elem, el.ArcLine):
            warnings.append("ArcLine is drawn with dash arrays: use drawsvg Arc instead")
            return
        elif isinstance(elem, el.Path):
            shapes.extend(path_to_beziers(args.get('d', '')))
        elif isinstance(elem, el.Circle):
            r = _num_attr(args, 'r')
            shapes.append((ellipse_beziers(_num_attr(args, 'cx'), _num_attr(args, 'cy'), r, r), True))
        elif isinstance(elem, el.Ellipse):
            shapes.append((ellipse_beziers(_num_attr(args, 'cx'), _num_attr(args, 'cy'),
                                           _num_attr(args, 'rx'), _num_attr(args, 'ry')), True))
        elif isinstance(elem, el.Rectangle):
            x, y = _num_attr(args, 'x'), _num_attr(args, 'y')
            w, h = _num_attr(args, 'width'), _num_attr(args, 'height')
            shapes.append(([Anchor(q) for q in ((x, y), (x + w, y), (x + w, y + h), (x, y + h))], True))
        elif elem.__class__.__name__ in ('NoElement',):
            return
        else:
            warnings.append(f"{elem.__class__.__name__} is not supported and was skipped")
            return

        stroke_c = parse_color(st.stroke)
        fill_c = parse_color(st.fill)
        for anchors, closed in shapes:
            if len(anchors) < 2:
                continue
            anchors = [Anchor(mat_apply(matrix, *a.p), mat_apply(matrix, *a.hl),
                              mat_apply(matrix, *a.hr)) for a in anchors]
            pts = sample_bezier(anchors, closed, resolution)
            if stroke_c is not None:
                stroke_rgba = stroke_c[:3] + (stroke_c[3] * st.opacity,)
            else:
                stroke_rgba = None
            fill_rgba = (fill_c[:3] + (fill_c[3] * st.opacity,)) if fill_c and closed else None
            strokes.append(Stroke(
                points=pts, bezier=anchors,
                closed=closed, stroke=stroke_rgba, fill=fill_rgba,
                width=st.width * math.sqrt(abs(matrix[0] * matrix[3] - matrix[1] * matrix[2])),
                layer=layer, id=args.get('id')))

    root_style = _Style()
    for e in elems:
        if isinstance(e, el.Group):
            gid = e.args.get('id') or default_layer
            walk(e, IDENTITY, root_style, str(gid))
        else:
            walk(e, IDENTITY, root_style, default_layer)
    return strokes, warnings
