"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demo arrows
--------------------

Building arrows

updates
-------
- creation : 2025/05/29

$ DOC START

[Source Code](../demos/observe.py)

This demo provides a modifier which crates an animated Observer

> [!NOTE]
> Modifiers:
> - Observer

``` python
from geonodes.demos import observer

observer.demo()
```
"""

from geonodes import *

def demo():

    # =============================================================================================================================
    # Shader

    with ShaderNodes("Obs Skin"):

        color  = [0.650011, 0.523698, 0.411225, 1.000000]
        transp = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.Principled(
            base_color = color,
            roughness  = .9,
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)
        shader.out()

    with ShaderNodes("Obs Eye"):
        white = snd.attribute(attribute_type='GEOMETRY', attribute_name="White").factor
        color = Color((0, 0, 0)).mix(white, Color((1, 1, 1)))
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.Principled(
            base_color = color,
            roughness  = 0,
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)

        shader.out()

    with ShaderNodes("Obs Hair"):

        color   = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.PrincipledHair(
            color = color,
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)

        shader.out()

    with ShaderNodes("Obs Blouse"):

        color   = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.Principled(
            base_color = color,
            roughness  = .8,
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)

        shader.out()

    with ShaderNodes("Obs Shoe"):

        color   = [0.000000, 0.000000, 0.000000, 1.000000]
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").factor

        ped = Shader.Principled(
            base_color = color,
            roughness  = .3,
        )

        shader = ped.mix(Shader.Transparent(), factor=transp)

        shader.out()

    # ====================================================================================================
    # Key function
    # ====================================================================================================

    def key_function(param, *keys):

        curve = [tuple(k) for k in keys]
        if [curve[0][0]] != 0:
            curve.insert(0, (0, curve[0][0]))
        if [curve[-1][0]] != 1:
            curve.append((1, curve[-1][0]))

        return param.curve(factor = None, curve=curve)
    
    # ====================================================================================================
    # ====================================================================================================
    # =============================================================================================================================
    # Hair and Moustache
    # ====================================================================================================
    # ====================================================================================================

    # ====================================================================================================
    # Hair scalp
    # ====================================================================================================

    with GeoNodes("Hair Scalp", is_group=True):

        mesh     = Mesh()
        top_z    = Float(.75, "Top")
        back_z   = Float(.1, "Back")
        rot      = Vector.Euler((0, pi/4, 0), "Rotation")

        x, y, z = nd.position.xyz

        mesh.points._Yes = x < .1

        mesh.transform(rotation=rot)
        mesh.points._BScalp = (z >= back_z) & Boolean("Yes")
        mesh.transform(rotation=rot.scale(-1))

        mesh.points._BScalp = Boolean("BScalp") | (z >= top_z)

        mesh.points._Hair_Scalp = Float(Boolean("BScalp"))
        mesh.remove_named_attribute(name="BScalp")

        mesh.out()
        Float("Hair Scalp").out("Hair Scalp")

    # ====================================================================================================
    # Moustache scalp
    # ====================================================================================================

    with GeoNodes("Moustache Scalp", is_group=True):

        mesh     = Mesh()
        top_z    = Float( -.3, "Top")
        bot_z    = Float( -.6, "Bottom")
        width    = Float( 1.1, "Width")

        x, y, z = nd.position.xyz

        scalp = (z <= top_z) & (z >= bot_z) & (x > 0) & (gnmath.abs(y) < width/2)
        mesh.points._Moustache_Scalp = scalp

        mesh.out()
        Float("Moustache Scalp").out("Moustache Scalp")

    # ====================================================================================================
    # Hair
    # ====================================================================================================

    with GeoNodes("Hair", is_group=True):

        mesh = Mesh()
        scalp = Float.Factor(1, "Scalp", 0, 1)

        with Panel("Hair"):
            color   = Color((0.439239, 0.078419, 0.007497, 1.000000), "Color")
            length  = Float(.4, "Length")
            curl    = Float.Factor(0, "Curl", 0, 1)
            radius  = Float(.01, "Radius", 0, .1)
            density = Float(50_000., "Density")

        with Layout("Generate"):

            count = curl.map_range(to_min=6, to_max=12).to_integer()

            hair_node = G().generate_hair_curves(
                    surface         = mesh,
                    hair_length     = length,
                    control_points  = count,
                    density         = density,
                    density_mask    = scalp,
                    viewport_amount = .1,
                    ).node

        with Layout("To Mesh"):
            hair = hair_node.curves

            hair = G().set_hair_curve_profile(
                hair,
                replace_radius = True,
                radius     = radius,
                shape      = .5,
                factor_min = .1,
                factor_max = 1,
            )
            hair = Curve(hair)

            hair = hair.to_mesh(profile_curve=Curve.Circle(resolution=6, radius=1), scale=nd.radius, fill_caps=True)

            hair.faces.Color = color
            hair.faces.material = "Obs Hair"

        (mesh + hair).out()

    # ====================================================================================================
    # ====================================================================================================
    # Observer modifiers
    # ====================================================================================================
    # ====================================================================================================

    # ====================================================================================================
    # Articulated sausage
    # ====================================================================================================

    with GeoNodes("Sausage", is_group=True):

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

    with GeoNodes("Finger", is_group=True):

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

            finger = G().sausage(
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

    with GeoNodes("Thumb", is_group=True):

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

            finger = G().sausage(
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

    with GeoNodes("Hand", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol = Integer(4, "Resolution", 1, 8)
        right_hand = Boolean(False, "Right")

        bend    = [None]*5
        fold    = [None]*5
        lateral = [None]*5

        with Panel("Angles"):
            for i in range(5):
                name = "Thumb" if i == 0 else f"Finger {i}"
                with Panel(name):
                    if i == 0:
                        pinch = Float.Angle(0, "Pinch", 0, pi/2)
                    bend[i]    = Float.Angle(0, "Bend", 0, pi/2)
                    fold[i]    = Float.Angle(0, "Fold", 0, pi/2)
                    ag = pi/2 if i == 0 else pi/8
                    lateral[i] = Float.Angle(0, "Lateral", -ag, ag)

        with Panel("Location"):
            use_arm = Boolean(True, "Arm")
            arm_lat = Float.Angle(0, "Arm Lateral", 0, pi)
            arm_fwd = Float.Angle(0, "Arm Forward", -pi/2, pi)

            elbow   = Float.Angle(0, "Elbow", 0, pi)
            twist   = Float.Angle(0, "Twist", -pi/2, pi/2)

            walk    = Float.Factor(0, "Walk", 0, 1)
            speed   = Float.Factor(0, "Speed",0, 1)

        with Panel("Hand Shape"):
            use_shape = Boolean(True, "Shape")
            shape0 = Integer(0, "From")
            shape1 = Integer(1, "To")
            fing_fac = Float.Factor(0, "Factor", 0, 1)


        r = lambda deg: np.radians(deg)

        angles = [
            # Shape 0
            [{'bend': r(  6), 'fold': r(  6), 'lateral': r(  6), 'pinch': r( 15)},
             {'bend': r(  6), 'fold': r(  6), 'lateral': r(  0)},
             {'bend': r(  6), 'fold': r(  6), 'lateral': r(  0)},
             {'bend': r(  6), 'fold': r(  6), 'lateral': r(  0)},
             {'bend': r(  6), 'fold': r(  6), 'lateral': r(  0)},],

            # Shape 1 (Fist)
            [{'bend': r( 43), 'fold': r( 44), 'lateral': r(-90), 'pinch': r( 77)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},],

            # Shape 2 (Show)
            [{'bend': r( 41), 'fold': r( 17), 'lateral': r( 17), 'pinch': r( 15)},
             {'bend': r(  0), 'fold': r(  0), 'lateral': r(  0)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},
             {'bend': r( 80), 'fold': r( 70), 'lateral': r(  0)},],

            # Shape 2 (Five)
            [{'bend': r(  0), 'fold': r(  0), 'lateral': r(  0), 'pinch': r( 15)},
             {'bend': r(  0), 'fold': r(  0), 'lateral': r(-14)},
             {'bend': r(  0), 'fold': r(  0), 'lateral': r(  0)},
             {'bend': r(  0), 'fold': r(  0), 'lateral': r(  7)},
             {'bend': r(  0), 'fold': r(  0), 'lateral': r( 18)},],

        ]

        def get_angle(i, name):
            with Layout(f"Angle {name}, finger {i}"):
                with Float.IndexSwitch(index=shape0) as ag0:
                    Float(angles[0][i][name]).out()
                    Float(angles[1][i][name]).out()
                    Float(angles[2][i][name]).out()
                    Float(angles[3][i][name]).out()

                with Float.IndexSwitch(index=shape1) as ag1:
                    Float(angles[0][i][name]).out()
                    Float(angles[1][i][name]).out()
                    Float(angles[2][i][name]).out()
                    Float(angles[3][i][name]).out()

                if name == 'pinch':
                    ag = pinch
                else:
                    ag = {'bend': bend, 'fold': fold, 'lateral': lateral}[name][i]

                return ag.switch(use_shape, fing_fac.map_range(to_min=ag0, to_max=ag1))

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Fingers"):
            hand = None
            lengths = [.6, .9, 1, .9, .8]
            radius  = .11
            room    = .12

            hand = G().thumb(
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

                finger = G().finger(
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
            hand.faces.material = "Obs Skin"

        with Layout("Left Hand"):
            side_fac = Integer.Switch(right_hand, -1, 1)
            hand = hand.switch_false(right_hand, Mesh(hand).transform(scale=(1, -1, 1)).flip_faces())


        with Layout("Walk"):
            walk_fwd_max = key_function(speed, (0, .4), (1, .6))
            walk_fwd = walk_fwd_max*gnmath.sin(walk*(pi*2))

            walk_elbow = key_function(speed, (0, 0), (1, .8))


        with Layout("Location"):

            armed = Mesh(hand)

            armed.transform(rotation=(0, pi, -pi/2 + twist*side_fac), scale=.38)

            armed.transform(translation=(0, 0, -.7))
            armed.transform(rotation=(-elbow - walk_elbow, 0, 0))

            armed.transform(translation=(0, 0, -.7))
            armed.transform(rotation=(0, -arm_lat*side_fac, 0))
            armed.transform(rotation=(-arm_fwd + walk_fwd, 0, 0))

            hand = hand.switch(use_arm, armed)

        hand.out()

    # ====================================================================================================
    # Walk control
    # ====================================================================================================

    with GeoNodes("Walk", is_group = True):

        time  = Float(0,         "Time")
        speed = Float.Factor(.5, "Speed", 0, 1, tip="Walk speed")
        size  = Float(1,         "Size", 0)
        right = Boolean(False,   "Right")

        time = time.switch(right, time + 0.5)

        with Layout("Walk between 0 and 1"):
            time = ((time % 1).switch(time < 0, 1 - ((-time) % 1)))._lc("Walk")
            walk = time.curve(
                factor = speed, 
                curve=[(0.000, 0.000, 'AUTO'), (0.200, 0.300, 'AUTO'), (0.800, 0.700, 'AUTO'), (1.000, 1.000, 'AUTO')])

        with Layout("Walk Length and Height"):
            length  = speed.map_range(to_min=0.0, to_max=3.0)._lc("Length")
            #length2 = (length/2)._lc("Half Length")
            height  = speed.map_range(to_min=0.0, to_max=1.0)._lc("Height")
            ag_fac  = speed

        up = 0.28
        dn = 1 - up

        with Layout("Horizontal"):
            shoe_y = walk.curve(factor = None, 
                curve=[(0.000, 0.500, 'VECTOR'), (up, 0.000, 'VECTOR'), (dn, 1.000, 'VECTOR'), (1.000, 0.500, 'VECTOR')]
                )
            # Minus for orientation
            shoe_y = -shoe_y.map_range(to_min=-0.8*length, to_max=0.5*length)

        with Layout("Vertical"):        
            shoe_z = walk.curve(factor=None,
                curve=[(up, 0.000, 'AUTO'), (up + 0.077, 0.334, 'VECTOR'), (up + 0.314, 0.825, 'VECTOR'), (dn, 0.00, 'VECTOR'), (1.000, 0.000, 'AUTO')]
                )
            shoe_z = shoe_z*height

            shoe_x = Float.Switch(right, -size/3, size/3)
        
            shoe_loc = Vector((shoe_x, shoe_y, shoe_z))

        with Layout("Tilt"):
            shoe_tilt = walk.curve(factor=None,
                curve=[(0.000, 0.500, 'VECTOR'), (up, 0.500, 'VECTOR'), (0.368, 1.000, 'AUTO'), (0.627, 0.126, 'AUTO'), (dn, 0.500, 'VECTOR'), (1.000, 0.500, 'VECTOR')]
                )
            shoe_tilt = shoe_tilt.map_range(to_min=-0.8, to_max=0.8)*ag_fac

        with Layout("tiptoe"):
            shoe_tiptoe = walk.curve(factor=None,
                curve=[(0.000, 0.000, 'AUTO'), (up, 0.000, 'VECTOR'), (0.289, 0.720, 'VECTOR'), (0.466, 0.000, 'VECTOR'), (1.000, 0.000, 'AUTO')]
                )
            shoe_tiptoe *= -1*ag_fac

        # Outing

        walk.out(       "Walk")
        speed.out(      "Speed")
        shoe_loc.out(   "Location")
        shoe_tilt.out(  "Tilt")
        shoe_tiptoe.out("Tiptoe")

    # ====================================================================================================
    # Shoe
    # ====================================================================================================

    with GeoNodes("Shoe", is_group=True):

        resol  = Integer(16,    "Resolution")
        size   = Float(1,       "Size", 0)
        twist  = Float.Angle(0, "Twist")

        loc    = Vector(None,   "Location")
        tilt   = Float.Angle(0, "Tilt")
        tiptoe = Float.Angle(0, "Tiptoe")


        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(4)]

            curve = Curve.Line(start=(-.2, 0, 0), end=(.8, 0, 0)).resample(count=4)
            curve.points[ind[1]].position = (0, 0, 0)
            curve.points[ind[2]].position = (.5, 0, 0)

            curve.points[ind[0]].radius = 0
            curve.points[ind[1]].radius = 1
            curve.points[ind[2]].radius = .8
            curve.points[ind[3]].radius = 0

            curve.points._Angle = 0.
            curve.points[ind[2]]._Angle = tiptoe
            curve.transform(scale=size)

        with Layout("Profile"):
            profile = Curve.Circle(radius=.22).resample(count=2*resol + 2)
            profile.points[(nd.index > 0) & (nd.index <= resol)].delete()
            profile.transform(scale=size)

        with Layout("Shoe Shape"):

            shoe = G().sausage(
                curve               = curve,
                profile             = profile,
                angle               = Float("Angle"),
                joints              = True,
                joints_width        = .4,
                axis                = 'Y',
                start_shape         = .4,
                start_resolution    =  4,
                end_shape           = .4,
                end_resolution      =  4,
            )
        shoe = Mesh(shoe.transform(rotation=(0, 0, -pi/2)))

        with Layout("Finalize"):
            shoe.faces.shade_smooth = True
            shoe.faces.material = "Obs Shoe"

        with Layout("Orientation in space"):
            shoe.transform(translation=loc, rotation=(tilt, 0, 0))
            shoe.transform(rotation=(0, 0, twist))

        shoe.out()

    # ====================================================================================================
    # Observer
    # ====================================================================================================

    with GeoNodes("Observer"):

        # ---------------------------------------------------------------------------
        # Params
        # ---------------------------------------------------------------------------

        resol  = Integer(8, "Resolution", 1, 8)
        color  = Color((1, 0, 0), "Color")
        transp = Float.Factor(0, "Transparency", 0, 1)

        with Panel("Walk"):
            time  = Float(0.0, "Time")
            speed = Float.Factor(.5, "Speed", 0, 1)
            #walk_factor = Float.Factor(0,  "Factor", 0, 1)

        with Panel("Head"):

            head_hrz = Float.Angle(0, "Head Horizontal", -pi/2, pi/2)
            head_vrt = Float.Angle(0, "Head Vertical",   -pi/3, pi/3)
            head_lat = Float.Angle(0, "Head Lateral",    -pi/3, pi/3)

            with Panel("Eyes"):
                hrz_angle     = Float.Angle(0,    "Horizontal", -pi/4, pi/4)
                vrt_angle     = Float.Angle(0,    "Vertical",   -pi/4, pi/4)
                ag_eyelid     = Float.Factor(.25, "Eyelid", -1, 1)
                left_eyelid   = Float.Factor(0,   "Left Eyelid", -1, 1)
                right_eyelid  = Float.Factor(0,   "Right Eyelid", -1, 1)
                angryness     = Float.Factor(.5,  "Angryness", 0, 1)

            with Panel("Hair"):
                hair_obj  = Object(None, "Hair Object")
                hair_mat  = Material("Obs Hair", "Hair Material")
                use_hair  = Boolean(True,    "Hair")
                hair_col  = Color([0.061606, 0.008269, 0.002920, 1.000000], "Hair Color")
                use_moust = Boolean(True,    "Moustache")
                moust_col = Color([0.061606, 0.008269, 0.002920, 1.000000], "Moustache Color")

        # ---------------------------------------------------------------------------
        # Main
        # ---------------------------------------------------------------------------

        with Layout("Base Sphere"):
            segments = resol*8
            rings    = resol*4

            sphere = Mesh.UVSphere(segments=segments, rings=rings, radius=1)
            sphere.faces.shade_smooth = True
            sphere.faces.material = "Obs Skin"

        with Layout("Head"):

            with Layout("Hair and Moustache"):
                sphere.transform(rotation=(0, 0, pi/2))

                head = G().hair_scalp(sphere)
                head = G().moustache_scalp(head)

                head.transform(rotation=(0, 0, -pi/2))

            head = head.transform(scale=(.8, .8, 1))
            nose = Mesh(sphere).transform(scale=(.3, .39, .3), translation=(0, -.91, -.08))

            head += nose

            with Layout("Eyes"):
                eye = Mesh.UVSphere(segments=segments//2, rings=rings//2, radius=.24)
                eye.faces._White = nd.position.z < .9*.24
                eye.transform(rotation=(pi/2, 0, 0))

                eye.faces.shade_smooth = True
                eye.faces.material = "Obs Eye"

                eye_rot = Vector((-vrt_angle, 0, -hrz_angle))

                eye_loc0 = ( .5, -.6, .4)
                eye_loc1 = (-.5, -.6, .4)

                head += Mesh(eye).transform(translation=eye_loc0, rotation=eye_rot)
                head += Mesh(eye).transform(translation=eye_loc1, rotation=eye_rot)

            with Layout("Eyelids"):

                r = .24*1.2
                nsegms = segments // 2
                eyelid = Mesh.UVSphere(segments=nsegms, rings=rings//2, radius=r)
                eyelid.points[nd.position.z < -0.01].delete()

                eyelid.faces.shade_smooth = True
                disk = Mesh.Circle(vertices=nsegms, radius=r, fill_type='NGON').flip_faces()

                eyelid += disk
                eyelid.merge_by_distance()

                eyelid.faces.material = "Obs Skin"

                left_ag  = (ag_eyelid + left_eyelid).map_range(-1., 1., pi/2, -pi/2)
                right_ag = (ag_eyelid + right_eyelid).map_range(-1., 1., pi/2, -pi/2)

                ag = key_function(angryness, (0, -.6), (1, .6))

                left_eyelid  = Mesh(eyelid).transform(translation=eye_loc0, rotation=(left_ag, -ag, 0))
                right_eyelid = Mesh(eyelid).transform(translation=eye_loc1, rotation=(right_ag, ag, 0))

                head += (left_eyelid, right_eyelid)

            with Layout("External Hair"):
                hair_geo = Mesh(hair_obj.info().geometry)
                hair_geo.faces.material = hair_mat
                hair_geo.faces._Color = hair_col
                hair_geo.transform(scale=4)
                head = Mesh(head + hair_geo)

            with Panel("Head Orientation"):
                head.transform(translation=(0, 0, 1.1))
                head.transform(translation=(0, 0, -1.1), rotation=(-head_vrt, head_lat, head_hrz))

        with Layout("Body"):
            body = Mesh(sphere).transform(scale=(1.15, 1.15, 1.8))
            tshirt = nd.position.z < 1.6
            body.faces[tshirt]._Color = (1, 1, 1)
            body.faces[tshirt].material = "Obs Blouse"

            blouse = Mesh(body).transform(scale=(1.02, 1.02, 1.02))
            blouse.faces.material = "Obs Blouse"
            blouse.faces._Color   = color

            cube = Mesh.Cube(size=(3, 3, 1.7)).transform(translation=(0, 0, 1.7/2))
            # Set a différent material to delete faces
            cube.faces.material = "Obs Skin"
            blouse = blouse.intersect(cube)

            cyl = Mesh.Cylinder(vertices=8).transform(rotation=(0, 2*pi/3, 0), translation=(0.8, 0, 2.3))
            cyl.faces.material = "Obs Skin"

            blouse = blouse.difference(cyl)
            blouse.transform(rotation=(0, 0, -pi/2))

            blouse.faces[nd.material_index==0].delete()

            top = nd.position.z < .01
            for _ in range(10):
                top = blouse.edges[top].extrude(offset=(0, 0, -.25)).top_

            body += blouse

            body.transform(translation=(0, 0, -3))

        obs = body + head

        obs.transform(translation=(0, 0, 3), scale=.46)

        with Layout("Shoes"):

            node  = G().walk(time=time, speed=speed, right=False).node
            left_shoe = G().shoe(location=node.location, tilt=node.tilt, tiptoe=node.tiptoe)

            wlk = node.walk
            spd = node.speed

            node  = G().walk(time=time, speed=speed, right=True).node
            right_shoe = G().shoe(location=node.location, tilt=node.tilt, tiptoe=node.tiptoe)

            shoes = left_shoe + right_shoe

        with Panel("Left Hand"):
            left_hand  = G().hand(
                resolution  = resol,
                right       = False,
                arm         = True,
                walk        = wlk,
                shape       = True,
                speed       = spd).node.link_inputs(exclude=['Resolution', 'Left', 'Arm', 'Walk', 'Speed', 'Angles'])

        with Panel("Right Hand"):
            right_hand = G().hand(
                resolution  = resol,
                right       = True,
                arm         = True,
                walk        = (wlk + .5)%1,
                shape       = True,
                speed       = spd).node.link_inputs(exclude=['Resolution', 'Left', 'Arm', 'Walk', 'Speed', 'Angles'])

            dx, dz = -.75, 2.5
            left_hand = left_hand._out.transform(translation=(dx, 0, dz))
            right_hand = right_hand._out.transform(translation=(-dx, 0, dz))

            obs += (left_hand, right_hand)

        with Layout("Body Posture"):

            front_ag_max = spd.map_range(to_min= .05, to_max=.1)
            front_ag = gnmath.sin(gnmath.sin(wlk*(4*pi))*front_ag_max) + spd.map_range(to_min=0., to_max=.05)

            side_ag_max = spd.map_range(to_min= .02, to_max=.1)
            side_ag = gnmath.sin(gnmath.sin(wlk*(2*pi))*side_ag_max)

            z_max = spd.map_range(to_min=0, to_max=.2)
            z = (1 - gnmath.cos(wlk*(4*pi)))*z_max

            obs.transform(translation=(0, 0, z), rotation=(front_ag, side_ag, 0))

            obs += shoes

        obs = Mesh(obs)

        with Layout("Hair and Moustache"):

            scalp = Float("Hair Scalp")
            scalp *= scalp.exists_
            obs = G().hair(obs,
                scalp   = scalp,
                color   = hair_col,
                length  = .5,
                curl    = 0,
                density = 5_000,
                radius  = .01).switch_false(use_hair, obs)

            scalp = Float("Moustache Scalp")
            scalp *= scalp.exists_
            obs = G().hair(obs,
                scalp   = scalp,
                color   = moust_col,
                length  = .16,
                curl    = 0,
                density = 10_000,
                radius  = .01).switch_false(use_moust, obs)

            obs = Mesh(obs)

        obs.transform(scale=.5)
        obs.faces._Transparency = transp

        obs.out()
