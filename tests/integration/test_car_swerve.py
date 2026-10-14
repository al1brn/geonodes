"""Procedural right-turn crash: rigid parts, controls and continuous projection."""
import itertools
from math import pi

import bpy
import pytest
from mathutils import Matrix, Vector

from geonodes.demos import carcrash


@pytest.fixture
def swerve_scene():
    old_frame = bpy.context.scene.frame_current
    old_start = bpy.context.scene.frame_start
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_set(1)
    old_groups = set(bpy.data.node_groups.keys())
    carcrash.swerve()
    group = bpy.data.node_groups['Car Swerve']
    boxes = [((0, -1.2, 0.4), (0.8, -0.8, 1.2)),
             ((1.5, -0.2, 0.2), (2.3, 0.2, 0.8)),
             ((3.2, 0.8, 0), (4, 1.2, 0.6))]
    vertices = [Vector(p) for lo, hi in boxes for p in itertools.product(*zip(lo, hi))]
    mesh = bpy.data.meshes.new('Swerve test')
    mesh.from_pydata(vertices, [], [])
    for name, kind in [('Part', 'INT'), ('Min', 'FLOAT_VECTOR'), ('Max', 'FLOAT_VECTOR')]:
        attr = mesh.attributes.new(name, kind, 'POINT')
        for i, entry in enumerate(attr.data):
            if name == 'Part':
                entry.value = (7, 103, 42)[i // 8]
            else:
                entry.vector = boxes[i // 8][0 if name == 'Min' else 1]
    obj = bpy.data.objects.new('Swerve test', mesh)
    bpy.context.scene.collection.objects.link(obj)
    wrapper = bpy.data.node_groups.new('Swerve harness', 'GeometryNodeTree')
    wrapper.interface.new_socket(name='Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
    wrapper.interface.new_socket(name='Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')
    source = wrapper.nodes.new('NodeGroupInput')
    target = wrapper.nodes.new('NodeGroupOutput')
    node = wrapper.nodes.new('GeometryNodeGroup')
    node.node_tree = group
    wrapper.links.new(source.outputs[0], next(s for s in node.inputs if s.type == 'GEOMETRY'))
    wrapper.links.new(next(s for s in node.outputs if s.type == 'GEOMETRY'), target.inputs[0])
    path_data = bpy.data.curves.new('Swerve path', 'CURVE')
    path_data.dimensions = '3D'
    spline = path_data.splines.new('POLY')
    spline.points.add(3)
    for point, co in zip(spline.points, [(10, 0, 0, 1), (5, 0, 0, 1),
                                       (4, 1, 0, 1), (4, 5, 0, 1)]):
        point.co = co
    path = bpy.data.objects.new('Swerve path', path_data)
    bpy.context.scene.collection.objects.link(path)
    node.inputs['Path'].default_value = path
    obj.modifiers.new('Swerve', 'NODES').node_group = wrapper

    def evaluate(factor, time):
        bpy.context.scene.frame_set(1)
        node.inputs['Factor'].default_value = factor
        node.inputs['Time'].default_value = time
        obj.update_tag()
        bpy.context.view_layer.update()
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        result = evaluated.to_mesh()
        try:
            return [v.co.copy() for v in result.vertices]
        finally:
            evaluated.to_mesh_clear()

    try:
        yield vertices, evaluate
    finally:
        bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.meshes.remove(mesh)
        bpy.data.node_groups.remove(wrapper)
        bpy.data.objects.remove(path, do_unlink=True)
        bpy.data.curves.remove(path_data)
        bpy.context.scene.frame_start = old_start
        bpy.context.scene.frame_set(old_frame)
        for tree in list(bpy.data.node_groups):
            if tree.name not in old_groups:
                bpy.data.node_groups.remove(tree)



def path_pose(distance):
    from math import atan2, sqrt
    points = [Vector((10, 0, 0)), Vector((5, 0, 0)), Vector((4, 1, 0)), Vector((4, 5, 0))]
    directions = [(b - a).normalized() for a, b in zip(points, points[1:])]
    # Blender interpolates the averaged vertex tangents on a poly spline.
    tangents = [directions[0], (directions[0] + directions[1]).normalized(),
                (directions[1] + directions[2]).normalized(), directions[2]]
    distance = max(0, min(distance, 9 + sqrt(2)))
    for i, length in enumerate((5, sqrt(2), 4)):
        if distance <= length or i == 2:
            factor = distance / length
            position = points[i].lerp(points[i + 1], factor)
            tangent = tangents[i].lerp(tangents[i + 1], factor)
            yaw = atan2(-tangent.y, -tangent.x)
            return position, Matrix.Rotation(yaw, 3, 'Z')
        distance -= length


def test_car_centre_follows_path_and_front_follows_tangent(swerve_scene):
    vertices, evaluate = swerve_scene
    anchor = Vector((2, 0, 0))
    for distance in (0, 1, 4, 5.5, 7.5, 100):
        coords = evaluate(0, distance)
        position, rotation = path_pose(distance)
        for actual, original in zip(coords, vertices):
            assert (actual - (position + rotation @ (original - anchor))).length < 1e-5


def test_released_parts_are_independent_of_subsequent_path_motion(swerve_scene):
    vertices, _ = swerve_scene
    scene = bpy.context.scene
    original = bpy.data.objects['Swerve test']
    other = bpy.data.objects.new('Swerve moving car', original.data)
    scene.collection.objects.link(other)
    wrapper = bpy.data.node_groups['Swerve harness']
    other_wrapper = wrapper.copy()
    other.modifiers.new('Swerve', 'NODES').node_group = other_wrapper
    for tree, moving in ((wrapper, False), (other_wrapper, True)):
        node = next(n for n in tree.nodes if n.bl_idname == 'GeometryNodeGroup')
        node.inputs['Factor'].driver_add('default_value').driver.expression = 'min((frame - 1) / 20, 1)'
        node.inputs['Time'].driver_add('default_value').driver.expression = (
            'min((frame - 1) / 20, 1)' if not moving else
            'min((frame - 1) / 20, 1) if frame <= 21 else 9')
        if moving:
            node.inputs['Body Roll'].driver_add('default_value').driver.expression = (
                '0 if frame <= 21 else min((frame - 21) / 20, 1) * pi / 2')
            node.inputs['Z'].driver_add('default_value').driver.expression = (
                '0 if frame <= 21 else 0.7')

    def snapshot(obj):
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        mesh = evaluated.to_mesh()
        try:
            return ([v.co.copy() for v in mesh.vertices],
                    [a.value for a in mesh.attributes['Dynamic'].data])
        finally:
            evaluated.to_mesh_clear()

    try:
        for frame in range(1, 81):
            scene.frame_set(frame)
            left, left_dynamic = snapshot(original)
            right, right_dynamic = snapshot(other)
            for coords in (left, right):
                assert min(p.z for p in coords) >= -1e-4
                for start in (0, 8, 16):
                    for i, j in itertools.combinations(range(start, start + 8), 2):
                        assert abs((coords[i] - coords[j]).length - (vertices[i] - vertices[j]).length) < 1e-4
            assert not any(left_dynamic[16:])
            assert not any(right_dynamic[16:])
            if frame >= 22:
                assert all(left_dynamic[:16]) and all(right_dynamic[:16])
                # Path motion, body roll and Z cannot move already released debris.
                assert all((a - b).length < 1e-5 for a, b in zip(left[:16], right[:16]))
                assert (left[16] - right[16]).length > 1
        assert abs(min(p.z for p in left[:8])) < 1e-3
    finally:
        bpy.data.objects.remove(other, do_unlink=True)
        bpy.data.node_groups.remove(other_wrapper)


def test_path_object_transform_and_missing_path(swerve_scene):
    vertices, evaluate = swerve_scene
    baseline = evaluate(0, 1)
    bpy.data.objects['Swerve path'].location = (2, 3, 1)
    shifted = evaluate(0, 1)
    assert all((b - a - Vector((2, 3, 1))).length < 1e-5 for a, b in zip(baseline, shifted))
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes if n.bl_idname == 'GeometryNodeGroup')
    node.inputs['Path'].default_value = None
    assert all((a - b).length < 1e-5 for a, b in zip(evaluate(1, 10), vertices))


def test_wheels_and_bolts_roll_along_the_curve(swerve_scene):
    vertices, evaluate = swerve_scene
    mesh = bpy.data.objects['Swerve test'].data
    types = mesh.attributes.new('Part ID', 'INT', 'POINT')
    ids = mesh.attributes.new('Wheel ID', 'INT', 'POINT')
    for i in range(len(vertices)):
        types.data[i].value = 8 if i < 8 else 0
        ids.data[i].value = 1 if i < 16 else 0
    pivot = sum(vertices[:8], Vector()) / 8
    anchor = Vector((2, 0, 0))
    for distance in (0, 1, 5.5, 8):
        coords = evaluate(0, distance)
        position, turn = path_pose(distance)
        roll = Matrix.Rotation(-distance / 0.4, 3, 'Y')
        expected = [position + turn @ ((pivot + roll @ (v - pivot) if i < 16 else v) - anchor)
                    for i, v in enumerate(vertices)]
        for start in (0, 8, 16):
            correction = max(0, -min(v.z for v in expected[start:start + 8]))
            for i in range(start, start + 8):
                assert (coords[i] - expected[i] - Vector((0, 0, correction))).length < 1e-5


def test_identifiers_71_and_79_stay_rigidly_attached(swerve_scene):
    vertices, _ = swerve_scene
    obj = bpy.data.objects['Swerve test']
    identifier = obj.data.attributes.new('Identifier', 'INT', 'POINT')
    for i, entry in enumerate(identifier.data):
        entry.value = 71 if i < 8 else (79 if i < 16 else 0)
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes
                if n.bl_idname == 'GeometryNodeGroup')
    node.inputs['Factor'].driver_add('default_value').driver.expression = 'min((frame - 1) / 10, 1)'
    node.inputs['Time'].driver_add('default_value').driver.expression = '(frame - 1) / 4'
    anchor = Vector((2, 0, 0))
    for frame in range(1, 41):
        bpy.context.scene.frame_set(frame)
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        result = evaluated.to_mesh()
        try:
            assert not any(a.value for a in result.attributes['Dynamic'].data[:16])
            position, rotation = path_pose((frame - 1) / 4)
            for actual, original in zip(result.vertices, vertices):
                assert (actual.co - (position + rotation @ (original - anchor))).length < 1e-4
        finally:
            evaluated.to_mesh_clear()


@pytest.mark.parametrize('angle', [-pi / 2, -0.3, 0.3, pi / 2])
def test_body_roll_keeps_assembly_rigid_and_on_ground(swerve_scene, angle):
    vertices, evaluate = swerve_scene
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes
                if n.bl_idname == 'GeometryNodeGroup')
    node.inputs['Body Roll'].default_value = angle
    anchor = Vector((2, 0, 0))
    for distance in (0, 7.5):
        position, yaw = path_pose(distance)
        rotation = yaw @ Matrix.Rotation(angle, 3, 'X')
        expected = [position + rotation @ (p - anchor) for p in vertices]
        bottom = min(p.z for p in expected)
        expected = [p + Vector((0, 0, position.z - bottom)) for p in expected]
        actual = evaluate(0, distance)
        assert min(p.z for p in actual) == pytest.approx(position.z, abs=1e-5)
        assert all((a - b).length < 1e-4 for a, b in zip(actual, expected))


