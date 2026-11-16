"""Draw with Geometry Nodes: shapes built from socket values, so a drawing can be driven by modifier inputs.

Use inside a `GeoNodes` tree. Coordinates are SVG-like (x right, y down, any unit); every number can be a
Python number or a socket (Float, ...). `build()` returns a Grease Pencil socket:

    with GeoNodes("Face"):
        blink = Float(0., "Blink", 0, 1)
        dr = NodeDrawing(scale=0.01)
        with dr.group("eyes", stroke="#222", width=3) as g:
            g.ellipse(-45, -25, 20, 20*(1 - blink).max(0.05))
        with dr.group("mouth", stroke="#222", fill="#aa3344") as g:
            g.path().M(-30, 35).Q(0, 70, 30, 35).Z()
        dr.build().out()

- a group is a Grease Pencil layer (named, via Set Geometry Name + instances as layers)
- stroke / fill / opacity / width are per group; stroke, fill and width may be sockets too
- Beziers are sampled to polylines (`resolution` segments per curve), so that connected segments
  become one stroke and closed paths can be filled.
"""

from contextlib import contextmanager

from geonodes import Curve, Float, Vector, nd, pi, Mesh
from geonodes import GreasePencil
from .flatten import parse_color


def _vec(x, y):
    return Vector((x, y, 0.0))


class NodePath:
    """Absolute path commands M L Q C Z whose coordinates can be sockets."""

    def __init__(self, group):
        self.group = group
        self.segments = []
        self.start = None
        self.cur = None

    def M(self, x, y):
        self._flush_if_needed()
        self.start = self.cur = (x, y)
        return self

    def _flush_if_needed(self):
        if self.segments:
            self.group._add_connected(self.segments)
            self.segments = []

    def _need_start(self):
        if self.cur is None:
            raise ValueError("A path must start with M(x, y)")

    def L(self, x, y):
        self._need_start()
        self.segments.append(Curve.Line(start=_vec(*self.cur), end=_vec(x, y)))
        self.cur = (x, y)
        return self

    def Q(self, cx, cy, x, y):
        self._need_start()
        self.segments.append(Curve.QuadraticBezier(
            resolution=self.group.resolution, start=_vec(*self.cur), middle=_vec(cx, cy), end=_vec(x, y)))
        self.cur = (x, y)
        return self

    def C(self, c1x, c1y, c2x, c2y, x, y):
        self._need_start()
        self.segments.append(Curve.BezierSegment(
            resolution=self.group.resolution, start=_vec(*self.cur), start_handle=_vec(c1x, c1y),
            end_handle=_vec(c2x, c2y), end=_vec(x, y)))
        self.cur = (x, y)
        return self

    def Z(self):
        """Close the path with a straight segment back to the start (then starts over)."""
        self._need_start()
        self.L(*self.start)
        self._flush_if_needed()
        self.cur = self.start
        return self

    def done(self):
        self._flush_if_needed()
        return self.group


class NodeGroup:
    """A layer: a set of shapes sharing stroke, fill, opacity and width."""

    def __init__(self, drawing, name, stroke, fill, width, opacity):
        self.drawing = drawing
        self.name = name
        self.stroke = stroke
        self.fill = fill
        self.width = width
        self.opacity = opacity
        self.resolution = drawing.resolution
        self.shapes = []
        self._paths = []

    # ----- shapes ---------------------------------------------------------------------------------

    def _add_connected(self, segments):
        """Join segments into a single curve (one spline when they chain, cyclic when they close)."""
        curve = segments[0]
        if len(segments) > 1:
            curve = Curve(segments[0].join(*segments[1:]))
        mesh = Mesh(curve.to_mesh())
        mesh.merge_by_distance(distance=1e-3)
        self.shapes.append(mesh.to_curve())

    def path(self):
        p = NodePath(self)
        self._paths.append(p)
        return p

    def line(self, x1, y1, x2, y2):
        self.shapes.append(Curve.Line(start=_vec(x1, y1), end=_vec(x2, y2)))
        return self

    def polyline(self, *points, close=False):
        p = self.path().M(*points[0])
        for pt in points[1:]:
            p.L(*pt)
        if close:
            p.Z()
        p.done()
        return self

    def rect(self, x, y, w, h):
        return self.polyline((x, y), (x + w, y), (x + w, y + h), (x, y + h), close=True)

    def ellipse(self, cx, cy, rx, ry):
        circle = Curve.Circle(resolution=4 * self.resolution, radius=1.0)
        self.shapes.append(circle.transform(translation=_vec(cx, cy), scale=Vector((rx, ry, 1.0))))
        return self

    def circle(self, cx, cy, r):
        return self.ellipse(cx, cy, r, r)

    def arc(self, cx, cy, r, start_deg, end_deg):
        """Circular arc, angles in degrees from the x axis toward +y (as drawsvg)."""
        arc = Curve.Arc(resolution=self.resolution, radius=r, start_angle=start_deg * pi / 180,
                        sweep_angle=(end_deg - start_deg) * pi / 180)
        self.shapes.append(arc.transform(translation=_vec(cx, cy)))
        return self

    # ----- context manager ------------------------------------------------------------------------

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        for p in self._paths:
            p.done()
        return False

    def curves(self):
        for p in self._paths:
            p.done()
        self._paths = []
        if not self.shapes:
            return None
        first = self.shapes[0]
        geo = first if len(self.shapes) == 1 else first.join(*self.shapes[1:])
        # SVG space (x right, y down) -> Blender XZ plane (z up)
        s = self.drawing.scale
        curve = Curve(geo).transform(scale=Vector((s, -s, s)), rotation=(pi / 2, 0, 0))
        return Curve(curve).set_radius(Float(self.width) * (self.drawing.width_scale * s))


class NodeDrawing:
    """Collects groups and builds one Grease Pencil with one named layer per group."""

    def __init__(self, scale=0.01, resolution=12, width_scale=0.5):
        self.scale = scale
        self.resolution = resolution
        self.width_scale = width_scale
        self.groups = []

    def group(self, name, stroke="black", fill=None, width=2.0, opacity=1.0):
        g = NodeGroup(self, name, stroke, fill, width, opacity)
        self.groups.append(g)
        return g

    def build(self):
        named = []
        for g in self.groups:
            curves = g.curves()
            if curves is not None:
                named.append((g, nd.set_geometry_name(curves, g.name)))
        if not named:
            raise ValueError("Nothing to draw")
        instances = named[0][1].to_instance(*[n[1] for n in named[1:]])
        gp = Curve(instances).to_grease_pencil(instances_as_layers=True)
        for g, _ in named:
            sel = GreasePencil.named_selection(g.name)
            if g.stroke is not None:
                gp = nd.set_grease_pencil_color(gp, selection=sel, color=_color(g.stroke), opacity=g.opacity, mode='STROKE')
            if g.fill is not None:
                gp = nd.set_grease_pencil_color(gp, selection=sel, color=_color(g.fill), opacity=g.opacity, mode='FILL')
        return GreasePencil(gp)


def _color(value):
    if isinstance(value, (str, tuple, list)):
        rgba = parse_color(value)
        return rgba if rgba is not None else (0, 0, 0, 0)
    return value        # a Color socket
