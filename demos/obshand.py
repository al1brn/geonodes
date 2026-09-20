"""Standalone workshop for the Observer hand mesh.

Run ``obshand.demo()`` and use the ``Obs Hand Lab`` modifier on a mesh object.
The hand uses one connected cage with shared vertices at the finger webs.
Bend deforms the palm through metacarpal weights, then subdivision rounds
the surface. All groups and the material are separate from Observer.
The previous construction remains available through build_legacy_hand().
"""

import bpy
from geonodes import *

import math


def demo():

    from geonodes.demos import meshutil
    #meshutil.demo()

    # ====================================================================================================
    # Hand bones
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # One Finger bones
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Finger Bones", is_group=True):

        length = Float(1.0, "Size")

        single_fold = Boolean(True, "Single Fold")
        lateral = Float.Angle(0, "Lateral")
        bend = Float.Angle(0, "Bend")
        fold = Float.Angle(0, "Fold")
        fold2 = Float.Angle(0, "Second Fold")
        bend_factor = Float.Factor(0.0, "Bend Factor")
        subdiv = Integer(5, "Palm Subdivisions", 0)
        position = Vector(0, "Position")

        with Layout("Prepare"):
            fold2.switch(single_fold, fold)
            l3 = (length/3)._lc("l")

        line = G().build_poly_line(length=length, angle=pi/2, plane='YZ')
        line = G().build_poly_line(line, length=length*0.4, angle=bend, plane='XZ')
        line = G().build_poly_line(line, length=length*0.3, angle=fold, plane='XZ')
        line = G().build_poly_line(line, length=length*0.3, angle=fold2, plane='XZ')

        pivot = line.points.sample_index(nd.position, index=2)
        line.points[nd.index > 2].position = pivot + Rotation((lateral, 0, 0)) @ (nd.position - pivot)

        line = G().round_joints(line, selection=nd.index >= 1, resolution=2, length=0.07)

        line = G().subdivide_segment(line, index=0, subdivisions=subdiv)
        line.points.radius = 1.0
        line.points[nd.index < subdiv].radius = 1.2
        line.points[nd.index == subdiv].radius = 1.1

        with Layout("Meshes"):
            c = Curve(line).points[nd.index > subdiv + 3].delete()
            palm_mesh = c.to_mesh(
                    profile_curve=Curve.Circle(radius=0.15, resolution=8),
                    fill_caps=False,
                    scale = nd.radius,
                    )
            palm_mesh = meshutil.set_cylinder_topology(palm_mesh, nrings=subdiv + 4, nsegms=8)
            palm_mesh = G().close_cylinder(palm_mesh, rings=3, height=0.15, flatten_last=True, append=True)

            c = Curve(line).points[nd.index < subdiv + 3].delete()        
            finger_mesh = c.curve_to_tube(
                    scale=0.15,
                    profile_resolution=8,
                    caps=True,
                    caps_type='Round',
                    )

        # Additional bend changes the vertices numbering
        # It is applied after mesh computation

        with Layout("Additional Bend"):
            add_bend = bend.map_range(from_max=math.radians(20), to_max=math.radians(10))*bend_factor
            line.position = position + Rotation((0, add_bend, 0)) @ nd.position
            palm_mesh.position = position + Rotation((0, add_bend, 0)) @ nd.position
            finger_mesh.position = position + Rotation((0, add_bend, 0)) @ nd.position

        line.out("Bones")
        palm_mesh.out("Palm")
        finger_mesh.out("Finger")

    # ----------------------------------------------------------------------------------------------------
    # Thumb bones
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Thumb Bones", is_group=True):

        length = 1.0

        lateral = Float.Angle(0, "Lateral")
        bend = Float.Angle(0, "Bend")
        fold = Float.Angle(0, "Fold")
        pinch = Float.Angle(0, "Pinch")

        with Layout("Prepare"):
            ph = length/3 

        line = G().build_poly_line(length=length*0.5, angle=pi/2, plane='YZ')
        line = G().build_poly_line(line, length=ph, angle=bend, plane='XZ')
        line = G().build_poly_line(line, length=ph, angle=fold, plane='XZ')

        line.transform(rotation=(0, 0, math.radians(35)))
        line.transform(rotation=(math.radians(45) + lateral, 0, 0))
        line.transform(rotation=(0, 0, pinch))

        with Layout("Thumb Mesh"):
            # A wider base blends into the palm; the two phalanges taper.
            profile = Curve(line)
            profile.points.radius = 1.0
            profile.points[nd.index == 0].radius = 1.4
            profile.points[nd.index == 1].radius = 1.2
            profile = G().round_joints(profile, resolution=2, length=0.07)
            thumb_mesh = profile.curve_to_tube(
                scale=0.15,
                profile_resolution=10,
                caps=True,
                caps_type='Round',
            )

        thumb_mesh.out("Thumb")
        line.out("Bones")

    # ----------------------------------------------------------------------------------------------------
    # Hand bones
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Hand Bones", is_group=True):

        subdiv = Integer(0, "Palm Subdivisions")

        delta_y = 0.3

        with Panel("Thumb"):
            thumb_node = G().thumb_bones().link_inputs().node
            bones0 = Curve(thumb_node.bones)
            bones0.offset = (0, delta_y*(-1.4), 0.05)
            thumb_mesh = thumb_node.thumb
            thumb_mesh.offset = (0, delta_y*(-1.4), 0.05)

            bones0.points.radius = 1.0
            bones0.points[0].radius = 1.4
            bones0.points[1].radius = 1.2

        with Panel("Finger 1"):
            bones1 = G().finger_bones(
                size=1.0, 
                palm_subdivisions=subdiv,
                position=(0, delta_y*(-1.5), 0)).link_inputs()

        with Panel("Finger 2"):
            bones2 = G().finger_bones(
                size=1.1, 
                palm_subdivisions=subdiv,
                position=(0, delta_y*(-0.5), 0)).link_inputs()

        with Panel("Finger 3"):
            bones3 = G().finger_bones(
                size=1.0, 
                bend_factor=0.5, 
                palm_subdivisions=subdiv,
                position=(0, delta_y*( 0.5), 0)).link_inputs()

        with Panel("Finger 4"):
            bones4 = G().finger_bones(
                size=0.95, 
                bend_factor=1.0, 
                palm_subdivisions=subdiv,
                position=(0, delta_y*( 1.5), 0)).link_inputs()

        fingers = [bones1, bones2, bones3, bones4]

        for i, finger in enumerate(fingers):
            finger.out(f"Bones {i+1}")
            finger.palm.out(f"Palm {i+1}")
            finger.finger.out(f"Finger {i+1}")

        (bones0 + tuple(fingers)).out("All Bones")
        thumb_mesh.out("Thumb")

    # ====================================================================================================
    # Hand
    # ====================================================================================================

    with GeoNodes("Hand"):

        SUBDIV = 5

        size = Float(1.0, "Size", 0.001)

        node = G().hand_bones(palm_subdivisions=SUBDIV).link_inputs().node

        palm_meshes = [node.palm_1, node.palm_2, node.palm_3, node.palm_4]
        finger_meshes = [node.thumb, node.finger_1, node.finger_2, node.finger_3, node.finger_4]

        # palm indices matching with tubes
        # Columns
        matches = [
            [{"n": 5, "from": 4, "to": 7}],
            [
                {"n": 1, "from": 4, "to": 6},
                {"n": 1, "from": 0, "to": 12},
            ],
            [
                {"n": 1, "from": 4, "to": 5},
                {"n": 1, "from": 0, "to": 13},
            ],
            [{"n": 5, "from": 0, "to": 0}],
        ]

        with Layout("Palm Mesh"):

            nrings, _ = meshutil.get_cylinder_topology(palm_meshes[0])
            palm = G().new_cylinder(rings=nrings, segments=14)

            for i_finger, (model, match) in enumerate(zip(palm_meshes, matches, strict=True)):
                with Layout(f"Finger {i_finger+1}"):
                    f = model
                    for d in match:
                        palm = G().cylinder_copy_position(
                            palm,
                            ring_index      = 0,
                            ring_count      = nrings,
                            col_index       = d["to"],
                            col_count       = d["n"],
                            model           = f,
                            from_ring_index = 0,
                            from_col_index  = d["from"],
                        )

        with Layout("Add Fingers"):

            hand = palm + tuple(finger_meshes)

        hand.out()
        #palm_meshes[0].out()
        #(palm + palm_meshes[0]).out()
        raise Break()
    
        palm.faces.shade_smooth=True



        #(palm + palm_meshes[3] + labels).out()
        #(palm_meshes[0] + finger_meshes[0]).out()
        #(palm + tuple(finger_meshes)).out()
        raise Break()

        mesh = meshes[0] + tuple(meshes[1:])

        (mesh + node.all_bones).out()











