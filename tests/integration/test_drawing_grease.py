"""drawing.to_grease_pencil — requires Blender >= 5.x."""
import os
import sys

import bpy
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from geonodes.drawing import draw, to_grease_pencil  # noqa: E402


def sample():
    d = draw.Drawing(200, 200, origin='center')
    g = draw.Group(id='mouth')
    g.append(draw.Path(stroke='red', fill='#ffcc00', stroke_width=4).M(-40, 0).Q(0, 40, 40, 0).Z())
    d.append(g)
    d.append(draw.Circle(0, 0, 80, fill='none', stroke='black', stroke_width=2))
    return d


@pytest.fixture
def gp():
    data = bpy.data.grease_pencils.new("t")
    yield data
    bpy.data.grease_pencils.remove(data)


def test_layers_named_by_group(gp):
    to_grease_pencil(sample(), gp)
    assert [l.name for l in gp.layers] == ['mouth', 'Drawing']


def test_stroke_attributes(gp):
    to_grease_pencil(sample(), gp, scale=0.01)
    mouth = gp.layers['mouth'].frames[0].drawing.strokes[0]
    assert mouth.cyclic
    assert tuple(mouth.fill_color) == pytest.approx((1.0, 0.8, 0.0, 1.0), abs=1e-3)
    p = mouth.points[0]
    assert tuple(p.position) == pytest.approx((-0.4, 0.0, 0.0), abs=1e-5)
    assert p.radius == pytest.approx(0.02)
    assert tuple(p.vertex_color) == pytest.approx((1.0, 0.0, 0.0, 1.0), abs=1e-3)


def test_y_axis_is_flipped_to_z_up(gp):
    d = draw.Drawing(100, 100, origin='center')
    d.append(draw.Line(0, 0, 0, 10, stroke='black'))      # SVG: going down
    to_grease_pencil(d, gp, scale=1.0)
    pts = gp.layers[0].frames[0].drawing.strokes[0].points
    assert pts[1].position[2] < pts[0].position[2]


def test_frames_and_replace(gp):
    to_grease_pencil(sample(), gp, frame=1)
    to_grease_pencil(sample(), gp, frame=10)
    to_grease_pencil(sample(), gp, frame=10)              # replaces, does not duplicate
    assert [f.frame_number for f in gp.layers['mouth'].frames] == [1, 10]
    assert len(gp.layers['mouth'].frames[1].drawing.strokes) == 1


def test_face_drawing_poses_and_svg(tmp_path):
    from geonodes.demos2 import face_drawing as fd
    gp = fd.demo(name="FaceTest")
    try:
        assert [l.name for l in gp.layers] == ['head', 'eyes', 'pupils', 'brows', 'mouth']
        frames = [f.frame_number for f in gp.layers['mouth'].frames]
        assert frames == [1, 11, 21, 31, 41, 51, 61, 63]
    finally:
        bpy.data.grease_pencils.remove(gp)
    fd.save_svgs(str(tmp_path))
    assert len(list(tmp_path.glob("*.svg"))) == 6


# ----------------------------------------------------------------------------------------------------
# Bezier strokes

def evaluated_curve_points(gp):
    """Evaluate the stroke curves of `gp` (Grease Pencil to Curves -> Curve to Mesh): vertex list."""
    ob = bpy.data.objects.new("bz_gp", gp)
    bpy.context.scene.collection.objects.link(ob)
    ng = bpy.data.node_groups.new("BZ", 'GeometryNodeTree')
    ng.is_modifier = True
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    gout = ng.nodes.new("NodeGroupOutput")
    info = ng.nodes.new("GeometryNodeObjectInfo")
    info.inputs[0].default_value = ob
    to_curves = ng.nodes.new("GeometryNodeGreasePencilToCurves")
    to_curves.inputs['Layers as Instances'].default_value = False
    to_mesh = ng.nodes.new("GeometryNodeCurveToMesh")
    ng.links.new(info.outputs['Geometry'], to_curves.inputs[0])
    ng.links.new(to_curves.outputs[0], to_mesh.inputs[0])
    ng.links.new(to_mesh.outputs[0], gout.inputs[0])
    mesh_ob = bpy.data.objects.new("bz_mesh", bpy.data.meshes.new("bz"))
    bpy.context.scene.collection.objects.link(mesh_ob)
    mesh_ob.modifiers.new("N", 'NODES').node_group = ng
    bpy.context.view_layer.update()
    ev = mesh_ob.evaluated_get(bpy.context.evaluated_depsgraph_get())
    pts = [tuple(v.co) for v in ev.data.vertices]
    bpy.data.objects.remove(mesh_ob)
    bpy.data.objects.remove(ob)
    bpy.data.node_groups.remove(ng)
    return pts


