"""A simulated cartoon car crash made of rigid mesh parts.

Build with::

    from geonodes.demos import carcrash
    carcrash.demo(rebuild=True)

Add ``Car Crash`` as a Geometry Nodes modifier. Start playback at the scene's
first frame with ``X`` positive, then decrease it towards zero and below. X is
the car's translation along X; the wall stays fixed at X=0. Positive X simply
translates the car and rolls its wheels, while negative X drives the crash. Reset/delete the
simulation bake and restart playback after changing the input mesh or settings.
The front is X=0, the ground Z=0 and the centre line Y=0, in object coordinates.
Realize instances upstream. Point attributes ``Part`` (integer), ``Min`` and
``Max`` (vectors) describe each original part. They must be constant per part.

Anticipation moves and rotates attached parts without gravity. ``Dynamic``
becomes true only on wall contact and stays true during the crash. Returning to positive X resets the part state. ``Velocity``
(object units/s in the car's reference frame) and ``Angular Velocity`` (radians/s, object axes) are
also exposed on the output points. State is replicated at each vertex of a
part to preserve the original mesh topology and attributes without rebuilding
instances. Every vertex of a part gets exactly the same rigid transform.

Advance, Spread and Lift control the anticipation displacement and, multiplied
by Impact Speed (1/s), the launch velocity. Roll, Pitch and Yaw similarly set
anticipation angles and launch spin. Internally the wall moves by -X in the
car's reference frame; the final X translation keeps the visible wall at zero.
Relative impact speed contributes to the launch. Gravity, Air Drag,
Bounce, Friction and Angular Damping control the subsequent motion.

Rotated bounding boxes are kept ahead of the wall. Ground contact uses the
lowest transformed vertex of each Part, computed with Attribute Statistic.
Collisions between parts and physically accurate contact torques are omitted.
Distances are object units, gravity is units/s^2, damping rates are 1/s.

Architecture
------------
``utilities()`` builds ten reusable node groups: Crash Wheel Setup, Crash Initialize, Crash Part
Behaviour, Crash Influence, Crash Part Release, Crash Part Dynamics, Crash Wall
Contact, Crash Ground Contact, Crash Wheel Rest and Crash Apply Pose. Car Crash owns the simulation,
substeps, reset and bake. The groups pass state as mesh attributes; original
vertex positions are retained until Apply Pose. Behaviour is the extension point for launch animation. Wheel Rest handles
Pneu (8) and Jante (9), selected through the integer attribute named by Type
Attribute (default Part ID). Once grounded and vertical bounce speed is below
Rest Speed, wheels tip around their contact towards a horizontal resting pose.
Wheel ID (1 to 4) groups rims, tyres and bolts for rolling; 0 does not roll.
Each wheel uses its rim's current input bounding-box centre as a shared pivot
(falling back to the tyre, then all wheel members if no rim is marked).
Wheel Radius sets rolling angle Y = X / radius while the wheel is attached.
The rolling pose is retained at release; free parts then follow the simulation.
Wheel Axle is the axle direction in the original mesh (default Y); Wheel Rest
Rate controls settling in 1/s, with zero disabling it. Unmarked parts are unchanged.
``demo(rebuild=True)`` rebuilds the modifier and all its dependencies.
"""

from math import radians

from geonodes import (
    Boolean, Curve, Float, GeoNodes, Group, Instances, Integer, Layout, Mesh, Object, Panel, Rotation, String, Vector,
    nd, repeat, simulation,
)


_CENTRE = "_CarCrash Centre"
_ROTATION = "_CarCrash Rotation"
_IMPACTED = "_CarCrash Impacted"
_WHEEL_CENTRE = "_CarCrash Wheel Centre"


def _bounds(rotation, half):
    """Half extents of the rotated original bounding box: abs(R) @ half."""
    return ((rotation @ Vector((1, 0, 0))).abs() * half.x
            + (rotation @ Vector((0, 1, 0))).abs() * half.y
            + (rotation @ Vector((0, 0, 1))).abs() * half.z)


def _rest_centre():
    return (Vector.Named("Min") + Vector.Named("Max")) * 0.5


def _rest_half():
    return (Vector.Named("Max") - Vector.Named("Min")) * 0.5


def _store_state(mesh, values, selection=None):
    """Evaluate every next-state field before overwriting any old-state attribute."""
    if selection is not None:
        selection = mesh.points.capture_attribute(selection)
    captured = [mesh.points.capture_attribute(value) for value in values.values()]
    for name, value in zip(values, captured):
        if selection is None:
            mesh.points.set(name, value)
        else:
            mesh.points[selection].set(name, value)


def utilities(rebuild=False):
    """Build the stateless stages used inside and around the simulation.

    Mesh vertices remain in their rest positions until Crash Apply Pose.
    The mesh carries the current rigid pose (_CENTRE, _ROTATION), Dynamic,
    Velocity, Angular Velocity and the one-shot _IMPACTED flag. Each stage
    reads that state and commits its own changes atomically. This geometry
    link is the state interface; no simulation zone is hidden inside a group.
    """
    _wheel_setup_group(rebuild)
    _initialize_group(rebuild)
    _behaviour_group(rebuild)
    _influence_group(rebuild)
    _release_group(rebuild)
    _dynamics_group(rebuild)
    _wall_contact_group(rebuild)
    _ground_contact_group(rebuild)
    _wheel_rest_group(rebuild)
    _apply_pose_group(rebuild)


