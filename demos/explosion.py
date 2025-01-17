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

module : demo explosion
-----------------------

Simulation zone demo

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/explosion.py)

A simple demo of a ***Simulation*** zone.

Explode points from the points of the initial geometry.
The particles can be either generated or taken from a collection.

> [!NOTE]
> Modifiers:
> - Explosion

``` python
from geonodes.demos import explosion

explosion.demo()
```
"""

import numpy as np

from geonodes import *
from geonodes import macros

def demo():

    # =============================================================================================================================
    # Simulate gravity on particles with an initial speed

    with GeoNodes("Gravity"):

        # ----- Input sockets

        with Panel("Gravity"):
            #gravity   = Vector.Acceleration((0, 0, -9.86), "Gravity", tip="Gravity vector")
            gravity   = Vector.Acceleration((0, 0, -9.86), "Gravity", tip="Gravity vector", single_value=True)
            vis_fac   = Float(0, "Viscosity Factor", single_value=True)
            vis_exp   = Float(2, "Viscosity Exponent", single_value=True)
            speed_max = Float(10, "Maximum Speed", tip="Used to generate random speed is named attribute 'Speed' is not defined", single_value=True)

        frame0 = Integer(1, "Start Frame", single_value=True)
        seed   = Integer(name="Seed", single_value=True)

        # ----- Input geometry is supposed to be points

        cloud = Cloud(name="Points", tip="Geometry with points")

        # ----- Initialization

        with Layout("Initial speed and rotation"):
            speed = Vector.Named("Speed")
            speed = speed.switch(-speed.exists_, Vector.Random(-speed_max, speed_max, seed=seed))
            cloud.points.store("Speed", speed)

            rotation = Vector.Named("Rotation")
            rotation = Vector.Random(0, tau, seed=seed+1).switch(rotation.exists_, rotation)
            cloud.points.store("Rotation", rotation)

            omega = Vector.Random(0, tau, seed=seed+2)

        with Simulation(cloud=cloud, speed=speed) as sim:

            sim.skip = nd.scene_time().frame.less_than(frame0)

            dt = sim.delta_time

            with Layout("Speed"):
                old_speed = sim.cloud.points.capture(sim.speed)

                with Layout("Viscosity"):
                    speed_norm = old_speed.length()
                    force = vis_fac*speed_norm**vis_exp
                    force = gnmath.min(force, speed_norm/dt)
                    viscosity = old_speed.normalize().scale(-force*dt)

                acc = (gravity + viscosity._lc("Viscostiy"))._lc("Acceleration")

                new_speed = old_speed + acc*dt

                sim.cloud.offset = (old_speed + new_speed)*dt

            sim.speed = new_speed

            with Layout("Rotation"):
                old_rot = Rotation(Vector.Named("Rotation"))
                new_rot = old_rot.rotate(omega*dt)
                sim.cloud.points.store("Rotation", new_rot)

        sim.cloud.out()

    # =============================================================================================================================
    # Explode particles places on the input mesh

    with GeoNodes("Explosion"):

        with Panel("Particles"):
            density   = Float(50, "Particles density", 0, 100, single_value=True)
            use_coll  = Boolean(False, "Use collection for particles", single_value=True)
            particles = Collection(None, "Particles collection")
            part_size = Float(.1, "Particles size")
            only_up   = Boolean(False, "Only up faces", tip="Put particles on faces with tangent in the upward direction", single_value=True)
            seed      = Integer(0, "Seed", single_value=True)

        with Panel("Gravity"):
            max_speed = Float(5, "Maximum Speed", 0, single_value=True)

        with Layout("Generate the points on the input mesh"):
            selection = (nd.normal @ (0, 0, 1)).greater_than(0).switch(-only_up, True)
            cloud = Mesh()[selection].distribute_points_on_faces(density=density, seed=seed)
            normal = cloud.normal_

        with Layout("Random speeds, aligned with normal plus some noise"):
            speed = normal * (max_speed * Float.Random(0, 1, seed=seed + 1))
            cloud.points._Speed = speed

        with Layout("Rotation aligned with normals"):
            cloud.points._Rotation = Rotation.AlignToVector(normal)

        with Layout("Gravity loop"):
            simul = Group("Gravity",
                    {'Points': cloud,
                     'Seed' : seed.hash_value(119),
                    }, link_from='TREE')
            cloud = Cloud(simul.geometry)

        with Layout("Instances coming from collection"):
            coll_parts = particles.info(separate_children=True).instances

        with Layout("Randomly generated instances"):

            for i, count in enumerate((4, 3, 2, 1)):
                verts = i + 3
                with Layout(f"{count} polys of {verts} vertices"):

                    poly  = Mesh.Circle(radius=part_size, vertices=verts, fill_type='NGON')
                    polys = Cloud.Points(count=count).instance_on(poly)
                    polys.insts.scale = Vector.Random(.5, 1.5, seed=200 + i)

                    if i == 0:
                        rand_parts = polys
                    else:
                        rand_parts += polys

            mesh_parts = Mesh(rand_parts.realize())
            mesh_parts.offset = Vector.Random((-1, -1, 0), (1, 1, 0), seed=1000+seed)*(part_size/1)
            mesh_parts = macros.solidify(mesh_parts, thickness=part_size/10, individual=True, merge_distance=0)

            rand_parts = mesh_parts.points.split_to_instances(group_id=mesh_parts.island_index)

        parts = rand_parts.switch(use_coll, coll_parts)

        with Layout("Put particles on the points and rotate with Rotation attribute"):
            insts = cloud.instance_on(instance=parts, pick_instance=True)
            insts.insts.rotation = cloud.points.sample_index(Vector("Rotation"), nd.index)

        with Layout("Final geometry"):
            insts.switch(nd.scene_time().frame.less_than(frame0), Mesh()).out('Geometry')
