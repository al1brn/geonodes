"""Write a drawsvg Drawing into Blender Grease Pencil data.

Mapping
-------
- SVG space (x right, y down) -> Blender XZ plane: (x, y) -> (x*scale, 0, -y*scale)
- top level `Group(id='name')` -> Grease Pencil layer named 'name' (other elements: 'Drawing')
- one SVG shape -> one stroke; `stroke_width` -> point radius, closed shapes -> cyclic strokes
- `frame` -> Grease Pencil frame number, which allows pose-by-pose animation
"""

import bpy

from .flatten import flatten

MATERIAL_NAME = "Geonodes Drawing"


def drawing_material():
    """Grease Pencil material using both stroke and fill (created once)."""
    mat = bpy.data.materials.get(MATERIAL_NAME)
    if mat is None:
        mat = bpy.data.materials.new(MATERIAL_NAME)
        bpy.data.materials.create_gpencil_data(mat)
    mat.grease_pencil.show_stroke = True
    mat.grease_pencil.show_fill = True
    return mat


def _layer(gp, name):
    layer = gp.layers.get(name) if hasattr(gp.layers, 'get') else None
    if layer is None:
        for l in gp.layers:
            if l.name == name:
                layer = l
                break
    return layer or gp.layers.new(name)


def _frame(layer, number, clear=True):
    for f in layer.frames:
        if f.frame_number == number:
            if clear:
                layer.frames.remove(number)
                break
            return f
    return layer.frames.new(number)


def _is_curved(anchors):
    return any(a.hl != a.p or a.hr != a.p for a in anchors)


def to_grease_pencil(drawing, gp=None, *, frame=1, scale=0.01, resolution=16,
                     center=True, name="Drawing", width_scale=0.5, bezier=True):
    """Draw `drawing` into Grease Pencil data `gp` at `frame` and return `gp`.

    Parameters
    ----------
    drawing : drawsvg.Drawing (or list of elements)
    gp : bpy.types.GreasePencil, optional. Created with `name` if omitted.
    frame : frame number. An existing drawing at this frame in a touched layer is replaced.
    scale : Blender units per SVG unit.
    resolution : segments per curve. Used for polylines (bezier=False, or straight shapes).
    bezier : keep curved shapes as Bezier strokes (one point per anchor, with free handles).
        With False every shape is sampled to a polyline.
    center : move the center of the Drawing view box to the origin.
    width_scale : SVG stroke width -> point radius factor (radius = width * scale * width_scale).
    """
    if gp is None:
        gp = bpy.data.grease_pencils.new(name)
    strokes, warnings = flatten(drawing, resolution=resolution)
    for w in warnings:
        print(f"drawing warning: {w}")

    ox = oy = 0.0
    vb = getattr(drawing, 'view_box', None)
    if center and vb:
        ox, oy = vb[0] + vb[2] / 2, vb[1] + vb[3] / 2

    mat = drawing_material()
    if mat.name not in [m.name for m in gp.materials if m]:
        gp.materials.append(mat)
    mat_index = [m.name if m else None for m in gp.materials].index(mat.name)

    # Group strokes by layer, keeping the drawing order
    by_layer = {}
    for s in strokes:
        by_layer.setdefault(s.layer, []).append(s)

    for layer_name, items in by_layer.items():
        layer = _layer(gp, layer_name)
        drw = _frame(layer, frame).drawing
        curved = [bezier and s.bezier is not None and _is_curved(s.bezier) for s in items]
        drw.add_strokes([len(s.bezier) if c else len(s.points) for s, c in zip(items, curved)])
        bez_indices = [i for i, c in enumerate(curved) if c]
        if bez_indices:
            drw.set_types(type='BEZIER', indices=bez_indices)

        def xyz(q):
            return ((q[0] - ox) * scale, 0.0, -(q[1] - oy) * scale)

        for gs, s, c in zip(drw.strokes, items, curved):
            gs.cyclic = s.closed
            gs.material_index = mat_index
            if s.fill is not None:
                gs.fill_color = s.fill
            radius = max(s.width, 0.0) * scale * width_scale
            rgba = s.stroke if s.stroke is not None else (0.0, 0.0, 0.0, 0.0)
            coords = s.bezier if c else s.points
            for p, q in zip(gs.points, coords):
                if c:
                    p.position = xyz(q.p)
                    p.handle_left.position = xyz(q.hl)
                    p.handle_right.position = xyz(q.hr)
                else:
                    p.position = xyz(q)
                p.radius = radius if s.stroke is not None else 0.0
                p.vertex_color = rgba
                p.opacity = 1.0
        drw.tag_positions_changed()
    return gp
