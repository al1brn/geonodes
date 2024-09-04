#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/08/02

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/rain
-------------------
Simulates rain falling on a terrain.
The input geometry is a terrain with holes containing water
The dips falling in the holes produce waves.
The dips falling outside of the holes, generate smaller dips bouncing on the terrain

updates
-------
- creation : 2024/08/02
- update   : 2024/08/03

"""

from geonodes import *
from geonodes import macros

# ====================================================================================================
# A Wave produced by a dip

def dip_wave(center, t, length=3., c=5, falloff=30, omega=4, height=1, amp_only=False):
    """ Wave produced by a dip

    Note that location and center are supposed to be in plane (x, y)

    Arguments
    ---------
    - center (Vector): dip impact location
    - t (Float) : time
    - length (Float = 3) : length non null amplitude
    - c (Float = 5) : wave celerity
    - falloff (Float = 30) : falloff factor
    - omega (Float = 4) : wave omega
    - height (Float = 1) : wave height
    - amp_only (Boolean = False) : show only the amplitude

    Returns
    -------
    - Float : wave heigth at position
    """

    with Layout("Dip Wave", color='MACRO'):
        dist = nd.position.distance(center)

        amp = macros.impulsion(dist,
            from_min     = -length,
            from_max     = 0,
            amplitude    = height,
            increase     = 2.5*length,
            decrease     = 0.5*length,
            c            = c,
            t            = t,
            dist_falloff = falloff,
            time_falloff = falloff,
        )

        z = amp*gnmath.sin(omega*(c*t - dist))

        return z.switch(amp_only, amp)

# ====================================================================================================
# Single wave
# Used to tune the parameters

def single_wave():

    with GeoNodes("Single Wave"):
        grid = Mesh.Grid(20, 20, 200, 200)
        grid.faces.smooth = True

        z = dip_wave(
            center      = 0,
            t           = Float(0, "Time"),
            length      = Float(3, "Length"),
            c           = Float(5, "c"),
            falloff     = Float(30, "Falloff"),
            omega       = Float(4, "Omega"),
            height      = Float(1, "Height"),
            amp_only    = Boolean(False, "Amplitude Only"))

        grid.points.offset = (0, 0, z)

        grid.out()

# ====================================================================================================
# Rain falling on a terrain

def demo():

    with GeoNodes("Rain"):

        subdivision    = Integer(1, "Subdivision", 0, 10, "Subdivision to apply to the input terrain")
        z_water        = Float.Distance(0, "Water level")
        density        = Float(.1, "Density", tip="Rain intensity")
        age_max        = Float.Time(2, "Dip life", .1)
        length         = Float.Distance(2, "Length", tip="Interval length of non null waves")
        omega          = Float(10, "Omega")
        height         = Float.Distance(.1, "Height")
        c              = Float(2, "Celerity")
        falloff        = Float(5, "Falloff", 0)
        proj_speed     = Float(1, "Projection speed", 0)
        proj_size      = Float.Distance(.05, "Projection size", 0)
        material       = Material(None, "Puddles Material")
        proj_mat       = Material(None, "Projection Material")

        # ----------------------------------------------------------------------------------------------------
        # Water mesh

        terrain = Mesh()

        with Layout("Build water from input mesh"):
            puddles = Mesh(terrain).subdivide(subdivision)
            puddles.faces.smooth   = True
            puddles.faces.material = material

        # ----------------------------------------------------------------------------------------------------
        # Dips fallen before simulation start

        with Layout("Initial dips"):
            dips = puddles.faces.distribute_points(density=density*age_max, seed=10000)
            dips.points.store("Age", Float.Random(0, age_max, seed=10001))

            puddles_index = terrain.points.sample_nearest(dips.position)
            z = puddles.points.sample_index(puddles.position.z, puddles_index)
            dips = dips.points[z.greater_than(z_water)].delete()

        # ----------------------------------------------------------------------------------------------------
        # Simulation loop : generates new dips at each frame
        # Generates new projections

        projs = Cloud.Points(count=0)

        with Simulation(dips=dips, projs=projs) as sim:

            with Layout("New dips"):

                dips = puddles.faces.distribute_points(density=density*sim.delta_time, seed=nd.scene_time.frame)

                puddles_index = terrain.points.sample_nearest(dips.position)
                dip_position = puddles.points.sample_index(puddles.position, puddles_index)
                z = dip_position.z

                dips = dips.points[z.less_equal(z_water)].separate()
                start_projs = dips.inverted_

                dips.points.store("Age", 0)
                sim.dips += dips

            with Layout("Update age"):
                age = Float.Named("Age")
                sim.dips.points.store("Age", age + sim.delta_time)
                sim.dips = sim.dips.points[age.greater_than(age_max)].delete()

            with Layout("New Projections"):
                new_projs = start_projs.points.duplicate_elements(amount=Integer.Random(3, 7, seed=nd.scene_time.frame + 1000))
                new_projs.points.store("Speed", Vector.Random((-.4, -.4, 1), (.4, .4, 1), seed=nd.scene_time.frame + 2000)*proj_speed)
                new_projs.points.radius = Float.Random(.5, 2, seed=nd.scene_time.frame + 3000)*proj_size
                sim.projs += new_projs

            with Layout("Projections motion"):
                old_speed = Vector.Named("Speed")
                new_speed = old_speed + Vector((0, 0, -9.86)).scale(sim.delta_time)
                sim.projs.points.offset = (old_speed + new_speed)*(sim.delta_time/2)

                sim.projs.points.store("Speed", new_speed)

            with Layout("Kill Projections"):
                sim.projs = sim.projs.points[nd.position.z.less_than(z_water)].delete()

        pts = sim.dips

        # ----------------------------------------------------------------------------------------------------
        # Loop on each dip to compute one wvae per dip

        with Repeat(z=0., index=0, iterations=pts.points.count) as rep:

            with Layout("Dip location and age"):
                center = pts.points.sample_index(dips.position, index=rep.index)
                age    = pts.points.sample_index(Float.Named("Age"), index=rep.index)
                rep.index += 1

            with Layout("Wave height"):
                h = dip_wave(center, t=age, c=c, falloff=falloff, omega=omega, height=height)
                h *= (1 - Float.Named("Water"))

            rep.z += h

        # ----------------------------------------------------------------------------------------------------
        # We set the total height to the water

        with Layout("Update water height"):
            x, y = puddles.position.x, puddles.position.y
            fac = puddles.position.z.map_range_smooth(z_water, z_water + .02, 1., 0.)
            puddles.points.position = (x, y, z_water + rep.z * fac)

        # ----------------------------------------------------------------------------------------------------
        # Projections

        with Layout("Projection dips"):
            cube = Mesh.Cube()
            cube.faces.material = proj_mat
            proj_dips = sim.projs.points.instance_on(
                instance = cube,
                rotation = Vector.Random(0, tau, seed=nd.scene_time.frame + 4000),
                scale    = nd.radius)

        geo  = Geometry.Switch(Boolean(True,  "Show Terrain"), None, terrain)
        geo += Geometry.Switch(Boolean(True,  "Show Puddles"), None, puddles)
        geo += Geometry.Switch(Boolean(True,  "Show Projections"), None, proj_dips)
        geo += Geometry.Switch(Boolean(False, "Show Points"), None, pts + sim.projs)

        geo.out()
