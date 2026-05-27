# WORK IN PROGRESS

import math

from geonodes import *
from .constants import *

def demo():

    # ====================================================================================================
    # Geometrical Primitives
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Bezier Circle
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("G Bezier Circle"):

        sqrt2 = 1.4142135623730951
        c = Curve.Quadrilateral(width=sqrt2, height=sqrt2)
        c.splines.type = 'BEZIER'
        c.transform(rotation=(0, 0, pi/4))

        sel = nd.index == 0
        c[sel].set_left_handle_positions(position=(  0.552125, 1, 0))
        c[sel].set_right_handle_positions(position=(-0.552125, 1, 0))

        sel = nd.index == 2
        c[sel].set_left_handle_positions(position=( -0.552125,-1, 0))
        c[sel].set_right_handle_positions(position=( 0.552125,-1, 0))

        sel = nd.index == 1
        c[sel].set_left_handle_positions(position=( -1,  0.552125, 0))
        c[sel].set_right_handle_positions(position=(-1, -0.552125, 0))

        sel = nd.index == 3
        c[sel].set_left_handle_positions(position=(  1, -0.552125, 0))
        c[sel].set_right_handle_positions(position=( 1,  0.552125, 0))

        Curve(c).out()

    # ----------------------------------------------------------------------------------------------------
    # Profile
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("G Profile", is_group=IS_GROUP):

        with Panel("Profile"):
            sx     = Float.Distance(.2, "Size X", MIN_SIZE)
            sy     = Float.Distance(.2, "Size Y", MIN_SIZE)
            prof   = Integer(0, "Profile")
            radius = Float(0.01, "Radius")

            preview, lod = render_input(with_seed=False)

        sx2, sy2 = sx/2, sy/2
        radius = gnmath.min(gnmath.min(radius, sx2), sy2)

        circle = G("G").bezier_circle()

        # ---------------------------------------------------------------------------
        # Preview
        # ---------------------------------------------------------------------------

        preview_prof = Curve.Quadrilateral(width=sx, height=sy)

        # ---------------------------------------------------------------------------
        # Rectangle
        # ---------------------------------------------------------------------------

        with Curve.IndexSwitch(index=prof) as curve:
            preview_prof.out()

        # ---------------------------------------------------------------------------
        # Cut corners
        # ---------------------------------------------------------------------------

        with curve:
            c = Curve.Circle(resolution=8)
            c.points[nd.index==0].position = (sx2 - radius, -sy2, 0)
            c.points[nd.index==1].position = (sx2, -sy2 + radius, 0)
            c.points[nd.index==2].position = (sx2, sy2 - radius, 0)
            c.points[nd.index==3].position = (sx2 - radius, sy2, 0)
            c.points[nd.index==4].position = (-sx2 + radius, sy2, 0)
            c.points[nd.index==5].position = (-sx2, sy2 - radius, 0)
            c.points[nd.index==6].position = (-sx2, -sy2 + radius, 0)
            c.points[nd.index==7].position = (-sx2 + radius, -sy2, 0)

            c.switch(lod > 2*radius, preview_prof)

            c.out()

        # ---------------------------------------------------------------------------
        # Rounded corners
        # ---------------------------------------------------------------------------

            # TBD
            Curve(c).out()

        # ---------------------------------------------------------------------------
        # Circle
        # ---------------------------------------------------------------------------

        with curve:
            c = Curve(circle).transform(scale=(radius, radius, 1))
            c.out()

        # ---------------------------------------------------------------------------
        # Ellipsis
        # ---------------------------------------------------------------------------

        with curve:
            c = Curve(circle).transform(scale=(sx, sy, 1))
            c.out()

        # ---------------------------------------------------------------------------
        # Curve Size x
        # ---------------------------------------------------------------------------

        with curve:
            c = Curve(circle).transform(scale=(sx, sx, 1))
            c.out()

        # ---------------------------------------------------------------------------
        # Curve Size y
        # ---------------------------------------------------------------------------

        with curve:
            c = Curve(circle).transform(scale=(sy, sy, 1))
            c.out()

        # ---------------------------------------------------------------------------
        # Level of detail
        # ---------------------------------------------------------------------------

        with Layout("Level of detail"):
            p = 2*(sx + sy)
            p.switch(prof == PROF_CIRCLE, tau*radius)

            n = gnmath.max(4, (p/lod).to_integer())
            n.switch(preview, 4)

            curve = Curve(curve).resample(count=n)
            curve.switch(preview, preview_prof)

        curve.out()

    # ====================================================================================================
    # Architectural components
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # A Beam
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("ARCH Beam", is_group=IS_GROUP):

        length = Float.Distance(1.0, "Length")

        prof = G("G").profile().link_panel(("Profile","Render"))

        sx, sy  = Float.Input("Size X"), Float.Input("Size Y")
        preview = Boolean.Input("Preview")
        lod     = Float.Input("LOD")

        n = gnmath.max(2, (length/lod).to_integer())
        n.switch(preview, 2)

        line = Curve.Line(end=(0, 0, length)).resample(count=n)
        beam = line.to_mesh(profile_curve=prof, fill_caps=True)

        beam.out()

    return

    # ----------------------------------------------------------------------------------------------------
    # A Stone
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("ARCH Stone", is_group=IS_GROUP):

        pos     = Vector.Translation((0, 0, 0), "Position")
        height  = Float.Distance(2.5, "Height", MIN_HEIGHT)
        sx      = Float.Distance(.2, "Size X", MIN_SIZE)
        sy      = Float.Distance(.2, "Size Y", MIN_SIZE)
        use_cyl = Boolean(False, "Cylinder")

        preview, lod, seed = render_input()

        with Geometry.Switch(use_cyl) as stone:

            cube = Mesh.Cube(size=(sx, sy, height))
            cube.out("False")

            cyl = Mesh.Cylinder(radius = (sx + sy)/2, depth = height)
            cyl.out("True")

        stone.transform(translation=pos + (0, 0, height/2))
        stone.out()
        seed.out("Seed")


    # ----------------------------------------------------------------------------------------------------
    # Pillar Socle
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("ARCH Pillar Socle", is_group=IS_GROUP):

        pos    = Vector.Translation((0, 0, 0), "Position")
        height = Float.Distance(2.5, "Height", MIN_HEIGHT)
        sx     = Float.Distance(.2, "Size X", MIN_SIZE)
        sy     = Float.Distance(.2, "Size Y", MIN_SIZE)
        socle  = Integer(0, "Socle")

        preview, lod, seed = render_input()

        scale_x = G("Random").normal_value(1.3, .1, seed=seed).single
        seed = scale_x.seed

        scale_y = G("Random").normal_value(1.3, .1, seed=seed).single
        seed = scale_y.seed

        hofs = G("Random").normal_value(height, .05, seed=seed).single
        seed = hofs.seed

        sx *= scale_x
        sy *= scale_y
        height += hofs

        with Geometry.IndexSwitch(None, index=socle) as geo:

            gsocle = G("ARCH").beam(position=pos, end=pos + (0, 0, height), size_x=sx, size_y=sy, seed=cseed(seed)).link_panel("Render")
            gsocle.out()

        with geo:
            gsocle = G("ARCH").stone(position=pos, height=height, size_x=sx, size_y=sy, seed=cseed(seed)).link_panel("Render")
            gsocle.out()

        with geo:
            gsocle = G("ARCH").stone(position=pos, height=height, size_x=sx, size_y=sy, cylinder=True, seed=cseed(seed)).link_panel("Render")
            gsocle.out()

        height.switch(socle==0)
        pos += (0, 0, height)

        geo.out()
        pos.out('Position')
        height.out("Height")
        seed.out("Seed")

    # ----------------------------------------------------------------------------------------------------
    # A Pillar
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("ARCH Wood Pillar", is_group=IS_GROUP):

        pos          = Vector.Translation((0, 0, 0), "Position")
        height       = Float.Distance(2.5, "Height", MIN_HEIGHT)
        sx           = Float.Distance(.2, "Size X", MIN_SIZE)
        sy           = Float.Distance(.2, "Size Y", MIN_SIZE)
        socle        = Integer(0, "Socle")
        socle_height = Float.Distance(.2, "Socle Height", MIN_SIZE)

        preview, lod, seed = render_input()

        gsocle = G("ARCH").pillar_socle(
            position = pos,
            height = socle_height,
            size_x = sx,
            size_y = sy,
            socle = socle,
            seed = seed,
        )
        pos = gsocle.position_
        socle_height = gsocle.height
        seed = gsocle.seed

        height -= socle_height

        pillar = G("ARCH").beam(
            position = pos,
            end      = pos + (0, 0, height),
            size_x   = sx,
            size_y   = sy,
            seed     = seed,
        )
        seed = pillar.seed

        pillar += gsocle

        pillar.out()
        seed.out()

    # ----------------------------------------------------------------------------------------------------
    # A Stone Pillar
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("ARCH Stone Pillar", is_group=IS_GROUP):

        pos          = Vector.Translation((0, 0, 0), "Position")
        height       = Float.Distance(2.5, "Height", MIN_HEIGHT)
        sx           = Float.Distance(.2, "Size X", MIN_SIZE)
        sy           = Float.Distance(.2, "Size Y", MIN_SIZE)
        use_cyl      = Boolean(False, "Cylinder")
        socle        = Integer(0, "Socle")
        socle_height = Float.Distance(.2, "Socle Height", MIN_SIZE)

        preview, lod, seed = render_input()

        row = Cloud(G("Random").row(length=height, part=0.45, scale=0.1, seed=seed))
        seed = row.seed

        for rep in repeat(row.points.count, cloud=row, pillar=None, pos=pos):
            l = rep.cloud.points.sample_index(Float("Length"), index=rep.iteration)
            stone = G("ARCH").stone(
                position = rep.pos,
                height = l,
                size_x = sx,
                size_y = sy,
                cylinder = use_cyl,
                seed = seed + rep.iteration,
            ).link_panel("Render")
            rep.pillar += stone

            rep.pos += (0, 0, l)

        pillar = rep.pillar

        pillar.out()
        (seed + 1).out()        









