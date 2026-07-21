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

        with Layout("Copy to Cyldinder"):

            n = mesh.points.count
            cyl = Mesh.Cylinder(vertices=n, radius=1.0, depth=thickness, side_segments=1)
            circ_index = nd.index // 2

            pos = mesh.points.sample_index(nd.position, index=nd.index % n)
            x, y, _ = pos.xyz
            z = nd.position.z

            cyl.points.position = (x, y, z)

        #cyl.bevel().link_inputs(from_panel="Bevel")

        cyl.out()

    # ====================================================================================================
    # Hole in surface
    # Cylinder boolean with a Mesh
    # Depth 
    # ====================================================================================================

    with GeoNodes("Dig Mesh"):

        mesh = Mesh()
        keep = Mesh(mesh)

        shape_index = Integer.MenuSwitch({
                "None" : 0,
                "Circle" : 1,
                "Pies" : 2,
                }, menu=Input("Shape"))
        use_top = Boolean(True, "Top")
        use_bot = Boolean(True, "Bottom")

        radius = Float.Distance(0.5, "Radius")
        vertices = Integer(32, "Vertices", 3)
        depth = Float.Distance(0.5, "Depth", tip="Depth from mesh max z")
        ncuts = Integer(3, "Cuts", 0, 10)
        inner_radius = Float.Distance(0.1, "Inner Radius", 0.)

        with Panel("Bevel"):
            use_bevel = Boolean(True, "Bevel")
            bev_offset = Float(0.01, "Offset")
            bev_segments = Integer(1, "Segments", 1, 10)

        with Layout("Dimensions"):
            node = mesh.points.attribute_statistic(nd.position.z).node
            z0 = node.min
            z1 = node.max
            hmesh = z1 - z0

            depth.switch(use_top & use_bot & (depth > hmesh/2), hmesh + 1.0)
            hcyl = 1. + depth

        with Layout("Mark Initial vertices"):
            init_sel = mesh.points.get("Initial", 'Boolean')
            init_sel.value = True

        with Mesh.IndexSwitch(index=shape_index - 1) as digger:

            cyl = Mesh.Cylinder(radius=radius, vertices=vertices, depth = 1. + depth)
            cyl.out()

            cube = Mesh.Cube(size = (radius/(ncuts + 5), 2*radius + 1, 2. + depth))
            ag = pi/ncuts
            for rep in repeat(ncuts, cyl=cyl):

                cut = Mesh(cube).transform(rotation=(0, 0, ag*rep.iteration))

                rep.cyl = rep.cyl.difference(cut)

            rep.cyl.out()

        with Layout("Remove inner cylinder"):
            inner_radius = gnmath.min(inner_radius, 0.9*radius)
            inner_cyl = Mesh.Cylinder(radius=inner_radius, vertices=vertices, depth = 2. + depth)

            digger = Mesh(digger).difference(inner_cyl)

        with Layout("Top Hole"):

            top_dig = Mesh(digger)
            top_dig.offset = 0.0, 0.0, hcyl/2 + z1 - depth

            diff = Mesh(mesh).difference(top_dig)

            mesh.switch(use_top, diff)

        with Layout("Bot Hole"):
            digger.offset = 0.0, 0.0, -hcyl/2 + z0 + depth

            diff = Mesh(mesh).difference(digger)
            use_bot &= (depth < hmesh) | use_top.bnot()

            mesh.switch(use_bot, diff)

        with Layout("Bevel"):
            beveled = Mesh(mesh)[init_sel.value.bnot()].bevel(
                affect_kind = 'Edges',
                start_left_offset = bev_offset,
                start_right_offset = bev_offset,
                end_left_offset = bev_offset,
                end_right_offset = bev_offset,
                miter = False,
                spread = 0.01,
            ).link_inputs(from_panel="Bevel")
            mesh.switch(use_bevel, beveled)

        with Layout("Internal faces"):
            z = nd.position.z
            margin = depth*0.01
            dig_faces = z.equal(z1 - depth, epsilon=margin)
            dig_faces |= z.equal(z0 + depth, epsilon=margin)

            dig_faces &= nd.normal.z.abs() > 0.9

            mesh.faces.set('Dig', dig_faces)

        mesh.switch(shape_index.equal(0), keep)

        mesh.out()

    # ====================================================================================================
    # Gear
    # ====================================================================================================

    GEAR_SIGNATURE = {
        "Position"      : 'Vector',
        "Radius"        : 'Float',
        "Reverse"       : 'Boolean',
        "Tooth"         : 'Float',
        "Rotation"      : 'Float',
        "Height"        : 'Float',
        "Tooth width"   : 'Float',
        "Rounded Inner" : 'Float',
        "Rounded Outer" : 'Float',
        "Tooth Arc"     : 'Float',
        "Thickness"     : 'Float',
    }

    with GeoNodes("Gear"):

        simplified = Boolean(False, "Simplified")
        with Layout("From Gear"):
            use_other = Boolean(False, "Couple with Gear")
            other_obj = Object(None, "Gear Object")
            share_axis = Boolean(False, "Share Axis")
            other_angle = Float.Angle(0, name="Direction")

        with Panel("Rotation"):
            reverse = Boolean(False, "Reverse")
            tooth = Float(0.0, "Tooth")
            tooth_phase = Float(0.0, "Phase")
            rotation = Float.Angle(0.0, "Rotation")

        with Panel("Shape"):
            radius = Float.Distance(1.0, "Radius")
            #aaa
            count = Integer(16, "Count", 4)
            height = Float.Distance(0.2, "Height")
            width_fac = Float.Factor(0.25, "Tooth Width", 0.0, 1.0)
            round_fac0 = Float.Factor(0.1, "Rounded Inner", 0, 1)
            round_fac1 = Float.Factor(0.1, "Rounded Outer", 0, 1)

        with Panel("Object"):
            gear_pos = Vector(0, "Position")
            thickness = Float(0.3, "Thickness", 0.3)
            mat = Material(None, "Material")
            use_smoooth = Boolean(False, "Shade Smooth")

        with Panel("Bevel"):
            use_bevel = Boolean(True, "Bevel")
            bev_offset = Float(0.01, "Offset")
            bev_segments = Integer(1, "Segments", 1, 10)

        with Layout("Other Gear"):
            other_bundle = other_obj.info().geometry.get_bundle().separate(signature=GEAR_SIGNATURE)

            is_driven = use_other & share_axis.bnot()
            is_glued = use_other & share_axis

            other_pos = other_bundle.position
            other_radius = other_bundle.radius

            dist = other_radius + radius
            delta = (dist*other_angle.cos(), dist*other_angle.sin(), 0)

            gear_pos.switch(is_driven, other_pos + delta)
            gear_pos.switch(is_glued, other_pos + (0, 0, other_bundle.thickness + gear_pos.z))

            reverse.switch(is_driven, other_bundle.reverse.bnot())
            reverse.switch(is_glued, other_bundle.reverse)

            tooth.switch(is_glued, 0.)
            rotation.switch(is_glued, other_bundle.rotation)

            tooth.switch(is_driven, other_bundle.tooth)
            rotation.switch(is_driven, 0.0)

            height.switch(is_driven, other_bundle.height)
            width_fac.switch(is_driven, other_bundle.tooth_width)
            round_fac0.switch(is_driven, other_bundle.rounded_inner)
            round_fac1.switch(is_driven, other_bundle.rounded_outer)
            other_tooth_arc = other_bundle.tooth_arc

            n = ((radius*tau)/other_tooth_arc).to_integer()
            count.switch(is_driven, n)

            thickness.switch(is_driven, other_bundle.thickness)

        with Layout("Dims"):
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

        with Layout("Inner segments must have the same size"):
            seg_length = seg_vector.length()._lc("Segment Length")
            inner_length = gear.points.sample_index(seg_length, index=0)
            outer_length = gear.points.sample_index(seg_length, index=2)

            gear[sel_outer].position = seg_center + (nd.position - seg_center).scale(inner_length/outer_length)

        with Layout("Tooth Width"):
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

            simplified &= nd.is_viewport
            circ.switch(simplified, Mesh.Circle(radius=radius))

            gear = G().thicken_flat_xy(circ, thickness=thickness).link_inputs()

        with Layout("Bevel"):
            beveled = Mesh(gear)
            for i in range(2):
                sel = nd.position.z > thickness/4 if i == 0 else nd.position.z < -thickness/4
                beveled[sel].bevel(
                    affect_kind = 'Edges',
                    start_left_offset = bev_offset,
                    start_right_offset = bev_offset,
                    end_left_offset = bev_offset,
                    end_right_offset = bev_offset,
                    miter = False,
                    spread = 0.01,
                ).link_inputs(from_panel="Bevel")

            gear.switch(use_bevel & simplified.bnot(), beveled)

        with Layout("Dig"):
            digged = G().dig_mesh(gear).link_inputs(from_panel="Object > Shape")
            gear.switch_false(simplified, digged)

        with Layout("Rotation"):
            tooth_angle = tau/count

            angle = tooth*tooth_angle + rotation
            act_rotation = tooth_phase*tooth_angle + Float.Switch(reverse, angle, -angle)
            gear.transform(translation=gear_pos, rotation=(0, 0, act_rotation))

            actual_tooth = angle/tooth_angle

        with Layout("Finalize"):
            gear.faces.shade_smooth = use_smoooth
            gear.faces.material = mat

        with Bundle() as bdl:
            gear_pos.out("Position")
            radius.out("Radius")
            reverse.out("Reverse")
            actual_tooth.out("Tooth")
            angle.out("Rotation")

            height.out("Height")
            width_fac.out("Tooth width")
            round_fac0.out("Rounded Inner")
            round_fac1.out("Rounded Outer")

            (radius*tau/count).out("Tooth Arc")
            thickness.out("Thickness")

        gear.set_bundle(bdl)

        gear.out()



    return

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