def build_legacy_hand():
    """Build the experimental hand, thumb, finger and articulation groups."""
    if bpy.data.materials.get("Obs Hand Lab Skin") is None:
        with ShaderNodes("Obs Hand Lab Skin"):
            Shader.Principled(base_color=(0.65, 0.52, 0.41, 1.0), roughness=0.9).out()

    with GeoNodes("Obs Mesh Hand Lab Sausage", is_group=True):

        curve    = Curve()
        profile  = Curve(None, "Profile")
        angle    = Float.Angle(.2, "Angle", hide_value=False)
        twist    = Float.Angle(0, "Twist", -pi, pi)
        axis     = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2}, menu=Input("Axis"))
        use_mesh = Boolean(True, "Mesh")

        with Panel("Joints"):
            use_joints   = Boolean(True, "Joints")
            joints_width = Float.Factor(.1, "Joints Width", 0, 1)

        with Panel("Extremities"):
            start_shape = Float(.4,    "Start Shape", 0, 5)
            start_resol = Integer(0,   "Start Resolution", 0)
            end_shape   = Float(.4,    "End Shape", 0, 5)
            end_resol   = Integer(0,   "End Resolution", 0)

        n  = curve.points.count

        for rep in repeat(n-1, curve=curve):
            index   = rep.iteration + 1
            pos     = nd.position
            center  = rep.curve.points.sample_index(pos, index=index)
            ag      = rep.curve.points.sample_index(angle, index=index)
            rot     = Rotation.IndexSwitch((ag, 0, 0), (0, ag, 0), (0, 0, ag), index=axis)
            p       = center + rot @ (pos - center)
            rep.curve.points[nd.index > index].position = p

        curve = rep.curve

        with Layout("Joints"):

            # 0------1------2------3------4------5
            # 0      1 2  3 4 5  6 7 8  9 10     11

            n_joints = n - 3
            m = n + n_joints*2 # 3n - 6
            last = m - 1

            with Layout("Joints Selection"):
                i = nd.index + 2
                joint_sel   = (i % 3).equal(0)
                joint_index = i // 3

            with Layout("Left"):
                i = nd.index + 1
                left_sel = (i % 3).equal(0) & nd.index.not_equal(last)
                left0 = i // 3
                left1 = left0 + 1

            with Layout("Right"):
                i = nd.index
                right_sel = (i % 3).equal(0) & i.not_equal(0)
                right0 = i // 3
                right1 = right0 + 1

            new_curve = Curve(curve).resample(count=m)

            # ----- Left

            with Layout("Left"):

                jfac = .3*joints_width

                pos0 = curve.points.sample_index(nd.position, index=left0)
                pos1 = curve.points.sample_index(nd.position, index=left1)
                new_curve.points[left_sel].position = pos0 + jfac*(pos1 - pos0)

                r0 = curve.points.sample_index(nd.radius, index=left0)
                r1 = curve.points.sample_index(nd.radius, index=left1)
                new_curve.points[left_sel].radius = r0 + jfac*(r1 - r0)

            with Layout("Right"):

                jfac = 1 - jfac

                pos0 = curve.points.sample_index(nd.position, index=right0)
                pos1 = curve.points.sample_index(nd.position, index=right1)
                new_curve.points[right_sel].position = pos0 + jfac*(pos1 - pos0)

                r0 = curve.points.sample_index(nd.radius, index=right0)
                r1 = curve.points.sample_index(nd.radius, index=right1)
                new_curve.points[right_sel].radius = r0 + jfac*(r1 - r0)

            with Layout("Joints"):
                new_curve.points[joint_sel].position = curve.points.sample_index(nd.position, index=joint_index)
                new_curve.points[joint_sel].radius   = curve.points.sample_index(nd.radius,   index=joint_index)

            curve = Curve(curve.switch(use_joints, new_curve))
            n = curve.points.count

        with Layout("Twist"):
            curve = curve.transform(rotation=(0, 0, twist))

        with Layout("Start Shape"):

            m = n + start_resol
            start_resol1 = start_resol + 1

            new_curve = Curve(curve).resample(count=m)
            new_curve.points[nd.index > start_resol].position = curve.points.sample_index(nd.position, index=nd.index - start_resol)
            new_curve.points[nd.index > start_resol].radius   = curve.points.sample_index(nd.radius,   index=nd.index - start_resol)

            fac = nd.index/start_resol1

            pos0 = curve.points.sample_index(nd.position, index=0)
            pos1 = curve.points.sample_index(nd.position, index=1)

            new_curve.points[nd.index <= start_resol].position = pos0 + (pos1 - pos0).scale(fac)

            radius = curve.points.sample_index(nd.radius, index=1)
            new_curve.points[nd.index <= start_resol].radius = radius*fac**start_shape

            curve = new_curve
            n = curve.points.count

        with Layout("End Shape"):

            m = n + end_resol
            last = n - 2

            new_curve = Curve(curve).resample(count=m)
            new_curve.points[nd.index <= last].position = curve.points.sample_index(nd.position, index=nd.index)
            new_curve.points[nd.index <= last].radius   = curve.points.sample_index(nd.radius,   index=nd.index)

            fac = (nd.index - last)/(end_resol + 1)

            pos0 = curve.points.sample_index(nd.position, index=n-2)
            pos1 = curve.points.sample_index(nd.position, index=n-1)

            new_curve.points[nd.index > last].position = pos0 + (pos1 - pos0).scale(fac)

            radius = curve.points.sample_index(nd.radius, index=n-2)
            new_curve.points[nd.index > last].radius = radius*(1-fac)**end_shape

            curve = new_curve
            #n = curve.points.count


        mesh = curve.to_mesh(profile_curve=profile, scale=nd.radius)
        curve.switch(use_mesh, mesh).out()


    # ====================================================================================================
    # Finger
    # ====================================================================================================

    with GeoNodes("Obs Mesh Hand Lab Finger", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol        = Integer(4, "Resolution", 1, 8)
        length       = Float(1, "Length", 0)
        radius       = Float(.12, "Radius", 0)
        bend         = Float.Angle(0, "Bend", 0, pi/2, shape='Single')
        fold         = Float.Angle(0, "Fold", 0, pi/2, shape='Single')
        lateral      = Float.Angle(0, "Lateral", -pi/8, pi/8, shape='Single')

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(6)]

            curve = Curve.Line(start=(0, 0, -.2), end=(0, 0, 1)).resample(count=6)
            curve.points[ind[1]].position = (0, 0, 0)
            curve.points[ind[2]].position = (0, 0, .33)
            curve.points[ind[3]].position = (0, 0, .66)
            curve.points[ind[4]].position = (0, 0, .92)

            curve.points.radius = 1.
            curve.points[ind[0]].radius = .3
            curve.points[ind[5]].radius = 0.

            curve.points._Angle = 0.
            curve.points[ind[1]]._Angle = bend
            curve.points[ind[2]]._Angle = fold
            curve.points[ind[3]]._Angle = fold

            curve.points._Circle_index = Float(nd.index)


            curve.transform(scale=length)

        with Layout("Profile"):
            resolution = resol*4
            profile = Curve.Circle(radius=radius).resample(count=resolution)

        with Layout("Finger Shape"):

            finger = G().obs_mesh_hand_lab_sausage(
                curve               = curve,
                profile             = profile,
                angle               = Float("Angle"),
                joints              = True,
                joints_width        = .4,
                axis                = 'X',
                start_shape         =  1,
                start_resolution    =  0,
                end_shape           = .4,
                end_resolution      =  4,
            )
        finger = Mesh(finger)

        with Layout("Finalize"):
            finger.transform(rotation=(0, lateral, 0))

        finger.out()

    # ====================================================================================================
    # Thumb
    # ====================================================================================================

    with GeoNodes("Obs Mesh Hand Lab Thumb", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol        = Integer(4, "Resolution", 1, 8)
        length       = Float(1, "Length", 0)
        radius       = Float(.12, "Radius", 0)
        pinch        = Float.Angle(0, "Pinch", 0, pi/2, shape='Single')
        bend         = Float.Angle(0, "Bend", 0, pi/2, shape='Single')
        fold         = Float.Angle(0, "Fold", 0, pi/2, shape='Single')
        lateral      = Float.Angle(0, "Lateral", -pi/2, pi/2, shape='Single')

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(6)]

            curve = Curve.Line(start=(0, 0, -.5), end=(0, 0, 1)).resample(count=6)
            curve.points[ind[1]].position = (0, 0, 0)
            curve.points[ind[2]].position = (0, 0, .5)
            curve.points[ind[3]].position = (0, 0, 1)
            curve.points[ind[4]].position = (0, 0, 1.2)
            curve.points[ind[5]].position = (0, 0, 1.5)


            curve.points.radius = 1.
            curve.points[ind[0]].radius = 0
            curve.points[ind[1]].radius = 1.1
            curve.points[ind[5]].radius = 0

            curve.points._Angle = 0.
            curve.points[ind[1]]._Angle = pinch
            curve.points[ind[2]]._Angle = bend
            curve.points[ind[3]]._Angle = fold

            curve.transform(scale=length)

        with Layout("Profile"):
            resolution = resol*4
            profile = Curve.Circle(radius=radius).resample(count=resolution)

        with Layout("Finger Shape"):

            finger = G().obs_mesh_hand_lab_sausage(
                curve               = curve,
                profile             = profile,
                angle               = Float("Angle"),
                joints              = True,
                joints_width        = .4,
                axis                = 'X',
                start_shape         =  1,
                start_resolution    =  0,
                end_shape           = .3,
                end_resolution      =  6,
            )
        finger = Mesh(finger)

        with Layout("Finalize"):
            finger.transform(rotation=(0, lateral, 0))
            finger.transform(translation=(-.3, 0, -.6), rotation=(0, -pi/3, 0))

        finger.out()

    # ====================================================================================================
    # Hand
    # ====================================================================================================

    with GeoNodes("Legacy Hand", is_group=False):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol = Integer(4, "Resolution", 1, 8)
        right_hand = Boolean(False, "Right")

        bend    = [None]*5
        fold    = [None]*5
        lateral = [None]*5

        with Panel("Angles"):
            for i in range(5):
                name = "Thumb" if i == 0 else f"Finger {i}"
                if i == 0:
                    pinch = Float.Angle(0, "Thumb Pinch")
                bend[i] = Float.Angle(0, f"{name} Bend")
                fold[i] = Float.Angle(0, f"{name} Fold")
                lateral[i] = Float.Angle(0, f"{name} Lateral")

        with Panel("Location"):
            use_arm = Boolean(True, "Arm")
            arm_lat = Float.Angle(0, "Arm Lateral", 0, pi)
            arm_fwd = Float.Angle(0, "Arm Forward", -pi/2, pi)

            elbow   = Float.Angle(0, "Elbow", 0, pi)
            twist   = Float.Angle(0, "Twist", -pi/2, pi/2)

        def get_angle(i, name):
            return pinch if name == 'pinch' else {
                'bend': bend, 'fold': fold, 'lateral': lateral,
            }[name][i]

        with Layout("Fingers"):
            hand = None
            lengths = [.6, .9, 1, .9, .8]
            radius  = .11
            room    = .12

            hand = G().obs_mesh_hand_lab_thumb(
                    resolution   = resol,
                    length       = lengths[0],
                    radius       = .17,
                    pinch        = get_angle(0, 'pinch'),
                    bend         = get_angle(0, 'bend'),
                    fold         = get_angle(0, 'fold'),
                    lateral      = get_angle(0, 'lateral'),
                )

            x = -room*3
            for i in range(1, 5):

                finger = G().obs_mesh_hand_lab_finger(
                    resolution   = resol,
                    length       = lengths[i],
                    radius       = radius,
                    bend         = get_angle(i, 'bend'),
                    fold         = get_angle(i, 'fold'),
                    lateral      = get_angle(i, 'lateral'),

                    #bend         = .1 + bend[i],
                    #fold         = .1 + fold[i],
                    #lateral      = lateral[i],
                )

                finger.transform(translation=(x, 0, 0))
                x += 2*room

                hand += finger

            hand.transform(translation=(0, 0, .97))

        with Layout("Palm"):

            n = resol*4 + 2
            half = resol*2

            dx = 3*room
            z = 1

            palm = Mesh.Circle(vertices=n, fill_type='NGON')

            ag = nd.index/half*pi
            palm.points[nd.index <= half].position = (dx + radius*gnmath.sin(ag), -radius*gnmath.cos(ag), z)

            ag = (nd.index - half - 1)/half*pi
            palm.points[nd.index > half].position = (-dx  -radius*gnmath.sin(ag), radius*gnmath.cos(ag), z)

            start = Mesh(palm)

            top = True
            top = palm.faces[top].extrude(offset=(0, 0, -.02), individual=False).top_
            palm.points[top].position *= (1.0, 1.0, 1)

            top = palm.faces[top].extrude(offset=(0, 0, -.5), individual=False).top_
            palm.points[top].position *= (1.01, 1.3, 1)

            top = palm.faces[top].extrude(offset=(0, 0, -.2), individual=False).top_
            palm.points[top].position *= (.9, 1, 1)


            dz = -.07
            f  = .95

            for i in range(4):
                top = palm.faces[top].extrude(offset=(0, 0, dz), individual=True).top_
                s = f**(i+1)
                palm.points[top].position *= (s, 1, 1)

            palm.flip_faces()
            palm += start
            palm.merge_by_distance()
            hand += palm

            hand = Mesh(hand)

            hand.faces.shade_smooth = True
            hand.faces.material = "Obs Hand Lab Skin"

        with Layout("Left Hand"):
            side_fac = Integer.Switch(right_hand, -1, 1)
            hand = hand.switch_false(right_hand, Mesh(hand).transform(scale=(1, -1, 1)).flip_faces())


        with Layout("Location"):

            armed = Mesh(hand)

            armed.transform(rotation=(0, pi, -pi/2 + twist*side_fac), scale=.38)

            armed.transform(translation=(0, 0, -.7))
            armed.transform(rotation=(-elbow, 0, 0))

            armed.transform(translation=(0, 0, -.7))
            armed.transform(rotation=(0, -arm_lat*side_fac, 0))
            armed.transform(rotation=(-arm_fwd, 0, 0))

            hand = hand.switch(use_arm, armed)

        hand.transform(scale=.5)
        hand.out()


