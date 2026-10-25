import bpy

from geonodes import *
from geonodes.demos import shaders

def demo(rebuild=False):

    shaders.colored_shaders()

    # ----------------------------------------------------------------------------------------------------
    # Set a bezier point with relative left and right offsets
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes(".Bezier Point", is_group=True, rebuild=rebuild):
        
        c = Curve()
        index = Integer(0, "Index")
        pos = Vector(name="Position")
        left = Vector(name="Left")
        right = Vector(name="Right")
        
        
        sel = nd.index == index
        c[sel].position = pos
        c[sel].left_handle_position = pos + left
        c[sel].right_handle_position = pos + right
        
        c.out()

    # ----------------------------------------------------------------------------------------------------
    # Symmetric copy of position and handles
    # ----------------------------------------------------------------------------------------------------
        
    with GeoNodes(".Bezier Point Symmetry", is_group=True, rebuild=rebuild):
        
        c = Curve()
        index = Integer(0, "Index")
        sym = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2}, menu=Input("Symmetry"))
        from_index = Integer(0, "From Index")
        
        hpos = Curve.handle_positions(relative=True).node
        
        pos0 = c.points.sample_index(nd.position, index=from_index)
        left0 = c.points.sample_index(hpos.left, index=from_index)
        right0 = c.points.sample_index(hpos.right, index=from_index)
        
        pos1 = Vector.IndexSwitch(
            (pos0 * (-1,  1,  1)),
            (pos0 * ( 1, -1,  1)),
            (pos0 * ( 1,  1, -1)),
            index=sym)
            
        left1 = Vector.IndexSwitch(
            (left0 * (-1,  1,  1)),
            (left0 * ( 1, -1,  1)),
            (left0 * ( 1,  1, -1)),
            index=sym)
        
        right1 = Vector.IndexSwitch(
            (right0* (-1,  1,  1)),
            (right0 * ( 1, -1,  1)),
            (right0 * ( 1,  1, -1)),
            index=sym)
            
        G()._bezier_point(c, index, pos1, right1, left1).out()

    # ====================================================================================================
    # Bezier Curly Bracket
    # ====================================================================================================

    with GeoNodes("Curly Bracket", rebuild=rebuild):
        
        show = Float.Factor(1.0, "Show", 0, 1)
        height = Float(1.0, "Height")
        width  = Float(1.0, "Width")
        use_fill = Boolean(True, "Fill")
        mat = Material("Colored Mat", "Material")
        col = Color("White", "Color")
        
        
        with Layout("Base"):
            bracket = Curve.Circle().resample(count=11)
            bracket.splines.type = "Bezier"
            bracket.handle_type = 'Vector'
            
        with Layout("Dims"):
            h = (height/2)._lc("h")
            th_top = (h/12)._lc("h top")
            th_vrt = (1.15*th_top)._lc("h top")
            th_mid = (1.1*th_top)._lc("h top")
            x_vrt = (0.5*width)._lc("x vrt")
            
        with Layout("Build"):
            bracket = G()._bezier_point(bracket, 0, (x_vrt - th_vrt/2, h/2, 0), (0, -h/3, 0), (0, h/3, 0))
            bracket = G()._bezier_point(bracket, 1, (0, h - th_top, 0), (width/3, 0, 0), (0, th_top/3, 0))
            bracket = G()._bezier_point(bracket, 2, (0, h, 0), (0, -th_top/3, 0), (width/2, 0, 0))
            bracket = G()._bezier_point(bracket, 3, (x_vrt + th_vrt/2, h/2, 0), (0, h/3, 0), (0, -h/3, 0))
            bracket = G()._bezier_point(bracket, 4, (width, th_mid/2, 0), (-width/3, 0, 0), (0, -th_mid/3, 0))

            bracket = G()._bezier_point(bracket, 10, (width -th_top,  0, 0), (-width/3, 0, 0), (-width/3, 0, 0))
            
        with Layout("Y Symmetry"):
            for i in range(5):
                bracket = G()._bezier_point_symmetry(bracket, index=9-i, symmetry='Y', from_index=i)
                
        with Layout("Mesh"):
            mesh = Curve(bracket).fill()
            mesh.faces.material = mat
            mesh.faces.set('Color', col)
            mesh.faces.set('Transparency', 1 - show)
            
            bracket.switch(use_fill, mesh).switch(show == 0).out()

    # ====================================================================================================
    # Bezier Circle
    # ====================================================================================================

    with GeoNodes("Bezier Circle", rebuild=rebuild):
        
        OFS = 0.552125
        
        radius = Float(1.0, "Radius")
        
        circle = Curve.Circle().resample(count=4)
        circle.splines.type = 'Bezier'
        circle.set_handle_type('Vector')
        
        circle.left_handle_position  = nd.position + Rotation((0, 0,  -pi/2 + nd.index*(pi/2))) @ (OFS, 0, 0)
        circle.right_handle_position = nd.position + Rotation((0, 0,  pi/2 + nd.index*(pi/2))) @ (OFS, 0, 0)
        
        circle.transform(scale=radius)
        
        circle.out()

    # ====================================================================================================
    # Rounded Rectangle
    # ====================================================================================================

    with GeoNodes("Rounded Rectangle", rebuild=rebuild):
        
        sx = Float(1, "Size X")/2
        sy = Float(.5, "Size Y")/2
        rd_fac = Float.Factor(0.1, "Rounded", 0, 1)
        use_radius = Boolean(False, "Use Radius")
        radius = Float(0.01, "Radius", 0)
        resolution = Integer(12, "Resolution", 2, 128)
        fill_mesh = Boolean(False, "Fill Mesh")
        
        rd_size = gnmath.min(sx, sy)    
        rd = Float.Switch(use_radius, rd_size*rd_fac, radius.max(0).min(rd_size))
        
        line = Curve.Line().resample(count=8)
        
        line.splines.type = "BEZIER"
        
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
        
        tg=rd*0.552125

        # The other handle lies on the point to keep the straight sections straight.
        zero = (0, 0, 0)
        handles = [
            ((-tg, 0, 0), zero),
            (zero, (tg, 0, 0)),
            ((0, -tg, 0), zero),
            (zero, (0, tg, 0)),
            ((tg, 0, 0), zero),
            (zero, (-tg, 0, 0)),
            ((0, tg, 0), zero),
            (zero, (0, -tg, 0)),
        ]
        for i, (position, (left, right)) in enumerate(zip(corners, handles)):
            line = G()._bezier_point(
                line, index=i, position=position, left=left, right=right,
            )
        
        line.is_cyclic = True

        # Sample each rounded corner from the same Bezier control points.
        # Rounded Box needs exactly 4 * Resolution vertices, in stable order.
        count = resolution.max(2)
        mesh = Mesh.Circle(vertices=4*count, fill_type='N-Gon')
        corner = nd.index // count
        t = (nd.index % count) / (count - 1)
        starts = [corners[i] for i in (1, 3, 5, 7)]
        ends = [corners[i] for i in (2, 4, 6, 0)]
        control1 = [corners[i] + handles[i][1] for i in (1, 3, 5, 7)]
        control2 = [corners[i] + handles[i][0] for i in (2, 4, 6, 0)]
        p0 = Vector.IndexSwitch(*starts, index=corner)
        p1 = Vector.IndexSwitch(*control1, index=corner)
        p2 = Vector.IndexSwitch(*control2, index=corner)
        p3 = Vector.IndexSwitch(*ends, index=corner)
        mesh.position = (
            p0 * (1 - t)**3 + p1 * (3*(1 - t)**2*t)
            + p2 * (3*(1 - t)*t*t) + p3 * t**3
        )
        mesh = mesh.faces[fill_mesh.bnot()].delete_only_face()

        with Geometry.MenuSwitch(menu=Input("Geometry"), default_menu='Curve') as geometry:
            line.out("Curve")
            mesh.out("Mesh")
        geometry.out()