def _wheel_setup_group(rebuild):
    """One common rest pivot per Wheel ID, computed outside the simulation."""
    with GeoNodes("Crash Wheel Setup", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        part_type = Integer(0, "Part Type")
        wheel_id = Integer.Named("Wheel ID")
        mesh.points.set(_WHEEL_CENTRE, _rest_centre())
        for number in range(1, 5):
            members = wheel_id == number
            rims = members & (part_type == 9)
            tyres = members & (part_type == 8)
            has_rim = mesh.points[rims].attribute_statistic(Float(1)).sum_ > 0
            has_tyre = mesh.points[tyres].attribute_statistic(Float(1)).sum_ > 0
            pivot_selection = Boolean.Switch(has_rim,
                                             Boolean.Switch(has_tyre, members, tyres), rims)
            bounds = mesh.points[pivot_selection].attribute_statistic(nd.position)
            pivot = (bounds.min_ + bounds.max_) * 0.5
            mesh.points[members].set(_WHEEL_CENTRE, pivot)
        mesh.out("Mesh")


def _initialize_group(rebuild):
    with GeoNodes("Crash Initialize", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        centre = _rest_centre()
        mesh.points.set("Dynamic", Boolean(False))
        mesh.points.set(_IMPACTED, Boolean(False))
        mesh.points.set("Velocity", Vector(0))
        mesh.points.set("Angular Velocity", Vector(0))
        mesh.points.set(_CENTRE, centre)
        mesh.points.set(_ROTATION, Rotation((0, 0, 0)))
        # A compact ID table also supports sparse or negative Part IDs.
        rank = mesh.points.accumulate_field(Integer(1), group_id=Integer.Named("Part")).trailing_
        parts = Mesh(mesh).points[rank != 0].delete()
        mesh.out("Mesh")
        parts.out("Parts")


def _behaviour_group(rebuild):
    """Current generic behaviour; the extension point for the marked part types."""
    with GeoNodes("Crash Part Behaviour", is_group=True, rebuild=rebuild):
        half_width = Float(0.8, "Half Width")
        advance = Float(0.15, "Advance")
        spread = Float(1.2, "Spread")
        lift = Float(0.7, "Lift")
        roll = Float.Angle(radians(35), "Roll")
        pitch = Float.Angle(radians(70), "Pitch")
        yaw = Float.Angle(radians(25), "Yaw")
        randomness = Float.Factor(0.65, "Randomness")
        seed = Integer(0, "Seed")
        part = Integer.Named("Part")
        centre = _rest_centre()
        amount = randomness.clamp(0, 1)

        def noise(offset):
            return Float.Random(-1, 1, id=part, seed=seed + offset)

        def variation(offset):
            return 1 + 0.6 * amount * noise(offset)

        side = (centre.y / half_width.max(0.001)).clamp(-1, 1)
        Vector((advance * variation(2), spread * side * variation(3),
                lift * variation(4))).out("Displacement")
        Vector((roll * (side + amount * noise(5)),
                pitch * (0.35 + amount * noise(6)),
                yaw * (0.3 * side + amount * noise(7)))).out("Spin")
        variation(1).out("Reach Scale")


def _influence_group(rebuild):
    with GeoNodes("Crash Influence", is_group=True, rebuild=rebuild):
        wall = Float(0, "Wall")
        start = Float(0.25, "Start Distance")
        anticipation = Float(0.8, "Anticipation")
        reach_scale = Float(1, "Reach Scale")
        reach = anticipation.max(0.001) * reach_scale
        distance = (Vector.Named("Min").x - wall).max(0)
        reaction = (1 - (-wall / start.max(0.001)).exp()) * (-distance / reach).exp()
        reaction.out("Reaction")


def _release_group(rebuild):
    """Attached pose and the single launch impulse; no integration here."""
    with GeoNodes("Crash Part Release", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        reaction = Float(0, "Reaction")
        displacement = Vector(0, "Displacement")
        spin = Vector(0, "Spin")
        wall = Float(0, "Wall")
        wall_speed = Float(0, "Wall Speed")
        frame_time = Float(0, "Frame Time")
        impact_speed = Float(3, "Impact Speed")
        wheel_rotation = Rotation((0, 0, 0), "Wheel Rotation")
        wheel_centre = Vector(0, "Wheel Centre")
        centre, half = _rest_centre(), _rest_half()
        dynamic = Boolean.Named("Dynamic")
        impacted = Boolean.Named(_IMPACTED)
        rolled_centre = wheel_centre + wheel_rotation @ (centre - wheel_centre)
        position = Vector.Switch(dynamic, rolled_centre + displacement * reaction, Vector.Named(_CENTRE))
        attached_rotation = Rotation(spin * reaction).rotate_local(wheel_rotation)
        rotation = Rotation.Switch(dynamic, attached_rotation, Rotation.Named(_ROTATION))
        bounds = _bounds(rotation, half)
        hit = ((position.x - bounds.x <= wall) & (wall > 0) & (frame_time > 0))
        active = dynamic | hit
        launched = hit & impacted.bnot()
        velocity = Vector.Switch(launched, Vector.Named("Velocity"),
                                 displacement * impact_speed + Vector((wall_speed, 0, 0)))
        omega = Vector.Switch(launched, Vector.Named("Angular Velocity"), spin * impact_speed)
        _store_state(mesh, {
            "Dynamic": active,
            "Velocity": Vector.Switch(active, Vector(0), velocity),
            "Angular Velocity": Vector.Switch(active, Vector(0), omega),
            _CENTRE: position, _ROTATION: rotation, _IMPACTED: impacted | hit,
        })
        mesh.out("Mesh")


def _dynamics_group(rebuild):
    with GeoNodes("Crash Part Dynamics", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        dt = Float(0, "Delta Time")
        gravity = Float(9.81, "Gravity")
        drag = Float(0.15, "Air Drag")
        velocity = Vector.Named("Velocity")
        velocity = (velocity + Vector((0, 0, -gravity.max(0))) * dt) * (-drag.max(0) * dt).exp()
        velocity = Vector.Switch(Boolean.Named("Dynamic"), Vector(0), velocity)
        omega = Vector.Named("Angular Velocity") * (-drag.max(0) * dt).exp()
        turn = Rotation.FromAxisAngle(axis=omega.normalize(), angle=omega.length() * dt)
        _store_state(mesh, {
            _CENTRE: Vector.Named(_CENTRE) + velocity * dt,
            _ROTATION: Rotation.Named(_ROTATION).rotate_global(turn),
            "Velocity": velocity, "Angular Velocity": omega,
        })
        mesh.out("Mesh")


def _wall_contact_group(rebuild):
    with GeoNodes("Crash Wall Contact", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        wall = Float(0, "Wall")
        wall_speed = Float(0, "Wall Speed")
        half = _rest_half()
        position = Vector.Named(_CENTRE)
        velocity = Vector.Named("Velocity")
        bounds = _bounds(Rotation.Named(_ROTATION), half)
        active = Boolean.Named("Dynamic")
        at_wall = active & (position.x - bounds.x <= wall)
        position = Vector((Float.Switch(active, position.x, position.x.max(wall + bounds.x)),
                           position.y, position.z))
        velocity = Vector((Float.Switch(at_wall, velocity.x, velocity.x.max(wall_speed)),
                           velocity.y, velocity.z))
        _store_state(mesh, {_CENTRE: position, "Velocity": velocity})
        mesh.out("Mesh")


def _ground_contact_group(rebuild):
    with GeoNodes("Crash Ground Contact", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        parts = Mesh(name="Parts")
        dt = Float(0, "Delta Time")
        wall = Float(0, "Wall")
        wall_speed = Float(0, "Wall Speed")
        bounce = Float.Factor(0.25, "Bounce")
        friction = Float(5, "Friction")
        angular_damping = Float(4, "Angular Damping")
        rest_speed = Float(0.2, "Rest Speed")
        centre, half = _rest_centre(), _rest_half()
        part = Integer.Named("Part")
        for ground in repeat(parts.points.count, mesh=mesh):
            grounded = Mesh(ground.mesh)
            part_id = parts.points.sample_index(part, index=ground.iteration)
            selection = part == part_id
            current_centre = Vector.Named(_CENTRE)
            current_rotation = Rotation.Named(_ROTATION)
            transformed = current_centre + current_rotation @ (nd.position - centre)
            lowest = grounded.points[selection].attribute_statistic(transformed.z).min_
            on_floor = Boolean.Named("Dynamic") & (lowest <= 0.00001)
            velocity = Vector.Named("Velocity")
            omega = Vector.Named("Angular Velocity")
            rebound = Float.Switch(-velocity.z > rest_speed.max(0), 0,
                                   -velocity.z * bounce.clamp(0, 1))
            vz = Float.Switch(on_floor & (velocity.z < 0), velocity.z, rebound)
            ground_drag = Float.Switch(on_floor, 1, (-friction.max(0) * dt).exp())
            vx = velocity.x * ground_drag
            wall_contact = current_centre.x - _bounds(current_rotation, half).x <= wall + 0.00001
            vx = Float.Switch(wall_contact & Boolean.Named("Dynamic"), vx, vx.max(wall_speed))
            new_velocity = Vector((vx, velocity.y * ground_drag, vz))
            new_omega = omega * Float.Switch(on_floor, 1, (-angular_damping.max(0) * dt).exp())
            new_omega = Vector.Switch(on_floor & (new_omega.length() < 0.01), new_omega, Vector(0))
            _store_state(grounded, {
                _CENTRE: current_centre + Vector((0, 0, -lowest.min(0))),
                "Velocity": new_velocity, "Angular Velocity": new_omega,
            }, selection=selection)
            ground.mesh = grounded
        Mesh(ground.mesh).out("Mesh")


def _wheel_rest_group(rebuild):
    """Art-directed settling: lay a wheel's axle on vertical around its contact."""
    with GeoNodes("Crash Wheel Rest", is_group=True, rebuild=rebuild):
        mesh = Mesh()
        parts = Mesh(name="Parts")
        wheel = Boolean(False, "Wheel")
        axle = Vector((0, 1, 0), "Axle")
        rate = Float(2, "Rate")
        dt = Float(0, "Delta Time")
        rest_speed = Float(0.2, "Rest Speed")
        wall = Float(0, "Wall")
        wall_speed = Float(0, "Wall Speed")
        centre, half = _rest_centre(), _rest_half()
        part = Integer.Named("Part")
        for settle in repeat(parts.points.count, mesh=mesh):
            state = Mesh(settle.mesh)
            part_id = parts.points.sample_index(part, index=settle.iteration)
            selection = part == part_id
            position = Vector.Named(_CENTRE)
            rotation = Rotation.Named(_ROTATION)
            velocity = Vector.Named("Velocity")
            transformed = position + rotation @ (nd.position - centre)
            lowest = state.points[selection].attribute_statistic(transformed.z).min_
            enabled = (wheel & Boolean.Named("Dynamic") & (lowest <= 0.00001)
                       & (velocity.z.abs() <= rest_speed.max(0.001))
                       & (rate > 0) & (dt > 0) & (axle.length() > 0.000001))

            # Use actual contact vertices as the pivot, including an edge/patch.
            contact = state.points[selection & (transformed.z <= lowest + 0.0001)].attribute_statistic(transformed)
            normal = rotation @ axle.normalize()
            # Choose the nearest side; perfectly upright wheels fall outwards.
            sign = Float.Switch(normal.z < 0, 1, -1)
            sign = Float.Switch(normal.z.abs() < 0.000001, sign,
                                Float.Switch(normal.y * centre.y < 0, -1, 1))
            target = Vector((0, 0, sign))
            angle = normal.dot(target).clamp(-1, 1).acos()
            factor = 1 - (-rate.max(0) * dt).exp()
            turn = Rotation.FromAxisAngle(axis=normal.cross(target).normalize(), angle=angle * factor)
            new_rotation = rotation.rotate_global(turn)
            new_position = contact + turn @ (position - contact)

            # Recompute exact ground height after rotation, moving the whole part.
            rotated = new_position + new_rotation @ (nd.position - centre)
            new_lowest = state.points[selection].attribute_statistic(rotated.z).min_
            new_position += Vector((0, 0, -new_lowest))
            bounds = _bounds(new_rotation, half)
            new_position = Vector((new_position.x.max(wall + bounds.x),
                                   new_position.y, new_position.z))
            at_wall = new_position.x - bounds.x <= wall + 0.00001
            new_velocity = Vector((Float.Switch(at_wall, velocity.x, velocity.x.max(wall_speed)),
                                   velocity.y, 0))
            _store_state(state, {
                _CENTRE: new_position, _ROTATION: new_rotation,
                "Velocity": new_velocity, "Angular Velocity": Vector(0),
            }, selection=selection & enabled)
            settle.mesh = state
        Mesh(settle.mesh).out("Mesh")


def _apply_pose_group(rebuild):
    with GeoNodes("Crash Apply Pose", is_group=True, rebuild=rebuild):
        result = Mesh()
        initial = Mesh(name="Initial")
        x = Float(0, "X")
        wheel_rotation = Rotation((0, 0, 0), "Wheel Rotation")
        wheel_centre = Vector(0, "Wheel Centre")
        centre = _rest_centre()
        result.points.position = (Vector.Named(_CENTRE)
                                  + Rotation.Named(_ROTATION) @ (nd.position - centre)
                                  + Vector((x, 0, 0)))
        initial.points.position = wheel_centre + wheel_rotation @ (nd.position - wheel_centre) + Vector((x, 0, 0))
        result = Mesh.Switch(x > 0, result, initial)
        for name in (_CENTRE, _ROTATION, _IMPACTED, _WHEEL_CENTRE):
            result.remove_named_attribute(name=name)
        result.out("Mesh")
        for name in (_CENTRE, _ROTATION, _IMPACTED, _WHEEL_CENTRE):
            initial.remove_named_attribute(name=name)
        initial.out("Approach")


def demo(rebuild=False):
    """Build utilities and the modifier; preserve existing groups by default."""
    show_parts(rebuild=rebuild)
    transform_part(rebuild=rebuild)
    utilities(rebuild=rebuild)
    swerve(rebuild=rebuild)
    turn_wheel(rebuild=rebuild)

    with GeoNodes("Car Crash", rebuild=rebuild):
        mesh = Mesh()
        skip = Boolean(False, "Skip")
        x = Float(0, "X")
        # Simulate in the car's rest frame, then translate back to the fixed wall.
        wall = (-x).max(0)

        with Panel("Propagation"):
            start = Float(0.25, "Start Distance", min=0.001)
            anticipation = Float(0.8, "Anticipation", min=0.001)
            half_width = Float(0.8, "Half Width", min=0.001)

        with Panel("Translation"):
            advance = Float(0.15, "Advance", min=0)
            spread = Float(1.2, "Spread", min=0)
            lift = Float(0.7, "Lift", min=0)

        with Panel("Rotation"):
            roll = Float.Angle(radians(35), "Roll")
            pitch = Float.Angle(radians(70), "Pitch")
            yaw = Float.Angle(radians(25), "Yaw")

        with Panel("Dynamics"):
            impact_speed = Float(3, "Impact Speed", min=0)
            gravity = Float(9.81, "Gravity", min=0)
            drag = Float(0.15, "Air Drag", min=0)
            bounce = Float.Factor(0.25, "Bounce")
            friction = Float(5, "Friction", min=0)
            angular_damping = Float(4, "Angular Damping", min=0)
            rest_speed = Float(0.2, "Rest Speed", min=0)
            substeps = Integer(4, "Substeps", min=1, max=64)

        with Panel("Wheel Rest"):
            type_attribute = String("Part ID", "Type Attribute")
            wheel_radius = Float(0.3, "Wheel Radius", min=0.001)
            wheel_rate = Float(2, "Wheel Rest Rate", min=0)
            wheel_axle = Vector((0, 1, 0), "Wheel Axle")
            part_type = Integer.Named(type_attribute)
            wheel = (part_type == 8) | (part_type == 9)

        with Panel("Randomness"):
            randomness = Float.Factor(0.65, "Randomness")
            seed = Integer(0, "Seed")

        with Layout("Initialize parts and choose their behaviour"):
            mesh = Mesh(Group("Crash Wheel Setup", mesh=mesh, part_type=part_type).mesh)
            initial = Group("Crash Initialize", mesh=mesh)
            mesh = Mesh(initial.mesh)
            behaviour = Group("Crash Part Behaviour", half_width=half_width,
                              advance=advance, spread=spread, lift=lift,
                              roll=roll, pitch=pitch, yaw=yaw,
                              randomness=randomness, seed=seed)

        with Layout("Wheel rolling from X, outside simulation"):
            wheel_id = Integer.Named("Wheel ID")
            wheel_member = (wheel_id >= 1) & (wheel_id <= 4)
            wheel_centre = Vector.Named(_WHEEL_CENTRE)
            rolling = Rotation(Vector((0, Float.Switch(wheel_member, 0, x / wheel_radius.max(0.001)), 0)))

        for sim in simulation(mesh=mesh, previous_wall=wall.max(0)):
            sim.skip = skip
            steps = substeps.max(1)
            dt = sim.delta_time / steps
            wall_end = wall.max(0)
            wall_speed = ((wall_end - sim.previous_wall)
                          / sim.delta_time.max(0.000001)).max(0)

            for rep in repeat(steps, mesh=sim.mesh):
                m = sim.previous_wall + (wall_end - sim.previous_wall) * ((rep.iteration + 1) / steps)
                influence = Group("Crash Influence", wall=m, start_distance=start,
                                  anticipation=anticipation, reach_scale=behaviour.reach_scale)
                state = Group("Crash Part Release", mesh=rep.mesh,
                              reaction=influence.reaction, displacement=behaviour.displacement,
                              spin=behaviour.spin, wall=m, wall_speed=wall_speed,
                              frame_time=sim.delta_time, impact_speed=impact_speed,
                              wheel_rotation=rolling, wheel_centre=wheel_centre).mesh
                state = Group("Crash Part Dynamics", mesh=state, delta_time=dt,
                              gravity=gravity, air_drag=drag).mesh
                state = Group("Crash Wall Contact", mesh=state, wall=m, wall_speed=wall_speed).mesh
                state = Group("Crash Ground Contact", mesh=state, parts=initial.parts,
                              delta_time=dt, wall=m, wall_speed=wall_speed,
                              bounce=bounce, friction=friction,
                              angular_damping=angular_damping, rest_speed=rest_speed).mesh
                state = Group("Crash Wheel Rest", mesh=state, parts=initial.parts,
                              wheel=wheel, axle=wheel_axle, rate=wheel_rate,
                              delta_time=dt, rest_speed=rest_speed,
                              wall=m, wall_speed=wall_speed).mesh
                rep.mesh = state

            sim.mesh = Mesh.Switch(x > 0, rep.mesh, mesh)
            sim.previous_wall = wall_end

        pose = Group("Crash Apply Pose", mesh=sim.mesh, initial=mesh, x=x,
                     wheel_rotation=rolling, wheel_centre=wheel_centre)
        crashed = Mesh(pose.mesh).bake()
        # The approach depends only on live input geometry and X, even with a
        # baked simulation. It never needs the simulation/bake output.
        Mesh.Switch(x > 0, crashed, pose.approach).out()


def swerve(rebuild=False):
    """Follow a Curve object and progressively scatter the car's rigid parts.

    Path supplies the trajectory in object-relative coordinates (first spline).
    Time is distance from its start, increasing forwards and clamped to its
    length. The car's XY bounds centre follows the path; its bottom sits at
    path height. The original front (-X) follows the horizontal curve tangent.
    Factor progressively releases pieces and drives outward impulses, not the trajectory.
    Body Roll tilts the attached assembly around its longitudinal axis, keeping
    a shared ground contact, and never transforms already released pieces.
    Z adds a manual height correction to the remaining body after ground contact.
    Skip freezes debris simulation; attached body controls remain live.
    Reverse the curve direction in Blender if it runs the wrong way.

    The rightmost 15 percent of part centres remains attached. Wheel ID 1..4
    rolls tyres, rims and bolts together using distance travelled. Missing or
    empty Path leaves the input geometry unchanged. Released pieces simulate in
    object space independently of the path, with gravity, ground contact and
    a fixed wall at X=0 (debris stays on the positive-X side).
    Play sequentially from the scene start; clear simulation caches after edits.
    """
    _wheel_setup_group(rebuild=rebuild)
    with GeoNodes("Car Swerve", rebuild=rebuild):
        mesh = Mesh()
        original = Mesh(mesh)
        factor = Float.Factor(0, "Factor", 0, 1)
        time = Float(0, "Time", min=0)
        body_roll = Float.Angle(0, "Body Roll")
        body_z = Float(0, "Z")
        skip = Boolean(False, "Skip")
        path_object = Object(None, "Path")
        path = Curve(path_object.info(transform_space='Relative').geometry_)
        path = path.splines[nd.index != 0].delete()
        path_length = path.length()
        distance = time.max(0).min(path_length)
        sample = path.sample_length(value=Float(0), length=distance, curve_index=0)
        part = Integer.Named("Part")
        centre = _rest_centre()

        with Layout("Wheel rolling from Time around each shared axle"):
            wheel_id = Integer.Named("Wheel ID")
            part_type = Integer.Named("Part ID")
            mesh = Mesh(Group("Crash Wheel Setup", mesh=mesh, part_type=part_type).mesh)
            # Derive wheel radii from the tyres, independently of the turn radius.
            radius_name = "_CarSwerve Wheel Radius"
            mesh.points.set(radius_name, Float(1))
            for number in range(1, 5):
                members = wheel_id == number
                tyres = members & (part_type == 8)
                has_tyre = mesh.points[tyres].attribute_statistic(Float(1)).sum_ > 0
                wheel_bounds = mesh.points[Boolean.Switch(has_tyre, members, tyres)].attribute_statistic(nd.position)
                size = wheel_bounds.max_ - wheel_bounds.min_
                radius = (size.x.max(size.z) * 0.5).max(0.001)
                mesh.points[members].set(radius_name, radius)
            wheel = (wheel_id >= 1) & (wheel_id <= 4)
            roll_angle = Float.Switch(wheel, 0, -distance / Float.Named(radius_name))
            rolling = Rotation(Vector((0, roll_angle, 0)))
            wheel_centre = Vector.Named(_WHEEL_CENTRE)

        with Layout("Follow the curve position and tangent"):
            bounds = mesh.points.attribute_statistic(nd.position)
            lower, upper = bounds.min_, bounds.max_
            width = (upper.y - lower.y).max(0.001)
            anchor = Vector(((lower.x + upper.x) * 0.5,
                             (lower.y + upper.y) * 0.5, lower.z))
            tangent = sample.tangent_
            yaw = (-tangent.y).atan2(-tangent.x)
            turn = Rotation(Vector((0, 0, yaw)))
            body_rotation = turn.rotate_local(Rotation(Vector((body_roll, 0, 0))))
            ground_height = sample.position_.z
            # This pivot only defines the outward scatter direction in rest space.
            pivot = anchor + Vector((0, width * 0.55, 0))

        with Layout("Keep the right edge attached"):
            sides = mesh.points.attribute_statistic(centre.y)
            span = (sides.max_ - sides.min_).max(0.001)
            across = ((sides.max_ - centre.y) / span).clamp(0, 1)
            strength = ((across - 0.15) / 0.85).clamp(0, 1)
            identifier = Integer.Named("Identifier")
            protected = (identifier == 71) | (identifier == 79)
            strength = Float.Switch(protected, strength, 0)
            detached = strength > 0
            rank = mesh.points.accumulate_field(Integer(1), group_id=part).trailing_
            parts = Mesh(mesh).points[rank != 0].delete()

        with Layout("Attached pose and release controls"):
            radial = ((centre - pivot) * Vector((1, 1, 0))).normalize()
            outward = turn @ radial
            release_at = 0.05 + 0.7 * (1 - strength) + Float.Random(0, 0.2, id=part, seed=83)
            kick = width * strength * Float.Random(0.75, 1.25, id=part, seed=81)
            spin = Vector.Random((-1.5, -1.5, -2), (1.5, 1.5, 2), id=part, seed=82)
            lean = Rotation(spin * strength * factor * 0.15)
            attached_rotation = body_rotation.rotate_local(lean).rotate_local(rolling)
            rolled_centre = wheel_centre + rolling @ (centre - wheel_centre)
            attached_centre = sample.position_ + body_rotation @ (rolled_centre - anchor)
            target_name = "_CarSwerve Target"
            outward_name = "_CarSwerve Outward"
            floor_name = "_CarSwerve Ground"
            mesh.points.set(_CENTRE, attached_centre)
            mesh.points.set(_ROTATION, attached_rotation)
            mesh.points.set("Dynamic", Boolean(False))
            mesh.points.set("Velocity", Vector(0))
            mesh.points.set("Angular Velocity", Vector(0))
            mesh.points.set(target_name, attached_centre)
            mesh.points.set(outward_name, Vector(0))
            mesh.points.set(floor_name, ground_height)

        def support_body(state):
            # One ground correction for the entire remaining body preserves its
            # rigid assembly. Detached pieces keep their independent contacts.
            attached = Boolean.Named("Dynamic").bnot()
            position = Vector.Named(_CENTRE)
            transformed = position + Rotation.Named(_ROTATION) @ (nd.position - centre)
            lowest = state.points[attached].attribute_statistic(transformed.z).min_
            lift = Float.Switch(body_roll != 0, 0, ground_height - lowest)
            _store_state(state, {_CENTRE: position + Vector((0, 0, lift))}, selection=attached)

        for sim in simulation(mesh=mesh, previous_factor=factor):
            sim.skip = skip
            dt = sim.delta_time / 4
            advance = (factor - sim.previous_factor).max(0) / 4
            for step in repeat(4, mesh=sim.mesh):
                state = Mesh(step.mesh)
                dynamic = Boolean.Named("Dynamic")
                released = dynamic.bnot() & detached & (factor >= release_at) & (dt > 0)
                active = dynamic | released
                previous_target = Vector.Named(target_name)
                following_velocity = (attached_centre - previous_target) / sim.delta_time.max(0.000001)
                # Freeze launch direction and ground height at detachment. Neither
                # free position nor free orientation depends on the current path.
                launch_direction = Vector.Switch(released, Vector.Named(outward_name), outward)
                floor = Float.Switch(active, ground_height, Float.Named(floor_name))
                floor = Float.Switch(released, floor, ground_height)
                velocity = Vector.Switch(released, Vector.Named("Velocity"),
                                         following_velocity + outward * kick + Vector((0, 0, kick * 0.6)))
                velocity += launch_direction * kick * advance * 2
                velocity = (velocity + Vector((0, 0, -9.81)) * dt) * (-0.15 * dt).exp()
                velocity = Vector.Switch(active, Vector(0), velocity)
                omega = Vector.Switch(released, Vector.Named("Angular Velocity"), spin * strength)
                omega *= (-0.15 * dt).exp()
                omega = Vector.Switch(active, Vector(0), omega)
                flying_centre = Vector.Switch(released, Vector.Named(_CENTRE), attached_centre) + velocity * dt
                flying_rotation = Rotation.Switch(released, Rotation.Named(_ROTATION), attached_rotation)
                delta = Rotation.FromAxisAngle(axis=omega.normalize(), angle=omega.length() * dt)
                flying_rotation = flying_rotation.rotate_global(delta)
                _store_state(state, {
                    _CENTRE: flying_centre,
                    _ROTATION: flying_rotation,
                    "Dynamic": active, "Velocity": velocity, "Angular Velocity": omega,
                    outward_name: launch_direction, floor_name: floor,
                }, selection=active)
                moving_parts = Mesh(state).points[(rank != 0) | Boolean.Named("Dynamic").bnot()].delete()
                for ground in repeat(moving_parts.points.count, mesh=state):
                    result = Mesh(ground.mesh)
                    part_id = moving_parts.points.sample_index(part, index=ground.iteration)
                    selection = (part == part_id) & Boolean.Named("Dynamic")
                    pos = Vector.Named(_CENTRE)
                    rot = Rotation.Named(_ROTATION)
                    transformed = pos + rot @ (nd.position - centre)
                    minimum = result.points[selection].attribute_statistic(transformed).min_
                    height = minimum.z - Float.Named(floor_name)
                    grounded = Boolean.Named("Dynamic") & (height <= 0.00001)
                    wall_contact = Boolean.Named("Dynamic") & (minimum.x <= 0.00001)
                    vel = Vector.Named("Velocity")
                    wall_hit = wall_contact & (vel.x < 0)
                    vx = Float.Switch(wall_hit, vel.x, -vel.x * 0.3)
                    wall_push = Float.Switch(Boolean.Named("Dynamic"), 0, -minimum.x.min(0))
                    bounce = Float.Switch(-vel.z > 0.2, 0, -vel.z * 0.2)
                    vz = Float.Switch(grounded & (vel.z < 0), vel.z, bounce)
                    friction = Float.Switch(grounded, 1, (-5 * dt).exp())
                    angular_drag = Float.Switch(grounded, 1, (-4 * dt).exp())
                    angular_drag *= Float.Switch(wall_hit, 1, 0.8)
                    _store_state(result, {
                        _CENTRE: pos + Vector((wall_push, 0, -height.min(0))),
                        "Velocity": Vector((vx * friction, vel.y * friction, vz)),
                        "Angular Velocity": Vector.Named("Angular Velocity") * angular_drag,
                    }, selection=selection)
                    ground.mesh = result
                step.mesh = ground.mesh
            state = Mesh(step.mesh)
            state.points.set(target_name, attached_centre)
            sim.mesh = state
            sim.previous_factor = factor

        result = Mesh(sim.mesh)
        # Live body pose is evaluated after the simulation, including when its
        # state is frozen by Skip. Only released pieces use simulated poses.
        _store_state(result, {_CENTRE: attached_centre, _ROTATION: attached_rotation},
                     selection=Boolean.Named("Dynamic").bnot())
        support_body(result)
        for contact in repeat(parts.points.count, mesh=result):
            body = Mesh(contact.mesh)
            part_id = parts.points.sample_index(part, index=contact.iteration)
            selection = ((part == part_id) & Boolean.Named("Dynamic").bnot()
                         & (body_roll == 0))
            pos = Vector.Named(_CENTRE)
            transformed = pos + Rotation.Named(_ROTATION) @ (nd.position - centre)
            lowest = body.points[selection].attribute_statistic(transformed.z).min_
            _store_state(body, {_CENTRE: pos + Vector((0, 0, (ground_height - lowest).max(0)))},
                         selection=selection)
            contact.mesh = body
        result = Mesh(contact.mesh)
        result.points.position = Vector.Named(_CENTRE) + Rotation.Named(_ROTATION) @ (nd.position - centre)
        # Manual art-direction offset, after contact resolution. Keep it out of
        # the simulation so it never translates or accelerates detached debris.
        result.points[Boolean.Named("Dynamic").bnot()].position = nd.position + Vector((0, 0, body_z))
        for name in (radius_name, _WHEEL_CENTRE, _CENTRE, _ROTATION, target_name, outward_name, floor_name):
            result.remove_named_attribute(name=name)
        Mesh.Switch(path_length > 0.000001, original, result).out()


def turn_wheel(rebuild=False):
    """Roll Wheel ID 1..4 along Y rotated by the car's existing Z rotation."""
    _wheel_setup_group(rebuild=rebuild)
    with GeoNodes("Turn Wheel", rebuild=rebuild):
        mesh = Mesh()
        angle = Float.Angle(0, "Rotation")
        car_angle = Float.Angle(0, "Car Rotation")
        mesh = Mesh(Group("Crash Wheel Setup", mesh=mesh,
                          part_type=Integer.Named("Part ID")).mesh)
        wheel_id = Integer.Named("Wheel ID")
        selection = (wheel_id >= 1) & (wheel_id <= 4)
        pivot = Vector.Named(_WHEEL_CENTRE)
        axle = Rotation(Vector((0, 0, car_angle))) @ Vector((0, 1, 0))
        rotation = Rotation.FromAxisAngle(axis=axle, angle=angle)
        mesh.points[selection].position = pivot + rotation @ (nd.position - pivot)
        mesh.remove_named_attribute(name=_WHEEL_CENTRE)
        mesh.out()


def show_parts(rebuild=False):
    """Show positive Identifiers or filtered Part numbers at current part centres."""
    with GeoNodes("Car Parts", rebuild=rebuild):
        mesh = Mesh()
        offset = Float(0.2, "Offset")
        size = Float(0.15, "Font Size", min=0.001)
        identifiers = Boolean(True, "Identifiers")
        part_min = Integer(0, "Part Min")
        parts_count = Integer(1000, "Parts Count", min=0)
        part = Integer.Named("Part")
        identifier = Integer.Named("Identifier")
        # Current geometry bounds, independently of the displayed range.
        bounds = mesh.points.attribute_statistic(nd.position)
        global_centre = (bounds.min_ + bounds.max_) * 0.5

        # Only the first vertex of each Part emits a label.
        rank = mesh.points.accumulate_field(Integer(1), group_id=part).trailing_
        in_range = (part >= part_min) & (part < part_min + parts_count)
        selection = (rank == 0) & Boolean.Switch(identifiers, in_range, identifier > 0)
        value = Integer.Switch(identifiers, part, identifier)
        for label_part in mesh.points[selection].for_each(value=value, part_index=part):
            centre = mesh.points[part == label_part.part_index].attribute_statistic(nd.position)
            position = centre + (centre - global_centre).normalize().scale(offset)
            label = Curve(label_part.value.to_string().to_curves(size=size, align_x='CENTER'))
            label.transform(translation=position, rotation=(radians(90), 0, 0))
            line = Curve.Line(centre, position)
            line = line.to_mesh(profile_curve=Curve.Circle(resolution=6, radius=0.002))
            (label.fill() + line).out()

        labels = Mesh(Instances(label_part.generated).realize())
        (mesh + labels).out()


def transform_part(rebuild=False):
    """Select by Identifier or Part and rotate around the current mean + Pivot.

    Offset translates the result. All inputs use object coordinates.
    """
    with GeoNodes("Car Transform Part", rebuild=rebuild):
        mesh = Mesh()
        part = Integer(0, "Part")
        identifier = Boolean(True, "Identifier")
        offset = Vector((0, 0, 0), "Offset")
        rotation = Rotation((0, 0, 0), "Rotation")
        pivot_offset = Vector((0, 0, 0), "Pivot")

        selected_id = Integer.Switch(identifier, Integer.Named("Part"), Integer.Named("Identifier"))
        selection = selected_id == part
        centre = mesh.points[selection].attribute_statistic(nd.position)
        pivot = centre + pivot_offset
        mesh.points[selection].position = (
            pivot + rotation @ (nd.position - pivot) + offset)
        mesh.out()
