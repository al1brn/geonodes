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

        with Panel("Terrain"):
            show_terrain = Boolean(True,  "Show Terrain")
            sub_terrain  = Integer(1, "Subdivision", 0, 10, "Subdivision to apply to the terrain")
            noise_scale  = Float(.1, "Noise Scale", 0)
            noise_height = Float(2, "Noise Height", 0)

        with Panel("Puddles"):
            show_puddles = Boolean(True,  "Show Puddles")
            sub_puddles  = Integer(1, "Subdivision", 0, 10, "Subdivision to apply to the puddles")
            z_water      = Float.Distance(0, "Water level")
            material     = Material(None, "Puddles Material")

        with Panel("Rain"):
            density        = Float(.1, "Density", tip="Rain intensity")
            age_max        = Float.Time(2, "Dip life", .1)
            length         = Float.Distance(2, "Length", tip="Interval length of non null waves")
            omega          = Float(10, "Omega")
            height         = Float.Distance(1, "Height")
            c              = Float(2, "Celerity")
            falloff        = Float(5, "Falloff", 0)
            seed           = Integer(0, "Seed")
            show_points    = Boolean(False, "Show Points")

        with Panel("Projections"):
            show_projs     = Boolean(True,  "Show Projections")
            proj_speed     = Float(1, "Projection speed", 0)
            proj_size      = Float.Distance(.05, "Projection size", 0)
            proj_mat       = Material(None, "Projection Material")

        # ----------------------------------------------------------------------------------------------------
        # Water mesh

        terrain = Mesh()

        with Layout("Prepare the terrain"):
            terrain = Mesh(terrain).subdivide(sub_terrain)
            z_noise = Texture.Noise(scale=noise_scale, detail=None, roughness=None, lacunarity=None, distortion=None, noise_dimensions='3D', noise_type='FBM', normalize=True)
            terrain.offset = (0, 0, (z_noise - .5)*noise_height)


        with Layout("Build water from input mesh"):
            puddles = Mesh(terrain).subdivide(gnmath.max(sub_puddles - sub_terrain, 0))
            puddles.faces.smooth   = True
            puddles.faces.material = material

        # ----------------------------------------------------------------------------------------------------
        # Dips fallen before simulation start

        with Layout("Initial dips"):
            dips = puddles.faces.distribute_points(density=density*age_max, seed=seed)
            dips.points.store("Age", Float.Random(0, age_max, seed=seed + 1))

            puddles_index = terrain.points.sample_nearest(dips.position)
            z = puddles.points.sample_index(puddles.position.z, puddles_index)
            dips = dips.points[z.greater_than(z_water)].delete()

        # ----------------------------------------------------------------------------------------------------
        # Simulation loop : generates new dips at each frame
        # Generates new projections

        projs = Cloud.Points(count=0)

        with Simulation(dips=dips, projs=projs) as sim:

            with Layout("New dips"):

                dips = puddles.faces.distribute_points(density=density*sim.delta_time, seed=seed.hash_value(Float.frame))

                puddles_index = terrain.points.sample_nearest(dips.position)
                dip_position = puddles.points.sample_index(puddles.position, puddles_index)
                z = dip_position.z

                dips = dips.points[z.less_equal(z_water)].separate()
                start_projs = Cloud(dips.inverted_)

                dips.points.store("Age", 0)
                sim.dips += dips

            with Layout("Update age"):
                age = Float.Named("Age")
                sim.dips.points.store("Age", age + sim.delta_time)
                sim.dips.points[age.greater_than(age_max)].delete()

            with Layout("New Projections"):
                new_projs = start_projs.points.duplicate(amount=Integer.Random(3, 7, seed=seed.hash_value(Float.frame + 1)))
                new_projs.points.store("Speed", Vector.Random((-.4, -.4, 1), (.4, .4, 1), seed=seed.hash_value(Float.frame + 2))*proj_speed)
                new_projs.points.radius = Float.Random(.5, 2, seed=seed.hash_value(Float.frame + 3))*proj_size
                sim.projs += new_projs

            with Layout("Projections motion"):
                old_speed = Vector.Named("Speed")
                new_speed = old_speed + Vector((0, 0, -9.86)).scale(sim.delta_time)
                sim.projs.points.offset = (old_speed + new_speed)*(sim.delta_time/2)

                sim.projs.points.store("Speed", new_speed)

            with Layout("Kill Projections"):
                sim.projs.points[nd.position.z.less_than(z_water)].delete()

        pts = sim.dips

        # ----------------------------------------------------------------------------------------------------
        # Loop on each dip to compute one wave per dip

        with Repeat(z=0., iterations=pts.points.count) as rep:

            with Layout("Dip location and age"):
                center = pts.points.sample_index(dips.position, index=rep.iteration)
                age    = pts.points.sample_index(Float.Named("Age"), index=rep.iteration)

            with Layout("Wave height"):
                h = dip_wave(center, t=age, c=c, falloff=falloff, omega=omega, height=height)
                h *= (1 - Float.Named("Water"))

            rep.z += h

        # ----------------------------------------------------------------------------------------------------
        # We set the total height to the water

        with Layout("Update water height"):
            x, y = puddles.position.x, puddles.position.y
            fac = puddles.position.z.map_range_smooth_step(z_water, z_water + .02, 1., 0.)
            puddles.points.position = (x, y, z_water + rep.z * fac)

        # ----------------------------------------------------------------------------------------------------
        # Projections

        with Layout("Projection dips"):
            cube = Mesh.Cube()
            cube.faces.material = proj_mat
            proj_dips = sim.projs.points.instance_on(
                instance = cube,
                rotation = Vector.Random(0, tau, seed=Float.frame + 4000),
                scale    = nd.radius)

        if True:
            geo = terrain.switch_false(show_terrain)
            geo += puddles.switch_false(show_puddles)
            geo += proj_dips.switch_false(show_projs)
            geo += (pts + sim.projs).switch_false(show_points)

        else:
            geo  = Geometry.Switch(Boolean(True,  "Show Terrain"), None, terrain)
            geo += Geometry.Switch(Boolean(True,  "Show Puddles"), None, puddles)
            geo += Geometry.Switch(Boolean(True,  "Show Projections"), None, proj_dips)
            geo += Geometry.Switch(Boolean(False, "Show Points"), None, pts + sim.projs)

        geo.out()
