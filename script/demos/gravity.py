#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : demos/gravity
----------------------
Simulate Newton gravity law between planets. The planets wan merge when colliding.
A central sun can be created.

updates
-------
- creation : 2024/08/02
"""


from geonodes.script import *

# ====================================================================================================
# Newton's law simulation

def demo():

    with GeoNodes("Gravity"):

        planets_count = Integer(500, "Planets count", 1)
        max_mass      = Float(100, "Maximum mass", 1, tip="Mass is randomly generated between 1 and max_mass")
        sun_ratio     = Float(100, "Sun ratio", 1, tip="Create a sun with the given ratio for mass")
        space_size    = Float.Distance(100., "Initial Space Size")
        planar        = Boolean(False, "Planar")
        max_speed     = Float(10, "Maximum velocity")
        vis_radius    = Float.Distance(.3, "Planet radius", .01, tip="Actual radius is computed by multipliying by mass**1/3")
        G             = Float(1, "G Constant", .001)
        merge_planets = Boolean(True, "Merge planets", tip="Merge the planets when they collide")
        coll_radius   = Float.Distance(.1, "Collision radius", .01)
        material      = Material(None, "Planets material")
        seed          = Integer(0, "Seed")

        # ====================================================================================================
        # Initialization

        with Layout("Initialization"):

            position  = Vector.Random(-1, 1, seed=seed)*(space_size, space_size, space_size.switch(planar))
            speed     = Vector.Random(-1, 1, seed=seed+1).normalize()*(max_speed, max_speed, max_speed.switch(planar))
            mass      = Float.Random(1, max_mass, seed=seed+2)
            radius    = vis_radius * mass**(1/3)
            collision = coll_radius * mass**(1/3)

            planets = Cloud.Points(count=planets_count, position=position)
            planets.points.store("Mass", mass)
            planets.points.store("Collision", collision)
            planets.points.store("Speed", speed)
            planets.points.radius = radius
            planets.points.store("Hue", Float.Random(0, 1, seed=seed+3))
            planets.points.store("Sun", nd.index.equal(0))

            with Layout("Sun"):
                sun_mass = max_mass*sun_ratio
                planets.points[0].store("Mass", sun_mass)
                planets.points[0].store("Speed", Vector())
                planets.points[0].store("Collision", coll_radius * sun_mass**(1/3))
                planets.points[0].radius = vis_radius * sun_mass**(1/3)
                planets.points[0].position = 0


        # ====================================================================================================
        # Simulation

        with Simulation(planets=planets) as sim:

            sim.planets.points.store("Acceleration", Vector())
            with Repeat(planets=sim.planets, index=0, iterations=sim.planets.points.count) as rep:

                center = sim.planets.points.sample_index(nd.position, index=rep.index)
                M      = sim.planets.points.sample_index(Float.Named("Mass"), index=rep.index)

                v = center - nd.position
                r = gnmath.max(v.length, .01)
                acc = v.scale(G*M*r**(-3))
                rep.planets.points[nd.index.not_equal(rep.index)].store("Acceleration", Vector.Named("Acceleration") + acc)

                rep.index += 1

            planets = rep.planets

            with Layout("Move the planets"):
                old_speed = Vector.Named("Speed")
                new_speed = old_speed + Vector.Named("Acceleration")*sim.delta_time
                planets.points.offset = (old_speed + new_speed)*(sim.delta_time/2)
                planets.points.store("Speed", new_speed)

            # ====================================================================================================
            # Collisions

            with Layout("Planets who are both the nearest of the other"):

                merged = Cloud(planets)
                merged.points.store("IoN", nd.position.index_of_nearest())
                ion = Integer.Named("IoN")._lc("IoN")
                # ----- Index of nearest attribute of nearest planet
                nearest_ion = merged.points.sample_index(ion, ion)
                merged.points.store("Merge", merge_planets & nearest_ion.equal(nd.index))

                merge = Boolean.Named("Merge")

            with Layout("Distance to nearest"):
                pos0 = nd.position
                pos1 = merged.points.sample_index(pos0, index=ion)
                dist = pos0.distance(pos1)

            with Layout("Collision distance"):
                coll0  = Float.Named("Collision")
                coll1  = merged.points.sample_index(coll0, index=ion)
                coll   = gnmath.max(coll0, coll1)

            with Layout("Merge if distance less than collision distance"):
                merged.points.store("Merge", merge & dist.less_than(coll))

            with Layout("Merge the two planets"):
                mass0 = Float.Named("Mass")
                mass1 = planets.points.sample_index(mass0, index=ion)
                mass = mass0 + mass1

                hue0 = Float.Named("Hue")
                hue1 = planets.points.sample_index(hue0, index=ion)
                hue = hue0.switch(mass1.greater_than(mass0), hue1)

                collision = coll_radius * mass**(1/3)
                merged.points.store("Collision", collision)
                merged.points.radius = vis_radius * mass**(1/3)

                merged.points.position = (mass0*pos0 + mass1*pos1)/mass

                speed0 = Vector.Named("Speed")
                speed1 = merged.points.sample_index(speed0, index=ion)
                merged.points.store("Speed", (mass0*speed0 + mass1*speed1)/mass)

                merged.points.store("Hue", hue)

                # ----- Mass as last attributes depending upon the mass

                merged.points.store("Mass", mass)

            with Layout("Delete merged planets and add newly created ones"):
                planets.points.store("Merge", merged.points.sample_index(Boolean.Named("Merge"), index=nd.index))
                merged.points[nd.index.greater_than(Integer.Named("IoN"))].store("Merge", False)

                planets = planets.points[Boolean.Named("Merge")].delete()
                planets += merged.points[-Boolean.Named("Merge")].delete()

            sim.planets = planets

        # ----- End of Simulation Loop

        planets = sim.planets
        planets.points.store("Sun", Float.Named("Mass").equal(planets.points.attribute_statistic(Float.Named("Mass")).max))

        # ====================================================================================================
        # Planet spheres

        sphere = Mesh.UVSphere()
        sphere.corners.store("UV Map", sphere.uv_map_)
        sphere.faces.smooth = True
        sphere.faces.material = material
        spheres = planets.points.instance_on(sphere, scale=nd.radius)

        spheres.out()
