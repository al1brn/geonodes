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

!!! note
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

    # ----------------------------------------------------------------------------------------------------
    # Load Arrows groups
    # ----------------------------------------------------------------------------------------------------

    if G.get_tree("Arrow") is None:
        from . import arrows
        arrows.demo()

    if G.get_tree("Dynamics Visualizer") is None:
        from . import common
        common.demo()

    # ----------------------------------------------------------------------------------------------------
    # Planet Shader
    # ----------------------------------------------------------------------------------------------------

    with ShaderNodes("Planet"):

        ped = Shader.Principled(
            base_color = Color.CombineHSV(snd.attribute("Hue", attribute_type='INSTANCER').factor, .8, .9),
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
            G_constant    = Float(1, "G Constant", .001)
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

        for sim in simulation(planets=planets):
            
            sim.planets = Cloud(sim.planets)
            sim.planets.points._Acceleration = Vector()

            for rep in repeat(sim.planets.points.count, planets=sim.planets):

                rep.planets = Cloud(rep.planets)

                center = sim.planets.points.sample_index(nd.position, index=rep.iteration)
                M      = sim.planets.points.sample_index(Float("Mass"), index=rep.iteration)

                v = center - nd.position
                r = gnmath.max(v.length(), .01)
                acc = v.scale(G_constant*M*r**(-3))
                rep.planets.points[nd.index.not_equal(rep.iteration)].Acceleration = Vector("Acceleration") + acc

            planets = Cloud(rep.planets)

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
                sun.points[sun.points.attribute_statistic(Float("Mass")).max_ > 1.01*Float("Mass")].delete()
                planets.transform(translation=-sun.points.sample_index(nd.position, 0))
                planets = no_center.switch(center_sun, planets)

            sim.planets = planets

        # ----- End of Simulation Loop

        planets = Cloud(sim.planets)
        planets.points.Sun = Float("Mass").equal(planets.points.attribute_statistic(Float("Mass")).max_)

        # ====================================================================================================
        # Planet spheres

        sphere = Mesh.UVSphere()
        sphere.corners.store_uv("UV Map", sphere.uv_map_)
        sphere.faces.shade_smooth = True
        sphere.material = material
        spheres = planets.instance_on(sphere, scale=nd.radius)

        spheres.out()

    # ====================================================================================================
    # Dual system
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constants
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Gravity Constants", is_group=True, color_tag='Input'):
        Float(10.0).out("G")
        Float(1.0).out("Mass")

    # ----------------------------------------------------------------------------------------------------
    # Dual Computation
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Dual Computation", is_group=True):

        # Constants
        G_constant = G()._gravity_constants().G
        M = G_constant.mass
        GM = G_constant*M

        # Inputs

        V_depth = Float(0.0, "V Depth", 0.0, tip="Potential energy grid depth")
        
        with Panel("System"):
            m_factor = Float.Factor(0.5, "m", 0.01, 0.99, tip="Planet 1 mass")
            eccentricity = Float(
                0.5, "Eccentricity", 0.0, 10.0,
                tip="< 1: ellipse, > 1: hyperbola",
            )
            semi_major_axis = Float.Distance(
                1.0, "Semi-major Axis", 0.01,
                tip="Semi-major axis magnitude",
            )
            clockwise = Boolean(False, "Clockwise")
            
        with Closure() as gravitation:
            
            time = Float.Time(0.0, "Time", tip="Physical simulation time")
            index = Integer(0, "Index")
            motion = Float(0.5, "Motion")
            V_scale = Float(0.0, "V Scale")

            with Layout("Adjust Parameters"):

                m1 = m_factor*M
                m2 = M - m1

                ratio1 = m2 / M
                ellipse = eccentricity.less_than(1.0)
                e = Float.Switch(
                    ellipse,
                    gnmath.max(eccentricity, 1.01),
                    gnmath.min(eccentricity, 0.99),
                )
                a = semi_major_axis
                direction = Float.Switch(clockwise, 1.0, -1.0)

            with Layout("Conic Parameters"):

                ellipse_b = a * gnmath.max(1.0 - e**2, 0.0).sqrt()
                hyperbola_b = a * gnmath.max(e**2 - 1.0, 0.0).sqrt()
                mean_motion = (GM / a**3).sqrt()
                period = 2.0 * np.pi / mean_motion

            with Layout("Relative Position"):

                mean_anomaly = mean_motion * time

                # Elliptic Kepler equation
                eccentric_anomaly = mean_anomaly
                for _ in range(8):
                    eccentric_anomaly -= (
                        eccentric_anomaly
                        - motion * e * eccentric_anomaly.sin()
                        - mean_anomaly
                    ) / (
                        1.0 - motion * e * eccentric_anomaly.cos()
                    )

                ellipse_position = Vector((
                    a * (eccentric_anomaly.cos() - e),
                    direction * ellipse_b * eccentric_anomaly.sin(),
                    0.0,
                ))

                # Hyperbolic Kepler equation, blended with uniform anomaly
                sinh_guess = mean_anomaly / e
                physical_guess = gnmath.log(
                    sinh_guess + (sinh_guess**2 + 1.0).sqrt(),
                    np.e,
                )
                hyperbolic_anomaly = (
                    (1.0 - motion) * mean_anomaly
                    + motion * physical_guess
                )
                for _ in range(8):
                    sinh_h = hyperbolic_anomaly.sinh()
                    cosh_h = hyperbolic_anomaly.cosh()
                    hyperbolic_anomaly -= (
                        (1.0 - motion) * hyperbolic_anomaly
                        + motion * (e * sinh_h - hyperbolic_anomaly)
                        - mean_anomaly
                    ) / (
                        (1.0 - motion)
                        + motion * (e * cosh_h - 1.0)
                    )

                hyperbola_position = Vector((
                    a * (e - hyperbolic_anomaly.cosh()),
                    direction * hyperbola_b * hyperbolic_anomaly.sinh(),
                    0.0,
                ))

                relative_position = Vector.Switch(
                    ellipse,
                    hyperbola_position,
                    ellipse_position,
                )

            with Layout("Relative Velocity"):

                eccentric_anomaly_dot = mean_motion / (
                    1.0 - e * eccentric_anomaly.cos()
                )

                ellipse_velocity = Vector((
                    -a * eccentric_anomaly.sin() * eccentric_anomaly_dot,
                    direction * ellipse_b * eccentric_anomaly.cos() * eccentric_anomaly_dot,
                    0.0,
                ))

                hyperbolic_anomaly_dot = mean_motion / (
                    e * hyperbolic_anomaly.cosh() - 1.0
                )

                hyperbola_velocity = Vector((
                    -a * hyperbolic_anomaly.sinh() * hyperbolic_anomaly_dot,
                    direction * hyperbola_b * hyperbolic_anomaly.cosh() * hyperbolic_anomaly_dot,
                    0.0,
                ))

                relative_velocity = Vector.Switch(
                    ellipse,
                    hyperbola_velocity,
                    ellipse_velocity,
                )

                relative_acceleration = (
                    relative_position
                    * (-GM / relative_position.length()**3)
                )

            with Layout("Dynamic"):

                ratio2 = m1 / M

                position1 =  relative_position * ratio1
                position2 = -relative_position * ratio2

                velocity1 =  relative_velocity * ratio1
                velocity2 = -relative_velocity * ratio2

                acceleration1 =  relative_acceleration * ratio1
                acceleration2 = -relative_acceleration * ratio2

            with Layout("Potential Energy"):
                d = (position2 - position1).length()
                V = -GM / d
                specific_energy = Float.Switch(
                    ellipse,
                    GM/(2.0*a),
                    -GM/(2.0*a),
                )
                specific_kinetic = relative_velocity.length()**2/2.0

            with Layout("Potential Vizualisation"):

                center1 = V_scale.less_than(0)
                fac = Float.Switch(center1, V_scale, -V_scale)
                pos = Vector.Switch(center1, position2, position1)
                x, y, _ = (-pos).xyz

                delta = Vector((x*fac, y*fac, V*V_depth*fac))

                position1 += delta
                position2 += delta

            with Layout("Index selection"):
                second = index.equal(1)
                pos = Vector.Switch(second, position1, position2)
                vel = Vector.Switch(second, velocity1, velocity2)
                acc = Vector.Switch(second, acceleration1, acceleration2)
                mass = Float.Switch(second, m1, m2)

                specific_kinetic.out("Kinetic")
                V.out("Potential")
                specific_energy.out("Total Energy")

            pos.out("Position")
            vel.out("Velocity")
            acc.out("Acceleration")
            mass.out("Mass")

            m1.out("m1")
            m2.out("m2")
            e.out("Eccentricity")
            a.out("Semi-major Axis")
            period.out("Period")
            V_depth.out("V Depth")
            
        gravitation.out("Gravitation")
        
        GRAV_SIG = gravitation.get_signature()

    # ----------------------------------------------------------------------------------------------------
    # Utility    
    # ----------------------------------------------------------------------------------------------------
        
    def eval_gravity(gravitation, time, index, motion, v_scale):
        return gravitation.evaluate(
            time        = time, 
            index       = index, 
            motion      = motion,
            v_scale     = v_scale,
            signature   = GRAV_SIG).node

    # ----------------------------------------------------------------------------------------------------
    # Dual System
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Dual System"):

        time = Float.Time(0.0, "Time", tip="Physical simulation time")
        motion = Float.Factor(
            1.0, "Motion", 0.0, 1.0,
            tip="0: uniform eccentric anomaly, 1: physical Kepler motion"
        )
        V_scale = Float.Factor(0.0, "V Scale", -1, 1)
        
        with Panel("Planet 1"):
            obj1 = Object(name="Object 1")

        with Panel("Planet 2"):
            obj2  = Object(name="Object 2")
            
        grav = G().dual_computation().link_inputs().gravitation
            
        with Layout("Visualization"):
            
            node1 = eval_gravity(grav, time, 0, motion, V_scale)
            geo1 = obj1.info().geometry
            geo1.offset = node1.position
            
            node2 = eval_gravity(grav, time, 1, motion, V_scale)
            geo2 = obj2.info().geometry
            geo2.offset = node2.position
            
            geo = geo1 + geo2
            
        with Bundle() as bundle:
            
            time.out("Time")
            grav.out("Gravitation")
            motion.out("Motion")
            V_scale.out("V Scale")
            
        SYSTEM_SIG = bundle.get_signature()
            
        geo.set_bundle(bundle)
        geo.out()  

    # ----------------------------------------------------------------------------------------------------
    # Conics
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Dual Conics"):

        # Constants
        G_constant = G()._gravity_constants().G

        # Inputs
        geo = Geometry()
        
        show_planets = Boolean(True, "Show Planets")
        
        with Panel("Conics"):
            section = Float(0.05, "Section")
            mat = Material("Arrow", "Material")
            count = Integer(100, "Resolution", 10, 2000)
            hyperbola_extent = Float(
                1.0, "Hyperbola Extent", 0.01, 10.0,
                tip="Number of pseudo-periods shown on each side of the periapsis",
            )
            pot_fac = Float.Factor(0.0, "Stick to potential", 0, 1)
            
            show = []
            color = []
            for i in range(2):
                with Panel(f"Conic {i + 1}"):
                    show.append(Float.Factor(1.0, "Show", 0, 1))
                    color.append(Color(name="Color"))
                    
        with Panel("Potential Energy"):
            grid_show = Float.Factor(1.0, "Show", 0, 1)
            grid_cut = Boolean(False, "Cut")
            grid_size  = Float(10.0, "Size", 1.0)
            grid_resol = Integer(10, "Resolution", 10, 2000)
            grid_scale = Float(1.0, "Scale", 0.0)
            grid_mat = Material(None, "Material")

        with Panel("Total Energy"):
            total_show = Float.Factor(1.0, "Show", 0, 1)
            total_cut = Boolean(False, "Cut")
            total_size = Float(10.0, "Size", 1.0)
            total_scale = Float(1.0, "Scale", 0.0)
            total_mat = Material(None, "Material")
            
        with Layout("Getting Bundle & Closure"):
            bundle = geo.get_bundle(remove=True)
            bundle_node = bundle.separate(signature=SYSTEM_SIG)
            grav = bundle_node.gravitation
            V_scale = bundle_node.v_scale    
            
            node = eval_gravity(grav, 0, index=0, motion=0.0, v_scale=1.0)
            V_depth = node.v_depth
            
            GM = (
                -G_constant
                * V_depth
                * (node.m1 + node.m2)
            )._lc("GM * V Depth")

            d = gnmath.max(nd.position.length(), 0.01)._lc("Distance")
            V = (grid_scale*GM/d)._lc("Potential")

        with Layout("Potential Energy Grid"):
            grid = Mesh.Grid(size_x=grid_size, size_y=grid_size, vertices_x=grid_resol, vertices_y=grid_resol)

            grid.points[nd.position.length().less_than(0.01)].delete()
            
            grid.offset = (0.0, 0.0, V)
            
            grid.faces.Transparency = 1 - grid_show
            grid.faces.material = grid_mat
            grid.faces.shade_smooth = True
            grid.points[grid_cut & nd.position.y.less_than(0.0)].delete()
            grid.switch(grid_show.equal(0.0))

        with Layout("Total Energy Plane"):
            total_plane = Mesh.Grid(
                size_x=total_size,
                size_y=total_size,
                vertices_x=2,
                vertices_y=Integer.Switch(total_cut, 2, 3),
            )

            total_plane.offset = (
                0.0,
                0.0,
                node.total_energy*V_depth*total_scale,
            )

            total_plane.faces.Transparency = 1 - total_show
            total_plane.faces.material = total_mat
            total_plane.faces.shade_smooth = True
            total_plane.points[
                total_cut & nd.position.y.less_than(0.0)
            ].delete()
            total_plane.switch(total_show.equal(0.0))
                    
        with Layout("Preparation"):
            circle = Curve.Circle(resolution=count)
            line = Curve.Line().resample(count=count)
            mesh_conics = []
            csec = Curve.Circle(radius=section, resolution=16)

            hyperbola = node.eccentricity.greater_than(1.0)
            curve_time = Float.Switch(
                hyperbola,
                nd.spline_parameter().factor*node.period,
                (2.0*nd.spline_parameter().factor - 1.0)
                * hyperbola_extent
                * node.period,
            )
            
        for i in range(2):
            with Layout(f"Conic {i + 1}"):
                conic = Curve(Curve.Switch(hyperbola, circle, line))
                
                conic.points.position = eval_gravity(
                    grav,
                    curve_time,
                    index=i,
                    motion=0.0,
                    v_scale=V_scale,
                ).position
                
                mesh_conic = conic.to_mesh(profile_curve=csec)
                mesh_conic.faces.material = mat
                mesh_conic.faces.set("Color", color[i])
                mesh_conic.faces.set("Transparency", 1.0 - show[i])
                mesh_conic.switch(show[i].equal(0))
                
                if i == 0:
                    mesh_conics = mesh_conic
                else:
                    mesh_conics += mesh_conic
                    
        geo.switch_false(show_planets)
        geo += mesh_conics, grid, total_plane
        
        geo.set_bundle(bundle)
        
        geo.out()

    # ----------------------------------------------------------------------------------------------------
    # Dynamics Visualizer
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Planet Dynamics Visualizer"):

        geo = Geometry()

        index = Integer(0, "Planet Index", 0, 1)

        with Layout("Getting Bundle & Closure"):
            bundle = geo.get_bundle(remove=True)
            bundle_node = bundle.separate(signature=SYSTEM_SIG)

            node = eval_gravity(
                bundle_node.gravitation,
                bundle_node.time,
                index,
                bundle_node.motion,
                bundle_node.v_scale,
            )

        visualizer = G().dynamics_visualizer(
            geo,
            position=node.position,
            velocity=node.velocity,
            acceleration=node.acceleration,
        )
        visualizer.node.link_inputs()
        visualizer.node.link_panel(("Velocity", "Acceleration"))
        geo = visualizer

        geo.set_bundle(bundle)
        geo.out()
