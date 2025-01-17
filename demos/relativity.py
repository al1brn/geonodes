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

module : demo relativity
------------------------


Generates modifiers for special relativity

The space-time is (x, y, z=t) : space in 2D plus time dimension on z axis

Geometry Nodes
--------------
    - "Plane Line Intersection" (group) : intersection between a line and a plane
    - "Frame Change" (group) : Change position and direction to align X axis along the given direction
    - "Normalize Speed" (group) : Normalize speed
    - "Transformation" (group) : Lorentz or Galilean transformation
    - "Simulateneity Plane" (group): Compute the simultaneity plane of event + speed
    - "Simultaneity Intersection" (modifier) : Compute the intersection of the simultaneity plane with the provided curve
    - "Accelerated Transformation" (modifier) : transform a uniform motion into an accelerated frame defined a curve in (x, y, t=z) space time
    - "Rounded Triangle" (group) : function t -> (x, y) producing a triangle with a rounded summit

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/relativity.py)

WORK IN PROGRESS

"""

from pathlib import WindowsPath
from bpy.types import Attribute, PARTICLE_PT_hair_dynamics_presets
from geonodes import *

DEBUG = True
SPEED_FWD = True

def demo():

    print('-'*100)

    Tree._reset_counters()

    # =============================================================================================================================
    # Cut exactly a curve at a given z

    with GeoNodes("Vertical Cut"):

        curve = Curve()
        factor = Float.Factor(1, "Cut", 0, 1, tip="Vertical cut Factor")

        line = Curve(Curve)
        line.points.store("Factor", nd.spline_parameter.factor)
        line.points.position = (0, 0, nd.position.z)

        length = line.length

        fac = line.sample(Float.Named("Factor"), length=factor*length)

        line = curve.trim_factor(end=fac)

        line.out("Curve")



    # =============================================================================================================================
    # Plane and Line intersection
    #
    # M is given by k such as:
    # (M - L) = kl
    # (M - P).p = 0
    #
    # (L + kl - P).p = kl.p = (P - L).p
    # k = (P - L).p/l.p

    with GeoNodes("Plane Line Intersection", is_group=True):

        P = Vector(0, "Plane Origin")
        p = Vector((0, 0, 1), "Plane Vector")
        L = Vector(0, "Line Origin")
        l = Vector((0, 0, 1), "Line Vector")

        k = (P - L).dot(p)/l.dot(p)

        (L + k*l).out("Event")

    # =============================================================================================================================
    # Frame change
    #
    # Transform position and rotation such as the X axis is along the provided direction

    with GeoNodes("Frame Change", is_group=True):

        event   = Vector(0, "Event")
        origin  = Vector(0, "Origin")
        x_axis  = Vector((1, 0, 0), "X Axis")
        pos_dir = Vector((0, 0, 0), "Positive Direction")
        reverse = Boolean(False, "Reverse")

        # ----- Rotation to have the x axis

        with Layout("Rotation to have x direction along speed"):
            ag = gnmath.atan2(x_axis.y, x_axis.x)

            negative = pos_dir.dot(x_axis) < 0

            ag = ag.switch(negative, ag + pi)

            rotation = Rotation.FromAxisAngle((0, 0, 1), ag)
            inverse  = rotation.invert()

        # ----- Direct & Reverse

        d_event  = rotation @ (event - origin)
        r_event = origin + inverse @ event

        d_event.switch(reverse, r_event).out("Event")

    # =============================================================================================================================
    # Normalize Speed

    with GeoNodes("Normalize Speed", is_group=True):
        speed   = Vector((0, 0, 1), "Speed")
        lorentz = Boolean(True, "Lorentz")

        speed = speed.switch(speed.z.equal(0), (speed.x, speed.y, 1))
        speed_norm = Vector((speed.x, speed.y, 0)).length/speed.z
        beta = speed_norm.switch(lorentz, gnmath.min(speed_norm, .999))
        ratio = beta/speed_norm/speed.z
        speed = Vector((speed.x*ratio, speed.y*ratio, 1))

        speed.out("Speed")
        beta.out("Beta")

    def normalize_speed(speed, lorentz):
        node = GroupF().normalize_speed(speed=speed, lorentz=lorentz)
        return node.speed, node.beta

    # =============================================================================================================================
    # Lorentz Transformation

    with GeoNodes("Transformation", is_group=True):

        event       = Vector(     0, "Event")
        speed       = Vector(     0, "Speed")
        origin      = Vector(     0, "Origin")
        use_x_speed = Boolean(False, "X Along Speed", tip="Align accelerated frame X axis along speed")
        reverse     = Boolean(False, "Reverse")
        use_lorentz = Boolean(True,  "Lorentz", tip="Lorentz (True) or Galilean (False)")

        speed, beta = normalize_speed(speed, use_lorentz)

        with Layout("Rotation"):
            ag = gnmath.atan2(speed.y, speed.x)
            rotation = Rotation.FromAxisAngle((0, 0, 1), -ag)
            inverse  = rotation.invert()

        with Layout("Gamma"):
            gamma = Float.Switch(use_lorentz, 1, (1 - beta**2)**(-.5))

        # ---------------------------------------------------------------------------
        # Transformations

        with Layout("Direct"):
            evt      = rotation @ (event - origin)
            x, y, t  = evt.x, evt.y, evt.z
            t_       = t.switch(use_lorentz, gamma*(t - beta*x))
            x_       = gamma*(x - beta*t)
            d_event_ = Vector((x_, y, t_))
            d_event_ = (inverse @ d_event_).switch(use_x_speed, d_event_)

        with Layout("Reverse"):
            evt      = (rotation @ event).switch(use_x_speed, event)
            x, y, t  = evt.x, evt.y, evt.z
            t_       = t.switch(use_lorentz, gamma*(t + beta*x))
            x_       = gamma*(x + beta*t)
            r_event_ = origin + (inverse @ Vector((x_, y, t_)))

        # ----- Selection and done

        event_ = d_event_.switch(reverse, r_event_)

        event_.out(  "Event")
        beta.out(    "Beta")
        gamma.out(   "Gamma")
        rotation.out("Space Rotation")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Combine speeds

    with GeoNodes("Combine Speeds", is_group=True):

        u = Vector(0, "u")
        v = Vector(0, "v")
        lor = Boolean(True, "Lorentz")

        u, _ = normalize_speed(u, lor)
        v, _ = normalize_speed(v, lor)

        w = GroupF().transformation(event=v, speed=u, lorentz=lor, reverse=True).event
        w.out("DEBUG")
        w, beta = normalize_speed(w, lor)

        w.out("w")
        beta.out("Beta")

    # =============================================================================================================================
    # Simultaneity plane of a point and speed direction
    #
    # Return also the intersection with a straigth line into several frames:
    # - Event : into the reference frame
    # - Local Event : into the moving frame
    # - Rotated Event : into the moving frame with X axis is oriented along the speed

    with GeoNodes("Simultaneity Plane", is_group=True):

        speed        = Vector(       0, "Speed")
        use_lorentz  = Boolean(   True, "Lorentz", tip="Lorentz (True) or Galilean (False)")

        event        = Vector(       0, "Event")
        event0       = Vector(       0, "Uniform Event", tip="An event from the uniform motion")
        speed0       = Vector((0, 0, 1),"Uniform Speed", tip="Speed of the uniform motion")

        with Layout("Simultaneity Plane"):

            speed, beta = normalize_speed(speed, use_lorentz)

            with Layout("Speed angle in space"):
                space_angle = gnmath.atan2(speed.y, speed.x)
                space_rot = Rotation((0, 0, space_angle))

            with Layout("Beta = tan of speed angle with time axis"):
                k = Vector((0, 0, 1))
                perp = speed.cross(k)
                time_angle = Float.Switch(use_lorentz, 0, gnmath.atan(beta))
                time_rot = Rotation.FromAxisAngle(perp, time_angle)

            with Layout("Combine the two rotations"):
                rot = space_rot @ time_rot

            plane = rot @ k

        with Layout("Intersection with uniform moition"):
            speed0, beta0 = normalize_speed(speed0, use_lorentz)

            evt = GroupF().plane_line_intersection(plane_origin=event, plane_vector=plane, line_origin=event0, line_vector=speed0).event
            loc_evt = GroupF().transformation(event=evt, speed=speed, origin=event, lorentz=use_lorentz).event

            rot_evt = rot.invert() @ (evt - event)

            with Layout("Alpha = 1/Gamma"):
                alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1 - beta**2))
                rot_evt *= (alpha, 1, 1)

        # ----- Done

        plane.out(      "Plane")
        rot.out(        "Rotation")
        beta.out(       "Beta")
        space_angle.out("Space Angle")

        evt.out(         "Event")
        loc_evt.out(     "Local Event")
        rot_evt.out(     "Rotated Event")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Intersection of a simultaneity plane with a space time curve

    with GeoNodes("Simultaneity Intersection With Curve"):

        curve = Curve()

        event  = Vector(0, "Event")
        speed  = Vector(0, "Speed")
        use_lorentz = Boolean(True, "Lorentz", tip="Lorentz (True) or Galilean (False)")
        size = Float(100, "Size")

        plane_node = GroupF().simultaneity_plane(speed=speed, lorentz=use_lorentz)
        plane_perp = plane_node.plane

        with Layout("Simultaneity plane"):
            plane = Mesh.Cube(size=(size, size, .01))
            rot = Rotation.AlignZToVector(plane_perp)
            plane = plane.transform(rotation=rot, translation=event)

        with Layout("Intersection"):
            curve.splines.resolution = 128
            meshed_curve = curve.to_mesh(Curve.Circle(radius=.1))
            circle = plane.intersect(meshed_curve)

        p = circle.points.attribute_statistic(nd.position).mean

        p.out("Event")
        plane_perp.out("Plane")
        plane_node.rotation.out("Rotation")
        plane_node.beta.out("Beta")
        plane_node.space_angle.out("Space Angle")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Proper duration of a line

    with GeoNodes("Proper Duration"):

        curve       = Curve()
        use_lorentz = Boolean(True, "Lorentz", tip="Lorentz (True) or Galilean (False)")


        count = curve.points.count

        pos = curve.points.sample_index(nd.position, index=0)
        tan = curve.points.sample_index(nd.curve_tangent, index=0)

        curve.points.store("Proper Time", 0.)
        curve.points.store("Interval", 0.)

        with Repeat(curve=curve, pos=pos, tan=tan, proper_time=0., interval=0., index=1, iterations=count-1) as rep:

            new_pos = curve.points.sample_index(nd.position, index=rep.index)
            new_tan = curve.points.sample_index(nd.curve_tangent, index=rep.index)

            speed, beta = normalize_speed(rep.tan, use_lorentz)
            alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1 - beta**2))

            dt = new_pos.z - rep.pos.z
            new_t = rep.proper_time + dt*alpha

            sel = rep.index.equal(nd.index)

            ds = (Vector((new_pos.x, new_pos.y, 0)) - (rep.pos.x, rep.pos.y, 0)).length
            ds = ds.switch(use_lorentz, gnmath.sqrt(dt**2 - ds**2))
            new_s = rep.interval + ds

            rep.curve.points[sel].store("Proper Time", new_t)
            rep.curve.points[sel].store("Distance",    new_s)

            rep.pos = new_pos
            rep.tan = new_tan
            rep.proper_time = new_t
            rep.interval = new_s
            rep.index += 1


        rep.curve.out(      "Curve")
        rep.proper_time.out("Proper Time")
        rep.interval.out(   "Interval")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Accelerated transformation of a uniform motion
    #
    # Uniform motion is the z axis
    # We need the intersection of the simultaneity plane with the z axis

    with GeoNodes("Accelerated Transformation"):

        curve       = Curve(      None, "Accelerated")
        event0      = Vector(        0, "Uniform Event", tip="An event from the uniform motion")
        speed0      = Vector((0, 0, 1), "Uniform Speed", tip="Speed of the uniform motion")
        use_x_speed = Boolean(   False, "X Along Speed", tip="Align accelerated frame X axis along speed")
        count       = Integer(     100, "Resolution", 2, tip="Resolution")
        use_lorentz = Boolean(    True, "Lorentz", tip="Lorentz (True) or Galilean (False)")

        curve = curve.resample(count)
        curve.splines.resolution = 128
        start_event = curve.points.sample_index(nd.position, index=0)

        with Repeat(transformed=curve, last_event=start_event, s=0., t=0., index=0, iterations=count) as rep:

            cur_event = curve.points.sample_index(nd.position, index=rep.index)
            cur_speed = curve.points.sample_index(nd.curve_tangent, index=rep.index)

            node = GroupF().simultaneity_plane(event=cur_event, speed=cur_speed, uniform_event=event0, uniform_speed=speed0, lorentz=use_lorentz)

            with Layout("Event time"):
                alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1 - node.beta**2))._lc("Alpha")
                dt = ((cur_event.z - rep.last_event.z)*alpha)._lc("dt'")

            with Layout("Distance"):
                new_s = rep.s + node.beta*dt

            new_t = (rep.t + dt)._lc("New t")
            evt = node.local_event.switch(use_x_speed, node.rotated_event) + (0, 0, new_t)

            sel = rep.index.equal(nd.index)

            rep.transformed.points[sel].position = evt

            rep.transformed.points[sel].store("Event0", cur_event)
            rep.transformed.points[sel].store("Event1", node.event)
            rep.transformed.points[sel].store("Speed", cur_speed)
            rep.transformed.points[sel].store("Space Angle",  node.space_angle)
            rep.transformed.points[sel].store("Beta",  node.beta)
            rep.transformed.points[sel].store("Alpha", alpha)
            rep.transformed.points[sel].store("Distance", new_s)

            rep.last_event = cur_event
            rep.s = new_s
            rep.t = new_t
            rep.index += 1

        transformed = rep.transformed

        transformed.out("Curve")

    # =============================================================================================================================
    # Utility : Rounded  triangle function

    with GeoNodes("Rounded Triangle", is_group=True):

        t      = Float( 0, "t")
        L      = Float( 5, "Length", 1)
        D      = Float( 2, "Delta",  0)
        r      = Float(.2, "Radius",  0)
        tc     = Float(.4, "Curve Start", .1, .5)
        time   = Float( 0, "Time")

        with Layout("Dimensions"):
            H = gnmath.sqrt(L**2 + D**2)
            tan_ag = D/L
            ag = gnmath.atan(tan_ag)
            cos_ag = L/H
            sin_ag = D/H

        with Layout("D Point"):
            Dx = L - r*sin_ag

        with Layout("Circle Center"):
            Cx = L
            Cy = D - r/cos_ag

        with Layout("Symmetry"):
            sym = t > .5
            t = t.switch(sym, 1 - t)

        with Layout("Straight part"):
            sx   = (t/tc)*Dx
            sy   = sx*tan_ag
            sdir = ag

        with Layout("Rounded part"):
            theta = (t - .5)/(.5 - tc)*ag

            rx   = Cx + r*gnmath.sin(theta)
            ry   = Cy + r*gnmath.cos(theta)
            rdir = -theta

        with Layout("Combine"):
            rounded = (t > tc) & (t < 1 - tc)

            x   = sx.switch(rounded, rx)
            y   = sy.switch(rounded, ry)
            dir = sdir.switch(rounded, rdir)

        with Layout("Central Symmetry"):
            x = x.switch(sym, 2*L - x)
            dir = dir.switch(sym, -dir)

        x.out("x")
        y.out("y")
        (time*x/L/2).out("z")
        dir.out("dir")

    # =============================================================================================================================
    # Twins

    with GeoNodes("Twins"):

        red_beta    = Float.Factor( .8, "Traveller Beta", -.999, .999,     tip="Speed back and forth of the traveller along X axis")
        duration    = Float.Time(   10, "Duration", 1,                     tip="Experiment duration")
        u_turn      = Float.Factor( .2, "U Turn duration", 0.001, 1,       tip="Time spent for U turn in % of total duration")
        count       = Integer(      20, "Resolution", 2, 10000,            tip="Number of points")
        use_lorentz = Boolean(    True, "Lorentz",                         tip="Special relativity")
        factor      = Float.Factor(  0, "Factor", 0, 1,                    tip="Frame change factor")
        end         = Float.Factor(  1, "End",    0, 1,                    tip="Trim end")

        with Layout("Parameters"):
            resolution = 2*count + 1
            dt = (duration/(resolution - 1))._lc("dt")
            acc_index = gnmath.min(round(count*(1 - u_turn)), count-1)

        with Layout("Build Accelerated Red Line"):
            blue_line0 = Curve.Line((0, 0, 0), (0, 0, duration)).resample(resolution)
            red_line0  = Curve(blue_line0)

        with Repeat(blue_line0=blue_line0, red_line0=red_line0, beta=red_beta, red_event0=Vector(), proper_time=0., index=1, iterations=resolution - 1) as rep:

            with Layout("Current Speed"):
                beta0 = rep.index.map_range_linear(acc_index, count, red_beta, 0)
                beta1 = rep.index.map_range_linear(count, resolution - 1 - acc_index, 0, -red_beta)
                new_beta = beta0.switch(rep.index > count, beta1)

                beta = ((rep.beta + new_beta)/2)._lc("Beta")
                rep.beta = new_beta

                speed = Vector((beta, 0, 1))

                alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1 - beta**2))
                new_t = rep.proper_time + dt*alpha

            sel = rep.index.equal(nd.index)

            with Layout("Red Line 0 current event"):
                red_event0 = (rep.red_event0 + speed*dt)._lc("Red Event 0")
                rep.red_line0.points[sel].position = red_event0
                rep.red_line0.points[sel].store("Proper Time", new_t)
                rep.red_event0 = red_event0

            with Layout("Blue Line 0 simultaneous event"):
                x, t = red_event0.x, red_event0.z
                t = t.switch(use_lorentz, t - x*beta)
                blue_event0 = Vector((0, 0, t))._lc("Blue Event 0")
                rep.blue_line0.points[sel].position = blue_event0

            rep.red_line0.points[sel].store("Blue Event", blue_event0)
            blue_local = GroupF().transformation(event=blue_event0, speed=speed, origin=red_event0, lorentz=use_lorentz).event
            blue_local += (0, 0, new_t)
            rep.red_line0.points[sel].store("Blue Local", blue_local)

            rep.proper_time = new_t
            rep.index += 1

        blue_line0 = rep.blue_line0
        blue_line0.points.store("Proper Time", nd.spline_parameter.factor*duration)
        red_line0  = rep.red_line0

        with Layout("Transformation into the Red Line accelerated frame"):
            red_line1 = Curve(red_line0)
            red_line1.points.position = (0, 0, Float.Named("Proper Time"))
            red_line1.resample(resolution)

            blue_line1 = Curve(red_line1)
            blue_line1.points.position = Vector.Named("Blue Local")
            blue_line1.points.store("Proper Time", Vector.Named("Blue Local").z)

        # -----------------------------------------------------------------------------------------------------------------------------
        # Finalization

        with Layout("Frame change"):
            blue_line = Curve(blue_line0)
            red_line  = Curve(red_line0)

            blue_line.points.position = nd.position.mix(factor, blue_line1.points.sample_index(nd.position, index=nd.index))
            red_line.points.position  = nd.position.mix(factor, red_line1.points.sample_index(nd.position, index=nd.index))

        with Layout("Trim"):
            blue_line = GroupF().vertical_cut(curve=blue_line, cut=end).curve
            red_line  = GroupF().vertical_cut(curve=red_line, cut=end).curve

        # Done

        (blue_line + red_line).out("Both")

        blue_line.out("Blue Line")
        red_line.out("Red Line")

        blue_line0.out("Blue Line 0")
        red_line0.out("Red Line 0")
        blue_line1.out("Blue Line 1")
        red_line1.out("Red Line 1")

    # =============================================================================================================================
    # Twins

    with GeoNodes("Space Twins"):

        red_beta    = Float.Factor( .8, "Traveller Beta", -.999, .999,     tip="Speed back and forth of the traveller along X axis")
        beta_y      = Float.Factor( .4, "Perpendicular Beta", -.999, .999, tip="Common speed of the two twins along the Y axis")
        duration    = Float.Time(   10, "Duration", 1,                     tip="Experiment duration")
        u_turn      = Float.Factor( .2, "U Turn duration", 0.001, 1,       tip="Time spent for U turn in % of total duration")
        count       = Integer(      20, "Resolution", 2, 10000,            tip="Number of points")
        use_lorentz = Boolean(    True, "Lorentz",                         tip="Special relativity")
        factor      = Float.Factor(  0, "Factor", 0, 1,                    tip="Frame change factor")
        end         = Float.Factor(  1, "End",    0, 1,                    tip="Trim end")
        time_scale  = Float.Factor(  1, "Time Scale", 0, 1,                tip="Scale to apply on z axis" )

        with Layout("Twins in one space dimension"):

            twins = GroupF().twins(end=Float(1))
            twins.link_from()

            blue_line0 = Curve(twins.blue_line_0)
            red_line0  = Curve(twins.red_line_0)
            blue_line1 = Curve(twins.blue_line_1)
            red_line1  = Curve(twins.red_line_1)

        resolution = red_line0.points.count

        with Layout("Transformation in moving frame along Y"):
            blue_line0.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz).event
            red_line0.points.position  = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz).event

            blue_line0.points.store("Distance", nd.spline_parameter.factor*beta_y*duration)

        red_line0.points[rep.index].store("Distance", 0.)
        with Layout("Proper distance"):
            start_event = red_line0.points.sample_index(nd.position, index=0)
            with Repeat(red_line0=red_line0, event=start_event, s=0., index=1, iterations=resolution - 1) as rep:
                loc = red_line0.points.sample_index(nd.position, rep.index)
                tan = red_line0.points.sample_index(nd.curve_tangent, rep.index)

                speed, beta = normalize_speed(tan, use_lorentz)
                alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1- beta**2))
                ds = (Vector((loc.x, loc.y, 0)) - (rep.event.x, rep.event.y, 0)).length
                s = rep.s + ds*alpha

                rep.red_line0.points[rep.index].store("Distance", s)
                rep.event = loc
                rep.s = s
                rep.index += 1

            red_line0 = rep.red_line0

        red_line0_rot  = Curve(red_line0).transform(rotation=(0, 0, -halfpi))

        blue_line1 = GroupF().accelerated_transformation(accelerated=red_line0_rot, uniform_speed=(beta_y, 0, 1), x_along_speed=True, resolution=resolution, lorentz=use_lorentz).curve
        x = blue_line1.points.sample_index(Float.Named("Distance"), index=nd.index)
        t = blue_line1.points.sample_index(nd.position.z, index=nd.index)

        red_line1.points.position = (x, 0, t)
        red_line1.points.store("Distance", x)

        blue_line1.points.offset = (x, 0, 0)

        blue_line1.transform(rotation=(0, 0, halfpi))
        red_line1.transform(rotation=(0, 0, halfpi))

        # -----------------------------------------------------------------------------------------------------------------------------
        # Finalization

        with Layout("Frame change"):
            blue_line = Curve(blue_line0)
            red_line  = Curve(red_line0)

            blue_line.points.position = nd.position.mix(factor, blue_line1.points.sample_index(nd.position, index=nd.index))
            red_line.points.position  = nd.position.mix(factor, red_line1.points.sample_index(nd.position, index=nd.index))

        with Layout("Trim and time scale"):
            blue_line = GroupF().vertical_cut(curve=blue_line, cut=end).curve
            red_line  = GroupF().vertical_cut(curve=red_line, cut=end).curve

            blue_line.transform(scale=(1, 1, time_scale))
            red_line.transform(scale=(1, 1, time_scale))

        # Done

        (blue_line + red_line).out("Both")

        blue_line.out("Blue Line")
        red_line.out("Red Line")

        blue_line0.out("Blue Line 0")
        red_line0.out("Red Line 0")
        blue_line1.out("Blue Line 1")
        red_line1.out("Red Line 1")


    # =============================================================================================================================
    # Done

    print(f"Relativity Geometry Nodes built : {Tree._total_nodes} nodes, {Tree._total_links} links")
    print()
