#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : demos/relativity
-------------------------
Generates modifiers for special relativity

The space-time is (x, y, z=t) : space in 2D plus time dimension on z axis

Geometry Nodes
--------------
    - "Plane Line Intersection" (group) : intersection between a line and a plane
    - "Frame Change" (group) : Change position and direction to align X axis along the given direction
    - "Galilean Transformation" (group) : Galilean transformation
    - "Lorentz Transformation" (group) : Lorentz transformation
    - "Transformation" (group) : Lorentz or Galilean transformation
    - "Simulateneity Plane" (group): Compute the simultaneity plane of event + speed
    - "Simultaneity Intersection" (modifier) : Compute the intersection of the simultaneity plane with the provided curve
    - "Accelerated Transformation" (modifier) : transform a uniform motion into an accelerated frame defined a curve in (x, y, t=z) space time
    - "Rounded Triangle" (group) : function t -> (x, y) producing a triangle with a rounded summit

updates
-------
- creation : 2024/08/25
"""

from pathlib import WindowsPath
from bpy.types import Attribute
from ..geonodes import *
from .. import shadernodes as sh

DEBUG = True
SPEED_FWD = True

def demo():

    print('-'*100)

    Tree._reset_counters()

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

        event    = Vector(0, "Event")
        origin   = Vector(0, "Origin")
        x_axis   = Vector((1, 0, 0), "X Axis")
        pos_dir  = Vector((0, 0, 0), "Positive Direction")
        reverse  = Boolean(False, "Reverse")

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
    # Galilean Transformation

    with GeoNodes("Galilean Transformation", is_group=True):

        event    = Vector(0, "Event")
        speed    = Vector(0, "Speed")
        origin   = Vector(0, "Origin")
        reverse  = Boolean(False, "Reverse")

        # ---------------------------------------------------------------------------
        # Normalize speed

        with Layout("Speed (x, y)"):
            speed = Vector((speed.x, speed.y, 0))

        # ---------------------------------------------------------------------------
        # Transformations

        with Layout("Direct"):
            d_event_ = event - origin
            t = d_event_.z
            d_event_ = rotation @ (d_event_ - speed*t)

        with Layout("Reverse"):
            t = event.z
            r_event_ = origin + (inverse @ event) + speed*t

        event_ = d_event_.switch(reverse, r_event_)

        event_.out("Event")

    # =============================================================================================================================
    # Lorentz Transformation

    with GeoNodes("Lorentz Transformation", is_group=True):

        event    = Vector(0, "Event")
        speed    = Vector(0, "Speed")
        origin   = Vector(0, "Origin")
        reverse  = Boolean(False, "Reverse")

        with Layout("Normalize speed"):
            speed = speed.switch(speed.z.equal(0), Vector((speed.x, speed.y, 1))).normalize()._lc("Speed")
            beta  = gnmath.min(Vector((speed.x, speed.y, 0)).length/speed.z, .999)

            ag = gnmath.atan2(speed.y, speed.x)

            rotation = Rotation.FromAxisAngle((0, 0, 1), -ag)
            inverse  = rotation.invert()

        with Layout("Gamma"):
            gamma = (1 - beta**2)**(-.5)

        # ---------------------------------------------------------------------------
        # Transformations

        with Layout("Direct"):
            evt = rotation @ (event - origin)
            x, y, t = evt.x, evt.y, evt.z
            t_ = gamma*(t - beta*x)
            x_ = gamma*(x - beta*t)
            d_event_ = inverse @ Vector((x_, y, t_))

        with Layout("Reverse"):
            evt = rotation @ event
            x, y, t = evt.x, evt.y, evt.z
            t_ = gamma*(t + beta*x)
            x_ = gamma*(x + beta*t)
            r_event_ = origin + (inverse @ Vector((x_, y, t_)))

        event_ = d_event_.switch(reverse, r_event_)

        event_.out("Event")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Galilean / Lorentz transformation

    with GeoNodes("Transformation", is_group=True):

        event    = Vector(0, "Event")
        speed    = Vector(0, "Speed")
        origin   = Vector(0, "Origin")
        reverse  = Boolean(False, "Reverse")

        use_lorentz = Boolean(True, "Lorentz", tip="Lorentz (True) or Galilean (False)")

        g_node = Group("Galilean Transformation")
        g_node.plug_node_into()

        l_node = Group("Lorentz Transformation")
        l_node.plug_node_into()

        event = g_node.event.switch(use_lorentz, l_node.event)

        event.out("Event")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Combine speeds

    with GeoNodes("Combine Speeds", is_group=True):

        u = Vector(0, "u")
        v = Vector(0, "v")
        lor = Boolean(True, "Lorentz")

        u = u.switch(u.z.equal(0), (u.x, u.y, 1))
        v = v.switch(v.z.equal(0), (v.x, v.y, 1))

        w = GroupF().transformation(event=v, speed=u, lorentz=lor, reverse=True).event
        w = Vector((w.x/w.z, w.y/w.z, 1))

        w.out("w")

    # =============================================================================================================================
    # Simultaneity plane of a point and speed direction

    with GeoNodes("Simultaneity Plane", is_group=True):

        event        = Vector(0, "Event")
        speed        = Vector(0, "Speed")
        use_lorentz  = Boolean(True, "Lorentz", tip="Lorentz (True) or Galilean (False)")

        with Layout("Normalize Speed"):
            speed = speed.switch(speed.z.equal(0), Vector((speed.x, speed.y, 1))).normalize()._lc("Normalized speed")

        with Layout("Simultaneity plane angle"):
            k = Vector((0, 0, 1))
            perp = k.cross(speed)
            ag = gnmath.asin(perp.length)._lc("Angle")

        with Layout("Perpendicular vector to simultaneity plane"):
            plane = Rotation.FromAxisAngle(perp, -ag) @ k
            plane = k.switch(use_lorentz, plane)

        with Layout("Beta"):
            beta = (speed*(1, 1, 0)).length/speed.z

        # ----- Out

        plane.out("Plane")
        beta.out("Beta")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Simultaneity plane of a point and speed direction

    with GeoNodes("Simultaneity Intersection"):

        curve = Curve()

        event  = Vector(0, "Event")
        speed  = Vector(0, "Speed")
        use_lorentz = Boolean(True, "Lorentz", tip="Lorentz (True) or Galilean (False)")
        size = Float(100, "Size")

        plane_node = Group("Simultaneity Plane", {"Event": event, "Speed": speed, "Lorentz": use_lorentz})
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
        plane_perp.out("Simultaneity Plane")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Accelerated transformation of a uniform motion
    #
    # Uniform motion is the z axis
    # We need the intersection of the simultaneity plane with the z axis

    with GeoNodes("Accelerated Transformation"):

        curve       = Curve(None,   "Accelerated")
        start       = Vector(0,     "Uniform Event")
        speed       = Vector(0,     "Uniform Speed")
        count       = Integer(100,  "Resolution", 2, tip="Resolution")
        use_lorentz = Boolean(True, "Lorentz", tip="Lorentz (True) or Galilean (False)")

        if DEBUG:
            with_debug = Boolean(False, "Debug")
        else:
            with_debug = False

        with Layout("Normalize Speed"):
            speed = speed.switch(speed.z.equal(0), Vector((speed.x, speed.y, 1)))
            speed = speed.switch(use_lorentz, speed.normalize())

        with Layout("Prepare"):
            curve.splines.resolution=10*count
            curve = curve.resample(count)
            transf = Curve.Line().resample(count)

        with Layout("Start time"):
            loc = curve.points.sample_index(nd.position, index=0)
            start_time = loc.z

        debug = Curve.Line().resample(count)

        with Repeat(transf=transf, debug=debug, time=start_time, proper_time=0., index=0, iterations=count) as rep:

            with Layout("Current event and tangent"):
                loc = curve.points.sample_index(nd.position, index=rep.index)
                tan = curve.points.sample_index(nd.curve_tangent, index=rep.index)

            sim_node = GroupF().simultaneity_plane(event=loc, speed=tan, lorentz=use_lorentz)

            beta = sim_node.beta
            axis_event = GroupF().plane_line_intersection(
                plane_origin = loc,
                plane_vector = sim_node.plane,
                line_origin  = start,
                line_vector  = speed).event

            # Into accelerated frame
            local_axis_event = GroupF().transformation(event=axis_event, speed=tan, origin=loc, lorentz=use_lorentz).event
            local_axis_event = GroupF().frame_change(event=local_axis_event, origin=loc, x_axis=tan).event

            if DEBUG:
                rep.debug += Curve.Line(loc, axis_event)

            with Layout("Alpha = 1/Gamma"):
                alpha = gnmath.sqrt(1 - beta**2).switch(-use_lorentz, 1)._lc("Alpha")

            with Layout("Update proper time"):
                dt = loc.z - rep.time
                proper_time = (rep.proper_time + dt*alpha)._lc("Proper Time")

            local_event = Vector((local_axis_event.x, local_axis_event.y, proper_time))

            rep.transf.points[rep.index].position = local_event
            rep.transf.points[rep.index].store("Beta", beta)
            rep.transf.points[rep.index].store("Alpha", alpha)

            rep.time = loc.z
            rep.proper_time = proper_time
            rep.index += 1

        transf = rep.transf
        debug  = rep.debug


        if DEBUG:
            transf = transf + debug.switch(-with_debug)

        transf.out()

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

    with GeoNodes("Twins OLD"):

        beta_x      = Float.Factor(.8,   "Beta along x", -.999, .999, tip="Speed back and forth along X axis")
        beta_y      = Float.Factor(.4,   "Beta along y", -.999, .999, tip="Constant speed along Y axis")
        duration    = Float.Time(10,     "Duration", 1, tip="Experiment duration")
        u_turn      = Float.Factor(.2,   "U Turn duration", 0.001, 1, tip="Time spent for U turn in % of total duration")
        count       = Integer(20,        "Resolution", 2, 10000, tip="Number of points")
        use_lorentz = Boolean(True,   "Lorentz", tip="Special relativity")

        resolution = 2*count + 1

        with Layout("Combine Speed"):
            w = GroupF().combine_speeds(u=(beta_x, 0, 1), v=(0, beta_y, 1), lorentz=use_lorentz).w
            beta_x = w.x
            beta_y = w.y

        blue_line0 = Curve.Line((0, 0, 0), (0, 0, duration)).resample(resolution)
        red_line0  = Curve(blue_line0)
        blue_line1 = Curve.Line(0, 0).resample(resolution)
        red_line1  = Curve(blue_line1)

        dt = duration/(resolution - 1)
        acc_index = gnmath.min(round(count*(1 - u_turn)), count-1)

        with Repeat(
                red_line0   = red_line0,
                blue_line1  = blue_line1,
                red_line1   = red_line1,

                debug  = Cloud.Points(count=resolution),
                curves = Cloud.Points(count=1),

                beta        = beta_x,
                red_event0  = Vector(),
                red_event1  = Vector(),

                index       = 1,
                iterations  = resolution - 1) as rep:

            with Layout("Current Speed"):
                beta0 = rep.index.map_range_linear(acc_index, count, beta_x, 0)
                beta1 = rep.index.map_range_linear(count, resolution - 1 - acc_index, 0, -beta_x)
                new_beta = beta0.switch(rep.index > count, beta1)

                beta = ((rep.beta + new_beta)/2)._lc("Beta")
                rep.beta = new_beta

                speed = Vector((beta, 0, 1))._lc("Speed")

            with Layout("Alpha = 1/gamma"):
                alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1 - beta**2))._lc("Alpha")
                dt_alpha = (dt*alpha)._lc("dt_alpha")

            with Layout("Red Line 0"):
                red_event0 = rep.red_event0 + (beta*dt, 0, dt)
                rep.red_line0.points[rep.index].position = red_event0
                rep.red_event0 = red_event0

                rep.debug.points[rep.index].position = red_event0

            with Layout("Red Line 1"):
                red_event1 = rep.red_event1 + (0, 0, dt_alpha)
                rep.red_line1.points[rep.index].position = red_event1
                rep.red_event1 = red_event1

            with Layout("Blue Line 1"):
                sim_plane   = GroupF().simultaneity_plane(event=red_event0, speed=speed, lorentz=use_lorentz).plane
                evt = GroupF().plane_line_intersection(plane_origin=red_event0, plane_vector=sim_plane).event
                evt = GroupF().transformation(event=evt, speed=speed, origin=red_event0, lorentz=use_lorentz).event
                evt += (0, 0, red_event1.z)

                blue_event1 = GroupF().frame_change(event = evt, x_axis=speed, positive_direction=(1, 0, 0)).event
                rep.blue_line1.points[rep.index].position = blue_event1

            rep.index += 1

        red_line0  = rep.red_line0
        red_line1  = rep.red_line1
        blue_line1 = rep.blue_line1

        debug = rep.debug
        curves = rep.curves

        with Layout("Transformation in Y moving Frame"):

            blue_line0.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)
            red_line0.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)
            red_line1.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)
            blue_line1.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)

        # Space orientation along x

        last_evt = blue_line0.points.sample_index(nd.position, index=resolution-1)
        time_ratio = last_evt.z/last_evt.y

        with Repeat(blue_line1=blue_line1, debug=Cloud.Points(resolution), curves=Cloud.Points(1), index=1, iterations=resolution - 2) as rep:
            red_loc = red_line0.points.sample_index(nd.position, index=rep.index)
            red_tan = red_line0.points.sample_index(nd.curve_tangent, index=rep.index)
            blue_loc = blue_line0.points.sample_index(nd.position, index=rep.index)

            rep.curves += Curve.Line(red_loc, blue_loc)
            rep.curves += Curve.Line(red_loc, red_loc + red_tan*(3, 3, 0))

            #ag = gnmath.atan2(red_tan.y, red_tan.x)
            ag = gnmath.atan2(red_tan.x, red_tan.y)
            rep.debug.points[rep.index].store("AG", gnmath.degrees(ag))
            rot = Rotation.FromEuler((0, 0, ag))

            plane = GroupF().simultaneity_plane(speed=red_tan, lorentz=use_lorentz).plane
            rot_sim = Rotation.AlignZToVector(plane)
            #rot = rot_sim @ rot
            #rep.curves += Curve.Line(red_loc, red_loc + (rot @ red_tan)*(3, 3, 0))


            O = red_line1.points.sample_index(nd.position, index=rep.index)
            blue_loc = O + (rot @ (blue_loc - red_loc))

            rep.curves += Curve.Line(O, blue_loc)


            #blue_loc = (rot @ (blue_loc - red_loc)) + (0, 0, red_line1.points.sample_index(nd.position, index=rep.index).z)
            rep.blue_line1.points[rep.index].position = blue_loc

            if False:
                # loc + k*dir -> x = 0
                # k = -loc/dir

                k = loc.x/tan.y
                y = loc.y - k*tan.x

                evt = (0, y, y*time_ratio)
                rep.debug.points[rep.index].position = evt

                if True:
                    evt = GroupF().transformation(event=evt, speed=tan, origin=loc*(1, 1, 0), lorentz=use_lorentz).event
                    #evt = (evt.x, evt.y, loc.z)

                    blue_event1 = GroupF().frame_change(event = evt, x_axis=tan, positive_direction=(0, 1, 0)).event
                    rep.blue_line1.points[rep.index].position = blue_event1

            rep.index += 1

        blue_line1 = rep.blue_line1

        debug = rep.debug
        curves = rep.curves

        # Done

        blue_line0.out("Blue Line 0")
        red_line0.out( "Red Line 0")
        blue_line1.out("Blue Line 1")
        red_line1.out( "Red Line 1")

        debug.out("Debug")
        curves.out("Curves")


    # =============================================================================================================================
    # Twins

    with GeoNodes("Twins"):

        beta_x      = Float.Factor(.8,   "Beta along x", -.999, .999, tip="Speed back and forth along X axis")
        beta_y      = Float.Factor(.4,   "Beta along y", -.999, .999, tip="Constant speed along Y axis")
        duration    = Float.Time(10,     "Duration", 1, tip="Experiment duration")
        u_turn      = Float.Factor(.2,   "U Turn duration", 0.001, 1, tip="Time spent for U turn in % of total duration")
        count       = Integer(20,        "Resolution", 2, 10000, tip="Number of points")
        use_lorentz = Boolean(True,      "Lorentz", tip="Special relativity")

        resolution = 2*count + 1

        with Layout("Combine Speed"):
            w = GroupF().combine_speeds(u=(beta_x, 0, 1), v=(0, beta_y, 1), lorentz=use_lorentz).w
            beta_x = w.x
            beta_y = w.y

        blue_line0 = Curve.Line((0, 0, 0), (0, beta_y*duration, duration)).resample(resolution)
        red_line0  = Curve(blue_line0)
        blue_line1 = Curve.Line(0, 0).resample(resolution)
        red_line1  = Curve(blue_line1)

        dt = duration/(resolution - 1)
        acc_index = gnmath.min(round(count*(1 - u_turn)), count-1)

        with Repeat(
                red_line0   = red_line0,
                blue_line1  = blue_line1,
                red_line1   = red_line1,

                debug  = Cloud.Points(count=resolution),
                curves = Cloud.Points(count=1),

                beta        = beta_x,
                red_event0  = Vector(),
                red_event1  = Vector(),

                index       = 1,
                iterations  = resolution - 1) as rep:

            with Layout("Current Speed"):
                beta0 = rep.index.map_range_linear(acc_index, count, beta_x, 0)
                beta1 = rep.index.map_range_linear(count, resolution - 1 - acc_index, 0, -beta_x)
                new_beta = beta0.switch(rep.index > count, beta1)

                beta = ((rep.beta + new_beta)/2)._lc("Beta")
                rep.beta = new_beta

                speed = Vector((beta, beta_y, 0))
                speed_norm = speed.length._lc("Speed Norm")
                speed = (speed + (0, 0, 1))._lc("Speed")

            with Layout("Alpha = 1/gamma"):
                alpha = Float.Switch(use_lorentz, 1, gnmath.sqrt(1 - beta**2))._lc("Alpha")
                dt_alpha = (dt*alpha)._lc("dt_alpha")

            with Layout("Red Line 0"):
                red_event0 = rep.red_event0 + speed*dt
                rep.red_line0.points[rep.index].position = red_event0
                rep.red_event0 = red_event0

                rep.debug.points[rep.index].position = red_event0

            with Layout("Red Line 1"):
                red_event1 = rep.red_event1 + (0, speed_norm*dt_alpha, dt_alpha)
                rep.red_line1.points[rep.index].position = red_event1
                rep.red_event1 = red_event1

            with Layout("Blue Line 1"):

                with Layout("Where is the blue twin ?"):
                    sim_plane   = GroupF().simultaneity_plane(event=red_event0, speed=speed, lorentz=use_lorentz).plane
                    evt = GroupF().plane_line_intersection(plane_origin=red_event0, plane_vector=sim_plane, line_vector=(0, beta_y, 1)).event

                    #rep.curves += Curve.Line(red_event0, evt)

                with Layout("Transform in the red space"):
                    evt = GroupF().transformation(event=evt, speed=speed, origin=red_event0, lorentz=use_lorentz).event
                    rep.curves += Curve.Line(red_event1, red_event1 + evt)

                with Layout("Orient axes along the space speed"):
                    ag = gnmath.atan2(beta, beta_y)
                    rot = Rotation.FromEuler((0, 0, ag))

                    blue_event1 = red_event1 + (rot @ evt)
                    rep.blue_line1.points[rep.index].position = blue_event1

                    rep.curves += Curve.Line(red_event1, blue_event1)

            rep.index += 1

        red_line0  = rep.red_line0
        red_line1  = rep.red_line1
        blue_line1 = rep.blue_line1

        debug = rep.debug
        curves = rep.curves

        """

        with Layout("Transformation in Y moving Frame"):

            blue_line0.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)
            red_line0.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)
            red_line1.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)
            blue_line1.points.position = GroupF().transformation(event=nd.position, speed=(0, -beta_y, 1), lorentz=use_lorentz)

        # Space orientation along x

        last_evt = blue_line0.points.sample_index(nd.position, index=resolution-1)
        time_ratio = last_evt.z/last_evt.y

        with Repeat(blue_line1=blue_line1, debug=Cloud.Points(resolution), curves=Cloud.Points(1), index=1, iterations=resolution - 2) as rep:
            red_loc = red_line0.points.sample_index(nd.position, index=rep.index)
            red_tan = red_line0.points.sample_index(nd.curve_tangent, index=rep.index)
            blue_loc = blue_line0.points.sample_index(nd.position, index=rep.index)

            rep.curves += Curve.Line(red_loc, blue_loc)
            rep.curves += Curve.Line(red_loc, red_loc + red_tan*(3, 3, 0))

            #ag = gnmath.atan2(red_tan.y, red_tan.x)
            ag = gnmath.atan2(red_tan.x, red_tan.y)
            rep.debug.points[rep.index].store("AG", gnmath.degrees(ag))
            rot = Rotation.FromEuler((0, 0, ag))

            plane = GroupF().simultaneity_plane(speed=red_tan, lorentz=use_lorentz).plane
            rot_sim = Rotation.AlignZToVector(plane)
            #rot = rot_sim @ rot
            #rep.curves += Curve.Line(red_loc, red_loc + (rot @ red_tan)*(3, 3, 0))


            O = red_line1.points.sample_index(nd.position, index=rep.index)
            blue_loc = O + (rot @ (blue_loc - red_loc))

            rep.curves += Curve.Line(O, blue_loc)


            #blue_loc = (rot @ (blue_loc - red_loc)) + (0, 0, red_line1.points.sample_index(nd.position, index=rep.index).z)
            rep.blue_line1.points[rep.index].position = blue_loc

            if False:
                # loc + k*dir -> x = 0
                # k = -loc/dir

                k = loc.x/tan.y
                y = loc.y - k*tan.x

                evt = (0, y, y*time_ratio)
                rep.debug.points[rep.index].position = evt

                if True:
                    evt = GroupF().transformation(event=evt, speed=tan, origin=loc*(1, 1, 0), lorentz=use_lorentz).event
                    #evt = (evt.x, evt.y, loc.z)

                    blue_event1 = GroupF().frame_change(event = evt, x_axis=tan, positive_direction=(0, 1, 0)).event
                    rep.blue_line1.points[rep.index].position = blue_event1

            rep.index += 1

        blue_line1 = rep.blue_line1

        debug = rep.debug
        curves = rep.curves
        """

        # Done

        blue_line0.out("Blue Line 0")
        red_line0.out( "Red Line 0")
        blue_line1.out("Blue Line 1")
        red_line1.out( "Red Line 1")

        debug.out("Debug")
        curves.out("Curves")


























    # =============================================================================================================================
    # Done

    print(f"Relativity Geometry Nodes built : {Tree._total_nodes} nodes, {Tree._total_links} links")
    print()
