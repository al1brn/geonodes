"""drawing.nodes: a drawing built from Geometry Nodes and driven by modifier inputs (Blender >= 5.x)."""
import math
import os
import sys

import bpy
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from geonodes.core_new.root.tree import Tree  # noqa: E402
from geonodes.demos2 import face_nodes, face_drawing  # noqa: E402
from geonodes.drawing import to_grease_pencil  # noqa: E402

NAMES = ['mouth', 'brows', 'pupils', 'eyes', 'head']      # layer order produced by the instances


class Rig:
    def __init__(self, tree_name):
        ng = bpy.data.node_groups[tree_name]
        self.ob = bpy.data.objects.new("rig_" + tree_name, bpy.data.grease_pencils.new("rig"))
        bpy.context.scene.collection.objects.link(self.ob)
        self.md = self.ob.modifiers.new("N", 'NODES')
        self.md.node_group = ng
        self.ids = {i.name: i.identifier for i in ng.interface.items_tree if i.in_out == 'INPUT'}

    def set(self, **values):
        for name, v in values.items():
            getattr(self.md.properties.inputs, self.ids[name.replace('_', ' ')]).value = v

    def layers(self):
        """name -> list of strokes, each stroke a dict (points, cyclic, bounds)."""
        self.ob.update_tag()
        bpy.context.view_layer.update()
        data = self.ob.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
        out = {}
        for layer in data.layers:
            strokes = []
            for f in layer.frames:
                for s in f.drawing.strokes:
                    pts = [tuple(p.position) for p in s.points]
                    xs, zs = [p[0] for p in pts], [p[2] for p in pts]
                    strokes.append(dict(n=len(pts), cyclic=s.cyclic, radius=s.points[0].radius,
                                        x=(min(xs), max(xs)), z=(min(zs), max(zs)),
                                        fill=tuple(s.fill_color), color=tuple(s.points[0].vertex_color)))
            out[layer.name] = strokes
        return out


@pytest.fixture(scope="module")
def rig():
    Tree.TREE_STACK.clear()
    face_nodes.demo(rebuild=True)
    yield Rig("Face Drawing")
    Tree.TREE_STACK.clear()


def test_layers_are_named(rig):
    rig.set(Blink=0.0)
    assert sorted(rig.layers()) == sorted(NAMES)


def test_blink_squashes_eyes(rig):
    rig.set(Blink=0.0)
    open_h = rig.layers()['eyes'][0]['z']
    rig.set(Blink=1.0)
    closed_h = rig.layers()['eyes'][0]['z']
    assert (closed_h[1] - closed_h[0]) < 0.3 * (open_h[1] - open_h[0])
    rig.set(Blink=0.0)


def test_look_moves_pupils(rig):
    rig.set(Look_X=-1.0)
    left = min(s['x'][0] for s in rig.layers()['pupils'])
    rig.set(Look_X=1.0)
    right = min(s['x'][0] for s in rig.layers()['pupils'])
    assert right > left
    rig.set(Look_X=0.0)


def test_vowels_change_mouth(rig):
    sizes = {}
    for v in range(6):
        rig.set(Vowel=float(v))
        m = rig.layers()['mouth'][0]
        sizes[v] = (m['x'][1] - m['x'][0], m['z'][1] - m['z'][0])
    assert sizes[1][1] > sizes[3][1] and sizes[3][0] > sizes[1][0]          # A taller, I wider
    assert len({tuple(round(x, 3) for x in s) for s in sizes.values()}) == 6
    rig.set(Vowel=0.0)


def test_color_socket_drives_layers(rig):
    layers = rig.layers()
    assert layers['mouth'][0]['fill'] == pytest.approx((0.67, 0.2, 0.27, 1.0), abs=1e-3)
    assert layers['head'][0]['color'] == pytest.approx((0.13, 0.13, 0.13, 1.0), abs=1e-3)
    assert layers['mouth'][0]['cyclic']


def test_parity_with_baked_drawing(rig):
    """The same pose gives the same layout in node mode and in baked (bpy) mode."""
    rig.set(Blink=0.0, Look_X=0.0, Look_Y=0.0, Vowel=1.0, Mouth_Open=1.0, Brow_Raise=0.0)
    nodes = rig.layers()
    gp = bpy.data.grease_pencils.new("baked")
    to_grease_pencil(face_drawing.face_drawing(vowel=1), gp, scale=0.01, bezier=False, resolution=12)   # sampled: Bezier anchors alone would miss curve extents
    for layer in gp.layers:
        pts = [tuple(p.position) for s in layer.frames[0].drawing.strokes for p in s.points]
        xs, zs = [p[0] for p in pts], [p[2] for p in pts]
        bx = (min(xs), max(xs))
        nx = (min(s['x'][0] for s in nodes[layer.name]), max(s['x'][1] for s in nodes[layer.name]))
        assert nx == pytest.approx(bx, abs=0.02), layer.name
        nz = (min(s['z'][0] for s in nodes[layer.name]), max(s['z'][1] for s in nodes[layer.name]))
        assert nz == pytest.approx((min(zs), max(zs)), abs=0.02), layer.name
    bpy.data.grease_pencils.remove(gp)


# ----------------------------------------------------------------------------------------------------
# Shapes

def shapes_rig(name, build):
    from geonodes import GeoNodes, Float
    from geonodes.drawing.nodes import NodeDrawing
    Tree.TREE_STACK.clear()
    with GeoNodes(name, rebuild=True):
        w = Float(2.0, "Width", 0, 20)
        dr = NodeDrawing(scale=0.01, resolution=8)
        build(dr, w)
        dr.build().out()
    return Rig(name)


def test_rect_is_one_closed_stroke():
    r = shapes_rig("ND Rect", lambda dr, w: dr.group("r", stroke="red").rect(-10, -20, 40, 30))
    s, = r.layers()['r']
    assert s['cyclic'] and s['n'] == 4
    assert s['x'] == pytest.approx((-0.1, 0.3), abs=1e-4) and s['z'] == pytest.approx((-0.1, 0.2), abs=1e-4)


def test_open_path_is_one_open_stroke():
    def build(dr, w):
        dr.group("p", stroke="black").path().M(0, 0).L(10, 0).C(20, 0, 20, 20, 10, 20)
    s, = shapes_rig("ND Open", build).layers()['p']
    assert not s['cyclic'] and s['n'] == 1 + 1 + 8


def test_arc_half_circle():
    r = shapes_rig("ND Arc", lambda dr, w: dr.group("a", stroke="black").arc(0, 0, 50, 0, 180))
    s, = r.layers()['a']
    assert not s['cyclic']
    assert s['x'] == pytest.approx((-0.5, 0.5), abs=1e-3)
    assert max(abs(s['z'][0]), abs(s['z'][1])) == pytest.approx(0.5, abs=0.015)      # apex falls between samples


def test_width_is_a_modifier_input():
    r = shapes_rig("ND Width", lambda dr, w: (setattr(dr.group("l", width=w), 'name', 'l') or dr.groups[-1].line(0, 0, 10, 0)))
    r.set(Width=2.0)
    assert r.layers()['l'][0]['radius'] == pytest.approx(0.01)
    r.set(Width=8.0)
    assert r.layers()['l'][0]['radius'] == pytest.approx(0.04)


def test_many_shapes_in_one_layer():
    def build(dr, w):
        g = dr.group("m", stroke="black")
        g.circle(0, 0, 10)
        g.rect(20, 0, 5, 5)
        g.line(0, 30, 10, 30)
    assert len(shapes_rig("ND Many", build).layers()['m']) == 3