# Reference cage dimensions, before the final hand scale.
PALM_TOP = 1.0
PALM_BEND_START = 0.35
PALM_BEND_MAX_DEGREES = (0.0, 3.0, 6.0, 10.0)
FINGER_LENGTHS = (0.9, 1.0, 0.9, 0.75)
# Match the shared base width to the full finger diameter.
DIGIT_THICKNESS = 1.5
FINGER_RADIUS = .11 * DIGIT_THICKNESS
FINGER_CENTERS = tuple(i * FINGER_RADIUS for i in (-3, -1, 1, 3))
# Shared columns keep the webs welded while raising the two central bases.
PALM_TOP_OFFSETS = (0.0, 0.0, 0.12, 0.0, 0.0)
FINGER_BASE_HEIGHTS = tuple(
    PALM_TOP + (PALM_TOP_OFFSETS[i] + PALM_TOP_OFFSETS[i+1]) / 2
    for i in range(4)
)
THUMB_GIRTH = 1.35
# Roll the thumb's flexion plane toward the fingers, while retaining forward motion.
THUMB_FLEXION_ROLL = 60 * pi / 180
# Rounded palm silhouette: broad sides and a lowered, curved heel.
PALM_WIDTH_PROFILE = (.80, .92, .98, 1.0, 1.0, 1.0)
PALM_HEEL_DEPTH = .20


