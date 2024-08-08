#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : demos/explosion
------------------------
Explode points from the points of the initial geometry.
The particles can be either generated or taken from a collection.

updates
-------
- creation : 2024/08/02
"""


import numpy as np

from ..geonodes import *

def demo():

    # =============================================================================================================================
    # Simulate gravity on particles with an initial speed

    with GeoNodes("Gravity"):

        # ----- Input sockets

        frame0    = Integer(1, "Start Frame")
        gravity   = Vector.Acceleration((0, 0, -9.86), "Gravity", tip="Gravity vector")
        vis_fac   = Float(0, "Viscosity factor")
        vis_exp   = Float(2, "Viscosity exponent")
        speed_max = Float(2, "Maximum Speed", tip="Used to generate random speed is named attribute 'Speed' is not defined")
        seed      = Integer(name="Seed")

        # ----- Input geometry is supposed to be points

        points = Cloud(name="Points", tip="Geometry with points")

        # ----- Initialization

        with Layout("Initial speed and rotation"):
            speed = Vector.Named("Speed")
            speed = speed.switch(-speed.exists_, Vector.Random(-speed_max, speed_max, seed=seed))
            speed.store(points.points, "Speed")

            rotation = Vector.Named("Rotation")
            rotation = Vector.Random(0, tau, seed=seed+1).switch(rotation.exists_, rotation)
            rotation.store(points.points, "Rotation")

            omega = Vector.Random(0, tau, seed=seed+2)

        with Simulation(points=points, speed=speed) as sim:

            sim.skip = nd.scene_time.frame.less_than(frame0)

            dt = sim.delta_time

            with Layout("Speed"):
                old_speed = sim.points.points.capture(sim.speed)

                with Layout("Viscosity"):
                    speed_norm = old_speed.length
                    force = vis_fac*speed_norm**vis_exp
                    force = gnmath.min(force, speed_norm/dt)
                    viscosity = old_speed.normalize().scale(-force*dt)

                acc = (gravity + viscosity._lc("Viscostiy"))._lc("Acceleration")

                new_speed = old_speed + acc*dt

                sim.points.points.offset = (old_speed + new_speed)*dt

            sim.speed = new_speed

            with Layout("Rotation"):
                old_rot = Rotation(Vector.Named("Rotation"))
                new_rot = old_rot.rotate(omega*dt)
                new_rot = Vector(new_rot).store(sim.points.points, "Rotation")

        sim.points.out()

    # =============================================================================================================================
    # Explode particles places on the input mesh

    with GeoNodes("Explosion"):

        frame0    = Integer(1, "Start frame")
        gravity   = Vector.Acceleration((0, 0, -9.86), "Gravity", tip="Gravity vector")
        vis_fac   = Float(0, "Viscosity factor")
        vis_exp   = Float(2, "Viscosity exponent")
        density   = Float(50, "Particles density", 0, 100)
        max_speed = Float(5, "Maximum speed", 0)
        use_coll  = Boolean(False, "Use collection for particles")
        particles = Collection(None, "Particles collection")
        part_size = Float(.1, "Particles size")
        only_up   = Boolean(False, "Only up faces", tip="Put particles on faces with tangent in the upward direction")
        seed      = Integer(0, "Seed")

        with Layout("Generate the points on the input mesh"):
            selection = (nd.normal @ (0, 0, 1)).greater_than(0).switch(-only_up, True)
            points = Mesh().faces[selection].distribute_points(density=density, seed=seed)

        with Layout("Random speeds, aligned with normal plus some noise"):
            speed = points.normal_ * (max_speed * Float.Random(0, 1, seed=seed + 1))
            speed.store(points.points, "Speed")

        with Layout("Rotation aligned with normals"):
            rotation = Rotation.AlignToVector(points.normal_)
            rotation.store(points.points, "Rotation")

        with Layout("Gravity loop"):
            simul = Group("Gravity",
                    {'Points': points,
                     'Start Frame': frame0,
                     'Gravity': gravity,
                     'Viscosity factor': vis_fac,
                     'Viscosity exponent': vis_exp,
                    })
            points = Cloud(simul.geometry)

        with Layout("Instances coming from collection"):
            coll_parts = particles.info(separate_children=True).instances

        with Layout("Randomly generated instances"):

            for i, count in enumerate((4, 3, 2, 1)):
                verts = i + 3
                with Layout(f"{count} polys of {verts} vertices"):

                    poly  = Mesh.Circle(radius=part_size, vertices=verts, fill_type='NGON')
                    polys = Cloud.Points(count=count).points.instance_on(poly)
                    polys.insts.scale = Vector.Random(.5, 1.5, seed=200+i)

                    if i == 0:
                        rand_parts = polys
                    else:
                        rand_parts += polys

            mesh_parts = Mesh(rand_parts.realize())
            mesh_parts.points.offset = Vector.Random((-1, -1, 0), (1, 1, 0), seed=1000+seed)*(part_size/1)
            mesh_parts = macros.solidify(mesh_parts, thickness=part_size/10, individual=True, merge_distance=0)

            rand_parts = mesh_parts.points.split_to_instances(group_id=mesh_parts.island_index)

        parts = rand_parts.switch(use_coll, coll_parts)

        with Layout("Put particles on the points and rotate with Rotation attribute"):
            insts = parts.on_points(points, pick_instance=True)
            insts.insts.rotation = points.points.sample_index(Vector.Named("Rotation"), nd.index)

        with Layout("Final geometry"):
            insts.switch(nd.scene_time.frame.less_than(frame0), Mesh()).out('Geometry')
