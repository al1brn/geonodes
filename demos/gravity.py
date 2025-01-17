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

module : demo gravity
---------------------

Simulate Newton gravity law between planets. The planets wan merge when colliding.
A central sun can be created.

updates
-------
- creation :   2024/08/03
- update : 2025/01/16

$ DOC START

[Source Code](../demos/gravity.py)

Simulate Newton gravity law between planets. The planets can merge when colliding.
A central sun can be created.

Simulation can be run in 2D or 3D.

> [!NOTE]
> Modifiers:
> - A Tree
> - Trees Collection
> - Forest
> - Forest Demo

``` python
from geonodes.demos import gravity

gravity.demo()
```
"""

from geonodes import *

# ====================================================================================================
# Newton's law simulation

def demo():

    with ShaderNodes("Planet"):

        ped = Shader.Principled(
            base_color = Color.CombineHSV(snd.attribute("Hue", attribute_type='INSTANCER').fac, .8, .9),
            roughness  = .3,
            metallic   = .2,
        )

        ped.out()


    with GeoNodes("Gravity"):

        with Panel("Planets"):
            planets_count = Integer(500, "Planets count", 1)
            material      = Material("Planet", "Planets material")
            seed          = Integer(0, "Seed")

        with Panel("Dimensions"):
            space_size    = Float.Distance(100., "Initial Space Size")
            sun_ratio     = Float(100, "Sun ratio", 1, tip="Create a sun with the given ratio for mass")
            vis_radius    = Float.Distance(.3, "Planet radius", .01, tip="Actual radius is computed by multipliying by mass**1/3")
            coll_radius   = Float.Distance(.1, "Collision radius", .01)

        with Panel("Gravity"):
            G             = Float(1, "G Constant", .001)
            max_mass      = Float(100, "Maximum mass", 1, tip="Mass is randomly generated between 1 and max_mass")
            max_speed     = Float(10, "Maximum velocity")

        with Panel("Options"):
            planar        = Boolean(False, "Planar")
            merge_planets = Boolean(True, "Merge planets", tip="Merge the planets when they collide")
            center_sun    = Boolean(False, "Center Sun", tip="Keep the sun at center")

        # ====================================================================================================
        # Initialization

        with Layout("Initialization"):

            position  = Vector.Random(-1, 1, seed=seed)*(space_size, space_size, space_size.switch(planar))
            speed     = Vector.Random(-1, 1, seed=seed+1).normalize()*(max_speed, max_speed, max_speed.switch(planar))
            mass      = Float.Random(1, max_mass, seed=seed+2)
            radius    = vis_radius * mass**(1/3)
            collision = coll_radius * mass**(1/3)

            planets = Cloud.Points(count=planets_count, position=position)
            planets.points._Mass      = mass
            planets.points._Collision = collision
            planets.points._Speed     = speed
            planets.points.radius     = radius
            planets.points._Hue       = Float.Random(0, 1, seed=seed + 3)
            planets.points._Sun       = nd.index.equal(0)

            with Layout("Sun"):
                sun_mass = max_mass*sun_ratio
                planets.points[0]._Mass = sun_mass
                planets.points[0]._Speed = Vector()
                planets.points[0]._Collision = coll_radius * sun_mass**(1/3)
                planets.points[0].radius = vis_radius * sun_mass**(1/3)
                planets.points[0].position = 0


        # ====================================================================================================
        # Simulation

        with Simulation(planets=planets) as sim:

            sim.planets.points._Acceleration = Vector()
            with Repeat(planets=sim.planets, iterations=sim.planets.points.count) as rep:

                center = sim.planets.points.sample_index(nd.position, index=rep.iteration)
                M      = sim.planets.points.sample_index(Float("Mass"), index=rep.iteration)

                v = center - nd.position
                r = gnmath.max(v.length(), .01)
                acc = v.scale(G*M*r**(-3))
                #rep.planets.points[nd.index.not_equal(rep.iteration)]._Acceleration = Vector("Acceleration") + acc
                rep.planets.points[nd.index.not_equal(rep.iteration)]._Acceleration += acc

            planets = rep.planets

            with Layout("Move the planets"):
                old_speed = Vector("Speed")
                new_speed = old_speed + Vector("Acceleration")*sim.delta_time
                planets.offset = (old_speed + new_speed)*(sim.delta_time/2)
                planets.points._Speed = new_speed

            # ====================================================================================================
            # Collisions

            with Layout("Planets who are both the nearest of the other"):

                merged = Cloud(planets)
                merged.points.store("IoN", nd.index_of_nearest(nd.position))
                ion = Integer("IoN")._lc("IoN")
                # ----- Index of nearest attribute of nearest planet
                nearest_ion = merged.points.sample_index(ion, ion)
                merged.points._Merge = merge_planets & nearest_ion.equal(nd.index)

                merge = Boolean("Merge")

            with Layout("Distance to nearest"):
                pos0 = nd.position
                pos1 = merged.points.sample_index(pos0, index=ion)
                dist = pos0.distance(pos1)

            with Layout("Collision distance"):
                coll0  = Float("Collision")
                coll1  = merged.points.sample_index(coll0, index=ion)
                coll   = gnmath.max(coll0, coll1)

            with Layout("Merge if distance less than collision distance"):
                merged.points._Merge = merge & dist.less_than(coll)

            with Layout("Merge the two planets"):
                mass0 = Float("Mass")
                mass1 = planets.points.sample_index(mass0, index=ion)
                mass = mass0 + mass1

                hue0 = Float("Hue")
                hue1 = planets.points.sample_index(hue0, index=ion)
                hue = hue0.switch(mass1.greater_than(mass0), hue1)

                collision = coll_radius * mass**(1/3)
                merged.points._Collision = collision
                merged.points.radius = vis_radius * mass**(1/3)

                merged.position = (mass0*pos0 + mass1*pos1)/mass

                speed0 = Vector("Speed")
                speed1 = merged.points.sample_index(speed0, index=ion)
                merged.points._Speed = (mass0*speed0 + mass1*speed1)/mass

                merged.points._Hue = hue

                # ----- Mass as last attributes depending upon the mass

                merged.points._Mass = mass

            with Layout("Delete merged planets and add newly created ones"):
                planets.points._Merge = merged.points.sample_index(Boolean("Merge"), index=nd.index)
                merged.points[nd.index.greater_than(Integer("IoN"))]._Merge = False

                planets = planets.points[Boolean("Merge")].delete()
                planets += merged.points[-Boolean("Merge")].delete()

            with Layout("Sun center"):
                no_center = Cloud(planets)
                sun = Cloud(planets)
                sun.points[sun.points.attribute_statistic(sun._Mass).max > 1.01*sun._Mass].delete()
                planets.transform(translation=-sun.points.sample_index(nd.position, 0))
                planets = no_center.switch(center_sun, planets)

            sim.planets = planets

        # ----- End of Simulation Loop

        planets = sim.planets
        planets.points._Sun = Float("Mass").equal(planets.points.attribute_statistic(Float("Mass")).max)

        # ====================================================================================================
        # Planet spheres

        sphere = Mesh.UVSphere()
        sphere.corners.store_uv("UV Map", sphere.uv_map_)
        sphere.faces.shade_smooth = True
        sphere.material = material
        spheres = planets.instance_on(sphere, scale=nd.radius)

        spheres.out()
