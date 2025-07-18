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
        transp = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        ped = Shader.Principled(
            base_color = color,
            roughness  = .9,
        )

        shader = ped.mix(Shader.Transparent(), fac=transp)
        shader.out()

    with ShaderNodes("Obs Eye"):
        white = snd.attribute(attribute_type='GEOMETRY', attribute_name="White").fac
        color = Color((0, 0, 0)).mix(white, Color((1, 1, 1)))
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        ped = Shader.Principled(
            base_color = color,
            roughness  = 0,
        )

        shader = ped.mix(Shader.Transparent(), fac=transp)

        shader.out()

    with ShaderNodes("Obs Hair"):

        color   = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        ped = Shader.PrincipledHair(
            color = color,
        )

        shader = ped.mix(Shader.Transparent(), fac=transp)

        shader.out()

    with ShaderNodes("Obs Blouse"):

        color   = Color(snd.attribute(attribute_type='GEOMETRY', attribute_name="Color").vector)
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        ped = Shader.Principled(
            base_color = color,
            roughness  = .8,
        )

        shader = ped.mix(Shader.Transparent(), fac=transp)

        shader.out()

    with ShaderNodes("Obs Shoe"):

        color   = [0.000000, 0.000000, 0.000000, 1.000000]
        transp  = snd.attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

        ped = Shader.Principled(
            base_color = color,
            roughness  = .3,
        )

        shader = ped.mix(Shader.Transparent(), fac=transp)

        shader.out()

    # =============================================================================================================================
    # Key function

    def key_function(param, *keys):

        with Layout("Key Function"):
            value = None
            for i in range(len(keys) - 1):
                (key0, val0), (key1, val1) = keys[i], keys[i+1]

                val = param.map_range(from_min=Float(key0), from_max=Float(key1), to_min=Float(val0), to_max=Float(val1))

                if i == 0:
                    value = val

                else:
                    value = value.switch(param >= key0, val)

        return value

    # =============================================================================================================================
    # =============================================================================================================================
    # Hair and Moustache
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # Hair scalp

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
        mesh.remove_named_attribute("BScalp")

        mesh.out()
        Float("Hair Scalp").out("Hair Scalp")

    # =============================================================================================================================
    # Moustache scalp

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

    # =============================================================================================================================
    # Hair

    with GeoNodes("Hair", is_group=True):

        mesh = Mesh()
        scalp = Float.Factor(1, "Scalp", 0, 1)

        with Panel("Hair"):
            color  = Color((0.439239, 0.078419, 0.007497, 1.000000), "Color")
            length = Float(.4, "Length")
            curl   = Float.Factor(0, "Curl", 0, 1)
            radius = Float(.01, "Radius", 0, .1)

        with Layout("Generate"):

            count = curl.map_range(to_min=6, to_max=12).to_integer()

            hair_node = G().generate_hair_curves(
                    surface         = mesh,
                    hair_length     = length,
                    control_points  = count,
                    density         = 10000,
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

            hair = hair.to_mesh(profile_curve=Curve.Circle(resolution=6, radius=1), fill_caps=True)

            hair.faces._Color = color
            hair.faces.material = "Obs Hair"
            hair.faces._Color = color

        (mesh + hair).out()

    # =============================================================================================================================
    # =============================================================================================================================
    # Observer modifiers
    # =============================================================================================================================
    # =============================================================================================================================

    # =============================================================================================================================
    # Articulated sausage

    with GeoNodes("Sausage", is_group=True):

        curve   = Curve()
        profile = Curve(None, "Profile")
        angle   = Float.Angle(.2, "Angle", hide_value=False)
        twist   = Float.Angle(0, "Twist", -pi, pi)
        axis    = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2}, menu='X', name='Axis')
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

        with Repeat(curve=curve, iterations=n-1) as rep:
            index = rep.iteration + 1
            pos = nd.position
            center = rep.curve.points.sample_index(pos, index=index)
            ag = rep.curve.points.sample_index(angle, index=index)
            rot = Rotation.IndexSwitch((ag, 0, 0), (0, ag, 0), (0, 0, ag), index=axis)
            p = center + rot @ (pos - center)
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

            new_curve = Curve(curve).resample(m)

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

            curve = curve.switch(use_joints, new_curve)
            n = curve.points.count

        with Layout("Twist"):
            curve = curve.transform(rotation=(0, 0, twist))


        if False:
            pts = curve.points.instance_on(Mesh.UVSphere(radius=.01))
            (curve + pts).out()
            raise Break()

        with Layout("Start Shape"):

            m = n + start_resol
            start_resol1 = start_resol + 1

            new_curve = Curve(curve).resample(m)
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

            new_curve = Curve(curve).resample(m)
            new_curve.points[nd.index <= last].position = curve.points.sample_index(nd.position, index=nd.index)
            new_curve.points[nd.index <= last].radius   = curve.points.sample_index(nd.radius,   index=nd.index)

            fac = (nd.index - last)/(end_resol + 1)

            pos0 = curve.points.sample_index(nd.position, index=n-2)
            pos1 = curve.points.sample_index(nd.position, index=n-1)

            new_curve.points[nd.index > last].position = pos0 + (pos1 - pos0).scale(fac)

            radius = curve.points.sample_index(nd.radius, index=n-2)
            new_curve.points[nd.index > last].radius = radius*(1-fac)**end_shape

            curve = new_curve
            n = curve.points.count


        if True:
            mesh = curve.to_mesh(profile_curve=profile)
            curve.switch(use_mesh, mesh).out()

        else:
            pts = curve.points.instance_on(Mesh.UVSphere(radius=.02))
            (curve + pts).out()

    # =============================================================================================================================
    # Finger

    with GeoNodes("Finger", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol        = Integer(4, "Resolution", 1, 8)
        length       = Float(1, "Length", 0)
        radius       = Float(.12, "Radius", 0)
        bend         = Float.Angle(0, "Bend", 0, pi/2, single_value=True)
        fold         = Float.Angle(0, "Fold", 0, pi/2, single_value=True)
        lateral      = Float.Angle(0, "Lateral", -pi/8, pi/8, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(6)]

            curve = Curve.Line(start=(0, 0, -.2), end=(0, 0, 1)).resample(6)
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
            profile = Curve.Circle(radius=radius).resample(resolution)

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

    # =============================================================================================================================
    # Finger

    with GeoNodes("Thumb", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol        = Integer(4, "Resolution", 1, 8)
        length       = Float(1, "Length", 0)
        radius       = Float(.12, "Radius", 0)
        pinch        = Float.Angle(0, "Pinch", 0, pi/2, single_value=True)
        bend         = Float.Angle(0, "Bend", 0, pi/2, single_value=True)
        fold         = Float.Angle(0, "Fold", 0, pi/2, single_value=True)
        lateral      = Float.Angle(0, "Lateral", -pi/2, pi/2, single_value=True)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(6)]

            curve = Curve.Line(start=(0, 0, -.5), end=(0, 0, 1)).resample(6)
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
            profile = Curve.Circle(radius=radius).resample(resolution)

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

    # =============================================================================================================================
    # Hand

    with GeoNodes("Hand", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol = Integer(4, "Resolution", 1, 8)
        left_hand  = Boolean(False, "Left")

        bend    = [None]*5
        fold    = [None]*5
        lateral = [None]*5
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
                    pinch        = pinch,
                    bend         = bend[0],
                    fold         = fold[0],
                    lateral      = lateral[0],
                )

            x = -room*3
            for i in range(1, 5):

                finger = G().finger(
                    resolution   = resol,
                    length       = lengths[i],
                    radius       = radius,
                    bend         = .1 + bend[i],
                    fold         = .1 + fold[i],
                    lateral      = lateral[i],
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
            side_fac = Integer.Switch(left_hand, 1, -1)
            hand = hand.switch(left_hand, Mesh(hand).transform(scale=(1, -1, 1)).flip_faces())


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

    # =============================================================================================================================
    # Walk / run control

    with GeoNodes("Walk", is_group = True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        walk         = Float(0,         "Walk")
        speed        = Float.Factor(.5, "Speed", 0, 1)
        walk_factor  = Float.Factor(1,  "Factor", 0, 1)
        size         = Float(1,         "Size", 0)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        # Foot location phases:
        # 0       -> Back  : Backwards
        # Back    -> Front : Ellipsis in the air
        # Front   -> 0     : Back to initial position

        # Tilt phases:
        # 0       -> flat0 : flat
        # flat0   -> down  : tilted down
        # down    -> up    : tilted up
        # up      -> flat1 : flat agin

        # Tiptoe phases
        # flat0   -> tip   : 0 to tip
        # tip     -> tip0  : tip to 0

        with Layout("Walk between 0 and 1"):
            walk = ((walk % 1).switch(walk < 0, 1 - ((-walk) % 1))*walk_factor)._lc("Walk")
            speed = (speed*walk_factor)._lc("Speed")

        with Layout("Walk Length and Height"):
            length  = speed.map_range(to_min=1.1, to_max=1.5)._lc("Length")
            length2 = (length/2)._lc("Half Length")
            height  = speed.map_range(to_min=.3, to_max=1.1)._lc("Height")

        with Layout("Foot Location"):

            walk_back  = key_function(speed, (0, .2), (1, 0.18))
            back       = key_function(speed, (0, -length*.8), (1, -length*.8))
            walk_front = walk_back + key_function(speed, (0, .4), (1, .7))
            front      = back + length
            pivot      = length2# + back

            angle   = key_function(walk, (walk_back, 0), (walk_front, pi))
            delta_x = key_function(walk, (0, 0), (walk_back, back), (walk_front, 0), (1, -length))

            x = pivot - length2*gnmath.cos(angle)
            z = height*gnmath.sin(angle)
            foot_loc = Vector((delta_x + x, 0, z))

        with Layout("Foot Tilt"):
            walk_flat0 = walk_back
            walk_down  = walk_flat0 + key_function(speed, (0, .1), (1, .05))
            walk_up    = walk_front
            walk_flat1 = walk_up + key_function(speed, (0, .1), (1, .05))
            down       = key_function(speed, (0, .4), (1, .7))
            up         = key_function(speed, (0, -.4), (1, -1))
            tilt       = key_function(walk, (walk_flat0, 0), (walk_down, down), (walk_up, up), (walk_flat1, 0))

        with Layout("Tiptoe"):
            dt      = key_function(speed, (0, .1), (1, .05))
            angle   = key_function(speed, (0, -.4), (1, -.8))
            tiptoe  = key_function(walk, (walk_flat0, 0), (walk_flat0 + dt, angle), (walk_flat0 + 1.6*dt, 0))

        walk.out(       "Walk")
        speed.out(      "Speed")
        foot_loc.scale(size).out(   "Location")
        tilt.out(       "Tilt")
        tiptoe.out(     "Tiptoe")

    # =============================================================================================================================
    # Shoe

    with GeoNodes("Shoe", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol  = Integer(16,    "Resolution")
        size   = Float(1,       "Size", 0)
        twist  = Float.Angle(0, "Twist")

        loc    = Vector(None,   "Location")
        tilt   = Float.Angle(0, "Tilt")
        tiptoe = Float.Angle(0, "Tiptoe")

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Curve"):

            ind = [nd.index.equal(i) for i in range(4)]

            curve = Curve.Line(start=(-.2, 0, 0), end=(.8, 0, 0)).resample(4)
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
            profile = Curve.Circle(radius=.22).resample(2*resol + 2)
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
        shoe = Mesh(shoe)

        with Layout("Finalize"):
            shoe.faces.shade_smooth = True
            shoe.faces.material = "Obs Shoe"

        with Layout("Orientation in space"):
            shoe.transform(translation=loc, rotation=(0, tilt, 0))
            shoe.transform(rotation=(0, 0, twist))

        shoe.out()

    # =============================================================================================================================
    # Shoes

    with GeoNodes("Shoes", is_group=True):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol  = Integer(16,    "Resolution")
        size   = Float(1,       "Size", 0)

        with Panel("Walk"):
            walk    = Float(0,         "Walk")
            speed   = Float.Factor(.5, "Speed", 0, 1)
            factor  = Float.Factor(1,  "Factor", 0, 1)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        with Layout("Left"):
            left_walk = G().walk(
                walk    = walk,
                speed   = speed,
                factor  = factor,
                size    = size).node

            left_shoe = G().shoe(
                resolution = resol,
                size       = size,
                twist      = -pi/2,

                location   = left_walk.location,
                tilt       = left_walk.tilt,
                tiptoe     = left_walk.tiptoe,
                )

            walk_out  = left_walk.walk_
            speed_out = left_walk.speed_

        with Layout("Right"):
            right_walk = G().walk(
                walk    = walk + .5,
                speed   = speed,
                factor  = factor,
                size    = size).node

            right_shoe = G().shoe(
                resolution = resol,
                size       = size,
                twist      = -pi/2,

                location   = right_walk.location,
                tilt       = right_walk.tilt,
                tiptoe     = right_walk.tiptoe,
                )

        dx = .5
        left_shoe.transform(translation=(dx, 0, 0))
        right_shoe.transform(translation=(-dx, 0, 0))

        shoes = left_shoe + right_shoe
        shoes.out()
        walk_out.out("Walk")
        speed_out.out("Speed")

    # =============================================================================================================================
    # Observer

    with GeoNodes("Observer"):

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        resol  = Integer(8, "Resolution", 1, 8)
        color  = Color((1, 0, 0), "Color")
        transp = Float.Factor(0, "Transparency", 0, 1)

        with Panel("Walk"):
            speed       = Float.Factor(.5, "Speed", 0, 1)
            walk_factor = Float.Factor(0,  "Factor", 0, 1)

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

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

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

            if True:
                blouse.faces[nd.material_index==0].delete()

            else:
                blouse += cyl
                blouse.out()
                raise Break()

            top = nd.position.z < .01
            for _ in range(10):
                top = blouse.edges[top].extrude(offset=(0, 0, -.25)).top_

            body += blouse

            body.transform(translation=(0, 0, -3))

        obs = body + head

        obs.transform(translation=(0, 0, 3), scale=.46)

        with Layout("Shoes"):

            walk = nd.scene_time().seconds*speed.map_range(to_min=.5, to_max=2)

            shoes = G().shoes(walk=walk, speed=speed, factor=walk_factor)
            wlk = shoes.walk_
            spd = shoes.speed_


        with Layout("Hands"):
            left_hand  = G().hand(
                resolution  = resol,
                left        = True,
                arm         = True,
                walk        = wlk,
                speed       = spd).node.link_from(exclude=['Resolution', 'Left', 'Arm', 'Walk', 'Speed'],  panel="Left Hand")

            right_hand = G().hand(
                resolution  = resol,
                left        = False,
                arm         = True,
                walk        = (wlk + .5)%1,
                speed       = spd).node.link_from(exclude=['Resolution', 'Left', 'Arm', 'Walk', 'Speed'], panel="Right Hand")

            dx, dz = -.75, 2.5
            left_hand = left_hand.transform(translation=(dx, 0, dz))
            right_hand = right_hand.transform(translation=(-dx, 0, dz))

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
                scalp  = scalp,
                color  = hair_col,
                length = .5,
                curl   = 0,
                radius = .002).switch_false(use_hair, obs)

            scalp = Float("Moustache Scalp")
            scalp *= scalp.exists_
            obs = G().hair(obs,
                scalp = scalp,
                color  = moust_col,
                length = .16,
                curl   = 0,
                radius = .002).switch_false(use_moust, obs)

            obs = Mesh(obs)

        obs.transform(scale=.5)
        obs.faces._Transparency = transp

        obs.out()
