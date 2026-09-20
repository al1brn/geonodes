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

module : demo common utilities
------------------------------

Common utilities

updates
-------
- creation :   2026/07/23

"""

from geonodes import *
from geonodes.demos.shaders import arrow_shader, formula_shader

def load():
    if G.get_tree(".Vector Input") is None:
        demo()

def demo():

    arrow_shader()
    formula_shader()

    # ====================================================================================================
    # Vector input
    # ====================================================================================================

    with GeoNodes(".Vector Input", is_group=True):

        geo = Geometry()

        input_index = Integer.MenuSwitch({
            'XYZ' : 0,
            'Cylindrical' : 1,
            'Spherical' : 2,
            'Object Location' : 3,
            'Curve Position' : 4,
            'Curve Tangent' : 5,
            'Track to' : 6,
            'Track to Bundle' : 7,
        }, menu=Input("Type"))

        vector = Vector(None, "Vector")
        R = Float(None, "R")
        phi = Float.Angle(None, "Phi")
        z = Float(None, "z")
        theta = Float.Angle(None, "Theta")

        # Curve
        obj = Object(name="Curve")
        curve_fac = Float.Factor(0.5, "Curve Factor", 0, 1)
        curve_scale = Float(1.0, "Curve Scale")

        # Bundle
        use_bundle = Boolean(False, "From Bundle")
        bundle_index = Integer(0, "List Index", 0)
        self_pos = Vector(None, "Self Position", hide_value=True)

        with Layout("Curve & Tracking"):
            obj_info = obj.info()
            obj_geo = obj_info.geometry

            curve_node = Curve(obj_geo).sample_factor(factor=curve_fac).node

            obj_pos = obj_info.location
            bund_pos = obj_geo.get_bundle().separate(signature={'Position': Vector}).position

            obj_pos = (obj_pos - self_pos).normalize()
            bund_pos = (bund_pos - self_pos).normalize()

        with Layout("User Input"):
            vec = Vector.IndexSwitch(

                vector,
                G().combine_cylindrical(R=R, phi=phi, z=z),
                G().combine_spherical(R=R, phi=phi, theta=theta),

                obj_info.location,

                curve_node.position,
                curve_node.tangent.scale(curve_scale),

                obj_pos,
                bund_pos,

                index=input_index)

            

        with Layout("From Bundle"):
            bundle = geo.get_bundle().separate(signature={
                'Vectors': Vector,
                'Vector Names': String})

            count = bundle.vectors.list_length()
            error = bundle_index.greater_equal(count)

            bundle_vec = bundle.vectors[bundle_index]
            vec_name = bundle.vector_names[bundle_index]
            vec.switch(use_bundle, bundle_vec)

            (use_bundle & error.bnot()).info("Bundle: " + vec_name)
            (use_bundle & error).error("Bundle index " + bundle_index.to_string() + ' > ' + count.to_string())

        vec.out()

    # ====================================================================================================
    # Value input
    # ====================================================================================================

    with GeoNodes(".Value Input", is_group=True):

        geo = Geometry()

        value = Float(0, "Value")

        use_bundle = Boolean(False, "From Bundle")
        bundle_index = Integer(0, "List Index", 0)

        with Layout("From Bundle"):
            bundle = geo.get_bundle().separate(signature={
                'Values': Float,
                'Value Names': String})

            count = bundle.values.list_length()
            error = bundle_index.greater_equal(count)

            bundle_val = bundle.values[bundle_index]
            val_name = bundle.value_names[bundle_index]
            value.switch(use_bundle, bundle_val)

            (use_bundle & error.bnot()).info("Bundle: " + val_name)
            (use_bundle & error).error("Bundle index " + bundle_index.to_string() + ' > ' + count.to_string())

        value.out()

    # ====================================================================================================
    # Join a geometry with a Show factor
    #
    # Show is between 0 and 1
    # Add the attribute Transparency = 1 - show on mesh faces before joining
    # ====================================================================================================

    with GeoNodes(".Join Mesh With Show", is_group=True):
        geo = Geometry(name="Geometry")

        mesh = Mesh(name="Mesh")
        show = Float.Factor(1.0, "Show", 0, 1)

        mesh.switch(show.equal(0))
        mesh.faces.set('Transparency', 1.0 - show)

        (geo + mesh).out()

    # ====================================================================================================
    # Encapsulate strings to curves to centralize the font
    # ====================================================================================================

    if G.get_tree(".String to Curves") is None:

        with GeoNodes(".String to Curves", is_group=True):

            node = Node("String to Curves", font="BFont Regular").link_inputs()

            node.out()

    # ====================================================================================================
    # Dynamic Object
    # ====================================================================================================

    with GeoNodes("Dynamic Object"):

        geo = Geometry()
        show = Float(1.0, "Show", 0, 1)

        position = G()._vector_input(from_bundle=False, list_index=0).link_inputs(from_panel="Position")
        velocity = G()._vector_input(from_bundle=False, list_index=0, self_position=position).link_inputs(from_panel="Velocity")
        acceleration = G()._vector_input(from_bundle=False, list_index=0, self_position=position).link_inputs(from_panel="Acceleration")
        free_vector =  G()._vector_input(from_bundle=False, list_index=0, self_position=position).link_inputs(from_panel="Free Vector")

        mass = Float(1.0, "Mass")
        free_value = Float(0.0, "Free Value")

        color = Color(name="Color")
        geo.set('Color', color, domain='Face')
        geo.set('Transparency', 1.0 - show, domain='Face')

        with Layout("Tangent / Radial Acceleration"):
            nvel = velocity.normalize()
            tan_acc = nvel.scale(acceleration.dot(nvel))
            rad_acc = acceleration - tan_acc

        with Layout("Tangent / Radial Velocity"):
            nacc = acceleration.normalize()
            tan_vel = nacc.scale(velocity.dot(nacc))
            rad_vel = velocity - tan_vel

        with Layout("Kinetic energy"):
            impulsion = velocity.scale(mass)
            kinetic = (mass/2)*velocity**2

        vectors = Vector.List(
            position, 
            velocity, 
            acceleration,
            free_vector,
            impulsion,
            tan_acc,
            rad_acc,
            tan_vel,
            rad_vel,
            )
        vec_names = String.List(
            "Position", 
            "Velocity", 
            "Acceleration",
            "Free Vector",
            "Impulsion",
            "Tangent Acceleration",
            "Radial Acceleration",
            "Tangent Velocity",
            "Radial Velocity",
        )

        values = Float.List(
            mass,
            free_value,
            kinetic,
            impulsion.length(),
        )

        val_names = String.List("Mass", "Free Value", "Kinetic", "Impulsion")

        with Bundle() as bundle:
            position.out("Position")
            velocity.out("Velocity")
            acceleration.out("Acceleration")
            free_vector.out("Free Vector")            
            impulsion.out("Impulsion")

            mass.out("Mass")
            free_value.out("Free Value")
            kinetic.out("Kinetic")

            vectors.out("Vectors")
            vec_names.out("Vector Names")
            values.out("Values")
            val_names.out("Value Names")

        geo.set_bundle(bundle)

        geo.offset = position

        geo.out()

    # ====================================================================================================
    # Display a value
    # ====================================================================================================

    with GeoNodes("Value Display"):

        geo = Geometry()
        
        show = Float.Factor(1.0, "Show", 0, 1)
        offset = Vector(0, "Offset")

        position = geo.get_bundle().separate(signature={'Position': Vector}).position
        position += offset

        use_string = Boolean(False, "Use String")
        #value = Float(0.0, "Value")
        value = G()._value_input(geo).link_inputs()
        decimals = Integer(2, "Decimals", 0, 5)
        string_value = String("", "String")

        size = Float(1.0, "Size")
        mat = Material("Formula", "Material")
        color = Color("Black", "Color")
        
        s = value.to_string(decimals=decimals)
        s.switch(use_string, string_value)

        curves = G()._string_to_curves(
            s,
            size = size,
            align_x = Input("X Align"),
            align_y = Input("Y Align"),
        )

        text = Curve(curves.realize()).fill()
            
        text.faces.material = mat
        text.faces.store_named_attribute("face_color", color)

        with Layout("Orientation"):
            track_to = Boolean(False, "Track to")
            obj = Object(None, "Tracked")

            with Rotation.Switch(track_to) as rot:
                Rotation.MenuSwitch({
                        'XY' : (0.0, 0.0, 0.0),
                        'XZ' : (pi/2, 0.0, 0.0),
                        'YZ' : (pi/2, 0.0, pi/2),
                    }, menu=Input("Plane"),
                ).out("False")

            with rot:
                cam_info = obj.info(transform_space='RELATIVE')

                to_camera = cam_info.location - position
                camera_up = cam_info.rotation.rotate_vector((0.0, 1.0, 0.0))

                Rotation.FromAxes(
                    to_camera,
                    camera_up,
                    primary_axis='Z',
                    secondary_axis='Y',
                ).out("True")


            text.transform(translation=position, rotation=rot)

        G()._join_mesh_with_show(geo, text, show).out()

    # ====================================================================================================
    # Camera Culling
    # ====================================================================================================

    with GeoNodes("Camera Culling"):
        
        pts = Cloud(Geometry())
        focal = Float(0.05, "Focal", 0.001)
        size = Vector((36, 36/16*9, 0), "Sensor Size", dimensions=2)
        margin = Float(1.01, "Margin", .1, 2)
        
        
        with Layout("Transformation"):
            cam = nd.active_camera.info()
            transformed = Cloud(pts).transform(transform=cam.transform.invert(), mode='Matrix')
            
        with Layout("Projection"):
            
            x, y, z = nd.position.xyz
            visible = z < -focal
            transformed.points.set("Hidden", visible.bnot())
            
            ratio = -focal/z
            transformed[visible].position = (x*ratio, y*ratio, -focal)
            
        
        with Layout("To Delete"):
            
            sx, sy, _ = size.scale(focal/100*margin).xyz
            x, y, z  = nd.position.abs().xyz
            
            delete = Attribute("Hidden", Boolean).value | (x >= sx) | (y >= sy)
            
            delete = transformed.points.sample_index(delete, index=nd.index)

            pts.points[delete].delete()        
            
        Geometry(pts).out() 
        delete.bnot().out("Visible")
        delete.out("Hidden")

    # ====================================================================================================
    # Bounce
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Bounce Max
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Bounce Max", is_group=True):
        
        x = Float(0, "X")
        v = Float(0, "Speed")
        max = Float(1, "Max")
        efac = Float.Factor(1.0, "Energy Factor", 0.0, 2.0)
        
        bounce = x > max
        dx = x - max
        x.switch(bounce, max - dx*efac).out("X")
        v.switch(bounce, -v*efac).out("Speed")
        bounce.out("Bounce")
        
    # ----------------------------------------------------------------------------------------------------
    # Bounce Min Max
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes("Bounce Min Max", is_group=True):
        
        x = Float(0, "X")
        v = Float(0, "Speed")
        min = Float(1, "Min")
        max = Float(1, "Max")
        size = Float(0, "Size")
        efac = Float.Factor(1.0, "Energy Factor", 0.0, 2.0)
        
        x = G()._bounce_max(x=x, speed=v, max=max - size, energy_factor=efac)
        v = x.speed
        bounce = x.bounce
        
        x2 = G()._bounce_max(x=-x, max=-min + size, energy_factor=efac)
        x.switch(x2.bounce, -x2)
        v.switch(x2.bounce, -v)
        bounce.switch(x2.bounce, True)

        x.out("X")
        v.out("Speed")
        bounce.out("Bounce")
        
    # ----------------------------------------------------------------------------------------------------
    # Bounce Box
    # ----------------------------------------------------------------------------------------------------
            
    with GeoNodes("Bounce Box", is_group=True):
        
        use_3D = Boolean(True, "3D")
        
        pos = Vector(None, "Position")
        speed = Vector(None, "Speed")
        pmin = Vector(None, "Min")
        pmax = Vector(None, "Max")
        size = Vector(None, "Size")
        efac = Float.Factor(1.0, "Energy Factor", 0.0, 2.0)
        
        x, y, z = pos.xyz
        vx, vy, vz = speed.xyz
        sx, sy, sz = size.xyz
        
        xmin, ymin, zmin = pmin.xyz
        xmax, ymax, zmax = pmax.xyz
        
        x = G().bounce_min_max(x, vx, min=xmin, max=xmax, size=sx, energy_factor=efac)
        vx = x.speed
        bounce = x.bounce

        y = G().bounce_min_max(y, vy, min=xmin, max=xmax, size=sy, energy_factor=efac)
        vy = y.speed
        bounce |= y.bounce
        
        z_ = G().bounce_min_max(z, vz, min=zmin, max=zmax, size=sz, energy_factor=efac)
        vz_ = z_.speed
        zbounce  = z_.bounce
        
        Vector((x, y, z.switch(use_3D, z_))).out("Position")
        Vector((vx, vy, vz.switch(use_3D, vz_))).out("Speed")
        bounce.switch(use_3D, bounce | zbounce).out("Bounce")

    # ----------------------------------------------------------------------------------------------------
    # Particles in a box
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Particles in a Box"):

        count = Integer(100, "Count", 10)
        speed = Float(1, "Speed", 0)
        box = Vector((1, 1, 1), "Box")
        efac = Float.Factor(1.0, "Energy Factor", 0, 2)
        seed = Integer(0, "Seed")
        
        with Layout("Points"):    
            box_min = box.scale(-0.5)
            box_max = box.scale( 0.5)
            
            pts = Cloud.Points(count=count, position=Vector.Random(box_min - 0.01, box_max + 0.01, seed=seed))
            seed += 1
            rot = Rotation(Vector.Random(-pi, pi, seed=seed))
            seed += 1
            n = Float.Random(speed/2, speed*1.5, seed=seed)

            v = rot.rotate_vector((0, 0, n))
            pts.set('Speed', v)
            
        for sim in simulation(pts=pts):
            v = sim.pts.get('Speed', Vector).value
            pos = nd.position + v.scale(sim.delta_time)
            pos = G().bounce_box(position=pos, speed=v, min=box_min, max=box_max, energy_factor=efac)
            
            sim.pts.position = pos
            sim.pts.set('Speed', pos.speed)
            

        sim.pts.out()

    # ====================================================================================================
    # Rounded Rectangle
    # ====================================================================================================

    with GeoNodes("Rounded Rectangle"):
        
        sx = Float(1, "Size X")/2
        sy = Float(.5, "Size Y")/2
        rd_fac = Float.Factor(0.1, "Rounded", 0, 1)
        
        rd_size = gnmath.min(sx, sy)    
        rd = rd_size*rd_fac
        
        line = Curve.Line().resample(count=8)
        
        line.splines.type = "BEZIER"
        
        idx = [nd.index == i for i in range(8)]
        
        corners = [
            Vector((-sx+rd, -sy,    0)),
            Vector(( sx-rd, -sy,    0)),
            Vector(( sx,    -sy+rd, 0)),
            Vector(( sx,     sy-rd, 0)),
            Vector(( sx-rd,  sy,    0)),
            Vector((-sx+rd,  sy,    0)),
            Vector((-sx,     sy-rd, 0)),
            Vector((-sx,    -sy+rd, 0)),
        ]
        
        for i in range(8):
            line[idx[i]].position = corners[i]
        
        
        tg=rd*0.552125
        
        line[idx[0]].left_handle_position  = corners[0] + (-tg,   0, 0)
        line[idx[1]].right_handle_position = corners[1] + ( tg,   0, 0)
        line[idx[2]].left_handle_position  = corners[2] + (  0, -tg, 0)
        line[idx[3]].right_handle_position = corners[3] + (  0,  tg, 0)
        line[idx[4]].left_handle_position  = corners[4] + ( tg,   0, 0)
        line[idx[5]].right_handle_position = corners[5] + (-tg,   0, 0)
        line[idx[6]].left_handle_position  = corners[6] + (  0,  tg, 0)
        line[idx[7]].right_handle_position = corners[7] + (  0, -tg, 0)
        
        line.is_cyclic = True
        
        line.out()
            
            
    
        
        
        
                
                
                
    



    





    

