from geonodes import *


def stretch(geo, delta, selection=True):
    with Layout("Stretch"):
        x, y, _ = nd.position.normalize().xyz
        geo[selection].offset = x*delta, y*delta, 0.0
        return geo

def demo():

    # ====================================================================================================
    # Thicken a flat shape
    # ====================================================================================================

    with GeoNodes("Thicken Flat XY"):

        mesh = Mesh()
        thickness = Float.Distance(0.4, "Thickness", 0.0)
        with Panel("Bevel"):
            bevel = Float.Distance(0.01, "Size", 0.0)
            bevel_count = Integer(1, "Lines", 0, 16)
            bevel_shape = Float.Factor(1, "Shape", -1, 1)   

        with Layout("Copy to Cyldinder"):
            n = mesh.points.count
            circ_count = 2*(1 + bevel_count)
            cyl = Mesh.Cylinder(vertices=n, radius=1.0, depth=thickness, side_segments=1 + 2*bevel_count)

            circ_index = nd.index // n

            pos = mesh.points.sample_index(nd.position, index=nd.index % n)
            x, y, _ = pos.xyz
            z = nd.position.z

            cyl.points.position = (x, y, z)

        for rep in repeat(bevel_count + 1, mesh=cyl):

            radius = nd.position.length()

            ag = pi/2 - rep.iteration/(bevel_count + 1) * pi/2
            br = bevel*ag.cos()
            bz = bevel*ag.sin()

            r0 = radius - bevel
            z0 = thickness/2 - bevel

            r = bevel_shape.map_range(-1, 1, radius - bz, r0 + br)
            z = bevel_shape.map_range(-1, 1, thickness/2 - br, z0 + bz)

            v = nd.position.normalize().scale(r)
            v = mesh.points.sample_index(v, index=nd.index % n)
            x, y, _ = v.xyz

            rep.mesh.points[circ_index.equal(rep.iteration)].position = (x, y, z)
            rep.mesh.points[circ_index.equal(circ_count - 1 - rep.iteration)].position = (x, y, -z)

        mesh = rep.mesh

        with Layout("Null Thickness"):
            disk = Mesh.Circle(vertices=n, fill_type="N-Gon")
            disk.position = mesh.points.sample_index(nd.position, index=nd.index)

        mesh.switch(thickness.equal(0.0), disk)
        mesh.mesh.out()

    # ====================================================================================================
    # Cylinder with bevel
    # ====================================================================================================

    with GeoNodes("Cylinder"):

        radius = Float.Distance(1.0, "Radius", 0.1)
        vertices = Integer(32, "Vertices", 3)
        depth = Float.Distance(1.0, "Depth", 0.1)

        circ = Mesh.Circle(radius=radius, vertices=vertices)
        cyl = G().thicken_flat_xy(circ, thickness=depth).link_inputs()
        cyl.out()

    # ====================================================================================================
    # Hole in surface
    # Cylinder boolean with a Mesh
    # Depth 
    # ====================================================================================================

    with GeoNodes("Cylindrical Hole"):

        mesh = Mesh()

        use_top = Boolean(True, "Top")
        use_bot = Boolean(True, "Bottom")
        radius = Float.Distance(0.5, "Radius")
        vertices = Integer(32, "Vertices", 3)
        depth = Float.Distance(0.5, "Depth", tip="Depth from mesh max z")

        node = mesh.points.attribute_statistic(nd.position.z).node
        z0 = node.min
        z1 = node.max
        hmesh = z1 - z0

        with Layout("Hole through the mesh"):
            depth.switch(use_top & use_bot & (depth > hmesh/2), hmesh + 1.0)

        with Layout("Base Cylinders"):
            hcyl = (1.0 + depth)._lc("H Cylinder")
            cyl = G().cylinder(radius=radius, vertices=vertices, depth=hcyl, shape=1.0).link_inputs()

            bevel = Float.Input("Bevel > Size")

            hbevel_cyl = (1.0 + bevel)._lc("H Bevel Cylinder")
            bevel_cyl = G().cylinder(radius=radius + bevel, vertices=vertices, depth=hbevel_cyl, shape=-1.0).link_inputs()
        
        with Layout("Top Hole"):

            with Layout("Main"):
                top_cyl = Mesh(cyl)
                top_cyl.offset = 0.0, 0.0, hcyl/2 + z1 - depth

                diff = Mesh(mesh).difference(top_cyl)

            with Layout("Top Bevel"):
                top_cyl = Mesh(bevel_cyl)
                top_cyl.offset = 0.0, 0.0, hbevel_cyl/2 + z1 - bevel

                diff = diff.difference(top_cyl)

            mesh.switch(use_top, diff)

        with Layout("Bot Hole"):
            with Layout("Main"):
                cyl.offset = 0.0, 0.0, -hcyl/2 + z0 + depth

                diff = Mesh(mesh).difference(cyl)
                use_bot &= (depth < hmesh) | use_top.bnot()

            with Layout("Bot Bevel"):
                bevel_cyl.offset = 0.0, 0.0, -hbevel_cyl/2 + z0 + bevel

                diff = diff.difference(bevel_cyl)

            mesh.switch(use_bot, diff)

        mesh.out()

    # ====================================================================================================
    # Gear
    # ====================================================================================================

    with GeoNodes("Gear"):

        with Panel("Rotation"):
            reverse = Boolean(False, "Reverse")
            tooth = Float(0.0, "Tooth")
            tooth_phase = Float(0.0, "Phase")
            rotation = Float.Angle(0.0, "Rotation")

        radius = Float.Distance(1.0, "Radius")
        count = Integer(16, "Count", 4)
        height = Float.Distance(0.2, "Height")
        width_fac = Float.Factor(0.25, "Teeth width", 0.0, 1.0)
        round_fac0 = Float.Factor(0.1, "Rounded Inner", 0, 1)
        round_fac1 = Float.Factor(0.1, "Rounded Outer", 0, 1)

        h2 = height/2
        teeth_scale = (tau*radius)/count

        with Layout("Initial Circle"):
            total = count*4

            gear = Curve.Circle(radius=radius, resolution=total)
            sel_inner0 = nd.index.modulo(4).equal(0)._lc("Inner 0")
            sel_inner1 = nd.index.modulo(4).equal(1)._lc("Inner 1")
            sel_outer0 = nd.index.modulo(4).equal(2)._lc("Outer 0")
            sel_outer1 = nd.index.modulo(4).equal(3)._lc("Outer 1")

            sel_inner = (sel_inner0 | sel_inner1)._lc("Inner")
            sel_outer = (sel_outer0 | sel_outer1)._lc("Outer")

            gear = stretch(gear, -h2, sel_inner)
            gear = stretch(gear, h2, sel_outer)

        with Layout("Segments"):

            neighbour = Integer.Switch(
                nd.index.modulo(2).equal(0), 
                (nd.index - 1) % total, 
                (nd.index + 1) % total,
                )

            nbh_pos = gear.points.sample_index(nd.position, index=neighbour)
            seg_center = (nd.position + nbh_pos)*0.5
            seg_vector = nd.position - nbh_pos
            #seg_dir = seg_vector.normalize()

        with Layout("Inner segments must have the same size"):
            seg_length = seg_vector.length()._lc("Segment Length")
            inner_length = gear.points.sample_index(seg_length, index=0)
            outer_length = gear.points.sample_index(seg_length, index=2)

            gear[sel_outer].position = seg_center + (nd.position - seg_center).scale(inner_length/outer_length)

        with Layout("Teeth Width"):
            gear.position = seg_center + (nd.position - seg_center).scale(width_fac*4)

        with Layout("Rounding"):

            gear.splines.type = "Bezier"

            seg_dir = seg_vector.normalize()

            gear[sel_inner0].left_handle_offset = seg_dir.scale(round_fac0*teeth_scale)
            gear[sel_inner1].right_handle_offset = seg_dir.scale(round_fac0*teeth_scale)
            gear[sel_outer0].left_handle_offset = seg_dir.scale(round_fac1*teeth_scale)
            gear[sel_outer1].right_handle_offset = seg_dir.scale(round_fac1*teeth_scale)

        with Layout("To Mesh"):

            n = total*12
            circ = Mesh.Circle(vertices=n)
            circ.position = gear.resample(count=n).points.sample_index(nd.position, index=nd.index)

            gear = G().thicken_flat_xy(circ).link_inputs()

            with Panel("Hole"):
                gear = G().cylindrical_hole(
                    gear,
                    top = Boolean(True, "Top"),
                    bottom = Boolean(True, "Bottom"),
                    radius = Float.Factor(1.0, "Radius", 0, 1)*(radius - height),
                    vertices = Integer(32, "Vertices", 3),
                    depth = Float.Distance(0.1, "Depth", tip="Depth from mesh max z"),
                    bevel_size = Float.Input("Bevel > Size"),
                    bevel_lines = Integer.Input("Bevel > Lines"),
                    )
                
        with Layout("Rotation"):
            tooth_angle = tau/count

            angle = tooth*tooth_angle + rotation
            #angle.switch(reverse, -angle)
            gear.transform(rotation=(0, 0, tooth_phase*tooth_angle + Float.Switch(reverse, angle, -angle)))

            actual_tooth = angle/tooth_angle

        with Layout("Finalize"):
            gear.faces.shade_smooth = Boolean(False, "Shade Smooth")
            gear.faces.material = Material(name="Material")

        gear.out()
        actual_tooth.out("Tooth")
        tooth_angle.out("Tooth Angle")
        (tau*radius/count).out("Tooth Length")
        angle.out("Rotation")

    with GeoNodes("Gears Demo"):

        tooth = Float(0.0, "Tooth")

        with Layout("Gear 0"):
            r0 = 1.0
            gear0 = G().gear(
                radius=r0, 
                count=17, 
                tooth=tooth,
                phase=0.75,
                )
            tag = gear0.tooth_angle
            tln = gear0.tooth_length

        with Layout("Gear 1"):
            r1 = 3.0
            gear1 = G().gear(
                radius=r1,
                count=(tau*r1/tln).to_integer(), 
                reverse=True, 
                tooth=tooth,
                )
            rot1 = gear1.rotation
            gear1.offset = r0 + r1, 0, 0

        with Layout("Gear 2"):
            r2 = 0.5
            gear2 = G().gear(
                radius=r2, 
                count=(tau*r2/tln).to_integer(), 
                reverse=True, 
                rotation=rot1,
            )
            tooth2 = gear2.tooth
            gear2.offset = r0 + r1, 0, .25

        with Layout("Gear 3"):
            r3 = 4.0
            gear3 = G().gear(
                phase=0.26,
                radius=r3, 
                count=(tau*r3/tln).to_integer(), 
                reverse=False, 
                tooth=tooth2,
                )
            gear3.offset = r0 + r1 + r2 + r3, 0, .25


        gears = gear0 + (gear1, gear2, gear3)
        gears.out()






