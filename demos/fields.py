#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/24

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/fields
---------------------
Builds Geometry Nodes to generate fields. Fields can be visualized with Arrows.

Two types of trees are built:
    - Field computation : groups which compute the field vectors at given locations
    - Field visualization : modifiers which visualizes the previus field

Electromagnetic fields
----------------------

The computing groups computes E and B fields from parameters.
The modifiers use the groups to visualize one of the two fields

- G X Moving Charge Field / X Moving Charge Field : a single charge moving along X axis
- G Moving Charge Field / Moving Charge Field : a single charge moving in an arbitraty direction
- G Charges on Curve Field / Charges on Curve Fielf : several charges moving along a curve
- G XY Loop Radial Field : the radial field generated by a single solenoid loop
- G XY Loop Field : the field generated by a single solenoid loop
- G Solenoid Field / Solenoid Field : the field generated by a solenoid
- G Electric Field / Electric Field : electric field generated by charges

Utilities
---------
- Compute Lines of Field : compute field lines from a field computation. The field group uses position as socket input.
  the output socket E or B is used as input of the group 'G Field Lines'

updates
-------
- creation : 2024/07/24
- update   : 2024/08/03
"""

import numpy as np

from geonodes.demos import arrows as arrows_module
from geonodes import *

def demo():

    print("\nCreate fields Geometry Nodes...")

    arrows_module.demo()

    field_prefix = "Field"
    util_prefix  = "Util"
    show_prefix  = "Show"

    # =============================================================================================================================
    # Computing

    # -----------------------------------------------------------------------------------------------------------------------------
    # Frame change

    with GeoNodes("Frame Change", is_group=True, prefix=util_prefix):

        position  = Vector(0, "Position")
        vector    = Vector(0, "Vector")

        center    = Vector(0, "Center")
        direction = Vector.Direction((1, 0, 0), "Direction")
        reverse   = Boolean(False, "Reverse")

        # ----- Rotation to have the direction along x axis

        with Layout("Rotation to have direction along x axis"):

            rotation = Rotation.AlignXToVector(vector=direction)
            inverse  = rotation.invert()

        # ----- Rotate vectors

        with Layout("Rotate vectors"):

            forward_vector  = inverse @ vector
            backward_vector = rotation @ vector

            transformed_vector = forward_vector.switch(reverse, backward_vector)

        # ----- Transformation locations

        with Layout("Transform locations"):

            forward_position  = inverse @ (position - center)
            backward_position = (rotation @ position) + center

            transformed_position = forward_position.switch(reverse, backward_position)

        transformed_position.out("Position")
        transformed_vector.out(  "Vector")

    # =============================================================================================================================
    # Compute Curl

    with GeoNodes("Compute Curl", is_group=True, prefix=util_prefix) as tree:

        # ----- Parameters

        field       = Vector(0, "Field", tip="Field vector at the input geometry points")
        ds          = Float(.1,  "ds", 0.001, tip="Precision")
        normalize   = Boolean(True, "Normalize", tip="Return the raw (False) or normalized (True) field")
        scale       = Float(1, "Scale", tip="Scale")

        # ---- Main

        with Layout("Computation points"):
            geo = Geometry()
            cloud = geo.point_cloud + geo.mesh.points.to_points()

        ds2_ = (-.5*ds)._lc("ds/2")

        with Layout("TEMP Along X"):
            cloud.points.offset = (ds2_, 0, 0)
            cloud.points.store("TEMP Before", field)
            cloud.points.offset = (ds, 0, 0)
            cloud.points.store("TEMP After", field)
            cloud.points.offset = (ds2_, 0, 0)

            cloud.points.store("TEMP dvx", Vector.Named("TEMP After") - Vector.Named("TEMP Before"))

        with Layout("Along Y"):
            cloud.points.offset = (0, ds2_, 0)
            cloud.points.store("TEMP Before", field)
            cloud.points.offset = (0, ds, 0)
            cloud.points.store("TEMP After", field)
            cloud.points.offset = (0, ds2_, 0)

            cloud.points.store("TEMP dvy", Vector.Named("TEMP After") - Vector.Named("TEMP Before"))

        with Layout("TEMP Along Z"):
            cloud.points.offset = (0, 0, ds2_)
            cloud.points.store("TEMP Before", field)
            cloud.points.offset = (0, 0, ds)
            cloud.points.store("TEMP After", field)
            cloud.points.offset = (0, 0, ds2_)

            cloud.points.store("TEMP dvz", Vector.Named("TEMP After") - Vector.Named("TEMP Before"))

        with Layout("Curl"):
            dvx, dvy, dvz = Vector.Named("TEMP dvx"), Vector.Named("TEMP dvy"), Vector.Named("TEMP dvz")
            curl = Vector((
                dvy.z - dvz.y,
                dvx.z - dvz.x,
                dvx.y - dvy.x,
            )).scale(scale)
            cloud.points.store("Vectors", curl.switch(normalize, curl.scale(1/ds)))

        cloud.remove_named_attribute("TEMP *", exact=False)

        cloud.out()

    # =============================================================================================================================
    # Compute the lines of field

    with GeoNodes("Lines of Field", prefix=util_prefix):

        # ----- Field

        field       = Vector(0, "Field", tip="Field vector at the input geometry points")

        # ----- Algorithm parameter

        iterations  = Integer(20, "Iterations", 1, tip="Number of iterations per line")
        delta       = Float(.1, "Delta", .001, tip="Distance to move at each iteration")
        direction   = Integer(1, "Direction",  tip="Move forwards (+1) or backwards (-1)")

        # ----------------------------------------------------------------------------------------------------
        # Main

        with Layout("Starting points"):
            geo = Geometry()
            mesh = geo.mesh.faces.delete_edges_and_faces() + geo.point_cloud.to_vertices()

            mesh.points.store("DELTA", delta*direction)

        with Repeat(mesh=mesh, top=True, iterations=iterations) as rep:

            mesh = rep.mesh

            with Layout("Displacement from current points"):
                v0 = field
                l0 = v0.length

                mesh.points[rep.top].store("Intensity", l0)

                rep.top &= l0.greater_than(0.001)

                v0 = v0.normalize().scale(Float.Named("DELTA"))

            with Layout("Extrude from this first displacement"):

                mesh.points[rep.top].extrude(offset=v0)
                top  = mesh.top_

            with Layout("Displacement from extruded point"):

                v1 = field
                v1 = v1.normalize().scale(Float.Named("DELTA"))
                v1 = (v1 - v0).scale(.5)

                mesh.points[top].offset = v1

            rep.top  = top
            rep.mesh = mesh

        mesh = rep.mesh
        mesh.remove_named_attribute("DELTA")

        curve = mesh.to_curve()
        curve.points.radius = gnmath.log(1 + Float.Named("Intensity"))

        curve.out("Curve")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Electric Field

    with GeoNodes("Electrostatic", is_group=True, prefix=field_prefix):

        charges_loc = Geometry(None, "Charges Locations", tip="Charge locations")
        charges_val = Float(1, "Charges Values", tip="Electric charges")
        max_len     = Float(1000, "Max Length", 1, tip="Max field vector length")

        with Layout("Mesh or Points input"):
            cloud = charges_loc.point_cloud + charges_loc.mesh.points.to_points()
            count = cloud.points.count

        with Layout("Charge values"):
            charges_val = cloud.points.capture(charges_val)

        with Repeat(field=Vector(), index=0, iterations=count) as rep:

            charge_loc = cloud.points.sample_index(nd.position, index=rep.index)
            charge_val = cloud.points.sample_index(charges_val, index=rep.index)

            v = nd.position - charge_loc
            l = v.length
            l3 = gnmath.max(1/max_len, l**3)
            rep.field += charge_val*v/l3

            rep.index += 1

        rep.field.out("E")
        Vector().out("B")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Electromagnetic field generated by a charge moving in an arbitray direction

    with GeoNodes("Moving Charge", is_group=True, prefix=field_prefix) as tree:

        charge_loc = Vector(0, "Charge Location", tip="Location of the moving charge")
        charge     = Float(1,  "Charge", tip="Value of the charge")
        speed      = Vector((.8, 0, 0), "Speed", tip="Speed of the moving charge as a percentage of speed of light.")
        max_len    = Float(1000, "Max Length", 1, tip="Max field vector length")

        with Layout("Ensure beta is not greater than 1"):
            length = speed.length
            beta   = gnmath.min(length, .999)
            speed  = speed.scale(beta/length)

        with Layout("Gamma"):
            gamma = 1/gnmath.sqrt(1 - beta**2)

        with Layout("Align speed along X axis"):
            rotation = Rotation.AlignXToVector(speed)
            inv_rot  = rotation.invert()

            rotated_position = inv_rot @ (nd.position - charge_loc)

        with Layout("Charge*gamma/rho**3"):
            rho = rotated_position.length
            gr3 = charge*gamma/rho**3

        with Layout("E and B in rotated frame"):
            E = gr3*rotated_position
            B = (gr3*beta)*Vector((0, -rotated_position.z, rotated_position.y))

        with Layout("Maximum length"):
            E = E.normalize().scale(gnmath.min(E.length, max_len))
            B = B.normalize().scale(gnmath.min(B.length, max_len))

        with Layout("Back to the initial frame"):
            E = rotation @ E
            B = rotation @ B

        E.out("E")
        B.out("B")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Electromagnetic field generated by charges along a curve

    with GeoNodes("Moving Charges on a Curve", is_group=True, prefix=field_prefix):

        source      = Curve(None, "Source Curve", tip="Curve on which charges are moving")
        count       = Integer(1, "Count", 1, 1000, tip="Number on charges on the curve")
        t           = Float(0, "t", tip="Time")
        charge      = Float(1, "Charge", tip="Charge value")
        beta        = Float(.8, "Beta", -.999, .999, tip="Charges speed in percentage of the speed of light")

        # ----------------------------------------------------------------------------------------------------
        # Main

        dt = 1/count
        centers = Cloud.Points(count=count)

        with Repeat(centers=centers, e=Vector(), b=Vector(), index=0, iterations=count) as rep:

            sample = source.sample(factor=abs(rep.index*dt + t) % 1)

            charge_loc   = sample.position_
            charge_speed = sample.tangent_.scale(beta)

            field_node = Group.Prefix(field_prefix, "Moving Charge", {
                'Charge Location': charge_loc,
                'Charge'         : charge/count,
                'Speed'          : speed,
                })

            rep.e += field_node.e
            rep.b += field_node.b

            # ----- To visualize charges locations

            rep.centers.points[rep.index].position = charge_loc

            # ----- Next

            rep.index += 1

        rep.e.out("E")
        rep.b.out("B")
        rep.centers.out("Charge Locations")

    # =============================================================================================================================
    # Lorentz transformation for electromagnetic field

    with GeoNodes("EM Lorentz", is_group=True, prefix=util_prefix):

        speed = Vector((.8, 0, 0), "Speed")
        E     = Vector(0, "E")
        B     = Vector(0, "B")

        # ----- Make sure beta is ok

        with Layout("Ensure beta is not greater than 1"):
            length = speed.length
            beta   = gnmath.min(length, .999)
            speed  = speed.scale(beta/length)

        # ----- Rotate to have speed along x axis

        with Layout("Rotate fields to have speed long x axis"):

            rotation = Rotation.AlignXToVector(speed)
            inverse  = rotation.invert()

            E_rot = inverse @ E
            B_rot = inverse @ B

        # ----- Lorentz transformation

        with Layout("Lorentz transformation"):

            gamma = (1 - beta**2)**(-.5)

            Erx, Ery, Erz = E_rot.x, E_rot.y, E_rot.z
            Brx, Bry, Brz = B_rot.x, B_rot.y, B_rot.z

            E_rot_ = Vector((Erx, gamma*(Ery - beta*Brz), gamma*(Erz + beta*Bry)))
            B_rot_ = Vector((Brx, gamma*(Bry + beta*Erz), gamma*(Brz - beta*Ery)))

        # ----- Rotate back

        with Layout("Rotate back"):
            E_ = rotation @ E_rot_
            B_ = rotation @ B_rot_

        # ----- Done

        E_.out("E")
        B_.out("B")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Electromagnetic field generated by a solenoid

    with GeoNodes("Solenoid", is_group=True, prefix=field_prefix):

        charge      = Float(1,    "Charge", tip="Total charge of the solenoid")
        beta        = Float(.8,   "Beta", -.999, .999, tip="Speed in percentage of the speed of light")
        R           = Float(1,    "Radius",  .1, 10, tip="Solenoid radius")
        loops       = Integer(10, "Loops", 1, tip="Number of loops")
        length      = Float(5,    "Length", .1, 10, tip="Solenoid length")

        with Layout("Position converted to cylindrical coordinates along x"):
            pos = nd.position
            x = pos.x._lc("x")
            r = Vector((0, pos.y, pos.z)).length._lc("r")
            lam = gnmath.atan2(pos.z, pos.y)._lc("lambda")
            cos_lam = (pos.y/r)._lc("cos lambda")
            sin_lam = (pos.z/r)._lc("sin lambda")

        with Layout("Number of charges on a each loop"):
            count = round(R*32)._lc("Count")
            circle = Mesh.Circle(vertices=count, radius=1)

        with Layout("Split Solenoid length in loops"):
            xs0 = (-length/2)._lc("xs0")
            dxs = (length/gnmath.max(1, loops-1))._lc("dxs")

        # ----------------------------------------------------------------------------------------------------
        # Loop on theta

        with Repeat(ex=0., er=0., bx=0., br=0., index=0, iterations=count) as rep_theta:

            cs = circle.points.sample_index(nd.position, index=rep_theta.index)
            cos_theta, sin_theta = (cs.x)._lc("cos theta"), cs.y._lc("sin theta")

            with Layout("Once : R2sin2 + (r - Rcos)2"):
                rho_cst = (R*sin_theta)**2 + (r - R*cos_theta)**2

            # ----------------------------------------------------------------------------------------------------
            # Loop on solenoids loops

            with Repeat(ex=rep_theta.ex, er=rep_theta.er, bx=rep_theta.bx, br=rep_theta.br, index=0, iterations=loops) as rep_xs:

                x_s = gnmath.multiply_add(rep_xs.index, dxs, xs0)._lc("x_s")
                rep_xs.index += 1

                with Layout("1/Rho**3"):
                    rho3 = (((x - x_s)**2 + rho_cst)**(-1.5))._lc("1/rho**3")

                with Layout("Ex"):
                    rep_xs.ex += (x - x_s)*rho3

                with Layout("Er"):
                    rep_xs.er += (r - R*cos_theta)*rho3

                with Layout("Bx"):
                    rep_xs.bx += (R - r*cos_theta)*rho3

                with Layout("Br"):
                    rep_xs.br += (x - x_s)*cos_theta*rho3

            # ----- Next loop

            rep_theta.ex += rep_xs.ex
            rep_theta.er += rep_xs.er
            rep_theta.bx += rep_xs.bx
            rep_theta.br += rep_xs.br

            rep_theta.index += 1

        # ----------------------------------------------------------------------------------------------------
        # Finalize the fields

        with Layout("-2*gamma*charge"):
            gam_charge = (-2*charge/count/loops)*(1 - beta**2)**(-0.5)

        with Layout("Electric Field"):
            E = Vector((
                rep_theta.ex,
                rep_theta.er*cos_lam,
                rep_theta.er*sin_lam,
            )).scale(gam_charge)

        with Layout("Magnetic Field"):
            B = Vector((
                rep_theta.bx,
                rep_theta.br*cos_lam,
                rep_theta.br*sin_lam,
            )).scale(gam_charge*beta)

        E.out("E")
        B.out("B")

    # ----------------------------------------------------------------------------------------------------
    # Magnet field

    with GeoNodes("Magnet", is_group=True, prefix=field_prefix):

        width_scale = Float(1., "Width Scale",  0.01, tip="Width scale")
        location    = Vector(0, "Location", tip="Magnet location")
        rotation    = Rotation(0, "Rotation", tip="Magnet rotation")
        speed       = Vector(0, "Speed", tip="Magnet speed in percentage of the speed of light")

        # ----- Computation is made for a magnet centered along the x axis

        with Layout("Center Magnet and align along x"):
            position = rotation.invert() @ (nd.position - location)
            x, y, z = position.x, position.y, position.z

        # ----- Plane passing through x axis

        with Layout("Plane containing point and x axis"):
            angle = gnmath.atan2(z, y)
            rot_y = gnmath.sqrt(y**2 + z**2)

        # ----- Width scale

        y_ = rot_y/width_scale

        # ----- Normalized radius

        r = (x**2 + y_**2)/2/y_

        # ----- Normalized B

        B = Vector(((r - y_)/width_scale, x, 0)).normalize()

        # ----- Rotation

        B = Rotation((angle, 0, 0)) @ B

        # ----- Back to the initial frame

        B = rotation @ B

        with Layout("Take speed into account"):

            transf_node = Group.Prefix(util_prefix, "EM Lorentz", {'Speed': speed, 'B': B})
            E = transf_node.e
            B = transf_node.b

        # ----- Done

        E.out("E")
        B.out("B")

    # =============================================================================================================================
    # Points in space where to compute the fields

    with GeoNodes("Source Points", prefix=util_prefix):

        location = Vector(0,         "Location")
        size     = Vector((5, 5, 5), "Size")
        density  = Float(1,          "Density")
        rotation = Rotation(0,       "Rotation")
        max_dist = Float(100,        "Max Distance", 1, tip="Remove points farther than maximum distance to the center")
        center   = Vector(0,         "Center for Max Distance", tip="Center to compute maximum distance")
        seed     = Integer(0,        "Seed")

        geo = Geometry()

        with Layout("Points on faces"):
            pts_faces_cloud = Mesh(geo).faces.distribute_points(density=density, seed=seed)

        with Layout("Points in volume"):
            pts_vol_cloud = Mesh(geo).to_volume(density=density).distribute_points(seed=seed)

        with Layout("Plane"):
            grid = Mesh.Grid(size.x, size.y, 2, 2)
            plane_cloud = grid.faces.distribute_points(density=density, seed=seed)

        with Layout("Disk"):
            disk = Mesh.Disk()
            disk.transform(scale=(size.x, size.y, 1))
            disk_cloud = disk.faces.distribute_points(density=density, seed=seed)

        with Layout("Cube"):
            cube = Mesh.Cube(size)
            cube_cloud = cube.to_volume(density=density).distribute_points(seed=seed)

        with Layout("Cylinder"):
            cyl = Mesh.Cylinder(depth=1)
            cyl.transform(scale=(size.x, size.y, size.z))
            cyl_cloud = cyl.to_volume(density=density).distribute_points(seed=seed)

        with Layout("Sphere"):
            sphere = Mesh.UVSphere()
            sphere.transform(scale=(size.x, size.y, size.z))
            sphere_cloud = sphere.to_volume(density=density).distribute_points(seed=seed)

        cloud = Cloud.MenuSwitch(items={
            'Input Geometry'   : Cloud(geo),
            'Points on faces'  : pts_faces_cloud,
            'Points in volume' : pts_vol_cloud,
            'Plane'            : plane_cloud,
            'Disk'             : disk_cloud,
            'Cube'             : cube_cloud,
            'Cylinder'         : cyl_cloud,
            'Sphere'           : sphere_cloud,
        }, menu='Cube', name='Shape')

        cloud.transform(translation=location, rotation=rotation)
        cloud.points[nd.position.distance(center).greater_than(max_dist)].delete()

        cloud.out()

    # =============================================================================================================================
    # Visualize some of the fields

    with GeoNodes("Field", prefix=show_prefix):

        field = Vector(0, "Field", tip="Field to visualize")

        cloud = Cloud(name='Geometry')

        with Layout("Arrows:"):

            show_arrows = Boolean(True, "Show arrows")

            arrows_group = Group("Arrows", {'Geometry': cloud, 'Vectors': field})
            arrows_group.link_input_from(include=['Scale', 'Logarithm'], rename={'Color': 'Arrow Color'})
            arrows_mat = Material("Arrow", "Arrows Material")
            arrows_group.shaft = arrows_mat
            arrows_group.head  = arrows_mat
            arrows = arrows_group._out

        with Layout("Lines of field computation"):
            lines_group = Group.Prefix(util_prefix, "Lines of Field", {
                'Geometry': cloud,
                'Field': field,
                'Direction': Integer.Random(0, 1, seed=0)*2 - 1,
            })
            curves = Curve(lines_group._out)

        with Layout("Lines of field as mesh"):
            show_lines = Boolean(False, "Lines of Field")
            lines_color = Color(None, "Lines Color")
            curves.points.store("Color", lines_color)
            curves.points.store("Transparency", 1 - lines_color.alpha)

            mesh_curves = curves.to_mesh(profile_curve=Curve.Circle(radius=Float(.02, "Lines Section", 0)), fill_caps=True)
            mesh_curves.faces.smooth = True
            mesh_curves.faces.material = Material("Arrow", "Lines material")

        with Layout("Arrows on lines of field"):
            show_lines_arrows = Boolean(False, "Arrows on Lines")
            lar_delta = Float(.5, "Interval",.1, tip="Distance between arrows on the lines of field")
            lar_scale = Float(1., "Lines Arrows Scale",.01, tip="Scale of arrows on the lines of field")
            lar_origins = Curve(curves).resample(length=gnmath.max(.1, lar_delta))
            lar_vectors = lar_origins.tangent.scale(Float.Named("Intensity")*lar_scale)

            lar_group = Group("Arrows", {'Geometry': lar_origins, 'Vectors': lar_vectors})
            lar_group.link_input_from(include=[], rename={'Logarithm': 'Lines Arrows Log', 'Color': 'Lines Arrows Color'})

            lar_arrows = lar_group._out

        geo = Mesh.Switch(show_arrows, None, arrows)
        geo += Mesh.Switch(show_lines, None, mesh_curves)
        geo += Mesh.Switch(show_lines_arrows, None, lar_arrows)

        geo.out()

    # =============================================================================================================================
    # Visualize some of the fields

    with GeoNodes("Visualize some fields"):

        # ----------------------------------------------------------------------------------------------------
        # Source points

        # Make sure Input geometry exists

        geo = Geometry()

        source_node = Group.Prefix(util_prefix, "Source Points")
        source_node.link_input_from(include=['Geometry', 'Size', 'Density', 'Seed', 'Shape'])
        cloud = source_node._out

        use_magnetic = Boolean(False, "Magnetic Field", tip="Magnetic field if True, electric field otherwise")

        with Layout("Static Electric field from charges"):
            node = Group.Prefix(field_prefix, "Electrostatic",{
                'Charges Locations' : Cloud.Points(count=6, position=Vector.Random(-1, 1, seed=100+seed)),
                'Charges Values'    : Float.Random(-1, 1, seed=101+seed),
                })
            static_field = node.e.switch(use_magnetic, node.b)

        with Layout("Moving charge"):
            node = Group.Prefix(field_prefix, "Moving Charge")
            moving_field = node.e.switch(use_magnetic, node.b)

        with Layout("Solenoid"):
            node = Group.Prefix(field_prefix, "Solenoid")
            solenoid_field = node.e.switch(use_magnetic, node.b)

        with Layout("Magnet"):
            node = Group.Prefix(field_prefix, "Magnet")
            magnet_field = node.e.switch(use_magnetic, node.b)


        field = Vector.MenuSwitch({
            'Electrostatic' : static_field,
            'Moving charge' : moving_field,
            'Solenoid'      : solenoid_field,
            'Magnet'        : magnet_field,
            }, menu=0, name='Field', tip="Field to visualize")

        show_node = Group.Prefix(show_prefix, "Field", {
            'Geometry': cloud,
            'Field': field,
        })

        show_node.link_input_from()
        geo = show_node._out

        geo.out()
