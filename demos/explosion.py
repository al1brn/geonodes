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

!!! note
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

    # ====================================================================================================
    # Mesh to located instances
    #
    # Overrids Mesh to Instances with:
    # - capability to solidify instances
    # - instances are located at parts geometric center
    # ====================================================================================================

    with GeoNodes("Mesh to Located Instances"):
        """ 'Split to instances' locates islands at (0, 0, 0)

        This Group locates instances at their center
        """
        
        mesh = Mesh()
        use_islands = Boolean(True, "Use Islands")
        gid  = Integer(name="Group ID", hide_value=True)
        thickness = Float(0, "Thickness")
        separate = Float.Factor(1.0, "Separate", 1.0, 2.0)

        gid.switch(use_islands, nd.mesh_island().island_index)
        
        instances = mesh.faces.split_to_instances(group_id=gid)
        
        for rep in instances.insts.for_each():

            m = Mesh(Instances(rep.element).realize())

            with Layout("Solidify"):
                solidified = Mesh(m).faces.extrude(offset_scale=-thickness, individual=False).flip_faces()
                solidified += m
                solidified.merge_by_distance()
                m.switch(thickness != 0.0, solidified)

            with Layout("Dimensions"):
                dims = m.points.attribute_statistic(nd.position)
                c = (dims.min_ + dims.max_)/2
                m.offset = -c
                
                size = dims.max_ + dims.min_
                sx, sy, sz = size.xyz
                vol = sx*sy*sz

            with Layout("To Instance"):
                cell = m.points.split_to_instances()
                cell.position = c
                cell.insts.Volume = vol
                cell.insts.Size = size
            
            rep.geometry = cell

        insts = Instances(rep.generated)
        insts.position = nd.position.scale(separate)
            
        insts.out()

    # ====================================================================================================
    # Fracturing by splitting in two parts
    # ====================================================================================================

    with GeoNodes("Plane Split"):
        
        mesh = Mesh()
        min_size = Float(.1, "Min Size")
        seed = Integer(0, "Seed")
        
        rot = mesh.points.sample_index(Vector.Random(-pi, pi, seed=seed), index=0)
        
        with Layout("Rotation"):
            mesh.transform(rotation=rot)
        
        with Layout("Mesh loc and dims"):
            dims = mesh.points.attribute_statistic(nd.position)
            
            center = ((dims.min_ + dims.max_)/2)._lc("Center")
            size = (dims.max_ - dims.min_)._lc("Size")
            
        with Layout("Mesh size"):
            sx, sy, sz = size.xyz
            small = (sx + sy + sz) < min_size
            small._lc("Small part")
                
        with Layout("Split with central plane"):
            plane = Mesh.Cube(size=(sx + 1, sy + 1, 0.01))
            offset = plane.points.sample_index(Float.Random(-0.3*sz, 0.3*sz, seed=seed + 1), index=0)
            plane.transform(translation=center + (0, 0, offset))
            
            splitted = mesh.difference(plane)
            
        with Layout("Rotate back"):
            splitted.transform(rotation=Rotation(rot).invert())
            
        splitted.switch(small, Mesh())
        insts = splitted.points.split_to_instances(group_id=nd.mesh_island().island_index)
        
        insts.out()
    
    # ====================================================================================================
    # Iterator
    # ====================================================================================================
        
    with GeoNodes("Break with Planes Slicings"):
        
        mesh = Mesh()
        count = Integer(5, "Count", 1, 20)
        min_size = Float(.1, "Min Size")
        seed = Integer(0, "Seed")
        
        cells = mesh.points.split_to_instances()
        for rep in repeat(count, cells=cells):
            
            rep_seed = seed.hash_value(rep.iteration)
            
            for feel in Instances(rep.cells).insts.for_each():
                
                part = feel.element.realize()
                feel.geometry = G().plane_split(
                    mesh     = part,
                    min_size = min_size,
                    seed     = rep_seed.hash_value(feel.index),
                    )
                        
            rep.cells = feel.generated

        insts = Instances(rep.cells)
            
        parts_count = insts.insts.count
        Boolean(True).info("Cells: " + parts_count.to_string())
        insts.out()

    # ====================================================================================================
    # Cell fracturation
    # ====================================================================================================

    with GeoNodes("Break with Subdivisions"):
        
        mesh      = Mesh()
        subd      = Integer(1,        "Divisions", 0, 7)
        disp      = Float.Factor(1.,  "Displacement", 0, 2)
        merge     = Float.Factor(0.2, "Merge", 0, 1)
        thickness = Float(0.0,        "Thickness")
        seed      = Integer(0,        "Seed")

        
        with Layout("Dimensions"):
            node = mesh.points.attribute_statistic(nd.position).node
            size = node.max - node.min
            x, y, z = size.xyz
            min_size = gnmath.min(x, gnmath.min(y, z))
            
            max_disp = min_size/2**subd
            
            disp *= max_disp
            
        with Layout("Subdivide and displace"):
            count = mesh.points.count
            edges_count = mesh.edges.count
            
            mesh = mesh.subdivide(subd)
            v = Vector.Random(-disp, disp, seed=seed)
            v -= nd.normal.scale(v.dot(nd.normal))
            
            int_count = count + edges_count*(2**subd - 1)
                
            mesh.offset = v.switch(nd.index < int_count)
            
        with Layout("Split faces and merge some of them"):
            
            mesh.faces.Temp_Pos = nd.position
            mesh.faces.Cell_ID = nd.index
            
            for rep in repeat(mesh.edges.count, mesh=mesh, merge=Boolean.Random(merge, seed=seed + 20)):
                
                corner0 = nd.corners_of_edge(edge_index=rep.iteration, sort_index=0)
                corner1 = nd.corners_of_edge(edge_index=rep.iteration, sort_index=1)
                do_merge = rep.mesh.edges.sample_index(rep.merge, index=rep.iteration)
                
                face0 = nd.face_of_corner(corner0)
                face1 = nd.face_of_corner(corner1)
                
                new_index = rep.mesh.faces.sample_index(Integer("Cell ID"), index=face0)
                mesh = Mesh(rep.mesh)
                mesh.faces[nd.index == face1].Cell_ID = new_index
                    
                rep.mesh.switch(do_merge, mesh)
                
        with Layout("Split to islands"):
                
            mesh = Mesh(rep.mesh)
            mesh.remove_named_attribute("Wildcard", "Temp*")

            cells = G().mesh_to_located_instances(
                mesh, 
                use_islands = False, 
                group_id    = Integer("Cell ID"),
                thickness   = thickness,
                )
            
            cells.remove_named_attribute(name="Cell ID")
            
        cells.out()


    # ====================================================================================================
    # Gravity
    # ====================================================================================================

    with GeoNodes("Gravity Closure", is_group=True):

        g = Vector((0, 0, -9.81), "Gravity")

        with Closure() as cl:
            cloud = Cloud()         # Simulation points (with their attributes)
            t = Float(name="t")     # Time (for forces depending on time)
            dt = Float(name="dt")   # Simulation delta time

            acc = Vector("Acceleration")
            acc = acc.switch_false(acc.exists)
            acc += g
            cloud.points.Acceleration = acc
            cloud.out()

        cl.out()

    # ====================================================================================================
    # Gravity
    # ====================================================================================================

    with GeoNodes("Viscosity Closure", is_group=True):

        v_fac = Float(1.3, "Factor")
        v_exp = Float(1.7, "Power")
        a_max = Float(100.0, "Max acceleration", 0.0)

        with Closure() as cl:

            cloud = Cloud()          # Simulation points (with their attributes)
            t     = Float(name="t")  # Time (for forces depending on time)
            dt    = Float(name="dt") # Simulation delta time

            speed = Vector("Speed")
            mass  = Float("Mass")
            mass.switch_false(mass.exists_, 1.)

            v = speed.length()
            visc = v_fac*(v**v_exp)/mass
            visc = gnmath.min(visc, v/dt/2)

            acc = Vector("Acceleration")
            acc = acc.switch_false(acc.exists)
            acc += speed.normalize().scale(-visc)
            cloud.points.Acceleration = acc
            cloud.out()

        cl.out()

    # ====================================================================================================
    # Interaction between particles
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Newton law as interaction law
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Newton Law Interaction", is_group = True):

        G_ = Float(1, "G")

        with Closure() as cl:
            cloud = Cloud(None, "Cloud")
            index = Integer(0, "Index")

            mass = Float("Mass")
            mass.switch_false(mass.exists, 1.)

            r = Vector("V").length()
            cloud.points.V = G_*mass*Vector("V").scale(r**(-3))

            cloud.out()

        cl.out()

    # ----------------------------------------------------------------------------------------------------
    # Interaction closure : sum of interaction law between particles
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Interaction Closure", is_group = True):

        law = Closure(None, "Law")
        use_max_acc = Boolean(False, "Bound Acceleration")
        max_acc = Float(100.0, "Max acceleration", 0.0)

        with Closure() as cl:       

            cloud   = Cloud(name = "Cloud")
            t       = Float(name = "t")
            dt      = Float(name = "dt")
            
            n = cloud.points.count
            cloud.points.Acceleration = (0, 0, 0)
            
            for rep in repeat(n, cloud=cloud):
                
                # Current point position
                pos = rep.cloud.points.sample_index(nd.position, index=rep.iteration)

                # Vectors in V
                rep.cloud.points.V = nd.position - pos

                # Basic law: contributions are in V
                rep.cloud = Cloud(law.evaluate(
                    cloud       = rep.cloud, 
                    index       = rep.iteration, 
                    signature   = ({
                        "Cloud"  : Cloud,
                        "Index"  : Integer,
                    }, {
                        "Cloud" : Cloud,
                    })))

                # Add contributions
                sel = nd.index == rep.iteration
                acc = rep.cloud.points[sel.bnot()].attribute_statistic(Vector("V")).node.sum

                # Max acceleration
                lacc = gnmath.max(max_acc, acc.length())
                bounded_acc = acc.scale(max_acc/lacc)
                acc.switch(use_max_acc, bounded_acc)

                # Set acceleration
                rep.cloud.points[sel].Acceleration = acc
                
            cloud = rep.cloud
            
            cloud.out("Cloud")

        cl.out()

    # ====================================================================================================
    # Kinematics
    # ====================================================================================================

    with GeoNodes("Kinematics Engine", is_group=True):

        # ---------------------------------------------------------------------------
        # Input geometry must be a cloud of points
        # ---------------------------------------------------------------------------

        cloud = Cloud()
        active = Boolean(True, "Active")
        speed = Vector(     name = "Speed",     hide_value=True)
        rot   = Rotation(   name = "Rotation",  hide_value=True)
        omega = Float(      name = "Omega",     hide_value=True)

        subs   = gnmath.max(1, Integer(1, "Sub Steps", 1))
        frame0 = Integer(1, "Start Frame", shape='Single')

        # ---------------------------------------------------------------------------
        # Initialize Velocity and Rotation
        # ---------------------------------------------------------------------------

        with Layout("Initialization"):

            #cloud.points.Active = active
            cloud.points.Speed = speed

            axis = rot.to_axis_angle()

            cloud.points.Axis = axis
            cloud.points.Angle = 0.0
            cloud.points.Omega = omega
            cloud.points.Rotation = Rotation()

        # ---------------------------------------------------------------------------
        # Simulation Loop
        # ---------------------------------------------------------------------------

        with Panel("Accelerations"):

            gravity   = Closure(name = "Gravity")
            viscosity = Closure(name = "Viscosity")

            sig = ({'Cloud': 'Cloud', 't': 'Float', 'dt': 'Float'}, {'Cloud': 'Cloud'})

        for sim in cloud.simulation():

            sim.skip = nd.scene_time().frame.less_than(frame0)

            dt = sim.delta_time/subs

            for rep in repeat(subs, cloud=sim.cloud):

                # Reinit acceleration
                rep.cloud.points.Acceleration = Vector()

                # Evaluate the forces
                for cl in [gravity, viscosity]:
                    rep.cloud = Cloud(cl.evaluate(cloud=rep.cloud, t=0.0, dt=dt, signature=sig))

                # Simulation
                acc   = Vector("Acceleration")
                speed = Vector("Speed")
                #act   = Boolean("Active")

                # New position and speed
                new_speed = speed + acc*dt
                rep.cloud.points[active].Speed = new_speed
                rep.cloud[active].offset = (speed + new_speed).scale(dt/2)

                # Rotation            
                angle = Float("Angle") + Float("Omega")*dt
                rep.cloud.points[active].Rotation = Rotation.FromAxisAngle(Vector("Axis"), angle)
                rep.cloud.points[active].Angle = angle

            rep.cloud.out()

        cloud = sim.cloud

        cloud.out()

    # ====================================================================================================
    # Instances kinematics
    # ====================================================================================================

    with GeoNodes("Instances Kinematics"):

        instances = Instances()

        cloud = Cloud.Points(count = instances.insts.count)
        cloud.position = instances.insts.sample_index(nd.position, index=nd.index)

        cloud = Group("Kinematics Engine", cloud=cloud).link_inputs().cloud

        instances.position = cloud.points.sample_index(nd.position, index=nd.index)
        instances.rotate(cloud.points.sample_index(Rotation("Rotation"), index=nd.index))

        instances.out()

    # ====================================================================================================
    # Mesh kinematics
    # ====================================================================================================

    with GeoNodes("Mesh Kinematics"):

        mesh = Mesh()
        omega_max = Float.Angle(1, "Max Omega")
        seed = Integer(0, "Seed")

        instances = G().mesh_to_located_instances(mesh=mesh).instances

        vol = Float("Volume")
        stats = instances.insts.attribute_statistic(vol)
        min_vol = gnmath.max(0.01, stats.min_)
        max_vol = stats.max_
        omega = vol.map_range(min_vol, max_vol, omega_max, omega_max*0.1)

        delta = 0.2*omega_max
        omega += Float.Random(-delta, delta, seed=seed)
        rot = G().random_rotation(seed=seed + 1).rotation

        Group("Instances Kinematics", instances=instances, rotation=rot, omega=omega).link_inputs().out()

    # ====================================================================================================
    # Kinematics
    # ====================================================================================================

    with GeoNodes("Kinematics Demo"):

        mesh = Mesh()
        solidify = Boolean(True, "Solidify")

        with Layout("Solidify"):
            solidified = Mesh(mesh).faces.extrude(nd.position*(-0.1), individual=False)
            solidified[solidified.top].flip_faces()
            mesh.faces.Ext = 1.
            solidified.faces.Ext = 0.
            solidified += mesh
            solidified.merge_by_distance()

            mesh.switch(solidify, solidified)

        mesh = G().cone_split(mesh=mesh).link_inputs(from_panel="Fracture")

        max_speed = Float(1., "Max Speed")

        seed = Integer(0, "Seed")

        anim = G().mesh_kinematics(
            mesh = mesh,
            max_omega = Input("Max Omega"),
            speed = nd.position.scale(Float.Random(0.7*max_speed, max_speed, seed=seed)),
            seed = seed + 1,
            gravity = G().gravity_closure().closure,
            viscosity = G().viscosity_closure().closure,
            start_frame = Input("Start Frame"),
        )

        anim.out()

    
    # ====================================================================================================
    # Solar system demo
    # ====================================================================================================

    with GeoNodes("Solar System Demo"):

        count = Integer(8, "Planets")
        G_    = Float(1., "G")/10000
        seed  = Integer(0, "Seed")

        r = Float.Random(5, 30, seed=seed)
        theta = Float.Random(0, tau, seed=seed + 1)

        pos = (r*theta.cos(), r*theta.sin(), 0)
        rth = theta + Float.Random(-1, 1, seed=seed + 2)
        speed = Vector((-rth.sin(),rth.cos(), 0))*Float.Random(5, 30, seed=seed + 3)

        cloud = Cloud.Points(count+1, position=pos)
        cloud.points.Speed = speed
        cloud.points.Mass = Float.Random(1, 3, seed= seed + 4)
        cloud.points.radius = Float("Mass")*.3

        sun_sel = nd.index == 0
        cloud.points[sun_sel].position = Vector()
        cloud.points[sun_sel].Speed = Vector()
        cloud.points[sun_sel].Mass = 1000.0
        cloud.points[sun_sel].radius = 3.0

        law = G().newton_law_interaction(g=G_)
        interaction = G().interaction_closure(
            law = law,            
        )

        anim = G().kinematics_engine(
            cloud = cloud,
            speed = Vector("Speed"),
            #seed = seed + 100,
            sub_steps = Input("Sub Steps"),
            gravity = interaction,
            start_frame = Input("Start Frame"),
        )

        mesh = anim.cloud.instance_on(instance=Mesh.UVSphere(radius=1),scale=nd.radius)

        mesh.out()








