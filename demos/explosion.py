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
        
        #splitted.out()
        insts.out()
    
    # ====================================================================================================
    # Iterator
    # ====================================================================================================
        
    with GeoNodes("Break into parts"):
        
        mesh = Mesh()
        count = Integer(5, "Count", 1, 20)
        min_size = Float(.1, "Min Size")
        seed = Integer(0, "Seed")
        
        cells = mesh.points.split_to_instances()
        for rep in repeat(count, cells=cells):
            
            rep_seed = seed.hash_value(rep.iteration)
            
            #parts = rep.mesh.points.split_to_instances(group_id = nd.mesh_island().island_index)
            
            for feel in Instances(rep.cells).insts.for_each():
                
                part = feel.element.realize()
                feel.geometry = G().plane_split(
                    mesh     = part,
                    min_size = min_size,
                    seed     = rep_seed.hash_value(feel.index),
                    )
                        
            rep.cells = feel.generated
            
        parts_count = Instances(rep.cells).insts.count
        Boolean(True).info("Cells: " + parts_count.to_string())
            
        rep.cells.out()
        

    # ====================================================================================================
    # Fracturing with cones
    # ====================================================================================================

    with GeoNodes("Cone Split"):
        
        mesh = Mesh()
        count = Integer(10, "Count", 0)
        min_size = Float(.1, "Min Size")
        seed = Integer(0, "Seed")
        
        #rot = mesh.points.sample_index(Vector.Random(-pi, pi, seed=seed), index=0)    
        #rot = Rotation()
        
        #with Layout("Rotation"):
        #    mesh.transform(rotation=rot)
        
        with Layout("Mesh loc and dims"):
            dims = mesh.points.attribute_statistic(nd.position)
            
            center = ((dims.min_ + dims.max_)/2)._lc("Center")
            sizes = (dims.max_ - dims.min_)._lc("Size")
            
        with Layout("Mesh size"):
            sx, sy, sz = sizes.xyz
            size = gnmath.max(gnmath.max(sx, sy), sz)
            small = size < min_size
            small._lc("Small part")
            
            count.switch(small, 0)
            
        for rep in repeat(count, mesh=mesh):
            
            rep_seed = seed.hash_value(rep.iteration)
            
            n = rep.mesh.points.sample_index(Integer.Random(3, 10, seed=rep_seed), index=0)
            r = rep.mesh.points.sample_index(Float.Random(0.7, 1.3, seed=rep_seed + 1), index=0)
            
            with Layout("A random polygon"):
                cone = Mesh.Cone(
                    radius_bottom   = 0, 
                    radius_top      = r, 
                    vertices        = n, 
                    depth           = 1.1,
                    fill_type       = 'N-Gon')
                    
                rot = rep.mesh.points.sample_index(Vector.Random(-pi, pi, seed=rep_seed + 2), index=0)
                cone[nd.index != 0].offset = Vector.Random(-0.4*r, .4*r, seed=rep_seed + 3)*(1, 1, 0)
                
                cone.transform(translation=center, scale=size, rotation=rot)
                
                a = Mesh(rep.mesh).intersect(cone, solver='Manifold')
                b = Mesh(rep.mesh).difference(cone, solver='Manifold')
                
                rep.mesh = a + b
                
        rep.mesh.out()

    # ====================================================================================================
    # Mesh to located instances
    # ====================================================================================================

    with GeoNodes("Mesh to Located Instances"):
        """ 'Split to instances' locates islands at (0, 0, 0)

        This Group locates instances at their center
        """
        
        mesh = Mesh()
        
        instances = mesh.points.split_to_instances(group_id=nd.mesh_island().island_index)
        
        for rep in instances.insts.for_each():
            m = Mesh(Instances(rep.element).realize())
            dims = m.points.attribute_statistic(nd.position)
            c = (dims.min_ + dims.max_)/2
            m.offset = -c
            
            size = dims.max_ + dims.min_
            sx, sy, sz = size.xyz
            vol = sx*sy*sz 
            
            cell = m.points.split_to_instances()
            cell.position = c
            cell.insts.Volume = vol
            cell.insts.Size = size
            
            rep.geometry = cell
            
        rep.generated.out()

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

            cloud = Cloud()         # Simulation points (with their attributes)
            t = Float(name="t")     # Time (for forces depending on time)
            dt = Float(name="dt")   # Simulation delta time

            speed = Vector("Velocity")
            mass  = Float("Mass")

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
    # Kinematics
    # ====================================================================================================

    with GeoNodes("Kinematics Engine", is_group=True):

        # ---------------------------------------------------------------------------
        # Input geometry must be a cloud of points
        # ---------------------------------------------------------------------------

        cloud = Cloud()
        speed = Vector(name="Speed", hide_value=True)
        rot   = Rotation(name="Rotation", hide_value=True)
        omega = Float(name="Omega", hide_value=True)

        frame0 = Integer(1, "Start Frame", shape='Single')

        # ---------------------------------------------------------------------------
        # Initialize Velocity and Rotation
        # ---------------------------------------------------------------------------

        with Layout("Initialization"):

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

            gravity   = Closure(name="Gravity")
            viscosity = Closure(name="Viscosity")

            sig = ({'Cloud': 'Cloud', 't': 'Float', 'dt': 'Float'}, {'Cloud': 'Cloud'})

        for sim in cloud.simulation():

            sim.skip = nd.scene_time().frame.less_than(frame0)

            dt = sim.delta_time

            # Reinit acceleration
            cloud.points.Acceleration = Vector()

            # Evaluate the forces
            for cl in [gravity, viscosity]:
                cloud = cl.evaluate(cloud=cloud, t=0.0, dt=dt, signature=sig)

            # Simulation
            acc = Vector("Acceleration")
            speed = Vector("Speed")

            # New position and speed
            new_speed = speed + acc*dt
            cloud.points.Velocity = new_speed
            cloud.offset = (speed + new_speed).scale(dt/2)

            # Rotation            
            angle = Float("Angle") + Float("Omega")*dt
            cloud.points.Rotation = Rotation.FromAxisAngle(Vector("Axis"), angle)
            cloud.points.Angle = angle

            cloud.out()

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