def _build_cage():
    """Build a closed, indexed surface. Junctions reuse vertex indices."""
    import math
    from mathutils import Vector as V
    vertices, faces, weights = [], [], []
    indices = {}
    xs = (-0.48, -0.24, 0.0, 0.24, 0.48)
    ys = (-0.14, 0.0, 0.14)
    zs = (0.0, 0.18, 0.36, 0.60, 0.80, PALM_TOP)

    def vertex(key):
        if key not in indices:
            i, j, k = key
            z = zs[k]
            # Widen the actual thumb opening, including its shared palm vertices.
            if i == 0 and k in (2, 3):
                z += -0.09 if k == 2 else 0.09
            thickness = 0.85 + 0.15 * math.sin(z * math.pi)
            indices[key] = len(vertices)
            top_influence = max(0.0, (z - 0.6) / (PALM_TOP - 0.6))
            # Keep broad sides below the knuckles instead of a funnel-shaped wrist.
            upper = max(0.0, min(1.0, (z - .35) / .45))
            upper = upper*upper*(3.0-2.0*upper)
            x_scale = FINGER_RADIUS/.12 * PALM_WIDTH_PROFILE[k]
            y_scale = 1.0 + ((.12*DIGIT_THICKNESS)/(.14*thickness) - 1.0)*upper
            if k == 0:
                # Curve the bottom contour upward at the sides, not a flat cap.
                z = -PALM_HEEL_DEPTH + .18*(xs[i]/.48)**2
            vertices.append((xs[i] * x_scale, ys[j] * thickness * y_scale,
                             z + PALM_TOP_OFFSETS[i] * top_influence))
            # Smoothly distribute palm motion between neighboring metacarpals.
            finger_weights = [math.exp(-((xs[i] * x_scale - x) / (.18*x_scale))**2) for x in FINGER_CENTERS]
            total = sum(finger_weights)
            weights.append([0.0] + [w / total for w in finger_weights])
        return indices[key]

    # Four sides of the palm; the thumb replaces two side faces.
    for k in range(len(zs)-1):
        for i in range(4):
            faces.append([vertex((i,0,k)),vertex((i+1,0,k)),vertex((i+1,0,k+1)),vertex((i,0,k+1))])
            faces.append([vertex((i,2,k+1)),vertex((i+1,2,k+1)),vertex((i+1,2,k)),vertex((i,2,k))])
        for j in range(2):
            if k != 2:
                faces.append([vertex((0,j,k+1)),vertex((0,j+1,k+1)),vertex((0,j+1,k)),vertex((0,j,k))])
            faces.append([vertex((4,j,k)),vertex((4,j+1,k)),vertex((4,j+1,k+1)),vertex((4,j,k+1))])
    for i in range(4):
        for j in range(2):
            faces.append([vertex((i,j+1,0)),vertex((i+1,j+1,0)),vertex((i+1,j,0)),vertex((i,j,0))])

    def extrude_digit(root, digit, direction, length):
        center = sum((V(vertices[i]) for i in root), V()) / len(root)
        raw_offsets = [V(vertices[i]) - center for i in root]
        # Sections perpendicular to the skeleton: palm slopes stop at the base.
        across = V((.6, 0, .8)) if digit == 0 else V((1, 0, 0))
        depth = V((0, 1, 0))
        radius = (.12 * THUMB_GIRTH if digit == 0 else .11) * DIGIT_THICKNESS
        depth_radius = (.14 * THUMB_GIRTH if digit == 0 else .12) * DIGIT_THICKNESS
        offsets = []
        for offset in raw_offsets:
            angle = math.atan2(offset.dot(depth), offset.dot(across))
            if digit == 0:
                offsets.append(across * (radius * math.cos(angle))
                               + depth * (depth_radius * math.sin(angle)))
            else:
                # Same section from the shared palm contour to the tip cap:
                # subdivision rounds it without a narrow-to-wide transition.
                offsets.append(V((offset.x, offset.y, 0.0)))
        previous = root

        def ring_at(distance, scale, blend=1.0):
            nonlocal previous
            ring = []
            for raw, rounded in zip(raw_offsets, offsets):
                ring.append(len(vertices))
                offset = raw.lerp(rounded, blend) * scale
                vertices.append(tuple(center + direction * distance + offset))
                weights.append([float(i == digit) for i in range(5)])
            for j in range(len(root)):
                n = (j+1) % len(root)
                faces.append([previous[j],previous[n],ring[n],ring[j]])
            previous = ring

        cap_start = length - radius
        # Rings are concentrated on the arcs; straight phalanges need only ends.
        if digit == 0:
            distances = (.06, .21, .265, .32, .375, .43, cap_start)
        else:
            distances = tuple(length*t for t in (
                .06, .12, .18, .21, .27, .33, .39, .45,
                .54, .60, .66, .72, .78)) + (cap_start,)
        for distance in sorted(set(d for d in distances if d <= cap_start)):
            ring_at(distance, 1.0, min(distance / (length*.18), 1.0))
        # A hemispherical cap, ending at one shared pole rather than a flat ngon.
        for angle in (math.pi/6, math.pi/3):
            ring_at(cap_start + radius*math.sin(angle), math.cos(angle))
        tip = len(vertices)
        vertices.append(tuple(center + direction*length))
        weights.append([float(i == digit) for i in range(5)])
        for j in range(len(root)):
            faces.append([previous[j], previous[(j+1) % len(root)], tip])

    # Adjacent digit bases share the whole two-edge web, not coincident copies.
    for i, length in enumerate(FINGER_LENGTHS):
        root = [vertex((i,0,5)),vertex((i+1,0,5)),vertex((i+1,1,5)),
                vertex((i+1,2,5)),vertex((i,2,5)),vertex((i,1,5))]
        extrude_digit(root, i+1, V((0,0,1)), length)

    thumb_root = [vertex((0,0,3)),vertex((0,1,3)),vertex((0,2,3)),
                  vertex((0,2,2)),vertex((0,1,2)),vertex((0,0,2))]
    for i in thumb_root:
        weights[i] = [0.7] + [w*.3 for w in weights[i][1:]]
    extrude_digit(thumb_root, 0, V((-.8,0,.6)), .65)

    # Spread metacarpal influence through the thumb-side palm, not just its rim.
    def smooth(value):
        value = max(0.0, min(1.0, value))
        return value*value*(3.0-2.0*value)

    palm_vertices = set(indices.values())
    for index in palm_vertices:
        x, y, z = vertices[index]
        influence = .85 * smooth((-x-.08)/.45) * (1.0-smooth((z-.60)/.30))
        influence = max(weights[index][0], influence)
        others = sum(weights[index][1:])
        weights[index] = [influence] + [w*(1.0-influence)/others for w in weights[index][1:]]

    name = 'Obs Hand Lab Cage'
    obj = bpy.data.objects.get(name)
    if obj is None:
        obj = bpy.data.objects.new(name, bpy.data.meshes.new(name))
        # The object is a data source only: it is not linked into the scene.
    mesh = obj.data
    obj['thumb_root'] = tuple(sum((V(vertices[i]) for i in thumb_root), V()) / len(thumb_root))
    mesh.clear_geometry()
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    # Orient all faces consistently, including the wrist cap.
    import bmesh
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
    assert all(e.is_manifold for e in bm.edges), 'Hand cage must be closed and manifold'
    bm.to_mesh(mesh)
    bm.free()
    palm_attribute = mesh.attributes.get('Hand Lab Palm') or mesh.attributes.new('Hand Lab Palm', 'FLOAT', 'POINT')
    palm_attribute.data.foreach_set('value', [float(i in palm_vertices) for i in range(len(vertices))])
    for digit in range(5):
        name = f'Hand Lab Weight {digit}'
        attribute = mesh.attributes.get(name) or mesh.attributes.new(name, 'FLOAT', 'POINT')
        attribute.data.foreach_set('value', [w[digit] for w in weights])
    return obj