def test_ejected_parts_bounce_off_fixed_wall(swerve_scene):
    vertices, _ = swerve_scene
    obj = bpy.data.objects['Swerve test']
    bpy.data.objects['Swerve path'].location.x = -7
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes
                if n.bl_idname == 'GeometryNodeGroup')
    node.inputs['Factor'].driver_add('default_value').driver.expression = 'min((frame - 1) / 10, 1)'
    node.inputs['Time'].driver_add('default_value').driver.expression = 'min((frame - 1) / 10, 1)'
    bounced = False
    for frame in range(1, 81):
        bpy.context.scene.frame_set(frame)
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        result = evaluated.to_mesh()
        try:
            for start in (0, 8):
                if not result.attributes['Dynamic'].data[start].value:
                    continue
                coords = [v.co.copy() for v in result.vertices[start:start + 8]]
                assert min(p.x for p in coords) >= -1e-4
                assert min(p.z for p in coords) >= -1e-4
                for i, j in itertools.combinations(range(8), 2):
                    assert abs((coords[i] - coords[j]).length -
                               (vertices[start + i] - vertices[start + j]).length) < 1e-4
                velocity = result.attributes['Velocity'].data[start].vector
                if min(p.x for p in coords) < 0.03 and velocity.x > 0.01:
                    bounced = True
        finally:
            evaluated.to_mesh_clear()
    assert bounced, 'Expected an ejected part to rebound towards positive X'


