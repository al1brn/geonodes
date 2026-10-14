"""Evaluate the car crash simulation in Blender, including its rigid geometry."""
import itertools

import bpy
import pytest
from mathutils import Vector

from geonodes.demos import carcrash


@pytest.fixture
def crash_scene():
    scene = bpy.context.scene
    original_frame = scene.frame_current
    original_timing = (scene.frame_start, scene.frame_end, scene.render.fps, scene.render.fps_base)
    scene.frame_start, scene.frame_end = 1, 160
    scene.render.fps, scene.render.fps_base = 24, 1.0
    scene.frame_set(1)
    original_groups = set(bpy.data.node_groups.keys())
    carcrash.demo()
    group = bpy.data.node_groups['Car Crash']
    boxes = [((0, -1, 0), (0.8, -0.4, 0.7)),
             ((1, 0.4, 0), (2, 1, 1)),
             ((3, -0.3, 0.3), (4, 0.3, 1.2))]
    vertices = [Vector(p) for lo, hi in boxes
                for p in itertools.product(*zip(lo, hi))]
    # Front part has no bounding-box corners: a rotated box would make it float.
    lo, hi = (Vector(v) for v in boxes[0])
    centre, half = (lo + hi) / 2, (hi - lo) / 2
    vertices[:8] = [centre + Vector(offset) for offset in
                    [(-half.x, 0, 0), (half.x, 0, 0), (0, -half.y, 0),
                     (0, half.y, 0), (0, 0, -half.z), (0, 0, half.z),
                     (-half.x / 2, 0, 0), (half.x / 2, 0, 0)]]
    mesh = bpy.data.meshes.new('Car crash test')
    mesh.from_pydata(vertices, [], [])
    for name, kind in [('Part', 'INT'), ('Min', 'FLOAT_VECTOR'), ('Max', 'FLOAT_VECTOR')]:
        attribute = mesh.attributes.new(name, kind, 'POINT')
        for i, entry in enumerate(attribute.data):
            if name == 'Part':
                # IDs need not be contiguous or ordered vertex indices.
                entry.value = (7, 103, 42)[i // 8]
            else:
                entry.vector = boxes[i // 8][0 if name == 'Min' else 1]
    obj = bpy.data.objects.new('Car crash test', mesh)
    scene.collection.objects.link(obj)
    wrapper = bpy.data.node_groups.new('Car crash test harness', 'GeometryNodeTree')
    wrapper.interface.new_socket(name='Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
    wrapper.interface.new_socket(name='Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')
    source = wrapper.nodes.new('NodeGroupInput')
    target = wrapper.nodes.new('NodeGroupOutput')
    crash = wrapper.nodes.new('GeometryNodeGroup')
    crash.node_tree = group
    wrapper.links.new(source.outputs['Geometry'], next(s for s in crash.inputs if s.type == 'GEOMETRY'))
    wrapper.links.new(next(s for s in crash.outputs if s.type == 'GEOMETRY'), target.inputs['Geometry'])
    wall = wrapper.nodes.new('ShaderNodeValue').outputs[0]
    wrapper.links.new(wall, crash.inputs['X'])
    # Driver avoids modifier input API differences between Blender releases.
    wall.driver_add('default_value').driver.expression = '-min(max((frame - 1) / 40, 0), 0.5)'
    modifier = obj.modifiers.new('Car crash test', 'NODES')
    modifier.node_group = wrapper

    def evaluate(frame):
        scene.frame_set(frame)
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        result = evaluated.to_mesh()
        try:
            return {
                'position': [v.co.copy() for v in result.vertices],
                'dynamic': [a.value for a in result.attributes['Dynamic'].data],
                'velocity': [a.vector.copy() for a in result.attributes['Velocity'].data],
                'omega': [a.vector.copy() for a in result.attributes['Angular Velocity'].data],
                'x': wall.default_value,
            }
        finally:
            evaluated.to_mesh_clear()

    try:
        yield crash, wall, vertices, evaluate
    finally:
        bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.meshes.remove(mesh)
        bpy.data.node_groups.remove(wrapper)
        for tree in list(bpy.data.node_groups):
            if tree.name not in original_groups:
                bpy.data.node_groups.remove(tree)
        scene.frame_start, scene.frame_end, scene.render.fps, scene.render.fps_base = original_timing
        scene.frame_set(original_frame)


def assert_rigid_and_clear(sample, vertices):
    coords = sample['position']
    assert len(coords) == len(vertices)
    assert min(p.x for p in coords) >= -1e-4
    assert min(p.z for p in coords) >= -1e-4
    for start in range(0, len(vertices), 8):
        for i, j in itertools.combinations(range(start, start + 8), 2):
            assert abs((coords[i] - coords[j]).length
                       - (vertices[i] - vertices[j]).length) < 1e-4
            assert sample['dynamic'][i] == sample['dynamic'][j]
            assert (sample['velocity'][i] - sample['velocity'][j]).length < 1e-5
            assert (sample['omega'][i] - sample['omega'][j]).length < 1e-5


def test_anticipation_stays_attached_and_impacted_part_reaches_ground(crash_scene):
    crash, wall, vertices, evaluate = crash_scene
    # Keep the launch airborne long enough to observe gravity after Wall stops.
    crash.inputs['Lift'].default_value = 2.0
    samples = []
    for frame in range(1, 161):
        sample = evaluate(frame)
        samples.append(sample)
        assert_rigid_and_clear(sample, vertices)
        assert not any(sample['dynamic'][8:])
        assert all(v.length < 1e-6 for v in sample['velocity'][8:])
        assert all(v.length < 1e-6 for v in sample['omega'][8:])
        if frame == 1:
            assert not any(sample['dynamic'])
            assert all((a - b).length < 1e-5 for a, b in zip(sample['position'], vertices))
        if frame > 30:
            assert all(sample['dynamic'][:8])
    assert any(s['velocity'][0].z > 0.1 for s in samples)
    assert any(s['velocity'][0].z < -0.1 for s in samples[21:])
    assert any(s['omega'][0].length > 0.1 for s in samples)
    assert samples[-1]['velocity'][0].length < 0.05
    assert samples[-1]['omega'][0].length < 0.02
    assert abs(min(p.z for p in samples[-1]['position'][:8])) < 1e-4
    # Rear pieces anticipate (including rotation), but never fall while attached.
    assert min(p.z for p in samples[-1]['position'][16:]) > 0.1
    rear_edge = vertices[17] - vertices[16]
    moved_edge = samples[-1]['position'][17] - samples[-1]['position'][16]
    assert (moved_edge - rear_edge).length > 1e-4
    assert all((a - b).length < 1e-5 for a, b in
               zip(samples[30]['position'][8:], samples[-1]['position'][8:]))


def test_impulse_is_once_and_fast_wall_catches_parts(crash_scene):
    crash, wall, vertices, evaluate = crash_scene
    for name, value in [('Gravity', 0), ('Air Drag', 0), ('Roll', 0),
                        ('Pitch', 0), ('Yaw', 0), ('Lift', 4), ('Randomness', 0)]:
        crash.inputs[name].default_value = value
    wall.driver_add('default_value').driver.expression = (
        '-min(max((frame - 1) / 40, 0), 0.5) if frame < 41 else -6.0')
    samples = []
    for frame in range(1, 51):
        sample = evaluate(frame)
        samples.append(sample)
        assert_rigid_and_clear(sample, vertices)
        if 22 <= frame <= 40:
            assert (sample['velocity'][0] - samples[20]['velocity'][0]).length < 1e-5
        if frame >= 41:
            assert all(sample['dynamic'])
    assert samples[20]['velocity'][0].z > 1
    assert samples[40]['velocity'][0].x > samples[39]['velocity'][0].x


def test_positive_x_only_translates_and_then_crashes(crash_scene):
    crash, x, vertices, evaluate = crash_scene
    x.driver_add('default_value').driver.expression = '0.25 - (frame - 1) / 40'
    for frame in range(1, 25):
        sample = evaluate(frame)
        assert_rigid_and_clear(sample, vertices)
        if sample['x'] >= 0:
            assert not any(sample['dynamic'])
            for actual, original in zip(sample['position'], vertices):
                assert (actual - original - Vector((sample['x'], 0, 0))).length < 1e-5
        else:
            assert all(sample['dynamic'][:8])
            assert not any(sample['dynamic'][8:])


def test_utility_groups_preserved_and_rebuilt_with_modifier():
    previous = set(bpy.data.node_groups.keys())
    try:
        carcrash.demo()
        modifier = bpy.data.node_groups['Car Crash']
        utilities = {node.node_tree.name: node.node_tree for node in modifier.nodes
                     if node.bl_idname == 'GeometryNodeGroup'}
        assert len(utilities) == 10
        assert all(not group.is_modifier for group in utilities.values())
        snapshots = {name: tuple(node.as_pointer() for node in group.nodes)
                     for name, group in utilities.items()}
        interface = [(item.name, item.identifier) for item in modifier.interface.items_tree]
        carcrash.demo()
        assert interface == [(item.name, item.identifier) for item in modifier.interface.items_tree]
        assert all(tuple(node.as_pointer() for node in group.nodes) == snapshots[name]
                   for name, group in utilities.items())
        for group in utilities.values():
            group.nodes.new('NodeFrame').name = '_customization'
        carcrash.demo(rebuild=True)
        assert all(group.nodes.get('_customization') is None for group in utilities.values())
        assert all(node.node_tree is not None for node in modifier.nodes
                   if node.bl_idname == 'GeometryNodeGroup')
    finally:
        for group in list(bpy.data.node_groups):
            if group.name not in previous:
                bpy.data.node_groups.remove(group)


@pytest.mark.parametrize('part_type', [8, 9])
def test_wheels_settle_on_their_side_at_actual_ground_contact(crash_scene, part_type):
    crash, x, vertices, evaluate = crash_scene
    mesh = bpy.data.objects['Car crash test'].data
    marking = mesh.attributes.new('Part ID', 'INT', 'POINT')
    for i, entry in enumerate(marking.data):
        entry.value = part_type if i < 8 else 0
    # Force an initially upright launch so the resting behaviour must tip it.
    for name in ('Roll', 'Pitch', 'Yaw'):
        crash.inputs[name].default_value = 0
    crash.inputs['Randomness'].default_value = 0
    crash.inputs['Bounce'].default_value = 0
    previous = None
    tipped = False
    for frame in range(1, 121):
        sample = evaluate(frame)
        assert_rigid_and_clear(sample, vertices)
        axle = (sample['position'][3] - sample['position'][2]).normalized()
        lowest = min(p.z for p in sample['position'][:8])
        if lowest > 0.001:
            # The free-flight wheel does not prematurely rotate to its rest pose.
            assert abs(axle.z) < 1e-4
        if previous is not None:
            assert axle.dot(previous) > 0.97, 'rest rotation jumped'
        tipped |= abs(axle.z) > 0.1
        previous = axle
    assert tipped
    assert abs(axle.z) > 0.995
    assert abs(lowest) < 1e-4


@pytest.mark.parametrize('part_type', [8, 9])
@pytest.mark.parametrize('skip', [False, True])
def test_wheel_roll_uses_x_and_radius_around_its_own_centre(crash_scene, part_type, skip):
    from mathutils import Matrix
    crash, x, vertices, evaluate = crash_scene
    mesh = bpy.data.objects['Car crash test'].data
    marking = mesh.attributes.new('Part ID', 'INT', 'POINT')
    for i, entry in enumerate(marking.data):
        entry.value = part_type if i < 8 else 0
    wheel_ids = mesh.attributes.new('Wheel ID', 'INT', 'POINT')
    for i, entry in enumerate(wheel_ids.data):
        entry.value = 1 if i < 8 else 0
    crash.inputs['Skip'].default_value = skip
    radius = 0.4
    crash.inputs['Wheel Radius'].default_value = radius
    x.driver_add('default_value').driver.expression = '1.0 - (frame - 1) / 10'
    centre = sum(vertices[:8], Vector()) / 8
    for frame in range(1, 5):
        sample = evaluate(frame)
        rotation = Matrix.Rotation(sample['x'] / radius, 3, 'Y')
        shift = Vector((sample['x'], 0, 0))
        assert not any(sample['dynamic'])
        for i, position in enumerate(sample['position']):
            expected = centre + rotation @ (vertices[i] - centre) + shift if i < 8 else vertices[i] + shift
            assert (position - expected).length < 1e-5


@pytest.mark.parametrize('wheel_number', [1, 2, 3, 4])
def test_wheel_bolts_orbit_the_rim_centre_and_zero_id_does_not_roll(crash_scene, wheel_number):
    from mathutils import Matrix
    crash, x, vertices, evaluate = crash_scene
    mesh = bpy.data.objects['Car crash test'].data
    marking = mesh.attributes.new('Part ID', 'INT', 'POINT')
    wheel_ids = mesh.attributes.new('Wheel ID', 'INT', 'POINT')
    for i in range(len(vertices)):
        marking.data[i].value = 9 if i < 8 or i >= 16 else 0
        wheel_ids.data[i].value = wheel_number if i < 16 else 0
    crash.inputs['Skip'].default_value = True
    crash.inputs['Wheel Radius'].default_value = 0.4
    x.driver_add('default_value').driver.expression = '0.8 - (frame - 1) / 10'
    pivot = sum(vertices[:8], Vector()) / 8
    for frame in range(1, 4):
        sample = evaluate(frame)
        rotation = Matrix.Rotation(sample['x'] / 0.4, 3, 'Y')
        shift = Vector((sample['x'], 0, 0))
        for i, actual in enumerate(sample['position']):
            expected = pivot + rotation @ (vertices[i] - pivot) + shift if i < 16 else vertices[i] + shift
            assert (actual - expected).length < 1e-5