def build_hand():
    """Build a continuous hand cage, then deform and smooth that single mesh."""
    source = _build_cage()
    if bpy.data.materials.get('Obs Hand Lab Skin') is None:
        with ShaderNodes('Obs Hand Lab Skin'):
            Shader.Principled(base_color=(.65,.52,.41,1), roughness=.9).out()

    def sweep(distance, joints):
        """Integrate straight segments and constant-curvature joint arcs.

        Return the skeleton center and tangent angle at the ring abscissa.
        Section vertices are placed around that frame, never rigidly folded.
        """
        center = Vector((0, 0, distance.min(0.0)))
        heading = Float(0.0)
        tangent = Float(0.0)
        previous = 0.0
        for start, end, angle in joints:
            straight = (distance - previous).clamp(0.0, start - previous)
            center = center + Rotation.FromEuler((heading,0,0)) @ Vector((0,0,straight))
            width = end - start
            travel = (distance - start).clamp(0.0, width)
            turn = angle * (travel / width)
            zero = angle.abs() < 0.00001
            denominator = Float(angle).switch(zero, 1.0)
            arc = Vector((0, (turn.cos()-1.0)*width/denominator,
                          turn.sin()*width/denominator))
            arc = arc.switch(zero, Vector((0,0,travel)))
            center = center + Rotation.FromEuler((heading,0,0)) @ arc
            tangent = tangent + turn
            heading = heading + angle
            previous = end
        tail = (distance - previous).max(0.0)
        center = center + Rotation.FromEuler((heading,0,0)) @ Vector((0,0,tail))
        return center, tangent

    with GeoNodes('Hand Lab', is_group=False):
        resolution = Integer(2, 'Resolution', 0, 3)
        right = Boolean(False, 'Right')
        angles = []
        for i in range(5):
            name = 'Thumb' if i == 0 else f'Finger {i}'
            with Panel(name):
                bend = Float.Angle(0, name + ' Bend')
                fold = Float.Angle(0, name + ' Fold')
                lateral = Float.Angle(0, name + ' Lateral')
                if i == 0:
                    pinch = Float.Angle(0, 'Thumb Pinch')
                angles.append((bend, fold, lateral))

        with Layout('Continuous Cage'):
            hand = Mesh(Object(source).info().geometry)
            position = nd.position
            displacement = Vector((0,0,0))

        for i, (bend, fold, lateral) in enumerate(angles):
            with Layout('Thumb' if i == 0 else f'Finger {i}'):
                if i == 0:
                    pivot = Vector(tuple(source['thumb_root']))
                    local = position - pivot
                    # Thumb axis is tilted outward by atan2(-.8, .6).
                    local = Rotation.FromEuler((0, .927295218, 0)) @ local
                    center, tangent = sweep(local.z, ((.21, .43, fold),))
                    local = center + Rotation.FromEuler((tangent,0,0)) @ Vector((local.x,local.y,0))
                    local = Rotation.FromEuler((bend, lateral, pinch)) @ local
                    moved = Rotation.FromEuler((0,-.927295218,0)) @ local + pivot
                else:
                    length = FINGER_LENGTHS[i-1]
                    base_height = FINGER_BASE_HEIGHTS[i-1]
                    pivot = Vector((FINGER_CENTERS[i-1],0,base_height))
                    local = position - pivot
                    center, tangent = sweep(local.z, (
                        (0.0, length*.18, bend),
                        (length*.21, length*.45, fold),
                        (length*.54, length*.78, fold),
                    ))
                    section = Rotation.FromEuler((tangent,0,0)) @ Vector((local.x,local.y,0))
                    moved = center + section
                    lateral_influence = local.z.map_range(0.0, length*.18)
                    moved = Rotation.FromEuler((0,lateral*lateral_influence,0)) @ moved + pivot

                    # A separate, capped palm bend carries the whole finger.
                    # Preserve the sign: +/-30 degrees reaches the palm limit.
                    palm_angle = (bend / (pi/6)).clamp(-1.0, 1.0) * (
                        PALM_BEND_MAX_DEGREES[i-1] * pi/180)
                    influence = position.z.map_range_smooth_step(PALM_BEND_START, base_height)
                    pivot = Vector((FINGER_CENTERS[i-1],0,PALM_BEND_START))
                    moved = Rotation.FromEuler((palm_angle*influence,0,0)) @ (moved-pivot) + pivot
                displacement = displacement + (moved-position) * Float(f'Hand Lab Weight {i}')

        with Layout('Surface'):
            hand.points.position = position + displacement
            hand = hand.subdivision_surface(level=resolution)
            hand.faces.shade_smooth = True
            hand.faces.material = 'Obs Hand Lab Skin'
            mirrored = Mesh(hand).transform(scale=(-1,1,1)).flip_faces()
            hand = hand.switch(right, mirrored)
            hand.transform(scale=.5)
            hand.out()




