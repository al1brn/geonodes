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

module : demo fields
--------------------

Electromagntic fields computation

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/fields.py)

To compute an electromagnetic, you need two sets of locations:
- location of the electric charges
- location of the points in the spac where you want to compute the field

The modifiers and groups form two parts:
- field computation at given positions
- field visu either as arrows or as lines of fields

To visualize a field, you have to stack 3 groupds:
1. Compute a field giving E and B (for instance "Compute Electric Charges")
2. Chose points where to compute the field (for instance with "Field Computation Points" group)
3. Chose Arrows or Lines of Field to visualize E or B

The modifier "Fields Show Case" is an example of this process.

> [!NOTE]
> Modifiers:
> - Field Computation Points: generated points in space where to compute the field
> - Field Lines: visualize the lines of fields at starting positions
> - Field Arrows: visualize field arrows at given positions
> - Compute Electric Charges: compute E and B from a set of electric charges
> - Compute Solenoid: compute E & B for a solenoid
> - Compute Magnet: compute B for a normalized magnet
> - Fields Show Case: shows how to combine the modifiers to visualize fields

``` python
from geonodes.demos import fields

fields.demo()
```
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

        cloud.remove_names("TEMP *")

        cloud.out()

    # =============================================================================================================================
    # Field visualization

    # -----------------------------------------------------------------------------------------------------------------------------
    # Lines of field

    with GeoNodes("Field Lines"):

        geo = Geometry()

        field = Vector(None, "Field", tip="Field vector at the input geometry points", hide_value=True)

        with Panel("Lines Parameters"):
            iterations  = Integer(20, "Iterations", 1, tip="Number of iterations per line")
            delta       = Float(.1, "Delta", .001, tip="Distance to move at each iteration")
            direction   = Integer(1, "Direction",  tip="Move forwards (+1) or backwards (-1)")

        with Panel("Lines"):
            keep_curves = Boolean(False, "Keep Curves")
            line_radius = Float(.02, "Radius",0.)
            line_resol  = Integer(12, "Resolution", 3)
            line_mat    = Material("Arrow", "Material")
            line_color  = Color((0, 0, 1), "Color")

        with Layout("Prepare Mesh"):
            mesh = geo.mesh.points.delete_edge_face() + geo.point_cloud.to_vertices()
            mesh.points.store("DELTA", delta*direction)

        # ----------------------------------------------------------------------------------------------------
        # Extrusion loop

        with Repeat(mesh=mesh, top=True, iterations=iterations) as rep:

            mesh = rep.mesh

            with Layout("Displacement from current points"):

                v0 = field
                l0 = v0.length()

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

        with Layout("Curves"):
            mesh.remove_named_attribute("DELTA")

            curve = mesh.to_curve()
            curve.points.radius = gnmath.log(1 + Float.Named("Intensity"))

        with Layout("To Mesh"):

            mesh_lines = curve.to_mesh(profile_curve=Curve.Circle(radius=line_radius, resolution=line_resol))
            mesh_lines.faces.material = line_mat
            mesh_lines.faces._Color = line_color
            mesh_lines.faces.smooth = True

        mesh_lines.switch(keep_curves, curve).out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Arrows

    with GeoNodes("Field Arrows"):

        geo = Geometry()

        field = Vector(None, "Field", tip="Field vector at the input geometry points", hide_value=True)

        with Layout("Prepare Mesh"):
            mesh = geo.mesh.points.delete_edge_face() + geo.point_cloud.to_vertices()
            mesh.points.store("DELTA", delta*direction)

        node = Group("Arrows", geometry=geo, vector=field, link_from='TREE')

        node.geometry.out()


    # =============================================================================================================================
    # Field computation

    # -----------------------------------------------------------------------------------------------------------------------------
    # E & B from a single electric charge

    with GeoNodes("Compute Moving Electric Charge", is_group=True):

        pos = Vector.Position()

        with Panel("Charge"):
            charge_loc = Vector(0, "Charge Location", tip="Location of the moving charge")
            charge     = Float(1,  "Charge", tip="Value of the charge")
            speed      = Vector((.8, 0, 0), "Speed", tip="Speed of the moving charge as a percentage of speed of light.")
            max_len    = Float(1000, "Max Length", 1, tip="Max field vector length")

        with Layout("Ensure beta is not greater than 1"):
            length = speed.length()
            beta   = gnmath.min(length, .999)
            speed  = speed.scale(beta/length)

        with Layout("Gamma"):
            gamma = 1/gnmath.sqrt(1 - beta**2)

        with Layout("Align speed along X axis"):
            rotation = Rotation.AlignXToVector(speed)
            inv_rot  = rotation.invert()

            rotated_position = inv_rot @ (nd.position - charge_loc)

        with Layout("Charge*gamma/rho**3"):
            rho = rotated_position.length()
            gr3 = charge*gamma/rho**3

        with Layout("E and B in rotated frame"):
            E = gr3*rotated_position
            B = (gr3*beta)*Vector((0, -rotated_position.z, rotated_position.y))

        with Layout("Maximum length"):
            E = E.normalize().scale(gnmath.min(E.length(), max_len))
            B = B.normalize().scale(gnmath.min(B.length(), max_len))

        with Layout("Back to the initial frame"):
            E = rotation @ E
            B = rotation @ B

        E.out("E")
        B.out("B")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Electric charges
    # E & B from several moving electric charges

    with GeoNodes("Compute Electric Charges", is_group=True):

        pos = Vector.Position()

        with Panel("Charges"):
            geo    = Geometry(None, "Charge Locations", tip="Charge locations")
            charge = Float(1, "Charges", tip="Electric charges")
            speed  = Vector(0, "Speed", tip="Speed of the moving charge as a percentage of speed of light.")

        cloud = geo.point_cloud + geo.mesh.to_points() + geo.curve.to_points()

        with Panel("Options"):
            max_len = Float(1000, "Max Length", 1, tip="Max field vector length", single_value=True)

        with Repeat(cloud=cloud, charge=charge, speed=speed, field_e=Vector(), field_b=Vector(), iterations=cloud.points.count) as rep:

            rep_loc    = rep.cloud.points.sample_index(nd.position, rep.iteration)
            rep_charge = rep.cloud.points.sample_index(rep.charge,  rep.iteration)
            rep_speed  = rep.cloud.points.sample_index(rep.speed,   rep.iteration)

            node = Group("Compute Moving Electric Charge", position=pos, charge_location=rep_loc, charge=rep_charge, speed=rep_speed)

            rep.field_e += node.e
            rep.field_b += node.b

        rep.field_e.out("E")
        rep.field_b.out("B")

    # =============================================================================================================================
    # Lorentz transformation for electromagnetic field

    with GeoNodes("Compute EM Lorentz", is_group=True):

        speed = Vector((.8, 0, 0), "Speed")
        E     = Vector(0, "E")
        B     = Vector(0, "B")

        # ----- Make sure beta is ok

        with Layout("Ensure beta is not greater than 1"):
            length = speed.length()
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

    with GeoNodes("Compute Solenoid", is_group=True):

        pos = Vector.Position()

        with Panel("Solenoid"):
            charge      = Float(1,    "Charge", tip="Total charge of the solenoid")
            beta        = Float(.8,   "Beta", -.999, .999, tip="Speed in percentage of the speed of light")
            R           = Float(1,    "Radius",  .1, 10, tip="Solenoid radius")
            loops       = Integer(10, "Loops", 1, tip="Number of loops")
            length      = Float(5,    "Length", .1, 10, tip="Solenoid length")

        with Layout("Position converted to cylindrical coordinates along x"):
            x = pos.x._lc("x")
            r = Vector((0, pos.y, pos.z)).length()._lc("r")
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

        with Layout("Solenoid vis"):
            sol = Curve.Spiral(start_radius=R, end_radius=R, rotations=loops, height=length)
            sol.transform(rotation=(0, pi/2, 0), translation=(-length/2, 0, 0))

        sol.out("Solenoid")

    # ----------------------------------------------------------------------------------------------------
    # Magnet field

    with GeoNodes("Compute Magnet", is_group=True):

        pos = Vector.Position()

        with Panel("Magnet"):
            width_scale = Float(1., "Width Scale",  0.01, tip="Width scale")
            location    = Vector(0, "Location", tip="Magnet location")
            rotation    = Rotation(0, "Rotation", tip="Magnet rotation")
            speed       = Vector(0, "Speed", tip="Magnet speed in percentage of the speed of light")

        # ----- Computation is made for a magnet centered along the x axis

        with Layout("Center Magnet and align along x"):
            position = rotation.invert() @ (pos - location)
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

            transf_node = Group("Compute EM Lorentz", {'Speed': speed, 'B': B})
            E = transf_node.e
            B = transf_node.b

        # ----- Done

        E.out("E")
        B.out("B")


    # =============================================================================================================================
    # Points in space where to compute the fields

    with GeoNodes("Field Computation Points"):

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
            #disk = Mesh.Disk()
            disk = Mesh.Circle(fill_type='NGON')
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

    with GeoNodes("Fields Show Case"):

        # ----------------------------------------------------------------------------------------------------
        # Source points

        source = Group("Field Computation Points", geometry=Mesh.Cube(),
            size = 10,
            density=.1,
            shape='Cube',
            seed=100).geometry
        use_B = Boolean(False, "Magnetic Field")
        vis_arrows = Boolean(False, "Arrows")
        vis_lines  = Boolean(True, "Lines of Field")
        line_sect  = Float(.02, "Lines Section")

        # ----------------------------------------------------------------------------------------------------
        # Single Charge

        fields = {}

        with Layout("Single Electric Charge"):
            node = Group("Compute Electric Charges", charge_locations=Cloud.Points(1))
            fields['Single Charge'] = node.e.switch(use_B, node.b)

        with Layout("7 Electric Charges"):
            locs = Cloud.Points(7, position=Vector.Random(-5, 5, seed=10))
            node = Group("Compute Electric Charges", charge_locations=locs, charges=Float.Random(-1, 1, seed=11))
            fields['7 Electric Charges'] = node.e.switch(use_B, node.b)

        with Layout("Electric Line"):
            line = Curve.LinePoints((0, 0, -2), (0, 0, 2)).resample(30)
            node = Group("Compute Electric Charges", charge_locations=line, charges=1, speed=(0, 0, .8))
            fields['Electric Line'] = node.e.switch(use_B, node.b)

        with Layout("Solenoid"):
            node = Group("Compute Solenoid", charge=1, beta=.8, radius=1, loops=10, length=5)
            fields['Solenoid'] = node.e.switch(use_B, node.b)

        field = Vector.MenuSwitch(fields, menu=0, name='Field')

        # ----- Arrows

        arrows = Group("Field Arrows", geometry=source, field=field, color=(0, 0, 1)).geometry

        # ----- Lines of field

        d = Integer.Random(0, 1, seed=10000)*2 - 1
        lines = Group("Field Lines", geometry=source, field=field,
            direction=d,
            iterations=50,
            delta=.5,
            radius=line_sect,
            color=(0, 1, 0)).geometry

        geo = Geometry.Switch(vis_arrows, None, arrows) + Geometry.Switch(vis_lines, None, lines)

        geo.out()
