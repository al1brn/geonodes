"""Grease Pencil animated face (demos2/face.py) — requires Blender >= 5.x."""
import os
import sys

import bpy
import pytest

# `geonodes` is the repository itself: its parent directory must be importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from geonodes.core_new.root.tree import Tree  # noqa: E402
from geonodes.demos2 import face  # noqa: E402

# Join Geometry stacks its inputs in reverse order; layers have no name yet
LAYERS = ["mouth", "brows", "pupils", "eyes", "head"]
MOUTH, BROWS, PUPILS, EYES, HEAD = range(5)


@pytest.fixture(scope="module")
def rig():
    Tree.TREE_STACK.clear()
    face.demo(rebuild=True)
    ng = bpy.data.node_groups["Face"]
    ob = bpy.data.objects.new("face", bpy.data.grease_pencils.new("face"))
    bpy.context.scene.collection.objects.link(ob)
    md = ob.modifiers.new("Face", 'NODES')
    md.node_group = ng
    ids = {i.name: i.identifier for i in ng.interface.items_tree if i.in_out == 'INPUT'}
    yield ob, md, ids
    Tree.TREE_STACK.clear()


def evaluate(rig, **values):
    """Set the modifier inputs, evaluate, return a list of layer bounding boxes."""
    ob, md, ids = rig
    defaults = {"Blink": 0.0, "Look X": 0.0, "Look Y": 0.0, "Vowel": 0.0,
                "Mouth Open": 1.0, "Brow Raise": 0.0}
    defaults.update(values)
    for name, v in defaults.items():
        getattr(md.properties.inputs, ids[name]).value = v
    ob.update_tag()
    bpy.context.view_layer.update()
    data = ob.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    boxes = []
    for layer in data.layers:
        pts = [p.position for f in layer.frames for s in f.drawing.strokes for p in s.points]
        assert pts, f"layer {layer.name} has no points"
        xs, ys, zs = zip(*[(p[0], p[1], p[2]) for p in pts])
        boxes.append(((min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs))))
    return boxes


def height(box):
    return box[2][1] - box[2][0]


def width(box):
    return box[0][1] - box[0][0]


def test_has_five_layers(rig):
    assert len(evaluate(rig)) == len(LAYERS)


def test_blink_closes_eyes(rig):
    open_eyes = evaluate(rig, Blink=0.0)[EYES]
    closed = evaluate(rig, Blink=1.0)[EYES]
    assert height(closed) < 0.3 * height(open_eyes)


def test_look_moves_pupils(rig):
    left = evaluate(rig, **{"Look X": -1.0})[PUPILS]
    right = evaluate(rig, **{"Look X": 1.0})[PUPILS]
    assert right[0][0] > left[0][0]


@pytest.mark.parametrize("vowel", [1, 2, 3, 4, 5])
def test_vowel_poses_differ_from_rest(rig, vowel):
    rest = evaluate(rig, Vowel=0.0)[MOUTH]
    pose = evaluate(rig, Vowel=float(vowel))[MOUTH]
    assert (abs(width(pose) - width(rest)) > 1e-3) or (abs(height(pose) - height(rest)) > 1e-3)


def test_vowel_a_is_open_wider_than_i(rig):
    a = evaluate(rig, Vowel=1.0)[MOUTH]
    i = evaluate(rig, Vowel=3.0)[MOUTH]
    assert height(a) > height(i)
    assert width(i) > width(a)