def demo_old():
    """Build the standalone continuous hand preview."""
    from . import meshutil
    meshutil.demo()
    #build_hand()
    if bpy.data.node_groups.get('Hand Lab') is not None:
        with GeoNodes('Obs Hand Lab'):
            G().hand_lab().link_inputs().out()


    # ----------------------------------------------------------------------------------------------------
    # Arc between two segments
    # ----------------------------------------------------------------------------------------------------

        
    # ----------------------------------------------------------------------------------------------------
    # Finger Backbone
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Finger", is_group=False):

        FULL0 = True
        
        #is_thumb = Boolean(False, "Thumb")
        
        joint_resol = Integer(3, "Resolution", 0, 10)
        joint_len = Float.Distance(0.003, "Joint Length", 0, 0.01)
        
        angle_0 = Float.Angle(0, "Angle 0")
        angle_1 = Float.Angle(0, "Angle 1")
        angle_2 = Float.Angle(0, "Angle 2")
        
        l1 = Float.Distance(0.015, "Length 1", 0.001, 0.03)
        l2 = Float.Distance(0.015, "Length 2", 0.001, 0.03)
        l3 = Float.Distance(0.015, "Length 3", 0.001, 0.03)

        radius_0 = Float.Distance(0.004, "Radius 0", 0.001, 0.02)
        radius_1 = Float.Distance(0.004, "Radius 1", 0.001, 0.02)
        radius_2 = Float.Distance(0.004, "Radius 2", 0.001, 0.02)
        radius_3 = Float.Distance(0.004, "Radius 3", 0.001, 0.02)
        
        with Panel("Mesh"):
            use_mesh = Boolean(True, "Mesh")
            mesh_resol = Integer(12, "Resolution", 6, 32)

        def corner_length(angle, max_trim):
            magnitude = angle.abs().min(pi-.001)
            tangent = (magnitude/2).tan().max(.00001)
            maximum = (max_trim*magnitude/tangent).switch(magnitude < .00001, 2*max_trim)
            return joint_len.max(0.0).min(maximum)

        with Layout("Base Line"):

            # 4 base points + joint_resol before and after the 3 joints
            if FULL0:
                # First joint is full
                total = 4 + 6*joint_resol
            else:
                # First joint is half a joint
                total = 4 + 5*joint_resol

            bb = Curve.Line().resample(count=total)
            
            pos1 = Rotation((0, angle_0, 0)) @ Vector((0, 0, l1))
            pos2 = pos1 + Rotation((0, angle_0 + angle_1, 0)) @ Vector((0, 0, l2))
            pos3 = pos2 + Rotation((0, angle_0 + angle_1 + angle_2, 0)) @ Vector((0, 0, l3))
        
        start_index = 0
        nindices = 2*joint_resol + 1
        
        with Layout("First Segment"):

            arc = G().rounded_joint(position=0.0, start_angle=0.0, angle=angle_0, resol=nindices, length=corner_length(angle_0, l1*.45))
            if FULL0:
                sel = nd.index < nindices
                arc_index = nd.index
            else:
                sel = nd.index < joint_resol + 1
                arc_index = nd.index + joint_resol
            bb.points[sel].position = arc.points.sample_index(nd.position, index=arc_index)
            bb.points[sel].radius = radius_0
            
            if FULL0:
                start_index += nindices
            else:
                start_index += joint_resol + 1

        with Layout("Second Segment"):
            
            arc = G().rounded_joint(position=pos1, start_angle=angle_0, angle=angle_1, resol=nindices, length=corner_length(angle_1, l1.min(l2)*.45))
            sel = (nd.index >= start_index) & (nd.index < start_index + nindices)
            bb.points[sel].position = arc.points.sample_index(nd.position, index=nd.index - start_index)
            bb.points[sel].radius = radius_1
            
            start_index += nindices
            
            
        with Layout("Third Segment & last points"):
            
            arc = G().rounded_joint(position=pos2, start_angle=angle_0 + angle_1, angle=angle_2, resol=nindices, length=corner_length(angle_2, l2.min(l3)*.45))
            sel = (nd.index >= start_index) & (nd.index < start_index + nindices)
            bb.points[sel].position = arc.points.sample_index(nd.position, index=nd.index - start_index)
            bb.points[sel].radius = radius_2
            
            #start_index += nindices
            sel = nd.index == total - 1
            bb.points[sel].position = pos3
            bb.points[sel].radius = radius_3
            
        with Layout("To Mesh"):
            # A fixed frame in the XZ bending plane keeps the same profile
            # indexing at every ring, including when the base angle changes.
            tangent = nd.curve_tangent
            bb.set_normal(mode='Free', normal=Vector((tangent.z, 0, -tangent.x)))
            c = Curve.Circle(radius=1.0, resolution=mesh_resol)    
            mesh = bb.to_mesh(profile_curve=c, scale=nd.radius)
            
        with Layout("Dome at the end"):        
            dome_rings = gnmath.max(mesh_resol//2, 4)
            dome = Mesh.UVSphere(radius=radius_3, segments=mesh_resol, rings=2*dome_rings)
            dome.points[nd.position.z < -0.0000001].delete()

        with Layout("Place the dome at the end plus exact base circle"):        
            rot = Rotation((0, angle_0 + angle_1 + angle_2, 0))
            dome.transform(rotation=rot, translation=pos3)
            # Keep the swept ring: replacing its vertices by index used to
            # rotate that ring independently and twist the last phalanx.
            mesh += dome
            mesh.merge_by_distance(distance=0.000001)
            mesh.faces.shade_smooth=True
                
        Geometry.Switch(use_mesh, bb, mesh).out()

    # ====================================================================================================
    # Buid a closed shape arround a bone
    # ====================================================================================================

        
    # ====================================================================================================
    # Build a cage around bones
    # ====================================================================================================

        
        
                
            
            
                
                
                    
            

    # ----------------------------------------------------------------------------------------------------
    # Continuous palm driven by the validated Finger backbones
    # ----------------------------------------------------------------------------------------------------
    source = _build_cage()
    if bpy.data.materials.get('Obs Hand Lab Skin') is None:
        with ShaderNodes('Obs Hand Lab Skin'):
            Shader.Principled(base_color=(.65,.52,.41,1), roughness=.9).out()

    with GeoNodes('New Hand'):
        resolution = Integer(3, 'Joint Resolution', 1, 10)
        surface_resolution = Integer(2, 'Surface Resolution', 0, 3)
        joint_length = Float.Distance(.008, 'Joint Length', .0001, .02)
        right = Boolean(False, 'Right')
        angles = []
        for i in range(5):
            name = 'Thumb' if i == 0 else f'Finger {i}'
            with Panel(name):
                if i == 0:
                    pinch = Float.Angle(0, 'Pinch')
                bend = Float.Angle(0, 'Bend')
                fold = Float.Angle(0, 'Fold')
                lateral = Float.Angle(0, 'Lateral')
                angles.append((bend, fold, lateral))

        # Finger uses meters; the cage retains the hand workshop's reference units.
        unit = .04
        with Layout('Shared Palm and Finger Sections'):
            hand = Mesh(Object(source).info().geometry)
            position = nd.position
            displacement = Vector((0,0,0))

        for i, (bend, fold, lateral) in enumerate(angles):
            with Layout('Thumb Backbone' if i == 0 else f'Finger {i} Backbone'):
                if i == 0:
                    root = Vector(tuple(source['thumb_root']))
                    rest_rotation = Rotation((0,-.927295218,0))
                    local = rest_rotation.invert() @ (position-root)
                    length = .65
                    radius = .12*THUMB_GIRTH*DIGIT_THICKNESS
                    first_length = .015
                    # The visible root is the end of the first (palmar) bone.
                    metacarpal_root = root - rest_rotation @ Vector((0,0,first_length/unit))
                    phalanx_length = (length-radius)*unit/2
                    backbone = G().finger(
                        resolution=resolution, joint_length=joint_length,
                        angle_0=pinch+bend, angle_1=0.0, angle_2=fold,
                        length_1=first_length, length_2=phalanx_length,
                        length_3=phalanx_length,
                    ).node
                    backbone['Mesh > Mesh'] = False
                    curve = Curve(backbone._out)
                    # The first segment is a metacarpal, not a visible tube.
                    start_factor = curve.points.sample_index(
                        nd.spline_parameter().factor, index=2*resolution+1)
                    baseline = Vector((0,0,first_length))
                else:
                    length = FINGER_LENGTHS[i-1]
                    radius = FINGER_RADIUS
                    root = Vector((FINGER_CENTERS[i-1],0,FINGER_BASE_HEIGHTS[i-1]))
                    rest_rotation = Rotation((0,0,0))
                    local = position-root
                    segment_length = (length-radius)*unit/3
                    backbone = G().finger(
                        resolution=resolution, joint_length=joint_length,
                        angle_0=bend, angle_1=fold, angle_2=fold,
                        length_1=segment_length, length_2=segment_length,
                        length_3=segment_length,
                    ).node
                    backbone['Mesh > Mesh'] = False
                    curve = Curve(backbone._out)
                    start_factor = Float(0.0)
                    baseline = Vector((0,0,0))

            with Layout('Thumb Surface' if i == 0 else f'Finger {i} Surface'):
                shaft_length = length-radius
                along = (local.z/shaft_length).clamp(0.0,1.0)
                factor = start_factor + (1.0-start_factor)*along
                sample = curve.sample_factor(factor=factor)
                center = (sample.position_-baseline)/unit
                # Finger bends in XZ; the hand's fingers bend in YZ.
                frame_angle = gnmath.atan2(sample.tangent_.x, sample.tangent_.z)
                center = Vector((0,-center.x,center.z))
                section = Vector((local.x,local.y,(local.z-shaft_length).max(0.0)))
                if i == 0:
                    flexion_plane = Rotation((0,0,THUMB_FLEXION_ROLL))
                    # Change the bending plane, not the resting cross-section.
                    moved = flexion_plane @ (center + Rotation((frame_angle,0,0)) @ (flexion_plane.invert() @ section))
                    center = flexion_plane @ center
                else:
                    moved = center + Rotation((frame_angle,0,0)) @ section
                # Keep the lower palm and wrist intact, blend toward the sampled base.
                lower = Vector((local.x,local.y,local.z)) + center
                moved = moved.switch(local.z < 0, lower)
                moved = rest_rotation @ moved + root

                if i != 0:
                    palm_angle = (bend/(pi/6)).clamp(-1.,1.) * (PALM_BEND_MAX_DEGREES[i-1]*pi/180)
                    influence = position.z.map_range_smooth_step(PALM_BEND_START,FINGER_BASE_HEIGHTS[i-1])
                    pivot = Vector((FINGER_CENTERS[i-1],0,PALM_BEND_START))
                    moved = Rotation((palm_angle*influence,lateral*influence,0)) @ (moved-pivot)+pivot
                    # Sampling the full first arc must not translate the wrist.
                    moved = Vector(position).mix(moved,factor=influence)
                else:
                    # Bend now acts on the intrapalmar bone, alongside Pinch.
                    palm_local = rest_rotation.invert() @ (position-metacarpal_root)
                    palm_moved = rest_rotation @ (flexion_plane @ (Rotation((pinch+bend,0,0)) @ (flexion_plane.invert() @ palm_local))) + metacarpal_root
                    moved = moved.switch(Float('Hand Lab Palm') > .5, palm_moved)
                    # Rotate the complete skeleton at angle 0, inside the palm,
                    # rather than at angle 1, where the visible thumb starts.
                    moved = Rotation((0,lateral,0)) @ (moved-metacarpal_root)+metacarpal_root
                displacement = displacement + (moved-position)*Float(f'Hand Lab Weight {i}')

        with Layout('Continuous Surface'):
            hand.points.position = position+displacement
            hand.subdivision_surface(level=surface_resolution)
            hand.faces.shade_smooth = True
            hand.faces.material = 'Obs Hand Lab Skin'
            mirrored = Mesh(hand).transform(scale=(-1,1,1)).flip_faces()
            hand = hand.switch(right,mirrored)
            hand.transform(scale=.5)
            hand.out()

    build_hand_bones()


def build_hand_bones():
    """Build only the skeleton and export each future cage's ordered polylines."""
    with GeoNodes('Hand Bones'):
        right = Boolean(False, 'Right')
        with Panel('Structure'):
            metacarpal_split = Float.Factor(.55, 'Palm Split', .1, .9,
                tip='Fraction of each metacarpal assigned to the lower cage.')
            phalanx_split = Float.Factor(.20, 'Finger Base', .01, .8,
                tip='Fraction of the first phalanx retained in the upper cage.')
        with Panel('Display'):
            radius = Float(.008, 'Bone Radius', .0001, .05)
            show_lower = Boolean(True, 'Lower Cage')
            show_upper = Boolean(True, 'Upper Cage')
            show_fingers = Boolean(True, 'Fingers')
            show_thumb = Boolean(True, 'Thumb')
        controls = []
        for i in range(5):
            with Panel('Thumb' if i == 0 else f'Finger {i}'):
                bend = Float.Angle(0, 'Bend')
                fold = Float.Angle(0, 'Fold')
                lateral = Float.Angle(0, 'Lateral')
                if i == 0:
                    pinch = Float.Angle(0, 'Pinch')
                controls.append((bend, fold, lateral))

        def polyline(points):
            curve = Curve.Line().resample(count=len(points))
            for index, point in enumerate(points):
                curve.points[nd.index == index].position = point
            return curve

        lower_curves, upper_curves, fingers = [], [], []
        origin = Vector((0,0,-PALM_HEEL_DEPTH))
        for i in range(4):
            with Layout(f'Finger {i+1} Bones'):
                bend, fold, lateral = controls[i+1]
                x = FINGER_CENTERS[i]
                heel = Vector((x*.6,0,-.12))
                anchor = Vector((x*.85,0,.05))
                rest_meta = Vector((x*.15,0,FINGER_BASE_HEIGHTS[i]-.05))
                palm_bend = (bend/(pi/6)).clamp(-1.,1.) * (PALM_BEND_MAX_DEGREES[i]*pi/180)
                palm_rotation = Rotation((palm_bend,lateral,0))
                metacarpal = palm_rotation @ rest_meta
                knuckle = anchor + metacarpal
                split = anchor + metacarpal*metacarpal_split

                # Orient the first phalanx relative to its own metacarpal.
                rest_heading = Rotation().align_z_to_vector(rest_meta)
                length = FINGER_LENGTHS[i]
                first_rotation = palm_rotation @ rest_heading @ Rotation((bend,0,0))
                first = first_rotation @ Vector((0,0,length*.33))
                finger_base = knuckle + first*phalanx_split
                joint1 = knuckle + first
                second_rotation = first_rotation @ Rotation((fold,0,0))
                joint2 = joint1 + second_rotation @ Vector((0,0,length*.33))
                third_rotation = second_rotation @ Rotation((fold,0,0))
                tip = joint2 + third_rotation @ Vector((0,0,length*.34))

                # Two heel edges, then the first portion of the metacarpal.
                lower_curves.append(polyline((origin,heel,anchor,split)))
                upper_curves.append(polyline((split,knuckle,finger_base)))
                fingers.append(polyline((finger_base,joint1,joint2,tip)))

        with Layout('Thumb Bones'):
            bend, fold, lateral = controls[0]
            heel = Vector((-.28,0,-.12))
            anchor = Vector((-.24,0,.10))
            plane = Rotation((0,0,THUMB_FLEXION_ROLL))
            rotation = Rotation((0,-.927295218+lateral,0)) @ plane @ Rotation((pinch+bend,0,0)) @ plane.invert()
            joint1 = anchor + rotation @ Vector((0,0,.50))
            joint2 = joint1 + rotation @ Vector((0,0,.32))
            distal_rotation = rotation @ plane @ Rotation((fold,0,0)) @ plane.invert()
            tip = joint2 + distal_rotation @ Vector((0,0,.33))
            thumb_lower = polyline((origin,heel,anchor,joint1))
            thumb = polyline((joint1,joint2,tip))

        with Layout('Ordered Cage Sections'):
            # Thumb first, followed by index through little finger: no crossing.
            def ordered(curves):
                for index, curve in enumerate(curves):
                    curve.splines._BoneOrder = Float(index)
                joined = Curve(Geometry.Join(*curves))
                joined.splines.sort(sort_weight=Float('BoneOrder'))
                return joined

            lower = ordered([thumb_lower, *lower_curves])
            upper = ordered(upper_curves)
            finger_curves = ordered(fingers)

            sections = {'Lower Cage': lower, 'Upper Cage': upper,
                        'Fingers': finger_curves, 'Thumb': thumb}
            for name, curve in sections.items():
                # Mirror all sections identically, preserving exact shared endpoints.
                scale_x = Float.Switch(right, 1.0, -1.0)
                curve.transform(scale=(scale_x*.5,.5,.5))

        with Layout('Bone Display'):
            visible = None
            for name, enabled in (('Lower Cage',show_lower),('Upper Cage',show_upper),
                                  ('Fingers',show_fingers),('Thumb',show_thumb)):
                curve = sections[name]
                tube = curve.to_mesh(profile_curve=Curve.Circle(radius=radius,resolution=8))
                tube.faces[enabled == False].delete()
                visible = tube if visible is None else visible + tube
            visible.out('Geometry')

        # Raw polylines for Cage Around, unaffected by visibility toggles.
        for name, curve in sections.items():
            curve.out(name)