def test_circle_is_one_bezier_stroke(gp):
    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Circle(0, 0, 80, fill='none', stroke='black'))
    to_grease_pencil(d, gp, scale=0.01)
    s = gp.layers[0].frames[0].drawing.strokes[0]
    assert s.curve_type == 2 and len(s.points) == 4 and s.cyclic
    right = s.points[0]
    assert tuple(right.position) == pytest.approx((0.8, 0, 0), abs=1e-5)
    k = 0.8 * 0.5522847498
    assert tuple(right.handle_right.position) == pytest.approx((0.8, 0, -k), abs=1e-4)   # SVG y down -> z up
    assert tuple(right.handle_left.position) == pytest.approx((0.8, 0, k), abs=1e-4)


def test_bezier_false_gives_polyline(gp):
    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Circle(0, 0, 80, fill='none', stroke='black'))
    to_grease_pencil(d, gp, bezier=False, resolution=8)
    s = gp.layers[0].frames[0].drawing.strokes[0]
    assert s.curve_type == 1 and len(s.points) == 32


def test_straight_shapes_stay_polylines(gp):
    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Rectangle(-10, -10, 20, 20, fill='none', stroke='black'))
    to_grease_pencil(d, gp)
    s = gp.layers[0].frames[0].drawing.strokes[0]
    assert s.curve_type == 1 and len(s.points) == 4


def test_mixed_strokes_in_one_layer(gp):
    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Rectangle(-10, -10, 20, 20, fill='none', stroke='black'))
    d.append(draw.Circle(0, 0, 50, fill='none', stroke='black'))
    d.append(draw.Line(0, 0, 10, 10, stroke='black'))
    to_grease_pencil(d, gp)
    types = [s.curve_type for s in gp.layers[0].frames[0].drawing.strokes]
    sizes = [len(s.points) for s in gp.layers[0].frames[0].drawing.strokes]
    assert types == [1, 2, 1] and sizes == [4, 4, 2]


def test_blender_evaluates_bezier_circle_accurately(gp):
    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Circle(0, 0, 80, fill='none', stroke='black'))
    to_grease_pencil(d, gp, scale=0.01)
    pts = evaluated_curve_points(gp)
    assert len(pts) > 16
    import math
    for x, y, z in pts:
        assert math.hypot(x, z) == pytest.approx(0.8, abs=0.002)


def test_blender_evaluates_bezier_arc_path(gp):
    d = draw.Drawing(200, 200, origin='center')
    d.append(draw.Path(stroke='black', fill='none').M(-50, 0).A(50, 50, 0, 0, 1, 50, 0))
    to_grease_pencil(d, gp, scale=0.01)
    pts = evaluated_curve_points(gp)
    import math
    assert max(abs(z) for x, y, z in pts) == pytest.approx(0.5, abs=0.01)      # a half circle
    assert min(x for x, y, z in pts) == pytest.approx(-0.5, abs=0.001) and max(x for x, y, z in pts) == pytest.approx(0.5, abs=0.001)
    for x, y, z in pts:
        assert math.hypot(x, z) == pytest.approx(0.5, abs=0.002)
