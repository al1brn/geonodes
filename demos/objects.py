from geonodes import *
from geonodes.demos import curveutil, shaders


def demo(rebuild=False):

    curveutil.demo()

    Tree._init_package('Objects')
    shaders.colored_shaders()
    shaders.chrome_shader()
    shaders.glass_shader()
    shaders.wood_handle_shader()

    # ====================================================================================================
    # Magnifying Glass
    # ====================================================================================================

    with GeoNodes("Magnifying Glass", rebuild=rebuild):

        BVL = 0.02
        THICK = 0.2
        HAND_LEN = 1.8
        
        size = Float(1, "Size")
        resolution  = Integer(64, "Resolution", 6, 512)
        z_rot = Float.Angle(0, "Rotation")
        zoom = Float(1.0, "Zoom")
        lens_transp = Float.Factor(0.0, "Lens Transparency", 0, 1)
        lens_ior = Float(1.45, "Lens IOR", 0.1, 2.0)
        del_radius = Float.Factor(1, "Deletion Radius", 0, 2)
        
        metal_mat = Material("Chrome", name="Metal")
        lens_mat = Material("Glass", name="Lens")
        hand_mat = Material("Wood Handle", name="Handle")

        with Panel("Image Content"):
            use_cont = Boolean(False, "Content")
            cont_mat = Material(None, name="Content")
            uv_scale = Vector(1, "UV Scale", dimensions=2)
            uv_ofs = Vector(None, "UV Offset", dimensions=2)

        with Panel("Object Content"):
            use_obj = Boolean(False, "Zoom on Object")
            obj_cont = Object(None, "Object")
            obj_ofs = Vector(0, "Offset")

        with Layout("Lens Circle"):
            mag = Curve.Circle(radius=1, resolution=resolution)
            prof = Curve.Quadrilateral(width=THICK/2, height=THICK)
            mag = mag.to_mesh(profile_curve=prof)
            
            mag[nd.position.z.abs() > 0.04].bevel('Edges', BVL, BVL, BVL, BVL, segments=3)
            mag.faces.shade_smooth = True
            mag.faces.material = metal_mat
            
        with Layout("Lens"):
            lens = Mesh.UVSphere(radius=1.0, segments=resolution, rings=resolution//2)
            lens.transform(scale=(1, 1, THICK/2))
            lens.faces.shade_smooth=True
            lens.faces.material=lens_mat
            lens.faces.set("IOR", lens_ior)
            lens.faces.set("Transparency", lens_transp)
            
            mag += lens
            
        with Layout("Handle"):
            handle = Curve.Line((-HAND_LEN/2, 0, 0), (HAND_LEN/2, 0, 0)).resample(count=resolution)
            f = (nd.spline_parameter().factor - 0.5).abs()
            f = f.map_range(0, 0.5, 0, 1, interpolation_type='Smooth Step')
            r = (THICK*0.4) + (THICK*0.2)*(1 - f)**0.6
            handle = handle.curve_to_tube(scale=r, profile_resolution=resolution)
            handle.faces.shade_smooth = True
            handle.faces.material = hand_mat
            handle.faces[nd.position.x.abs() > 0.7].material = metal_mat
            handle[nd.position.x == -HAND_LEN/2].bevel('Edges', BVL, BVL, BVL, BVL, segments=3)
            handle.offset =(-1 - HAND_LEN/2, 0, 0)
            
            mag += handle
            
        with Layout("Image Content"):
            content = Mesh.Circle(vertices=resolution, fill_type='N-Gon')
            content.faces.material = cont_mat

            # Scale with uv centered on (0, 0)
            uv = nd.position.scale(0.5)

            # Aspect scale
            uv *= uv_scale

            # Zoom
            uv = uv.scale(1/zoom)

            # Rotation
            uv = Rotation((0, 0, -z_rot)) @ uv

            # Offset
            uv += -uv_ofs + (0.5, 0.5, 0.5)

            # Done
            content.corners.store_uv('UVMap', uv)
            mag += content.switch_false(use_cont)

        with Layout("Size and rotation"):
            mag.transform(scale=size, rotation=(0, 0, z_rot))

        with Layout("Object Content"):
            geo = obj_cont.info(transform_space='Relative').geometry

            geo.transform(scale=(zoom, zoom, 1.), translation=-obj_ofs)

            d = (nd.position*(1, 1, 0)).length()
            geo = Mesh(geo).points[d>size*del_radius].delete()

            mag += geo.switch_false(use_obj)

        with Bundle() as bundle:
            size.out("Radius")

        mag.set_bundle(bundle)
            
        mag.out()

    with GeoNodes("Magnified", rebuild=rebuild):

        magnified_obj = Object(name="Magnified")
        magnifier_obj = Object(name="Magnifier")
        use_mag = Boolean(False, "Magnified")

        with Layout("Magnified"):
            node = magnified_obj.info().node
            loc0 = node.location
            geo0 = node.geometry
            mesh0 = Mesh(geo0)

        with Layout("Magnifier"):
            node = magnifier_obj.info().node
            loc1 = node.location
            geo1 = node.geometry

        with Layout("Delete Magnified part"):
            radius = geo1.get_bundle().get_item('Radius', socket_type='FLOAT')
            p = nd.position - loc0 - loc1
            d = (p*(1, 1, 0)).length()
            mesh0.points[d < radius].delete()

        geo0.switch(use_mag, mesh0).out()



    # ====================================================================================================
    # Here Symbol
    # ====================================================================================================

    with GeoNodes("Here", rebuild=rebuild):
        
        BASE = 1.2
        TIP = 0.4*BASE
        THICK = 0.2
        #IN_RADIUS = 0.65
        IN_DEPTH = 0.05
        BEV = 0.02
        
        
        show            = Float.Factor(1, "Show", 0, 1)
        count           = Integer(32, "Resolution", 5, 128)
        radius          = Float(1.0, "Radius")
        in_radius_fac   = Float.Factor(0.65, "In Radius", 0, 1) 
        bump_fac        = Float.Factor(0.55, "Bump", 0, 1)
        depth_fac       = Float.Factor(0.0, "Depth", 0, 1)
        color           = Color("Red", "Color") 
        point_color     = Color("White", "Point Color") 
        mat             = Material("Colored Shiny", "Material")
        
        
        with Layout("Base Shape"):
            circle = G().bezier_circle()
            
            sel = nd.index == 0
            circle[sel].offset = (BASE, 0, 0)
            circle[sel].left_handle_position = nd.position + (-TIP, 0,0)
            circle[sel].right_handle_position = nd.position + (-TIP, 0, 0)
            
            circle.resample(count=count)
            
        with Layout("Topology is a Cylinder"):
            
            in_radius = in_radius_fac.map_range(0, 1, 0.01, 0.95)        
            cyl = Mesh.Cylinder(radius=in_radius, depth=THICK*5, vertices=count, side_segments=5)
            
        with Layout("Base Shape Position"):
            pos = circle.points.sample_index(nd.position, index=nd.index % count)
            x, y, _ = pos.xyz
        
            in_sel = (nd.index >= 2*count) & (nd.index < 4*count)
            cyl[in_sel].position = (x, y, nd.position.z)
            
        with Layout("Adjuste Rings height"):
            sel_last = (nd.index < count) | (nd.index >= 5*count)
            sel_ulti = ((nd.index < 2*count) | (nd.index >= 4*count)) & sel_last.bnot()
            bump = bump_fac.map_range(0, 1, THICK/2, 2*THICK)
            depth = depth_fac.map_range(0, 1, bump - 0.52*THICK, bump + 0.52*THICK)
            
            z = nd.position.z.abs()
            
            cyl[sel_ulti].position = nd.position * (1, 1, bump/z)
            cyl[sel_last].position = nd.position * (1, 1, depth/z)
            
            cyl[sel_last].points.set('Last', 1.0)
                
            
        with Layout("Finalize"):        
            cyl[nd.position.z==0.1].bevel(
                start_left_offset = BEV,
                start_right_offset = BEV,
                end_left_offset = BEV,
                end_right_offset = BEV,
                )
                
            cyl.faces.shade_smooth=False
            cyl.faces.material=mat
            cyl.faces.set('Transparency', 1 - show)
            cyl.faces.set('Color', color)
            cyl.faces[Float('Last') > 0].set('Color', point_color)
            cyl.remove_named_attribute(pattern_mode='Exact', name='Last')
        
            cyl.transform(translation=(0, 0, (1 + BASE)*radius), rotation=(0, pi/2, -pi/2), scale=radius)
            
        cyl.switch(show==0).out()

    Tree._display_counter('Objects built')