def test_body_z_is_manual_offset_after_ground_contact(swerve_scene):
    _, evaluate = swerve_scene
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes
                if n.bl_idname == 'GeometryNodeGroup')
    for roll in (0, pi / 2):
        node.inputs['Body Roll'].default_value = roll
        node.inputs['Z'].default_value = 0
        baseline = evaluate(0, 7.5)
        for height in (-0.5, 0.7):
            node.inputs['Z'].default_value = height
            shifted = evaluate(0, 7.5)
            assert all((b - a - Vector((0, 0, height))).length < 1e-4
                       for a, b in zip(baseline, shifted))


def test_skip_keeps_body_controls_and_wheels_live(swerve_scene):
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes
                if n.bl_idname == 'GeometryNodeGroup')
    node.inputs['Skip'].default_value = True
    test_wheels_and_bolts_roll_along_the_curve(swerve_scene)
    node.inputs['Body Roll'].default_value = pi / 2
    node.inputs['Z'].default_value = 0.7
    _, evaluate = swerve_scene
    first = evaluate(0, 0)
    second = evaluate(0, 7.5)
    assert min(p.z for p in second) == pytest.approx(0.7, abs=1e-4)
    assert (first[0] - second[0]).length > 1


def test_skip_freezes_debris_but_not_remaining_body(swerve_scene):
    obj = bpy.data.objects['Swerve test']
    node = next(n for n in bpy.data.node_groups['Swerve harness'].nodes
                if n.bl_idname == 'GeometryNodeGroup')
    node.inputs['Factor'].driver_add('default_value').driver.expression = 'min((frame - 1) / 10, 1)'
    node.inputs['Skip'].driver_add('default_value').driver.expression = 'frame > 20'
    node.inputs['Time'].driver_add('default_value').driver.expression = 'max(0, (frame - 20) / 5)'
    node.inputs['Z'].driver_add('default_value').driver.expression = 'max(0, (frame - 20) / 10)'
    frozen = None
    for frame in range(1, 31):
        bpy.context.scene.frame_set(frame)
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        mesh = evaluated.to_mesh()
        try:
            coords = [v.co.copy() for v in mesh.vertices]
            if frame == 20:
                assert all(a.value for a in mesh.attributes['Dynamic'].data[:16])
                frozen = coords
            elif frame > 20:
                assert all((a - b).length < 1e-5 for a, b in zip(coords[:16], frozen[:16]))
                assert (coords[16] - frozen[16]).length > 0.05
        finally:
            evaluated.to_mesh_clear()
